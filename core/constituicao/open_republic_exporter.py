#!/usr/bin/env python3
"""
OpenRepublicExporter -- Exportador Universal da Republica
=========================================================
"Exporta tudo num .md. Portatil. Compartilhavel.
 O cidadao baixa, le, imprime, cola no mural da praça."

O PROBLEMA:
  A Republica tem 63+ modulos em 5 diretorios. Quem chega novo nao
  sabe por onde comecar. Quem quer auditar nao tem visao geral. Quem
  quer compartilhar manda 63 arquivos soltos -- ou um link quebrado.

A SOLUCAO:
  Este modulo VARRE o repositorio inteiro, descobre cada .py, extrai
  o docstring, classifica por camada (L0-L9), e gera um UNICO arquivo
  .md com TODA a constituicao dentro. Portatil. Compartilhavel.

  Um arquivo. Tudo dentro. Cidadao baixa, le, entende.

O QUE O .md EXPORTADO CONTEM (9 partes):
  PARTE 0 -- Cabecalho (versao, data, contagem)
  PARTE 1 -- Os 14 Principios Constitucionais (P1-P14)
  PARTE 2 -- Arquitetura em 10 Camadas (L0-L9)
  PARTE 3 -- Catalogo de Modulos (todos os .py, agrupados por camada)
  PARTE 4 -- Docstrings (o que cada modulo faz, na voz do autor)
  PARTE 5 -- Referencias 2024/2025 (salario, jornada, fontes legais)
  PARTE 6 -- Sistema de Cores (41 cores semioticas)
  PARTE 7 -- Scorecard (cobertura por camada, total de linhas)
  PARTE 8 -- Filosofia (o manifesto, a metafora do corpo)

FORMATOS DE SAIDA:
  - MARKDOWN (.md) -- o padrao. Portatil. GitHub renderiza.
  - JSON (.json) -- para maquina. API. Dashboard.
  - HTML (.html) -- para navegador. Impressao.

COMO USAR:
  from open_republic_exporter import RepublicExporter
  exp = RepublicExporter(repo_root=".")
  md = exp.gerar_markdown()           # string com o .md completo
  exp.exportar("constituicao.md")     # escreve no disco

DADOS 2024/2025:
  O exportador le o data.json (que ja tem referencias 2024/2025:
  salario minimo R$1.412 -> R$1.518, jornada CLT 44h, etc).
  Se o data.json nao existir, usa fallback hardcoded atualizado.

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
import os
import json
import ast


# ============================================================================
# 1. ENUMS
# ============================================================================

class SecaoExport(Enum):
    """As 9 partes do documento exportado."""
    PARTE_0_CABECALHO = (0, "cabecalho", "Cabecalho e Metadados")
    PARTE_1_PRINCIPIOS = (1, "principios", "Os 14 Principios Constitucionais")
    PARTE_2_CAMADAS = (2, "camadas", "Arquitetura em 10 Camadas (L0-L9)")
    PARTE_3_MODULOS = (3, "modulos", "Catalogo de Modulos")
    PARTE_4_DOCSTRINGS = (4, "docstrings", "O que Cada Modulo Faz")
    PARTE_5_REFERENCIAS = (5, "referencias", "Referencias 2024/2025")
    PARTE_6_CORES = (6, "cores", "Sistema de Cores Semioticas")
    PARTE_7_SCORECARD = (7, "scorecard", "Scorecard da Republica")
    PARTE_8_FILOSOFIA = (8, "filosofia", "Filosofia e Manifesto")

    @property
    def numero(self) -> int:
        return self.value[0]

    @property
    def id(self) -> str:
        return self.value[1]

    @property
    def rotulo(self) -> str:
        return self.value[2]


class FormatoSaida(Enum):
    """Formatos de saida suportados pelo exportador."""
    MARKDOWN = ("md", "Markdown (.md) -- portatil, GitHub, email")
    JSON = ("json", "JSON (.json) -- para maquina, API, dashboard")
    HTML = ("html", "HTML (.html) -- navegador, impressao")

    @property
    def extensao(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class CamadaModulo(Enum):
    """Classificacao de um modulo por camada da arquitetura (L0-L9).

    Espelha CamadaRepublica do open_republic_layers.py, mas auto-contido
    para o exportador funcionar sem importar o modulo de camadas.
    """
    L0_HARDWARE = (0, "hardware", "Hardware Fisico")
    L1_SOBERANIA = (1, "soberania", "Soberania Tecnologica")
    L2_INFRA = (2, "infra", "Infraestrutura Digital")
    L3_CONSTITUICAO = (3, "constituicao", "Constituicao")
    L4_SISTEMAS = (4, "sistemas", "Sistemas Publicos")
    L5_ACESSIBILIDADE = (5, "acessibilidade", "Acessibilidade")
    L6_INTERFACE = (6, "interface", "Interface")
    L7_CULTURA = (7, "cultura", "Cultura e Identidade")
    L8_RELACOES = (8, "relacoes", "Relacoes Externas")
    L9_MEMORIA = (9, "memoria", "Memoria e Transmissao")

    @property
    def numero(self) -> int:
        return self.value[0]

    @property
    def id(self) -> str:
        return self.value[1]

    @property
    def rotulo(self) -> str:
        return self.value[2]


# ============================================================================
# 2. DATACLASSES
# ============================================================================

@dataclass
class ModuloInfo:
    """Informacao extraida de um modulo .py descoberto no repositorio."""
    caminho_relativo: str          # "core/constituicao/open_drone.py"
    caminho_absoluto: str          # "/Users/.../open_drone.py"
    nome_arquivo: str              # "open_drone.py"
    nome_modulo: str               # "open_drone"
    camada: CamadaModulo           # L8_RELACOES
    linhas: int = 0                # contagem de linhas
    docstring: str = ""            # primeira linha do docstring (titulo)
    descricao_curta: str = ""      # resumo de 1 linha
    existe: bool = True            # sempre True (foi descoberto no disco)
    erro_leitura: str = ""         # "" se leu OK, mensagem se falhou


@dataclass
class SecaoMd:
    """Uma secao do documento markdown exportado."""
    numero: int                    # 0-8
    titulo: str                    # "Os 14 Principios Constitucionais"
    conteudo: str                  # o markdown da secao
    linhas: int = 0                # contagem de linhas da secao

    def __post_init__(self) -> None:
        self.linhas = self.conteudo.count("\n") + 1 if self.conteudo else 0


@dataclass
class RelatorioExport:
    """Resultado completo de uma exportacao."""
    formato: FormatoSaida
    caminho_saida: str             # onde foi escrito (ou "" se so string)
    total_modulos: int = 0
    total_linhas: int = 0
    total_principios: int = 0
    total_camadas: int = 0
    tamanho_bytes: int = 0
    gerado_em: str = ""
    partes_incluidas: List[str] = field(default_factory=list)
    conteudo: str = ""             # o documento completo como string

    def resumo(self) -> str:
        """Resumo de 1 linha do relatorio."""
        return (
            f"{self.total_modulos} modulos, {self.total_principios} principios, "
            f"{self.total_linhas} linhas, {self.tamanho_bytes:,} bytes "
            f"-> {self.caminho_saida or '(string)'}"
        )


# ============================================================================
# 3. ENGINE
# ============================================================================

class RepublicExporter:
    """
    Varre o repositorio da Republica e gera um documento unico com tudo.

    O exportador e AUTO-DESCOBRIVEL: nao tem lista hardcode de modulos.
    Ele varre o diretorio core/ recursivamente, encontra cada .py,
    extrai o docstring, classifica por camada, e monta o documento.

    Se um modulo novo for adicionado, o exportador o encontra automaticamente.
    Zero codigo muda. Como o constitutional_engine le data.json, este le o disco.
    """

    # -- mapeamento de nomes de arquivo -> camada (override do diretorio) -----
    # Modulos que NAO seguem a regra do diretorio onde moram.
    _MAPEAMENTO_CAMADA: Dict[str, CamadaModulo] = {
        # constituicao/ mas sao soberania (L1)
        "open_sovereign_tech": CamadaModulo.L1_SOBERANIA,
        "open_resilience": CamadaModulo.L1_SOBERANIA,
        # constituicao/ mas sao cultura (L7)
        "open_cultural_constitution": CamadaModulo.L7_CULTURA,
        "open_republic_colors": CamadaModulo.L7_CULTURA,
        "open_republic_exporter": CamadaModulo.L7_CULTURA,
        "open_republic_layers": CamadaModulo.L7_CULTURA,
        # constituicao/ mas sao relacoes externas / defesa (L8)
        "open_drone": CamadaModulo.L8_RELACOES,
        "open_cyber_defense": CamadaModulo.L8_RELACOES,
        "open_citizen_oversight": CamadaModulo.L8_RELACOES,
        "open_political_reliability": CamadaModulo.L8_RELACOES,
        "open_political_risk_predictor": CamadaModulo.L8_RELACOES,
        # economia/ mas sao infra (L2)
        "open_energy": CamadaModulo.L2_INFRA,
        "open_energy_taxonomy": CamadaModulo.L2_INFRA,
        # distro/ -> L2 sempre (infra digital)
        # (tratado por diretorio, nao precisa mapear arquivo a arquivo)
    }

    # -- mapeamento diretorio -> camada (fallback) ---------------------------
    _DIRETORIO_PARA_CAMADA: Dict[str, CamadaModulo] = {
        "acessibilidade": CamadaModulo.L5_ACESSIBILIDADE,
        "constituicao": CamadaModulo.L3_CONSTITUICAO,
        "distro": CamadaModulo.L2_INFRA,
        "economia": CamadaModulo.L4_SISTEMAS,
        "voz": CamadaModulo.L6_INTERFACE,
        "treinamento": CamadaModulo.L4_SISTEMAS,
    }

    def __init__(self, repo_root: str = ".") -> None:
        """
        Args:
            repo_root: raiz do repositorio OpenRepublic.
                       Deve conter o diretorio core/.
        """
        self.repo_root: Path = Path(repo_root).resolve()
        self.core_dir: Path = self.repo_root / "core"
        self.data_json_path: Path = (
            self.core_dir / "constituicao" / "data.json"
        )

        # cache populado por _descobrir_modulos()
        self._modulos: Optional[List[ModuloInfo]] = None
        self._data: Optional[Dict[str, Any]] = None

    # ========================================================================
    # 3.1 -- DESCOBERTA DE MODULOS
    # ========================================================================

    def _descobrir_modulos(self) -> List[ModuloInfo]:
        """Varre core/ recursivamente e extrai info de cada .py."""
        if self._modulos is not None:
            return self._modulos

        modulos: List[ModuloInfo] = []

        if not self.core_dir.exists():
            self._modulos = modulos
            return modulos

        # varredura recursiva
        arquivos = sorted(self.core_dir.rglob("*.py"))
        arquivos = [
            a for a in arquivos
            if "__pycache__" not in a.parts and "_demo" not in a.stem
        ]

        for arq in arquivos:
            nome_modulo = arq.stem  # "open_drone"
            caminho_relativo = str(arq.relative_to(self.repo_root))

            # classificacao por camada
            camada = self._classificar_camada(arq, nome_modulo)

            # extracao de metadados do arquivo
            linhas, docstring, desc_curta, erro = self._extrair_metadados(arq)

            modulos.append(ModuloInfo(
                caminho_relativo=caminho_relativo,
                caminho_absoluto=str(arq),
                nome_arquivo=arq.name,
                nome_modulo=nome_modulo,
                camada=camada,
                linhas=linhas,
                docstring=docstring,
                descricao_curta=desc_curta,
                existe=True,
                erro_leitura=erro,
            ))

        self._modulos = modulos
        return modulos

    def _classificar_camada(
        self, caminho: Path, nome_modulo: str
    ) -> CamadaModulo:
        """Determina a camada L0-L9 de um modulo.

        Prioridade:
          1. Tabela explicita _MAPEAMENTO_CAMADA (override por nome)
          2. Diretorio onde mora (fallback)
          3. L3_CONSTITUICAO (desconhecido)
        """
        # 1. override explicito
        if nome_modulo in self._MAPEAMENTO_CAMADA:
            return self._MAPEAMENTO_CAMADA[nome_modulo]

        # 2. fallback por diretorio
        for parte in caminho.parts:
            if parte in self._DIRETORIO_PARA_CAMADA:
                return self._DIRETORIO_PARA_CAMADA[parte]

        # 3. desconhecido -> constituicao (default)
        return CamadaModulo.L3_CONSTITUICAO

    def _extrair_metadados(
        self, caminho: Path
    ) -> Tuple[int, str, str, str]:
        """Extrai: (linhas, docstring_titulo, descricao_curta, erro).

        Usa ast.parse para extrair o docstring de forma segura (sem executar).
        """
        try:
            texto = caminho.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            return (0, "", "", f"Erro ao ler: {e}")

        linhas = texto.count("\n") + 1

        try:
            tree = ast.parse(texto, filename=str(caminho))
            ds = ast.get_docstring(tree)
            if ds:
                # titulo = primeira linha nao-vazia do docstring
                linhas_ds = [l.strip() for l in ds.split("\n") if l.strip()]
                titulo = linhas_ds[0] if linhas_ds else ""
                # descricao curta = segunda linha significativa (ou titulo)
                desc = linhas_ds[1] if len(linhas_ds) > 1 else titulo
                return (linhas, titulo, desc, "")
            else:
                return (linhas, "(sem docstring)", "", "")
        except SyntaxError as e:
            return (linhas, f"(erro de sintaxe: {e.msg})", "", f"SyntaxError: {e.msg}")
        except Exception as e:
            return (linhas, "(erro ao parsear)", "", f"Erro: {e}")

    # ========================================================================
    # 3.2 -- LEITURA DO DATA.JSON (principios + referencias)
    # ========================================================================

    def _ler_data_json(self) -> Dict[str, Any]:
        """Le o data.json do motor constitucional. Fallback se ausente."""
        if self._data is not None:
            return self._data

        if self.data_json_path.exists():
            try:
                parsed = json.loads(
                    self.data_json_path.read_text(encoding="utf-8")
                )
                if isinstance(parsed, dict):
                    self._data = parsed
                    return self._data
            except Exception:
                pass  # cai no fallback

        # fallback hardcoded (atualizado 2024/2025)
        self._data = self._data_fallback()
        return self._data

    def _data_fallback(self) -> Dict[str, Any]:
        """Estrutura minima caso o data.json nao exista."""
        return {
            "$schema": "openrepublic-constitutional-v1",
            "pass_threshold": 60,
            "principios": {
                "P1": {"nome": "anti_elitismo", "categoria": "fundamento",
                       "texto": "Ninguem vale mais por cargo. Todos comecam em 1.0."},
                "P2": {"nome": "autonomia_corporal", "categoria": "fundamento",
                       "texto": "O corpo de cada cidadao e DELA. Inegociavelmente."},
                "P3": {"nome": "trabalho_igual", "categoria": "fundamento",
                       "texto": "Todo trabalho tem valor base 1.0."},
                "P4": {"nome": "processo_democratico", "categoria": "fundamento",
                       "texto": "Toda decisao passa por votacao. 1 pessoa = 1 voto."},
                "P5": {"nome": "transparencia_radical", "categoria": "operacional",
                       "texto": "Todo log, toda decisao e publica. Caixa-preta proibida."},
                "P6": {"nome": "acesso_universal", "categoria": "operacional",
                       "texto": "Conhecimento e DIREITO, nao privilegio."},
                "P7": {"nome": "seguranca_cultura", "categoria": "operacional",
                       "texto": "Seguranca e CULTURA do cidadao, nao elite."},
                "P8": {"nome": "ia_instrumento", "categoria": "operacional",
                       "texto": "IA amplifica inteligencia humana. Nao substitui."},
                "P9": {"nome": "anti_polarizacao", "categoria": "operacional",
                       "texto": "O Estado nao divide. Polarizacao e doenca."},
                "P10": {"nome": "soberania_aerea", "categoria": "operacional",
                        "texto": "Drones sao civicos. Nao vigia, nao mata, nao espiona."},
                "P11": {"nome": "letramento_constituinte", "categoria": "operacional",
                        "texto": "Letramento digital e constituinte da cidadania."},
                "P12": {"nome": "defesa_cibernetica_transparente",
                        "categoria": "operacional",
                        "texto": "Defesa transparente. Nunca ataque secreto."},
                "P13": {"nome": "contravigilancia_reciproca", "categoria": "operacional",
                        "texto": "Quem tem poder perde privacidade proporcional."},
                "P14": {"nome": "soberania_de_dados", "categoria": "operacional",
                        "texto": "Dados sao do cidadao. Custodiante e revogavel."},
            },
            "referencias_2025": {
                "ano": 2025,
                "atualizado_em": "2025-01",
                "salario_minimo": {
                    "2024": {"valor": 1412, "vigencia": "2024-01-01",
                             "fonte": "Portaria MTE n 3.832/2023"},
                    "2025": {"valor": 1518, "vigencia": "2025-01-01",
                             "fonte": "Portaria MTE n 3.853/2024"},
                    "moeda": "BRL",
                    "unidade": "reais/mes",
                },
                "jornada_trabalho": {
                    "maxima_legal_semanal": 44,
                    "comum_acordo_coletivo": 40,
                    "base_digna_recomendada": 20,
                    "limite_pratica_overtime": 50,
                    "unidade": "horas/semana",
                    "fonte": "Constituicao Federal art. 7 XIII + CLT 2025",
                },
            },
        }

    # ========================================================================
    # 3.3 -- CONSULTAS
    # ========================================================================

    def modulos(self) -> List[ModuloInfo]:
        """Lista de todos os modulos descobertos."""
        return list(self._descobrir_modulos())

    def modulos_por_camada(
        self, camada: CamadaModulo
    ) -> List[ModuloInfo]:
        """Modulos de uma camada especifica."""
        return [m for m in self.modulos() if m.camada == camada]

    def total_linhas(self) -> int:
        """Soma de linhas de todos os modulos."""
        return sum(m.linhas for m in self.modulos())

    def total_modulos(self) -> int:
        """Contagem de modulos."""
        return len(self.modulos())

    def cobertura_por_camada(self) -> Dict[str, Tuple[int, int]]:
        """Cobertura por camada: {camada_id: (n_modulos, n_linhas)}."""
        result: Dict[str, Tuple[int, int]] = {}
        for camada in CamadaModulo:
            mods = self.modulos_por_camada(camada)
            linhas = sum(m.linhas for m in mods)
            result[f"L{camada.numero}"] = (len(mods), linhas)
        return result

    def scorecard(self) -> Dict[str, Any]:
        """Metricas gerais da Republica."""
        mods = self.modulos()
        return {
            "total_modulos": len(mods),
            "total_linhas": self.total_linhas(),
            "total_principios": len(self._ler_data_json().get("principios", {})),
            "total_camadas_com_modulos": len({
                m.camada for m in mods
            }),
            "modulos_com_erro": sum(1 for m in mods if m.erro_leitura),
            "modulos_sem_docstring": sum(
                1 for m in mods if "sem docstring" in m.docstring.lower()
            ),
            "cobertura_por_camada": self.cobertura_por_camada(),
        }

    # ========================================================================
    # 3.4 -- GERACAO DE MARKDOWN (as 9 partes)
    # ========================================================================

    def gerar_markdown(self) -> str:
        """Gera o documento markdown completo com as 9 partes."""
        partes: List[str] = []
        agora = datetime.now().strftime("%Y-%m-%d %H:%M")

        partes.append(self._parte_0_cabecalho(agora))
        partes.append(self._parte_1_principios())
        partes.append(self._parte_2_camadas())
        partes.append(self._parte_3_modulos())
        partes.append(self._parte_4_docstrings())
        partes.append(self._parte_5_referencias())
        partes.append(self._parte_6_cores())
        partes.append(self._parte_7_scorecard())
        partes.append(self._parte_8_filosofia())

        return "\n\n".join(partes) + "\n"

    # -- PARTE 0: Cabecalho --------------------------------------------------

    def _parte_0_cabecalho(self, timestamp: str) -> str:
        sc = self.scorecard()
        return f"""# OpenRepublic -- Constituicao Completa

