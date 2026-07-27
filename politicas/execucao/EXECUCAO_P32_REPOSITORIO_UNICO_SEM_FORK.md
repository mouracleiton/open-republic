# PLANO DE EXECUÇÃO — P32
# Repositório Único, Sem Fork

> Política: Um único repositório. Pull para puxar, merge request para propor. A assembleia vota com 51%. Tudo é testado antes de integrar. Forks que mutilam são proibidos. Tudo CC0. Custo: Zero — é política de desenvolvimento. Economia estimada: Prevenção de fragmentação e duplicação. Prazo: Imediato (fase 1). Base científica: Kernel do Linux — um repositório único há 30 anos. Torvalds, L. (2020) sobre maintainer model. Sistema: OpenRepoPolicy.

---

## 0. RESUMO EXECUTIVO

|| Item | Valor |
||------|-------|
|| Investimento total | R$ 0 (política de governança de código e processos) |
|| Economia esperada | Alta — evita duplicação de esforços, fragmentação de ecossistemas, perda de contribuições, conflitos de versão e desperdício de recursos humanos/técnicos. Valor estimado em dezenas de bilhões ao longo de décadas para projetos de escala nacional |
|| Prazo total | Imediato (fase 1) + manutenção contínua |
|| População-alvo | Todos os desenvolvedores, mantenedores e usuários dos 116+ sistemas OpenRepublic |
|| Estrutura atual | Múltiplos repositórios ou risco de forks em projetos abertos |
|| Meta | Único repositório oficial para cada sistema/projeto OpenRepublic; processo de merge baseado em testes + votação da assembleia (51%); forks mutiladores proibidos por regra comunitária + legal |
|| Confiança da estimativa | ALTA (modelo comprovado pelo kernel Linux e grandes projetos open source) |

---

## 1. MARCO LEGAL NECESSÁRIO

### 1.1 Regras internas e documentos fundacionais

**OpenRepoPolicy — Política de Repositório Único (documento oficial + código de conduta)**

- Estabelece que todo sistema OpenRepublic tem exatamente um repositório oficial (Git ou equivalente)
- Define o fluxo: 
  - Pull / fetch do repositório oficial
  - Contribuições via merge/pull requests
  - Todo merge passa por testes automatizados + revisão humana + aprovação da assembleia (51% para mudanças normais)
- Proíbe forks que "mutilam" o projeto (removem licença CC0, adicionam restrições, fragmentam o ecossistema, mudam nome de forma a confundir)
- Forks permitidos apenas para:
  - Experimentação temporária (com aviso claro)
  - Traduções / localizações
  - Projetos derivados que não competem diretamente e mantêm compatibilidade
- Tudo licenciado CC0 (ou equivalente permissivo) por padrão
- A assembleia digital (P29) tem poder final de decisão sobre merges controversos

**Integração com Licenciamento e Governança**

- Atualização do estatuto da OpenRepublic para incluir a política
- Cláusula em todos os repositórios: "Este é o repositório oficial. Forks que violem a política podem ser ignorados e o autor pode ser removido da comunidade"

**Aspectos Legais (se aplicável no contexto público)**

- Se sistemas OpenRepublic forem adotados pelo Estado: a política vira norma de desenvolvimento de software público (semelhante a políticas de software livre do governo)
- Evitar fragmentação de sistemas públicos (ex: múltiplas versões de OpenHealth em diferentes estados)

**Portarias / Documentos Imediatos**

- Publicação oficial da OpenRepoPolicy v1.0
- Template de repositório com CI/CD obrigatório, testes e processo de merge documentado

### 1.2 Cronograma (imediato)

|| Ação | Responsável | Prazo |
||------|-------------|-------|
|| Redação e aprovação da OpenRepoPolicy | Mantenedores + assembleia inicial | Mês 1-2 |
|| Aplicação a todos os repositórios existentes | Equipe técnica | Mês 2-6 |
|| Implementação de CI/CD e testes em todos os projetos | Mantenedores por sistema | Mês 3-12 |
|| Comunicação e educação da comunidade | OpenRepoPolicy team | Contínuo a partir de Mês 1 |
|| Auditoria inicial de forks existentes | Voluntários | Mês 4-8 |

---

## 2. ESTRUTURA INSTITUCIONAL

### 2.1 Governança

```
Comunidade / Desenvolvedores (pull requests)
         │
    Mantenedores por Sistema (revisão técnica)
         │
    Assembleia Digital / Votação (51% para decisões controversas — P29)
         │
    OpenRepoPolicy (regras centrais)
         │
    Repositório Oficial Único (git + CI/CD + testes)
         │
    Integração contínua → Produção (após aprovação)
```

### 2.2 Papéis

