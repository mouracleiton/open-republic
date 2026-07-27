# PLANO DE EXECUÇÃO — P29
# Democracia Participativa Digital

> Política: Sistema de democracia participativa em três camadas: (1) Representantes eleitos com mandato revogável (recall) — 4 anos com possibilidade de revogação. (2) Assembleia digital permanente aberta a TODOS os cidadãos: todo cidadão pode votar em qualquer proposta via OpenTerminal. (3) Conselho técnico permanente (especialistas sorteados por área) que analisa viabilidade antes da votação popular. O povo decide; os técnicos informam. Custo: R$ 2-3 bilhões em implementação digital (segurança blockchain, identificação biométrica). Economia estimada: R$ 50-100 bilhões/ano em corrupção reduzida. Prazo: 5-10 anos (fases 1-3). Base científica: Suíça — democracia direta há 800 anos (referendos nacionais). Taiwan — vTaiwan (2014-presente). Estonia — i-Voting desde 2005. Sistema: OpenDemocracy.

---

## 0. RESUMO EXECUTIVO

|| Item | Valor |
||------|-------|
|| Investimento total | R$ 2-3 bilhões em implementação + R$ 200-400 milhões/ano operação e manutenção |
|| Economia esperada | R$ 50-100 bilhões/ano em corrupção reduzida + maior legitimidade e eficiência de políticas |
|| Prazo total | 5-10 anos em 3 fases |
|| População-alvo | 150+ milhões de cidadãos aptos a votar (maiores de 16 anos com cadastro) |
|| Cobertura atual de participação digital | Muito baixa (portais de transparência, poucos mecanismos de voto direto) |
|| Meta | 80%+ dos cidadãos registrados e ativos na assembleia digital; recall funcional em todos os níveis |
|| Confiança da estimativa | BAIXA (modelagem própria baseada em casos internacionais; difícil quantificar corrupção exata) |

---

## 1. MARCO LEGAL NECESSÁRIO

### 1.1 Leis federais a aprovar

**Lei da Democracia Participativa Digital (nova — Lei da Assembleia Digital)**

- Institui a Assembleia Digital Permanente como instância de deliberação popular direta, com força de lei para propostas aprovadas por maioria simples (51%) após análise técnica
- Define o sistema de recall: qualquer representante eleito (deputado, senador, presidente, governadores, prefeitos) pode ser revogado por petição popular + referendo digital (limiares: 5% do eleitorado para petição, 50%+1 para revogação)
- Cria o Conselho Técnico Permanente: especialistas sorteados por área (saúde, educação, infraestrutura etc.) com mandatos de 2 anos, função consultiva e de análise de viabilidade (não veto)
- Estabelece identificação digital soberana (gov.br + biometria + OpenID-like) para votação, com auditoria pública e blockchain para integridade
- Regula o OpenTerminal como canal oficial de acesso (app, web, terminais físicos em cartórios, correios, UBS, escolas)
- Proíbe financiamento privado de campanhas para propostas na assembleia; tudo público e transparente

**Reforma da Constituição (PEC) e leis eleitorais**

- Emenda constitucional para incorporar a Assembleia Digital como poder de deliberação popular (complementar ao Congresso)
- Reforma da Lei das Eleições e Lei dos Partidos para integrar recall e vincular mandatos a plataformas aprovadas na assembleia
- Lei de Transparência e Integridade Digital (reforço da Lei 12.527/2011 e LGPD)

**Portarias e Decretos (execução)**

- Decreto que cria a Autoridade Nacional de Democracia Digital (ANDD) sob Casa Civil ou novo órgão
- Portaria que define protocolos de segurança, sorteio de conselheiros técnicos (aleatório com pesos por especialidade)
- Portaria que regula o cadastro biométrico universal e integração com TSE, Receita, etc.
- Normas para terminais físicos acessíveis (incluindo acessibilidade para deficientes, analfabetos funcionais, idosos)

### 1.2 Cronograma legislativo

|| Ação | Responsável | Prazo |
||------|-------------|-------|
|| Redação do PL da Assembleia Digital + PEC | Casa Civil + Ministério da Justiça + especialistas | Mês 1-4 |
|| Consulta pública ampla (incluindo plataformas existentes como vTaiwan, Participa.br) | ANDD (provisória) + Congresso | Mês 4-8 |
|| Audiências públicas (TSE, OAB, academia, movimentos sociais, partidos) | Comissões de Constituição e Justiça | Mês 8-14 |
|| Votação Câmara + Senado + Sanção + Referendo (se PEC) | Congresso + Presidência | Mês 14-24 |
|| Regulamentação via portarias e decreto | Executivo | Mês 18-30 |

