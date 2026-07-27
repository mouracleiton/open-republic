#!/usr/bin/env python3
"""
Conversor Python -> Portugol (pseudocodigo estruturado em portugues)
Salva saida em arquivos .md (markdown).
"""

import os
import re

ROOT = "/Users/cleitonmouraloura/Documents/open-republic"
OUT = os.path.join(ROOT, "portugol")


def converter_linha_python_para_portugol(linha: str) -> str:
    """Converte uma linha de Python para portugol (heuristica por linha)."""
    original = linha
    stripped = linha.lstrip()
    indent = linha[: len(linha) - len(stripped)]

    # Linha vazia ou comentario puro
    if not stripped:
        return linha
    if stripped.startswith("#"):
        texto = stripped[1:].strip()
        return f"{indent}// {texto}"

    # docstrings """ ou '''
    if stripped.startswith('"""') or stripped.startswith("'''"):
        conteudo = stripped.replace('"""', '').replace("'''", "")
        return f"{indent}// {conteudo}"

    r = stripped

    # ---- import ----
    m = re.match(r'^from\s+(\S+)\s+import\s+(.+)$', r)
    if m:
        return f"{indent}// importa {m.group(2)} de {m.group(1)}"

    if r.startswith("import "):
        resto = r[len("import "):].rstrip()
        return f"{indent}// importa {resto}"

    # from __future__ ...
    if r.startswith("from __future__"):
        return f"{indent}// diretiva de compatibilidade futura"

    # ---- class definition ----
    m = re.match(r'^class\s+(\w+)\s*\(([^)]*)\)\s*:', r)
    if m:
        base = m.group(2).strip()
        if base:
            return f"{indent}classe {m.group(1)} herda de {base}:"
        return f"{indent}classe {m.group(1)}:"

    m = re.match(r'^class\s+(\w+)\s*:', r)
    if m:
        return f"{indent}classe {m.group(1)}:"

    # ---- def (definicao de funcao/procedimento) ----
    m = re.match(r'^def\s+(\w+)\s*\((.*?)\)\s*(->\s*(.+?))?\s*:', r)
    if m:
        nome = m.group(1)
        params = m.group(2).strip()
        if m.group(4):
            retorno = m.group(4).strip()
            return f"{indent}funcao {nome}({params}) retorna {retorno}:"
        return f"{indent}funcao {nome}({params}):"

    # ---- async def ----
    m = re.match(r'^async\s+def\s+(\w+)\s*\((.*?)\)\s*(->\s*(.+?))?\s*:', r)
    if m:
        nome = m.group(1)
        params = m.group(2).strip()
        if m.group(4):
            return f"{indent}funcao assincrona {nome}({params}) retorna {m.group(4).strip()}:"
        return f"{indent}funcao assincrona {nome}({params}):"

    # ---- decorators ----
    if r.startswith("@"):
        return f"{indent}// decorador: {r}"

    # ---- controle de fluxo ----
    # if / elif / else
    m = re.match(r'^if\s+(.+):\s*$', r)
    if m:
        cond = _traduzir_condicao(m.group(1))
        return f"{indent}se {cond} entao:"

    m = re.match(r'^elif\s+(.+):\s*$', r)
    if m:
        cond = _traduzir_condicao(m.group(1))
        return f"{indent}senao se {cond} entao:"

    if r == "else:" or re.match(r'^else\s*:', r):
        return f"{indent}senao:"

    # for ... in ...
    m = re.match(r'^for\s+(\w+)\s+in\s+(.+):\s*$', r)
    if m:
        var = m.group(1)
        iterable = m.group(2).strip()
        return f"{indent}para cada {var} em {iterable}:"

    # for com unpacking: for a, b in ...
    m = re.match(r'^for\s+(\w+)\s*,\s*(\w+)\s+in\s+(.+):\s*$', r)
    if m:
        return f"{indent}para cada ({m.group(1)}, {m.group(2)}) em {m.group(3).strip()}:"

    # while
    m = re.match(r'^while\s+(.+):\s*$', r)
    if m:
        cond = _traduzir_condicao(m.group(1))
        return f"{indent}enquanto {cond} faca:"

    # ---- try/except/finally ----
    if r == "try:":
        return f"{indent}tente:"

    m = re.match(r'^except\s+(\w+)\s+as\s+(\w+)\s*:', r)
    if m:
        return f"{indent}capture {m.group(1)} como {m.group(2)}:"

    m = re.match(r'^except\s+(\w+)\s*:', r)
    if m:
        return f"{indent}capture {m.group(1)}:"

    m = re.match(r'^except\s*:', r)
    if m:
        return f"{indent}capture qualquer erro:"

    if r == "finally:":
        return f"{indent}finalmente:"

    # with ... as ...
    m = re.match(r'^with\s+(.+?)\s+as\s+(\w+)\s*:', r)
    if m:
        return f"{indent}use {m.group(1).strip()} como {m.group(2)}:"

    m = re.match(r'^with\s+(.+)\s*:', r)
    if m:
        return f"{indent}use {m.group(1).strip()}:"

    # ---- match/case (Python 3.10+) ----
    m = re.match(r'^match\s+(.+):\s*$', r)
    if m:
        return f"{indent}selecione {m.group(1).strip()}:"

    m = re.match(r'^case\s+(.+):\s*$', r)
    if m:
        return f"{indent}caso {m.group(1).strip()}:"

    # ---- comandos simples ----
    if r == "return" or r == "return None":
        return f"{indent}retorne nulo"

    m = re.match(r'^return\s+(.+)$', r)
    if m:
        expr = _traduzir_expressao(m.group(1))
        return f"{indent}retorne {expr}"

    if r in ("break",):
        return f"{indent}interrompa"

    if r in ("continue",):
        return f"{indent}continue"

    if r in ("pass",):
        return f"{indent}// (sem operacao)"

    if r.startswith("raise "):
        exc = r[len("raise "):]
        return f"{indent}lance {exc}"

    if r.startswith("yield "):
        val = r[len("yield "):]
        return f"{indent}produza {val}"

    if r.strip() == "yield":
        return f"{indent}produza"

    if r.startswith("global "):
        return f"{indent}// variavel global: {r[len('global '):]}"

    if r.startswith("nonlocal "):
        return f"{indent}// variavel nao-local: {r[len('nonlocal '):]}"

    if r.startswith("del "):
        return f"{indent}remova {r[len('del '):]}"

    if r.startswith("assert "):
        return f"{indent}afirme {r[len('assert '):]}"

    # ---- atribuicoes tipadas ----
    # variavel: Tipo = valor
    m = re.match(r'^(\w+)\s*:\s*([A-Za-z_][\w\[\], \.]*)\s*=\s*(.+)$', r)
    if m and not r.startswith("elif"):
        nome, tipo, valor = m.group(1), m.group(2), m.group(3)
        valor = _traduzir_expressao(valor)
        return f"{indent}declare {nome}: {tipo} <- {valor}"

    # variavel = valor (atribuicao simples)
    m = re.match(r'^(\w+)\s*\+=\s*(.+)$', r)
    if m:
        return f"{indent}{m.group(1)} <- {m.group(1)} + {_traduzir_expressao(m.group(2))}"

    m = re.match(r'^(\w+)\s*-=\s*(.+)$', r)
    if m:
        return f"{indent}{m.group(1)} <- {m.group(1)} - {_traduzir_expressao(m.group(2))}"

    m = re.match(r'^(\w+)\s*\*=\s*(.+)$', r)
    if m:
        return f"{indent}{m.group(1)} <- {m.group(1)} * {_traduzir_expressao(m.group(2))}"

    m = re.match(r'^(\w+)\s*/=\s*(.+)$', r)
    if m:
        return f"{indent}{m.group(1)} <- {m.group(1)} / {_traduzir_expressao(m.group(2))}"

    # Atribuicao multipla: x = y = 0
    # Atribuicao com tupla: a, b = 1, 2
    m = re.match(r'^([\w,\s]+)\s*=\s*(.+)$', r)
    if m:
        lhs = m.group(1).strip()
        rhs = _traduzir_expressao(m.group(2))
        if "," in lhs:
            return f"{indent}desempacote {lhs} <- {rhs}"
        return f"{indent}{lhs} <- {rhs}"

    # Caso geral: manter a linha quase como esta (expressao / chamada de funcao)
    # mas traduzir operadores logicos
    r_traduzido = _traduzir_expressao(r)

    # Converter comentarios inline # -> //
    # (procurar # que nao esta dentro de string)
    r_final = _converter_comentario_inline(r_traduzido)
    return f"{indent}{r_final}"


