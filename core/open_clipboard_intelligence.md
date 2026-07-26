# OpenClipboardIntelligence -- Clipboard que Pensa Antes de Colar

**Arquivo original:** `open-republic/core/open_clipboard_intelligence.py`

**Descricao:** =================================================================
"Voce copiou. A IA expandiu. Voce valida. So entao cola."
O PROBLEMA:
  Voce copia "energy.py linha 42" do terminal.
  Vai colar no Discord para pedir ajuda.
  Mas o texto sozinho nao tem CONTEXTO.
  Quem le nao sabe o que e energy.py.
  Voce copia um erro do terminal:
  "Traceback (most recent call last): File ... TypeError"
  Vai colar no issue do GitHub.
  Mas falta: versao do Python, OS, como reproduzir.
  A IA PEGA o clipboard, EXPANDE com contexto, e mostra.
  Voce valida. Se gostou, cola. Se nao, cola o original.
COMO FUNCIONA:
  1. CAPTURA: monitora o clipboard (xclip/wl-clipboard)
  2. CLASSIFICA: o que e? (codigo, erro, URL, texto, comando, numero)
  3. EXPANDE: LLM local (llama.cpp) melhora com contexto
  4. PREVIEW: mostra original vs expandido lado a lado
  5. VALIDA: usuario escolhe (original / expandido / editar)
  6. INJETA: cola o escolhido no campo ativo (xdotool/ydotool)
O LLM NUNCA COLA SOZINHO:
  A IA sempre mostra o preview. Nunca injeta sem validacao.
  O humano e o GATE. A IA e o ASSISTENTE.
6 TIPOS DE CLIPBOARD:
  1. CODIGO: "def foo():..." -> adiciona docstring, type hints, contexto
  2. ERRO/TRACEBACK: "TypeError..." -> adiciona causa provavel + solucao
  3. URL: "republica.local" -> adiciona titulo da pagina + resumo
  4. COMANDO: "sudo apt install X" -> adiciona o que faz + riscos
  5. TEXTO/EMAIL: "bom dia" -> expande para mensagem completa
  6. NUMERO/ID: "42" -> contextualiza (linha? issue? PR?)
Author: OpenRepublic Team

---

