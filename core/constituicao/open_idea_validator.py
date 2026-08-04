#!/usr/bin/env python3
"""
OpenIdeaValidator -- Validador de Ideias Independente de Sistema
==================================================================
"Nao valide SISTEMA. valide IDEA.
 Sistema e abstracao. Ideia tem impacto na VIDA."

O capitalista diz 'comunismo matou 100 milhoes'.
O comunista diz 'capitalismo mata 150 milhoes por pobreza'.
Ambos tem razao. Ambos perdem. Porque discutem quem matou mais.

Este modulo nao entra nesse debate. Faz outra coisa:

  1. CATALOGA dados historicos reais de 7 sistemas politicos
  2. MEDA quem tem melhor qualidade de vida (nao quem tem melhor teoria)
  3. EXTRAI os padroes comuns dos que funcionam
  4. DEFINE o LAYER 0 conceitual: criterios universais de VIDA
  5. VALIDA qualquer ideia contra esses criterios

O LAYER 0 NAO e capitalismo nem comunismo. E o que FUNCIONA.
Extraido de dados, nao de teoria. De vida, nao de livro.

OS 7 SISTEMAS ANALISADOS (dados validados):
  - Noruega       (social-democracia nordica)
  - Finlandia     (idem, #1 felicidade mundial 7 anos)
  - Dinamarca     (idem, primeira lei de transparencia do mundo)
  - Costa Rica    (ABOLIU exercito em 1948, #1 LatAm)
  - Uruguai       (#1 LatAm em democracia)
  - Kerala/India  (estado indiano, socialismo democratico)
  - Brasil        (referencia para comparacao)

FONTES:
  PNUD IDH 2022, World Bank Gini, World Happiness Report 2024,
  EIU Democracy Index, constituies nacionais.

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field


# ============================================================================
# 1. DADOS HISTORICOS VALIDADOS
# ============================================================================

@dataclass(frozen=True)
class SistemaPolitico:
    """Dados historicos validados de um sistema politico real."""
    nome: str
    modelo: str               # como se autodenomina
    idh: float                # PNUD 2022
    gini: float               # World Bank (0=igual, 1=desigual)
    felicidade: Optional[float]  # World Happiness Report 2024
    democracia: float         # EIU Index (0-10)
    horas_trabalho: float      # por semana
    ferias_dias: int
    saude_universal: bool
    educacao_gratuita: bool
    gasto_militar_pct: float  # % PIB
    cooperativas_pct: float   # % populacao em cooperativa
    mortalidade_infantil: float  # por 1000
    expectativa_vida: float
    ano_transparencia: int    # ano da primeira lei de acesso a informacao
    sem_exercito: bool        # aboliu exercito?
    nota_historica: str       # licao que este caso ensina
    fontes: List[str] = field(default_factory=list)


def _init_sistemas() -> List[SistemaPolitico]:
    return [
        SistemaPolitico(
            "Noruega", "Social-democracia nordica",
            0.961, 0.272, 7.394, 9.81, 37.5, 25,
            True, True, 1.7, 0.20, 2.3, 83.2, 1814, False,
            "Fundo soberano do petroleo: o lucro do recurso natural "
            "pertence ao POVO, nao a empresa. Investiu o dinheiro, "
            "gasta so os JUROS. Previu o fim do petroleo. "
            "Resultado: IDH #1 do mundo. NAO por teoria. Por GESTAO.",
            ["PNUD IDH 2022", "World Bank Gini", "EIU Democracy Index"],
        ),
        SistemaPolitico(
            "Finlandia", "Social-democracia nordica",
            0.942, 0.273, 7.741, 9.30, 37, 30,
            True, True, 2.3, 0.30, 2.1, 82.2, 1951, False,
            "#1 em felicidade mundial por 7 anos seguidos. NAO e "
            "felicidade alegre. E SATISFACAO. O cidadao confia no "
            "Estado porque o Estado entrega. Saude, educacao, seguranca. "
            "Sem cobertura de revista. Com cobertura de direto.",
            ["PNUD IDH 2022", "World Happiness Report 2024"],
        ),
        SistemaPolitico(
            "Dinamarca", "Social-democracia nordica",
            0.940, 0.274, 7.586, 9.50, 37, 31,
            True, True, 1.4, 0.25, 3.2, 81.5, 1766, False,
            "PRIMEIRA lei de transparencia do mundo (1766!). Ha 258 "
            "anos o cidadao dinamarques ve o que o Estado faz. "
            "P5 (transparencia radical) nao e ideia nova. E provada "
            "ha 2 seculos e meio.",
            ["PNUD IDH 2022", "World Bank Gini", "EIU Democracy Index"],
        ),
        SistemaPolitico(
            "Costa Rica", "Democracia sem exercito",
            0.806, 0.482, 6.614, 8.29, 48, 14,
            True, True, 0.0, 0.10, 7.8, 80.1, 2003, True,
            "ABOLIU O EXERCITO em 1948. Jose Figueres quebrou o muro "
            "do quartel com uma marretada. Investiu em EDUCACAO e "
            "SAUDE o que gastaria em armas. Resultado: #1 LatAm em "
            "democracia, felicidade e expectativa de vida. "
            "P10 (soberania sem militarismo) PROVADO ha 76 anos.",
            ["PNUD IDH 2022", "Constituicao CR 1948"],
        ),
        SistemaPolitico(
            "Uruguai", "Social-democracia sul-americana",
            0.830, 0.402, 6.387, 8.17, 44, 20,
            True, True, 1.6, 0.08, 6.7, 78.0, 2008, False,
            "Pequeno pais que chegou ao topo LatAm SEM revolcao "
            "armada. Por processo democratico. Legalizou maconha, "
            "casamento gay, aborto -- por VOTACAO, nao decreto. "
            "P4 (processo democratico) funcionando no mundo real.",
            ["PNUD IDH 2022", "EIU Democracy Index"],
        ),
        SistemaPolitico(
            "Kerala (India)", "Socialismo democratico (estado)",
            0.774, 0.380, None, 7.0, 48, 12,
            True, True, 0.0, 0.15, 6.0, 77.3, 2005, True,
            "Estado dentro da India. Mais pobre que a media nacional "
            "em PIB. Mas IDH SUPERIOR. Mortalidade infantil 6.0 vs "
            "26.6 da India. Alfabetizacao 96% vs 74%. PROVA que o "
            "PIB nao determina qualidade de vida. INVESTIMENTO "
            "PUBLICO sim.",
            ["India Human Development Report", "UNDP Kerala HDI"],
        ),
        SistemaPolitico(
            "Brasil", "Democracia imperfeita (referencia)",
            0.760, 0.489, 6.330, 6.68, 44, 30,
            True, True, 1.3, 0.03, 11.5, 75.9, 2011, False,
            "Tem SUS, tem escola publica, tem LAI (2011). Mas "
            "sub-financia tudo. Gini 0.489 = uma das maiores "
            "desigualdades do mundo. 6a maior economia, 89a em "
            "qualidade de vida. NAO e problema de dinheiro. "
            "E problema de DISTRIBUICAO.",
            ["PNUD IDH 2022", "World Bank Gini"],
        ),
    ]


# ============================================================================
# 2. LAYER 0 CONCEITUAL -- OS CRITERIOS UNIVERSAIS DE VIDA
# ============================================================================

class CriterioVida(Enum):
    """
    Os 10 criterios de VIDA extraidos dos dados.

    NAO sao 'direitos humanos' abstratos. Sao padroes OBSERVADOS
    nos sistemas que entregam melhor qualidade de vida.

    Cada criterio e mensuravel. Cada um tem evidencia historica.
    Nenhum depende de ideologia. Todos dependem de RESULTADO.
    """
    SAUDE = (
        "saude",
        "Saude universal: ninguem morre por nao ter dinheiro",
        "Todos os top 5 tem saude universal. Custo? Menos que "
        "o custo de tratar doentes tardios e epidemias.",
        True,  # valor nos top performers
    )
    EDUCACAO = (
        "educacao",
        "Educacao gratuita: conhecimento nao e privilegio",
        "Kerala provou: investir em educacao supera investir "
        "em PIB. IDH 0.774 com renda baixa. Por que? ESCOLA.",
        True,
    )
    DESIGUALDADE = (
        "desigualdade",
        "Gini baixo: a distancia entre rico e pobre e pequena",
        "Top 3: Gini 0.27. Brasil: 0.49. Quase o dobro. "
        "Desigualdade mata mais que cancer.",
        False,  # lower is better
    )
    TEMPO = (
        "tempo",
        "Tempo livre: 37h/semana, 25+ dias de ferias",
        "Finlandia: 37h/semana, #1 felicidade. Nao e coincidencia. "
        "Tempo livre e SAUDE MENTAL. Quem trabalha 60h nao vive. "
        "Sobrevive.",
        True,  # more free time
    )
    TRANSPARENCIA = (
        "transparencia",
        "Estado transparente: cidadao ve tudo",
        "Dinamarca tem lei de transparencia desde 1766. "
        "258 anos. Funciona. Brasil: 2011 (13 anos). "
        "Ta aprendendo ainda.",
        True,
    )
    MILITARISMO = (
        "militarismo",
        "Baixo gasto militar: armas nao alimentam crianca",
        "Costa Rica: 0%. Aboliu exercito. Investiu em escola. "
        "#1 LatAm. O exercito mais forte da regiao e Chile "
        "(2.6% PIB). Qual tem melhor IDH?",
        False,  # lower is better
    )
    COOPERATIVISMO = (
        "cooperativismo",
        "Economia cooperativa: o povo e dono do negocio",
        "Finlandia: 30% da populacao em cooperativa. Noruega: 20%. "
        "Brasil: 3%. Cooperativa e empresa que pertence a quem USA. "
        "Nao a quem EXPLORA.",
        True,
    )
    VIDA = (
        "vida",
        "Expectativa de vida alta + mortalidade infantil baixa",
        "Noruega: 83 anos, 2.3 mortes/1000. Brasil: 76 anos, "
        "11.5 mortes/1000. A diferenca e 7 anos de vida. "
        "Por que? SAUDE. So saude.",
        True,
    )
    DEMOCRACIA = (
        "democracia",
        "Democracia real: cidadao decide, nao elite",
        "Top 5 todos tem democracia 8.0+. Brasil: 6.68 "
        "(democracia imperfeita). Nao e que democracia falhou. "
        "E que a nossa e INCOMPLETA.",
        True,
    )
    PACIFICACAO = (
        "pacificacao",
        "Pais sem exercito ou com gasto militar minimo",
        "Costa Rica aboliu exercito em 1948. Kerala nao tem. "
        "Ambos com qualidade de vida superior a paises armados "
        "da regiao. O exercito PROTEGE de quem? Do proprio povo?",
        False,  # less militarism is better
    )

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def evidencia(self) -> str:
        return self.value[2]

    @property
    def mais_e_melhor(self) -> bool:
        """True = valor alto e melhor. False = valor baixo e melhor."""
        return self.value[3]


# ============================================================================
# 3. SIMULADOR
# ============================================================================

class IdeaValidator:
    """
    Simula e valida sistemas politicos contra criterios de VIDA.

    Faz 3 coisas:
    1. RANKEIA sistemas por qualidade de vida real
    2. EXTRAI o Layer 0 (padroes comuns dos que funcionam)
    3. VALIDA qualquer ideia contra os criterios de VIDA
    """

    def __init__(self) -> None:
        self.sistemas: List[SistemaPolitico] = _init_sistemas()

    # -- ranking ------------------------------------------------------------

    def ranking(self) -> List[Dict[str, Any]]:
        """Ranking por score composto de qualidade de vida."""
        scores = []
        for s in self.sistemas:
            score = self._score_vida(s)
            scores.append({
                "nome": s.nome,
                "modelo": s.modelo,
                "idh": s.idh,
                "gini": s.gini,
                "felicidade": s.felicidade,
                "score": score,
                "expectativa_vida": s.expectativa_vida,
                "mortalidade_infantil": s.mortalidade_infantil,
                "horas_trabalho": s.horas_trabalho,
                "sem_exercito": s.sem_exercito,
            })
        return sorted(scores, key=lambda x: x["score"], reverse=True)

    def _score_vida(self, s: SistemaPolitico) -> float:
        """
        Score 0-100 baseado em dados REAIS, nao ideologia.

        Componentes (pesos iguais):
        - IDH (0-1 -> 0-25 pts)
        - Desigualdade (gini invertido, 0-25 pts)
        - Felicidade (0-25 pts)
        - Democracia (0-10 -> 0-25 pts)
        """
        idh_pts = s.idh * 25
        gini_pts = (1.0 - s.gini) * 25
        fel_pts = (s.felicidade / 10.0 * 25) if s.felicidade else 12.5  # meio se sem dado
        dem_pts = (s.democracia / 10.0) * 25
        return round(idh_pts + gini_pts + fel_pts + dem_pts, 1)

    # -- layer 0 -----------------------------------------------------------

    def layer_zero(self) -> List[Dict[str, Any]]:
        """Os 10 criterios universais extraidos dos dados."""
        return [
            {"id": c.id, "rotulo": c.rotulo, "evidencia": c.evidencia,
             "mais_e_melhor": c.mais_e_melhor}
            for c in CriterioVida
        ]

    def padroes_comuns(self) -> List[str]:
        """O que TODOS os top 5 tem em comum -- independente de ismo."""
        top5 = sorted(self.sistemas, key=lambda s: self._score_vida(s), reverse=True)[:5]
        padroes = []

        # Saude universal
        if all(s.saude_universal for s in top5):
            padroes.append(
                "SAUDE UNIVERSAL: todos os top 5 tem. Nenhum deixa "
                "cidadao morrer por dinheiro. Nao e socialismo. E logica."
            )
        # Educacao gratuita
        if all(s.educacao_gratuita for s in top5):
            padroes.append(
                "EDUCACAO GRATUITA: todos os top 5 tem. Kerala provou "
                "que escola supera renda na qualidade de vida."
            )
        # Gini baixo
        ginis = [s.gini for s in top5]
        if max(ginis) < 0.50:
            padroes.append(
                f"DESIGUALDADE CONTROLADA: top 5 tem Gini medio "
                f"{sum(ginis)/len(ginis):.2f}. Brasil: 0.49. "
                f"Desigualdade e o maior preditor de violencia."
            )
        # Transparencia
        padroes.append(
            "TRANSPARENCIA RADICAL: Dinamarca tem desde 1766. "
            "Noruega desde 1814. Nao e moda. E tradicao que funciona."
        )
        # Cooperativismo
        coops = [s.cooperativas_pct for s in top5]
        if sum(coops) / len(coops) > 0.10:
            padroes.append(
                f"COOPERATIVISMO: top 5 tem em media "
                f"{sum(coops)/len(coops):.0%} da populacao em cooperativa. "
                f"Brasil: 3%. Cooperativa e negocio do povo, nao de acionista."
            )
        # Pacificacao
        pacifistas = [s for s in top5 if s.sem_exercito or s.gasto_militar_pct < 2.0]
        if len(pacifistas) >= 4:
            padroes.append(
                f"BAIXO MILITARISMO: {len(pacifistas)}/5 top gastam "
                f"<2% PIB em armas. Costa Rica aboliu exercito em 1948 "
                f"e lidera LatAm. Armas nao alimentam."
            )
        # Tempo
        horas = [s.horas_trabalho for s in top5]
        if sum(horas) / len(horas) <= 42:
            padroes.append(
                f"TEMPO LIVRE: top 5 trabalha em media "
                f"{sum(horas)/len(horas):.0f}h/semana. Finlandia (#1 felicidade): "
                f"37h. Quem trabalha 60h nao vive. Sobrevive."
            )

        return padroes

    # -- validador de ideias ------------------------------------------------

    def validar_idea(
        self,
        nome: str,
        descricao: str,
        saude: Optional[bool] = None,
        educacao: Optional[bool] = None,
        reduz_desigualdade: Optional[bool] = None,
        aumenta_tempo_livre: Optional[bool] = None,
        transparente: Optional[bool] = None,
        belico: Optional[bool] = None,
        cooperativo: Optional[bool] = None,
        aumenta_vida: Optional[bool] = None,
        democratico: Optional[bool] = None,
        pacifico: Optional[bool] = None,
    ) -> Dict[str, Any]:
        """
        Valida uma ideia contra os 10 criterios de VIDA.

        Retorna score 0-100 e veredito.
        Nao julga ideologia. Julga IMPACTO.
        """
        criterios = {
            "saude": (saude, True),
            "educacao": (educacao, True),
            "reduz_desigualdade": (reduz_desigualdade, True),
            "aumenta_tempo_livre": (aumenta_tempo_livre, True),
            "transparente": (transparente, True),
            "belico": (belico, False),
            "cooperativo": (cooperativo, True),
            "aumenta_vida": (aumenta_vida, True),
            "democratico": (democratico, True),
            "pacifico": (pacifico, True),
        }

        cumpridos = []
        violados = []
        nao_se_aplica = []

        for crit, (valor, positivo) in criterios.items():
            if valor is None:
                nao_se_aplica.append(crit)
            elif (valor and positivo) or (not valor and not positivo):
                cumpridos.append(crit)
            else:
                violados.append(crit)

        avaliados = len(cumpridos) + len(violados)
        score = (len(cumpridos) / avaliados * 100) if avaliados else 0.0

        if score >= 80:
            veredito = "VALE A PENA -- alinhado com VIDA"
        elif score >= 60:
            veredito = "PROMISSOR -- com ressalvas"
        elif score >= 40:
            veredito = "DUVIDOSO -- impacto misto"
        else:
            veredito = "REJEITADO -- prejudica VIDA"

        return {
            "ideia": nome,
            "descricao": descricao,
            "score": round(score, 1),
            "veredito": veredito,
            "cumpridos": cumpridos,
            "violados": violados,
            "nao_se_aplica": nao_se_aplica,
        }

    # -- comparador Brasil -------------------------------------------------

    def brasil_vs_top(self) -> List[Dict[str, Any]]:
        """Compara Brasil com a media dos top 3 em cada metrica."""
        top3 = sorted(self.sistemas, key=lambda s: self._score_vida(s), reverse=True)[:3]
        brasil = [s for s in self.sistemas if s.nome == "Brasil"][0]

        metricas = ["idh", "gini", "felicidade", "democracia", "horas_trabalho",
                    "cooperativas_pct", "mortalidade_infantil", "expectativa_vida"]

        resultado = []
        for m in metricas:
            vals_top = [getattr(s, m) for s in top3 if getattr(s, m) is not None]
            val_br = getattr(brasil, m)
            media_top = sum(vals_top) / len(vals_top) if vals_top else None

            # determine if higher or lower is better
            lower_better = m in ("gini", "horas_trabalho", "mortalidade_infantil")
            if media_top and val_br:
                if lower_better:
                    diferenca = val_br - media_top  # positive = Brasil pior
                    status = "BRASIL PIOR" if diferenca > 0 else "BRASIL MELHOR"
                else:
                    diferenca = val_br - media_top  # positive = Brasil melhor
                    status = "BRASIL PIOR" if diferenca < 0 else "BRASIL MELHOR"
            else:
                diferenca = None
                status = "N/A"

            resultado.append({
                "metrica": m,
                "top3_media": round(media_top, 3) if media_top else None,
                "brasil": val_br,
                "diferenca": round(diferenca, 3) if diferenca is not None else None,
                "status": status,
            })
        return resultado

    # -- scorecard ----------------------------------------------------------

    def scorecard(self) -> Dict[str, Any]:
        return {
            "sistemas_analisados": len(self.sistemas),
            "criterios_l0": len(list(CriterioVida)),
            "fontes": "PNUD, World Bank, World Happiness Report, EIU",
        }


# ============================================================================
# 4. DEMO
# ============================================================================

def _demo() -> None:
    v = IdeaValidator()

    print("=" * 70)
    print("OpenIdeaValidator -- Validador de Ideias Independente de Sistema")
    print("=" * 70)

    # --- Ranking ---
    print("\n[RANKING DE QUALIDADE DE VIDA (score 0-100)]\n")
    ranking = v.ranking()
    print(f"  {'#':<3} {'PAIS':<20} {'MODELO':<30} {'SCORE':>6} {'IDH':>5} {'GINI':>5} {'FEL':>5}")
    print(f"  {'-'*80}")
    for i, r in enumerate(ranking, 1):
        fel = f"{r['felicidade']:.1f}" if r["felicidade"] else "  N/A"
        print(f"  {i}.  {r['nome']:<20} {r['modelo']:<30} {r['score']:>5.1f} "
              f"{r['idh']:>5.3f} {r['gini']:>5.3f} {fel:>5}")

    # --- Padroes comuns ---
    print(f"\n\n[PADROES COMUNS DOS TOP 5 -- independente de ISMO]\n")
    for i, p in enumerate(v.padroes_comuns(), 1):
        print(f"  {i}. {p}\n")

    # --- Layer 0 ---
    print(f"\n[LAYER 0 CONCEITUAL -- {len(list(CriterioVida))} CRITERIOS DE VIDA]\n")
    print("  (extrado de dados, nao de teoria. De vida, nao de livro.)\n")
    for c in v.layer_zero():
        direcao = "mais = melhor" if c["mais_e_melhor"] else "menos = melhor"
        print(f"  [{c['id'].upper()}] {c['rotulo']}")
        print(f"    Direcao: {direcao}")
        print(f"    Evidencia: {c['evidencia']}\n")

    # --- Brasil vs Top ---
    print("[BRASIL vs MEDIA TOP 3]\n")
    print(f"  {'METRICA':<25} {'TOP3':>8} {'BRASIL':>8} {'DIFER.':>8} {'STATUS':<15}")
    print(f"  {'-'*70}")
    for r in v.brasil_vs_top():
        top_val = f"{r['top3_media']:.3f}" if r['top3_media'] else "N/A"
        br_val = f"{r['brasil']:.3f}" if r['brasil'] else "N/A"
        dif = f"{r['diferenca']:+.3f}" if r['diferenca'] is not None else "N/A"
        print(f"  {r['metrica']:<25} {top_val:>8} {br_val:>8} {dif:>8} {r['status']}")

    # --- Validar ideias ---
    print("\n\n[VALIDACAO DE IDEIAS]\n")

    # Idea 1: SUS
    r1 = v.validar_idea(
        "SUS (Saude Universal)",
        "Sistema unico de saude publico e gratuito para todos",
        saude=True, aumenta_vida=True, democratico=True, transparente=True,
    )
    print(f"  {r1['ideia']}: score={r1['score']} -> {r1['veredito']}")
    if r1["violados"]:
        print(f"    Violados: {r1['violados']}")

    # Idea 2: Privatizar saude
    r2 = v.validar_idea(
        "Privatizar Saude",
        "Acabar com SUS. Saude so pra quem pode pagar.",
        saude=False, aumenta_vida=False, democratico=False,
    )
    print(f"  {r2['ideia']}: score={r2['score']} -> {r2['veredito']}")
    if r2["violados"]:
        print(f"    Violados: {r2['violados']}")

    # Idea 3: Reducao jornada 40h
    r3 = v.validar_idea(
        "Jornada 40h/semana",
        "Reduzir jornada para 40h com salario mantido",
        aumenta_tempo_livre=True, democratico=True, cooperativo=False,
    )
    print(f"  {r3['ideia']}: score={r3['score']} -> {r3['veredito']}")

    # Idea 4: Comprar armas
    r4 = v.validar_idea(
        "Comprar 36 caças Gripen",
        "Gastar R$ 36 bilhoes em avioes de guerra",
        saude=None, educacao=None, belico=True, pacifico=False,
    )
    print(f"  {r4['ideia']}: score={r4['score']} -> {r4['veredito']}")
    if r4["violados"]:
        print(f"    Violados: {r4['violados']}")

    # Idea 5: Reforma agraria
    r5 = v.validar_idea(
        "Reforma Agraria",
        "Terra pra quem cuida. Guardiao, nao dono.",
        reduz_desigualdade=True, cooperativo=True, democratico=True,
        aumenta_vida=True, pacifico=True,
    )
    print(f"  {r5['ideia']}: score={r5['score']} -> {r5['veredito']}")

    # --- Licoes ---
    print("\n\n[LICOES HISTORICAS]\n")
    for s in sorted(v.sistemas, key=lambda x: v._score_vida(x), reverse=True):
        print(f"  [{s.nome.upper()}] ({s.modelo})")
        print(f"  Score: {v._score_vida(s)}")
        print(f"  Licao: {s.nota_historica}\n")

    # --- Filosofia ---
    print("=" * 70)
    print("FILOSOFIA -- O Layer 0 Nao Tem Ismo")
    print("=" * 70)
    print("""
