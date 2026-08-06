# O Brasil em números

Um retrato editorial do país a partir de dados públicos oficiais de 2024/2025.
Site estático, mobile-first, construído com D3.js.

🔗 **Ao vivo:** <https://mouracleiton.github.io/brasilemnumeros/>

> Números verificáveis de fontes oficiais, contados em infográficos editoriais.
> Sem opinião: o que a medição conta quando ninguém está olhando.

## O que é

Site de visualização de dados com 8 capítulos editoriais sobre o Brasil —
distribuição de renda, orçamento público, desigualdade racial, violência por
estado, comparação com a OCDE e uma linha do tempo de 500 anos. Todos os
números vêm de fontes públicas oficiais (IBGE, INEP, DataSUS, SINESP, etc.).

## Estrutura

```
brasilemnumeros/
├── index.html              Página única com 8 capítulos
├── assets/
│   ├── app.js              Lógica + 8 gráficos D3.js (50 KB)
│   └── styles.css          Estilos editoriais (14 KB)
├── dados_api.json           Dataset local (dossiês de políticos + 40 seções)
├── icon.png                Favicon / og:image
├── .gitignore
└── README.md
```

> O dataset `dados_api.json` é versionado no repositório (inclui os dossiês de
> políticos). Se ficar ausente, o site usa um bloco de dados de exemplo embutido
> em `app.js` (`MOCK_DATA`).

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
- **URL**: <https://mouracleiton.github.io/brasilemnumeros/>
- **HTTPS**: enforce

Para reconfigurar:

```bash
gh api -X PUT repos/mouracleiton/brasilemnumeros/pages \
  -f source[branch]=main -f source[path]=/
```

## Licença

CC0 Universal. Todo o conhecimento aqui é patrimônio público.

```
github.com/mouracleiton/brasilemnumeros
```
