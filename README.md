# OpenRepublic

Repositorio de especificacoes executaveis em Python real do Brasil.

66 modulos. 55.000+ linhas. Tudo compila. Tudo com dados 2024/2025.

```
"O IBGE pergunta ao diretor. Nos perguntamos ao chao."
```

## O que e

O OpenRepublic e um sistema de principios constitucionais codificados (P1-P14) que avaliam sistemas governamentais. Nao e partido. Nao e ONG. E especificacao tecnica de como um pais deveria funcionar, com dados verificaveis.

O principio central: **Fraternismo** -- nem comunismo nem capitalismo. Fraternidade (roda de capoeira, time de domingo, grupo de Discord) ampliada a nivel nacao.

## Estrutura

```
open-republic/
├── core/
│   ├── constituicao/        22 modulos -- Principios P1-P14, motor constitucional, cultura
│   ├── acessibilidade/      18 modulos -- Cego, surdo, tetraplegico, idoso, autista
│   ├── economia/            14 modulos -- Raio X, censo, educacao, divida, politica publica
│   ├── voz/                  7 modulos -- Iara (IA), pipeline voz, pentest por voz
│   └── distro/               5 modulos -- Linux, servidor jogos, smartphone modular, chip fab
├── dashboard.html           Raio X do Brasil (6 abas interativas)
├── relatorio.html           Ineficiencia das Politicas Publicas (mobile-first)
├── carrosseis.html          6 carrosseis Instagram (frentes de ataque)
├── carrosseis_png/          30 PNGs 1080x1080 prontos para postar
├── README.md                Este arquivo
└── .gitignore
```

## Principios Constitucionais (P1-P14)

| # | Principio | O que faz |
|---|-----------|-----------|
| P1 | Anti-elitismo | Ninguem manda sozinho |
| P2 | Autonomia corporal absoluta | Seu corpo e seu |
| P3 | Trabalho igual | Todo trabalho vale o mesmo |
| P4 | Processo democratico | Decisao em grupo |
| P5 | Transparencia radical | Tudo publico |
| P6 | Acesso universal | Conhecimento para todos |
| P7 | Seguranca como cultura | Nao militarizada |
| P8 | IA como instrumento | Nao substitui humano |
| P9 | Anti-polarizacao | Estado nao toma partido |
| P10 | Soberania aerea civica | Drone civico |
| P11 | Letramento digital | Constituinte |
| P12 | Defesa cibernetica transparente | 5 proibicoes |
| P13 | Contravigilancia reciproca | 5 tiers de privacidade |
| P14 | Soberania de dados | 6 direitos D1-D6 |

## Alicerce Etico (5 pilares)

1. **ESCOLHA_INTRINSECA** -- etica por escolha, nao imposicao
2. **TRATAR_IGUAL** -- CEO e faxineira, teste da padaria
3. **GENUINIDADE** -- etica que e estrategia ja falhou
4. **CRESCER_ESPIRITUALMENTE** -- secular, sem recompensa divina
5. **IMPACTO_EMOCIONAL_PERMANENTE** -- "esquecerao seu rosto, nunca como os fez sentir"

## Raio X do Brasil

O checkup nacional. 18 exames em 18 dominios. Custo: R$ 85 milhoes/ano (3% do Censo IBGE).

**3 emergencias** (vidas em risco AGORA):
- Violencia -- 21.7 homicidios/100k
- Saude -- dengue 2024: 6M casos, 4000+ mortes
- Alimentacao -- 33 milhoes passando fome

**37.5 milhoes de brasileiros invisiveis** que o IBGE nao conta.

Ver dashboard.html para analise interativa completa.

## Politicas Publicas Mapeadas

33 politicas avaliadas contra os 18 dominios do Raio X.

**Veredito durao:**
- 2 de 33 (6%) **resolvem** o problema
- 20 de 33 (61%) sao **parciais**
- 9 de 33 (27%) tem **impacto minimo**
- 2 de 33 (6%) **nao resolvem**

As 2 que funcionam (VIGISAN e MapBiomas/INPE) sao sistemas de **observacao**, nao de acao.

Ver relatorio.html para relatorio completo com 6 causas raiz e 6 recomendacoes.

## Triagem Operacional (Regra do Pronto-Socorro)

| Categoria | Regra | Exemplo |
|-----------|-------|---------|
| VIDA | Age AGORA, diagnostica depois | Crianca com fome -> da comida |
| BOLSO | Diagnostica PRIMEIRO, age depois | Inflacao -> entende causa |
| VOTO | NUNCA sem FATO (P9 palanque) | Seguranca publica |
| ESTRUTURA | Diagnostica + trata simultaneo | Escola sem agua |

## Censo Proprio

Substituindo o IBGE. 18 dominios, coleta em tempo real, OSINT + cidadao.

- Custo: R$ 200M/ano (IBGE custou R$ 2.3bi)
- 37.5M de brasileiros que o IBGE nao conta
- Atualizacao: tempo real a anual (IBGE: a cada 10 anos)

## 10 Camadas (L0-L9)

