#!/usr/bin/env python3
"""
OpenIara -- A IA da Republica com Corpo Visual no Terminal
============================================================
"Iara conversa. Jarvis executa. Ambas habitam o terminal transparente."

OpenIara e a UNIFICACAO de:
- Telefonista (conversa humanizada)
- VoiceOSControl (executa comandos)
- Jarvis Overlay (corpo visual transparente)
- Tutor CLI (ensina enquanto usa)

O TERMINAL E A CASA DA IARA:
A Republica usa tiling WM (i3/hyprland) como interface PADRAO.
Tiling WM e keyboard-first. Sem mouse. Sem busca de icone.
Tudo por atalho. Tudo por teclado.

PARA ACESSIBILIDADE, ISTO E REVOLUCIONARIO:
- Cego: nao precisa achar o mouse. Teclado e tudo.
- Tetraplegico: eye tracker + atalhos > mouse preciso.
- TDAH: sem distração visual. Sem icones. Sem clutter.
- Idoso: menos opçoes visuais = menos confusão.

MAS PRECISA ENSINAR. E ai entra o TUTOR CLI:
A Iara ENSINA os atalhos enquanto o usuario usa.
"Voce quer abrir o Firefox? Digite: Mod+d (workspace 1), depois 'firefox'".
Aprende fazendo. Kaizen: 1% ao dia.

I3 VS HYPRLAND (a decisao):

i3 (X11):
+ AT-SPI funciona. Orca le as janelas.
+ 15 anos de estabilidade. Documentacao vasta.
+ Configuracao em texto puro (~/.config/i3/config).
- X11 e legado (Wayland e o futuro).
- Sem animaçoes (purista).

HYPRLAND (Wayland):
+ Wayland nativo (moderno, seguro, performante).
+ Animaçoes e blur (bonito).
+ Configuração em texto (~/.config/hypr/hyprland.conf).
- AT-SPI instavel em Wayland com GPU rendering.
- Orca PODE nao funcionar (GPU renderiza, AT-SPI nao ve).
- Mais jovem (menos documentacao).

A DECISAO DA REPUBLICA:
i3 como PADRAO (acessibilidade garantida com AT-SPI + Orca).
Hyprland como ALTERNATIVA (para usuarios sem deficiencia visual).
Mesma logica do GNOME Terminal vs Kitty.
Acessibilidade decide o padrao, nao a estetica.

O OVERLAY JARVIS:
Terminal transparente (overlay) sempre visivel.
Mostra estado da Iara: ouvindo, pensando, falando.
Voz robotica (espeak) para comandos. Voz humana (Chatterbox) para conversa.
O usuario VE e OUVE a IA. A IA tem CORPO.

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field
from collections import defaultdict
from datetime import datetime
import re
import time


# ============================================================================
# 1. ENUMS
# ============================================================================

class ModoIara(Enum):
    """Modos de operacao da Iara."""
    IARA = ("iara", "Iara: conversa humanizada, responde perguntas")
    JARVIS = ("jarvis", "Jarvis: executa comandos, voz robotica, overlay")
    TUTOR = ("tutor", "Tutor: ensina CLI e atalhos enquanto usa")
    SILENCIOSO = ("silencioso", "Silencioso: so executa, sem voz nem overlay")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class EstadoVisual(Enum):
    """Estados do overlay visual da Iara."""
    DORMINDO = ("dormindo", "Dormindo: aguardando hot word ou hotkey")
    OUVINDO = ("ouvindo", "Ouvindo: capturando audio do microfone")
    PROCESSANDO = ("processando", "Processando: analisando comando")
    FALANDO = ("falando", "Falando: gerando resposta de voz")
    ERRO = ("erro", "Erro: algo deu errado")
    TUTORIAL = ("tutorial", "Tutorial: mostrando dica de CLI")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoVoz(Enum):
    """Tipos de voz da Iara."""
    ROBOTICA_ESPEAK = ("robotica", "Robotica (espeak-ng): estilo Jarvis, zero latencia")
    KOKORO_LEVE = ("kokoro", "Kokoro-82M: voz natural leve, todo hardware")
    CHATTERBOX_HUMANO = ("chatterbox", "Chatterbox: voz humanizada com emocao, GPU/NPU")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TilingWM(Enum):
    """Gerenciadores de janela tiling suportados."""
    I3 = ("i3", "i3wm (X11) -- PADRAO da Republica. AT-SPI + Orca funciona.")
    HYPRLAND = ("hyprland", "Hyprland (Wayland) -- alternativo. Sem Orca. Mais bonito.")
    SWAY = ("sway", "Sway (Wayland) -- i3-compatible. Mais estavel que Hyprland.")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class NivelTutorial(Enum):
    """Nivel de intrusao do tutor CLI."""
    DESLIGADO = ("desligado", "Desligado: sem dicas (usuario avancado)")
    SUTIL = ("sutil", "Sutil: dica no cado, sem interromper")
    ATIVO = ("ativo", "Ativo: dica + atalho sugerido apos cada acao")
    MODO_ESCOLA = ("escola", "Modo Escola: para no que faz errado e ensina o certo")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoAtalhoCLI(Enum):
    """Categorias de atalhos que o tutor ensina."""
    NAVEGACAO_WM = ("nav_wm", "Navegacao do WM (trocar workspace, janela)")
    JANELA = ("janela", "Manipular janela (mover, redimensionar, fechar)")
    TERMINAL = ("terminal", "Terminal (tab, split, copiar, colar)")
    SHELL = ("shell", "Shell (historico, auto-completar, pipes)")
    ARQUIVO = ("arquivo", "Sistema de arquivos (ls, cd, cp, mv, rm)")
    TEXTO = ("texto", "Edicao de texto (vim, nano, atalhos)")
    REPUBLICA = ("republica", "Apps da Republica (IDE, Telefonista, Energy)")
    ACESSIBILIDADE = ("a11y", "Acessibilidade (Orca, leitura, zoom)")

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
class AtalhoCLI:
    """Um atalho de teclado ou comando CLI que o tutor ensina."""
    id: str
    categoria: TipoAtalhoCLI
    combinacao: str        # "Mod+Return", "Mod+d", "cd ~/Documentos"
    acao: str              # "Abrir terminal", "Workspace 1", "Navegar para pasta"
    descricao: str = ""
    dica_tutor: str = ""   # o que a Iara diz quando ensina


@dataclass
class LicaoCLI:
    """Uma licao do tutor de CLI."""
    id: str
    titulo: str
    nivel_dificuldade: int  # 1 (iniciante) a 5 (avancado)
    pre_requisitos: List[str] = field(default_factory=list)
    atalhos_ensinados: List[str] = field(default_factory=list)  # IDs de AtalhoCLI
    exercicio: str = ""     # "Abra o Firefox no workspace 2"
    explicacao: str = ""


@dataclass
class OverlayFrame:
    """Um frame do overlay visual da Iara."""
    estado: EstadoVisual
    texto_superior: str = ""   # "ouvindo..." / "Iara" / "processando..."
    texto_inferior: str = ""   # transcrição parcial / resposta
    waveform: List[float] = field(default_factory=list)  # barras 0.0-1.0
    cor: str = "cyan"          # cor do overlay (cyan=ouvindo, verde=falando, vermelho=erro)
    opacidade: float = 0.85    # 0.0=invisivel, 1.0=opaco
    duracao_ms: int = 0        # quanto tempo mostrar


@dataclass
class SessaoIara:
    """Sessao ativa da Iara (overlay + voz + tutor + comandos)."""
    id: str
    modo_atual: ModoIara = ModoIara.SILENCIOSO
    estado_visual: EstadoVisual = EstadoVisual.DORMINDO
    voz_padrao: TipoVoz = TipoVoz.KOKORO_LEVE
    wm: TilingWM = TilingWM.I3
    nivel_tutor: NivelTutorial = NivelTutorial.ATIVO
    # perfil do usuario
    usuario: str = ""
    cego: bool = False
    surdo: bool = False
    motora: bool = False
    tdah: bool = False
    idoso: bool = False
    # estatisticas
    comandos_executados: int = 0
    liçoes_aprendidas: int = 0
    erros: int = 0
    tempo_uso_min: float = 0.0
    # historico de overlays
    overlays: List[OverlayFrame] = field(default_factory=list)


# ============================================================================
# 3. DADOS: ATALHOS E LICOES
# ============================================================================

def _init_atalhos() -> List[AtalhoCLI]:
    """Define os atalhos que o tutor ensina."""
    return [
        # === NAVEGACAO WM ===
        AtalhoCLI("nav_ws1", TipoAtalhoCLI.NAVEGACAO_WM, "Mod+1",
            "Ir para workspace 1", "Trocar de area de trabalho",
            "Mod e 1 juntas. Cada workspace e uma area limpa."),
        AtalhoCLI("nav_ws2", TipoAtalhoCLI.NAVEGACAO_WM, "Mod+2",
            "Ir para workspace 2", "Trocar de area de trabalho",
            "Mod e 2. Organize: workspace 1 = navegador, 2 = terminal, 3 = IDE."),
        AtalhoCLI("nav_prox_ws", TipoAtalhoCLI.NAVEGACAO_WM, "Mod+e",
            "Proximo workspace", "Avancar area de trabalho",
            "Mod e e (de esquerda). Como Alt+Tab mas entre areas."),
        AtalhoCLI("nav_ant_ws", TipoAtalhoCLI.NAVEGACAO_WM, "Mod+q",
            "Workspace anterior", "Voltar area de trabalho",
            "Mod e q. Volta para a area anterior."),
        AtalhoCLI("nav_foco", TipoAtalhoCLI.NAVEGACAO_WM, "Mod+j / Mod+k",
            "Mover foco entre janelas", "Trocar de janela ativa",
            "Mod+j = baixo, Mod+k = cima. Vim-style. Setas tambem funcionam."),
        # === JANELA ===
        AtalhoCLI("jan_term", TipoAtalhoCLI.JANELA, "Mod+Return",
            "Abrir terminal", "Iniciar novo terminal",
            "Mod e Enter. O terminal e sua casa. Sempre acessivel."),
        AtalhoCLI("jan_fechar", TipoAtalhoCLI.JANELA, "Mod+Shift+q",
            "Fechar janela ativa", "Matar a janela atual",
            "Mod+Shift+q. Cuidado: fecha sem perguntar."),
        AtalhoCLI("jan_fullscreen", TipoAtalhoCLI.JANELA, "Mod+f",
            "Fullscreen (tela cheia)", "Maximizar janela ativa",
            "Mod+f. Toggle: aperta de novo para sair."),
        AtalhoCLI("jan_mover", TipoAtalhoCLI.JANELA, "Mod+Shift+j / Mod+Shift+k",
            "Mover janela de posicao", "Reposicionar janela",
            "Mod+Shift+direcao. A janela segue o teclado."),
        AtalhoCLI("jan_split", TipoAtalhoCLI.JANELA, "Mod+h / Mod+v",
            "Dividir tela (horizontal/vertical)", "Split tiling",
            "Mod+h = horizontal, Mod+v = vertical. Duas janelas lado a lado."),
        # === TERMINAL ===
        AtalhoCLI("term_novo", TipoAtalhoCLI.TERMINAL, "Mod+Return (no tmux: Ctrl+b c)",
            "Nova aba/terminal", "Abrir novo terminal",
            "No tmux: Ctrl+b depois c. Nova janela sem fechar a atual."),
        AtalhoCLI("term_split_h", TipoAtalhoCLI.TERMINAL, "Ctrl+b \"",
            "Dividir terminal horizontal", "Split do tmux",
            "Ctrl+b, solta, depois aspas. Dois terminais empilhados."),
        AtalhoCLI("term_split_v", TipoAtalhoCLI.TERMINAL, "Ctrl+b %",
            "Dividir terminal vertical", "Split do tmux",
            "Ctrl+b, solta, depois %. Dois terminais lado a lado."),
        AtalhoCLI("term_navegar", TipoAtalhoCLI.TERMINAL, "Ctrl+b seta",
            "Navegar entre paineis", "Trocar de terminal no split",
            "Ctrl+b, solta, depois seta. Move entre os splits."),
        AtalhoCLI("term_copiar", TipoAtalhoCLI.TERMINAL, "Ctrl+Shift+c",
            "Copiar selecao", "Copiar texto do terminal",
            "Ctrl+Shift+c (nao Ctrl+c que interrompe processo!)."),
        AtalhoCLI("term_colar", TipoAtalhoCLI.TERMINAL, "Ctrl+Shift+v",
            "Colar", "Colar texto no terminal",
            "Ctrl+Shift+v. Nao confunda com Ctrl+v."),
        # === SHELL ===
        AtalhoCLI("shell_hist", TipoAtalhoCLI.SHELL, "Seta para cima",
            "Historico de comandos", "Repetir comando anterior",
            "Seta cima navega o passado. Enter repete. Economiza digitacao."),
        AtalhoCLI("shell_autocomp", TipoAtalhoCLI.SHELL, "Tab",
            "Auto-completar", "Completar comando/caminho",
            "Tab completa. Digite 'fire' + Tab = 'firefox'. Magica do shell."),
        AtalhoCLI("shell_pipe", TipoAtalhoCLI.SHELL, "| (pipe)",
            "Encadear comandos", "Saida de um vira entrada do outro",
            "Pipe | conecta. 'ls | grep .py' = lista so arquivos Python."),
        AtalhoCLI("shell_ctrl_c", TipoAtalhoCLI.SHELL, "Ctrl+c",
            "Interromper processo", "Parar comando em execucao",
            "Ctrl+c PARA tudo. Processo travado? Ctrl+c. Sempre."),
        AtalhoCLI("shell_ctrl_l", TipoAtalhoCLI.SHELL, "Ctrl+l",
            "Limpar tela", "Limpar terminal",
            "Ctrl+l = clear. Rapido e nao perde o historico."),
        # === ARQUIVO ===
        AtalhoCLI("arq_ls", TipoAtalhoCLI.ARQUIVO, "ls",
            "Listar arquivos", "Ver o que tem na pasta",
            "ls lista. ls -la mostra TUDO com detalhes. ls -lh mostra tamanhos."),
        AtalhoCLI("arq_cd", TipoAtalhoCLI.ARQUIVO, "cd <pasta>",
            "Navegar para pasta", "Mudar de diretorio",
            "cd documentos. cd .. = voltar. cd ~ = casa. cd - = anterior."),
        AtalhoCLI("arq_cp", TipoAtalhoCLI.ARQUIVO, "cp <origem> <destino>",
            "Copiar arquivo", "Duplicar arquivo",
            "cp relatorio.txt backup.txt. Original fica. Destino e criado."),
        AtalhoCLI("arq_mv", TipoAtalhoCLI.ARQUIVO, "mv <origem> <destino>",
            "Mover/renomear", "Mover ou renomear arquivo",
            "mv arquivo.txt novo_nome.txt = renomeia. mv arquivo.txt ~/Desktop = move."),
        AtalhoCLI("arq_rm", TipoAtalhoCLI.ARQUIVO, "rm <arquivo>",
            "Deletar arquivo", "Remover arquivo",
            "CUIDADO: rm nao tem lixo. rm -rf / = apaga TUDO. Nunca faca."),
        AtalhoCLI("arq_mkdir", TipoAtalhoCLI.ARQUIVO, "mkdir <nome>",
            "Criar pasta", "Novo diretorio",
            "mkdir projetos. mkdir -p a/b/c cria estrutura inteira."),
        AtalhoCLI("arq_grep", TipoAtalhoCLI.ARQUIVO, "grep <termo> <arquivo>",
            "Buscar texto", "Procurar dentro de arquivo",
            "grep 'energia' *.py = acha 'energia' em todos os Python."),
        # === REPUBLICA ===
        AtalhoCLI("rep_ide", TipoAtalhoCLI.REPUBLICA, "republica-ide",
            "Abrir IDE inclusiva", "Iniciar OpenInclusiveIDE",
            "Digita 'republica-ide' no terminal. A IDE abre no browser."),
        AtalhoCLI("rep_iara", TipoAtalhoCLI.REPUBLICA, "republica-iara",
            "Iniciar Iara", "Ativar Telefonista + VoiceControl",
            "Digita 'republica-iara'. A Iara acorda e comeca a ouvir."),
        AtalhoCLI("rep_energy", TipoAtalhoCLI.REPUBLICA, "republica-energy",
            "Monitor de energia", "Abrir OpenEnergy",
            "Digita 'republica-energy'. Ve o status da microgrid."),
        AtalhoCLI("rep_audit", TipoAtalhoCLI.REPUBLICA, "sudo lynis audit system",
            "Auditoria de seguranca", "Rodar Lynis",
            "Sudo lynis audit system. Ve o score de seguranca do seu PC."),
        # === ACESSIBILIDADE ===
        AtalhoCLI("a11y_orca", TipoAtalhoCLI.ACESSIBILIDADE, "orca",
            "Ligar leitor de tela", "Ativar Orca para cegos",
            "Digita 'orca'. O leitor de tela comeca a falar tudo."),
        AtalhoCLI("a11y_zoom", TipoAtalhoCLI.ACESSIBILIDADE, "Super+Alt+8",
            "Lupa de tela", "Zoom para baixa visao",
            "Super+Alt+8 liga. Super+Alt+roda do mouse ajusta o zoom."),
        AtalhoCLI("a11y_contraste", TipoAtalhoCLI.ACESSIBILIDADE, "Super+Alt+c",
            "Alto contraste", "Toggle tema de alto contraste",
            "Super+Alt+c. Para baixa visao e fotossensibilidade."),
        AtalhoCLI("a11y_teclado_lento", TipoAtalhoCLI.ACESSIBILIDADE, "Config > Acessibilidade > Teclas lentas",
            "Teclas lentas", "Filtro para tremor motor",
            "Teclas lentas ignora toques acidentais. Para Parkinson e tremor."),
    ]


def _init_licoes() -> List[LicaoCLI]:
    """Define as licoes do tutor de CLI."""
    return [
        LicaoCLI("lic_01_terminal", "Abrir e usar o terminal", 1,
            [], ["jan_term"],
            "Abra um terminal usando Mod+Return",
            "O terminal e a porta para TUDO na Republica. Mod+Return abre."),
        LicaoCLI("lic_02_workspaces", "Organizar com workspaces", 1,
            ["lic_01_terminal"], ["nav_ws1", "nav_ws2", "nav_prox_ws"],
            "Abra o Firefox no workspace 1 e o terminal no workspace 2",
            "Workspaces sao mesas virtuais. Organize por tarefa."),
        LicaoCLI("lic_03_navegar_arquivos", "Navegar arquivos no terminal", 2,
            ["lic_01_terminal"], ["arq_ls", "arq_cd"],
            "Liste os arquivos da sua pasta de Documentos",
            "ls lista. cd navega. cd ~/Documents && ls ve seus documentos."),
        LicaoCLI("lic_04_split", "Dividir a tela", 2,
            ["lic_01_terminal"], ["term_split_h", "term_split_v", "term_navegar"],
            "Divida o terminal em 4 paineis com tmux",
            "tmux split. Ctrl+b % (vertical), Ctrl+b \" (horizontal)."),
        LicaoCLI("lic_05_pipes", "Encadear comandos com pipe", 3,
            ["lic_03_navegar_arquivos"], ["shell_pipe", "arq_grep"],
            "Encontre todos os arquivos .py que contem a palavra 'energia'",
            "grep -rl 'energia' *.py | wc -l conta quantos tem."),
        LicaoCLI("lic_06_republica_apps", "Usar apps da Republica por CLI", 2,
            ["lic_01_terminal"], ["rep_ide", "rep_iara", "rep_energy"],
            "Inicie a Iara e abra a IDE",
            "republica-iara & republica-ide. O & roda em background."),
        LicaoCLI("lic_07_seguranca", "Auditar seguranca do sistema", 3,
            ["lic_03_navegar_arquivos"], ["rep_audit"],
            "Rode uma auditoria Lynis e le o score",
            "sudo lynis audit system. Aprenda a ler o hardening index."),
        LicaoCLI("lic_08_iara_voz", "Controlar o sistema por voz", 2,
            ["lic_06_republica_apps"], [],
            "Ative a Iara e abra o Firefox por voz",
            "Diga: 'republica, abrir firefox'. A Iara executa."),
        LicaoCLI("lic_09_acessibilidade", "Ativar recursos de acessibilidade", 1,
            [], ["a11y_orca", "a11y_zoom", "a11y_contraste"],
            "Ligue o Orca e o zoom de tela",
            "orca para leitor de tela. Super+Alt+8 para zoom."),
        LicaoCLI("lic_10_customizar_wm", "Customizar o i3/hyprland", 4,
            ["lic_02_workspaces", "lic_04_split"], [],
            "Edite ~/.config/i3/config para mudar o wallpaper",
            "O arquivo de config e TEXTO. Edite com nano ou vim. Recarregue com Mod+Shift+r."),
    ]


# ============================================================================
# 4. ENGINE
# ============================================================================

class IaraEngine:
    """Motor da Iara: overlay + voz + tutor + comandos unificados."""

    def __init__(self) -> None:
        self.atalhos: List[AtalhoCLI] = _init_atalhos()
        self.licoes: List[LicaoCLI] = _init_licoes()
        self.sessao: Optional[SessaoIara] = None
        self._frame_counter = 0

    # -- sessao ------------------------------------------------------------

    def acordar(
        self,
        usuario: str = "cidadao",
        wm: TilingWM = TilingWM.I3,
        cego: bool = False,
        surdo: bool = False,
        motora: bool = False,
        tdah: bool = False,
        idoso: bool = False,
    ) -> SessaoIara:
        """Acorda a Iara. Ela comeca a existir no sistema."""
        # decidir modo inicial por perfil
        if cego:
            modo = ModoIara.IARA  # cego precisa conversar (voz humana)
            voz = TipoVoz.KOKORO_LEVE  # leve para nao cansar
        elif motora:
            modo = ModoIara.JARVIS  # tetraplegico executa (voz robotica overlay)
            voz = TipoVoz.ROBOTICA_ESPEAK
        elif idoso:
            modo = ModoIara.IARA  # idoso precisa de conversa clara
            voz = TipoVoz.CHATTERBOX_HUMANO  # voz mais natural
        elif tdah:
            modo = ModoIara.SILENCIOSO  # TDAH nao quer sobrecarga sensorial
            voz = TipoVoz.KOKORO_LEVE
        else:
            modo = ModoIara.JARVIS  # padrao: overlay + comando
            voz = TipoVoz.CHATTERBOX_HUMANO

        # nivel tutor
        if idoso or cego:
            tutor = NivelTutorial.MODO_ESCOLA  # maximo ensino
        elif tdah:
            tutor = NivelTutorial.SUTIL  # minima intrusao
        else:
            tutor = NivelTutorial.ATIVO

        self.sessao = SessaoIara(
            id=f"IARA-{datetime.now().strftime('%H%M%S')}",
            modo_atual=modo,
            voz_padrao=voz,
            wm=wm,
            nivel_tutor=tutor,
            usuario=usuario,
            cego=cego, surdo=surdo, motora=motora, tdah=tdah, idoso=idoso,
        )
        return self.sessao

    # -- deteccao: comando vs conversa ------------------------------------

    def detectar_modo(self, texto: str) -> ModoIara:
        """
        Decide se o que o usuario disse e COMANDO (Jarvis) ou CONVERSA (Iara).
        Baseado em padroes de linguagem.
        """
        texto_lower = texto.strip().lower()

        # padroes de COMANDO (imperativo, curto, acao)
        padroes_comando = [
            r"^(abrir|fechar|maximizar|minimizar|trocar|mover|abre|fecha|maximiza|minimiza)",
            r"^(digitar|escrever|ditar|digita|escreve)",
            r"^(rolar|descer|subir|voltar|avançar|clicar)",
            r"^(aumentar|diminuir|ligar|desligar|mutar|silenciar)",
            r"^(ler|repetir|pausar|parar)",
            r"^(enter|confirmar|enviar|copiar|colar|desfazer)",
            r"^(bateria|horas|hora|que horas)",
            r"^(abrir|iniciar|chamar).+(ide|telefonista|iara|energy|terminal|navegador|orca|seguranca)",
        ]
        for padrao in padroes_comando:
            if re.match(padrao, texto_lower):
                return ModoIara.JARVIS

        # padroes de CONVERSA (pergunta, dialogo)
        palavras_conversa = ["como", "por que", "qual", "quais", "o que", "onde",
                            "quando", "quem", "pode", "voce", "obrigado", "bom dia",
                            "boa tarde", "boa noite", "tudo bem", "ajuda"]
        for palavra in palavras_conversa:
            if palavra in texto_lower:
                return ModoIara.IARA

        # curto demais e nao reconhecido = talvez comando
        if len(texto_lower.split()) <= 3:
            return ModoIara.JARVIS

        # padrao: conversa
        return ModoIara.IARA

    # -- overlay visual ----------------------------------------------------

    def gerar_overlay(self, estado: EstadoVisual, texto_inf: str = "",
                      texto_sup: str = "", duracao_ms: int = 3000) -> OverlayFrame:
        """Gera um frame do overlay visual da Iara."""
        cores = {
            EstadoVisual.DORMINDO: ("cinza", 0.3),
            EstadoVisual.OUVINDO: ("cyan", 0.85),
            EstadoVisual.PROCESSANDO: ("amarelo", 0.75),
            EstadoVisual.FALANDO: ("verde", 0.85),
            EstadoVisual.ERRO: ("vermelho", 0.90),
            EstadoVisual.TUTORIAL: ("azul", 0.80),
        }
        cor, opacidade = cores.get(estado, ("branco", 0.5))
        # gerar waveform simulada
        waveform = self._simular_waveform(estado)
        # textos padrao por estado
        textos_sup = {
            EstadoVisual.DORMINDO: "◉ Iara",
            EstadoVisual.OUVINDO: "◉ ouvindo...",
            EstadoVisual.PROCESSANDO: "◈ processando...",
            EstadoVisual.FALANDO: "◆ Iara",
            EstadoVisual.ERRO: "✕ erro",
            EstadoVisual.TUTORIAL: "📖 tutor",
        }
        frame = OverlayFrame(
            estado=estado,
            texto_superior=texto_sup or textos_sup.get(estado, ""),
            texto_inferior=texto_inf,
            waveform=waveform,
            cor=cor,
            opacidade=opacidade,
            duracao_ms=duracao_ms,
        )
        if self.sessao:
            self.sessao.overlays.append(frame)
            self.sessao.estado_visual = estado
        return frame

    def _simular_waveform(self, estado: EstadoVisual) -> List[float]:
        """Simula barras de waveform para o overlay."""
        import random
        if estado == EstadoVisual.FALANDO:
            return [random.uniform(0.3, 1.0) for _ in range(20)]
        if estado == EstadoVisual.OUVINDO:
            return [random.uniform(0.1, 0.7) for _ in range(20)]
        if estado == EstadoVisual.PROCESSANDO:
            return [0.2, 0.2, 0.2, 0.2, 0.2] * 4
        return [0.0] * 20

    def renderizar_overlay_ascii(self, frame: OverlayFrame) -> str:
        """Renderiza o overlay em ASCII art (para terminal)."""
        barras = ""
        for v in frame.waveform[:20]:
            altura = int(v * 8)
            barras += "▁▂▃▄▅▆▇█"[min(altura, 7)]
        linhas = [
            f"╔══════════════════════════════════╗",
            f"║  {frame.texto_superior:<32} ║",
            f"║  {barras:<32} ║",
            f"║  {frame.texto_inferior[:32]:<32} ║",
            f"╚══════════════════════════════════╝",
        ]
        return "\n".join(linhas)

    # -- tutor CLI ----------------------------------------------------------

    def sugerir_atalho(self, acao_realizada: str) -> Optional[AtalhoCLI]:
        """
        Apos o usuario fazer uma acao, o tutor sugere o atalho de teclado.
        Kaizen: ensina 1 atalho por vez, sem sobrecarregar.
        """
        if not self.sessao or self.sessao.nivel_tutor == NivelTutorial.DESLIGADO:
            return None
        # mapear acao -> atalho que ensina
        mapeamento = {
            "abrir_app": "nav_ws1",  # ensina a ir para workspace
            "abrir_terminal": "jan_term",
            "fechar_janela": "jan_fechar",
            "maximizar": "jan_fullscreen",
            "digitar_texto": "shell_hist",  # ensina historico
            "navegar_pasta": "arq_cd",
            "abrir_arquivo": "arq_ls",
            "ler_tela": "a11y_orca",
        }
        atalho_id = mapeamento.get(acao_realizada)
        if atalho_id:
            return next((a for a in self.atalhos if a.id == atalho_id), None)
        return None

    def proxima_licao(self) -> Optional[LicaoCLI]:
        """Sugere a proxima licao baseada no nivel do usuario."""
        if not self.sessao:
            return None
        # licoes nao aprendidas, ordenadas por dificuldade
        aprendidas = set()  # simplificado: sem persistencia
        nao_aprendidas = [
            l for l in self.licoes
            if l.id not in aprendidas
            and all(pre in aprendidas for pre in l.pre_requisitos)
        ]
        if nao_aprendidas:
            return min(nao_aprendidas, key=lambda l: l.nivel_dificuldade)
        return None

    # -- pipeline unificado ------------------------------------------------

    def processar_input(self, texto: str) -> Dict[str, Any]:
        """
        Pipeline completo: detecta modo, executa, gera overlay, ensina.
        """
        if not self.sessao:
            self.acordar()

        # 1. detectar modo
        modo = self.detectar_modo(texto)
        self.sessao.modo_atual = modo

        # 2. overlay: ouvindo -> processando
        self.gerar_overlay(EstadoVisual.OUVINDO, texto_inf=texto[:32], duracao_ms=1000)
        self.gerar_overlay(EstadoVisual.PROCESSANDO, duracao_ms=500)

        # 3. executar baseado no modo
        if modo == ModoIara.JARVIS:
            # modo comando: executar + overlay falando
            resposta = f"Afirmativo. Executando: {texto}"
            voz = TipoVoz.ROBOTICA_ESPEAK if not self.sessao.cego else TipoVoz.KOKORO_LEVE
            overlay = self.gerar_overlay(EstadoVisual.FALANDO,
                texto_inf=resposta[:32], duracao_ms=2000)
            self.sessao.comandos_executados += 1
            # tutor: sugerir atalho
            dica = self.sugerir_atalho("abrir_app")
            if dica and self.sessao.nivel_tutor in (NivelTutorial.ATIVO, NivelTutorial.MODO_ESCOLA):
                self.gerar_overlay(EstadoVisual.TUTORIAL,
                    texto_sup=f"Dica: {dica.combinacao}",
                    texto_inf=dica.acao[:32], duracao_ms=4000)
        elif modo == ModoIara.IARA:
            # modo conversa: responder humanizado
            resposta = f"Entendi. Voce disse: '{texto}'. Como posso ajudar?"
            voz = self.sessao.voz_padrao
            overlay = self.gerar_overlay(EstadoVisual.FALANDO,
                texto_inf=resposta[:32], duracao_ms=3000)
        else:
            resposta = ""
            voz = TipoVoz.KOKORO_LEVE
            overlay = None

        # 4. voltar a dormir
        self.gerar_overlay(EstadoVisual.DORMINDO, duracao_ms=999999)

        return {
            "texto_original": texto,
            "modo_detectado": modo.id,
            "resposta": resposta,
            "voz_usada": voz.id,
            "overlay_final": self.renderizar_overlay_ascii(overlay) if overlay else "",
            "sessao_estados": len(self.sessao.overlays) if self.sessao else 0,
        }

    # -- config do WM -------------------------------------------------------

    def config_i3_padrao(self) -> str:
        """Gera o ~/.config/i3/config padrao da Republica."""
        return (
            "# RepublicaOS / i3 config -- Gerado por OpenIara\n"
            "# Tecla Mod = Super (Windows)\n"
            "set $mod Mod4\n"
            "\n"
            "# Terminal: Mod+Enter\n"
            "bindsym $mod+Return exec gnome-terminal\n"
            "\n"
            "# Fechar janela: Mod+Shift+q\n"
            "bindsym $mod+Shift+q kill\n"
            "\n"
            "# Workspaces\n"
            "set $ws1 \"1:Republica\"\n"
            "set $ws2 \"2:Terminal\"\n"
            "set $ws3 \"3:IDE\"\n"
            "set $ws4 \"4:Seguranca\"\n"
            "set $ws5 \"5:Energia\"\n"
            "bindsym $mod+1 workspace $ws1\n"
            "bindsym $mod+2 workspace $ws2\n"
            "bindsym $mod+3 workspace $ws3\n"
            "bindsym $mod+4 workspace $ws4\n"
            "bindsym $mod+5 workspace $ws5\n"
            "\n"
            "# Navegacao (Vim-style)\n"
            "bindsym $mod+j focus left\n"
            "bindsym $mod+k focus down\n"
            "bindsym $mod+l focus up\n"
            "bindsym $mod+ccedilla focus right\n"
            "\n"
            "# Split\n"
            "bindsym $mod+h split h\n"
            "bindsym $mod+v split v\n"
            "\n"
            "# Fullscreen\n"
            "bindsym $mod+f fullscreen toggle\n"
            "\n"
            "# Recarregar config\n"
            "bindsym $mod+Shift+r reload\n"
            "bindsym $mod+Shift+c restart\n"
            "\n"
            "# Apps da Republica\n"
            "bindsym $mod+F1 exec republica-iara\n"
            "bindsym $mod+F2 exec republica-ide\n"
            "bindsym $mod+F3 exec republica-energy\n"
            "bindsym $mod+F4 exec republica-security\n"
            "\n"
            "# Acessibilidade\n"
            "bindsym $mod+a exec orca --toggle  # Toggle Orca\n"
            "\n"
            "# Barra de status\n"
            "bar {\n"
            "    status_command i3status\n"
            "    position top\n"
            "}\n"
            "\n"
            "# Overlay da Iara (floating)\n"
            "for_window [class=\"IaraOverlay\"] floating enable,\n"
            "    border none, opacity 0.85, sticky enable\n"
        )

    # -- scorecard ----------------------------------------------------------

    def scorecard(self) -> Dict[str, Any]:
        return {
            "atalhos_cadastrados": len(self.atalhos),
            "licoes_cadastradas": len(self.licoes),
            "categorias_atalho": len(list(TipoAtalhoCLI)),
            "modos_iara": len(list(ModoIara)),
            "estados_visuais": len(list(EstadoVisual)),
            "tipos_voz": len(list(TipoVoz)),
            "wms_suportados": len(list(TilingWM)),
            "sessao_ativa": self.sessao is not None,
            "overlays_gerados": len(self.sessao.overlays) if self.sessao else 0,
            "comandos_executados": self.sessao.comandos_executados if self.sessao else 0,
        }


# ============================================================================
# 5. DEMO
# ============================================================================

def _demo() -> None:
    e = IaraEngine()

    print("=" * 70)
    print("OpenIara -- A IA da Republica com Corpo Visual")
    print("=" * 70)

    # --- Acordar a Iara ---
    print("\n[ACORDAR] Iara, modo cego (Orca ativo)")
    sessao = e.acordar(usuario="Joao", cego=True)
    print(f"  Sessao: {sessao.id}")
    print(f"  Modo: {sessao.modo_atual.rotulo}")
    print(f"  Voz: {sessao.voz_padrao.rotulo}")
    print(f"  WM: {sessao.wm.rotulo}")
    print(f"  Tutor: {sessao.nivel_tutor.rotulo}")

    # --- Deteccao de modo ---
    print("\n[DETECCAO DE MODO -- Comando vs Conversa]")
    testes = [
        "abrir firefox",
        "que horas sao",
        "digitar ola mundo",
        "bom dia iara, como voce esta?",
        "aumentar volume",
        "pode me ajudar com algo?",
        "ler tela",
        "maximizar",
    ]
    for t in testes:
        modo = e.detectar_modo(t)
        print(f"  '{t}'")
        print(f"    -> Modo: {modo.id.upper()}")

    # --- Overlay visual ---
    print("\n[OVERLAY VISUAL -- Jarvis no terminal]")
    frame = e.gerar_overlay(EstadoVisual.OUVINDO, texto_inf="abrindo firefox...")
    print(f"\n{e.renderizar_overlay_ascii(frame)}")
    frame2 = e.gerar_overlay(EstadoVisual.FALANDO, texto_inf="Abrindo Firefox.")
    print(f"\n{e.renderizar_overlay_ascii(frame2)}")
    frame3 = e.gerar_overlay(EstadoVisual.TUTORIAL,
        texto_sup="Dica: Mod+1", texto_inf="Voltar ao workspace Republica")
    print(f"\n{e.renderizar_overlay_ascii(frame3)}")

    # --- Pipeline completo ---
    print("\n[PIPELINE COMPLETO -- Input -> Modo -> Overlay -> Resposta]")
    e.acordar(usuario="Maria", motora=True)
    for texto in ["abrir navegador", "obrigada iara", "ler tela", "bateria"]:
        resultado = e.processar_input(texto)
        print(f"\n  Input: '{texto}'")
        print(f"  Modo: {resultado['modo_detectado']}")
        print(f"  Resposta: {resultado['resposta']}")
        print(f"  Voz: {resultado['voz_usada']}")

    # --- Tutor CLI ---
    print("\n[TUTOR CLI -- Atalhos que a Iara ensina]")
    for cat in TipoAtalhoCLI:
        atalhos_cat = [a for a in e.atalhos if a.categoria == cat]
        print(f"\n  --- {cat.rotulo} ({len(atalhos_cat)}) ---")
        for a in atalhos_cat:
            print(f"    {a.combinacao:<30} {a.acao}")
            if a.dica_tutor:
                print(f"      Iara ensina: \"{a.dica_tutor}\"")

    # --- Licoes ---
    print(f"\n[LICOES DO TUTOR ({len(e.licoes)} licoes)]")
    for lic in sorted(e.licoes, key=lambda l: l.nivel_dificuldade):
        estrelas = "★" * lic.nivel_dificuldade + "☆" * (5 - lic.nivel_dificuldade)
        print(f"\n  [{estrelas}] {lic.titulo}")
        print(f"    Exercicio: {lic.exercicio}")

    # --- Config i3 ---
    print("\n[CONFIG i3 PADRAO DA REPUBLICA]")
    config = e.config_i3_padrao()
    print(config)

    # --- Argumento: i3 vs Hyprland ---
    print("[I3 VS HYPRLAND -- A decisao da Republica]")
    print("""
  I3 (PADRAO):
    + AT-SPI funciona. Orca LE as janelas. CEGO USA.
    + 15 anos de estabilidade. Bugs conhecidos e corrigidos.
    + Configuracao em texto puro (~/.config/i3/config).
    + Sem GPU necessaria. Roda em RepublicaPort Essencial.
    - X11 (legado). Wayland e o futuro.
    - Sem animacoes. Purista.

  HYPRLAND (ALTERNATIVA):
    + Wayland nativo. Moderno.
    + Animacoes, blur, transicoes.
    + Mais seguro (Wayland isola janelas).
    - AT-SPI instavel. Orca PODE NAO FUNCIONAR. CEGO NAO USA.
    - Requer GPU. Nao roda no Essencial.
    - Mais jovem. Menos documentacao.

  A DECISAO:
    i3 = PADRAO (acessibilidade garante).
    Hyprland = ALTERNATIVA (para usuarios sem deficiencia visual).
    Mesma logica do GNOME Terminal vs Kitty.
    ACESSIBILIDADE DECIDE O PADRAO. Estetica decide a alternativa.
