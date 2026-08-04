#!/usr/bin/env python3
"""
OpenRepublicColors -- Sistema de Cores da Republica
=====================================================
"Cada cor carrega um principio. Voce ve o verde, sabe: terra.
 Voce ve o preto, sabe: ancestralidade. Nao e decorativo. E CODIGO."

O sistema de cores da Republica NAO e estetica. E SEMIOTICA.
Cada cor tem: hex, RGB, HSL, nome, significado, principio associado,
projeto associado, e regras de combinacao.

COMO USAR:
  - Identidade visual (logos, documentos, UI)
  - Cores de equipes/projetos (cada grupo tem sua cor)
  - Status de auditoria (conforme=verde, banido=vermelho)
  - Niveis de alerta (do monitor constitucional)
  - Codigos de principio (P1-P14 cada um tem cor)
  - Identidade cultural (capoeira, samba, cordel)

A REGRA DE OURO:
  NUNCA usar cores de partido politico como cores da Republica.
  Vermelho PT, Amarelo bolsonarista, Azul tucano -- PROIBIDOS.
  A Republica nao polariza (P9). Suas cores sao NOVAS.
  Nao herdam simbolismo partidario. Herdam TERRA, POVO, LUTA.

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field


# ============================================================================
# 1. DATACLASS DE COR
# ============================================================================

@dataclass(frozen=True)
class CorRepublica:
    """Uma cor do sistema da Republica."""
    id: str                # identificador unico (snake_case)
    nome: str              # nome em portugues ("Verde Republica")
    hex: str               # "#1A5E3F"
    rgb: Tuple[int, int, int]  # (26, 94, 63)
    hsl: Tuple[int, int, int]  # (h, s%, l%) -- matiz, saturacao, luminosidade
    significado: str       # o que a cor COMUNICA
    categoria: str         # "identidade", "principio", "status", "alerta", "cultural", "equipe"
    associacoes: List[str] = field(default_factory=list)  # P1, constituicao, etc.
    # contraste: qual cor de texto usar sobre fundo desta cor
    texto_sobre: str = "branco"  # "branco" ou "preto"

    @property
    def css(self) -> str:
        """CSS pronto pra usar."""
        return f"#{self.hex.lstrip('#').upper()}"

    @property
    def rgb_css(self) -> str:
        return f"rgb({self.rgb[0]}, {self.rgb[1]}, {self.rgb[2]})"

    def descrever(self) -> str:
        return (
            f"{self.nome} ({self.css})\n"
            f"  RGB: {self.rgb} | HSL: {self.hsl}\n"
            f"  Categoria: {self.categoria}\n"
            f"  Significado: {self.significado}\n"
            f"  Associacoes: {', '.join(self.associacoes) or 'nenhuma'}\n"
            f"  Texto sobre: {self.texto_sobre}"
        )


# ============================================================================
# 2. SISTEMA COMPLETO DE CORES
# ============================================================================

def _init_cores() -> Dict[str, CorRepublica]:
    """Catalogo completo de cores da Republica."""
    return {

        # ====================================================================
        # IDENTIDADE CENTRAL (as cores da bandeira da Republica)
        # ====================================================================
        "verde_republica": CorRepublica(
            "verde_republica", "Verde Republica",
            "#1A5E3F", (26, 94, 63), (144, 57, 23),
            "A terra que e de quem cuida. Floresta que protege. Crescimento.",
            "identidade",
            ["P1", "open_agrarian_revolution", "terra"],
        ),
        "azul_povo": CorRepublica(
            "azul_povo", "Azul Povo",
            "#0A2540", (10, 37, 64), (213, 73, 14),
            "A profundidade do povo. O oceano que cerca a nacao. Os dados que sao nossos (P14).",
            "identidade",
            ["P14", "open_data_sovereignty", "open_network", "mar"],
        ),
        "preto_ancestral": CorRepublica(
            "preto_ancestral", "Preto Ancestral",
            "#1A1A1A", (26, 26, 26), (0, 0, 10),
            "Heranca africana. Capoeira. Quilombo. A resistencia que sobreviveu 400 anos.",
            "identidade",
            ["P2", "P7", "capoeira", "antropofagia", "quilombo"],
        ),
        "branco_transparencia": CorRepublica(
            "branco_transparencia", "Branco Transparencia",
            "#F5F5F0", (245, 245, 240), (60, 20, 95),
            "Transparencia radical. O que o Estado faz, o povo ve. Nada escondido.",
            "identidade",
            ["P5", "transparencia", "log_publico"],
            "preto",
        ),
        "vermelho_luta": CorRepublica(
            "vermelho_luta", "Vermelho Luta",
            "#8B1A1A", (139, 26, 26), (0, 69, 32),
            "O sangue de quem lutou. NAO e vermelho de partido. E de resistencia real.",
            "identidade",
            ["resistencia", "luta", "martyr"],
        ),
        "amarelo_conhecimento": CorRepublica(
            "amarelo_conhecimento", "Amarelo Conhecimento",
            "#D4A017", (212, 160, 23), (45, 80, 46),
            "Conhecimento universal. NAO e amarelo bolsonarista. E ouro do saber.",
            "identidade",
            ["P6", "educacao", "saber"],
            "preto",
        ),
        "terra_brasilis": CorRepublica(
            "terra_brasilis", "Terra Brasilis",
            "#8B5E3C", (139, 94, 60), (27, 40, 39),
            "A terra misturada. O caboclo. A miscigenacao que nao e fraqueza -- e forca.",
            "identidade",
            ["miscigenacao", "antropofagia", "caboclo"],
        ),

        # ====================================================================
        # PRINCIPIOS CONSTITUCIONAIS (P1-P14)
        # ====================================================================
        "p1_anti_elitismo": CorRepublica(
            "p1_anti_elitismo", "P1 Anti-Elitismo",
            "#2D6A4F", (45, 106, 79), (152, 41, 30),
            "Verde-esmeralda: ninguem vale mais por cargo. Todos comecam em 1.0.",
            "principio", ["P1"],
        ),
        "p2_autonomia_corporal": CorRepublica(
            "p2_autonomia_corporal", "P2 Autonomia Corporal",
            "#7B2D8B", (123, 45, 139), (292, 51, 36),
            "Violeta escuro: o corpo e teu. Inviolavel. Consentimento continuo.",
            "principio", ["P2"],
        ),
        "p3_trabalho_igual": CorRepublica(
            "p3_trabalho_igual", "P3 Trabalho Igual",
            "#52796F", (82, 121, 111), (165, 19, 40),
            "Verde-musgo: trabalho nao tem dono. Base 1.0 + impacto.",
            "principio", ["P3"],
        ),
        "p4_processo_democratico": CorRepublica(
            "p4_processo_democratico", "P4 Processo Democratico",
            "#3D5A80", (61, 90, 128), (214, 35, 37),
            "Azul-oceano: 1 pessoa = 1 voto. Proposta -> debate -> votacao.",
            "principio", ["P4"],
        ),
        "p5_transparencia_radical": CorRepublica(
            "p5_transparencia_radical", "P5 Transparencia Radical",
            "#E8E8E0", (232, 232, 224), (60, 20, 89),
            "Branco-papel: nada escondido. Log publico. Caixa-preta proibida.",
            "principio", ["P5"], "preto",
        ),
        "p6_acesso_universal": CorRepublica(
            "p6_acesso_universal", "P6 Acesso Universal",
            "#D4A017", (212, 160, 23), (45, 80, 46),
            "Amarelo-ouro: conhecimento para todos. Sem paywall. Sem diploma.",
            "principio", ["P6"], "preto",
        ),
        "p7_seguranca_cultura": CorRepublica(
            "p7_seguranca_cultura", "P7 Seguranca Cultura",
            "#4A4E69", (74, 78, 105), (234, 17, 35),
            "Chumbo-acinzentado: nmap e cultura. Seguranca nao e elite.",
            "principio", ["P7"],
        ),
        "p8_ia_instrumento": CorRepublica(
            "p8_ia_instrumento", "P8 IA Instrumento",
            "#6A4C93", (106, 76, 147), (262, 32, 44),
            "Roxo: a maquina serve. O humano decide. Engagement por furia proibido.",
            "principio", ["P8"],
        ),
        "p9_anti_polarizacao": CorRepublica(
            "p9_anti_polarizacao", "P9 Anti-Polarizacao",
            "#264653", (38, 70, 83), (193, 37, 24),
            "Azul-petroleo: o Estado nao divide. Diversidade = direito. Polarizacao = doenca.",
            "principio", ["P9"],
        ),
        "p10_soberania_aerea": CorRepublica(
            "p10_soberania_aerea", "P10 Soberania Aerea",
            "#2A9D8F", (42, 157, 143), (173, 58, 39),
            "Turquesa: o ceu e de todos. Drone nao vigia, nao mata, nao espia.",
            "principio", ["P10"],
        ),
        "p11_letramento_constituinte": CorRepublica(
            "p11_letramento_constituinte", "P11 Letramento Constituinte",
            "#E76F51", (231, 111, 81), (14, 76, 61),
            "Laranja-terracota: celular nao e requisito pra cidadania. E constituinte.",
            "principio", ["P11"],
        ),
        "p12_defesa_cibernetica": CorRepublica(
            "p12_defesa_cibernetica", "P12 Defesa Cibernetica",
            "#1D3557", (29, 53, 87), (211, 50, 23),
            "Azul-marinho profundo: defesa transparente. Nunca ataque secreto.",
            "principio", ["P12"],
        ),
        "p13_contravigilancia": CorRepublica(
            "p13_contravigilancia", "P13 Contravigilancia",
            "#C77DFF", (199, 125, 255), (273, 100, 74),
            "Lilas vibrante: o cidadao vigia o Estado de volta. Proporcional ao poder.",
            "principio", ["P13"], "preto",
        ),
        "p14_soberania_dados": CorRepublica(
            "p14_soberania_dados", "P14 Soberania Dados",
            "#00B4D8", (0, 180, 216), (191, 100, 42),
            "Ciano: o dado e teu. Quem coletou e custodiante revogavel, nao dono.",
            "principio", ["P14"], "preto",
        ),

        # ====================================================================
        # STATUS DE AUDITORIA CONSTITUCIONAL
        # ====================================================================
        "status_conforme": CorRepublica(
            "status_conforme", "Status: Conforme",
            "#52B788", (82, 183, 136), (150, 38, 52),
            "Verde: conforme com os principios. Tudo certo.",
            "status", ["conforme", "pass"],
        ),
        "status_revisao": CorRepublica(
            "status_revisao", "Status: Revisao",
            "#F4A261", (244, 162, 97), (28, 87, 67),
            "Laranja-claro: precisa revisao. Violacoes menores.",
            "status", ["revisao", "atencao"], "preto",
        ),
        "status_suspenso": CorRepublica(
            "status_suspenso", "Status: Suspenso",
            "#E76F51", (231, 111, 81), (14, 76, 61),
            "Laranja-vermelho: suspenso ate correcao. Violacao maior.",
            "status", ["suspenso", "urgente"],
        ),
        "status_banido": CorRepublica(
            "status_banido", "Status: Banido",
            "#D62828", (214, 40, 40), (0, 69, 50),
            "Vermelho-sangue: BANIDO. Violacao critica. Sistema rejeitado.",
            "status", ["banido", "critico"],
        ),

        # ====================================================================
        # NIVEIS DE ALERTA (do constitutional_monitor)
        # ====================================================================
        "alerta_info": CorRepublica(
            "alerta_info", "Alerta: Info",
            "#48CAE4", (72, 202, 228), (191, 75, 59),
            "Azul-claro: informativo. Evento registrado, sem anomalia.",
            "alerta", ["info", "log"], "preto",
        ),
        "alerta_atencao": CorRepublica(
            "alerta_atencao", "Alerta: Atencao",
            "#FFB703", (255, 183, 3), (43, 100, 50),
            "Amarelo-ouro: atencao. Padrao suspeito, investigar.",
            "alerta", ["atencao"], "preto",
        ),
        "alerta_importante": CorRepublica(
            "alerta_importante", "Alerta: Importante",
            "#FB8500", (251, 133, 0), (32, 100, 49),
            "Laranja-forte: possivel violacao constitucional.",
            "alerta", ["importante"],
        ),
        "alerta_urgente": CorRepublica(
            "alerta_urgente", "Alerta: Urgente",
            "#DC2F02", (220, 47, 2), (13, 98, 44),
            "Vermelho-laranja: violacao provavel. Agir agora.",
            "alerta", ["urgente"],
        ),
        "alerta_critico": CorRepublica(
            "alerta_critico", "Alerta: Critico",
            "#9D0208", (157, 2, 8), (358, 95, 31),
            "Vermelho-escuro: violacao confirmada em tempo real.",
            "alerta", ["critico"],
        ),

        # ====================================================================
        # EQUIPES / PROJETOS
        # ====================================================================
        "equipe_constituicao": CorRepublica(
            "equipe_constituicao", "Equipe Constituicao",
            "#264653", (38, 70, 83), (193, 37, 24),
            "Azul-petroleo: o nucleo. Os 14 principios. O motor.",
            "equipe", ["constituicao", "P1-P14"],
        ),
        "equipe_economia": CorRepublica(
            "equipe_economia", "Equipe Economia",
            "#40916C", (64, 145, 108), (143, 39, 41),
            "Verde-jade: divida, energia, terra. O valor que serve ao povo.",
            "equipe", ["economia", "divida", "energia"],
        ),
        "equipe_acessibilidade": CorRepublica(
            "equipe_acessibilidade", "Equipe Acessibilidade",
            "#7B2CBF", (123, 44, 191), (273, 63, 46),
            "Roxo-vibrante: cego, surdo, tetraplegico. A Republica serve a TODOS.",
            "equipe", ["acessibilidade", "cego", "surdo"],
        ),
        "equipe_voz": CorRepublica(
            "equipe_voz", "Equipe Voz",
            "#F77F00", (247, 127, 0), (31, 100, 48),
            "Laranja-quente: Iara fala. O cidadao manda. A voz que opera.",
            "equipe", ["voz", "iara", "pipeline"], "preto",
        ),
        "equipe_distro": CorRepublica(
            "equipe_distro", "Equipe Distro",
            "#6C757D", (108, 117, 125), (208, 7, 45),
            "Cinza-metal: o chao que roda tudo. Kali + acessibilidade + IA local.",
            "equipe", ["distro", "big_linux"],
        ),

        # ====================================================================
        # VETORES CULTURAIS
        # ====================================================================
        "cultura_cordel": CorRepublica(
            "cultura_cordel", "Cultura: Cordel",
            "#BC6C25", (188, 108, 37), (34, 67, 44),
            "Marrom-ouro: o jornal do povo em rima. Papel envelhecido da bancada.",
            "cultural", ["cordel", "P6"],
        ),
        "cultura_capoeira": CorRepublica(
            "cultura_capoeira", "Cultura: Capoeira",
            "#606C38", (96, 108, 56), (71, 32, 32),
            "Verde-oliva: a resistencia no corpo. Berimbau. Ginga. Pedra bruta.",
            "cultural", ["capoeira", "P7", "P12"],
        ),
        "cultura_samba": CorRepublica(
            "cultura_samba", "Cultura: Samba",
            "#9D4EDD", (157, 78, 221), (273, 68, 59),
            "Roxo-festa: a memoria que o Estado nao apaga. Batucada. Arquivo do povo.",
            "cultural", ["samba", "P5", "P13"],
        ),
        "cultura_antropofagia": CorRepublica(
            "cultura_antropofagia", "Cultura: Antropofagia",
            "#F4A261", (244, 162, 97), (28, 87, 67),
            "Laranja-terra: comer o estrangeiro, cuspir brasileiro. Oswald de Andrade.",
            "cultural", ["antropofagia", "P14"], "preto",
        ),
        "cultura_cinema_novo": CorRepublica(
            "cultura_cinema_novo", "Cultura: Cinema Novo",
            "#1B263B", (27, 38, 59), (218, 37, 17),
            "Azul-noite: a estetica da fome. Mostrar a violencia, nao maquiar.",
            "cultural", ["cinema_novo", "P1"],
        ),
        "cultura_roda": CorRepublica(
            "cultura_roda", "Cultura: Roda",
            "#E0A458", (224, 164, 88), (35, 68, 61),
            "Ambar: a assembleia sem servidor. Boca no ouvido. Quintal.",
            "cultural", ["roda", "P4"], "preto",
        ),
    }


# ============================================================================
# 3. REGRAS DE COMBINACAO (mistura de cores = mistura de significado)
# ============================================================================

@dataclass
class CombinacaoCores:
    """Quando duas cores se combinam, o significado se combina."""
    cor_a: str
    cor_b: str
    resultado: str  # descricao do significado da combinacao
    uso: str        # onde aplicar


def _init_combinacoes() -> List[CombinacaoCores]:
    return [
        CombinacaoCores(
            "verde_republica", "preto_ancestral",
            "Terra + Ancestralidade: a resistencia que brota do chao africano no Brasil.",
            "Identidade do projeto OpenAgrarianRevolution + OpenInclusiveIDE",
        ),
        CombinacaoCores(
            "azul_povo", "branco_transparencia",
            "Dados + Transparencia: o dado do povo, visivel ao povo.",
            "UI do data sovereignty dashboard",
        ),
        CombinacaoCores(
            "preto_ancestral", "vermelho_luta",
            "Ancestralidade + Luta: capoeira em combate. Quilombo armado.",
            "Identidade do OpenCyberDefense (P12)",
        ),
        CombinacaoCores(
            "amarelo_conhecimento", "terra_brasilis",
            "Conhecimento + Miscigenacao: antropofagia pura. Devorar e transformar.",
            "Identidade do manifesto antropofago digital",
        ),
        CombinacaoCores(
            "azul_povo", "preto_ancestral",
            "Dados + Ancestralidade: o dado que pertence ao povo ancestral.",
            "OpenDataSovereignty (P14) -- o dado e da comunidade, nao do extrator",
        ),
        CombinacaoCores(
            "verde_republica", "branco_transparencia",
            "Terra + Transparencia: a terra que e de quem cuida, visivel a todos.",
            "Documentos oficiais da Republica",
        ),
        CombinacaoCores(
            "vermelho_luta", "branco_transparencia",
            "Luta + Transparencia: denunciar com clareza. Sem sigilo, sem sombra.",
            "Alertas do constitutional_monitor (urgente+)",
        ),
        CombinacaoCores(
            "equipe_acessibilidade", "equipe_voz",
            "Acessibilidade + Voz: Iara fala pra quem nao ve. O sistema serve a TODOS.",
            "OpenIara + OpenDigitalGuide integration",
        ),
    ]


# ============================================================================
# 4. SISTEMA DE CORES
# ============================================================================

class RepublicColorSystem:
    """
    Sistema de cores da Republica Aberta.

    Cada cor e CODIGO. Voce ve a cor, sabe o significado.
    """

    # Cores PROIBIDAS (associacao partidaria -- P9)
    CORES_PROIBIDAS = {
        "amarelo_bolsonarista": ("#FFD700", "Amarelo duck associado a bolsonarismo. P9: nao polarizar."),
        "vermelho_pt": ("#E63946", "Vermelho associado ao PT. P9: nao polarizar."),
        "azul_tucano": ("#307FE2", "Azul associado ao PSDB. P9: nao polarizar."),
    }

    def __init__(self) -> None:
        self.cores: Dict[str, CorRepublica] = _init_cores()
        self.combinacoes: List[CombinacaoCores] = _init_combinacoes()

    # -- consulta -----------------------------------------------------------

    def cor(self, cor_id: str) -> Optional[CorRepublica]:
        return self.cores.get(cor_id)

    def por_categoria(self, categoria: str) -> List[CorRepublica]:
        return [c for c in self.cores.values() if c.categoria == categoria]

    def por_associacao(self, chave: str) -> List[CorRepublica]:
        return [c for c in self.cores.values() if chave in c.associacoes]

    def buscar(self, termo: str) -> List[CorRepublica]:
        """Busca por nome, hex, ou significado."""
        t = termo.lower()
        return [
            c for c in self.cores.values()
            if t in c.nome.lower()
            or t in c.hex.lower()
            or t in c.significado.lower()
            or any(t in a.lower() for a in c.associacoes)
        ]

    # -- categorias ---------------------------------------------------------

    def identidade(self) -> List[CorRepublica]:
        return self.por_categoria("identidade")

    def principios(self) -> List[CorRepublica]:
        return self.por_categoria("principio")

    def status(self) -> List[CorRepublica]:
        return self.por_categoria("status")

    def alertas(self) -> List[CorRepublica]:
        return self.por_categoria("alerta")

    def equipes(self) -> List[CorRepublica]:
        return self.por_categoria("equipe")

    def cultura(self) -> List[CorRepublica]:
        return self.por_categoria("cultural")

    # -- combinacao ---------------------------------------------------------

    def combinar(self, cor_a_id: str, cor_b_id: str) -> Optional[str]:
        """Retorna o significado de combinar duas cores."""
        for comb in self.combinacoes:
            if (comb.cor_a == cor_a_id and comb.cor_b == cor_b_id) or \
               (comb.cor_a == cor_b_id and comb.cor_b == cor_a_id):
                return f"{comb.resultado}\nUso: {comb.uso}"
        return None

    def todas_combinacoes(self) -> List[Dict[str, str]]:
        return [
            {"a": c.cor_a, "b": c.cor_b, "resultado": c.resultado, "uso": c.uso}
            for c in self.combinacoes
        ]

    # -- export ---------------------------------------------------------------

    def exportar_css(self) -> str:
        """Gera variaveis CSS para uso em UI/dashboards."""
        linhas = [":root {"]
        for cid, cor in sorted(self.cores.items()):
            linhas.append(f"  --{cid}: {cor.css};")
        linhas.append("}")
        return "\n".join(linhas)

    def exportar_json(self) -> str:
        """Exporta todas as cores como JSON."""
        import json
        data = {}
        for cid, cor in self.cores.items():
            data[cid] = {
                "nome": cor.nome,
                "hex": cor.css,
                "rgb": list(cor.rgb),
                "hsl": list(cor.hsl),
                "significado": cor.significado,
                "categoria": cor.categoria,
                "associacoes": cor.associacoes,
                "texto_sobre": cor.texto_sobre,
            }
        return json.dumps(data, ensure_ascii=False, indent=2)

    # -- paleta visual --------------------------------------------------------

    def paleta_resumo(self) -> str:
        """Resumo visual em texto (para terminal sem cor real)."""
        linhas = []
        cat_atual = ""
        for cor in sorted(self.cores.values(), key=lambda c: (c.categoria, c.nome)):
            if cor.categoria != cat_atual:
                cat_atual = cor.categoria
                linhas.append(f"\n  [{cat_atual.upper()}]")
            linhas.append(
                f"  {cor.css} {cor.nome:<35} RGB{str(cor.rgb):<16} "
                f"{cor.significado[:45]}"
            )
        return "\n".join(linhas)

    # -- scorecard ----------------------------------------------------------

    def scorecard(self) -> Dict[str, Any]:
        return {
            "total_cores": len(self.cores),
            "identidade": len(self.identidade()),
            "principios": len(self.principios()),
            "status": len(self.status()),
            "alertas": len(self.alertas()),
            "equipes": len(self.equipes()),
            "cultura": len(self.cultura()),
            "combinacoes": len(self.combinacoes),
            "cores_proibidas": len(self.CORES_PROIBIDAS),
        }


# ============================================================================
# 5. DEMO
# ============================================================================

def _demo() -> None:
    s = RepublicColorSystem()

    print("=" * 70)
    print("OpenRepublicColors -- Sistema de Cores da Republica")
    print("=" * 70)

    # --- Resumo por categoria ---
    print(f"\n[TOTAL: {len(s.cores)} CORES]")
    print(s.paleta_resumo())

    # --- Detalhe de cores identidade ---
    print("\n\n[CORES DE IDENTIDADE CENTRAL]")
    for cor in s.identidade():
        print(f"\n{cor.descrever()}")

    # --- Princípios em cor ---
    print(f"\n\n[OS {len(s.principios())} PRINCIPIOS EM COR]")
    for cor in s.principios():
        print(f"  {cor.css} {cor.nome:<40} {cor.significado[:50]}")

    # --- Status ---
    print(f"\n\n[STATUS DE AUDITORIA ({len(s.status())})]")
    for cor in s.status():
        print(f"  {cor.css} {cor.nome:<35} {cor.significado}")

    # --- Combinações ---
    print(f"\n\n[COMBINACOES ({len(s.combinacoes)})]")
    for comb in s.todas_combinacoes():
        print(f"\n  {comb['a']} + {comb['b']}")
        print(f"  = {comb['resultado']}")
        print(f"  Uso: {comb['uso']}")

    # --- CSS export ---
    print("\n\n[EXPORT CSS (primeiras 10 linhas)]")
    css = s.exportar_css()
    for linha in css.split("\n")[:12]:
        print(f"  {linha}")

    # --- Cores proibidas ---
    print("\n\n[CORES PROIBIDAS (P9 anti-polarizacao)]")
    for nome, (hex_val, motivo) in s.CORES_PROIBIDAS.items():
        print(f"  {nome}: {motivo}")

    # --- Scorecard ---
    print("\n\n[SCORECARD]")
    sc = s.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<24} {v}")

    # --- Filosofia ---
    print("\n" + "=" * 70)
    print("FILOSOFIA -- Cor e Codigo")
    print("=" * 70)
    print("""
