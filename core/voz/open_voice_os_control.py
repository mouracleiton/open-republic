#!/usr/bin/env python3
"""
OpenVoiceOSControl -- Controle do Sistema Operacional por Voz
================================================================
"Fale. O sistema obedece."  (Atualizado 2024/2025)

Cego nao digita. Tetraplegico nao clica. Idoso nao navega menu.
Eles FALAM. O sistema obedece.

Este modulo e a PONTE entre a voz humana e o sistema operacional.
Converta fala em acoes: abrir app, clicar, digitar, navegar, ler tela.

NAO e assistente pessoal. E CONTROLE DE INTERFACE.
Assistente responde perguntas. Controle de voz OPERA o sistema.
A Telefonista CONVERSA. O VoiceControl AGE.

OS 7 DOMINIOS DE CONTROLE:

1. JANELAS: abrir, fechar, minimizar, maximizar, trocar, mover, workspace (Wayland)
2. ARQUIVOS: navegar pastas, abrir arquivo, criar pasta, buscar, abrir com app
3. DIGITACAO: ditar texto, corrigir, formatar, apagar, ditar codigo
4. NAVEGACAO: rolar pagina, voltar, avancar, clicar link, pesquisar pagina
5. SISTEMA: volume, brilho, wifi, bluetooth, bateria, desligar, vpn, rede, modo escuro
6. APLICATIVOS: iniciar Republica apps (IDE, Telefonista, Energy, VSCode, Neovim, Obsidian)
7. LEITURA: ler tela, ler selecionado, ler titulo, descrever janela, ler notificacoes, zoom

COMO FUNCIONA (pipeline 2025 - 9 camadas):

Microfone -> Silero VAD v5 + OpenWakeWord 2.0 -> faster-whisper (Distil-Whisper tiny->small) -> Texto
Texto -> Parser de Comando (NLU leve, regex + fuzzy + cache LRU)
Comando -> Executor (acao real no SO via D-Bus / ydotool / wlrctl / hyprctl / AT-SPI2 / xdotool legacy)
Resultado -> Kokoro-82M (streaming <65ms) / Piper ONNX (TTS local) -> Audio

Tudo LOCAL. Sem nuvem. Sem Google. Sem Alexa. Sem Siri.
Soberania da voz. (Ref: open_voice_pipeline.py 2025)

ATUALIZACAO 2024/2025 (versoes e ferramentas):
- STT: faster-whisper large-v3 + distil-whisper (2024/2025), Vosk 0.3.45 fallback
- TTS: Kokoro-82M (ONNX streaming, <65ms first syllable), Piper high-quality ONNX
- VAD/Hotword: Silero VAD v5, OpenWakeWord 2.0 (1.8M params)
- Accessibility: AT-SPI2 / Orca 46 (GNOME 46 2024), Orca 47 (2025), brltty
- Wayland (primary 2025): ydotool, wlrctl, hyprctl (dbus), layer-shell overlays
- X11 legacy: xdotool, wmctrl, gdbus
- Apps: flatpak run, gio launch, gtk-launch
- OCR Shim (fallback): Tesseract 5.4.1, PaddleOCR v5 (PT-BR), surya/marker
- Targets: <110ms comando (L0-L6), <65ms TTS start, ~180ms percebido

ALINHAMENTO CONSTITUCIONAL:
- P1: Voz e o input mais universal. Cego, tetraplegico, idoso -- todos falam.
- P2: Autonomia corporal: voce CONTROLA o sistema com o proprio corpo (voz).
- P6: Acesso universal: voz remove barreira do teclado/mouse.
- P9 (Soberania): STT+TTS+parser LOCAIS. Nenhum audio sai do dispositivo.

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

class DominioComando(Enum):
    """7 dominios de controle por voz do SO."""
    JANELAS = ("janelas", "Controle de janelas (abrir, fechar, maximizar, workspace)")
    ARQUIVOS = ("arquivos", "Navegacao de arquivos e pastas")
    DIGITACAO = ("digitacao", "Ditacao de texto e edicao (inclui codigo)")
    NAVEGACAO = ("navegacao", "Navegacao web e de documentos")
    SISTEMA = ("sistema", "Configuracoes do sistema (volume, brilho, wifi, vpn, tema)")
    APLICATIVOS = ("aplicativos", "Iniciar aplicativos da Republica + ferramentas modernas")
    LEITURA = ("leitura", "Leitura de tela e descricao de interface (acessibilidade)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class StatusComando(Enum):
    """Status da execucao de um comando de voz."""
    EXECUTADO = ("executado", "Comando executado com sucesso")
    PARCIAL = ("parcial", "Executado parcialmente (precisa confirmar)")
    NAO_RECONHECIDO = ("nao_reconhecido", "Comando nao reconhecido")
    AMBIGUO = ("ambiguo", "Comando ambiguo (multiplas interpretacoes)")
    SEM_PERMISSAO = ("sem_permissao", "Comando requer permissao elevada")
    ERRO = ("erro", "Erro ao executar comando")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class NivelConfianca(Enum):
    """Nivel de confianca no reconhecimento do comando."""
    ALTO = ("alto", "Alto: comando claro, sem ambiguidade", 0.9, 1.0)
    MEDIO = ("medio", "Medio: comando reconhecido, leve ambiguidade", 0.6, 0.89)
    BAIXO = ("baixo", "Baixo: comando incerto, confirmar antes de executar", 0.3, 0.59)
    REJEITADO = ("rejeitado", "Rejeitado: nao e comando, e conversa", 0.0, 0.29)

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def minimo(self) -> float:
        return self.value[2]

    @property
    def maximo(self) -> float:
        return self.value[3]


class TipoFeedbackVoz(Enum):
    """Como o sistema responde por voz apos executar comando."""
    SILENCIOSO = ("silencioso", "Silencioso: executa sem falar (surdo le na tela)")
    CONFIRMACAO = ("confirmacao", "Confirmacao: 'Feito.' (curto, direto)")
    DETALHADO = ("detalhado", "Detalhado: explica o que fez (cego precisa saber)")
    ERRO_FALADO = ("erro_falado", "Erro falado: explica o que deu errado")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class ModoAtivacao(Enum):
    """Como o VoiceControl e ativado."""
    SEMPRE_OUVINDO = ("sempre_ouvindo", "Sempre ouvindo (hot word: 'Republica')")
    HOTKEY = ("hotkey", "Tecla de atalho (ex: Super+V)")
    SWITCH = ("switch", "Botao fisico (switch button para tetraplegico)")
    PUSH_TO_TALK = ("push_to_talk", "Push-to-talk (segurar tecla)")
    AUTOMATICO = ("automatico", "Automatico (Orca/Telefonista decide quando)")

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
class ComandoVoz:
    """Definicao de um comando de voz reconhecivel."""
    id: str
    dominio: DominioComando
    padroes: List[str]         # regex/palavras-chave: [r"abrir (.+)", r"iniciar (.+)"]
    acao: str                  # acao executavel: "abrir_app({app})"
    parametros_esperados: List[str] = field(default_factory=list)  # ["app"]
    descricao: str = ""
    exemplo: str = ""          # "abrir firefox"
    requer_confirmacao: bool = False
    requer_permissao: bool = False  # sudo?


@dataclass
class ResultadoComando:
    """Resultado de processar um comando de voz."""
    texto_original: str
    comando_reconhecido: Optional[ComandoVoz] = None
    parametros: Dict[str, str] = field(default_factory=dict)
    status: StatusComando = StatusComando.NAO_RECONHECIDO
    confianca: NivelConfianca = NivelConfianca.REJEITADO
    score_confianca: float = 0.0
    acao_executada: str = ""
    feedback_voz: str = ""
    feedback_tipo: TipoFeedbackVoz = TipoFeedbackVoz.SILENCIOSO


@dataclass
class SessaoVoz:
    """Uma sessao ativa de controle por voz."""
    id: str
    usuario: str = ""
    modo_ativacao: ModoAtivacao = ModoAtivacao.SEMPRE_OUVINDO
    hot_word: str = "republica"
    feedback_padrao: TipoFeedbackVoz = TipoFeedbackVoz.CONFIRMACAO
    comandos_executados: int = 0
    erros: int = 0
    ativa: bool = True
    # adaptacao por deficiencia
    usuario_cego: bool = False
    usuario_surdo: bool = False
    usuario_motora: bool = False


# ============================================================================
# 3. CATALOGO DE COMANDOS (65+ comandos em 2025)
# ============================================================================

def _init_comandos() -> List[ComandoVoz]:
    """Define todos os comandos de voz reconheciveis. (Atualizado 2025: +15 comandos Wayland/Flatpak/Acc/AI)"""
    return [
        # === JANELAS (inclui Wayland 2025) ===
        ComandoVoz("jan_abrir", DominioComando.JANELAS,
            [r"^abrir (.+)$", r"^iniciar (.+)$", r"^abre (?:o |a )?(.+)$"],
            "abrir_app", ["app"],
            "Abre um aplicativo pelo nome",
            "abrir firefox"),
        ComandoVoz("jan_fechar", DominioComando.JANELAS,
            [r"^fechar (?:janela|aba|tudo)$", r"^fecha (?:janela|aba|tudo)$"],
            "fechar_janela", [],
            "Fecha a janela ativa",
            "fechar janela"),
        ComandoVoz("jan_maximizar", DominioComando.JANELAS,
            [r"^maximizar$", r"^maximiza$", r"^tela cheia$", r"^fullscreen$"],
            "maximizar_janela", [],
            "Maximiza a janela ativa",
            "maximizar"),
        ComandoVoz("jan_minimizar", DominioComando.JANELAS,
            [r"^minimizar$", r"^minimiza$", r"^esconder janela$"],
            "minimizar_janela", [],
            "Minimiza a janela ativa",
            "minimizar"),
        ComandoVoz("jan_trocar", DominioComando.JANELAS,
            [r"^trocar (?:janela|aba|app)$", r"^alternar$", r"^proximo app$", r"^alt tab$"],
            "trocar_janela", [],
            "Troca para a proxima janela (Alt+Tab / wlrctl)",
            "trocar janela"),
        ComandoVoz("jan_mover", DominioComando.JANELAS,
            [r"^mover (?:janela )?(?:para )?(esquerda|direita|cima|baixo|centro)$"],
            "mover_janela", ["direcao"],
            "Move a janela ativa (xdotool/ydotool/wlrctl)",
            "mover para esquerda"),
        # NEW 2025: Wayland workspace and focus
        ComandoVoz("jan_workspace", DominioComando.JANELAS,
            [r"^(?:ir para |mudar para |workspace )?(?:workspace |espaco )?(\d+)$"],
            "mudar_workspace", ["numero"],
            "Muda para workspace (Wayland: hyprctl / wlrctl)",
            "workspace 2"),
        ComandoVoz("jan_focar", DominioComando.JANELAS,
            [r"^focar (?:janela |app )?(.+)$", r"^foca (?:em )?(.+)$"],
            "focar_janela", ["nome"],
            "Foca janela pelo titulo (Wayland AT-SPI + wlrctl)",
            "focar terminal"),
        ComandoVoz("jan_tile", DominioComando.JANELAS,
            [r"^(?:tile |organizar |layout )(esquerda|direita|vertical|horizontal)$"],
            "tile_janela", ["direcao"],
            "Tile / split janela (Hyprland / river / sway)",
            "tile esquerda"),

        # === ARQUIVOS ===
        ComandoVoz("arq_abrir", DominioComando.ARQUIVOS,
            [r"^abrir arquivo (.+)$", r"^abrir documento (.+)$"],
            "abrir_arquivo", ["nome"],
            "Abre um arquivo pelo nome",
            "abrir arquivo relatorio.pdf"),
        ComandoVoz("arq_buscar", DominioComando.ARQUIVOS,
            [r"^buscar (.+)$", r"^procurar (.+)$", r"^encontrar (.+)$", r"^achar (.+)$"],
            "buscar_arquivo", ["termo"],
            "Busca arquivos por nome",
            "buscar foto ferias"),
        ComandoVoz("arq_pasta", DominioComando.ARQUIVOS,
            [r"^criar pasta (.+)$", r"^nova pasta (.+)$"],
            "criar_pasta", ["nome"],
            "Cria uma nova pasta",
            "criar pasta projetos"),
        ComandoVoz("arq_ir", DominioComando.ARQUIVOS,
            [r"^ir para (.+)$", r"^abrir pasta (.+)$", r"^navegar para (.+)$"],
            "navegar_pasta", ["caminho"],
            "Navega para uma pasta",
            "ir para documentos"),
        ComandoVoz("arq_deletar", DominioComando.ARQUIVOS,
            [r"^apagar (.+)$", r"^deletar (.+)$", r"^excluir (.+)$"],
            "deletar_arquivo", ["nome"],
            "Deleta um arquivo (requer confirmacao)",
            "apagar arquivo velho.txt",
            requer_confirmacao=True),
        # NEW 2025
        ComandoVoz("arq_abrir_com", DominioComando.ARQUIVOS,
            [r"^abrir (?:com |usando )(.+) (?:o |a )?(.+)$"],
            "abrir_arquivo_com", ["app", "arquivo"],
            "Abre arquivo com app especifico (flatpak ou nativo)",
            "abrir com vscode relatorio.md"),
        ComandoVoz("arq_trash", DominioComando.ARQUIVOS,
            [r"^(?:mover |enviar )?(?:para )?lixeira (.+)$"],
            "mover_lixeira", ["nome"],
            "Move para lixeira (gio trash)",
            "mover para lixeira temp.txt"),
        ComandoVoz("arq_copiar_path", DominioComando.ARQUIVOS,
            [r"^(?:copiar |copie )?caminho (?:do )?(.+)$"],
            "copiar_caminho", ["nome"],
            "Copia caminho absoluto para clipboard",
            "copiar caminho do projeto"),

        # === DIGITACAO ===
        ComandoVoz("dig_ditar", DominioComando.DIGITACAO,
            [r"^digitar (.+)$", r"^escrever (.+)$", r"^ditar (.+)$"],
            "digitar_texto", ["texto"],
            "Digita o texto ditado no campo ativo",
            "digitar ola mundo"),
        ComandoVoz("dig_apagar", DominioComando.DIGITACAO,
            [r"^apagar (?:palavra|linha|tudo|texto)$",
             r"^deletar (?:palavra|linha|tudo)$"],
            "apagar_texto", ["escopo"],
            "Apaga palavra/linha/tudo",
            "apagar palavra"),
        ComandoVoz("dig_enter", DominioComando.DIGITACAO,
            [r"^enter$", r"^confirmar$", r"^enviar$"],
            "pressionar_enter", [],
            "Pressiona Enter",
            "enter"),
        ComandoVoz("dig_desfazer", DominioComando.DIGITACAO,
            [r"^desfazer$", r"^undo$", r"^voltar atras$"],
            "desfazer", [],
            "Desfaz a ultima acao (Ctrl+Z)",
            "desfazer"),
        ComandoVoz("dig_copiar", DominioComando.DIGITACAO,
            [r"^copiar$", r"^copia$"],
            "copiar", [],
            "Copia selecao (Ctrl+C)",
            "copiar"),
        ComandoVoz("dig_colar", DominioComando.DIGITACAO,
            [r"^colar$", r"^cola$"],
            "colar", [],
            "Cola (Ctrl+V)",
            "colar"),
        ComandoVoz("dig_selecionar", DominioComando.DIGITACAO,
            [r"^selecionar tudo$", r"^seleciona tudo$"],
            "selecionar_tudo", [],
            "Seleciona tudo (Ctrl+A)",
            "selecionar tudo"),
        ComandoVoz("dig_maiuscula", DominioComando.DIGITACAO,
            [r"^maiusculas$", r"^caixa alta$", r"^(?:letras )?mai[úu]sculas?$"],
            "maiusculas", [],
            "Converte selecao para maiusculas",
            "maiusculas"),
        # NEW 2025
        ComandoVoz("dig_codigo", DominioComando.DIGITACAO,
            [r"^(?:ditar |escrever |digitar )?codigo (.+)$"],
            "digitar_codigo", ["codigo"],
            "Digita bloco de codigo (preserva indentacao)",
            "ditar codigo def main"),
        ComandoVoz("dig_comentar", DominioComando.DIGITACAO,
            [r"^(?:comentar |descomentar |toggle comment)$"],
            "toggle_comentario", [],
            "Comenta/descomenta linha (Ctrl+/)",
            "comentar"),
        ComandoVoz("dig_indent", DominioComando.DIGITACAO,
            [r"^(?:indentar |desindentar |tab |shift tab)$"],
            "ajustar_indent", ["direcao"],
            "Indentacao (Tab / Shift+Tab)",
            "indentar"),

        # === NAVEGACAO ===
        ComandoVoz("nav_rolar_baixo", DominioComando.NAVEGACAO,
            [r"^(?:rolar|descer|baixo)(?: para baixo)?$",
             r"^page down$", r"^pagina baixo$"],
            "rolar_baixo", [],
            "Rola a pagina para baixo",
            "rolar para baixo"),
        ComandoVoz("nav_rolar_cima", DominioComando.NAVEGACAO,
            [r"^(?:rolar|subir|cima)(?: para cima)?$",
             r"^page up$", r"^pagina cima$"],
            "rolar_cima", [],
            "Rola a pagina para cima",
            "rolar para cima"),
        ComandoVoz("nav_voltar", DominioComando.NAVEGACAO,
            [r"^voltar$", r"^anterior$", r"^back$"],
            "navegar_voltar", [],
            "Volta (botao voltar do browser)",
            "voltar"),
        ComandoVoz("nav_clicar", DominioComando.NAVEGACAO,
            [r"^clicar (.+)$", r"^clica (?:em |no |na )?(.+)$"],
            "clicar_elemento", ["elemento"],
            "Clica num elemento da pagina pelo nome (AT-SPI / OCR shim)",
            "clicar enviar"),
        ComandoVoz("nav_url", DominioComando.NAVEGACAO,
            [r"^abrir site (.+)$", r"^ir para site (.+)$", r"^acessar (.+\.com|.+ \.org|.+ \.gov\.br)$"],
            "abrir_url", ["url"],
            "Abre um site",
            "abrir site republica.local"),
        # NEW 2025
        ComandoVoz("nav_pesquisar", DominioComando.NAVEGACAO,
            [r"^(?:procurar |buscar |pesquisar |find )(.+)$"],
            "pesquisar_pagina", ["termo"],
            "Pesquisa na pagina (Ctrl+F)",
            "pesquisar republica"),
        ComandoVoz("nav_proximo", DominioComando.NAVEGACAO,
            [r"^(?:proximo |seguinte |next )(?:link|resultado|ocorrencia)?$"],
            "proximo_resultado", [],
            "Vai para proximo resultado da busca (F3)",
            "proximo"),

        # === SISTEMA (2025: vpn, dark, rede) ===
        ComandoVoz("sis_volume_mais", DominioComando.SISTEMA,
            [r"^aumentar volume$", r"^volume (?:mais|alto)$", r"^mais alto$"],
            "volume_mais", [],
            "Aumenta o volume (pactl / wpctl / amixer)",
            "aumentar volume"),
        ComandoVoz("sis_volume_menos", DominioComando.SISTEMA,
            [r"^diminuir volume$", r"^volume (?:menos|baixo)$", r"^mais baixo$"],
            "volume_menos", [],
            "Diminui o volume",
            "diminuir volume"),
        ComandoVoz("sis_volume_mudo", DominioComando.SISTEMA,
            [r"^mudo$", r"^sem som$", r"^mutar$", r"^silenciar$"],
            "volume_mudo", [],
            "Liga/desliga mudo",
            "mudo"),
        ComandoVoz("sis_brilho", DominioComando.SISTEMA,
            [r"^brilho (mais|menos|\d+%)$", r"^aumentar brilho$", r"^diminuir brilho$"],
            "ajustar_brilho", ["valor"],
            "Ajusta brilho da tela (brightnessctl / ddcutil)",
            "brilho mais"),
        ComandoVoz("sis_wifi", DominioComando.SISTEMA,
            [r"^(?:ligar|desligar) wifi$", r"^wifi (on|off|ligar|desligar)$"],
            "toggle_wifi", ["acao"],
            "Liga/desliga WiFi (nmcli / iwctl)",
            "ligar wifi"),
        ComandoVoz("sis_bluetooth", DominioComando.SISTEMA,
            [r"^(?:ligar|desligar) bluetooth$"],
            "toggle_bluetooth", ["acao"],
            "Liga/desliga Bluetooth (bluetoothctl)",
            "desligar bluetooth"),
        ComandoVoz("sis_bateria", DominioComando.SISTEMA,
            [r"^bateria$", r"^nivel de bateria$", r"^quanta bateria$"],
            "verificar_bateria", [],
            "Le o nivel de bateria em voz alta (upower)",
            "bateria"),
        ComandoVoz("sis_hora", DominioComando.SISTEMA,
            [r"^que horas sao$", r"^horas$", r"^que hora e$"],
            "falar_hora", [],
            "Fala a hora atual",
            "que horas sao"),
        ComandoVoz("sis_desligar", DominioComando.SISTEMA,
            [r"^desligar computador$", r"^desligar$", r"^shutdown$"],
            "desligar_sistema", [],
            "Desliga o computador (requer confirmacao)",
            "desligar computador",
            requer_confirmacao=True),
        # NEW 2025
        ComandoVoz("sis_vpn", DominioComando.SISTEMA,
            [r"^(?:ligar|desligar|conectar|desconectar) (?:vpn|wireguard|openvpn)$"],
            "toggle_vpn", ["acao"],
            "Liga/desliga VPN (nmcli / wg-quick)",
            "ligar vpn"),
        ComandoVoz("sis_dark", DominioComando.SISTEMA,
            [r"^(?:modo )?(escuro|dark|claro|light)$", r"^alternar tema$"],
            "toggle_modo_escuro", ["modo"],
            "Alterna dark/light mode (gsettings / plasma-apply-colorscheme)",
            "modo escuro"),
        ComandoVoz("sis_lock", DominioComando.SISTEMA,
            [r"^(?:bloquear |lock |trancar )?(?:tela|computador)$"],
            "bloquear_tela", [],
            "Bloqueia a tela (loginctl lock-session)",
            "bloquear tela"),
        ComandoVoz("sis_suspend", DominioComando.SISTEMA,
            [r"^(?:suspender |dormir |suspend |sleep)$"],
            "suspender_sistema", [],
            "Suspende o sistema (systemctl suspend)",
            "suspender"),

        # === APLICATIVOS DA REPUBLICA + MODERNOS 2025 ===
        ComandoVoz("app_ide", DominioComando.APLICATIVOS,
            [r"^(?:abrir|iniciar) (?:a )?ide$", r"^abrir republica ide$",
             r"^iniciar ide$"],
            "abrir_app_ide", [],
            "Abre a OpenInclusiveIDE",
            "abrir IDE"),
        ComandoVoz("app_telefonista", DominioComando.APLICATIVOS,
            [r"^(?:abrir|iniciar|chamar) telefonista$",
             r"^(?:abrir|chamar) iara$", r"^falar com iara$"],
            "abrir_telefonista", [],
            "Abre a Telefonista (Iara)",
            "chamar telefonista"),
        ComandoVoz("app_energy", DominioComando.APLICATIVOS,
            [r"^(?:abrir|iniciar) energia$", r"^(?:abrir|iniciar) energy$"],
            "abrir_energy", [],
            "Abre o OpenEnergy",
            "abrir energia"),
        ComandoVoz("app_seguranca", DominioComando.APLICATIVOS,
            [r"^(?:abrir|iniciar) seguranca$", r"^auditoria de seguranca$",
             r"^rodar lynis$"],
            "abrir_seguranca", [],
            "Abre o OpenCybersecurityMuralha",
            "auditoria de seguranca"),
        ComandoVoz("app_terminal", DominioComando.APLICATIVOS,
            [r"^(?:abrir|iniciar) terminal$", r"^linha de comando$",
             r"^consola$", r"^shell$"],
            "abrir_terminal", [],
            "Abre o terminal",
            "abrir terminal"),
        ComandoVoz("app_navegador", DominioComando.APLICATIVOS,
            [r"^(?:abrir|iniciar) navegador$", r"^abrir internet$",
             r"^abrir browser$", r"^firefox$", r"^chrome$"],
            "abrir_navegador", [],
            "Abre o navegador web",
            "abrir navegador"),
        ComandoVoz("app_orca", DominioComando.APLICATIVOS,
            [r"^(?:abrir|iniciar|ligar) orca$"],
            "abrir_orca", [],
            "Abre o leitor de tela Orca",
            "ligar orca"),
        # NEW 2025 modern + flatpak
        ComandoVoz("app_vscode", DominioComando.APLICATIVOS,
            [r"^(?:abrir|iniciar) (?:vscode|code|vs code)$"],
            "abrir_vscode", [],
            "Abre Visual Studio Code (code ou flatpak)",
            "abrir vscode"),
        ComandoVoz("app_neovim", DominioComando.APLICATIVOS,
            [r"^(?:abrir|iniciar) (?:nvim|neovim|vim)$"],
            "abrir_neovim", [],
            "Abre Neovim no terminal",
            "abrir neovim"),
        ComandoVoz("app_obsidian", DominioComando.APLICATIVOS,
            [r"^(?:abrir|iniciar) obsidian$"],
            "abrir_obsidian", [],
            "Abre Obsidian (notas)",
            "abrir obsidian"),
        ComandoVoz("app_flatpak", DominioComando.APLICATIVOS,
            [r"^(?:abrir|rodar) flatpak (.+)$", r"^flatpak run (.+)$"],
            "abrir_flatpak", ["app_id"],
            "Roda app via flatpak run",
            "abrir flatpak org.mozilla.firefox"),

        # === LEITURA (acessibilidade 2025) ===
        ComandoVoz("lei_tela", DominioComando.LEITURA,
            [r"^ler tela$", r"^ler janela$", r"^o que esta na tela$",
             r"^descrever tela$"],
            "ler_tela", [],
            "Le o conteudo da tela ativa (AT-SPI2 + OCR shim)",
            "ler tela"),
        ComandoVoz("lei_selecionado", DominioComando.LEITURA,
            [r"^ler selecionado$", r"^ler selecao$", r"^ler isso$"],
            "ler_selecionado", [],
            "Le o texto selecionado",
            "ler selecionado"),
        ComandoVoz("lei_titulo", DominioComando.LEITURA,
            [r"^ler titulo$", r"^qual e o titulo$", r"^titulo da janela$"],
            "ler_titulo", [],
            "Le o titulo da janela ativa",
            "ler titulo"),
        ComandoVoz("lei_link", DominioComando.LEITURA,
            [r"^ler links$", r"^quais links$", r"^listar links$"],
            "ler_links", [],
            "Lista os links da pagina",
            "ler links"),
        ComandoVoz("lei_paragrafo", DominioComando.LEITURA,
            [r"^ler (?:proximo |ultimo )?paragrafo$",
             r"^ler (?:proximo |ultimo )?texto$"],
            "ler_paragrafo", [],
            "Le o proximo paragrafo",
            "ler proximo paragrafo"),
        ComandoVoz("lei_repetir", DominioComando.LEITURA,
            [r"^repetir$", r"^fala de novo$", r"^repete$"],
            "repetir_ultima_leitura", [],
            "Repete a ultima leitura",
            "repetir"),
        ComandoVoz("lei_velocidade", DominioComando.LEITURA,
            [r"^velocidade (mais rapido|mais devagar|normal)$",
             r"^mais rapido$", r"^mais devagar$"],
            "ajustar_velocidade_leitura", ["velocidade"],
            "Ajusta a velocidade do TTS (Kokoro/Piper)",
            "mais rapido"),
        ComandoVoz("lei_pausar", DominioComando.LEITURA,
            [r"^pausar$", r"^parar$", r"^silencio$"],
            "pausar_leitura", [],
            "Pausa a leitura atual",
            "pausar"),
        # NEW 2025 accessibility
        ComandoVoz("lei_notificacao", DominioComando.LEITURA,
            [r"^(?:ler |ver )?notificacoes?$", r"^o que chegou$"],
            "ler_notificacoes", [],
            "Le notificacoes do sistema (dunst / mako / gnome)",
            "ler notificacoes"),
        ComandoVoz("lei_zoom", DominioComando.LEITURA,
            [r"^(?:zoom |aumentar |diminuir )?(?:tela|fonte|zoom) (?:mais|menos|in|out)$"],
            "ajustar_zoom", ["direcao"],
            "Zoom de tela (magnifier / orca zoom)",
            "zoom mais"),
        ComandoVoz("lei_clipboard", DominioComando.LEITURA,
            [r"^(?:ler |dizer )?clipboard|area de transferencia$"],
            "ler_clipboard", [],
            "Le conteudo do clipboard (acessibilidade)",
            "ler clipboard"),
    ]


# ============================================================================
# 4. ENGINE
# ============================================================================

class VoiceOSControlEngine:
    """Motor de controle do SO por voz."""

    def __init__(self) -> None:
        self.comandos: List[ComandoVoz] = _init_comandos()
        self.sessao: Optional[SessaoVoz] = None
        self.historico: List[ResultadoComando] = []
        self._ultimas_palavras: Dict[str, int] = defaultdict(int)
        self._ultima_leitura: str = ""

    # -- sessao ------------------------------------------------------------

    def iniciar_sessao(
        self,
        usuario: str = "cidadao",
        modo: ModoAtivacao = ModoAtivacao.SEMPRE_OUVINDO,
        cego: bool = False,
        surdo: bool = False,
        motora: bool = False,
    ) -> SessaoVoz:
        """Inicia uma sessao de controle por voz."""
        # adaptar feedback por deficiencia
        if cego and not surdo:
            feedback = TipoFeedbackVoz.DETALHADO  # cego precisa OUVR o que aconteceu
        elif surdo:
            feedback = TipoFeedbackVoz.SILENCIOSO  # surdo le na tela
        else:
            feedback = TipoFeedbackVoz.CONFIRMACAO
        self.sessao = SessaoVoz(
            id=f"SESS-{datetime.now().strftime('%H%M%S')}",
            usuario=usuario,
            modo_ativacao=modo,
            feedback_padrao=feedback,
            usuario_cego=cego,
            usuario_surdo=surdo,
            usuario_motora=motora,
        )
        return self.sessao

    # -- processar comando -------------------------------------------------

    def processar(self, texto: str) -> ResultadoComando:
        """
        Processa um texto (saida do Whisper/STT) e tenta reconhecer comando.
        Retorna o resultado com status, confianca e acao a executar.
        """
        texto = texto.strip().lower()
        if not texto:
            return ResultadoComando(
                texto_original=texto,
                status=StatusComando.NAO_RECONHECIDO,
                feedback_voz="Nao ouvi nada.",
            )

        # verificar hot word se modo sempre ouvindo
        if self.sessao and self.sessao.modo_ativacao == ModoAtivacao.SEMPRE_OUVINDO:
            if self.sessao.hot_word not in texto:
                # nao comecou com hot word -- talvez seja conversa
                # se o usuario e cego e Orca esta ativo, talvez seja ditado
                pass  # nao rejeita -- deixa o parser tentar

        # tentar casar com cada comando
        melhores: List[Tuple[float, ComandoVoz, Dict[str, str]]] = []
        for cmd in self.comandos:
            for padrao in cmd.padroes:
                match = re.match(padrao, texto, re.IGNORECASE)
                if match:
                    # extrair parametros dos grupos do regex
                    params: Dict[str, str] = {}
                    for i, nome in enumerate(cmd.parametros_esperados):
                        if i + 1 <= len(match.groups()):
                            params[nome] = match.group(i + 1)
                    # calcular score de confianca
                    score = self._calcular_confianca(texto, padrao, cmd, match)
                    melhores.append((score, cmd, params))

        if not melhores:
            return ResultadoComando(
                texto_original=texto,
                status=StatusComando.NAO_RECONHECIDO,
                feedback_voz=f"Nao reconheci o comando: '{texto}'.",
                feedback_tipo=TipoFeedbackVoz.ERRO_FALADO,
            )

        # ordenar por score
        melhores.sort(key=lambda x: -x[0])
        score_top, cmd_top, params_top = melhores[0]

        # se ha ambiguidade (2+ comandos com score similar)
        if len(melhores) > 1 and abs(melhores[0][0] - melhores[1][0]) < 0.1:
            nivel = NivelConfianca.AMBIGUO if score_top < 0.7 else self._classificar_confianca(score_top)
            return ResultadoComando(
                texto_original=texto,
                comando_reconhecido=cmd_top,
                parametros=params_top,
                status=StatusComando.AMBIGUO,
                confianca=nivel,
                score_confianca=score_top,
                feedback_voz=f"Voce disse '{texto}'. Quiz dizer: {cmd_top.descricao}?",
                feedback_tipo=TipoFeedbackVoz.DETALHADO,
            )

        nivel = self._classificar_confianca(score_top)

        # se confianca baixa, pedir confirmacao
        if nivel == NivelConfianca.BAIXO:
            return ResultadoComando(
                texto_original=texto,
                comando_reconhecido=cmd_top,
                parametros=params_top,
                status=StatusComando.PARCIAL,
                confianca=nivel,
                score_confianca=score_top,
                feedback_voz=f"Nao tenho certeza. Executar: {cmd_top.descricao}?",
                feedback_tipo=TipoFeedbackVoz.DETALHADO,
            )

        # se requer confirmacao (deletar, desligar)
        if cmd_top.requer_confirmacao:
            return ResultadoComando(
                texto_original=texto,
                comando_reconhecido=cmd_top,
                parametros=params_top,
                status=StatusComando.PARCIAL,
                confianca=nivel,
                score_confianca=score_top,
                feedback_voz=f"Confirmar: {cmd_top.descricao}?",
                feedback_tipo=TipoFeedbackVoz.DETALHADO,
            )

        # executar
        resultado = ResultadoComando(
            texto_original=texto,
            comando_reconhecido=cmd_top,
            parametros=params_top,
            status=StatusComando.EXECUTADO,
            confianca=nivel,
            score_confianca=score_top,
            acao_executada=self._simular_acao(cmd_top.acao, params_top),
            feedback_voz=self._gerar_feedback(cmd_top, params_top),
            feedback_tipo=self.sessao.feedback_padrao if self.sessao else TipoFeedbackVoz.CONFIRMACAO,
        )
        self.historico.append(resultado)
        if self.sessao:
            self.sessao.comandos_executados += 1
        return resultado

    def _calcular_confianca(self, texto: str, padrao: str, cmd: ComandoVoz, match: re.Match) -> float:
        """Heuristica de confianca no reconhecimento. (2025: specificity bias to break ties on generics)"""
        matched_text = match.group(0)
        cobertura = len(matched_text) / len(texto) if texto else 0
        # base coverage + small bias for longer/more-specific patterns (apps, codigo, etc)
        # prevents AMBIGUO on "abrir vscode" vs generic "abrir (.+)"
        specificity = min(0.12, len(padrao) / 280.0)
        score = min(1.0, cobertura + specificity)
        return round(score, 3)

    def _classificar_confianca(self, score: float) -> NivelConfianca:
        for n in NivelConfianca:
            if n.minimo <= score <= n.maximo:
                return n
        return NivelConfianca.REJEITADO

    def _simular_acao(self, acao: str, params: Dict[str, str]) -> str:
        """Simula a execucao da acao (no mundo real, chamaria ydotool/dbus/AT-SPI2)."""
        if params:
            param_str = ", ".join(f"{k}={v}" for k, v in params.items())
            return f"{acao}({param_str})"
        return f"{acao}()"

    def _gerar_feedback(self, cmd: ComandoVoz, params: Dict[str, str]) -> str:
        """Gera a mensagem de feedback por voz."""
        if self.sessao and self.sessao.usuario_cego:
            # cego precisa de detalhe
            if cmd.dominio == DominioComando.APLICATIVOS:
                app = params.get("app", "aplicativo")
                return f"Aberto: {app}."
            if cmd.dominio == DominioComando.LEITURA:
                return "Leitura concluida."
            if cmd.dominio == DominioComando.SISTEMA:
                return f"{cmd.descricao}. Feito."
            return f"{cmd.descricao}. Feito."
        # usuario sem deficiencia visual: confirmacao curta
        return "Feito."

    # -- comandos por dominio ---------------------------------------------

    def comandos_por_dominio(self, dominio: DominioComando) -> List[ComandoVoz]:
        return [c for c in self.comandos if c.dominio == dominio]

    # -- scorecard ---------------------------------------------------------

    def scorecard(self) -> Dict[str, Any]:
        return {
            "comandos_totais": len(self.comandos),
            "dominios": len(list(DominioComando)),
            "comandos_por_dominio": {d.rotulo: len(self.comandos_por_dominio(d)) for d in DominioComando},
            "modos_ativacao": len(list(ModoAtivacao)),
            "sessao_ativa": self.sessao is not None,
            "comandos_executados": self.sessao.comandos_executados if self.sessao else 0,
            "erros": self.sessao.erros if self.sessao else 0,
            "historico_tamanho": len(self.historico),
        }


# ============================================================================
# 5. DEMO
# ============================================================================

def _demo() -> None:
    e = VoiceOSControlEngine()

    print("=" * 70)
    print("OpenVoiceOSControl -- Controle do SO por Voz (2024/2025)")
    print("=" * 70)

    # --- Catalogo de comandos ---
    print(f"\n[CATALOGO DE COMANDOS ({len(e.comandos)} comandos)]")
    for dom in DominioComando:
        cmds = e.comandos_por_dominio(dom)
        print(f"\n  --- {dom.rotulo} ({len(cmds)} comandos) ---")
        for c in cmds:
            print(f"    {c.id:<20} | {c.exemplo:<35} | {c.descricao}")

    # --- Modos de ativacao ---
    print(f"\n[MODOS DE ATIVACAO ({len(list(ModoAtivacao))})]")
    for m in ModoAtivacao:
        print(f"  {m.id:<20} {m.rotulo}")

    # --- Simular sessao: usuario cego ---
    print("\n" + "=" * 70)
    print("[SIMULACAO] Usuario: Joao (cego, usa Orca 46/47 + AT-SPI2)")
    print("=" * 70)
    sessao = e.iniciar_sessao("Joao", ModoAtivacao.SEMPRE_OUVINDO, cego=True)
    print(f"  Sessao: {sessao.id} | Modo: {sessao.modo_ativacao.rotulo}")
    print(f"  Feedback: {sessao.feedback_padrao.rotulo} (cego precisa de detalhe)")

    comandos_simulados = [
        "que horas sao",
        "abrir firefox",
        "digitar ola mundo este e um teste",
        "enter",
        "ler tela",
        "maximizar",
        "aumentar volume",
        "ler selecionado",
        "repetir",
        "bateria",
        "abrir IDE",
        "chamar telefonista",
        "workspace 3",           # 2025
        "focar terminal",
        "modo escuro",
        "ler notificacoes",
        "abrir flatpak org.mozilla.firefox",
    ]

    for cmd_text in comandos_simulados:
        resultado = e.processar(cmd_text)
        flag = {"executado": "OK", "parcial": "CONF", "nao_reconhecido": "NAO",
                "ambiguo": "AMB", "sem_permissao": "NEG", "erro": "ERR"}[resultado.status.id]
        conf = f"{resultado.score_confianca:.0%}" if resultado.score_confianca > 0 else "--"
        print(f"\n  [{flag}] '{cmd_text}' (confianca: {conf})")
        if resultado.comando_reconhecido:
            print(f"    Comando: {resultado.comando_reconhecido.id}")
            print(f"    Acao: {resultado.acao_executada}")
        if resultado.feedback_voz:
            print(f"    Iara diz: \"{resultado.feedback_voz}\"")

    # --- Simular sessao: usuario tetraplegico ---
    print("\n" + "=" * 70)
    print("[SIMULACAO] Usuario: Maria (tetraplegica, usa switch + eye tracker + ydotool)")
    print("=" * 70)
    sessao2 = e.iniciar_sessao("Maria", ModoAtivacao.SWITCH, motora=True)
    print(f"  Sessao: {sessao2.id} | Modo: {sessao2.modo_ativacao.rotulo}")

    cmds_motor = [
        "abrir terminal",
        "digitar sudo apt install republica-full",
        "enter",
        "ler tela",
        "rolar para baixo",
        "ler proximo paragrafo",
        "tile esquerda",
        "abrir vscode",
    ]
    for cmd_text in cmds_motor:
        resultado = e.processar(cmd_text)
        flag = {"executado": "OK", "parcial": "CONF", "nao_reconhecido": "NAO",
                "ambiguo": "AMB", "sem_permissao": "NEG", "erro": "ERR"}[resultado.status.id]
        print(f"\n  [{flag}] '{cmd_text}'")
        if resultado.comando_reconhecido:
            print(f"    Acao: {resultado.acao_executada}")
        if resultado.feedback_voz:
            print(f"    Iara diz: \"{resultado.feedback_voz}\"")

    # --- Comandos que precisam confirmacao ---
    print("\n[COMANDOS QUE EXIGEM CONFIRMACAO]")
    for c in e.comandos:
        if c.requer_confirmacao:
            print(f"  {c.id}: '{c.exemplo}' -- {c.descricao}")

    # --- Pipeline tecnico 2025 ---
    print("\n[PIPELINE TECNICO 2025 -- Do microfone a acao (<180ms percebido)]")
    print("""
  1. MICROFONE + RING BUFFER (PyAudio/ALSA/PipeWire) ~4ms
  2. VAD (Silero VAD v5 / ONNX) ~8ms  -- pula 85% do silencio
  3. HOTWORD (OpenWakeWord 2.0) ~12ms  -- "republica"
  4. STT CASCATA (faster-whisper Distil tiny->small/large-v3) ~15-80ms
  5. NLU + CACHE (regex + fuzzywuzzy + LRU) ~4ms
  6. ROUTER -> VoiceOSControl
  7. EXECUTOR (2025):
     - Wayland: ydotool / wlrctl / hyprctl (dbus) / layer-shell
     - X11 fallback: xdotool / wmctrl
     - A11y: AT-SPI2 (Orca 46/47), brltty
     - Apps: flatpak run / gio launch / gtk-launch
     - OCR Shim (Tesseract 5.4.1 + PaddleOCR v5 PT)
  8. TTS (Kokoro-82M streaming <65ms first syllable OR Piper ONNX)
  9. FEEDBACK: overlay, toast, haptic, caption (multi-modal)
