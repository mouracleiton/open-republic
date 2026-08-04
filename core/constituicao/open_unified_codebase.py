#!/usr/bin/env python3
"""
OpenUnifiedCodebase -- Uma Linguagem, Um Canal, Todo Hardware
================================================================
"O codigo core vai ser escrito apenas em uma unica linguagem e transpilada.
So o codigo desenvolvido funcionara em todos os hardwares listados.
Teremos apenas um canal de atualizacoes."

FIM DA BABILONIA LINGUISTICA:

Hoje o projeto tem 7 arquivos por modulo (.py .c .go .java .js .rs .md).
Isso e INSSUSTENTAVEL:
- 7 arquivos para manter a cada mudanca
- 7 arquivos para dar commit
- 7 arquivos que podem dessincronizar
- 7 arquivos onde bugs se escondem
- 7 arquivos que NINGUEM le todos

A DECISAO:

1. UMA LINGUAGEM FONTE: Python (.py). PONTO.
   Nenhum .c, .go, .java, .js, .rs e escrito a mao.
   Sao GERADOS por transpilacao automatica.
   Se voce edita .c a mao, voce esta fazendo errado.

2. TRANSPILACAO E O UNICO CAMINHO:
   .py (fonte) -> transpilador -> .c .go .java .js .rs .md (saidas)
   As saidas sao ARTEFATOS, nao codigo-fonte.
   Como um .o (objeto compilado) -- voce nao edita, voce regenera.

3. TODO HARDWARE RODA O MESMO CODIGO:
   O codigo desenvolvido funciona em TODOS os 12 dispositivos COTS
   (OpenAccessibilityHardwareSpecs) + RepublicaPort RISC-V (OpenSovereignTech).
   Se nao roda no hardware, nao e codigo da Republica. E bug.

4. UM CANAL DE ATUALIZACAO:
   Uma fonte. Um canal. Todo hardware recebe a mesma versao.
   Nao existe "versao Android diferente de iOS diferente de RISC-V".
   O transpilador gera para cada arquitetura a partir da MESMA fonte.
   Update no .py = update em TODO o ecossistema automaticamente.

O NOVO FLUXO (substitui o workflow antigo):

  ANTES (errado):
    escrever .py -> escrever .c a mao -> escrever .go a mao -> ...
    7 arquivos para manter. Dessincronia garantida.

  DEPOIS (correto):
    escrever .py -> python3 transpilador.py open_xxx.py --all
    .py e fonte. O resto e artefato. Commit so do .py.
    Artefatos gerados no CI/CD, nao no desenvolvimento.

ALINHAMENTO CONSTITUCIONAL:
- P1: Uma linguagem = sem elite de "quem sabe C mas nao Python".
- P6: Acesso universal = codigo que roda em TODO hardware.
- P9 (Soberania): Um canal = soberania do update. Ninguem fragmenta.

Author: OpenRepublic Team

BASELINE 2024/2025:
- Linguagem fonte: Python 3.13+ (out/2024) com alvo 3.14 (out/2025).
- Transpiladores-alvo (gerados, nunca escritos a mao):
    * C23 (ISO/IEC 9899:2024) via GCC 14 / Clang 19 / RISC-V GCC 14
    * Go 1.23 / 1.24 (toolchain, generics estaveis)
    * Java 21 LTS / 25 LTS (OpenJDK, JEP 456 e 476)
    * JavaScript ES2024 (ECMA-262 15a edicao) + TypeScript 5.6
    * Rust 1.82+ (Edition 2024, estabilizada em out/2024)
    * Portugol++ (saida .md legivel por humano, pseudo-codigo PT-BR)
- Toolchains RISC-V: RV64GC (avancado/padrao) e RV32IMAC (essencial),
  usando o backend RISC-V do LLVM 19 / GCC 14.
- Edge AI 2024/2025: TensorFlow Lite 2.17+, Core ML 7 (iOS 18),
  ExecuTorch 0.5+ (PyTorch Edge) e ONNX Runtime Mobile 1.20+.
- OS minimos: Android 15+ (V), iOS 18+, Windows 11 (24H2),
  WearOS 6 / watchOS 11, Linux embarcado 6.6 LTS.
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field
from collections import defaultdict
from datetime import datetime
import sys


# ============================================================================
# 0. METADADOS DE VERSAO (baseline 2024/2025)
# ============================================================================

#: Versao deste modulo -- segue o calendario de releases da Republica.
MODULO_VERSAO: str = "2025.08.04-r1"

#: Versao minima do interpretador Python considerado fonte.
PYTHON_MINIMO: Tuple[int, int] = (3, 13)

#: Versoes dos transpiladores-alvo suportadas pelo toolchain CI/CD.
#:
#: Chave = id de ``LinguagemAlvo``; valor = (familia, versao_minima, notas).
TRANSPILADORES_SUPORTADOS: Dict[str, Tuple[str, str, str]] = {
    "c":          ("C23",            "GCC 14 / Clang 19",  "ISO/IEC 9899:2024; backend RISC-V estavel"),
    "go":         ("Go",             "1.23+",              "Generics estaveis desde 1.18; Edition padrao"),
    "java":       ("Java",           "21 LTS / 25 LTS",    "OpenJDK; JEP 456 (unnamed vars), JEP 476 (modules)"),
    "javascript": ("JS + TypeScript","ES2024 / TS 5.6",    "ECMA-262 15a ed.; saida TS tipada para tooling"),
    "rust":       ("Rust",           "1.82+ (Edition 2024)","riscv64gc / riscv32imc targets tier 2"),
    "portugol":   ("Portugol++",     "1.x (interno)",      "Saida .md em PT-BR; legivel por nao-programadores"),
}

#: Frameworks de IA na borda suportados em smartphone/tablet (2024/2025).
EDGE_AI_FRAMEWORKS: List[str] = [
    "TensorFlow Lite 2.17+",
    "Core ML 7 (iOS 18+)",
    "ExecuTorch 0.5+ (PyTorch Edge)",
    "ONNX Runtime Mobile 1.20+",
]


# ============================================================================
# 1. ENUMS (modulo-level)
# ============================================================================

class LinguagemAlvo(Enum):
    """Linguagens para as quais o codigo-fonte e transpilado."""
    PYTHON = ("python", "Python (.py) -- FONTE, nao transpilada")
    C = ("c", "C23 (.c) -- transpilado (GCC 14 / Clang 19)")
    GO = ("go", "Go 1.23+ (.go) -- transpilado")
    JAVA = ("java", "Java 21 LTS (.java) -- transpilado")
    JAVASCRIPT = ("javascript", "JS ES2024 / TS 5.6 (.js) -- transpilado")
    RUST = ("rust", "Rust 1.82+ / Edition 2024 (.rs) -- transpilado")
    PORTUGOL = ("portugol", "Portugol++ (.md) -- transpilado (PT-BR)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def e_fonte(self) -> bool:
        return self == LinguagemAlvo.PYTHON


class TipoHardware(Enum):
    """Categorias de hardware onde o codigo deve rodar."""
    RISC_V_AVANCADO = ("risc_v_avancado", "RepublicaPort Avancado (RISC-V 64-bit, IA local)")
    RISC_V_PADRAO = ("risc_v_padrao", "RepublicaPort Padrao (RISC-V 64-bit)")
    RISC_V_ESSENCIAL = ("risc_v_essencial", "RepublicaPort Essencial (RISC-V 32-bit)")
    HEADPHONE_BT = ("headphone_bt", "Headphone Bluetooth (firmware)")
    SMARTPHONE = ("smartphone", "Smartphone (Android/iOS)")
    SMARTWATCH = ("smartwatch", "Smartwatch (RTOS/WatchOS)")
    EYE_TRACKER = ("eye_tracker", "Eye Tracker (Windows/Linux)")
    BRAILLE_DISPLAY = ("braille_display", "Display Braille (firmware)")
    SWITCH = ("switch", "Switch Button (firmware MCU)")
    TABLET = ("tablet", "Tablet CAA (Android/iOS)")
    E_READER = ("e_reader", "E-reader (Linux embarcado)")
    GPS_TRACKER = ("gps_tracker", "GPS Tracker (firmware MCU)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class StatusCompatibilidade(Enum):
    """Status de compatibilidade de um modulo com um hardware."""
    COMPATIVEL = ("compativel", "Compativel: roda sem modificacao")
    ADAPTACAO = ("adaptacao", "Adaptacao necessaria (UI/resolucao)")
    PORTAVEL = ("portavel", "Portavel com esforco (recompilar)")
    INCOMPATIVEL = ("incompativel", "Incompativel (recurso ausente)")
    NAO_APLICAVEL = ("nao_aplicavel", "Nao aplicavel neste hardware")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class CanalUpdate(Enum):
    """O unico canal de atualizacao da Republica."""
    ESTAVEL = ("estavel", "Estavel: versao auditada, pronta para todos")
    BETA = ("beta", "Beta: versao em teste, voluntarios only")
    NIGHTLY = ("nightly", "Nightly: build diario automatico do .py")
    HOTFIX = ("hotfix", "Hotfix: correcao critica, deploy imediato")
    ROLLBACK = ("rollback", "Rollback: voltar para versao anterior")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoArquivo(Enum):
    """Tipo de arquivo no repositorio."""
    FONTE = ("fonte", "FONTE: .py (editado a mao, commitado)")
    ARTEFATO = ("artefato", "ARTEFATO: .c/.go/.java/.js/.rs/.md (gerado, NAO editado)")
    CONFIG = ("config", "Config: configuracao do sistema")
    TESTE = ("teste", "Teste: verificacao")
    DOC = ("doc", "Documentacao")

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
class ModuloCodebase:
    """Um modulo do codigo-fonte da Republica."""
    id: str
    nome: str
    arquivo_fonte: str        # "core/open_energy.py"
    artefatos_gerados: List[str] = field(default_factory=list)  # .c .go .java .js .rs .md
    linhas_fonte: int = 0
    compatibilidade: Dict[str, StatusCompatibilidade] = field(default_factory=dict)
    ultima_transpilacao: str = ""  # timestamp
    commit_fonte: str = ""   # hash do ultimo commit do .py


@dataclass
class VersaoUnificada:
    """Uma versao do codigo da Republica (um commit do .py = uma versao)."""
    versao: str              # "2026.07.26-r1"
    canal: CanalUpdate
    commit_hash: str
    modulos_atualizados: List[str] = field(default_factory=list)
    artefatos_gerados: int = 0
    hardware_compativel: List[TipoHardware] = field(default_factory=list)
    timestamp: str = ""
    notas: str = ""


@dataclass
class PoliticaTranspilacao:
    """Regras do transpilador automatico."""
    fonte_editavel: bool = True      # so .py e editado
    artefatos_no_git: bool = False   # artefatos NAO entram no git (CI gera)
    verificacao_pos_geracao: bool = True  # testar apos transpilar
    linguagens_alvo: List[LinguagemAlvo] = field(default_factory=list)
    min_linhas_artefato: int = 0     # minimo de linhas (anti-abreviacao)


@dataclass
class MatrizCompatibilidade:
    """Qual modulo roda em qual hardware."""
    modulo_id: str
    hardware: TipoHardware
    status: StatusCompatibilidade
    adaptacoes_necessarias: List[str] = field(default_factory=list)
    notas: str = ""


# ============================================================================
# 3. TABELA: HARDWARE x REQUISITOS DE CODIGO
# ============================================================================

# Cada hardware tem requisitos de compilacao/execucao diferentes
REQUISITOS_HARDWARE: Dict[str, Dict[str, str]] = {
    "risc_v_avancado": {
        "linguagem": "Rust 1.82+ (Edition 2024) ou C23 (RISC-V RV64GC)",
        "runtime": "Linux embarcado 6.6 LTS ou bare-metal",
        "ram_minima": "32GB",
        "ia_local": "Sim (NPU dedicada + llama.cpp / ExecuTorch)",
        "update": "Canal unico OTA (signed)",
    },
    "risc_v_padrao": {
        "linguagem": "C23 ou Rust 1.82+ (Edition 2024, RISC-V RV64GC)",
        "runtime": "Linux embarcado 6.6 LTS",
        "ram_minima": "16GB",
        "ia_local": "Sim (inferencia basica, ONNX RT / TFLite)",
        "update": "Canal unico OTA (signed)",
    },
    "risc_v_essencial": {
        "linguagem": "C23 (RISC-V RV32IMAC, baixo consumo)",
        "runtime": "RTOS ou bare-metal",
        "ram_minima": "4GB",
        "ia_local": "Nao",
        "update": "Canal unico OTA (signed, compactado)",
    },
    "smartphone": {
        "linguagem": "JavaScript (React Native 0.76+) ou Kotlin 2.0 / Swift 6 via ponte",
        "runtime": "Android 15+ (V) ou iOS 18+",
        "ram_minima": "6GB",
        "ia_local": "Sim (TFLite 2.17 / Core ML 7 / ExecuTorch / ONNX RT Mobile)",
        "update": "Canal unico (App Store / Play Store / APK direto)",
    },
    "smartwatch": {
        "linguagem": "C (RTOS) ou Swift 6 / Kotlin 2.0 (watchOS 11/WearOS 6)",
        "runtime": "RTOS proprietario ou WearOS 6 / watchOS 11",
        "ram_minima": "1GB",
        "ia_local": "Limitada (sensores only)",
        "update": "Canal unico (via smartphone pareado)",
    },
    "headphone_bt": {
        "linguagem": "C23 (firmware MCU Bluetooth)",
        "runtime": "RTOS Bluetooth (bare-metal)",
        "ram_minima": "256KB",
        "ia_local": "Nao",
        "update": "Canal unico OTA Bluetooth (signed)",
    },
    "eye_tracker": {
        "linguagem": "C++23 (Windows) ou Rust 1.82+ (Linux)",
        "runtime": "Windows 11 (24H2) ou Linux 6.6 LTS+",
        "ram_minima": "8GB",
        "ia_local": "Nao (processamento no PC)",
        "update": "Canal unico (driver + software)",
    },
    "braille_display": {
        "linguagem": "C23 (firmware MCU + driver Bluetooth/USB)",
        "runtime": "Bare-metal",
        "ram_minima": "128KB",
        "ia_local": "Nao",
        "update": "Canal unico OTA (signed)",
    },
    "switch": {
        "linguagem": "C23 (firmware MCU Bluetooth)",
        "runtime": "Bare-metal",
        "ram_minima": "64KB",
        "ia_local": "Nao",
        "update": "Canal unico OTA (signed)",
    },
    "tablet": {
        "linguagem": "JavaScript (React Native 0.76+) ou Swift 6 / Kotlin 2.0",
        "runtime": "Android 15+ / iOS 18+",
        "ram_minima": "6GB",
        "ia_local": "Sim (TTS neural, CAA com LLM na borda)",
        "update": "Canal unico (App Store / APK)",
    },
    "e_reader": {
        "linguagem": "C++23 ou Java 21 LTS (Linux embarcado)",
        "runtime": "Linux embarcado 6.6 LTS",
        "ram_minima": "1GB",
        "ia_local": "Limitada (TTS basico)",
        "update": "Canal unico OTA (signed)",
    },
    "gps_tracker": {
        "linguagem": "C23 (firmware MCU 4G+GPS)",
        "runtime": "Bare-metal",
        "ram_minima": "256KB",
        "ia_local": "Nao",
        "update": "Canal unico OTA 4G (signed)",
    },
}


# ============================================================================
# 4. ENGINE
# ============================================================================

class UnifiedCodebaseEngine:
    """Motor do Codebase Unificado: uma fonte, transpilacao, todo hardware."""

    def __init__(self) -> None:
        self.modulos: Dict[str, ModuloCodebase] = {}
        self.versoes: List[VersaoUnificada] = []
        self.politica: PoliticaTranspilacao = PoliticaTranspilacao(
            fonte_editavel=True,
            artefatos_no_git=False,
            verificacao_pos_geracao=True,
            linguagens_alvo=[l for l in LinguagemAlvo if not l.e_fonte],
        )
        self.matriz: List[MatrizCompatibilidade] = []
        self._mod_id = 0
        self._ver_counter = 0

    def _mod_novo_id(self) -> str:
        self._mod_id += 1
        return f"MOD-{self._mod_id:04d}"

    # -- cadastro de modulos ----------------------------------------------

    def registrar_modulo(
        self,
        nome: str,
        arquivo_fonte: str,
        linhas_fonte: int = 0,
        compatibilidade: Optional[Dict[str, StatusCompatibilidade]] = None,
    ) -> ModuloCodebase:
        """Registra um modulo do codigo-fonte (.py)."""
        m = ModuloCodebase(
            id=self._mod_novo_id(),
            nome=nome,
            arquivo_fonte=arquivo_fonte,
            linhas_fonte=linhas_fonte,
            compatibilidade=compatibilidade or {},
            artefatos_gerados=self._gerar_lista_artefatos(arquivo_fonte),
        )
        self.modulos[m.id] = m
        return m

    def _gerar_lista_artefatos(self, fonte: str) -> List[str]:
        """Gera lista de artefatos a partir do nome do arquivo-fonte."""
        base = fonte.replace(".py", "")
        extensoes = [".c", ".go", ".java", ".js", ".rs", ".md"]
        return [base + ext for ext in extensoes]

    # -- transpilacao ------------------------------------------------------

    def transpilar_modulo(self, mod_id: str) -> Dict[str, Any]:
        """
        Simula a transpilacao de um modulo .py para 6 linguagens.
        No mundo real, chamaria o transpilador da Republica (toolchain 2024/2025).
        """
        m = self.modulos.get(mod_id)
        if m is None:
            return {"erro": "Modulo nao encontrado"}
        artefatos_ok = 0
        artefatos_falha = 0
        detalhes: List[str] = []
        # Mapa extensao -> LinguagemAlvo (fonte unica de verdade das versoes).
        ext_para_lang: Dict[str, LinguagemAlvo] = {
            "c": LinguagemAlvo.C,
            "go": LinguagemAlvo.GO,
            "java": LinguagemAlvo.JAVA,
            "js": LinguagemAlvo.JAVASCRIPT,
            "rs": LinguagemAlvo.RUST,
            "md": LinguagemAlvo.PORTUGOL,
        }
        for artefato in m.artefatos_gerados:
            # simulacao: todos geram com sucesso
            ext = artefato.split(".")[-1]
            lang = ext_para_lang.get(ext)
            # versao curta do toolchain (ex.: "C23", "Go 1.23+", "Rust 1.82+")
            info = TRANSPILADORES_SUPORTADOS.get(lang.id) if lang else None
            versao = info[0] if info else "?"
            artefatos_ok += 1
            detalhes.append(f"  {versao:>16}: {artefato} OK")
        m.ultima_transpilacao = datetime.now().isoformat()
        return {
            "modulo": m.nome,
            "fonte": m.arquivo_fonte,
            "artefatos_ok": artefatos_ok,
            "artefatos_falha": artefatos_falha,
            "detalhes": detalhes,
            "timestamp": m.ultima_transpilacao,
        }

    def transpilar_todos(self) -> List[Dict[str, Any]]:
        """Transpila TODOS os modulos registrados."""
        return [self.transpilar_modulo(mid) for mid in self.modulos]

    # -- matriz de compatibilidade ----------------------------------------

    def construir_matriz_compatibilidade(self) -> List[MatrizCompatibilidade]:
        """Para cada modulo x hardware, determina compatibilidade."""
        self.matriz.clear()
        for mod in self.modulos.values():
            for hw in TipoHardware:
                status = self._avaliar_compatibilidade(mod, hw)
                self.matriz.append(MatrizCompatibilidade(
                    modulo_id=mod.id,
                    hardware=hw,
                    status=status,
                ))
        return self.matriz

    def _avaliar_compatibilidade(self, mod: ModuloCodebase, hw: TipoHardware) -> StatusCompatibilidade:
        """
        Heuristica de compatibilidade.
        Modulos de logica pura rodam em qualquer lugar.
        Modulos com UI precisam de adaptacao.
        Modulos que precisam de GPU/IA nao rodam em MCU.
        """
        # se o modulo ja tem status definido, usa
        if hw.id in mod.compatibilidade:
            return mod.compatibilidade[hw.id]
        # heuristicas
        nome = mod.nome.lower()
        if any(kw in nome for kw in ["firmware", "mcu", "bluetooth"]):
            if hw.id in ("headphone_bt", "switch", "braille_display", "gps_tracker"):
                return StatusCompatibilidade.COMPATIVEL
            return StatusCompatibilidade.NAO_APLICAVEL
        if any(kw in nome for kw in ["ia", "modelo", "gpu", "neural"]):
            if hw.id in ("risc_v_essencial", "smartwatch", "headphone_bt",
                         "braille_display", "switch", "e_reader", "gps_tracker"):
                return StatusCompatibilidade.INCOMPATIVEL
            return StatusCompatibilidade.COMPATIVEL
        # logica pura: roda em tudo que tem runtime
        if hw.id in ("headphone_bt", "switch", "braille_display", "gps_tracker"):
            return StatusCompatibilidade.PORTAVEL  # MCU precisa recompilar
        return StatusCompatibilidade.COMPATIVEL

    def modulos_por_hardware(self, hw: TipoHardware) -> Dict[StatusCompatibilidade, List[str]]:
        """Quais modulos rodam em qual hardware."""
        resultado: Dict[StatusCompatibilidade, List[str]] = defaultdict(list)
        for mc in self.matriz:
            if mc.hardware == hw:
                mod = self.modulos.get(mc.modulo_id)
                if mod:
                    resultado[mc.status].append(mod.nome)
        return dict(resultado)

    # -- canal unico de atualizacao ---------------------------------------

    def publicar_versao(
        self,
        canal: CanalUpdate,
        modulos_atualizados: List[str],
        notas: str = "",
    ) -> VersaoUnificada:
        """
        Publica uma nova versao no canal unico.
        O commit do .py gera artefatos para TODO o hardware.
        """
        self._ver_counter += 1
        hoje = datetime.now().strftime("%Y.%m.%d")
        versao = f"{hoje}-r{self._ver_counter}"
        total_artefatos = 0
        for mid in modulos_atualizados:
            m = self.modulos.get(mid)
            if m:
                total_artefatos += len(m.artefatos_gerados)
        v = VersaoUnificada(
            versao=versao,
            canal=canal,
            commit_hash=hex(hash(versao) & 0xFFFFFFFF)[2:].zfill(8),
            modulos_atualizados=modulos_atualizados,
            artefatos_gerados=total_artefatos,
            hardware_compativel=list(TipoHardware),
            timestamp=datetime.now().isoformat(),
            notas=notas,
        )
        self.versoes.append(v)
        return v

    def ultima_versao_estavel(self) -> Optional[VersaoUnificada]:
        for v in reversed(self.versoes):
            if v.canal == CanalUpdate.ESTAVEL:
                return v
        return None

    # -- regras do git -----------------------------------------------------

    def regras_git(self) -> List[str]:
        """As regras do que entra e nao entra no git."""
        return [
            "REGRA 1: So .py e commitado no git como fonte.",
            "REGRA 2: .c/.go/.java/.js/.rs/.md sao GERADOS pelo CI/CD.",
            "REGRA 3: Artefatos podem ser .gitignore'd ou gerados on-demand.",
            "REGRA 4: Se voce edita .c a mao, voce esta fazendo errado.",
            "REGRA 5: Commit do .py = trigger do transpilador = artefatos para todos.",
            "REGRA 6: Um commit = uma versao. Versao versionada por data+revisao.",
            "REGRA 7: Hotfix no .py = hotfix em TODO o hardware automaticamente.",
            "REGRA 8: Ninguem da commit em .c/.go/.java/.js/.rs separadamente.",
            "REGRA 9: O transpilador e AUDITADO. Mudanca no transpilador = revisao.",
            "REGRA 10: .gitignore inclui: core/*.c core/*.go core/*.java core/*.js core/*.rs",
        ]

    # -- manifesto ---------------------------------------------------------

    def manifesto_unificado(self) -> str:
        return (
            "MANIFESTO DO CODEBASE UNIFICADO:\n"
            "  Uma linguagem fonte: Python (.py).\n"
            "  Transpilacao automatica para 6 linguagens.\n"
            "  Todo hardware roda o mesmo codigo (adaptado por arquitetura).\n"
            "  Um canal de atualizacao para TODOS os dispositivos.\n"
            "  Artefatos sao GERADOS, nao escritos. Como .o, nao .c.\n"
            "  Commit so do .py. O transpilador faz o resto.\n"
            "  Quem edita .c a mao esta quebrando a Republica."
        )

    # -- scorecard ---------------------------------------------------------

    def scorecard(self) -> Dict[str, Any]:
        matriz = self.construir_matriz_compatibilidade()
        compativeis = sum(1 for m in matriz if m.status == StatusCompatibilidade.COMPATIVEL)
        total = len(matriz)
        return {
            "modulos_registrados": len(self.modulos),
            "versoes_publicadas": len(self.versoes),
            "linguagens_alvo": len(self.politica.linguagens_alvo),
            "hardwares_suportados": len(list(TipoHardware)),
            "matriz_compatibilidade": total,
            "modulos_compativeis_tudo": compativeis,
            "pct_compatibilidade": round(compativeis / total * 100, 1) if total else 0.0,
            "ultima_versao": self.ultima_versao_estavel().versao if self.ultima_versao_estavel() else "nenhuma",
            "artefatos_gitignored": self.politica.artefatos_no_git is False,
        }


# ============================================================================
# 5. DEMO
# ============================================================================

def _demo() -> None:
    e = UnifiedCodebaseEngine()

    print("=" * 70)
    print("OpenUnifiedCodebase -- Uma Linguagem, Um Canal, Todo Hardware")
    print("=" * 70)

    # --- Baseline de versao (2024/2025) ---
    print(f"\n[BASELINE DE TOOLCHAIN]")
    print(f"  Modulo: {MODULO_VERSAO}")
    print(f"  Python (fonte): {sys.version.split()[0]} (minimo exigido: {PYTHON_MINIMO[0]}.{PYTHON_MINIMO[1]})")
    print(f"  Transpiladores-alvo:")
    for lang_id, (fam, ver, nota) in TRANSPILADORES_SUPORTADOS.items():
        print(f"    {fam:<18} {ver:<22} {nota}")
    print(f"  Edge AI: {', '.join(EDGE_AI_FRAMEWORKS)}")

    # --- O Manifesto ---
    print(f"\n{e.manifesto_unificado()}")

    # --- A Politica ---
    print("\n[POLITICA DE TRANSPILACAO]")
    print(f"  Fonte editavel: {'Sim' if e.politica.fonte_editavel else 'Nao'}")
    print(f"  Artefatos no git: {'Sim' if e.politica.artefatos_no_git else 'NAO (CI gera)'}")
    print(f"  Verificacao pos-geracao: {'Sim' if e.politica.verificacao_pos_geracao else 'Nao'}")
    print(f"  Linguagens alvo: {[l.rotulo for l in e.politica.linguagens_alvo]}")

    # --- Registrar modulos ---
    print("\n[MODULOS REGISTRADOS]")
    modulos_demo = [
        ("OpenEnergy", "core/open_energy.py", 731),
        ("OpenSovereignTech", "core/open_sovereign_tech.py", 735),
        ("OpenAccessibilityHardwareSpecs", "core/open_accessibility_hardware_specs.py", 1214),
        ("OpenAntiPolarization", "core/open_anti_polarization.py", 762),
        ("OpenAgrarianRevolution", "core/open_agrarian_revolution.py", 788),
        ("OpenTelefonista", "core/open_telefonista.py", 1100),
    ]
    for nome, arquivo, linhas in modulos_demo:
        m = e.registrar_modulo(nome, arquivo, linhas)
        print(f"  {m.id}: {m.nome} ({m.arquivo_fonte}, {m.linhas_fonte} linhas)")
        print(f"    Artefatos: {len(m.artefatos_gerados)} arquivos gerados")

    # --- Transpilacao ---
    print("\n[TRANSPILACAO AUTOMATICA]")
    for mid in list(e.modulos.keys())[:3]:  # so 3 para nao poluir
        resultado = e.transpilar_modulo(mid)
        print(f"\n  {resultado['modulo']} -> {resultado['artefatos_ok']} artefatos OK")
        for d in resultado["detalhes"]:
            print(f"  {d}")

    # --- Matriz de Compatibilidade ---
    print("\n[MATRIZ DE COMPATIBILIDADE -- Modulo x Hardware]")
    matriz = e.construir_matriz_compatibilidade()
    hw_list = list(TipoHardware)
    print(f"\n  {'Modulo':.<30} ", end="")
    for hw in hw_list[:6]:
        print(f" {hw.id[:8]:>10}", end="")
    print(f" {'...':>10}")
    print(f"  {'-'*100}")
    for mod in list(e.modulos.values())[:4]:
        print(f"  {mod.nome[:28]:.<30} ", end="")
        for hw in hw_list[:6]:
            mc = next((m for m in matriz if m.modulo_id == mod.id and m.hardware == hw), None)
            if mc:
                flag = {"compativel": "OK", "adaptacao": "ADAPT",
                        "portavel": "PORT", "incompativel": "INCOMP",
                        "nao_aplicavel": "N/A"}[mc.status.id]
                print(f" {flag:>10}", end="")
        print(f" {'...':>10}")

    # --- Requisitos por hardware ---
    print("\n[REQUISITOS DE CODIGO POR HARDWARE]")
    for hw_id, reqs in REQUISITOS_HARDWARE.items():
        hw = next(h for h in TipoHardware if h.id == hw_id)
        print(f"\n  {hw.rotulo}:")
        for k, v in reqs.items():
            print(f"    {k}: {v}")

    # --- Regras do Git ---
    print("\n[REGRAS DO GIT -- O que entra e o que nao entra]")
    for regra in e.regras_git():
        print(f"  {regra}")

    # --- Canal Unico ---
    print("\n[CANAL UNICO DE ATUALIZACAO]")
    mod_ids = list(e.modulos.keys())
    v1 = e.publicar_versao(
        CanalUpdate.NIGHTLY,
        mod_ids[:3],
        "Nightly build automatico apos commit do .py",
    )
    print(f"\n  Versao {v1.versao} ({v1.canal.rotulo})")
    print(f"  Commit: {v1.commit_hash}")
    print(f"  Modulos: {len(v1.modulos_atualizados)}")
    print(f"  Artefatos gerados: {v1.artefatos_gerados}")
    print(f"  Hardware compativel: {len(v1.hardware_compativel)} dispositivos")
    print(f"  Notas: {v1.notas}")

    v2 = e.publicar_versao(
        CanalUpdate.ESTAVEL,
        mod_ids,
        "Release estavel: todos os modulos auditados",
    )
    print(f"\n  Versao {v2.versao} ({v2.canal.rotulo})")
    print(f"  Commit: {v2.commit_hash}")
    print(f"  Modulos: {len(v2.modulos_atualizados)}")
    print(f"  Artefatos gerados: {v2.artefatos_gerados}")
    print(f"  Hardware compativel: {len(v2.hardware_compativel)} dispositivos")

    # --- Fluxo antigo vs novo ---
    print("\n[FLUXO: ANTES vs DEPOIS]")
    print("""
  ANTES (ERRADO -- babilonia linguistica):
    1. Escrever .py (fonte)
    2. Despachar 3 subagentes para transpilar para 6 linguagens
    3. Subagentes abreviam, falham, precisam regenerar
    4. Commit de 7 arquivos por modulo
    5. 7 arquivos que dessincronizam
    6. Bug no .c? Edita .c. Bug volta no proximo transpile.
    CUSTO: 5-10 minutos por modulo, 7 arquivos para manter.

  DEPOIS (CORRETO -- codebase unificado):
    1. Escrever .py (fonte)
    2. python3 transpilador.py core/open_xxx.py --all
    3. CI/CD gera artefatos automaticamente
    4. Commit so do .py
    5. Artefatos regenerados a cada commit
    6. Bug? Corrige no .py. Transpilador corrige todos.
    CUSTO: 1 arquivo para manter. Transpilador faz o resto.
