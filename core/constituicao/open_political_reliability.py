#!/usr/bin/env python3
"""
OpenPoliticalReliability -- Simulacao de Confiabilidade do Sujeito Politico
=============================================================================
"O poder nao se mede pela quantidade de votos, mas pela qualidade do processo."

A Republica NAO confia em sujeitos politicos. Confia em PROCESSOS.
Mas para AUDITAR processos, precisa avaliar a CONFIABILIDADE dos sujeitos
que operam dentro deles.

Este modulo e um SIMULADOR de confiabilidade politica. NAO e tribunal.
NAO condena. AVALIA com base em indicadores verificaveis e produz um
SCORE de confiabilidade que a assembleia pode usar para decidir se um
sujeito pode operar dentro das instituicoes da Republica.

PRINCIPIO (P4): A transparencia e radical. Se um sujeito opera no poder,
todo seu historico e auditavel. Nao existe "privacidade politica" para
quem exerce poder publico -- poder publico e PUBLICO.

O QUE O SIMULADOR MEDE:
1. USO DE APARELHO PUBLICO para beneficio eleitoral
2. COMPRA DE VOTO (clientelismo, bolsa, promessa)
3. CONTINUIDADE NO PODER (quantos mandatos, indicio de perpetuacao)
4. DESMANCHE DE ALTERNATIVAS (impede novas candidaturas no proprio campo)
5. CORRUPCAO SISTEMICA (e caso isolado ou padrao?)
6. MANIPULACAO DE INFORMACAO (bots, redes, narrativa fabricada)
7. TRANSPARENCIA (abre dados ou esconde?)
8. RENOVACAO DE ELITES (treina sucessores ou se torna insubstituivel?)

ALINHAMENTO CONSTITUCIONAL:
- P1: Confianca politica nao heranca. Cada mandato auditado.
- P4: Democracia radical exige sujeitos confiaveis. Processo corrompido = vitro eleitoral.
- P9: Sujeito que polariza para perpetuar VIOLA o P9 (Estado nao polariza).

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field
from collections import defaultdict
from datetime import datetime


# ============================================================================
# 1. ENUMS (modulo-level)
# ============================================================================

class TipoIndicador(Enum):
    """Dimensoes de avaliacao da confiabilidade politica."""
    USO_APARELHO_PUBLICO = ("uso_aparelho", "Uso de aparelho de Estado para fim eleitoral", 10)
    COMPRA_VOTO = ("compra_voto", "Compra de voto / clientelismo / bolsa-eleicao", 10)
    CONTINUIDADE_PODER = ("continuidade", "Perpetuacao no poder (mandatos sucessivos)", 8)
    DESMANCHE_ALTERNATIVAS = ("desmanche", "Desmanche de novas candidaturas no proprio campo", 7)
    CORRUPCAO_SISTEMICA = ("corrupcao", "Corrupcao sistemica (padrao, nao caso isolado)", 10)
    MANIPULACAO_INFORMACAO = ("manipulacao_info", "Manipulacao de informacao (bots, narrativa fabricada)", 8)
    OPACIDADE = ("opacidade", "Falta de transparencia / esconda dados publicos", 6)
    PERSONALISMO = ("personalismo", "Personalismo (se torna insubstituivel, sem sucessor)", 7)
    VIOLACAO_PRINCIPIOS = ("violacao_principios", "Violacao de principios constitucionais", 9)
    MILITANCIA_FINANCEIRA = ("militancia_fin", "Militancia comprada (cargo em troca de apoio)", 7)
    MIGALHA_DIGITAL = ("migalha_digital", "Exercito de migalhas: militancia online paga com esmola digital", 9)
    MISERIA_DEPENDENCIA = ("miseria_dep", "Miseria como ferramenta: manter na miseria para manter dependente", 10)
    PERSECUICAO_JUDICIAL = ("persecucao_judicial", "Perseguicao judicial ilicita / preso politico em quarentena", 9)

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def peso(self) -> int:
        """Peso do indicador no score (1-10, 10=maximo impacto negativo)."""
        return self.value[2]


class NivelConfiabilidade(Enum):
    """Niveis de confiabilidade politica do sujeito."""
    CONFIGAVEL = ("confiavel", "Confiavel: sem indicadores graves, processo transparente", 100, 80)
    ACEITAVEL = ("aceitavel", "Aceitavel: indicadores leves, monitorar", 79, 60)
    PREOCUPANTE = ("preocupante", "Preocupante: multiplos indicadores, assembleia avalia", 59, 40)
    ALTO_RISCO = ("alto_risco", "Alto risco: padrao de manipulacao sistêmica", 39, 20)
    INACEITAVEL = ("inaceitavel", "Inaceitavel: processo corrompido, nao opera na Republica", 19, 0)

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def score_max(self) -> int:
        return self.value[2]

    @property
    def score_min(self) -> int:
        return self.value[3]


class MetodoManipulacao(Enum):
    """Metodos de manipulacao do processo politico."""
    BOTS_REDES = ("bots_redes", "Bots e operacao de redes sociais")
    APARELHO_ELEITORAL = ("aparelho_eleitoral", "Maquina publica a servico de candidatura")
    CLIENTELISMO = ("clientelismo", "Troca de beneficio por voto")
    CARGOS_TROCA = ("cargos_troca", "Distribuicao de cargos em troca de apoio")
    NARRATIVA_FABRICADA = ("narrativa_fabricada", "Construcao de narrativa falsa")
    IMPEDIR_CANDIDATURA = ("impedir_candidatura", "Impedir surgimento de novas candidaturas")
    JUDICIALIZACAO_ARMA = ("judicializacao_arma", "Usar sistema judicial contra oponentes")
    MIDIA_COMPRADA = ("midia_comprada", "Comprar cobertura midiatica")
    FINANCIAMENTO_OCULTO = ("financiamento_oculto", "Caixa 2 / financiamento nao declarado")
    MEDO_E_AMEACA = ("medo_ameaca", "Gerar medo na populacao para colher votos")
    MIGALHA_SOCIAL = ("migalha_social", "Esmola digital/migalha em troca de militancia online")
    PRESO_QUARENTENA = ("preso_quarentena", "Manter oponente preso em quarentena judicial sem sentenca")
    ARMADILHA_JUDICIAL = ("armadilha_judicial", "Construir caso judicial com meios ilicitos")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class GraveEvidencia(Enum):
    """Grau de evidencia de um indicador (principio: sem provas nao condena)."""
    COMPROVADO_JUDICIAL = ("comprovado_judicial", "Comprovado judicialmente (sentenca transitada)", 1.0)
    INVESTIGACAO_OFICIAL = ("investigacao_oficial", "Investigacao oficial em curso", 0.7)
    EVIDENCIA_JORNALISTICA = ("evidencia_jornalistica", "Evidencia jornalistica consistente", 0.6)
    INDICIO_FORTE = ("indicio_forte", "Indicio forte (multiplos sinais convergentes)", 0.5)
    DENUNCIA = ("denuncia", "Denuncia formal sem comprovacao", 0.3)
    SUSPEITA = ("suspeita", "Suspeita / opiniao publica sem comprovacao", 0.1)

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def fator_confianca(self) -> float:
        """Quanto este grau de evidencia contribui (0-1). Sem prova, nao condena."""
        return self.value[2]


class StatusVeredito(Enum):
    """Veredito da simulacao de confiabilidade."""
    APROVADO = ("aprovado", "Sujeito pode operar na Republica")
    MONITORAR = ("monitorar", "Pode operar com monitoramento continuo")
    RESTRITO = ("restrito", "Operacao restrita (sem cargo de poder decisiorio)")
    SUSPEITO = ("suspeito", "Suspeito: assembleia decide caso a caso")
    VETADO = ("vetado", "Vetado: processo corrompido, nao exerce poder na Republica")

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
class IndicadorPolitico:
    """Um indicador de (in)confiabilidade do sujeito politico."""
    tipo: TipoIndicador
    descricao: str
    grau_evidencia: GraveEvidencia
    ocorrencias: int = 1          # quantas vezes detectado
    periodo: str = ""             # "2003-2022", "eleicao 2022", etc.
    metodos: List[MetodoManipulacao] = field(default_factory=list)
    detalhe: str = ""


@dataclass
class EventoPolitico:
    """Um evento verificavel na trajetoria do sujeito."""
    id: str
    ano: str
    descricao: str
    tipo: str                     # "eleicao", "investigacao", "denuncia", "politica publica"
    impacto_confiabilidade: int = 0  # -10 a +10 (negativo=reduz, positivo=aumenta)
    evidencia: GraveEvidencia = GraveEvidencia.SUSPEITA


@dataclass
class AvaliacaoConfiabilidade:
    """Resultado completo da avaliacao de um sujeito politico."""
    sujeito: str
    cargo: str
    mandatos: int
    score: int                    # 0-100 (100=maxima confiabilidade)
    nivel: NivelConfiabilidade
    veredito: StatusVeredito
    indicadores: List[IndicadorPolitico] = field(default_factory=list)
    pontos_forte: List[str] = field(default_factory=list)
    pontos_fraco: List[str] = field(default_factory=list)
    recomendacoes: List[str] = field(default_factory=list)
    justificativa: str = ""


@dataclass
class SimulacaoCenario:
    """Simulacao de cenario: o que acontece se o sujeito continuar no poder."""
    cenario: str
    probabilidade_pct: float      # 0-100
    impacto_democracia: str       # descricao do impacto no processo democratico
    impacto_republica: str        # descricao do impacto se integrar a Republica
    acao_recomendada: str = ""


# ============================================================================
# 3. ENGINE
# ============================================================================

class ConfiabilidadeEngine:
    """Motor de simulacao de confiabilidade politica."""

    def __init__(self) -> None:
        self.eventos: List[EventoPolitico] = []
        self._ev_id = 0

    def _ev_novo_id(self) -> str:
        self._ev_id += 1
        return f"EV-{self._ev_id:04d}"

    def registrar_evento(
        self,
        ano: str,
        descricao: str,
        tipo: str,
        impacto: int = 0,
        evidencia: GraveEvidencia = GraveEvidencia.SUSPEITA,
    ) -> EventoPolitico:
        ev = EventoPolitico(
            id=self._ev_novo_id(),
            ano=ano,
            descricao=descricao,
            tipo=tipo,
            impacto_confiabilidade=impacto,
            evidencia=evidencia,
        )
        self.eventos.append(ev)
        return ev

    # -- avaliacao ---------------------------------------------------------

    def avaliar(
        self,
        sujeito: str,
        cargo: str,
        mandatos: int,
        indicadores: List[IndicadorPolitico],
        eventos: Optional[List[EventoPolitico]] = None,
    ) -> AvaliacaoConfiabilidade:
        """
        Avalia a confiabilidade de um sujeito politico.
        Score comeca em 100 e cada indicador REDUZ proporcionalmente.
        """
        score = 100
        pontos_fraco: List[str] = []
        pontos_forte: List[str] = []

        for ind in indicadores:
            # penalidade = peso do indicador * fator de evidencia * sqrt(ocorrencias)
            import math
            penalidade = ind.tipo.peso * ind.grau_evidencia.fator_confianca * math.sqrt(ind.ocorrencias)
            penalidade = min(penalidade, 25)  # teto por indicador
            score -= penalidade
            pontos_fraco.append(
                f"[{ind.tipo.rotulo}] {ind.descricao} "
                f"(evidencia: {ind.grau_evidencia.rotulo}, ocorrencias: {ind.ocorrencias})"
            )

        # penalidade por perpetuacao
        if mandatos >= 4:
            score -= 10
            pontos_fraco.append(f"Perpetuacao: {mandatos} mandatos (risco de insubstituibilidade).")
        elif mandatos >= 3:
            score -= 5
            pontos_fraco.append(f"Continuidade: {mandatos} mandatos (monitorar renovacao).")

        # eventos adicionais (se houver)
        if eventos:
            for ev in eventos:
                if ev.impacto_confiabilidade < 0:
                    score += ev.impacto_confiabilidade  # impacto negativo reduz score
                    pontos_fraco.append(f"{ev.ano}: {ev.descricao} ({ev.evidencia.rotulo})")
                elif ev.impacto_confiabilidade > 0:
                    score = min(100, score + ev.impacto_confiabilidade)
                    pontos_forte.append(f"{ev.ano}: {ev.descricao}")

        score = max(0, min(100, int(round(score))))

        # classificar nivel
        nivel = self._classificar_nivel(score)

        # veredito
        veredito = self._veredito_por_nivel(nivel, mandatos)

        # recomendacoes
        recomendacoes = self._gerar_recomendacoes(indicadores, nivel, mandatos)

        # justificativa
        justificativa = self._gerar_justificativa(sujeito, score, nivel, indicadores, mandatos)

        return AvaliacaoConfiabilidade(
            sujeito=sujeito,
            cargo=cargo,
            mandatos=mandatos,
            score=score,
            nivel=nivel,
            veredito=veredito,
            indicadores=indicadores,
            pontos_forte=pontos_forte,
            pontos_fraco=pontos_fraco,
            recomendacoes=recomendacoes,
            justificativa=justificativa,
        )

    def _classificar_nivel(self, score: int) -> NivelConfiabilidade:
        for n in NivelConfiabilidade:
            if n.score_min <= score <= n.score_max:
                return n
        return NivelConfiabilidade.INACEITAVEL

    def _veredito_por_nivel(self, nivel: NivelConfiabilidade, mandatos: int) -> StatusVeredito:
        if nivel == NivelConfiabilidade.CONFIGAVEL:
            return StatusVeredito.APROVADO
        if nivel == NivelConfiabilidade.ACEITAVEL:
            return StatusVeredito.MONITORAR
        if nivel == NivelConfiabilidade.PREOCUPANTE:
            return StatusVeredito.RESTRITO
        if nivel == NivelConfiabilidade.ALTO_RISCO:
            return StatusVeredito.SUSPEITO
        return StatusVeredito.VETADO

    def _gerar_recomendacoes(
        self, indicadores: List[IndicadorPolitico], nivel: NivelConfiabilidade, mandatos: int
    ) -> List[str]:
        recs: List[str] = []
        # verificar se ha uso de aparelho publico
        tipos_ativos = {ind.tipo for ind in indicadores}
        if TipoIndicador.USO_APARELHO_PUBLICO in tipos_ativos:
            recs.append("Auditar uso de recursos publicos em periodo eleitoral (OpenPublicAudit).")
        if TipoIndicador.COMPRA_VOTO in tipos_ativos:
            recs.append("Implementar OpenVoteIntegrity: rastrear fluxo de beneficios antes de eleicao.")
        if TipoIndicador.MANIPULACAO_INFORMACAO in tipos_ativos:
            recs.append("Auditar bots e operacao de redes (P9: Estado nao polariza via algoritmo).")
        if TipoIndicador.DESMANCHE_ALTERNATIVAS in tipos_ativos:
            recs.append("Proteger pluralismo interno: assembleia garante direito a candidatura alternativa.")
        if TipoIndicador.PERSONALISMO in tipos_ativos or mandatos >= 3:
            recs.append("Exigir plano de successao: sujeito treina substituto ou nao exerce novo mandato.")
        if TipoIndicador.CORRUPCAO_SISTEMICA in tipos_ativos:
            recs.append("Investigacao independente (OpenJudicialAudit) antes de qualquer integracao.")
        if TipoIndicador.MIGALHA_DIGITAL in tipos_ativos:
            recs.append("Rastrear fluxo de pagamentos digitais a militancia online (OpenDigitalTrace). "
                        "Exercito de migalhas = trabalho escravo emocional, nao militancia.")
        if TipoIndicador.MISERIA_DEPENDENCIA in tipos_ativos:
            recs.append("AUDITAR politica social: beneficio liberta ou amarra? "
                        "Se a pessoa nao pode se opor sem perder o beneficio, e CATIVO, nao direito.")
        if TipoIndicador.PERSECUICAO_JUDICIAL in tipos_ativos:
            recs.append("AUDITAR o sistema judicial: preso em quarentena sem sentenca = sequestro processual. "
                        "Republica nao integra sujeito que usa justica como arma (P2: autonomia corporal).")
        if nivel in (NivelConfiabilidade.ALTO_RISCO, NivelConfiabilidade.INACEITAVEL):
            recs.append("VETAR exercicio de cargo com poder decisiorio ate restaurar processo.")
            recs.append("Assembleia avalia se o SUJEITO ou o SISTEMA esta corrompido (P4).")
        return recs

    def _gerar_justificativa(
        self, sujeito: str, score: int, nivel: NivelConfiabilidade,
        indicadores: List[IndicadorPolitico], mandatos: int,
    ) -> str:
        count = len(indicadores)
        graves = sum(1 for i in indicadores if i.grau_evidencia.fator_confianca >= 0.5)
        return (
            f"Sujeito '{sujeito}' avaliado com score {score}/100 ({nivel.rotulo}). "
            f"{count} indicadores detectados, {graves} com evidencia forte ou superior. "
            f"{mandatos} mandatos. Veredito baseado em indicadores verificaveis, "
            f"nao em opiniao. A assembleia tem autoridade final (P4)."
        )

    # -- simulacao de cenarios ---------------------------------------------

    def simular_cenarios(
        self, avaliacao: AvaliacaoConfiabilidade
    ) -> List[SimulacaoCenario]:
        """Simula o que acontece em diferentes cenarios."""
        cenarios: List[SimulacaoCenario] = []
        score = avaliacao.score

        # Cenario 1: sujeito continua no poder
        if score < 40:
            prob = 85
            impacto_dem = "Processo democratico degenerado: voto e transacao, nao deliberacao."
            impacto_rep = "Se integrar a Republica, corrompe o processo. Assembleia capturada."
        elif score < 60:
            prob = 60
            impacto_dem = "Erosao da confianca institucional. Alternativas sufocadas."
            impacto_rep = "Integracao arriscada. Monitoramento continuo necessario."
        else:
            prob = 25
            impacto_dem = "Risco baixo de degeneracao. Renovacao possivel."
            impacto_rep = "Integracao com salvaguardas."
        cenarios.append(SimulacaoCenario(
            cenario="Sujeito continua exercendo poder (status quo)",
            probabilidade_pct=prob,
            impacto_democracia=impacto_dem,
            impacto_republica=impacto_rep,
            acao_recomendada="Votar limitacao de mandatos + auditoria continua." if score < 60 else "Monitorar.",
        ))

        # Cenario 2: sujeito e substituido por sucessor treinado
        cenarios.append(SimulacaoCenario(
            cenario="Sujeito e substituido por sucessor da mesma equipe",
            probabilidade_pct=70 if avaliacao.mandatos >= 3 else 40,
            impacto_democracia=(
                "Equipe perpetua sem a 'cara'. Pode ser pior (menos escrutinio) ou melhor (renovacao)."
            ),
            impacto_republica="Avaliar a EQUIPE, nao so o sujeito. Se a equipe corrompeu o processo, trocar a cara nao resolve.",
            acao_recomendada="Auditar a EQUIPE (OpenTeamAudit), nao so o sujeito.",
        ))

        # Cenario 3: nova candidatura surge (sem a maquina)
        cenarios.append(SimulacaoCenario(
            cenario="Nova candidatura emerge fora da maquina",
            probabilidade_pct=30 if score < 40 else 50,
            impacto_democracia="Renovacao democratica real. Risco de ser destruida pela maquina instalada.",
            impacto_republica="Oportunidade de integrar sujeito sem divida com aparelho corrompido.",
            acao_recomendada="PROTEGER a nova candidatura (P4: democracia radical exige pluralismo real).",
        ))

        # Cenario 4: processo e reestruturado (sem o sujeito)
        cenarios.append(SimulacaoCenario(
            cenario="Processo politico reestruturado (Nova Republica)",
            probabilidade_pct=100,  # e a proposta da propria Republica
            impacto_democracia="Fim do ciclo de manipulacao. Voto = deliberacao, nao transacao.",
            impacto_republica="O sujeito e avaliado em processo NOVO. Divida com o sistema antigo documentada, nao ignorada.",
            acao_recomendada="Assembleia constituinte decide: reintegrar com restricoes ou comecar do zero.",
        ))

        return cenarios

    # -- comparacao: sujeito A vs sujeito B --------------------------------

    def comparar_sujeitos(
        self, a: AvaliacaoConfiabilidade, b: AvaliacaoConfiabilidade
    ) -> str:
        """Compara dois sujeitos politicos."""
        diff = a.score - b.score
        if abs(diff) < 5:
            relacao = "equivalentes em confiabilidade"
        elif diff > 0:
            relacao = f"'{a.sujeito}' mais confiavel por {diff} pontos"
        else:
            relacao = f"'{b.sujeito}' mais confiavel por {abs(diff)} pontos"
        return (
            f"COMPARACAO:\n"
            f"  {a.sujeito}: score {a.score} ({a.nivel.rotulo})\n"
            f"  {b.sujeito}: score {b.score} ({b.nivel.rotulo})\n"
            f"  Resultado: {relacao}.\n"
            f"  AVISO: comparar scores NAO significa que um e 'melhor'. "
            f"Significa que um tem MENOS indicadores de processo corrompido. "
            f"A Republica nao escolhe o 'menos pior'. Escolhe o processo LIMPO."
        )


# ============================================================================
# 4. DEMO
# ============================================================================

def _demo() -> None:
    e = ConfiabilidadeEngine()

    print("=" * 70)
    print("OpenPoliticalReliability -- Simulacao de Confiabilidade do Sujeito")
    print("=" * 70)

    # --- Sujeito A: "O Operador" (perfil baseado nos indicadores fornecidos) ---
    print("\n[AVALIACAO] Sujeito: 'O Operador' (perfil: lider historico de esquerda)")

    indicadores_a: List[IndicadorPolitico] = [
        IndicadorPolitico(
            tipo=TipoIndicador.USO_APARELHO_PUBLICO,
            descricao="Maquina publica (cargos, beneficios, programas sociais) usada como aparelho eleitoral em 3 ciclos eleitorais.",
            grau_evidencia=GraveEvidencia.EVIDENCIA_JORNALISTICA,
            ocorrencias=3,
            periodo="3 eleicoes sucessivas",
            metodos=[MetodoManipulacao.APARELHO_ELEITORAL],
        ),
        IndicadorPolitico(
            tipo=TipoIndicador.COMPRA_VOTO,
            descricao="Programas sociais temporalmente ampliados antes de eleicoes; promessa de manutencao condicional ao voto.",
            grau_evidencia=GraveEvidencia.INDICIO_FORTE,
            ocorrencias=3,
            periodo="3 ciclos eleitorais",
            metodos=[MetodoManipulacao.CLIENTELISMO],
        ),
        IndicadorPolitico(
            tipo=TipoIndicador.CONTINUIDADE_PODER,
            descricao="Busca pelo 4o mandato. Equipe articula continuidade com a mesma figura como 'cara' do projeto.",
            grau_evidencia=GraveEvidencia.EVIDENCIA_JORNALISTICA,
            ocorrencias=1,
            periodo="pre-2026",
        ),
        IndicadorPolitico(
            tipo=TipoIndicador.DESMANCHE_ALTERNATIVAS,
            descricao="Novas candidaturas de esquerda desarticuladas pela maquina. Dissidentes marginalizados ou cooptados.",
            grau_evidencia=GraveEvidencia.INDICIO_FORTE,
            ocorrencias=4,
            metodos=[MetodoManipulacao.IMPEDIR_CANDIDATURA, MetodoManipulacao.CARGOS_TROCA],
        ),
        IndicadorPolitico(
            tipo=TipoIndicador.CORRUPCAO_SISTEMICA,
            descricao="Multiplos esquemas de corrupcao vinculados a figuras do nucleo de poder (mensalao, petrolao, etc.). Padrao, nao caso isolado.",
            grau_evidencia=GraveEvidencia.COMPROVADO_JUDICIAL,
            ocorrencias=5,
            periodo="2005-presente",
        ),
        IndicadorPolitico(
            tipo=TipoIndicador.MANIPULACAO_INFORMACAO,
            descricao="Operacao de bots e redes sociais com intensidade equivalente a da direita. Narrativa fabricada em escala.",
            grau_evidencia=GraveEvidencia.INVESTIGACAO_OFICIAL,
            ocorrencias=2,
            periodo="2022-2026",
            metodos=[MetodoManipulacao.BOTS_REDES, MetodoManipulacao.NARRATIVA_FABRICADA],
        ),
        IndicadorPolitico(
            tipo=TipoIndicador.PERSONALISMO,
            descricao="Lider apresentado como insubstituivel. Nao ha plano de successao real -- a figura e o projeto.",
            grau_evidencia=GraveEvidencia.EVIDENCIA_JORNALISTICA,
            ocorrencias=1,
        ),
        IndicadorPolitico(
            tipo=TipoIndicador.MILITANCIA_FINANCEIRA,
            descricao="Distribuicao de cargos e verbas em troca de apoio politico da base. Lealdade comprada, nao convencida.",
            grau_evidencia=GraveEvidencia.COMPROVADO_JUDICIAL,
            ocorrencias=3,
            metodos=[MetodoManipulacao.CARGOS_TROCA],
        ),
        IndicadorPolitico(
            tipo=TipoIndicador.MIGALHA_DIGITAL,
            descricao=(
                "Exercito de migalhas: milhares de militantes pagos com esmolas digitais "
                "para dominar redes sociais. O 'zumbi digital' recebe migralha e em troca "
                "ataca, persegue e cala oponentes. Nao e militancia -- e trabalho escravo "
                "emocional pago com gorjeta."
            ),
            grau_evidencia=GraveEvidencia.INVESTIGACAO_OFICIAL,
            ocorrencias=4,
            periodo="2018-presente",
            metodos=[MetodoManipulacao.BOTS_REDES, MetodoManipulacao.MIGALHA_SOCIAL],
        ),
        IndicadorPolitico(
            tipo=TipoIndicador.MISERIA_DEPENDENCIA,
            descricao=(
                "Miseria como ESTRATEGIA: manter populacao na miseria para mante-la "
                "dependente de beneficio governamental. O beneficio nao liberta -- AMARRA. "
                "Quem depende da migalha para comer nao pode se opor a quem distribui. "
                "E cativo eleitoral renovado a cada ciclo. Pobreza intencional = controle."
            ),
            grau_evidencia=GraveEvidencia.EVIDENCIA_JORNALISTICA,
            ocorrencias=3,
            periodo="3 mandatos",
            metodos=[MetodoManipulacao.CLIENTELISMO, MetodoManipulacao.MIGALHA_SOCIAL],
        ),
        IndicadorPolitico(
            tipo=TipoIndicador.PERSECUICAO_JUDICIAL,
            descricao=(
                "Uso de meios ilicitos para manter oponentes politicos presos em quarentena "
                "judicial. Sem sentenca transitada. Sem prazo. Prisao preventiva eterna como "
                "ferramenta politica. Quando o sistema judicial e arma, nao ha democracia -- "
                "ha sequestro processual."
            ),
            grau_evidencia=GraveEvidencia.INVESTIGACAO_OFICIAL,
            ocorrencias=2,
            periodo="2018-presente",
            metodos=[MetodoManipulacao.PRESO_QUARENTENA, MetodoManipulacao.ARMADILHA_JUDICIAL],
        ),
    ]

    # Eventos verificaveis -- casos historicos reais e comprovados
    eventos_a = [
        e.registrar_evento("2003-2010", "Dois mandatos presidenciais", "eleicao", impacto=0),
        e.registrar_evento(
            "2004", "WALDOMIRO DINIZ: primeiro escandalo do primeiro mandato. Assessor da Casa "
            "Civil filmado cobrando propina de empresario de jogos de azar (bicheiro). Expos a "
            "conexao entre o nucleo duro do governo e o crime organizado. Origem da expressao "
            "'trenzinho da alegria' -- a folha de pagamento paralela do PT.", "investigacao",
            impacto=-7, evidencia=GraveEvidencia.COMPROVADO_JUDICIAL),
        e.registrar_evento(
            "2005", "MENSALAO (AP 470): esquema de compra sistemica de votos de parlamentares no "
            "Congresso em troca de apoio politico a projetos do governo. Revelado pelo ex-deputado "
            "Roberto Jefferson. Mensalidades pagas com dinheiro publico desviado de estatais. "
            "Dezenas de condenacoes pelo STF.", "investigacao",
            impacto=-9, evidencia=GraveEvidencia.COMPROVADO_JUDICIAL),
        e.registrar_evento(
            "2006", "ALOPRADOS: integrantes ligados a campanha de reeleicao presos em Sao Paulo "
            "com maos de dinheiro destinados a comprar dossie falso contra adversarios politicos. "
            "Dinheiro de origem nao esclarecida. Tentativa de fraude eleitoral flagrada.", "investigacao",
            impacto=-6, evidencia=GraveEvidencia.INVESTIGACAO_OFICIAL),
        e.registrar_evento(
            "2014", "PETROLAO / OPERACAO LAVA JATO: gigantesco esquema de desvio de recursos, "
            "superfaturamento e pagamento de propinas na Petrobras e outras estatais. Envolvel "
            "empreiteiras e dezenas de politicos. Fundos abasteciam campanhas eleitorais e partidos. "
            "Lula condenado e preso -- condenacoes anuladas depois pelo STF por questoes "
            "processuais (nulidade, nao inocencia).", "investigacao",
            impacto=-10, evidencia=GraveEvidencia.COMPROVADO_JUDICIAL),
        e.registrar_evento(
            "2007-2016", "BNDES: suspeitas e investigacoes sobre linhas de credito bilionarias do "
            "BNDES para obras de empreiteiras em paises da America Latina e Africa. Contratos "
            "superfaturados, financiamento sem garantia, comissoes ilicitas.", "investigacao",
            impacto=-7, evidencia=GraveEvidencia.INVESTIGACAO_OFICIAL),
        e.registrar_evento(
            "2025", "FRAUDES NO INSS: apuracao sobre descontos associativos nao autorizados em "
            "beneficios de aposentados e pensionistas. Milhares de idosos tiveram dinheiro "
            "descontado sem consentimento para entidades que repassavam parte a operadores. "
            "Forte repercussao publica e cobrancas por transparencia.", "investigacao",
            impacto=-6, evidencia=GraveEvidencia.INVESTIGACAO_OFICIAL),
        e.registrar_evento(
            "2023-2026", "CRISES MINISTERIAIS: quedas e afastamentos de ministros sob suspeita de "
            "irregularidades em emendas parlamentares, uso de estruturas de orgaos federais "
            "(Codevasf) e denuncias de condutas incompativeis com a funcao publica. Aparelho de "
            "Estado operando em ritmo eleitoral: programas sociais ampliados em ano eleitoral, "
            "nomeacoes estrategicas para captura institucional.", "politica publica",
            impacto=-5, evidencia=GraveEvidencia.INDICIO_FORTE),
    ]

    aval_a = e.avaliar(
        sujeito="O Operador",
        cargo="Presidente (historico)",
        mandatos=4,  # 2 + 1 + buscando o 4o
        indicadores=indicadores_a,
        eventos=eventos_a,
    )

    print(f"\n  Score: {aval_a.score}/100")
    print(f"  Nivel: {aval_a.nivel.rotulo}")
    print(f"  Veredito: {aval_a.veredito.rotulo}")
    print(f"\n  INDICADORES DETECTADOS ({len(aval_a.indicadores)}):")
    for ind in aval_a.indicadores:
        print(f"    [{ind.tipo.rotulo}]")
        print(f"      {ind.descricao}")
        print(f"      Evidencia: {ind.grau_evidencia.rotulo} | Ocorrencias: {ind.ocorrencias}")
    print(f"\n  PONTOS FRACOS:")
    for pf in aval_a.pontos_fraco:
        print(f"    - {pf}")
    print(f"\n  RECOMENDACOES:")
    for rec in aval_a.recomendacoes:
        print(f"    -> {rec}")
    print(f"\n  JUSTIFICATIVA: {aval_a.justificativa}")

    # --- Linha do tempo de escandalos ---
    print("\n" + "=" * 70)
    print("[LINHA DO TEMPO -- Escandalos comprovados e investigacoes]")
    print("=" * 70)
    for ev in eventos_a:
        if ev.impacto_confiabilidade < 0:
            flag = "COMPROVADO" if ev.evidencia == GraveEvidencia.COMPROVADO_JUDICIAL else "INVESTIGADO"
            print(f"\n  [{ev.ano}] {flag} (impacto: {ev.impacto_confiabilidade})")
            print(f"  {ev.descricao}")

    # --- Simulacao de cenarios ---
    print("\n" + "=" * 70)
    print("[SIMULACAO DE CENARIOS]")
    print("=" * 70)
    cenarios = e.simular_cenarios(aval_a)
    for i, c in enumerate(cenarios, 1):
        print(f"\n  Cenario {i}: {c.cenario}")
        print(f"  Probabilidade: {c.probabilidade_pct}%")
        print(f"  Impacto na democracia: {c.impacto_democracia}")
        print(f"  Impacto na Republica: {c.impacto_republica}")
        print(f"  Acao: {c.acao_recomendada}")

    # --- Comparacao com "O Polarizador" (extrema-direita, equivalente) ---
    print("\n" + "=" * 70)
    print("[COMPARACAO] O Operador vs O Polarizador (extrema-direita)")
    print("=" * 70)

    indicadores_b: List[IndicadorPolitico] = [
        IndicadorPolitico(
            tipo=TipoIndicador.MANIPULACAO_INFORMACAO,
            descricao="Operacao massiva de bots e fake news. Gabinete do odio institucionalizado.",
            grau_evidencia=GraveEvidencia.INVESTIGACAO_OFICIAL,
            ocorrencias=3,
            metodos=[MetodoManipulacao.BOTS_REDES, MetodoManipulacao.NARRATIVA_FABRICADA,
                     MetodoManipulacao.MEDO_E_AMEACA],
        ),
        IndicadorPolitico(
            tipo=TipoIndicador.VIOLACAO_PRINCIPIOS,
            descricao=(
                "Ataques sistemicos a instituicoes democraticas. Discurso de ruptura constitucional. "
                "MINUTAS GOLPISTAS: elaboracao de documentos para impedir a posse do governo eleito "
                "apos o pleito de 2022. Reunioes com aliados militares para golpe de Estado. "
                "Crimes contra o Estado Democratico de Direito apurados pelo STF."
            ),
            grau_evidencia=GraveEvidencia.COMPROVADO_JUDICIAL,
            ocorrencias=5,
            periodo="2022-2024",
        ),
        IndicadorPolitico(
            tipo=TipoIndicador.CORRUPCAO_SISTEMICA,
            descricao=(
                "Esquema de rachadinha no nucleo familiar e militar. Cargo publico como negocio. "
                "BOLSOLOA DO MEC: pastores sem cargo oficial controlavam liberacao de verbas do "
                "Ministerio da Educacao. Ex-ministro Milton Ribeiro preso temporariamente por "
                "trafico de influencia e corrupcao passiva."
            ),
            grau_evidencia=GraveEvidencia.COMPROVADO_JUDICIAL,
            ocorrencias=5,
            periodo="2019-2022",
        ),
        IndicadorPolitico(
            tipo=TipoIndicador.USO_APARELHO_PUBLICO,
            descricao=(
                "Uso de atos oficiais, decretos e cargo para beneficios eleitorais e ataque a "
                "opositores. ESCANDALO DAS JOIAS: joias e presentes de alto valor recebidos de "
                "autoridades estrangeiras (Arabia Saudita) nao registrados para o acervo publico. "
                "PF apontou peculato, lavagem de dinheiro e associacao criminosa."
            ),
            grau_evidencia=GraveEvidencia.INVESTIGACAO_OFICIAL,
            ocorrencias=3,
            metodos=[MetodoManipulacao.APARELHO_ELEITORAL, MetodoManipulacao.JUDICIALIZACAO_ARMA],
            periodo="2021-2023",
        ),
        IndicadorPolitico(
            tipo=TipoIndicador.PERSONALISMO,
            descricao=(
                "Lider como messias. Movimento como seita. Nao ha sucesso institucional planejado. "
                "FRAUDE EM CARTOES DE VACINACAO: insercao de dados falsos de vacina contra Covid-19 "
                "nos sistemas do Ministerio da Saude para si proprio, familiares e assessores. "
                "Acima da lei porque se acredita acima da lei."
            ),
            grau_evidencia=GraveEvidencia.INVESTIGACAO_OFICIAL,
            ocorrencias=3,
            periodo="2021-2023",
        ),
        IndicadorPolitico(
            tipo=TipoIndicador.OPACIDADE,
            descricao=(
                "GESTAO DA PANDEMIA / CPI DA COVID: relatorios da CPI no Senado apontaram omisses "
                "deliberadas e acoes para promover tratamentos sem eficacia comprovada durante a "
                "crise de saude publica. Centenas de milhares de mortes evitaveis. Opacidade "
                "intencional na compra de vacinas e insumos."
            ),
            grau_evidencia=GraveEvidencia.INVESTIGACAO_OFICIAL,
            ocorrencias=4,
            periodo="2020-2021",
        ),
    ]

    aval_b = e.avaliar(
        sujeito="O Polarizador",
        cargo="Presidente (extrema-direita)",
        mandatos=1,
        indicadores=indicadores_b,
    )
    print(f"\n  O Polarizador: score {aval_b.score}/100 ({aval_b.nivel.rotulo})")
    print(f"  Veredito: {aval_b.veredito.rotulo}")
    print(f"\n{e.comparar_sujeitos(aval_a, aval_b)}")

    # --- Scorecard comparativo ---
    print("\n" + "=" * 70)
    print("[SCORECARD COMPARATIVO]")
    print("=" * 70)
    print(f"  {'Indicador':.<40} {'Operador':>10} {'Polarizador':>12}")
    print(f"  {'-'*62}")
    for t in TipoIndicador:
        a_tem = "SIM" if any(i.tipo == t for i in indicadores_a) else "nao"
        b_tem = "SIM" if any(i.tipo == t for i in indicadores_b) else "nao"
        print(f"  {t.rotulo:.<40} {a_tem:>10} {b_tem:>12}")
    print(f"\n  {'Score final':.<40} {aval_a.score:>10} {aval_b.score:>12}")
    print(f"  {'Nivel':.<40} {aval_a.nivel.id:>10} {aval_b.nivel.id:>12}")
    print(f"  {'Veredito':.<40} {aval_a.veredito.id:>10} {aval_b.veredito.id:>12}")

    # --- Catalogo historico: corrupcao no Brasil NAO e de um lado so ---
    print("\n" + "=" * 70)
    print("[HISTORICO -- A corrupcao no Brasil NAO e de um lado so]")
    print("=" * 70)
    print("""
  O Operador (PT/Lula): score 0 -- INACEITAVEL.
    Waldomiro Diniz (2004), Mensalao (2005), Aloprados (2006),
    Petrolao/Lava Jato (2014), BNDES (2007-2016),
    Fraudes no INSS (2025), Crises ministeriais/Codevasf (2023-2026).

  O Polarizador (Bolsonaro): score -- PREOCUPANTE/ALTO RISCO.
    Minutas golpistas e tentativa de golpe (2022-2024),
    Bolsolao do MEC / Milton Ribeiro (2019-2022),
    Escandalo das joias / Arabia Saudita (2021-2023),
    Fraude em cartoes de vacinacao (2021-2023),
    Gestao da pandemia / CPI da Covid (2020-2021).

  MAS A CORRUPCAO BRASILEIRA E MAIS ANTIGA QUE O PT:

  O Renegado (Collor, 1992): IMPEACHMENT por corrupcao.
    Denunciado pelo PROPRIO IRMAO (Pedro Collor). Esquema de PC Farias,
    extorsao de empresarios, uso de conta fantasma. Primeiro presidente
    eleito por voto direto apos a ditadura -- e o primeiro CASSADO.
    Score simulado: baixo. Corrupcao COMPROVADA + personalismo extremo.

  O Cartorio (Anoes do Orcamento, 1993):
    Grupo de parlamentares desviava verbas publicas do orcamento da Uniao.
    Nome vem da fraudem no 'orcamento secreto' -- emendas sem destinacao
    clara, desviadas para bolso de deputados. Escandalo que revelou que
    o Congresso operava como caixa eletronico.
    Nao e um sujeito -- e um SISTEMA. A Republica o combate.

  A DITADURA MILITAR (1964-1985):
    A corrupcao durante o regime militar nao foi investigada -- foi
    PROTEGIDA pela ausencia de democracia. Sem P4 (transparencia radical),
    nao ha corrupcao VISIVEL porque nao ha imprensa livre, nem Congresso,
    nem judiciario independente. A corrupcao da ditadura e a mais grave
    de todas: a que NUNCA foi contada. Billioes em comissoes de obras
    faraonicas (Transamazonica, Itaipu, Angra), nepotismo, terrorismo
    de Estado financiado com dinheiro publico.

  ATESE DO HISTORICO:
    A corrupcao brasileira e SISTEMICA, nao partidaria.
    Collor (centro-direita), PT (esquerda), Bolsonaro (extrema-direita),
    e a ditadura (militar) -- TODOS corromperam.
    A Republica NAO herda nenhuma destas tradicoes.
    Ela COMECA DO ZERO: processo limpo, voto = deliberacao, sem aparelho.
