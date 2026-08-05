#!/usr/bin/env python3
"""
OpenPartidoUnificado -- Partido Comunista Unificado do Brasil
================================================================
"Não soma o que cada partido quer. Soma o que resolve o problema."
Pega o melhor de cada um. Descarta o resto. Um partido. Uma agenda.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Tuple
from collections import defaultdict


# ============================================================
# O QUE CADA PARTIDO APORTA DE MELHOR
# ============================================================

@dataclass
class AportePartido:
    """O melhor de cada partido, sem o pior."""
    partido: str
    lider: str
    o_que_aporta: str          # o MELHOR que esse partido faz
    a_quem_serve: str          # qual segmento da população
    score_capacidade: float
    cargo_no_partido_unificado: str

    # O que NÃO entra no partido unificado
    descartado: str


def _init_aportes() -> List[AportePartido]:
    return [
        AportePartido("UP", "Samara Martins",
            "Programa de 25 pontos. Diagnóstico 100%. Base MTST/periferia. Autossustentação.",
            "Famintos, periferia, sem-teto",
            1.50, "Secretaria-Geral do Programa",
            "Falta de equipe técnica (suprida pela coalizão)"),

        AportePartido("PCB", "Jones Manoel",
            "Comunicação (~2M). Análise econômica. 10 anos de coerência. Coerência socialista.",
            "Juventude, trabalhadores, periferia",
            2.50, "Coordenação de Comunicação e Mobilização",
            "Isolamento eleitoral (0 representantes)"),

        AportePartido("PT", "Camilo Santana / Haddad",
            "Máquina executiva. Ministério. Quadros técnicos. Experiência de governo.",
            "Nordeste, idosos, trabalhador formal",
            4.03, "Coordenação Executiva (Gestão Pública)",
            "Reformismo/concessões ao capital (descartado)"),

        AportePartido("PSOL", "Sonia Guajajara",
            "Direitos humanos. Indígena. LGBTQIA+. Mobilização de rua. Visibilidade.",
            "Indígenas, LGBTQIA+, mulheres",
            2.67, "Secretaria de Direitos e Diversidade",
            "Fragmentação interna (descartado)"),

        AportePartido("PCdoB", "Jandira Feghali",
            "Saúde técnica. Mais Médicos. Educação. Quadros profissionais.",
            "Idosos, SUS, estudantes",
            3.00, "Secretaria de Saúde e Educação",
            "Aliança automática com PT (absorvida)"),

        AportePartido("REDE", "Marina Silva",
            "Ambiente. Cisternas. PPCDAm (-80%). PAA. CONSEA. Amazônia.",
            "Nordeste rural, ribeirinhos, Amazônia",
            4.11, "Secretaria de Ambiente e Soberania",
            "Posição sobre drogas/aborto (descartada pela base)"),

        AportePartido("PDT", "Ciro Gomes",
            "Infraestrutura. Transposição. Ferrovias. Desenvolvimento nacional.",
            "Nordeste, interior, trabalhador industrial",
            3.81, "Secretaria de Infraestrutura e Energia",
            "Base empresarial/agrícola (descartada)"),

        AportePartido("PSTU", "—",
            "Sindicalismo de base. Crítica anticapitalista. Mobilização operária.",
            "Trabalhadores industriais",
            1.30, "Secretaria Sindical (consultiva)",
            "Intransigência eleitoral (descartada)"),

        AportePartido("PCO", "—",
            "Nada executivo. Apenas observador crítico.",
            "Nenhum (sem base)",
            1.20, "Observador (sem cargo)",
            "Tudo (não aporta execução)"),
    ]


# ============================================================
# O PARTIDO UNIFICADO
# ============================================================

@dataclass
class ComissaoCentral:
    """A coordenação do partido unificado. Um cargo por função."""
    cargo: str
    ocupante_partido: str
    ocupante_nome: str
    funcao: str
    score_capacidade: float


COMISSAO_CENTRAL = [
    ComissaoCentral("Secretaria-Geral", "UP", "Samara Martins",
        "Coordena o programa. Nó central. Diagnóstico e direção.", 1.50),
    ComissaoCentral("Comunicação", "PCB", "Jones Manoel",
        "Comunica ao povo. Mobiliza. Cobre. 10 anos de coerência.", 2.50),
    ComissaoCentral("Gestão Executiva", "PT", "Camilo Santana / Haddad",
        "Máquina. Ministério. Quadros técnicos. Sabe governar.", 4.03),
    ComissaoCentral("Direitos e Diversidade", "PSOL", "Sonia Guajajara",
        "Indígena. LGBTQIA+. Mulheres. Rua.", 2.67),
    ComissaoCentral("Saúde e Educação", "PCdoB", "Jandira Feghali",
        "SUS. Mais Médicos. Escola. Quadros.", 3.00),
    ComissaoCentral("Ambiente e Soberania", "REDE", "Marina Silva",
        "Amazônia. Cisternas. PAA. -80% desmatamento.", 4.11),
    ComissaoCentral("Infraestrutura", "PDT", "Ciro Gomes",
        "Estradas. Ferrovias. Transposição. Energia.", 3.81),
    ComissaoCentral("Sensores Independente", "—", "OpenRepublic",
        "Raio X. Censo. Gate. Triage. Ilumina, não decide.", 5.00),
]


# ============================================================
# O PROGRAMA UNIFICADO: O MELHOR DE CADA UM
# ============================================================

@dataclass
class PoliticaUnificada:
    """Uma política do programa unificado."""
    eixo: str
    titulo: str
    o_que_fazer: str
    quem_aporta: str           # qual partido aporta a capacidade
    quem_executa: str          # qual partido poe a mão na massa
    custo: str
    prazo: str
    meta: str
    pessoas_resolvidas_milhoes: float
    cobertura_pct: float

    @property
    def status(self) -> str:
        return "RESOLVIDO" if self.cobertura_pct >= 75 else ("PARCIAL" if self.cobertura_pct >= 50 else "FALHA")


def _init_programa() -> List[PoliticaUnificada]:
    return [
        # EMERGENCIAS
        PoliticaUnificada("alimentacao", "Fome Zero com rastreio individual",
            "PAA+CONSEA+VIGISAN+BF R$700+merenda local+rastreio criança-até-prato.",
            "REDE (PAA/CONSEA) + PT (BF) + UP (rastreio)",
            "REDE coordena. PT executa BF. UP executa rastreio.",
            "R$ 50 bi/ano", "2 anos", "0 (fome zero)",
            28.0, 85),

        PoliticaUnificada("agua", "Água universal + cisternas + esgoto",
            "1M cisternas. Saneamento estatizado. 90% esgoto. Mercúrio zero.",
            "REDE (cisternas) + PDT (infraestrutura)",
            "REDE coordena. PDT constrói.",
            "R$ 55 bi/ano", "4 anos", "0 sem água",
            26.0, 75),

        PoliticaUnificada("violencia", "Desmilitarização + prevenção",
            "PM->Comunitária. Prevenção>Repressão. Desarmamento. Conselhos populares.",
            "PSOL (direitos) + PCdoB (saúde mental) + PT (transição)",
            "PT executa transição. PSOL monitora direitos.",
            "R$ 20 bi/ano", "4 anos", "<15.000 homicídios/ano",
            28.5, 60),

        PoliticaUnificada("saude", "SUS 8% PIB + Mais Médicos + fim planos",
            "Dobrar SUS. Mais Médicos expandido. Fim planos. Dengue. Triagem.",
            "PCdoB (SUS/Mais Médicos) + PT (ministério)",
            "PCdoB coordena. PT aporta ministério.",
            "R$ 80 bi/ano", "4 anos", "Fila <30 dias",
            99.0, 70),

        PoliticaUnificada("soberania_alimentar", "Trigo + fertilizantes + sementes",
            "Produção nacional de trigo. Fertilizantes nacionais. Sementes crioulas.",
            "UP (reforma agrária) + PCB (planificação) + PT (EMBRAPA)",
            "PT executa via EMBRAPA. UP reforma terra. PCB planifica.",
            "R$ 20 bi/ano", "4 anos", "50% trigo nacional",
            100.0, 50),

        # ALTA
        PoliticaUnificada("educacao", "Escola integral + professor R$8k + censo próprio",
            "Escola 7h-17h. Piso R$8k. Censo escolar. Currículo P1-P14 (cordel, capoeira).",
            "PCdoB (educação) + PT (Camilo) + PCB (currículo popular)",
            "PT executa. PCdoB coordena. PCB aporta currículo.",
            "R$ 150 bi/ano", "4 anos", "PISA 450",
            32.5, 65),

        PoliticaUnificada("emprego", "Emprego garantido + jornada 6h + renda mínima",
            "Programa Nacional de Emprego Popular. Jornada 6h. Renda mínima R$2.600.",
            "PCB (coordena) + PT (executa obras) + PSTU (sindical)",
            "PT executa. PCB coordena. PSTU mobiliza.",
            "R$ 120 bi/ano", "4 anos", "<4% desemprego",
            4.7, 55),

        PoliticaUnificada("economia", "Nacionalização bancária + ISF + auditoria dívida",
            "Nacionalização gradual. ISF 1%+R$10M. Auditoria. Planificação. Remessas.",
            "PCB (planificação) + UP (programa) + PT (transição gradual)",
            "PT executa transição. PCB coordena plano. UP aporta programa.",
            "R$ 200 bi/ano ganho", "4 anos", "Spread <5%",
            100.0, 50),

        # MÉDIA
        PoliticaUnificada("ambiente", "PPCDAm + Amazônia + extrativismo",
            "PPCDAm reativado. Controle popular. Economia extrativista. Transição energética.",
            "REDE (PPCDAm) + PSOL (indígena) + PDT (energia)",
            "REDE coordena. PSOL protege terras. PDT faz transição.",
            "R$ 30 bi/ano", "4 anos", "<3.000 km²/ano",
            18.8, 75),

        PoliticaUnificada("indigena", "Demarcação + saúde + escola bilíngue",
            "251 terras. DSEI fortalecido. Escolas bilíngues. Mercúrio zero.",
            "PSOL (Sonia) + REDE (apoio) + PCdoB (saúde)",
            "PSOL coordena. PCdoB aporta saúde.",
            "R$ 5 bi/ano", "2 anos", "251 demarcadas",
            1.4, 80),

        PoliticaUnificada("agropecuaria", "Reforma agrária + agricultura familiar + fim agrotóxicos",
            "Nacionalização da terra. 500M famílias. Cooperativas. Agroecologia.",
            "UP (nacionalização) + REDE (familiar) + PCB (planificação)",
            "UP coordena. REDE executa cooperativas. PCB planifica.",
            "R$ 15 bi/ano", "4 anos", "Gini <0.6",
            8.3, 55),

        PoliticaUnificada("energia", "Reestatização + tarifa social + solar favela",
            "Petrobras 100% estatal. Tarifa social. Solar comunitária.",
            "PDT (infraestrutura) + PCB (estatização) + REDE (solar)",
            "PDT executa. PCB coordena estatização. REDE faz solar.",
            "R$ 80 bi/ano", "4 anos", "Tarifa social universal",
            60.0, 60),

        PoliticaUnificada("transporte", "Estatização + tarifa zero + frota elétrica + ferrovias",
            "Municipalização. Tarifa zero. Frota elétrica BR. Ferrovias.",
            "PDT (ferrovias) + UP (estatização)",
            "PDT executa. UP coordena estatização.",
            "R$ 40 bi/ano", "4 anos", "+50% passageiros",
            32.5, 65),

        PoliticaUnificada("habitacao", "Imóveis vazios + 4M moradias + reforma urbana",
            "Uso ou perda. Cooperativas. Caixa financiando. Reforma urbana.",
            "UP (imóveis vazios) + PT (MCMV) + PSOL (reforma urbana)",
            "PT executa construção. UP coordena ocupação.",
            "R$ 35 bi/ano", "4 anos", "Déficit zero",
            6.0, 75),

        PoliticaUnificada("saneamento", "Estatização + coleta universal",
            "Marco Legal revertido. Estatização. 90% esgoto. Coleta seletiva.",
            "PT (estatização) + PDT (infraestrutura)",
            "PT coordena. PDT constrói.",
            "R$ 25 bi/ano", "4 anos", "90% esgoto",
            70.0, 70),

        PoliticaUnificada("drogas", "Redução de danos + descriminalização",
            "Caps AD. Equipes de rua. Naloxona. Descriminalização do uso.",
            "PSOL (direitos) + PCdoB (saúde)",
            "PCdoB executa saúde. PSOL coordena política.",
            "R$ 8 bi/ano", "4 anos", "100% com tratamento",
            6.0, 60),

        PoliticaUnificada("cultura", "Cotização 40% + financiamento direto + cordel",
            "Conteúdo 40% nacional. Bolsa direta. Cordel/capoeira no currículo.",
            "PCB (nacionalização) + PSOL (cultura popular)",
            "PCB coordena. PSOL executa cultura.",
            "R$ 3 bi/ano", "2 anos", "50% nacional",
            16.5, 55),

        PoliticaUnificada("comunicacao", "Democratização + internet rural + fim doação empresa",
            "Quebra monopólio. Concessões públicas. Internet rural. Fim PJ.",
            "PCB (democratização) + PSOL (apoio) + PT (internet)",
            "PCB coordena. PT executa internet.",
            "R$ 5 bi/ano", "4 anos", "Herfindahl <0.3",
            35.0, 50),
    ]


# ============================================================
# O PARTIDO UNIFICADO
# ============================================================

class PartidoUnificado:
    """
    Partido Comunista Unificado do Brasil.
    Pega o melhor de cada um. Descarta o resto.
    """

    def __init__(self):
        self.aportes = _init_aportes()
        self.comissao = COMISSAO_CENTRAL
        self.programa = _init_programa()

    def scorecard(self) -> Dict[str, Any]:
        total_sofrendo = sum(p.pessoas_resolvidas_milhoes / (p.cobertura_pct / 100) for p in self.programa)
        total_resolvido = sum(p.pessoas_resolvidas_milhoes for p in self.programa)
        n_resolvidos = sum(1 for p in self.programa if p.status == "RESOLVIDO")
        n_parcial = sum(1 for p in self.programa if p.status == "PARCIAL")
        n_falha = sum(1 for p in self.programa if p.status == "FALHA")

        return {
            "modulo": "open_partido_unificado",
            "versao": "0.1.0-spec",
            "nome": "Partido Comunista Unificado do Brasil",
            "sigla": "PCU-B",
            "n_partidos_fundadores": len(self.aportes),
            "comissao_central": len(self.comissao),
            "politicas_total": len(self.programa),
            "eixos_resolvidos": n_resolvidos,
            "eixos_parciais": n_parcial,
            "eixos_falha": n_falha,
            "pessoas_resolvidas_milhoes": round(total_resolvido, 1),
            "cobertura_media": round(total_resolvido / total_sofrendo * 100, 1) if total_sofrendo else 0,
            "custo_anual": "R$ ~520 bilhoes/ano (financiado por ISF + nacionalização + fim subsídios)",
        }


def _demo():
    pu = PartidoUnificado()
    sc = pu.scorecard()

    print("=" * 95)
    print(f"PARTIDO COMUNISTA UNIFICADO DO BRASIL (PCU-B)")
    print(f"O melhor de 9 partidos. Descarta o resto. Um partido. Uma agenda.")
    print("=" * 95)

    print(f"""
  {sc['n_partidos_fundadores']} partidos fundadores -> 1 partido unificado
  {sc['comissao_central']} cargos na Comissão Central
  {sc['politicas_total']} políticas no programa unificado
  Score médio da comissão: {sum(c.score_capacidade for c in pu.comissao) / len(pu.comissao):.2f}/5.0

  PESSOAS RESOLVIDAS: {sc['pessoas_resolvidas_milhoes']} milhões
  COBERTURA MÉDIA: {sc['cobertura_media']}%

  CUSTO ANUAL: {sc['custo_anual']}
