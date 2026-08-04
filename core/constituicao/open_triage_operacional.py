#!/usr/bin/env python3
"""
OpenTriageOperacional -- Triagem: Sintoma vs Diagnostico
==========================================================
"Chega paciente com dor no peito. Nao espera raio X pra dar aspirina.
 Trata o sintoma AGORA, diagnostica DEPOIS. Mas com regra."

PRINCIPIO OPERACIONAL:
  Sintoma que ameaca VIDA    -> trata agora, diagnostica depois.
  Sintoma que afeta BOLSO    -> diagnostica primeiro, trata depois.
  Sintoma que afeta VOTO     -> nunca sem diagnostico (virou palanque).

O PERIGO:
  Tratar sintoma sem diagnostico vira tiro no escuro se voce confunde
  alivio com cura. Aspirina pra febre de apendice alivia a febre.
  O apendice estoura. O paciente morre "sem febre".

A SOLUCAO:
  Toda acao da Republica passa por triagem:
    1. Classifica sintoma (vida, bolso, voto, estrutura)
    2. Define se pode agir sem diagnostico
    3. Define prazo pra obter diagnostico
    4. Marca se acao e ALIVIO (sintoma) ou CURA (causa)
    5. Se ALIVIO: obrigatoriamente linka com diagnostico futuro

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional
from enum import Enum
from dataclasses import dataclass, field


# ============================================================================
# 1. ENUMS
# ============================================================================

class CategoriaSintoma(Enum):
    """Categoria do sintoma define prioridade de acao."""
    VIDA = ("vida", "Ameaca vida: trata AGORA, diagnostica depois")
    BOLSO = ("bolso", "Afeita bolso: diagnostica primeiro, trata depois")
    VOTO = ("voto", "Afeta voto: NUNCA sem diagnostico (virou palanque)")
    ESTRUTURA = ("estrutura", "Estrutural: diagnostica + trata simultaneo")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoAcao(Enum):
    """Tipo de acao no sintoma."""
    ALIVIO = ("alivio", "Alivio: trata sintoma, causa permanece")
    CURA = ("cura", "Cura: trata causa raiz, sintoma nao volta")
    PALIATIVO = ("paliativo", "Paliativo: alivio continuo, causa intratavel agora")
    DIAGNOSTICO = ("diagnostico", "Diagnostico: so investiga, nao age ainda")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class StatusTriagem(Enum):
    """Status da triagem de um sintoma."""
    AGIR_AGORA = ("agir", "AGIR AGORA: vida em risco, acao imediata sem diagnostico")
    AGIR_COM_RESSALVA = ("ressalva", "AGIR COM RESSALVA: acao temporaria enquanto diagnostica")
    DIAGNOSTICAR_PRIMEIRO = ("diagnosticar", "DIAGNOSTICAR PRIMEIRO: sem dado, sem acao")
    BLOQUEAR = ("bloquear", "BLOQUEAR: sem diagnostico vira palanque (P9)")
    MONITORAR = ("monitorar", "MONITORAR: nem alivio nem cura, so observar")

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
class Sintoma:
    """Um sintoma do Brasil que precisa triagem."""
    id: str
    nome: str
    categoria: CategoriaSintoma
    descricao: str
    tem_diagnostico: bool            # ja temos dado (FATO)?
    acao_alivio: str = ""            # o que fazer agora (sintoma)
    acao_cura: str = ""              # o que fazer depois (causa)
    prazo_diagnostico_dias: int = 0  # quanto tempo pra obter diagnostico
    risco_alivio_sem_cura: str = ""  # perigo de tratar sintoma so


@dataclass
class DecisaoTriagem:
    """Resultado da triagem de um sintoma."""
    sintoma: Sintoma
    status: StatusTriagem
    acao_recomendada: TipoAcao
    justificativa: str
    prazo_diagnostico_dias: int
    alerta: str = ""


# ============================================================================
# 3. CATALOGO DE SINTOMAS REAIS DO BRASIL
# ============================================================================

def _init_sintomas() -> List[Sintoma]:
    return [
        # ====================================================================
        # VIDA -- AGIR AGORA
        # ====================================================================
        Sintoma(
            "fome_infantil", "Crianca com fome",
            CategoriaSintoma.VIDA,
            "33 milhoes de brasileiros passam fome. Crianca nao come.",
            tem_diagnostico=False,
            acao_alivio="Distribuicao imediata de comida (merenda, cesta, restaurante popular)",
            acao_cura="Reforma agraria + soberania alimentar + renda minima",
            prazo_diagnostico_dias=30,
            risco_alivio_sem_cura="Comida hoje nao resolve causa. Sem cura, dependencia eterna.",
        ),
        Sintoma(
            "sem_agua_escola", "Escola sem agua",
            CategoriaSintoma.VIDA,
            "Escola sem agua potavel. Crianca nao bebe, nao lava mao.",
            tem_diagnostico=False,
            acao_alivio="Caminha pipa + filtro + poco artesiano",
            acao_cura="Saneamento universal + rede publica",
            prazo_diagnostico_dias=15,
            risco_alivio_sem_cura="Caminhao pipa vora orcamento se rede nunca chega.",
        ),
        Sintoma(
            "violencia_ativa", "Tiroteio/violencia em andamento",
            CategoriaSintoma.VIDA,
            "Tiroteio em favela. Criancas na escola. Vidas em risco AGORA.",
            tem_diagnostico=False,
            acao_alivio="Alerta comunidade + protege escola + acolhe vitimas",
            acao_cura="Desmilitarizacao + investimento social + estado de direito",
            prazo_diagnostico_dias=1,
            risco_alivio_sem_cura="So proteger nao para o tiro de amanha.",
        ),
        Sintoma(
            "surto_doenca", "Surto de doenca (dengue, malaria)",
            CategoriaSintoma.VIDA,
            "Surto ativo. Gente morrendo.",
            tem_diagnostico=False,
            acao_alivio="Vacina/repelente/ tratamento imediato",
            acao_cura="Saneamento + vigilancia + casa decente",
            prazo_diagnostico_dias=7,
            risco_alivio_sem_cura="Vacina hoje. Dengue volta se agua parada continua.",
        ),
        Sintoma(
            "desnutricao_indigena", "Desnutricao indigena",
            CategoriaSintoma.VIDA,
            "Crianca indigena desnutrida. Morrendo.",
            tem_diagnostico=False,
            acao_alivio="Envio de equipe medica + comida + agua",
            acao_cura="Demarcacao de terra + saude indigena + soberania",
            prazo_diagnostico_dias=7,
            risco_alivio_sem_cura="Comida enviada nao resolve terra invadida.",
        ),

        # ====================================================================
        # BOLSO -- DIAGNOSTICAR PRIMEIRO
        # ====================================================================
        Sintoma(
            "inflacao_alta", "Inflacao alta",
            CategoriaSintoma.BOLSO,
            "Preco de arroz subiu. Bolso do trabalhador aperta.",
            tem_diagnostico=False,
            acao_alivio="Subsidio temporario de cesta basica",
            acao_cura="Competitividade + reforma tributaria + quebra de monopolio",
            prazo_diagnostico_dias=15,
            risco_alivio_sem_cura="Subsidio sem diagnosticar causa = inflacao galopante depois.",
        ),
        Sintoma(
            "desemprego_massa", "Desemprego em massa",
            CategoriaSintoma.BOLSO,
            "Desemprego alto. Gente sem renda.",
            tem_diagnostico=False,
            acao_alivio="Programa de renda temporario",
            acao_cura="Politica industrial + educacao + credito sem juros",
            prazo_diagnostico_dias=30,
            risco_alivio_sem_cura="Renda temporaria sem emprego = dependencia.",
        ),
        Sintoma(
            "energia_cara", "Conta de luz cara",
            CategoriaSintoma.BOLSO,
            "Conta de luz subiu 40%. Gente nao paga.",
            tem_diagnostico=False,
            acao_alivio="Tarifa social / subsidio",
            acao_cura="Energia solar comunitaria + rede publica + microgrid",
            prazo_diagnostico_dias=30,
            risco_alivio_sem_cura="Subsidio semResolver causa = broke estado.",
        ),

        # ====================================================================
        # VOTO -- NUNCA SEM DIAGNOSTICO
        # ====================================================================
        Sintoma(
            "seguranca_publica", "Seguranca publica",
            CategoriaSintoma.VOTO,
            "Sensacao de inseguranca. Politico promete lei dura.",
            tem_diagnostico=False,
            acao_alivio="NENHUMA sem diagnostico",
            acao_cura="Investimento social + desmilitarizacao + dados reais",
            prazo_diagnostico_dias=90,
            risco_alivio_sem_cura="Lei dura sem dado mata inocente. Vira palanque (P9).",
        ),
        Sintoma(
            "reforma_politica", "Reforma politica",
            CategoriaSintoma.VOTO,
            "Todos querem reforma politica. Cada um com versao diferente.",
            tem_diagnostico=False,
            acao_alivio="NENHUMA sem diagnostico",
            acao_cura="Assembleia constituinte + P4 processo democratico",
            prazo_diagnostico_dias=180,
            risco_alivio_sem_cura="Reforma sem dado vira armadilha eleitoral.",
        ),
        Sintoma(
            "imigracao", "Imigracao / refugiado",
            CategoriaSintoma.VOTO,
            "Cresce xenofobia. Politico usa medo.",
            tem_diagnostico=False,
            acao_alivio="NENHUMA sem diagnostico",
            acao_cura="Politica migratoria humana + integracao + dados",
            prazo_diagnostico_dias=60,
            risco_alivio_sem_cura="Deportacao sem dado e palanque, nao politica.",
        ),

        # ====================================================================
        # ESTRUTURA -- DIAGNOSTICA + TRATA SIMULTANEO
        # ====================================================================
        Sintoma(
            "educacao_ruim", "Educacao de baixa qualidade",
            CategoriaSintoma.ESTRUTURA,
            "PISA baixo. Analfabetismo funcional alto.",
            tem_diagnostico=False,
            acao_alivio="Investimento em professor + merenda + escola integral",
            acao_cura="Reforma educacional completa (open_education_system)",
            prazo_diagnostico_dias=90,
            risco_alivio_sem_cura="Investir sem saber onde doi e jogar dinheiro fora.",
        ),
        Sintoma(
            "saneamento_falta", "Falta de saneamento",
            CategoriaSintoma.ESTRUTURA,
            "35M sem agua tratada. 100M sem esgoto.",
            tem_diagnostico=False,
            acao_alivio="Cisterna + fossa septica + filtro comunitario",
            acao_cura="Plano nacional de saneamento universal",
            prazo_diagnostico_dias=60,
            risco_alivio_sem_cura="Cisterna sem rede = perene dependencia de ONG.",
        ),
        Sintoma(
            "habitacao_precaria", "Habitação precaria",
            CategoriaSintoma.ESTRUTURA,
            "Milhoes em favela, cortico, rua.",
            tem_diagnostico=False,
            acao_alivio="Moradia temporaria + services para sem-teto",
            acao_cura="Programa habitacional + combate especulacao",
            prazo_diagnostico_dias=90,
            risco_alivio_sem_cura="Moradia temporaria vira permanente se causa ignora.",
        ),
    ]


# ============================================================================
# 4. MOTOR DE TRIAGEM
# ============================================================================

class TriageOperacional:
    """
    Triagem de sintomas do Brasil.

    Regra de ouro:
      VIDA    -> age agora, diagnostica depois.
      BOLSO   -> diagnostica primeiro.
      VOTO    -> nunca sem diagnostico.
      ESTRUTURA -> diagnostica + trata junto.
    """

    NOME = "OpenTriageOperacional"
    VERSAO = "0.1.0-spec"

    REGRA_OURO = [
        "Vida em risco -> age AGORA, diagnostica depois",
        "Bolso afetado -> diagnostica PRIMEIRO, age depois",
        "Voto em jogo -> NUNCA age sem diagnostico (vira palanque)",
        "Estrutura -> diagnostica e trata SIMULTANEAMENTE",
        "Alivio SEM cura = obrigacao de diagnosticar a causa",
        "Confundir alivio com cura mata o paciente",
    ]

    def __init__(self) -> None:
        self.sintomas: List[Sintoma] = _init_sintomas()

    # -- triagem ------------------------------------------------------------

    def triar(self, sintoma: Sintoma) -> DecisaoTriagem:
        """Tria um sintoma e retorna decisao."""

        # VIDA: age agora
        if sintoma.categoria == CategoriaSintoma.VIDA:
            return DecisaoTriagem(
                sintoma=sintoma,
                status=StatusTriagem.AGIR_AGORA,
                acao_recomendada=TipoAcao.ALIVIO,
                justificativa=(
                    f"VIDA em risco. Acao de alivio IMEDIATA. "
                    f"Diagnostico obrigatorio em {sintoma.prazo_diagnostico_dias} dias. "
                    f"Alivio nao e cura -- linka com diagnostico futuro."
                ),
                prazo_diagnostico_dias=sintoma.prazo_diagnostico_dias,
                alerta=sintoma.risco_alivio_sem_cura,
            )

        # BOLSO: diagnostica primeiro
        if sintoma.categoria == CategoriaSintoma.BOLSO:
            if sintoma.tem_diagnostico:
                return DecisaoTriagem(
                    sintoma=sintoma,
                    status=StatusTriagem.AGIR_COM_RESSALVA,
                    acao_recomendada=TipoAcao.CURA,
                    justificativa="Diagnostico disponivel. Agir na causa.",
                    prazo_diagnostico_dias=0,
                )
            return DecisaoTriagem(
                sintoma=sintoma,
                status=StatusTriagem.DIAGNOSTICAR_PRIMEIRO,
                acao_recomendada=TipoAcao.DIAGNOSTICO,
                justificativa=(
                    f"BOLSO afetado. Diagnostico OBRIGATORIO antes de agir. "
                    f"Acao sem dado causa dano economico maior."
                ),
                prazo_diagnostico_dias=sintoma.prazo_diagnostico_dias,
                alerta="Subsidio sem causa diagnosticada = inflacao galopante depois.",
            )

        # VOTO: nunca sem diagnostico
        if sintoma.categoria == CategoriaSintoma.VOTO:
            if sintoma.tem_diagnostico:
                return DecisaoTriagem(
                    sintoma=sintoma,
                    status=StatusTriagem.AGIR_COM_RESSALVA,
                    acao_recomendada=TipoAcao.CURA,
                    justificativa="Diagnostico disponivel. Agir com cautela (P9).",
                    prazo_diagnostico_dias=0,
                )
            return DecisaoTriagem(
                sintoma=sintoma,
                status=StatusTriagem.BLOQUEAR,
                acao_recomendada=TipoAcao.DIAGNOSTICO,
                justificativa=(
                    "VOTO em jogo. Acao sem diagnostico vira PALANQUE (P9). "
                    "Bloqueado ate ter FATO (7 criterios do gate epistemologico)."
                ),
                prazo_diagnostico_dias=sintoma.prazo_diagnostico_dias,
                alerta="Politico que age sem dado nao quer resolver. Quer voto.",
            )

        # ESTRUTURA: diagnostica + trata
        if sintoma.categoria == CategoriaSintoma.ESTRUTURA:
            return DecisaoTriagem(
                sintoma=sintoma,
                status=StatusTriagem.AGIR_COM_RESSALVA,
                acao_recomendada=TipoAcao.PALIATIVO,
                justificativa=(
                    "ESTRUTURAL. Alivio e cura andam juntos. "
                    "Investe enquanto diagnostica. Nao para um pelo outro."
                ),
                prazo_diagnostico_dias=sintoma.prazo_diagnostico_dias,
                alerta="Alivio sem cura vira dependencia permanente.",
            )

        return DecisaoTriagem(
            sintoma=sintoma,
            status=StatusTriagem.MONITORAR,
            acao_recomendada=TipoAcao.DIAGNOSTICO,
            justificativa="Categoria desconhecida. Monitorar.",
            prazo_diagnostico_dias=999,
        )

    # -- triagem em lote ----------------------------------------------------

    def triar_todos(self) -> List[DecisaoTriagem]:
        return [self.triar(s) for s in self.sintomas]

    def agir_agora(self) -> List[DecisaoTriagem]:
        """Sintomas que pode agir imediatamente."""
        return [d for d in self.triar_todos() if d.status == StatusTriagem.AGIR_AGORA]

    def bloqueados(self) -> List[DecisaoTriagem]:
        """Sintomas bloqueados (sem diagnostico, categoria VOTO)."""
        return [d for d in self.triar_todos() if d.status == StatusTriagem.BLOQUEAR]

    # -- catalogos ----------------------------------------------------------

    def todos_sintomas(self) -> List[Dict[str, Any]]:
        return [
            {
                "id": s.id,
                "nome": s.nome,
                "categoria": s.categoria.id,
                "tem_diagnostico": s.tem_diagnostico,
                "alivio": s.acao_alivio,
                "cura": s.acao_cura,
                "prazo_diag": s.prazo_diagnostico_dias,
                "risco_alivio": s.risco_alivio_sem_cura,
            }
            for s in self.sintomas
        ]

    # -- scorecard ----------------------------------------------------------

    def scorecard(self) -> Dict[str, Any]:
        todos = self.triar_todos()
        return {
            "sistema": self.NOME,
            "versao": self.VERSAO,
            "sintomas_catalogados": len(self.sintomas),
            "agir_agora": sum(1 for d in todos if d.status == StatusTriagem.AGIR_AGORA),
            "bloqueados": sum(1 for d in todos if d.status == StatusTriagem.BLOQUEAR),
            "diagnosticar_primeiro": sum(1 for d in todos if d.status == StatusTriagem.DIAGNOSTICAR_PRIMEIRO),
            "agir_com_ressalva": sum(1 for d in todos if d.status == StatusTriagem.AGIR_COM_RESSALVA),
            "categorias": len(list(CategoriaSintoma)),
            "tipos_acao": len(list(TipoAcao)),
            "status_triagem": len(list(StatusTriagem)),
        }


# ============================================================================
# 5. DEMO
# ============================================================================

def _demo() -> None:
    tri = TriageOperacional()

    print("=" * 70)
    print(f"{tri.NOME} v{tri.VERSAO} -- Triagem Operacional")
    print("=" * 70)

    # --- Regra de ouro ---
    print(f"\n[REGRA DE OURO]\n")
    for i, r in enumerate(tri.REGRA_OURO, 1):
        print(f"  {i}. {r}")

    # --- Categorias ---
    print(f"\n\n[CATEGORIAS]\n")
    for c in CategoriaSintoma:
        print(f"  {c.id.upper():<12} {c.rotulo}")

    # --- AGIR AGORA ---
    print(f"\n\n[AGIR AGORA -- vida em risco ({len(tri.agir_agora())})]\n")
    for d in tri.agir_agora():
        print(f"  [{d.sintoma.id.upper()}] {d.sintoma.nome}")
        print(f"  Categoria: {d.sintoma.categoria.id.upper()}")
        print(f"  Alivio: {d.sintoma.acao_alivio}")
        print(f"  Diagnostico em: {d.prazo_diagnostico_dias} dias")
        print(f"  Risco: {d.alerta}")
        print()

    # --- BLOQUEADOS ---
    print(f"\n[BLOQUEADOS -- sem diagnostico vira palanque ({len(tri.bloqueados())})]\n")
    for d in tri.bloqueados():
        print(f"  [{d.sintoma.id.upper()}] {d.sintoma.nome}")
        print(f"  Motivo: {d.justificativa}")
        print()

    # --- Triagem completa ---
    print(f"\n\n[TRIAGEM COMPLETA]\n")
    print(f"  {'ID':<24} {'CATEG':<10} {'STATUS':<16} {'ACAO':<14} {'PRAZO':>6}")
    print(f"  {'-'*75}")
    for d in tri.triar_todos():
        print(f"  {d.sintoma.id:<24} {d.sintoma.categoria.id:<10} "
              f"{d.status.id:<16} {d.acao_recomendada.id:<14} "
              f"{d.prazo_diagnostico_dias:>5}d")

    # --- Simulacao: apendice ---
    print(f"\n\n[SIMULACAO: Confundir alivio com cura]\n")
    print("""  Paciente chega com febre.
  Medico da aspirina. Febre baixa.
  Paciente vai pra casa. Apêndice estoura.
  Paciente morre 'sem febre'.

  Crianca passa fome.
  Estado da cesta. Crianca come.
  Estado para cesta. Crianca passa fome.
  Cesta nao e cura. E aspirina.

  Sem diagnosticar a CAUSA, todo alivio e temporario.
  E necessario. Salva vida. Mas NAO e cura.
  Confundir os dois mata mais devagar que a doenca.""")

    # --- Scorecard ---
    print(f"\n\n[SCORECARD]")
    sc = tri.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<28} {v}")


if __name__ == "__main__":
    _demo()