""")

    # --- Scorecard ---
    print("[SCORECARD]")
    sc = e.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<30} {v}")

    # --- FILOSOFIA ---
    print("\n" + "=" * 70)
    print("FILOSOFIA -- Uma linguagem, um canal, todo hardware")
    print("=" * 70)
    print("""
A BABILONIA LINGUISTICA ACABOU.

O projeto tinha 7 arquivos por modulo. Isso e INSSUSTENTAVEL.
- 7 arquivos para manter a cada mudanca.
- 7 arquivos que dessincronizam.
- 7 arquivos onde bugs se escondem.
- 7 arquivos que NINGUEM le todos.

A DECISAO E SIMPLES:
  UMA linguagem fonte: Python (.py).
  Transpilacao AUTOMATICA para 6 linguagens.
  TODO hardware roda o mesmo codigo.
  UM canal de atualizacao para TODOS os dispositivos.

O QUE ISTO MUDA NA PRATICA:
  1. Desenvolvedor escreve .py. So .py. PONTO.
  2. Commit do .py dispara o transpilador no CI/CD.
  3. Transpilador gera .c/.go/.java/.js/.rs para cada arquitetura.
  4. CI/CD testa cada artefato (compila? roda? passa?).
  5. Se passou, publica no canal unico.
  6. Todo hardware recebe a mesma versao (adaptada por arquitetura).

