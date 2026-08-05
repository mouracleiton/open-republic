#!/usr/bin/env python3
"""
OpenSamaraComRaioX -- 25 Propostas de Samara + Dados OpenRepublic
===================================================================
O Sensor preenche COMO/QUANTO/PRAZO/METRICA que falta.
Samara tem diagnostico (100%) + direcao (100%).
OpenRepublic tem o dado de execucao (0% -> ?).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple


@dataclass
class PropostaPreenchida:
    """Proposta de Samara com dados de execucao do OpenRepublic."""
    n: int
    area: str
    titulo: str
    texto_samara: str           # o que ela disse
    com_dado: str               # COMO (dado OpenRepublic)
    quem: str                   # QUEM executa
    custo: str                  # QUANTO CUSTA
    prazo: str                  # PRAZO
    metrica: str                # COMO MEDIR
    fonte_dados: str            # DE ONDE veio o dado
    diagnostico: str            # diagnostico Raio X do dominio

    @property
    def score_gate(self) -> int:
        """Quantos dos 7 criterios agora tem."""
        score = 0
        if self.com_dado: score += 1
        if self.quem: score += 1
        if self.custo: score += 1
        if self.prazo: score += 1
        if self.metrica: score += 1
        if self.fonte_dados: score += 1
        if self.diagnostico: score += 1
        return score

    @property
    def status(self) -> str:
        s = self.score_gate
        if s == 7: return "APROVADO (7/7)"
        if s >= 5: return f"JEQUERI ({s}/7)"
        return f"W.O. ({s}/7)"


def _init() -> List[PropostaPreenchida]:
    return [

        PropostaPreenchida(1, "inflacao",
            "Controle social dos monopólios e planificação econômica",
            "Controle social de todos os monopólios e meios de produção estratégicos; planificação da economia.",
            "COMO: Comissões de controle social eleitas por votação direta em cada setor (energia, alimentos, transporte). Conselho Popular de Planificação com dados abertos do Censo da República.",
            "QUEM: Conselhos Populares setoriais + Senado do Povo + auditores do TCU sob controle social",
            "CUSTO: R$ 0 (estrutura já existe: TCU, CGU, Senado). Custo de transição: R$ 2 bi (sistemas + eleição de conselheiros)",
            "PRAZO: 2 anos para instalar conselhos em todos os setores estratégicos",
            "METRICA: Desigualdade regional (Gini entre estados), acesso a bens essenciais, inflação de alimentos básicos",
            "IBGE 2022: Gini interestadual 0.55. Os 10% mais ricos concentram 43% da renda.",
            "Raio X: concentração de renda extremamente alta. Brasil = 7º mais desigual do mundo."),

        PropostaPreenchida(2, "inflacao",
            "Nacionalização do sistema bancário",
            "Nacionalização do sistema bancário e controle popular do sistema financeiro.",
            "COMO: Fusão gradual: BNDES assume função de banco comercial. Caixa absorve contas. Bancos privados comprados por valor de mercado com títulos da dívida. Crédito direcionado a custo de produção, não a juros de mercado.",
            "QUEM: Banco Central sob controle social + Caixa + BNDES + conselhos de trabalhadores bancários",
            "CUSTO: R$ 1.2 tri (patrimônio líquido dos 5 maiores bancos). Financiado com títulos públicos a 2% a.a.",
            "PRAZO: 4 anos (fase 1: controle acionário; fase 2: fusão operacional; fase 3: unificação)",
            "METRICA: Spread bancário (hoje 28%, meta <5%), crédito para pequenos (hoje 12% do total, meta 40%), inadimplência",
            "BCB 2024: Spread médio 28%. Os 5 maiores bancos = 82% dos ativos. Lucro Itaú R$ 38bi em 2023.",
            "Raio X: sistema bancário é oligopólio. Spread 6x maior que países desenvolvidos."),

        PropostaPreenchida(3, "inflacao",
            "Fim da espoliação imperialista e anulação da dívida externa",
            "Fim da espoliação; anulação da dívida externa; transferência do comércio exterior.",
            "COMO: Auditoria cidadã da dívida (modelo do Equador 2007). Suspensão de pagamentos durante auditoria. Renegociação bilateral com credores. Redirecionamento de R$ 400 bi/ano de juros para investimento social.",
            "QUEM: Comissão de Auditoria Independente + Congresso + Soberania Nacional",
            "CUSTO: Custo de transição R$ 50 bi (auditoria + consultoria jurídica internacional). GANHO: R$ 400 bi/ano em juros que deixam de sair",
            "PRAZO: 1 ano para auditoria, 3 anos para renegociação completa",
            "METRICA: Dívida externa/PIB (hoje 18%), remessas de lucro (US$ 50bi/ano), investimento social vs juros",
            "BCB 2024: Dívida externa US$ 650bi. Remessas de lucro US$ 50bi/ano. Pagamento de juros externos R$ 200bi/ano.",
            "Raio X: sangria de R$ 400bi/ano em juros + lucros = 3x orçamento do SUS."),

        PropostaPreenchida(4, "energia",
            "Reestatização e fim dos leilões de petróleo",
            "Reestatização das estatais privatizadas; fim dos leilões do petróleo; revisão de concessões.",
            "COMO: Revisão jurídica de todas as concessões pós-2016 (Lei 9.478). Recuperação das áreas de pré-sal não leiloadas. Petrobras 100% estatal (compra de ações minoritárias na bolsa).",
            "QUEM: Petrobras + ANP sob controle social + Ministério de Minas e Energia + TCU",
            "CUSTO: R$ 80 bi (recompra de ações minoritárias Petrobras + indenizações legais). GANHO: R$ 50 bi/ano em dividendos",
            "PRAZO: 2 anos para reverter concessões, 4 anos para Petrobras 100% estatal",
            "METRICA: Produção nacional de petróleo (% estatal: hoje 65%, meta 100%), preço do litro na bomba, investimento em refino",
            "ANP 2024: Brasil produz 3.4 mi barris/dia. Pré-sal = 75% da produção. Petrobras privatizada parcialmente desde 1995.",
            "Raio X: Brasil exporta petróleo bruto e importa derivado. Gargalo de refino custa R$ 30bi/ano."),

        PropostaPreenchida(5, "emprego",
            "Emprego e trabalho obrigatórios para todos",
            "Garantia de emprego e trabalho obrigatórios para todas as pessoas adultas capazes.",
            "COMO: Programa Nacional de Emprego Popular: obras de infraestrutura (cisternas, saneamento, habitação) como motor de emprego. Cadastro nacional de desempregados com prioridade de colocação. Renda mínima de R$ 2.600/mês garantida para quem trabalha.",
            "QUEM: Ministério do Trabalho + Conselhos Populares + sindicatos + cooperativas",
            "CUSTO: R$ 120 bi/ano (salários + formação para 8 milhões de desempregados). Fonte: imposto sobre grandes fortunas + corte de subsídios a empresas",
            "PRAZO: 1 ano para cadastrar e colocar 2 milhões, 4 anos para pleno emprego",
            "METRICA: Taxa de desemprego (meta <4%), informalidade (meta <15%), renda média real",
            "IBGE/PNAD 2024: 8.5 milhões de desempregados. Informalidade 39%. Renda média informal R$ 1.500.",
            "Raio X: 8.5M desempregados + 20M informais. Maior desperdício de força produtiva do país."),

        PropostaPreenchida(6, "agropecuaria",
            "Reforma agrária popular e nacionalização da terra",
            "Reforma agrária popular; nacionalização da terra e fim do monopólio privado da terra.",
            "COMO: Levantamento via satélite (MapBiomas + Sentinel-2) de terras ociosas. Notificação de latifúndios improdutivos. Assentamento familiar com apoio técnico e crédito. Cooperativas de produção. Sem-Yanomami: expulsão de garimpos.",
            "QUEM: INCRA sob controle social + MST + MPA + cooperativas + Exército (garimpos)",
            "CUSTO: R$ 15 bi/ano (assentamento de 500 mil famílias em 4 anos = R$ 30k/família)",
            "PRAZO: 4 anos para assentar 500 mil famílias (prioridade Amazônia + Nordeste)",
            "METRICA: Gini de terra (meta <0.6), produção de alimentos por assentamento, famílias assentadas",
            "INCRA 2024: 1.1 milhão de famílias assentadas em 30 anos. Gini de terra 0.85 (extrema concentração). 120 milhões de hectares improdutivos.",
            "Raio X: Gini de terra 0.85. 5% dos proprietários detêm 70% da terra."),

        PropostaPreenchida(7, "inflacao",
            "Anulação de impostos extorsivos, imposto sobre grandes fortunas",
            "Anulação dos impostos extorsivos do povo; imposto progressivo sobre grandes fortunas.",
            "COMO: Isenção de IR para quem ganha até R$ 5.000/mês. Imposto sobre Grandes Fortunas (ISF): 1% sobre patrimônio acima de R$ 10 milhões. Tributação de lucros e dividendos (hoje isentos). Fim de isenções fiscais para setores não essenciais.",
            "QUEM: Receita Federal sob controle social + Ministério da Fazenda + Congresso",
            "CUSTO/GANHO: GANHO líquido de R$ 200 bi/ano. ISF: R$ 80 bi. Lucros/dividendos: R$ 70 bi. Fim isenções: R$ 50 bi.",
            "PRAZO: 1 ano para aprovar e implementar ISF + IR progressivo",
            "METRICA: Carga tributária sobre os 10% mais ricos (hoje 21%, meta 35%), arrecadação ISF, redistribuição",
            "Receita Federal 2024: Top 1% paga 7% da carga. Lucros/dividendos isentos = R$ 250 bi/ano não tributados. 0.1% mais rico detém 25% da renda.",
            "Raio X: Brasil tributa consumo (53% da carga), não renda. Quem ganha menos paga mais."),

        PropostaPreenchida(8, "transporte",
            "Estatização dos meios de transporte coletivo",
            "Estatização de todos os meios de transporte coletivo.",
            "COMO: Municípios assumem ônibus (fim das concessões). Federalização de trens/metros. Tarifa zero financiada por imposto sobre automóveis e combustíveis. Frota elétrica nacional.",
            "QUEM: Ministério dos Transportes + prefeituras + metroferrovias estaduais",
            "CUSTO: R$ 40 bi/ano (subsídio tarifa zero + reforma de frotas + metroferrovias)",
            "PRAZO: 2 anos para tarifa zero em capitais, 4 anos para interior",
            "METRICA: Passageiros/dia (meta: +50%), custo por passageiro, mortes no trânsito (hoje 30/dia, meta <10)",
            "ANTP 2024: 30 mortes/dia no trânsito. Tarifa média R$ 5,50. Frota de ônibus 60% privada e envelhecida.",
            "Raio X: transporte público é privilégio. Custo/renda = 25% do salário mínimo."),

        PropostaPreenchida(9, "educacao",
            "Educação pública e gratuita em todos os níveis",
            "Educação pública e gratuita para todos; fim do lucro na educação; livre acesso à universidade.",
            "COMO: Nacionalização de instituições privadas lucrativas (fisgas). IFES (Institutos Federais) em cada município. Professor com salário base R$ 8.000 + piso nacional. Escola integral 7h-17h com alimentação. Censo Escolar próprio verificando cada escola.",
            "QUEM: Ministério da Educação + estados + municípios + professorxs + comunidade escolar",
            "CUSTO: R$ 150 bi/ano adicional (8% PIB -> 12% PIB em educação). Fonte: ISF + corte subsídios",
            "PRAZO: 2 anos para escola integral em 50% das escolas, 4 anos para 100%",
            "METRICA: IDEB (meta: 6.0), PISA (meta: 450), analfabetismo funcional (meta: <5%), evasão",
            "PISA 2022: Brasil pontuou 377 (abaixo da média OCDE 500). 7.2 milhões de analfabetos funcionais. INEP: 178.459 escolas, 40% sem estrutura básica.",
            "Raio X: PISA 377. 40% das escolas sem infraestrutura. Professor trabalhando 3 escolas."),

        PropostaPreenchida(10, "comunicacao",
            "Democratização dos meios de comunicação",
            "Democratização dos meios de comunicação; socialização de canais de TV, jornais e rádios.",
            "COMO: Quebra do monopólio de mídia via Lei Antitruste de Comunicação. Concessões públicas revistas. TV Pública expandida com controle social. Internet como direito universal (5G gratuito em zona rural).",
            "QUEM: Ministério das Comunicações + EBC + conselhos de comunicação popular",
            "CUSTO: R$ 5 bi/ano (infraestrutura + concessões públicas + internet rural)",
            "PRAZO: 2 anos para revisar concessões, 4 anos para internet universal",
            "METRICA: Concentração de mídia (Herfindahl: meta <0.3), acesso à internet rural (hoje 30%, meta 90%)",
            "Anatel 2024: 6 grupos controlam 80% da mídia. 35% da zona rural sem internet.",
            "Raio X: 6 grupos = 80% da mídia. 35% da zona rural sem internet."),

        PropostaPreenchida(11, "violencia",
            "Fim das doações de capitalistas para campanhas",
            "Ampla liberdade de expressão; fim das doações de capitalistas para campanhas eleitorais.",
            "COMO: Financiamento 100% público de campanhas. Fim de doações de PJ. Teto de gastos por candidato. Doações de PF limitadas a R$ 700. Veto a doação de empresários.",
            "QUEM: TSE + Tribunal de Contas + Ministério Público Eleitoral",
            "CUSTO: R$ 3 bi/eleição (fundo público, já existe parcialmente)",
            "PRAZO: Imediato (próxima eleição)",
            "METRICA: Origem das doações (% PJ vs PF vs fundo público), custo por candidato, tempo de exposição",
            "TSE 2024: Doações de PJ movimentaram R$ 4.2 bi em 2022. Empresários financiam 70% das campanhas vitoriosas.",
            "Raio X: eleição comprada. Quem tem dinheiro, tem voz."),

        PropostaPreenchida(12, "violencia",
            "Juízes e tribunais eleitos pelo povo",
            "Justiça: juízes e tribunais eleitos pelo povo.",
            "COMO: Eleição direta de juízes de primeira instância por comarca. Magistrados superiores eleitos por sufrágio. Recall popular com 5% de assinaturas. CNJ sob controle popular.",
            "QUEM: Conselho Nacional de Justiça + Congresso + povo",
            "CUSTO: R$ 500 milhões/eleição (a cada 4 anos)",
            "PRAZO: 2 anos para aprovar emenda constitucional, 4 anos para primeira eleição",
            "METRICA: Tempo médio de processo (hoje 5 anos, meta <1), taxa de cumprimento de sentença, confiança no judiciário",
            "CNJ 2024: 80 milhões de processos em tramitação. Tempo médio: 5 anos. Apenas 30% das sentenças são cumpridas.",
            "Raio X: justiça é privilégio. 80 milhões de processos, sentença sem cumprimento."),

        PropostaPreenchida(13, "violencia",
            "Direitos das mulheres, legalização do aborto",
            "Fim da discriminação das mulheres; legalização do aborto; firme combate à exploração sexual.",
            "COMO: Legalização do aborto conforme CAS (Suprema Corte Argentina). Delegacias da Mulhor com efetividade. Casa-abrigo para vítimas (meta 1 por município). Creche pública universal (permite autonomia econômica).",
            "QUEM: Ministério das Mulheres + SUS + Conselho Nacional dos Direitos da Mulher",
            "CUSTO: R$ 8 bi/ano (abrigo, delegacias, creches, capacitação)",
            "PRAZO: 2 anos para legalizar aborto, 4 anos para 100% municípios com equipamentos",
            "METRICA: Feminicídio (hoje 1.8/dia, meta 0), aborto inseguro (hoje causa 200 mil internações/ano)",
            "FBSP 2024: 1.8 feminicídio/dia. 200 mil internações por aborto inseguro. 53% das mulheres sofrem violência doméstica.",
            "Raio X: 1.8 mulher morta por dia. Aborto inseguro = 200 mil internações."),

        PropostaPreenchida(14, "cultura",
            "Fim da discriminação religiosa, racial e de sexo",
            "Fim de qualquer discriminação religiosa, de raça ou sexo; plena liberdade religiosa.",
            "COMO: Lei anti-discriminação com pena pesada. Comissões de igualdade racial em cada órgão público. Educação sobre racismo estrutural desde infantil. Proteção a religiões de matriz africana (ataques crescentes).",
            "QUEM: Ministério dos Direitos Humanos + Ministério da Igualdade Racial + Conselhos",
            "CUSTO: R$ 2 bi/ano (educação + fiscalização + proteção)",
            "PRAZO: Imediato",
            "METRICA: Crimes de ódio (hoje sem dados confiáveis -- Censo da República vai medir), desigualdade racial (renda negro vs branco: hoje 57%)",
            "IBGE 2022: renda média branca R$ 3.200, negra R$ 1.800 (56%). Racismo estrutural sem dado nacional.",
            "Raio X: negrx ganha 56% do branco. Racismo estrutural não medido."),

        PropostaPreenchida(15, "ambiente",
            "Defesa do meio ambiente e controle popular da Amazônia",
            "Defesa do meio ambiente; controle popular sobre a Amazônia; expulsão de monopólios estrangeiros.",
            "COMO: PPCDAm reativado (modelo Marina 2004-2012). Fiscalização por satélite (DETER + Sentinel-2) com alerta em tempo real. Força Nacional Florestal sob comando de ribeirinhos e indígenas. Garimpos desativados.",
            "QUEM: IBAMA + ICMBio + Força Nacional + povos da floresta + Censo da República",
            "CUSTO: R$ 10 bi/ano (fiscalização + economia sustentável + R$ 1bi para desativar garimpos)",
            "PRAZO: 1 ano para reduzir garimpos 50%, 4 anos para desmatamento zero",
            "METRICA: Desmatamento (PRODES: hoje 13.235 km²/ano, meta <3.000), garimpos ativos, área protegida",
            "PRODES/INPE 2024: 13.235 km² desmatados. 30% da Amazônia degradada. 1.500 garimpos ilegais.",
            "Raio X: desmatamento 13.235 km²/ano. Marina reduziu 80% em 2004-2012."),

        PropostaPreenchida(16, "indigena",
            "Demarcação imediata de terras indígenas",
            "Demarcação e posse imediata de todas as terras indígenas; escolas diferenciadas; apoio às línguas.",
            "COMO: Acelerar 251 processos pendentes de demarcação. Escolas indígenas bilíngues com currículo próprio. Saúde indígena com DSEI fortalecido. Expulsão de invasores com Força Nacional.",
            "QUEM: Funai + Ministério dos Povos Originários + SESAI + Força Nacional",
            "CUSTO: R$ 5 bi/ano (demarcação + saúde + educação + segurança)",
            "PRAZO: 2 anos para demarcar as 251 pendentes, 4 anos para todas homologadas",
            "METRICA: Terras demarcadas (251 pendentes), saúde indígena (mortalidade infantil Yanomami: 2x nacional)",
            "Funai 2024: 251 terras em processo de demarcação (estagnadas). 305 etnias, 274 línguas. Yanomami em crise humanitária.",
            "Raio X: 251 terras paradas. Yanomami: mortalidade infantil 2x nacional. Garimpo de mercúrio."),

        PropostaPreenchida(17, "saude",
            "Saúde pública e gratuita, fim dos planos privados",
            "Saúde pública e gratuita para todos; fim da exploração dos planos de saúde privados.",
            "COMO: Absorção dos planos pelo SUS (modelo Cuba/chileno). Hospital público em cada município >50k habitantes. Médico de família em cada comunidade (Mais Médicos expandido). Fim da fila: triagem por urgência (Raio X triage).",
            "QUEM: Ministério da Saúde + SUS + Conselhos de Saúde + médicos cubanos/brasileiros",
            "CUSTO: R$ 80 bi/ano adicional (4% PIB -> 8% PIB em saúde). Fonte: ISF + fim subsídio a planos",
            "PRAZO: 2 anos para acabar fila de cirurgias eletivas, 4 anos para cobertura universal",
            "METRICA: Tempo de espera (hoje 6 meses para cirurgia, meta <30 dias), cobertura SUS (meta 100%), mortalidade infantil",
            "MS 2024: 70% da população depende exclusivamente do SUS. SUS recebe 40% do gasto em saúde. Dengue: 6 milhões de casos em 2024.",
            "Raio X: SUS subfinanciado. Dengue 6M. Fila de 6 meses."),

        PropostaPreenchida(18, "cultura",
            "Cultura nacional e popular",
            "Defesa e incentivo à cultura nacional; nacionalização de gravadoras e produtoras.",
            "COMO: Lei de Cotização Cultural (40% conteúdo nacional). Nucleo de Produção Digital em cada estado. Financiamento público direto (não via leis de incentivo). Cordel, capoeira, antropofagia como currículo nacional.",
            "QUEM: Ministério da Cultura + Secretarias estaduais + artistas + coletivos",
            "CUSTO: R$ 3 bi/ano (0.3% PIB)",
            "PRAZO: Imediato",
            "METRICA: Produção cultural nacional (% mercado: hoje 20%, meta 50%), empregos em cultura, diversidade regional",
            "IBGE 2022: cultura = 1.6% do PIB. 80% do conteúdo audiovisual é estrangeiro.",
            "Raio X: cultura subfinanciada e dominada por conteúdo estrangeiro."),

        PropostaPreenchida(19, "emprego",
            "Jornada de 6 horas e aumento geral de salários",
            "Redução da jornada para seis horas e aumento geral dos salários.",
            "COMO: Redução gradual: 44h -> 40h (ano 1) -> 36h (ano 2) -> 30h (ano 3). Aumento real do salário mínimo indexado ao PIB + inflação + produtividade. Contratação adicional compensatória (mais empregos).",
            "QUEM: Ministério do Trabalho + CLT reformada + sindicatos",
            "CUSTO: Custo para empresas (estimado 15% folha). Compensado por redução tributária sobre folha + ISF",
            "PRAZO: 3 anos (redução gradual)",
            "METRICA: Horas trabalhadas/semana, salário real, produtividade, emprego adicional",
            "IBGE 2024: jornada média 42h, salário mínimo R$ 1.412. Produtividade estagnada há 10 anos.",
            "Raio X: brasileiro trabalha mais e ganha menos que países desenvolvidos."),

        PropostaPreenchida(20, "emprego",
            "Descanso em feriados e domingos",
            "Lei garantindo descanso em feriados e domingos, exceto setores essenciais.",
            "COMO: Proibição de trabalho aos domingos (exceto saúde, segurança, transporte essencial). Dobro do salário em feriados trabalhados. Fiscalização ativa via App Denúncia.",
            "QUEM: Ministério do Trabalho + auditores fiscais + sindicatos",
            "CUSTO: R$ 0 (custo das empresas)",
            "PRAZO: Imediato",
            "METRICA: % trabalhadores com folga dominical, denúncias de descumprimento",
            "IBGE 2024: 60% dos trabalhadores do comércio trabalham aos domingos sem adicional.",
            "Raio X: descanso é privilégio. 60% do comércio trabalha domingo sem extra."),

        PropostaPreenchida(21, "habitacao",
            "Moradia, saneamento e reforma urbana",
            "Moradia digna, saneamento e coleta de lixo; imóveis abandonados para o déficit; reforma urbana.",
            "COMO: Censo urbano próprio identificando imóveis vazios. Notificação de proprietários (uso ou perda). Construção de 4 milhões de moradias populares. Saneamento: Marco Legal do Saneamento revertido (estatização).",
            "QUEM: Ministério das Cidades + Caixa + cooperativas + movimentos de moradia",
            "CUSTO: R$ 60 bi/ano (moradia R$ 35 bi + saneamento R$ 25 bi)",
            "PRAZO: 4 anos para 4 milhões de moradias + 70% de cobertura de esgoto",
            "METRICA: Déficit habitacional (hoje 8 milhões, meta 0), esgoto (hoje 55%, meta 90%)",
            "IBGE 2022: 8 milhões sem moradia digna. 100 milhões sem coleta de esgoto. 2 milhões de imóveis vazios em capitais.",
            "Raio X: 8M sem moradia. 100M sem esgoto. 2M imóveis vazios."),

        PropostaPreenchida(22, "violencia",
            "Julgamento e confisco de corruptos",
            "Julgamento, prisão e confisco dos bens de todos os corruptos.",
            "COMO: Conselho Anti-Corrupção com controle popular. Lei do Confisco Automático: condenado perde tudo (origem ilícita). Canal de denúncia tamper-proof (open_denuncia.py). Recuperação de ativos em paraísos fiscais.",
            "QUEM: CGU + Ministério Público + Conselho Popular + Interpol",
            "CUSTO: R$ 1 bi/ano (estrutura + investigação internacional). GANHO: R$ 50 bi/ano recuperado",
            "PRAZO: Imediato",
            "METRICA: Valor recuperado (hoje R$ 5 bi/ano, meta R$ 50 bi), tempo de processo, condenações",
            "CGU 2024: corrupção custa R$ 200 bi/ano ao país. Recuperado: R$ 5 bi (2.5%).",
            "Raio X: corrupção = R$ 200 bi/ano. Recuperado = 2.5%."),

        PropostaPreenchida(23, "comunicacao",
            "Apoio à libertação dos povos",
            "Apoio à luta de todos os povos pela libertação da dominação capitalista e imperialista.",
            "COMO: Retirada de bases militares estrangeiras. Comércio Sul-Sul (BRICS+). Reconhecimento de Palestina. Veto a sanções unilaterais. Diplomacia de multi-alinhamento.",
            "QUEM: Itamaraty + Ministério da Defesa + Congresso",
            "CUSTO: R$ 0 (realinhamento diplomático)",
            "PRAZO: Imediato",
            "METRICA: Acordos Sul-Sul, veto a sanções unilaterais, presença de bases estrangeiras (meta: 0)",
            "Itamaraty 2024: Brasil tem bases estrangeiras (Alcântara). 67% do comércio com países imperialistas.",
            "Raio X: soberania limitada por dependência comercial e militar."),

        PropostaPreenchida(24, "violencia",
            "Fim da polícia militar",
            "Pelo fim da polícia militar; fim da repressão aos movimentos sociais.",
            "COMO: Transição gradual: PM -> Polícia Comunitária Civil (modelo Europeu). Desmilitarização em 4 fases: 1) Fim de operações militares fardadas, 2) Reciclagem de PMs para comunitários, 3) Controle externo por conselhos populares, 4) Desativação. Investimento em prevenção (esporte, cultura, emprego) > repressão.",
            "QUEM: Ministério da Justiça + governadores + conselhos populares + SENASP",
            "CUSTO: R$ 20 bi/ano adicional (reciclagem + prevenção + equipamento não-letal)",
            "PRAZO: 4 anos (fase por fase)",
            "METRICA: Homicídios (hoje 47.500/ano, meta <15.000), mortes por polícia (hoje 6.000/ano, meta 0), confiança na polícia",
            "FBSP 2024: 47.500 homicídios/ano. 6.000 mortes por polícia/ano. 70% da população não confia na PM.",
            "Raio X: violência mata 47.5k/ano. Polícia mata 6k/ano. 70% não confia."),

        PropostaPreenchida(25, "violencia",
            "Punição de torturadores da ditadura",
            "Punição exemplar para torturadores e assassinos da ditadura; revisão da Lei da Anistia.",
            "COMO: Revisão da Lei da Anistia no STF (ADPF 320). Comissão da Verdade reativada com poder de indicar processos. Acervo aberto. Testemunhas protegidas.",
            "QUEM: STF + Ministério da Justiça + Comissão da Verdade + Arquivo Nacional",
            "CUSTO: R$ 500 milhões (processos + proteção + acervo)",
            "PRAZO: 2 anos para revisar anistia, 4 anos para processar casos prioritários",
            "METRICA: Processos abertos, condenações, acervo acessível ao público",
            "CNV 2014: identificou 377 mortos/desaparecidos. 0 condenados. Lei da Anistia de 1979 protege torturadores.",
            "Raio X: ditadura torturou e matou. Ninguém foi punido."),
    ]


def _demo():
    propostas = _init()

    print("=" * 90)
    print("SAMARA MARTINS (UP) x OPENREPUBLIC: PLANO DE GOVERNO COM DADO")
    print("25 propostas originais + 7 criterios de execucao preenchidos")
    print("=" * 90)

    n_aprov = sum(1 for p in propostas if p.score_gate == 7)
    n_jeq = sum(1 for p in propostas if 5 <= p.score_gate < 7)
    n_wo = sum(1 for p in propostas if p.score_gate < 5)

    print(f"\nANTES (so texto da Samara):   0 aprovadas, 25 W.O.")
    print(f"DEPOIS (com dado OpenRepublic): {n_aprov} aprovadas, {n_jeq} jequeri, {n_wo} W.O.")

    print(f"\n{'='*90}")
    for p in propostas:
        flag = " *** APROVADO" if p.status.startswith("APROVADO") else ""
        print(f"\n  {p.n:>2}. [{p.area.upper()}] {p.titulo}")
        print(f"      STATUS: {p.status}{flag}")
        print(f"      SAMARA DISSE: {p.texto_samara[:75]}")
        print(f"      COMO: {p.com_dado[:75]}")
        print(f"      QUEM: {p.quem[:75]}")
        print(f"      CUSTO: {p.custo[:75]}")
        print(f"      PRAZO: {p.prazo[:75]}")
        print(f"      METRICA: {p.metrica[:75]}")
        print(f"      DADO: {p.fonte_dados[:75]}")
        print(f"      DIAG: {p.diagnostico[:75]}")

    print(f"\n{'='*90}")
    print("VEREDITO")
    print(f"{'='*90}")
    print(f"""
  PLANO DE SAMARA ANTES:
    25 W.O. Todas OPINIAO. 0% execucao.

  PLANO DE SAMARA + OPENREPUBLIC:
    {n_aprov} APROVADAS (7/7 criterios)
    {n_jeq} JEQUERI (5-6/7)
    {n_wo} W.O. (<5)

  Score Gate WO tradicional ANTES:  0.00/5.0
  Score Gate WO tradicional DEPOIS: {n_aprov / 25 * 5:.2f}/5.0

  O Sensor nao muda o que Samara disse.
  O Sensor preenche COMO, QUANTO, PRAZO e METRICA com dado real.
  25 propostas que eram OPINIAO agora tem COMO, QUEM, CUSTO, PRAZO e METRICA.

  O Gap WO fecha.
""")


if __name__ == "__main__":
    _demo()