""")

    # --- FILOSOFIA ---
    print("=" * 70)
    print("FILOSOFIA -- Tiling WM como alfabetizacao digital")
    print("=" * 70)
    print("""
O PARADIGMA:

  Interface tradicional (GNOME, Windows, macOS):
    Mouse + icones + menus = FACIL PARA COMECAR.
    Mas o usuario NUNCA APRENDE o que acontece por baixo.
    E um PASSAGEIRO do sistema. Clica onde mandam.

  Tiling WM (i3, Hyprland):
    Teclado + atalhos + terminal = DIFICIL NO PRIMEIRO DIA.
    Mas o usuario APRENDE a estrutura do sistema.
    Vira PILOTO. Entende pastas, processos, rede, permissoes.

  A Republica escolhe o CAMINHO DIFICIL no inicio
  porque leva ao CAMINHO LIVRE no final.
  Kaizen: 1% ao dia. 37x em 1 ano.

A IARA ENSINA ENQUANTO USA:

  O usuario quer abrir o Firefox.
  Em vez de clicar num icone, ele APRENDE:
  "Mod+2 (workspace 2) -> firefox -> Enter"
  A Iara mostra a dica no overlay.
  O usuario faz. A Iara confirma: "Feito."
  Proxima vez, ele ja sabe. Nao precisa da dica.

  Cada acao e uma MICRO-LICAO.
  Cada dia, o usuario sabe 1% mais.
  Em 6 meses, ele e POWER USER sem ter feito curso.

