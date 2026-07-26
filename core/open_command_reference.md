# OpenCommandReference -- Documentacao Acessivel de Comandos (tldr + Vosk + Output Adaptativo)

**Arquivo original:** `open-republic/core/open_command_reference.py`

**Descricao:** =============================================================================================
"Usuario diz 'ajuda tar'. Sistema responde. Na voz, no braille, no leitor de tela."
SUBSTITUI man pages como fonte primaria de ajuda. man pages sao:
- Textos densos, longos, sem estrutura de navegacao
- Pesadelo de acessibilidade (Orca le 500 linhas sem pausa)
- Ingles-centricos, traducoes incompletas
tldr-pages (~6000 comandos) e o oposto:
- Exemplos curtos e praticos (5-8 por comando)
- Formato markdown previsivel, parseavel
- Comunidade mantem, 40 idiomas incluindo pt_BR
- CC BY 4.0 (livre para usar/modificar)
A ARQUITETURA (3 camadas):
1. INDEXACAO LOCAL (tldr-pages)
   Clone do repo github.com/tldr-pages/tldr em /usr/share/republica/tldr/
   Parser converte markdown -> estruturas CommandPage (titulo, descricao, exemplos)
   Busca por nome, keyword, categoria, plataforma
   Prioridade: pt_BR primeiro, fallback ingles
2. INPUT POR VOZ (Vosk dual-STT)
   Vosk (lightweight, ~50ms): hotword "ajuda" + comando curto
   whisper.cpp (heavyweight): apenas se Vosk falhar ou ditado longo
   Fluxo: Microfone -> Vosk -> "ajuda tar" -> busca no indice
   Offline. Sem nuvem. Sem Big Tech. Sem spyware.
3. OUTPUT ADAPTATIVO
   O MESMO resultado e entregue em MULTIPLOS canais simultaneos:
   - IARA (Chatterbox TTS): voz humana natural, conversa
   - JARVIS (espeak-ng): voz robotica, comando rapido
   - ORCA (AT-SPI): leitor de tela le via arvore de acessibilidade
   - BRLTTY: display braille exibe o texto tatil
   - ALTO_CONTRASTE: terminal com fonte grande + fundo preto/amarelo
O USO:
  Cenario 1 -- Cego quer saber usar tar:
    Usuario: (voz) "ajuda tar"
    Vosk: reconhece "ajuda tar" (50ms)
    Sistema: busca tldr -> encontra 8 exemplos
    Iara: (voz humana) "Tar serve para arquivar. Quer ouvir os exemplos?"
    Usuario: (voz) "sim"
    Iara: le os 8 exemplos em voz natural
    Orca: simultaneamente expoe via AT-SPI para navegacao por tab
  Cenario 2 -- Surdo quer saber usar git:
    Usuario: digita "ajuda git commit" no terminal
    Sistema: busca tldr -> encontra exemplos
    Terminal: alto contraste, fonte grande, exemplos formatados
    (sem audio -- surdo nao precisa)
  Cenario 3 -- Tetraplegico usando eye tracker + switch:
    Usuario: (voz via Vosk) "ajuda nmap"
    Sistema: busca tldr
    Brltty: exibe exemplos no display braille
    (sem precisar mover os olhos para a tela)
  Cenario 4 -- Idoso com baixa visao:
    Usuario: digita "ajuda cp"
    Terminal: alto contraste (preto/amarelo), fonte 24pt
    Jarvis: (espeak) le os exemplos em voz alta
ALINHAMENTO CONSTITUCIONAL:
- P1: Documentacao acessivel para TODOS. Ninguem excluido por deficiencia.
- P6: Acesso universal ao conhecimento. man pages excluem; tldr inclui.
- P2: Output adaptativo respeita o corpo/corpo digital do usuario.
- P8: IA como instrumento (Vosk reconhece, Iara fala) -- amplifica humano.
- P4: tldr e aberto, auditavel, modificavel pela comunidade.
INTEGRACAO:
- OpenBigLinux: instalado como pacote republica-command-reference
- OpenAccessibilityShim: usa o Shim para apps que nao tem AT-SPI
- VoiceOSControl: Vosk e o mesmo motor do pipeline de 9 camadas
- OpenInclusiveIDE: IDE consulta comandos durante programacao
Author: OpenRepublic Team

---

