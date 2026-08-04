#!/usr/bin/env python3
"""
OpenCyberDefense -- P12: Defesa Cibernetica Transparente
=========================================================
"A Republica nao tem exercito secreto. Tem cidadaos armados de nmap."

TESE (atualizado 2025):
  Russia e China mantêm e expandiram exercitos cibernéticos por 4 vias (2024-2025):
  1. Cooptacao do cibercrime (FSB/GRU continua usando REvil, Conti remanescentes)
  2. Recrutamento universitario e "esquadrões científicos" (China intensificou competições)
  3. Hacktivismo patriotico e grupos de fachada (Killnet, NoName057(16), Volt Typhoon proxies)
  4. Terceirizacao via empresas privadas (i-Soon leak 2024 confirmou escala; novos contractors)

  Atividades 2024/2025: Volt Typhoon e Salt Typhoon continuam pre-posicionamento em infra crítica
  (energia, telecom, água). Novos APTs chineses (UNC5221, Storm-1849, Flax Typhoon) focam em
  living-off-the-land, supply-chain e persistência longa. Russia intensificou hybrid warfare
  (destruição + desinformação).

  A Republica responde DIFERENTE. Nao replica o modelo ofensivo.
  Se a Republica criar um "exercito cibernetico secreto", vira Russia com
  bandeira verde-amarela. A doenca com outro nome ainda e doenca.

A RESPOSTA DA REPUBLICA (P12):

  Em vez de exercito secreto, CULTURA DEFENSIVA DE MASSA.
  Em vez de cooptar criminosos, ERRADICAR cibercrime (P1: miseria=crime).
  Em vez de recrutar universitarios pra guerra, ENSINAR seguranca a TODOS.
  Em vez de grupos de fachada, TRANSPARENCIA RADICAL (P5).
  Em vez de terceirizar ataques, AUDITAR infraestrutura publica.

O MODELO DE AMEACA (atualizado 2025):

  O motor cataloga as 4 doutrinas ofensivas inimigas + novos APTs reportados em 2024/2025
  (Volt Typhoon persistente, Salt Typhoon em telecom, UNC5221, Storm-1849, Flax Typhoon,
  NoName057(16)). Conhecer o inimigo nao e copiar o inimigo.

  | Doutrina             | Russia                          | China                              |
  |----------------------|---------------------------------|------------------------------------|
  | Cibercrime           | FSB/GRU cooptam (REvil remnants)| Menos tolerante, mas contractors   |
  | Universidades        | Esquadrões científicos          | Competicoes + programas estatais   |
  | Hacktivismo          | Killnet, NoName057(16), Cyber Army | Honker Union, proxies Volt Typhoon |
  | Terceirizacao        | Empresas criminosas             | i-Soon (leak 2024), novos firms    |
  | Foco 2024/2025       | Hybrid (DDoS + destruição física + desinfo) | Pre-posicionamento em OT, living-off-land, supply-chain |

  A Republica conhece tudo isso. Mas a resposta NAO e contra-ataque ofensivo.

O QUE A REPUBLICA PROIBE (5 NAO):

  1. NAO COOPTA: nenhum cibercriminoso e recrutado. Cadeia ou recuperacao.
  2. NAO MILITARIZA: universitarios aprendem DEFESA, nao desenvolvem malware.
  3. NAO FACHADA: nenhum grupo "civil" recebe direcionamento secreto do Estado.
  4. NAO OFENSIVA: a Republica nao ataca primeiro. Defender-se, sim.
  5. NAO SECRETA: toda operacao cibernetica e publica e auditavel (P5).

O QUE A REPUBLICA FAZ (5 SIM):

  1. CULTURA DE MASSA: nmap, wireshark, metasploit em toda escola (P7).
  2. DEFESA COMUNITARIA: cidadaos auditam infraestrutura local.
  3. MURALHA: IDS/IPS em toda fronteira digital da Republica.
  4. RESPOSTA PROPORCIONAL: se atacada, responde com isolamento + sanção, nao arma.
  5. COALIZAO ABERTA: alianca com paises que rejeitam guerra cibernetica.

PRINCIPIO CONSTITUCIONAL (P12):

  A Republica mantem defesa cibernetica TRANSPARENTE e DEFENSIVA.
  Nenhum sistema de ataque ofensivo secreto e permitido.
  Todo cidadao e treinado em seguranca digital como CULTURA (P7).
  A Republica nao coopta criminosos, nao militariza civis,
  nao financia grupos de fachada, nao terceiriza operacoes ofensivas.

Constituicao: P1, P4, P5, P7, P8, P9, P12.

Author: OpenRepublic Team (atualizado 2025 com dados de relatorios CISA/Microsoft/Mandiant)
"""

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime


