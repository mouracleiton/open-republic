#!/usr/bin/env python3
"""
OpenFrenteUnificada -- Resolucao de Rixas + Triagem Aberta + Cotas do Povo
=============================================================================
"Rixas antigas se resolvem com dado, nao com abraco.
 Limites ideologicos sao claros, nao borrados.
 Quem migra de partido passa pela triagem, nao pela relacao.
 Cotas sao definidas pelo povo, nao pela cpula."
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Tuple
from collections import defaultdict


class TipoRixa(Enum):
    HISTORICA = "HISTORICA"         # rixa de decadas (PT x PSOL, etc)
    IDEOLOGICA = "IDEOLOGICA"       # divergencia de principio
    TATICA = "TATICA"               # divergencia de estrategia
    PESSOAL = "PESSOAL"             # entre liderancas


class StatusRixa(Enum):
    IRRESOLVIDA = "IRRESOLVIDA"
    EM_NEGOCIACAO = "EM_NEGOCIACAO"
    RESOLVIDA = "RESOLVIDA"
    IMPASSAVEL = "IMPASSAVEL"


class TipoCota(Enum):
    GENERO = "GENERO"               # minimo 50% mulheres
    RACA = "RACA"                   # minimo 56% negros (proporcao populacional)
    CLASSE = "CLASSE"               # minimo trabalhador/sem partido tradicional
    REGIAO = "REGIAO"               # minimo por regiao (N/NE/CO/SE/S)
    INDIGENA = "INDIGENA"           # minimo representacao originaria
    JOVEM = "JOVEM"                 # minimo 18-29 anos
    LGBTQIA = "LGBTQIA"             # minimo representacao
    PCD = "PCD"                     # minimo pessoas com deficiencia
    SEM_PARTIDO = "SEM_PARTIDO"     # minimo gente sem mandato anterior


@dataclass
class Rixa:
    """Uma rixa historica entre partidos/faccoes da esquerda."""
    id: str
    partido_a: str
    partido_b: str
    tipo: TipoRixa
    descricao: str
    status: StatusRixa
    Condicao_resolucao: str        # o que precisa pra resolver
    nao_negociavel: str            # o que NUNCA se negocia


@dataclass
class LimiteIdeologico:
    """Limite claro do que a frente aceita e nao aceita."""
    principio: str
    aceita: List[str]              # o que esta dentro do limite
    rejeita: List[str]             # o que esta fora do limite


@dataclass
class CotaPovo:
    """Cota definida pelo povo, nao pela cpula."""
    tipo: TipoCota
    minimo_pct: float              # minimo % de representacao
    justificativa: str             # baseado em que dado?
    fonte: str                     # IBGE, Raio X, etc
    nao_negociavel: bool           # povo definiu, nao muda


@dataclass
class CandidatoMigracao:
    """Candidato de outro partido querendo migrar pra frente."""
    nome: str
    partido_origem: str
    cargo_atual: str
    uf: str

    # Score de capacidade (mesma formula 3 camadas)
    score_capacidade: float
    score_propostas: float         # Gate WO das propostas

    # Criterios de triagem (0 ou 1 cada)
    aceita_gate_wo: bool           # proposta passa no Gate?
    aceita_transparencia: bool     # aceita Raio X em cima?
    aceita_cotas: bool             # aceita cotas do povo?
    sem_corrupcao_comprovada: bool # TSE/CGU limpo?
    aceita_ser_medido: bool        # aceita FATO como metrica?
    nao_e_dono_de_feudo: bool      # nao traz maquina pessoal?

    # Preenche quais cotas
    cotas_preenchidas: List[TipoCota] = field(default_factory=list)

    @property
    def passa_triagem(self) -> bool:
        return all([
            self.aceita_gate_wo, self.aceita_transparencia, self.aceita_cotas,
            self.sem_corrupcao_comprovada, self.aceita_ser_medido,
            self.nao_e_dono_de_feudo
        ])

    @property
    def score_triagem(self) -> float:
        """Score de triagem (0-5). Combina capacidade + proposta + triagem."""
        if not self.passa_triagem:
            return 0.0
        base = (self.score_capacidade + self.score_propostas) / 2
        bonus_cotas = len(self.cotas_preenchidas) * 0.2  # +0.2 por cota preenchida
        return min(5.0, base + bonus_cotas)


def _init_rixas() -> List[Rixa]:
    return [
        Rixa("pt_psol", "PT", "PSOL", TipoRixa.HISTORICA,
             "PSOL nasceu da ruptura com PT (2004). Mandates, mensalao, governabilidade.",
             StatusRixa.EM_NEGOCIACAO,
             "PT aceita que PSOL mantenha autonomia e criticize o governo publicamente",
             "PSOL nao se dissolve no PT. PT nao exige disciplina de voto."),

        Rixa("pt_pcb", "PT", "PCB", TipoRixa.IDEOLOGICA,
             "PCB considera PT reformista/burgues. PT considera PCB ultrapassado.",
             StatusRixa.IRRESOLVIDA,
             "Reconhecimento mutuo de que o inimigo e a direita, nao o companheiro",
             "PCB nao abre mao do socialismo. PT nao exige abandono da critica."),

        Rixa("pt_pstu", "PT", "PSTU", TipoRixa.HISTORICA,
             "PSTU rompeu com PT nos anos 90. Acusa PT de trair a classe trabalhadora.",
             StatusRixa.IRRESOLVIDA,
             "PSTU aceita que a frente unificada nao significa abandono da critica",
             "PSTU nao e obrigado a votar com o governo. So nao sabota a frente."),

        Rixa("psol_pcb", "PSOL", "PCB", TipoRixa.IDEOLOGICA,
             "Divergem sobre tipo de socialismo, reforma vs revolucao, relacao com Estado.",
             StatusRixa.EM_NEGOCIACAO,
             "Acordo de que a frente e TATICA, nao fusao ideologica",
             "Nenhum partido impoe sua linha ao outro."),

        Rixa("pt_rede", "PT", "REDE", TipoRixa.HISTORICA,
             "Marina rompeu com PT em 2009. Acusa PT de abandono ambiental.",
             StatusRixa.EM_NEGOCIACAO,
             "Reconhecimento do papel de Marina na area ambiental, sem exigir silencio",
             "Marina mantem agenda ambiental como prioridade."),

        Rixa("pt_pdt", "PT", "PDT", TipoRixa.TATICA,
             "Ciro x Lula rivalidade presidencial. PDT se sente secundarizado.",
             StatusRixa.EM_NEGOCIACAO,
             "PDT recebe ministerios reais (nao de fachada) e autonomia",
             "Ciro nao e obrigado a apoiar Lula em tudo. So na frente."),

        Rixa("psol_rede", "PSOL", "REDE", TipoRixa.TATICA,
             "Divergencia sobre desenvolvimento x preservacao, povo x classe media.",
             StatusRixa.EM_NEGOCIACAO,
             "Agenda ambiental com justica social (nao uma coisa OU outra)",
             "Ambiente sem povo e ONG. Povo sem ambiente e deserto."),

        Rixa("pt_up", "PT", "UP", TipoRixa.IDEOLOGICA,
             "UP e socialista revolucionaria. PT e social-democrata. Divergencia fundamental.",
             StatusRixa.IRRESOLVIDA,
             "Acordo tatico: frente contra a direita, sem fusao ideologica",
             "UP nao abandona o socialismo. PT nao exige reformismo da UP."),

        Rixa("pcb_pstu", "PCB", "PSTU", TipoRixa.IDEOLOGICA,
             "Divergem sobre modelo de partido, insercao nos movimentos, tatica eleitoral.",
             StatusRixa.EM_NEGOCIACAO,
             "Unidade na acao, diversidade na teoria",
             "Nenhum impoe tatica ao outro."),

        Rixa("pt_pcob", "PT", "PCdoB", TipoRixa.TATICA,
             "PCdoB foi aliado historico de PT. Tensao por espaco e ministerios.",
             StatusRixa.RESOLVIDA,
             "Ja operam juntos na base governista. Ministerio real.",
             "PCdoB mantem autonomia em educacao e direitos."),
    ]


def _init_limites() -> List[LimiteIdeologico]:
    return [
        LimiteIdeologico(
            "Anti-fascismo",
            aceita=["defesa da democracia", "combate ao bolsonarismo", "eleicao como processo"],
            rejeita=["golpe militar", "ditadura", "fechamento do congresso"]),

        LimiteIdeologico(
            "Anti-imperialismo",
            aceita=["soberania nacional", "multi-alinhamento", "Sul global"],
            rejeita=["submissao a EUA", "intervencao estrangeira", "bases militares gringas"]),

        LimiteIdeologico(
            "Justica social",
            aceita=["redistribuicao de renda", "reforma agraria", "direitos trabalhistas",
                    "saude e educacao gratuitas", "moradia como direito"],
            rejeita=["privatizacao do essencial", "precarizacao", "trabalho escravo"]),

        LimiteIdeologico(
            "Transparencia radical (P5)",
            aceita=["dados abertos", "Raio X em cima de tudo", "Gate WO em propostas",
                    "accountability em tempo real"],
            rejeita=["opacidade", "dado escondido", "acordo secreto", "gaveta"]),

        LimiteIdeologico(
            "Diversidade real",
            aceita=["cotas do povo", "representatividade de minorias", "paridade de genero"],
            rejeita=["palanque de diversidade", "figuracao", "cota de fachada"]),

        LimiteIdeologico(
            "Anti-feudo",
            aceita=["rotatividade de poder", "fiscalizacao reciproca", "limite de mandatos"],
            rejeita=["dinastia politica", "maquina pessoal", "coronelismo"]),
    ]


def _init_cotas() -> List[CotaPovo]:
    return [
        CotaPovo(TipoCota.GENERO, 50.0, "50% da populacao e mulher (IBGE 2022)", "IBGE", True),
        CotaPovo(TipoCota.RACA, 56.0, "56% da populacao e negra/parda (IBGE 2022)", "IBGE", True),
        CotaPovo(TipoCota.CLASSE, 40.0, "40% minimo de candidatos sem mandato anterior (povo, nao politico)", "Raio X", True),
        CotaPovo(TipoCota.REGIAO, 15.0, "15% minimo por regiao (N/NE nao pode ser minoria)", "IBGE", True),
        CotaPovo(TipoCota.INDIGENA, 5.0, "305 etnias originarias, sub-representadas historicamente", "Raio X/IBGE", True),
        CotaPovo(TipoCota.JOVEM, 20.0, "20% minimo 18-29 anos (juventude sem representacao)", "IBGE", True),
        CotaPovo(TipoCota.LGBTQIA, 3.0, "Estimativa 3-5% da populacao, zero representacao historica", "Raio X", False),
        CotaPovo(TipoCota.PCD, 5.0, "8.4% da populacao tem alguma deficiencia (IBGE 2010)", "IBGE", True),
        CotaPovo(TipoCota.SEM_PARTIDO, 15.0, "15% minimo de candidatos sem filiacao partidaria anterior", "Raio X", False),
    ]


class FrenteUnificada:
    """
    Frente que resolve rixas, estabelece limites e faz triagem aberta.
    """

    def __init__(self):
        self.rixas = _init_rixas()
        self.limites = _init_limites()
        self.cotas = _init_cotas()

    def rixas_por_status(self) -> Dict[str, List[Rixa]]:
        resultado = defaultdict(list)
        for r in self.rixas:
            resultado[r.status.value].append(r)
        return dict(resultado)

    def limites_aceita_ou_rejeita(self, proposta: str) -> str:
        """Verifica se uma posicao esta dentro ou fora dos limites."""
        proposta_lower = proposta.lower()
        for lim in self.limites:
            for rejeita in lim.rejeita:
                if rejeita.lower() in proposta_lower:
                    return f"REJEITADO por {lim.principio}: {rejeita}"
        for lim in self.limites:
            for aceita in lim.aceita:
                if aceita.lower() in proposta_lower:
                    return f"ACEITO por {lim.principio}: {aceita}"
        return "NEUTRO (nao previsto)"

    def cotas_resumo(self) -> List[Dict[str, Any]]:
        return [{
            "tipo": c.tipo.value, "minimo_pct": c.minimo_pct,
            "justificativa": c.justificativa, "fonte": c.fonte,
            "nao_negociavel": c.nao_negociavel,
        } for c in self.cotas]

    def scorecard(self) -> Dict[str, Any]:
        n_resolvidas = sum(1 for r in self.rixas if r.status == StatusRixa.RESOLVIDA)
        n_negociacao = sum(1 for r in self.rixas if r.status == StatusRixa.EM_NEGOCIACAO)
        n_irresolvidas = sum(1 for r in self.rixas if r.status == StatusRixa.IRRESOLVIDA)
        return {
            "modulo": "open_frente_unificada",
            "versao": "0.1.0-spec",
            "rixas_total": len(self.rixas),
            "rixas_resolvidas": n_resolvidas,
            "rixas_em_negociacao": n_negociacao,
            "rixas_irresolvidas": n_irresolvidas,
            "limites_ideologicos": len(self.limites),
            "cotas_do_povo": len(self.cotas),
            "principio": "Rixas se resolvem com dado. Limites sao claros. Cotas sao do povo.",
        }


def _demo():
    fu = FrenteUnificada()
    sc = fu.scorecard()
    rixas_status = fu.rixas_por_status()

    print("=" * 85)
    print("FRENTE UNIFICADA -- Rixas, Limites, Cotas e Triagem")
    print("=" * 85)

    print(f"\n{sc['rixas_total']} rixas mapeadas:")
    print(f"  Resolvidas:      {sc['rixas_resolvidas']}")
    print(f"  Em negociacao:   {sc['rixas_em_negociacao']}")
    print(f"  Irresolvidas:    {sc['rixas_irresolvidas']}")
    print(f"  Limites:         {sc['limites_ideologicos']}")
    print(f"  Cotas do povo:   {sc['cotas_do_povo']}")

    print(f"\n{'='*85}")
    print("RIXAS HISTORICAS E IDEOLOGICAS")
    print(f"{'='*85}")
    for r in fu.rixas:
        print(f"\n  [{r.status.value}] {r.partido_a} x {r.partido_b}")
        print(f"    Tipo: {r.tipo.value}")
        print(f"    Rixa: {r.descricao[:70]}")
        print(f"    Condicao de resolucao: {r.Condicao_resolucao[:70]}")
        print(f"    NAO NEGOCIAVEL: {r.nao_negociavel[:70]}")

    print(f"\n{'='*85}")
    print("LIMITES IDEOLOGICOS DA FRENTE")
    print(f"{'='*85}")
    for lim in fu.limites:
        print(f"\n  {lim.principio}")
        print(f"    ACEITA: {', '.join(lim.aceita[:4])}")
        print(f"    REJEITA: {', '.join(lim.rejeita[:3])}")

    print(f"\n{'='*85}")
    print("COTAS DEFINIDAS PELO POVO")
    print(f"{'='*85}")
    for c in fu.cotas:
        n = "*** NAO NEGOCIAVEL ***" if c.nao_negociavel else "(flexivel)"
        print(f"\n  {c.tipo.value:<15} minimo={c.minimo_pct:.0f}%  {n}")
        print(f"    Base: {c.justificativa}")
        print(f"    Fonte: {c.fonte}")

    print(f"\n{'='*85}")
    print("TRIAGEM ABERTA (criterios para migrar)")
    print(f"{'='*85}")
    print("""
  6 CRITERIOS OBRIGATORIOS (todos = 1):

  1. Aceita Gate WO?          -- proposta passa nos 7 criterios?
  2. Aceita Transparencia?    -- Raio X medindo em cima de tudo?
  3. Aceita Cotas do Povo?    -- respeita cotas definidas pelo povo?
  4. Sem Corrupcao?           -- TSE/CGU/TCU limpo?
  5. Aceita Ser Medido?       -- FATO como metrica, nao opiniao?
  6. Nao e Dono de Feudo?     -- nao traz maquina pessoal/coronelismo?

  6/6 = APTO PARA MIGRAR (score calculado)
  <6/6 = BARRADO

  BONUS DE COTAS:
  +0.2 por cota preenchida (genero, raca, regiao, jovem, etc)
  
  CORTE FINAL: >= 4.0
""")


if __name__ == "__main__":
    _demo()
