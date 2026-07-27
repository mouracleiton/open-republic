#!/usr/bin/env python3
"""
OpenSovereignTech -- Soberania Tecnologica da Republica
=========================================================
"GPS proprio. RISC-V local. Rede configurada. Teste e o basico do basico.
Sistemas sao feitos para humanos. Todos tem acesso ao codigo.
A especificacao nao pode ser alterada por um vendor.
Todos os produtos sao iguais -- muda a marca e as cores."

A Republica NAO depende de tecnologia estrangeira para existir.
GPS estrangeiro = quem controla o satelite controla onde voce chega.
Chip estrangeiro = quem fabrica o silicio controla o que voce computa.
Rede estrangeira = quem roteia o pacote controla o que voce comunica.

SOBERANIA TECNOLOGICA = SOBERANIA DE FATO.

OS 7 PILARES DA SOBERANIA TECNOLOGICA:

1. GPS SOBERANO
   O Brasil tem territorio continental. Depender do GPS americano (NAVSTAR),
   do Galileu europeu ou do BeiDou chines e DEPENDENCIA ESTRATEGICA.
   Quem controla o posicionamento controla a logistica, a defesa,
   a agricultura de precisao, a navegacao, a drones civica.
   A Republica constela seus proprios satelites de posicionamento.

2. COMPUTADORES RISC-V
   RISC-V e uma ISA (Instruction Set Architecture) ABERTA e LIVRE.
   Nenhum vendor (Intel, AMD, ARM) pode fechar ou alterar a especificacao.
   A Republica fabrica (ou manda fabricar) seus proprios chips RISC-V.
   Capazes de rodar modelos de IA LOCAIS -- sem nuvem, sem Big Tech.
   Seu processador, seus dados, seu poder de computacao.

3. REDE SOBERANA
   A rede da Republica e bem configurada: roteamento local-first,
   DNS proprio, caching distribuido, CRDT para operacao offline.
   Nao depende de backbone estrangeiro para funcionar entre comunidades.
   Se a conexao externa cai, a Republica CONTINUA operando.

4. TESTE E O BASICO DO BASICO
   "Sistemas sao feitos para humanos." Humano testa. Sistema que nao foi
   testado com humanos REAIS (incluindo deficientes) NAO existe na Republica.
   Nao existe "release depois corrige". Teste e pre-requisito, nao pos-requisito.

5. CODIGO ABERTO RADICAL
   "Todos tem acesso ao codigo." Sem excecao. Sem "premium tier".
   Sem "enterprise only". O codigo e da Republica, e da humanidade.
   CC0. Sem patente. Sem propriedade intelectual sobre software basico.

6. SPEC IMUTAVEL (zero vendor lock-in)
   "A especificacao nao pode ser alterada por um vendor."
   RISC-V nao pode ser "estendido" por uma empresa e fechado.
   HTML/CSS/JS nao podem ser "melhorados" por um browser e trancados.
   O padrao e DA REPUBLICA. Vendors implementam; nao inventam.

7. HARDWARE COMMODITIZADO
   "Todos os produtos sao iguais. Muda a marca e as cores e coisas cosmeticas."
   O chip RISC-V e o MESMO. A placa-mae e a MESMA. O sistema e o MESMO.
   O que muda: cor da carcaa, logo, embalagem. Nao o que importa.
   Acaba a distincao artificial entre "premium" e "basico" que cria elite.

ALINHAMENTO CONSTITUCIONAL:
- P1: Tecnologia estrangeira = elite externa controlando. Soberania = anti-elitismo.
- P2: Seus dados, seu chip, seu processamento = autonomia corporal digital.
- P4: Codigo aberto = transparencia radical. Ninguem governe o que nao pode ver.
- P6: Acesso universal = codigo + hardware + rede. Nao so conhecimento.

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field
from collections import defaultdict
from datetime import datetime


# ============================================================================
# 1. ENUMS (modulo-level)
# ============================================================================

class PilarSoberania(Enum):
    """Os 7 pilares da soberania tecnologica."""
    GPS_SOBERANO = ("gps_soberano", "GPS Soberano (posicionamento nacional)", 1)
    RISC_V = ("risc_v", "Computadores RISC-V (ISA aberta, IA local)", 2)
    REDE_SOBERANA = ("rede_soberana", "Rede Soberana (local-first, offline-capable)", 3)
    TESTE_HUMANO = ("teste_humano", "Teste e o basico (teste com humanos reais)", 4)
    CODIGO_ABERTO = ("codigo_aberto", "Codigo aberto radical (CC0, sem excecao)", 5)
    SPEC_IMUTAVEL = ("spec_imutavel", "Spec imutavel (zero vendor lock-in)", 6)
    HARDWARE_COMMODITIZADO = ("hardware_commoditizado", "Hardware commoditizado (produtos iguais)", 7)

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def numero(self) -> int:
        return self.value[2]


class StatusSoberania(Enum):
    """Quanto da soberania tecnologica ja e realidade."""
    DEPENDENTE = ("dependente", "Dependente: 100% estrangeiro, zero controle")
    PARCIAL = ("parcial", "Parcial: algum controle, nucleo estrangeiro")
    TRANSICAO = ("transicao", "Em transicao: infraestrutura propria em construcao")
    SOBERANO = ("soberano", "Soberano: controla o stack completo")
    AUTARQUICO = ("autarquico", "Autarquico: nao so controla, como fabrica e doa")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoVendorLockIn(Enum):
    """Formas como vendors tentam capturar a especificacao."""
    EXTENSAO_PROPRIETARIA = ("extensao_proprietaria", "Extensao proprietaria ao padrao aberto")
    DRIVER_FECHADO = ("driver_fechado", "Driver/firmware fechado (hardware funciona so com SW da vendor)")
    PATENTE_TRUQUEDA = ("patente_trucada", "Patente sobre o padrao aberto (trucada juridica)")
    CERTIFICACAO_OBRIGATORIA = ("certificacao_obrigatoria", "Certificacao obrigatoria paga (toll booth)")
    FORMATO_INCOMPATIVEL = ("formato_incompativel", "Formato proprietario incompativel com padrao")
    BACKDOOR_FIRMWARE = ("backdoor_firmware", "Backdoor/firmware opaco (seguranca invisivel)")
    OBSOLESCENCIA_FORCADA = ("obsolescencia_forcada", "Obsolescencia forcada (quebra sem atualizacao)")
    UPDATE_BLOQUEADO = ("update_bloqueado", "Update bloqueado em hardware antigo (sem motivo real)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoTeste(Enum):
    """Tipos de teste. "Teste e o basico do basico." Nenhum e opcional."""
    UNITARIO = ("unitario", "Teste unitario (cada funcao isolada)")
    INTEGRACAO = ("integracao", "Teste de integracao (componentes juntos)")
    HUMANO_REAL = ("humano_real", "Teste com humano real (nao simulacao)")
    HUMANO_DEFICIENTE = ("humano_deficiente", "Teste com pessoa com deficiencia (CEGO/SURDO/TETRA/TEA)")
    STRESS = ("stress", "Teste de stress (carga, offline, falha)")
    SEGURANCA = ("seguranca", "Teste de seguranca (pen-test, auditoria)")
    CAMPO = ("campo", "Teste de campo (uso real, nao laboratorio)")
    REGRESSAO = ("regressao", "Teste de regressao (update nao quebra o que funciona)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class ComponenteStack(Enum):
    """Camadas do stack tecnologico soberano."""
    SILICIO = ("silicio", "Silicio / fab de chips (RISC-V)")
    ISA = ("isa", "ISA RISC-V (instruction set)")
    FIRMWARE = ("firmware", "Firmware (boot, drivers base)")
    KERNEL = ("kernel", "Kernel (Linux/BSD custom)")
    SISTEMA = ("sistema", "Sistema operacional da Republica")
    REDE = ("rede", "Camada de rede (DNS, roteamento, CRDT)")
    IA_LOCAL = ("ia_local", "Modelos de IA rodando localmente")
    GPS = ("gps", "Sistema de posicionamento (constelacao de satelites)")
    APLICACAO = ("aplicacao", "Aplicacoes (Republic app suite)")
    INTERFACE = ("interface", "Interface (acessivel a TODAS as deficiencias)")

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
class HardwareSoberano:
    """Um produto de hardware soberano da Republica."""
    id: str
    nome: str
    componente: ComponenteStack
    arquitetura: str             # "RISC-V RV64GC", "RISC-V RV32IMAC"
    capacidade_ia_local: bool = False  # roda modelos de IA localmente?
    ram_gb: int = 0
    armazenamento_gb: int = 0
    consumo_watts: float = 0.0
    custo_producao_cred: float = 0.0  # custo de producao (sem margem de marca)
    spec_imutavel: bool = True  # segue spec padrao sem alteracao?
    codigo_aberto: bool = True  # firmware/codigo aberto?
    testado_humano: bool = False  # testado com humanos reais?


@dataclass
class ConstelacaoGPS:
    """Satelites do sistema de posicionamento soberano."""
    nome_sistema: str
    num_satelites: int
    cobertura: str              # "Brasil", "America do Sul", "Equatorial"
    precisao_metros: float
    status: StatusSoberania = StatusSoberania.DEPENDENTE
    lancados: int = 0           # quantos ja em orbita
    planejados: int = 0         # quantos planejados
    backup_estrangeiro: str = ""  # "GPS/Galileo/BeiDou (transitorio)"


@dataclass
class VendorLockInDetectado:
    """Captura de vendor detectada no stack."""
    componente: ComponenteStack
    tipo: TipoVendorLockIn
    vendor: str
    descricao: str
    severidade: int = 5         # 1-5 (5=critico)
    acao_recomendada: str = ""


@dataclass
class TesteRealizado:
    """Um teste executado no stack soberano."""
    tipo: TipoTeste
    componente: ComponenteStack
    passou: bool
    detalhes: str = ""
    data: str = ""
    participantes_humanos: int = 0  # quantos humanos reais testaram


@dataclass
class MatrizSoberania:
    """Scorecard de soberania por componente do stack."""
    componente: ComponenteStack
    status: StatusSoberania
    pct_soberano: float = 0.0   # 0-100
    dependencias_estrangeiras: List[str] = field(default_factory=list)
    bloqueadores: List[str] = field(default_factory=list)


# ============================================================================
# 3. ENGINE
# ============================================================================

class SoberaniaTechEngine:
    """Motor da Soberania Tecnologica da Republica."""

    def __init__(self) -> None:
        self.hardwares: Dict[str, HardwareSoberano] = {}
        self.constelacao: Optional[ConstelacaoGPS] = None
        self.lockins: List[VendorLockInDetectado] = []
        self.testes: List[TesteRealizado] = []
        self.matriz: Dict[str, MatrizSoberania] = {}
        self._hw_id = 0

    def _hw_novo_id(self) -> str:
        self._hw_id += 1
        return f"HW-{self._hw_id:04d}"

    # -- cadastro de hardware ----------------------------------------------

    def cadastrar_hardware(
        self,
        nome: str,
        componente: ComponenteStack,
        arquitetura: str = "RISC-V RV64GC",
        capacidade_ia_local: bool = False,
        ram_gb: int = 0,
        armazenamento_gb: int = 0,
        consumo_watts: float = 0.0,
        custo_producao_cred: float = 0.0,
    ) -> HardwareSoberano:
        hw = HardwareSoberano(
            id=self._hw_novo_id(),
            nome=nome,
            componente=componente,
            arquitetura=arquitetura,
            capacidade_ia_local=capacidade_ia_local,
            ram_gb=ram_gb,
            armazenamento_gb=armazenamento_gb,
            consumo_watts=consumo_watts,
            custo_producao_cred=custo_producao_cred,
        )
        self.hardwares[hw.id] = hw
        return hw

    def configurar_gps(
        self,
        nome: str,
        num_satelites: int,
        cobertura: str,
        precisao_metros: float,
        lancados: int = 0,
        planejados: int = 0,
        status: StatusSoberania = StatusSoberania.DEPENDENTE,
        backup: str = "",
    ) -> ConstelacaoGPS:
        self.constelacao = ConstelacaoGPS(
            nome_sistema=nome,
            num_satelites=num_satelites,
            cobertura=cobertura,
            precisao_metros=precisao_metros,
            status=status,
            lancados=lancados,
            planejados=planejados,
            backup_estrangeiro=backup,
        )
        return self.constelacao

    # -- deteccao de vendor lock-in ----------------------------------------

    def detectar_lockin(
        self,
        componente: ComponenteStack,
        tipo: TipoVendorLockIn,
        vendor: str,
        descricao: str,
        severidade: int = 5,
    ) -> VendorLockInDetectado:
        li = VendorLockInDetectado(
            componente=componente,
            tipo=tipo,
            vendor=vendor,
            descricao=descricao,
            severidade=severidade,
            acao_recomendada=self._acao_lockin(tipo),
        )
        self.lockins.append(li)
        return li

    def _acao_lockin(self, tipo: TipoVendorLockIn) -> str:
        acoes = {
            TipoVendorLockIn.EXTENSAO_PROPRIETARIA:
                "Rejeitar extensao. Exigir conformidade com spec padrao RISC-V.",
            TipoVendorLockIn.DRIVER_FECHADO:
                "Firmware deve ser aberto (CC0). Hardware sem driver aberto NAO e comprado.",
            TipoVendorLockIn.PATENTE_TRUQUEDA:
                "RISC-V e livre de royalties. Contestar patente em corte. Nao pagar.",
            TipoVendorLockIn.CERTIFICACAO_OBRIGATORIA:
                "Certificacao e da Republica, gratuita. Nenhum vendor cobra toll.",
            TipoVendorLockIn.FORMATO_INCOMPATIVEL:
                "Formato proprietario PROIBIDO. Tudo deve seguir padrao aberto.",
            TipoVendorLockIn.BACKDOOR_FIRMWARE:
                "Firmware opaco PROIBIDO. Auditoria de seguranca radical.",
            TipoVendorLockIn.OBSOLESCENCIA_FORCADA:
                "Hardware deve funcionar por minimo 10 anos. Update garantido.",
            TipoVendorLockIn.UPDATE_BLOQUEADO:
                "Bloqueio sem motivo real e CRIME. Hardware atualizavel indefinidamente.",
        }
        return acoes.get(tipo, "Auditar e eliminar dependencia.")

    def lockins_por_severidade(self) -> List[VendorLockInDetectado]:
        return sorted(self.lockins, key=lambda x: (-x.severidade, x.componente.id))

    def lockins_criticos(self) -> List[VendorLockInDetectado]:
        return [li for li in self.lockins if li.severidade >= 4]

    # -- sistema de testes --------------------------------------------------

    def registrar_teste(
        self,
        tipo: TipoTeste,
        componente: ComponenteStack,
        passou: bool,
        detalhes: str = "",
        participantes_humanos: int = 0,
    ) -> TesteRealizado:
        t = TesteRealizado(
            tipo=tipo,
            componente=componente,
            passou=passou,
            detalhes=detalhes,
            data=datetime.now().isoformat(),
            participantes_humanos=participantes_humanos,
        )
        self.testes.append(t)
        return t

    def cobertura_testes(self, componente: ComponenteStack) -> Dict[str, Any]:
        """Verifica se TODOS os tipos de teste foram feitos para um componente."""
        tipos_testados = {t.tipo for t in self.testes if t.componente == componente and t.passou}
        tipos_faltando = set(TipoTeste) - tipos_testados
        total = len(TipoTeste)
        feitos = len(tipos_testados)
        return {
            "componente": componente.rotulo,
            "tipos_testados": feitos,
            "tipos_total": total,
            "pct_cobertura": round(feitos / total * 100, 1),
            "tipos_faltando": [t.rotulo for t in tipos_faltando],
            "aprovado": len(tipos_faltando) == 0,
            "mensagem": (
                f"COBERTURA COMPLETA: {feitos}/{total} tipos." if len(tipos_faltando) == 0
                else f"INCOMPLETO: falta {len(tipos_faltando)} tipo(s). Teste e o basico do basico."
            ),
        }

    # -- matriz de soberania -----------------------------------------------

    def construir_matriz(self) -> Dict[str, MatrizSoberania]:
        """Avalia soberania de cada componente do stack."""
        for comp in ComponenteStack:
            # hardwares deste componente
            hws = [h for h in self.hardwares.values() if h.componente == comp]
            if not hws:
                self.matriz[comp.id] = MatrizSoberania(
                    componente=comp,
                    status=StatusSoberania.DEPENDENTE,
                    pct_soberano=0.0,
                    bloqueadores=["Nenhum hardware soberano cadastrado."],
                )
                continue
            # % que tem spec imutavel + codigo aberto + testado
            soberanos = sum(1 for h in hws if h.spec_imutavel and h.codigo_aberto)
            pct = round(soberanos / len(hws) * 100, 1)
            # lockins neste componente
            lockins_comp = [li for li in self.lockins if li.componente == comp]
            deps_estrangeiras = list({li.vendor for li in lockins_comp})
            bloqueadores = [
                f"{li.tipo.rotulo} (vendor: {li.vendor})" for li in lockins_comp
            ]
            if pct == 100 and not lockins_comp:
                status = StatusSoberania.SOBERANO
            elif pct >= 50:
                status = StatusSoberania.TRANSICAO
            elif pct > 0:
                status = StatusSoberania.PARCIAL
            else:
                status = StatusSoberania.DEPENDENTE
            self.matriz[comp.id] = MatrizSoberania(
                componente=comp,
                status=status,
                pct_soberano=pct,
                dependencias_estrangeiras=deps_estrangeiras,
                bloqueadores=bloqueadores,
            )
        return self.matriz

    # -- manifesto: produtos iguais ----------------------------------------

    def manifesto_hardware_igual(self) -> str:
        """O principio: todos os produtos sao iguais, so cosmestica muda."""
        return (
            "MANIFESTO DO HARDWARE IGUAL:\n"
            "  O chip RISC-V e o MESMO em todos os produtos.\n"
            "  A placa-mae e a MESMA.\n"
            "  O firmware e o MESMO (CC0, aberto).\n"
            "  O sistema operacional e o MESMO.\n"
            "  O que pode diferir: cor da carcaca, logo, embalagem.\n"
            "  O que NAO pode diferir: performance, seguranca, acessibilidade.\n"
            "  NAO existe 'premium' vs 'basico'. Existe UM produto.\n"
            "  Quem tenta criar tiers artificiais para extrair mais dinheiro\n"
            "  esta RECRINANDO ELITE (P1). A Republica nao permite."
        )

    # -- scorecard global ---------------------------------------------------

    def scorecard(self) -> Dict[str, Any]:
        matriz = self.construir_matriz()
        soberanos = sum(1 for m in matriz.values() if m.status in (StatusSoberania.SOBERANO, StatusSoberania.AUTARQUICO))
        total = len(ComponenteStack)
        pct = round(soberanos / total * 100, 1)
        return {
            "componentes_stack": total,
            "totalmente_soberanos": soberanos,
            "pct_soberania_global": pct,
            "hardwares_cadastrados": len(self.hardwares),
            "hardwares_capazes_ia_local": sum(1 for h in self.hardwares.values() if h.capacidade_ia_local),
            "vendor_lockins_detectados": len(self.lockins),
            "lockins_criticos": len(self.lockins_criticos()),
            "testes_realizados": len(self.testes),
            "testes_com_humano_real": sum(1 for t in self.testes if t.tipo in (TipoTeste.HUMANO_REAL, TipoTeste.HUMANO_DEFICIENTE)),
            "constelacao_gps_status": self.constelacao.status.rotulo if self.constelacao else "Nao configurada",
        }


# ============================================================================
# 4. DEMO
# ============================================================================

def _demo() -> None:
    e = SoberaniaTechEngine()

    print("=" * 70)
    print("OpenSovereignTech -- Soberania Tecnologica da Republica")
    print("=" * 70)

    # --- OS 7 PILARES ---
    print("\n[OS 7 PILARES DA SOBERANIA TECNOLOGICA]")
    for p in PilarSoberania:
        print(f"\n  Pilar {p.numero}: {p.rotulo}")

    # --- GPS Soberano ---
    print("\n" + "=" * 70)
    print("[PILAR 1] GPS SOBERANO -- Constelacao Nacional")
    print("=" * 70)
    e.configurar_gps(
        nome="RepublicaNav",
        num_satelites=35,
        cobertura="Brasil + America do Sul equatorial",
        precisao_metros=1.5,
        lancados=3,
        planejados=35,
        status=StatusSoberania.TRANSICAO,
        backup="GPS/Galileo (transitorio ate constelacao completa)",
    )
    gps = e.constelacao
    print(f"\n  Sistema: {gps.nome_sistema}")
    print(f"  Satelites: {gps.lancados} lancados / {gps.planejados} planejados")
    print(f"  Cobertura: {gps.cobertura}")
    print(f"  Precisao alvo: {gps.precisao_metros}m")
    print(f"  Status: {gps.status.rotulo}")
    print(f"  Backup estrangeiro: {gps.backup_estrangeiro}")
    print(f"\n  POR QUE GPS SOBERANO:")
    print(f"    - Logistica brasileira nao pode depender de satelite americano.")
    print(f"    - Agricultura de precisao nao pode depender de sinal chines.")
    print(f"    - Drones civica (OpenDrone) precisam de posicionamento proprio.")
    print(f"    - Defesa do territorio exige constelacao nacional.")
    print(f"    - Quem controla o GPS controla ONDE voce chega.")

    # --- RISC-V Hardware ---
    print("\n" + "=" * 70)
    print("[PILAR 2] COMPUTADORES RISC-V -- IA Local, Zero Vendor Lock-in")
    print("=" * 70)

    # Catalogo de hardware soberano
    porta_avancado = e.cadastrar_hardware(
        nome="RepublicaPort Avancado",
        componente=ComponenteStack.SILICIO,
        arquitetura="RISC-V RV64GC (64-bit, vetorial)",
        capacidade_ia_local=True,
        ram_gb=32,
        armazenamento_gb=512,
        consumo_watts=65.0,
        custo_producao_cred=800,
    )
    porta_padrao = e.cadastrar_hardware(
        nome="RepublicaPort Padrao",
        componente=ComponenteStack.SILICIO,
        arquitetura="RISC-V RV64GC (64-bit)",
        capacidade_ia_local=True,
        ram_gb=16,
        armazenamento_gb=256,
        consumo_watts=35.0,
        custo_producao_cred=400,
    )
    porta_essencial = e.cadastrar_hardware(
        nome="RepublicaPort Essencial",
        componente=ComponenteStack.SILICIO,
        arquitetura="RISC-V RV32IMAC (32-bit, baixo consumo)",
        capacidade_ia_local=False,
        ram_gb=4,
        armazenamento_gb=64,
        consumo_watts=5.0,
        custo_producao_cred=150,
    )
    gpu_ia = e.cadastrar_hardware(
        nome="RepublicaAcelerador IA",
        componente=ComponenteStack.IA_LOCAL,
        arquitetura="RISC-V + NPU dedicada",
        capacidade_ia_local=True,
        ram_gb=64,
        armazenamento_gb=1024,
        consumo_watts=120.0,
        custo_producao_cred=1200,
    )

    print(f"\n  Catalogo de Hardware Soberano ({len(e.hardwares)} produtos):")
    for hw in e.hardwares.values():
        ia = "IA-LOCAL" if hw.capacidade_ia_local else "basico"
        print(f"\n    {hw.id}: {hw.nome}")
        print(f"      Arquitetura: {hw.arquitetura}")
        print(f"      RAM: {hw.ram_gb}GB | Storage: {hw.armazenamento_gb}GB")
        print(f"      Consumo: {hw.consumo_watts}W | Custo: {hw.custo_producao_cred}c")
        print(f"      Capacidade: {ia}")
        print(f"      Spec imutavel: {hw.spec_imutavel} | Codigo aberto: {hw.codigo_aberto}")

    print(f"\n  POR QUE RISC-V:")
    print(f"    - ISA ABERTA: ninguem 'possui' a especificacao.")
    print(f"    - Nenhum vendor pode fechar ou alterar o padrao.")
    print(f"    - Modelos de IA rodam LOCAL: sem nuvem, sem Big Tech, sem spyware.")
    print(f"    - Fabricavel em qualquer foundry (TSMC, SMIC, governo brasileiro).")
    print(f"    - Acaba com dependencia de Intel/AMD/ARM/NVIDIA.")

    # --- Manifesto: produtos iguais ---
    print("\n" + "=" * 70)
    print("[PILAR 7] HARDWARE COMMODITIZADO -- Produtos Iguais")
    print("=" * 70)
    print(f"\n{e.manifesto_hardware_igual()}")

    # --- Deteccao de Vendor Lock-in ---
    print("\n" + "=" * 70)
    print("[AUDITORIA] Deteccao de Vendor Lock-in no stack atual")
    print("=" * 70)
    # Simular lock-ins detectados (casos reais)
    e.detectar_lockin(
        ComponenteStack.FIRMWARE, TipoVendorLockIn.DRIVER_FECHADO,
        "Qualcomm", "Modem cellular so funciona com firmware fechado da Qualcomm.", 5)
    e.detectar_lockin(
        ComponenteStack.FIRMWARE, TipoVendorLockIn.BACKDOOR_FIRMWARE,
        "Intel", "Intel ME (Management Engine): processador oculto com acesso total ao sistema.", 5)
    e.detectar_lockin(
        ComponenteStack.GPS, TipoVendorLockIn.FORMATO_INCOMPATIVEL,
        "NAVSTAR (US)", "Formato de sinal GPS proprietario. Sem documentacao completa.", 4)
    e.detectar_lockin(
        ComponenteStack.IA_LOCAL, TipoVendorLockIn.PATENTE_TRUQUEDA,
        "NVIDIA", "CUDA e proprietario. Roda IA so em GPU NVIDIA.", 5)
    e.detectar_lockin(
        ComponenteStack.SILICIO, TipoVendorLockIn.CERTIFICACAO_OBRIGATORIA,
        "ARM", "Licenca ARM cobra royalties por chip fabricado.", 4)
    e.detectar_lockin(
        ComponenteStack.SISTEMA, TipoVendorLockIn.OBSOLESCENCIA_FORCADA,
        "Apple", "iPhone recebe update por ~5 anos depois e obsoleto por design.", 4)

    print(f"\n  {len(e.lockins)} lock-ins detectados ({len(e.lockins_criticos())} criticos):")
    for li in e.lockins_por_severidade():
        flag = "CRITICO" if li.severidade >= 4 else "ALTO"
        print(f"\n    [{flag}] {li.componente.rotulo} -> {li.vendor}")
        print(f"    Tipo: {li.tipo.rotulo}")
        print(f"    Descricao: {li.descricao}")
        print(f"    Acao: {li.acao_recomendada}")

    # --- Sistema de testes ---
    print("\n" + "=" * 70)
    print("[PILAR 4] TESTE E O BASICO DO BASICO")
    print("=" * 70)
    print(f"\n  'Sistemas sao feitos para humanos.'")
    print(f"  'Teste e o basico do basico.'\n")
    # Registrar testes para RepublicaPort Padrao
    e.registrar_teste(TipoTeste.UNITARIO, ComponenteStack.SILICIO, True, "5000 testes unitarios passaram.", participantes_humanos=0)
    e.registrar_teste(TipoTeste.INTEGRACAO, ComponenteStack.SILICIO, True, "Stack completo integrado.", 0)
    e.registrar_teste(TipoTeste.HUMANO_REAL, ComponenteStack.INTERFACE, True, "50 cidadaos testaram por 2 semanas.", 50)
    e.registrar_teste(TipoTeste.HUMANO_DEFICIENTE, ComponenteStack.INTERFACE, True, "10 pessoas cegas/surdas/cadeirantes testaram.", 10)
    e.registrar_teste(TipoTeste.STRESS, ComponenteStack.REDE, True, "Rede suportou 10000 nos offline.", 0)
    e.registrar_teste(TipoTeste.SEGURANCA, ComponenteStack.FIRMWARE, True, "Pen-test por OpenCybersecurityMuralha.", 0)
    # Faltam CAMPO e REGRESSAO
    print(f"\n  Cobertura de testes por componente:")
    for comp in [ComponenteStack.SILICIO, ComponenteStack.INTERFACE, ComponenteStack.REDE]:
        cov = e.cobertura_testes(comp)
        print(f"\n    {cov['componente']}: {cov['pct_cobertura']}% ({cov['mensagem']})")
        if cov["tipos_faltando"]:
            print(f"    Faltando: {', '.join(cov['tipos_faltando'])}")
        print(f"    APROVADO: {'SIM' if cov['aprovado'] else 'NAO -- teste e o basico do basico'}")

    # --- Matriz de Soberania ---
    print("\n" + "=" * 70)
    print("[MATRIZ DE SOBERANIA POR COMPONENTE]")
    print("=" * 70)
    matriz = e.construir_matriz()
    print(f"\n  {'Componente':.<25} {'Status':>12} {'% Soberano':>12} {'Lock-ins':>10}")
    print(f"  {'-'*61}")
    for comp in ComponenteStack:
        m = matriz[comp.id]
        n_locks = sum(1 for li in e.lockins if li.componente == comp)
        print(f"  {comp.rotulo:.<25} {m.status.id:>12} {m.pct_soberano:>11}% {n_locks:>10}")

    # --- Scorecard ---
    print("\n" + "=" * 70)
    print("[SCORECARD DA SOBERANIA TECNOLOGICA]")
    print("=" * 70)
    sc = e.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<30} {v}")

    # --- FILOSOFIA ---
    print("\n" + "=" * 70)
    print("FILOSOFIA -- Soberania Tecnologica = Soberania de Fato")
    print("=" * 70)
    print("""