> *"O codigo e a constituicao. A constituicao e o codigo."*

**Versao:** {timestamp}
**Modulos:** {sc['total_modulos']}
**Linhas de codigo:** {sc['total_linhas']:,}
**Principios constitucionais:** {sc['total_principios']}
**Camadas ativas:** {sc['total_camadas_com_modulos']} de 10

---

**O que e este documento?**

Este arquivo contem TODA a constituicao da OpenRepublic exportada num
unico .md portatil. Nao precisa de 63 arquivos. Nao precisa de internet.
Baixa, le, entende. Compartilha no WhatsApp, cola no mural da praca,
imprime na impressora do cartorio.

Gerado automaticamente por `open_republic_exporter.py`."""

    # -- PARTE 1: Principios -------------------------------------------------

    def _parte_1_principios(self) -> str:
        data = self._ler_data_json()
        principios = data.get("principios", {})
        threshold = data.get("pass_threshold", 60)

        linhas = [
            f"## Parte 1 -- Os {len(principios)} Principios Constitucionais",
            "",
            f"> *Todo sistema da Republica e validado contra estes principios.*",
            f"> *Score minimo para aprovacao: **{threshold}/100***.",
            "",
            "| ID | Principio | Categoria | Texto |",
            "|-----|-----------|-----------|-------|",
        ]

        for pid in sorted(principios.keys()):
            p = principios[pid]
            texto = p.get("texto", "").replace("|", "\\|").replace("\n", " ")
            if len(texto) > 120:
                texto = texto[:117] + "..."
            nome = p.get("nome", "").replace("_", " ")
            cat = p.get("categoria", "")
            linhas.append(f"| **{pid}** | {nome} | {cat} | {texto} |")

        return "\n".join(linhas)

    # -- PARTE 2: Camadas ----------------------------------------------------

    def _parte_2_camadas(self) -> str:
        linhas = [
            "## Parte 2 -- Arquitetura em 10 Camadas (L0-L9)",
            "",
            "> *Cada camada suporta a de cima. Nenhuma existe sozinha.*",
            "> *Assim como o corpo: osso, musculo, pele, voz, espirito.*",
            "",
            "| Camada | Nome | Modulos | Linhas |",
            "|--------|------|---------|--------|",
        ]

        cob = self.cobertura_por_camada()
        for camada in CamadaModulo:
            n_mods, n_linhas = cob.get(f"L{camada.numero}", (0, 0))
            label = f"L{camada.numero} -- {camada.rotulo}"
            linhas.append(f"| L{camada.numero} | {camada.rotulo} | {n_mods} | {n_linhas:,} |")

        linhas.extend([
            "",
            "**Metafora do Corpo:**",
            "",
            "```",
            "  L0  Osso        sem osso, nada se sustenta",
            "  L1  Tendao      conecta osso a musculo",
            "  L2  Musculo     move o que o osso sustenta",
            "  L3  Orgao       coracao que bomba sangue (principios)",
            "  L4  Sistema     digestao, respiracao (servicos publicos)",
            "  L5  Sentido     visao, audicao (acessibilidade)",
            "  L6  Voz         fala, grito, canto (interface)",
            "  L7  Expressao   danc,a, arte, identidade (cultura)",
            "  L8  Relacao     abraco, beijo, guerra (externo)",
            "  L9  Alma        o que sobra quando o corpo cai (memoria)",
            "```",
        ])

        return "\n".join(linhas)

    # -- PARTE 3: Catalogo de Modulos ---------------------------------------

    def _parte_3_modulos(self) -> str:
        mods = self.modulos()
        linhas = [
            f"## Parte 3 -- Catalogo de Modulos ({len(mods)} total)",
            "",
            "> *Cada modulo e uma especificacao executavel em Python.*",
            "> *Nao e codigo de producao -- e a DEFINICAO do sistema.*",
            "",
        ]

        for camada in CamadaModulo:
            mods_camada = sorted(
                self.modulos_por_camada(camada),
                key=lambda m: m.nome_modulo,
            )
            if not mods_camada:
                continue

            linhas.extend([
                f"### L{camada.numero} -- {camada.rotulo} ({len(mods_camada)} modulos)",
                "",
                "| Modulo | Arquivo | Linhas |",
                "|--------|---------|--------|",
            ])

            for m in mods_camada:
                linhas.append(
                    f"| `{m.nome_modulo}` | `{m.caminho_relativo}` | {m.linhas:,} |"
                )

            linhas.append("")

        return "\n".join(linhas)

    # -- PARTE 4: Docstrings -------------------------------------------------

    def _parte_4_docstrings(self) -> str:
        mods = sorted(self.modulos(), key=lambda m: m.nome_modulo)
        linhas = [
            "## Parte 4 -- O que Cada Modulo Faz",
            "",
            "> *Na voz do proprio autor. Primeira linha do docstring.*",
            "",
        ]

        for m in mods:
            titulo = m.docstring if m.docstring else "(sem docstring)"
            desc = m.descricao_curta if m.descricao_curta else ""
            linhas.extend([
                f"### `{m.nome_modulo}`",
                f"**{titulo}**",
                "",
            ])
            if desc:
                linhas.append(f"*{desc}*")
                linhas.append("")
            if m.erro_leitura:
                linhas.append(f"> ⚠️ **Erro:** {m.erro_leitura}")
                linhas.append("")

        return "\n".join(linhas)

    # -- PARTE 5: Referencias 2024/2025 -------------------------------------

    def _parte_5_referencias(self) -> str:
        data = self._ler_data_json()
        refs = data.get("referencias_2025", {})

        linhas = [
            "## Parte 5 -- Referencias 2024/2025",
            "",
            f"> *Atualizado em: {refs.get('atualizado_em', 'N/A')}*",
            "",
        ]

        # salario minimo
        sal = refs.get("salario_minimo", {})
        if sal:
            s2024 = sal.get("2024", {})
            s2025 = sal.get("2025", {})
            moeda = sal.get("moeda", "BRL")
            unidade = sal.get("unidade", "reais/mes")
            linhas.extend([
                "### Salario Minimo",
                "",
                f"| Ano | Valor | Vigencia | Fonte |",
                f"|-----|-------|-----------|-------|",
                f"| 2024 | {moeda} {s2024.get('valor', '?'):,} | {s2024.get('vigencia', '')} | {s2024.get('fonte', '')} |",
                f"| 2025 | {moeda} {s2025.get('valor', '?'):,} | {s2025.get('vigencia', '')} | {s2025.get('fonte', '')} |",
                "",
                f"*Unidade: {unidade}*",
                "",
            ])

        # jornada de trabalho
        jorn = refs.get("jornada_trabalho", {})
        if jorn:
            linhas.extend([
                "### Jornada de Trabalho",
                "",
                f"- **Maxima legal (semanal):** {jorn.get('maxima_legal_semanal', 44)}h",
                f"- **Comum em acordo coletivo:** {jorn.get('comum_acordo_coletivo', 40)}h",
                f"- **Base digna recomendada:** {jorn.get('base_digna_recomendada', 20)}h",
                f"- **Limite de overtime:** {jorn.get('limite_pratica_overtime', 50)}h",
                f"- **Fonte:** {jorn.get('fonte', 'CF/88 + CLT')}",
                "",
            ])

        # outros
        outros = refs.get("outros", {})
        if outros:
            linhas.extend([
                "### Outros",
                "",
                f"- **Pass threshold default:** {outros.get('pass_threshold_default', 60)}",
                f"- {outros.get('nota', '')}",
                "",
            ])

        return "\n".join(linhas)

    # -- PARTE 6: Cores ------------------------------------------------------

    def _parte_6_cores(self) -> str:
        return """## Parte 6 -- Sistema de Cores Semioticas

