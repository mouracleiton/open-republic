#!/usr/bin/env python3
"""
OpenUniversalCaption -- Legendas em Tempo Real para TUDO
==========================================================
"Todo audio que sai do SO e legendado. Surdo nao perde nada."

O surdo nao ouve:
- Videochamada no Jitsi/Meet
- Video no YouTube
- Podcast no navegador
- Musica com letra
- Notificacao do sistema
- Alerta do sistema
- Voz da Iara

Este modulo captura TODO o audio que sai do SO (system audio)
e transcreve em tempo real com Whisper, exibindo legendas flutuantes.

NAO e legenda de um app so. E legenda do SISTEMA INTEIRO.

COMO FUNCIONA (pipeline):

  Audio do SO (PulseAudio/PipeWire/WASM loopback)
  -> Captura em chunks de 500ms
  -> Whisper (STT local) transcreve
  -> Filtro de ruido (musica != fala)
  -> Formatador de legenda (CC standard)
  -> Overlay flutuante na tela

3 MODOS DE LEGENDA:

1. MODO TOTAL: legendas tudo (videochamada + YouTube + podcast + sistema)
2. MODO COMUNICACAO: so transcreve fala humana (ignora musica/ruido)
3. MODO SISTEMA: so transcreve voz da Iara e notificacoes

FORMATO DA LEGENDA (CC standard):

  [14:32:05] Maria: "Bom dia, vamos comecar a reuniao."
  [14:32:12] Joao: "Pode deixar, ja estou com a apresentacao."
  [14:32:20] Maria: "Otimo. Primeiro item: orcamento."

CARACTERISTICAS:
- Posicao configuravel (baixo da tela, topo, overlay)
- Fonte configuravel (tamanho, cor, fundo)
- Cores por falante (se diarizacao disponivel)
- Timestamp em cada linha
- Buffer das ultimas 5 linhas (historico visivel)
- Maximo 2 linhas simultaneas (nao cobre tela inteira)

A ETICA DE LEGENDAR:

  O surdo tem DIREITO a saber o que esta sendo dito.
  Videochamada sem legenda e EXCLUSAO.
  Video institucional sem legenda e DESCASO.
  Podcast sem legenda e INACESSIBILIDADE.

  A Republica NAO pede legenda. A Republica LEGENDA.
  Automaticamente. Para tudo. Em tempo real. Local.

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field
from collections import deque
from datetime import datetime, timedelta
import re


# ============================================================================
# 1. ENUMS
# ============================================================================

class FonteAudio(Enum):
    """Fontes de audio que o SO pode legendars."""
    VIDEOCHAMADA = ("videochamada", "Videochamada (Jitsi, Meet, Zoom)")
    NAVEGADOR = ("navegador", "Navegador (YouTube, sites, podcasts)")
    MEDIA_PLAYER = ("media", "Player de midia (VLC, mpv)")
    SISTEMA = ("sistema", "Sistema (notificacoes, alertas)")
    IARA = ("iara", "Iara (voz da Telefonista)")
    MICROFONE_LOCAL = ("microfone", "Microfone local (pessoa falando ao lado)")
    DESCONHECIDA = ("desconhecida", "Fonte desconhecida")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class ModoLegenda(Enum):
    """Modos de operacao da legenda universal."""
    TOTAL = ("total", "Total: legendas todo audio do SO")
    COMUNICACAO = ("comunicacao", "Comunicacao: so fala humana (ignora musica)")
    SISTEMA = ("sistema", "Sistema: so Iara + notificacoes")
    DESLIGADO = ("desligado", "Desligado")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class PosicaoLegenda(Enum):
    """Onde a legenda aparece na tela."""
    BAIXO_CENTRO = ("baixo_centro", "Baixo centro (padrao TV/film)")
    BAIXO_ESQUERDA = ("baixo_esq", "Baixo esquerda")
    TOPO_CENTRO = ("topo_centro", "Topo centro")
    TOPO_DIREITA = ("topo_dir", "Topo direita (overlay)")
    CENTRO = ("centro", "Centro (para surdo-cego)")
    FLUTUANTE = ("flutuante", "Flutuante ( segue o foco)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class EstiloLegenda(Enum):
    """Estilo visual da legenda."""
    PADRAO = ("padrao", "Padrao: fundo preto semi-transparente, texto branco")
    ALTO_CONTRASTE = ("alto_contraste", "Alto contraste: fundo preto, texto amarelo")
    CAIXA = ("caixa", "Caixa: fundo preto opaco, texto branco, borda")
    MINIMALISTA = ("minimalista", "Minimalista: sem fundo, texto com sombra")
    GRANDE = ("grande", "Grande: fonte 28pt para baixa visao surdo-cego")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class StatusTranscricao(Enum):
    """Status de uma transcricao em andamento."""
    OUVINDO = ("ouvindo", "Ouvindo: capturando audio")
    TRANSCRIVENDO = ("transcrevendo", "Transcrevendo: Whisper processando")
    PRONTO = ("pronto", "Pronto: texto transcrito")
    VAZIO = ("vazio", "Vazio: silencio detectado")
    ERRO = ("erro", "Erro: falha na transcricao")
    MUSICA = ("musica", "Musica: audio nao-fala detectado (ignorar)")

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
class LinhaLegenda:
    """Uma linha de legenda exibida na tela."""
    id: str
    texto: str
    timestamp: str          # "14:32:05"
    fonte: FonteAudio = FonteAudio.DESCONHECIDA
    falante: str = ""       # "Maria" (se diarizacao)
    confianca: float = 0.0  # confianca do Whisper
    duracao_ms: int = 4000  # quanto tempo fica na tela
    cor_falante: str = "#FFFFFF"  # cor por falante
    parcial: bool = False   # transcrição parcial (ainda processando)


@dataclass
class SessaoLegenda:
    """Sessao ativa de legenda universal."""
    id: str
    modo: ModoLegenda = ModoLegenda.COMUNICACAO
    posicao: PosicaoLegenda = PosicaoLegenda.BAIXO_CENTRO
    estilo: EstiloLegenda = EstiloLegenda.PADRAO
    fonte_tamanho: int = 20  # pt
    max_linhas_tela: int = 2  # max simultaneas
    buffer_historico: int = 50  # linhas guardadas
    transcricoes_totais: int = 0
    silencios_ignorados: int = 0
    musicas_ignoradas: int = 0
    inicio: str = ""
    ativa: bool = True


@dataclass
class ConfigWhisper:
    """Configuracao do modelo Whisper para legenda (atualizado 2025)."""
    modelo: str = "large-v3-turbo"  # tiny, base, small, medium, large-v3, large-v3-turbo, distil-large-v3
    # 2024/2025 recomendados (OpenAI + community):
    # - large-v3-turbo: 809M params, otimizado para realtime, qualidade ~large-v3 com 4-8x velocidade
    # - distil-large-v3: distilled (756M), ~2x mais rapido que large-v3, qualidade muito proxima
    # - large-v3: 1550M params, estado-da-arte qualidade (Setembro 2023, ainda top em 2025)
    idioma: str = "pt"      # pt-BR (ou "pt", "en", "auto")
    chunk_ms: int = 500     # tamanho do chunk de audio (melhor 200-1000ms para latencia)
    beam_size: int = 1      # 1 = rapido (greedy), 5 = preciso (mais lento)
    vad_filter: bool = True # Voice Activity Detection (silencio skip)
    filtrar_musica: bool = True  # ignorar audio nao-fala (economiza GPU/CPU)
    device: str = "auto"    # "cpu", "cuda", "auto" (2025: cuda para large models)
    compute_type: str = "float16"  # "int8", "float16", "float32" (faster-whisper)


@dataclass
class PerfilUsuarioCC:
    """Perfil do usuario de legenda."""
    usuario: str = "cidadao"
    surdo: bool = True
    surdo_cego: bool = False
    baixa_visao: bool = False
    tdah: bool = False
    ler_labios: bool = False  # se le labios, ver o video e importante
    # preferencias
    velocidade_leitura: str = "normal"  # lento, normal, rapido
    mostrar_timestamp: bool = True
    mostrar_falante: bool = True
    max_caracteres_linha: int = 42  # CC standard


@dataclass
class ConfigDiarizacao:
    """Configuracao de diarizacao de falantes (atualizado 2025).

    Diarizacao = identificar QUEM falou o que ("Maria: ...", "Joao: ...").
    Essencial para videochamadas com multiplos participantes.
    """
    habilitada: bool = False
    # Modelos 2024/2025 recomendados:
    # - pyannote/speaker-diarization-3.1 (HuggingFace): SOTA em 2024/2025, excelente PT-BR
    #   Requer: pip install pyannote.audio ; huggingface-cli login (token gratuito)
    # - whisperX (bain/whisperX no GitHub): Whisper + diarizacao integrada + word-level alignment
    #   Mais usado em producao para legendas com speaker ID
    # - NeMo diarization (NVIDIA) ou Sortformer: mais rapido em GPUs NVIDIA
    # - pyannote 3.1 + clustering: qualidade mais alta, latencia maior
    modelo: str = "pyannote/speaker-diarization-3.1"
    min_duracao_falante: float = 0.5   # segundos minimos para registrar falante
    max_falantes: int = 6              # limite para evitar over-segmentation em calls grandes
    device: str = "cpu"                # "cuda" ou "mps" (Apple) recomendado para realtime em 2025
    hf_token: str = ""                 # token HuggingFace para modelos gated (pyannote)


# ============================================================================
# 3. MOTOR DE TRANSCRICAO (simulado)
# ============================================================================

class TranscritorWhisper:
    """
    Simula a transcricao de audio pelo Whisper em tempo real.
    No mundo real: faster-whisper ou whisper.cpp capturando audio do sistema.
    Aqui: simulacao deterministica para o demo.
    """

    # frases de exemplo para a simulacao
    FRASES_EXEMPLO = [
        "Bom dia a todos, vamos comecar a reuniao.",
        "Primeiro item da pauta: orcamento do trimestre.",
        "Alguem tem alguma duvida sobre os numeros?",
        "Acho que precisamos rever os custos de energia.",
        "Concordo, vamos colocar isso como prioridade.",
        "Pode passar para o proximo slide, por favor.",
        "O prazo final e sexta-feira que vem.",
        "Vou enviar o relatorio por email hoje a tarde.",
        "Obrigado pela participacao de todos.",
        "Boa tarde, em que posso ajudar?",
        "Estou com dificuldade para ouvir, pode repetir?",
        "Vamos definir as responsabilidades de cada um.",
    ]

    FRASES_IARA = [
        "Abrindo Firefox.",
        "Feito.",
        "Comando executado com sucesso.",
        "Nao reconheci o comando.",
        "Bateria em 45 por cento.",
        "Sao 14 horas e 32 minutos.",
    ]

    FRASES_SISTEMA = [
        "Atualizacao disponivel.",
        "Bateria fraca. Conecte o carregador.",
        "Conexao WiFi restabelecida.",
        "Novo email recebido.",
    ]

    MUSICAS_EXEMPLO = [
        "[musica instrumental]",
        "[trilha sonora]",
        "[efeito sonoro]",
        "[ruido de fundo]",
    ]

    def __init__(self) -> None:
        self._counter = 0

    def transcrever_chunk(
        self, fonte: FonteAudio = FonteAudio.DESCONHECIDA
    ) -> Optional[Tuple[str, float, bool]]:
        """
        Simula transcrever 1 chunk de audio.
        Retorna (texto, confianca, e_musica) ou None (silencio).
        """
        self._counter += 1

        # 60% silencio
        if self._counter % 10 < 6:
            return None

        # 10% musica/ruido (nao-fala)
        if self._counter % 10 == 6:
            if fonte == FonteAudio.NAVEGADOR:
                import random
                return (random.choice(self.MUSICAS_EXEMPLO), 0.3, True)
            return None

        # 30% fala
        import random
        if fonte == FonteAudio.IARA:
            texto = random.choice(self.FRASES_IARA)
        elif fonte == FonteAudio.SISTEMA:
            texto = random.choice(self.FRASES_SISTEMA)
        elif fonte == FonteAudio.VIDEOCHAMADA:
            texto = random.choice(self.FRASES_EXEMPLO)
        elif fonte == FonteAudio.NAVEGADOR:
            texto = random.choice(self.FRASES_EXEMPLO)
        else:
            texto = random.choice(self.FRASES_EXEMPLO)

        confianca = random.uniform(0.75, 0.98)
        return (texto, round(confianca, 3), False)


# ============================================================================
# 4. ENGINE
# ============================================================================

class UniversalCaptionEngine:
    """Motor de legenda universal para o SO."""

    def __init__(self) -> None:
        self.sessao: Optional[SessaoLegenda] = None
        self.transcritor = TranscritorWhisper()
        self.linhas: deque = deque(maxlen=50)  # historico
        self.tela_atual: List[LinhaLegenda] = []  # na tela agora
        self.perfil: PerfilUsuarioCC = PerfilUsuarioCC()
        self.config_whisper = ConfigWhisper()
        self.config_diarizacao = ConfigDiarizacao()
        self._linha_id = 0
        self._falante_colors: Dict[str, str] = {}
        self._paleta = ["#FFFFFF", "#00FF00", "#00CCFF", "#FFAA00",
                        "#FF69B4", "#AA77FF"]

    # -- sessao ------------------------------------------------------------

    def iniciar(
        self,
        usuario: str = "cidadao",
        modo: ModoLegenda = ModoLegenda.COMUNICACAO,
        posicao: PosicaoLegenda = PosicaoLegenda.BAIXO_CENTRO,
        estilo: EstiloLegenda = EstiloLegenda.PADRAO,
        surdo: bool = True,
        surdo_cego: bool = False,
        baixa_visao: bool = False,
    ) -> SessaoLegenda:
        """Inicia sessao de legenda universal."""
        # adaptar para surdo-cego
        if surdo_cego:
            posicao = PosicaoLegenda.CENTRO
            estilo = EstiloLegenda.GRANDE
        elif baixa_visao:
            estilo = EstiloLegenda.GRANDE

        self.sessao = SessaoLegenda(
            id=f"CC-{datetime.now().strftime('%H%M%S')}",
            modo=modo, posicao=posicao, estilo=estilo,
            inicio=datetime.now().isoformat(),
        )
        self.perfil = PerfilUsuarioCC(
            usuario=usuario, surdo=surdo, surdo_cego=surdo_cego,
            baixa_visao=baixa_visao,
        )
        return self.sessao

    # -- processar chunk ---------------------------------------------------

    def processar_chunk(
        self, fonte: FonteAudio = FonteAudio.DESCONHECIDA
    ) -> Optional[LinhaLegenda]:
        """
        Processa 1 chunk de audio do SO.
        No mundo real: captura de PulseAudio/PipeWire monitor.
        Aqui: simulacao.
        """
        if not self.sessao or not self.sessao.ativa:
            return None

        # filtrar por modo
        if self.sessao.modo == ModoLegenda.SISTEMA:
            if fonte not in (FonteAudio.IARA, FonteAudio.SISTEMA):
                return None
        elif self.sessao.modo == ModoLegenda.COMUNICACAO:
            if fonte == FonteAudio.SISTEMA and "notificacao" in fonte.id:
                pass  # nao ignora sistema, so filtra musica

        # transcrever
        resultado = self.transcritor.transcrever_chunk(fonte)

        if resultado is None:
            self.sessao.silencios_ignorados += 1
            return None

        texto, confianca, e_musica = resultado

        # filtrar musica se configurado
        if e_musica and self.config_whisper.filtrar_musica:
            self.sessao.musicas_ignoradas += 1
            return None

        # filtrar confianca baixa
        if confianca < 0.50:
            return None

        # criar linha de legenda
        self._linha_id += 1
        agora = datetime.now()
        timestamp = agora.strftime("%H:%M:%S")
        falante = self._detectar_falante(texto, fonte)

        linha = LinhaLegenda(
            id=f"CC-{self._linha_id:04d}",
            texto=texto,
            timestamp=timestamp,
            fonte=fonte,
            falante=falante,
            confianca=confianca,
            duracao_ms=self._calcular_duracao(texto),
            cor_falante=self._cor_para_falante(falante),
        )

        self.linhas.append(linha)
        self.sessao.transcricoes_totais += 1
        return linha

    def _detectar_falante(self, texto: str, fonte: FonteAudio) -> str:
        """Heuristica simples para identificar falante."""
        if fonte == FonteAudio.IARA:
            return "Iara"
        if fonte == FonteAudio.SISTEMA:
            return "Sistema"
        # simulacao: alternar entre 2 falantes em videochamada
        if fonte == FonteAudio.VIDEOCHAMADA:
            import random
            return random.choice(["Maria", "Joao", "Pedro"])
        return ""

    def _calcular_duracao(self, texto: str) -> int:
        """Calcula quanto tempo a legenda fica na tela (ms)."""
        # CC standard: ~15 caracteres por segundo de leitura
        chars = len(texto)
        segs = max(2, chars / 15)
        if self.perfil and self.perfil.velocidade_leitura == "lento":
            segs *= 1.5
        return int(segs * 1000)

    def _cor_para_falante(self, falante: str) -> str:
        """Atribui cor consistente a cada falante."""
        if not falante:
            return "#FFFFFF"
        if falante not in self._falante_colors:
            cor_idx = len(self._falante_colors) % len(self._paleta)
            self._falante_colors[falante] = self._paleta[cor_idx]
        return self._falante_colors[falante]

    # -- renderizar legenda (ASCII) ----------------------------------------

    def renderizar_ascii(self) -> str:
        """Renderiza a legenda atual como ASCII art (para terminal)."""
        if not self.tela_atual:
            return ""
        linhas_render = []
        for linha in self.tela_atual[-self.sessao.max_linhas_tela:]:
            ts = linha.timestamp if self.perfil.mostrar_timestamp else ""
            falante = f"{linha.falante}: " if linha.falante and self.perfil.mostrar_falante else ""
            prefix = f"[{ts}] {falante}"
            texto = linha.texto[:self.perfil.max_caracteres_linha]
            linhas_render.append(f"  {prefix}{texto}")
        return "\n".join(linhas_render)

    def renderizar_cc_box(self) -> str:
        """Renderiza legenda em formato de caixa CC standard."""
        if not self.tela_atual:
            return ""
        largura = self.perfil.max_caracteres_linha + 4
        borda = "═" * largura
        linhas_render = [f"  ╔{borda}╗"]
        for linha in self.tela_atual[-self.sessao.max_linhas_tela:]:
            ts = linha.timestamp if self.perfil.mostrar_timestamp else ""
            falante = f"{linha.falante}: " if linha.falante and self.perfil.mostrar_falante else ""
            texto = linha.texto[:self.perfil.max_caracteres_linha]
            conteudo = f"[{ts}] {falante}{texto}"
            conteudo = conteudo[:self.perfil.max_caracteres_linha].ljust(self.perfil.max_caracteres_linha)
            linhas_render.append(f"  ║ {conteudo} ║")
        linhas_render.append(f"  ╚{borda}╝")
        return "\n".join(linhas_render)

    # -- exportar transcricao ----------------------------------------------

    def exportar_transcricao(self) -> str:
        """Exporta a transcricao completa da sessao em texto."""
        if not self.linhas:
            return "(sem transcricao)"
        linhas_texto = []
        for linha in self.linhas:
            falante = f"{linha.falante}: " if linha.falante else ""
            linhas_texto.append(f"[{linha.timestamp}] {falante}{linha.texto}")
        return "\n".join(linhas_texto)

    # -- scorecard ---------------------------------------------------------

    def scorecard(self) -> Dict[str, Any]:
        return {
            "modos": len(list(ModoLegenda)),
            "fontes_audio": len(list(FonteAudio)),
            "posicoes": len(list(PosicaoLegenda)),
            "estilos": len(list(EstiloLegenda)),
            "transcricoes_totais": self.sessao.transcricoes_totais if self.sessao else 0,
            "silencios_ignorados": self.sessao.silencios_ignorados if self.sessao else 0,
            "musicas_ignoradas": self.sessao.musicas_ignoradas if self.sessao else 0,
            "linhas_historico": len(self.linhas),
            "falantes_identificados": len(self._falante_colors),
            "config_whisper_modelo": self.config_whisper.modelo,
            "config_chunk_ms": self.config_whisper.chunk_ms,
            "diarizacao_habilitada": self.config_diarizacao.habilitada if hasattr(self, "config_diarizacao") else False,
            "diarizacao_modelo": self.config_diarizacao.modelo if hasattr(self, "config_diarizacao") else "",
        }


# ============================================================================
# 5. DEMO
# ============================================================================

def _demo() -> None:
    e = UniversalCaptionEngine()

    print("=" * 70)
    print("OpenUniversalCaption -- Legendas em Tempo Real para TUDO")
    print("=" * 70)

    # --- Visao geral ---
    print(f"""
