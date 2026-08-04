#!/usr/bin/env python3
"""
OpenCitizenOversight -- P13: Contravigilancia Reciproca
========================================================
"O Estado ja te vigia. Ele so nao fala disso publicamente.
 Ate a clara do ovo que o presidente comeu precisa ser publica."

TESE:
  Hoje a vigilancia e assimetrica:
  - Estado sabe tudo de voce (PRISM, XKeyscore, Five Eyes, dados de app).
  - Voce nao sabe nada do Estado ("seguranca nacional", sigilo, opacidade).
  - Eles mentem quando perguntados (Clapper, 2013: "not wittingly").
  - Eles nao param quando descobertos. Adaptam-se.

  Viver no mundo das fadas dizendo "AI nao me vigia" e suicidio digital.
  A Republica NAO promete "nao vamos te vigiar". Promete o CONTRARIO:
  "voce vai vigiar NOS de volta". E proporcional ao poder.

O PRINCIPIO (P13):

  Contravigilancia reciproca. Quem exerce poder publico PERDE privacidade
  PROPORCIONAL ao poder exercido.

  - Cidadao comum: PRIVACIDADE TOTAL (P2). Estado nao espiona sem due process.
  - Servidor publico: transparencia financeira + comunicacoes institucionais.
  - Autoridade eleita: vida publica 24/7 no cargo. Reunioes, gastos, contatos.
  - Presidente/ministros: ate o ovo do cafe da manha.

  Nao e vinganca. E SIMETRIA. Quem decide sobre milhoes nao tem direito
  ao mesmo nivel de privacidade de quem so decide sobre a propria vida.

OS TIERS DE TRANSPARENCIA (proporcionais ao poder):

  T1 - CIDADAO COMUM:
    Privacidade TOTAL (P2). Dados pessoais protegidos.
    Estado precisa de ordem judicial PARA CADA pedido.
    Coleta massiva sem mandado e CRIME (P5 violado).

  T2 - SERVIDOR PUBLICO:
    Declaracao de bens PUBLICA.
    Comunicacao institucional (email, celular do cargo) PUBLICA.
    Vida pessoal permanece privada.
    Cartao corporativo: todos os gastos PUBLICOS em tempo real.

  T3 - AUTORIDADE ELEITA (vereador, deputado, prefeito, governador):
    Tudo de T2 +
    Agenda publica (com quem se encontra, onde, quando).
    Patrimonio declarado e auditado.
    Comunicacao no cargo e PUBLICA (nao ha direito a sigilo pessoal).
    Votos e justificativas PUBLICOS.

  T4 - EXECUTIVO DE ALTO ESCALAO (presidente, ministros, chefes de agencia):
    Tudo de T3 +
    Reunioes gravadas e publicadas (nao ha reuniao secreta de Estado
    sem justificativa formal, temporaria, e auditada).
    Gastos pessoais durante o mandato: auditados.
    Saude: informe publico de capacidade funcional.
    Comunicacoes privadas com lobbies/empresarios: PROIBIDAS em sigilo.
    O "ovo do presidente" e PUBLICO. Nao por cruelty. Por SIMETRIA.

  T5 - INTELIGENCIA/MILITAR (o contra-ponto):
    Aqui e onde a Republica diverge do modelo atual.
    Hoje: inteligencia tem sigilo "absoluto" e ninguem vigia.
    Republica: inteligencia e vigiada por CIDADAO FISCALIZADOR eleito
    com clearance, mandato revogavel, e log publico de TUDO que pediu.
    Nenhuma requisicao de dados e secreta APOS ser executada.
    O cidadao tem 90 dias pra saber que foi espionado. Sempre.

O CIDADAO FISCALIZADOR:

  A Republica treina cada cidadao como SENSOR de contravigilancia.
  Nao espiao. SENSOR. A diferenca:
    Espiao: coleta em SEGREDO para o Estado.
    Sensor: ve em PUBLICO para a comunidade.

  Ferramentas do cidadao fiscalizador:
    - nmap: ve portas abertas em servicos publicos
    - wireshark: ve que dados o app do governo envia
    - osmocom: detecta torres celular falsas (IMSI catcher)
    - FOIA-Like: todo cidadao pode pedir dados do Estado
    - Audit continuo: gasto publico, agenda, votacoes

  O cidadao fiscalizador opera DENTRO E FORA do territorio.
  O brasileiro que viaja aos EUA sabe que e interceptado.
  O brasileiro que recebe estrangeiro sabe o que observar.

A INVERSAO DA BURROICE:

  Modelo atual: "confie no Estado. Ele protege voce."
  Resultado: Estado protege a si mesmo. Voce e alvo.

  Modelo Republica: "Estado e SERVO. Cidadao e FISCAL."
  Resultado: Estado trabalha SOB vigilancia. Cidadao e soberano.

  Quem quer privacidade NAO ENTRA no poder publico.
  O momento que voce aceita cargo, salario, orcamento ou autoridade
  paga com dinheiro publico, sua vida viva nesse cargo e REGISTRO PUBLICO.

  Nao e optativo. Nao e "para os amigos". Nao e "seguranca nacional".
  E a CLAUSULA DO PODER: voce recebe poder do povo, devolve transparencia.

Constituicao: P2 (autonomia corporal do cidadao), P4 (processo democratico),
P5 (transparencia radical do Estado), P7 (seguranca como cultura).

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime


# ============================================================================
# 1. ENUMS
# ============================================================================

class TierTransparencia(Enum):
    """Tier de transparencia proporcional ao poder exercido."""
    T1_CIDADAO = (1, "cidadao", "Cidadao comum: privacidade TOTAL (P2)")
    T2_SERVIDOR = (2, "servidor", "Servidor publico: transparencia financeira + institucional")
    T3_ELEITO = (3, "eleito", "Autoridade eleita: vida publica 24/7 no cargo")
    T4_EXECUTIVO = (4, "executivo", "Executivo alto escalao: agenda + gastos + reunioes publicas")
    T5_INTELIGENCIA = (5, "inteligencia", "Inteligencia/militar: vigiada por cidadao fiscalizador eleito")

    @property
    def peso(self) -> int:
        return self.value[0]

    @property
    def id(self) -> str:
        return self.value[1]

    @property
    def rotulo(self) -> str:
        return self.value[2]


class TipoDadoVigilado(Enum):
    """Tipos de dado que o Estado coleta de cidadaos (e que precisam ser reciprocal)."""
    COMUNICACOES = ("comunicacoes", "Comunicacoes: emails, mensagens, ligacoes")
    LOCALIZACAO = ("localizacao", "Localizacao: GPS, antena celular, WiFi scan")
    FINANCEIRO = ("financeiro", "Dados financeiros: transacoes, saldos, gastos")
    BIOMETRICO = ("biometrico", "Dados biometricos: digital, facial, voz")
    NAVEGACAO = ("navegacao", "Historico de navegacao e metadados de rede")
    SAUDE = ("saude", "Dados de saude e atendimentos")
    SOCIAL = ("social", "Relacoes sociais: com quem fala, com quem se encontra")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoDadoPublico(Enum):
    """Tipos de dado que servidores/autoridades DEVEM tornar publicos."""
    DECLARACAO_BENS = ("bens", "Declaracao de bens e patrimonio")
    GASTOS_CORPORATIVOS = ("gastos", "Gastos com cartao corporativo/orcamento publico")
    AGENDA = ("agenda", "Agenda: com quem se encontra, onde, quando")
    COMUNICACAO_INSTITUCIONAL = ("com_inst", "Emails e comunicacoes do cargo")
    VOTOS_DECISOES = ("votos", "Votos e decisoes com justificativa")
    REUNIOES = ("reunioes", "Reunioes gravadas e publicadas")
    PATROCINIO = ("patrocinio", "Patrocinios, doacoes, financiamento de campanha")
    SAUDE_FUNCIONAL = ("saude", "Informe de capacidade funcional")
    CONFLITO_INTERESSE = ("conflito", "Declaracao de conflito de interesses")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoAgenteExogeno(Enum):
    """Tipos de agentes exogenos (substitui 'espiao' com precisao)."""
    PASSIVO_INCONSCIENTE = ("passivo", "Turista/visitante com dispositivo que coleta sem saber")
    PASSIVO_CONSCIENTE = ("passivo_c", "Pessoa que sabe que seu dispositivo coleta")
    ATIVO_CORPORATIVO = ("corporativo", "Empresa estrangeira que coleta dados de cidadaos")
    ATIVO_ESTADUAL = ("estadual", "Agente de Estado estrangeiro (inteligencia)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class StatusOversight(Enum):
    """Status de conformidade de uma autoridade/servidor com P13."""
    CONFORME = ("conforme", "Transparencia proporcional ao poder exercida")
    REVISAO = ("revisao", "Faltam dados publicos exigidos pelo tier")
    SUSPENSO = ("suspenso", "Recusou divulgar dados do cargo")
    BANIDO = ("banido", "Usou cargo para esconder ato publico = banido do cargo")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class FerramentaFiscalizacao(Enum):
    """Ferramentas do cidadao fiscalizador (nao-espiao, sensor publico)."""
    NMAP = ("nmap", "nmap: ve portas abertas em servicos publicos")
    WIRESHARK = ("wireshark", "wireshark: ve que dados o app envia")
    OSMOCOM = ("osmocom", "osmocom: detecta torres celular falsas (IMSI catcher)")
    FOIA = ("foia", "Pedido de acesso a informacao (LAI/FOIA-like)")
    AUDIT_GASTO = ("audit_gasto", "Audit de gasto publico em tempo real")
    AUDIT_AGENDA = ("audit_agenda", "Audit de agenda de autoridade")
    AUDIT_VOTO = ("audit_voto", "Audit de votacoes e justificativas")
    OSINT = ("osint", "OSINT: informacao de fonte aberta")

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
class AgentePublico:
    """Um agente publico avaliado quanto a transparencia proporcional."""
    id: str
    nome: str
    cargo: str
    tier: TierTransparencia = TierTransparencia.T2_SERVIDOR
    # dados publicos fornecidos
    declaracao_bens_publica: bool = False
    gastos_corporativos_publicos: bool = False
    agenda_publica: bool = False
    comunicacao_institucional_publica: bool = False
    votos_justificados: bool = False
    reunioes_gravadas: bool = False
    conflito_interesse_declarado: bool = False
    saude_funcional_publica: bool = False
    patrocinio_publico: bool = False
    # violacoes
    recusou_divulgar: bool = False
    usou_sigilo_para_esconder: bool = False
    comunicacao_secreta_com_lobby: bool = False
    # metadata
    status: Optional[StatusOversight] = None


@dataclass
class DadoVigilado:
    """Um tipo de dado que o Estado coleta (e que cidadaos devem saber)."""
    tipo: TipoDadoVigilado
    coletor: str          # quem coleta (NSA, ABIN, empresa, app)
    metodo: str           # como (cabos submarinos, metadata, app SDK)
    legalidade: str       # base legal ou falta dela
    notificacao_90dias: bool = False  # cidadao e notificado em 90 dias?


@dataclass
class EventoFiscalizacao:
    """Um evento de fiscalizacao registrado por um cidadao."""
    id: str
    fiscalizador: str      # nome/cpf do cidadao (ou anonimizado)
    ferramenta: FerramentaFiscalizacao
    alvo: str              # o que foi auditado
    achado: str            # o que encontrou
    publico: bool = True   # fiscalizacao e sempre publica
    timestamp: str = ""


# ============================================================================
# 3. REQUISITOS POR TIER (qual dado cada tier deve tornar publico)
# ============================================================================

def _requisitos_por_tier() -> Dict[TierTransparencia, List[TipoDadoPublico]]:
    """Define quais dados publicos cada tier de poder exige."""
    return {
        TierTransparencia.T1_CIDADAO: [],  # cidadao nao deve nada
        TierTransparencia.T2_SERVIDOR: [
            TipoDadoPublico.DECLARACAO_BENS,
            TipoDadoPublico.GASTOS_CORPORATIVOS,
            TipoDadoPublico.CONFLITO_INTERESSE,
        ],
        TierTransparencia.T3_ELEITO: [
            TipoDadoPublico.DECLARACAO_BENS,
            TipoDadoPublico.GASTOS_CORPORATIVOS,
            TipoDadoPublico.AGENDA,
            TipoDadoPublico.COMUNICACAO_INSTITUCIONAL,
            TipoDadoPublico.VOTOS_DECISOES,
            TipoDadoPublico.CONFLITO_INTERESSE,
            TipoDadoPublico.PATROCINIO,
        ],
        TierTransparencia.T4_EXECUTIVO: [
            TipoDadoPublico.DECLARACAO_BENS,
            TipoDadoPublico.GASTOS_CORPORATIVOS,
            TipoDadoPublico.AGENDA,
            TipoDadoPublico.COMUNICACAO_INSTITUCIONAL,
            TipoDadoPublico.VOTOS_DECISOES,
            TipoDadoPublico.REUNIOES,
            TipoDadoPublico.CONFLITO_INTERESSE,
            TipoDadoPublico.PATROCINIO,
            TipoDadoPublico.SAUDE_FUNCIONAL,
        ],
        TierTransparencia.T5_INTELIGENCIA: [
            TipoDadoPublico.DECLARACAO_BENS,
            TipoDadoPublico.GASTOS_CORPORATIVOS,
            TipoDadoPublico.CONFLITO_INTERESSE,
            # Inteligencia tem sigilo operacional, MAS:
            # - Toda requisicao de dados de cidadao e logada
            # - Cidadao e notificado em 90 dias
            # - Cidadao fiscalizador eleito audita os logs
        ],
    }


# ============================================================================
# 4. CATALOGO DE VIGILANCIA (o que e feito contra cidadaos)
# ============================================================================

def _init_catalogo_vigilancia() -> List[DadoVigilado]:
    """Cataloga metodos de vigilancia que cidadaos precisam conhecer."""
    return [
        DadoVigilado(
            tipo=TipoDadoVigilado.COMUNICACOES,
            coletor="NSA (EUA) via PRISM/XKeyscore",
            metodo="Cabos submarinos, parcerias com Big Tech (Google, Meta, Apple)",
            legalidade="FISA Court secreta. Sem mandado judicial individual.",
            notificacao_90dias=False,
        ),
        DadoVigilado(
            tipo=TipoDadoVigilado.LOCALIZACAO,
            coletor="Apps (Google Maps, Uber, Instagram)",
            metodo="GPS + antena celular + WiFi scan continuo",
            legalidade="Termo de servico (ninguem le). Sem mandado.",
            notificacao_90dias=False,
        ),
        DadoVigilado(
            tipo=TipoDadoVigilado.NAVEGACAO,
            coletor="Provedores de internet + Big Tech",
            metodo="Metadata de conexao, cookies, fingerprinting",
            legalidade="Sem mandado. Dado 'metadado' tratado como nao-conteudo.",
            notificacao_90dias=False,
        ),
        DadoVigilado(
            tipo=TipoDadoVigilado.BIOMETRICO,
            coletor="Reconhecimento facial em via publica (empresas + Estado)",
            metodo="Camera publicas + banco de faces (Clearview AI e similares)",
            legalidade="Nenhuma regulamentacao efetiva no Brasil.",
            notificacao_90dias=False,
        ),
        DadoVigilado(
            tipo=TipoDadoVigilado.FINANCEIRO,
            coletor="Coaf, bancos, fintechs",
            metodo="Comunicacao de operacoes, metadata de transacoes",
            legalidade="Lei de lavagem de dinheiro. Sem mandado individual.",
            notificacao_90dias=False,
        ),
        DadoVigilado(
            tipo=TipoDadoVigilado.SOCIAL,
            coletor="Big Tech (Meta, Google, TikTok)",
            metodo="Grafo social: com quem fala, com quem esta, quem conhece",
            legalidade="Termo de servico. Ninguem le.",
            notificacao_90dias=False,
        ),
    ]


# ============================================================================
# 5. ENGINE
# ============================================================================

class CitizenOversightEngine:
    """
    Avalia agentes publicos quanto a transparencia proporcional (P13).

    Faz tres coisas:
    1. AVALIAR AGENTES: um servidor/autoridade publica o que seu tier exige?
    2. CATALOGAR VIGILANCIA: o que e feito contra cidadaos (consciencia).
    3. REGISTRAR FISCALIZACAO: cidadaos auditam e reportam publicamente.
    """

    def __init__(self) -> None:
        self.requisitos = _requisitos_por_tier()
        self.vigilancia = _init_catalogo_vigilancia()
        self.agentes: Dict[str, AgentePublico] = {}
        self.fiscalizacoes: List[EventoFiscalizacao] = []

    def registrar_agente(self, a: AgentePublico) -> None:
        self.agentes[a.id] = a

    # -- avaliar agente ----------------------------------------------------

    def avaliar_agente(self, agente_id: str) -> Dict[str, Any]:
        """Avalia se um agente publico cumpre a transparencia do seu tier."""
        a = self.agentes.get(agente_id)
        if a is None:
            return {"erro": f"Agente nao encontrado: {agente_id}"}

        # Mapear campos do AgentePublico para TipoDadoPublico
        campos_publicos = {
            TipoDadoPublico.DECLARACAO_BENS: a.declaracao_bens_publica,
            TipoDadoPublico.GASTOS_CORPORATIVOS: a.gastos_corporativos_publicos,
            TipoDadoPublico.AGENDA: a.agenda_publica,
            TipoDadoPublico.COMUNICACAO_INSTITUCIONAL: a.comunicacao_institucional_publica,
            TipoDadoPublico.VOTOS_DECISOES: a.votos_justificados,
            TipoDadoPublico.REUNIOES: a.reunioes_gravadas,
            TipoDadoPublico.CONFLITO_INTERESSE: a.conflito_interesse_declarado,
            TipoDadoPublico.SAUDE_FUNCIONAL: a.saude_funcional_publica,
            TipoDadoPublico.PATROCINIO: a.patrocinio_publico,
        }

        exigidos = self.requisitos.get(a.tier, [])
        cumpridos = [d for d in exigidos if campos_publicos.get(d, False)]
        faltantes = [d for d in exigidos if not campos_publicos.get(d, False)]

        # violacoes graves
        violacoes: List[str] = []
        if a.recusou_divulgar:
            violacoes.append("Recusou divulgar dados exigidos pelo cargo. SUSPENSAO.")
        if a.usou_sigilo_para_esconder:
            violacoes.append(
                "Usou sigilo para esconder ato publico. BANIDO do cargo. "
                "Sigilo nao e cortina para corrupcao."
            )
        if a.comunicacao_secreta_com_lobby:
            violacoes.append(
                "Comunicacao secreta com lobby/empresario. PROIBIDO. "
                "Toda comunicacao no cargo e PUBLICA."
            )

        # status
        if violacoes and any("BANIDO" in v for v in violacoes):
            status = StatusOversight.BANIDO
        elif violacoes:
            status = StatusOversight.SUSPENSO
        elif faltantes:
            status = StatusOversight.REVISAO
        else:
            status = StatusOversight.CONFORME

        a.status = status

        pct = (len(cumpridos) / len(exigidos) * 100) if exigidos else 100.0

        return {
            "agente_id": a.id,
            "agente_nome": a.nome,
            "cargo": a.cargo,
            "tier": f"T{a.tier.peso} ({a.tier.id})",
            "tier_rotulo": a.tier.rotulo,
            "dados_exigidos": len(exigidos),
            "dados_cumpridos": len(cumpridos),
            "dados_faltantes": [d.rotulo for d in faltantes],
            "pct_transparencia": round(pct, 1),
            "violacoes": violacoes,
            "status": f"{status.id} -- {status.rotulo}",
            "timestamp": datetime.now().isoformat(),
        }

    def avaliar_todos(self) -> Dict[str, Any]:
        resultados = {}
        for aid in self.agentes:
            resultados[aid] = self.avaliar_agente(aid)
        conforme = sum(
            1 for r in resultados.values()
            if isinstance(r, dict) and r.get("status", "").startswith("Conforme")
        )
        total = len(resultados)
        pct = (conforme / total * 100) if total else 0
        return {
            "total_agentes": total,
            "conformes": conforme,
            "suspensos": sum(1 for r in resultados.values()
                             if isinstance(r, dict) and "Suspenso" in r.get("status", "")),
            "banidos": sum(1 for r in resultados.values()
                           if isinstance(r, dict) and "banido" in r.get("status", "").lower()),
            "taxa_transparencia": f"{conforme}/{total} ({pct:.0f}%)",
            "resultados": resultados,
        }

    # -- catalogo de vigilancia --------------------------------------------

    def listar_vigilancia(self) -> List[Dict[str, Any]]:
        """Lista metodos de vigilancia que cidadaos devem conhecer."""
        return [
            {
                "tipo": v.tipo.rotulo,
                "coletor": v.coletor,
                "metodo": v.metodo,
                "legalidade": v.legalidade,
                "notificacao_90dias": v.notificacao_90dias,
            }
            for v in self.vigilancia
        ]

    # -- fiscalizacao cidada -----------------------------------------------

    def registrar_fiscalizacao(
        self, fiscalizador: str, ferramenta: FerramentaFiscalizacao,
        alvo: str, achado: str,
    ) -> EventoFiscalizacao:
        """Registra um evento de fiscalizacao cidada (sempre publico)."""
        ev = EventoFiscalizacao(
            id=f"FISC-{len(self.fiscalizacoes) + 1:06d}",
            fiscalizador=fiscalizador, ferramenta=ferramenta,
            alvo=alvo, achado=achado, publico=True,
            timestamp=datetime.now().isoformat(),
        )
        self.fiscalizacoes.append(ev)
        return ev

    def fiscalizacoes_recentes(self, limite: int = 10) -> List[Dict[str, Any]]:
        return [
            {
                "id": e.id,
                "fiscalizador": e.fiscalizador,
                "ferramenta": e.ferramenta.rotulo,
                "alvo": e.alvo,
                "achado": e.achado,
                "timestamp": e.timestamp,
            }
            for e in self.fiscalizacoes[-limite:]
        ]

    # -- ferramentas do cidadao --------------------------------------------

    @staticmethod
    def ferramentas_cidadao() -> List[Dict[str, str]]:
        """Lista as ferramentas do cidadao fiscalizador."""
        return [{"id": f.id, "rotulo": f.rotulo} for f in FerramentaFiscalizacao]

    # -- scorecard ---------------------------------------------------------

    def scorecard(self) -> Dict[str, Any]:
        return {
            "agentes_avaliados": len(self.agentes),
            "tiers_transparencia": len(list(TierTransparencia)),
            "tipos_dado_vigilado": len(list(TipoDadoVigilado)),
            "tipos_dado_publico": len(list(TipoDadoPublico)),
            "tipos_agente_exogeno": len(list(TipoAgenteExogeno)),
            "ferramentas_cidadao": len(list(FerramentaFiscalizacao)),
            "fiscalizacoes_registradas": len(self.fiscalizacoes),
            "vigilancia_catalogada": len(self.vigilancia),
            "principio": "P13 -- Contravigilancia Reciproca",
        }


# ============================================================================
# 6. DEMO
# ============================================================================

def _demo() -> None:
    eng = CitizenOversightEngine()

    print("=" * 70)
    print("OpenCitizenOversight -- P13: Contravigilancia Reciproca")
    print("=" * 70)

    # --- Tiers de transparencia ---
    print(f"\n[OS {len(list(TierTransparencia))} TIERS DE TRANSPARENCIA]")
    print("  (privacidade inversamente proporcional ao poder)")
    for t in TierTransparencia:
        reqs = eng.requisitos.get(t, [])
        print(f"\n  T{t.peso} ({t.id.upper()}) -- {t.rotulo}")
        if reqs:
            print(f"    Deve tornar publico ({len(reqs)} itens):")
            for r in reqs:
                print(f"      - {r.rotulo}")
        else:
            print(f"    Privacidade TOTAL (P2). Estado nao espiona sem due process.")

    # --- Catalogo de vigilancia ---
    print(f"\n\n[CATALOGO DE VIGILANCIA ATUAL ({len(eng.vigilancia)})]")
    print("  (o que e feito contra cidadaos HOJE -- consciencia)")
    for v in eng.vigilancia:
        print(f"\n  {v.tipo.rotulo}")
        print(f"    Coletor: {v.coletor}")
        print(f"    Metodo: {v.metodo}")
        print(f"    Legalidade: {v.legalidade}")
        notif = "SIM" if v.notificacao_90dias else "NAO (cidadao nao sabe)"
        print(f"    Notifica em 90 dias: {notif}")

    # --- Agentes de teste ---
    print("\n\n[AVALIACAO DE AGENTES PUBLICOS]")

    # T4 presidente que oculta tudo
    eng.registrar_agente(AgentePublico(
        id="pres_opaco", nome="Presidente Opaco (hipotetico)",
        cargo="Presidente da Republica", tier=TierTransparencia.T4_EXECUTIVO,
        # nada publico
    ))

    # T4 presidente conforme (Republica ideal)
    eng.registrar_agente(AgentePublico(
        id="pres_ok", nome="Presidente Transparente (Republica ideal)",
        cargo="Presidente da Republica", tier=TierTransparencia.T4_EXECUTIVO,
        declaracao_bens_publica=True, gastos_corporativos_publicos=True,
        agenda_publica=True, comunicacao_institucional_publica=True,
        votos_justificados=True, reunioes_gravadas=True,
        conflito_interesse_declarado=True, patrocinio_publico=True,
        saude_funcional_publica=True,
    ))

    # T3 deputado com comunicacao secreta com lobby
    eng.registrar_agente(AgentePublico(
        id="dep_lobby", nome="Deputado com Lobby Secreto",
        cargo="Deputado Federal", tier=TierTransparencia.T3_ELEITO,
        declaracao_bens_publica=True, gastos_corporativos_publicos=True,
        agenda_publica=True, conflito_interesse_declarado=True,
        comunicacao_secreta_com_lobby=True,
    ))

    # T2 servidor conforme
    eng.registrar_agente(AgentePublico(
        id="serv_ok", nome="Servidor Conforme",
        cargo="Analista Ministerial", tier=TierTransparencia.T2_SERVIDOR,
        declaracao_bens_publica=True, gastos_corporativos_publicos=True,
        conflito_interesse_declarado=True,
    ))

    # T2 servidor que recusou divulgar
    eng.registrar_agente(AgentePublico(
        id="serv_opaco", nome="Servidor Opaco",
        cargo="Diretor de Agencia", tier=TierTransparencia.T2_SERVIDOR,
        recusou_divulgar=True,
    ))

    resultado = eng.avaliar_todos()
    print(f"\n  Taxa de transparencia: {resultado['taxa_transparencia']}")
    print(f"  Conformes: {resultado['conformes']}")
    print(f"  Suspensos: {resultado['suspensos']}")
    print(f"  Banidos: {resultado['banidos']}")

    print("\n[DETALHES POR AGENTE]")
    for aid, res in resultado["resultados"].items():
        if not isinstance(res, dict):
            continue
        print(f"\n  {res['agente_nome']} ({res['cargo']})")
        print(f"    Tier: {res['tier']}")
        print(f"    Status: {res['status']}")
        print(f"    Transparencia: {res['pct_transparencia']}% "
              f"({res['dados_cumpridos']}/{res['dados_exigidos']})")
        if res["dados_faltantes"]:
            print(f"    Faltantes: {', '.join(res['dados_faltantes'])}")
        if res["violacoes"]:
            for v in res["violacoes"]:
                print(f"    VIOLACAO: {v}")

    # --- Fiscalizacao cidada ---
    print("\n\n[FISCALIZACAO CIDADA (sensores publicos)]")
    print("  (cidadao fiscaliza, reporta PUBLICO -- nao espiona)")
    eng.registrar_fiscalizacao(
        "Cidadao A", FerramentaFiscalizacao.NMAP,
        "site gov.br",
        "Porta 22 (SSH) aberta sem rate-limiting. Recomendo fail2ban.",
    )
    eng.registrar_fiscalizacao(
        "Cidadao B", FerramentaFiscalizacao.WIRESHARK,
        "app da Caixa",
        "App envia device_id + GPS para analytics.google.com sem consentimento.",
    )
    eng.registrar_fiscalizacao(
        "Cidadao C", FerramentaFiscalizacao.AUDIT_GASTO,
        "cartao corporativo deputado X",
        "Gasto R$ 47.000 em restaurante em 1 mes. Sem justificativa publica.",
    )
    eng.registrar_fiscalizacao(
        "Cidadao D", FerramentaFiscalizacao.OSMOCOM,
        "torre celular proxima ao Congresso",
        "Torre falsa (IMSI catcher) detectada. Captura IMSI de parlamentares.",
    )

    for f in eng.fiscalizacoes_recentes():
        print(f"\n  [{f['id']}] {f['ferramenta']}")
        print(f"    Fiscalizador: {f['fiscalizador']}")
        print(f"    Alvo: {f['alvo']}")
        print(f"    Achado: {f['achado']}")

    # --- Agentes exogenos ---
    print("\n\n[VOCABULARIO: AGENTES EXOGENOS (substitui 'espiao')]")
    for a in TipoAgenteExogeno:
        print(f"  {a.id:<20} {a.rotulo}")

    # --- Scorecard ---
    print("\n\n[SCORECARD]")
    sc = eng.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<28} {v}")

    # --- Filosofia ---
    print("\n" + "=" * 70)
    print("FILOSOFIA -- A Inversao da Vigilancia")
    print("=" * 70)
    print("""
