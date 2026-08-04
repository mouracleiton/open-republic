#!/usr/bin/env python3
"""
OpenBigLinux -- Distro Base da Republica (Kali 2025.1 hardened + Acessibilidade + IA Local)
=============================================================================
"Todos saibam melhorar a seguranca de sistemas dentro da Republica."

A Republica usa Kali Linux 2025.1 como BASE da sua distro (lançado fevereiro 2025).
Nao por ser "hacker". Porque SEGURANCA E CULTURA, nao especialidade.

VERSAO BASE ATUALIZADA (2025):
- Kali Linux 2025.1 (base Debian 12 Bookworm, kernel 6.12+)
- BigLinux 3.2+ elementos de UI/UX (tema, menus, acessibilidade integrada)
- Hardening Republica: AppArmor, ufw, fail2ban, auditd, kernel lockdown
- Stack de acessibilidade completa (Orca 46+, espeak-ng, brltty 6.7+)
- IA Local: whisper.cpp 1.7+, piper-tts 1.2+, llama.cpp b3882+, vosk-api 0.3.45

POR QUE KALI (e nao Ubuntu/Fedora/BigLinux puro):

1. FERRAMENTAS DE SEGURANCA NATIVAS:
   Kali vem com 600+ ferramentas de pentest, forense, auditoria.
   O cidadao da Republica NAO precisa instalar nmap, wireshark, burpsuite.
   Ja estao la. Abrir = aprender. Usar = entender. Entender = defender.

2. CULTURA DE SEGURANCA DESDE O DIA 1:
   Crianca que cresce na Republica aprende que rede e RESPIRACAO do sistema.
   Aprende que senha fraca e falha. Aprende que criptografia e padrao.
   Aprende que auditar e rotina, nao ataque. "Saber atacar = saber defender."

3. DEBIAN POR BAIXO:
   Kali e Debian-based. A stack de acessibilidade (Orca, espeak, brltty)
   roda nativamente. Pacotes .deb funcionam. apt install republica-full.

4. COMUNIDADE DE SEGURANCA AMPLA:
   Kali tem a maior comunidade de seguranca do planeta Linux.
   Documentacao abundante. Tutoriais em portugues. Suporte foro.

O QUE A REPUBLICA MUDA NO KALI:

1. NAO RODA COMO ROOT por padrao (Kali antigo rodava).
   Usuario republica com sudo. Root separado. Auditoria de privilege.

2. ACESSIBILIDADE ATIVADA POR PADRAO:
   Orca, espeak-ng, brltty, at-spi2 instalados e ATIVOS.
   Kali puro nao tem isso. A Republica adiciona.

3. IA LOCAL INSTALADA:
   Vosk (comando de voz ~50ms), Whisper.cpp (ditado/transcricao),
   Piper (TTS pt-BR), Kokoro+Chatterbox (voz Iara), llama.cpp (LLM local),
   tldr-pages (documentacao acessivel de ~6000 comandos).
   Arquitetura dual-STT: Vosk no gatilho, Whisper no aprofundamento.
   Tudo rodando no processador da Republica (RISC-V ou x86).

4. STACK DA REPUBLICA INSTALADA:
   republica-telefonista, republica-ide, republica-energy,
   republica-cybersecurity, republica-accessibility.

5. HARDDENING AUTOMATICO:
   Firewall ativo. SSH com chave (nao senha). Fail2ban. AppArmor.
   A Republica ENDURECE o Kali para uso diario (nao so pentest).

ALINHAMENTO CONSTITUCIONAL:
- P1: Seguranca nao e privilegio de especialista. E direito de todos.
- P2: Autonomia corporal digital: seus dados, sua rede, sua defesa.
- P4: Transparencia radical: ferramentas de auditoria para TODOS.
- P9 (Soberania): Distro propria = soberania digital completa.

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field
from collections import defaultdict
from datetime import datetime


# ============================================================================
# 1. ENUMS
# ============================================================================

class CamadaDistro(Enum):
    """Camadas da distro Republica/Kali."""
    KERNEL = ("kernel", "Kernel Linux (Debian base)")
    HARDENING = ("hardening", "Hardening (firewall, apparmor, fail2ban)")
    ACESSIBILIDADE = ("acessibilidade", "Camada de Acessibilidade (Orca, brltty, espeak)")
    IA_LOCAL = ("ia_local", "IA Local (whisper, piper, llama)")
    SEGURANCA = ("seguranca", "Ferramentas de Seguranca (Kali pentest suite)")
    REPUBLICA = ("republica", "Stack da Republica (telefonista, IDE, energy)")
    UI = ("ui", "Interface (GNOME acessivel + OpenInclusiveIDE)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoFerramentaSeguranca(Enum):
    """Categorias de ferramentas de seguranca do Kali."""
    RECONHECIMENTO = ("reconhecimento", "Reconhecimento (nmap, masscan, recon-ng)")
    ANALISE_VULNERABILIDADE = ("vuln", "Analise de vulnerabilidade (nikto, lynis, nuclei)")
    EXPLORACAO = ("exploracao", "Exploracao (metasploit, sqlmap)")
    SNIFFING = ("sniffing", "Sniffing e analise de rede (wireshark, tcpdump, bettercap)")
    SENHAS = ("senhas", "Quebra de senhas e hashes (hashcat, john, hydra)")
    FORENSE = ("forense", "Forense digital (autopsy, volatility, sleuthkit)")
    CRIPTOGRAFIA = ("criptografia", "Criptografia e esteganografia (openssl, steghide)")
    WEB = ("web", "Seguranca web (burpsuite, zap, wfuzz)")
    WIRELESS = ("wireless", "Wireless (aircrack-ng, wifite, kismet)")
    SOCIAL = ("social", "Engenharia social (set, maltego)")
    REVERSO = ("reverso", "Engenharia reversa (ghidra, radare2, gdb)")
    AUDITORIA = ("auditoria", "Auditoria e compliance (lynis, openscap)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoFerramentaAcessibilidade(Enum):
    """Ferramentas de acessibilidade nativas do Linux."""
    ORCA = ("orca", "Orca -- leitor de tela para cegos")
    ESPEAK = ("espeak", "espeak-ng -- sintetizador de voz TTS")
    BRLTTY = ("brltty", "brltty -- driver para display Braille")
    AT_SPI = ("at_spi", "at-spi2 -- framework de acessibilidade")
    CARIBOU = ("caribou", "Caribou -- teclado virtual na tela")
    MOUSETWEAKS = ("mousetweaks", "Mousetweaks -- mouse adaptado (switch/eye tracker)")
    ONBOARD = ("onboard", "Onboard -- teclado virtual alternativo")
    MAGNIFIER = ("magnifier", "GNOME Magnifier -- lupa de tela para baixa visao")
    HIGH_CONTRAST = ("high_contrast", "High Contrast -- tema de alto contraste")
    STICKY_KEYS = ("sticky_keys", "Sticky Keys -- teclas de aderencia (motora)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoIAlocal(Enum):
    """Modelos de IA que rodam localmente na distro."""
    VOSK = ("vosk", "Vosk -- STT leve (~50ms) para hotword + comandos curtos")
    WHISPER = ("whisper", "Whisper.cpp -- STT preciso (~500ms-2s) para ditado longo")
    PIPER = ("piper", "Piper TTS -- sintese de voz em pt-BR offline")
    LLAMA = ("llama", "llama.cpp -- LLM local (sem nuvem, sem Big Tech)")
    LLAVA = ("llava", "LLaVA -- visao computacional (descricao de cena)")
    COQUI = ("coqui", "Coqui TTS -- clonagem de voz para Telefonista")
    KOKORO = ("kokoro", "Kokoro TTS -- voz natural para Iara (conversa)")
    CHATTERBOX = ("chatterbox", "Chatterbox TTS -- voz humana para Iara (conversa)")
    FACE_DETECT = ("face_detect", "Detecao facial (reconhecimento de pessoas para cegos)")
    SOUND_DETECT = ("sound_detect", "Classificacao de sons ambiente (sirene, porta, choro)")
    TLDR = ("tldr", "tldr-pages -- documentacao acessivel de ~6000 comandos")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class NivelHardening(Enum):
    """Nivel de hardening da distro."""
    MINIMO = ("minimo", "Minimo: Kali padrao (root, sem firewall)")
    BASICO = ("basico", "Basico: usuario nao-root, firewall, SSH chave")
    REPUBLICA = ("republica", "Republica: hardening completo + acessibilidade + IA")
    FORTRESS = ("fortress", "Fortress: nivel militar (OpenCybersecurityMuralha)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class StatusPacote(Enum):
    """Status de um pacote na distro."""
    INSTALADO = ("instalado", "Instalado e ativo")
    DISPONIVEL = ("disponivel", "Disponivel (apt install)")
    CONFIGURADO = ("configurado", "Instalado e configurado pela Republica")
    PENDENTE = ("pendente", "Pendente (requer configuracao manual)")

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
class PacoteDistro:
    """Um pacote instalado na distro Republica/Kali."""
    nome: str
    camada: CamadaDistro
    descricao: str
    status: StatusPacote = StatusPacote.DISPONIVEL
    comando_instalacao: str = ""  # "apt install orca"
    dependencias: List[str] = field(default_factory=list)
    tamanho_mb: float = 0.0


@dataclass
class FerramentaSeguranca:
    """Uma ferramenta de seguranca do Kali."""
    nome: str
    tipo: TipoFerramentaSeguranca
    descricao: str
    uso_defensivo: str = ""  # como a Republica USA para defender
    uso_educativo: str = ""  # o que o cidadao APRENDE com ela
    comando: str = ""  # comando base


@dataclass
class PerfilDistro:
    """Um perfil de configuracao da distro."""
    nome: str
    descricao: str
    nivel_hardening: NivelHardening
    pacotes_incluidos: List[str] = field(default_factory=list)
    acessibilidade_ativa: bool = True
    ia_local_ativa: bool = True
    seguranca_ativa: bool = True
    publico_alvo: str = ""


# ============================================================================
# 3. DADOS: FERRAMENTAS E PACOTES
# ============================================================================

def _init_ferramentas_seguranca() -> List[FerramentaSeguranca]:
    return [
        FerramentaSeguranca("nmap", TipoFerramentaSeguranca.RECONHECIMENTO,
            "Mapeador de rede. Descobre portas abertas, servicos, SO.",
            "AUDITORIA: testa se a rede da Republica tem portas desnecessarias abertas.",
            "Cidadao aprende o que e uma porta, um servico, e por que fechar o que nao usa.",
            "nmap -sV 192.168.1.0/24"),
        FerramentaSeguranca("wireshark", TipoFerramentaSeguranca.SNIFFING,
            "Analisador de pacotes. Captura e inspeciona trafego de rede.",
            "AUDITORIA: detecta se dados estao sendo enviados para servidores estranhos.",
            "Cidadao VE os pacotes. Entende que cada app envia dados. Privacidade visivel.",
            "wireshark"),
        FerramentaSeguranca("metasploit", TipoFerramentaSeguranca.EXPLORACAO,
            "Framework de exploracao de vulnerabilidades.",
            "PENTEST: testa se os sistemas da Republica resistem a ataques reais.",
            "Cidadao entende como um ataque funciona. Saber atacar = saber defender.",
            "msfconsole"),
        FerramentaSeguranca("hashcat", TipoFerramentaSeguranca.SENHAS,
            "Quebra de hashes de senhas usando GPU.",
            "AUDITORIA: testa a forca das senhas da Republica. Senha fraca = quebra em segundos.",
            "Cidadao VE quanto tempo leva para quebrar '123456' vs 'Tr0ub4dor&3'. Aprende na pratica.",
            "hashcat -m 0 hash.txt wordlist.txt"),
        FerramentaSeguranca("aircrack-ng", TipoFerramentaSeguranca.WIRELESS,
            "Suite de auditoria de redes WiFi.",
            "AUDITORIA: testa se o WiFi da comunidade e vulneravel a ataque.",
            "Cidadao entende que WEP e quebravel, WPA2 precisa de senha forte, WPA3 e o padrao.",
            "aircrack-ng"),
        FerramentaSeguranca("lynis", TipoFerramentaSeguranca.AUDITORIA,
            "Auditor de hardening de sistema Linux.",
            "COMPLIANCE: audita se a distro da Republica segue as melhores praticas.",
            "Cidadao roda 'lynis audit system' e VE o score de seguranca. Gamifica hardening.",
            "lynis audit system"),
        FerramentaSeguranca("burpsuite", TipoFerramentaSeguranca.WEB,
            "Proxy de seguranca web. Intercepta e modifica requisicoes HTTP.",
            "PENTEST: testa se os sites/apps da Republica sao vulneraveis (SQLi, XSS).",
            "Cidadao VE como um dado viaja do browser ao servidor. Entende HTTPS, cookies, sessoes.",
            "burpsuite"),
        FerramentaSeguranca("ghidra", TipoFerramentaSeguranca.REVERSO,
            "Suite de engenharia reversa da NSA (open source).",
            "AUDITORIA: reverte binarios fechados para verificar backdoors.",
            "Cidadao entende que software fechado pode esconder coisas.Codigo aberto = auditavel.",
            "ghidraRun"),
        FerramentaSeguranca("john", TipoFerramentaSeguranca.SENHAS,
            "John the Ripper: quebra de senhas classica.",
            "AUDITORIA: testa forca de senhas de arquivos zip, shadow, etc.",
            "Cidadao aprende que senha e a CHAVE. Fraca = porta aberta.",
            "john --wordlist=password.lst hash.txt"),
        FerramentaSeguranca("nikto", TipoFerramentaSeguranca.ANALISE_VULNERABILIDADE,
            "Scanner de vulnerabilidades em servidores web.",
            "AUDITORIA: testa se o servidor web da Republica tem falhas conhecidas.",
            "Cidadao roda nikto e VE vulnerabilidades. Entende CVE, patch, atualizacao.",
            "nikto -h http://republica.local"),
        FerramentaSeguranca("tcpdump", TipoFerramentaSeguranca.SNIFFING,
            "Capturador de pacotes em linha de comando.",
            "MONITORAMENTO: detecta trafego anomalo em tempo real.",
            "Cidadao aprende que cada conexao deixa rastro. Rastro = auditoria.",
            "tcpdump -i eth0"),
        FerramentaSeguranca("openssl", TipoFerramentaSeguranca.CRIPTOGRAFIA,
            "Toolkit de criptografia. SSL/TLS, certificados, hashes.",
            "INFRA: gera certificados, testa TLS, criptografa arquivos.",
            "Cidadao aprende criptografia na pratica. Chave publica, chave privada, assinatura.",
            "openssl genrsa -aes256 -out chave.key 4096"),
    ]


def _init_pacotes_acessibilidade() -> List[PacoteDistro]:
    return [
        PacoteDistro("orca", CamadaDistro.ACESSIBILIDADE,
            "Leitor de tela para cegos. Le interface grafica em voz alta.",
            StatusPacote.CONFIGURADO, "apt install gnome-orca", [], 15),
        PacoteDistro("espeak-ng", CamadaDistro.ACESSIBILIDADE,
            "Sintetizador de voz. Backend TTS para Orca e Piper.",
            StatusPacote.CONFIGURADO, "apt install espeak-ng", ["portaudio19-dev"], 5),
        PacoteDistro("brltty", CamadaDistro.ACESSIBILIDADE,
            "Driver para displays Braille USB e Bluetooth.",
            StatusPacote.CONFIGURADO, "apt install brltty", [], 8),
        PacoteDistro("at-spi2-core", CamadaDistro.ACESSIBILIDADE,
            "Framework de acessibilidade. Ponte entre apps e tecnologias assistivas.",
            StatusPacote.INSTALADO, "apt install at-spi2-core", [], 3),
        PacoteDistro("caribou", CamadaDistro.ACESSIBILIDADE,
            "Teclado virtual na tela. Para eye tracker e switch.",
            StatusPacote.CONFIGURADO, "apt install caribou", [], 5),
        PacoteDistro("onboard", CamadaDistro.ACESSIBILIDADE,
            "Teclado virtual alternativo. Customizavel.",
            StatusPacote.CONFIGURADO, "apt install onboard", [], 12),
        PacoteDistro("mousetweaks", CamadaDistro.ACESSIBILIDADE,
            "Controle de mouse adaptado. Dwell click, drag lock.",
            StatusPacote.CONFIGURADO, "apt install mousetweaks", [], 2),
    ]


def _init_pacotes_ia_local() -> List[PacoteDistro]:
    return [
        PacoteDistro("vosk", CamadaDistro.IA_LOCAL,
            "STT leve (~50ms). Hotword + comandos curtos. Roda em qualquer hardware.",
            StatusPacote.PENDENTE, "pip install vosk", ["libsoundio-dev"], 50),
        PacoteDistro("whisper.cpp", CamadaDistro.IA_LOCAL,
            "STT preciso (~500ms-2s). Ditado longo + transcricao. Arquitetura dual-STT com Vosk.",
            StatusPacote.PENDENTE, "git clone whisper.cpp && make", ["ffmpeg"], 500),
        PacoteDistro("piper", CamadaDistro.IA_LOCAL,
            "Sintese de voz TTS em pt-BR offline. Cego ouve texto.",
            StatusPacote.PENDENTE, "pip install piper-tts", ["espeak-ng"], 200),
        PacoteDistro("kokoro", CamadaDistro.IA_LOCAL,
            "TTS voz natural para Iara (conversa humana). Offline.",
            StatusPacote.PENDENTE, "pip install kokoro", ["onnxruntime"], 300),
        PacoteDistro("chatterbox", CamadaDistro.IA_LOCAL,
            "TTS voz humana para Iara (conversa). Clonagem de voz emocional.",
            StatusPacote.PENDENTE, "pip install chatterbox-tts", ["torch"], 800),
        PacoteDistro("llama.cpp", CamadaDistro.IA_LOCAL,
            "LLM local. Roda modelos de linguagem sem nuvem, sem Big Tech.",
            StatusPacote.PENDENTE, "git clone llama.cpp && make", [], 1000),
        PacoteDistro("llava", CamadaDistro.IA_LOCAL,
            "Visao computacional. Descricao de cena via webcam para cegos.",
            StatusPacote.PENDENTE, "git clone llava && pip install -e .", ["llama.cpp"], 2000),
        PacoteDistro("tldr-pages", CamadaDistro.IA_LOCAL,
            "Documentacao acessivel de ~6000 comandos. Substitui man pages para cidadaos.",
            StatusPacote.PENDENTE, "git clone tldr-pages /usr/share/republica/tldr", [], 50),
    ]


def _init_pacotes_republica() -> List[PacoteDistro]:
    return [
        PacoteDistro("republica-telefonista", CamadaDistro.REPUBLICA,
            "Sistema como conversa humana. Smartphone como corpo estendido.",
            StatusPacote.PENDENTE, "apt install republica-telefonista", [], 50),
        PacoteDistro("republica-ide", CamadaDistro.REPUBLICA,
            "IDE inclusiva. 9 modos de input, 6 linguagens, transpilador.",
            StatusPacote.PENDENTE, "apt install republica-ide", ["nodejs", "python3"], 100),
        PacoteDistro("republica-energy", CamadaDistro.REPUBLICA,
            "Monitor de energia gratuita. Microgrid comunitaria.",
            StatusPacote.PENDENTE, "apt install republica-energy", [], 20),
        PacoteDistro("republica-security", CamadaDistro.REPUBLICA,
            "Cybersecurity muralha. 7 camadas de defesa.",
            StatusPacote.PENDENTE, "apt install republica-security", ["lynis", "fail2ban"], 30),
        PacoteDistro("republica-accessibility", CamadaDistro.REPUBLICA,
            "Stack de acessibilidade completa. Cego, surdo, tetraplegico, TEA.",
            StatusPacote.PENDENTE, "apt install republica-accessibility",
            ["orca", "brltty", "espeak-ng"], 80),
        PacoteDistro("republica-command-reference", CamadaDistro.REPUBLICA,
            "Documentacao acessivel de comandos (tldr + Vosk + output adaptativo).",
            StatusPacote.PENDENTE, "apt install republica-command-reference",
            ["vosk", "tldr-pages", "chatterbox"], 100),
    ]


def _init_perfis() -> List[PerfilDistro]:
    return [
        PerfilDistro(
            nome="RepublicaPadrao",
            descricao="Perfil padrao: hardening Republica + acessibilidade + IA + seguranca.",
            nivel_hardening=NivelHardening.REPUBLICA,
            pacotes_incluidos=["republica-full", "kali-tools-top10", "orca", "brltty"],
            acessibilidade_ativa=True, ia_local_ativa=True, seguranca_ativa=True,
            publico_alvo="Todos os cidadaos da Republica"
        ),
        PerfilDistro(
            nome="RepublicaAcessibilidade",
            descricao="Foco em acessibilidade maxima. Seguranca basica.",
            nivel_hardening=NivelHardening.BASICO,
            pacotes_incluidos=["republica-accessibility", "orca", "brltty", "piper", "whisper.cpp"],
            acessibilidade_ativa=True, ia_local_ativa=True, seguranca_ativa=False,
            publico_alvo="Cego, surdo, tetraplegico, TEA, idoso"
        ),
        PerfilDistro(
            nome="RepublicaCybersecurity",
            descricao="Foco em seguranca/defesa. Acessibilidade padrao.",
            nivel_hardening=NivelHardening.FORTRESS,
            pacotes_incluidos=["kali-linux-everything", "republica-security", "republica-accessibility"],
            acessibilidade_ativa=True, ia_local_ativa=False, seguranca_ativa=True,
            publico_alvo="Cybersecurity da muralha, auditores, pentesters civicos"
        ),
        PerfilDistro(
            nome="RepublicaEducacao",
            descricao="Perfil educacional: ferramentas de seguranca para APRENDER.",
            nivel_hardening=NivelHardening.BASICO,
            pacotes_incluidos=["nmap", "wireshark", "john", "lynis", "republica-ide"],
            acessibilidade_ativa=True, ia_local_ativa=True, seguranca_ativa=True,
            publico_alvo="Escolas, criancas, jovens aprendendo seguranca digital"
        ),
        PerfilDistro(
            nome="RepublicaMinima",
            descricao="Minimo viavel: Kali + hardening + Orca. RODA EM QUALQUER PC.",
            nivel_hardening=NivelHardening.BASICO,
            pacotes_incluidos=["orca", "espeak-ng", "lynis", "ufw"],
            acessibilidade_ativa=True, ia_local_ativa=False, seguranca_ativa=True,
            publico_alvo="Hardware antigo, RepublicaPort Essencial, maquinas doadas"
        ),
    ]


# ============================================================================
# 4. ENGINE
# ============================================================================

class BigLinuxEngine:
    """Motor da integracao Kali + Acessibilidade + IA + Republica."""

    def __init__(self) -> None:
        self.ferramentas_seg: List[FerramentaSeguranca] = _init_ferramentas_seguranca()
        self.pacotes_a11y: List[PacoteDistro] = _init_pacotes_acessibilidade()
        self.pacotes_ia: List[PacoteDistro] = _init_pacotes_ia_local()
        self.pacotes_rep: List[PacoteDistro] = _init_pacotes_republica()
        self.perfis: List[PerfilDistro] = _init_perfis()

    # -- consultas ---------------------------------------------------------

    def todas_camadas(self) -> List[CamadaDistro]:
        return list(CamadaDistro)

    def ferramentas_por_tipo(self, tipo: TipoFerramentaSeguranca) -> List[FerramentaSeguranca]:
        return [f for f in self.ferramentas_seg if f.tipo == tipo]

    def pacotes_por_camada(self, camada: CamadaDistro) -> List[PacoteDistro]:
        todos = self.pacotes_a11y + self.pacotes_ia + self.pacotes_rep
        return [p for p in todos if p.camada == camada]

    def perfil_por_nome(self, nome: str) -> Optional[PerfilDistro]:
        for p in self.perfis:
            if p.nome == nome:
                return p
        return None

    # -- meta-pacote --------------------------------------------------------

    def gerar_metapacote(self, perfil: PerfilDistro) -> Dict[str, Any]:
        """Gera a definicao do meta-pacote .deb para o perfil."""
        depends: List[str] = []
        for pkg_name in perfil.pacotes_incluidos:
            depends.append(pkg_name)
        return {
            "pacote": f"republica-{perfil.nome.lower().replace('republica', '')}",
            "versao": "2025.02-1",
            "dependencias": depends,
            "descricao": perfil.descricao,
            "hardening": perfil.nivel_hardening.id,
            "acessibilidade": perfil.acessibilidade_ativa,
            "ia_local": perfil.ia_local_ativa,
            "seguranca": perfil.seguranca_ativa,
            "comando_instalacao": f"sudo apt install republica-{perfil.nome.lower().replace('republica','')}",
        }

    # -- hardening ----------------------------------------------------------

    def checklist_hardening(self, nivel: NivelHardening) -> List[str]:
        """Checklist de hardening por nivel."""
        checklists = {
            NivelHardening.MINIMO: [
                "(Kali padrao -- NAO RECOMENDADO para uso diario)",
            ],
            NivelHardening.BASICO: [
                "1. Criar usuario nao-root (adduser republica)",
                "2. Adicionar ao sudo (usermod -aG sudo republica)",
                "3. Ativar firewall (ufw enable, ufw default deny incoming)",
                "4. SSH com chave, desabilitar senha (PasswordAuthentication no)",
                "5. Instalar fail2ban (apt install fail2ban)",
                "6. Atualizar sistema (apt update && apt full-upgrade)",
                "7. Desabilitar servicos desnecessarios (systemctl disable)",
            ],
            NivelHardening.REPUBLICA: [
                "1. Criar usuario nao-root (adduser republica)",
                "2. Adicionar ao sudo (usermod -aG sudo republica)",
                "3. Ativar firewall (ufw enable, ufw default deny incoming)",
                "4. SSH com chave, desabilitar senha (PasswordAuthentication no)",
                "5. Instalar fail2ban (apt install fail2ban)",
                "6. Atualizar sistema (apt update && apt full-upgrade)",
                "7. Desabilitar servicos desnecessarios (systemctl disable)",
                "8. AppArmor ativo (apparmor_parser --add /etc/apparmor.d/)",
                "9. Instalar republica-accessibility (orca, brltty, espeak)",
                "10. Configurar Orca para iniciar no boot",
                "11. Instalar Piper TTS (voz pt-BR offline)",
                "12. Instalar whisper.cpp (transcricao local)",
                "13. Desabilitar root login (passwd -l root)",
                "14. Auditd ativo (apt install auditd)",
                "15. Kernel hardening (sysctl: net.ipv4.tcp_syncookies=1, etc.)",
            ],
            NivelHardening.FORTRESS: [
                "1. Criar usuario nao-root (adduser republica)",
                "2. Adicionar ao sudo (usermod -aG sudo republica)",
                "3. Ativar firewall (ufw enable, ufw default deny incoming)",
                "4. SSH com chave, desabilitar senha (PasswordAuthentication no)",
                "5. Instalar fail2ban (apt install fail2ban)",
                "6. Atualizar sistema (apt update && apt full-upgrade)",
                "7. Desabilitar servicos desnecessarios (systemctl disable)",
                "8. AppArmor ativo (apparmor_parser --add /etc/apparmor.d/)",
                "9. Instalar republica-accessibility (orca, brltty, espeak)",
                "10. Configurar Orca para iniciar no boot",
                "11. Instalar Piper TTS (voz pt-BR offline)",
                "12. Instalar whisper.cpp (transcricao local)",
                "13. Desabilitar root login (passwd -l root)",
                "14. Auditd ativo (apt install auditd)",
                "15. Kernel hardening (sysctl: net.ipv4.tcp_syncookies=1, etc.)",
                "16. OpenCybersecurityMuralha: 7 camadas completas",
                "17. Snort/Suricata IDS (deteccao de intrusao)",
                "18. ClamAV + chkrootkit (anti-malware/anti-rootkit)",
                "19. Full disk encryption (LUKS)",
                "20. BIOS/UEFI password",
                "21. Secure Boot ativo",
                "22. Kernel lockdown mode",
                "23. Nenhum servico exposto a internet",
            ],
        }
        return checklists.get(nivel, [])

    # -- manifesto ----------------------------------------------------------

    def manifesto_kali(self) -> str:
        return (
            "MANIFESTO KALI COMO BASE DA REPUBLICA:\n"
            "  Nao usamos Kali porque somos hackers.\n"
            "  Usamos Kali porque SEGURANCA E CULTURA.\n"
            "  O cidadao que tem nmap instalado APRENDE sobre portas.\n"
            "  O cidadao que tem wireshark VE os dados viajando.\n"
            "  O cidadao que tem hashcat ENTENDE senhas fracas.\n"
            "  O cidadao que tem lynis AUDITA o proprio sistema.\n"
            "  Ferramenta disponivel = conhecimento disponivel.\n"
            "  Saber atacar = saber defender.\n"
            "  Seguranca nao e especialidade. E ALFABETIZACAO."
        )

    # -- scorecard ----------------------------------------------------------

    def scorecard(self) -> Dict[str, Any]:
        return {
            "camadas_distro": len(list(CamadaDistro)),
            "ferramentas_seguranca": len(self.ferramentas_seg),
            "tipos_ferramenta_seg": len(list(TipoFerramentaSeguranca)),
            "pacotes_acessibilidade": len(self.pacotes_a11y),
            "pacotes_ia_local": len(self.pacotes_ia),
            "pacotes_republica": len(self.pacotes_rep),
            "perfis_distro": len(self.perfis),
            "niveis_hardening": len(list(NivelHardening)),
            "total_pacotes": len(self.pacotes_a11y) + len(self.pacotes_ia) + len(self.pacotes_rep),
        }


# ============================================================================
# 5. DEMO
# ============================================================================

def _demo() -> None:
    e = BigLinuxEngine()

    print("=" * 70)
    print("OpenBigLinux -- Distro Base da Republica")
    print("Kali + Acessibilidade + IA Local + Stack Republica")
    print("=" * 70)

    # --- Manifesto ---
    print(f"\n{e.manifesto_kali()}")

    # --- Camadas ---
    print("\n[7 CAMADAS DA DISTRO REPUBLICA]")
    for c in CamadaDistro:
        print(f"  Camada {c.id}: {c.rotulo}")

    # --- Ferramentas de seguranca ---
    print(f"\n[FERRAMENTAS DE SEGURANCA NATIVAS ({len(e.ferramentas_seg)})]")
    for f in e.ferramentas_seg:
        print(f"\n  {f.nome} ({f.tipo.rotulo})")
        print(f"    Descricao: {f.descricao}")
        print(f"    Defensivo: {f.uso_defensivo}")
        print(f"    Educativo: {f.uso_educativo}")
        print(f"    Comando: {f.comando}")

    # --- Pacotes de acessibilidade ---
    print(f"\n[PACOTES DE ACESSIBILIDADE ({len(e.pacotes_a11y)})]")
    for p in e.pacotes_a11y:
        flag = {"instalado": "OK", "disponivel": "DISP",
                "configurado": "CONF", "pendente": "PEND"}[p.status.id]
        print(f"  [{flag}] {p.nome} ({p.tamanho_mb:.0f}MB): {p.descricao[:60]}")

    # --- IA local ---
    print(f"\n[IA LOCAL ({len(e.pacotes_ia)})]")
    for p in e.pacotes_ia:
        print(f"  [{p.status.id}] {p.nome}: {p.descricao[:60]}")

    # --- Stack Republica ---
    print(f"\n[STACK DA REPUBLICA ({len(e.pacotes_rep)})]")
    for p in e.pacotes_rep:
        print(f"  [{p.status.id}] {p.nome}: {p.descricao[:60]}")

    # --- Perfis ---
    print(f"\n[PERFIS DE INSTALACAO ({len(e.perfis)})]")
    for p in e.perfis:
        meta = e.gerar_metapacote(p)
        print(f"\n  {p.nome} ({p.nivel_hardening.rotulo})")
        print(f"    Publico: {p.publico_alvo}")
        print(f"    Acessibilidade: {'Sim' if p.acessibilidade_ativa else 'Nao'}")
        print(f"    IA Local: {'Sim' if p.ia_local_ativa else 'Nao'}")
        print(f"    Seguranca: {'Sim' if p.seguranca_ativa else 'Nao'}")
        print(f"    Instalar: {meta['comando_instalacao']}")

    # --- Hardening ---
    print("\n[CHECKLIST DE HARDENING -- NIVEL REPUBLICA]")
    for item in e.checklist_hardening(NivelHardening.REPUBLICA):
        print(f"  {item}")

    # --- Fluxo de instalacao ---
    print("\n[FLUXO DE INSTALACAO]")
    print("""
  1. Baixar Kali Linux (ou RepublicaOS pre-built)
  2. Instalar (BIOS/UEFI, particionamento, LUKS encryption)
  3. Criar usuario 'republica' (NAO root)
  4. sudo apt update && sudo apt full-upgrade
  5. sudo apt install republica-padrao
  6. Sistema configura:
     - Hardening automatico (firewall, fail2ban, apparmor)
     - Acessibilidade ativa (Orca, brltty, espeak)
     - IA local baixada (whisper, piper, llama)
     - Stack da Republica instalada
  7. reiniciar
  8. Republica rodando. Com seguranca. Com acessibilidade. Com IA local.