```portugol

// !/usr/bin/env python3
// 
OpenCommandReference -- Documentacao Acessivel de Comandos (tldr + Vosk + Output Adaptativo)
=============================================================================================
"Usuario diz 'ajuda tar'. Sistema responde. Na voz, no braille, no leitor de tela."

SUBSTITUI man pages como fonte primaria de ajuda. man pages sao:
- Textos densos, longos, sem estrutura de navegacao
- Pesadelo de acessibilidade (Orca le 500 linhas sem pausa)
- Ingles-centricos, traducoes incompletas

tldr-pages (~6000 comandos) e o oposto:
- Exemplos curtos e praticos (5-8 por comando)
- Formato markdown previsivel, parseavel
- Comunidade mantem, 40 idiomas incluindo pt_BR
- CC BY 4.0 (livre para usar/modificar)

A ARQUITETURA (3 camadas):

1. INDEXACAO LOCAL (tldr-pages)
   Clone do repo github.com/tldr-pages/tldr em /usr/share/republica/tldr/
   Parser converte markdown -> estruturas CommandPage (titulo, descricao, exemplos)
   Busca por nome, keyword, categoria, plataforma
   Prioridade: pt_BR primeiro, fallback ingles

2. INPUT POR VOZ (Vosk dual-STT)
   Vosk (lightweight, ~50ms): hotword "ajuda" + comando curto
   whisper.cpp (heavyweight): apenas se Vosk falhar ou ditado longo
   Fluxo: Microfone -> Vosk -> "ajuda tar" -> busca no indice
   Offline. Sem nuvem. Sem Big Tech. Sem spyware.

3. OUTPUT ADAPTATIVO
   O MESMO resultado e entregue em MULTIPLOS canais simultaneos:
   - IARA (Chatterbox TTS): voz humana natural, conversa
   - JARVIS (espeak-ng): voz robotica, comando rapido
   - ORCA (AT-SPI): leitor de tela le via arvore de acessibilidade
   - BRLTTY: display braille exibe o texto tatil
   - ALTO_CONTRASTE: terminal com fonte grande + fundo preto/amarelo

O USO:

  Cenario 1 -- Cego quer saber usar tar:
    Usuario: (voz) "ajuda tar"
    Vosk: reconhece "ajuda tar" (50ms)
    Sistema: busca tldr -> encontra 8 exemplos
    Iara: (voz humana) "Tar serve para arquivar. Quer ouvir os exemplos?"
    Usuario: (voz) "sim"
    Iara: le os 8 exemplos em voz natural
    Orca: simultaneamente expoe via AT-SPI para navegacao por tab

  Cenario 2 -- Surdo quer saber usar git:
    Usuario: digita "ajuda git commit" no terminal
    Sistema: busca tldr -> encontra exemplos
    Terminal: alto contraste, fonte grande, exemplos formatados
    (sem audio -- surdo nao precisa)

  Cenario 3 -- Tetraplegico usando eye tracker + switch:
    Usuario: (voz via Vosk) "ajuda nmap"
    Sistema: busca tldr
    Brltty: exibe exemplos no display braille
    (sem precisar mover os olhos para a tela)

  Cenario 4 -- Idoso com baixa visao:
    Usuario: digita "ajuda cp"
    Terminal: alto contraste (preto/amarelo), fonte 24pt
    Jarvis: (espeak) le os exemplos em voz alta

ALINHAMENTO CONSTITUCIONAL:
- P1: Documentacao acessivel para TODOS. Ninguem excluido por deficiencia.
- P6: Acesso universal ao conhecimento. man pages excluem; tldr inclui.
- P2: Output adaptativo respeita o corpo/corpo digital do usuario.
- P8: IA como instrumento (Vosk reconhece, Iara fala) -- amplifica humano.
- P4: tldr e aberto, auditavel, modificavel pela comunidade.

INTEGRACAO:
- OpenBigLinux: instalado como pacote republica-command-reference
- OpenAccessibilityShim: usa o Shim para apps que nao tem AT-SPI
- VoiceOSControl: Vosk e o mesmo motor do pipeline de 9 camadas
- OpenInclusiveIDE: IDE consulta comandos durante programacao

Author: OpenRepublic Team
// 
// importa annotations de __future__
// importa Any, Dict, List, Optional, Tuple, Set de typing
// importa Enum de enum
// importa dataclass, field de dataclasses
// importa defaultdict de collections
// importa datetime de datetime
// importa re


// ============================================================================
// 1. ENUMS
// ============================================================================

classe PlataformaTldr herda de Enum:
    // Plataformas de comandos no tldr-pages.
    COMMON <- ("common", "Comandos comuns a todas as plataformas (~1000)")
    LINUX <- ("linux", "Comandos especificos Linux (~1000)")
    OSX <- ("osx", "macOS (~369)")
    WINDOWS <- ("windows", "Windows (~301)")
    ANDROID <- ("android", "Android (22)")
    SUNOS <- ("sunos", "SunOS/Solaris (11)")
    FREEBSD <- ("freebsd", "FreeBSD")
    NETBSD <- ("netbsd", "NetBSD")
    OPENBSD <- ("openbsd", "OpenBSD")
    CISCO_IOS <- ("cisco-ios", "Cisco IOS")
    DOS <- ("dos", "DOS")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe IdiomaTldr herda de Enum:
    // Idiomas do tldr-pages relevantes para a Republica.
    PT_BR <- ("pt_BR", "Portugues Brasileiro (prioridade)")
    PT_PT <- ("pt_PT", "Portugues de Portugal")
    EN <- ("en", "Ingles (fallback universal)")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe MotorSTT herda de Enum:
    // Motores de Speech-to-Text disponiveis (arquitetura dual-STT).
    VOSK <- ("vosk", "Vosk -- leve, ~50ms, comandos curtos e hotword")
    WHISPER <- ("whisper", "Whisper.cpp -- preciso, ~500ms-2s, ditado longo")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe CanalSaida herda de Enum:
    // Canais de output adaptativo para entrega da documentacao.
    IARA <- ("iara", "Iara (Chatterbox TTS) -- voz humana natural, conversa")
    JARVIS <- ("jarvis", "Jarvis (espeak-ng) -- voz robotica, comando rapido")
    ORCA <- ("orca", "Orca (AT-SPI) -- leitor de tela, navegacao por tab")
    BRLTTY <- ("brltty", "Brltty -- display braille, texto tatil")
    ALTO_CONTRASTE <- ("alto_contraste", "Terminal alto contraste + fonte grande")
    TERMINAL_PADRAO <- ("terminal", "Terminal padrao (sem adaptacao)")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe TipoConsulta herda de Enum:
    // Como o usuario consultou o sistema.
    VOZ_VOSK <- ("voz_vosk", "Voz via Vosk (hotword + comando)")
    VOZ_WHISPER <- ("voz_whisper", "Voz via Whisper (ditado longo)")
    TEXTO <- ("texto", "Digitado no terminal")
    IDE <- ("ide", "Consulta automatica da OpenInclusiveIDE")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe StatusIndexacao herda de Enum:
    // Status da indexacao de uma pagina tldr.
    PRONTO <- ("pronto", "Indexada e busca funcionando")
    PARCIAL <- ("parcial", "Indexada mas sem traducao pt_BR")
    FALLBACK_EN <- ("fallback_en", "So existe em ingles")
    AUSENTE <- ("ausente", "Comando nao encontrado no tldr")

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
classe ExemploComando:
    // Um exemplo de uso de um comando (uma linha do tldr).
    descricao: str         // "- [c]reate an archive and write it to a [f]ile:"
    comando: str           // "tar cf {{path/to/target.tar}} {{path/to/file1 path/to/file2 ...}}"


// decorador: @dataclass
classe CommandPage:
    // Uma pagina completa de comando do tldr-pages, parseada.
    comando: str                           // "tar", "git-commit", "nmap"
    titulo: str                            // "# tar"
    descricao: str                         // "> Archiving utility."
    declare link_mais_info: str  <- ""  // "<https://...>"
    declare plataforma: PlataformaTldr  <- PlataformaTldr.COMMON
    declare idioma: IdiomaTldr  <- IdiomaTldr.PT_BR
    declare exemplos: List[ExemploComando]  <- field(default_factory=list)

    // decorador: @property
    funcao num_exemplos(self) retorna int:
        retorne len(self.exemplos)


// decorador: @dataclass
classe ConfigVosk:
    // Configuracao do motor Vosk para comando de voz.
    declare modelo: str  <- "vosk-model-small-pt-BR-0.3"
    declare modelo_path: str  <- "/usr/share/republica/models/vosk-pt-br"
    declare sample_rate: int  <- 16000
    declare latencia_alvo_ms: int  <- 50
    declare hotword: str  <- "ajuda"
    declare grammar_comandos: List[str]  <- field(default_factory=lambda: [
        "ajuda", "parar", "repetir", "proximo", "anterior",
        "mais lento", "mais rapido", "exemplo",
    ])

    // decorador: @property
    funcao ativo(self) retorna bool:
        // No OpenBigLinux, Vosk e o motor STT primario para comandos.
        retorne VERDADEIRO


// decorador: @dataclass
classe ConfigWhisperFallback:
    // Configuracao do whisper.cpp como fallback STT.
    declare modelo: str  <- "ggml-base.pt-BR.bin"
    declare modelo_path: str  <- "/usr/share/republica/models/whisper-pt-br"
    declare latencia_alvo_ms: int  <- 2000
    declare ativa_em: List[str]  <- field(default_factory=lambda: [
        "vosk_falhou",
        "ditado_longo",
        "transcricao_audio",
        "transcricao_video",
    ])


// decorador: @dataclass
classe ResultadoBusca:
    // Resultado de uma busca por comando.
    query: str
    encontrou: bool
    declare pagina: Optional[CommandPage]  <- nulo
    declare status: StatusIndexacao  <- StatusIndexacao.AUSENTE
    declare alternativas: List[str]  <- field(default_factory=list)
    declare idioma_usado: IdiomaTldr  <- IdiomaTldr.EN


// decorador: @dataclass
classe EntregaOutput:
    // Como o resultado foi entregue ao usuario (multi-canal).
    declare canais_ativos: List[CanalSaida]  <- field(default_factory=list)
    declare tipo_consulta: TipoConsulta  <- TipoConsulta.TEXTO
    declare motor_stt: Optional[MotorSTT]  <- nulo
    declare latencia_ms: int  <- 0
    declare texto_entregue: str  <- ""


// decorador: @dataclass
classe PerfilSaidaUsuario:
    // Perfil de output do usuario (quais canais ativar).
    declare cego: bool  <- FALSO
    declare surdo: bool  <- FALSO
    declare baixa_visao: bool  <- FALSO
    declare tetraplegico: bool  <- FALSO
    declare usa_braille: bool  <- FALSO
    declare prefere_voz_humana: bool  <- VERDADEIRO  // Iara > Jarvis
    declare idioma_pref: IdiomaTldr  <- IdiomaTldr.PT_BR

    funcao canais(self) retorna List[CanalSaida]:
        // Determina quais canais de output ativar baseado no perfil.
        declare canais: List[CanalSaida]  <- []
        se self.cego  E  self.usa_braille entao:
            canais.extend([CanalSaida.IARA, CanalSaida.BRLTTY])
        senao se self.cego entao:
            canais.extend([CanalSaida.IARA, CanalSaida.ORCA])
        se self.surdo  OU  self.baixa_visao entao:
            canais.append(CanalSaida.ALTO_CONTRASTE)
        se self.tetraplegico  E  self.usa_braille entao:
            canais.append(CanalSaida.BRLTTY)
        se NAO  canais entao:
            canais.append(CanalSaida.TERMINAL_PADRAO)
        se self.cego  E  NAO  self.prefere_voz_humana entao:
            // Remove IARA, adiciona JARVIS
            canais <- [c for c in canais if c != CanalSaida.IARA]
            canais.insert(0, CanalSaida.JARVIS)
        retorne list(dict.fromkeys(canais))  // dedup preservando ordem


// ============================================================================
// 3. DADOS: COMANDOS SAMPLE (simula o que o tldr-pages fornece)
// ============================================================================

funcao _init_comandos_sample() retorna List[CommandPage]:
    // Comandos de exemplo que simulam o parse do tldr-pages.
    No deploy real, estes vem do clone em /usr/share/republica/tldr/."""
    retorne [
        CommandPage(
            comando <- "tar",
            titulo <- "# tar",
            descricao <- "Utilidade de arquivamento. Combinado com gzip ou bzip2 para compressao.",
            link_mais_info <- "https://www.gnu.org/software/tar/manual/tar.html",
            plataforma <- PlataformaTldr.COMMON,
            idioma <- IdiomaTldr.PT_BR,
            exemplos <- [
                ExemploComando(
                    "[c]riar um arquivo e salva-lo em um [f]icheiro:",
                    "tar cf {{caminho/para/destino.tar}} {{caminho/para/arquivo1 caminho/para/arquivo2 ...}}"),
                ExemploComando(
                    "[c]riar um arquivo g[z]ippado:",
                    "tar czf {{caminho/para/destino.tar.gz}} {{caminho/para/arquivo1 caminho/para/arquivo2 ...}}"),
                ExemploComando(
                    "E[x]trair um arquivo (comprimido) no diretorio atual [v]erbosamente:",
                    "tar xvf {{caminho/para/origem.tar[.gz|.bz2|.xz]}}"),
                ExemploComando(
                    "E[x]trair um arquivo no diretorio de destino:",
                    "tar xf {{caminho/para/origem.tar}} -C {{caminho/para/diretorio}}"),
                ExemploComando(
                    "Lis[t]ar o conteudo de um arquivo tar [v]erbosamente:",
                    "tar tvf {{caminho/para/origem.tar}}"),
            ]),
        CommandPage(
            comando <- "git-commit",
            titulo <- "# git commit",
            descricao <- "Registra alteracoes no repositorio.",
            link_mais_info <- "https://git-scm.com/docs/git-commit",
            plataforma <- PlataformaTldr.COMMON,
            idioma <- IdiomaTldr.PT_BR,
            exemplos <- [
                ExemploComando(
                    "Abre um editor para escrever a mensagem e commita arquivos stageados:",
                    "git commit"),
                ExemploComando(
                    "Commita arquivos stageados com uma mensagem especifica:",
                    "git commit -m {{\"mensagem\"}}"),
                ExemploComando(
                    "Auto-stageia arquivos modificados/deletados e commita:",
                    "git commit -a -m {{\"mensagem\"}}"),
                ExemploComando(
                    "Atualiza o ultimo commit adicionando alteracoes atuais:",
                    "git commit --amend"),
            ]),
        CommandPage(
            comando <- "nmap",
            titulo <- "# nmap",
            descricao <- "Scanner de rede. Descobre hosts, portas abertas, servicos e sistema operacional.",
            link_mais_info <- "https://nmap.org/",
            plataforma <- PlataformaTldr.LINUX,
            idioma <- IdiomaTldr.PT_BR,
            exemplos <- [
                ExemploComando(
                    "Escaneia as 1000 portas mais comuns de um host:",
                    "nmap {{host_exemplo.com}}"),
                ExemploComando(
                    "Detecta servico e versao nas portas abertas:",
                    "nmap -sV {{host_exemplo.com}}"),
                ExemploComando(
                    "Escaneia uma faixa de IPs (subnet):",
                    "nmap {{192.168.1.0/24}}"),
                ExemploComando(
                    "Detecta sistema operacional do alvo:",
                    "nmap -O {{host_exemplo.com}}"),
                ExemploComando(
                    "Escaneio rapido de portas (top 100):",
                    "nmap -F {{host_exemplo.com}}"),
                ExemploComando(
                    "Escaneio agressivo (OS + versao + scripts + traceroute):",
                    "nmap -A {{host_exemplo.com}}"),
            ]),
        CommandPage(
            comando <- "ffmpeg",
            titulo <- "# ffmpeg",
            descricao <- "Conversor de video/audio. Grava, transmite, processa multimidia.",
            link_mais_info <- "https://ffmpeg.org/ffmpeg.html",
            plataforma <- PlataformaTldr.COMMON,
            idioma <- IdiomaTldr.PT_BR,
            exemplos <- [
                ExemploComando(
                    "Extrai audio de um video:",
                    "ffmpeg -i {{video.mp4}} {{audio.mp3}}"),
                ExemploComando(
                    "Converte video para outro formato:",
                    "ffmpeg -i {{entrada.avi}} {{saida.mp4}}"),
                ExemploComando(
                    "Redimensiona video para 1280x720:",
                    "ffmpeg -i {{entrada.mp4}} -s 1280x720 {{saida.mp4}}"),
                ExemploComando(
                    "Corta os primeiros 60 segundos de um video:",
                    "ffmpeg -ss 00:01:00 -i {{entrada.mp4}} {{saida.mp4}}"),
                ExemploComando(
                    "Grava a tela do computador (Linux):",
                    "ffmpeg -f x11grab -i :0.0 {{saida.mp4}}"),
            ]),
        CommandPage(
            comando <- "find",
            titulo <- "# find",
            descricao <- "Busca arquivos e diretorios por nome, tipo, tamanho, data.",
            link_mais_info <- "https://www.gnu.org/software/findutils/",
            plataforma <- PlataformaTldr.COMMON,
            idioma <- IdiomaTldr.PT_BR,
            exemplos <- [
                ExemploComando(
                    "Busca arquivos por nome em um diretorio:",
                    "find {{caminho/para/diretorio}} -name {{\"*.txt\"}}"),
                ExemploComando(
                    "Busca arquivos modificados nos ultimos N dias:",
                    "find {{caminho/para/diretorio}} -mtime -{{N}}"),
                ExemploComando(
                    "Busca arquivos maiores que um tamanho:",
                    "find {{caminho/para/diretorio}} -size +{{100M}}"),
                ExemploComando(
                    "Busca e executa um comando em cada resultado:",
                    "find {{caminho/para/diretorio}} -name {{\"*.py\"}} -exec wc -l {} \\;"),
                ExemploComando(
                    "Apaga arquivos encontrados (pede confirmacao):",
                    "find {{caminho/para/diretorio}} -name {{\"*.tmp\"}} -delete"),
            ]),
        CommandPage(
            comando <- "grep",
            titulo <- "# grep",
            descricao <- "Busca padroes de texto dentro de arquivos.",
            link_mais_info <- "https://www.gnu.org/software/grep/",
            plataforma <- PlataformaTldr.COMMON,
            idioma <- IdiomaTldr.PT_BR,
            exemplos <- [
                ExemploComando(
                    "Busca por um padrao em um arquivo:",
                    "grep {{\"padrao_de_busca\"}} {{caminho/para/arquivo}}"),
                ExemploComando(
                    "Busca sem distinguir maiusculas/minusculas:",
                    "grep -i {{\"padrao\"}} {{caminho/para/arquivo}}"),
                ExemploComando(
                    "Busca recursivamente em todos os arquivos:",
                    "grep -r {{\"padrao\"}} {{caminho/para/diretorio}}"),
                ExemploComando(
                    "Mostra apenas o trecho correspondente (sem a linha inteira):",
                    "grep -o {{\"padrao\"}} {{caminho/para/arquivo}}"),
                ExemploComando(
                    "Mostra linhas ANTES e DEPOIS do contexto:",
                    "grep -C {{3}} {{\"padrao\"}} {{caminho/para/arquivo}}"),
            ]),
        CommandPage(
            comando <- "ssh",
            titulo <- "# ssh",
            descricao <- "Cliente SSH para acesso remoto seguro a outra maquina.",
            link_mais_info <- "https://www.openssh.com/",
            plataforma <- PlataformaTldr.COMMON,
            idioma <- IdiomaTldr.PT_BR,
            exemplos <- [
                ExemploComando(
                    "Conecta a um servidor remoto:",
                    "ssh {{usuario}}@{{host}}"),
                ExemploComando(
                    "Conecta usando uma porta especifica:",
                    "ssh -p {{2222}} {{usuario}}@{{host}}"),
                ExemploComando(
                    "Copia chave publica para o servidor (passwordless):",
                    "ssh-copy-id {{usuario}}@{{host}}"),
                ExemploComando(
                    "Encaminha porta local para o servidor (tunnel):",
                    "ssh -L {{8080}}:localhost:80 {{usuario}}@{{host}}"),
                ExemploComando(
                    "Executa um comando no servidor sem abrir shell:",
                    "ssh {{usuario}}@{{host}} {{comando}}"),
            ]),
        CommandPage(
            comando <- " systemctl",
            titulo <- "# systemctl",
            descricao <- "Gerencia servicos do systemd (init do Linux).",
            link_mais_info <- "https://www.freedesktop.org/software/systemd/man/systemctl.html",
            plataforma <- PlataformaTldr.LINUX,
            idioma <- IdiomaTldr.PT_BR,
            exemplos <- [
                ExemploComando(
                    "Verifica se um servico esta ativo:",
                    "systemctl status {{servico}}"),
                ExemploComando(
                    "Inicia um servico:",
                    "sudo systemctl start {{servico}}"),
                ExemploComando(
                    "Habilita um servico para iniciar no boot:",
                    "sudo systemctl enable {{servico}}"),
                ExemploComando(
                    "Reinicia um servico (apos config change):",
                    "sudo systemctl restart {{servico}}"),
                ExemploComando(
                    "Lista todos os servicos ativos:",
                    "systemctl list-units --type=service --state=running"),
            ]),
        CommandPage(
            comando <- "apt",
            titulo <- "# apt",
            descricao <- "Gerenciador de pacotes do Debian/Ubuntu/Kali.",
            link_mais_info <- "https://wiki.debian.org/Apt",
            plataforma <- PlataformaTldr.LINUX,
            idioma <- IdiomaTldr.PT_BR,
            exemplos <- [
                ExemploComando(
                    "Atualiza a lista de pacotes disponiveis:",
                    "sudo apt update"),
                ExemploComando(
                    "Instala um pacote:",
                    "sudo apt install {{pacote}}"),
                ExemploComando(
                    "Remove um pacote:",
                    "sudo apt remove {{pacote}}"),
                ExemploComando(
                    "Atualiza todos os pacotes do sistema:",
                    "sudo apt full-upgrade"),
                ExemploComando(
                    "Busca um pacote por nome:",
                    "apt search {{palavra_chave}}"),
                ExemploComando(
                    "Mostra detalhes de um pacote:",
                    "apt show {{pacote}}"),
            ]),
        CommandPage(
            comando <- "docker",
            titulo <- "# docker",
            descricao <- "Gerencia containers de aplicacao isolados.",
            link_mais_info <- "https://docs.docker.com/",
            plataforma <- PlataformaTldr.COMMON,
            idioma <- IdiomaTldr.PT_BR,
            exemplos <- [
                ExemploComando(
                    "Lista containers em execucao:",
                    "docker ps"),
                ExemploComando(
                    "Inicia um container a partir de uma imagem:",
                    "docker run {{imagem}}"),
                ExemploComando(
                    "Para um container em execucao:",
                    "docker stop {{container_id}}"),
                ExemploComando(
                    "Baixa uma imagem do Docker Hub:",
                    "docker pull {{imagem}}"),
                ExemploComando(
                    "Constroi uma imagem a partir de um Dockerfile:",
                    "docker build -t {{nome_imagem}} {{caminho/para/Dockerfile}}"),
            ]),
        CommandPage(
            comando <- "chmod",
            titulo <- "# chmod",
            descricao <- "Modifica permissoes de arquivos e diretorios.",
            link_mais_info <- "https://www.gnu.org/software/coreutils/chmod",
            plataforma <- PlataformaTldr.COMMON,
            idioma <- IdiomaTldr.PT_BR,
            exemplos <- [
                ExemploComando(
                    "Da permissao de execucao ao dono:",
                    "chmod u+x {{caminho/para/arquivo}}"),
                ExemploComando(
                    "Define permissoes para dono, grupo e outros (octal):",
                    "chmod 755 {{caminho/para/arquivo}}"),
                ExemploComando(
                    "Remove permissoes de escrita do grupo e outros:",
                    "chmod go-w {{caminho/para/arquivo}}"),
                ExemploComando(
                    "Aplica permissoes recursivamente em um diretorio:",
                    "chmod -R 755 {{caminho/para/diretorio}}"),
            ]),
    ]


funcao _init_keywords() retorna Dict[str, List[str]]:
    // Mapeia keywords naturais para nomes de comandos.
    retorne {
        "arquivar": ["tar", "zip"],
        "compactar": ["tar", "gzip"],
        "extrair": ["tar", "unzip"],
        "commitar": ["git-commit"],
        "git": ["git-commit"],
        "rede": ["nmap", "ssh"],
        "scanear": ["nmap"],
        "portas": ["nmap"],
        "audio": ["ffmpeg"],
        "video": ["ffmpeg"],
        "converter": ["ffmpeg"],
        "buscar": ["find", "grep"],
        "encontrar": ["find"],
        "arquivo": ["find"],
        "texto": ["grep"],
        "remoto": ["ssh"],
        "servidor": ["ssh", "systemctl"],
        "servico": ["systemctl"],
        "iniciar": ["systemctl"],
        "pacote": ["apt"],
        "instalar": ["apt"],
        "atualizar": ["apt"],
        "container": ["docker"],
        "permissao": ["chmod"],
    }


// ============================================================================
// 4. PARSER (markdown tldr -> CommandPage)
// ============================================================================

def parse_tldr_markdown(conteudo: str, plataforma: PlataformaTldr,
                        declare idioma: IdiomaTldr  <- IdiomaTldr.PT_BR) -> CommandPage:
    // Converte o conteudo markdown de uma pagina tldr em CommandPage.

    Formato tldr:
        // tar
        > Archiving utility.
        > More information: <https://...>.

        - Create an archive:
        `tar cf {{path/to/target.tar}} {{path/to/file1}}`
    // 
    linhas <- conteudo.strip().split("\n")
    titulo <- ""
    declare descricao_parts: List[str]  <- []
    link <- ""
    declare exemplos: List[ExemploComando]  <- []

    i <- 0
    enquanto i < len(linhas) faca:
        linha <- linhas[i].strip()
        se linha.startswith("# ") entao:
            titulo <- linha
        senao se linha.startswith("> ") entao:
            texto <- linha[2:]
            match <- re.search(r'<(https?://[^>]+)>', texto)
            se match entao:
                link <- match.group(1)
                texto <- re.sub(r'<https?://[^>]+>', '', texto).strip()
            se texto entao:
                descricao_parts.append(texto)
        senao se linha.startswith("- ") entao:
            desc <- linha[2:]
            // Procura o comando nas proximas linhas (pula linhas vazias)
            j <- i + 1
            enquanto j < len(linhas)  E  NAO  linhas[j].strip() faca:
                j <- j + 1
            se j < len(linhas)  E  linhas[j].strip().startswith("`") entao:
                cmd <- linhas[j].strip().strip("`")
                exemplos.append(ExemploComando(desc, cmd))
                i <- j
            senao se j < len(linhas)  E  j > i + 1 entao:
                i <- j - 1
        i <- i + 1

    nome_cmd <- titulo.replace("# ", "").replace(" ", "-")
    retorne CommandPage(
        comando <- nome_cmd,
        titulo <- titulo,
        descricao <- " ".join(descricao_parts),
        link_mais_info <- link,
        plataforma <- plataforma,
        idioma <- idioma,
        exemplos <- exemplos,
    )