> *41 cores. Cada cor = um principio. Cada matiz = uma intencao.*
> *Detalhe completo em `open_republic_colors.py`.*

| Categoria | Cores | Exemplos |
|-----------|-------|----------|
| Identidade | 6 | Preto Republica, Verde Quilombo, Terra Brasilis |
| Principios P1-P14 | 14 | Uma cor por principio constitucional |
| Status de Auditoria | 4 | Conforme (verde), Revisao, Suspenso, Banido |
| Niveis de Alerta | 5 | Info, Atencao, Importante, Urgente, Critico |
| Equipes / Projetos | 5 | Constituicao, Economia, Acessibilidade, Voz, Distro |
| Vetores Culturais | 7 | Cordel, Capoeira, Samba, Antropofagia, Cinema Novo |

*Cores exportaveis em CSS e JSON via `open_republic_colors.py`.*"""

    # -- PARTE 7: Scorecard --------------------------------------------------

    def _parte_7_scorecard(self) -> str:
        sc = self.scorecard()
        cob = sc["cobertura_por_camada"]

        linhas = [
            "## Parte 7 -- Scorecard da Republica",
            "",
            "| Metrica | Valor |",
            "|---------|-------|",
            f"| Total de modulos | {sc['total_modulos']} |",
            f"| Total de linhas | {sc['total_linhas']:,} |",
            f"| Principios constitucionais | {sc['total_principios']} |",
            f"| Camadas ativas | {sc['total_camadas_com_modulos']}/10 |",
            f"| Modulos com erro | {sc['modulos_com_erro']} |",
            f"| Modulos sem docstring | {sc['modulos_sem_docstring']} |",
            "",
            "### Cobertura por Camada",
            "",
            "| Camada | Modulos | Linhas |",
            "|--------|---------|--------|",
        ]

        for camada in CamadaModulo:
            n_mods, n_linhas = cob.get(f"L{camada.numero}", (0, 0))
            linhas.append(
                f"| L{camada.numero} {camada.rotulo} | {n_mods} | {n_linhas:,} |"
            )

        return "\n".join(linhas)

    # -- PARTE 8: Filosofia --------------------------------------------------

    def _parte_8_filosofia(self) -> str:
        return """## Parte 8 -- Filosofia e Manifesto