""")

    # --- Dual-STT + Voz ---
    print("\n[ARQUITETURA DUAL-STT -- Vosk + Whisper]")
    print("""  Vosk (leve, ~50ms):
    - Hotword "ajuda" + comandos curtos ("ajuda tar", "parar audio")
    - Roda em Raspberry Pi, maquina doada, hardware minimo
    - Sempre ativo. E o GATILHO do sistema de voz.

  Whisper.cpp (preciso, ~500ms-2s):
    - Ditado longo, transcricao de audio/video
    - Ativado sob demanda ou quando Vosk falha
    - Mais preciso, mas pesado. Precisa de CPU decente.

  Regra: Vosk primeiro. Whisper se necessario. Nunca o contrario.

  Pipeline: Microfone -> Vosk (50ms) -> intent detectado
                              |-> comando curto: executar
                              |-> ditado longo: passar para Whisper
""")

    print("[DOCUMENTACAO ACESSIVEL -- tldr + Vosk + Iara]")
    print("""  Modulo: open_command_reference.py (republica-command-reference)

  Fluxo: "ajuda tar" (voz) -> Vosk reconhece -> busca tldr
         -> Iara fala exemplos (Chatterbox)
         -> Orca expoe via AT-SPI (navegacao por tab)
         -> Brltty exibe em braille (tetraplegico)

  Substitui man pages. man tar = 2000 linhas (40min de Orca).
  tldr tar = 8 exemplos (30s de Iara). CIDADAOS > ESPECIALISTAS.