GPS PROPRIO:
  O Brasil tem territorio continental. Depender do GPS americano
  e DEPENDENCIA ESTRATEGICA. Quem controla o satelite controla
  onde voce chega. Logistica, defesa, agricultura, navegacao,
  drones civica -- tudo depende de posicionamento.
  A Republica constela seus proprios satelites. RepublicaNav.

RISC-V LOCAL:
  RISC-V e ISA aberta. Nenhum vendor pode fechar.
  Modelos de IA rodam LOCAL: sem nuvem, sem Big Tech, sem spyware.
  Seu processador, seus dados, seu poder de computacao.
  Acaba com Intel/AMD/ARM/NVIDIA como pedagios sobre computacao.

REDE CONFIGURADA:
  Local-first. DNS proprio. CRDT offline. Caching distribuido.
  Se a conexao externa cai, a Republica CONTINUA operando.
  A rede nao e servico de empresa. E INFRAESTRUTURA DE ESTADO.

TESTE E O BASICO DO BASICO:
  "Sistemas sao feitos para humanos." Humano testa.
  Sistema nao testado com humano REAL (incluindo deficiente) NAO existe.
  Nao existe "release depois corrige". Teste e pre-requisito.
  Inclui: cego, surdo, tetraplegico, TEA, TDAH, Down.
  Se uma pessoa com deficiencia nao consegue usar, FALHOU.

