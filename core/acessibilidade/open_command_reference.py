#!/usr/bin/env python3
"""
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
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field
from collections import defaultdict
from datetime import datetime
import re


# ============================================================================
# 1. ENUMS
# ============================================================================

class PlataformaTldr(Enum):
    """Plataformas de comandos no tldr-pages."""
    COMMON = ("common", "Comandos comuns a todas as plataformas (~1000)")
    LINUX = ("linux", "Comandos especificos Linux (~1000)")
    OSX = ("osx", "macOS (~369)")
    WINDOWS = ("windows", "Windows (~301)")
    ANDROID = ("android", "Android (22)")
    SUNOS = ("sunos", "SunOS/Solaris (11)")
    FREEBSD = ("freebsd", "FreeBSD")
    NETBSD = ("netbsd", "NetBSD")
    OPENBSD = ("openbsd", "OpenBSD")
    CISCO_IOS = ("cisco-ios", "Cisco IOS")
    DOS = ("dos", "DOS")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class IdiomaTldr(Enum):
    """Idiomas do tldr-pages relevantes para a Republica."""
    PT_BR = ("pt_BR", "Portugues Brasileiro (prioridade)")
    PT_PT = ("pt_PT", "Portugues de Portugal")
    EN = ("en", "Ingles (fallback universal)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class MotorSTT(Enum):
    """Motores de Speech-to-Text disponiveis (arquitetura dual-STT)."""
    VOSK = ("vosk", "Vosk -- leve, ~50ms, comandos curtos e hotword")
    WHISPER = ("whisper", "Whisper.cpp -- preciso, ~500ms-2s, ditado longo")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class CanalSaida(Enum):
    """Canais de output adaptativo para entrega da documentacao."""
    IARA = ("iara", "Iara (Chatterbox TTS) -- voz humana natural, conversa")
    JARVIS = ("jarvis", "Jarvis (espeak-ng) -- voz robotica, comando rapido")
    ORCA = ("orca", "Orca (AT-SPI) -- leitor de tela, navegacao por tab")
    BRLTTY = ("brltty", "Brltty -- display braille, texto tatil")
    ALTO_CONTRASTE = ("alto_contraste", "Terminal alto contraste + fonte grande")
    TERMINAL_PADRAO = ("terminal", "Terminal padrao (sem adaptacao)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoConsulta(Enum):
    """Como o usuario consultou o sistema."""
    VOZ_VOSK = ("voz_vosk", "Voz via Vosk (hotword + comando)")
    VOZ_WHISPER = ("voz_whisper", "Voz via Whisper (ditado longo)")
    TEXTO = ("texto", "Digitado no terminal")
    IDE = ("ide", "Consulta automatica da OpenInclusiveIDE")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class StatusIndexacao(Enum):
    """Status da indexacao de uma pagina tldr."""
    PRONTO = ("pronto", "Indexada e busca funcionando")
    PARCIAL = ("parcial", "Indexada mas sem traducao pt_BR")
    FALLBACK_EN = ("fallback_en", "So existe em ingles")
    AUSENTE = ("ausente", "Comando nao encontrado no tldr")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


# ============================================================================
# 2. DATACLASSES
# ============================================================================

@dataclass
class ExemploComando:
    """Um exemplo de uso de um comando (uma linha do tldr)."""
    descricao: str        # "- [c]reate an archive and write it to a [f]ile:"
    comando: str          # "tar cf {{path/to/target.tar}} {{path/to/file1 path/to/file2 ...}}"


@dataclass
class CommandPage:
    """Uma pagina completa de comando do tldr-pages, parseada."""
    comando: str                          # "tar", "git-commit", "nmap"
    titulo: str                           # "# tar"
    descricao: str                        # "> Archiving utility."
    link_mais_info: str = ""              # "<https://...>"
    plataforma: PlataformaTldr = PlataformaTldr.COMMON
    idioma: IdiomaTldr = IdiomaTldr.PT_BR
    exemplos: List[ExemploComando] = field(default_factory=list)

    @property
    def num_exemplos(self) -> int:
        return len(self.exemplos)


@dataclass
class ConfigVosk:
    """Configuracao do motor Vosk para comando de voz."""
    modelo: str = "vosk-model-small-pt-BR-0.3"
    modelo_path: str = "/usr/share/republica/models/vosk-pt-br"
    sample_rate: int = 16000
    latencia_alvo_ms: int = 50
    hotword: str = "ajuda"
    grammar_comandos: List[str] = field(default_factory=lambda: [
        "ajuda", "parar", "repetir", "proximo", "anterior",
        "mais lento", "mais rapido", "exemplo",
    ])

    @property
    def ativo(self) -> bool:
        """No OpenBigLinux, Vosk e o motor STT primario para comandos."""
        return True


@dataclass
class ConfigWhisperFallback:
    """Configuracao do whisper.cpp como fallback STT."""
    modelo: str = "ggml-base.pt-BR.bin"
    modelo_path: str = "/usr/share/republica/models/whisper-pt-br"
    latencia_alvo_ms: int = 2000
    ativa_em: List[str] = field(default_factory=lambda: [
        "vosk_falhou",
        "ditado_longo",
        "transcricao_audio",
        "transcricao_video",
    ])


@dataclass
class ResultadoBusca:
    """Resultado de uma busca por comando."""
    query: str
    encontrou: bool
    pagina: Optional[CommandPage] = None
    status: StatusIndexacao = StatusIndexacao.AUSENTE
    alternativas: List[str] = field(default_factory=list)
    idioma_usado: IdiomaTldr = IdiomaTldr.EN


@dataclass
class EntregaOutput:
    """Como o resultado foi entregue ao usuario (multi-canal)."""
    canais_ativos: List[CanalSaida] = field(default_factory=list)
    tipo_consulta: TipoConsulta = TipoConsulta.TEXTO
    motor_stt: Optional[MotorSTT] = None
    latencia_ms: int = 0
    texto_entregue: str = ""


@dataclass
class PerfilSaidaUsuario:
    """Perfil de output do usuario (quais canais ativar)."""
    cego: bool = False
    surdo: bool = False
    baixa_visao: bool = False
    tetraplegico: bool = False
    usa_braille: bool = False
    prefere_voz_humana: bool = True  # Iara > Jarvis
    idioma_pref: IdiomaTldr = IdiomaTldr.PT_BR

    def canais(self) -> List[CanalSaida]:
        """Determina quais canais de output ativar baseado no perfil."""
        canais: List[CanalSaida] = []
        if self.cego and self.usa_braille:
            canais.extend([CanalSaida.IARA, CanalSaida.BRLTTY])
        elif self.cego:
            canais.extend([CanalSaida.IARA, CanalSaida.ORCA])
        if self.surdo or self.baixa_visao:
            canais.append(CanalSaida.ALTO_CONTRASTE)
        if self.tetraplegico and self.usa_braille:
            canais.append(CanalSaida.BRLTTY)
        if not canais:
            canais.append(CanalSaida.TERMINAL_PADRAO)
        if self.cego and not self.prefere_voz_humana:
            # Remove IARA, adiciona JARVIS
            canais = [c for c in canais if c != CanalSaida.IARA]
            canais.insert(0, CanalSaida.JARVIS)
        return list(dict.fromkeys(canais))  # dedup preservando ordem


# ============================================================================
# 3. DADOS: COMANDOS SAMPLE (simula o que o tldr-pages fornece)
# ============================================================================

def _init_comandos_sample() -> List[CommandPage]:
    """Comandos de exemplo que simulam o parse do tldr-pages.
    No deploy real, estes vem do clone em /usr/share/republica/tldr/."""
    return [
        CommandPage(
            comando="tar",
            titulo="# tar",
            descricao="Utilidade de arquivamento. Combinado com gzip ou bzip2 para compressao.",
            link_mais_info="https://www.gnu.org/software/tar/manual/tar.html",
            plataforma=PlataformaTldr.COMMON,
            idioma=IdiomaTldr.PT_BR,
            exemplos=[
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
            comando="git-commit",
            titulo="# git commit",
            descricao="Registra alteracoes no repositorio.",
            link_mais_info="https://git-scm.com/docs/git-commit",
            plataforma=PlataformaTldr.COMMON,
            idioma=IdiomaTldr.PT_BR,
            exemplos=[
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
            comando="nmap",
            titulo="# nmap",
            descricao="Scanner de rede. Descobre hosts, portas abertas, servicos e sistema operacional.",
            link_mais_info="https://nmap.org/",
            plataforma=PlataformaTldr.LINUX,
            idioma=IdiomaTldr.PT_BR,
            exemplos=[
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
            comando="ffmpeg",
            titulo="# ffmpeg",
            descricao="Conversor de video/audio. Grava, transmite, processa multimidia.",
            link_mais_info="https://ffmpeg.org/ffmpeg.html",
            plataforma=PlataformaTldr.COMMON,
            idioma=IdiomaTldr.PT_BR,
            exemplos=[
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
            comando="find",
            titulo="# find",
            descricao="Busca arquivos e diretorios por nome, tipo, tamanho, data.",
            link_mais_info="https://www.gnu.org/software/findutils/",
            plataforma=PlataformaTldr.COMMON,
            idioma=IdiomaTldr.PT_BR,
            exemplos=[
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
            comando="grep",
            titulo="# grep",
            descricao="Busca padroes de texto dentro de arquivos.",
            link_mais_info="https://www.gnu.org/software/grep/",
            plataforma=PlataformaTldr.COMMON,
            idioma=IdiomaTldr.PT_BR,
            exemplos=[
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
            comando="ssh",
            titulo="# ssh",
            descricao="Cliente SSH para acesso remoto seguro a outra maquina.",
            link_mais_info="https://www.openssh.com/",
            plataforma=PlataformaTldr.COMMON,
            idioma=IdiomaTldr.PT_BR,
            exemplos=[
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
            comando=" systemctl",
            titulo="# systemctl",
            descricao="Gerencia servicos do systemd (init do Linux).",
            link_mais_info="https://www.freedesktop.org/software/systemd/man/systemctl.html",
            plataforma=PlataformaTldr.LINUX,
            idioma=IdiomaTldr.PT_BR,
            exemplos=[
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
            comando="apt",
            titulo="# apt",
            descricao="Gerenciador de pacotes do Debian/Ubuntu/Kali.",
            link_mais_info="https://wiki.debian.org/Apt",
            plataforma=PlataformaTldr.LINUX,
            idioma=IdiomaTldr.PT_BR,
            exemplos=[
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
            comando="docker",
            titulo="# docker",
            descricao="Gerencia containers de aplicacao isolados.",
            link_mais_info="https://docs.docker.com/",
            plataforma=PlataformaTldr.COMMON,
            idioma=IdiomaTldr.PT_BR,
            exemplos=[
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
            comando="chmod",
            titulo="# chmod",
            descricao="Modifica permissoes de arquivos e diretorios.",
            link_mais_info="https://www.gnu.org/software/coreutils/chmod",
            plataforma=PlataformaTldr.COMMON,
            idioma=IdiomaTldr.PT_BR,
            exemplos=[
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


def _init_keywords() -> Dict[str, List[str]]:
    """Mapeia keywords naturais para nomes de comandos."""
    return {
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


# ============================================================================
# 4. PARSER (markdown tldr -> CommandPage)
# ============================================================================

def parse_tldr_markdown(conteudo: str, plataforma: PlataformaTldr,
                        idioma: IdiomaTldr = IdiomaTldr.PT_BR) -> CommandPage:
    """Converte o conteudo markdown de uma pagina tldr em CommandPage.

    Formato tldr:
        # tar
        > Archiving utility.
        > More information: <https://...>.

        - Create an archive:
        `tar cf {{path/to/target.tar}} {{path/to/file1}}`
    """
    linhas = conteudo.strip().split("\n")
    titulo = ""
    descricao_parts: List[str] = []
    link = ""
    exemplos: List[ExemploComando] = []

    i = 0
    while i < len(linhas):
        linha = linhas[i].strip()
        if linha.startswith("# "):
            titulo = linha
        elif linha.startswith("> "):
            texto = linha[2:]
            match = re.search(r'<(https?://[^>]+)>', texto)
            if match:
                link = match.group(1)
                texto = re.sub(r'<https?://[^>]+>', '', texto).strip()
            if texto:
                descricao_parts.append(texto)
        elif linha.startswith("- "):
            desc = linha[2:]
            # Procura o comando nas proximas linhas (pula linhas vazias)
            j = i + 1
            while j < len(linhas) and not linhas[j].strip():
                j += 1
            if j < len(linhas) and linhas[j].strip().startswith("`"):
                cmd = linhas[j].strip().strip("`")
                exemplos.append(ExemploComando(desc, cmd))
                i = j
            elif j < len(linhas) and j > i + 1:
                i = j - 1
        i += 1

    nome_cmd = titulo.replace("# ", "").replace(" ", "-")
    return CommandPage(
        comando=nome_cmd,
        titulo=titulo,
        descricao=" ".join(descricao_parts),
        link_mais_info=link,
        plataforma=plataforma,
        idioma=idioma,
        exemplos=exemplos,
    )


# ============================================================================
# 5. ENGINE
# ============================================================================

class CommandReferenceEngine:
    """Motor de busca e entrega de documentacao acessivel de comandos."""

    def __init__(self) -> None:
        self.comandos: List[CommandPage] = _init_comandos_sample()
        self._indice_nome: Dict[str, CommandPage] = {
            c.comando.lower(): c for c in self.comandos
        }
        self._indice_nome_canonico: Dict[str, CommandPage] = {}
        for c in self.comandos:
            self._indice_nome_canonico[c.comando.lower().replace("-", " ")] = c
            self._indice_nome_canonico[c.comando.lower().replace("-", "-")] = c
        self.keywords: Dict[str, List[str]] = _init_keywords()
        self.vosk_config = ConfigVosk()
        self.whisper_config = ConfigWhisperFallback()

    # -- busca -------------------------------------------------------------

    def buscar(self, query: str,
               idioma_pref: IdiomaTldr = IdiomaTldr.PT_BR) -> ResultadoBusca:
        """Busca um comando por nome ou keyword."""
        q = query.strip().lower()

        # Tentativa 1: nome exato
        if q in self._indice_nome:
            return ResultadoBusca(
                query=query, encontrou=True,
                pagina=self._indice_nome[q],
                status=StatusIndexacao.PRONTO,
                idioma_usado=self._indice_nome[q].idioma)

        # Tentativa 2: nome canonico (hifens/espacos)
        q_canon = q.replace(" ", "-")
        if q_canon in self._indice_nome:
            return ResultadoBusca(
                query=query, encontrou=True,
                pagina=self._indice_nome[q_canon],
                status=StatusIndexacao.PRONTO,
                idioma_usado=self._indice_nome[q_canon].idioma)

        # Tentativa 3: keyword natural
        if q in self.keywords:
            alts = self.keywords[q]
            for alt in alts:
                if alt in self._indice_nome:
                    return ResultadoBusca(
                        query=query, encontrou=True,
                        pagina=self._indice_nome[alt],
                        status=StatusIndexacao.PRONTO,
                        idioma_usado=self._indice_nome[alt].idioma)
            return ResultadoBusca(
                query=query, encontrou=False,
                status=StatusIndexacao.AUSENTE,
                alternativas=alts)

        # Tentativa 4: fuzzy -- prefixo
        matches = [c.comando for c in self.comandos if c.comando.lower().startswith(q)]
        if matches:
            return ResultadoBusca(
                query=query, encontrou=False,
                status=StatusIndexacao.AUSENTE,
                alternativas=matches[:5])

        return ResultadoBusca(
            query=query, encontrou=False,
            status=StatusIndexacao.AUSENTE)

    def buscar_multipla(self, termos: List[str]) -> List[ResultadoBusca]:
        """Busca varios comandos de uma vez."""
        return [self.buscar(t) for t in termos]

    def todos_comandos(self) -> List[str]:
        return sorted(c.comando for c in self.comandos)

    def comandos_por_plataforma(self, plat: PlataformaTldr) -> List[CommandPage]:
        return [c for c in self.comandos if c.plataforma == plat]

    # -- Vosk (input por voz) ---------------------------------------------

    def processar_comando_voz(self, texto_reconhecido: str,
                              perfil: PerfilSaidaUsuario) -> Tuple[ResultadoBusca, EntregaOutput]:
        """Processa um comando de voz reconhecido pelo Vosk.

        Fluxo: "ajuda tar" -> strip hotword -> buscar("tar") -> entregar adaptativo
        """
        inicio = datetime.now()
        texto = texto_reconhecido.strip().lower()
        hotword = self.vosk_config.hotword.lower()

        # Strip da hotword
        if texto.startswith(hotword):
            query = texto[len(hotword):].strip()
        elif hotword in texto:
            idx = texto.index(hotword)
            query = texto[idx + len(hotword):].strip()
        else:
            query = texto  # sem hotword, assume que e direto

        if not query:
            return (
                ResultadoBusca(query="", encontrou=False, status=StatusIndexacao.AUSENTE),
                EntregaOutput(
                    canais_ativos=perfil.canais(),
                    tipo_consulta=TipoConsulta.VOZ_VOSK,
                    motor_stt=MotorSTT.VOSK,
                    latencia_ms=0,
                    texto_entregue="Nenhum comando reconhecido apos hotword.")
            )

        resultado = self.buscar(query, perfil.idioma_pref)
        texto_saida = self.formatar_saida(resultado, perfil)
        fim = datetime.now()
        lat = int((fim - inicio).total_seconds() * 1000)

        entrega = EntregaOutput(
            canais_ativos=perfil.canais(),
            tipo_consulta=TipoConsulta.VOZ_VOSK,
            motor_stt=MotorSTT.VOSK,
            latencia_ms=lat,
            texto_entregue=texto_saida)

        return resultado, entrega

    # -- Output adaptativo -------------------------------------------------

    def formatar_saida(self, resultado: ResultadoBusca,
                       perfil: PerfilSaidaUsuario) -> str:
        """Formata o texto de saida para entrega multi-canal."""
        if not resultado.encontrou or resultado.pagina is None:
            if resultado.alternativas:
                alt_str = ", ".join(resultado.alternativas)
                return (f"Nao encontrei '{resultado.query}'. "
                        f"Comandos parecidos: {alt_str}")
            return f"Nao encontrei '{resultado.query}'."

        pg = resultado.pagina
        linhas: List[str] = []

        # Cabecalho
        linhas.append(f"Comando: {pg.comando}")
        linhas.append(f"Para que serve: {pg.descricao}")
        if pg.link_mais_info:
            linhas.append(f"Saiba mais: {pg.link_mais_info}")
        linhas.append("")

        # Exemplos
        linhas.append(f"Exemplos ({pg.num_exemplos}):")
        for i, ex in enumerate(pg.exemplos, 1):
            linhas.append(f"  {i}. {ex.descricao}")
            linhas.append(f"     {ex.comando}")
            linhas.append("")

        return "\n".join(linhas)

    def entregar(self, texto: str, canais: List[CanalSaida]) -> Dict[str, str]:
        """Simula a entrega multi-canal. Retorna o que cada canal "disse"."""
        entregas: Dict[str, str] = {}
        for canal in canais:
            if canal == CanalSaida.IARA:
                entregas[canal.id] = (
                    f"[IARA TTS -- voz humana Chatterbox] "
                    f"Processando texto para sintese de voz natural...\n"
                    f"  -> piper --model pt-BR --text \"{texto[:80]}...\"\n"
                    f"  [Voz natural falando: \"{texto[:120]}...\"]")
            elif canal == CanalSaida.JARVIS:
                entregas[canal.id] = (
                    f"[JARVIS -- espeak-ng voz robotica]\n"
                    f"  -> espeak-ng -v pt-BR \"{texto[:80]}...\"\n"
                    f"  [Voz robotica falando: \"{texto[:120]}...\"]")
            elif canal == CanalSaida.ORCA:
                entregas[canal.id] = (
                    f"[ORCA -- leitor de tela via AT-SPI]\n"
                    f"  -> Texto exposto na arvore AT-SPI\n"
                    f"  -> Orca le com navegacao por tab/setas")
            elif canal == CanalSaida.BRLTTY:
                entregas[canal.id] = (
                    f"[BRLTTY -- display braille]\n"
                    f"  -> Texto enviado para display braille\n"
                    f"  -> Linha tatil atualizada")
            elif canal == CanalSaida.ALTO_CONTRASTE:
                entregas[canal.id] = (
                    f"[TERMINAL ALTO CONTRASTE]\n"
                    f"  Fundo preto, fonte amarela 24pt\n"
                    f"  {texto}")
            else:
                entregas[canal.id] = texto
        return entregas

    # -- dual-STT ----------------------------------------------------------

    def selecionar_motor_stt(self, duracao_audio_sec: float,
                             tem_hotword: bool) -> MotorSTT:
        """Seleciona o motor STT certo para a situacao.

        Vosk: comandos curtos (<5s) com hotword. Latencia ~50ms.
        Whisper: ditado longo (>5s) ou transcricao. Latencia ~500ms-2s.
        """
        if tem_hotword and duracao_audio_sec < 5.0:
            return MotorSTT.VOSK
        if duracao_audio_sec > 10.0:
            return MotorSTT.WHISPER
        # 5-10s: whisper se vosk falhou, senao vosk
        return MotorSTT.WHISPER

    # -- instalacao tldr ---------------------------------------------------

    def instrucoes_instalacao_tldr(self) -> str:
        """Como instalar o tldr-pages localmente no OpenBigLinux."""
        return (
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

    # -- scorecard ---------------------------------------------------------

    def scorecard(self) -> Dict[str, Any]:
        return {
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


# ============================================================================
# 6. DEMO
# ============================================================================

def _demo() -> None:
    e = CommandReferenceEngine()

    print("=" * 70)
    print("OpenCommandReference -- Documentacao Acessivel de Comandos")
    print("tldr-pages + Vosk dual-STT + Output Adaptativo")
    print("=" * 70)

    # --- Arquitetura ---
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
""")

    # --- Comandos indexados ---
    print(f"[COMANDOS INDEXADOS ({len(e.comandos)})]")
    for c in e.comandos:
        print(f"  {c.comando:20s} | {c.plataforma.id:8s} | "
              f"{c.num_exemplos} exemplos | {c.descricao[:50]}")

    # --- Busca por nome ---
    print("\n[BUSCA POR NOME -- 'tar']")
    r = e.buscar("tar")
    print(f"  Encontrou: {r.encontrou}")
    if r.pagina:
        print(f"  Comando: {r.pagina.comando}")
        print(f"  Descricao: {r.pagina.descricao}")
        print(f"  Exemplos ({r.pagina.num_exemplos}):")
        for ex in r.pagina.exemplos:
            print(f"    {ex.descricao}")
            print(f"    -> {ex.comando}")

    # --- Busca por keyword ---
    print("\n[BUSCA POR KEYWORD -- 'arquivar']")
    r = e.buscar("arquivar")
    print(f"  Keyword mapeada para: {r.alternativas if r.alternativas else 'N/A'}")
    if r.pagina:
        print(f"  Resultado: {r.pagina.comando} -- {r.pagina.descricao[:60]}")

    # --- Voz: perfil cego ---
    print("\n" + "=" * 70)
    print("[CENARIO 1 -- CEGO USA VOZ]")
    print("=" * 70)
    perfil_cego = PerfilSaidaUsuario(
        cego=True, usa_braille=False, prefere_voz_humana=True)
    print(f"  Perfil: cego, prefere voz humana (Iara)")
    print(f"  Canais ativos: {[c.id for c in perfil_cego.canais()]}")
    print(f"  Usuario diz: 'ajuda tar'")
    print(f"  Vosk reconhece: 'ajuda tar' (latencia alvo: {e.vosk_config.latencia_alvo_ms}ms)")
    r, entrega = e.processar_comando_voz("ajuda tar", perfil_cego)
    motor_nome = entrega.motor_stt.rotulo if entrega.motor_stt else "N/A"
    print(f"  Motor STT: {motor_nome}")
    print(f"  Latencia: {entrega.latencia_ms}ms")
    print(f"  Canais entrega: {[c.id for c in entrega.canais_ativos]}")
    print(f"\n  --- ENTREGA ---")
    for canal_id, msg in e.entregar(entrega.texto_entregue, entrega.canais_ativos).items():
        print(f"\n  [{canal_id}]")
        for linha in msg.split("\n"):
            print(f"    {linha}")

    # --- Voz: perfil surdo ---
    print("\n" + "=" * 70)
    print("[CENARIO 2 -- SURDO DIGITA NO TERMINAL]")
    print("=" * 70)
    perfil_surdo = PerfilSaidaUsuario(surdo=True, baixa_visao=True)
    print(f"  Perfil: surdo, baixa visao")
    print(f"  Canais ativos: {[c.id for c in perfil_surdo.canais()]}")
    r = e.buscar("git-commit")
    texto = e.formatar_saida(r, perfil_surdo)
    print(f"\n  --- ENTREGA ---")
    entregas = e.entregar(texto, perfil_surdo.canais())
    for canal_id, msg in entregas.items():
        print(f"\n  [{canal_id}]")
        for linha in msg.split("\n"):
            print(f"    {linha}")

    # --- Voz: perfil tetraplegico ---
    print("\n" + "=" * 70)
    print("[CENARIO 3 -- TETRAPLEGICO USA VOZ + BRAILLE]")
    print("=" * 70)
    perfil_tetra = PerfilSaidaUsuario(
        tetraplegico=True, usa_braille=True,
        prefere_voz_humana=False)
    print(f"  Perfil: tetraplegico, usa braille, prefere Jarvis (espeak)")
    print(f"  Canais ativos: {[c.id for c in perfil_tetra.canais()]}")
    print(f"  Usuario diz: 'ajuda nmap'")
    r, entrega = e.processar_comando_voz("ajuda nmap", perfil_tetra)
    motor_nome = entrega.motor_stt.rotulo if entrega.motor_stt else "N/A"
    print(f"  Motor STT: {motor_nome}")
    print(f"\n  --- ENTREGA ---")
    for canal_id, msg in e.entregar(entrega.texto_entregue, entrega.canais_ativos).items():
        print(f"\n  [{canal_id}]")
        for linha in msg.split("\n"):
            print(f"    {linha}")

    # --- Dual-STT ---
    print("\n[DUAL-STT -- SELECAO DE MOTOR]")
    cenarios_stt = [
        ("Comando curto com hotword", 2.0, True),
        ("Comando curto sem hotword", 3.0, False),
        ("Ditado medio (5-10s)", 7.0, False),
        ("Ditado longo (>10s)", 30.0, False),
        ("Transcricao de reuniao (5min)", 300.0, False),
    ]
    for desc, dur, hot in cenarios_stt:
        motor = e.selecionar_motor_stt(dur, hot)
        print(f"  {desc:40s} -> {motor.id:8s} ({motor.rotulo})")

    # --- Instalacao ---
    print("\n[INSTALACAO NO OPENBIGLINUX]")
    print(e.instrucoes_instalacao_tldr())

    # --- Scorecard ---
    print("\n[SCORECARD]")
    sc = e.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<30} {v}")

    # --- Parser ---
    print("\n[PARSER TLDR MARKDOWN]")
    sample_md = """# tar

> Archiving utility.
> More information: <https://www.gnu.org/software/tar/manual/tar.html>.

- [c]reate an archive and write it to a [f]ile:

`tar cf {{path/to/target.tar}} {{path/to/file1 path/to/file2 ...}}`

- E[x]tract a (compressed) archive [f]ile:

`tar xf {{path/to/source.tar[.gz|.bz2|.xz]}}`
"""
    pg = parse_tldr_markdown(sample_md, PlataformaTldr.COMMON, IdiomaTldr.EN)
    print(f"  Input: markdown bruto (8 linhas)")
    print(f"  Output: CommandPage(comando='{pg.comando}', "
          f"descricao='{pg.descricao[:40]}...', "
          f"exemplos={pg.num_exemplos})")
    for ex in pg.exemplos:
        print(f"    {ex.descricao[:60]}")
        print(f"    -> {ex.comando}")

    # --- FILOSOFIA ---
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
""")


if __name__ == "__main__":
    _demo()