ESTE MODULO DA LEGENDAS PARA TODO O AUDIO DO SO:

  Videochamada (Jitsi/Meet/Zoom)   -> legendado
  YouTube / video no navegador      -> legendado
  Podcast / radio streaming         -> legendado
  Notificacoes do sistema           -> legendado
  Voz da Iara                       -> legendado
  Pessoa falando ao lado            -> legendado

  Tudo em tempo real. Tudo local. Sem nuvem. Sem Google.
  Whisper roda no processador. Legendas aparecem na tela.
""")

    # --- Fontes de audio ---
    print(f"[FONTES DE AUDIO SUPORTADAS ({len(list(FonteAudio))})]")
    for f in FonteAudio:
        print(f"  {f.id:<15} {f.rotulo}")

    # --- Modos ---
    print(f"\n[MODOS DE LEGENDA ({len(list(ModoLegenda))})]")
    for m in ModoLegenda:
        print(f"  {m.id:<15} {m.rotulo}")

    # --- Posicoes ---
    print(f"\n[POSICOES ({len(list(PosicaoLegenda))})]")
    for p in PosicaoLegenda:
        print(f"  {p.id:<15} {p.rotulo}")

    # --- Estilos ---
    print(f"\n[ESTILOS ({len(list(EstiloLegenda))})]")
    for est in EstiloLegenda:
        print(f"  {est.id:<15} {est.rotulo}")

    # --- Simulacao: videochamada ---
    print("\n" + "=" * 70)
    print("[SIMULACAO] Videochamada -- Maria e Joao em reuniao")
    print("=" * 70)
    e.iniciar("Maria", modo=ModoLegenda.COMUNICACAO, surdo=True)
    print(f"  Sessao: {e.sessao.id}")
    print(f"  Modo: {e.sessao.modo.rotulo}")
    print(f"  Posicao: {e.sessao.posicao.rotulo}")
    print(f"  Estilo: {e.sessao.estilo.rotulo}")

    for i in range(40):
        fonte = FonteAudio.VIDEOCHAMADA
        linha = e.processar_chunk(fonte)
        if linha:
            e.tela_atual.append(linha)
            print(f"\n{e.renderizar_cc_box()}")

    # --- Simulacao: Iara ---
    print("\n" + "=" * 70)
    print("[SIMULACAO] Iara executando comandos")
    print("=" * 70)
    e2 = UniversalCaptionEngine()
    e2.iniciar("Joao", modo=ModoLegenda.SISTEMA, surdo=True)
    for i in range(20):
        linha = e2.processar_chunk(FonteAudio.IARA)
        if linha:
            e2.tela_atual.append(linha)
            print(f"\n{e2.renderizar_cc_box()}")

    # --- Simulacao: YouTube ---
    print("\n" + "=" * 70)
    print("[SIMULACAO] YouTube -- video educativo")
    print("=" * 70)
    e3 = UniversalCaptionEngine()
    e3.iniciar("Pedro", modo=ModoLegenda.COMUNICACAO, surdo=True)
    print("  (musica de introducao deve ser IGNORADA)")
    for i in range(30):
        linha = e3.processar_chunk(FonteAudio.NAVEGADOR)
        if linha:
            e3.tela_atual.append(linha)
            print(f"\n{e3.renderizar_cc_box()}")

    # --- Surdo-cego ---
    print("\n" + "=" * 70)
    print("[SIMULACAO] Surdo-cego -- posicao CENTRO, fonte GRANDE")
    print("=" * 70)
    e4 = UniversalCaptionEngine()
    e4.iniciar("Ana", surdo_cego=True)
    print(f"  Posicao: {e4.sessao.posicao.rotulo}")
    print(f"  Estilo: {e4.sessao.estilo.rotulo}")
    for i in range(15):
        linha = e4.processar_chunk(FonteAudio.VIDEOCHAMADA)
        if linha:
            e4.tela_atual.append(linha)
            print(f"\n{e4.renderizar_cc_box()}")

    # --- Exportar transcricao ---
    print("\n[EXPORTAR TRANSCRICAO COMPLETA]")
    print("-" * 50)
    transcricao = e.exportar_transcricao()
    print(transcricao[:1000])
    if len(transcricao) > 1000:
        print(f"\n  ... ({len(transcricao) - 1000} caracteres a mais)")

    # --- Pipeline tecnico ---
    print("\n[PIPELINE TECNICO]")
    print("""
  1. CAPTURA DE AUDIO DO SISTEMA:
     PulseAudio/PipeWire monitor source (loopback).
     Sem isso, nao tem audio para transcrever.
     - PulseAudio: module-loopback
     - PipeWire: pipewire-pulse
     - Wayland: xdg-desktop-portal (captura de tela + audio)
     - WASM (browser): Web Audio API

  2. CHUNKING:
     Audio dividido em chunks de 500ms.
     Buffer circular: sempre processa o ultimo segundo.
     Chunk menor = menor latencia, mais ruido.
     Chunk maior = mais preciso, mais latencia.

  3. WHISPER (STT local):
     faster-whisper ou whisper.cpp com modelo 'base' ou 'small'.
     - base: 74M params, ~1x realtime em CPU, bom para uso diario
     - small: 244M params, ~0.5x realtime em CPU, mais preciso
     VAD (Voice Activity Detection): pula silencio automaticamente.
     filtrar_musica=True: ignora audio nao-fala (economiza CPU).

  4. FORMATACAO CC:
     Texto formatado como Closed Caption standard:
     - Max 42 caracteres por linha
     - Max 2 linhas simultaneas
     - Timestamp [HH:MM:SS]
     - Falante: "Maria: ..."
     - Cor por falante (se diarizacao)

  5. OVERLAY NA TELA:
     - X11: overlay transparente via xrender
     - Wayland: layer-shell protocol (wlr-layer-shell)
     - GNOME: extension que desenha na tela
     - Browser: DIV flutuante (position: fixed)
     Posicao, tamanho e estilo configuraveis.

  6. HISTORICO E EXPORT:
     Ultimas 50 linhas guardadas no buffer.
     Transcricao completa exportavel em .txt ou .srt.
     Para relatorios de reuniao, atas, auditoria.