- **Mantenedores:** Responsáveis por revisão técnica, merge de mudanças menores, manutenção do repositório oficial
- **Assembleia:** Decide em casos de conflito, mudanças de arquitetura, licenciamento, forks controversos
- **Fundador (P30):** Voz consultiva, voto normal
- **Comunidade:** Qualquer um pode propor via PR; contribuições são bem-vindas

---

## 3. FASES DE EXECUÇÃO

### FASE 1 — IMPLEMENTAÇÃO IMEDIATA (Mês 1-12)

**Objetivo:** Estabelecer a política, aplicar a todos os projetos atuais, configurar infraestrutura de merge seguro.

**3.1.1 Política e Documentação**

- Aprovar e publicar OpenRepoPolicy
- Criar templates de repositório com:
  - README com regras claras
  - Código de conduta
  - Processo de contribuição
  - CI/CD pipeline obrigatório
- Custo: R$ 0

**3.1.2 Migração de Repositórios Existentes**

- Identificar todos os repositórios atuais dos sistemas OpenRepublic
- Consolidar em repositórios únicos oficiais (se houver duplicatas)
- Configurar proteção de branch (main protegido, só merge via PR + testes)
- Custo: R$ 0-20 milhões (se houver custos de migração de hospedagem)

**3.1.3 Infraestrutura de Testes e CI/CD**

- Padronizar uso de GitHub Actions / GitLab CI / equivalente soberano
- Exigir testes automatizados (unit, integration, lint) antes de merge
- Adicionar revisão de segurança básica
- Treinar mantenedores
- Custo: baixo (ferramentas open source)

**3.1.4 Gestão de Forks Existentes**

- Mapear forks
- Contatar autores: convidar para contribuir no oficial ou marcar como experimental
- Proibir forks mutiladores via política comunitária
- Custo: R$ 0

**MARCO FASE 1 (Mês 12):**

- [ ] OpenRepoPolicy v1.0 aprovada e publicada
- [ ] 100% dos sistemas OpenRepublic em repositório único oficial
- [ ] CI/CD + testes obrigatórios em todos os repositórios principais
- [ ] Processo de merge documentado e em uso
- [ ] Zero forks mutiladores ativos

**TOTAL FASE 1: R$ 0-50 milhões (integrado)**

---

### FASE 2 — CULTURA E ESCALA (Anos 1-3)

**Objetivo:** Internalizar a prática, expandir para novos projetos, reforçar com ferramentas.

- Educação contínua via OpenSkills e documentação
- Ferramentas automatizadas para detectar forks não autorizados
- Processo de votação da assembleia para merges grandes (via integração com OpenDemocracy)
- Auditorias anuais de aderência
- Custo: R$ 0

**MARCO FASE 2 (Ano 3):**

- [ ] 100% das contribuições seguem o fluxo oficial
- [ ] Ferramentas de detecção de fragmentação em produção
- [ ] Várias decisões de merge grandes tomadas pela assembleia
- [ ] Política replicada em projetos parceiros

---

### FASE 3 — MATURIDADE (Anos 4+)

**Objetivo:** Modelo consolidado, exportável.

- Documentação para outros projetos adotarem o modelo
- Evolução da política conforme lições aprendidas
- Integração com OpenRepair (P34) para ferramentas de manutenção
- Custo: R$ 0

---

## 4. ORÇAMENTO DETALHADO

Custo direto: R$ 0

Custos indiretos mínimos:

- Hospedagem de repositórios (GitHub/GitLab gratuito ou soberano baixo custo)
- Tempo de mantenedores (voluntário ou parte de outros orçamentos)
- Ferramentas de CI (gratuitas para open source)

Nenhum orçamento novo dedicado.

---

## 5. TECNOLOGIA

### 5.1 Stack do Repositório

- Git (ou equivalente distribuído)
- Plataforma: GitHub, GitLab, ou instância soberana (ex: Gitea self-hosted)
- CI/CD: GitHub Actions / GitLab CI / Jenkins ou similar
- Testes: obrigatórios por linguagem (pytest, jest, etc.)
- Code review: obrigatório via PR
- Branch protection: main só atualizado por merge aprovado
- Ferramentas de detecção de forks: scripts + bots

### 5.2 OpenRepoPolicy

- Documento vivo no repositório oficial
- Versões versionadas
- Integração com OpenDemocracy para votação de mudanças na política

### 5.3 Automação

- Bot que comenta em forks: "Este fork viola a política X. Contribua no repositório oficial."
- Verificação de licença CC0 em PRs
- Verificação de testes passando antes de permitir merge

---

## 6. RECURSOS HUMANOS

- Mantenedores por sistema: 1-5 por projeto (existentes ou novos)
- Equipe central OpenRepoPolicy: 3-5 pessoas (parte time)
- Comunidade de revisores
- Nenhum RH novo de grande escala

---

## 7. RISCOS E MITIGAÇÕES

