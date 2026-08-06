# O Brasil em dados

Um retrato editorial do país a partir de dados públicos oficiais de 2024/2025,
dossiês de políticos e uma máquina de propaganda pronta para espalhar.
Site estático, mobile-first, construído com D3.js.

🔗 **Ao vivo:** <https://mouracleiton.github.io/open-republic/>

> Números verificáveis de fontes oficiais, contados em infográficos editoriais.
> Sem opinião: o que a medição conta quando ninguém está olhando.

## O que é

Site de visualização de dados com **9 capítulos editoriais** sobre o Brasil —
distribuição de renda, orçamento público, desigualdade racial, violência por
estado, comparação com a OCDE, uma linha do tempo de 500 anos e dossiês de 525
políticos ativos — mais a seção **OpenRepublic**, renderizada dinamicamente a
partir de 40 seções do JSON, agrupadas em capítulos temáticos (A-I).

Todos os números vêm de fontes públicas oficiais
(IBGE, INEP, DataSUS, SINESP, TSE, CGU, TCU, etc.).

Ao final, a **máquina de propaganda** gera carrosséis para Instagram, mensagens
para WhatsApp, tweets, roteiros de áudio, prompts e dossiês contra — tudo
client-side, sem upload.

## Estrutura

```
open-republic-website/
├── index.html              Página única: 9 capítulos + máquina de propaganda
├── dados_api.json           Dataset unificado (1.4 MB, 42 seções, JSON válido)
├── assets/
│   ├── app.js              Gráficos D3.js (capítulos 1-8) + carregamento de dados
│   ├── carrosseis.js        Definição dos carrosséis de Instagram
│   ├── carousel-site.js     Renderização e download de carrosséis (ZIP)
│   ├── dossies-render.js    Renderiza os 525 dossiês de políticos a partir do JSON
│   ├── machine.js           Máquina de propaganda (WhatsApp, X, áudio, prompts)
│   ├── data-sections.js     Renderiza 40 seções do JSON em capítulos A-I
│   ├── mais-valia.js        Calculadora de mais-valia (Marx)
│   ├── glossario.js         Glossário interativo com busca
│   ├── tutoriais.js         4 tutoriais de organização popular
│   ├── styles.css           Estilos editoriais (tema escuro + vermelho UP)
│   └── up_logo.svg          Logo da Unidade Popular
├── icon.png                Favicon / og:image
├── .gitignore
└── README.md
```

> O dataset `dados_api.json` é versionado no repositório. Se ficar ausente, o
> site usa um bloco de dados de exemplo embutido em `app.js` (`MOCK_DATA`).

## Estrutura de dados

O `dados_api.json` é a **única fonte de dados** do site, com 42 seções
temáticas:

- **Capítulos 1-8**: `raio_x_nacional`, `orcamento_publico`, `trabalho_renda`,
  `mapa_estados`, `violencia_detalhada`, `comparativo_internacional`,
  `dados_para_acao`, `historia_brasil_524_anos`
- **Dossiês**: `dossie_politicos` (525 perfis), `rankings_politicos`,
  `ranking_dinheiro_publico`, `bancadas_parlamentares`, `dados_eleitorais`
- **Seções OpenRepublic** (capítulos A-I): `manifesto`, `requisitos_politico`,
  `frente_comunista_unuda`, `propostas_executaveis`, `saude_detalhada`,
  `educacao_detalhada`, `direitos_humanos`, `moradia_cidades`,
  `ambiente_detalhado`, `reforma_agraria`, `energia_detalhada`,
  `povos_originarios`, `tributacao`, `transporte_mobilidade`, etc.
- **Máquina de propaganda**: `carrosseis_instagram`,
  `compartilhamento_whatsapp`, frases prontas, hashtags, manchetes

Todos os módulos carregam o JSON via `fetch()` e renderizam dinamicamente.

## Capítulos

| # | Capítulo | O que mostra |
|---|----------|--------------|
| 01 | O raio-x do país | 18 domínios vitais, checkup nacional |
| 02 | Para onde vai o dinheiro | Orçamento público por área |
| 03 | A escada da renda | Distribuição de R$ 300 a R$ 25.000 |
| 04 | A cor do abismo | Desigualdade racial nos extremos |
| 05 | A violência por estado | Homicídios por UF |
| 06 | O país no espelho do mundo | Brasil vs. países ricos (OCDE) |
| 07 | Números que gritam | Mosaico filtrável de fatos |
| 08 | A linha do tempo | 500 anos, evento por evento |
| 09 | Dossiês de políticos ativos | 525 perfis (14 detalhados + 511 em compilação) |

Após os 9 capítulos, a seção **OpenRepublic** (capítulos A-I) expande o dataset
em rankings, propostas executáveis, mapa por estado e indicadores detalhados.

## Stack

- **HTML/CSS/JS** — sem build, sem framework
- **D3.js v7** via CDN
- **Fontes**: Inter + Space Grotesk (Google Fonts)
- **Mobile-first** com fallback HTML puro nos gráficos
- **Dados**: 2024/2025, fontes públicas oficiais listadas no rodapé do site

## Como rodar localmente

Não requer build. Como `dados_api.json` é carregado via `fetch()`, use um
servidor local (não `file://`):

```bash
# Python 3
python3 -m http.server 8000

# ou Node
npx serve
```

Depois abra <http://localhost:8000>.

## GitHub Pages

O site é publicado automaticamente a partir do branch `main` (raiz do repo)
via GitHub Pages:

- **Source**: branch `main` / `/`
- **URL**: <https://mouracleiton.github.io/open-republic/>
- **HTTPS**: enforce

Para reconfigurar:

```bash
gh api -X PUT repos/mouracleiton/open-republic/pages \
  -f source[branch]=main -f source[path]=/
```

## Licença

CC0 Universal. Todo o conhecimento aqui é patrimônio público.

```
github.com/mouracleiton/open-republic
```