""")

    # --- Adaptacao por deficiencia ---
    print("[ADAPTACAO POR DEFICIENCIA]")
    print("""
  SURDO:
    Legenda principal. Fonte padrao (20pt).
    Posicao baixo centro (nao atrapalha video).
    Mostra falante e timestamp.

  SURDO-CEGO:
    Fonte GRANDE (28pt+). Posicao CENTRO.
    Alto contraste maximo (preto/amarelo).
    Integracao com display Braille (saida alternativa).
    Linha unica (nao 2 linhas -- confuso para baixa visao+tatil).

  BAIXA VISAO + SURDO (Helen Keller profile):
    Mesmo que surdo-cego. Fonte grande, contraste maximo.
    Reduz velocidade de leitura (legenda fica mais tempo).

  TDAH:
    Legenda minimalista (sem fundo, texto com sombra).
    Sem timestamp (pode distrair).
    Sem cores (apenas branco).
    Reduz sobrecarga visual.

  IDOSO:
    Fonte grande (24pt+).
    Velocidade de leitura LENTA (1.5x mais tempo na tela).
    Alto contraste.
    Falante sempre mostrado (ajuda a seguir conversa).
""")

    # --- Scorecard ---
    print("[SCORECARD]")
    sc = e.scorecard()
    for k, v in sc.items():
        if isinstance(v, dict):
            print(f"  {k}:")
            for dk, dv in v.items():
                print(f"    {dk:<25} {dv}")
        else:
            print(f"  {k:.<28} {v}")

    # --- Filosofia ---
    print("\n" + "=" * 70)
    print("FILOSOFIA -- Legenda e direito, nao favor")
    print("=" * 70)
    print("""
