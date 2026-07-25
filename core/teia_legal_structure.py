#!/usr/bin/env python3
"""
TEIA -- Estrutura Juridica: Cooperativa vs EPP vs Hibrido -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
TEIA -- Estrutura Juridica: Cooperativa vs EPP vs Hibrido
============================================================
A DECISAO:
TEIA precisa de uma estrutura juridica para:
1. Contratar revendedores
2. Receber mensalidade do SaaS
3. Receber 30% sobre artefatos
4. Pagar royalty chain
5. Aceitar cripto
6. Emitir NF-and
7. Contratar funcionarios/cooperados
3 OPCOES:
A. Cooperativa (Lei 5.764/1971)
B. EPP LTDA (Simples Nacional)
C. HIBRIDO: EPP para TEIA + Associacao para Republica
Author: TEIA / OpenRepublic Team
# 
# importa annotations de __future__
# importa dataclass, field de dataclasses
# importa List, Dict de typing
# ============================================================================
# 1. COMPARACAO DIRETA
# ============================================================================
# decorador: @dataclass
class StructureComparison:
    # Comparacao ponto a ponto.
    criterio: texto
    cooperativa: texto
    epp_ltda: texto
    hibrido: texto
COMPARACAO: [StructureComparison] = [
    StructureComparison(
        "FILosofia OpenRepublic",
        "PERFEITO. Sem dono. 1 pessoa = 1 voto. Assembleia decide. Anti-elitismo nativo.",
        "CONTRADIZ. Tem dono (socio majoritario). Poder concentrado. Contra P1.",
        "MELHOR DOS DOIS. EPP opera comercial. Associacao opera Republica. Cada um no seu.",
    ),
    StructureComparison(
        "Velocidade de abertura",
        "30-60 dias. Estatuto complexo. Junta comercial + OCERGS. Assembleia de fundacao.",
        "1-3 dias. Portal do Empreendedor. Contrato social simples.",
        "1-3 dias EPP + 30 dias Associacao (em paralelo).",
    ),
    StructureComparison(
        "Custo de abertura",
        "R$5-15k (advogado cooperativista + taxas + OCERGS)",
        "R$0-2k (contador + taxas)",
        "R$0-2k EPP + R$1-3k Associacao",
    ),
    StructureComparison(
        "Tributacao",
        "ISENTO de INSS patronal, PIS, COFINS sobre atos cooperativos. "
        "Sobras rateadas not sao lucro tributavel.",
        "Simples Nacional: 6-15% sobre faturamento (anexo III/V). "
        "Tudo tributado.",
        "EPP: Simples (6-15%). Associacao: isenta IR (imunidade). "
        "Pool vai para Associacao (not tributado).",
    ),
    StructureComparison(
        "Vender para governo",
        "PODE. Lei 11.488/2007 permite cooperativa participar de licitacao. "
        "Mas alguns editais exigem LTDA/SA.",
        "PODE. Sem restricao. Maioria dos editais aceita.",
        "PODE. EPP licita. Sem restricao.",
    ),
    StructureComparison(
        "Vender SaaS para revendedor",
        "PODE. Mas juridicamente complicado: cooperado and 'dono', not 'cliente'. "
        "Relacao comercial fica ambigua.",
        "PODE. Simples: empresa vende servico para cliente. "
        "Contrato SaaS padrao.",
        "PODE. EPP vende SaaS. Claro and direto.",
    ),
    StructureComparison(
        "Receber 30% sobre artefatos",
        "PODE. Mas and 'sobras' or 'receita'? Juridicamente confuso. "
        "Receita Federal pode questionar.",
        "PODE. E receita normal. Tributada. Clara.",
        "PODE. EPP recebe como receita normal.",
    ),
    StructureComparison(
        "Aceitar cripto",
        "PODE mas juridicamente complexo. Cooperativa not and 'empresa' tradicional. "
        "Exchanges pedem CNPJ + contrato social.",
        "PODE. CNPJ + contrato social LTDA. "
        "Exchanges aceitam sem problema.",
        "PODE. EPP aceita cripto como PJ normal.",
    ),
    StructureComparison(
        "Emitir NF-and",
        "PODE. Mas tipo de documento and diferente (nota de servico cooperado). "
        "Alguns municipios not tem modelo para cooperativa.",
        "PODE. NF-and padrao. Sem complicacao.",
        "PODE. NF-and padrao pela EPP.",
    ),
    StructureComparison(
        "Contratar pessoas",
        "Cooperados not sao CLT (sao 'donos'). "
        "Nao ha vinculo empregaticio. "
        "Mas: se julgar que ha subordinacao, Justiça pode configurar CLT.",
        "CLT normal. Sem risco. "
        "Pode contratar quantos precisar.",
        "EPP contrata CLT. "
        "Associacao tem voluntarios/associados.",
    ),
    StructureComparison(
        "Captar investimento",
        "MUITO DIFICIL. Cooperativa not emite quotas para investidor. "
        "Sem equity. Ninguem investe no que not and dono.",
        "PODE. LTDA pode ter socio investidor. "
        "Percentual negociavel.",
        "EPP pode ter investidor. "
        "Associacao not (mas not precisa).",
    ),
    StructureComparison(
        "Governanca",
        "Assembleia decide TUDO. Democratico mas LENTO. "
        "Decisao comercial not pode esperar assembleia.",
        "Socio decide. Rapido. "
        "Mas: concentracao de poder.",
        "EPP: socio decide (rapido). "
        "Associacao: assembleia decide Republica (democratico).",
    ),
    StructureComparison(
        "Dividir lucro/prejuizo",
        "Sobras rateadas por proporcionalidade. "
        "Complexo de calcular com royalty chain.",
        "Lucro = do socio. Decide como distribuir. "
        "Simples.",
        "EPP: lucro do socio. "
        "Pool vai para Associacao (rateado democraticamente).",
    ),
    StructureComparison(
        "Risco juridico",
        "MAIOR. Receita Federal costuma auditor cooperativas. "
        "Se atos not-cooperativos > cooperativos, perde isencao.",
        "MENOR. Regime claro. Burocracia padrao.",
        "MEDIO. EPP claro. Associacao precisa ter cuidado com imunidade.",
    ),
    StructureComparison(
        "Imagem publica",
        "COOPERATIVA soa bem para governo/ONG/comunidade. "
        "Associado a Banco Palmas, economia solidaria.",
        "EMPRESA soa neutro. Nao ajuda nem atrapalha.",
        "EPP comercial + Associacao social. "
        "Melhor narrativa: 'empresa que financia projeto social.'",
    ),
    StructureComparison(
        "Alinhacao com modelo revendedor",
        "PROBLEMATICO. Revendedor not and cooperado. "
        "E cliente/parceiro comercial. "
        "Cooperativa not foi desenhada para ter 'clientes'.",
        "PERFEITO. Revendedor = cliente do SaaS. "
        "Relacao comercial clara.",
        "PERFEITO. EPP gerencia revendedores. "
        "Associacao gerencia Republica.",
    ),
    StructureComparison(
        "Pool da Republica (7,5%)",
        "E natural. Sobras viram pool. "
        "Mas juridicamente complexo separar 'pool' de 'sobras'.",
        "PRECISA de estrutura separada. "
        "EPP not pode doar 7,5% sem tributacao. "
        "Faria acordo comercial.",
        "NATURAL. EPP repassa 7,5% para Associacao "
        "(despesa operacional dedutivel). Associacao and isenta.",
    ),
    StructureComparison(
        "Escalabilidade internacional",
        "DIFICIL. Cooperativa brasileira not opera facil no exterior. "
        "Revendedor internacional = juridicao complexa.",
        "PODE. LTDA pode ter clientes internacionais. "
        "Contrato SaaS global.",
        "PODE. EPP opera global. Associacao not precisa.",
    ),
]
# ============================================================================
# 2. ARQUITETURA SAAS EM VPN (o produto real)
# ============================================================================
SAAS_ARCHITECTURE = """
ARQUITETURA DO PRODUTO (SaaS em VPN)
=====================================
O PRODUTO:
Nao and o Hermes. O Hermes and interno (desenvolvimento).
O produto and um SaaS web que roda em rede VPN fechada.
[Revendedor] --VPN--> [Servidor TEIA] --[dados]--> [Artefato]
POR QUE VPN (limitar spectro de ataque):
1. SaaS PUBLICO (sem VPN):
    - Qualquer IP no mundo pode tentar acessar
    - DDoS, brute force, SQL injection, scraping
    - Superficie de ataque = INTERNET INTEIRA
    - Precisa de WAF, rate limiting, CAPTCHA, etc