---

## 2. ESTRUTURA INSTITUCIONAL

### 2.1 Governança

```
Cidadãos (via OpenTerminal / app / terminais físicos)
         │
    Assembleia Digital Permanente (votações 51%)
         │
    Conselho Técnico Permanente (sorteados por área — análise de viabilidade)
         │
    Autoridade Nacional de Democracia Digital (ANDD)
         │
    ┌────┴────┬──────────┬────────────┐
    │         │          │            │
Coord.      Coord.     Coord.       Coord.
de Plataforma  de Segurança  de Recall   de Educação
(nacional)  e Auditoria   e Eleições   Cívica Digital
            (nacional)    (nacional)   (nacional)
         │
    Integração com TSE, Congresso, Executivos
```

### 2.2 Coordenadores Regionais e Níveis

- 27 coordenações estaduais + DF + coordenações municipais em capitais e grandes cidades
- Cada estado tem "assembléias regionais" complementares para temas locais
- Integração obrigatória com Congresso Nacional: propostas aprovadas na digital vão automaticamente para tramitação prioritária ou viram lei se aplicável
- Reportes mensais públicos:
  - Número de cidadãos ativos / cadastrados
  - Taxa de participação por votação
  - Propostas aprovadas vs. implementadas
  - Recall iniciados / concluídos
  - Tempo médio de análise técnica
  - Incidentes de segurança / fraudes detectadas

---

## 3. FASES DE EXECUÇÃO

### FASE 1 — FUNDAÇÃO E PILOTO (Anos 1-3)

**Objetivo:** Aprovar marco legal, construir plataforma segura, piloto em 3 estados + nível federal limitado.

**3.1.1 Marco Legal e Autoridade**

- Aprovação da lei e PEC (se necessária)
- Criação da ANDD
- Sorteio e formação do primeiro Conselho Técnico (500 especialistas iniciais)
- Custo: R$ 100-200 milhões

**3.1.2 Plataforma Digital (MVP)**

- Desenvolvimento do OpenTerminal (app + web + WhatsApp/Telegram bots + terminais físicos)
- Infraestrutura: nuvem soberana (Serpro ou equivalente), blockchain para votação (auditoria pública, não controle)
- Identificação: integração gov.br + biometria facial/ digital + prova de vida
- Segurança: auditoria independente (ex: academia + TCU + hackers éticos), testes de penetração
- Piloto: 3 estados (um Norte, um Nordeste, um Sul) + votações federais em temas não vinculantes primeiro
- Custo: R$ 800 milhões - 1,2 bilhões (desenvolvimento + infra + segurança)

**3.1.3 Cadastro e Educação**

- Campanha nacional de cadastro biométrico (integrado com recadastramento eleitoral)
- Educação cívica digital obrigatória nas escolas + campanhas
- Materiais em múltiplos idiomas e formatos acessíveis
- Custo: R$ 300-500 milhões

**3.1.4 Recall Piloto**

- Implementar recall para prefeitos e vereadores em municípios piloto
- Meta: 5 recalls processados com sucesso
- Custo: incluso na plataforma

**MARCO FASE 1 (Ano 3):**

- [ ] Lei e estrutura institucional operantes
- [ ] Plataforma MVP segura auditada
- [ ] 20% da população cadastrada e testando
- [ ] 10+ votações nacionais com participação >10%
- [ ] Recall funcional em nível municipal

**TOTAL FASE 1: R$ 1,2-1,9 bilhões**

---

### FASE 2 — EXPANSÃO NACIONAL (Anos 4-6)

**Objetivo:** Cobertura nacional, vinculação de propostas à lei, recall em todos os níveis.

**3.2.1 Expansão da Plataforma**

- Rollout para todos os municípios (terminais físicos em 100% dos cartórios, correios selecionados, UBS)
- Integração plena com sistemas do Congresso (propostas aprovadas entram automaticamente na pauta)
- Votações vinculantes para temas orçamentários, leis de iniciativa popular etc.
- Custo: R$ 400-600 milhões

**3.2.2 Recall Nacional**

