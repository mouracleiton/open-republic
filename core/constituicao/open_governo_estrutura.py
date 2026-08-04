#!/usr/bin/env python3
"""
OpenGovernoEstrutura -- Governo Republicano com Sensor
=========================================================
"Co-presidentes com mesmo poder. Sensor independente. Povo cobra."
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


class TipoCargo(Enum):
    CO_PRESIDENTE = "co_presidente"
    SENSOR = "sensor"
    MINISTRO = "ministro"
    CONSELHO_POVO = "conselho_povo"


class NivelAcesso(Enum):
    EXECUTIVO = "executivo"        # decide e executa
    SENSOR = "sensor"              # mede, nao decide
    POVO = "povo"                  # cobra, nao administra
    CONSULTIVO = "consultivo"      # opina, nao executa


@dataclass
class MembroGoverno:
    """Um membro do governo hipotetico."""
    nome: str
    cargo: TipoCargo
    nivel: NivelAcesso
    dominios_raiox: List[str]      # quais dominios do Raio X cobre
    score_capacidade: float         # score 0-5 (formula Camada 1+2+3)
    veredito_gate: str              # APROVADO / JEQUERI / WO
    responsabilidades: List[str]
    nao_pode: List[str]             # limites explicitos
    baground: str = ""              # quem e, de onde vem


class GovernoEstrutura:
    """
    Estrutura: 2 co-presidentes + sensor independente + conselho do povo.
    
    REGRA FUNDAMENTAL: o sensor nunca decide. Ilumina. O povo cobra.
    """

    def __init__(self):
        self.membros: List[MembroGoverno] = []
        self.regras: List[str] = []
        self._init_estrutura()

    def _init_estrutura(self):
        self.membros = [

            # === CO-PRESIDENTE 1 ===
            MembroGoverno(
                nome="Marina Silva",
                cargo=TipoCargo.CO_PRESIDENTE,
                nivel=NivelAcesso.EXECUTIVO,
                dominios_raiox=["ambiente", "agua", "alimentacao", "agropecuaria",
                                "saude", "educacao", "indigena", "energia"],
                score_capacidade=4.11,
                veredito_gate="APROVADO",
                responsabilidades=[
                    "Executar politicas publicas nos dominios do Raio X",
                    "Representar o Estado nacional e internacionalmente",
                    "Propor orcamento e plano de acao ao Conselho do Povo",
                    "Nomear ministros (com aprovacao do Gate WO)",
                    "Assinar decretos e leis aprovadas",
                ],
                nao_pode=[
                    "Alterar dados do Raio X (CRIME -- P5)",
                    "Esconder ou bloquear dados do sensor (CRIME -- P5+P13)",
                    "Decidir sozinho quando discordar do co-presidente",
                    "Usar Raio X para perseguir adversario politico (CRIME -- P13)",
                    "Nomear ministro que nao passe no Gate WO",
                ],
                baground="Seringueira do Acre. Reduziu desmatamento 80%. Criou Cisternas. Criou PAA. 3x candidata a presidente. Score: 4.11.",
            ),

            # === CO-PRESIDENTE 2 ===
            MembroGoverno(
                nome="Jones Manoel",
                cargo=TipoCargo.CO_PRESIDENTE,
                nivel=NivelAcesso.EXECUTIVO,
                dominios_raiox=["violencia", "emprego", "transporte", "habitacao",
                                "inflacao", "cultura"],
                score_capacidade=2.50,
                veredito_gate="WO (capacidade abaixo de 4.0, mas comunicador funcional)",
                responsabilidades=[
                    "Comunicar ao povo o estado real do pais (com dados do Raio X)",
                    "Cobrar ministros publicamente com dados na mao",
                    "Representar as ruas, os sindicatos, os movimentos",
                    "Liderar a comunicacao de governo (transparencia radical)",
                    "Conduzir audiencias publicas com dados abertos",
                ],
                nao_pode=[
                    "Alterar dados do Raio X (CRIME -- P5)",
                    "Esconder ou bloquear dados do sensor (CRIME -- P5+P13)",
                    "Decidir sozinho quando discordar do co-presidente",
                    "Usar Raio X como arma partidaria (CRIME -- P9)",
                    "Negar informacao ao povo (CRIME -- P5)",
                ],
                baground="Comunicador. YouTuber (~2M inscritos). 10+ anos de producao politica. Score: 2.50. Nunca administrou orgao publico. Forca: comunicacao e cobranca.",
            ),

            # === SENSOR INDEPENDENTE ===
            MembroGoverno(
                nome="Sensor (Raio X + Censo + Gate + Triage)",
                cargo=TipoCargo.SENSOR,
                nivel=NivelAcesso.SENSOR,
                dominios_raiox=["violencia", "saude", "alimentacao", "agua",
                                "saneamento", "educacao", "emprego", "inflacao",
                                "agropecuaria", "energia", "transporte", "habitacao",
                                "comunicacao", "ambiente", "indigena", "drogas",
                                "cultura", "seguranca_alimentar"],
                score_capacidade=5.0,
                veredito_gate="APROVADO (construiu o sistema)",
                responsabilidades=[
                    "Manter o Raio X rodando em 18 dominios em tempo real",
                    "Manter o Censo Proprio atualizado (tempo real a anual)",
                    "Aplicar o Gate Epistemologico (FATO/DADO/OPINIAO) em toda afirmacao",
                    "Aplicar o Checklist WO em toda proposta de governo",
                    "Aplicar a Triagem (VIDA/BOLSO/VOTO/ESTRUTURA) em toda crise",
                    "Manter o canal de denuncias tamper-proof ativo",
                    "Publicar dados em CC0 (ninguem e dono do dado)",
                    "ILUMINAR, NAO DECIDIR",
                ],
                nao_pode=[
                    "DECIDER (qualquer decisao executiva) -- CRIME DE ESTADO",
                    "Esconder dados do povo (CRIME -- P5)",
                    "Manipular dados (CRIME -- falsificacao)",
                    "Tomar partido politico (CRIME -- P9)",
                    "Silenciar denuncia (CRIME -- P5+canal_denuncia)",
                    "Privatizar o dado (CRIME -- CC0/P14)",
                ],
                baground="Perfil: engenheiro de sistemas. Quem constroi o motor, nao dirige o carro.",
            ),

            # === CONSELHO DO POVO ===
            MembroGoverno(
                nome="Conselho do Povo (Protesto Digital + Fisico)",
                cargo=TipoCargo.CONSELHO_POVO,
                nivel=NivelAcesso.POVO,
                dominios_raiox=["violencia", "saude", "alimentacao", "agua",
                                "saneamento", "educacao", "emprego", "inflacao",
                                "agropecuaria", "energia", "transporte", "habitacao",
                                "comunicacao", "ambiente", "indigena", "drogas",
                                "cultura", "seguranca_alimentar"],
                score_capacidade=5.0,
                veredito_gate="APROVADO (e o povo)",
                responsabilidades=[
                    "Acompanhar dados do Raio X publicados pelo Sensor",
                    "Cobrar co-presidentes e ministros com dados na mao",
                    "Protesto DIGITAL: viralizar, pressionar, denunciar online",
                    "Protesto FISICO: rua, greve, ocupacao, manifestacao",
                    "Denunciar desvio/corrupcao pelo canal tamper-proof",
                    "Verificar no campo (coleta comunitaria do censo proprio)",
                    "ASSINAR FATO (7 criterios) para virar politica",
                ],
                nao_pode=[
                    "Alterar dados do Raio X (so o Sensor tecnicamente pode)",
                    "Usar dados falsos para protestar (Gate Epistemologico)",
                    "Violencia (protesto pacifico e direito, violencia e crime)",
                    "Condicionar ajuda a partisanismo (P9)",
                ],
                baground="Perfil: cidadao comum com dado na mao. O juiz final.",
            ),
        ]

        self.regras = [
            "1. CO-PRESIDENTES TEM MESMO PODER. Nenhum dita o ritmo do outro.",
            "2. SE DISCORDAM: o dado do Raio X ilumina qual dominio e mais urgente. O povo cobra. A rua decide.",
            "3. SENSOR NAO DECIDE. Mede, ilumina, publica. Decidir e CRIME DE ESTADO.",
            "4. O POVO E O JUIZ. Com dados na mao, cobra digital e fisicamente.",
            "5. TODA PROPOSTA PASSA PELO GATE WO. Sem COMO/POR QUEM/QUANTO/PRAZO/METRICA = desclassificada.",
            "6. TODA AFIRMACAO DE GOVERNO PASSA PELO GATE EPISTEMOLOGICO. Opiniao nunca vira politica.",
            "7. TODA CRISE PASSA PELA TRIAGEM. VIDA age agora. BOLSO diagnostica. VOTO bloqueia ate FATO.",
            "8. TODA DADOS SAO CC0. Ninguem e dono do dado do pais.",
            "9. ALTERAR OU ESCONDER DADO DO RAIO X E CRIME EQUIVALENTE A FALSIFICACAO DOCUMENTAL.",
            "10. MINISTRO QUE NAO PASSA NO GATE WO NAO TOMA POSSE. Sem excecao.",
            "11. O SENSOR E INDEPENDENTE. Nao responde a co-presidentes. Responde ao DADO.",
            "12. O CONSELHO DO POVO ACIONA O SENSOR POR DEMANDA. Qualquer cidadao pode pedir dado.",
        ]

    def fluxo_decisao(self, proposta: str, dominio: str) -> List[str]:
        """Como uma proposta passa pelo sistema."""
        return [
            "1. Proposta chega -> Checklist WO (7 criterios)",
            "   Se WO: arquivada. Fim.",
            "   Se JEQUERI: devolvida para correcao.",
            "   Se APROVADO: avanca.",
            "",
            "2. Proposta aprovada -> Gate Epistemologico",
            "   Opiniao? Descartada.",
            "   Dado? Precisa de mais verificacao.",
            "   FATO (7 criterios)? Vira politica.",
            "",
            "3. Politica aprovada -> Triagem Operacional",
            f"   Dominio: {dominio}",
            "   VIDA? Age agora, mede depois.",
            "   BOLSO? Diagnostica primeiro.",
            "   VOTO? Bloqueia ate FATO.",
            "   ESTRUTURA? Trata + diagnostica simultaneo.",
            "",
            "4. Execucao -> Sensor mede em tempo real",
            "   Raio X acompanhando indicadores do dominio",
            "   Rastreio individual do beneficiario",
            "   Dado publicado em CC0",
            "",
            "5. Resultado -> Povo cobra",
            "   Melhorou? Povo ve. Governo ganha credito.",
            "   Piorou? Povo ve. Protesto digital + fisico.",
            "   Desvio? Denuncia tamper-proof. Investigacao.",
            "",
            "6. Avaliacao -> Politica e renovada ou extinta",
            "   Funcionou (FATO)? Renova orcamento.",
            "   Nao funcionou? Extinta. Dinheiro vai pra outra.",
            "   Sem dado? Sem renovacao.",
        ]

    def scorecard(self) -> Dict[str, Any]:
        return {
            "modulo": "open_governo_estrutura",
            "versao": "0.1.0-spec",
            "estrutura": "2 co-presidentes + sensor independente + conselho do povo",
            "membros": len(self.membros),
            "regras": len(self.regras),
            "principio_base": "Sensor ilumina. Povo cobra. Co-presidentes executam.",
            "fluxo": "Proposta -> WO -> FATO -> Triagem -> Execucao -> Medicao -> Cobranca -> Renovacao/Extincao",
        }


def _demo():
    gov = GovernoEstrutura()
    sc = gov.scorecard()

    print("=" * 70)
    print("GOVERNO REPUBLICANO COM SENSOR")
    print("2 co-presidentes + sensor independente + conselho do povo")
    print("=" * 70)

    print(f"\n{sc['regras']} regras fundamentais\n")

    print("MEMBROS:")
    for m in gov.membros:
        print(f"\n  [{m.cargo.value.upper()}] {m.nome}")
        print(f"    Score: {m.score_capacidade} | Gate: {m.veredito_gate}")
        print(f"    Dominios: {', '.join(m.dominios_raiox[:5])}{'...' if len(m.dominios_raiox)>5 else ''}")
        print(f"    Responsabilidades ({len(m.responsabilidades)}):")
        for r in m.responsabilidades[:3]:
            print(f"      + {r}")
        print(f"    NAO PODE ({len(m.nao_pode)}):")
        for n in m.nao_pode[:2]:
            print(f"      X {n}")

    print(f"\n{'='*70}")
    print("REGRAS FUNDAMENTAIS:")
    for r in gov.regras:
        print(f"\n  {r}")

    print(f"\n{'='*70}")
    print("FLUXO DE DECISAO:")
    for p in gov.fluxo_decisao("Hipotetica", "alimentacao"):
        print(f"  {p}")


if __name__ == "__main__":
    _demo()
