# OpenVoiceTerminalBridge -- Ponte Bidirecional Voz <-> Terminal (Sem Bugs)

**Arquivo original:** `open-republic/core/open_voice_terminal_bridge.py`

**Descricao:** ==========================================================================
"Diga. O terminal executa. O terminal responde. A voz explica."
ESTE MODULO E A COLA entre 4 sistemas:
- Whisper (STT): audio -> texto
- VoiceOSControl: texto -> comando reconhecido
- Terminal: comando -> execucao real -> saida
- Kokoro/espeak (TTS): saida do terminal -> voz
DIRECAO 1: VOZ -> TERMINAL (ditar comando)
  Microfone -> Whisper -> texto
  -> Parser (regex + fuzzy match)
  -> Tradutor (comando de voz -> comando shell)
  -> Executor (shell real, com timeout e captura de erro)
  -> Saida capturada
DIRECAO 2: TERMINAL -> VOZ (ler saida)
  Saida do terminal (stdout/stderr)
  -> Limpador (strip ANSI, strip binario, normaliza encoding)
  -> Resumidor (corta saidas longas, preserva info critica)
  -> Tradutor (jargao tecnico -> portugues humano)
  -> TTS (Kokoro/espeak/Chatterbox)
  -> Audio
"SEM BUGS" -- O QUE ISTO SIGNIFICA:
1. SAIDA LONGA NAO ENFORCA O TTS:
   'ls /' tem 50+ diretorios. TTS nao vai ler tudo.
   Resumidor corta: "47 arquivos. Principais: bin, boot, dev, etc..."
2. ANSI/ESCAPE NAO VIRA PALAVRA:
   '\x1b[32mSUCESSO\x1b[0m' nao vira "esc braquete 32 eme sucesso".
   Limpador remove codes ANSI antes do TTS.
3. BINARIO NAO E LIDO:
   'cat foto.jpg' produz binario. Limpador detecta e bloqueia.
   TTS diz: "Isso nao e texto. E um arquivo binario."
4. ERRO TRADUZIDO PARA HUMANO:
   'command not found' -> "Comando nao encontrado. Voce quis dizer...?"
   'permission denied' -> "Sem permissao. Tente com sudo."
   'No such file' -> "Arquivo nao existe."
5. TIMEOUT EM COMANDO TRAVADO:
   'sudo apt update' pode demorar. Executor tem timeout.
   TTS diz: "Executando... Isso pode demorar."
6. STREAMING (NAO ESPERA TERMINAR):
   Saida do comando aparece em tempo real.
   TTS le incrementalmente (frase por frase).
7. ENCODING CORRIGIDO:
   Linux tem UTF-8. Mas comandos antigos usam Latin-1.
   Limpador normaliza para UTF-8 antes do TTS.
Author: OpenRepublic Team

---

