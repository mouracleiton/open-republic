#!/usr/bin/env python3
"""
OpenPoliticalRiskPredictor -- Antecipacao Preditiva de Risco Politico
======================================================================
"O modelo nao condena. O modelo PRIORIZA auditoria."

Atualizado com dados publicos 2024/2025.

TESE:
  O constitutional_monitor detecta o evento enquanto acontece.
  O political_reliability avalia o historico passado.
  Este modulo antecipa: o padrao ATUAL sugere risco futuro?

  O politico ainda nao fez merda. Mas o padrao de comportamento
  se parece com o padrao de quem DEPOIS fez. O modelo aponta.
  A assembleia decide.

O LIMITE ETICO (duro):

  1. O modelo NAO condena. Score alto nao e culpa. E ATENCAO.
     "Esta pessoa merece mais fiscalizacao porque o padrao
     se parece com o de quem depois fez merda."

  2. O modelo e TRANSPARENTE (P5). Cada score e explicavel
     por fator. Sem caixa-preta. Sem ML opaco. Regras com peso
     visivel, dado mensuravel, justificacao clara.

  3. O modelo e REVIGAVEL. Se o dado muda, o score muda.
     Nao e marcacao eterna. Politico que melhora ve score cair.

  4. O modelo NAO usa dados intimos (P2). Nao analisa sexualidade,
     religiao, saude mental. So dados PUBLICOS de ATO PUBLICO.

  5. O modelo e AUDITAVEL. Todo cidadao ve o score de toda
     autoridade. E ve COMO o score foi calculado (P13).

DADOS DE REFERENCIA 2024/2025 (publicos, verificaveis):

  - Subsidio de Deputado Federal 2024-2025: R$ 41.850,93/mes
    (teto do funcionalismo, reajuste de 6,78% em jan/2024 -- Lei 14.651/2023).
  - Subsidio de Senador 2024-2025: R$ 41.850,93/mes (mesmo teto).
  - Orçamento da Uniao 2024 (LOA, Lei 14.793/2024): R$ 578,6 bi autorizados.
  - Orçamento da Uniao 2025 (LOA, Lei 14.974/2024): R$ 616,3 bi autorizados.
  - Resolucao TSE 23.732/2024: PROIBE deepfakes e IA generativa para
    criar conteudo falso em campanhas eleitorais (municipais 2024).
  - Lei 14.960/2024 (minirreforma eleitoral): regras para uso de IA em
    campanhas, rotulagem obrigatoria, proibicao de deepfake.
  - Declaracao de Bens TSE 2024: patrimonio declarado em candidatura
    e publico no Sistema de Candidaturas (transparencia ativa).

OS 9 FATORES PREDITIVOS (baseados em padroes historicos reais):

  Cada fator tem peso. O score final e a soma ponderada.
  Quanto maior o score, maior o risco predito.

  F1. ACESSO A RECURSO (peso 10): controla orcamento grande?
      Quem controla muito dinheiro tem mais oportunidade.
      Prefeito de capital > vereador de cidade pequena.

  F2. REDE DE OBRIGACAO (peso 9): quantas nomeacoes fez?
      Quem deve cargo a alguem cria rede de obrigacao.
      Cada nomeacao e um no de lealdade (nao competencia).

  F3. PADRAO DE GASTO ANOMALO (peso 10): gastos fora de padrao?
      R$ 47k em restaurante. Cartao corporativo em combustivel
      de carro que nao e frota. Gasto noturno em local estranho.

  F4. PROXIMIDADE TEMPORAL COM LICITACAO (peso 9): reuniao
      com empresario do setor X seguida de licitacao de X?
      O monitor detecta depois. O preditor antecipa: se o
      padrao de reunioes-lavagem se repete, o risco sobe.

  F5. CONTINUIDADE NO PODER (peso 8): quantos mandatos?
      Mais de 3 mandatos = provavel rede estabelecida.
      O pessoalismo cresce. A rede se consolida.

  F6. OSCILACAO DE PATRIMONIO (peso 10): patrimonio cresceu
      mais que o salario permite? Declaracao de bens publica
      (P13) permite comparar. Salario de R$ 41,8k/mes (deputado
      2024-2025) mas patrimonio +R$ 5M em 4 anos = inexplicavel.

  F7. MANIPULACAO DE INFORMACAO (peso 8): bots, narrativa
      fabricada, militancia paga? O padrao de comunicacao
      revela estrategia de poder, nao apenas discurso.

  F8. OPACIDADE CRESCENTE (peso 7): recusas de transparencia
      estao aumentando? Politico que era transparente e ficou
      opaco esta escondendo algo (probabilidade, nao certeza).

  F9. INTELIGENCIA ARTIFICIAL E DEEPFAKE (peso 9 -- NOVO 2024):
      Usa deepfakes, IA generativa sem rotulagem, robos de IA
      para impulsionar desinformacao? Resolucao TSE 23.732/2024
      e Lei 14.960/2024 criminalizam. Eleicoes municipais 2024
      mostraram onda de deepfakes. Fator critico para 2026+.

COMO O SCORE FUNCIONA:

  Cada fator: 0 (sem risco) a 10 (risco maximo observavel).
  Score final = soma(peso * valor) / soma(pesos) * 10
  Range: 0-100.

  0-20  BAIXO    -- fiscalizacao rotineira
  21-40 MODERADO -- fiscalizacao ativa
  41-60 ALTO     -- auditoria prioritaria
  61-80 CRITICO  -- assembleia avalia continuidade
  81-100 PROIBITIVO -- suspenso ate auditoria completa

O QUE O MODELO NAO E:

  Nao e ML blackbox. Nao e sentença judicial.
  Nao e political reliability (historico).
  Nao e monitor (tempo real).
  E PREDICAO baseada em padroes transparentes.

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field
from collections import defaultdict
from datetime import datetime, timedelta
import math


# ============================================================================
# 1. ENUMS
# ============================================================================

class FatorPreditivo(Enum):
    """Os 8 fatores preditivos de risco politico."""
    F1_ACESSO_RECURSO = ("acesso_recurso", "Acesso a recurso publico (orcamento controlado)", 10)
    F2_REDE_OBRIGACAO = ("rede_obrigacao", "Rede de obrigacao (nomeacoes politicas)", 9)
    F3_GASTO_ANOMALO = ("gasto_anomalo", "Padrao de gasto anomalo (fora do esperado)", 10)
    F4_PROXIMIDADE_LICITACAO = ("prox_licitacao", "Proximidade temporal reuniao-licitacao", 9)
    F5_CONTINUIDADE_PODER = ("continuidade", "Continuidade no poder (mandatos sucessivos)", 8)
    F6_OSCILACAO_PATRIMONIO = ("oscilacao_patrim", "Oscilacao de patrimonio alem do salario", 10)
    F7_MANIPULACAO_INFO = ("manip_info", "Manipulacao de informacao (bots, narrativa)", 8)
    F8_OPACIDADE_CRESCENTE = ("opacidade", "Opacidade crescente (recusas de transparencia)", 7)
    F9_IA_DEEPFAKE = ("ia_deepfake", "IA generativa e deepfake (Res. TSE 23.732/2024)", 9)

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def peso(self) -> int:
        return self.value[2]


class NivelRisco(Enum):
    """Nivel de risco predito."""
    BAIXO = ("baixo", "Fiscalizacao rotineira", 0, 20)
    MODERADO = ("moderado", "Fiscalizacao ativa", 21, 40)
    ALTO = ("alto", "Auditoria prioritaria", 41, 60)
    CRITICO = ("critico", "Assembleia avalia continuidade", 61, 80)
    PROIBITIVO = ("proibitivo", "Suspenso ate auditoria completa", 81, 100)

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def score_min(self) -> int:
        return self.value[2]

    @property
    def score_max(self) -> int:
        return self.value[3]

    @classmethod
    def from_score(cls, score: float) -> "NivelRisco":
        for nivel in cls:
            if nivel.score_min <= score <= nivel.score_max:
                return nivel
        return cls.PROIBITIVO if score > 100 else cls.BAIXO


class TipoDadoPatrimonial(Enum):
    """Tipos de dado patrimonial para analise F6."""
    SALARIO_MENSAL = ("salario", "Salario bruto mensal do cargo")
    PATRIMONIO_INICIAL = ("pat_init", "Patrimonio declarado no inicio do mandato")
    PATRIMONIO_ATUAL = ("pat_atual", "Patrimonio declarado atualmente")
    OUTROS_RENDIMENTOS = ("outros_rend", "Outros rendimentos declarados")

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
class PerfilPolitico:
    """Perfil de um politico para analise preditiva."""
    id: str
    nome: str
    cargo: str
    # F1: acesso a recurso
    orcamento_controlado: float = 0.0  # R$ por ano
    # F2: rede de obrigacao
    nomeacoes_feitas: int = 0
    nomeacoes_competencia: int = 0  # quantas foram tecnicas (nao politicas)
    # F3: gasto anomalo
    gastos_anomalos: List[Tuple[str, float]] = field(default_factory=list)
    # (descricao, valor) de gastos suspeitos
    gasto_total_periodo: float = 0.0  # total gasto no periodo analisado
    # F4: proximidade temporal (do monitor)
    reunioes_antes_licitacao: int = 0  # quantas reunioes seguidas de licitacao
    # F5: continuidade
    mandatos: int = 1
    anos_no_poder: int = 0
    # F6: patrimonio
    salario_mensal: float = 0.0
    patrimonio_inicial: float = 0.0
    patrimonio_atual: float = 0.0
    outros_rendimentos_anuais: float = 0.0
    anos_mandato: int = 4  # duracao do mandato atual
    # F7: manipulacao de informacao
    incidencia_bots: int = 0  # contas suspeitas apoiando
    narrativas_fabricadas: int = 0  # narrativas desmentidas
    militancia_paga: bool = False
    # F8: opacidade crescente
    recusas_transparencia: int = 0
    era_transparente: bool = True  # era antes e deixou de ser?
    # F9: IA generativa e deepfake (NOVO 2024 -- Res. TSE 23.732/2024)
    deepfakes_criados: int = 0          # numero de deepfakes identificados
    ia_generativa_sem_rotulagem: int = 0  # usos de IA sem rotulagem obrigatoria
    robos_ia_desinformacao: int = 0    # robos automatizados impulsionando fake news
    ia_para_extorsao_ou_chantagem: bool = False  # IA usada para manipular adversario
    # metadata
    historico_reliability: float = 50.0  # score do political_reliability (0-100)


@dataclass
class FatorScore:
    """Score de um fator individual (transparencia)."""
    fator: FatorPreditivo
    valor: float        # 0-10
    peso: int
    contribuicao: float  # valor * peso / soma_pesos * 10
    justificativa: str   # explicacao humana-legivel


@dataclass
class PredicaoRisco:
    """Resultado completo da predicao de risco de um politico."""
    politico_id: str
    politico_nome: str
    cargo: str
    score_geral: float          # 0-100
    nivel: NivelRisco
    fatores: List[FatorScore] = field(default_factory=list)
    recomendacao: str = ""
    acao_audit: str = ""        # que auditoria priorizar
    timestamp: str = ""
    # disernmento explicito
    nao_e_condenacao: bool = True  # lembrete: score nao e culpa


# ============================================================================
# 3. ENGINE PREDITIVA
# ============================================================================

class PoliticalRiskPredictor:
    """
    Modelo preditivo de risco politico. Transparente. Auditavel.

    O modelo NAO condena. PRIORIZA auditoria.
    Cada score e explicavel por fator. Sem caixa-preta.
    """

    # escalas de orcamento (F1)
    ORCAMENTO_ALTO = 1_000_000_000   # R$ 1 bi+
    ORCAMENTO_MEDIO = 100_000_000    # R$ 100M+
    ORCAMENTO_BAIXO = 10_000_000     # R$ 10M+

    # limiares de patrimonio (F6)
    RENDA_ESPERADA_MULTIPLICADOR = 1.5  # patrimonio pode crescer ate 1.5x a renda total

    # DADOS DE REFERENCIA 2024/2025 (publicos, verificaveis)
    SUBSIDIO_DEPUTADO_2024 = 41850.93   # R$/mes -- teto do funcionalismo (Lei 14.651/2023)
    SUBSIDIO_DEPUTADO_2025 = 41850.93   # R$/mes -- mantido em 2025 (sem reajuste do teto)
    ORCAMENTO_UNIAO_2024 = 578_600_000_000.0   # R$ 578,6 bi (LOA, Lei 14.793/2024)
    ORCAMENTO_UNIAO_2025 = 616_300_000_000.0   # R$ 616,3 bi (LOA, Lei 14.974/2024)

    def __init__(self) -> None:
        self.perfis: Dict[str, PerfilPolitico] = {}

    def registrar(self, p: PerfilPolitico) -> None:
        self.perfis[p.id] = p

    # -- predicao -----------------------------------------------------------

    def prever(self, politico_id: str) -> PredicaoRisco:
        """Calcula score preditivo de risco para um politico."""
        p = self.perfis.get(politico_id)
        if p is None:
            return PredicaoRisco(
                politico_id=politico_id, politico_nome="?", cargo="?",
                score_geral=0, nivel=NivelRisco.BAIXO,
                recomendacao="Perfil nao encontrado.",
            )

        fatores: List[FatorScore] = []
        fatores.append(self._calc_f1_acesso_recurso(p))
        fatores.append(self._calc_f2_rede_obrigacao(p))
        fatores.append(self._calc_f3_gasto_anomalo(p))
        fatores.append(self._calc_f4_proximidade_licitacao(p))
        fatores.append(self._calc_f5_continuidade(p))
        fatores.append(self._calc_f6_oscilacao_patrimonio(p))
        fatores.append(self._calc_f7_manipulacao_info(p))
        fatores.append(self._calc_f8_opacidade_crescente(p))
        fatores.append(self._calc_f9_ia_deepfake(p))

        # score geral ponderado
        soma_pesos = sum(f.peso for f in fatores)
        score = sum(f.contribuicao for f in fatores)
        score_geral = min(100.0, score) if soma_pesos > 0 else 0.0
        nivel = NivelRisco.from_score(score_geral)

        # recomendacao baseada no nivel
        recomendacao, acao = self._gerar_recomendacao(nivel, fatores)

        return PredicaoRisco(
            politico_id=p.id, politico_nome=p.nome, cargo=p.cargo,
            score_geral=round(score_geral, 1), nivel=nivel,
            fatores=fatores, recomendacao=recomendacao,
            acao_audit=acao,
            timestamp=datetime.now().isoformat(),
        )

    # -- fatores individuais (cada um transparente) ------------------------

    def _fator(
        self, fator: FatorPreditivo, valor: float, justificativa: str,
        soma_pesos: int,
    ) -> FatorScore:
        """Cria um FatorScore com contribuicao calculada."""
        valor = max(0.0, min(10.0, valor))
        contrib = (valor * fator.peso / soma_pesos) * 10
        return FatorScore(
            fator=fator, valor=round(valor, 1), peso=fator.peso,
            contribuicao=round(contrib, 2),
            justificativa=justificativa,
        )

    SOMA_PESOS = sum(f.peso for f in FatorPreditivo)  # 80 (9 fatores)

    def _calc_f1_acesso_recurso(self, p: PerfilPolitico) -> FatorScore:
        """F1: Quanto orcamento controla."""
        orc = p.orcamento_controlado
        if orc >= self.ORCAMENTO_ALTO:
            valor = 10.0
            just = f"Controla R$ {orc/1e9:.1f} bi/ano. Acesso massivo a recurso."
        elif orc >= self.ORCAMENTO_MEDIO:
            valor = 7.0
            just = f"Controla R$ {orc/1e6:.0f} M/ano. Acesso significativo."
        elif orc >= self.ORCAMENTO_BAIXO:
            valor = 4.0
            just = f"Controla R$ {orc/1e6:.0f} M/ano. Acesso moderado."
        else:
            valor = 1.0
            just = f"Controla R$ {orc/1e3:.0f} k/ano. Acesso limitado."
        return self._fator(FatorPreditivo.F1_ACESSO_RECURSO, valor, just, self.SOMA_PESOS)

    def _calc_f2_rede_obrigacao(self, p: PerfilPolitico) -> FatorScore:
        """F2: Rede de nomeacoes politicas."""
        if p.nomeacoes_feitas == 0:
            valor = 0.0
            just = "Nenhuma nomeacao. Sem rede de obrigacao."
        else:
            pct_politica = 1.0 - (p.nomeacoes_competencia / p.nomeacoes_feitas)
            if pct_politica > 0.7:
                valor = 9.0
                just = (f"{p.nomeacoes_feitas} nomeacoes, "
                        f"{pct_politica:.0%} politicas. Rede de obrigacao densa.")
            elif pct_politica > 0.4:
                valor = 6.0
                just = (f"{p.nomeacoes_feitas} nomeacoes, "
                        f"{pct_politica:.0%} politicas. Rede moderada.")
            else:
                valor = 3.0
                just = (f"{p.nomeacoes_feitas} nomeacoes, "
                        f"{pct_politica:.0%} politicas. Maioria tecnica.")
        return self._fator(FatorPreditivo.F2_REDE_OBRIGACAO, valor, just, self.SOMA_PESOS)

    def _calc_f3_gasto_anomalo(self, p: PerfilPolitico) -> FatorScore:
        """F3: Padrao de gasto anomalo."""
        if not p.gastos_anomalos:
            valor = 0.0
            just = "Nenhum gasto anomalo registrado."
        else:
            total_anomalo = sum(v for _, v in p.gastos_anomalos)
            pct = (total_anomalo / p.gasto_total_periodo * 100
                   if p.gasto_total_periodo > 0 else 100)
            num = len(p.gastos_anomalos)
            if pct > 20 or num > 5:
                valor = 10.0
                just = (f"{num} gastos anomalos totalizando R$ {total_anomalo:,.0f} "
                        f"({pct:.0f}% do periodo). Padrao grave.")
            elif pct > 5 or num > 2:
                valor = 7.0
                just = (f"{num} gastos anomalos (R$ {total_anomalo:,.0f}, "
                        f"{pct:.0f}%). Padrao suspeito.")
            else:
                valor = 4.0
                just = f"{num} gasto(s) anomalo(s). Isolado, mas observar."
        return self._fator(FatorPreditivo.F3_GASTO_ANOMALO, valor, just, self.SOMA_PESOS)

    def _calc_f4_proximidade_licitacao(self, p: PerfilPolitico) -> FatorScore:
        """F4: Proximidade temporal reuniao-licitacao."""
        n = p.reunioes_antes_licitacao
        if n >= 5:
            valor = 10.0
            just = f"{n} reunioes com empresarios seguidas de licitacao. Padrao sistemico."
        elif n >= 3:
            valor = 7.0
            just = f"{n} reunioes-licitacao. Padrao recorrente."
        elif n >= 1:
            valor = 4.0
            just = f"{n} reuniao(oes)-licitacao. Investigar."
        else:
            valor = 0.0
            just = "Nenhuma reuniao antes de licitacao detectada."
        return self._fator(FatorPreditivo.F4_PROXIMIDADE_LICITACAO, valor, just, self.SOMA_PESOS)

    def _calc_f5_continuidade(self, p: PerfilPolitico) -> FatorScore:
        """F5: Continuidade no poder."""
        m = p.mandatos
        a = p.anos_no_poder
        if m >= 4 or a >= 16:
            valor = 10.0
            just = f"{m} mandatos ({a} anos). Perpetuacao. Rede consolidada."
        elif m >= 3 or a >= 10:
            valor = 7.0
            just = f"{m} mandatos ({a} anos). Risco de enraizamento."
        elif m >= 2:
            valor = 4.0
            just = f"{m} mandatos ({a} anos). Observar."
        else:
            valor = 1.0
            just = f"{m} mandato ({a} anos). Sem continuidade excessiva."
        return self._fator(FatorPreditivo.F5_CONTINUIDADE_PODER, valor, just, self.SOMA_PESOS)

    def _calc_f6_oscilacao_patrimonio(self, p: PerfilPolitico) -> FatorScore:
        """F6: Patrimonio cresceu alem do salario?"""
        renda_total = (p.salario_mensal * 12 * p.anos_mandato
                       + p.outros_rendimentos_anuais * p.anos_mandato)
        crescimento = p.patrimonio_atual - p.patrimonio_inicial
        if renda_total <= 0:
            valor = 5.0
            just = "Dados de renda insuficientes. Nao e possivel avaliar."
            return self._fator(FatorPreditivo.F6_OSCILACAO_PATRIMONIO, valor, just, self.SOMA_PESOS)

        razao = crescimento / renda_total if renda_total > 0 else 0
        if crescimento <= 0:
            valor = 0.0
            just = "Patrimonio nao cresceu. Conforme."
        elif razao <= self.RENDA_ESPERADA_MULTIPLICADOR:
            valor = 2.0
            just = (f"Crescimento R$ {crescimento:,.0f} dentro da renda "
                    f"(razao {razao:.1f}x). Conforme.")
        elif razao <= 3.0:
            valor = 6.0
            just = (f"Crescimento R$ {crescimento:,.0f} eh {razao:.1f}x a renda. "
                    f"Investigar origem.")
        else:
            valor = 10.0
            just = (f"Crescimento R$ {crescimento:,.0f} eh {razao:.1f}x a renda "
                    f"total de R$ {renda_total:,.0f}. INEXPLICAVEL pelo salario.")
        return self._fator(FatorPreditivo.F6_OSCILACAO_PATRIMONIO, valor, just, self.SOMA_PESOS)

    def _calc_f7_manipulacao_info(self, p: PerfilPolitico) -> FatorScore:
        """F7: Manipulacao de informacao."""
        score = 0.0
        notas: List[str] = []
        if p.incidencia_bots >= 100:
            score += 4.0
            notas.append(f"{p.incidencia_bots} contas suspeitas apoiando")
        elif p.incidencia_bots >= 20:
            score += 2.0
            notas.append(f"{p.incidencia_bots} contas suspeitas")
        if p.narrativas_fabricadas >= 3:
            score += 3.0
            notas.append(f"{p.narrativas_fabricadas} narrativas desmentidas")
        elif p.narrativas_fabricadas >= 1:
            score += 1.5
            notas.append(f"{p.narrativas_fabricadas} narrativa desmentida")
        if p.militancia_paga:
            score += 3.0
            notas.append("militancia paga confirmada")
        valor = min(10.0, score)
        just = "; ".join(notas) if notas else "Sem indicadores de manipulacao."
        return self._fator(FatorPreditivo.F7_MANIPULACAO_INFO, valor, just, self.SOMA_PESOS)

    def _calc_f8_opacidade_crescente(self, p: PerfilPolitico) -> FatorScore:
        """F8: Opacidade crescente."""
        if p.recusas_transparencia == 0:
            valor = 0.0
            just = "Nenhuma recusa de transparencia."
        elif not p.era_transparente:
            # sempre foi opaco
            valor = min(10.0, 3.0 + p.recusas_transparencia)
            just = f"{p.recusas_transparencia} recusas. Sempre opaco."
        else:
            # ERA transparente e ficou opaco = pior sinal
            valor = min(10.0, 5.0 + p.recusas_transparencia)
            just = (f"{p.recusas_transparencia} recusas. ERA transparente e ficou opaco. "
                    f"Mudanca de padrao = forte indicador.")
        return self._fator(FatorPreditivo.F8_OPACIDADE_CRESCENTE, valor, just, self.SOMA_PESOS)

    def _calc_f9_ia_deepfake(self, p: PerfilPolitico) -> FatorScore:
        """F9: IA generativa e deepfake (Res. TSE 23.732/2024, Lei 14.960/2024).

        Eleicoes municipais 2024 mostraram onda de deepfakes. O TSE proibiu
        uso de IA generativa para criar conteudo falso. Quem usa opera na
        ilegalidade. Risco altissimo -- e fator novo, critico para 2026+.
        """
        score = 0.0
        notas: List[str] = []

        if p.deepfakes_criados >= 3:
            score += 6.0
            notas.append(f"{p.deepfakes_criados} deepfakes identificados (PADRAO SISTEMICO)")
        elif p.deepfakes_criados >= 1:
            score += 4.0
            notas.append(f"{p.deepfakes_criados} deepfake identificado")

        if p.ia_generativa_sem_rotulagem >= 5:
            score += 3.0
            notas.append(f"{p.ia_generativa_sem_rotulagem} usos de IA sem rotulagem (Lei 14.960/2024)")
        elif p.ia_generativa_sem_rotulagem >= 1:
            score += 1.5
            notas.append(f"{p.ia_generativa_sem_rotulagem} uso(s) de IA sem rotulagem")

        if p.robos_ia_desinformacao >= 50:
            score += 3.0
            notas.append(f"{p.robos_ia_desinformacao} robos de IA impulsionando desinformacao")
        elif p.robos_ia_desinformacao >= 10:
            score += 1.5
            notas.append(f"{p.robos_ia_desinformacao} robos de IA")

        if p.ia_para_extorsao_ou_chantagem:
            score += 4.0
            notas.append("IA usada para extorsao/chantagem (GRAVISSIMO)")

        valor = min(10.0, score)
        just = "; ".join(notas) if notas else (
            "Sem indicadores de deepfake ou IA generativa ilicita (Res. TSE 23.732/2024)."
        )
        return self._fator(FatorPreditivo.F9_IA_DEEPFAKE, valor, just, self.SOMA_PESOS)

    # -- recomendacao -------------------------------------------------------

    def _gerar_recomendacao(
        self, nivel: NivelRisco, fatores: List[FatorScore],
    ) -> Tuple[str, str]:
        """Gera recomendacao e acao de auditoria baseadas no nivel e fatores."""
        rec = {
            NivelRisco.BAIXO: "Fiscalizacao rotineira. Sem acao prioritaria.",
            NivelRisco.MODERADO: "Fiscalizacao ativa. Monitorar padroes.",
            NivelRisco.ALTO: "Auditoria prioritaria recomendada.",
            NivelRisco.CRITICO: "Assembleia deve avaliar continuidade no cargo.",
            NivelRisco.PROIBITIVO: "SUSPENDO ate auditoria completa. Risco muito alto.",
        }
        recomendacao = rec.get(nivel, "Avaliar.")

        # identificar os 2 fatores mais altos pra priorizar auditoria
        top2 = sorted(fatores, key=lambda f: f.contribuicao, reverse=True)[:2]
        prioridades = [f"{f.fator.id} ({f.valor}/10)" for f in top2]
        acao = f"Auditoria focar em: {', '.join(prioridades)}."
        return recomendacao, acao

    # -- comparacao ---------------------------------------------------------

    def ranking_risco(self) -> List[PredicaoRisco]:
        """Retorna todos os politicos ordenados por risco (maior primeiro)."""
        preds = [self.prever(pid) for pid in self.perfis]
        return sorted(preds, key=lambda p: p.score_geral, reverse=True)

    def prever_todos(self) -> Dict[str, Any]:
        preds = self.ranking_risco()
        return {
            "total": len(preds),
            "baixo": sum(1 for p in preds if p.nivel == NivelRisco.BAIXO),
            "moderado": sum(1 for p in preds if p.nivel == NivelRisco.MODERADO),
            "alto": sum(1 for p in preds if p.nivel == NivelRisco.ALTO),
            "critico": sum(1 for p in preds if p.nivel == NivelRisco.CRITICO),
            "proibitivo": sum(1 for p in preds if p.nivel == NivelRisco.PROIBITIVO),
            "ranking": [
                {
                    "nome": p.politico_nome, "cargo": p.cargo,
                    "score": p.score_geral, "nivel": p.nivel.id,
                    "acao": p.acao_audit,
                }
                for p in preds
            ],
        }

    def scorecard(self) -> Dict[str, Any]:
        return {
            "politicos_analisados": len(self.perfis),
            "fatores_preditivos": len(list(FatorPreditivo)),
            "soma_pesos": self.SOMA_PESOS,
            "niveis_risco": len(list(NivelRisco)),
            "modelo": "transparente (regras com peso visivel, nao ML)",
            "limite_etico": "Score nao e condenacao. E priorizacao de auditoria.",
        }


# ============================================================================
# 4. DEMO
# ============================================================================

def _demo() -> None:
    pred = PoliticalRiskPredictor()

    print("=" * 70)
    print("OpenPoliticalRiskPredictor -- Antecipacao Preditiva Transparente")
    print("=" * 70)

    # --- Os 8 fatores ---
    print(f"\n[OS {len(list(FatorPreditivo))} FATORES PREDITIVOS]")
    print("  (cada fator tem peso. Score = soma ponderada. 0-100.)")
    for f in FatorPreditivo:
        print(f"\n  {f.id} (peso {f.peso}) -- {f.rotulo}")

    # --- Cenarios ---
    print("\n\n[CENARIOS DE PREDICAO]")

    # Cenario A: politico limpo (salario de vereador 2024)
    pred.registrar(PerfilPolitico(
        id="limpo", nome="Vereadora Ana (perfil limpo)",
        cargo="Vereadora", orcamento_controlado=5_000_000,
        nomeacoes_feitas=2, nomeacoes_competencia=2,
        mandatos=1, anos_no_poder=2,
        salario_mensal=8000, patrimonio_inicial=200000,
        patrimonio_atual=280000, anos_mandato=2,
        deepfakes_criados=0, ia_generativa_sem_rotulagem=0, robos_ia_desinformacao=0,
    ))

    # Cenario B: politico com padrao suspeito (salario de prefeito capital 2024)
    pred.registrar(PerfilPolitico(
        id="suspeito", nome="Prefeito Bruno (padrao suspeito)",
        cargo="Prefeito", orcamento_controlado=500_000_000,
        nomeacoes_feitas=45, nomeacoes_competencia=10,
        gastos_anomalos=[
            ("Restaurante noturno", 47000),
            ("Combustivel carro particular", 12000),
            ("Hotel fuera ciudad", 8000),
        ],
        gasto_total_periodo=200000,
        reunioes_antes_licitacao=4,
        mandatos=3, anos_no_poder=12,
        salario_mensal=18000, patrimonio_inicial=300000,
        patrimonio_atual=5000000, outros_rendimentos_anuais=0,
        anos_mandato=4,
        incidencia_bots=150, narrativas_fabricadas=4,
        militancia_paga=True,
        recusas_transparencia=3, era_transparente=True,
        # F9 (2024): 2 deepfakes + IA sem rotulagem + robos
        deepfakes_criados=2, ia_generativa_sem_rotulagem=6,
        robos_ia_desinformacao=30,
    ))

    # Cenario C: politico critico (estilo caso real, salario de governador 2024)
    pred.registrar(PerfilPolitico(
        id="critico", nome="Governador Carlos (risco critico)",
        cargo="Governador", orcamento_controlado=30_000_000_000,
        nomeacoes_feitas=200, nomeacoes_competencia=30,
        gastos_anomalos=[
            ("Jato particular", 800000),
            ("Mansao fora declaracao", 2000000),
            ("Restaurante", 47000),
            ("Combustivel", 25000),
        ],
        gasto_total_periodo=5000000,
        reunioes_antes_licitacao=8,
        mandatos=4, anos_no_poder=16,
        salario_mensal=30000, patrimonio_inicial=500000,
        patrimonio_atual=25000000, anos_mandato=4,
        incidencia_bots=500, narrativas_fabricadas=10,
        militancia_paga=True,
        recusas_transparencia=7, era_transparente=True,
        # F9 (2024): campanha sistemica de deepfakes (Res. TSE 23.732/2024)
        deepfakes_criados=5, ia_generativa_sem_rotulagem=12,
        robos_ia_desinformacao=80,
        ia_para_extorsao_ou_chantagem=True,
    ))

    # --- Predicoes ---
    for pid in ["limpo", "suspeito", "critico"]:
        r = pred.prever(pid)
        print(f"\n{'='*60}")
        print(f"{r.politico_nome}")
        print(f"  Cargo: {r.cargo}")
        print(f"  SCORE: {r.score_geral}/100 -- {r.nivel.id.upper()} ({r.nivel.rotulo})")
        print(f"  Recomendacao: {r.recomendacao}")
        print(f"  Auditoria: {r.acao_audit}")
        print(f"\n  FATORES (transparentes):")
        for f in r.fatores:
            bar = "#" * int(f.valor)
            print(f"    {f.fator.id:<20} [{bar:<10}] {f.valor:>4}/10 "
                  f"(peso {f.peso}, contrib {f.contribuicao})")
            print(f"    {'':<22} {f.justificativa}")

    # --- Ranking ---
    print(f"\n{'='*60}")
    print("[RANKING DE RISCO (transparencia radical -- P13)]")
    ranking = pred.prever_todos()
    for i, r in enumerate(ranking["ranking"], 1):
        print(f"  {i}. {r['nome']:<40} {r['score']:>5}/100  {r['nivel'].upper()}")
    print(f"\n  Total: {ranking['total']} | Baixo: {ranking['baixo']} | "
          f"Moderado: {ranking['moderado']} | Alto: {ranking['alto']} | "
          f"Critico: {ranking['critico']} | Proibitivo: {ranking['proibitivo']}")

    # --- Scorecard ---
    print(f"\n[SCORECARD]")
    sc = pred.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<32} {v}")

    # --- Filosofia ---
    print(f"\n{'='*70}")
    print("FILOSOFIA -- Prever nao e condenar")
    print("=" * 70)
    print("""