- Recall para deputados, senadores, governadores, presidente
- Petição digital + referendo com quóruns definidos
- Auditoria independente de cada processo
- Custo: R$ 100-200 milhões/ano (operação + campanhas)

**3.2.3 Conselho Técnico em Escala**

- Expandir para 2.000+ conselheiros sorteados
- Plataforma para submissão de análises técnicas
- Custo: R$ 150 milhões/ano (bolsas + operação)

**3.2.4 Educação e Adesão em Massa**

- Integração com OpenCivicEducation (P15)
- Meta: 60% da população cadastrada
- Custo: R$ 200 milhões/ano

**MARCO FASE 2 (Ano 6):**

- [ ] 60%+ cidadãos cadastrados
- [ ] 50+ leis ou diretrizes originadas da assembleia digital implementadas
- [ ] Recall disponível e usado em todos os níveis eletivos
- [ ] Participação média por votação >25%
- [ ] Zero incidentes graves de fraude em 2 anos

**TOTAL FASE 2: R$ 0,85-1,15 bi/ano (pico)**

---

### FASE 3 — CONSOLIDAÇÃO E MATURIDADE (Anos 7-10+)

**Objetivo:** Sistema maduro, alta participação, redução de corrupção mensurável, integração cultural.

**3.3.1 Otimização e IA de Apoio (não decisão)**

- IA para sumarização de propostas, detecção de duplicatas, sugestão de agrupamento de votações (decisão final humana)
- Integração com OpenDemocracy e outros sistemas OpenRepublic
- Redução de custos operacionais
- Custo: R$ 100-200 milhões/ano

**3.3.2 Expansão para Temas Locais e Setoriais**

- Assembléias regionais e setoriais (saúde, educação, ambiente) com poder deliberativo
- Integração com orçamento participativo digital
- Custo: incluso

**3.3.3 Avaliação Independente e Ajustes**

- Avaliação externa (universidades + OCDE ou equivalente + sociedade civil)
- Medir redução de corrupção (via CGU, TCU, estudos acadêmicos), legitimidade, qualidade de políticas
- Ajustes legislativos se necessário
- Custo: R$ 50 milhões (uma vez + anual)

**MARCO FASE 3 (Ano 10):**

- [ ] 80%+ população cadastrada e ativa periodicamente
- [ ] 200+ políticas impactantes originadas da assembleia
- [ ] Redução documentada de 30-50% em casos de corrupção em áreas cobertas
- [ ] Recall usado regularmente como ferramenta de accountability
- [ ] Sistema auto-sustentável com custos operacionais baixos

**CUSTO DE CRUZEIRO (steady-state): R$ 300-500 milhões/ano**

**ECONOMIA ESPERADA (steady-state): R$ 50-100 bilhões/ano (principalmente via redução de corrupção e melhor alocação de recursos)**

---

## 4. ORÇAMENTO DETALHADO

### 4.1 Por componente (médio anual Fase 2)

|| Componente | R$ milhões/ano | % do total |
||------------|----------------|------------|
|| Desenvolvimento e manutenção de plataforma | 400-600 | 40% |
|| Segurança, auditoria e blockchain | 150-250 | 15% |
|| Conselho Técnico (bolsas + operação) | 150-200 | 12% |
|| Terminais físicos e acessibilidade | 100-150 | 10% |
|| Educação cívica e cadastro | 150-200 | 12% |
|| Operação de recall e fiscalizações | 100-150 | 8% |
|| Gestão, avaliação e comunicação | 50-100 | 3% |
|| **TOTAL** | **1.100-1.650** | **100%** |

### 4.2 Fontes de financiamento

|| Fonte | Mecanismo | R$ bi/ano |
||-------|-----------|-----------|
|| Orçamento da União | Dotação + emendas | 1,0-1,5 |
|| Fundo de combate à corrupção / transparência | Parte de multas, recuperação de ativos | 0,1-0,2 |
|| Estados e Municípios | Contrapartida para terminais locais | 0,1-0,2 |
|| Parcerias internacionais | Cooperação técnica (Estonia, Taiwan, Suíça) + doações para auditoria | 0,05 |
|| **TOTAL** | | **1,25-1,95** |

---

## 5. TECNOLOGIA

### 5.1 Arquitetura da Assembleia Digital