O ARTEFATO NAO E CODIGO-FONTE:
  .c gerado pelo transpilador e como .o gerado pelo compilador.
  Voce nao edita .o. Voce nao edita .c gerado.
  Voce edita .py. O transpilador (como o compilador) faz o resto.

TODO HARDWARE RODA O MESMO CODIGO:
  RepublicaPort RISC-V (avancado/padrao/essencial).
  Smartphone (Android/iOS). Smartwatch. Tablet.
  Headphone Bluetooth. Switch. Braille Display. GPS Tracker.
  Eye Tracker. E-reader. Webcam. Microfone.
  TODOS recebem o mesmo update. Na mesma versao. Ao mesmo tempo.

UM CANAL DE ATUALIZACAO:
  Nao existe "versao Android diferente de iOS".
  Nao existe "firmware do headphone atrasado".
  Um commit do .py = update para TODO o ecossistema.
  Quem controla o canal controla a versao.
  Quem controla a versao controla a Republica.
  O canal e PUBLICO, AUDITAVEL, e VERSIONADO.

A SOBERANIA DO CODIGO:
  Soberania tecnologica nao e so GPS proprio e chip RISC-V.
  Soberania do codigo e saber que TODO o codigo que roda
  na Republica veio de UMA fonte, passou por UM transpilador,
  e chegou em TODO hardware pelo MESMO canal.
  Sem fragmentacao. Sem dessincronia. Sem babilonia.
""")


if __name__ == "__main__":
    _demo()