def _converter_comentario_inline(linha: str) -> str:
    """Converte # comentario inline -> // comentario, protegendo strings."""
    # Proteger strings
    placeholders = {}

    def _guarda_str(m):
        key = f"__STR{len(placeholders)}__"
        placeholders[key] = m.group(0)
        return key

    protegida = re.sub(r'(["\'])(?:(?=(\\?))\2.)*?\1', _guarda_str, linha)

    # Se nao ha # fora de string, retornar como esta
    idx = protegida.find(" #")
    if idx == -1:
        idx = protegida.find("\t#")
    if idx == -1 and protegida.strip().startswith("#") and not protegida.strip().startswith("#!"):
        # Linha so de comentario
        pass

    # Procurar # que nao seja shebang
    if " #" in protegida:
        partes = protegida.rsplit(" #", 1)
        # Verificar se a parte depois nao esta dentro de string (ja protegida)
        codigo = partes[0]
        comentario = partes[1].strip() if len(partes) > 1 else ""
        resultado = f"{codigo}  // {comentario}"
    else:
        resultado = protegida

    # Restaurar strings
    for key, val in placeholders.items():
        resultado = resultado.replace(key, val)

    return resultado


def _traduzir_condicao(cond: str) -> str:
    """Traduz operadores logicos e comparacoes em condicoes."""
    s = cond
    s = re.sub(r'\band\b', ' E ', s)
    s = re.sub(r'\bor\b', ' OU ', s)
    s = re.sub(r'\bnot\b', 'NAO ', s)
    s = s.replace(" is not None", " nao e nulo")
    s = s.replace(" is None", " e nulo")
    s = s.replace(" is not ", " nao e ")
    s = s.replace(" is ", " e ")
    return s.strip()


