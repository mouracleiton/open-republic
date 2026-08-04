#!/usr/bin/env python3
"""
OpenRecyclersHardware -- L0: Reciclagem de Hardware
=====================================================
Spec de reciclagem, reuso e segundo ciclo de vida de hardware.

O PROBLEMA:
  Brasil descarta 2.1 milhoes de toneladas de lixo eletronico por ano.
  90% vai pra aterro. Ouro, prata, cobre, terras raras perdidos.

A OPORTUNIDADE:
  1 smartphone = 0.03g ouro. 1M smartphones = 30kg ouro = R$ 9M.
  1 desktop descartado = monitor reusavel + RAM reusavel + fonte reusavel.

O MODEL:
  - Desmontagem comunitaria (nao industrial)
  - Triagem por tipo de material
  - Reuso > Reciclagem > Descarte
  - Catador e engenheiro, nao lixo

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field


# ============================================================================
# 1. ENUMS
# ============================================================================

class TipoLixoEletronico(Enum):
    """Categorias de lixo eletronico (baseado na diretiva WEEE)."""
    COMPUTADOR = ("computador", "Computador desktop/tower")
    NOTEBOOK = ("notebook", "Notebook/Ultrabook")
    SMARTPHONE = ("smartphone", "Smartphone/Tablet")
    MONITOR = ("monitor", "Monitor/Display")
    PERIFERICO = ("periferico", "Teclado, mouse, webcam, speaker")
    COMPONENTE = ("componente", "RAM, GPU, CPU, HDD, SSD, placa")
    ELETRODOMESTICO = ("eletro", "TV, microondas, geladeira (placas)")
    CABO = ("cabo", "Cabos, fontes, adaptadores")
    BATERIA = ("bateria", "Baterias (Li-ion, NiMH, Pb)")
    PEQUENO = ("pequeno", "Router, IoT, smartwatch, dongle")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class MaterialRecuperavel(Enum):
    """Materiais recuperaveis e seus valores de mercado (BRL/kg)."""
    OURO = ("ouro", "Ouro (Au)", 350.0)
    PRATA = ("prata", "Prata (Ag)", 3.0)
    COBRE = ("cobre", "Cobre (Cu)", 45.0)
    ALUMINIO = ("aluminio", "Aluminio (Al)", 12.0)
    FERRO = ("ferro", "Ferro/Aco (Fe)", 2.5)
    CHUMBO = ("chumbo", "Chumbo (Pb)", 15.0)
    ESTANHO = ("estanho", "Estanho (Sn)", 120.0)
    PALADIO = ("paladio", "Paladio (Pd)", 250.0)
    VIDRO = ("vidro", "Vidro", 0.5)
    PLASTICO_ABS = ("plastico", "Plastico ABS", 5.0)
    TERRA_RARA = ("terra_rara", "Terras Raras (Nd, Dy)", 80.0)
    SILICIO = ("silicio", "Silicio (Si)", 20.0)
    LITIO = ("litio", "Litio (Li)", 90.0)
    COBALTO = ("cobalto", "Cobalto (Co)", 35.0)

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def valor_brl_kg(self) -> float:
        return self.value[2]


class DestinoComponente(Enum):
    """Destino pos-triagem de um componente ou material."""
    REUSO = ("reuso", "Reuso: componente funciona, reusa direto")
    REFURB = ("refurb", "Refurbishment: repara e reusa")
    RECICLAGEM_QUIMICA = ("quimica", "Reciclagem quimica: extrai material")
    RECICLAGEM_MECANICA = ("mecanica", "Reciclagem mecanica: tritura e separa")
    DESCARTE_SEGURO = ("descarte", "Descarte seguro: contaminante sem valor")
    DOACAO = ("doacao", "Doacao: componente funciona, doa pra escola/ONG")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


# ============================================================================
# 2. DATACLASSES
# ============================================================================

@dataclass(frozen=True)
class TeorMaterial:
    """Teor de material recuperavel por tipo de eletronico (g por unidade)."""
    tipo: TipoLixoEletronico
    material: MaterialRecuperavel
    gramas_por_unidade: float


@dataclass
class ProcessoReciclagem:
    """Um processo de reciclagem."""
    id: str
    nome: str
    descricao: str
    equipamento_necessario: List[str]
    custo_estimado_brl: int
    valor_recuperado_brl: int
    risco_seguranca: str  # "baixo", "medio", "alto"
    perfis_envolvidos: List[str] = field(default_factory=list)


# ============================================================================
# 3. DADOS: TEORES DE MATERIAL
# ============================================================================

def _init_teores() -> List[TeorMaterial]:
    """Teores de material por tipo (fontes: UNIDO, ISO 14001)."""
    return [
        # Smartphone (1 unidade)
        TeorMaterial(TipoLixoEletronico.SMARTPHONE, MaterialRecuperavel.OURO, 0.03),
        TeorMaterial(TipoLixoEletronico.SMARTPHONE, MaterialRecuperavel.PRATA, 0.25),
        TeorMaterial(TipoLixoEletronico.SMARTPHONE, MaterialRecuperavel.COBRE, 15.0),
        TeorMaterial(TipoLixoEletronico.SMARTPHONE, MaterialRecuperavel.COBALTO, 5.5),
        TeorMaterial(TipoLixoEletronico.SMARTPHONE, MaterialRecuperavel.TERRA_RARA, 0.5),
        TeorMaterial(TipoLixoEletronico.SMARTPHONE, MaterialRecuperavel.LITIO, 3.5),
        TeorMaterial(TipoLixoEletronico.SMARTPHONE, MaterialRecuperavel.PLASTICO_ABS, 35.0),
        TeorMaterial(TipoLixoEletronico.SMARTPHONE, MaterialRecuperavel.VIDRO, 40.0),
        # Computador (1 desktop tower)
        TeorMaterial(TipoLixoEletronico.COMPUTADOR, MaterialRecuperavel.OURO, 0.20),
        TeorMaterial(TipoLixoEletronico.COMPUTADOR, MaterialRecuperavel.PRATA, 1.0),
        TeorMaterial(TipoLixoEletronico.COMPUTADOR, MaterialRecuperavel.COBRE, 500.0),
        TeorMaterial(TipoLixoEletronico.COMPUTADOR, MaterialRecuperavel.ALUMINIO, 3000.0),
        TeorMaterial(TipoLixoEletronico.COMPUTADOR, MaterialRecuperavel.FERRO, 5000.0),
        TeorMaterial(TipoLixoEletronico.COMPUTADOR, MaterialRecuperavel.PLASTICO_ABS, 1500.0),
        # Notebook
        TeorMaterial(TipoLixoEletronico.NOTEBOOK, MaterialRecuperavel.OURO, 0.10),
        TeorMaterial(TipoLixoEletronico.NOTEBOOK, MaterialRecuperavel.PRATA, 0.5),
        TeorMaterial(TipoLixoEletronico.NOTEBOOK, MaterialRecuperavel.COBRE, 100.0),
        TeorMaterial(TipoLixoEletronico.NOTEBOOK, MaterialRecuperavel.ALUMINIO, 500.0),
        TeorMaterial(TipoLixoEletronico.NOTEBOOK, MaterialRecuperavel.LITIO, 50.0),
        # Monitor
        TeorMaterial(TipoLixoEletronico.MONITOR, MaterialRecuperavel.OURO, 0.05),
        TeorMaterial(TipoLixoEletronico.MONITOR, MaterialRecuperavel.COBRE, 200.0),
        TeorMaterial(TipoLixoEletronico.MONITOR, MaterialRecuperavel.VIDRO, 2000.0),
        TeorMaterial(TipoLixoEletronico.MONITOR, MaterialRecuperavel.ALUMINIO, 800.0),
        TeorMaterial(TipoLixoEletronico.MONITOR, MaterialRecuperavel.PLASTICO_ABS, 1000.0),
        # Bateria Li-ion (1 smartphone)
        TeorMaterial(TipoLixoEletronico.BATERIA, MaterialRecuperavel.LITIO, 2.0),
        TeorMaterial(TipoLixoEletronico.BATERIA, MaterialRecuperavel.COBALTO, 4.0),
        TeorMaterial(TipoLixoEletronico.BATERIA, MaterialRecuperavel.COBRE, 2.0),
        TeorMaterial(TipoLixoEletronico.BATERIA, MaterialRecuperavel.ALUMINIO, 5.0),
        # Placa (1 motherboard)
        TeorMaterial(TipoLixoEletronico.COMPONENTE, MaterialRecuperavel.OURO, 0.15),
        TeorMaterial(TipoLixoEletronico.COMPONENTE, MaterialRecuperavel.PRATA, 0.8),
        TeorMaterial(TipoLixoEletronico.COMPONENTE, MaterialRecuperavel.COBRE, 150.0),
        TeorMaterial(TipoLixoEletronico.COMPONENTE, MaterialRecuperavel.PALADIO, 0.02),
        TeorMaterial(TipoLixoEletronico.COMPONENTE, MaterialRecuperavel.ESTANHO, 20.0),
        TeorMaterial(TipoLixoEletronico.COMPONENTE, MaterialRecuperavel.CHUMBO, 50.0),
        # Cabos (1kg)
        TeorMaterial(TipoLixoEletronico.CABO, MaterialRecuperavel.COBRE, 400.0),
        TeorMaterial(TipoLixoEletronico.CABO, MaterialRecuperavel.PLASTICO_ABS, 400.0),
    ]


def _init_processos() -> List[ProcessoReciclagem]:
    return [
        ProcessoReciclagem(
            "triagem_manual", "Triagem Manual",
            "Desmontagem por tipo. Separar funcionais de danificados. "
            "Sem quimica. So mao de obra e chave de fenda.",
            ["Chave Phillips/Torx", "Banco de trabalho", "Caixas separadoras",
             "Luvas", "Oculos de seguranca"],
            0, 500,
            "baixo",
            ["Catador treinado", "Coordenador"],
        ),
        ProcessoReciclagem(
            "teste_reuso", "Teste de Reuso",
            "Testar cada componente: RAM, SSD, GPU, monitor, teclado. "
            "Funciona? Reusa. Nao funciona? Recicla.",
            ["Fonte ATX tester", "Motherboard test card", "Multimetro",
             "Cabo HDMI/DP", "PC de teste"],
            50, 2000,
            "baixo",
            ["Tecnico de hardware"],
        ),
        ProcessoReciclagem(
            "extracao_ouro_basica", "Extracao de Ouro (Aqua Regia)",
            "Dissolucao de placa em acido nitrico+cloridrico. "
            "Recupera ouro. PERIGOSO. Requer extrator e EPI.",
            ["Capela de exaustao", "Becker de vidro", "Acido nitrico",
             "Acido cloridrico", "EPI completo", "Neutralizador"],
            300, 5000,
            "alto",
            ["Quimico", "Tecnico de seguranca"],
        ),
        ProcessoReciclagem(
            "refurb_monitor", "Refurb de Monitor",
            "Trocar capacitores inchados, limpar, calibrar. "
            "Monitor morto volta a funcionar.",
            ["Ferro de solda", "Capacitores 1000uF/16V", "Multimetro",
             "Alcool isopropilico", "Chave de fenda"],
            20, 300,
            "medio",
            ["Tecnico de eletronica"],
        ),
        ProcessoReciclagem(
            "reciclagem_bateria", "Reciclagem de Bateria Li-ion",
            "Descarga segura, desmontagem em atmosfera inerte, "
            "separacao Li/Co/Cu. INCENDIO se mal feita.",
            ["Caixa de areia", "Balde com salmoura", "Luvas nitrilo",
             "Pinceis", "Balanca", "Recipiente metalico"],
            100, 800,
            "alto",
            ["Tecnico especializado"],
        ),
        ProcessoReciclagem(
            "doacao_escola", "Doacao para Escola",
            "Desktop refurb doado para escola publica. "
            "Linux leve. Hardware de 10 anos funciona.",
            ["Linux leve (AntiX/Puppy)", "Limpeza", "Teste de estabilidade"],
            0, 0,
            "baixo",
            ["Professor de TI", "Aluno estagiario"],
        ),
    ]


# ============================================================================
# 4. SPEC DO SISTEMA DE RECICLAGEM
# ============================================================================

class RecyclersHardware:
    """
    Spec do sistema de reciclagem comunitaria de hardware.

    Reuso > Reciclagem > Descarte.
    Catador e engenheiro, nao lixo.
    """

    NOME = "OpenRecyclers"
    VERSAO = "0.1.0-spec"

    def __init__(self) -> None:
        self.teores: List[TeorMaterial] = _init_teores()
        self.processos: List[ProcessoReciclagem] = _init_processos()

    # -- valor por tipo ----------------------------------------------------

    def valor_por_tipo(self, tipo: TipoLixoEletronico, qtd: int = 1) -> Dict[str, Any]:
        """Calcula valor recuperavel de N unidades de um tipo."""
        teores_tipo = [t for t in self.teores if t.tipo == tipo]
        detalhe = {}
        total = 0.0
        for t in teores_tipo:
            gramas = t.gramas_por_unidade * qtd
            kg = gramas / 1000
            valor = kg * t.material.valor_brl_kg
            detalhe[t.material.id] = {
                "material": t.material.rotulo,
                "gramas": round(gramas, 2),
                "valor_brl": round(valor, 2),
            }
            total += valor
        return {
            "tipo": tipo.id,
            "quantidade": qtd,
            "valor_total_brl": round(total, 2),
            "detalhe": detalhe,
        }

    def valor_lote(self, lote: Dict[TipoLixoEletronico, int]) -> Dict[str, Any]:
        """Calcula valor de um lote misto de lixo eletronico."""
        total = 0.0
        por_tipo = {}
        for tipo, qtd in lote.items():
            r = self.valor_por_tipo(tipo, qtd)
            por_tipo[tipo.id] = r["valor_total_brl"]
            total += r["valor_total_brl"]
        return {
            "valor_total_brl": round(total, 2),
            "por_tipo": por_tipo,
        }

    # -- fluxo ---------------------------------------------------------------

    def fluxo_processamento(self) -> List[Dict[str, str]]:
        """Fluxo de processamento de lixo eletronico."""
        return [
            {"passo": "1", "acao": "Coleta", "desc": "Ponto de coleta comunitario. Catador recebe por kg."},
            {"passo": "2", "acao": "Triagem", "desc": "Separar por tipo. Funcional vs danificado."},
            {"passo": "3", "acao": "Teste", "desc": "Testar funcionais. RAM, SSD, monitor, fonte."},
            {"passo": "4", "acao": "Reuso", "desc": "Funcionais -> doacao, refurb, venda."},
            {"passo": "5", "acao": "Desmontagem", "desc": "Danificados -> desmontar por material."},
            {"passo": "6", "acao": "Extracao", "desc": "Extrair metais preciosos. Ouro, prata, paladio."},
            {"passo": "7", "acao": "Separacao", "desc": "Cobre, aluminio, plastico, vidro."},
            {"passo": "8", "acao": "Venda", "desc": "Material recuperado vendido para indstria."},
        ]

    # -- catalogos -----------------------------------------------------------

    def todos_processos(self) -> List[Dict[str, Any]]:
        return [
            {
                "id": p.id,
                "nome": p.nome,
                "custo_brl": p.custo_estimado_brl,
                "valor_brl": p.valor_recuperado_brl,
                "lucro_brl": p.valor_recuperado_brl - p.custo_estimado_brl,
                "risco": p.risco_seguranca,
                "equipamento": p.equipamento_necessario,
            }
            for p in self.processos
        ]

    # -- scorecard ----------------------------------------------------------

    def scorecard(self) -> Dict[str, Any]:
        return {
            "sistema": self.NOME,
            "versao": self.VERSAO,
            "tipos_lixo_catalogados": len(list(TipoLixoEletronico)),
            "materiais_preciosos": len(list(MaterialRecuperavel)),
            "processos": len(self.processos),
            "principio": "Reuso > Reciclagem > Descarte",
        }


# ============================================================================
# 5. DEMO
# ============================================================================

def _demo() -> None:
    rec = RecyclersHardware()

    print("=" * 70)
    print(f"{rec.NOME} v{rec.VERSAO} -- Reciclagem de Hardware")
    print("=" * 70)

    # --- Valor de 1 smartphone ---
    print("\n[VALOR DE 1 SMARTPHONE RECICLADO]\n")
    v = rec.valor_por_tipo(TipoLixoEletronico.SMARTPHONE, 1)
    print(f"  Valor total: R$ {v['valor_total_brl']}")
    for mat_id, d in sorted(v["detalhe"].items(), key=lambda x: x[1]["valor_brl"], reverse=True):
        print(f"    {d['material']:<20} {d['gramas']:>8.3f}g = R$ {d['valor_brl']:>7.2f}")

    # --- Valor de 1000 smartphones ---
    print("\n\n[VALOR DE 1.000 SMARTPHONES RECICLADOS]\n")
    v = rec.valor_por_tipo(TipoLixoEletronico.SMARTPHONE, 1000)
    print(f"  Valor total: R$ {v['valor_total_brl']:,.2f}")

    # --- Valor de 1 desktop ---
    print("\n\n[VALOR DE 1 DESKTOP RECICLADO]\n")
    v = rec.valor_por_tipo(TipoLixoEletronico.COMPUTADOR, 1)
    print(f"  Valor total: R$ {v['valor_total_brl']}")
    for mat_id, d in sorted(v["detalhe"].items(), key=lambda x: x[1]["valor_brl"], reverse=True):
        print(f"    {d['material']:<20} {d['gramas']:>8.1f}g = R$ {d['valor_brl']:>7.2f}")

    # --- Lote comunitario ---
    print("\n\n[LOTE COMUNITARIO (100 smartphones + 50 desktops + 200 baterias)]\n")
    lote = {
        TipoLixoEletronico.SMARTPHONE: 100,
        TipoLixoEletronico.COMPUTADOR: 50,
        TipoLixoEletronico.BATERIA: 200,
    }
    r = rec.valor_lote(lote)
    print(f"  Valor total: R$ {r['valor_total_brl']:,.2f}")
    for tipo, val in r["por_tipo"].items():
        print(f"    {tipo:<15} R$ {val:,.2f}")

    # --- Fluxo ---
    print("\n\n[FLUXO DE PROCESSAMENTO]\n")
    for passo in rec.fluxo_processamento():
        desc = passo.get("desc", passo.get("destino", ""))
        print(f"  Passo {passo['passo']}: {passo['acao']}")
        print(f"    {desc}")

    # --- Processos ---
    print(f"\n\n[PROCESSOS DE RECICLAGEM ({len(rec.processos)})]\n")
    for p in rec.todos_processos():
        print(f"  [{p['id']}] {p['nome']}")
        print(f"    Custo: R$ {p['custo_brl']} | Valor: R$ {p['valor_brl']} | "
              f"Lucro: R$ {p['lucro_brl']} | Risco: {p['risco']}")

    # --- Materiais ---
    print(f"\n\n[MATERIAIS RECUPERAVEIS ({len(list(MaterialRecuperavel))})]\n")
    print(f"  {'MATERIAL':<20} {'VALOR (R$/kg)':>15}")
    print(f"  {'-'*40}")
    for mat in MaterialRecuperavel:
        print(f"  {mat.rotulo:<20} R$ {mat.valor_brl_kg:>10.2f}")

    # --- Scorecard ---
    print("\n\n[SCORECARD]")
    sc = rec.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<28} {v}")


if __name__ == "__main__":
    _demo()
