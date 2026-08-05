#!/usr/bin/env python3
"""
OpenBriefingEstadual -- Briefing por Estado: Problema + Dado + Desafio
=========================================================================
"Cada estado tem um inferho próprio. Quem quer governar precisa
 saber qual é e trazer proposta. Sem proposta = W.O."

Compila dados de 27 estados e DESAFIA quem quer participar:
  - Governador: resolve o Raio X estadual
  - Senador: vota leis que atacem o problema
  - Deputado: propõe emenda/orçamento

Sem proposta com Gate WO 7/7, não tem cargo.

AVISO: Dados MOCK baseados em PNAD/IBGE/FBSP/INEP até triangulação.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Tuple
from collections import defaultdict


class NivelProblema(Enum):
    EMERGENCIA = "EMERGENCIA"       # mata agora
    ALTA = "ALTA"                    # estrutural urgente
    MEDIA = "MEDIA"                  # importante
    MONITORAR = "MONITORAR"


@dataclass
class ProblemaEstado:
    """Um problema real de um estado com dado e fonte."""
    problema: str
    nivel: NivelProblema
    indicador: str                   # o número de hoje
    meta: str                        # o número que resolve
    fonte: str
    cargo_responsavel: str           # governador/senador/deputado
    proposta_exigida: str            # o que o candidato precisa trazer


@dataclass
class BriefingEstado:
    """Briefing completo de um estado para candidatos."""
    uf: str
    nome: str
    regiao: str
    populacao_milhoes: float

    # Economia real (distribuição, não média)
    p10: float                       # 10% mais pobre
    p50: float                       # mediana
    p99: float                       # 1% mais rico
    desigualdade_x: float            # P99/P10
    gap_racial: float                # branco/negro
    gap_genero: float                # homem/mulher
    pct_indigente: float             # % com R$ 0-100

    # Problemas (top 5)
    problemas: List[ProblemaEstado]

    # Como o povo sobrevive
    economia_real: str               # de que vive o estado

    # Desafio por cargo
    desafio_governador: str
    desafio_senador: str
    desafio_deputado: str

    @property
    def n_problemas_emergencia(self) -> int:
        return sum(1 for p in self.problemas if p.nivel == NivelProblema.EMERGENCIA)

    @property
    def status_briefing(self) -> str:
        if self.n_problemas_emergencia >= 3:
            return "CRITICO"
        elif self.n_problemas_emergencia >= 1:
            return "ALERTA"
        return "OBSERVAR"


def _init_briefings() -> List[BriefingEstado]:
    return [

        # ================================================================
        # NORTE
        # ================================================================
        BriefingEstado("AC", "Acre", "Norte", 0.9,
            p10=100, p50=900, p99=12000, desigualdade_x=120, gap_racial=1.71, gap_genero=1.38, pct_indigente=8,
            problemas=[
                ProblemaEstado("Miséria extrema", NivelProblema.EMERGENCIA,
                    "8% em indigência (R$ 0-100/mês). 23% abaixo de R$ 300.", "0% indigência",
                    "PNAD 2023", "Governador",
                    "Programa de renda mínima + emprego real (cooperativa, extrativismo)"),
                ProblemaEstado("Narcotráfico (rota Peru/Bolívia)", NivelProblema.EMERGENCIA,
                    "Fronteira sem controle. Rota ativa.", "Fim da rota (força estadual + federal)",
                    "PF 2024", "Governador + Senador",
                    "Plano de segurança fronteiriça com Força Nacional"),
                ProblemaEstado("Desmatamento", NivelProblema.EMERGENCIA,
                    "Entre os mais altos do Brasil per capita.", "-80% em 4 anos",
                    "PRODES/INPE 2024", "Governador",
                    "PPCDAm estadual. Fim da madeira ilegal."),
                ProblemaEstado("Funcionalismo inflado (cabide)", NivelProblema.ALTA,
                    "Serviço público maior que capacidade.", "Auditoria total. Fim de cabide.",
                    "TCE-AC 2024", "Governador",
                    "Auditoria completa em 90 dias. Demissão de cargos sem função."),
                ProblemaEstado("Saneamento (60% sem cobertura)", NivelProblema.ALTA,
                    "60% sem coleta de esgoto.", "90% em 4 anos",
                    "SNIS 2024", "Governador",
                    "Plano de saneamento com custo, prazo e métrica."),
            ],
            economia_real="Pecuária (predatória), madeira (legal/ilegal), castanha, mandioca, serviço público, Bolsa Família, narcotráfico (não oficial).",
            desafio_governador="Resolver miséria + narcotráfico + desmatamento + cabide. Proposta com Gate WO 7/7.",
            desafio_senador="Votar leis de segurança fronteiriça + financiamento para saneamento rural.",
            desafio_deputado="Propor emenda orçamentária para renda mínima + emprego no AC."),

        BriefingEstado("AM", "Amazonas", "Norte", 4.3,
            p10=150, p50=1100, p99=15000, desigualdade_x=100, gap_racial=1.78, gap_genero=1.30, pct_indigente=7,
            problemas=[
                ProblemaEstado("Manaus: pobreza extrema", NivelProblema.EMERGENCIA,
                    "Periferia de Manaus: fome, violência, sem saneamento.", "Renda + saneamento + segurança",
                    "IBGE 2023", "Governador",
                    "Plano integrado Manaus: BF ampliado + esgoto + UPP social"),
                ProblemaEstado("Desmatamento + garimpo", NivelProblema.EMERGENCIA,
                    "Top 3 desmatamento. Garimpo ilegal massivo.", "-80% desmatamento. Fim garimpo.",
                    "PRODES 2024", "Governador + Senador",
                    "Operação garimpo zero. Fiscalização por satélite + força."),
                ProblemaEstado("Povos originários em crise", NivelProblema.EMERGENCIA,
                    "Yanomami: mercurio, desnutrição, garimpo.", "Sai o garimpo. Entra saúde DSEI.",
                    "Funai 2024", "Senador + Deputado",
                    "Propor lei de expulsão de garimpo em terra indígena."),
                ProblemaEstado("Logística (só por barco/avião)", NivelProblema.MEDIA,
                    "Sem estradas. Tudo por rio. Custo 3x.", "BR-319 + hidrovias",
                    "DNIT 2024", "Senador",
                    "Emenda orçamentária para BR-319 com estudo ambiental."),
                ProblemaEstado("Educação (analfabetismo rural)", NivelProblema.ALTA,
                    "Analfabetismo rural: 20%.", "Reduzir a 5%",
                    "INEP 2024", "Governador",
                    "Programa alfabetização rural com meta e prazo."),
            ],
            economia_real="Zona Franca de Manaus (indústria), comércio, serviço público, pesca, extrativismo, turismo.",
            desafio_governador="Resolver Manaus (pobreza) + Amazônia (desmatamento/garimpo) + indígena.",
            desafio_senador="Votar lei de garimpo zero em terra indígena + financiamento ZFM.",
            desafio_deputado="Propor emenda para BR-319 + saúde Yanomami."),

        BriefingEstado("AP", "Amapá", "Norte", 0.9,
            p10=120, p50=850, p99=12000, desigualdade_x=100, gap_racial=1.85, gap_genero=1.33, pct_indigente=8,
            problemas=[
                ProblemaEstado("Pobreza extrema", NivelProblema.EMERGENCIA,
                    "8% indigência. Ilhas sem luz elétrica.", "Renda + eletrificação",
                    "PNAD 2023", "Governador",
                    "Programa renda + solar comunitário nas ilhas."),
                ProblemaEstado("Mineração ilegal", NivelProblema.EMERGENCIA,
                    "Garimpo de ouro. Mercúrio nos rios.", "Fim do garimpo. Remediação.",
                    "IBAMA 2024", "Governador + Senador",
                    "Operação garimpo zero + remediação de mercúrio."),
                ProblemaEstado("Saneamento zero", NivelProblema.ALTA,
                    "60% sem esgoto.", "90% em 4 anos",
                    "SNIS 2024", "Governador",
                    "Plano de saneamento com custo e prazo."),
                ProblemaEstado("Saúde (interior sem nada)", NivelProblema.ALTA,
                    "Interior sem médico. UPA sem insumo.", "Mais Médicos ampliado",
                    "MS 2024", "Deputado",
                    "Emenda para Mais Médicos no AP + UPA rural."),
            ],
            economia_real="Mineração (ilegal), pesca, mangue (caranguejo), serviço público, BF.",
            desafio_governador="Resolver pobreza + mineração + saneamento. Estado invisível.",
            desafio_senador="Votar lei de mineração ilegal + financiamento AP.",
            desafio_deputado="Propor emenda para eletrificação rural + saúde."),

        BriefingEstado("PA", "Pará", "Norte", 8.8,
            p10=100, p50=850, p99=13000, desigualdade_x=130, gap_racial=2.00, gap_genero=1.33, pct_indigente=9,
            problemas=[
                ProblemaEstado("Violência rural (mortes no campo)", NivelProblema.EMERGENCIA,
                    "Líder em mortes no campo. Grileiros. Conflito agrário.", "Fim da grilagem",
                    "CPT 2024", "Governador + Senador",
                    "Plano de regularização fundiária + proteção a lideranças."),
                ProblemaEstado("Garimpo ilegal (Mercúrio)", NivelProblema.EMERGENCIA,
                    "Maior garimpo ilegal do Brasil. Mercúrio no Tapajós.", "Fim garimpo. Remediação.",
                    "IBAMA 2024", "Governador + Senador",
                    "Operação garimpo zero no Tapajós + remediação."),
                ProblemaEstado("Belém: violência urbana", NivelProblema.EMERGENCIA,
                    "Belém: homicídios altos. Narcotráfico.", "-50% homicídios",
                    "FBSP 2024", "Governador",
                    "Desmilitarização + prevenção juvenil."),
                ProblemaEstado("Marajó: invisível", NivelProblema.EMERGENCIA,
                    "Ilha do Marajó: sem saúde, sem escola, sem luz.", "Plano Marajó",
                    "IBGE 2023", "Governador",
                    "Plano integrado Marajó (saúde + escola + energia solar)."),
                ProblemaEstado("Educação (pior PISA regional)", NivelProblema.ALTA,
                    "PISA entre os piores do Brasil.", "PISA 420 em 4 anos",
                    "INEP 2023", "Governador",
                    "Escola integral + professor R$8k + merenda local."),
            ],
            economia_real="Mineração (ferro, ouro), pecuária, grãos, madeira, pesca, comércio Belém, narcotráfico.",
            desafio_governador="Pará é o estado mais complexo do Norte. Violência rural + garimpo + Belém + Marajó.",
            desafio_senador="Votar lei garimpo zero + regularização fundiária + financiamento Marajó.",
            desafio_deputado="Propor emenda para Marajó + proteção lideranças rurais."),

        BriefingEstado("RO", "Rondônia", "Norte", 1.8,
            p10=150, p50=1000, p99=14000, desigualdade_x=93, gap_racial=1.63, gap_genero=1.33, pct_indigente=6,
            problemas=[
                ProblemaEstado("Desmatamento (TOP 3)", NivelProblema.EMERGENCIA,
                    "Top 3 desmatamento. Pecuária ilegal.", "-80% em 4 anos",
                    "PRODES 2024", "Governador",
                    "PPCDAm estadual. Fim pecuária ilegal."),
                ProblemaEstado("Trabalho escravo (agropecuária)", NivelProblema.EMERGENCIA,
                    "Recorrente em fazendas.", "Fim trabalho escravo (auditoria)",
                    "MPT 2024", "Governador + Senador",
                    "Operação anti-trabalho escravo + multa + confisco."),
                ProblemaEstado("Violência (narcotráfico fronteira)", NivelProblema.ALTA,
                    "Fronteira com Bolívia. Narcotráfico.", "Reduz 50%",
                    "FBSP 2024", "Governador",
                    "Plano fronteira + Força Nacional."),
                ProblemaEstado("Saúde rural", NivelProblema.ALTA,
                    "Interior sem cobertura.", "Mais Médicos ampliado",
                    "MS 2024", "Deputado",
                    "Emenda Mais Médicos rural RO."),
            ],
            economia_real="Pecuária (predatória), pecuária, grãos, madeira, narcotráfico fronteira.",
            desafio_governador="Desmatamento + trabalho escravo + narcotráfico. Estado feito de pecuária ilegal.",
            desafio_senador="Votar lei trabalho escravo (confisco de terra).",
            desafio_deputado="Propor emenda para PPCDAm estadual."),

        BriefingEstado("RR", "Roraima", "Norte", 0.7,
            p10=150, p50=950, p99=13000, desigualdade_x=87, gap_racial=1.73, gap_genero=1.35, pct_indigente=7,
            problemas=[
                ProblemaEstado("Crise Yanomami", NivelProblema.EMERGENCIA,
                    "Desnutrição infantil 2x nacional. Mercúrio. Garimpo.", "Saída garimpo + saúde DSEI",
                    "Funai/MS 2024", "Governador + Senador",
                    "Operação garimpo zero Yanomami + saúde emergencial."),
                ProblemaEstado("Imigração Venezuela", NivelProblema.EMERGENCIA,
                    "100k+ venezuelanos em Boa Vista. Sobrecarga.", "Plano acolhimento",
                    "ACNUR 2024", "Governador",
                    "Plano de acolhimento + trabalho + saúde para migrantes."),
                ProblemaEstado("Violência urbana (Boa Vista)", NivelProblema.ALTA,
                    "Boa Vista: homicídios altos.", "-50%",
                    "FBSP 2024", "Governador",
                    "Prevenção + desmilitarização."),
            ],
            economia_real="Serviço público, comércio, pesca, garimpo (ilegal), agricultura de subsistência, BF.",
            desafio_governador="Yanomami (genocídio em curso) + imigração + violência. Menor estado, maior crise.",
            desafio_senador="Votar lei garimpo zero + financiamento Yanomami.",
            desafio_deputado="Propor emenda para saúde indígena + acolhimento migrantes."),

        BriefingEstado("TO", "Tocantins", "Norte", 1.6,
            p10=150, p50=950, p99=13000, desigualdade_x=87, gap_racial=1.73, gap_genero=1.29, pct_indigente=7,
            problemas=[
                ProblemaEstado("Agronegócio predatório", NivelProblema.ALTA,
                    "Soja expandindo. Desmatamento Cerrado.", "Agroecologia + zoneamento",
                    "EMBRAPA 2024", "Governador",
                    "Zoneamento + fim desmatamento Cerrado."),
                ProblemaEstado("Trabalho escravo (carvão)", NivelProblema.EMERGENCIA,
                    "Carvoaria com trabalho escravo.", "Fim trabalho escravo",
                    "MPT 2024", "Governador + Senador",
                    "Operação anti-carvão + multa + confisco."),
                ProblemaEstado("Educação rural", NivelProblema.ALTA,
                    "Escola rural sem professor.", "Escola integral rural",
                    "INEP 2024", "Governador",
                    "Programa professor rural com moradia."),
            ],
            economia_real="Agronegócio (soja, pecuária), carvão vegetal, agricultura, comércio, BF.",
            desafio_governador="Agronegócio predatório + trabalho escravo + educação rural.",
            desafio_senador="Votar lei trabalho escravo + zoneamento Cerrado.",
            desafio_deputado="Propor emenda para escola rural."),

        # ================================================================
        # NORDESTE
        # ================================================================
        BriefingEstado("MA", "Maranhão", "Nordeste", 7.2,
            p10=0, p50=550, p99=10000, desigualdade_x=0, gap_racial=2.25, gap_genero=1.44, pct_indigente=12,
            problemas=[
                ProblemaEstado("Pior mediana de renda do Brasil", NivelProblema.EMERGENCIA,
                    "Mediana R$ 550. 12% em indigência.", "Renda mínima R$ 1.500",
                    "PNAD 2023", "Governador + Senador",
                    "Programa renda mínima estadual + emprego (cooperaiva)."),
                ProblemaEstado("Violência rural (mortes no campo)", NivelProblema.EMERGENCIA,
                    "TOP mortes no campo. Grileiros.", "Fim da grilagem",
                    "CPT 2024", "Governador",
                    "Regularização fundiária + proteção lideranças."),
                ProblemaEstado("Analfabetismo (pior do Brasil)", NivelProblema.EMERGENCIA,
                    "Analfabetismo 20%+. Escola sem professor.", "Reduzir a 5%",
                    "INEP 2024", "Governador",
                    "Alfabetização emergencial + professor R$8k."),
                ProblemaEstado("Saneamento (40% cobertura)", NivelProblema.ALTA,
                    "60% sem esgoto.", "90% em 4 anos",
                    "SNIS 2024", "Governador",
                    "Plano saneamento com custo/prazo/métrica."),
                ProblemaEstado("Saúde (interior sem nada)", NivelProblema.ALTA,
                    "Interior sem médico. Fila meses.", "Mais Médicos rural",
                    "MS 2024", "Deputado",
                    "Emenda Mais Médicos MA rural."),
            ],
            economia_real="Agricultura de subsistência, pecuária, algodão, BF (alta dependência), serviço público.",
            desafio_governador="MA é o estado mais pobre. Renda + violência + analfabetismo + saúde. Tudo é urgente.",
            desafio_senador="Votar ISF (imposto grandes fortunas) + financiamento MA.",
            desafio_deputado="Propor emenda para renda mínima + escola rural MA."),

        BriefingEstado("PI", "Piauí", "Nordeste", 3.3,
            p10=0, p50=650, p99=10000, desigualdade_x=0, gap_racial=2.00, gap_genero=1.36, pct_indigente=10,
            problemas=[
                ProblemaEstado("Seca (semi-árido)", NivelProblema.EMERGENCIA,
                    "Seca recorrente. Sem água.", "Cisternas + adutoras",
                    "ANA 2024", "Governador",
                    "1 cisterna por família + adutoras (com custo/prazo)."),
                ProblemaEstado("Miséria", NivelProblema.EMERGENCIA,
                    "10% indigência. Mediana R$ 650.", "Renda mínima",
                    "PNAD 2023", "Governador",
                    "Programa renda + emprego (cooperativa agrícola)."),
                ProblemaEstado("Educação (analfabetismo alto)", NivelProblema.ALTA,
                    "Analfabetismo 18%.", "Reduzir a 5%",
                    "INEP 2024", "Governador",
                    "Alfabetização + escola integral."),
                ProblemaEstado("Saúde (interior)", NivelProblema.ALTA,
                    "Interior sem médico.", "Mais Médicos rural",
                    "MS 2024", "Deputado",
                    "Emenda Mais Médicos PI rural."),
            ],
            economia_real="Agricultura (subsistência, mandioca, feijão), BF, servoço público, carnaúba.",
            desafio_governador="Seca + miséria + analfabetismo. Estado que o Brasil esqueceu.",
            desafio_senador="Votar lei de financiamento para semi-árido.",
            desafio_deputado="Propor emenda para cisternas + escola."),

        BriefingEstado("CE", "Ceará", "Nordeste", 9.3,
            p10=100, p50=850, p99=12000, desigualdade_x=120, gap_racial=2.00, gap_genero=1.33, pct_indigente=8,
            problemas=[
                ProblemaEstado("Violência Fortaleza", NivelProblema.EMERGENCIA,
                    "Fortaleza: homicídios altos. Facções.", "-50%",
                    "FBSP 2024", "Governador",
                    "Prevenção juvenil + desmilitarização."),
                ProblemaEstado("Seca (semi-árido)", NivelProblema.ALTA,
                    "Interior sem água.", "Cisternas + adutoras",
                    "ANA 2024", "Governador",
                    "Cisternas + transposição."),
                ProblemaEstado("Desigualdade (120x)", NivelProblema.ALTA,
                    "P10 R$100. P99 R$12.000.", "Reduzir gap",
                    "PNAD 2023", "Senador",
                    "Votar ISF + reforma tributária progressiva."),
                ProblemaEstado("Educação (em progresso)", NivelProblema.MEDIA,
                    "IDEB subindo (Camilo). Mas PISA baixo.", "PISA 420",
                    "INEP 2024", "Governador",
                    "Continuar escola integral + professor R$8k."),
            ],
            economia_real="Indústria (têxtil, calçados), turismo, serviço público, BF, agricultura, pesca.",
            desafio_governador="Violência Fortaleza + seca + desigualdade. Estado com progresso mas gap enorme.",
            desafio_senador="Votar ISF + financiamento semi-árido.",
            desafio_deputado="Propor emenda para prevenção juvenil."),

        BriefingEstado("RN", "Rio Grande do Norte", "Nordeste", 3.5,
            p10=100, p50=750, p99=11000, desigualdade_x=110, gap_racial=2.00, gap_genero=1.38, pct_indigente=9,
            problemas=[
                ProblemaEstado("Violência Natal", NivelProblema.EMERGENCIA,
                    "Natal: homicídios altos. Narcotráfico.", "-50%",
                    "FBSP 2024", "Governador",
                    "Prevenção + desmilitarização + fronteira."),
                ProblemaEstado("Pobreza litoral", NivelProblema.EMERGENCIA,
                    "Mediana R$ 750. 9% indigência.", "Renda mínima",
                    "PNAD 2023", "Governador",
                    "Programa renda + turismo popular."),
                ProblemaEstado("Saúde (filas)", NivelProblema.ALTA,
                    "Fila SUS meses.", "Fila <30 dias",
                    "CNJ 2024", "Governador",
                    "Triagem + Mais Médicos."),
            ],
            economia_real="Turismo, sal (salinas), petróleo (onshore), BF, pesca, serviço público.",
            desafio_governador="Violência Natal + pobreza + saúde.",
            desafio_senador="Votar lei segurança + financiamento turismo.",
            desafio_deputado="Propor emenda para prevenção + saúde."),

        BriefingEstado("PB", "Paraíba", "Nordeste", 4.1,
            p10=100, p50=700, p99=10500, desigualdade_x=105, gap_racial=2.10, gap_genero=1.42, pct_indigente=9,
            problemas=[
                ProblemaEstado("Seca", NivelProblema.EMERGENCIA,
                    "Semi-árido. Sem água.", "Cisternas + adutoras",
                    "ANA 2024", "Governador",
                    "Cisternas + transposição."),
                ProblemaEstado("Miséria", NivelProblema.EMERGENCIA,
                    "Mediana R$ 700. 9% indigência.", "Renda mínima",
                    "PNAD 2023", "Governador",
                    "Programa renda + cooperativa."),
                ProblemaEstado("Subemprego (Campina Grande)", NivelProblema.ALTA,
                    "Campina: desemprego alto. Tecnologia minguando.", "Polo tech + emprego",
                    "IBGE 2024", "Governador",
                    "Polo tecnologia + cooperativa."),
            ],
            economia_real="Agricultura (subsistência), BF, serviço público, tecnologia (Campina), pesca.",
            desafio_governador="Seca + miséria + subemprego.",
            desafio_senador="Votar financiamento semi-árido + tech.",
            desafio_deputado="Propor emenda para cisternas + polo tech."),

        BriefingEstado("PE", "Pernambuco", "Nordeste", 9.7,
            p10=100, p50=800, p99=14000, desigualdade_x=140, gap_racial=2.17, gap_genero=1.36, pct_indigente=8,
            problemas=[
                ProblemaEstado("Violência Recife", NivelProblema.EMERGENCIA,
                    "Recife: homicídios altos. Facções.", "-50%",
                    "FBSP 2024", "Governador",
                    "Prevenção + desmilitarização."),
                ProblemaEstado("Seca (sertão)", NivelProblema.ALTA,
                    "Sertão sem água.", "Cisternas + transposição",
                    "ANA 2024", "Governador",
                    "Transposição São Francisco."),
                ProblemaEstado("Desigualdade (140x)", NivelProblema.ALTA,
                    "P99/P10 = 140x. Gap racial 2.17x.", "Reduzir gap",
                    "PNAD 2023", "Senador",
                    "Votar ISF + reforma tributária."),
                ProblemaEstado("Saúde (fila)", NivelProblema.ALTA,
                    "Fila SUS.", "Fila <30 dias",
                    "CNJ 2024", "Deputado",
                    "Emenda saúde PE."),
            ],
            economia_real="Indústria (Suape), turismo, cana-de-açúcar, serviço público, BF, pesca.",
            desafio_governador="Violência Recife + seca sertão + desigualdade.",
            desafio_senador="Votar ISF + transposição.",
            desafio_deputado="Propor emenda prevenção + saúde."),

        BriefingEstado("AL", "Alagoas", "Nordeste", 3.4,
            p10=0, p50=550, p99=9500, desigualdade_x=0, gap_racial=2.25, gap_genero=1.44, pct_indigente=12,
            problemas=[
                ProblemaEstado("Pior IDH do Brasil", NivelProblema.EMERGENCIA,
                    "IDH mais baixo. 12% indigência.", "IDH subir 0.1",
                    "PNUD 2023", "Governador",
                    "Programa integrado: renda + escola + saúde."),
                ProblemaEstado("Analfabetismo", NivelProblema.EMERGENCIA,
                    "Analfabetismo 22%.", "Reduzir a 5%",
                    "INEP 2024", "Governador",
                    "Alfabetização emergencial."),
                ProblemaEstado("Violência (Maceió)", NivelProblema.EMERGENCIA,
                    "Maceió: homicídios altos.", "-50%",
                    "FBSP 2024", "Governador",
                    "Prevenção + desmilitarização."),
                ProblemaEstado("Saneamento", NivelProblema.ALTA,
                    "60% sem esgoto.", "90%",
                    "SNIS 2024", "Governador",
                    "Plano saneamento."),
            ],
            economia_real="Agricultura (cana, subsistência), BF, serviço público, pesca, açúcar/álcool.",
            desafio_governador="AL é o pior IDH. Tudo é urgente. Renda + escola + saúde + segurança.",
            desafio_senador="Votar ISF + financiamento AL emergencial.",
            desafio_deputado="Propor emenda para IDH (renda + escola + saúde)."),

        BriefingEstado("SE", "Sergipe", "Nordeste", 2.3,
            p10=100, p50=700, p99=10500, desigualdade_x=105, gap_racial=2.10, gap_genero=1.42, pct_indigente=9,
            problemas=[
                ProblemaEstado("Pobreza", NivelProblema.EMERGENCIA,
                    "Mediana R$ 700. 9% indigência.", "Renda mínima",
                    "PNAD 2023", "Governador",
                    "Programa renda + emprego."),
                ProblemaEstado("Saneamento zero", NivelProblema.ALTA,
                    "70% sem esgoto.", "90%",
                    "SNIS 2024", "Governador",
                    "Plano saneamento."),
                ProblemaEstado("Saúde", NivelProblema.ALTA,
                    "Fila SUS. Interior sem médico.", "Mais Médicos",
                    "MS 2024", "Deputado",
                    "Emenda Mais Médicos SE."),
            ],
            economia_real="Petróleo (onshore), BF, serviço público, agricultura, pesca.",
            desafio_governador="Pobreza + saneamento + saúde. Menor estado do NE.",
            desafio_senador="Votar financiamento saneamento.",
            desafio_deputado="Propor emenda saúde + renda."),

        BriefingEstado("BA", "Bahia", "Nordeste", 14.9,
            p10=100, p50=700, p99=12000, desigualdade_x=120, gap_racial=2.18, gap_genero=1.42, pct_indigente=9,
            problemas=[
                ProblemaEstado("Violência Salvador", NivelProblema.EMERGENCIA,
                    "Salvador: homicídios altos. Negro 80% vítimas.", "-50%",
                    "FBSP 2024", "Governador",
                    "Prevenção + desmilitarização + anti-racismo."),
                ProblemaEstado("Pobreza extrema (interior)", NivelProblema.EMERGENCIA,
                    "Interior: 9% indigência. Semi-árido.", "Renda + água",
                    "PNAD 2023", "Governador",
                    "Programa renda + cisternas + cooperativa."),
                ProblemaEstado("Racismo estrutural", NivelProblema.EMERGENCIA,
                    "Negro 80% da população. Renda 50% do branco.", "Igualdade racial",
                    "IBGE 2023", "Senador + Deputado",
                    "Política de igualdade racial + cota + renda."),
                ProblemaEstado("Semi-árido (seca)", NivelProblema.ALTA,
                    "Sertão baiano sem água.", "Cisternas + adutoras",
                    "ANA 2024", "Governador",
                    "Cisternas + transposição."),
                ProblemaEstado("Educação", NivelProblema.ALTA,
                    "Analfabetismo 15%.", "Reduzir a 5%",
                    "INEP 2024", "Governador",
                    "Alfabetização + escola integral."),
            ],
            economia_real="Turismo, petróleo (pré-sal), agricultura (cacau), pecuária, indústria (CAC), BF.",
            desafio_governador="BA é a maior população negra fora da África. Violência + racismo + pobreza + seca.",
            desafio_senador="Votar política de igualdade racial + ISF.",
            desafio_deputado="Propor emenda para prevenção + renda + cisternas."),

        # ================================================================
        # CENTRO-OESTE
        # ================================================================
        BriefingEstado("MT", "Mato Grosso", "Centro-Oeste", 3.7,
            p10=200, p50=1300, p99=20000, desigualdade_x=100, gap_racial=1.80, gap_genero=1.36, pct_indigente=5,
            problemas=[
                ProblemaEstado("Desmatamento (TOP 1)", NivelProblema.EMERGENCIA,
                    "Maior desmatamento do Brasil. Soja + pecuária.", "-80% em 4 anos",
                    "PRODES 2024", "Governador",
                    "PPCDAm estadual + zoneamento."),
                ProblemaEstado("Trabalho escravo (fazendas)", NivelProblema.EMERGENCIA,
                    "Recorrente.", "Fim trabalho escravo",
                    "MPT 2024", "Governador + Senador",
                    "Operação anti-escravidão + confisco."),
                ProblemaEstado("Povos originários (Xingu)", NivelProblema.ALTA,
                    "Xingu sob pressão. Agro tóxico nos rios.", "Proteção Xingu",
                    "Funai 2024", "Senador",
                    "Votar proteção Xingu + fim agrotóxico."),
                ProblemaEstado("Saúde rural", NivelProblema.MEDIA,
                    "Interior sem médico.", "Mais Médicos",
                    "MS 2024", "Deputado",
                    "Emenda Mais Médicos rural."),
            ],
            economia_real="Agronegócio (soja #1, pecuária, algodão, milho), madeira, mineração.",
            desafio_governador="MT é o motor do agro predatório. Desmatar + escravidão + Xingu.",
            desafio_senador="Votar lei trabalho escravo + PPCDAm.",
            desafio_deputado="Propor emenda proteção Xingu."),

        BriefingEstado("MS", "Mato Grosso do Sul", "Centro-Oeste", 2.8,
            p10=200, p50=1300, p99=18000, desigualdade_x=90, gap_racial=1.70, gap_genero=1.27, pct_indigente=5,
            problemas=[
                ProblemaEstado("Violência fronteiriça", NivelProblema.EMERGENCIA,
                    "Fronteira Paraguai. Narcotráfico.", "-50%",
                    "FBSP 2024", "Governador",
                    "Plano fronteira + Força Nacional."),
                ProblemaEstado("Indígena Guarani-Kaiowá", NivelProblema.EMERGENCIA,
                    "Guarani: conflito fundiário. Despejos.", "Demarcação",
                    "Funai 2024", "Governador + Senador",
                    "Demarcação Guarani-Kaiowá + proteção."),
                ProblemaEstado("Pecuária predatória", NivelProblema.ALTA,
                    "Pecuária + desmatamento Pantanal.", "Pantanal protegido",
                    "PRODES 2024", "Governador",
                    "Zoneamento + proteção Pantanal."),
                ProblemaEstado("Trabalho escravo (carvão)", NivelProblema.ALTA,
                    "Carvoaria recorrente.", "Fim trabalho escravo",
                    "MPT 2024", "Senador",
                    "Votar lei trabalho escravo."),
            ],
            economia_real="Agronegócio (pecuária, soja), narcotráfico (fronteira), turismo (Pantanal), BF.",
            desafio_governador="Fronteira + Guarani + Pantanal. Estado de conflito.",
            desafio_senador="Votar demarcação Guarani + lei trabalho escravo.",
            desafio_deputado="Propor emenda proteção Pantanal + fronteira."),

        BriefingEstado("GO", "Goiás", "Centro-Oeste", 7.2,
            p10=150, p50=1100, p99=16000, desigualdade_x=106, gap_racial=1.76, gap_genero=1.37, pct_indigente=6,
            problemas=[
                ProblemaEstado("Crescimento desordenado (Goiânia)", NivelProblema.ALTA,
                    "Goiânia: periferia sem infraestrutura.", "Plano diretor",
                    "IBGE 2024", "Governador",
                    "Plano diretor popular + habitação."),
                ProblemaEstado("Saúde (fila)", NivelProblema.ALTA,
                    "Fila SUS.", "Fila <30 dias",
                    "CNJ 2024", "Governador",
                    "Triagem + Mais Médicos."),
                ProblemaEstado("Agronegócio (Cerrado)", NivelProblema.MEDIA,
                    "Soja expandindo. Desmatamento Cerrado.", "Zoneamento",
                    "EMBRAPA 2024", "Governador",
                    "Zoneamento + agroecologia."),
            ],
            economia_real="Agronegócio (soja, pecuária), mineração, indústria, comércio Goiânia.",
            desafio_governador="Crescimento desordenado + saúde + agro.",
            desafio_senador="Votar financiamento saúde.",
            desafio_deputado="Propor emenda habitação + saúde."),

        BriefingEstado("DF", "Distrito Federal", "Centro-Oeste", 3.1,
            p10=300, p50=2200, p99=40000, desigualdade_x=133, gap_racial=2.19, gap_genero=1.56, pct_indigente=3,
            problemas=[
                ProblemaEstado("Contraste riqueza/periferia", NivelProblema.EMERGENCIA,
                    "Plano Piloto: R$ 4.500. Periferia: R$ 1.600.", "Reduzir gap",
                    "PNAD 2023", "Governador",
                    "Renda mínima + habitação periferia + escola."),
                ProblemaEstado("Gap racial (2.19x, pior do Brasil)", NivelProblema.EMERGENCIA,
                    "Branco R$ 3.500. Negro R$ 1.600.", "Igualdade racial",
                    "IBGE 2023", "Governador",
                    "Política racial + cota + renda."),
                ProblemaEstado("Violência periferia", NivelProblema.ALTA,
                    "Taguatinga/Ceilândia: violência.", "-50%",
                    "FBSP 2024", "Governador",
                    "Prevenção + desmilitarização."),
                ProblemaEstado("Funcionalismo inflado (cabide)", NivelProblema.ALTA,
                    "Maior cabide do Brasil.", "Auditoria total",
                    "TCDF 2024", "Governador",
                    "Auditoria completa + fim cabide."),
            ],
            economia_real="Serviço público (maior empregador), comércio, tecnologia, informalidade periferia.",
            desafio_governador="DF é o espelho da desigualdade brasileira. Plano Piloto vs periferia. Gap racial pior.",
            desafio_senador="DF nao tem senador -- 8 deputados distritais.",
            desafio_deputado="Propor lei distrital renda + habitação + auditoria."),

        # ================================================================
        # SUDESTE
        # ================================================================
        BriefingEstado("SP", "São Paulo", "Sudeste", 45.9,
            p10=300, p50=2000, p99=35000, desigualdade_x=117, gap_racial=2.00, gap_genero=1.47, pct_indigente=3,
            problemas=[
                ProblemaEstado("Violência periferia (Cracolândia)", NivelProblema.EMERGENCIA,
                    "Periferia SP: homicídios. Cracolândia. Facções.", "-50%",
                    "FBSP 2024", "Governador",
                    "Redução de danos + desmilitarização + emprego juvenil."),
                ProblemaEstado("Habitação (sem-teto + periferia)", NivelProblema.EMERGENCIA,
                    "Centro vazio. Periferia distante. Sem transporte.", "Imóveis vazios + moradia",
                    "IBGE 2024", "Governador",
                    "Imóveis vazios para déficit + reforma urbana."),
                ProblemaEstado("Transporte (periferia isolada)", NivelProblema.EMERGENCIA,
                    "4h de transporte/dia. Tarifa cara.", "Tarifa zero + trem",
                    "ANTP 2024", "Governador",
                    "Tarifa zero + recuperação ferroviária CPTM."),
                ProblemaEstado("Drogas (guerra falhou)", NivelProblema.ALTA,
                    "Cracolândia. Caps sem cobertura.", "Redução danos + Caps",
                    "SENAD 2024", "Governador",
                    "Caps AD + redução de danos + descriminalização."),
                ProblemaEstado("Educação (PISA baixo)", NivelProblema.ALTA,
                    "PISA 410. Escola pública periferia falha.", "PISA 450",
                    "INEP 2024", "Governador",
                    "Escola integral + professor R$8k."),
            ],
            economia_real="Indústria (automotivo, químico), serviços, finanças, tecnologia, comércio. Maior PIB estadual.",
            desafio_governador="SP é 45M de pessoas. Periferia: violência + moradia + transporte + drogas. Estado-país.",
            desafio_senador="Votar tarifa zero federal + habitação + redução danos.",
            desafio_deputado="Propor emenda para Cracolândia + transporte + escola."),

        BriefingEstado("RJ", "Rio de Janeiro", "Sudeste", 16.5,
            p10=200, p50=1600, p99=30000, desigualdade_x=150, gap_racial=2.08, gap_genero=1.43, pct_indigente=4,
            problemas=[
                ProblemaEstado("Violência favela (polícia mata)", NivelProblema.EMERGENCIA,
                    "Polícia mata mais que EUA. Favelas em guerra.", "-70% mortes polícia",
                    "FBSP 2024", "Governador",
                    "Desmilitarização total + UPP social + redução danos."),
                ProblemaEstado("Desigualdade (150x)", NivelProblema.EMERGENCIA,
                    "P10 R$200. P99 R$30.000. Maior gap.", "Reduzir gap",
                    "PNAD 2023", "Senador",
                    "Votar ISF + reforma tributária."),
                ProblemaEstado("Saúde (fila + dengue)", NivelProblema.ALTA,
                    "Fila SUS. Dengue 2024.", "Fila <30 dias",
                    "CNJ 2024", "Governador",
                    "Triagem + combate dengue."),
                ProblemaEstado("Transporte (subway sucateado)", NivelProblema.ALTA,
                    "Metrô sucateado. Barco Niterói caro.", "Tarifa zero + metrô",
                    "ANTP 2024", "Governador",
                    "Tarifa zero + recuperação metrô."),
                ProblemaEstado("Drogas (guerra falhou)", NivelProblema.ALTA,
                    "Favelas: tráfico + milícia + polícia.", "Redução danos",
                    "FBSP 2024", "Governador",
                    "Redução danos + fim milícia."),
            ],
            economia_real="Petróleo (pré-sal), turismo, serviços, indústria (químico), narcotráfico, milícia.",
            desafio_governador="RJ é o laboratório da desigualdade armada. Polícia mata + favela + milícia.",
            desafio_senador="Votar ISF + desmilitarização federal.",
            desafio_deputado="Propor emenda redução danos + desmilitarização."),

        BriefingEstado("MG", "Minas Gerais", "Sudeste", 21.3,
            p10=150, p50=1200, p99=18000, desigualdade_x=120, gap_racial=1.89, gap_genero=1.40, pct_indigente=5,
            problemas=[
                ProblemaEstado("Saneamento (interior sem esgoto)", NivelProblema.ALTA,
                    "Interior: 60% sem esgoto.", "90% em 4 anos",
                    "SNIS 2024", "Governador",
                    "Plano saneamento estadual."),
                ProblemaEstado("Brumadinho/Mariana (mineração)", NivelProblema.ALTA,
                    "Rompimento barragem. Sem remediação total.", "Fim barragem a montante",
                    "IBAMA 2024", "Governador + Senador",
                    "Lei estadual fim barragem + reparação."),
                ProblemaEstado("Violência (Belo Horizonte)", NivelProblema.ALTA,
                    "BH: homicídios.", "-50%",
                    "FBSP 2024", "Governador",
                    "Prevenção + desmilitarização."),
                ProblemaEstado("Educação (interior)", NivelProblema.MEDIA,
                    "Interior sem professor.", "Escola rural",
                    "INEP 2024", "Governador",
                    "Professor rural com moradia."),
            ],
            economia_real="Mineração (ferro), siderurgia, agropecuária, turismo histórico, serviços.",
            desafio_governador="Saneamento + mineração (Brumadinho) + violência BH.",
            desafio_senador="Votar lei fim barragem a montante.",
            desafio_deputado="Propor emenda saneamento + reparação."),

        BriefingEstado("ES", "Espírito Santo", "Sudeste", 4.1,
            p10=200, p50=1300, p99=17000, desigualdade_x=85, gap_racial=1.70, gap_genero=1.27, pct_indigente=5,
            problemas=[
                ProblemaEstado("Petróleo vs pobreza", NivelProblema.ALTA,
                    "Petróleo rico. Povo pobre.", "Renda do petróleo",
                    "ANP 2024", "Governador",
                    "Royalties para renda + saúde + escola."),
                ProblemaEstado("Violência (Vitória)", NivelProblema.ALTA,
                    "Grande Vitória: homicídios.", "-50%",
                    "FBSP 2024", "Governador",
                    "Prevenção + desmilitarização."),
                ProblemaEstado("Saúde", NivelProblema.MEDIA,
                    "Fila SUS.", "Fila <30 dias",
                    "CNJ 2024", "Governador",
                    "Triagem + Mais Médicos."),
            ],
            economia_real="Petróleo (pré-sal), mineração, moagem (papel/celulose), pecuária, pesca, turismo.",
            desafio_governador="Petróleo rico vs povo pobre. Violência + saúde.",
            desafio_senador="Votar lei royalties para povo.",
            desafio_deputado="Propor emenda royalties + saúde."),

        # ================================================================
        # SUL
        # ================================================================
        BriefingEstado("PR", "Paraná", "Sul", 11.8,
            p10=200, p50=1400, p99=20000, desigualdade_x=100, gap_racial=1.70, gap_genero=1.33, pct_indigente=4,
            problemas=[
                ProblemaEstado("Agronegócio (soja desmata)", NivelProblema.ALTA,
                    "Soja expandindo. Mata Atlântica.", "Zoneamento",
                    "PRODES 2024", "Governador",
                    "Zoneamento + proteção Mata Atlântica."),
                ProblemaEstado("Desemprego (Curitiba)", NivelProblema.ALTA,
                    "Curitiba: desemprego. Indústria minguando.", "Polo tech + emprego",
                    "IBGE 2024", "Governador",
                    "Polo tecnologia + cooperativa."),
                ProblemaEstado("Saúde", NivelProblema.MEDIA,
                    "Fila SUS.", "Fila <30 dias",
                    "CNJ 2024", "Governador",
                    "Triagem + Mais Médicos."),
            ],
            economia_real="Agronegócio (soja, milho, café), indústria (automotivo, papel), serviços, tecnologia.",
            desafio_governador="Agro vs floresta + desemprego Curitiba + saúde.",
            desafio_senador="Votar zoneamento + financiamento emprego.",
            desafio_deputado="Propor emenda emprego + Mata Atlântica."),

        BriefingEstado("SC", "Santa Catarina", "Sul", 7.8,
            p10=300, p50=1900, p99=25000, desigualdade_x=83, gap_racial=1.57, gap_genero=1.38, pct_indigente=3,
            problemas=[
                ProblemaEstado("Desigualdade (3% indigência)", NivelProblema.MEDIA,
                    "Melhor distribuição mas ainda tem pobreza.", "Erradicar indigência",
                    "PNAD 2023", "Governador",
                    "Renda mínima para residual."),
                ProblemaEstado("Enchentes (2024)", NivelProblema.ALTA,
                    "Enchentes 2024. 500k desabrigados.", "Prevenção + reconstrução",
                    "Defesa Civil 2024", "Governador",
                    "Plano de prevenção + reconstrução com custo/prazo."),
                ProblemaEstado("Conservadorismo (político)", NivelProblema.MONITORAR,
                    "Direita forte. Bancada da fé.", "Mobilização popular",
                    "TSE 2024", "Senador + Deputado",
                    "Campanha popular + comunicação."),
            ],
            economia_real="Indústria (têxtil, eletrodomésticos), agro, tecnologia, turismo, serviços.",
            desafio_governador="SC é o melhor estado em distribuição. Mas tem enchente + 3% em indigência.",
            desafio_senador="Votar financiamento prevenção enchentes.",
            desafio_deputado="Propor emenda reconstrução + renda residual."),

        BriefingEstado("RS", "Rio Grande do Sul", "Sul", 10.9,
            p10=250, p50=1600, p99=23000, desigualdade_x=92, gap_racial=1.67, gap_genero=1.36, pct_indigente=3,
            problemas=[
                ProblemaEstado("Enchente 2024 (500k desabrigados)", NivelProblema.EMERGENCIA,
                    "Maio 2024: 500k desabrigados. 175 mortos.", "Reconstrução + prevenção",
                    "Defesa Civil 2024", "Governador + Senador",
                    "Plano reconstrução R$30bi + prevenção (adutoras, diques, reassentamento)."),
                ProblemaEstado("Habitação (desabrigados)", NivelProblema.EMERGENCIA,
                    "500k desabrigados. Sem moradia.", "Moradia digna",
                    "Defesa Civil 2024", "Governador",
                    "Construção de moradias + cooperativas + imóveis vazios."),
                ProblemaEstado("Saúde (pós-enchente)", NivelProblema.ALTA,
                    "Hospitais destruídos. Doenças.", "Reconstrução SUS",
                    "MS 2024", "Governador",
                    "Reconstruir hospitais + Mais Médicos."),
                ProblemaEstado("Agronegócio (soja)", NivelProblema.MEDIA,
                    "Soja dominante. Pequeno agricultor sumindo.", "Reforma agrária",
                    "EMBRAPA 2024", "Governador",
                    "Agricultura familiar + cooperativa."),
            ],
            economia_real="Agronegócio (soja, pecuária, arroz), indústria (calçados, petroquímica), serviços, BF.",
            desafio_governador="RS é emergência nacional. 500k desabrigados. Reconstrução + prevenção.",
            desafio_senador="Votar R$30bi reconstrução + prevenção.",
            desafio_deputado="Propor emenda reconstrução + moradia + SUS."),
    ]


def scorecard() -> Dict[str, Any]:
    briefings = _init_briefings()
    n_estados = len(briefings)
    total_problemas = sum(len(b.problemas) for b in briefings)
    emergencias = sum(b.n_problemas_emergencia for b in briefings)
    criticos = sum(1 for b in briefings if b.status_briefing == "CRITICO")

    return {
        "modulo": "open_briefing_estadual",
        "versao": "0.1.0-spec",
        "estados": n_estados,
        "total_problemas": total_problemas,
        "emergencias": emergencias,
        "estados_criticos": criticos,
    }


def _demo():
    briefings = _init_briefings()
    sc = scorecard()

    print("=" * 95)
    print("BRIEFING ESTADUAL: PROBLEMA + DADO + DESAFIO")
    print(f"{sc['estados']} estados · {sc['total_problemas']} problemas · {sc['emergencias']} emergências")
    print(f"{sc['estados_criticos']} estados CRÍTICOS (3+ emergências)")
    print("=" * 95)

    # Por regiao
    regioes = {
        "NORTE": ["AC", "AM", "AP", "PA", "RO", "RR", "TO"],
        "NORDESTE": ["MA", "PI", "CE", "RN", "PB", "PE", "AL", "SE", "BA"],
        "CENTRO-OESTE": ["MT", "MS", "GO", "DF"],
        "SUDESTE": ["SP", "RJ", "MG", "ES"],
        "SUL": ["PR", "SC", "RS"],
    }

    for regiao, ufs in regioes.items():
        print(f"\n{'='*95}")
        print(f"{regiao}")
        print(f"{'='*95}")

        for b in briefings:
            if b.uf not in ufs:
                continue

            status = b.status_briefing
            flag = " *** CRÍTICO" if status == "CRITICO" else (" *** ALERTA" if status == "ALERTA" else "")

            print(f"""
  ┌─ {b.uf} ({b.nome}){flag}
  │ POPULAÇÃO: {b.populacao_milhoes}M
  │ MEDIANA: R$ {b.p50:.0f}/mês  |  P10: R$ {b.p10:.0f}  |  P99: R$ {b.p99:.0f}
  │ DESIGUALDADE: {b.desigualdade_x:.0f}x  |  INDIGÊNCIA: {b.pct_indigente:.0f}%
  │ RACIAL: {b.gap_racial:.1f}x  |  GÊNERO: {b.gap_genero:.1f}x
  │ ECONOMIA: {b.economia_real[:80]}
  │
  │ PROBLEMAS ({b.n_problemas_emergencia} emergência):""")

            for p in b.problemas:
                nivel_flag = "🚨" if p.nivel == NivelProblema.EMERGENCIA else ("⚠️" if p.nivel == NivelProblema.ALTA else "📍")
                print(f"  │   {nivel_flag} [{p.cargo_responsavel}] {p.problema}")
                print(f"  │      Indicador: {p.indicador}")
                print(f"  │      Meta: {p.meta}")
                print(f"  │      Fonte: {p.fonte}")
                print(f"  │      PROPOSTA EXIGIDA: {p.proposta_exigida}")

            print(f"  │")
            print(f"  │ DESAFIO POR CARGO:")
            print(f"  │   🏛️ GOVERNADOR: {b.desafio_governador[:75]}")
            print(f"  │   📋 SENADOR: {b.desafio_senador[:75]}")
            print(f"  │   📄 DEPUTADO: {b.desafio_deputado[:75]}")
            print(f"  └─")

    print(f"\n{'='*95}")
    print(f"VEREDITO: {sc['estados_criticos']} estados CRÍTICOS")
    print(f"{'='*95}")
    print(f"""
  {sc['estados']} estados briefing completo.
  {sc['total_problemas']} problemas identificados com dado e fonte.
  {sc['emergencias']} emergências (matam agora).
  {sc['estados_criticos']} estados com 3+ emergências.

  CADA CANDIDATO QUE QUER ENTRAR:
    1. Lê o briefing do seu estado.
    2. Identifica o problema que seu cargo resolve.
    3. Traz proposta com Gate WO 7/7 (COMO, QUEM, CUSTO, PRAZO, MÉTRICA, FONTE, DIAGNÓSTICO).
    4. Sem proposta = W.O.

  O briefing existe pra NINGUÉM poder dizer 'não sabia'.
""")


if __name__ == "__main__":
    _demo()