```portugol

// !/usr/bin/env python3
// 
OpenClipboardIntelligence -- Clipboard que Pensa Antes de Colar
=================================================================
"Voce copiou. A IA expandiu. Voce valida. So entao cola."

O PROBLEMA:

  Voce copia "energy.py linha 42" do terminal.
  Vai colar no Discord para pedir ajuda.
  Mas o texto sozinho nao tem CONTEXTO.
  Quem le nao sabe o que e energy.py.

  Voce copia um erro do terminal:
  "Traceback (most recent call last): File ... TypeError"
  Vai colar no issue do GitHub.
  Mas falta: versao do Python, OS, como reproduzir.

  A IA PEGA o clipboard, EXPANDE com contexto, e mostra.
  Voce valida. Se gostou, cola. Se nao, cola o original.

COMO FUNCIONA:

  1. CAPTURA: monitora o clipboard (xclip/wl-clipboard)
  2. CLASSIFICA: o que e? (codigo, erro, URL, texto, comando, numero)
  3. EXPANDE: LLM local (llama.cpp) melhora com contexto
  4. PREVIEW: mostra original vs expandido lado a lado
  5. VALIDA: usuario escolhe (original / expandido / editar)
  6. INJETA: cola o escolhido no campo ativo (xdotool/ydotool)

O LLM NUNCA COLA SOZINHO:
  A IA sempre mostra o preview. Nunca injeta sem validacao.
  O humano e o GATE. A IA e o ASSISTENTE.

6 TIPOS DE CLIPBOARD:

  1. CODIGO: "def foo():..." -> adiciona docstring, type hints, contexto
  2. ERRO/TRACEBACK: "TypeError..." -> adiciona causa provavel + solucao
  3. URL: "republica.local" -> adiciona titulo da pagina + resumo
  4. COMANDO: "sudo apt install X" -> adiciona o que faz + riscos
  5. TEXTO/EMAIL: "bom dia" -> expande para mensagem completa
  6. NUMERO/ID: "42" -> contextualiza (linha? issue? PR?)

Author: OpenRepublic Team
// 
// importa annotations de __future__
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa dataclass, field de dataclasses
// importa datetime de datetime
// importa re


// ============================================================================
// 1. ENUMS
// ============================================================================

classe TipoClipboard herda de Enum:
    // Tipos de conteudo detectados no clipboard.
    CODIGO <- ("codigo", "Codigo-fonte (Python, JS, C, etc)")
    ERRO <- ("erro", "Erro / Traceback / excecao")
    URL <- ("url", "URL / link web")
    COMANDO <- ("comando", "Comando de shell/terminal")
    TEXTO <- ("texto", "Texto livre / mensagem / email")
    NUMERO <- ("numero", "Numero / ID / referencia")
    JSON <- ("json", "JSON / dados estruturados")
    PATH <- ("path", "Caminho de arquivo")
    VAZIO <- ("vazio", "Clipboard vazio")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe StatusExpansao herda de Enum:
    // Status do processamento do clipboard.
    CAPTURADO <- ("capturado", "Capturado: clipboard lido")
    CLASSIFICADO <- ("classificado", "Classificado: tipo detectado")
    EXPANDIDO <- ("expandido", "Expandido: LLM melhorou")
    VALIDADO <- ("validado", "Validado: usuario aprovou")
    REJEITADO <- ("rejeitado", "Rejeitado: usuario quer original")
    EDITADO <- ("editado", "Editado: usuario modificou antes de colar")
    INJETADO <- ("injetado", "Injetado: colado no campo ativo")
    ERRO_LLM <- ("erro_llm", "Erro: LLM falhou, usar original")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe EscolhaUsuario herda de Enum:
    // O que o usuario escolhe no preview.
    USAR_EXPANDIDO <- ("expandido", "Usar versao expandida pela IA")
    USAR_ORIGINAL <- ("original", "Usar original (ignorar expansao)")
    EDITAR <- ("editar", "Editar manualmente antes de colar")
    CANCELAR <- ("cancelar", "Cancelar (nao colar nada)")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe ContextoDestino herda de Enum:
    // Onde o clipboard vai ser colado (detectado pela janela ativa).
    TERMINAL <- ("terminal", "Terminal (GNOME Terminal, kitty)")
    EDITOR <- ("editor", "Editor (VS Code, vim, nano)")
    NAVEGADOR <- ("navegador", "Navegador (Firefox, Chrome)")
    CHAT <- ("chat", "Chat (Discord, Slack, Telegram)")
    EMAIL <- ("email", "Email (Thunderbird, webmail)")
    ISSUE <- ("issue", "Issue/PR (GitHub, GitLab)")
    MENSAGEM <- ("mensagem", "Mensagem (WhatsApp, Signal)")
    DESCONHECIDO <- ("desconhecido", "Destino desconhecido")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


// ============================================================================
// 2. DATACLASSES
// ============================================================================

// decorador: @dataclass
classe ItemClipboard:
    // Um item capturado do clipboard.
    id: str
    texto_original: str
    timestamp: str
    declare tipo: TipoClipboard  <- TipoClipboard.TEXTO
    declare destino: ContextoDestino  <- ContextoDestino.DESCONHECIDO
    declare texto_expandido: str  <- ""
    declare status: StatusExpansao  <- StatusExpansao.CAPTURADO
    declare escolha: Optional[EscolhaUsuario]  <- nulo
    declare texto_final: str  <- ""  // o que foi realmente colado
    declare tokens_llm: int  <- 0
    declare latencia_ms: float  <- 0.0


// decorador: @dataclass
classe ConfigClipboardIntel:
    // Configuracao do sistema de clipboard inteligente.
    declare ativo: bool  <- VERDADEIRO
    declare llm_modelo: str  <- "llama-3.2-3b-instruct"  // modelo local
    declare llm_host: str  <- "localhost:8080"  // llama.cpp server
    declare auto_preview: bool  <- VERDADEIRO  // mostrar preview automaticamente
    declare max_tokens_expansao: int  <- 500
    declare temperatura: float  <- 0.3  // baixa = mais conservador
    declare historico_tamanho: int  <- 50
    // o que expandir (ligar/desligar por tipo)
    declare expandir_codigo: bool  <- VERDADEIRO
    declare expandir_erro: bool  <- VERDADEIRO
    declare expandir_url: bool  <- VERDADEIRO
    declare expandir_comando: bool  <- VERDADEIRO
    declare expandir_texto: bool  <- VERDADEIRO
    declare expandir_numero: bool  <- FALSO  // numero sozinho raramente precisa
    // atalho para validar
    declare atalho_preview: str  <- "Super+Shift+V"  // segurar para ver preview
    declare atalho_aceitar: str  <- "Return"  // aceitar expandido
    declare atalho_rejeitar: str  <- "Escape"  // rejeitar, usar original
    declare atalho_editar: str  <- "Super+E"  // editar antes de colar


// ============================================================================
// 3. CLASSIFICADOR DE CLIPBOARD
// ============================================================================

classe ClassificadorClipboard:
    // Detecta o tipo de conteudo no clipboard.

    // decorador: @staticmethod
    funcao classificar(texto: str) retorna TipoClipboard:
        se NAO  texto  OU  NAO  texto.strip() entao:
            retorne TipoClipboard.VAZIO

        texto_strip <- texto.strip()

        // URL
        se re.match(r'^https?://', texto_strip)  OU  re.match(r'^www\.', texto_strip) entao:
            retorne TipoClipboard.URL
        se re.match(r'^[a-z0-9-]+\.(com|org|net|gov\.br|io|dev)$', texto_strip, re.I) entao:
            retorne TipoClipboard.URL

        // Path de arquivo
        se re.match(r'^[/~]', texto_strip)  E  '/' in texto_strip entao:
            if any(texto_strip.endswith(ext) for ext in
                   ['.py', '.js', '.c', '.go', '.rs', '.java', '.md', '.txt',
                    '.json', '.yaml', '.yml', '.csv', '.html', '.css']):
                retorne TipoClipboard.PATH

        // JSON
        se texto_strip.startswith('{')  E  texto_strip.endswith('}') entao:
            retorne TipoClipboard.JSON
        se texto_strip.startswith('[')  E  texto_strip.endswith(']') entao:
            retorne TipoClipboard.JSON

        // Erro/Traceback
        if any(kw in texto_strip for kw in
               ['Traceback', 'Error:', 'Exception', 'TypeError', 'ValueError',
                'KeyError', 'ImportError', 'AttributeError', 'RuntimeError',
                'command not found', 'No such file', 'Permission denied',
                'syntax error', 'SEGFAULT', 'Segmentation fault']):
            retorne TipoClipboard.ERRO

        // Comando shell
        primeira_linha <- texto_strip.split('\n')[0]
        if re.match(r'^(sudo\s+)?(apt|pip|npm|git|cd|ls|cp|mv|rm|mkdir|chmod|chown|'
                    r'curl|wget|ssh|scp|docker|kubectl|systemctl|nmap|ping|grep|'
                    r'find|cat|echo|export|source|python|node|rustc|gcc|make)\b',
                    primeira_linha):
            retorne TipoClipboard.COMANDO

        // Codigo-fonte
        if any(kw in texto_strip for kw in
               ['def ', 'function ', 'class ', 'import ', 'from ', 'const ',
                'let ', 'var ', 'public ', 'private ', 'fn ', 'struct ',
                '#include', 'package ']):
            retorne TipoClipboard.CODIGO
        // indentacao consistente (4 espacos) = provavel codigo
        linhas <- texto_strip.split('\n')
        se len(linhas) > 2 entao:
            indentadas <- sum(1 for l in linhas if l.startswith('    '))
            se indentadas / len(linhas) > 0.3 entao:
                retorne TipoClipboard.CODIGO

        // Numero puro
        se re.match(r'^[\d-]+$', texto_strip)  E  len(texto_strip) < 20 entao:
            retorne TipoClipboard.NUMERO

        // Texto livre (default)
        retorne TipoClipboard.TEXTO


// ============================================================================
// 4. EXPANSOR LLM (simulado)
// ============================================================================

classe ExpansorLLM:
    // 
    Expande o texto do clipboard com contexto usando LLM local.
    No mundo real: chamada HTTP para llama.cpp server (localhost:8080).
    Aqui: simulacao deterministica por tipo.
    // 

    // decorador: @staticmethod
    def expandir(
        texto: str,
        tipo: TipoClipboard,
        destino: ContextoDestino,
    ) -> Tuple[str, int, float]:
        // 
        Expande o texto. Retorna (texto_expandido, tokens, latencia_ms).
        // 
        tokens <- 0
        latencia <- 0.0

        se tipo == TipoClipboard.CODIGO entao:
            retorne ExpansorLLM._expandir_codigo(texto, destino)
        senao se tipo == TipoClipboard.ERRO entao:
            retorne ExpansorLLM._expandir_erro(texto, destino)
        senao se tipo == TipoClipboard.URL entao:
            retorne ExpansorLLM._expandir_url(texto, destino)
        senao se tipo == TipoClipboard.COMANDO entao:
            retorne ExpansorLLM._expandir_comando(texto, destino)
        senao se tipo == TipoClipboard.TEXTO entao:
            retorne ExpansorLLM._expandir_texto(texto, destino)
        senao se tipo == TipoClipboard.JSON entao:
            retorne ExpansorLLM._expandir_json(texto, destino)
        senao se tipo == TipoClipboard.PATH entao:
            retorne ExpansorLLM._expandir_path(texto, destino)
        senao:
            retorne texto, 0, 0.0

    // decorador: @staticmethod
    funcao _expandir_codigo(texto: str, destino: ContextoDestino) retorna Tuple[str, int, float]:
        // Expande codigo adicionando docstring e contexto.
        // se ja tem docstring, nao adiciona
        se '"""' in texto  OU  "'''" in texto entao:
            retorne texto, 0, 0.0

        // se destino e chat/issue, formata como bloco de codigo
        if destino in (ContextoDestino.CHAT, ContextoDestino.ISSUE,
                       ContextoDestino.MENSAGEM):
            linguagem <- ExpansorLLM._detectar_linguagem(texto)
            expandido <- (
                f"```{linguagem}\n{texto}\n```\n\n"
                f"_Trecho de codigo compartilhado da Republica._"
            )
            retorne expandido, len(expandido) // 4, 350.0

        // se destino e editor, adiciona docstring
        se destino == ContextoDestino.EDITOR entao:
            linhas <- texto.strip().split('\n')
            primeira <- linhas[0] if linhas else ""
            // extrair nome da funcao/classe
            match <- re.match(r'def\s+(\w+)', primeira)
            nome_func <- match.group(1) if match else "funcao"
            docstring <- f'    """TODO: documentar {nome_func}."""\n'
            expandido <- primeira + "\n" + docstring + "\n".join(linhas[1:])
            retorne expandido, 45, 280.0

        retorne texto, 0, 0.0

    // decorador: @staticmethod
    funcao _expandir_erro(texto: str, destino: ContextoDestino) retorna Tuple[str, int, float]:
        // Expande erro adicionando causa provavel e contexto do sistema.
        // detectar tipo de erro
        causa <- "Erro detectado."
        solucao <- ""

        se 'TypeError' in texto entao:
            causa <- "TypeError: tipo de dado incorreto passado para uma funcao."
            solucao <- "Verifique os tipos dos argumentos. Use type() para debug."
        senao se 'KeyError' in texto entao:
            causa <- "KeyError: chave inexistente em dicionario."
            solucao <- "Use dict.get(chave, default) ou verifique 'chave in dict'."
        senao se 'ImportError' in texto entao:
            causa <- "ImportError: modulo nao encontrado."
            solucao <- "Verifique: pip install <modulo> ou caminho do PYTHONPATH."
        senao se 'command NAO  found' in texto entao:
            causa <- "Comando nao encontrado no sistema."
            solucao <- "Verifique: sudo apt install <pacote> ou alias."
        senao se 'Permission denied' in texto entao:
            causa <- "Sem permissao de acesso."
            solucao <- "Tente: sudo, ou chmod/chown no arquivo."
        senao se 'No such file' in texto entao:
            causa <- "Arquivo ou diretorio nao existe."
            solucao <- "Verifique o caminho com ls ou pwd."

        contexto_sistema <- (
            f"\n-- Contexto --\n"
            f"Python: 3.11 | OS: RepublicaOS (Kali/Debian) | Kernel: Linux 6.x\n"
        )

        se destino in (ContextoDestino.ISSUE, ContextoDestino.CHAT) entao:
            expandido <- (
                f"## Erro ao executar\n\n"
                f"```\n{texto}\n```\n\n"
                f"**Causa provavel:** {causa}\n"
                f"**Solucao sugerida:** {solucao}\n"
                f"{contexto_sistema}"
            )
        senao:
            expandido <- f"{texto}\n\n# Causa: {causa}\n# Solucao: {solucao}"

        retorne expandido, len(expandido) // 4, 420.0

    // decorador: @staticmethod
    funcao _expandir_url(texto: str, destino: ContextoDestino) retorna Tuple[str, int, float]:
        // Expande URL adicionando titulo e resumo (simulado).
        se destino in (ContextoDestino.CHAT, ContextoDestino.ISSUE) entao:
            expandido <- (
                f"[Republica Aberta - Documentacao]({texto})\n\n"
                f"Site oficial da Republica com docs, foruns e downloads."
            )
            retorne expandido, 25, 500.0  // 500ms = buscar titulo da pagina
        retorne texto, 0, 0.0

    // decorador: @staticmethod
    funcao _expandir_comando(texto: str, destino: ContextoDestino) retorna Tuple[str, int, float]:
        // Expande comando explicando o que faz.
        explicacoes <- {
            'apt install': 'Instala pacote do repositorio APT.',
            'pip install': 'Instala pacote Python do PyPI.',
            'npm install': 'Instala pacote Node.js do npm.',
            'git clone': 'Clona repositorio Git remoto.',
            'git push': 'Envia commits locais para repositorio remoto.',
            'sudo': 'Executa com privilegios de administrador.',
            'chmod': 'Altera permissoes de arquivo.',
            'systemctl': 'Controla servico do systemd.',
            'nmap': 'Escaneia rede/portas.',
            'curl': 'Faz requisicao HTTP.',
        }
        explicacao <- "Comando de terminal."
        para cada (cmd, desc) em explicacoes.items():
            se cmd in texto entao:
                explicacao <- desc
                interrompa

        se destino == ContextoDestino.CHAT entao:
            expandido <- f"`{texto}`\n\n_{explicacao}_"
            retorne expandido, 20, 200.0
        retorne texto, 0, 0.0

    // decorador: @staticmethod
    funcao _expandir_texto(texto: str, destino: ContextoDestino) retorna Tuple[str, int, float]:
        // Expande texto curto em mensagem completa.
        texto_lower <- texto.lower().strip()

        // templates de expansao por destino
        se destino == ContextoDestino.EMAIL entao:
            se 'bom dia' in texto_lower entao:
                expandido <- (
                    "Bom dia,\n\n"
                    "Espero que esteja bem.\n\n"
                    "[conteudo da mensagem]\n\n"
                    "Atenciosamente,\n[seu nome]"
                )
                retorne expandido, 40, 300.0
            se 'obrigado' in texto_lower entao:
                expandido <- (
                    "Muito obrigado pela atencao.\n\n"
                    "Fico a disposicao caso precise de mais informacoes.\n\n"
                    "Atenciosamente,\n[seu nome]"
                )
                retorne expandido, 30, 280.0

        se destino == ContextoDestino.CHAT entao:
            se len(texto) < 20 entao:
                expandido <- texto + " (mais detalhes: pode explicar melhor?)"
                retorne expandido, 15, 200.0

        se destino == ContextoDestino.ISSUE entao:
            expandido <- (
                f"## {texto}\n\n"
                f"### Comportamento esperado\n[descreva]\n\n"
                f"### Comportamento atual\n[descreva]\n\n"
                f"### Passos para reproduzir\n1. \n2. \n3.\n"
            )
            retorne expandido, 60, 350.0

        retorne texto, 0, 0.0

    // decorador: @staticmethod
    funcao _expandir_json(texto: str, destino: ContextoDestino) retorna Tuple[str, int, float]:
        // Formata JSON (pretty print) para leitura.
        // importa json as json_mod
        tente:
            obj <- json_mod.loads(texto)
            expandido <- json_mod.dumps(obj, indent=2, ensure_ascii=FALSO)
            se destino in (ContextoDestino.CHAT, ContextoDestino.ISSUE) entao:
                expandido <- f"```json\n{expandido}\n```"
            retorne expandido, len(expandido) // 4, 100.0
        capture Exception:
            retorne texto, 0, 0.0

    // decorador: @staticmethod
    funcao _expandir_path(texto: str, destino: ContextoDestino) retorna Tuple[str, int, float]:
        // Expande caminho de arquivo.
        se destino == ContextoDestino.CHAT entao:
            arquivo <- texto.split('/')[-1]
            expandido <- f"Arquivo: `{texto}` ({arquivo})"
            retorne expandido, 15, 150.0
        retorne texto, 0, 0.0

    // decorador: @staticmethod
    funcao _detectar_linguagem(texto: str) retorna str:
        // Detecta linguagem do codigo para syntax highlight.
        se 'def ' in texto  OU  'import ' in texto entao:
            retorne "python"
        se 'function ' in texto  OU  'const ' in texto entao:
            retorne "javascript"
        se '#include' in texto entao:
            retorne "c"
        se 'fn ' in texto entao:
            retorne "rust"
        se 'func ' in texto entao:
            retorne "go"
        se 'public class' in texto entao:
            retorne "java"
        retorne "text"


// ============================================================================
// 5. ENGINE
// ============================================================================

classe ClipboardIntelligenceEngine:
    // Motor de clipboard inteligente.

    funcao __init__(self, config: Optional[ConfigClipboardIntel] = None) retorna None:
        self.config = config  OU  ConfigClipboardIntel()
        self.historico: List[ItemClipboard] = []
        self.classificador = ClassificadorClipboard()
        self.expansor = ExpansorLLM()
        self._counter = 0

    // -- capturar clipboard ------------------------------------------------

    def capturar(
        self,
        texto: str,
        declare destino: ContextoDestino  <- ContextoDestino.DESCONHECIDO,
    ) -> ItemClipboard:
        // Captura texto do clipboard e processa.
        self._counter += 1
        item <- ItemClipboard(
            id <- f"CLIP-{self._counter:04d}",
            texto_original <- texto,
            timestamp <- datetime.now().isoformat(),
            destino <- destino,
        )

        // classificar
        item.tipo = self.classificador.classificar(texto)
        item.status = StatusExpansao.CLASSIFICADO

        se item.tipo == TipoClipboard.VAZIO entao:
            retorne item

        // verificar se deve expandir este tipo
        deve_expandir <- self._deve_expandir(item.tipo)
        se NAO  deve_expandir entao:
            item.texto_expandido = texto
            item.status = StatusExpansao.EXPANDIDO
            retorne item

        // expandir com LLM
        desempacote expandido, tokens, latencia <- self.expansor.expandir(
            texto, item.tipo, destino
        )
        item.texto_expandido = expandido
        item.tokens_llm = tokens
        item.latencia_ms = latencia
        item.status = StatusExpansao.EXPANDIDO

        self.historico.append(item)
        retorne item

    funcao _deve_expandir(self, tipo: TipoClipboard) retorna bool:
        // Verifica se o tipo deve ser expandido.
        mapa <- {
            TipoClipboard.CODIGO: self.config.expandir_codigo,
            TipoClipboard.ERRO: self.config.expandir_erro,
            TipoClipboard.URL: self.config.expandir_url,
            TipoClipboard.COMANDO: self.config.expandir_comando,
            TipoClipboard.TEXTO: self.config.expandir_texto,
            TipoClipboard.NUMERO: self.config.expandir_numero,
            TipoClipboard.JSON: VERDADEIRO,
            TipoClipboard.PATH: VERDADEIRO,
        }
        retorne mapa.get(tipo, FALSO)

    // -- preview -----------------------------------------------------------

    funcao gerar_preview(self, item: ItemClipboard) retorna str:
        // Gera o preview visual: original vs expandido.
        se item.texto_expandido == item.texto_original entao:
            retorne f"[SEM EXPANSAO] {item.texto_original[:100]}"

        linhas <- [
            f"┌─ Clipboard Intelligence ──────────────────────────┐",
            f"│ Tipo: {item.tipo.id:<12}  Destino: {item.destino.id:<16} │",
            f"├─ ORIGINAL ────────────────────────────────────────┤",
        ]
        para cada linha em item.texto_original.split('\n')[:5]:
            linhas.append(f"│ {linha[:48]:<48} │")
        se len(item.texto_original.split('\n')) > 5 entao:
            linhas.append(f"│ {'... (truncado)':<48} │")
        linhas.append(f"├─ EXPANDIDO PELA IA ({item.tokens_llm} tokens, {item.latencia_ms:.0f}ms) ──────┤")
        para cada linha em item.texto_expandido.split('\n')[:8]:
            linhas.append(f"│ {linha[:48]:<48} │")
        se len(item.texto_expandido.split('\n')) > 8 entao:
            linhas.append(f"│ {'... (' + str(len(item.texto_expandido.split(chr(10))) - 8) + ' linhas)':<48} │")
        linhas.append(f"├─ ESCOLHA ─────────────────────────────────────────┤")
        linhas.append(f"│ [Enter] Expandido  [Esc] Original  [Super+E] Editar │")
        linhas.append(f"└───────────────────────────────────────────────────┘")
        retorne "\n".join(linhas)

    // -- validar (escolha do usuario) --------------------------------------

    def validar(self, item: ItemClipboard, escolha: EscolhaUsuario,
                declare texto_editado: str  <- "") -> ItemClipboard:
        // Processa a escolha do usuario.
        item.escolha = escolha

        se escolha == EscolhaUsuario.USAR_EXPANDIDO entao:
            item.texto_final = item.texto_expandido
            item.status = StatusExpansao.VALIDADO
        senao se escolha == EscolhaUsuario.USAR_ORIGINAL entao:
            item.texto_final = item.texto_original
            item.status = StatusExpansao.REJEITADO
        senao se escolha == EscolhaUsuario.EDITAR entao:
            item.texto_final = texto_editado  OU  item.texto_expandido
            item.status = StatusExpansao.EDITADO
        senao se escolha == EscolhaUsuario.CANCELAR entao:
            item.texto_final = ""
            item.status = StatusExpansao.REJEITADO

        retorne item

    // -- injetar (colar) ---------------------------------------------------

    funcao injetar(self, item: ItemClipboard) retorna str:
        // Simula a injecao do texto final no campo ativo.
        se NAO  item.texto_final entao:
            retorne "Nada para colar (cancelado)."
        item.status = StatusExpansao.INJETADO
        // no mundo real: xdotool type / ydotool / wl-copy
        retorne f"[COLADO] {item.texto_final[:60]}..."

    // -- estatisticas -------------------------------------------------------

    funcao scorecard(self) retorna Dict[str, Any]:
        total <- len(self.historico)
        validados <- sum(1 for i in self.historico if i.status == StatusExpansao.VALIDADO)
        rejeitados <- sum(1 for i in self.historico if i.status == StatusExpansao.REJEITADO)
        editados <- sum(1 for i in self.historico if i.status == StatusExpansao.EDITADO)
        retorne {
            "tipos_clipboard": len(list(TipoClipboard)),
            "destinos": len(list(ContextoDestino)),
            "historico_total": total,
            "aceitos_expansao": validados,
            "rejeitados_original": rejeitados,
            "editados_manual": editados,
            "taxa_aceitacao": f"{validados}/{total}" if total > 0 else "0/0",
            "tokens_llm_total": sum(i.tokens_llm for i in self.historico),
        }


// ============================================================================
// 6. DEMO
// ============================================================================

funcao _demo() retorna None:
    e <- ClipboardIntelligenceEngine()

    print("=" * 70)
    print("OpenClipboardIntelligence -- Clipboard que Pensa Antes de Colar")
    print("=" * 70)

    print(f"""
O FLUXO:
  1. Voce COPIA algo (Ctrl+C)
  2. A IA CLASSIFICA (codigo? erro? URL? comando?)
  3. A IA EXPANDE com contexto (LLM local, llama.cpp)
  4. PREVIEW aparece: original vs expandido
  5. Voce VALIDA:
     [Enter] = usar expandido
     [Esc] = usar original
     [Super+E] = editar antes
  6. SO ENTAO cola no campo ativo

  A IA NUNCA cola sozinha. O humano e o GATE.
// )

    // --- Cenario 1: Codigo no chat ---
    print("=" * 70)
    print("[CENARIO 1] Copiou CODIGO -> vai colar no DISCORD (chat)")
    print("=" * 70)
    item1 <- e.capturar(
        "def calcular_energia(consumo, perda):\n    return consumo - perda",
        destino <- ContextoDestino.CHAT
    )
    print(f"\n  Tipo: {item1.tipo.id}")
    print(f"  Original:\n    {item1.texto_original[:80]}")
    print(f"\n  Expandido:\n    {item1.texto_expandido[:120]}")
    print(f"\n{e.gerar_preview(item1)}")
    // validar
    item1 <- e.validar(item1, EscolhaUsuario.USAR_EXPANDIDO)
    print(f"\n  Escolha: {item1.escolha.rotulo}")
    print(f"  {e.injetar(item1)}")

    // --- Cenario 2: Erro no issue ---
    print("\n" + "=" * 70)
    print("[CENARIO 2] Copiou ERRO -> vai colar no GITHUB ISSUE")
    print("=" * 70)
    item2 <- e.capturar(
        "Traceback (most recent call last):\n  File 'main.py', line 42\n"
        "TypeError: unsupported operand type(s) for +: 'int' and 'str'",
        destino <- ContextoDestino.ISSUE
    )
    print(f"\n  Tipo: {item2.tipo.id}")
    print(f"\n{e.gerar_preview(item2)}")
    item2 <- e.validar(item2, EscolhaUsuario.USAR_EXPANDIDO)
    print(f"\n  Escolha: {item2.escolha.rotulo}")
    print(f"  {e.injetar(item2)}")

    // --- Cenario 3: Texto curto no email ---
    print("\n" + "=" * 70)
    print("[CENARIO 3] Copiou 'bom dia' -> vai colar no EMAIL")
    print("=" * 70)
    item3 <- e.capturar("bom dia", destino=ContextoDestino.EMAIL)
    print(f"\n  Tipo: {item3.tipo.id}")
    print(f"\n{e.gerar_preview(item3)}")

    // --- Cenario 4: Comando no chat ---
    print("\n" + "=" * 70)
    print("[CENARIO 4] Copiou COMANDO -> vai colar no CHAT")
    print("=" * 70)
    item4 <- e.capturar("sudo apt install firefox", destino=ContextoDestino.CHAT)
    print(f"\n  Tipo: {item4.tipo.id}")
    print(f"\n{e.gerar_preview(item4)}")

    // --- Cenario 5: Usuario REJEITA expansao ---
    print("\n" + "=" * 70)
    print("[CENARIO 5] Usuario REJEITA expansao (quer original)")
    print("=" * 70)
    item5 <- e.capturar("def foo():\n    pass", destino=ContextoDestino.CHAT)
    print(f"\n  Tipo: {item5.tipo.id}")
    print(f"  Original: {item5.texto_original}")
    print(f"  Expandido: {item5.texto_expandido[:80]}...")
    item5 <- e.validar(item5, EscolhaUsuario.USAR_ORIGINAL)
    print(f"\n  Escolha: {item5.escolha.rotulo}")
    print(f"  {e.injetar(item5)}")

    // --- Cenario 6: Usuario EDITA ---
    print("\n" + "=" * 70)
    print("[CENARIO 6] Usuario EDITA antes de colar")
    print("=" * 70)
    item6 <- e.capturar("TypeError no main.py", destino=ContextoDestino.ISSUE)
    item6 <- e.validar(item6, EscolhaUsuario.EDITAR,
                      texto_editado <- "TypeError no main.py linha 42 ao processar energia")
    print(f"  Escolha: {item6.escolha.rotulo}")
    print(f"  Texto editado: {item6.texto_final}")
    print(f"  {e.injetar(item6)}")

    // --- Cenario 7: JSON ---
    print("\n" + "=" * 70)
    print("[CENARIO 7] Copiou JSON compacto -> formata (pretty print)")
    print("=" * 70)
    item7 <- e.capturar('{"nome":"Republica","versao":"2026.07","modulos":140}',
                       destino <- ContextoDestino.CHAT)
    print(f"\n  Tipo: {item7.tipo.id}")
    print(f"  Original: {item7.texto_original}")
    print(f"  Expandido:\n{item7.texto_expandido}")

    // --- Cenario 8: URL ---
    print("\n" + "=" * 70)
    print("[CENARIO 8] Copiou URL -> expande com titulo e descricao")
    print("=" * 70)
    item8 <- e.capturar("https://republica.local/docs", destino=ContextoDestino.CHAT)
    print(f"\n  Tipo: {item8.tipo.id}")
    print(f"\n{e.gerar_preview(item8)}")

    // --- Classificador em acao ---
    print("\n[TESTE DO CLASSIFICADOR]")
    testes_class <- [
        ("def foo(): pass", TipoClipboard.CODIGO),
        ("Traceback (most recent call last)", TipoClipboard.ERRO),
        ("https://google.com", TipoClipboard.URL),
        ("sudo apt update", TipoClipboard.COMANDO),
        ("bom dia pessoal", TipoClipboard.TEXTO),
        ("42", TipoClipboard.NUMERO),
        ('{"key": "value"}', TipoClipboard.JSON),
        ("~/Documentos/projeto/main.py", TipoClipboard.PATH),
        ("", TipoClipboard.VAZIO),
    ]
    para cada (texto, esperado) em testes_class:
        detectado <- ClassificadorClipboard.classificar(texto)
        ok <- "OK" if detectado == esperado else "FAIL"
        display <- texto[:30] if texto else "(vazio)"
        print(f"  [{ok}] '{display}' -> {detectado.id} (esperado: {esperado.id})")

    // --- Scorecard ---
    print(f"\n[SCORECARD]")
    sc <- e.scorecard()
    para cada (k, v) em sc.items():
        print(f"  {k:.<28} {v}")

    // --- Pipeline tecnico ---
    print(f"\n[PIPELINE TECNICO]")
    print("""
  1. MONITOR DE CLIPBOARD:
     Wayland: wl-paste --watch (monitora mudancas)
     X11: xclip -o em loop ou xsel
     Python: pyperclip ou biblioteca clipboard

  2. DETECCAO DE DESTINO (janela ativa):
     xdotool getactivewindow getwindowname -> "Discord"
     Mapeia para ContextoDestino (CHAT, EDITOR, ISSUE...)

  3. CLASSIFICACAO (regex + heuristicas):
     Detecta: codigo, erro, URL, comando, texto, JSON, path, numero

  4. EXPANSAO LLM (llama.cpp server localhost:8080):
     POST /completions
     {
       "model": "llama-3.2-3b-instruct",
       "prompt": "Expanda este texto com contexto: ...",
       "max_tokens": 500,
       "temperature": 0.3,
       "stream": false
     }
     Latencia: 200-500ms (local, sem nuvem)

  5. PREVIEW (overlay GTK / layer-shell Wayland):
     Janela flutuante mostra: original | expandido
     declare Atalhos: Enter <- expandido, Esc=original, Super+E=editar

  6. INJECAO (colar no campo ativo):
     Wayland: wtype ou ydotool
     X11: xdotool type --delay 0
     Ou: wl-copy (substitui clipboard) + Ctrl+V simulado
// )

    // --- Filosofia ---
    print(f"{'='*70}")
    print(f"FILOSOFIA -- A IA sugere. O humano decide.")
    print(f"{'='*70}")
    print("""
O PRINCIPIO DO GATE HUMANO:

  A IA processa o clipboard. Mas NUNCA cola sozinha.
  Sempre mostra o preview. O humano valida.
  Enter <- aceita. Esc = rejeita. Super+E = edita.

  Isto e P8 (IA = instrumento, nao autor).
  A IA nao age POR voce. age COM voce.
  A decisao final e SEMPRE sua.

POR QUE EXPANDIR:

  Clipboard cru e sem contexto.
  "def foo(): pass" nao significa nada para quem le no chat.
  A IA adiciona: bloco de codigo, linguagem, descricao.

  "TypeError" sozinho nao ajuda num issue.
  A IA adiciona: causa provavel, solucao, contexto do sistema.

  "bom dia" num email e comico de curto.
  A IA expande para: saudacao + espaco para conteudo + assinatura.

  A expansao nao SUBSTITUI o original.
  Ela OFERECE uma versao melhor. Voce decide.

POR QUE LOCAL (llama.cpp):

  O clipboard contem DADOS PRIVADOS.
  Senhas (se copiou), codigos, mensagens, tokens.
  Enviar para GPT-4/Claude = VAZAMENTO.
  llama.cpp roda em localhost. Dados nao saem do PC.

  Latencia: 200-500ms (local). Aceitavel para clipboard.
  Modelo: 3B params roda em CPU. 8B precisa de GPU.

A INTEGRACAO COM A IARA:

  Quando o usuario pressiona Super+Shift+V:
  Iara mostra o overlay: "Clipboard capturado. Expandido pela IA."
  "Quer usar a versao expandida?"
  Usuario: "Sim." -> Iara cola.
  Usuario: "Nao." -> Iara cola original.

  Para cego: Iara le o original e o expandido em voz alta.
  "Original: def foo pass. Expandido: bloco de codigo Python. Quer qual?"

  Para surdo: overlay mostra os dois lado a lado.
  Para tetrapregico: escolhe por voz. "Usar expandido."

O CLIPBOARD E O MALOTE:

  O clipboard e como um malote que passa informacao entre apps.
  O OpenClipboardIntelligence e a ALFANDEGA.
  Inspeciona. Melhora. Cobra imposto de contexto.
  Mas so libera DEPOIS que o dono (voce) assina.
// )


se __name__ == "__main__" entao:
    _demo()

```
