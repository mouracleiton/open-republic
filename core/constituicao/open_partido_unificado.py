#!/usr/bin/env python3
"""
OpenPartidoUnificado -- Partido Comunista Unificado do Brasil (PCU-B)
=======================================================================
Sem siglas. Sem "eu sou do X". Só gente que sabe fazer algo servindo a um programa.
A sigla morreu. O cargo fica. A habilidade fica. O nome fica.

AVISO: TODOS os nomes sao MOCK (placeholder).
A composicao final so e definida apos analise individual
pelo Gate WO + score de capacidade + triangulacao de fontes.
O sistema de medicao e REAL. As pessoas sao HIPOTETICAS.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List
from collections import defaultdict


# ============================================================
# PESSOAS COM HABILIDADES (sem sigla, sem partido)
# ============================================================

@dataclass
class Pessoa:
    """Uma pessoa que sabe fazer algo. Sem sigla."""
    nome: str
    origem: str                    # de onde veio (histórico, não identidade)
    habilidade: str                # o que sabe fazer
    serve_a: str                   # a quem serve
    score_capacidade: float
    cargo: str                     # o que faz no partido unificado
    descartado: str                # o que NÃO entra (vício da origem)


def _init_pessoas() -> List[Pessoa]:
    return [
        Pessoa("Samara Martins", "movimento popular",
            "Programa de 25 pontos. Diagnóstico 100%. Base MTST/periferia.",
            "Famintos, periferia, sem-teto",
            1.50, "Secretaria-Geral do Programa",
            "Falta de equipe técnica (suprida pela coalizão)"),

        Pessoa("Jones Manoel", "comunicação política",
            "Comunicação (~2M). Análise econômica. 10 anos de coerência.",
            "Juventude, trabalhadores",
            2.50, "Coordenação de Comunicação e Mobilização",
            "Intransigência eleitoral"),

        Pessoa("Camilo Santana", "gestão pública (educação)",
            "Governador 2x. IDEB subiu. Vacinação 95%. Sabe governar educação.",
            "Nordeste, educação",
            4.72, "Secretaria de Educação",
            "Restrição: sem cargo de chefe de Estado (definido pelo sensor)"),

        Pessoa("Fernando Haddad", "economia e planejamento",
            "Ministro Fazenda. Prefeito SP. Técnico. Planificação econômica.",
            "Trabalhador formal, economia",
            4.03, "Secretaria de Economia e Planejamento",
            "Restrição: sem cargo de chefe de Estado (definido pelo sensor)"),

        Pessoa("Sonia Guajajara", "direitos e diversidade",
            "Liderança indígena. APIB. Ministério. Visibilidade.",
            "Indígenas, LGBTQIA+, mulheres",
            2.67, "Secretaria de Direitos e Diversidade",
            "Fragmentação interna"),

        Pessoa("Jandira Feghali", "saúde",
            "Médica. Deputada. Coerência. Saúde pública.",
            "Idosos, SUS",
            3.00, "Secretaria de Saúde",
            "Aliança automática com qualquer sigla"),

        Pessoa("Orlando Silva", "educação e esporte",
            "Ministro Esporte. Professor. Educação popular.",
            "Juventude, estudantes",
            2.83, "Secretaria de Educação e Esporte",
            "Sub-representação eleitoral"),

        Pessoa("Marina Silva", "ambiente e soberania",
            "Ministra. -80% desmatamento. Cisternas. PAA. CONSEA.",
            "Nordeste rural, Amazônia, ribeirinhos",
            4.11, "Secretaria de Ambiente e Soberania",
            "Posição sobre drogas/aborto (descartada pela base)"),

        Pessoa("Ciro Gomes", "infraestrutura",
            "Governador. Ministro. Transposição. Ferrovias. Desenvolvimento.",
            "Nordeste, interior, indústria",
            3.81, "Secretaria de Infraestrutura e Energia",
            "Base empresarial/agrícola"),

        Pessoa("Flavio Dino", "justiça e segurança",
            "Governador. Reduziu homicídios. Ministro Justiça. STF.",
            "Nordeste, segurança pública",
            4.14, "Secretaria de Justiça e Segurança",
            "Centralização de poder"),

        Pessoa("Paulo Paim", "trabalho e previdência",
            "Senador 5x. Sindicalista. 30 anos direitos trabalhistas.",
            "Trabalhadores, aposentados",
            3.17, "Secretaria de Trabalho e Previdência",
            "Tempo excessivo no mesmo cargo"),

        Pessoa("Patrus Ananias", "cidades e habitação",
            "Ministro Cidades 2x. Minha Casa Minha Vida. Saneamento.",
            "Sem-moradia, periferia urbana",
            3.29, "Secretaria de Cidades e Habitação",
            "Filiação partidária automática"),

        Pessoa("Erika Hilton", "direitos humanos",
            "Deputada. Vereadora. Primeira transexual eleita.",
            "LGBTQIA+, periferia",
            1.67, "Subsecretaria de Direitos Humanos",
            "Falta de experiência executiva"),

        Pessoa("Luiza Erundina", "cultura",
            "Prefeita SP. 30 anos coerência. Educação, saúde, cultura.",
            "Cultura popular, periferia",
            3.13, "Secretaria de Cultura",
            "Idade (mas coerência compensa)"),
    ]


# ============================================================
# O PROGRAMA: O QUE A COALIZÃO FAZ PELA POPULAÇÃO
# ============================================================

@dataclass
class PoliticaUnificada:
    """Uma política do programa. Sem sigla. Com nome de quem executa."""
    eixo: str
    titulo: str
    o_que_fazer: str
    quem_coordena: str           # nome da pessoa
    quem_executa: str            # nome da pessoa
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
        PoliticaUnificada("alimentacao", "Fome Zero com rastreio individual",
            "PAA+CONSEA+VIGISAN+BF R$700+merenda local+rastreio criança-até-prato.",
            "Marina Silva", "Samara Martins",
            "R$ 50 bi/ano", "2 anos", "0 (fome zero)", 28.0, 85),

        PoliticaUnificada("agua", "Água universal + cisternas + esgoto",
            "1M cisternas. Saneamento estatizado. 90% esgoto. Mercúrio zero.",
            "Marina Silva", "Ciro Gomes",
            "R$ 55 bi/ano", "4 anos", "0 sem água", 26.0, 75),

        PoliticaUnificada("violencia", "Desmilitarização + prevenção",
            "PM->Comunitária. Prevenção>Repressão. Desarmamento. Conselhos.",
            "Flavio Dino", "Jones Manoel",
            "R$ 20 bi/ano", "4 anos", "<15.000 homicídios/ano", 28.5, 60),

        PoliticaUnificada("saude", "SUS 8% PIB + Mais Médicos + fim planos",
            "Dobrar SUS. Mais Médicos. Fim planos. Dengue. Triagem.",
            "Jandira Feghali", "Camilo Santana",
            "R$ 80 bi/ano", "4 anos", "Fila <30 dias", 99.0, 70),

        PoliticaUnificada("soberania_alimentar", "Trigo + fertilizantes + sementes",
            "Produção nacional. Fertilizantes. Sementes crioulas.",
            "Samara Martins", "Camilo Santana",
            "R$ 20 bi/ano", "4 anos", "50% trigo nacional", 100.0, 50),

        PoliticaUnificada("educacao", "Escola integral + professor R$8k + censo",
            "Escola 7h-17h. Piso R$8k. Censo escolar. Cordel/capoeira.",
            "Orlando Silva", "Camilo Santana",
            "R$ 150 bi/ano", "4 anos", "PISA 450", 32.5, 65),

        PoliticaUnificada("emprego", "Emprego garantido + jornada 6h + renda",
            "Programa Nacional de Emprego. Jornada 6h. Renda mínima R$2.600.",
            "Paulo Paim", "Camilo Santana",
            "R$ 120 bi/ano", "4 anos", "<4% desemprego", 4.7, 55),

        PoliticaUnificada("economia", "Nacionalização bancária + ISF + auditoria",
            "Nacionalização gradual. ISF. Auditoria dívida. Planificação.",
            "Fernando Haddad", "Samara Martins",
            "R$ 200 bi/ano ganho", "4 anos", "Spread <5%", 100.0, 50),

        PoliticaUnificada("ambiente", "PPCDAm + Amazônia + extrativismo",
            "PPCDAm. Controle popular. Extrativismo. Transição energética.",
            "Marina Silva", "Sonia Guajajara",
            "R$ 30 bi/ano", "4 anos", "<3.000 km²/ano", 18.8, 75),

        PoliticaUnificada("indigena", "Demarcação + saúde + escola bilíngue",
            "251 terras. DSEI. Escolas bilíngues. Mercúrio zero.",
            "Sonia Guajajara", "Jandira Feghali",
            "R$ 5 bi/ano", "2 anos", "251 demarcadas", 1.4, 80),

        PoliticaUnificada("agropecuaria", "Reforma agrária + agricultura familiar",
            "Nacionalização da terra. 500M famílias. Cooperativas.",
            "Samara Martins", "Marina Silva",
            "R$ 15 bi/ano", "4 anos", "Gini <0.6", 8.3, 55),

        PoliticaUnificada("energia", "Reestatização + tarifa social + solar",
            "Petrobras 100% estatal. Tarifa social. Solar comunitária.",
            "Ciro Gomes", "Marina Silva",
            "R$ 80 bi/ano", "4 anos", "Tarifa social universal", 60.0, 60),

        PoliticaUnificada("transporte", "Estatização + tarifa zero + elétrico",
            "Municipalização. Tarifa zero. Frota elétrica. Ferrovias.",
            "Ciro Gomes", "Ciro Gomes",
            "R$ 40 bi/ano", "4 anos", "+50% passageiros", 32.5, 65),

        PoliticaUnificada("habitacao", "Imóveis vazios + 4M moradias + reforma",
            "Uso ou perda. Cooperativas. Caixa. Reforma urbana.",
            "Patrus Ananias", "Samara Martins",
            "R$ 35 bi/ano", "4 anos", "Déficit zero", 6.0, 75),

        PoliticaUnificada("saneamento", "Estatização + coleta universal",
            "Marco Legal revertido. 90% esgoto. Coleta seletiva.",
            "Patrus Ananias", "Ciro Gomes",
            "R$ 25 bi/ano", "4 anos", "90% esgoto", 70.0, 70),

        PoliticaUnificada("drogas", "Redução de danos + descriminalização",
            "Caps AD. Equipes de rua. Naloxona. Descriminalização.",
            "Erika Hilton", "Jandira Feghali",
            "R$ 8 bi/ano", "4 anos", "100% com tratamento", 6.0, 60),

        PoliticaUnificada("cultura", "Cotização 40% + financiamento direto",
            "Conteúdo 40% nacional. Bolsa direta. Cordel/capoeira.",
            "Luiza Erundina", "Jones Manoel",
            "R$ 3 bi/ano", "2 anos", "50% nacional", 16.5, 55),

        PoliticaUnificada("comunicacao", "Democratização + internet rural",
            "Quebra monopólio. Concessões públicas. Internet rural. Fim PJ.",
            "Jones Manoel", "Fernando Haddad",
            "R$ 5 bi/ano", "4 anos", "Herfindahl <0.3", 35.0, 50),
    ]


# ============================================================
# O PARTIDO UNIFICADO
# ============================================================

class PartidoUnificado:
    """
    Partido Comunista Unificado do Brasil (PCU-B).
    Sem siglas. Só gente. Só habilidade. Só programa.

    AVISO: TODOS os nomes sao MOCK (placeholder).
    A composicao final so e definida apos analise individual
    pelo Gate WO + score de capacidade + triangulacao de fontes.
    O sistema de medicao e REAL. As pessoas sao HIPOTETICAS.
    """

    def __init__(self):
        self.pessoas = _init_pessoas()
        self.programa = _init_programa()

    def scorecard(self) -> Dict[str, Any]:
        total_sofrendo = sum(p.pessoas_resolvidas_milhoes / (p.cobertura_pct / 100) for p in self.programa)
        total_resolvido = sum(p.pessoas_resolvidas_milhoes for p in self.programa)
        n_resolvidos = sum(1 for p in self.programa if p.status == "RESOLVIDO")

        return {
            "modulo": "open_partido_unificado",
            "versao": "0.2.0-spec (sem siglas)",
            "nome": "Partido Comunista Unificado do Brasil",
            "sigla": "PCU-B",
            "pessoas": len(self.pessoas),
            "politicas": len(self.programa),
            "eixos_resolvidos": n_resolvidos,
            "pessoas_resolvidas_milhoes": round(total_resolvido, 1),
            "cobertura_media": round(total_resolvido / total_sofrendo * 100, 1) if total_sofrendo else 0,
        }


def _demo():
    pu = PartidoUnificado()
    sc = pu.scorecard()

    print("=" * 90)
    print("PARTIDO COMUNISTA UNIFICADO DO BRASIL (PCU-B)")
    print("Sem siglas. Só gente. Só habilidade. Só programa.")
    print("=" * 90)

    print(f"""
  {sc['pessoas']} pessoas. {sc['politicas']} políticas. 18 eixos.

  A sigla morreu. O cargo fica. A habilidade fica. O nome fica.
  Quem entra não entra como "membro do X".
  Entra como gente que sabe fazer algo.

  PESSOAS RESOLVIDAS: {sc['pessoas_resolvidas_milhoes']} milhões
  COBERTURA MÉDIA: {sc['cobertura_media']}%