|| Risco | Probabilidade | Impacto | Mitigação |
||-------|--------------|---------|-----------|
|| Alguém cria fork mutilador popular | Média | Alto | Política clara + comunicação forte; ferramentas de detecção; assembleia pode declarar fork inválido; pressão comunitária |
|| Mantenedores abusam de poder de merge | Média | Médio | Revisão obrigatória por pares; votação da assembleia para mudanças grandes; logs públicos; possibilidade de remoção |
|| Baixa adesão inicial ("vou fork porque é mais fácil") | Alta | Médio | Educação; templates fáceis; benefícios claros do oficial (visibilidade, integração, suporte) |
|| Conflito entre assembleia e mantenedores técnicos | Baixa | Médio | Processo claro: técnico decide qualidade; assembleia decide direção quando há impasse |
|| Fragmentação em projetos dependentes | Média | Alto | Política se aplica a todos os sistemas OpenRepublic; integração obrigatória via monorepo ou submodules gerenciados |
|| Dificuldade com contribuintes externos | Média | Baixo | Processo simples de PR + documentação excelente + mentoria |

---

## 8. KPIs E MONITORAMENTO

### 8.1 Indicadores de processo

|| KPI | Linha de base | Meta Ano 1 | Meta Ano 3 |
||-----|---------------|-------------|-----------|
|| Sistemas em repositório único oficial | Variável | 100% | 100% |
|| PRs com testes passando antes de merge | Baixo | 95%+ | 99%+ |
|| Forks detectados e tratados | — | Mapear todos | Manter zero mutiladores |
|| Votações da assembleia sobre merges | 0 | 10+ | 50+ |

### 8.2 Indicadores de resultado

|| KPI | Linha de base | Meta Ano 2 | Meta Ano 5 |
||-----|---------------|-------------|-----------|
|| Contribuições totais (PRs merged) | Base | +50% | +200% (efeito rede) |
|| Duplicação de código entre projetos | Alta | Reduzir 50% | Reduzir 80% |
|| Tempo médio de integração de contribuição | Variável | Reduzir | Estável baixo |
|| Conflitos de versão / breaking forks | — | Zero | Zero |

### 8.3 Frequência

- **Contínua:** CI/CD reports públicos
- **Mensal:** Dashboard de contribuições e forks
- **Anual:** Auditoria de aderência à OpenRepoPolicy + relatório

---

## 9. CRONOGRAMA VISUAL

```
MÊS  1-3   4-6   7-12  Ano2  Ano3  Ano5+
     │     │     │     │     │     │
FASE1 █████ █████ █████       Implementação
FASE2             ████████████ Cultura + Escala
FASE3                         █████ Maturação
     │     │     │     │     │     │
POLICY ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
REPO   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ (100%)
CI/CD  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
VOTO         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
R$     0     0     baixo 0     0     0
```

---

## 10. MARCOS DE AVALIAÇÃO E GATILHOS

|| Marco | Quando | Gatilho se NÃO alcançar |
||-------|--------|------------------------|
|| Política aprovada e publicada | Mês 2 | Revisão imediata pela comunidade |
|| 100% repositórios únicos | Mês 6 | Migração forçada + suporte técnico |
|| CI/CD + testes em todos | Mês 12 | Bloqueio de merges até implementação |
|| Zero forks mutiladores | Ano 1 | Comunicação + assembleia declara inválidos |
|| Aumento mensurável de contribuições | Ano 2 | Análise de barreiras + simplificação de processo |

---

## 11. SISTEMAS DA OPENREPUBLIC ENVOLVIDOS

|| Sistema | Função na execução |
||---------|--------------------|
|| OpenRepoPolicy | Política central e documentação do modelo |
|| Todos os 116 sistemas | Devem seguir o repositório único e processo de merge |
|| OpenDemocracy (P29) | Votação de assembleia para decisões controversas de merge |
|| OpenFounderRole (P30) | Papel do fundador no processo (voz + voto normal) |
|| OpenRepair (P34) | Ferramentas de reparo e manutenção de código no repositório oficial |
|| OpenSkills (P16) | Registro de competências de mantenedores e contribuidores |

---

## 12. NOTAS FINAIS

Este plano é uma simulação de execução baseada integralmente na descrição da P32 em POLITICAS_PUBLICAS_BRASIL_V2.md. O custo é zero porque é uma política de desenvolvimento, não um programa com orçamento.

O modelo é inspirado diretamente no sucesso do kernel do Linux: um único repositório há décadas, mantido por Linus e comunidade, com processo rigoroso de revisão e testes.

A proibição de forks mutiladores protege o ecossistema coletivo contra fragmentação que beneficia apenas quem quer dividir para controlar ou monetizar.

A assembleia (P29) fornece o mecanismo democrático para resolver impasses que mantenedores técnicos sozinhos não conseguem.

*Licença: CC0 Universal*
*OpenRepublic — 116 sistemas, 91.729 linhas de código*