2. SaaS EM VPN (fechado):
    - So quem tem certificado VPN acessa
    - Zero ataque externo
    - Superficie de ataque = SO revendedores autenticados
    - DDoS impossivel (not ha IP publico exposto)
    - Scraping impossivel (sem acesso a rede)
3. MODELO:
    - WireGuard (VPN moderna, leve, rapida)
    - Cada revendedor recebe: chave VPN + credencial SaaS
    - Conecta na VPN -> acessa o SaaS
    - Sem VPN = sem acesso
    - Revendedor desligado (not pagou) = chave VPN revogada
4. BENEFICIOS:
    - Latencia baixa (WireGuard and UDP nativo)
    - Criptografia end-to-end (dados not passam em claro)
    - Auditavel (log de conexao por revendedor)
    - Barreira de entrada para atacante
    - Compativel com cripto (pagamento libera chave VPN)
5. INFRA:
    - 1 servidor (VPS Hetzner/DigitalOcean): R$200-500/mes
    - WireGuard: gratuito (open source)
    - SaaS: Streamlit/Dash/Flask (Python) -> depois Rust
    - Dados: PostgreSQL + Parquet files
    - Backup: diario, automatico, encriptado
ESTRUTURA TECNICA:
Internet publica
    |
    | (not exposto)
    |