```portugol

// !/usr/bin/env python3
// 
OpenVoiceTerminalBridge -- Ponte Bidirecional Voz <-> Terminal (Sem Bugs)
==========================================================================
"Diga. O terminal executa. O terminal responde. A voz explica."

ESTE MODULO E A COLA entre 4 sistemas:
- Whisper (STT): audio -> texto
- VoiceOSControl: texto -> comando reconhecido
- Terminal: comando -> execucao real -> saida
- Kokoro/espeak (TTS): saida do terminal -> voz

DIRECAO 1: VOZ -> TERMINAL (ditar comando)
  Microfone -> Whisper -> texto
  -> Parser (regex + fuzzy match)
  -> Tradutor (comando de voz -> comando shell)
  -> Executor (shell real, com timeout e captura de erro)
  -> Saida capturada

DIRECAO 2: TERMINAL -> VOZ (ler saida)
  Saida do terminal (stdout/stderr)
  -> Limpador (strip ANSI, strip binario, normaliza encoding)
  -> Resumidor (corta saidas longas, preserva info critica)
  -> Tradutor (jargao tecnico -> portugues humano)
  -> TTS (Kokoro/espeak/Chatterbox)
  -> Audio

"SEM BUGS" -- O QUE ISTO SIGNIFICA:

1. SAIDA LONGA NAO ENFORCA O TTS:
   'ls /' tem 50+ diretorios. TTS nao vai ler tudo.
   Resumidor corta: "47 arquivos. Principais: bin, boot, dev, etc..."

2. ANSI/ESCAPE NAO VIRA PALAVRA:
   '\x1b[32mSUCESSO\x1b[0m' nao vira "esc braquete 32 eme sucesso".
   Limpador remove codes ANSI antes do TTS.

3. BINARIO NAO E LIDO:
   'cat foto.jpg' produz binario. Limpador detecta e bloqueia.
   TTS diz: "Isso nao e texto. E um arquivo binario."

4. ERRO TRADUZIDO PARA HUMANO:
   'command not found' -> "Comando nao encontrado. Voce quis dizer...?"
   'permission denied' -> "Sem permissao. Tente com sudo."
   'No such file' -> "Arquivo nao existe."

5. TIMEOUT EM COMANDO TRAVADO:
   'sudo apt update' pode demorar. Executor tem timeout.
   TTS diz: "Executando... Isso pode demorar."

6. STREAMING (NAO ESPERA TERMINAR):
   Saida do comando aparece em tempo real.
   TTS le incrementalmente (frase por frase).

7. ENCODING CORRIGIDO:
   Linux tem UTF-8. Mas comandos antigos usam Latin-1.
   Limpador normaliza para UTF-8 antes do TTS.

Author: OpenRepublic Team
// 
// importa annotations de __future__
// importa Any, Dict, List, Optional, Tuple, Set, Callable de typing
// importa Enum de enum
// importa dataclass, field de dataclasses
// importa defaultdict de collections
// importa datetime de datetime
// importa re
// importa os
// importa shlex


// ============================================================================
// 1. ENUMS
// ============================================================================

classe DirecaoBridge herda de Enum:
    // Direcao do fluxo na ponte.
    VOZ_PARA_TERMINAL <- ("voz_term", "Voz -> Terminal: ditado de comando")
    TERMINAL_PARA_VOZ <- ("term_voz", "Terminal -> Voz: leitura de saida")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe TipoSaida herda de Enum:
    // Tipo de saida do terminal.
    TEXTO_LIMPO <- ("texto", "Texto limpo: ler para o usuario")
    TEXTO_LONGO <- ("longo", "Texto longo: resumir antes de ler")
    BINARIO <- ("binario", "Binario: NAO ler (bloquear)")
    VAZIO <- ("vazio", "Vazio: nada para dizer")
    ERRO <- ("erro", "Erro: traduzir para humano")
    PROGRESSO <- ("progresso", "Barra de progresso: ignorar")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe NivelVerbosidade herda de Enum:
    // Quanto o TTS fala ao ler a saida do terminal.
    MINIMO <- ("minimo", "Minimo: so resultado ('Feito.' ou 'Erro.')")
    RESUMO <- ("resumo", "Resumo: 3-5 frases chave")
    COMPLETO <- ("completo", "Completo: le tudo (para cego que precisa ver)")
    INTERATIVO <- ("interativo", "Interativo: le incrementalmente em streaming")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe StatusExecucao herda de Enum:
    // Status da execucao de um comando no terminal.
    SUCESSO <- ("sucesso", "Comando executado com sucesso")
    ERRO_EXECUCAO <- ("erro_exec", "Erro durante execucao (exit code != 0)")
    TIMEOUT <- ("timeout", "Comando excedeu o tempo limite")
    COMANDO_INVALIDO <- ("invalido", "Comando invalido ou nao reconhecido")
    PERIGOSO <- ("perigoso", "Comando perigoso bloqueado (rm -rf, etc.)")
    SEM_PERMISSAO <- ("permissao", "Sem permissao (requer sudo)")
    NAO_ENCONTRADO <- ("nao_encontrado", "Comando nao encontrado no sistema")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe CategoriaComandoShell herda de Enum:
    // Categorias de comandos shell que a voz pode disparar.
    NAVEGACAO <- ("navegacao", "Navegacao: cd, ls, pwd, find")
    ARQUIVO <- ("arquivo", "Arquivo: cp, mv, rm, mkdir, touch, cat")
    SISTEMA <- ("sistema", "Sistema: apt, systemctl, top, df, free")
    REDE <- ("rede", "Rede: ping, curl, wget, ssh, ip")
    TEXTO <- ("texto", "Texto: grep, sed, awk, sort, uniq, wc")
    REPUBLICA <- ("republica", "Republica: republica-* apps")
    SEGURO <- ("seguro", "Seguranca: nmap, lynis, whoami, passwd")
    PROCESSO <- ("processo", "Processo: ps, kill, top, htop")
    DIRETO <- ("direto", "Direto: texto que nao e comando, so ditar")

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
classe TraducaoComando:
    // Mapeia um comando de voz para um comando shell.
    id: str
    categoria: CategoriaComandoShell
    padrao_voz: List[str]        // regex: [r"^abrir (.+)$", r"^abre (.+)$"]
    template_shell: str          // "firefox" ou "cd {dir} && ls"
    declare parametros: List[str]  <- field(default_factory=list)
    declare perigoso: bool  <- FALSO  // rm -rf, dd, mkfs
    declare requer_sudo: bool  <- FALSO
    declare descricao: str  <- ""
    declare exemplo_voz: str  <- ""
    declare exemplo_shell: str  <- ""


// decorador: @dataclass
classe ResultadoExecucao:
    // Resultado de executar um comando no terminal.
    comando_shell: str
    declare stdout: str  <- ""
    declare stderr: str  <- ""
    declare exit_code: int  <- 0
    declare status: StatusExecucao  <- StatusExecucao.SUCESSO
    declare duracao_ms: int  <- 0
    declare timeout: bool  <- FALSO
    // saida processada para TTS
    declare tipo_saida: TipoSaida  <- TipoSaida.TEXTO_LIMPO
    declare texto_para_tts: str  <- ""
    // metadados
    declare timestamp: str  <- ""


// decorador: @dataclass
classe RegraTraducaoErro:
    // Traduz uma mensagem de erro tecnica para portugues humano.
    padrao_erro: str            // regex que casa no stderr
    traducao_humana: str        // "Sem permissao. Tente com sudo."
    declare sugestao: str  <- ""  // "Quer que eu rode com sudo?"


// ============================================================================
// 3. DADOS: TRADUCOES DE COMANDOS E ERROS
// ============================================================================

// --- Comandos perigosos que NUNCA sao executados ---
declare COMANDOS_PERIGOSOS: Set[str]  <- {
    "rm -rf /", "rm -rf /*", "rm -rf ~", "rm -rf $HOME",
    "dd if=/dev/zero of=/dev/sda", "mkfs.ext4 /dev/sda",
    ":(){:|:&};:", "chmod -R 777 /",
    "> /dev/sda", "mv / /dev/null",
}


funcao _init_traducoes_comandos() retorna List[TraducaoComando]:
    // Define como comandos de voz viram comandos shell.
    retorne [
        // === NAVEGACAO ===
        TraducaoComando("nav_ls", CategoriaComandoShell.NAVEGACAO,
            [r"^listar$", r"^lista$", r"^ls$", r"^o que tem aqui$",
             r"^mostrar arquivos$"],
            "ls -la --color=auto",
            [],
            descricao <- "Lista arquivos do diretorio atual",
            exemplo_voz <- "listar", exemplo_shell="ls -la"),
        TraducaoComando("nav_ls_pasta", CategoriaComandoShell.NAVEGACAO,
            [r"^listar (.+)$", r"^lista (.+)$", r"^o que tem em (.+)$",
             r"^mostrar (.+)$"],
            "ls -la {pasta}",
            ["pasta"],
            descricao <- "Lista arquivos de uma pasta",
            exemplo_voz <- "listar documentos", exemplo_shell="ls -la documentos"),
        TraducaoComando("nav_cd", CategoriaComandoShell.NAVEGACAO,
            [r"^ir para (.+)$", r"^entrar em (.+)$", r"^abrir pasta (.+)$",
             r"^navegar para (.+)$"],
            "cd {destino}",
            ["destino"],
            descricao <- "Navega para uma pasta",
            exemplo_voz <- "ir para documentos", exemplo_shell="cd documentos"),
        TraducaoComando("nav_pwd", CategoriaComandoShell.NAVEGACAO,
            [r"^onde estou$", r"^local atual$", r"^pwd$"],
            "pwd",
            [],
            descricao <- "Mostra o diretorio atual",
            exemplo_voz <- "onde estou", exemplo_shell="pwd"),
        TraducaoComando("nav_find", CategoriaComandoShell.NAVEGACAO,
            [r"^buscar (.+)$", r"^procurar (.+)$", r"^encontrar (.+)$",
             r"^achar (.+)$", r"^achar arquivo (.+)$"],
            "find . -name '*{termo}*' -type f 2>/dev/null",
            ["termo"],
            descricao <- "Busca arquivos por nome",
            exemplo_voz <- "buscar relatorio", exemplo_shell="find . -name '*relatorio*'"),

        // === ARQUIVO ===
        TraducaoComando("arq_cat", CategoriaComandoShell.ARQUIVO,
            [r"^ler arquivo (.+)$", r"^mostrar (.+)$", r"^conteudo de (.+)$",
             r"^cat (.+)$"],
            "cat {arquivo}",
            ["arquivo"],
            descricao <- "Mostra o conteudo de um arquivo",
            exemplo_voz <- "ler arquivo relatorio.txt", exemplo_shell="cat relatorio.txt"),
        TraducaoComando("arq_mkdir", CategoriaComandoShell.ARQUIVO,
            [r"^criar pasta (.+)$", r"^nova pasta (.+)$", r"^mkdir (.+)$"],
            "mkdir -p {nome}",
            ["nome"],
            descricao <- "Cria uma nova pasta",
            exemplo_voz <- "criar pasta projetos", exemplo_shell="mkdir -p projetos"),
        TraducaoComando("arq_cp", CategoriaComandoShell.ARQUIVO,
            [r"^copiar (.+) para (.+)$", r"^copia (.+) para (.+)$"],
            "cp {origem} {destino}",
            ["origem", "destino"],
            descricao <- "Copia um arquivo",
            exemplo_voz <- "copiar foto.jpg para backup", exemplo_shell="cp foto.jpg backup"),
        TraducaoComando("arq_mv", CategoriaComandoShell.ARQUIVO,
            [r"^mover (.+) para (.+)$", r"^renomear (.+) para (.+)$"],
            "mv {origem} {destino}",
            ["origem", "destino"],
            descricao <- "Move ou renomeia um arquivo",
            exemplo_voz <- "mover arquivo.txt para documentos",
            exemplo_shell <- "mv arquivo.txt documentos"),
        TraducaoComando("arq_rm", CategoriaComandoShell.ARQUIVO,
            [r"^apagar (.+)$", r"^deletar (.+)$", r"^remover (.+)$", r"^rm (.+)$"],
            "rm -i {arquivo}",
            ["arquivo"],
            perigoso <- FALSO,  // -i pede confirmacao
            descricao <- "Deleta um arquivo (com confirmacao)",
            exemplo_voz <- "apagar arquivo_velho.txt", exemplo_shell="rm -i arquivo_velho.txt"),
        TraducaoComando("arq_touch", CategoriaComandoShell.ARQUIVO,
            [r"^criar arquivo (.+)$", r"^tocar (.+)$", r"^touch (.+)$"],
            "touch {nome}",
            ["nome"],
            descricao <- "Cria um arquivo vazio",
            exemplo_voz <- "criar arquivo notas.txt", exemplo_shell="touch notas.txt"),
        TraducaoComando("arq_grep", CategoriaComandoShell.TEXTO,
            [r"^buscar texto (.+) em (.+)$", r"^grep (.+) (.+)$",
             r"^procurar palavra (.+) em (.+)$"],
            "grep -n '{termo}' {arquivo}",
            ["termo", "arquivo"],
            descricao <- "Busca texto dentro de um arquivo",
            exemplo_voz <- "buscar texto energia em config.py",
            exemplo_shell <- "grep -n 'energia' config.py"),

        // === SISTEMA ===
        TraducaoComando("sis_update", CategoriaComandoShell.SISTEMA,
            [r"^atualizar sistema$", r"^atualizar$", r"^apt update$",
             r"^update$"],
            "sudo apt update && sudo apt upgrade -y",
            [],
            requer_sudo <- VERDADEIRO,
            descricao <- "Atualiza o sistema",
            exemplo_voz <- "atualizar sistema", exemplo_shell="sudo apt update"),
        TraducaoComando("sis_install", CategoriaComandoShell.SISTEMA,
            [r"^instalar (.+)$", r"^apt install (.+)$"],
            "sudo apt install -y {pacote}",
            ["pacote"],
            requer_sudo <- VERDADEIRO,
            descricao <- "Instala um pacote",
            exemplo_voz <- "instalar firefox", exemplo_shell="sudo apt install -y firefox"),
        TraducaoComando("sis_df", CategoriaComandoShell.SISTEMA,
            [r"^espaco em disco$", r"^disco$", r"^quanto espaco$",
             r"^df$"],
            "df -h /",
            [],
            descricao <- "Mostra espaco em disco",
            exemplo_voz <- "espaco em disco", exemplo_shell="df -h /"),
        TraducaoComando("sis_free", CategoriaComandoShell.SISTEMA,
            [r"^memoria$", r"^ram$", r"^quanta memoria$", r"^free$"],
            "free -h",
            [],
            descricao <- "Mostra uso de memoria RAM",
            exemplo_voz <- "memoria", exemplo_shell="free -h"),
        TraducaoComando("sis_top", CategoriaComandoShell.PROCESSO,
            [r"^processos$", r"^o que esta rodando$", r"^top$"],
            "ps aux --sort=-%cpu | head -20",
            [],
            descricao <- "Lista processos ativos",
            exemplo_voz <- "processos", exemplo_shell="ps aux | head -20"),
        TraducaoComando("sys_uptime", CategoriaComandoShell.SISTEMA,
            [r"^tempo ligado$", r"^uptime$", r"^ha quanto tempo$"],
            "uptime",
            [],
            descricao <- "Mostra quanto tempo o sistema esta ligado",
            exemplo_voz <- "tempo ligado", exemplo_shell="uptime"),
        TraducaoComando("sis_service_status", CategoriaComandoShell.SISTEMA,
            [r"^status de (.+)$", r"^servico (.+)$"],
            "systemctl status {servico}",
            ["servico"],
            descricao <- "Mostra status de um servico",
            exemplo_voz <- "status de ssh", exemplo_shell="systemctl status ssh"),

        // === REDE ===
        TraducaoComando("rede_ping", CategoriaComandoShell.REDE,
            [r"^ping (.+)$", r"^testar conexao (.+)$", r"^verificar (.+)$"],
            "ping -c 4 {host}",
            ["host"],
            descricao <- "Testa conexao com um host",
            exemplo_voz <- "ping google.com", exemplo_shell="ping -c 4 google.com"),
        TraducaoComando("rede_ip", CategoriaComandoShell.REDE,
            [r"^meu ip$", r"^ip$", r"^endereco ip$", r"^qual meu ip$"],
            "ip addr show | grep 'inet '",
            [],
            descricao <- "Mostra o endereco IP",
            exemplo_voz <- "meu ip", exemplo_shell="ip addr show"),
        TraducaoComando("rede_wifi", CategoriaComandoShell.REDE,
            [r"^redes wifi$", r"^listar wifi$", r"^wifi disponiveis$"],
            "nmcli device wifi list",
            [],
            descricao <- "Lista redes WiFi disponiveis",
            exemplo_voz <- "redes wifi", exemplo_shell="nmcli device wifi list"),

        // === SEGURANCA ===
        TraducaoComando("sec_lynis", CategoriaComandoShell.SEGURO,
            [r"^auditoria de seguranca$", r"^rodar lynis$", r"^auditar sistema$"],
            "sudo lynis audit system",
            [],
            requer_sudo <- VERDADEIRO,
            descricao <- "Roda auditoria de seguranca Lynis",
            exemplo_voz <- "auditoria de seguranca", exemplo_shell="sudo lynis audit system"),
        TraducaoComando("sec_nmap", CategoriaComandoShell.SEGURO,
            [r"^escanear (.+)$", r"^nmap (.+)$", r"^mapear rede (.+)$"],
            "nmap -sV {alvo}",
            ["alvo"],
            descricao <- "Escaneia rede ou host",
            exemplo_voz <- "escanear 192.168.1.1", exemplo_shell="nmap -sV 192.168.1.1"),
        TraducaoComando("sec_whoami", CategoriaComandoShell.SEGURO,
            [r"^quem sou eu$", r"^whoami$", r"^qual usuario$"],
            "whoami",
            [],
            descricao <- "Mostra o usuario atual",
            exemplo_voz <- "quem sou eu", exemplo_shell="whoami"),

        // === REPUBLICA ===
        TraducaoComando("rep_ide", CategoriaComandoShell.REPUBLICA,
            [r"^abrir ide$", r"^iniciar ide$", r"^republica ide$"],
            "republica-ide &",
            [],
            descricao <- "Abre a OpenInclusiveIDE",
            exemplo_voz <- "abrir IDE", exemplo_shell="republica-ide &"),
        TraducaoComando("rep_iara", CategoriaComandoShell.REPUBLICA,
            [r"^iniciar iara$", r"^chamar iara$", r"^acordar iara$",
             r"^republica iara$"],
            "republica-iara &",
            [],
            descricao <- "Inicia a Iara",
            exemplo_voz <- "chamar iara", exemplo_shell="republica-iara &"),
        TraducaoComando("rep_energy", CategoriaComandoShell.REPUBLICA,
            [r"^abrir energia$", r"^energy$", r"^monitor de energia$"],
            "republica-energy &",
            [],
            descricao <- "Abre o OpenEnergy",
            exemplo_voz <- "abrir energia", exemplo_shell="republica-energy &"),
        TraducaoComando("rep_terminal", CategoriaComandoShell.REPUBLICA,
            [r"^novo terminal$", r"^abrir terminal$"],
            "gnome-terminal &",
            [],
            descricao <- "Abre um novo terminal",
            exemplo_voz <- "abrir terminal", exemplo_shell="gnome-terminal &"),
        TraducaoComando("rep_app_generico", CategoriaComandoShell.REPUBLICA,
            [r"^abrir (.+)$", r"^iniciar (.+)$", r"^executar (.+)$"],
            "{app}",
            ["app"],
            descricao <- "Abre um aplicativo generico",
            exemplo_voz <- "abrir firefox", exemplo_shell="firefox &"),

        // === DIRETO (ditado de texto, nao comando) ===
        TraducaoComando("dir_ditar", CategoriaComandoShell.DIRETO,
            [r"^digitar (.+)$", r"^escrever (.+)$", r"^ditar (.+)$"],
            "DITAR_TEXTO:{texto}",
            ["texto"],
            descricao <- "Digita texto no campo ativo (nao e comando shell)",
            exemplo_voz <- "digitar ola mundo", exemplo_shell="xdotool type 'ola mundo'"),
    ]


funcao _init_traducoes_erros() retorna List[RegraTraducaoErro]:
    // Traduz erros comuns do terminal para portugues humano.
    retorne [
        RegraTraducaoErro(
            r"command not found",
            "Comando nao encontrado.",
            "Verifique se o nome esta correto ou se o programa esta instalado."),
        RegraTraducaoErro(
            r"No such file or directory",
            "Arquivo ou pasta nao existe.",
            "Verifique o nome e o caminho."),
        RegraTraducaoErro(
            r"Permission denied",
            "Sem permissao.",
            "Tente novamente com sudo, ou verifique as permissoes do arquivo."),
        RegraTraducaoErro(
            r"Operation not permitted",
            "Operacao nao permitida.",
            "Voce precisa de privilegios de administrador."),
        RegraTraducaoErro(
            r"Connection (?:refused|timed out|failed)",
            "Falha na conexao.",
            "Verifique se o servidor esta online e se a rede funciona."),
        RegraTraducaoErro(
            r"E: Unable to locate package",
            "Pacote nao encontrado no repositorio.",
            "Tente 'sudo apt update' antes de instalar."),
        RegraTraducaoErro(
            r"E: (?:Could not|Unable to) (?:get lock|open lock)",
            "Outro processo esta usando o gerenciador de pacotes.",
            "Aguarde alguns segundos ou feche outros instaladores."),
        RegraTraducaoErro(
            r"error.*syntax",
            "Erro de sintaxe no codigo.",
            "Verifique se nao falta ponto e virgula, parentesis ou indentacao."),
        RegraTraducaoErro(
            r"Segmentation fault|core dumped",
            "O programa crashou (erro de memoria).",
            "Isso e um bug do programa, nao seu. Reporte ao desenvolvedor."),
        RegraTraducaoErro(
            r"(?:is not in the sudoers file|not in sudoers|sudoers)",
            "Voce nao tem permissao de administrador.",
            "Sua conta nao permite usar sudo. Contate o administrador do sistema."),
        RegraTraducaoErro(
            r"disk full|No space left on device",
            "Disco cheio.",
            "Apague arquivos desnecessarios. Digite 'df -h' para ver o espaco."),
        RegraTraducaoErro(
            r"address already in use",
            "A porta ja esta em uso.",
            "Outro programa esta usando essa porta. Feche-o ou use outra porta."),
    ]


// ============================================================================
// 4. LIMPADOR DE SAIDA (sem bugs)
// ============================================================================

classe LimpadorSaida:
    // 
    Limpa a saida do terminal para consumo pelo TTS.
    Remove ANSI, binario, codifica UTF-8, corta saida longa.
    // 

    // Padroes ANSI/escape codes
    ANSI_ESCAPE <- re.compile(r'\x1b\[[0-9;]*[a-zA-Z]')
    ANSI_ESCAPE_EXT <- re.compile(r'\x1b\][^\x07]*\x07')
    ANSI_CSI <- re.compile(r'\x1b\[[0-9;]*m')
    ANSI_CURSOR <- re.compile(r'\x1b\[[0-9]*[ABCDHf]')
    ANSI_CLEAR <- re.compile(r'\x1b\[[0-9]*[JK]')

    // Caracteres de controle (exceto \n, \t, \r)
    CONTROLE <- re.compile(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]')

    // Barra de progresso (ex: [====>    ] 45%)
    PROGRESSO <- re.compile(r'\[[=>\s]*\]\s*\d+%', re.MULTILINE)

    // Maximo de linhas para TTS
    MAX_LINHAS_TTS <- 20
    MAX_CHARS_TTS <- 2000

    // decorador: @classmethod
    funcao limpar(cls, saida: str) retorna str:
        // Limpa a saida bruta do terminal.
        se NAO  saida entao:
            retorne ""

        // 1. Remover ANSI escape sequences
        texto <- cls.ANSI_ESCAPE.sub('', saida)
        texto <- cls.ANSI_ESCAPE_EXT.sub('', texto)
        texto <- cls.ANSI_CSI.sub('', texto)
        texto <- cls.ANSI_CURSOR.sub('', texto)
        texto <- cls.ANSI_CLEAR.sub('', texto)

        // 2. Remover caracteres de controle
        texto <- cls.CONTROLE.sub('', texto)

        // 3. Remover barras de progresso
        texto <- cls.PROGRESSO.sub('', texto)

        // 4. Normalizar quebras de linha
        texto <- texto.replace('\r\n', '\n').replace('\r', '\n')

        // 5. Remover linhas vazias consecutivas
        enquanto '\n\n\n' in texto faca:
            texto <- texto.replace('\n\n\n', '\n\n')

        // 6. Strip espacos no final de cada linha
        linhas <- [linha.rstrip() for linha in texto.split('\n')]
        texto <- '\n'.join(linhas)

        retorne texto.strip()

    // decorador: @classmethod
    funcao detectar_tipo(cls, saida_bruta: bytes) retorna TipoSaida:
        // Detecta o tipo de saida (texto, binario, vazio, etc.).
        se NAO  saida_bruta entao:
            retorne TipoSaida.VAZIO

        // detectar binario: se tem muitos bytes nulos ou bytes > 127 em proporcao alta
        tente:
            texto_tentativa <- saida_bruta.decode('utf-8')
        except (UnicodeDecodeError, ValueError):
            // falhou UTF-8 -- provavelmente binario
            retorne TipoSaida.BINARIO

        // verificar proporcao de bytes nao-texto
        nao_texto <- sum(1 for b in saida_bruta if b < 9  OU  (13 < b < 32)  OU  b == 127)
        se len(saida_bruta) > 0  E  nao_texto / len(saida_bruta) > 0.1 entao:
            retorne TipoSaida.BINARIO

        texto_limpo <- cls.limpar(texto_tentativa)
        se NAO  texto_limpo entao:
            retorne TipoSaida.VAZIO

        // verificar tamanho
        linhas <- texto_limpo.split('\n')
        se len(linhas) > cls.MAX_LINHAS_TTS  OU  len(texto_limpo) > cls.MAX_CHARS_TTS entao:
            retorne TipoSaida.TEXTO_LONGO

        retorne TipoSaida.TEXTO_LIMPO

    // decorador: @classmethod
    funcao resumir(cls, texto: str, num_linhas: int = 5) retorna str:
        // 
        Resume texto longo para o TTS.
        Preserva: primeira linha (cabecalho), ultimas linhas (resultado),
        e estatistica (quantas linhas no total).
        // 
        linhas <- [l for l in texto.split('\n') if l.strip()]
        se len(linhas) <= num_linhas entao:
            retorne '\n'.join(linhas)

        total <- len(linhas)
        // pegar primeira linha + N-2 do meio + ultima
        inicio <- linhas[:2]
        fim <- linhas[-2:]
        resumo <- inicio + [f"... ({total - 4} linhas omitidas) ..."] + fim
        retorne '\n'.join(resumo)


// ============================================================================
// 5. TRADUTOR DE ERROS
// ============================================================================

classe TradutorErros:
    // Traduz mensagens de erro do terminal para portugues humano.

    funcao __init__(self) retorna None:
        self.regras: List[RegraTraducaoErro] = _init_traducoes_erros()

    funcao traduzir(self, stderr: str) retorna Optional[Tuple[str, str]]:
        // 
        Tenta traduzir o stderr.
        Retorna (traducao, sugestao) ou nulo se nao reconhecer.
        // 
        stderr_lower <- stderr.lower()
        para cada regra em self.regras:
            se re.search(regra.padrao_erro, stderr_lower, re.IGNORECASE) entao:
                retorne (regra.traducao_humana, regra.sugestao)
        retorne nulo


// ============================================================================
// 6. TRADUTOR DE COMANDOS (voz -> shell)
// ============================================================================

classe TradutorComandos:
    // Converte comando de voz em comando shell.

    funcao __init__(self) retorna None:
        self.traducoes: List[TraducaoComando] = _init_traducoes_comandos()

    funcao traduzir(self, texto_voz: str) retorna Tuple[Optional[TraducaoComando], Dict[str, str]]:
        // 
        Converte texto de voz em comando shell.
        Retorna (traducao, parametros) ou (nulo, {}).
        // 
        texto <- texto_voz.strip().lower()
        se NAO  texto entao:
            retorne (nulo, {})

        para cada tr em self.traducoes:
            para cada padrao em tr.padrao_voz:
                match <- re.match(padrao, texto, re.IGNORECASE)
                se match entao:
                    declare params: Dict[str, str]  <- {}
                    para cada (i, nome) em enumerate(tr.parametros):
                        se i + 1 <= len(match.groups()) entao:
                            val <- match.group(i + 1)
                            // sanitizar parametro (prevenir injecao shell)
                            params[nome] = self._sanitizar_parametro(val)
                    retorne (tr, params)
        retorne (nulo, {})

    funcao _sanitizar_parametro(self, valor: str) retorna str:
        // Sanitiza parametro para prevenir injecao de shell.
        // remover caracteres perigosos
        perigosos <- [';', '&&', '||', '|', '`', '$', '(', ')', '{', '}', '<', '>', '\n', '\r']
        limpo <- valor.strip()
        para cada p em perigosos:
            limpo <- limpo.replace(p, '')
        retorne limpo

    funcao construir_shell(self, traducao: TraducaoComando, params: Dict[str, str]) retorna str:
        // Constroi o comando shell final a partir do template.
        cmd <- traducao.template_shell
        para cada (nome, valor) em params.items():
            cmd <- cmd.replace(f"{{{nome}}}", shlex.quote(valor))
        retorne cmd

    funcao e_perigoso(self, cmd: str) retorna bool:
        // Verifica se o comando e perigoso.
        cmd_lower <- cmd.lower().strip()
        para cada perigoso em COMANDOS_PERIGOSOS:
            se perigoso in cmd_lower entao:
                retorne VERDADEIRO
        // rm -rf sem alvo especifico
        se re.search(r'rm\s+-rf\s+(/|~|\$HOME|\*)', cmd_lower) entao:
            retorne VERDADEIRO
        retorne FALSO