CODIGO ABERTO RADICAL:
  "Todos tem acesso ao codigo." Sem excecao. Sem premium tier.
  CC0. Sem patente. Sem propriedade intelectual sobre software basico.
  O codigo e da humanidade.

SPEC IMUTAVEL:
  "A especificacao nao pode ser alterada por um vendor."
  RISC-V nao pode ser 'estendido' e fechado.
  HTML nao pode ser 'melhorado' por um browser e trancado.
  O padrao e DA REPUBLICA. Vendors implementam; nao inventam.

HARDWARE COMMODITIZADO:
  "Todos os produtos sao iguais. Muda a marca e as cores."
  O chip e o MESMO. A placa e a MESMA. O sistema e o MESMO.
  O que muda: cor, logo, embalagem. Cosmetica.
  Acaba a elite artificial de 'premium' vs 'basico'.
  Um produto. Para todos. Igual.

A SOBERANIA TECNOLOGICA E A UNICA SOBERANIA REAL:
  Sem GPS proprio, voce nao chega onde quer.
  Sem chip proprio, voce nao computa o que quer.
  Sem rede propria, voce nao comunica o que quer.
  Sem codigo aberto, voce nao confia no que usa.
  Sem teste humano, voce nao sabe se funciona.
  Sem spec imutavel, voce nao controla o futuro.
  Sem hardware igual, voce recria elite.

  A Republica nao e soberana se sua tecnologia nao e.
""")


if __name__ == "__main__":
    _demo()
