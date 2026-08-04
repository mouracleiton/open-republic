#!/usr/bin/env python3
"""
OpenRepublicLayers -- Arquitetura em Camadas da Republica
==========================================================
"Cada camada suporta a de cima. Nenhuma existe sozinha.
 Assim como o corpo: osso, musculo, pele, voz, espirito."

A Republica nao e uma colecao de modulos soltos. E uma PILHA.
Cada camada depende da que esta embaixo. Cada camada alimenta
a que esta em cima.

O modelo OSI define 7 camadas de rede. A Republica tem 10 camadas
de NACAO. Da terra ao espirito. Do silicio ao samba.

AS 10 CAMADAS (de baixo pra cima):

  L0  HARDWARE FISICO       o silicio, o metal, o corpo
  L1  SOBERANIA TECNOLOGICA quem controla o chip, o cabo, o satelite
  L2  INFRAESTRUTURA DIGITAL  a distro, o codigo, os dados
  L3  CONSTITUICAO          os 14 principios, o motor que valida
  L4  SISTEMAS PUBLICOS     energia, saude, economia, educacao
  L5  ACESSIBILIDADE        cego, surdo, tetra, baixa visao
  L6  INTERFACE             voz, Iara, terminal, guia
  L7  CULTURA E IDENTIDADE  cordel, samba, capoeira, cores, alicerce
  L8  RELACOES EXTERNAS     diplomacia, coalizao, fronteira, defesa
  L9  MEMORIA E TRANSMISSAO o que sobrevive se tudo cair

CAMADAS COM VAZIOS (slots que existem mas sem modulo ainda):

  L0: eletronica aberta, fab de chip nacional, reciclagem
  L4: saude publica, transporte, saneamento, habitacao, alimentacao
  L8: diplomacia digital, tratado de nao-agressao cibernetica
  L9: arquivo permanente, cronista comunitario, museum digital

O vazio NAO e falha. E CONVITE. Cada vazio e um projeto futuro.

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field


# ============================================================================
# 1. ENUMS
# ============================================================================

class CamadaRepublica(Enum):
    """As 10 camadas da arquitetura da Republica, de baixo pra cima."""
    L0_HARDWARE = (0, "hardware", "Hardware Fisico: o silicio, o metal, o corpo")
    L1_SOBERANIA = (1, "soberania", "Soberania Tecnologica: quem controla chip, cabo, satelite")
    L2_INFRA_DIGITAL = (2, "infra_digital", "Infraestrutura Digital: distro, codigo, dados")
    L3_CONSTITUICAO = (3, "constituicao", "Constituicao: os 14 principios, o motor que valida")
    L4_SISTEMAS = (4, "sistemas", "Sistemas Publicos: energia, saude, economia, educacao")
    L5_ACESSIBILIDADE = (5, "acessibilidade", "Acessibilidade: cego, surdo, tetra, baixa visao")
    L6_INTERFACE = (6, "interface", "Interface: voz, Iara, terminal, guia digital")
    L7_CULTURA = (7, "cultura", "Cultura e Identidade: cordel, samba, capoeira, cores")
    L8_RELACOES = (8, "relacoes", "Relacoes Externas: diplomacia, coalizao, fronteira")
    L9_MEMORIA = (9, "memoria", "Memoria e Transmissao: o que sobrevive se tudo cair")

    @property
    def numero(self) -> int:
        return self.value[0]

    @property
    def id(self) -> str:
        return self.value[1]

    @property
    def rotulo(self) -> str:
        return self.value[2]


class StatusSlot(Enum):
    """Status de um slot (modulo) numa camada."""
    EXISTENTE = ("existente", "Modulo existe e compilando")
    VAZIO = ("vazio", "Slot definido, modulo ainda nao existe")
    RASCUNHO = ("rascunho", "Modulo existe mas e portugol/nao-compila (deletado)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoDependencia(Enum):
    """Como uma camada depende de outra."""
    OBRIGATORIA = ("obrigatoria", "Sem esta dependencia, nada funciona")
    RECOMENDADA = ("recomendada", "Funciona sem, mas melhor com")
    OPCIONAL = ("opcional", "Independente")

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
class Slot:
    """Um slot (modulo/projeto) numa camada da Republica."""
    id: str                    # identificador (snake_case)
    nome: str                  # nome legivel
    camada: CamadaRepublica
    arquivo: str               # caminho do .py (ou "" se vazio)
    status: StatusSlot
    descricao: str             # o que faz
    populacao_alvo: str = "todos"  # quem serve
    principios: List[str] = field(default_factory=list)  # P1, P14, etc.


@dataclass
class DependenciaCamada:
    """Como uma camada depende de outra."""
    de: CamadaRepublica
    para: CamadaRepublica
    tipo: TipoDependencia
    razao: str


# ============================================================================
# 3. CATALOGO DE SLOTS (existentes + vazios)
# ============================================================================

def _init_slots() -> List[Slot]:
    """Todos os slots da Republica -- existentes e vazios."""
    return [

        # ====================================================================
        # L0 -- HARDWARE FISICO
        # ====================================================================
        Slot("open_hardware_specs", "Specs de Hardware COTS",
             CamadaRepublica.L0_HARDWARE, "core/acessibilidade/open_accessibility_hardware_specs.py",
             StatusSlot.EXISTENTE,
             "Cataloga 12 dispositivos COTS com specs minimas. 45+ produtos em R$."),
        Slot("open_forge_os", "Forge OS (NixOS gaming server)",
             CamadaRepublica.L0_HARDWARE, "",
             StatusSlot.VAZIO,
             "Sistema operacional para Mini PC servidor de games. NixOS + GOW.",
             "gamers, familias"),
        Slot("open_modular_phone", "Smartphone Modular BR",
             CamadaRepublica.L0_HARDWARE, "",
             StatusSlot.VAZIO,
             "Sucessor do N900. RK3588 ARM V1, RISC-V V2. Modulos removiveis.",
             "cidadaos que querem controle do hardware"),
        Slot("open_recyclers_hardware", "Reciclagem de Hardware",
             CamadaRepublica.L0_HARDWARE, "",
             StatusSlot.VAZIO,
             "Desmontagem, reuso de componentes, segundo ciclo de vida.",
             "catadores, meio ambiente"),
        Slot("open_chip_fab", "Fab de Chip Nacional",
             CamadaRepublica.L0_HARDWARE, "",
             StatusSlot.VAZIO,
             "Soberania de silicio. Producao nacional de chip basico (RISC-V).",
             "industria, soberania"),

        # ====================================================================
        # L1 -- SOBERANIA TECNOLOGICA
        # ====================================================================
        Slot("open_sovereign_tech", "Soberania Tecnologica",
             CamadaRepublica.L1_SOBERANIA, "core/constituicao/open_sovereign_tech.py",
             StatusSlot.EXISTENTE,
             "7 pilares: GPS soberano, RISC-V, rede soberana, teste humano, CC0."),
        Slot("open_unified_codebase", "Codebase Unificada",
             CamadaRepublica.L1_SOBERANIA, "core/constituicao/open_unified_codebase.py",
             StatusSlot.EXISTENTE,
             ".py e a UNICA source. Transpilacao automatica. Um canal pra tudo."),
        Slot("open_republica_nav", "RepublicaNav (GPS soberano)",
             CamadaRepublica.L1_SOBERANIA, "",
             StatusSlot.VAZIO,
             "Constelacao de 35 satelites. GPS que nao depende dos EUA.",
             "todos (infraestrutura invisivel)"),
        Slot("open_network", "Rede Soberana",
             CamadaRepublica.L1_SOBERANIA, "",
             StatusSlot.VAZIO,
             "Rede local-first, CRDT, offline-capavel. Nao depende de backbone gringo.",
             "comunidades, regioes remotas"),
        Slot("open_mesh", "Malha Mesh (Meshtastic/Briar)",
             CamadaRepublica.L1_SOBERANIA, "",
             StatusSlot.VAZIO,
             "Comunicacao P2P sem torre. Radio lo-ra + Bluetooth + WiFi mesh.",
             "comunidades isoladas, emergencias"),

        # ====================================================================
        # L2 -- INFRAESTRUTURA DIGITAL
        # ====================================================================
        Slot("open_big_linux", "OpenBigLinux (distro base)",
             CamadaRepublica.L2_INFRA_DIGITAL, "core/distro/open_big_linux.py",
             StatusSlot.EXISTENTE,
             "Kali hardened + acessibilidade + IA local. 7 camadas de distro."),
        Slot("open_data_sovereignty", "Soberania de Dados (P14)",
             CamadaRepublica.L2_INFRA_DIGITAL, "core/constituicao/open_data_sovereignty.py",
             StatusSlot.EXISTENTE,
             "O dado e do cidadao. Custodiante revogavel. 6 direitos.",
             principios=["P14"]),
        Slot("open_local_ai", "IA Local (llama.cpp, whisper.cpp)",
             CamadaRepublica.L2_INFRA_DIGITAL, "",
             StatusSlot.VAZIO,
             "IA que roda no seu hardware. Sem nuvem. Sem vigilancia. Sem Big Tech.",
             "todos"),
        Slot("open_identity", "Identidade Digital Soberana",
             CamadaRepublica.L2_INFRA_DIGITAL, "",
             StatusSlot.VAZIO,
             "Identidade que nao depende de gov.br. Chave local, revogavel, auditavel.",
             "todos"),
        Slot("open_backup", "Backup Comunitario",
             CamadaRepublica.L2_INFRA_DIGITAL, "",
             StatusSlot.VAZIO,
             "Backup distribuido entre vizinhos. Se um cai, outro tem.",
             "comunidades"),

        # ====================================================================
        # L3 -- CONSTITUICAO
        # ====================================================================
        Slot("constitutional_engine", "Motor Constitucional (P1-P14)",
             CamadaRepublica.L3_CONSTITUICAO, "core/constituicao/constitutional_engine.py",
             StatusSlot.EXISTENTE,
             "14 principios data-driven. Valida sistemas. Acima do fundador.",
             principios=["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]),
        Slot("open_anti_polarization", "Anti-Polarizacao (P9)",
             CamadaRepublica.L3_CONSTITUICAO, "core/constituicao/open_anti_polarization.py",
             StatusSlot.EXISTENTE,
             "Estado nao polariza. Gate como WCAG.",
             principios=["P9"]),
        Slot("open_drone", "Soberania Aerea (P10)",
             CamadaRepublica.L3_CONSTITUICAO, "core/constituicao/open_drone.py",
             StatusSlot.EXISTENTE,
             "Drone nao vigia, nao mata, nao espia.",
             principios=["P10"]),
        Slot("open_digital_literacy", "Letramento Constituinte (P11)",
             CamadaRepublica.L3_CONSTITUICAO, "core/constituicao/open_digital_literacy.py",
             StatusSlot.EXISTENTE,
             "Letramento nao e requisito. E constituinte.",
             principios=["P11"]),
        Slot("open_cyber_defense", "Defesa Cibernetica (P12)",
             CamadaRepublica.L3_CONSTITUICAO, "core/constituicao/open_cyber_defense.py",
             StatusSlot.EXISTENTE,
             "Defesa transparente. Catalogo de ameacas Russia/China. 5 NAO.",
             principios=["P12"]),
        Slot("open_citizen_oversight", "Contravigilancia (P13)",
             CamadaRepublica.L3_CONSTITUICAO, "core/constituicao/open_citizen_oversight.py",
             StatusSlot.EXISTENTE,
             "Cidadao vigia Estado. Tiers de transparencia. T1-T5.",
             principios=["P13"]),
        Slot("open_constitutional_monitor", "Monitor em Tempo Real",
             CamadaRepublica.L3_CONSTITUICAO, "core/constituicao/open_constitutional_monitor.py",
             StatusSlot.EXISTENTE,
             "Detecta corrupcao, conflito, hipocrisia enquanto acontece."),
        Slot("open_political_risk_predictor", "Preditor de Risco Politico",
             CamadaRepublica.L3_CONSTITUICAO, "core/constituicao/open_political_risk_predictor.py",
             StatusSlot.EXISTENTE,
             "8 fatores transparentes. Antecipa. Nao condena."),
        Slot("open_political_reliability", "Confiabilidade Politica",
             CamadaRepublica.L3_CONSTITUICAO, "core/constituicao/open_political_reliability.py",
             StatusSlot.EXISTENTE,
             "Score de confiabilidade baseado em 13 indicadores verificaveis."),

        # ====================================================================
        # L4 -- SISTEMAS PUBLICOS
        # ====================================================================
        Slot("open_energy", "Energia Gratuita",
             CamadaRepublica.L4_SISTEMAS, "core/economia/open_energy.py",
             StatusSlot.EXISTENTE,
             "Energia nao e commodity. E direito. Microgrid comunitaria."),
        Slot("open_energy_taxonomy", "Taxonomia Energetica",
             CamadaRepublica.L4_SISTEMAS, "core/economia/open_energy_taxonomy.py",
             StatusSlot.EXISTENTE,
             "10 sistemas energeticos do corpo mapeados pra civilizacao."),
        Slot("open_agrarian_revolution", "Reforma Agraria",
             CamadaRepublica.L4_SISTEMAS, "core/economia/open_agrarian_revolution.py",
             StatusSlot.EXISTENTE,
             "Terra e de quem cuida. Guardiao, nao dono."),
        Slot("open_debt_abolition", "Abolicao da Divida",
             CamadaRepublica.L4_SISTEMAS, "core/economia/open_debt_abolition.py",
             StatusSlot.EXISTENTE,
             "Prova matematica: a divida nunca se paga."),
        # --- VAZIOS L4 ---
        Slot("open_health", "Saude Publica",
             CamadaRepublica.L4_SISTEMAS, "",
             StatusSlot.VAZIO,
             "SUS redesenhado. Atendimento universal. Telemedicina com IA local.",
             "todos"),
        Slot("open_transport", "Transporte Publico",
             CamadaRepublica.L4_SISTEMAS, "",
             StatusSlot.VAZIO,
             "Mobilidade de massa. Onibus, metro, bicicleta. Sem carro obrigatorio.",
             "todos"),
        Slot("open_housing", "Habitação Digna",
             CamadaRepublica.L4_SISTEMAS, "",
             StatusSlot.VAZIO,
             "Moradia como direito. Sem aluguel extorsivo. Sem speculacao.",
             "sem-teto, classe baixa"),
        Slot("open_sanitation", "Saneamento Universal",
             CamadaRepublica.L4_SISTEMAS, "",
             StatusSlot.VAZIO,
             "Agua, esgoto, lixo. O basico que 35 milhoes de brasileiros nao tem.",
             "periferias, rural"),
        Slot("open_food", "Soberania Alimentar",
             CamadaRepublica.L4_SISTEMAS, "",
             StatusSlot.VAZIO,
             "Comida como direito, nao commodity. Agricultura familiar.",
             "todos, foco em inseguranca alimentar"),
        Slot("open_credit", "Credito Sem Juros",
             CamadaRepublica.L4_SISTEMAS, "",
             StatusSlot.VAZIO,
             "Banco publico sem agiotagem. Credito como direito.",
             "pequeno produtor, trabalhador"),
        Slot("open_education_system", "Educacao Nacional",
             CamadaRepublica.L4_SISTEMAS, "",
             StatusSlot.VAZIO,
             "Escola publica redesenhada. Curriculo civico. Sem vestibular extorsivo.",
             "criancas, jovens, adultos"),
        Slot("open_labor_system", "Sistema de Trabalho",
             CamadaRepublica.L4_SISTEMAS, "",
             StatusSlot.VAZIO,
             "Trabalho base 1.0 (P3). 20h-40h/semana. Sem exploracao.",
             "trabalhadores"),

        # ====================================================================
        # L5 -- ACESSIBILIDADE
        # ====================================================================
        Slot("open_inclusive_ide", "IDE Inclusiva",
             CamadaRepublica.L5_ACESSIBILIDADE, "core/acessibilidade/open_inclusive_ide.py",
             StatusSlot.EXISTENTE,
             "IDE pra TODAS as deficiencias. Cego, surdo, tetra, TDAH."),
        Slot("open_inclusive_hardware", "Hardware Acessivel",
             CamadaRepublica.L5_ACESSIBILIDADE, "core/acessibilidade/open_inclusive_hardware.py",
             StatusSlot.EXISTENTE,
             "44 dispositivos acessiveis integrados."),
        Slot("open_inclusive_home", "Casa Inclusiva",
             CamadaRepublica.L5_ACESSIBILIDADE, "core/acessibilidade/open_inclusive_home.py",
             StatusSlot.EXISTENTE,
             "Casa que se adapta a pessoa. Tetra, idoso, cego, autista."),
        Slot("open_inclusive_education", "Educacao Adaptativa",
             CamadaRepublica.L5_ACESSIBILIDADE, "core/acessibilidade/open_inclusive_education.py",
             StatusSlot.EXISTENTE,
             "Plataforma de educacao pra todas as deficiencias."),
        Slot("open_accessibility_shim", "Shim de Acessibilidade",
             CamadaRepublica.L5_ACESSIBILIDADE, "core/acessibilidade/open_accessibility_shim.py",
             StatusSlot.EXISTENTE,
             "Injeta a11y em apps sem suporte. OCR, contraste, caption."),
        Slot("open_auth_access", "Auth Adaptativa",
             CamadaRepublica.L5_ACESSIBILIDADE, "core/acessibilidade/open_auth_access.py",
             StatusSlot.EXISTENTE,
             "Multi-factor por capacidade, nao por deficiencia. evdev."),
        Slot("open_command_reference", "Doc de Comando Acessivel",
             CamadaRepublica.L5_ACESSIBILIDADE, "core/acessibilidade/open_command_reference.py",
             StatusSlot.EXISTENTE,
             "tldr + Vosk + output adaptativo. 'ajuda tar' por voz."),
        Slot("open_haptic_navigation", "Navegacao Tatil",
             CamadaRepublica.L5_ACESSIBILIDADE, "core/acessibilidade/open_haptic_navigation.py",
             StatusSlot.EXISTENTE,
             "Vibracao direcional pra cegos."),
        Slot("open_libras_bridge", "Ponte Libras",
             CamadaRepublica.L5_ACESSIBILIDADE, "core/acessibilidade/open_libras_bridge.py",
             StatusSlot.EXISTENTE,
             "Bidirecional Libras <-> Portugues."),
        Slot("open_sign_language_policy", "Politica de Libras",
             CamadaRepublica.L5_ACESSIBILIDADE, "core/acessibilidade/open_sign_language_policy.py",
             StatusSlot.EXISTENTE,
             "Lingua de sinais como novo ingles."),
        Slot("open_sign_language_universal", "Libras Universal",
             CamadaRepublica.L5_ACESSIBILIDADE, "core/acessibilidade/open_sign_language_universal.py",
             StatusSlot.EXISTENTE,
             "Ponte entre todas as linguas de sinais."),
        Slot("open_universal_caption", "Legendas Universais",
             CamadaRepublica.L5_ACESSIBILIDADE, "core/acessibilidade/open_universal_caption.py",
             StatusSlot.EXISTENTE,
             "Legenda em tempo real pra TODO audio do SO."),
        Slot("open_ambient_sound", "Som Ambiente (cao-guia digital)",
             CamadaRepublica.L5_ACESSIBILIDADE, "core/acessibilidade/open_ambient_sound.py",
             StatusSlot.EXISTENTE,
             "SO ouve o mundo 24/7. Campainha, sirene, bebe chorando."),
        Slot("open_body_camera", "Camera Corporal",
             CamadaRepublica.L5_ACESSIBILIDADE, "core/acessibilidade/open_body_camera.py",
             StatusSlot.EXISTENTE,
             "Smartphone como olhos do cego. Descreve cenas."),
        Slot("open_digital_guide", "Guia Digital",
             CamadaRepublica.L5_ACESSIBILIDADE, "core/acessibilidade/open_digital_guide.py",
             StatusSlot.EXISTENTE,
             "GPS + visao + OCR. Onde estou, como chego, o que tem aqui."),
        Slot("open_digital_dog_guide", "Cao-Guia Digital",
             CamadaRepublica.L5_ACESSIBILIDADE, "core/acessibilidade/open_digital_dog_guide.py",
             StatusSlot.EXISTENTE,
             "5 sistemas: audicao, visao, navegacao, seguranca, vinculo."),
        Slot("open_human_net", "Rede Humana",
             CamadaRepublica.L5_ACESSIBILIDADE, "core/acessibilidade/open_human_net.py",
             StatusSlot.EXISTENTE,
             "Chamar o humano autorizado mais proximo em emergencia."),

        # ====================================================================
        # L6 -- INTERFACE
        # ====================================================================
        Slot("open_iara", "Iara (IA com corpo visual)",
             CamadaRepublica.L6_INTERFACE, "core/voz/open_iara.py",
             StatusSlot.EXISTENTE,
             "IA no terminal. 4 modos: IARA, JARVIS, TUTOR, SILENCIOSO."),
        Slot("open_telefonista", "Telefonista",
             CamadaRepublica.L6_INTERFACE, "core/voz/open_telefonista.py",
             StatusSlot.EXISTENTE,
             "Sistema como conversa humana."),
        Slot("open_voice_pipeline", "Pipeline de Voz",
             CamadaRepublica.L6_INTERFACE, "core/voz/open_voice_pipeline.py",
             StatusSlot.EXISTENTE,
             "9 camadas, <150ms. Latencia IS accessibility."),
        Slot("open_voice_os_control", "Controle de SO por Voz",
             CamadaRepublica.L6_INTERFACE, "core/voz/open_voice_os_control.py",
             StatusSlot.EXISTENTE,
             "50+ comandos. Janelas, arquivos, digitacao, sistema."),
        Slot("open_voice_terminal_bridge", "Ponte Voz-Terminal",
             CamadaRepublica.L6_INTERFACE, "core/voz/open_voice_terminal_bridge.py",
             StatusSlot.EXISTENTE,
             "Voz -> shell e terminal -> voz. Sem bugs. Bloqueia perigos."),
        Slot("open_voice_pentest", "Pentest por Voz",
             CamadaRepublica.L6_INTERFACE, "core/voz/open_voice_pentest.py",
             StatusSlot.EXISTENTE,
             "16 ferramentas de seguranca por comando de voz. 3 gates eticos."),
        Slot("open_clipboard_intelligence", "Clipboard Inteligente",
             CamadaRepublica.L6_INTERFACE, "core/voz/open_clipboard_intelligence.py",
             StatusSlot.EXISTENTE,
             "Clipboard que pensa antes de colar. LLM local. Humano no loop."),
        # --- VAZIOS L6 ---
        Slot("open_tui", "Interface TUI (terminal rico)",
             CamadaRepublica.L6_INTERFACE, "",
             StatusSlot.VAZIO,
             "Interface rica no terminal pra quem nao tem GPU. Acessivel por design."),
        Slot("open_ar_interface", "Interface de Realidade Aumentada",
             CamadaRepublica.L6_INTERFACE, "",
             StatusSlot.VAZIO,
             "AR pra guiar cego, traduzir libras, marcar perigos na rua."),

        # ====================================================================
        # L7 -- CULTURA E IDENTIDADE
        # ====================================================================
        Slot("open_cultural_constitution", "Constituicao Cultural",
             CamadaRepublica.L7_CULTURA, "core/constituicao/open_cultural_constitution.py",
             StatusSlot.EXISTENTE,
             "Alicerce + universais + anti-padroes + cordel + manifesto."),
        Slot("open_republic_colors", "Sistema de Cores",
             CamadaRepublica.L7_CULTURA, "core/constituicao/open_republic_colors.py",
             StatusSlot.EXISTENTE,
             "41 cores semioticas. Cada cor = principio."),
        Slot("open_republic_exporter", "Exporter Universal",
             CamadaRepublica.L7_CULTURA, "core/constituicao/open_republic_exporter.py",
             StatusSlot.EXISTENTE,
             "Exporta tudo num .md. Portatil. Compartilhavel."),
        # --- VAZIOS L7 ---
        Slot("open_cordel_publisher", "Publicadora de Cordel",
             CamadaRepublica.L7_CULTURA, "",
             StatusSlot.VAZIO,
             "Gera cordel em PDF pronto pra imprimir e vender na feira."),
        Slot("open_samba_archive", "Arquivo de Samba",
             CamadaRepublica.L7_CULTURA, "",
             StatusSlot.VAZIO,
             "Samba-enredo que conta a verdade que o Estado omite. Arquivo do povo."),
        Slot("open_capoeira_protocol", "Protocolo Capoeira",
             CamadaRepublica.L7_CULTURA, "",
             StatusSlot.VAZIO,
             "Metodologia de ensino da capoeira como codigo moral praticado."),

        # ====================================================================
        # L8 -- RELACOES EXTERNAS
        # ====================================================================
        # --- TODOS VAZIOS ---
        Slot("open_diplomacy", "Diplomacia Digital",
             CamadaRepublica.L8_RELACOES, "",
             StatusSlot.VAZIO,
             "Tratados P2P entre Republicas. Sem ONU. Sem topo. Rede de pares.",
             principios=["P4"]),
        Slot("open_border_guard", "Guarda de Fronteira Digital",
             CamadaRepublica.L8_RELACOES, "",
             StatusSlot.VAZIO,
             "Detecta agente exogeno. Torneira falsa. Hardware comprometido.",
             principios=["P12", "P13"]),
        Slot("open_coalition", "Coalizao Anti-Guerra-Cibernetica",
             CamadaRepublica.L8_RELACOES, "",
             StatusSlot.VAZIO,
             "Alianca aberta de paises que rejeitam guerra cibernetica (P12).",
             principios=["P12"]),
        Slot("open_refugee_net", "Rede de Refugio",
             CamadaRepublica.L8_RELACOES, "",
             StatusSlot.VAZIO,
             "Cidadao perseguido em outro pas conecta com a Republica. Asilo digital.",
             principios=["P2", "P13"]),

        # ====================================================================
        # L9 -- MEMORIA E TRANSMISSAO
        # ====================================================================
        # --- TODOS VAZIOS ---
        Slot("open_eternal_archive", "Arquivo Eterno",
             CamadaRepublica.L9_MEMORIA, "",
             StatusSlot.VAZIO,
             "O que sobrevive se tudo cair. Gravado em metal, papel, pedra. Anti-apagao."),
        Slot("open_chronicler", "Cronista Comunitario",
             CamadaRepublica.L9_MEMORIA, "",
             StatusSlot.VAZIO,
             "Cada comunidade tem um cronista. Registra o que acontece. Arquivo local."),
        Slot("open_oral_tradition", "Tradição Oral Digital",
             CamadaRepublica.L9_MEMORIA, "",
             StatusSlot.VAZIO,
             "O que o samba lembra, o cordel conta, a roda repete. Em formato digital."),
        Slot("open_failure_protocol", "Protocolo de Falha",
             CamadaRepublica.L9_MEMORIA, "",
             StatusSlot.VAZIO,
             "Se a Republica cair, como RECONSTROI. Manual de reconstrucao gravado em metal.",
             principios=["P1", "P5"]),
    ]


def _init_dependencias() -> List[DependenciaCamada]:
    """Como cada camada depende das outras."""
    return [
        DependenciaCamada(
            CamadaRepublica.L9_MEMORIA, CamadaRepublica.L7_CULTURA,
            TipoDependencia.OBRIGATORIA,
            "A memoria precisa da cultura pra ser transmitida (cordel, samba)."
        ),
        DependenciaCamada(
            CamadaRepublica.L7_CULTURA, CamadaRepublica.L3_CONSTITUICAO,
            TipoDependencia.OBRIGATORIA,
            "A cultura expressa os principios. Sem principios, e so folclore."
        ),
        DependenciaCamada(
            CamadaRepublica.L6_INTERFACE, CamadaRepublica.L2_INFRA_DIGITAL,
            TipoDependencia.OBRIGATORIA,
            "A interface roda na distro. Sem OS, nao ha Iara."
        ),
        DependenciaCamada(
            CamadaRepublica.L5_ACESSIBILIDADE, CamadaRepublica.L6_INTERFACE,
            TipoDependencia.RECOMENDADA,
            "Acessibilidade USA a interface (voz, Iara). Funciona sem, mas melhor com."
        ),
        DependenciaCamada(
            CamadaRepublica.L4_SISTEMAS, CamadaRepublica.L3_CONSTITUICAO,
            TipoDependencia.OBRIGATORIA,
            "Todo sistema publico e validado pelo motor constitucional."
        ),
        DependenciaCamada(
            CamadaRepublica.L3_CONSTITUICAO, CamadaRepublica.L2_INFRA_DIGITAL,
            TipoDependencia.OBRIGATORIA,
            "O motor constitucional roda em codigo. Sem OS, sem engine."
        ),
        DependenciaCamada(
            CamadaRepublica.L2_INFRA_DIGITAL, CamadaRepublica.L1_SOBERANIA,
            TipoDependencia.OBRIGATORIA,
            "A distro roda em hardware. Sem soberania de chip, a distro e refem."
        ),
        DependenciaCamada(
            CamadaRepublica.L1_SOBERANIA, CamadaRepublica.L0_HARDWARE,
            TipoDependencia.OBRIGATORIA,
            "Soberania tecnologica precisa de hardware fisico. Sem silicio, sem soberania."
        ),
        DependenciaCamada(
            CamadaRepublica.L8_RELACOES, CamadaRepublica.L3_CONSTITUICAO,
            TipoDependencia.OBRIGATORIA,
            "Relacoes externas seguem a constituicao. Tratado que viola P e nulo."
        ),
        DependenciaCamada(
            CamadaRepublica.L9_MEMORIA, CamadaRepublica.L2_INFRA_DIGITAL,
            TipoDependencia.OPCIONAL,
            "A memoria pode ser analoga (papel, metal). Digital e bonus."
        ),
    ]


# ============================================================================
# 4. ENGINE
# ============================================================================

class RepublicLayersEngine:
    """
    Mapeia a arquitetura completa da Republica em 10 camadas.

    Mostra o que existe, o que falta, e como tudo se conecta.
    """

    def __init__(self) -> None:
        self.slots: List[Slot] = _init_slots()
        self.dependencias: List[DependenciaCamada] = _init_dependencias()

    # -- consulta por camada -----------------------------------------------

    def camada(self, camada: CamadaRepublica) -> List[Slot]:
        """Todos os slots de uma camada."""
        return [s for s in self.slots if s.camada == camada]

    def existentes_na_camada(self, camada: CamadaRepublica) -> List[Slot]:
        return [s for s in self.camada(camada) if s.status == StatusSlot.EXISTENTE]

    def vazios_na_camada(self, camada: CamadaRepublica) -> List[Slot]:
        return [s for s in self.camada(camada) if s.status == StatusSlot.VAZIO]

    # -- mapa geral ---------------------------------------------------------

    def todas_camadas(self) -> List[Dict[str, Any]]:
        """Mapa de todas as camadas com contagem de existentes/vazios."""
        resultado = []
        for camada in CamadaRepublica:
            slots = self.camada(camada)
            existentes = len(self.existentes_na_camada(camada))
            vazios = len(self.vazios_na_camada(camada))
            resultado.append({
                "camada": f"L{camada.numero}",
                "id": camada.id,
                "rotulo": camada.rotulo,
                "total_slots": len(slots),
                "existentes": existentes,
                "vazios": vazios,
            })
        return resultado

    # -- proximos vazios (o que construir) ---------------------------------

    def proximos_vazios(self) -> List[Slot]:
        """Vazios ordenados por camada (de baixo pra cima). Prioridade L0->L9."""
        return sorted(
            [s for s in self.slots if s.status == StatusSlot.VAZIO],
            key=lambda s: s.camada.numero,
        )

    def vazios_por_camada(self) -> Dict[str, List[Slot]]:
        """Agrupa vazios por camada."""
        result: Dict[str, List[Slot]] = {}
        for slot in self.proximos_vazios():
            key = f"L{slot.camada.numero}_{slot.camada.id}"
            result.setdefault(key, []).append(slot)
        return result

    # -- dependencias -------------------------------------------------------

    def dependencias_de(self, camada: CamadaRepublica) -> List[DependenciaCamada]:
        """O que esta camada precisa."""
        return [d for d in self.dependencias if d.de == camada]

    def quem_depende_de(self, camada: CamadaRepublica) -> List[DependenciaCamada]:
        """Quem precisa desta camada."""
        return [d for d in self.dependencias if d.para == camada]

    # -- metricas -----------------------------------------------------------

    def cobertura(self) -> Dict[str, Any]:
        """Taxa de cobertura da arquitetura."""
        total = len(self.slots)
        existentes = sum(1 for s in self.slots if s.status == StatusSlot.EXISTENTE)
        vazios = sum(1 for s in self.slots if s.status == StatusSlot.VAZIO)
        pct = (existentes / total * 100) if total else 0
        return {
            "total_slots": total,
            "existentes": existentes,
            "vazios": vazios,
            "taxa_cobertura": f"{existentes}/{total} ({pct:.0f}%)",
        }

    def cobertura_por_camada(self) -> Dict[str, str]:
        """Cobertura de cada camada individualmente."""
        result = {}
        for camada in CamadaRepublica:
            slots = self.camada(camada)
            ex = len(self.existentes_na_camada(camada))
            total = len(slots)
            pct = (ex / total * 100) if total else 0
            result[f"L{camada.numero}"] = f"{ex}/{total} ({pct:.0f}%)"
        return result

    def scorecard(self) -> Dict[str, Any]:
        cob = self.cobertura()
        return {
            "camadas_totais": len(list(CamadaRepublica)),
            "slots_totais": cob["total_slots"],
            "slots_existentes": cob["existentes"],
            "slots_vazios": cob["vazios"],
            "taxa_cobertura": cob["taxa_cobertura"],
            "dependencias_mapeadas": len(self.dependencias),
        }


# ============================================================================
# 5. DEMO
# ============================================================================

def _demo() -> None:
    eng = RepublicLayersEngine()

    print("=" * 70)
    print("OpenRepublicLayers -- Arquitetura em 10 Camadas")
    print("=" * 70)

    # --- Mapa de camadas ---
    print(f"\n[MAPA DE CAMADAS (de cima pra baixo)]\n")
    print(f"  {'CAMADA':<8} {'ROTULO':<55} {'EX/VZ':>8}")
    print(f"  {'-'*75}")
    for camada in reversed(list(CamadaRepublica)):
        slots = eng.camada(camada)
        ex = len(eng.existentes_na_camada(camada))
        vz = len(eng.vazios_na_camada(camada))
        print(f"  L{camada.numero} {'(' + camada.id + ')':<8} {camada.rotulo:<50} {ex}/{vz:>3}")

    # --- Cobertura ---
    cob = eng.cobertura()
    print(f"\n[COBERTURA GERAL]\n  {cob['taxa_cobertura']}")
    print(f"  Existentes: {cob['existentes']} | Vazios: {cob['vazios']} | Total: {cob['total_slots']}")

    print("\n[COBERTURA POR CAMADA]")
    for camada_id, pct in eng.cobertura_por_camada().items():
        bar_len = int(int(pct.split("%")[0].split("(")[1]) / 10)
        bar = "#" * bar_len + "." * (10 - bar_len)
        print(f"  {camada_id} [{bar}] {pct}")

    # --- Slots existentes ---
    print("\n\n[SLOTS EXISTENTES]")
    for slot in sorted(eng.slots, key=lambda s: (s.camada.numero, s.id)):
        if slot.status == StatusSlot.EXISTENTE:
            print(f"  [L{slot.camada.numero}] {slot.id:<35} {slot.arquivo}")

    # --- Proximos vazios (convite) ---
    print(f"\n\n[SLOTS VAZIOS -- O QUE FALTA CONSTRUIR ({len(eng.proximos_vazios())})]\n")
    print("  (cada vazio e um CONVITE, nao uma falha)")
    for slot in eng.proximos_vazios():
        print(f"\n  [L{slot.camada.numero}] {slot.nome}")
        print(f"  ID: {slot.id}")
        print(f"  Descricao: {slot.descricao}")
        print(f"  Populacao: {slot.populacao_alvo}")

    # --- Dependencias ---
    print(f"\n\n[DEPENDENCIAS ENTRE CAMADAS ({len(eng.dependencias)})]\n")
    for dep in eng.dependencias:
        print(f"  L{dep.de.numero} -> L{dep.para.numero} [{dep.tipo.id}]")
        print(f"    {dep.razao}")

    # --- Scorecard ---
    print("\n\n[SCORECARD]")
    sc = eng.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<28} {v}")

    # --- Filosofia ---
    print("\n" + "=" * 70)
    print("FILOSOFIA -- A Pilha da Nacao")
    print("=" * 70)
    print("""
