# PLANO DE EXECUÇÃO — P21
# Ligação Predatória Proibida

> Política: Proibir toda ligação não solicitada. Opt-in obrigatório: ninguém liga sem autorização prévia. Três denúncias geram bloqueio permanente. A IA bloqueia antes de tocar. Robocall deixa de existir. Golpe confirmado é crime. Custo: Zero — é regulação + tecnologia existente. Economia estimada: R$ 3-5 bilhões/ano em golpes evitados (ProCon estimativas). Prazo: 1-2 anos (fase 1). Base: Brasil já tem o "Não Me Ligue" do ProCon — precisa de fiscalização efetiva. LGPD (Lei 13.709/2018). Sistema: OpenAntiSpamCall.

---

## 0. RESUMO EXECUTIVO

|| Item | Valor |
||------|-------|
|| Investimento total | R$ 0-200 milhões/ano (regulação + plataforma de bloqueio + fiscalização) |
|| Economia esperada | R$ 3-5 bilhões/ano em golpes, fraudes e tempo perdido com telemarketing abusivo |
|| Prazo total | 1-2 anos em 2 fases |
|| População-alvo | 200+ milhões de linhas móveis + fixas no Brasil |
|| Meta | Quase zero ligações não solicitadas + robocalls; 100% opt-in para contatos comerciais |
|| Confiança da estimativa | MÉDIA |

---

## 1. MARCO LEGAL NECESSÁRIO

### 1.1 Leis e regulamentos

**Lei do Opt-in Obrigatório e Bloqueio de Ligações Predatórias (nova ou reforma forte do "Não Me Ligue")**
- Proíbe toda ligação telefônica não solicitada (comercial, cobrança, pesquisa, etc.) sem consentimento prévio explícito (opt-in)
- Ligações de cobrança só permitidas se houver relação contratual prévia e opt-in específico
- Três denúncias confirmadas de uma mesma origem = bloqueio permanente da linha/número para ligar (lista negra nacional)
- IA / sistemas automáticos devem bloquear chamadas antes de tocar no destinatário quando identificadas como predatórias
- Robocalls (chamadas automáticas gravadas) proibidas exceto em casos de emergência pública autorizada
- Golpe confirmado (engenharia social, fraude) = crime com agravante + pena mínima mais alta

**Reforma da LGPD e Código de Defesa do Consumidor**
- Reforça consentimento explícito para contato telefônico
- Define "ligação predatória" como prática abusiva com sanções pesadas

**Portarias (Anatel, Procon, Ministério da Justiça)**
- Regulamentação técnica de sistemas de bloqueio por IA
- Definição de "não solicitada" e exceções limitadas (ex: alertas de segurança, saúde pública)
- Criação/atualização do cadastro nacional de opt-in e lista negra

### 1.2 Cronograma

|| Ação | Responsável | Prazo |
||------|-------------|-------|
|| Redação da Lei de Opt-in + Bloqueio | Anatel + Ministério da Justiça + Casa Civil | Mês 1-3 |
|| Consulta com operadoras, Procon, consumidores, associações de call centers | Anatel | Mês 3-6 |
|| Audiências e tramitação | Comissões de Comunicações e Defesa do Consumidor | Mês 6-11 |
|| Votação e Sanção | Congresso + Presidência | Mês 11-16 |

---

## 2. ESTRUTURA INSTITUCIONAL

### 2.1 Governança

```
Anatel + Senacon (Procon Nacional)
         │
    Coordenação Nacional Anti-Spam e Anti-Golpe (nova ou ampliada)
         │
    ┌────┴────┬──────────┬────────────┐
    │         │          │            │
Bloqueio    Fiscalização  Lista de    Educação e
por IA      e Sanções     Opt-in/Negra  Denúncias
(nacional)  (nacional)    (nacional)   (nacional)
```

Operadoras de telefonia devem implementar os bloqueios obrigatoriamente.

Integração com operadoras, bancos, Procon, Polícia Federal (para golpes).

---

## 3. FASES DE EXECUÇÃO

### FASE 1 — LEI E IMPLEMENTAÇÃO TÉCNICA (Anos 1-1)

**Objetivo:** Aprovar lei forte, criar/atualizar plataforma, implementar bloqueio em operadoras e grandes players.

**3.1.1 Marco Legal**
- Sanção da lei
- Custo: baixo

