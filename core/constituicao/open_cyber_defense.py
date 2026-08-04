#!/usr/bin/env python3
"""
OpenCyberDefense -- P12: Defesa Cibernetica Transparente
=========================================================
"A Republica nao tem exercito secreto. Tem cidadaos armados de nmap."

TESE:
  Russia e China construíram exercitos cibernéticos por 4 vias:
  1. Cooptacao do cibercrime (hackers presos viram Estado ou presos)
  2. Recrutamento universitario ("esquadrões científicos")
  3. Hacktivismo patriotico (grupos de fachada tipo Killnet, Volt Typhoon)
  4. Terceirizacao (empresas privadas tipo i-Soon)

  O resultado: capacidade ofensiva massiva, negacao plausivel, guerra híbrida.

  A Republica responde DIFERENTE. Nao replica o modelo ofensivo.
  Se a Republica criar um "exercito cibernetico secreto", vira Russia com
  bandeira verde-amarela. A doenca com outro nome ainda e doenca.

A RESPOSTA DA REPUBLICA (P12):

  Em vez de exercito secreto, CULTURA DEFENSIVA DE MASSA.
  Em vez de cooptar criminosos, ERRADICAR cibercrime (P1: miseria=crime).
  Em vez de recrutar universitarios pra guerra, ENSINAR seguranca a TODOS.
  Em vez de grupos de fachada, TRANSPARENCIA RADICAL (P5).
  Em vez de terceirizar ataques, AUDITAR infraestrutura publica.

O MODELO DE AMEACA (o que Russia/China fazem):

  O motor cataloga as 4 doutrinas ofensivas inimigas para que a Republica
  saiba o que enfrenta. Conhecer o inimigo nao e copiar o inimigo.

  | Doutrina         | Russia              | China              |
  |------------------|---------------------|--------------------|
  | Cibercrime       | FSB coopta (ultimato)|-Menos tolerante    |
  | Universidades    | Esquadrões cientif. | Competicoes estado |
  | Hacktivismo      | Killnet, Cyber Army | Honker Union       |
  | Terceirizacao    | -                   | i-Soon, empresas   |
  | Foco             | DDoS, caos, ransom  | Pre-posicionamento |

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
  4. RESPOSTA PROPORCIONAL: se atacada, responde com隔离 + sanção, nao arma.
  5. COALIZAO ABERTA: alianca com paises que rejeitam guerra cibernetica.

PRINCIPIO CONSTITUCIONAL (P12):

  A Republica mantem defesa cibernetica TRANSPARENTE e DEFENSIVA.
  Nenhum sistema de ataque ofensivo secreto e permitido.
  Todo cidadao e treinado em seguranca digital como CULTURA (P7).
  A Republica nao coopta criminosos, nao militariza civis,
  nao financia grupos de fachada, nao terceiriza operacoes ofensivas.

Constituicao: P1, P4, P5, P7, P8.

Author: OpenRepublic Team
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
    RUSSIA = ("russia", "Russia: tolerancia com crime local, DDoS, ransom, caos")
    CHINA = ("china", "China: pre-posicionamento, espionagem industrial, terceirizacao")
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
    nome_grupo: str           # ex: "Volt Typhoon", "Killnet"
    descricao: str
    alvo_tipico: str
    mitlagao_republicana: str  # como a Republica se defende disso
    gravidade: int = 3         # 1-5


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
# 4. CATALOGO DE AMEACAS (Russia + China)
# ============================================================================

def _init_catalogo_ameacas() -> List[AmeacaCatalogada]:
    """Cataloga as ameacas reais para que a Republica saiba o que enfrenta."""
    return [
        AmeacaCatalogada(
            tipo=TipoAmeaca.PRE_POSICIONAMENTO,
            adversario=ModeloAdversario.CHINA,
            doutrina=DoutrinaOfensiva.TERCEIRIZACAO,
            nome_grupo="Volt Typhoon",
            descricao="Infiltracao em infraestrutura critica dos EUA (agua, energia, "
                      "telecom). Objetivo: pré-posicionar para sabotagem em conflito futuro.",
            alvo_tipico="Sistemas SCADA, redes electricas, tratamento de agua",
            mitlagao_republicana="Segmentacao de rede OT/IT. Air-gap onde possivel. "
                                  "Audit continuo de trafego outbound. Cidadaos treinados "
                                  "detectam anomalias (P7).",
            gravidade=5,
        ),
        AmeacaCatalogada(
            tipo=TipoAmeaca.ESPIONAGEM,
            adversario=ModeloAdversario.CHINA,
            doutrina=DoutrinaOfensiva.TERCEIRIZACAO,
            nome_grupo="Salt Typhoon",
            descricao="Invasao de redes de telecomunicacoes para interceptar "
                      "comunicacoes de alto nivel.",
            alvo_tipico="Operadoras de telecom, backbones, satelites",
            mitlagao_republicana="Criptografia end-to-end obrigatoria na Republica. "
                                  "Rede soberana (OpenNetwork). Nenhum backdoor.",
            gravidade=5,
        ),
        AmeacaCatalogada(
            tipo=TipoAmeaca.DDoS,
            adversario=ModeloAdversario.RUSSIA,
            doutrina=DoutrinaOfensiva.HACKTIVISMO_PATRIOTICO,
            nome_grupo="Killnet",
            descricao="Grupo de hackers patriotas russos. Ataques DDoS massivos "
                      "contra paises inimigos de Moscou.",
            alvo_tipico="Sites gov, servicos online, infraestrutura digital",
            mitlagao_republicana="CDN distribuido. Mitigacao DDoS na borda. "
                                  "Servicos criticos com modo offline (P4: processo "
                                  "democratico nao pode depender de uptime).",
            gravidade=3,
        ),
        AmeacaCatalogada(
            tipo=TipoAmeaca.SUPPLY_CHAIN,
            adversario=ModeloAdversario.CHINA,
            doutrina=DoutrinaOfensiva.TERCEIRIZACAO,
            nome_grupo="i-Soon (vazamento)",
            descricao="Empresa privada chinesa que terceirizava ataques ciberneticos "
                      "para o Estado. Vazamento confirmou operacoes contra governos "
                      "estrangeiros.",
            alvo_tipico="Governos, ONGs, dissidentes, empresas estrangeiras",
            mitlagao_republicana="Republica nao terceiriza. Todo codigo e publico "
                                  "(CC0) e auditavel. Software livre eliminina "
                                  "cadeia de suprimentos opaca.",
            gravidade=4,
        ),
        AmeacaCatalogada(
            tipo=TipoAmeaca.RANSOMWARE,
            adversario=ModeloAdversario.RUSSIA,
            doutrina=DoutrinaOfensiva.COOPTACAO_CRIME,
            nome_grupo="Conti / REvil (cooptados)",
            descricao="Grupos ransomware cooptados pela FSB. Atacam alvos "
                      "estrangeiros enquanto tolerados em territorio russo.",
            alvo_tipico="Empresas, hospitais, governos estrangeiros",
            mitlagao_republicana="Backups offline obrigatorios. Republica nao paga "
                                  "resgate (negociacao incentiva crime). Recuperacao "
                                  "em horas, nao dias.",
            gravidade=4,
        ),
        AmeacaCatalogada(
            tipo=TipoAmeaca.DESINFORMACAO,
            adversario=ModeloAdversario.RUSSIA,
            doutrina=DoutrinaOfensiva.HACKTIVISMO_PATRIOTICO,
            nome_grupo="IRA / Cyber Army of Russia Reborn",
            descricao="Campanhas de desinformacao em redes sociais para polarizar "
                      "sociedades adversarias. Conta com bots e trolis pagos.",
            alvo_tipico="Eleicoes, debate publico, confianca institucional",
            mitlagao_republicana="P9 (anti-polarizacao). Estado nao amplifica. "
                                  "Midia publica com P5 (transparencia). Cidadaos "
                                  "alfabetizados em informacao (P6+P7).",
            gravidade=4,
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
                "A Republica nao replica o modelo russo/chines. "
                "Exercito cibernetico secreto = Russia com outra bandeira."
                if violacoes else
                "Conforme. Defesa transparente, nunca ofensiva secreta."
            ),
        }

    # -- catalogo de ameacas -----------------------------------------------

    def listar_ameacas(self) -> List[Dict[str, Any]]:
        """Lista todas as ameacas catalogadas para conhecimento."""
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
            }
            for a in self.ameacas
        ]

    def ameacas_por_adversario(self, adv: ModeloAdversario) -> List[Dict[str, Any]]:
        return [a for a in self.listar_ameacas() if adv.id in a["adversario"]]

    def scorecard(self) -> Dict[str, Any]:
        return {
            "ameacas_catalogadas": len(self.ameacas),
            "doutrinas_ofensivas": len(list(DoutrinaOfensiva)),
            "modelos_adversario": len(list(ModeloAdversario)),
            "pilares_defesa": len(list(PilarDefesaRepublica)),
            "proibicoes_P12": len(list(ProibicaoP12)),
            "sistemas_avaliados": len(self.sistemas),
            "principio": "P12 -- Defesa Cibernetica Transparente",
        }


# ============================================================================
# 6. DEMO
# ============================================================================

def _demo() -> None:
    eng = CyberDefenseEngine()

    print("=" * 70)
    print("OpenCyberDefense -- P12: Defesa Cibernetica Transparente")
    print("=" * 70)

    # --- Catalogo de ameacas ---
    print(f"\n[CATALOGO DE AMEACAS ({len(eng.ameacas)})]")
    for a in eng.ameacas:
        sev = "*" * a.gravidade
        print(f"\n  [{sev}] {a.nome_grupo} ({a.adversario.id})")
        print(f"  Tipo: {a.tipo.rotulo}")
        print(f"  Doutrina: {a.doutrina.rotulo}")
        print(f"  Descricao: {a.descricao}")
        print(f"  Alvo: {a.alvo_tipico}")
        print(f"  Republica responde: {a.mitlagao_republicana}")

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
        if res["proibicoes_violadas"]:
            for p in res["proibicoes_violadas"]:
                print(f"    VIOLACAO: {p}")

    # --- Auditar doutrinas propostas ---
    print("\n\n[AUDITORIA DE DOUTRINAS PROPOSTAS]")

    doutrinas = [
        {"nome": "Esquadrão Cientifico Universitario (modelo russo)",
         "militariza": True, "e_secreta": True},
        {"nome": "Cooptacao de Cibercriminosos (modelo russo)",
         "coopta": True},
        {"nome": "Empresa de Fachada para Ataques (modelo chines i-Soon)",
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
    print("FILOSOFIA -- A Republica Nao Replica o Inimigo")
    print("=" * 70)
    print("""