O MODELO PREDITIVO:

  O modelo olha para o padrao ATUAL e estima risco FUTURO.
  O politico ainda nao fez merda. Mas o padrao de comportamento
  se parece com o padro de quem DEPOIS fez.

  O modelo aponta. A assembleia decide.

O LIMITE ETICO (duro):

  1. Score alto nao e CONDENACAO. E ATENCAO.
     "Esta pessoa merece mais fiscalizacao porque o padrao
     se parece com o de quem depois fez merda."

  2. O modelo e TRANSPARENTE (P5). Cada score e explicavel
     por fator. Sem caixa-preta. Sem ML opaco.
     Regras com peso visivel, dado mensuravel, justificacao.

  3. O modelo e REVERSIVEL. Se o dado muda, o score muda.
     Politico que melhora ve score cair.
     Politico que piora ve score subir.
     Nao e marcacao eterna. E PADRAO atual.

  4. O modelo NAO usa dados intimos (P2). Nao analisa
     sexualidade, religiao, saude mental.
     So dados PUBLICOS de ATO PUBLICO.

  5. O modelo e AUDITAVEL. Todo cidadao ve o score de toda
     autoridade. E ve COMO foi calculado (P13).

POR QUE NAO ML OPACO:

  ML blackbox (redes neurais) nao e auditavel. Nao da pra
  explicar POR QUE o score e alto. O cidadao nao pode
  contestar um numero que ninguem sabe de onde veio.

  A Republica usa REGRAS TRANSPARENTES. Cada fator tem:
  - O QUE mediu
  - QUEM peso tem
  - POR QUE contribuiu

  Se o cidadao nao concorda, pode ver o calculo e contestar.
  ML opaco nao permite contestacao. E anti-democratico (P4).

