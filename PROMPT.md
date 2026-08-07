# PROMPT: Gerar site estático de dados políticos + máquina de propaganda

Copia e cola este prompt numa IA generativa (Claude, GPT, etc.), fornecendo o JSON de dados como anexo ou colado no fim. O resultado será um site estático equivalente ao original.

---

## INSTRUÇÕES PARA A IA

Gera um **site estático de página única** (single-page application) que consome um arquivo JSON via `fetch()` e renderiza dados políticos/sociais em capítulos editoriais com visualizações interativas, além de uma "máquina de propaganda" que gera conteúdo para redes sociais. **Sem build step, sem framework, sem backend, sem npm.** Apenas HTML + CSS + JS puro + D3.js via CDN.

### Stack técnica obrigatória
- **HTML5** semântico, página única (`index.html`)
- **CSS** num ficheiro (`styles.css`), design system com variáveis CSS
- **JavaScript ES6+** puro (sem bundler), módulos IIFE por responsabilidade
- **D3.js v7** via CDN (`https://cdn.jsdelivr.net/npm/d3@7`)
- **Google Fonts**: Inter (400-800)
- **Zero dependências de build** — tudo roda abrindo o `index.html` num servidor estático

### Princípios de design
1. **Mobile-first**: base = 1 coluna; breakpoints em 640px e 960px expandem layout
2. **Tema escuro editorial**: fundo preto puro (`#000`), cards `#0B0B0E`, texto branco
3. **Acento cromado-vermelho**: cor de destaque `#C00810` (vermelho editorial)
4. **Tipografia**: Inter em tudo; títulos grandes com `letter-spacing: -0.02em`
5. **Sem ícones de partido**: o sistema é neutro/multi-partidário — nenhum logo, watermark de conta, ou marca própria aparece no output gerado
6. **Acessibilidade**: navegação por teclado, `aria-label` em elementos interativos, `role="tablist"` nas abas

---

## ESTRUTURA DO SITE (13 capítulos + secções dinâmicas)

### Layout padrão de cada capítulo
```html
<section class="chapter" id="ch-ID">
  <div class="container">
    <header class="chapter-head">
      <span class="chapter-no">NN</span>
      <p class="kicker">SUBTÍTULO CURTO</p>
      <h2>TÍTULO DO CAPÍTULO</h2>
      <p class="chapter-lede">Parágrafo de introdução editorial.</p>
    </header>
    <!-- conteúdo específico do capítulo -->
  </div>
</section>
```

### Capítulos fixos (com HTML hardcoded)

| # | ID | Título | Conteúdo |
|---|-----|--------|----------|
| 01 | ch-raiox | Raio-X do país | 18 barras horizontais (lollipop) com % de automação por domínio, coloridas por urgência (Emergência=vermelho, Urgente=âmbar, Automatizável=teal) |
| 02 | ch-orcamento | Orçamento público | Barras empilhadas horizontais mostrando distribuição do orçamento por área |
| 03 | ch-renda | Escada da renda | Barras verticais escalonadas de R$300 a R$25.000 mostrando distribuição |
| 04 | ch-racial | Desigualdade racial | Cards HTML (não SVG) comparando indicadores por cor/raça |
| 05 | ch-violencia | Violência por estado | Mapa de calor (grid colorido) de homicídios por UF + faixa horizontal de estados |
| 06 | ch-ocde | Brasil vs. mundo | Gráfico de barras comparando indicadores Brasil vs. média OCDE |
| 07 | ch-fatos | Mosaico de fatos | Pills filtráveis por categoria + grid de fact-cards. Clique no pill filtra |
| 08 | ch-timeline | Linha do tempo | `<ol>` vertical com eventos históricos, cada um com ano + descrição |
| 09 | ch-dossies | Dossiês de políticos | Grid de `<details>` accordions (525+ políticos), clicável para abrir |
| 10 | ch-propaganda | Máquina de propaganda | Tabs com geradores (ver abaixo) |
| 11 | ch-mais-valia | Calculadora de Mais-Valia | Formulário interativo + resultados calculados (ver abaixo) |
| 12 | ch-glossario | Glossário político | Lista de termos `<dl>` com busca textual |
| 13 | ch-tutoriais | Tutoriais de organização | 4 manuais passo-a-passo em accordions |

