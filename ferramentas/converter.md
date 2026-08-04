# Conversor Python -> Portugol

**Arquivo:** `ferramentas/converter.py`

**Descricao:** Conversor de codigo Python para pseudocodigo estruturado em portugues (portugol). Gera arquivos .md (markdown) com o codigo convertido em blocos ```portugol```.

## O que faz

Le todos os arquivos .py do projeto, converte linha-a-linha para portugol usando regex heuristicas, e salva cada um como .md numa pasta de saida.

## Regras de conversao

| Python | Portugol |
|--------|----------|
| `class X(Y):` | `classe X herda de Y:` |
| `def foo(a) -> int:` | `funcao foo(a) retorna int:` |
| `if x:` | `se x entao:` |
| `elif x:` | `senao se x entao:` |
| `else:` | `senao:` |
| `for i in x:` | `para cada i em x:` |
| `while x:` | `enquanto x faca:` |
| `return x` | `retorne x` |
| `x = 5` | `x <- 5` |
| `try:` / `except:` | `tente:` / `capture:` |
| `True` / `False` / `None` | `VERDADEIRO` / `FALSO` / `nulo` |
| `and` / `or` / `not` | `E` / `OU` / `NAO` |
| `# comentario` | `// comentario` |

## Uso

```bash
python3 ferramentas/converter.py
```

Converte todos os .py do projeto. Saida em `portugol/` com a mesma estrutura de diretorios.

## Funcoes principais

- `converter_linha_python_para_portugol(linha)` -- converte 1 linha
- `processar_arquivo(caminho)` -- le .py, retorna .md completo
- `main()` -- percorre todo o projeto, converte tudo

## Dependencias

Nenhuma externa. Apenas stdlib (`os`, `re`).

## Categoria
TOOL
