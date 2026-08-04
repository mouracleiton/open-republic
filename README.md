# OpenRepublic

Republica Aberta: repositorio de especificacoes de politicas publicas e
sistemas para o Brasil.

Cada modulo e uma ESPECIFICACAO executavel: o codigo Python (.py) e a
fonte canonica, e o .md e a documentacao human-readable. Nao ha
transpilados -- as especificacoes vivem em uma unica linguagem.

Licenca: CC0 Universal

## Estrutura

```
open-republic/
├── core/                           Modulos do sistema (spec .py + doc .md)
│                                   open_health, open_credit, open_democracy,
│                                   teia_*, open_*, constitutional_*, ...
├── ferramentas/                    Ferramentas (converter.py + howto)
├── teia-terminal/                  TEIA Terminal
├── politicas/                      Politicas publicas
│   ├── propostas/                  Documentos de proposta
│   ├── execucao/                   Planos de execucao (P01-P43)
│   └── polyglot/                   POLITICAS_PUBLICAS_BRASIL em varias linguagens
├── visualizacoes/                  Visualizacoes da divida publica
└── docs/                           Documentacao tecnica
```

## Especificacoes

Cada modulo tem 2 arquivos:
- `.py` -- especificacao canonica (codigo executavel que define enums,
  dataclasses e engine do sistema)
- `.md` -- documentacao do modulo

O .py e a VERDADE. O .md e o RESUMO.

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

## Principios Constitucionais (P1-P10)

- P1: Miseria e crime do sistema, nao falha individual
- P2: Autonomia do corpo
- P6: Acesso universal ao conhecimento
- P8: IA como instrumento, nao substituto humano
- P9: Anti-polarizacao do Estado
- P10: OpenDrone (soberania do espaco aereo civico)