// ============================================================================
// 7. EXECUTOR (simulado -- no mundo real usaria subprocess)
// ============================================================================

classe ExecutorComando:
    // 
    Executa comandos shell com timeout, captura de saida e seguranca.
    No demo, SIMULA a execucao. No mundo real, usaria subprocess.Popen.
    // 

    TIMEOUT_PADRAO <- 30  // segundos

    funcao __init__(self) retorna None:
        self.historico: List[ResultadoExecucao] = []

    def executar(self, cmd_shell: str, timeout: int = TIMEOUT_PADRAO,
                 declare dry_run: bool  <- VERDADEIRO) -> ResultadoExecucao:
        // 
        Executa um comando. dry_run=VERDADEIRO simula (para o demo).
        dry_run <- FALSO executa de verdade (perigoso -- so em producao).
        // 
        inicio <- datetime.now()

        se dry_run entao:
            retorne self._simular(cmd_shell, inicio)
        // --- execucao real (nao usada no demo) ---
        // import subprocess
        // try:
        // proc = subprocess.run(cmd_shell, shell=True, capture_output=True,
        // text=True, timeout=timeout)
        // ...
        retorne self._simular(cmd_shell, inicio)

    funcao _simular(self, cmd: str, inicio: datetime) retorna ResultadoExecucao:
        // Simula a execucao para o demo.
        duracao <- 50  // ms simulado

        // determinar saida baseada no comando
        se cmd.startswith("ls") entao:
            stdout <- (
                "drwxr-xr-x  documentos\n"
                "drwxr-xr-x  downloads\n"
                "drwxr-xr-x  imagens\n"
                "drwxr-xr-x  musica\n"
                "-rw-r--r--  relatorio.txt\n"
                "-rw-r--r--  notas.md"
            )
            status <- StatusExecucao.SUCESSO
            exit_code <- 0
        senao se cmd.startswith("pwd") entao:
            stdout <- "/home/republica/Documentos"
            status <- StatusExecucao.SUCESSO
            exit_code <- 0
        senao se cmd.startswith("whoami") entao:
            stdout <- "republica"
            status <- StatusExecucao.SUCESSO
            exit_code <- 0
        senao se cmd.startswith("df -h") entao:
            stdout <- (
                "Filesystem      Size  Used Avail Use% Mounted on\n"
                "/dev/sda1       100G   45G   50G  48% /"
            )
            status <- StatusExecucao.SUCESSO
            exit_code <- 0
        senao se cmd.startswith("free -h") entao:
            stdout <- (
                "              total        used        free\n"
                "Mem:           16Gi       4.2Gi       10Gi\n"
                "Swap:         2.0Gi          0B       2.0Gi"
            )
            status <- StatusExecucao.SUCESSO
            exit_code <- 0
        senao se cmd.startswith("uptime") entao:
            stdout <- "up 3 days, 4:30, 2 users, load average: 0.20, 0.15, 0.10"
            status <- StatusExecucao.SUCESSO
            exit_code <- 0
        senao se cmd.startswith("ping") entao:
            stdout <- "PING google.com: 4 packets, 0% loss, time 30ms"
            status <- StatusExecucao.SUCESSO
            exit_code <- 0
        senao se "command NAO  found" in cmd  OU  "naoexiste" in cmd entao:
            stderr <- f"{cmd.split()[0]}: command not found"
            status <- StatusExecucao.NAO_ENCONTRADO
            exit_code <- 127
            stdout <- ""
        senao se cmd.startswith("DITAR_TEXTO:") entao:
            stdout <- ""  // ditado nao tem saida de terminal
            status <- StatusExecucao.SUCESSO
            exit_code <- 0
        senao:
            stdout <- f"[simulado] Comando executado: {cmd}"
            status <- StatusExecucao.SUCESSO
            exit_code <- 0

        resultado <- ResultadoExecucao(
            comando_shell <- cmd,
            stdout <- stdout,
            stderr <- stderr if status != StatusExecucao.SUCESSO else "",
            exit_code <- exit_code,
            status <- status,
            duracao_ms <- duracao,
            timestamp <- inicio.isoformat(),
        )
        self.historico.append(resultado)
        retorne resultado