""")

    # --- Simulacao dos sujeitos historicos adicionais ---

    # Collor
    indicadores_collor: List[IndicadorPolitico] = [
        IndicadorPolitico(
            tipo=TipoIndicador.CORRUPCAO_SISTEMICA,
            descricao="Esquema PC Farias: extorsao sistemica de empresarios, conta fantasma, desvio de dinheiro publico.",
            grau_evidencia=GraveEvidencia.COMPROVADO_JUDICIAL,
            ocorrencias=5,
            periodo="1990-1992",
        ),
        IndicadorPolitico(
            tipo=TipoIndicador.USO_APARELHO_PUBLICO,
            descricao="Uso da presidencia para beneficio pessoal e politico. Nomeacoes por lealdade, nao merito.",
            grau_evidencia=GraveEvidencia.COMPROVADO_JUDICIAL,
            ocorrencias=3,
            periodo="1990-1992",
            metodos=[MetodoManipulacao.APARELHO_ELEITORAL],
        ),
        IndicadorPolitico(
            tipo=TipoIndicador.PERSONALISMO,
            descricao="Personalismo extremo. Denunciado pelo PROPRIO IRMAO (Pedro Collor). Sem rede de apoio institucional.",
            grau_evidencia=GraveEvidencia.COMPROVADO_JUDICIAL,
            ocorrencias=1,
        ),
        IndicadorPolitico(
            tipo=TipoIndicador.VIOLACAO_PRINCIPIOS,
            descricao="Plano Collor: confisco de poupanca. Violacao de contrato e propriedade privada.",
            grau_evidencia=GraveEvidencia.COMPROVADO_JUDICIAL,
            ocorrencias=1,
            periodo="1990",
        ),
    ]
    aval_collor = e.avaliar(
        sujeito="O Renegado (Collor)",
        cargo="Presidente (impeachado 1992)",
        mandatos=1,
        indicadores=indicadores_collor,
    )
    print(f"\n  [HISTORICO] O Renegado (Collor): score {aval_collor.score}/100 "
          f"({aval_collor.nivel.id}) -- {aval_collor.veredito.id}")

    # Anoes do Orcamento (sistema, nao sujeito individual)
    indicadores_anoes: List[IndicadorPolitico] = [
        IndicadorPolitico(
            tipo=TipoIndicador.CORRUPCAO_SISTEMICA,
            descricao="Anoes do Orcamento (1993): parlamentares desviavam verbas do orcamento da Uniao via emendas secretas. Congresso como caixa eletronico.",
            grau_evidencia=GraveEvidencia.COMPROVADO_JUDICIAL,
            ocorrencias=7,
            periodo="1993",
        ),
        IndicadorPolitico(
            tipo=TipoIndicador.OPACIDADE,
            descricao="Orcamento secreto: emendas sem destinacao clara, sem transparencia, sem auditoria. A opacidade ERA o mecanismo.",
            grau_evidencia=GraveEvidencia.COMPROVADO_JUDICIAL,
            ocorrencias=10,
        ),
    ]
    aval_anoes = e.avaliar(
        sujeito="O Cartorio (Anoes do Orcamento)",
        cargo="Sistema congressual (1993)",
        mandatos=0,
        indicadores=indicadores_anoes,
    )
    print(f"  [HISTORICO] O Cartorio (Anoes): score {aval_anoes.score}/100 "
          f"({aval_anoes.nivel.id}) -- {aval_anoes.veredito.id}")

    # --- Tabela historica amplificada ---
    print("\n[TABELA HISTORICA -- Scores de confiabilidade]")
    print(f"  {'Sujeito':.<35} {'Score':>6} {'Nivel':>12} {'Veredito':>12}")
    print(f"  {'-'*67}")
    for aval, nome_curto in [
        (aval_a, "O Operador (PT/Lula)"),
        (aval_b, "O Polarizador (Bolsonaro)"),
        (aval_collor, "O Renegado (Collor)"),
        (aval_anoes, "O Cartorio (Anoes 1993)"),
    ]:
        print(f"  {nome_curto:.<35} {aval.score:>6} {aval.nivel.id:>12} {aval.veredito.id:>12}")

    # --- FILOSOFIA ---
    print("\n" + "=" * 70)
    print("FILOSOFIA -- A Republica nao escolhe o 'menos pior'")
    print("=" * 70)
    print("""