[WireGuard VPN Gateway]
    |
    |--- [SaaS TEIA - Streamlit/Flask]
    | |-- Modulos (filtrados por ID/certificacao)
    | |-- Gerador de dossies
    | |-- Simulador
    | |-- API interna
    |
    |--- [PostgreSQL - dados]
    | |-- VIGISAN, SNIS, CAGED, INEP, etc
    | |-- Modelos de impacto fiscal
    | |-- Log de artefatos gerados (royalty chain)
    |
    |--- [Auth - por ID]
    | |-- Revendedor ID -> cert nivel -> modulos
    | |-- Log de acessos
    | |-- Bloqueio de dados sensiveis
    |
    |--- [Billing]
            |-- Mensalidade terminal
            |-- 30% sobre artefatos
            |-- Cripto (USDC) or PIX
            |-- Chave VPN revogada se inadimplente
# 
# ============================================================================
# 3. RECOMENDACAO
# ============================================================================
RECOMMENDATION = """
RECOMENDACAO: HIBRIDO (EPP LTDA + Associacao sem fins lucrativos)
=================================================================
ESTRUTURA:
1. EPP LTDA "TEIA Inteligencia Estrategica Ltda."
    - CNPJ em 1-3 dias
    - Simples Nacional
    - Socio: Cleiton (inicialmente)
    - Funcao: OPERACAO COMERCIAL
    - Vende SaaS (terminal)
    - Contrata revendedores
    - Recebe 30%
    - Paga royalty chain
    - Emite NF-and
    - Aceita cripto
    - Licita/contratos
2. Associacao "Instituto OpenRepublic"
    - CNPJ em 30 dias (sem fins lucrativos)
    - Imunidade tributaria (IR, IPTU, etc)
    - Assembleia de associados
    - Funcao: IDEAL / IMPACTO
    - Recebe pool (7,5% repassado da EPP)
    - Financia pilotos comunitarios (OpenCredit)
    - Mantem open-source CC0
    - Gestao democratica (P1-P4)
    - Comunidades reais
3. FLUXO FINANCEIRO:
    Revendedor paga R$50.000 (artefato)
    |
    v
    EPP TEIA recebe R$50.000
    |-- 70% (R$35.000) -> repassa para revendedor (comissao)
    |-- 9% (R$4.500) -> paga royalty chain (criadores de dados)
    |-- 4,5% (R$2.250) -> manutencao terminal
    |-- 3% (R$1.500) -> infraestrutura
    |-- 2,4% (R$1.200) -> certificacao/qualidade
    |-- 2,1% (R$1.050) -> fundo de garantia
    |-- 1,5% (R$750) -> equipe fundadora (Cleiton)
    |-- 7,5% (R$3.750) -> REPASSA para Associacao (dedutivel)
    |
    v
    Associacao OpenRepublic recebe R$3.750
    |-- 20% operacoes
    |-- 25% desenvolvimento
    |-- 15% comunidade
    |-- 20% piloto comunitario
    |-- 10% emergencia
    |-- 10% reinvestimento
POR QUE HIBRIDO and MELHOR:
1. EPP and RAPIDA para operar comercialmente
    - Decisao em minutos, not assembleia
    - Contrato SaaS padrao
    - NF-and, cripto, licitacao: tudo funciona
2. Associacao protege o IDEAL
    - Pool not and "lucro da empresa"
    - and "doacao para projeto social" (dedutivel)
    - Imunidade tributaria
    - Governance democratica separada
3. DualMode natural
    - EPP = "O Executavel opera"
    - Associacao = "O Ideal guia"
    - Cada um otimizado para sua funcao
4. Defesa juridica
    - Se EPP para processada, Associacao not and afetada
    - Se Associacao para questionada, EPP continua operando
    - Separacao de risco
5. Captar investimento (futuro)
    - Investidor entra na EPP (equity)
    - Associacao permanece independente
    - Investor not controla o Ideal
6. Narrativa para cliente
    - "TEIA and uma empresa de inteligencia (EPP)"
    - "Que financia o Instituto OpenRepublic (Associacao)"
    - "Cada compra apoia comunidades reais"
    - ESG nativo (not greenwashing)
# 
# ============================================================================
# 4. CRONOGRAMA DE ABRIR
# ============================================================================
TIMELINE = """
CRONOGRAMA (o que fazer nos proximos dias):
D+1: Abrir EPP LTDA
- Portal do Empreendedor ( RedeSim )
- Contrato social: EPP unipessoal or LTDA com 2 socios
- CNAE: 6204-0/00 (consultoria em TI) + 8599-6/99 (educacao)
- Regime: Simples Nacional (Anexo III para servico)
- Custo: R$0 (Portal) a R$1.500 (contador)
- Tempo: 1-3 dias uteis
D+3: Abrir conta PJ + MEI not (EPP)
- Banco Inter, Nubank PJ, or Sicredi (cooperativa de credito)
- PIX PJ
- Custo: R$0
D+7: Regularidade fiscal
- CND Receita Federal (emitir online)
- CND INSS/FGTS
- Certidao Negativa Estadual and Municipal
- Manter renovada (60-180 dias dependendo)
D+14: SICAF (para licitacao futuro)
- Cadastrar em www.compras.gov.br
- Habilitacao juridica + fiscal + trabalhista
- Tempo: 1-3 semanas para aprovacao
D+14: Contrato social da Associacao
- Estatuto: Instituto OpenRepublic
- Natureza: sem fins lucrativos
- Finalidade: desenvolvimento social, tecnologia aberta, comunidades
- Minimo 5 associados fundadores (Cleiton + 4)
- Registro em cartorio + Junta Commercial
- Tempo: 30 dias
D+30: Infraestrutura SaaS
- VPS (Hetzner CX21: R$100/mes, 4GB RAM)
- WireGuard VPN
- Streamlit/Flask SaaS
- PostgreSQL
- Deploy + teste
D+45: Primeiro revendedor (piloto)
- Certificacao TEIA Base (16h remoto)
- Feedback de usabilidade
- Ajustar SaaS
- Cobrar R$1.500/mes + treinamento R$2.000
# 
# ============================================================================
# 5. RELATORIO
# ============================================================================
def print_report() -> str:
    lines = []
    lines.append("=" * 115)
    lines.append("TEIA -- ESTRUTURA JURIDICA: COOPERATIVA vs EPP vs HIBRIDO")
    lines.append("=" * 115)
    lines.append("")
    # Tabela comparativa
    lines.append("COMPARACAO PONTO A PONTO")
    lines.append("-" * 115)
    lines.append("")
    for c in COMPARACAO:
        lines.append("  {c.criterio.upper()}")
        lines.append("    Cooperativa:  {c.cooperativa}")
        lines.append("    EPP LTDA:     {c.epp_ltda}")
        lines.append("    Hibrido:      {c.hibrido}")
        lines.append("")
    # Arquitetura
    lines.append("-" * 115)
    lines.append(SAAS_ARCHITECTURE)
    lines.append("")
    # Recomendacao
    lines.append("-" * 115)
    lines.append(RECOMMENDATION)
    lines.append("")
    # Timeline
    lines.append("-" * 115)
    lines.append(TIMELINE)
    lines.append("")
    # Resumo
    lines.append("=" * 115)
    lines.append("VEREDICTO")
    lines.append("=" * 115)
    lines.append("")
    lines.append("  COOPERATIVA:")
    lines.append("    + Alinhada com OpenRepublic filosoficamente")
    lines.append("    - LENTA para operar comercialmente")
    lines.append("    - Revendedor not encaixa (not and 'cooperado')")
    lines.append("    - Receita Federal auditoria mais")
    lines.append("    - Sem investidor")
    lines.append("    VEREDICTO: BONITO MAS IMPRATICAVEL PARA FASE 1")
    lines.append("")
    lines.append("  EPP LTDA pura:")
    lines.append("    + Rapida, flexivel, comercialmente clara")
    lines.append("    - Contradiz anti-elitismo (tem dono)")
    lines.append("    - Pool fica tributado")
    lines.append("    VEREDICTO: FUNCIONA MAS FILOSOFICAMENTE INCOMPLETA")
    lines.append("")
    lines.append("  HIBRIDO (EPP + Associacao):")
    lines.append("    + Rapida comercialmente (EPP)")
    lines.append("    + Pool protegido and not-tributado (Associacao)")
    lines.append("    + DualMode natural")
    lines.append("    + Separacao de risco")
    lines.append("    + Narrativa ESG autentica")
    lines.append("    + Investidor futuro sem perder Republica")
    lines.append("    - Mais complexa (2 CNPJ)")
    lines.append("    - Mais burocracia (2 contabilidades)")
    lines.append("    VEREDICTO: MELHOR OPCAO")
    lines.append("")
    lines.append("=" * 115)
    return "\n".join(lines)
if __name__ == "__main__":
    print(print_report())
