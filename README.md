# OpenRepublic

Republica Aberta: 130+ modulos de politicas publicas para o Brasil.
Baseada em 116 sistemas, 91.729 linhas de codigo, transpilada para 7 linguagens.

Licenca: CC0 Universal

## Estrutura

```
open-republic/
├── politicas/                      Politicas publicas
│   ├── propostas/                  Documentos de proposta (POLITICAS_PUBLICAS_BRASIL*.md)
│   ├── execucao/                   43 planos de execucao detalhados (P01-P43)
│   ├── polyglot/                   POLITICAS_PUBLICAS_BRASIL em 7 linguagens
│   └── dashboard.html              Visualizador HTML dos planos
├── core/                           116 modulos do sistema (7 linguagens cada)
│                                   open_health, open_credit, open_democracy, ...
│                                   teia_*, open_*, constitutional_*, ...
├── ferramentas/
│   ├── converter.py                Conversor Python -> Portugol
│   └── howto/                      HOWTO_COMPLETO em 7 linguagens
├── teia-terminal/                  TEIA Terminal (main em 7 linguagens)
├── visualizacoes/                  Visualizacoes da divida publica
└── docs/                           Documentacao tecnica
    └── hermes-agent/               Engenharia reversa do Hermes Agent
```

## Linguagens

Cada modulo existe em 7 implementacoes:
- Python (.py)
- C (.c)
- Go (.go)
- Rust (.rs)
- JavaScript (.js)
- Java (.java)
- Markdown (.md) — documentacao do modulo

## As 43 Politicas

| Eixo | Politicas |
|------|-----------|
| Saude | P01-P06 |
| Economia | P07-P11 |
| Educacao | P13-P16 |
| Seguranca | P09, P12, P22-P24 |
| Soberania | P11, P36-P42 |
| Transicao | P43 |

Ver `politicas/execucao/` para planos detalhados de cada uma.