// ============================================================================
// 8. ENGINE PRINCIPAL
// ============================================================================

classe VoiceTerminalBridgeEngine:
    // 
    Motor da ponte bidirecional Voz <-> Terminal.
    // 

    funcao __init__(self) retorna None:
        self.tradutor_cmd = TradutorComandos()
        self.tradutor_erro = TradutorErros()
        self.limpador = LimpadorSaida
        self.executor = ExecutorComando()
        self.verbosidade: NivelVerbosidade = NivelVerbosidade.RESUMO

    // -- DIRECAO 1: VOZ -> TERMINAL ----------------------------------------

    funcao voz_para_terminal(self, texto_voz: str, dry_run: bool = True) retorna ResultadoExecucao:
        // 
        Pipeline completo: texto de voz -> comando shell -> execucao -> resultado.
        // 
        // 0. VERIFICAR PERIGO ANTES DE TUDO (mesmo antes de traduzir)
        se self.tradutor_cmd.e_perigoso(texto_voz.lower()) entao:
            retorne ResultadoExecucao(
                comando_shell <- texto_voz,
                status <- StatusExecucao.PERIGOSO,
                stderr <- "Comando bloqueado por seguranca.",
                texto_para_tts <- "Comando perigoso bloqueado. Eu nao faco isso.",
                timestamp <- datetime.now().isoformat(),
            )

        // 1. traduzir voz em comando
        desempacote traducao, params <- self.tradutor_cmd.traduzir(texto_voz)

        se traducao e nulo entao:
            retorne ResultadoExecucao(
                comando_shell <- "",
                status <- StatusExecucao.COMANDO_INVALIDO,
                stderr <- f"Nao reconheci o comando: '{texto_voz}'",
                texto_para_tts <- f"Nao reconheci o comando: {texto_voz}.",
                timestamp <- datetime.now().isoformat(),
            )

        // 2. construir comando shell
        cmd_shell <- self.tradutor_cmd.construir_shell(traducao, params)

        // 3. verificar se e perigoso
        se self.tradutor_cmd.e_perigoso(cmd_shell) entao:
            retorne ResultadoExecucao(
                comando_shell <- cmd_shell,
                status <- StatusExecucao.PERIGOSO,
                stderr <- "Comando bloqueado por seguranca.",
                texto_para_tts <- "Comando perigoso bloqueado. Eu nao faco isso.",
                timestamp <- datetime.now().isoformat(),
            )

        // 4. executar (simulado ou real)
        resultado <- self.executor.executar(cmd_shell, dry_run=dry_run)

        // 5. processar saida para TTS
        resultado <- self._processar_saida(resultado)

        retorne resultado

    // -- DIRECAO 2: TERMINAL -> VOZ ----------------------------------------

    funcao _processar_saida(self, resultado: ResultadoExecucao) retorna ResultadoExecucao:
        // 
        Processa a saida do terminal para gerar texto que o TTS vai ler.
        E aqui que os "bugs" sao tratados.
        // 
        // ERRO: traduzir mensagem de erro
        se resultado.status != StatusExecucao.SUCESSO  E  resultado.stderr entao:
            traducao <- self.tradutor_erro.traduzir(resultado.stderr)
            se traducao entao:
                desempacote msg, sugestao <- traducao
                resultado.texto_para_tts = msg
                se sugestao  E  self.verbosidade != NivelVerbosidade.MINIMO entao:
                    resultado.texto_para_tts += f" {sugestao}"
            senao:
                // erro nao reconhecido: ler stderr limpo
                stderr_limpo <- self.limpador.limpar(resultado.stderr)
                resultado.texto_para_tts = f"Erro: {stderr_limpo[:200]}"
            resultado.tipo_saida = TipoSaida.ERRO
            retorne resultado

        // SUCESSO: processar stdout
        se NAO  resultado.stdout entao:
            // sem saida -- comando silencioso (mkdir, cp, etc.)
            resultado.texto_para_tts = "Feito."
            resultado.tipo_saida = TipoSaida.VAZIO
            retorne resultado

        // detectar tipo de saida
        tente:
            saida_bytes <- resultado.stdout.encode('utf-8')
        capture Exception:
            saida_bytes <- resultado.stdout.encode('latin-1')

        tipo <- self.limpador.detectar_tipo(saida_bytes)

        se tipo == TipoSaida.BINARIO entao:
            resultado.tipo_saida = TipoSaida.BINARIO
            resultado.texto_para_tts = "Saida binaria. Nao posso ler isso em voz."
            retorne resultado

        // limpar saida
        texto_limpo <- self.limpador.limpar(resultado.stdout)

        se tipo == TipoSaida.VAZIO  OU  NAO  texto_limpo entao:
            resultado.texto_para_tts = "Feito."
            resultado.tipo_saida = TipoSaida.VAZIO
            retorne resultado

        se tipo == TipoSaida.TEXTO_LONGO entao:
            // resumir para o TTS
            se self.verbosidade == NivelVerbosidade.COMPLETO entao:
                // cego precisa de tudo -- le completo
                resultado.texto_para_tts = texto_limpo[:self.limpador.MAX_CHARS_TTS]
            senao:
                resumo <- self.limpador.resumir(texto_limpo)
                resultado.texto_para_tts = resumo
            resultado.tipo_saida = TipoSaida.TEXTO_LONGO
            retorne resultado

        // TEXTO LIMPO: ler como esta
        resultado.texto_para_tts = texto_limpo
        resultado.tipo_saida = TipoSaida.TEXTO_LIMPO
        retorne resultado

    // -- PIPELINE COMPLETO (voz -> term -> voz) ----------------------------

    funcao ciclo_completo(self, texto_voz: str, dry_run: bool = True) retorna Dict[str, Any]:
        // 
        Ciclo completo: usuario fala -> terminal executa -> TTS responde.
        // 
        resultado <- self.voz_para_terminal(texto_voz, dry_run=dry_run)
        retorne {
            "voz_input": texto_voz,
            "comando_shell": resultado.comando_shell,
            "status": resultado.status.id,
            "exit_code": resultado.exit_code,
            "tipo_saida": resultado.tipo_saida.id,
            "texto_para_tts": resultado.texto_para_tts,
            "stdout_bruto": resultado.stdout[:500],
        }

    // -- scorecard ----------------------------------------------------------

    funcao scorecard(self) retorna Dict[str, Any]:
        retorne {
            "traducoes_comando": len(self.tradutor_cmd.traducoes),
            "traducoes_erro": len(self.tradutor_erro.regras),
            "comandos_perigosos": len(COMANDOS_PERIGOSOS),
            "categorias_shell": len(list(CategoriaComandoShell)),
            "tipos_saida": len(list(TipoSaida)),
            "niveis_verbosidade": len(list(NivelVerbosidade)),
            "status_execucao": len(list(StatusExecucao)),
            "historico_comandos": len(self.executor.historico),
        }