A COR NAO E DECORATIVA. E SEMIOTICA.

  Cada cor da Republica carrega um PRINCIPIO.
  Voce ve o verde, sabe: terra. Quem cuida, guarda.
  Voce ve o preto, sabe: ancestralidade. Capoeira. Quilombo.
  Voce ve o ciano, sabe: dado. Seu. Revogavel.
  Voce ve o lilas, sabe: contravigilancia. O cidadao ve de volta.

  Nao e paleta de designer. E alfabeto visual.
  Quem aprende as cores, aprende a Republica.

AS CORES QUE NAO PODEM:

  Amarelo duck. Vermelho estrela. Azul tucano.
  Essas cores foram CAPTURADAS por partidos.
  Usa-las e polarizar (P9).
  A Republica tem cores PROPRIAS que nao pertencem a tribo nenhuma.

  Verde Republica nao e verde de bandeira partidaria.
  Azul Povo nao e azul de selecao.
  Vermelho Luta nao e vermelho de partido.
  Sao cores que significam TERRA, POVO, LUTA.
  Nao votam. Nao polemizam. Identificam.

A MISTURA:

  Cores combinam como principios combinam.
  Verde + Preto = resistencia ancestral da terra.
  Azul + Branco = dados transparentes do povo.
  Vermelho + Branco = denuncia clara, sem sombra.
  A mistura NAO e estetica. E MENSAGEM.
""")


if __name__ == "__main__":
    _demo()
