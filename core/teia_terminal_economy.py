#!/usr/bin/env python3
"""
TEIA Terminal Economy -- Simulacao Completa -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
TEIA Terminal Economy -- Simulacao Completa
=============================================
O MODELO:
1. TERMINAL (Hermes customizado) = produto principal
2. REVENDEDOR usa terminal para produzir artefatos
3. REVENDEDOR paga 30% sobre produto final
4. TEIA DIRETO (not revendedor) executa sem pagar 30%
5. POOL revisto para melhor distribuicao
6. CERTIFICACAO obrigatoria
7. ID bloqueia dados sensiveis
8. PAGAMENTO pode ser cripto (legislacao)
9. MODULO FALTANTE = sistema bloqueia artefato
Author: TEIA / OpenRepublic Team
# 
# importa annotations de __future__
# importa math
# importa random
# importa dataclass, field de dataclasses
# importa Any, Dict, List, Optional, Tuple de typing
# importa Enum de enum
# importa defaultdict de collections
# ============================================================================
# 1. PERFIS DE REVENDEDOR (quem compra o terminal)
# ============================================================================
class ResellerProfile(Enum):
    # Arquetipos de quem compraria o terminal TEIA.
    CONSULTOR_INDEPENDENTE = (
        "Consultor Independente",
        "Consultor politico/socioeconomico autonomo. Ja vende parecere para prefeitura/ONG.",
        0.60, // probabilidade de comprar terminal
        3, // artefatos/mes produzidos
        15_000, // ticket medio por artefato
    )
    ASSESSOR_PARLAMENTAR = (
        "Assessor Parlamentar",
        "Trabalha em gabinete. Precisa de dossies para o deputado/senador.",
        0.40,
        5,
        8_000,
    )
    ONG_ANALISTA = (
        "Analista de ONG",
        "ONG precisa de dados para advocacy. Hoje paga FGV/IPEA.",
        0.50,
        2,
        20_000,
    )
    JORNALISTA_DADOS = (
        "Jornalista de Dados",
        "Veiculo/jornalista independente que precisa de analise tecnica.",
        0.30,
        4,
        5_000,
    )
    ESCRITORIO_ADVOCACIA = (
        "Escritorio de Advocacia",
        "Pareceres para audiencias publicas, acoes civis publicas.",
        0.35,
        2,
        30_000,
    )
    CONSULTORIA_ESTUDANTE = (
        "Estudante de Pos/Mestrado",
        "Pesquisador que precisa de dados curados para tese/artigo.",
        0.20,
        1,
        3_000,
    )
    SEBRAE_SENAC = (
        "Instrutor SEBRAE/SENAC/Escola de Governo",
        "Ensina politica publica. Usa terminal como ferramenta + revende.",
        0.25,
        3,
        12_000,
    )
    STARTUP_GOVTECH = (
        "Startup Govtech",
        "Empresa que vende para governo. TEIA and insumo.",
        0.45,
        6,
        25_000,
    )
    funcao __init__(self, label: texto, description: texto,
                buy_probability: flutuante,
                artifacts_per_month: inteiro,
                avg_ticket_brl: flutuante):
        self.label = label
        self.description = description
        self.buy_probability = buy_probability
        self.artifacts_per_month = artifacts_per_month
        self.avg_ticket_brl = avg_ticket_brl
# ============================================================================
# 2. MERCADO ENDERECAVEL (quantos existem no Brasil)
# ============================================================================
MARKET_SIZE = {
    ResellerProfile.CONSULTOR_INDEPENDENTE: 2_000, // consultores politicos no Brasil
    ResellerProfile.ASSESSOR_PARLAMENTAR: 3_500, // 594 parlamentares x ~6 assessores
    ResellerProfile.ONG_ANALISTA: 1_500, // ONGs com foco em policy
    ResellerProfile.JORNALISTA_DADOS: 800, // jornalistas de dados/economia
    ResellerProfile.ESCRITORIO_ADVOCACIA: 500, // escritorios com area publico
    ResellerProfile.CONSULTORIA_ESTUDANTE: 5_000, // pos-grad em ciencia social
    ResellerProfile.SEBRAE_SENAC: 1_200, // instrutores de escolas de governo
    ResellerProfile.STARTUP_GOVTECH: 300, // govtechs ativas no Brasil
}
# ============================================================================
# 3. SIMULACAO DE DEMANDA
# ============================================================================
# decorador: @dataclass
class SimulationResult:
    profile: ResellerProfile
    market_size: inteiro
    interested: inteiro // quantos comprariam
    terminal_revenue: flutuante // receita de mensalidade
    training_revenue: flutuante // receita de treinamento
    artifact_revenue: flutuante // receita 30% sobre produtos
    total_revenue: flutuante
    artifacts_produced: inteiro
funcao simulate_demand(
    terminal_monthly_brl: float = 1_500,
    training_brl: float = 2_000,
    teia_pct: float = 0.30,
    months: int = 12,
    seed: int = 42,
) -> [SimulationResult]:
    # Simula quantos comprariam o terminal e quanto ganhamos.
    rng = random.Random(seed)
    results = []
    for profile in ResellerProfile:
        market = MARKET_SIZE[profile]
        # Quantos comprariam (probabilidade x mercado)
        # Aplicar ruido (mercado real nao e deterministico)
        base_interested = inteiro(market * profile.buy_probability)
        # Fase de adocao (nao todo mundo compra no mes 1)
        # Mes 1: 10% dos interessados
        # Mes 6: 50%
        # Mes 12: 90%
        adoption_curve = [0.10, 0.15, 0.25, 0.35, 0.45, 0.50,
                        0.60, 0.70, 0.78, 0.84, 0.88, 0.90]
        # interessados no final de 12 meses
        final_interested = inteiro(base_interested * adoption_curve[-1])
        # Receita de terminal (mensalidade)
        avg_active = inteiro(base_interested * sum(adoption_curve) / len(adoption_curve))
        terminal_rev = avg_active * terminal_monthly_brl * months
        # Receita de treinamento (todo novo revendedor paga treinamento uma vez)
        training_rev = final_interested * training_brl
        # Receita de artefatos (30% sobre produtos vendidos pelos revendedores)
        active_monthly = inteiro(base_interested * adoption_curve[-1])
        artifacts_month = active_monthly * profile.artifacts_per_month
        artifact_rev_month = artifacts_month * profile.avg_ticket_brl * teia_pct
        artifact_rev = artifact_rev_month * months * 0.5 // 50% do ano (curva de adocao)
        total = terminal_rev + training_rev + artifact_rev
        results.append(SimulationResult(
            profile = profile,
            market_size = market,
            interested = final_interested,
            terminal_revenue = terminal_rev,
            training_revenue = training_rev,
            artifact_revenue = artifact_rev,
            total_revenue = total,
            artifacts_produced = artifacts_month * months,
        ))
    return results
# ============================================================================
# 4. DISTRIBUICAO DOS 30% (o coracao do modelo)
# ============================================================================
# decorador: @dataclass
class RevenueSplit:
    # Como os 30% do produto final se distribuem.
    EXEMPLO:
    Revendedor vende dossie por R$50.000.
    30% = R$15.000 vai para TEIA.
    70% = R$35.000 fica com revendedor.
    Dos R$15.000 (30%):
        - Pool da Republica (revisado)
        - Criadores dos dados/modelos (royalty chain)
        - Manutencao do terminal
        - Infraestrutura
        - Certificacao/qualidade
        - Fundo de garantia
    # 
    # ATE AGORA: 5% pool fixo.
    # REVISAO: pool nao e mais 5% fixo. E UMA DAS FATIAS dos 30%.
    # Distribuicao dos 30%:
    POOL_REPUBLICA = 0.25 // 25% dos 30% = 7,5% do produto final
    ROYALTY_CHAIN = 0.30 // 30% dos 30% = 9% do produto final
    TERMINAL_MAINT = 0.15 // 15% dos 30% = 4,5% do produto final
    INFRASTRUCTURE = 0.10 // 10% dos 30% = 3% do produto final
    CERTIFICATION = 0.08 // 8% dos 30% = 2,4% do produto final
    GUARANTEE_FUND = 0.07 // 7% dos 30% = 2,1% do produto final
    FOUNDING_TEAM = 0.05 // 5% dos 30% = 1,5% do produto final
    # decorador: @classmethod
    def validate(cls) -> bool:
        total = (cls.POOL_REPUBLICA + cls.ROYALTY_CHAIN + cls.TERMINAL_MAINT +
                cls.INFRASTRUCTURE + cls.CERTIFICATION + cls.GUARANTEE_FUND +
                cls.FOUNDING_TEAM)
        return abs(total - 1.0) < 0.001
    # decorador: @classmethod
    funcao breakdown(cls, product_price_brl: flutuante) retorna List[{texto: qualquer}]:
        # Detalha para onde vai cada centavo dos 30%.
        teia_share = product_price_brl * 0.30
        items = [
            ("Pool da Republica", cls.POOL_REPUBLICA,
            "Distribuido democraticamente (assembleia). Financia OpenRepublic."),
            ("Royalty Chain", cls.ROYALTY_CHAIN,
            "Quem criou os dados/modelos usados no artefato. Proporcional ao peso."),
            ("Manutencao Terminal", cls.TERMINAL_MAINT,
            "Atualizacoes, bugfix, suporte, evolucao do Hermes customizado."),
            ("Infraestrutura", cls.INFRASTRUCTURE,
            "Servidor, API, armazenamento, processamento."),
            ("Certificacao", cls.CERTIFICATION,
            "Auditoria de qualidade, revisao de artefatos, treinamento."),
            ("Fundo de Garantia", cls.GUARANTEE_FUND,
            "Reserva para reembolso se artefato tiver erro comprovado."),
            ("Equipe Fundadora", cls.FOUNDING_TEAM,
            "Cleiton + nucleo inicial. Reconhecimento de trabalho de construcao."),
        ]
        result = []
        para name, pct, desc in items:
            amount = teia_share * pct
            result.append({
                "item": name,
                "pct_of_30": pct,
                "pct_of_product": pct * 0.30,
                "amount_brl": amount,
                "description": desc,
            })
        return result
# ============================================================================
# 5. DISTRIBUICAO DO POOL (revisada)
# ============================================================================
class PoolDistribution:
    # Como o POOL DA REPUBLICA e distribuido internamente.
    ANTES: 5% fixo para "pool da Republica" (caixa unico).
    PROBLEMA: 5% not cobre as necessidades da organizacao.
    AGORA: o pool and 25% dos 30% (7,5% do produto final).
    and distribuido em SUB-FATIAS para garantir que cada area recebe:
    - OPERACOES (servidor, API, infra basica)
    - DESENVOLVIMENTO (novos modulos, melhorias)
    - COMUNIDADE (eventos, comunicacao, X/Twitter)
    - PILOTO COMUNITARIO (OpenCredit em comunidades)
    - EMERGENCIA (fundo de crise)
    - REINVESTIMENTO (novos dados, novos modelos)
    # 
    POOL_SPLITS = {
        "operacoes": 0.20,          // 20% do pool
        "desenvolvimento": 0.25,    // 25% do pool
        "comunidade": 0.15,         // 15% do pool
        "piloto_comunitario": 0.20,# 20% do pool
        "emergencia": 0.10,         // 10% do pool
        "reinvestimento": 0.10,     // 10% do pool
    }
    # decorador: @classmethod
    def validate(cls) -> bool:
        return abs(sum(cls.POOL_SPLITS.values()) - 1.0) < 0.001
    # decorador: @classmethod
    funcao breakdown(cls, pool_amount_brl: flutuante) retorna List[{texto: qualquer}]:
        result = []
        desc_map = {
            "operacoes": "Servidor, API, DNS, certificados, monitoramento.",
            "desenvolvimento": "Novos modulos, melhorias, migracao Python->Rust.",
            "comunidade": "Eventos, X/Twitter, documentacao publica, onboarding.",
            "piloto_comunitario": "OpenCredit em comunidades. Implementacao + manutencao.",
            "emergencia": "Reserva para crise (processo, ataque, falha critica).",
            "reinvestimento": "Comprar novos dados, contratar pesquisadores, expandir.",
        }
        for each (name, pct) in cls.POOL_SPLITS.items():
            result.append({
                "area": name,
                "pct": pct,
                "amount_brl": pool_amount_brl * pct,
                "description": desc_map[name],
            })
        return result
# ============================================================================
# 6. CERTIFICACAO
# ============================================================================
class Certification(Enum):
    # Niveis de certificacao para revendedores.
    Sem certificacao: not pode revender.
    Cada nivel desbloqueia modulos do terminal.
    # 
    TEIA_BASE = (
        "TEIA Base",
        "Treinamento 16h remoto. Aprende a usar o terminal, gerar dossies basicos.",
        2_000, // custo do treinamento
        ["fome", "saneamento", "emprego", "educacao"],   // modulos desbloqueados
    )
    TEIA_ANALISTA = (
        "TEIA Analista",
        "Base + 24h. Aprende modelos de impacto fiscal, cruzamento de dados.",
        4_000,
        ["fome", "saneamento", "emprego", "educacao", "impacto_fiscal", "simulador"],
    )
    TEIA_ESPECIALISTA = (
        "TEIA Especialista",
        "Analista + 32h. Aprende due diligence, parecer juridico, modelos avancados.",
        8_000,
        ["*"],   // todos os modulos exceto sensiveis
    )
    funcao __init__(self, label: texto, description: texto,
                training_cost_brl: flutuante, unlocked_modules: [texto]):
        self.label = label
        self.description = description
        self.training_cost_brl = training_cost_brl
        self.unlocked_modules = unlocked_modules
# ============================================================================
# 7. CONTROLE DE ACESSO POR ID (dados sensiveis)
# ============================================================================
# decorador: @dataclass
class ModuleAccess:
    # Cada modulo do terminal requer nivel de certificacao.
    Modulos sensiveis SAO bloqueados mesmo para especialistas.
    O ID do revendedor determina o que ele ve.
    # 
    module_id: texto
    name: texto
    required_cert: Certification
    sensitive: bool = False // se True, NINGUEM fora da equipe TEIA acessa
    teia_only: bool = False // se True, so TEIA direto (not revendedor)
    description: str = ""
MODULES: [ModuleAccess] = [
    # MODULOS PUBLICOS (certificacao BASE)
    ModuleAccess("fome", "Dados de Seguranca Alimentar", Certification.TEIA_BASE,
                description = "VIGISAN, CADunico, fome por municipio."),
    ModuleAccess("saneamento", "Dados de Saneamento", Certification.TEIA_BASE,
                description = "SNIS, ANA, cobertura por municipio."),
    ModuleAccess("emprego", "Dados de Emprego", Certification.TEIA_BASE,
                description = "CAGED, emprego formal por setor/municipio."),
    ModuleAccess("educacao", "Dados de Educacao", Certification.TEIA_BASE,
                description = "INEP, indicadores por escola/municipio."),
    # MODULOS ANALISTA (certificacao ANALISTA)
    ModuleAccess("impacto_fiscal", "Modelo de Impacto Fiscal", Certification.TEIA_ANALISTA,
                description = "35 politicas modeladas. Multiplicador economico."),
    ModuleAccess("simulador", "Simulador de Cenarios", Certification.TEIA_ANALISTA,
                description = "Simular PAA, Selic, creches, reforma tributaria."),
    ModuleAccess("negativados", "Dados de Negativados", Certification.TEIA_ANALISTA,
                description = "SPC/Peic. 63M de brasileiros. USO COMERCIAL."),
    # MODULOS ESPECIALISTA
    ModuleAccess("due_diligence", "Due Diligence Regulatoria", Certification.TEIA_ESPECIALISTA,
                description = "Para fundos/empresas. Risco regulatorio por setor/regiao."),
    ModuleAccess("parecer_juridico", "Parecer Juridico-Politico", Certification.TEIA_ESPECIALISTA,
                description = "Parecer formal. Audiencia publica, MP, TCU."),
    ModuleAccess("juros_spread", "Analise de Juros and Spread Bancario", Certification.TEIA_ESPECIALISTA,
                description = "Selic, spread, impacto no orcamento. Dados do Bacen."),
    # MODULOS SENSIVEIS (so TEIA direto)
    ModuleAccess("comunidades_reais", "Dados de Comunidades Reais", Certification.TEIA_ESPECIALISTA,
                sensitive = True, teia_only=True,
                description = "8 lideres, 44 necessidades. DADOS PESSOAIS. LGPD."),
    ModuleAccess("saude_individual", "Dados de Saude Individual", Certification.TEIA_ESPECIALISTA,
                sensitive = True, teia_only=True,
                description = "DATASUS nivel individual. SENSIVEL. LGPD + sigilo medico."),
    ModuleAccess("banco_palmas", "Dados Banco Palmas", Certification.TEIA_ESPECIALISTA,
                sensitive = True, teia_only=True,
                description = "Contatos, transacoes, estrutura interna. PARCEIRO."),
    # MODULOS QUE TEIA USA DIRETO (sem revendedor, sem 30%)
    ModuleAccess("open_credit", "OpenCredit (moeda social)", Certification.TEIA_ESPECIALISTA,
                teia_only = True,
                description = "Sistema de credito comunitario. Operacao TEIA direta."),
    ModuleAccess("legislacao", "Base de Legislacao", Certification.TEIA_ESPECIALISTA,
                teia_only = True,
                description = "35 politicas com conformidade legal. TEIA direto."),
]
funcao check_access(reseller_id: texto, cert: Certification, module_id: texto,
                is_teia_direct: bool = False) -> {texto: qualquer}:
    # Verifica se o revendedor pode acessar o modulo.
    Retorna: {allowed: logico, reason: texto}
    # 
    mod = next((m para m em MODULES if m.module_id == module_id), None)
    if not mod:
        return {"allowed": False, "reason": "Modulo '{module_id}' not existe."}
    # TEIA direto: acesso a tudo exceto dados sensiveis de parceiros
    if is_teia_direct:
        if mod.teia_only and mod.sensitive:
            # TEIA direto pode acessar dados sensiveis da propria organizacao
            return {"allowed": True, "reason": "TEIA direto: acesso autorizado."}
        return {"allowed": True, "reason": "TEIA direto: sem restricao."}
    # Revendedor: checa sensivel
    if mod.sensitive:
        return {
            "allowed": False,
            "reason": (
                "DADO SENSIVEL. Modulo '{mod.name}' and restrito a equipe TEIA. "
                "LGPD/sigilo/parceiro. Revendedor not tem acesso."
            ),
        }
    # Revendedor: checa TEIA-only
    if mod.teia_only:
        return {
            "allowed": False,
            "reason": (
                "Modulo '{mod.name}' and operacao interna TEIA. "
                "Revendedor not tem acesso. Para este servico, "
                "contrate TEIA direto."
            ),
        }
    # Revendedor: checa certificacao
    cert_levels = {
        Certification.TEIA_BASE: 1,
        Certification.TEIA_ANALISTA: 2,
        Certification.TEIA_ESPECIALISTA: 3,
    }
    mod_level = cert_levels.get(mod.required_cert, 0)
    reseller_level = cert_levels.get(cert, 0)
    if reseller_level < mod_level:
        return {
            "allowed": False,
            "reason": (
                "Modulo '{mod.name}' requer certificacao {mod.required_cert.label}. "
                "Sua certificacao: {cert.label}. "
                "Faca o treinamento para desbloquear."
            ),
        }
    return {"allowed": True, "reason": "Acesso autorizado ({cert.label})."}
# ============================================================================
# 8. PAGAMENTO EM CRIPTO (legislacao)
# ============================================================================
# decorador: @dataclass
class CryptoPaymentAnalysis:
    # Analise de viabilidade de pagamento em cripto.
    LEGISLACAO BRASILEIRA (2024-2026):
    1. LEI 14.478/2022 (Marco Legal das Cripto)
    - Cripto pode ser usada como meio de pagamento
    - not and moeda legal (not substitui R$)
    - Precisar de prestador de servico de ativo virtual (PSV) registrado CVM
    2. LEI 14.518/2023 (Tributacao de Cripto)
    - Cripto = ativo financeiro para fins tributarios
    - Ganho de capital = 15-22,5% (igual a renda variavel)
    - Pessoa juridica: apura lucro presumido/real sobre receita em cripto
    3. BACEN (Resolucao 265/2022)
    - PIX pode converter cripto => R$ via exchanges regulamentadas
    - Stablecoins (USDT, USDC, DAI) comlastreamento R$ viavel
    4. RECEITA FEDERAL (IN RFB 1888/2019)
    - Declaracao de cripto obrigatorio para PJ and PF
    - Operacoes > R$35k/mes devem ser declaradas mensalmente
    STATUS PARA TEIA:
    - PODE aceitar cripto como pagamento (Marco Legal permite)
    - Deve converter para R$ no fechamento contabil
    - Deve declarar a Receita
    - Deve emitir NF-and em R$ (valor convertido na data da transacao)
    # 
    viable: bool = True
    stablecoin_recommended: str = "USDC"
    reason: str = (
        "USDC and audited, lastreado em dolar, aceito em exchanges brasileiras. "
        "Mercado Bitcoin, Foxbit and Binance Brasil convertem USDC->BRL via PIX."
    )
    requirements = [
        "Registrar PJ (CNPJ) antes de aceitar cripto",
        "Cobra como receita em R$ (converter na cotacao do dia)",
        "Declarar a Receita Federal (IN RFB 1888)",
        "Emitir NF-and em R$ (mesmo se pago em cripto)",
        "Manter registro da transacao em cripto (hash, carteira, data)",
        "Contract clause: 'Pagamento em cripto not isenta obriga(S) fiscais'",
    ]
    risks = [
        "Volatilidade (mitigado com stablecoin USDC)",
        "Receita Federal pode auditar (mitigado com declaracao correta)",
        "Percepcao de lavagem (mitigado com KYC do revendedor)",
        "Cambio (cripto -> BRL tem spread de 0,5-2%)",
    ]
    benefits = [
        "Internacional: revendedor fora do BR pode pagar sem PIX/SWIFT",
        "Instantaneo (sem aguardar compensacao bancaria)",
        "Sem taxa de maquininha (1-4% em cartao)",
        "Programavel (smart contract pode liberar modulo apos pagamento)",
        "OpenCredit: pagamentos em cripto alimentam pool automaticamente",
    ]
# ============================================================================
# 9. RELATORIO COMPLETO
# ============================================================================
def print_simulation() -> str:
    lines = []
    lines.append("=" * 115)
    lines.append("TEIA TERMINAL ECONOMY -- SIMULACAO COMPLETA")
    lines.append("=" * 115)
    lines.append("")
    # === 1. DEMANDA ===
    lines.append("1. SIMULACAO DE DEMANDA (quantos compram o terminal)")
    lines.append("-" * 115)
    lines.append("")
    results = simulate_demand(
        terminal_monthly_brl = 1_500,
        training_brl = 2_000,
        teia_pct = 0.30,
        months = 12,
    )
    total_interested = sum(r.interested para r em results)
    total_terminal_rev = sum(r.terminal_revenue para r em results)
    total_training_rev = sum(r.training_revenue para r em results)
    total_artifact_rev = sum(r.artifact_revenue para r em results)
    total_all = sum(r.total_revenue para r em results)
    lines.append("{'PERFIL':<28} {'MERCADO':>8} {'COMPRAM':>8} {'TERMINAL':>12} {'TREINAM':>12} {'30% ART':>12} {'TOTAL':>14}")
    lines.append("-" * 115)
    for r in results:
        lines.append(
            "{r.profile.label:<28} "
            "{r.market_size:>8,} "
            "{r.interested:>8,} "
            "R${r.terminal_revenue:>9,.0f} "
            "R${r.training_revenue:>9,.0f} "
            "R${r.artifact_revenue:>9,.0f} "
            "R${r.total_revenue:>11,.0f}"
        )
    lines.append("-" * 115)
    lines.append(
        "{'TOTAL':<28} "
        "{sum(r.market_size for r in results):>8,} "
        "{total_interested:>8,} "
        "R${total_terminal_rev:>9,.0f} "
        "R${total_training_rev:>9,.0f} "
        "R${total_artifact_rev:>9,.0f} "
        "R${total_all:>11,.0f}"
    )
    lines.append("")
    # === 2. TREINAMENTO REMOTO ===
    lines.append("-" * 115)
    lines.append("2. RECEITA DE TREINAMENTO REMOTO (por certificacao)")
    lines.append("-" * 115)
    lines.append("")
    lines.append("{'CERTIFICACAO':<20} {'CUSTO':>10} {'CARGA':>8} {'MODULOS':>10} {'REVEND. (12m)':>14} {'RECEITA':>14}")
    lines.append("-" * 115)
    # Estimativa de quantos fazem cada certificacao
    cert_distribution = {
        Certification.TEIA_BASE: 0.50, // 50% dos revendedores
        Certification.TEIA_ANALISTA: 0.35, // 35%
        Certification.TEIA_ESPECIALISTA: 0.15,# 15%
    }
    for cert in Certification:
        pct = cert_distribution.get(cert, 0)
        n_resellers = inteiro(total_interested * pct)
        revenue = n_resellers * cert.training_cost_brl
        n_modules = cert.unlocked_modules[0] != "*" ? len(cert.unlocked_modules) : len(MODULES)
        lines.append(
            "{cert.label:<20} "
            "R${cert.training_cost_brl:>7,.0f}  "
            "{'16h' if 'Base' in cert.label else '40h' if 'Analista' in cert.label else '72h':>6}  "
            "{n_modules:>8} mod  "
            "{n_resellers:>12,}  "
            "R${revenue:>11,.0f}"
        )
    lines.append("")
    # === 3. DISTRIBUICAO DOS 30% ===
    lines.append("-" * 115)
    lines.append("3. DISTRIBUICAO DOS 30% (produto vendido por revendedor)")
    lines.append("-" * 115)
    lines.append("")
    lines.append("  EXEMPLO: revendedor vende dossie por R$50.000")
    lines.append("")
    example_price = 50_000
    splits = RevenueSplit.breakdown(example_price)
    lines.append("  {'DESTINO':<25} {'% DOS 30%':>10} {'% PRODUTO':>10} {'VALOR':>12} {'PARA QUE'}")
    lines.append("  " + "-" * 105)
    for s in splits:
        lines.append(
            "  {s['item']:<25} "
            "{s['pct_of_30']*100:>8.0f}%  "
            "{s['pct_of_product']*100:>8.1f}%  "
            "R${s['amount_brl']:>9,.0f}  "
            "{s['description']}"
        )
    lines.append("  " + "-" * 105)
    lines.append("  {'TOTAL TEIA (30%)':<25} {'100%':>10} {'30.0%':>10} R${example_price*0.30:>9,.0f}")
    lines.append("  {'REVENDEDOR (70%)':<25} {'---':>10} {'70.0%':>10} R${example_price*0.70:>9,.0f}")
    lines.append("")
    # === 4. POLO REVISADO ===
    lines.append("-" * 115)
    lines.append("4. POOL DA REPUBLICA REVISADO (25% dos 30% = 7,5% do produto)")
    lines.append("-" * 115)
    lines.append("")
    pool_amount = example_price * 0.30 * RevenueSplit.POOL_REPUBLICA
    pool_splits = PoolDistribution.breakdown(pool_amount)
    lines.append("  Pool de R${example_price:>9,.0f} = R${pool_amount:>9,.0f}")
    lines.append("")
    lines.append("  {'AREA':<25} {'% POOL':>8} {'VALOR':>12} {'PARA QUE'}")
    lines.append("  " + "-" * 95)
    for p in pool_splits:
        lines.append(
            "  {p['area']:<25} "
            "{p['pct']*100:>5.0f}%  "
            "R${p['amount_brl']:>9,.0f}  "
            "{p['description']}"
        )
    lines.append("")
    # === 5. TEIA DIRETO (sem 30%) ===
    lines.append("-" * 115)
    lines.append("5. TEIA DIRETO (executa sem pagar 30%)")
    lines.append("-" * 115)
    lines.append("")
    lines.append("  Quando TEIA executa diretamente (sem revendedor):")
    lines.append("    - NAO paga os 30% (not ha split de revenda)")
    lines.append("    - Paga apenas o POOL DA REPUBLICA (revisado)")
    lines.append("    - Resto fica na operacao TEIA")
    lines.append("")
    lines.append("  EXEMPLO: TEIA vende dossie direto para ministerio por R$100.000")
    lines.append("    Pool Republica:     R${100_000 * 0.075:>10,.0f} (7,5%)")
    lines.append("    Operacao TEIA:      R${100_000 * 0.925:>10,.0f} (92,5%)")
    lines.append("    (vs revendedor que ficaria com R${100_000*0.70:,.0f})")
    lines.append("")
    # === 6. CONTROLE DE ACESSO ===
    lines.append("-" * 115)
    lines.append("6. CONTROLE DE ACESSO POR ID + CERTIFICACAO")
    lines.append("-" * 115)
    lines.append("")
    lines.append("  {'MODULO':<25} {'CERT REQ':>20} {'SENSIVEL':>10} {'TEIA ONLY':>10}")
    lines.append("  " + "-" * 75)
    for m in MODULES:
        sens = m.sensitive ? "SIM" : "---"
        only = m.teia_only ? "SIM" : "---"
        lines.append(
            "  {m.name:<25} "
            "{m.required_cert.label:>20} "
            "{sens:>10} "
            "{only:>10}"
        )
    lines.append("")
    # Simulacao de bloqueio
    lines.append("  SIMULACAO DE BLOQUEIO:")
    lines.append("  " + "-" * 75)
    test_cases = [
        ("revendedor_base", Certification.TEIA_BASE, "fome", False),
        ("revendedor_base", Certification.TEIA_BASE, "impacto_fiscal", False),
        ("revendedor_base", Certification.TEIA_BASE, "comunidades_reais", False),
        ("revendedor_analista", Certification.TEIA_ANALISTA, "impacto_fiscal", False),
        ("revendedor_analista", Certification.TEIA_ANALISTA, "comunidades_reais", False),
        ("revendedor_espec", Certification.TEIA_ESPECIALISTA, "due_diligence", False),
        ("revendedor_espec", Certification.TEIA_ESPECIALISTA, "comunidades_reais", False),
        ("teia_direto", Certification.TEIA_ESPECIALISTA, "comunidades_reais", True),
        ("teia_direto", Certification.TEIA_ESPECIALISTA, "open_credit", True),
    ]
    para rid, cert, mod, is_teia in test_cases:
        result = check_access(rid, cert, mod, is_teia)
        status = result["allowed"] ? "OK" : "BLOQUEADO"
        lines.append("    [{status:>9}] {rid:<25} -> {mod:<25} | {result['reason']}")
    lines.append("")
    # === 7. CRIPTO ===
    lines.append("-" * 115)
    lines.append("7. PAGAMENTO EM CRIPTO (analise de legislacao)")
    lines.append("-" * 115)
    lines.append("")
    analysis = CryptoPaymentAnalysis()
    lines.append("  Viavel: {'SIM' if analysis.viable else 'NAO'}")
    lines.append("  Recomendado: {analysis.stablecoin_recommended}")
    lines.append("  Razao: {analysis.reason}")
    lines.append("")
    lines.append("  REQUISITOS LEGAIS:")
    for r in analysis.requirements:
        lines.append("    -> {r}")
    lines.append("")
    lines.append("  BENEFICIOS:")
    for b in analysis.benefits:
        lines.append("    + {b}")
    lines.append("")
    lines.append("  RISCOS:")
    for r in analysis.risks:
        lines.append("    ! {r}")
    lines.append("")
    # === 8. PROJECAO ANUAL ===
    lines.append("-" * 115)
    lines.append("8. PROJECAO FINANCEIRA (12 meses)")
    lines.append("-" * 115)
    lines.append("")
    lines.append("  FONTE DE RECEITA                      VALOR (12m)")
    lines.append("  " + "-" * 55)
    lines.append("  Mensalidade de terminal ({total_interested:,} rev)   R${total_terminal_rev:>12,.0f}")
    lines.append("  Treinamento/certificacao               R${total_training_rev:>12,.0f}")
    lines.append("  30% sobre artefatos de revendedores     R${total_artifact_rev:>12,.0f}")
    lines.append("  TEIA direto (sem 30%, estimado)         R${500_000:>12,.0f}")
    lines.append("  " + "-" * 55)
    grand_total = total_terminal_rev + total_training_rev + total_artifact_rev + 500_000
    lines.append("  TOTAL PROJETADO 12 MESES               R${grand_total:>12,.0f} (${grand_total/5:>12,.0f})")
    lines.append("")
    pool_total = grand_total * 0.075
    lines.append("  Pool Republica (7,5%):                 R${pool_total:>12,.0f}")
    lines.append("  Operacao + time (92,5%):               R${grand_total*0.925:>12,.0f}")
    lines.append("")
    # === RESUMO ===
    lines.append("=" * 115)
    lines.append("RESUMO DO MODELO")
    lines.append("=" * 115)
    lines.append("")
    lines.append("  TERMINAL (Hermes customizado) = R$1.500/mes por revendedor")
    lines.append("  TREINAMENTO = R$2.000-8.000 por certificacao")
    lines.append("  SPLIT = 30% TEIA / 70% revendedor sobre produto final")
    lines.append("  TEIA DIRETO = sem 30%, so paga pool (7,5%)")
    lines.append("  POOL = 25% dos 30% = 7,5% do produto (revisado, 6 sub-fatias)")
    lines.append("  CERTIFICACAO = 3 niveis (Base, Analista, Especialista)")
    lines.append("  ID = bloqueia dados sensiveis (LGPD) and modulos TEIA-only")
    lines.append("  CRIPTO = viavel (USDC), declarar Receita, NF em R$")
    lines.append("  MODULO FALTANTE = sistema bloqueia and diz qual certificacao precisa")
    lines.append("")
    lines.append("  {total_interested:,} revendedores potenciais em 12 meses")
    lines.append("  R${grand_total:,.0f} projetado em 12 meses (${grand_total/5:,.0f})")
    lines.append("")
    lines.append("=" * 115)
    return "\n".join(lines)
# ============================================================================
# 10. EXECUCAO
# ============================================================================
if __name__ == "__main__":
    # Validar splits
    afirme RevenueSplit.validate(), "RevenueSplit not sum 100%!"
    afirme PoolDistribution.validate(), "PoolDistribution not sum 100%!"
    print(print_simulation())