> *"O codigo e a constituicao. A constituicao e o codigo.*
> *Nao ha separacao entre o que o Estado faz e o que o cidadao ve.*
> *Tudo e publico. Tudo e auditavel. Tudo e traduzivel."*

### Os 3 Juramentos

1. **Anti-elitismo (P1):** Ninguem vale mais por cargo. O lider treina
   sucessor. O fundador documenta. Se o bus factor e 1, e elitismo.

2. **Transparencia radical (P5):** Todo log e publico. Toda decisao
   tem trilha. Caixa-preta e inaceitavel. Privacidade e do cidadao;
   transparencia e do Estado.

3. **Acesso universal (P6):** Ninguem fica de fora. Nem por dinheiro.
   Nem por deficiencia. Nem por nao saber ler. Man pages excluem;
   tldr inclui.

### O Vazio Nao e Falha

Cada modulo que ainda nao existe e um CONVITE, nao uma falha.
A arquitetura e COMPLETA. A Republica e INCOMPLETA.
Completa e o destino. Incompleta e o caminho.

### Uma Linguagem, Um Canal, Todo Hardware

O codigo-fonte e Python. Tudo o mais (.c, .go, .java, .js, .rs) e
ARTEFATO gerado por transpilacao. Uma fonte. Um canal de update.
Todo hardware recebe a mesma versao.