# ============================================================================
# 1. ENUMS -- MODELO DE AMEACA (o que inimigos fazem)
# ============================================================================

class DoutrinaOfensiva(Enum):
    """As 4 doutrinas ofensivas usadas por Estados adversarios."""
    COOPTACAO_CRIME = ("crime", "Cooptacao do cibercrime: hacker preso vira Estado ou preso")
    RECRUTAMENTO_UNIV = ("universidades", "Recrutamento universitario: esquadrões/competicoes")
    HACKTIVISMO_PATRIOTICO = ("hacktivismo", "Hacktivismo patriotico: grupos civis de fachada")
    TERCEIRIZACAO = ("terceirizacao", "Terceirizacao: empresas privadas executam ataques")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class ModeloAdversario(Enum):
    """Modelos de Estado adversario na guerra cibernetica."""
    RUSSIA = ("russia", "Russia: tolerancia com crime local, DDoS, ransom, caos, hybrid warfare 2024/25")
    CHINA = ("china", "China: pre-posicionamento, espionagem industrial, terceirizacao, living-off-land (2024/25)")
    OUTRO_ESTADO = ("outro", "Outro Estado-nação com capacidade cibernetica")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoAmeaca(Enum):
    """Tipos de ameaca cibernetica que a Republica enfrenta."""
    DDoS = ("ddos", "Negação de servico distribuída (torna serviço indisponível)")
    RANSOMWARE = ("ransom", "Ransomware: criptografa dados e exige resgate")
    ESPIONAGEM = ("espionagem", "Espionagem: roubo de dados/classificados")
    SABOTAGEM = ("sabotagem", "Sabotagem: dano a infraestrutura física via rede")
    DESINFORMACAO = ("desinformacao", "Desinformação: manipulação de informação em massa")
    PRE_POSICIONAMENTO = ("prepos", "Pre-posicionamento: infiltrar-se ANTES do conflito")
    SUPPLY_CHAIN = ("supply", "Ataque a cadeia de suprimentos: comprometer fornecedor")
    ZERO_DAY = ("zeroday", "Exploração de vulnerabilidade desconhecida (0-day)")
    LIVING_OFF_THE_LAND = ("lotl", "Living-off-the-land: uso de ferramentas nativas do SO para persistencia")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


# ============================================================================
# 2. ENUMS -- RESPOSTA DA REPUBLICA (o que ela FAZ)
# ============================================================================