// ============================================================================
// 5. ENGINE
// ============================================================================

classe CommandReferenceEngine:
    // Motor de busca e entrega de documentacao acessivel de comandos.

    funcao __init__(self) retorna None:
        self.comandos: List[CommandPage] = _init_comandos_sample()
        self._indice_nome: Dict[str, CommandPage] = {
            c.comando.lower(): c for c in self.comandos
        }
        self._indice_nome_canonico: Dict[str, CommandPage] = {}
        para cada c em self.comandos:
            self._indice_nome_canonico[c.comando.lower().replace("-", " ")] = c
            self._indice_nome_canonico[c.comando.lower().replace("-", "-")] = c
        self.keywords: Dict[str, List[str]] = _init_keywords()
        self.vosk_config = ConfigVosk()
        self.whisper_config = ConfigWhisperFallback()

    // -- busca -------------------------------------------------------------

    def buscar(self, query: str,
               declare idioma_pref: IdiomaTldr  <- IdiomaTldr.PT_BR) -> ResultadoBusca:
        // Busca um comando por nome ou keyword.
        q <- query.strip().lower()

        // Tentativa 1: nome exato
        se q in self._indice_nome entao:
            retorne ResultadoBusca(
                query <- query, encontrou=VERDADEIRO,
                pagina <- self._indice_nome[q],
                status <- StatusIndexacao.PRONTO,
                idioma_usado <- self._indice_nome[q].idioma)

        // Tentativa 2: nome canonico (hifens/espacos)
        q_canon <- q.replace(" ", "-")
        se q_canon in self._indice_nome entao:
            retorne ResultadoBusca(
                query <- query, encontrou=VERDADEIRO,
                pagina <- self._indice_nome[q_canon],
                status <- StatusIndexacao.PRONTO,
                idioma_usado <- self._indice_nome[q_canon].idioma)

        // Tentativa 3: keyword natural
        se q in self.keywords entao:
            alts <- self.keywords[q]
            para cada alt em alts:
                se alt in self._indice_nome entao:
                    retorne ResultadoBusca(
                        query <- query, encontrou=VERDADEIRO,
                        pagina <- self._indice_nome[alt],
                        status <- StatusIndexacao.PRONTO,
                        idioma_usado <- self._indice_nome[alt].idioma)
            retorne ResultadoBusca(
                query <- query, encontrou=FALSO,
                status <- StatusIndexacao.AUSENTE,
                alternativas <- alts)

        // Tentativa 4: fuzzy -- prefixo
        matches <- [c.comando for c in self.comandos if c.comando.lower().startswith(q)]
        se matches entao:
            retorne ResultadoBusca(
                query <- query, encontrou=FALSO,
                status <- StatusIndexacao.AUSENTE,
                alternativas <- matches[:5])

        retorne ResultadoBusca(
            query <- query, encontrou=FALSO,
            status <- StatusIndexacao.AUSENTE)

    funcao buscar_multipla(self, termos: List[str]) retorna List[ResultadoBusca]:
        // Busca varios comandos de uma vez.
        retorne [self.buscar(t) for t in termos]

    funcao todos_comandos(self) retorna List[str]:
        retorne sorted(c.comando for c in self.comandos)

    funcao comandos_por_plataforma(self, plat: PlataformaTldr) retorna List[CommandPage]:
        retorne [c for c in self.comandos if c.plataforma == plat]

    // -- Vosk (input por voz) ---------------------------------------------

    def processar_comando_voz(self, texto_reconhecido: str,
                              perfil: PerfilSaidaUsuario) -> Tuple[ResultadoBusca, EntregaOutput]:
        // Processa um comando de voz reconhecido pelo Vosk.

        Fluxo: "ajuda tar" -> strip hotword -> buscar("tar") -> entregar adaptativo
        // 
        inicio <- datetime.now()
        texto <- texto_reconhecido.strip().lower()
        hotword <- self.vosk_config.hotword.lower()

        // Strip da hotword
        se texto.startswith(hotword) entao:
            query <- texto[len(hotword):].strip()
        senao se hotword in texto entao:
            idx <- texto.index(hotword)
            query <- texto[idx + len(hotword):].strip()
        senao:
            query <- texto  // sem hotword, assume que e direto

        se NAO  query entao:
            retorne (
                ResultadoBusca(query="", encontrou=FALSO, status=StatusIndexacao.AUSENTE),
                EntregaOutput(
                    canais_ativos <- perfil.canais(),
                    tipo_consulta <- TipoConsulta.VOZ_VOSK,
                    motor_stt <- MotorSTT.VOSK,
                    latencia_ms <- 0,
                    texto_entregue <- "Nenhum comando reconhecido apos hotword.")
            )

        resultado <- self.buscar(query, perfil.idioma_pref)
        texto_saida <- self.formatar_saida(resultado, perfil)
        fim <- datetime.now()
        lat <- int((fim - inicio).total_seconds() * 1000)

        entrega <- EntregaOutput(
            canais_ativos <- perfil.canais(),
            tipo_consulta <- TipoConsulta.VOZ_VOSK,
            motor_stt <- MotorSTT.VOSK,
            latencia_ms <- lat,
            texto_entregue <- texto_saida)

        retorne resultado, entrega

    // -- Output adaptativo -------------------------------------------------

    def formatar_saida(self, resultado: ResultadoBusca,
                       perfil: PerfilSaidaUsuario) -> str:
        // Formata o texto de saida para entrega multi-canal.
        se NAO  resultado.encontrou  OU  resultado.pagina e nulo entao:
            se resultado.alternativas entao:
                alt_str <- ", ".join(resultado.alternativas)
                retorne (f"Nao encontrei '{resultado.query}'. "
                        f"Comandos parecidos: {alt_str}")
            retorne f"Nao encontrei '{resultado.query}'."

        pg <- resultado.pagina
        declare linhas: List[str]  <- []

        // Cabecalho
        linhas.append(f"Comando: {pg.comando}")
        linhas.append(f"Para que serve: {pg.descricao}")
        se pg.link_mais_info entao:
            linhas.append(f"Saiba mais: {pg.link_mais_info}")
        linhas.append("")

        // Exemplos
        linhas.append(f"Exemplos ({pg.num_exemplos}):")
        para cada (i, ex) em enumerate(pg.exemplos, 1):
            linhas.append(f"  {i}. {ex.descricao}")
            linhas.append(f"     {ex.comando}")
            linhas.append("")

        retorne "\n".join(linhas)

    funcao entregar(self, texto: str, canais: List[CanalSaida]) retorna Dict[str, str]:
        // Simula a entrega multi-canal. Retorna o que cada canal "disse".
        declare entregas: Dict[str, str]  <- {}
        para cada canal em canais:
            se canal == CanalSaida.IARA entao:
                entregas[canal.id] = (
                    f"[IARA TTS -- voz humana Chatterbox] "
                    f"Processando texto para sintese de voz natural...\n"
                    f"  -> piper --model pt-BR --text \"{texto[:80]}...\"\n"
                    f"  [Voz natural falando: \"{texto[:120]}...\"]")
            senao se canal == CanalSaida.JARVIS entao:
                entregas[canal.id] = (
                    f"[JARVIS -- espeak-ng voz robotica]\n"
                    f"  -> espeak-ng -v pt-BR \"{texto[:80]}...\"\n"
                    f"  [Voz robotica falando: \"{texto[:120]}...\"]")
            senao se canal == CanalSaida.ORCA entao:
                entregas[canal.id] = (
                    f"[ORCA -- leitor de tela via AT-SPI]\n"
                    f"  -> Texto exposto na arvore AT-SPI\n"
                    f"  -> Orca le com navegacao por tab/setas")
            senao se canal == CanalSaida.BRLTTY entao:
                entregas[canal.id] = (
                    f"[BRLTTY -- display braille]\n"
                    f"  -> Texto enviado para display braille\n"
                    f"  -> Linha tatil atualizada")
            senao se canal == CanalSaida.ALTO_CONTRASTE entao:
                entregas[canal.id] = (
                    f"[TERMINAL ALTO CONTRASTE]\n"
                    f"  Fundo preto, fonte amarela 24pt\n"
                    f"  {texto}")
            senao:
                entregas[canal.id] = texto
        retorne entregas

    // -- dual-STT ----------------------------------------------------------

    def selecionar_motor_stt(self, duracao_audio_sec: float,
                             tem_hotword: bool) -> MotorSTT:
        // Seleciona o motor STT certo para a situacao.

        Vosk: comandos curtos (<5s) com hotword. Latencia ~50ms.
        Whisper: ditado longo (>5s) ou transcricao. Latencia ~500ms-2s.
        // 
        se tem_hotword  E  duracao_audio_sec < 5.0 entao:
            retorne MotorSTT.VOSK
        se duracao_audio_sec > 10.0 entao:
            retorne MotorSTT.WHISPER
        // 5-10s: whisper se vosk falhou, senao vosk
        retorne MotorSTT.WHISPER

    // -- instalacao tldr ---------------------------------------------------

    funcao instrucoes_instalacao_tldr(self) retorna str:
        // Como instalar o tldr-pages localmente no OpenBigLinux.
        retorne (
            "INSTALACAO DO TLDR-PAGES NO OPENBIGLINUX:\n"
            "\n"
            "1. Clonar o repo:\n"
            "   sudo git clone --depth 1 https://github.com/tldr-pages/tldr.git /usr/share/republica/tldr\n"
            "\n"
            "2. Indexar (parser converte markdown -> CommandPage):\n"
            "   republica-tldr-index --src /usr/share/republica/tldr/pages\n"
            "   republica-tldr-index --src /usr/share/republica/tldr/pages.pt_BR\n"
            "\n"
            "3. Instalar cliente tldr (opcional, para terminal):\n"
            "   sudo apt install tldr   # ou: cargo install tlrc\n"
            "\n"
            "4. Instalar Vosk + modelo pt-BR:\n"
            "   sudo apt install python3-vosk\n"
            "   sudo republica-vosk-setup --model pt-BR-small\n"
            "   # Baixa vosk-model-small-pt-BR-0.3 (~40MB)\n"
            "\n"
            "5. Testar:\n"
            "   ajuda tar          (texto)\n"
            "   ajuda nmap         (texto)\n"
            "   (diga) \"ajuda git\"  (voz via Vosk)\n"
            "\n"
            "6. O sistema responde no canal certo:\n"
            "   - Cego: Iara fala + Orca expoe via AT-SPI\n"
            "   - Surdo: terminal alto contraste\n"
            "   - Tetraplegico: brltty exibe + Vosk escuta\n"
            "\n"
            "COMANDO INTEGRADOR:\n"
            "   apt install republica-command-reference\n"
            "   # Instala: tldr-pages + vosk + parser + lancador 'ajuda'"
        )

    // -- scorecard ---------------------------------------------------------

    funcao scorecard(self) retorna Dict[str, Any]:
        retorne {
            "comandos_indexados": len(self.comandos),
            "plataformas_cobertas": len(set(c.plataforma for c in self.comandos)),
            "exemplos_totais": sum(c.num_exemplos for c in self.comandos),
            "keywords_mapeadas": len(self.keywords),
            "motores_stt": len(list(MotorSTT)),
            "canais_saida": len(list(CanalSaida)),
            "vosk_latencia_alvo_ms": self.vosk_config.latencia_alvo_ms,
            "whisper_latencia_alvo_ms": self.whisper_config.latencia_alvo_ms,
            "hotword": self.vosk_config.hotword,
        }