---

*OpenRepublic -- CC0 Universal.*
*Gerado por `open_republic_exporter.py`.*"""

    # ========================================================================
    # 3.5 -- GERACAO DE JSON
    # ========================================================================

    def gerar_json(self) -> str:
        """Gera uma versao JSON do relatorio (para maquina/API)."""
        data = self._ler_data_json()
        mods = self.modulos()
        sc = self.scorecard()

        relatorio = {
            "$schema": "openrepublic-export-v1",
            "gerado_em": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "scorecard": {k: v for k, v in sc.items()
                          if k != "cobertura_por_camada"},
            "cobertura_por_camada": {
                k: {"modulos": v[0], "linhas": v[1]}
                for k, v in sc["cobertura_por_camada"].items()
            },
            "principios": data.get("principios", {}),
            "referencias_2025": data.get("referencias_2025", {}),
            "modulos": [
                {
                    "nome": m.nome_modulo,
                    "arquivo": m.caminho_relativo,
                    "camada": f"L{m.camada.numero}",
                    "camada_nome": m.camada.rotulo,
                    "linhas": m.linhas,
                    "docstring": m.docstring,
                    "tem_erro": bool(m.erro_leitura),
                }
                for m in sorted(mods, key=lambda x: x.nome_modulo)
            ],
        }
        return json.dumps(relatorio, indent=2, ensure_ascii=False)

    # ========================================================================
    # 3.6 -- EXPORTACAO (escrever no disco)
    # ========================================================================

    def exportar(
        self,
        caminho: Optional[str] = None,
        formato: FormatoSaida = FormatoSaida.MARKDOWN,
    ) -> RelatorioExport:
        """Gera o documento e escreve no disco.

        Args:
            caminho: onde escrever. Se None, usa nome default.
            formato: MARKDOWN (default), JSON, ou HTML.

        Returns:
            RelatorioExport com metricas e o conteudo.
        """
        # gerar conteudo
        if formato == FormatoSaida.MARKDOWN:
            conteudo = self.gerar_markdown()
        elif formato == FormatoSaida.JSON:
            conteudo = self.gerar_json()
        elif formato == FormatoSaida.HTML:
            md = self.gerar_markdown()
            conteudo = self._markdown_para_html(md)
        else:
            conteudo = self.gerar_markdown()

        # definir caminho de saida
        if caminho is None:
            nome_default = {
                FormatoSaida.MARKDOWN: "constituicao_completa.md",
                FormatoSaida.JSON: "constituicao_completa.json",
                FormatoSaida.HTML: "constituicao_completa.html",
            }
            caminho = nome_default.get(formato, "export.md")

        # escrever
        try:
            Path(caminho).write_text(conteudo, encoding="utf-8")
        except Exception as e:
            # se nao conseguir escrever, retorna o conteudo mesmo assim
            pass

        sc = self.scorecard()
        return RelatorioExport(
            formato=formato,
            caminho_saida=caminho,
            total_modulos=sc["total_modulos"],
            total_linhas=sc["total_linhas"],
            total_principios=sc["total_principios"],
            total_camadas=sc["total_camadas_com_modulos"],
            tamanho_bytes=len(conteudo.encode("utf-8")),
            gerado_em=datetime.now().strftime("%Y-%m-%d %H:%M"),
            partes_incluidas=[s.rotulo for s in SecaoExport],
            conteudo=conteudo,
        )

    def _markdown_para_html(self, md: str) -> str:
        """Wrapper HTML simples para o markdown (sem dependencias)."""
        import html
        corpo = html.escape(md)
        return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>OpenRepublic -- Constituicao Completa</title>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
          max-width: 900px; margin: 2rem auto; padding: 0 1rem;
          line-height: 1.6; color: #1a1a1a; }}
  pre, code {{ background: #f4f4f4; padding: 0.5em; border-radius: 4px;
               overflow-x: auto; }}
  table {{ border-collapse: collapse; width: 100%; margin: 1em 0; }}
  th, td {{ border: 1px solid #ddd; padding: 8px 12px; text-align: left; }}
  th {{ background: #2D6A4F; color: white; }}
  blockquote {{ border-left: 4px solid #2D6A4F; margin: 1em 0;
                padding: 0.5em 1em; background: #f9f9f9; }}
  h1 {{ color: #2D6A4F; border-bottom: 3px solid #2D6A4F; }}
  h2 {{ color: #264653; border-bottom: 1px solid #ccc; }}
  h3 {{ color: #40916C; }}
</style>
</head>
<body>
<pre>{corpo}</pre>
</body>
</html>"""