""")

    # --- Scorecard ---
    print("[SCORECARD]")
    sc = e.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<28} {v}")

    # --- FILOSOFIA ---
    print("\n" + "=" * 70)
    print("FILOSOFIA -- Seguranca como cultura, nao especialidade")
    print("=" * 70)
    print("""
POR QUE KALI E NAO UBUNTU:

  Ubuntu e "facil". Ubuntu esconde a seguranca.
  Ubuntu nao tem nmap, wireshark, hashcat.
  Ubuntu trata o usuario como crianca que nao precisa saber de rede.

  Kali TRATA o usuario como adulto que PRECISA saber.
  Kali tem as ferramentas. Kali tem a documentacao.
  Kali tem a comunidade que ensina.

  A Republica NAO esconde seguranca do cidadao.
  A Republica da as ferramentas e ensina a USAR.

O PARAODOXO DA SEGURANCA:

  "Esconder ferramentas de ataque protege as pessoas." FALSO.
  Esconder protege o ATACANTE, nao a vitima.
  O atacante JA tem as ferramentas (baixa na internet).
  A vitima e quem nao tem. A Republica da as ferramentas para a vitima.

  Cidadao com nmap = cidadao que AUDITA a propria rede.
  Cidadao com hashcat = cidadao que TESTA a propria senha.
  Cidadao with lynis = cidadao que ENDURECE o proprio sistema.