### Capítulos dinâmicos (A-K, gerados do JSON)
Um renderizador genérico lê secções do JSON e cria capítulos automaticamente. Cada secção torna-se um bloco com: stat grids (dicts chave→valor), tabelas (listas de objectos), e veredito (callout editorial). Agrupar 30+ secções temáticas em 8-12 capítulos por domínio.

### Máquina de propaganda (capítulo 10) — 8 abas
1. **Imagens**: Grid de carrosséis Instagram renderizados em `<canvas>` (1080px), download como ZIP
2. **Dossiês**: Carrosséis gerados a partir dos dossiês de políticos
3. **WhatsApp**: 3 mensagens prontas para copiar, customizáveis por tema e @
4. **X (Twitter)**: 3 tweets com contador de 280 caracteres
5. **Mensagens**: 3 variações (pessoal, grupo, curta)
6. **Áudio**: TTS via Web Speech API com controlo de velocidade/tom
7. **Prompts**: Gerador de prompts para IA (TikTok/YouTube/Reels/X) com salvar no localStorage
8. **Dossiê contra**: Propaganda de oposição baseada em factos do dossiê do político

Todas as mensagens têm um campo `@` (handle da rede) sincronizado entre abas.

---

## DESIGN SYSTEM (variáveis CSS)

```css
:root {
  /* Fundos */
  --paper: #000000;
  --paper-2: #0F0F13;
  --card: #0B0B0E;
  /* Texto */
  --ink: #FFFFFF;
  --ink-soft: #D4D4DA;
  --ink-faint: #909096;
  /* Bordas */
  --line: #202026;
  --line-strong: #33333B;
  /* Cores de acento */
  --coral: #C00810;
  --coral-deep: #8A0509;
  --amber: #E9A13B;
  --orange: #D97E2B;
  --teal: #0E7C7B;
  --violet: #6C5B9E;
  --green: #2F8F4E;
  --steel: #5B6B7A;
  /* Tipografia */
  --sans: 'Inter', system-ui, sans-serif;
  --disp: 'Inter', system-ui, sans-serif;
  /* Forma */
  --radius: 14px;
  --shadow-soft: 0 10px 30px rgba(0,0,0,0.55);
  --shadow-lift: 0 18px 50px rgba(0,0,0,0.65);
}
```

### Componentes CSS chave
- `.container`: `max-width: 1060px; margin: 0 auto; padding: 0 20px`
- `.masthead`: hero com gradiente radial subtil no fundo, título com `<em>` colorido em `--coral`
- `.stat-grid`: grid 2 colunas (mobile) → 4 colunas (desktop) com contadores animados
- `.chapter`: `padding: 56px 0 60px; border-bottom: 1px solid var(--line)`
- `.chart`: container responsivo para SVGs D3
- `.tabs` + `.tab-btn` + `.tab-panel`: navegação por abas com `is-active`
- `.msg-card`: card de mensagem gerada com label + texto + botão copiar
- `.doss-card`: `<details>` com summary clicável, badges de partido/UF
- `.btn-primary` / `.btn-ghost`: botões com hover states

---

## ARQUITETURA JAVASCRIPT

### Estrutura de ficheiros
```
assets/
  app.js              — Bootstrap: carrega JSON, orquestra todos os renders
  carousel-site.js    — Geração de carrosséis em canvas + download ZIP
  carrosseis.js       — Carrega carrosseis_instagram do JSON para window.CARROSSEIS
  machine.js          — Máquina de propaganda (mensagens, áudio, prompts)
  data-sections.js    — Renderizador genérico de capítulos dinâmicos A-K
  dossies-render.js   — Renderiza dossiês de políticos com filtro de placeholders
  mais-valia.js       — Calculadora de mais-valia interativa
  glossario.js        — Busca textual no glossário
  tutoriais.js        — Renderiza tutoriais
  styles.css          — Design system completo
```

### Padrão de carregamento de dados
```javascript
async function loadData() {
  try {
    const res = await fetch('dados_api.json', { cache: 'no-cache' });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.warn('[dados] fetch falhou:', err.message);
    return {};  // objeto vazio — nada quebra
  }
}
```