""")

    print(f"{'='*90}")
    print("QUEM FAZ O QUE (sem sigla, sem partido, sem 'eu')")
    print(f"{'='*90}")
    for p in pu.pessoas:
        bar = "#" * int(p.score_capacidade)
        print(f"""
  [{p.cargo}]
    NOME: {p.nome} (score {p.score_capacidade:.1f}) [{bar}]
    VEIO DE: {p.origem}
    SABE FAZER: {p.habilidade}
    SERVE A: {p.serve_a}
    DESCARTADO: {p.descartado}""")

    print(f"\n{'='*90}")
    print("PROGRAMA: QUEM EXECUTA O QUÊ")
    print(f"{'='*90}")
    for pol in pu.programa:
        bar = "#" * int(pol.cobertura_pct / 5)
        flag = " *** RESOLVIDO" if pol.status == "RESOLVIDO" else ""
        print(f"""
  [{pol.eixo.upper()}] {pol.titulo} {flag}
    FAZER: {pol.o_que_fazer[:70]}
    COORDENA: {pol.quem_coordena}
    EXECUTA: {pol.quem_executa}
    CUSTO: {pol.custo} | PRAZO: {pol.prazo} | META: {pol.meta}
    RESOLVE: {pol.pessoas_resolvidas_milhoes:.1f}M ({pol.cobertura_pct}%) [{bar}]""")

    print(f"\n{'='*90}")
    print("VEREDITO")
    print(f"{'='*90}")
    print(f"""
  {sc['pessoas']} pessoas com habilidades servindo a {sc['politicas']} políticas.

  Não existe "eu sou do PT". Não existe "eu sou do PCB".
  Existe: "eu sei fazer X e vou fazer X pelo programa".

  Samara coordena o programa. Não como "da UP". Como quem escreveu 25 pontos.
  Jones comunica. Não como "do PCB". Como quem tem 2M e 10 anos de coerência.
  Camilo executa educação. Não como "do PT". Como quem fez IDEB subir.
  Marina cuida da Amazônia. Não como "da REDE". Como quem reduziu desmatamento 80%.
  Ciro constrói. Não como "do PDT". Como fez a transposição.

  A única métrica: {sc['pessoas_resolvidas_milhoes']:.0f} milhões param de sofrer.
  Falta: {100 - sc['cobertura_media']:.0f}% ainda sofrendo.

  Partido é ferramenta. População é fim.
  Não existe eu. Existe o que falta resolver.
""")


if __name__ == "__main__":
    _demo()