O CORPO E A METAFORA:

  L0  Osso        sem osso, nada se sustenta
  L1  Tendao      conecta osso a musculo
  L2  Musculo     move o que o osso sustenta
  L3  Orgao       coracao que bomba sangue (principios)
  L4  Sistema     digestao, respiracao (servicos publicos)
  L5  Sentido     visao, audicao (acessibilidade)
  L6  Voz         fala, grito, canto (interface)
  L7  Expressao   danc,a, arte, identidade (cultura)
  L8  Relacao     abraco, beijo, guerra (externo)
  L9  Alma        o que sobra quando o corpo cai (memoria)

VAZIO NAO E FALHA:

  Cada slot vazio e um CONVITE.
  A arquitetura e COMPLETA. A Republica e INCOMPLETA.
  Completa e o destino. Incompleta e o caminho.

  L0 (hardware) tem 4 vazios de 5. Sem chip, sem silicio.
  L4 (sistemas) tem 8 vazios de 12. Sem saude, sem saneamento.
  L8 (relacoes) tem 4 vazios de 4. Sem diplomacia ainda.
  L9 (memoria) tem 4 vazios de 4. Sem arquivo ainda.

  Onde comecar? DE BAIXO PRA CIMA.
  Sem L0 (hardware), L9 (memoria) e castelo de areia.
  Mas sem L9 (memoria), L0 (hardware) e pedra sem significado.

  Por isso a capoeira comecou no CORPO (L0+L7 junto).
  E por isso a Republica comecou na CONSTITUICAO (L3).
  O osso primeiro. Depois a alma. Depois tudo entre.

CADA CAMADA PROTEGE A OUTRA:

  Se L3 (constituicao) cai, L4 (sistemas) fica sem regras.
  Se L1 (soberania) cai, L2 (distro) fica refem de gringo.
  Se L7 (cultura) cai, L9 (memoria) esquece tudo.

  Por isso a arquitetura e PILHA, nao lista.
  Nenhuma camada e opcional. Todas se sustentam.
""")


if __name__ == "__main__":
    _demo()