### Padrão de bootstrap de gráficos (responsivo + lazy-load)
Cada gráfico usa `IntersectionObserver` (renderiza quando entra na viewport) + `ResizeObserver` (re-renderiza quando o container muda de largura):
```javascript
function makeChart(selector, draw) {
  const el = document.querySelector(selector);
  // IntersectionObserver → draw() na primeira entrada na viewport
  // ResizeObserver → re-desenha se largura mudar >8px
}
```

### Padrão de dados assíncronos (race condition)
Carrosséis chegam via `fetch()` assíncrono. Scripts que dependem deles devem escutar o evento `carrosseis-loaded`:
```javascript
document.addEventListener('carrosseis-loaded', init);
```

### Padrão de números em pt-BR
Interpretar strings como "R$ 1.600", "21,2", "33 milhões":
```javascript
function toNum(s) {
  // Detecta vírgula decimal (pt-BR) vs ponto decimal (en-US)
  // Remove separadores de milhar, converte para número
}
```

---

## SCHEMA DO JSON DE DADOS (a fornecer)

O JSON tem estas secções principais. Adapta os nomes ao teu dataset:

```json
{
  "_meta": {
    "descricao": "Descrição do projeto",
    "atualizacao": "vX (data)",
    "resumo": ["40 seções temáticas", "27 estados", "525 dossiês", "..."]
  },
  "projeto": "Nome do projeto",
  "url_base": "https://exemplo.com/",

  "capitulos": {
    "ch-raiox": { "numero": "01", "kicker": "...", "titulo": "...", "lede": "..." },
    "...": "..."
  },

  "raio_x_nacional": {
    "exames": [
      { "dominio": "saude", "freq": "anual", "custo": "R$ X",
        "automacao_pct": 85, "urgencia_rotulo": "Emergencia",
        "gap": "Texto do que falta" }
    ]
  },

  "orcamento_publico": { "resumo_geral": {}, "despesas_por_area_2025": [] },
  "trabalho_renda": { "resumo": { "renda_mediana_mensal": "..." } },
  "violencia_detalhada": { "resumo": { "taxa_homicidios_2023": "...", "homicidios_2023": "..." } },
  "comparativo_internacional": { "indicadores": [] },
  "historia_timeline_expandida": { "eventos": [ { "ano": "...", "evento": "..." } ] },

  "mapa_estados": { "AC": { "nome": "...", "populacao": "...", "..." }, "...": {} },

  "dossie_politicos": {
    "metadados": { "data_compilacao": "...", "fonte_principal": "..." },
    "politicos": [
      {
        "nome": "...", "cargo_atual": "...", "partido_atual": "...",
        "estado": "UF",
        "perfil_trajetoria": { "origem": "...", "formacao_academica": "...",
          "filiacoes_partidarias": [], "cargos_publicos": [] },
        "bens_patrimonio": { "evolucao": [], "questionamentos": [] },
        "financiamento_gastos": { "doadores_principais": [], "ceap_verba_gabinete": "...", "glosas_irregularidades": [] },
        "questoes_judiciais_eticas": { "processos_tse_tcu": [], "inqueritos_denuncias": [], "ficha_limpa": "..." },
        "relevancia_imagem_publica": { "polemicas": [], "avaliacao_pesquisas": "..." }
      }
    ]
  },

  "rankings_politicos": {
    "metodologia": { "score_base": "(C1×3 + C2×2 + C3×1) / 6 × 5", "corte": 4 },
    "aprovados": [ { "nome": "...", "score": 4.5, "etiquetas_positivas": [], "etiquetas_negativas": [] } ],
    "em_analise": [ "..." ],
    "bloqueados_exemplo": [ "..." ]
  },

  "carrosseis_instagram": [
    {
      "id": "manifesto", "nome": "MANIFESTO", "cor": "#C00810",
      "tagline": "Frase de efeito", "dados_chave": "Dado principal com fonte",
      "slides": [
        { "tipo": "cover" },
        { "tipo": "content", "pill": "ROTULO", "titulo": "...", "stat": "...",
          "statLabel": "...", "texto": "...", "gap": "Citação" },
        { "tipo": "cta" }
      ]
    }
  ],

  "compartilhamento_whatsapp": [
    { "cat": "categoria", "label": "rótulo", "num": "número",
      "fonte": "fonte oficial", "cor": "#hex" }
  ],

  "manifesto": {}, "requisitos_politico": {}, "propostas_executaveis": {},
  "saude_detalhada": {}, "educacao_detalhada": {}, "direitos_humanos": {},
  "...outras 30 secções temáticas...": {}
}
```

