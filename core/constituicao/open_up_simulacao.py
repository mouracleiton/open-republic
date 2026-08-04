#!/usr/bin/env python3
"""
OpenUPSimulacao -- Programa da Unidade Popular vs Gate WO
============================================================
25 propostas reais extraidas de unidadepopular.org.br/programa
Validadas pelo Gate WO (7 criterios) + Epistemologico (FATO/DADO/OPINIAO).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List


class StatusGate(Enum):
    APROVADO = "APROVADO"
    JEQUERI = "JEQUERI"
    WO = "W.O."


@dataclass
class PropostaUP:
    """Uma proposta real do programa da UP."""
    n: int
    area: str           # dominio Raio X
    titulo: str         # resumo curto
    texto_original: str  # texto real do site

    # 5 criticos
    tem_como: bool
    tem_quem: bool
    tem_custo: bool
    tem_prazo: bool
    tem_metrica: bool
    # 2 jequeri
    tem_fonte_dados: bool
    tem_diagnostico: bool

    # Epistemologia
    classificacao: str  # FATO, DADO, OPINIAO

    # Avaliacao de diagnostico vs direcao vs execucao (camadas separadas)
    diagnostico_correto: bool   # entende o problema?
    direcao_correta: bool       # aponta pra solucao que ataca a causa?
    execucao_detalhada: bool    # tem COMO/QUANTO/PRAZO/METRICA?

    @property
    def n_criticos(self) -> int:
        return sum([self.tem_como, self.tem_quem, self.tem_custo,
                    self.tem_prazo, self.tem_metrica])

    @property
    def status(self) -> StatusGate:
        if self.n_criticos == 5:
            return StatusGate.APROVADO if self.tem_fonte_dados and self.tem_diagnostico else StatusGate.JEQUERI
        else:
            return StatusGate.WO

    @property
    def score_3_camadas(self) -> float:
        """Score separando diagnostico, direcao e execucao (0-5)."""
        diag = 1.0 if self.diagnostico_correto else 0.0
        dire = 1.0 if self.direcao_correta else 0.0
        exec_ = self.n_criticos / 5.0  # 0-1
        # Diagnostico peso 2, direcao peso 2, execucao peso 1
        # (nao pune quem nao tem acesso a dados pra detalhar execucao)
        return round((diag * 2 + dire * 2 + exec_ * 1) / 5 * 5, 2)


def _init_propostas() -> List[PropostaUP]:
    return [

        PropostaUP(1, "inflacao", "Controle social dos monopólios e planificação econômica",
            "Controle social de todos os monopólios e consórcios capitalistas e dos meios de produção nos setores estratégicos da economia; planificação da economia para atender às necessidades da população e acabar com as desigualdades regionais e sociais.",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao="OPINIAO",
            diagnostico_correto=True, direcao_correta=True, execucao_detalhada=False),

        PropostaUP(2, "inflacao", "Nacionalização do sistema bancário",
            "Nacionalização do sistema bancário e controle popular do sistema financeiro.",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao="OPINIAO",
            diagnostico_correto=True, direcao_correta=True, execucao_detalhada=False),

        PropostaUP(3, "inflacao", "Fim da espoliação imperialista e anulação da dívida externa",
            "Fim da espoliação imperialista; anulação dos acordos e dívidas do Estado com capitalistas estrangeiros; transferência do comércio exterior para órgãos do Estado.",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao="OPINIAO",
            diagnostico_correto=True, direcao_correta=True, execucao_detalhada=False),

        PropostaUP(4, "energia", "Reestatização e fim dos leilões de petróleo",
            "Reestatização das estatais privatizadas; fim dos leilões do petróleo; revisão das concessões dos portos, aeroportos e estradas.",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao="OPINIAO",
            diagnostico_correto=True, direcao_correta=True, execucao_detalhada=False),

        PropostaUP(5, "emprego", "Emprego e trabalho obrigatórios para todos",
            "Garantia de emprego e trabalho obrigatórios para todas as pessoas adultas capazes de trabalhar; proibição da exploração do trabalho infantil.",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao="OPINIAO",
            diagnostico_correto=True, direcao_correta=True, execucao_detalhada=False),

        PropostaUP(6, "agropecuaria", "Reforma agrária popular e nacionalização da terra",
            "Reforma agrária popular; nacionalização da terra e fim do monopólio privado da terra.",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao="OPINIAO",
            diagnostico_correto=True, direcao_correta=True, execucao_detalhada=False),

        PropostaUP(7, "inflacao", "Anulação de impostos extorsivos, imposto sobre grandes fortunas",
            "Anulação dos impostos extorsivos cobrados do povo; imposto sobre as grandes fortunas e progressivo. Quem ganha mais, paga mais.",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao="OPINIAO",
            diagnostico_correto=True, direcao_correta=True, execucao_detalhada=False),

        PropostaUP(8, "transporte", "Estatização dos meios de transporte coletivo",
            "Estatização de todos os meios de transporte coletivo.",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao="OPINIAO",
            diagnostico_correto=True, direcao_correta=True, execucao_detalhada=False),

        PropostaUP(9, "educacao", "Educação pública e gratuita em todos os níveis",
            "Educação pública e gratuita para todos e em todos os níveis; fim do lucro na educação; livre acesso à universidade; fim do vestibular.",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao="OPINIAO",
            diagnostico_correto=True, direcao_correta=True, execucao_detalhada=False),

        PropostaUP(10, "comunicacao", "Democratização dos meios de comunicação",
            "Democratização dos meios de comunicação, com a socialização de todos os grandes canais de televisão, jornais e rádios.",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao="OPINIAO",
            diagnostico_correto=True, direcao_correta=True, execucao_detalhada=False),

        PropostaUP(11, "violencia", "Fim das doações de capitalistas para campanhas",
            "Ampla liberdade de expressão e organização para os trabalhadores; fim das doações de capitalistas para campanhas eleitorais.",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao="OPINIAO",
            diagnostico_correto=True, direcao_correta=True, execucao_detalhada=False),

        PropostaUP(12, "violencia", "Juízes e tribunais eleitos pelo povo",
            "Justiça: juízes e tribunais eleitos pelo povo.",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao="OPINIAO",
            diagnostico_correto=True, direcao_correta=True, execucao_detalhada=False),

        PropostaUP(13, "violencia", "Direitos das mulheres, legalização do aborto",
            "Fim da discriminação das mulheres; direitos iguais; fim do racismo; descriminalização e legalização do aborto; punição aos infratores.",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao="OPINIAO",
            diagnostico_correto=True, direcao_correta=True, execucao_detalhada=False),

        PropostaUP(14, "cultura", "Fim da discriminação religiosa, racial e de sexo",
            "Fim de qualquer discriminação religiosa, de raça ou sexo; plena garantia à liberdade religiosa.",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao="OPINIAO",
            diagnostico_correto=True, direcao_correta=True, execucao_detalhada=False),

        PropostaUP(15, "ambiente", "Defesa do meio ambiente e controle popular da Amazônia",
            "Defesa e proteção do meio ambiente; proibição da destruição de florestas; controle popular sobre a Amazônia; expulsão de monopólios estrangeiros.",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao="OPINIAO",
            diagnostico_correto=True, direcao_correta=True, execucao_detalhada=False),

        PropostaUP(16, "indigena", "Demarcação imediata de terras indígenas",
            "Demarcação e posse imediata de todas as terras indígenas; escolas diferenciadas; apoio às línguas indígenas; defesa da cultura.",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao="OPINIAO",
            diagnostico_correto=True, direcao_correta=True, execucao_detalhada=False),

        PropostaUP(17, "saude", "Saúde pública e gratuita, fim dos planos privados",
            "Garantia de saúde pública e gratuita para todos; fim da exploração dos planos de saúde privados.",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao="OPINIAO",
            diagnostico_correto=True, direcao_correta=True, execucao_detalhada=False),

        PropostaUP(18, "cultura", "Cultura nacional e popular",
            "Defesa e incentivo à cultura nacional e popular; nacionalização de companhias gravadoras e produtoras de filmes.",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao="OPINIAO",
            diagnostico_correto=True, direcao_correta=True, execucao_detalhada=False),

        PropostaUP(19, "emprego", "Jornada de 6 horas e aumento geral de salários",
            "Jornada de trabalho: redução para seis horas para todos os trabalhadores e aumento geral dos salários.",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao="OPINIAO",
            diagnostico_correto=True, direcao_correta=True, execucao_detalhada=False),

        PropostaUP(20, "emprego", "Descanso em feriados e domingos",
            "Lei garantindo o descanso em dias festivos, domingos e feriados para os trabalhadores, excetuando setores essenciais.",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao="OPINIAO",
            diagnostico_correto=True, direcao_correta=True, execucao_detalhada=False),

        PropostaUP(21, "habitacao", "Moradia, saneamento e reforma urbana",
            "Garantia de moradia digna, saneamento e coleta de lixo para todas as famílias; imóveis abandonados para resolver o déficit habitacional; reforma urbana.",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao="OPINIAO",
            diagnostico_correto=True, direcao_correta=True, execucao_detalhada=False),

        PropostaUP(22, "violencia", "Julgamento e confisco de corruptos",
            "Julgamento, prisão e confisco dos bens de todos os corruptos.",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao="OPINIAO",
            diagnostico_correto=True, direcao_correta=True, execucao_detalhada=False),

        PropostaUP(23, "comunicacao", "Apoio à libertação dos povos",
            "Apoio à luta de todos os povos e países pela libertação da dominação capitalista e da espoliação imperialista.",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao="OPINIAO",
            diagnostico_correto=True, direcao_correta=True, execucao_detalhada=False),

        PropostaUP(24, "violencia", "Fim da polícia militar",
            "Pelo fim da polícia militar; fim de qualquer repressão aos movimentos sociais.",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao="OPINIAO",
            diagnostico_correto=True, direcao_correta=True, execucao_detalhada=False),

        PropostaUP(25, "violencia", "Punição de torturadores da ditadura",
            "Punição exemplar para os torturadores e assassinos da ditadura, revisão imediata da Lei da Anistia.",
            tem_como=False, tem_quem=False, tem_custo=False, tem_prazo=False, tem_metrica=False,
            tem_fonte_dados=False, tem_diagnostico=True,
            classificacao="OPINIAO",
            diagnostico_correto=True, direcao_correta=True, execucao_detalhada=False),
    ]


def _demo():
    propostas = _init_propostas()

    print("=" * 85)
    print("SIMULACAO: PROGRAMA DA UNIDADE POPULAR (Samara Martins) vs GATE WO")
    print("25 propostas reais de unidadepopular.org.br/programa")
    print("=" * 85)

    n_aprov = sum(1 for p in propostas if p.status == StatusGate.APROVADO)
    n_jeq = sum(1 for p in propostas if p.status == StatusGate.JEQUERI)
    n_wo = sum(1 for p in propostas if p.status == StatusGate.WO)

    print(f"\n25 propostas avaliadas")
    print(f"APROVADAS (7/7): {n_aprov}")
    print(f"JEQUERI (5/5 criticos): {n_jeq}")
    print(f"W.O. (<5 criticos): {n_wo}")

    print(f"\n{'='*85}")
    print("ANALISE POR 3 CAMADAS (diagnostico + direcao + execucao)")
    print(f"{'='*85}")
    n_diag = sum(1 for p in propostas if p.diagnostico_correto)
    n_dire = sum(1 for p in propostas if p.direcao_correta)
    n_exec = sum(1 for p in propostas if p.execucao_detalhada)
    print(f"  Diagnostico correto: {n_diag}/25")
    print(f"  Direcao correta:     {n_dire}/25")
    print(f"  Execucao detalhada:  {n_exec}/25")

    score_medio = sum(p.score_3_camadas for p in propostas) / len(propostas)
    print(f"  Score medio (diag2+dire2+exec1): {score_medio:.2f}/5.0")

    print(f"\n{'='*85}")
    print("PROPOSTA POR PROPOSTA")
    print(f"{'='*85}")
    for p in propostas:
        flag = ""
        if p.status == StatusGate.APROVADO: flag = " APROVADO"
        elif p.status == StatusGate.WO: flag = " W.O."
        print(f"\n  {p.n:>2}. [{p.area.upper()}] {p.titulo}")
        print(f"      Gate: {p.status.value}{flag} ({p.n_criticos}/5 criticos)")
        print(f"      Diag: {'OK' if p.diagnostico_correto else 'FALHA'} | Dire: {'OK' if p.direcao_correta else 'FALHA'} | Exec: {'OK' if p.execucao_detalhada else 'FALHA'}")
        print(f"      Score 3 camadas: {p.score_3_camadas:.2f}/5.0")
        print(f"      Texto: {p.texto_original[:80]}...")

    print(f"\n{'='*85}")
    print("VEREDITO")
    print(f"{'='*85}")
    print(f"""
  METODO GATE WO TRADICIONAL:
    0 de 25 aprovadas. 25 W.O.
    Nenhuma tem COMO, QUEM, CUSTO, PRAZO ou METRICA.

  METODO 3 CAMADAS (sem vies de acesso):
    Diagnostico: 25/25 corretos (100%)
    Direcao:     25/25 corretas (100%)
    Execucao:    0/25 detalhadas (0%)

  O QUE ISSO SIGNIFICA:
    A UP entende TODOS os problemas do Brasil.
    A UP aponta TODAS as direcoes corretas.
    Mas NAO detalha COMO executar nada.
    
  O vies: quem nao tem acesso a dados/equipe tecnica nao detalha execucao.
  O novo metodo nao pune isso. Mede separado.

  Score UP (3 camadas): {score_medio:.2f}/5.0
    = 100% diagnostico + 100% direcao + 0% execucao
    = (1.0*2 + 1.0*2 + 0.0*1) / 5 * 5 = 4.0/5.0

  COMPARACAO:
    Marina (Gate tradicional): 3.00/5.0 (3 aprovadas de 5)
    Marina (3 camadas):        ~4.5/5.0 (diag ok + dire ok + exec ok em 3)
    UP (Gate tradicional):     0.00/5.0 (0 aprovadas de 25)
    UP (3 camadas):            4.00/5.0 (diag 100% + dire 100% + exec 0%)
    
  A diferenca: Marina detalha execucao porque tem dados. UP nao detalha
  porque nao tem. Mas o diagnostico e a direcao da UP sao coerentes.
""")


if __name__ == "__main__":
    _demo()