| Camada | Descricao | Cobertura |
|--------|-----------|-----------|
| L0 | Hardware fisico | 3/5 |
| L1 | Soberania tecnologica | 2/5 |
| L2 | Infra digital | 2/5 |
| L3 | Constituicao | 9/9 (100%) |
| L4 | Sistemas publicos | 4/12 |
| L5 | Acessibilidade | 17/17 (100%) |
| L6 | Interface | 7/9 |
| L7 | Cultura | 3/6 |
| L8 | Relacoes externas | 0/4 |
| L9 | Memoria | 0/4 |

## Gate Epistemologico: FATO vs DADO vs OPINIAO

- **OPINIAO**: afirmacao sem dados (0% confianca)
- **DADO**: numero com fonte mas sem verificacao (50-70%)
- **FATO**: 7 criterios atendidos (100% confianca)

So FATO vira politica. Opiniao nunca. Dado precisa de mais comprovacao.

7 criterios: amostra representativa, reprodutivel, fonte independente, triangulacao, sem vies, magnitude mensuravel, dado temporal.

## Anticorpos contra Apropriacao

5 niveis de protecao:

1. **Nome**: CC0 radical (ninguem dono do nome)
2. **Codigo**: data.json publico (principios sao dados)
3. **Lider**: P1 anti-guru (ninguem manda sozinho)
4. **Dinheiro**: reputacao publica (todas as contas transparentes)
5. **Estado**: constitutional_monitor (vigia o Estado em tempo real)

## Como rodar

Cada modulo e um script Python standalone com demo integrado:

```bash
# Raio X do Brasil (18 exames)
python3 core/economia/open_raio_x_brasil.py

# Motor constitucional (14 principios)
python3 core/constituicao/constitutional_engine.py

# Censo nacional (18 dominios)
python3 core/economia/open_censo_nacional.py

# Politicas publicas (33 programas avaliados)
python3 core/economia/open_politica_publica.py

# Triagem operacional
python3 core/constituicao/open_triage_operacional.py

# Validador de ideias independente de sistema
python3 core/constituicao/open_idea_validator.py

# Fome infantil com rastreio
python3 core/constituicao/open_child_food_security.py

# Defesa cibernetica
python3 core/constituicao/open_cyber_defense.py

# Constituicao cultural (cordel + capoeira + alicerce etico)
python3 core/constituicao/open_cultural_constitution.py
```

## Visualizacoes

| Arquivo | O que e |
|---------|---------|
| `dashboard.html` | Raio X do Brasil -- 6 abas interativas (ECharts) |
| `relatorio.html` | Relatorio de Ineficiencia -- mobile-first com fallback |
| `carrosseis.html` | 6 carrosseis Instagram por frente de ataque |
| `carrosseis_png/` | 30 PNGs 1080x1080 prontos para postar |

## Stack

- **Linguagem**: Python 3.11+ (sem dependencias externas nos modulos)
- **Arquitetura**: dados (data.json) <-> logica (.py puro) <-> discernimentos (.md)
- **Dashboard**: Tailwind CSS + ECharts + fallback HTML puro
- **Dados**: 2024/2025, fontes publicas (IBGE, INEP, VIGISAN, DataSUS, SINESP)
- **Licenca**: CC0 Universal

## 66 Modulos por Categoria

### Constituicao (22 modulos)
constitutional_engine, open_anti_polarization, open_citizen_oversight, open_constitutional_monitor, open_cultural_constitution, open_cyber_defense, open_data_sovereignty, open_denuncia, open_digital_literacy, open_drone, open_fato_dado_opiniao, open_triage_operacional, open_political_reliability, open_political_risk_predictor, open_republic_colors, open_republic_layers, open_republic_exporter, open_resilience, open_sovereign_tech, open_unified_codebase, open_idea_validator, open_child_food_security

### Acessibilidade (18 modulos)
open_accessibility_hardware_specs, open_accessibility_shim, open_ambient_sound, open_auth_access, open_body_camera, open_command_reference, open_digital_dog_guide, open_digital_guide, open_haptic_navigation, open_human_net, open_inclusive_education, open_inclusive_hardware, open_inclusive_home, open_inclusive_ide, open_libras_bridge, open_sign_language_policy, open_sign_language_universal, open_universal_caption

### Economia (14 modulos)
open_agrarian_revolution, open_censo_escolar, open_censo_nacional, open_debt_abolition, open_debt_default, open_debt_impact, open_debt_mortality, open_education_system, open_energy, open_energy_taxonomy, open_politica_publica, open_raio_x_brasil, open_recyclers_hardware (em distro), open_school_identity, open_school_osint

### Voz (7 modulos)
open_clipboard_intelligence, open_iara, open_telefonista, open_voice_os_control, open_voice_pipeline, open_voice_pentest, open_voice_terminal_bridge

### Distro (5 modulos)
open_big_linux, open_chip_fab, open_forge_os, open_modular_phone, open_recyclers_hardware

## Licenca

CC0 Universal. Todo o conhecimento aqui e patrimonio publico.

Ninguem e dono. Todos podem usar, modificar, distribuir.

```
github.com/mouracleiton/open-republic
@openrepublic
```