O OVERLAY E O CORPO DA IARA:

  A Iara nao e so voz. Ela TEM CORPO.
  O overlay transparente e o corpo dela no terminal.
  O usuario VE que ela esta ouvindo (cyan).
  VE que ela esta pensando (amarelo).
  VE que ela esta falando (verde).
  VE quando ela ensina (azul).

  O cego OUVE os estados. O surdo VE os estados.
  Todo mundo sabe o que a Iara esta fazendo.
  Transparencia radical. P4.

VOZ ROBOTICA E IDENTIDADE, NAO DEFEITO:

  Jarvis tem voz robotica. GLaDOS tem voz robotica.
  A voz robotica diz: "EU SOU IA. NAO SOU HUMANO. NAO FINJO SER."
  E HONESTO. E P9 (transparencia).
  A Iara em modo Jarvis usa espeak (robotico) para COMANDOS.
  A Iara em modo Iara usa Chatterbox (humano) para CONVERSA.
  O usuario sabe qual modo esta ativo PELA VOZ.

O TERMINAL E A CASA:

  GNOME, Windows, macOS escondem o terminal.
  Tratam o terminal como ferramenta de especialista.
  A Republica COLOCA O TERMINAL NO CENTRO.
  O terminal e a CASA. A Iara vive la.
  Tudo comeca no terminal. Tudo volta pro terminal.
  Quem domina o terminal domina o sistema.
  Quem domina o sistema e LIVRE.
""")


if __name__ == "__main__":
    _demo()