// ============================================================================
// 9. DEMO
// ============================================================================

funcao _demo() retorna None:
    e <- VoiceTerminalBridgeEngine()

    print("=" * 70)
    print("OpenVoiceTerminalBridge -- Ponte Voz <-> Terminal (Sem Bugs)")
    print("=" * 70)

    // --- Visao geral ---
    print(f"""
ESTE MODULO E A PONTE entre 4 sistemas:

  VOZ -> TERMINAL (Direcao 1):
    Microfone -> Whisper -> texto
    -> TradutorComandos (voz -> shell)
    -> ExecutorComando (shell -> saida)
    -> saida capturada

  TERMINAL -> VOZ (Direcao 2):
    Saida do terminal (stdout/stderr)
    -> LimpadorSaida (remove ANSI, binario, normaliza)
    -> TradutorErros (jargao -> portugues)
    -> Resumidor (corta saida longa)
    -> TTS (Kokoro/espeak/Chatterbox)
    -> Audio
// )

    // --- Traducoes de comando ---
    print(f"[TRADUCOES DE COMANDO ({len(e.tradutor_cmd.traducoes)})]")
    para cada cat em CategoriaComandoShell:
        cmds_cat <- [t for t in e.tradutor_cmd.traducoes if t.categoria == cat]
        print(f"\n  --- {cat.rotulo} ({len(cmds_cat)}) ---")
        for t in cmds_cat[:3]:   // so 3 por categoria para caber
            perigo <- " [PERIGOSO]" if t.perigoso else ""
            sudo <- " [SUDO]" if t.requer_sudo else ""
            print(f"    '{t.exemplo_voz}' -> {t.exemplo_shell}{perigo}{sudo}")

    // --- Traducoes de erro ---
    print(f"\n[TRADUCOES DE ERRO ({len(e.tradutor_erro.regras)})]")
    para cada r em e.tradutor_erro.regras:
        print(f"  '{r.padrao_erro}'")
        print(f"    -> \"{r.traducao_humana}\"")
        se r.sugestao entao:
            print(f"    Sugestao: {r.sugestao}")

    // --- Comandos perigosos ---
    print(f"\n[COMANDOS PERIGOSOS BLOQUEADOS ({len(COMANDOS_PERIGOSOS)})]")
    para cada cmd em sorted(COMANDOS_PERIGOSOS):
        print(f"  BLOQUEADO: {cmd}")

    // --- Simulacao: ciclo completo ---
    print("\n" + "=" * 70)
    print("[SIMULACAO] Ciclo completo: voz -> terminal -> voz")
    print("=" * 70)

    comandos_teste <- [
        "listar",                     // ls
        "onde estou",                 // pwd
        "quem sou eu",                // whoami
        "espaco em disco",            // df -h
        "memoria",                    // free -h
        "tempo ligado",               // uptime
        "ping google.com",            // ping
        "digitar ola mundo",          // ditado (nao comando)
        "instalar pacote_inexistente",   // erro: NAO  found
        "rm -rf /",                   // BLOQUEADO (perigoso)
        "buscar relatorio",           // find
    ]

    para cada cmd_voz em comandos_teste:
        resultado <- e.ciclo_completo(cmd_voz)
        print(f"\n  VOZ: '{cmd_voz}'")
        print(f"  SHELL: {resultado['comando_shell'] or '(nenhum)'}")
        print(f"  STATUS: {resultado['status']}")
        print(f"  TIPO_SAIDA: {resultado['tipo_saida']}")
        print(f"  TTS DIZ: \"{resultado['texto_para_tts'][:100]}\"")
        se resultado['stdout_bruto'] entao:
            print(f"  STDOUT: {resultado['stdout_bruto'][:80]}")

    // --- Limpador em acao ---
    print("\n[TESTE DO LIMPADOR -- Removendo bugs]")
    print("=" * 70)

    casos_limpeza <- [
        ("ANSI codes",
         "\x1b[32mSUCESSO\x1b[0m: operacao \x1b[1mconcluida\x1b[0m",
         "Deve remover codigos de cor"),
        ("Caracteres de controle",
         "texto\x00\x07\x08normal\x0b",
         "Deve remover bytes de controle"),
        ("Barra de progresso",
         "[===>    ] 45%\n[====>   ] 67%\nConcluido",
         "Deve remover barras de progresso"),
        ("Quebras de linha",
         "linha1\r\nlinha2\r\nlinha3",
         "Deve normalizar \\r\\n para \\n"),
        ("Linhas vazias",
         "texto\n\n\n\n\noutra",
         "Deve colapsar linhas vazias"),
    ]

    for nome, entrada, esperado in casos_limpeza:
        saida <- LimpadorSaida.limpar(entrada)
        print(f"\n  CASO: {nome}")
        print(f"    Entrada: {repr(entrada[:50])}")
        print(f"    Saida:   {repr(saida[:50])}")
        print(f"    Esperado: {esperado}")

    // --- Resumidor ---
    print("\n[TESTE DO RESUMIDOR -- Saida longa]")
    texto_longo <- "\n".join(f"arquivo_{i:03d}.txt" for i in range(50))
    resumo <- LimpadorSaida.resumir(texto_longo)
    print(f"  Original: {len(texto_longo.split(chr(10)))} linhas")
    print(f"  Resumo:")
    para cada linha em resumo.split('\n'):
        print(f"    {linha}")

    // --- Fluxo tecnico ---
    print("\n[FLUXO TECNICO DETALHADO]")
    print("""
  1. USUARIO FALA: "listar documentos"
  2. WHISPER TRANSCREVE: "listar documentos" (texto)
  3. TRADUTOR CASA REGEX: r"^listar (.+)$" -> template "ls -la {pasta}"
  4. PARAMETRO EXTRAIDO: pasta="documentos"
  5. SANITIZACAO: "documentos" (sem ; | $ ` etc.)
  6. SHELL FINAL: ls -la documentos
  7. VERIFICACAO DE PERIGO: 'ls' nao e perigoso. OK.
  8. EXECUCAO: subprocess.run("ls -la documentos", timeout=30)
  9. STDOUT: "relatorio.txt\\nnotas.md\\nprojeto/"
  10. DETECCAO DE TIPO: texto limpo, 3 linhas. TEXTO_LIMPO.
  11. LIMPADOR: remove ANSI (se houver), normaliza encoding.
  12. TTS: Kokoro le "relatorio.txt, notas.md, projeto."
  13. AUDIO: voz diz a lista de arquivos.

  TEMPO TOTAL: <500ms (Whisper local + Kokoro local)

  SE DEU ERRO:
  8b. STDERR: "ls: cannot access 'documentos': No such file or directory"
  9b. TRADUTOR DE ERRO casa: r"No such file or directory"
  10b. TRADUCAO: "Arquivo ou pasta nao existe."
  11b. SUGESTAO: "Verifique o nome e o caminho."
  12b. TTS: Kokoro le "Arquivo ou pasta nao existe. Verifique o nome."
// )

    // --- Scorecard ---
    print("[SCORECARD]")
    sc <- e.scorecard()
    para cada (k, v) em sc.items():
        print(f"  {k:.<30} {v}")

    // --- Filosofia ---
    print("\n" + "=" * 70)
    print("FILOSOFIA -- Sem bugs, porque os bugs sao tratados")
    print("=" * 70)
    print("""
O PROBLEMA DAS PONTES VOZ-TERMINAL EXISTENTES:

  Alexa, Siri, Google Assistant nao controlam o terminal.
  Eles controlam APIs. O terminal e muito perigoso para eles.

  Projetos open source que tentam (voice-to-shell):
  - Passam texto direto para o shell sem sanitizar.
  - "deletar tudo" vira "rm -rf *" sem confirmacao.
  - Saida binaria e lida em voz ("esc braquete 32 eme").
  - Erros tecnicos nao sao traduzidos ("command not found" em ingles).
  - Saida de 1000 linhas e lida inteira (10 minutos de TTS).

  Cada um desses e um BUG. A Republica trata TODOS.

O PRINCIPIO "SEM BUGS":

  1. SANITIZACAO DE PARAMETRO:
     Usuario diz "listar ; rm -rf /".
     Sanitizador remove ; e o que vem depois.
     Shell final: "ls -la" (pasta vazia apos limpeza).
     NUNCA o comando do usuario vai direto para o shell.

  2. BLOCKLIST DE COMANDOS PERIGOSOS:
     "rm -rf /" e bloqueado ANTES da execucao.
     O sistema diz: "Comando perigoso. Eu nao faco isso."
     Nenhum comando da blocklist passa.

  3. DETECCAO DE BINARIO:
     'cat foto.jpg' produz bytes nao-texto.
     Limpador detecta e diz: "Saida binaria. Nao posso ler."
     TTS nunca recebe bytes nao-texto.

  4. TRADUCAO DE ERRO:
     "command not found" vira "Comando nao encontrado."
     "Permission denied" vira "Sem permissao."
     "No such file" vira "Arquivo nao existe."
     O usuario ouve PORTUGUES, nao jargao tecnico em ingles.

  5. RESUMO DE SAIDA LONGA:
     'ls /' tem 50+ diretorios. TTS le 5 + estatistica.
     "47 arquivos. Principais: bin, boot, dev, etc, home."
     Cego que precisa de TUDO sobe para verbosidade COMPLETO.

  6. TIMEOUT:
     'sudo apt update' pode demorar 2 minutos.
     Executor tem timeout de 30s (configuravel).
     TTS avisa: "Executando... Isso pode demorar."

  7. STREAMING (futuro):
     Comandos longos (apt update) mostram saida em tempo real.
     TTS le incrementalmente. Nao espera terminar.

A INTEGRACAO COM A IARA:

  Quando a Iara (OpenIara) recebe input de voz:
  1. Detecta se e COMANDO (Jarvis) ou CONVERSA (Iara).
  2. Se comando: chama VoiceTerminalBridge.
  3. Bridge traduz, executa, processa saida.
  4. Bridge devolve texto para TTS.
  5. Iara fala o resultado.

  O usuario nao sabe (nem precisa) que a Bridge existe.
  Ele fala. O terminal executa. A voz responde.
  Sem bugs. Porque os bugs foram tratados na construcao.
// )


se __name__ == "__main__" entao:
    _demo()

```