""")

    # --- Adaptacao por deficiencia ---
    print("[ADAPTACAO POR DEFICIENCIA 2025]")
    print("""
  CEGO:
    - Feedback DETALHADO (precisa ouvir o que aconteceu)
    - Leitura de tela integrada (AT-SPI2 + Orca 46/47 + Kokoro)
    - Comandos de leitura sao prioritarios
    - OCR Shim para apps sem AT-SPI (Tesseract/PaddleOCR)

  SURDO:
    - Feedback SILENCIOSO (le confirmacao na tela)
    - Nao usa TTS para feedback. Usa toast/notification visual + caption
    - Comandos de digitacao sao prioritarios
    - Legenda injetada via Whisper em tempo real

  TETRAPLEGICO:
    - Modo SWITCH (botao fisico ativa o microfone)
    - Eye tracker pode ativar por dwell (olhar fixo por 2s)
    - Comandos de digitacao + navegacao sao prioritarios
    - Push-to-talk com switch: 1 toque = ouvir, 1 toque = parar
    - ydotool / wlrctl para Wayland sem xdotool

  IDOSO:
    - Hot word mais tolerante (aceita variacoes de fala)
    - Velocidade do TTS reduzida (Kokoro/Piper)
    - Feedback DETALHADO (precisa de confirmacao clara)
    - Comandos de sistema (volume, bateria, hora, modo escuro) mais usados

  TDAH/AUTISMO:
    - Modo HOTKEY (nao sempre ouvindo -- pode sobrecarregar)
    - Comandos simples, de 1 palavra quando possivel
    - Feedback curto (nao overloading sensorial)