O CAPITALISTA DIZ:
  "O comunismo matou 100 milhoes."

O COMUNISTA DIZ:
  "O capitalismo mata 150 milhoes por pobreza."

O VALIDADOR DIZ:
  "Ambos tem razao. Ambos perdem. Vamos ver os DADOS."

OS DADOS DIZEM:
  Noruega: IDH 0.961, Gini 0.27, felicidade 7.4
  Costa Rica: aboliu exercito, #1 LatAm
  Kerala: mais pobre, mais alfabetizado que a India
  Finlandia: #1 felicidade 7 anos, 37h/semana

NENHUM destes funcionou por ISMO. Funcionou por:

  1. Saude universal
  2. Educacao gratuita
  3. Baixa desigualdade
  4. Transparencia
  5. Cooperativismo
  6. Baixo militarismo
  7. Tempo livre
  8. Democracia real
  9. Vida longa
  10. Pacificacao

Chame de capitalismo. Chame de socialismo. Chame de o que quiser.
Se entregar esses 10, FUNCIONA. Se nao entregar, FALHOU.

O LAYER 0 NAO TEM ISMO.
TEM VIDA.

A proxima vez que alguem disser "capitalismo e repressor" ou
"comunismo e repressor", pergunte:

  "Trata o faxineiro bem?"

Se sim, importa o ismo? Se nao, importa o ismo?
""")


if __name__ == "__main__":
    _demo()
