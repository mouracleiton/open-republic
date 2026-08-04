#!/usr/bin/env python3
"""
OpenPlanoGoverno -- Plano de Governo vs Raio X: Cumprimento + Lacunas
=======================================================================
"O plano de governo e uma promessa. O Raio X e a realidade.
 Cruzando os dois: o que foi cumprido, o que faltou, o que ninguem prometeu."
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple


class StatusCumprimento(Enum):
    CUMPRIDO = "cumprido"
    PARCIAL = "parcial"
    NAO_CUMPRIDO = "nao_cumprido"
    CONTRADIZ = "contradiz"        # fez o contrario
    SEM_DADO = "sem_dado"          # nao tem como medir

    @property
    def rotulo(self) -> str:
        return {
            "cumprido": "CUMPRIDO",
            "parcial": "PARCIAL",
            "nao_cumprido": "NAO CUMPRIDO",
            "contradiz": "CONTRADIZ (fez o contrario)",
            "sem_dado": "SEM DADO PARA MEDIR",
        }[self.value]


class CategoriaProposta(Enum):
    EXPANSAO = "expansao"          # ampliar algo existente
    CRIACAO = "criacao"            # criar do zero
    RECUPERACAO = "recuperacao"   # recuperar algo perdido
    REFORMA = "reforma"            # mudar estrutura
    EXTINCAO = "extincao"          # acabar com algo


@dataclass
class PropostaGoverno:
    """Uma proposta do plano de governo oficial."""
    id: str
    eixo: str                    # eixo tematico do plano
    proposta: str                # o que prometeram
    dominio_raiox: str           # qual dominio do Raio X corresponde
    status: StatusCumprimento
    dado_realidade: str          # o que o Raio X/dados dizem
    ano_meta: str                # prazo prometido
    fonte_promessa: str          # onde no plano esta
    prioridade_openrepublic: str = ""  # o que OpenRepublic recomenda


@dataclass
class LacunaGoverno:
    """O que FALTA no plano de governo -- problemas reais que ninguem prometeu tratar."""
    dominio_raiox: str
    problema: str                # o problema real
    dado_raiox: str              # o dado que comprova
    ausencia: str                # por que nao esta no plano
    recomendacao: str            # o que OpenRepublic propoe


class PlanoGovernoRaioX:
    """
    Cruza plano de governo (2023-2026) com Raio X do Brasil.
    """

    def __init__(self):
        self.propostas: List[PropostaGoverno] = []
        self.lacunas: List[LacunaGoverno] = []
        self._init_propostas()
        self._init_lacunas()

    def _init_propostas(self):
        """Plano de governo 2023-2026 cruzado com Raio X."""

        dados = [

            # === EIXO 1: COMBATE A FOME E POBREZA ===
            {"id": "p01", "eixo": "Combate a Fome",
             "proposta": "Revigorar o Bolsa Familia com R$600 + R$150 por crianca ate 7 anos",
             "dominio": "alimentacao", "status": "cumprido",
             "realidade": "BF restaurado. 21 milhoes de familias recebem. MAS: 33 milhoes ainda passam fome (VIGISAN 2022). Dinheiro entra, fome persiste. 17% das familias beneficiarias continuam em inseguranca alimentar.",
             "meta": "2023", "fonte": "Plano de Governo, Eixo Social",
             "recomendacao": "Rastreio individual por crianca. Verificar se R$ virou comida no prato (open_child_food_security)."},

            {"id": "p02", "eixo": "Combate a Fome",
             "proposta": "Recriar o CONSEA (Conselho Nacional de Seguranca Alimentar)",
             "dominio": "alimentacao", "status": "cumprido",
             "realidade": "CONSEA recriado em 2023. Mas CONSEA e consultivo, nao executa. Nenhum programa novo de alimentacao criado a partir dele.",
             "meta": "2023", "fonte": "Plano de Governo, Eixo Social"},

            {"id": "p03", "eixo": "Combate a Fome",
             "proposta": "Fortalecer o PNAE (merenda escolar)",
             "dominio": "alimentacao", "status": "parcial",
             "realidade": "Orcamento do PNAE aumentou para R$ 2.5 bi/ano. Mas 1.6 milhoes de criancas FORA da escola = sem merenda. Terceirizacao em 70% dos municipios. Qualidade nao medida.",
             "meta": "2026", "fonte": "Plano de Governo, Eixo Educacao"},

            # === EIXO 2: SAUDE ===
            {"id": "p04", "eixo": "Saude",
             "proposta": "Mais Medicos para o SUS",
             "dominio": "saude", "status": "parcial",
             "realidade": "Programa retomado. ~18 mil medicos. Mas cobertura ainda insuficiente. Interior e periferia seguem sem medico. Interrompido parcialmente em 2023 (cubanos).",
             "meta": "2023", "fonte": "Plano de Governo, Eixo Saude"},

            {"id": "p05", "eixo": "Saude",
             "proposta": "Recuperar calendario nacional de vacinacao",
             "dominio": "saude", "status": "nao_cumprido",
             "realidade": "Cobertura vacinal: 68% (2023). Meta: 95%. CAIU desde 2023. Sarampo reapareceu. Polio ameaca voltar. Nenhum plano nacional efetivo de recuperacao.",
             "meta": "2026", "fonte": "Plano de Governo, Eixo Saude",
             "recomendacao": "Campanha vacinal casa-a-casa com rastreio individual (open_censo_nacional)."},

            {"id": "p06", "eixo": "Saude",
             "proposta": "Investir R$ 25 bi em saneamento para saude",
             "dominio": "saneamento", "status": "parcial",
             "realidade": "Recurso liberado via PAC. Mas cobertura de esgoto: 53% (urbano). Rural: 15%. Ritmo: 0.8%/ano. Meta de 90% so chega em 2050.",
             "meta": "2026", "fonte": "Plano de Governo, Eixo Saude/Infra"},

            # === EIXO 3: EDUCACAO ===
            {"id": "p07", "eixo": "Educacao",
             "proposta": "Pais na Escola -- engajar familias na educacao",
             "dominio": "educacao", "status": "sem_dado",
             "realidade": "Programa anunciado. Sem metricas publicas de implementacao. Nao ha dado de adesao por municipio ou escola.",
             "meta": "2026", "fonte": "Plano de Governo, Eixo Educacao"},

            {"id": "p08", "eixo": "Educacao",
             "proposta": "Aumentar investimento em educacao para 6% do PIB",
             "dominio": "educacao", "status": "nao_cumprido",
             "realidade": "Brasil investe ~4.5% do PIB em educacao (2024). Meta: 6%. PISA 2022: 393/410/403 vs OCDE 472/476/485. 50% do 7o ano nao sabem ler.",
             "meta": "2026", "fonte": "Plano de Governo, Eixo Educacao",
             "recomendacao": "Censo escolar proprio (open_censo_escolar) com OSINT por escola. Saber onde o dinheiro chega."},

            # === EIXO 4: SEGURANCA PUBLICA ===
            {"id": "p09", "eixo": "Seguranca Publica",
             "proposta": "Plano Nacional de Seguranca Publica com foco em inteligencia e prevencao",
             "dominio": "violencia", "status": "parcial",
             "realidade": "Plano lancado em 2023. Homicidios: 21.7/100k (2023), caiu ~3%. Mas violencia domestica subnotificada 70%. SINESP com 6-12h de atraso. Nao previne, conta.",
             "meta": "2026", "fonte": "Plano de Governo, Eixo Seguranca"},

            {"id": "p10", "eixo": "Seguranca Publica",
             "proposta": "Recriar estrutura de prevencao a violencia (PRONASCI类似)",
             "dominio": "violencia", "status": "sem_dado",
             "realidade": "Sem programa estruturado de prevencao anunciado ou implementado com metricas. Foco continua em repressao.",
             "meta": "2026", "fonte": "Plano de Governo, Eixo Seguranca"},

            # === EIXO 5: ECONOMIA ===
            {"id": "p11", "eixo": "Economia",
             "proposta": "Novo Arcabouco Fiscal responsavel",
             "dominio": "inflacao", "status": "parcial",
             "realidade": "Arcabouco aprovado. IPCA 2023: 4.62%. Mas cesta basica subiu mais. Arroz +50%, feijao +30% em 2024. Pobre paga mais inflacao que o IPCA mede.",
             "meta": "2023", "fonte": "Plano de Governo, Eixo Economia"},

            {"id": "p12", "eixo": "Economia",
             "proposta": "Plano Safra recorde para agricultura familiar",
             "dominio": "agropecuaria", "status": "parcial",
             "realidade": "Plano Safra 2024/25: R$ 400 bi. PRONAF: R$ 60 bi. Mas agricultura familiar produz 70% da comida com 30% do credito. Demanda e 4x maior.",
             "meta": "anual", "fonte": "Plano de Governo, Eixo Economia"},

            # === EIXO 6: MEIO AMBIENTE ===
            {"id": "p13", "eixo": "Meio Ambiente",
             "proposta": "Zerar desmatamento ilegal na Amazonia ate 2030",
             "dominio": "ambiente", "status": "parcial",
             "realidade": "Desmatamento caiu 22% (2022->2023): 13.235 km2. Ainda 2x a meta. Ibama multa mas 80% das multas nao sao pagas.",
             "meta": "2030", "fonte": "Plano de Governo, Eixo Ambiente",
             "recomendacao": "Cruzar MapBiomas/INPE com denominacao de responsabilidade. Quem e dono da area desmatada?"},

            {"id": "p14", "eixo": "Meio Ambiente",
             "proposta": "Reativar Fundo Amazonia",
             "dominio": "ambiente", "status": "cumprido",
             "realidade": "Fundo Amazonia reativado em 2023. Doacoes retomadas (Noruega, Alemanha, EUA). R$ 3 bi disponiveis.",
             "meta": "2023", "fonte": "Plano de Governo, Eixo Ambiente"},

            # === EIXO 7: INDIGENA ===
            {"id": "p15", "eixo": "Povos Originarios",
             "proposta": "Demarcar terras indigenas e combater garimpo ilegal",
             "dominio": "indigena", "status": "nao_cumprido",
             "realidade": "Zero novas demarcacoes (Marco Temporal/STF 2023). 570 criancas Yanomami morreram de fome (2022-2023). Garimpo cresceu. Operacoes tmidas no Yanomami.",
             "meta": "2026", "fonte": "Plano de Governo, Eixo Indigena",
             "recomendacao": "Censo proprio indigena (open_censo_nacional, dominio indigena). Saude por DSEI com rastreio por aldeia."},

            # === EIXO 8: HABITACAO ===
            {"id": "p16", "eixo": "Habitacao",
             "proposta": "Retomar Minha Casa Minha Vida para baixa renda",
             "dominio": "habitacao", "status": "parcial",
             "realidade": "MCMV retomado em 2023. ~2 milhoes de unidades no PAC. Mas casas longe do centro = sem servicos. Favelas crescem mais rapido que construcao.",
             "meta": "2026", "fonte": "Plano de Governo, Eixo Habitacao"},

            # === EIXO 9: CULTURA ===
            {"id": "p17", "eixo": "Cultura",
             "proposta": "Reativar Ministerio da Cultura e Lei Rouanet",
             "dominio": "cultura", "status": "cumprido",
             "realidade": "MinC recriado. Lei Paulo Gustavo: R$ 3.8 bi. Lei Aldir Blanc 2: R$ 3 bi. Mas Lei Rouanet concentra 90% em 10% (ricos). Cultura periferica sem acesso.",
             "meta": "2023", "fonte": "Plano de Governo, Eixo Cultura"},

            # === EIXO 10: TRANSPORTE ===
            {"id": "p18", "eixo": "Transporte",
             "proposta": "PAC Mobilidade Urbana com metro/VLT",
             "dominio": "transporte", "status": "parcial",
             "realidade": "R$ 40 bi anunciados. Mas Brasil tem 10 linhas de metro vs 200+ em paises equivalentes. Pobre gasta 2h+ em transporte. Tarifa nao subsidiada federalmente.",
             "meta": "2026", "fonte": "Plano de Governo, Eixo Infra"},

            # === EIXO 11: COMUNICACAO ===
            {"id": "p19", "eixo": "Comunicacao",
             "proposta": "Democratizar acesso a internet (5G + rural)",
             "dominio": "comunicacao", "status": "nao_cumprido",
             "realidade": "5G lancado nas capitais. Mas 70% da zona rural SEM internet. PNBL extinto. Escola rural sem conexao. Nenhum plano federal de banda larga rural.",
             "meta": "2026", "fonte": "Plano de Governo, Eixo Digital",
             "recomendacao": "Conectividade escola-a-escola com OSINT (open_school_osint). Verificar quem tem internet de verdade."},

            # === EIXO 12: IGUALDADE RACIAL ===
            {"id": "p20", "eixo": "Igualdade Racial",
             "proposta": "Politicas afirmativas e combate ao racismo estrutural",
             "dominio": "violencia", "status": "sem_dado",
             "realidade": "Ministerio da Igualdade Racial criado. Programas anunciados. Mas homicidio de jovens negros: 2.7x maior que brancos. Sem metricas claras de impacto.",
             "meta": "2026", "fonte": "Plano de Governo, Eixo Igualdade"},
        ]

        for d in dados:
            self.propostas.append(PropostaGoverno(
                id=d["id"], eixo=d["eixo"], proposta=d["proposta"],
                dominio_raiox=d["dominio"],
                status=StatusCumprimento(d["status"]),
                dado_realidade=d["realidade"],
                ano_meta=d["meta"], fonte_promessa=d["fonte"],
                prioridade_openrepublic=d.get("recomendacao", ""),
            ))

    def _init_lacunas(self):
        """Problemas REAIS que o plano de governo NEM PROMETEU tratar."""

        self.lacunas = [
            LacunaGoverno(
                dominio_raiox="drogas",
                problema="Epidemia de crack e drogas sinteticas",
                dado_raiox="Drogas sinteticas cresceram 400% (2019-2024). So 17% dos dependentes tem tratamento. Lei de drogas eca racial.",
                ausencia="Plano nao menciona politica de reducao de danos. Zero novas unidades CAPS-AD.",
                recomendacao="Reducao de danos como politica de Estado. Tratamento como saude, nao seguranca."
            ),
            LacunaGoverno(
                dominio_raiox="saneamento",
                problema="47% do Brasil sem coleta de esgoto",
                dado_raiox="Cobertura: 53% urbano, 15% rural. Crianca continua morrendo de diarreia no Norte.",
                ausencia="Plano promete investimento mas nao tem meta de cobertura MENSURAVEL por municipio.",
                recomendacao="Censo de saneamento por escola/posto/bairro. Dado em tempo real, nao SNIS autopreenchido."
            ),
            LacunaGoverno(
                dominio_raiox="agua",
                problema="35 milhoes sem agua tratada",
                dado_raiox="Sertao: <30% tem agua potavel. Cisternas cobrem 33% da demanda.",
                ausencia="Plano nao tem meta de agua por regiao. Programa Cisternas oscila com governo.",
                recomendacao="Agua como prioridade de sobrevivencia (triagem INFRA). Meta: 100% agua potavel em 5 anos."
            ),
            LacunaGoverno(
                dominio_raiox="comunicacao",
                problema="70% da zona rural sem internet",
                dado_raiox="Escola rural sem conexao = sem EAD, sem telemedicina, sem servico publico digital.",
                ausencia="PNBL extinto. Plano atual nao substitui. 5G e para capital, nao para o sertao.",
                recomendacao="Internet como direito constituinte (P11 letramento digital). Banda larga rural por lei."
            ),
            LacunaGoverno(
                dominio_raiox="seguranca_alimentar",
                problema="Fome mede a cada 2 anos (VIGISAN bienal)",
                dado_raiox="33M com fome. Fome muda em dias, VIGISAN mede a cada 24 meses. dado obsoleto entre coletas.",
                ausencia="Plano nao propoe medicao continua. VIGISAN nao e prioridade de orcamento.",
                recomendacao="VIGISAN mensal + cestas basicas monitoradas por bairro (open_raio_x_brasil)."
            ),
            LacunaGoverno(
                dominio_raiox="violencia",
                problema="Violencia domestica subnotificada 70%",
                dado_raiox="1.8M medidas protetivas/ano. So 198 abrigos no Brasil. Cumprimento de medidas: ~40%.",
                ausencia="Plano nao tem meta de abrigos. Nao tem rastreio de cumprimento de medidas protetivas.",
                recomendacao="Monitor de violencia em tempo real (open_constitutional_monitor). Abrigo por lei em todo municipio >100k."
            ),
            LacunaGoverno(
                dominio_raiox="emprego",
                problema="40 milhoes na informalidade sem protecao",
                dado_raiox="Informal: ~40% da forca de trabalho. Sem seguro-desemprego, sem FGTS, sem direito trabalhista.",
                ausencia="Plano nao propoe rede de protecao para informal. Empreendedorismo individual nao e protecao social.",
                recomendacao="Renda basica universal como direito. Desvinculada de vinculo empregaticio."
            ),
            LacunaGoverno(
                dominio_raiox="indigena",
                problema="Saude indigena em colapso (Yanomami)",
                dado_raiox="570 criancas Yanomami mortas de fome (2022-2023). SASI-SUS subfinanciado. Garimpo cresce.",
                ausencia="Plano promete combater garimpo mas Marco Temporal impediu demarcacoes. Saude indigena sem medico.",
                recomendacao="Censo proprio por etnia. Saude por aldeia com rastreio. Garimpo como crime federal."
            ),
        ]

    def scorecard(self) -> Dict[str, Any]:
        total = len(self.propostas)
        counts = {"cumprido": 0, "parcial": 0, "nao_cumprido": 0, "contradiz": 0, "sem_dado": 0}
        for p in self.propostas:
            counts[p.status.value] += 1

        return {
            "modulo": "open_plano_governo",
            "versao": "0.1.0-spec",
            "propostas_avaliadas": total,
            "cumprimento": counts,
            "pct_cumprido": f"{counts['cumprido']}/{total} ({counts['cumprido']/total*100:.0f}%)",
            "pct_nao_cumprido": f"{counts['nao_cumprido']}/{total} ({counts['nao_cumprido']/total*100:.0f}%)",
            "pct_sem_dado": f"{counts['sem_dado']}/{total} ({counts['sem_dado']/total*100:.0f}%)",
            "lacunas_identificadas": len(self.lacunas),
            "veredito": (
                f"{counts['cumprido']} cumpridas, {counts['parcial']} parciais, "
                f"{counts['nao_cumprido']} nao cumpridas, {counts['sem_dado']} sem dado. "
                f"{len(self.lacunas)} problemas reais que o plano nem prometeu tratar."
            ),
        }

    def to_dict(self) -> Dict[str, Any]:
        return {
            "propostas": [{
                "id": p.id, "eixo": p.eixo, "proposta": p.proposta,
                "dominio": p.dominio_raiox, "status": p.status.value,
                "status_rotulo": p.status.rotulo,
                "realidade": p.dado_realidade, "meta": p.ano_meta,
                "fonte": p.fonte_promessa,
                "recomendacao": p.prioridade_openrepublic,
            } for p in self.propostas],
            "lacunas": [{
                "dominio": l.dominio_raiox, "problema": l.problema,
                "dado": l.dado_raiox, "ausencia": l.ausencia,
                "recomendacao": l.recomendacao,
            } for l in self.lacunas],
            "scorecard": self.scorecard(),
        }


def _demo():
    pg = PlanoGovernoRaioX()
    sc = pg.scorecard()

    print("=" * 70)
    print("PLANO DE GOVERNO vs RAIO X DO BRASIL")
    print("Cumprimento + Lacunas")
    print("=" * 70)

    print(f"\n{sc['propostas_avaliadas']} propostas avaliadas\n")

    # Cumprimento
    print("CUMPRIMENTO:")
    for p in pg.propostas:
        icon = {"cumprido": "OK", "parcial": "~~", "nao_cumprido": "XX",
                "contradiz": "!!", "sem_dado": "??"}[p.status.value]
        print(f"  [{icon}] {p.id} ({p.eixo}) {p.proposta[:60]}")

    print(f"\n{'='*70}")
    print(f"LACUNAS ({len(pg.lacunas)} problemas que o plano NEM PROMETEU):")
    for l in pg.lacunas:
        print(f"\n  [{l.dominio_raiox.upper()}]")
        print(f"    Problema: {l.problema}")
        print(f"    Dado: {l.dado_raiox[:80]}")
        print(f"    Recomendacao: {l.recomendacao[:80]}")

    print(f"\n{'='*70}")
    print("VEREDITO:")
    for k, v in sc.items():
        if k not in ("modulo", "versao"):
            print(f"  {k}: {v}")


if __name__ == "__main__":
    _demo()