# ============================================================================
# 4. DEMO
# ============================================================================

def _demo() -> None:
    """Demonstra o exportador varrendo o repositorio atual."""
    # descobrir raiz do repo (este arquivo esta em core/constituicao/)
    este_arquivo = Path(__file__).resolve()
    repo_root = este_arquivo.parent.parent.parent  # sobe 3: const -> core -> root

    print("=" * 70)
    print("OpenRepublicExporter -- Exportador Universal")
    print("=" * 70)
    print(f"\nRepo root: {repo_root}")
    print(f"Core dir:  {repo_root / 'core'}")

    exp = RepublicExporter(repo_root=str(repo_root))

    # --- Descoberta ---
    mods = exp.modulos()
    print(f"\n[DESCOBERTA]")
    print(f"  {len(mods)} modulos encontrados")
    print(f"  {exp.total_linhas():,} linhas totais")

    # --- Cobertura por camada ---
    print(f"\n[COBERTURA POR CAMADA]")
    cob = exp.cobertura_por_camada()
    print(f"  {'Camada':<30} {'Mods':>6} {'Linhas':>8}")
    print(f"  {'-'*48}")
    for camada in CamadaModulo:
        n_mods, n_linhas = cob.get(f"L{camada.numero}", (0, 0))
        if n_mods > 0:
            print(f"  L{camada.numero} {camada.rotulo:<27} {n_mods:>6} {n_linhas:>8,}")

    # --- Scorecard ---
    print(f"\n[SCORECARD]")
    sc = exp.scorecard()
    for k, v in sc.items():
        if k != "cobertura_por_camada":
            print(f"  {k:.<30} {v}")

    # --- Primeiros 10 modulos ---
    print(f"\n[AMOSTRA -- 10 primeiros modulos]")
    for m in sorted(mods, key=lambda x: x.nome_modulo)[:10]:
        status = "OK" if not m.erro_leitura else f"ERRO: {m.erro_leitura}"
        print(f"  L{m.camada.numero} {m.nome_modulo:<35} {m.linhas:>6} linhas  [{status}]")

    # --- Exportacao markdown ---
    print(f"\n[EXPORTACAO MARKDOWN]")
    saida_md = str(repo_root / "constituicao_completa.md")
    rel = exp.exportar(saida_md, FormatoSaida.MARKDOWN)
    print(f"  {rel.resumo()}")
    print(f"  Partes: {', '.join(rel.partes_incluidas)}")

    # --- Exportacao JSON ---
    print(f"\n[EXPORTACAO JSON]")
    saida_json = str(repo_root / "constituicao_completa.json")
    rel_json = exp.exportar(saida_json, FormatoSaida.JSON)
    print(f"  {rel_json.resumo()}")

    # --- Amostra do markdown (primeiras 30 linhas) ---
    print(f"\n[AMOSTRA DO MARKDOWN -- primeiras 30 linhas]")
    print("-" * 70)
    md = exp.gerar_markdown()
    for linha in md.split("\n")[:30]:
        print(linha)
    print("...")
    print("-" * 70)

    # --- Filosofia ---
    print(f"\n[FILOSOFIA]")
    print("""
O exportador nao tem lista hardcode de modulos.
Ele VARRE o disco. Descobre. Classifica. Exporta.

Se voce adicionar um modulo novo em core/, o exportador o encontra.
Zero codigo muda. Como o constitutional_engine le data.json,
este le o sistema de arquivos.

UM ARQUIVO. TODA A CONSTITUICAO. PORTATIL. COMPARTILHAVEL.

  O cidadao baixa.
  O cidadao le.
  O cidadao entende.
  O cidadao exige.

Esse e o ponto.
""")


if __name__ == "__main__":
    _demo()