OS 9 FATORES (com base em padroes historicos reais):

  F1. ACESSO A RECURSO: controla orcamento grande.
  F2. REDE DE OBRIGACAO: nomeou muita gente politica.
  F3. GASTO ANOMALO: padrao de gasto fora do normal.
  F4. PROXIMIDADE LICITACAO: reunioes antes de licitacao.
  F5. CONTINUIDADE: mandatos sucessivos.
  F6. PATRIMONIO: cresceu alem do salario.
  F7. MANIPULACAO INFO: bots, narrativa fabricada.
  F8. OPACIDADE: recusas de transparencia crescentes.
  F9. IA/DEEPFAKE: uso de deepfakes e IA generativa ilicita (NOVO 2024).

DADOS DE REFERENCIA 2024/2025:

  - Subsidio de deputado/senador: R$ 41.850,93/mes (teto).
  - Orcamento da Uniao 2024: R$ 578,6 bi. 2025: R$ 616,3 bi.
  - Res. TSE 23.732/2024 e Lei 14.960/2024: proibem deepfake e IA sem rotulagem.

A DIFERENCA DOS 3 MODULOS:

  political_reliability: olha pra TRAS (historico).
  constitutional_monitor: detecta AGORA (tempo real).
  political_risk_predictor: antecipa DEPOIS (predicao).

  Os 3 juntos formam VIGILANCIA REPROCIPCA COMPLETA:
  passado + presente + futuro. Tudo transparente.
  Tudo auditavel. Tudo contestavel.
""")


if __name__ == "__main__":
    _demo()