// ============================================================================
// 6. DEMO
// ============================================================================

funcao _demo() retorna None:
    e <- CommandReferenceEngine()

    print("=" * 70)
    print("OpenCommandReference -- Documentacao Acessivel de Comandos")
    print("tldr-pages + Vosk dual-STT + Output Adaptativo")
    print("=" * 70)

    // --- Arquitetura ---
    print("\n[ARQUITETURA -- 3 CAMADAS]")
    print("""
  1. INDEXACAO: tldr-pages (~6000 comandos) clonado em /usr/share/republica/tldr/
     Parser markdown -> CommandPage. Prioridade pt_BR, fallback en.

  2. INPUT DUAL-STT:
     Vosk (50ms): hotword "ajuda" + comando curto. LEVE. Sem GPU.
     Whisper.cpp (500ms-2s): ditado longo, transcricao. PRECISO. Opcional GPU.

  3. OUTPUT ADAPTATIVO: mesmo resultado, multiplos canais simultaneos
     IARA (Chatterbox): voz humana natural -- conversa
     JARVIS (espeak-ng): voz robotica -- comando rapido
     ORCA (AT-SPI): leitor de tela -- navegacao por tab
     BRLTTY: display braille -- texto tatil
     ALTO_CONTRASTE: terminal preto/amarelo fonte 24pt
// )

    // --- Comandos indexados ---
    print(f"[COMANDOS INDEXADOS ({len(e.comandos)})]")
    para cada c em e.comandos:
        print(f"  {c.comando:20s} | {c.plataforma.id:8s} | "
              f"{c.num_exemplos} exemplos | {c.descricao[:50]}")

    // --- Busca por nome ---
    print("\n[BUSCA POR NOME -- 'tar']")
    r <- e.buscar("tar")
    print(f"  Encontrou: {r.encontrou}")
    se r.pagina entao:
        print(f"  Comando: {r.pagina.comando}")
        print(f"  Descricao: {r.pagina.descricao}")
        print(f"  Exemplos ({r.pagina.num_exemplos}):")
        para cada ex em r.pagina.exemplos:
            print(f"    {ex.descricao}")
            print(f"    -> {ex.comando}")

    // --- Busca por keyword ---
    print("\n[BUSCA POR KEYWORD -- 'arquivar']")
    r <- e.buscar("arquivar")
    print(f"  Keyword mapeada para: {r.alternativas if r.alternativas else 'N/A'}")
    se r.pagina entao:
        print(f"  Resultado: {r.pagina.comando} -- {r.pagina.descricao[:60]}")

    // --- Voz: perfil cego ---
    print("\n" + "=" * 70)
    print("[CENARIO 1 -- CEGO USA VOZ]")
    print("=" * 70)
    perfil_cego <- PerfilSaidaUsuario(
        cego <- VERDADEIRO, usa_braille=FALSO, prefere_voz_humana=VERDADEIRO)
    print(f"  Perfil: cego, prefere voz humana (Iara)")
    print(f"  Canais ativos: {[c.id for c in perfil_cego.canais()]}")
    print(f"  Usuario diz: 'ajuda tar'")
    print(f"  Vosk reconhece: 'ajuda tar' (latencia alvo: {e.vosk_config.latencia_alvo_ms}ms)")
    desempacote r, entrega <- e.processar_comando_voz("ajuda tar", perfil_cego)
    motor_nome <- entrega.motor_stt.rotulo if entrega.motor_stt else "N/A"
    print(f"  Motor STT: {motor_nome}")
    print(f"  Latencia: {entrega.latencia_ms}ms")
    print(f"  Canais entrega: {[c.id for c in entrega.canais_ativos]}")
    print(f"\n  --- ENTREGA ---")
    para cada (canal_id, msg) em e.entregar(entrega.texto_entregue, entrega.canais_ativos).items():
        print(f"\n  [{canal_id}]")
        para cada linha em msg.split("\n"):
            print(f"    {linha}")

    // --- Voz: perfil surdo ---
    print("\n" + "=" * 70)
    print("[CENARIO 2 -- SURDO DIGITA NO TERMINAL]")
    print("=" * 70)
    perfil_surdo <- PerfilSaidaUsuario(surdo=VERDADEIRO, baixa_visao=VERDADEIRO)
    print(f"  Perfil: surdo, baixa visao")
    print(f"  Canais ativos: {[c.id for c in perfil_surdo.canais()]}")
    r <- e.buscar("git-commit")
    texto <- e.formatar_saida(r, perfil_surdo)
    print(f"\n  --- ENTREGA ---")
    entregas <- e.entregar(texto, perfil_surdo.canais())
    para cada (canal_id, msg) em entregas.items():
        print(f"\n  [{canal_id}]")
        para cada linha em msg.split("\n"):
            print(f"    {linha}")

    // --- Voz: perfil tetraplegico ---
    print("\n" + "=" * 70)
    print("[CENARIO 3 -- TETRAPLEGICO USA VOZ + BRAILLE]")
    print("=" * 70)
    perfil_tetra <- PerfilSaidaUsuario(
        tetraplegico <- VERDADEIRO, usa_braille=VERDADEIRO,
        prefere_voz_humana <- FALSO)
    print(f"  Perfil: tetraplegico, usa braille, prefere Jarvis (espeak)")
    print(f"  Canais ativos: {[c.id for c in perfil_tetra.canais()]}")
    print(f"  Usuario diz: 'ajuda nmap'")
    desempacote r, entrega <- e.processar_comando_voz("ajuda nmap", perfil_tetra)
    motor_nome <- entrega.motor_stt.rotulo if entrega.motor_stt else "N/A"
    print(f"  Motor STT: {motor_nome}")
    print(f"\n  --- ENTREGA ---")
    para cada (canal_id, msg) em e.entregar(entrega.texto_entregue, entrega.canais_ativos).items():
        print(f"\n  [{canal_id}]")
        para cada linha em msg.split("\n"):
            print(f"    {linha}")

    // --- Dual-STT ---
    print("\n[DUAL-STT -- SELECAO DE MOTOR]")
    cenarios_stt <- [
        ("Comando curto com hotword", 2.0, VERDADEIRO),
        ("Comando curto sem hotword", 3.0, FALSO),
        ("Ditado medio (5-10s)", 7.0, FALSO),
        ("Ditado longo (>10s)", 30.0, FALSO),
        ("Transcricao de reuniao (5min)", 300.0, FALSO),
    ]
    for desc, dur, hot in cenarios_stt:
        motor <- e.selecionar_motor_stt(dur, hot)
        print(f"  {desc:40s} -> {motor.id:8s} ({motor.rotulo})")

    // --- Instalacao ---
    print("\n[INSTALACAO NO OPENBIGLINUX]")
    print(e.instrucoes_instalacao_tldr())

    // --- Scorecard ---
    print("\n[SCORECARD]")
    sc <- e.scorecard()
    para cada (k, v) em sc.items():
        print(f"  {k:.<30} {v}")

    // --- Parser ---
    print("\n[PARSER TLDR MARKDOWN]")
    sample_md <- """# tar

> Archiving utility.
> More information: <https://www.gnu.org/software/tar/manual/tar.html>.

- [c]reate an archive  E  write it to a [f]ile:

`tar cf {{path/to/target.tar}} {{path/to/file1 path/to/file2 ...}}`

- E[x]tract a (compressed) archive [f]ile:

`tar xf {{path/to/source.tar[.gz|.bz2|.xz]}}`
// 
    pg <- parse_tldr_markdown(sample_md, PlataformaTldr.COMMON, IdiomaTldr.EN)
    print(f"  Input: markdown bruto (8 linhas)")
    print(f"  Output: CommandPage(comando='{pg.comando}', "
          f"descricao='{pg.descricao[:40]}...', "
          f"exemplos={pg.num_exemplos})")
    para cada ex em pg.exemplos:
        print(f"    {ex.descricao[:60]}")
        print(f"    -> {ex.comando}")

    // --- FILOSOFIA ---
    print("\n" + "=" * 70)
    print("FILOSOFIA -- Documentacao como direito, nao privilegio")
    print("=" * 70)
    print("""
POR QUE SUBSTITUIR MAN PAGES:

  man tar tem 2000+ linhas. Orca le por 40 minutos.
  tldr tar tem 8 exemplos curtos. Iara le em 30 segundos.

  O cidadao nao precisa saber TUDO sobre tar.
  Precisa saber o ENESSIMO exemplo que resolve o problema AGORA.

  man pages sao para ESPECIALISTAS.
  tldr e para CIDADAOS.

DUAL-STT (VOSK + WHISPER):

  Vosk e LEVE. Roda em Raspberry Pi. Roda em maquina doada.
  Latencia de 50ms. Suficiente para "ajuda tar".

  Whisper e PRECISO. Mas pesado. Precisa de CPU decente.
  Latencia de 500ms-2s. Para ditado longo e transcricao.

  A Republica usa OS DOIS. Cada um no seu lugar:
  - Vosk no GATILHO (hotword + comando). Sempre on.
  - Whisper no aprofundamento. Sob demanda.

  Ninguem precisa escolher entre rapido e preciso.
  O sistema escolhe sozinho baseado no contexto.

OUTPUT ADAPTATIVO:

  O MESMO conhecimento. Entregue de N formas.
  Cego OUVE (Iara). Surdo VE (terminal alto contraste).
  Tetraplegico TATEIA (braille). Baixa visao LE (fonte grande).

  O conhecimento nao muda. O canal muda.
  Porque o DIREITO ao conhecimento e o mesmo (P6).
  O que muda e como cada corpo o recebe (P2).

VOZ HUMANA vs VOZ ROBOTICA:

  Iara (Chatterbox) = voz humana. Para CONVERSA.
  Jarvis (espeak) = voz robotica. Para COMANDO.

  Quando o cidadao pergunta "ajuda tar", e uma CONVERSA.
  Iara responde natural: "Tar e para arquivar. Quer os exemplos?"

  Quando o cidadao diz "parar audio", e um COMANDO.
  Jarvis responde rapido: "OK" (voz robotica, sem frescura).

  A Republica nao usa voz robotica para conversa.
  A Republica nao usa voz humana para comando.
  Cada voz no seu lugar. Como na vida.

O PRINCIPIO FINAL:

  Documentacao acessivel nao e "feature". E DIREITO.
  Um cidadao que nao sabe usar o sistema e UM REFEM.
  Um cidadao que sabe e LIVRE.

  man pages fazem refens (so especialistas leem).
  tldr + Vosk + Iara libertam (todos entendem).

  P1: Ninguem excluido. Nem por deficiencia. Nem por documento-ao.
  P6: Conhecimento para todos. Sem excecao. Sem nuvem. Sem Big Tech.
// )


se __name__ == "__main__" entao:
    _demo()

```