O MODELO RUSSO/CHINES:

  Russia coopta criminosos: hacker preso vira funcionario do FSB.
  China terceiriza: empresa privada i-Soon executa ataques para o Estado.
  Ambos militarizam universitarios: esquadrões científicos, competicoes.
  Ambos usam grupos de fachada: Killnet, Honker Union, Cyber Army.

  O resultado: exercito cibernetico massivo com negacao plausivel.
  "Nao fomos nos. Foi grupo civil independente." (mas foi financiado.)

A ARMADILHA:

  Se a Republica criar a MESMA estrutura, vira Russia com bandeira verde.
  Cooptar criminosos para "defender a patria" e a MESMA coisa que a FSB faz.
  Financiar grupo civil para atacar inimigo e a MESMA coisa que a China faz.

  A doenca com outro nome ainda e doenca.
  A tirania com outra bandeira ainda e tirania.

A RESPOSTA DA REPUBLICA:

  Em vez de exercito secreto: CULTURA DE MASSA.
  Cada cidadao com nmap APRENDE sobre portas.
  Cada cidadao com wireshark VE dados viajando.
  Nao sao soldados. Sao SENSORES.

  A Republica nao ataca primeiro. Defender-se, sim.
  A Republica nao coopta. Cadeia ou recuperacao (P1).
  A Republica nao financia fachadas. Transparencia radical (P5).
  A Republica nao terceiriza. Codigo publico CC0 auditavel.

CONHECER O INIMIGO NAO E COPIAR O INIMIGO:

  O motor cataloga Volt Typhoon, Killnet, i-Soon, REvil.
  Nao para replicar. Para SABER o que enfrentar.
  Para cada ameaca, a Republica tem MITIGACAO DEFENSIVA.
  Pre-posicionamento? Segmentacao OT/IT + audit continuo.
  Ransomware? Backups offline. Nao pagamos resgate.
  Desinformacao? P9 + cidadaos alfabetizados.

A DEFERENCA FUNDAMENTAL:

  Russia: cidadaos como ARMAS do Estado.
  China: cidadaos como SOLDADOS do Partido.
  Republica: cidadaos como SENSORES da propria comunidade.

  O cidadao nao serve ao Estado. O Estado serve ao cidadao.
  O cidadao com nmap protege a PROPRIA comunidade.
  Nao ataca inimigo do Estado. Defende o vizinho.
""")


if __name__ == "__main__":
    _demo()