A ASSIMETRIA ATUAL:

  O Estado sabe o que voce comeu no almoco (GPS + cartao + app).
  Voce nao sabe com quem o presidente almocou ontem ("seguranca nacional").

  A NSA grava suas mensagens. Voce nao pode ver a agenda do deputado.
  O app coleta sua localizacao. O servidor publico oculta seus gastos.

  Eles dizem: "confie no Estado. E para sua seguranca."
  Eles mentem quando pegos (Clapper: "not wittingly").
  Eles nao param. Adaptam-se.

O MUNDO DAS FADAS:

  "AI nao me vigia" e suicidio digital.
  Toda AI em nuvem loga. Toda. Sem excecao.
  ChatGPT, Claude, Gemini, Copilot -- todos retêm input.
  A unica AI que nao vigia roda no SEU hardware (llama.cpp, whisper.cpp).

  Dizer "eu nao tenho nada a esconder" e dizer "eu nao tenho nada a proteger".
  E abrir mao da propria dignidade.

A VIRADA DA REPUBLICA (P13):

  A Republica NAO promete "nao vamos te vigiar".
  O Estado ja vigia. Nao vai parar. Adaptar-se e sobreviver.

  A Republica promete o CONTRARIO:
  "Voce vai vigiar NOS de volta. Proporcional ao poder."

  - Cidadao comum: PRIVACIDADE TOTAL (P2).
  - Servidor: transparencia financeira + institucional.
  - Autoridade: vida publica 24/7 no cargo.
  - Presidente: ate o ovo do cafe da manha.

  Quem quer privacidade NAO ENTRA no poder publico.
  Aceitar cargo publico = aceitar CLAUSULA DA TRANSPARENCIA.
  O poder vem do povo. A transparencia volta pro povo.

CIDADAO COMO SENSOR:

  A Republica treina cada cidadao como SENSOR de contravigilancia.
  Nao espiao. SENSOR.
  O espiao coleta em SEGREDO para o Estado.
  O sensor ve em PUBLICO para a comunidade.

  O cidadao com nmap protege a PROPRIA comunidade.
  O cidadao com wireshark VE o que o app envia.
  O cidadao com osmocom DETECTA torres falsas.

  Dentro e fora do territorio.
  O brasileiro que viaja sabe que e interceptado.
  O brasileiro que recebe estrangeiro sabe o que observar.

  O Estado nao tem monopoly de vigilancia.
  O cidadao tem DIREITO de vigiar de volta.

O PRINCIPIO:

  Quem exerce poder publico PERDE privacidade proporcional ao poder.
  Quem nao exerce poder publico TEM privacidade total.

  Nao e vinganca. E SIMETRIA.
  Nao e opcional. E CONSTITUICAO.
""")


if __name__ == "__main__":
    _demo()