""")

    print(f"{'='*95}")
    print("COMISSÃO CENTRAL (o melhor de cada partido)")
    print(f"{'='*95}")
    for c in pu.comissao:
        score_bar = "#" * int(c.score_capacidade)
        print(f"\n  [{c.cargo}]")
        print(f"    Partido: {c.ocupante_partido} | Nome: {c.ocupante_nome} | Score: {c.score_capacidade:.1f} [{score_bar}]")
        print(f"    Função: {c.funcao}")

    print(f"\n{'='*95}")
    print("O QUE CADA PARTIDO APORTA (e o que é descartado)")
    print(f"{'='*95}")
    for a in pu.aportes:
        print(f"\n  [{a.partido}] {a.lider} (score {a.score_capacidade:.1f})")
        print(f"    APORTA: {a.o_que_aporta}")
        print(f"    SERVE A: {a.a_quem_serve}")
        print(f"    CARGO: {a.cargo_no_partido_unificado}")
        print(f"    DESCARTADO: {a.descartado}")

    print(f"\n{'='*95}")
    print("PROGRAMA UNIFICADO: 18 EIXOS, O MELHOR DE CADA UM")
    print(f"{'='*95}")
    for p in pu.programa:
        bar = "#" * int(p.cobertura_pct / 5)
        flag = " *** RESOLVIDO" if p.status == "RESOLVIDO" else (" *** FALHA" if p.status == "FALHA" else "")
        print(f"""
  [{p.eixo.upper()}] {p.titulo} {flag}
    FAZER: {p.o_que_fazer[:75]}
    APORTA: {p.quem_aporta}
    EXECUTA: {p.quem_executa}
    CUSTO: {p.custo} | PRAZO: {p.prazo} | META: {p.meta}
    RESOLVE: {p.pessoas_resolvidas_milhoes:.1f}M ({p.cobertura_pct}%) [{bar}]""")

    print(f"\n{'='*95}")
    print("VEREDITO")
    print(f"{'='*95}")
    print(f"""
  9 partidos viraram 1.

  COMISSÃO CENTRAL:
    Secretaria-Geral: UP (Samara) -- programa
    Comunicação: PCB (Jones) -- mobilização
    Executivo: PT (Camilo/Haddad) -- governo
    Direitos: PSOL (Sonia) -- indígena/diversidade
    Saúde/Educação: PCdoB (Jandira) -- SUS
    Ambiente: REDE (Marina) -- Amazônia
    Infraestrutura: PDT (Ciro) -- estradas/energia
    Sensor: OpenRepublic -- Raio X

  O QUE MUDA:
    PT perde o reformismo. Ganha máquina executiva.
    PCB perde o isolamento. Ganha canal de 2M.
    UP perde a falta de equipe. Ganha programa de 25 pontos.
    PSOL perde fragmentação. Ganha foco em direitos.
    PCdoB perde aliança automática. Ganha saúde + educação.
    REDE perde divergência em drogas. Ganha Amazônia.
    PDT perde base empresarial. Ganha infraestrutura nacional.

  NINGUÉM FAZ SOZINHO. TODOS FAZEM JUNTOS.

  A única métrica: {sc['pessoas_resolvidas_milhoes']:.0f} milhões param de sofrer.
  Falta: {(100 - sc['cobertura_media']):.0f}% ainda sofrendo.

  Partido é ferramenta. População é fim.
""")


if __name__ == "__main__":
    _demo()