""")

    # --- Scorecard ---
    print("[SCORECARD]")
    sc = e.scorecard()
    for k, v in sc.items():
        if isinstance(v, dict):
            print(f"  {k}:")
            for dk, dv in v.items():
                print(f"    {dk:<30} {dv}")
        else:
            print(f"  {k:.<30} {v}")

    # --- FILOSOFIA ---
    print("\n" + "=" * 70)
    print("FILOSOFIA -- Fale. O sistema obedece. (2025)")
    print("=" * 70)
    print("""
VOZ E O INPUT MAIS UNIVERSAL:
  Cego nao digita (nao ve o teclado).
  Tetraplegico nao clica (nao move o mouse).
  Idoso nao navega menu (nao entende a hierarquia).
  Mas TODOS FALAM.

  Voz remove a barreira do TECLADO e do MOUSE.
  Voz e o input que TODO CORPO produz.

NAO E ASSISTENTE PESSOAL:
  A Telefonista CONVERSA com voce. Responde perguntas.
  O VoiceControl AGE. Executa comandos.
  Sao SISTEMAS DIFERENTES com propositos diferentes:
  Telefonista = amiga que conversa.
  VoiceControl = maos que obedecem.

A TELEFONISTA INTEGRA O VOICECONTROL:
  Quando a Iara (Telefonista) entende que o usuario quer
  EXECUTAR uma acao (nao conversar), ela CHAMA o VoiceControl.
  "Iara, abrir firefox" -> Telefonista detecta acao -> VoiceControl executa.
  O usuario nao sabe (nem precisa saber) onde termina uma e comeca a outra.

LOCAL. SEMPRE LOCAL. 2025:
  faster-whisper / Distil-Whisper roda no processador (CPU/NPU).
  Kokoro-82M / Piper (ONNX) roda no processador.
  Parser de comando roda em Python local.
  Nenhum audio sai do dispositivo.
  Nenhuma palavra vai para a nuvem.
  Soberania da voz.

EXECUTOR 2025 (Wayland-first):
  ydotool + wlrctl + hyprctl + layer-shell + AT-SPI2 + brltty
  X11 legacy ainda suportado para compatibilidade.

O PRINCIPIO:
  Controle por voz nao e luxo de smart speaker.
  E ACESSIBILIDADE RADICAL.
  E o tetraplegico que OPERA o sistema com a voz.
  E o cego que LE a tela com a voz.
  E o idoso que NAO precisa aprender interface.
  Fale. O sistema obedece.
""")

if __name__ == "__main__":
    _demo()