class PilarDefesaRepublica(Enum):
    """Os 5 pilares da defesa cibernetica da Republica."""
    CULTURA_MASSA = ("cultura", "Cultura de massa: nmap/wireshark em toda escola (P7)")
    DEFESA_COMUNITARIA = ("comunitaria", "Defesa comunitaria: cidadaos auditam infra local")
    MURALHA = ("muralha", "Muralha: IDS/IPS em toda fronteira digital")
    RESPOSTA_PROPORCIONAL = ("proporcional", "Resposta proporcional: isolamento + sancao")
    COALIZAO_ABERTA = ("coalizao", "Coalizao aberta: alianca contra guerra cibernetica")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class ProibicaoP12(Enum):
    """Os 5 NAO da defesa cibernetica republicana."""
    NAO_COOPTA = ("nao_coopta", "NAO coopta cibercriminosos")
    NAO_MILITARIZA = ("nao_militariza", "NAO militariza universitarios para guerra")
    NAO_FACHADA = ("nao_fachada", "NAO financia grupos civis de fachada")
    NAO_OFENSIVA = ("nao_ofensiva", "NAO ataca primeiro (so defesa)")
    NAO_SECRETA = ("nao_secreta", "NAO ha operacoes secretas (transparencia P5)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class StatusDefesa(Enum):
    """Status da postura de defesa de um sistema."""
    INDEFESO = ("indefeso", "Sistema sem nenhuma protecao")
    BASICO = ("basico", "Protecao basica (firewall padrao)")
    DEFENDIDO = ("defendido", "Defesa adequada + monitoramento")
    FORTIFICADO = ("fortificado", "Fortificado: IDS + audit + resposta automatizada")
    CULTURA = ("cultura", "Maximo: cidadaos treinados + cultura de seguranca (P7)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


# ============================================================================
# 3. DATACLASSES
# ============================================================================

@dataclass
class AmeacaCatalogada:
    """Uma ameaca cibernetica catalogada (modelagem de inimigo)."""
    tipo: TipoAmeaca
    adversario: ModeloAdversario
    doutrina: DoutrinaOfensiva
    nome_grupo: str           # ex: "Volt Typhoon", "Salt Typhoon", "UNC5221"
    descricao: str
    alvo_tipico: str
    mitlagao_republicana: str  # como a Republica se defende disso
    gravidade: int = 3         # 1-5
    ano_referencia: str = "2024/2025"  # novo campo para rastrear atualizacoes


@dataclass
class SistemaDefensivo:
    """Um sistema da Republica avaliado quanto a postura defensiva."""
    id: str
    nome: str
    infraestrutura_critica: bool = False  # agua, energia, transporte, telecom
    # pilares de defesa implementados
    tem_firewall: bool = False
    tem_ids: bool = False           # intrusion detection
    tem_monitoramento: bool = False
    tem_resposta_auto: bool = False  # resposta automatizada
    tem_audit_publico: bool = False  # logs publicos (P5)
    cidadaos_treinados: bool = False # cultura de seguranca (P7)
    # proibicoes P12: este sistema viola alguma?
    coopta_criminosos: bool = False
    militariza_civis: bool = False
    financia_fachada: bool = False
    e_ofensivo: bool = False         # ataca primeiro?
    e_secreto: bool = False          # operacao secreta?
    status: Optional[StatusDefesa] = None


# ============================================================================
# 4. CATALOGO DE AMEACAS (atualizado com dados 2024/2025)
# ============================================================================

def _init_catalogo_ameacas() -> List[AmeacaCatalogada]:
    """Cataloga as ameacas reais (incluindo relatorios 2024/2025) para que a Republica saiba o que enfrenta."""
    return [
        AmeacaCatalogada(
            tipo=TipoAmeaca.PRE_POSICIONAMENTO,
            adversario=ModeloAdversario.CHINA,
            doutrina=DoutrinaOfensiva.TERCEIRIZACAO,
            nome_grupo="Volt Typhoon (APT41 proxies)",
            descricao="Campanha chinesa de pre-posicionamento em infraestrutura critica (energia, agua, telecom). "
                      "Continua ativa em 2024/2025 com foco em living-off-the-land e persistencia longa. "
                      "Relatorios Microsoft, CISA e Mandiant confirmam expansao.",
            alvo_tipico="Sistemas OT/SCADA, redes elétricas, tratamento de água, telecom nos EUA e aliados",
            mitlagao_republicana="Segmentacao rigorosa OT/IT. Air-gapping onde possivel. Monitoramento contínuo "
                                 "de comandos anormais. Auditoria publica de logs (P5). Cultura de detecção "
                                 "por cidadaos treinados (P7). Zero-trust em toda infra critica.",
            gravidade=5,
            ano_referencia="2024/2025",
        ),
        AmeacaCatalogada(
            tipo=TipoAmeaca.ESPIONAGEM,
            adversario=ModeloAdversario.CHINA,
            doutrina=DoutrinaOfensiva.TERCEIRIZACAO,
            nome_grupo="Salt Typhoon",
            descricao="Operacao chinesa de invasao a operadoras de telecomunicações para acesso a comunicacoes "
                      "governamentais e de alto nivel. Ativa em 2024 com comprometimento de múltiplas carriers "
                      "nos EUA. Foco em interceptacao e persistencia.",
            alvo_tipico="Operadoras de telecom, backbones, provedores de internet, satelites",
            mitlagao_republicana="Criptografia end-to-end obrigatoria (P8). Rede soberana OpenNetwork com "
                                 "controles de soberania. Auditoria publica e ausencia de backdoors. "
                                 "Monitoramento de anomalias em trafego de controle.",
            gravidade=5,
            ano_referencia="2024",
        ),
        AmeacaCatalogada(
            tipo=TipoAmeaca.LIVING_OFF_THE_LAND,
            adversario=ModeloAdversario.CHINA,
            doutrina=DoutrinaOfensiva.TERCEIRIZACAO,
            nome_grupo="UNC5221 / Flax Typhoon",
            descricao="Novos grupos/ clusters chineses ativos em 2024/2025. Usam técnicas living-off-the-land, "
                      "comprometimento de appliances de rede (Ivanti, etc) e persistencia em ambientes OT. "
                      "Foco em pre-posicionamento e coleta de inteligencia.",
            alvo_tipico="Dispositivos de rede, appliances empresariais, infra OT em paises ocidentais",
            mitlagao_republicana="Atualizacao rigorosa e patching automatizado. Inventario completo de "
                                 "dispositivos de rede. Monitoramento comportamental (anomalias em binarios nativos). "
                                 "Uso de software soberano auditavel.",
            gravidade=4,
            ano_referencia="2024/2025",
        ),
        AmeacaCatalogada(
            tipo=TipoAmeaca.DDoS,
            adversario=ModeloAdversario.RUSSIA,
            doutrina=DoutrinaOfensiva.HACKTIVISMO_PATRIOTICO,
            nome_grupo="NoName057(16) & Killnet",
            descricao="Grupos hacktivistas russos intensamente ativos em 2024/2025. Ataques DDoS coordenados "
                      "contra paises que apoiam Ucrania, combinados com operacoes de desinformacao. "
                      "Frequentemente usados como proxy para negacao plausivel.",
            alvo_tipico="Sites governamentais, servicos online, infraestrutura digital da OTAN e aliados",
            mitlagao_republicana="CDN global distribuido + anycast. Capacidade de fallback offline para servicos "
                                 "essenciais (P4). Mitigacao na borda e cultura de resiliencia.",
            gravidade=3,
            ano_referencia="2024/2025",
        ),
        AmeacaCatalogada(
            tipo=TipoAmeaca.SUPPLY_CHAIN,
            adversario=ModeloAdversario.CHINA,
            doutrina=DoutrinaOfensiva.TERCEIRIZACAO,
            nome_grupo="i-Soon (2024 leak) & Storm-1849",
            descricao="Vazamento de i-Soon em 2024 revelou escala de terceirizacao chinesa. Storm-1849 e clusters "
                      "relacionados representam novos atores de supply-chain attacks e espionagem industrial.",
            alvo_tipico="Governos, empresas de tecnologia, dissidentes, infra critica via fornecedores",
            mitlagao_republicana="Software 100% auditavel e de codigo aberto (CC0). Cadeia de suprimentos "
                                 "transparente. Proibicao constitucional de terceirizacao opaca (P12).",
            gravidade=4,
            ano_referencia="2024",
        ),
        AmeacaCatalogada(
            tipo=TipoAmeaca.RANSOMWARE,
            adversario=ModeloAdversario.RUSSIA,
            doutrina=DoutrinaOfensiva.COOPTACAO_CRIME,
            nome_grupo="REvil/Conti remnants & LockBit affiliates",
            descricao="Grupos de ransomware cooptados ou tolerados pela FSB. Atividade continua em 2024/2025 "
                      "contra alvos ocidentais enquanto operam com relativa impunidade na Russia.",
            alvo_tipico="Empresas, hospitais, governos, infra critica",
            mitlagao_republicana="Backups offline imutaveis e testados regularmente. Politica de nao pagamento "
                                 "de resgate. Recuperacao rapida via cultura de backup (P7).",
            gravidade=4,
            ano_referencia="2024/2025",
        ),
        AmeacaCatalogada(
            tipo=TipoAmeaca.DESINFORMACAO,
            adversario=ModeloAdversario.RUSSIA,
            doutrina=DoutrinaOfensiva.HACKTIVISMO_PATRIOTICO,
            nome_grupo="IRA successors & Cyber Army of Russia",
            descricao="Campanhas de desinformacao em massa via redes sociais, bots e trolls. Intensificadas em "
                      "2024/2025 durante ciclos eleitorais e conflitos hibridos.",
            alvo_tipico="Eleicoes, debate publico, confianca institucional, polarizacao social",
            mitlagao_republicana="P9 (anti-polarizacao) + P6 (alfabetizacao). Midia publica transparente (P5). "
                                 "Cidadaos treinados em verificacao de fontes e pensamento critico (P7).",
            gravidade=4,
            ano_referencia="2024/2025",
        ),
    ]


# ============================================================================
# 5. ENGINE
# ============================================================================

class CyberDefenseEngine:
    """
    Avalia sistemas e doutrinas contra P12 (defesa cibernetica transparente).

    Faz duas coisas:
    1. AVALIAR SISTEMAS: um sistema da Republica e defensivamente adequado?
    2. AUDITAR DOUTRINAS: uma proposta de Estado viola os 5 NAO de P12?
    """

    def __init__(self) -> None:
        self.ameacas: List[AmeacaCatalogada] = _init_catalogo_ameacas()
        self.sistemas: Dict[str, SistemaDefensivo] = {}

    def registrar_sistema(self, s: SistemaDefensivo) -> None:
        self.sistemas[s.id] = s

    # -- avaliar sistema ----------------------------------------------------

    def avaliar_sistema(self, sistema_id: str) -> Dict[str, Any]:
        """Avalia a postura defensiva de um sistema da Republica."""
        s = self.sistemas.get(sistema_id)
        if s is None:
            return {"erro": f"Sistema nao encontrado: {sistema_id}"}

        # 1. Verificar proibicoes P12 (5 NAO) -- qualquer uma = CRITICA
        proibicoes_violadas: List[str] = []
        if s.coopta_criminosos:
            proibicoes_violadas.append(
                f"{ProibicaoP12.NAO_COOPTA.rotulo}: Cooptar criminosos e PROIBIDO. "
                f"Cadeia ou recuperacao, nunca cooptacao."
            )
        if s.militariza_civis:
            proibicoes_violadas.append(
                f"{ProibicaoP12.NAO_MILITARIZA.rotulo}: Militarizar civis para "
                f"guerra cibernetica e PROIBIDO. Universidade ensina DEFESA."
            )
        if s.financia_fachada:
            proibicoes_violadas.append(
                f"{ProibicaoP12.NAO_FACHADA.rotulo}: Financiar grupos de fachada "
                f"e PROIBIDO. Transparencia radical (P5)."
            )
        if s.e_ofensivo:
            proibicoes_violadas.append(
                f"{ProibicaoP12.NAO_OFENSIVA.rotulo}: Ataque ofensivo e PROIBIDO. "
                f"A Republica nao ataca primeiro."
            )
        if s.e_secreto:
            proibicoes_violadas.append(
                f"{ProibicaoP12.NAO_SECRETA.rotulo}: Operacoes secretas sao PROIBIDAS. "
                f"Tudo auditavel (P5)."
            )

        # 2. Calcular nivel de defesa
        score = 0
        pilares: List[str] = []
        if s.tem_firewall:
            score += 15
            pilares.append("firewall basico")
        if s.tem_ids:
            score += 20
            pilares.append("IDS/IPS")
        if s.tem_monitoramento:
            score += 20
            pilares.append("monitoramento")
        if s.tem_resposta_auto:
            score += 20
            pilares.append("resposta automatizada")
        if s.tem_audit_publico:
            score += 15
            pilares.append("audit publico (P5)")
        if s.cidadaos_treinados:
            score += 10
            pilares.append("cultura cidadaa (P7)")

        if score >= 85:
            status = StatusDefesa.CULTURA
        elif score >= 65:
            status = StatusDefesa.FORTIFICADO
        elif score >= 45:
            status = StatusDefesa.DEFENDIDO
        elif score >= 20:
            status = StatusDefesa.BASICO
        else:
            status = StatusDefesa.INDEFESO

        # infraestrutura critica exige mais
        if s.infraestrutura_critica and score < 65:
            status = StatusDefesa.INDEFESO
            proibicoes_violadas.append(
                "INFRAESTRUTURA CRITICA com defesa insuficiente. "
                "Agua, energia, transporte e telecom exigem FORTIFICACAO minima."
            )

        s.status = status

        # 3. Status final
        if proibicoes_violadas:
            veredito = "REJEITADO -- Viola P12"
        elif status == StatusDefesa.CULTURA:
            veredito = "EXEMPLAR -- Cultura de defesa"
        elif status == StatusDefesa.FORTIFICADO:
            veredito = "ADEQUADO -- Fortificado"
        elif status == StatusDefesa.DEFENDIDO:
            veredito = "ACEITAVEL -- Defesa basica"
        else:
            veredito = "INSUFICIENTE -- Precisa de defesa"

        return {
            "sistema_id": s.id,
            "sistema_nome": s.nome,
            "infraestrutura_critica": s.infraestrutura_critica,
            "score_defesa": score,
            "nivel_defesa": status.rotulo,
            "pilares_implementados": pilares,
            "proibicoes_violadas": proibicoes_violadas,
            "veredito": veredito,
            "timestamp": datetime.now().isoformat(),
            "ameacas_relevantes": len([a for a in self.ameacas if a.gravidade >= 4]),
        }

    # -- auditar doutrina ---------------------------------------------------

    def auditar_doutrina(self, proposta: Dict[str, Any]) -> Dict[str, Any]:
        """
        Audita uma proposta de politica/doutrina cibernetica contra os 5 NAO.

        proposta e um dict com booleanos: coopta, militariza, financia_fachada,
        e_ofensiva, e_secreta.
        """
        proibicoes = {
            "coopta": ProibicaoP12.NAO_COOPTA,
            "militariza": ProibicaoP12.NAO_MILITARIZA,
            "financia_fachada": ProibicaoP12.NAO_FACHADA,
            "e_ofensiva": ProibicaoP12.NAO_OFENSIVA,
            "e_secreta": ProibicaoP12.NAO_SECRETA,
        }
        violacoes: List[str] = []
        for key, proib in proibicoes.items():
            if proposta.get(key, False):
                violacoes.append(proib.rotulo)

        return {
            "proposta": proposta.get("nome", "sem nome"),
            "violacoes_P12": violacoes,
            "veredito": "REJEITADA" if violacoes else "CONFORME",
            "explicacao": (
                "A Republica nao replica o modelo russo/chines de 2024/2025. "
                "Exercito cibernetico secreto = Russia com outra bandeira."
                if violacoes else
                "Conforme P12. Defesa transparente, nunca ofensiva secreta. Cultura de massa (P7)."
            ),
        }

    # -- catalogo de ameacas -----------------------------------------------

    def listar_ameacas(self) -> List[Dict[str, Any]]:
        """Lista todas as ameacas catalogadas para conhecimento (atualizado 2025)."""
        return [
            {
                "tipo": a.tipo.rotulo,
                "adversario": a.adversario.rotulo,
                "doutrina": a.doutrina.rotulo,
                "grupo": a.nome_grupo,
                "descricao": a.descricao,
                "alvo": a.alvo_tipico,
                "mitigacao": a.mitlagao_republicana,
                "gravidade": a.gravidade,
                "ano": a.ano_referencia,
            }
            for a in self.ameacas
        ]

    def ameacas_por_adversario(self, adv: ModeloAdversario) -> List[Dict[str, Any]]:
        return [a for a in self.listar_ameacas() if adv.id in a["adversario"].lower()]

    def scorecard(self) -> Dict[str, Any]:
        return {
            "ameacas_catalogadas": len(self.ameacas),
            "doutrinas_ofensivas": len(list(DoutrinaOfensiva)),
            "modelos_adversario": len(list(ModeloAdversario)),
            "pilares_defesa": len(list(PilarDefesaRepublica)),
            "proibicoes_P12": len(list(ProibicaoP12)),
            "sistemas_avaliados": len(self.sistemas),
            "principio": "P12 -- Defesa Cibernetica Transparente (atualizado 2025)",
            "novos_apt_mencionados": ["UNC5221", "Storm-1849", "Flax Typhoon", "NoName057(16)"],
        }


# ============================================================================
# 6. DEMO
# ============================================================================

def _demo() -> None:
    eng = CyberDefenseEngine()

    print("=" * 70)
    print("OpenCyberDefense -- P12: Defesa Cibernetica Transparente (Atualizado 2025)")
    print("=" * 70)

    # --- Catalogo de ameacas ---
    print(f"\n[CATALOGO DE AMEACAS ({len(eng.ameacas)} entradas - dados 2024/2025)]")
    for a in eng.ameacas:
        sev = "*" * a.gravidade
        print(f"\n  [{sev}] {a.nome_grupo} ({a.adversario.id.upper()}) [{a.ano_referencia}]")
        print(f"  Tipo: {a.tipo.rotulo}")
        print(f"  Doutrina: {a.doutrina.rotulo}")
        print(f"  Descricao: {a.descricao[:120]}...")
        print(f"  Alvo: {a.alvo_tipico}")
        print(f"  Republica responde: {a.mitlagao_republicana[:100]}...")

    # --- Os 5 NAO ---
    print("\n\n[OS 5 NAO DE P12 -- O QUE A REPUBLICA PROIBE]")
    for p in ProibicaoP12:
        print(f"  {p.rotulo}")

    # --- Os 5 SIM ---
    print("\n[OS 5 SIM DE P12 -- O QUE A REPUBLICA FAZ]")
    for p in PilarDefesaRepublica:
        print(f"  {p.rotulo}")

    # --- Avaliar sistemas ---
    print("\n\n[AVALIACAO DE SISTEMAS DA REPUBLICA]")

    # Sistema exemplar (muralha + cultura)
    eng.registrar_sistema(SistemaDefensivo(
        id="muralha", nome="Muralha da Republica (IDS+audit+cultura)",
        infraestrutura_critica=True, tem_firewall=True, tem_ids=True,
        tem_monitoramento=True, tem_resposta_auto=True,
        tem_audit_publico=True, cidadaos_treinados=True,
    ))

    # Sistema indefeso (infraestrutura critica sem defesa)
    eng.registrar_sistema(SistemaDefensivo(
        id="indefeso", nome="Rede Eletrica (sem defesa)",
        infraestrutura_critica=True,
    ))

    # Sistema ofensivo (VIOLA P12)
    eng.registrar_sistema(SistemaDefensivo(
        id="ofensivo", nome="Unidade de Ataque Cibernetico Secreto",
        e_ofensivo=True, e_secreto=True, financia_fachada=True,
    ))

    # Sistema que coopta criminosos (VIOLA P12)
    eng.registrar_sistema(SistemaDefensivo(
        id="coopta", nome="Programa de Recrutamento de Hackers Presos",
        coopta_criminosos=True,
    ))

    for sid in ["muralha", "indefeso", "ofensivo", "coopta"]:
        res = eng.avaliar_sistema(sid)
        print(f"\n  {res['sistema_nome']}")
        print(f"    Veredito: {res['veredito']}")
        print(f"    Score: {res['score_defesa']} | Nivel: {res['nivel_defesa']}")
        if res.get("proibicoes_violadas"):
            for p in res["proibicoes_violadas"]:
                print(f"    VIOLACAO: {p}")

    # --- Auditar doutrinas propostas ---
    print("\n\n[AUDITORIA DE DOUTRINAS PROPOSTAS]")

    doutrinas = [
        {"nome": "Esquadrão Cientifico Universitario (modelo russo/chines 2025)",
         "militariza": True, "e_secreta": True},
        {"nome": "Cooptacao de Cibercriminosos (modelo russo)",
         "coopta": True},
        {"nome": "Empresa de Fachada para Ataques (modelo chines i-Soon/Storm-1849)",
         "financia_fachada": True, "e_ofensiva": True, "e_secreta": True},
        {"nome": "Treinamento de Cidadaos em Defesa (modelo Republica)",
         "coopta": False, "militariza": False, "financia_fachada": False,
         "e_ofensiva": False, "e_secreta": False},
    ]

    for d in doutrinas:
        res = eng.auditar_doutrina(d)
        icon = "[REJEITADA]" if res["violacoes_P12"] else "[CONFORME]  "
        print(f"\n  {icon} {res['proposta']}")
        if res["violacoes_P12"]:
            for v in res["violacoes_P12"]:
                print(f"           Violou: {v}")
        print(f"           {res['explicacao']}")

    # --- Scorecard ---
    print("\n\n[SCORECARD]")
    sc = eng.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<28} {v}")

    # --- Filosofia ---
    print("\n" + "=" * 70)
    print("FILOSOFIA -- A Republica Nao Replica o Inimigo (2025)")
    print("=" * 70)
    print("""
O MODELO RUSSO/CHINES (2024/2025):

  Russia continua cooptando criminosos (REvil remnants) e usa hacktivistas (NoName057).
  China expande pre-posicionamento via Volt Typhoon, Salt Typhoon, UNC5221, Flax Typhoon.
  Ambos usam terceirizacao (i-Soon leak expôs o modelo) e living-off-the-land.

  O resultado: capacidade massiva de pre-posicionamento e negacao plausivel.

A ARMADILHA:

  Se a Republica criar a MESMA estrutura (exercito cibernetico secreto, cooptacao,
  grupos de fachada), vira Russia ou China com bandeira verde-amarela.

A RESPOSTA DA REPUBLICA (P12):

  Em vez de exercito secreto: CULTURA DE MASSA.
  Cada cidadao com nmap APRENDE sobre portas.
  Cada cidadao com wireshark VE dados viajando.
  Nao sao soldados. Sao SENSORES da propria comunidade.

  A Republica nao ataca primeiro. Defender-se, sim.
  A Republica nao coopta. Cadeia ou recuperacao (P1).
  A Republica nao financia fachadas. Transparencia radical (P5).
  A Republica nao terceiriza. Codigo publico CC0 auditavel.

CONHECER O INIMIGO NAO E COPIAR O INIMIGO:

  O motor cataloga Volt Typhoon, Salt Typhoon, UNC5221, NoName057(16), Storm-1849.
  Nao para replicar. Para SABER o que enfrentar e construir mitigacoes defensivas.

  Pre-posicionamento? Segmentacao OT/IT rigorosa + audit continuo.
  Living-off-the-land? Monitoramento comportamental + software soberano.
  Ransomware? Backups offline imutaveis. Nao pagamos resgate.
  Desinformacao? P9 + alfabetizacao digital (P6+P7).

A DIFERENCA FUNDAMENTAL:

  Russia/China: cidadaos como ARMAS ou SOLDADOS do Estado.
  Republica: cidadaos como SENSORES e PROTETORES da propria comunidade.

  O cidadao nao serve ao Estado. O Estado serve ao cidadao.
  O cidadao com nmap protege o vizinho e a Republica.
""")


if __name__ == "__main__":
    _demo()