O PROBLEMA:

  Videochamada sem legenda = EXCLUSAO.
  O surdo nao participa da reuniao.
  Video institucional sem legenda = DESCASO.
  O surdo nao consome o conteudo.
  Podcast sem legenda = INACESSIBILIDADE.
  O surdo nao acessa a informacao.

  Hoje, legenda depende da boa vontade de cada plataforma:
  - Google Meet tem legenda automatica (mas so em chamada).
  - YouTube tem legenda automatica (mas nem sempre ligada).
  - Jitsi tem legenda (mas precisa ativar manualmente).
  - Zoom cobra extra por legenda.
  - Podcast: quase nenhum tem legenda.
  - Notificacao do sistema: nenhum tem legenda.

  A Republica NAO pede legenda. A Republica LEGENDA.
  Automaticamente. Para tudo. Em tempo real.

COMO FUNCIONA NA PRATICA:

  O surdo liga o RepublicaOS. Abre o YouTube.
  A legenda aparece automaticamente. Sem ativar nada.
  Abre o Jitsi. Legenda automatica.
  A Iara fala. Legenda automatica.
  Notificacao chega. Legenda automatica.

  O surdo NAO PRECISA PEDIR.
  O sistema JA SABE que o usuario e surdo (perfil).
  E legenda. Sempre. Tudo.