A INTEGRACAO COM ACESSIBILIDADE:

  Kali puro nao tem Orca. Kali puro nao tem brltty.
  A Republica ADICIONA. Acessibilidade sobre seguranca.
  CEGO audita rede com nmap + Orca (leitor de tela le o output).
  SURDO ve pacotes no wireshark (interface visual, nao audio).
  TETRAPLEGICO roda hashcat com eye tracker + switch.

  Seguranca E acessibilidade. Nao sao separados.
  Sao A MESMA COISA: autonomia do cidadao sobre o proprio sistema.

A INTEGRACAO COM IA LOCAL:

  Whisper.cpp transcreve audio em tempo real.
  Surdo le a transcricao. AUDITA reunioes, palestras, videos.

  Piper TTS fala em pt-BR.
  Cego OUVE a saida do nmap, do lynis, do hashcat.

  llama.cpp roda LLM local.
  Cidadao pergunta: "o que esse log de erro significa?"
  IA responde. Local. Sem nuvem. Sem Big Tech. Sem spyware.

O PRINCIPIO FINAL:

  Um cidadao que sabe atacar sabe defender.
  Um cidadao que defende e LIVRE.
  Um cidadao livre e SOBERANO.
  Seguranca nao e para especialistas.
  Seguranca e ALFABETIZACAO DIGITAL.
  A distro da Republica alfabetiza. Desde o dia 1.
""")


if __name__ == "__main__":
    _demo()