def _traduzir_expressao(expr: str) -> str:
    """Traduz operadores e palavras-chave em expressoes."""
    s = expr.strip()
    # NAO substituir dentro de strings -- protege-as
    # Extrair strings
    placeholders = {}
    def _guarda_str(m):
        key = f"__STR{len(placeholders)}__"
        placeholders[key] = m.group(0)
        return key
    s = re.sub(r'(["\'])(?:(?=(\\?))\2.)*?\1', _guarda_str, s)

    # Operadores logicos
    s = re.sub(r'\band\b', ' E ', s)
    s = re.sub(r'\bor\b', ' OU ', s)
    s = re.sub(r'\bnot\b', 'NAO ', s)

    # True / False / None
    s = re.sub(r'\bTrue\b', 'VERDADEIRO', s)
    s = re.sub(r'\bFalse\b', 'FALSO', s)
    s = re.sub(r'\bNone\b', 'nulo', s)

    # is None / is not None
    s = s.replace(" is not None", " nao e nulo")
    s = s.replace(" is None", " e nulo")

    # f-strings -> manter formato
    # lambda
    s = re.sub(r'lambda\s+(\w+)\s*:', r'funcao anonima(\1):', s)

    # Restaurar strings
    for key, val in placeholders.items():
        s = s.replace(key, val)

    return s