POR QUE LOCAL (Whisper):

  Google Meet usa servidores do Google para legenda.
  Isso significa: audio da sua reuniao vai para o Google.
  A Republica NAO ENVIA audio para ninguem.
  Whisper roda no processador. Audio fica no dispositivo.
  Legenda local = privacidade local.

  Latencia: Whisper 'base' em CPU ~500ms-1s.
  Para conversa em tempo real, aceitavel.
  Para video, perfeito (legenda sincroniza com video).

A METAFORA DO INTÉRPRETE:

  Um interprete de Libras traduz em tempo real.
  Cada palavra falada vira sinal.
  O surdo acompanha pela Libras.

  O OpenUniversalCaption e o INTERPRETE DIGITAL.
  Cada palavra falada vira TEXTO na tela.
  O surdo acompanha pela leitura.

  Diferente do interprete humano:
  - Esta disponivel 24/7.
  - Nao se cansa.
  - Nao precisa ser agendado.
  - Custo zero (depois de instalado).
  - Transcreve QUALQUER audio, nao so conversa.

A INTEGRACAO COM A IARA:

  Quando a Iara fala ("Abrindo Firefox."),
  a legenda mostra "[14:32] Iara: Abrindo Firefox."
  O surdo VE o que a Iara disse.
  Quando o OpenAmbientSoundAI detecta "campainha",
  a legenda mostra "[14:33] Sistema: CAMPAINHA"
  O surdo-cego com display Braille LE pelo tatil.

  Tudo conectado. Tudo acessivel. Tudo local.
""")


if __name__ == "__main__":
    _demo()