```
Cidadão (app OpenTerminal / web / WhatsApp / terminal físico)
        │
    Camada de Identidade Digital Soberana (gov.br + biometria + proof-of-personhood)
        │
    Plataforma de Votação (blockchain permissioned + auditoria pública)
        │
    ┌───┴───┬──────────┬──────────┐
    │       │          │          │
Triagem  Conselho   Votação    Execução
IA (apoio) Técnico   Popular   (Congresso / Executivo)
(análise)  (sorteado) (51%)
```

### 5.2 Stack tecnológico

- **Frontend:** App mobile (Android/iOS), web responsiva, bots em mensageiros populares, terminais físicos com interface simples (telas touch + voz)
- **Backend:** Nuvem soberana brasileira (Serpro ou similar), microsserviços
- **Blockchain/Auditoria:** Hyperledger ou similar permissioned para registro imutável de votos; zero-knowledge proofs para privacidade onde aplicável
- **Identidade:** Integração gov.br, TSE, CadÚnico; biometria com consentimento explícito
- **Segurança:** Criptografia ponta-a-ponta, auditoria contínua, bug bounty permanente, LGPD by design, acessibilidade WCAG 2.2
- **Integração:** APIs com Congresso (tramitação), TSE (eleições), eSocial, portais de transparência
- **Acessibilidade:** Suporte total a libras, áudio, baixo letramento, múltiplos idiomas, modo offline parcial

### 5.3 OpenTerminal

- Nome oficial do sistema de acesso
- Um só app para todas as votações, recalls, consultas
- Notificações opt-in, resumos semanais
- Modo "silêncio" compatível com P20

---

## 6. RECURSOS HUMANOS

### 6.1 Equipe central

- ANDD: ~300 pessoas (gestão, tecnologia, jurídico, educação, fiscalização)
- Conselho Técnico: 2.000+ especialistas (bolsistas ou voluntários com suporte)
- Equipes estaduais: 27 x ~50 = 1.350
- Total novo: ~2.000-2.500 profissionais

### 6.2 Formação

- Formação intensiva para operadores do sistema e facilitadores de educação cívica
- Curso nacional de "Democracia Digital" para servidores e sociedade civil
- Parcerias com universidades para pesquisa e avaliação

### 6.3 Custos de RH

- ~ R$ 400-600 milhões/ano em pessoal (incluído no orçamento)

---

## 7. RISCOS E MITIGAÇÕES

|| Risco | Probabilidade | Impacto | Mitigação |
||-------|--------------|---------|-----------|
|| Hackers ou fraude em votações | Média | Crítico | Blockchain + auditoria independente contínua; testes de penetração; rollback manual + investigação; bug bounty |
|| Baixa participação (apatia) | Alta | Alto | Educação cívica massiva; interface ultra-simples; notificações úteis; vinculação real de resultados; gamificação leve |
|| Manipulação por grupos organizados (bots, compra de votos) | Média | Alto | Identidade forte + prova de vida; limites de votação por pessoa; detecção de anomalias com IA + humano; auditoria amostral |
|| Congresso resiste ou ignora propostas aprovadas | Alta | Crítico | PEC que dá força de lei; pressão popular via recall dos parlamentares; transparência total de "propostas ignoradas" |
|| Exclusão digital (sem smartphone/internet) | Alta | Médio | Terminais físicos massivos; integração WhatsApp/Telegram/SMS; suporte em cartórios e serviços públicos; modo voz |
|| Descontinuidade política | Média | Crítico | Lei com status constitucional (PEC); dados públicos imutáveis; sociedade civil com poder de fiscalização via conselho |
|| Viés no Conselho Técnico | Baixa | Médio | Sorteio aleatório + critérios objetivos; transparência total das análises; possibilidade de contestação popular |
|| Sobrecarga de propostas | Alta | Médio | Triagem por IA de apoio + Conselho; priorização por impacto/popularidade; lotes de votação |

---

## 8. KPIs E MONITORAMENTO

### 8.1 Indicadores de processo

|| KPI | Linha de base | Meta Ano 5 | Meta Ano 10 |
||-----|---------------|-------------|-------------|
|| Cidadãos cadastrados na plataforma | <5% | 50% | 85%+ |
|| Terminais físicos instalados | 0 | 10.000 | 50.000+ |
|| Votações realizadas (nacionais + regionais) | — | 100+ | 500+ |
|| Propostas analisadas pelo Conselho Técnico | — | 200 | 1.000+ |

### 8.2 Indicadores de resultado