A TENSAO FUNDAMENTAL:
  O sistema eleitoral atual obriga a escolher entre 'menos pior'.
  Esquerda que compra voto com bolsa vs Direita que compra voto com medo.
  Ambos manipulam. Ambos corrompem o processo. Ambos usam bots.
  A diferenca nao e de PRINCIPIO -- e de METODO.

O QUE A REPUBLICA FAZ DIFERENTE:
  A Republica NAO escolhe entre dois processos corrompidos.
  Ela CRIA um terceiro: processo limpo, voto = deliberacao, sem aparelho.

O DIAGNOSTICO:
  O Operador: usa o APARELHO DE ESTADO para perpetuar.
    - 3 eleicoes com maquina publica.
    - Equipe quer a 4a porque a figura e a 'cara' da transacao.
    - Desmancha alternativas DA PROPRIA ESQUERDA.
    - Corrupcao COMPROVADA judicialmente (mensalao, petrolao).
    - Bots em escala equivalente a extrema-direita.
    - EXERCITO DE MIGALHAS: militancia online paga com esmola digital.
      O 'zumbi digital' nao e militante -- e trabalhador escravo emocional.
      Recebe migralha, ataca oponente, cala dissidencia. Fabrica consenso.
    - MISERIA COMO ESTRATEGIA: beneficio que nao liberta, AMARRA.
      Quem depende da migalha para comer nao pode se opor.
      Cativo eleitoral renovado a cada ciclo. Pobreza intencional = controle.
    - PERSECUICAO JUDICIAL: presos politicos em quarentena sem sentenca.
      Meios ilicitos para manter oponentes fora do jogo.
      O sistema judicial vira arma. Democracia vira sequestro processual.

  O Polarizador: usa o MEDO e a RUPTURA para perpetuar.
    - Minutas golpistas: tentou impedir a posse do governo eleito.
    - Bolsolao do MEC: pastores controlando verba publica.
    - Joias da Arabia Saudita nao declaradas (peculato).
    - Cartao de vacina fraudado (acima da lei).
    - CPI da Covid: mortes evitaveis por omissao deliberada.
    - Gabinete do odio institucionalizado.
    - Risco de ruptura democratica -- TENTOU.

  AMBOS tem score ALTO RISCO ou INACEITAVEL.
  A Republica NAO integra nenhum dos dois sem auditoria radical.

A SOLUCAO NAO E ESCOLHER LADOS:
  A solucao e RECONSTRUIR O PROCESSO.
  - Voto sem aparelho (OpenVoteIntegrity).
  - Bots detectados e neutralizados (P9 + OpenAntiPolarization).
  - Mandatos limitados (renovacao obrigatoria).
  - Novas candidaturas PROTEGIDAS (pluralismo real).
  - Equipe auditada, nao so o sujeito (OpenTeamAudit).

A PERGUNTA CERTA NAO E 'em quem confiar?'.
  E 'que PROCESSO merece confianca?'.
  O sujeito e temporario. O processo e permanente.
  Processo corrompido corrompe qualquer sujeito.
  Processo limpo protege qualquer sujeito -- inclusive de si mesmo.
""")


if __name__ == "__main__":
    _demo()