def _aplicar_comentario_inline_final(linha: str) -> str:
    """Pos-processa uma linha ja convertida para portugol.
    Converte quaisquer # comentario -> // comentario (protegendo strings)."""
    stripped = linha.lstrip()
    indent = linha[: len(linha) - len(stripped)]

    if not stripped:
        return linha

    # Proteger strings (incluindo f-strings)
    placeholders = {}

    def _guarda_str(m):
        key = f"__STR{len(placeholders)}__"
        placeholders[key] = m.group(0)
        return key

    protegida = re.sub(r'(["\'])(?:(?=(\\?))\2.)*?\1', _guarda_str, stripped)

    # Procurar # que representa comentario inline (espaco antes do #)
    # mas nao dentro de strings (ja protegidas)
    match = re.search(r'\s+#\s', protegida)
    if match:
        pos = match.start()
        codigo = protegida[:pos]
        comentario = protegida[match.end():].strip()
        protegida = f"{codigo}  // {comentario}"

    # Tambem tratar caso: linha so de comentario que escapou (# no inicio)
    # mas ja tratado antes

    # Restaurar strings
    resultado = protegida
    for key, val in placeholders.items():
        resultado = resultado.replace(key, val)

    return f"{indent}{resultado}"


def processar_arquivo(caminho: str) -> str:
    """Le arquivo Python, converte para portugol, retorna conteudo markdown."""
    with open(caminho, "r", encoding="utf-8", errors="replace") as f:
        conteudo = f.read()

    # Extrair nome base sem extensao
    nome_base = os.path.splitext(os.path.basename(caminho))[0]

    # Extrair docstring do topo se houver
    linhas = conteudo.split("\n")
    titulo = nome_base
    descricao = ""

    # Procurar docstring
    docstring_match = re.search(r'("""|\'\'\')(.*?)\1', conteudo, re.DOTALL)
    if docstring_match:
        ds = docstring_match.group(2).strip()
        ds_linhas = ds.split("\n")
        # Primeira linha nao-vazia como titulo
        primeira = ds_linhas[0].strip() if ds_linhas else ""
        if primeira:
            titulo = primeira
        if len(ds_linhas) > 1:
            desc_linhas = [l for l in ds_linhas[1:] if l.strip()]
            descricao = "\n".join(desc_linhas).strip()

    # Montar markdown
    md_parts = []
    md_parts.append(f"# {titulo}\n")
    md_parts.append(f"**Arquivo original:** `{os.path.relpath(caminho, ROOT)}`\n")
    if descricao:
        md_parts.append(f"**Descricao:** {descricao}\n")
    md_parts.append("---\n")
    md_parts.append("```portugol\n")

    # Converter cada linha
    for linha in linhas:
        convertida = converter_linha_python_para_portugol(linha)
        # Aplicar conversao de comentario inline em todas as linhas
        convertida = _aplicar_comentario_inline_final(convertida)
        md_parts.append(convertida)

    md_parts.append("```\n")
    return "\n".join(md_parts)


def main():
    os.makedirs(OUT, exist_ok=True)

    py_files = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        if "portugol" in dirpath:
            continue
        for fn in filenames:
            if fn.endswith(".py"):
                py_files.append(os.path.join(dirpath, fn))
    py_files.sort()

    convertidos = 0
    erros = 0

    for caminho in py_files:
        try:
            md_conteudo = processar_arquivo(caminho)

            # Calcular caminho relativo
            rel = os.path.relpath(caminho, ROOT)
            # Trocar .py por .md
            rel_md = os.path.splitext(rel)[0] + ".md"
            saida = os.path.join(OUT, rel_md)

            os.makedirs(os.path.dirname(saida), exist_ok=True)
            with open(saida, "w", encoding="utf-8") as f:
                f.write(md_conteudo)

            convertidos += 1
        except Exception as e:
            erros += 1
            print(f"ERRO em {caminho}: {e}")

    print(f"\nConvertidos: {convertidos}")
    print(f"Erros: {erros}")
    print(f"Pasta de saida: {OUT}")


if __name__ == "__main__":
    main()