|| KPI | Linha de base | Meta Ano 5 | Meta Ano 10 |
||-----|---------------|-------------|-------------|
|| Participação média por votação | <5% (em plebiscitos) | 20% | 35%+ |
|| Propostas da assembleia convertidas em lei ou política | 0 | 30 | 150+ |
|| Recall iniciados / bem-sucedidos | 0 | 20 / 5 | 100 / 30 |
|| Percepção de legitimidade do governo (pesquisas) | Baixa (~30-40% confiança) | +15 pontos | +30 pontos |
|| Casos de corrupção detectados/reduzidos em áreas priorizadas | Estimativa alta | -20% | -40-50% |
|| Satisfação com democracia (índice) | Baixa | +20% relativo | +40% |

### 8.3 Frequência de monitoramento

- **Diária/Semanal:** Métricas de uso da plataforma (ANDD dashboard público)
- **Mensal:** Relatórios agregados de participação, recalls
- **Trimestral:** Auditoria de segurança + relatório ao Congresso
- **Anual:** Avaliação independente de impacto + pesquisa nacional de opinião

---

## 9. CRONOGRAMA VISUAL

```
ANO   1   2   3   4   5   6   7   8   9   10
      │   │   │   │   │   │   │   │   │   │
FASE1 ████████                     Fundação + Piloto
FASE2         ████████████         Expansão Nacional
FASE3                     ████████ Consolidação
      │   │   │   │   │   │   │   │   │   │
LEI   ▓▓▓▓▓▓▓▓▓▓▓▓
PLAT  ▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
CAD   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ (5% → 85%)
RECALL     ▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
PART       ▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ (crescimento)
R$    0.8 1.5 1.2 1.0 1.1 1.0 0.5 0.4 0.4 0.4 (bi/ano)
```

---

## 10. MARCOS DE AVALIAÇÃO E GATILHOS

|| Marco | Quando | Gatilho se NÃO alcançar |
||-------|--------|------------------------|
|| Lei sancionada + ANDD criada | Ano 2 | Medida Provisória + pressão popular |
|| Plataforma MVP auditada e piloto em 3 estados | Ano 3 | Revisão de arquitetura + nova licitação |
|| 50% cadastrados + 20% participação média | Ano 6 | Campanha intensiva + simplificação de interface + incentivos cívicos |
|| 30+ políticas implementadas da assembleia | Ano 7 | Auditoria de bloqueios + recall de parlamentares resistentes |
|| Redução mensurável de corrupção | Ano 8-10 | Revisão profunda + ajuste de escopo para temas de alto impacto |
|| Sistema auto-sustentável | Ano 10 | Redução de orçamento para cruzeiro |

---

## 11. SISTEMAS DA OPENREPUBLIC ENVOLVIDOS

|| Sistema | Função na execução |
||---------|--------------------|
|| OpenDemocracy | Plataforma central: assembleia digital, votação, recall, OpenTerminal |
|| OpenConstituentAssembly (antigo nome) | Núcleo constitucional e legal da participação |
|| OpenCivicEducation (P15) | Educação cívica integrada para aumentar participação |
|| OpenAntiDeterminism (P13) | Apoio cultural para quebrar determinismo e incentivar engajamento |
|| OpenTransparency / OpenData | Publicação de todos os dados, análises e resultados em tempo real |
|| OpenFounderRole (P30) | Compatibilidade com governança fundadora (checks and balances) |

---

## 12. NOTAS FINAIS

Este plano é uma simulação de execução baseada na descrição da P29 em POLITICAS_PUBLICAS_BRASIL_V2.md e em evidências internacionais de democracia direta digital (Suíça, Taiwan vTaiwan, Estonia i-Voting). Os valores de economia em corrupção são estimativas de ordem de grandeza — a quantificação real exige estudos do TCU, CGU, IPEA e academia independente.

A maior barreira não é tecnológica, mas cultural e de confiança: convencer a população de que seu voto conta de verdade e que o sistema é à prova de manipulação. A arquitetura prioriza transparência radical, auditoria independente e acessibilidade máxima.

A execução depende de vontade política para ceder poder (recall e deliberação popular). O design com Conselho Técnico (informativo, não decisório) e força de lei para aprovações populares busca equilibrar deliberação qualificada com soberania popular.

*Licença: CC0 Universal*
*OpenRepublic — 116 sistemas, 91.729 linhas de código*