**3.1.2 Plataforma OpenAntiSpamCall + Integração com Operadoras**
- Atualização ou nova plataforma nacional de opt-in e lista negra
- Sistemas de IA nas operadoras para detecção e bloqueio pré-toque (usando padrões de robocall, números de golpe conhecidos, volume anormal)
- Integração com bancos para alertas de golpe em tempo real
- Custo: R$ 100-200 milhões (desenvolvimento + integração)

**3.1.3 Conformidade Imediata para Grandes Call Centers e Empresas**
- Empresas de telemarketing e cobrança têm 3-6 meses para migrar para opt-in only
- Custo: absorvido pelo setor privado

**MARCO FASE 1 (Mês 12-16):**
- [ ] Lei sancionada
- [ ] Plataforma nacional operante
- [ ] Todas as grandes operadoras com bloqueio IA ativo
- [ ] Redução drástica de robocalls e ligações não solicitadas (medido por amostragem)

**TOTAL FASE 1: R$ 100-250 milhões**

---

### FASE 2 — FISCALIZAÇÃO, BLOQUEIO PERMANENTE E CULTURA (Anos 1-2+)

**Objetivo:** Cobertura total, enforcement rigoroso, educação contra golpes, medição de economia.

**3.2.1 Bloqueio Automático e Lista Negra**
- Implementação plena de "3 denúncias = bloqueio permanente"
- Bloqueio de números de golpe em tempo real via IA + inteligência compartilhada
- Custo: R$ 50-100 milhões/ano

**3.2.2 Fiscalização e Sanções**
- Multas altas por ligação sem opt-in (proporcional ao faturamento)
- Fechamento de empresas reincidentes
- Integração com PF para casos de golpe
- Custo: R$ 100-200 milhões/ano

**3.2.3 Educação Anti-Golpe**
- Campanhas constantes (TV, redes, SMS oficial)
- Apps que alertam em tempo real
- Custo: R$ 100 milhões/ano

**MARCO FASE 2 (Ano 2):**
- [ ] Quase zero ligações predatórias ou robocalls
- [ ] Economia mensurável de R$ 2-4 bi/ano em fraudes evitadas
- [ ] Alta confiança da população em atender telefone novamente

**TOTAL FASE 2: R$ 250-400 milhões/ano (decrescente)**

---

## 4. ORÇAMENTO

|| Componente | R$ mi/ano |
||------------|-----------|
|| Plataforma e IA de bloqueio | 100-150 |
|| Fiscalização (Anatel + Procon + PF) | 100-200 |
|| Educação e comunicação | 50-100 |
|| **TOTAL** | **250-450** |

Fontes: Orçamento + multas revertidas.

---

## 5. TECNOLOGIA — OpenAntiSpamCall

- Plataforma central de opt-in, denúncias e lista negra
- Integração com todas as operadoras (API obrigatória)
- IA de detecção de padrões de golpe/robocall (volume, origem, conteúdo de voz/texto)
- App do cidadão para denúncia em 1 clique + histórico
- Alertas proativos para usuários de risco
- Blockchain ou registro imutável para lista negra (transparência)

---

## 6. RISCOS E MITIGAÇÕES

- Resistência do setor de call center/telemarketing → transição regulada com prazo + apoio para reconversão para canais opt-in (WhatsApp, e-mail autorizado)
- Contorno via números novos → bloqueio rápido + penalidade por uso de múltiplos números
- Golpes evoluindo para WhatsApp/Redes → complementar com regulação de spam em outros canais (P20, LGPD)

---

## 8. KPIs

|| KPI | Baseline | Meta Ano 1 | Meta Ano 2 |
||-----|----------|------------|------------|
|| Ligações não solicitadas por usuário/mês | 10+ | <2 | <0.5 |
|| Robocalls detectadas e bloqueadas | alto | 90%+ | 99%+ |
|| Golpes evitados (estimado) | — | R$ 1 bi | R$ 3-5 bi |
|| Denúncias processadas | — | baseline | declínio |

Frequência: Mensal para dados de volume, Anual para economia.

---

## 9-12. CRONOGRAMA, MARCOS, SISTEMAS E NOTAS

Cronograma curto: Lei em 12-16 meses, implementação plena em 24 meses.

Sistemas principais: OpenAntiSpamCall + integração com operadoras e OpenSilencePolicy / OpenAbsence.

Plano baseado diretamente na P21 de POLITICAS_PUBLICAS_BRASIL_V2.md. Política de custo quase zero com alto retorno em redução de irritação e fraudes.

*Licença: CC0 Universal*
*OpenRepublic — 116 sistemas, 91.729 linhas de código*