---

## FEATURES ESPECÍFICAS A IMPLEMENTAR

### 1. Carrosséis Instagram (canvas)
Cada carrossel tem 3 tipos de slide:
- **cover**: fundo preto + cor de acento, título grande + tagline + handle
- **content**: pill colorido, título, stat grande, texto, citação, rodapé com handle
- **cta**: pergunta provocadora + convite para seguir o handle

Os slides são renderizados em `<canvas>` 1080×1080 (ou 1080×1350). Download como ZIP (implementação manual do formato ZIP em JS, sem biblioteca externa). O handle (`@`) é customizável e aparece em todos os slides.

### 2. Dossiês de políticos
- Grid de `<details>` accordions (um por político)
- Summary: nome + cargo + badges (partido, UF)
- Body: secções com trajetória, património, financiamento, questões judiciais, etc.
- **Filtro de placeholders**: texto "Dados não disponíveis" não deve aparecer no render
- **Esquema de apoio popular**: políticos candidatos à reeleição com ficha limpa + score ≥ 3.5 no ranking + sem processos reais recebem uma borda verde subtil (`border-left: 3px solid var(--green)`)
- **Contador correcto**: distinguir "detalhados" (têm dados reais em `perfil_trajetoria.origem`) de "em compilação"

### 3. Calculadora de Mais-Valia
Inputs: salário bruto, jornada (horas/dia + dias/semana OU total/mês), valor produzido (direto OU markup %).
Calcula: taxa de mais-valia (%), tempo trabalhado "para si" vs "para o patrão", mais-valia por dia/hora/mês.
Output: barra proporcional, relógio da exploração ("você trabalha para si até as Xh"), grid de números.
Botão partilha copia resumo formatado para clipboard.

### 4. Máquina de mensagens
Para cada tema (carrossel), gera 3 variações de mensagem por canal (WhatsApp, X, Mensagens). O `@` é injetado em todas. Tweets têm truncagem a 280 caracteres com contador. Botões "Copiar" usam `navigator.clipboard` com fallback `execCommand`.

### 5. Áudio TTS
Usa `window.speechSynthesis` com `SpeechSynthesisUtterance`, `lang: 'pt-BR'`, sliders de velocidade (0.5-1.5) e tom (0.5-1.5). Botões Ouvir/Parar.

### 6. Prompts para IA
Gera prompt formatado para pedir roteiro de vídeo (TikTok/YouTube/Reels/X) com: tema, dados, tom, estrutura obrigatória. Salvar/carregar do `localStorage`.

---

## CHECKLIST DE VERIFICAÇÃO

O site gerado deve passar nestes critérios:

- [ ] `index.html` abre sem erros na consola (via servidor estático, não `file://`)
- [ ] JSON carrega via `fetch('dados_api.json')` com fallback gracioso
- [ ] Todos os 13 capítulos renderizam com dados do JSON
- [ ] Capítulos dinâmicos A-K gerados a partir de 30+ secções do JSON
- [ ] Gráficos D3 são responsivos (re-renderizam em resize)
- [ ] Gráficos carregam lazy (IntersectionObserver)
- [ ] Máquina de propaganda: 8 abas funcionais
- [ ] Carrosséis renderizam em canvas e baixam como ZIP
- [ ] `@` sincroniza entre todas as abas da máquina
- [ ] Dossiês: placeholders "Dados não disponíveis" filtrados do output
- [ ] Dossiês: accordions abrem/fechem ao clicar
- [ ] Calculadora de mais-valia calcula correctamente
- [ ] Glossário tem busca textual funcional
- [ ] Mobile-first: layout de 1 coluna em celular, expande em desktop
- [ ] Tema escuro com acento vermelho `#C00810`
- [ ] Sem logos, watermarks, ou marcas de partido único
- [ ] Todo o processamento é client-side (sem upload para servidor)

---

## DADOS

Aqui estão os dados em JSON. Usa este dataset como única fonte de dados do site:

```json
<!-- COLE O JSON AQUI -->
```
