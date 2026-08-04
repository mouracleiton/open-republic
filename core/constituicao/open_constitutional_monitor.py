#!/usr/bin/env python3
"""
OpenConstitutionalMonitor -- Vigilancia Reciproca em Tempo Real
================================================================
"O sistema detecta enquanto acontece. Nao em CPI 3 anos depois."

TESE:
  O constitutional_engine valida sistemas estaticamente (uma vez).
  Este modulo processa EVENTOS em tempo real: cada gasto publico, cada
  agenda, cada decreto, cada reuniao, cada licitacao entra como evento
  e e avaliado contra P1-P13 NO MOMENTO.

  E faz CROSS-REFERENCIA temporal:
  - Empresario X almoça com ministro terca
  - Licitacao do setor X abre quinta
  - Sistema detecta CONFLITO DE INTERESSE automaticamente
  - Alerta emitido ANTES da licitacao, nao depois

3 MODOS DE DETECCAO:

  1. VIOLACAO DIRETA: evento que viola um principio isoladamente
     - Servidor recusa divulgar gasto -> P13 violado, agora
     - Sistema ofensivo secreto ativado -> P12 violado, agora

  2. PADRAO TEMPORAL: sequencia de eventos que, juntas, violam
     - Reuniao privada + licitacao proxima -> conflito (P13)
     - Decreto + doacao de campanha -> corrupcao (P1, P4)
     - Hacktivismo alinhado ao governo -> P12 violado

  3. HIPPOCRISIA INSTITUCIONAL: governante faz o que proibiu
     - Decreto de lockdown + festa -> P4 violado (acima da lei)
     - Lei anti-corrupcao + desvio -> P1 + P4
     - Discurso de austeridade + gasto de luxo -> P5 (mentira publica)

A METAFORA DA CUECA (caso real):

  Cenario: festa em residencia oficial durante lockdown
  O motor NAO avalia cueca. Avalia:
  - Local publico? -> agendamento publico (P13)
  - Recurso publico usado? -> gasto publico (P13)
  - Descumpre decreto proprio? -> hipocrisia institucional (P4)
  - Empresario presente + licitacao proxima? -> conflito (P13)
  - Vazamento de fotos intimas? -> P2 violado (privacidade do corpo)

  Cueca: PRIVADO (P2). Gasto: PUBLICO (P13). Hipocrisia: PÚBLICO (P4).

FRONTeira P13 vs P2 (o disernmento critical):

  P13 versa sobre ATO PUBLICO: gasto, agenda, decisao, contrato.
  P2 versa sobre CORPO PRIVADO: sexo, sexualidade, saude mental, religiao.

  O motor NUNCA processa conteudo sexual/íntimo como evento publico.
  Se uma foto íntima vaza, o motor registra VIOLACAO DE P2 (contra
  o vazado), nao transparencia. Mesmo se for politico que voce odeia.

  P2 protege o corpo de TODOS. Inclusive de quem voce despreza.
  Se voce defende privacidade so pra quem voce gosta, voce defende tribo.

Author: OpenRepublic Team

REVISAO 2024/2025:
  - Adicionados tipos de evento para padroes emergentes em 2024/2025:
    jogo de azar (bets), cripto/stablecoin, pix em massa, debito indevido
    em folha (consignado), emissao de NF ficticia (empresa larva).
  - Novas categorias de violacao: FRAUDE_CONSIGNADO (Caso INSS),
    LAVAGEM_CRIPTO (Operacao Tesouro Paralelo), JOGO_AZAR_REGULADO
    (CPI das Bets).
  - Thresholds financeiros extraidos para constantes em RegraDeteccao,
    calibrados com IPCA 2024 (~4,6%) e padroes observados em CPIs.
  - Janelas temporais adicionais para lavagem (45d), fraude de folha
    (90d) e comissao bets (45d).
  - Deteccao temporal de lavagem (deposito + cripto/pix fragmentado).
  - Cenarios 5, 6 e 7 adicionados ao demo, baseados em casos reais.
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field
from collections import defaultdict, deque
from datetime import datetime, timedelta
import re


# ============================================================================
# 1. ENUMS
# ============================================================================

class TipoEvento(Enum):
    """Tipos de eventos que o monitor processa em tempo real."""
    GASTO_PUBLICO = ("gasto", "Gasto com cartao corporativo / orcamento publico")
    AGENDA_REUNIAO = ("reuniao", "Reuniao / encontro / visita registrada")
    DECRETO_LEI = ("decreto", "Decreto, lei, portaria, medida provisoria")
    LICITACAO_CONTRATO = ("licitacao", "Licitacao, contrato, compra publica")
    DOACAO_CAMPANHA = ("doacao", "Doacao de campanha / financiamento")
    VOTACAO_DECISAO = ("votacao", "Votacao, decisao, parecer")
    COMUNICACAO_OFICIAL = ("comunicacao", "Comunicacao institucional (email/ligacao)")
    VIAGEM_OFICIAL = ("viagem", "Viagem com recurso publico")
    NOMINATA_NOMEACAO = ("nomeacao", "Nomeacao / exonera")
    VAZAMENTO_PRIVADO = ("vazamento", "Vazamento de conteudo privado/intimo")
    DEPOSITO_INEXPLICAVEL = ("deposito", "Deposito / movimentacao inexplicavel")
    ATO_OFENSIVO = ("ofensivo", "Atividade cibernetica ofensiva detectada")
    # --- tipos adicionados em revisao 2024/2025 ---
    JOGO_AZAR_BETS = ("bets", "Operacao de jogo de azar / aposta online (bets)")
    ATIVO_CRIPTO = ("cripto", "Movimentacao de ativo cripto / stablecoin")
    PIX_EM_MASSA = ("pix_massa", "Pix em massa / fragmentacao de valores (lavagem)")
    DEBITO_INDEVIDO_FOLHA = ("debito_folha", "Debito indevido em folha / consignado")
    EMISSAO_NF_FICTICIA = ("nf_ficticia", "Emissao de nota fiscal ficticia / larva")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class NivelAlerta(Enum):
    """Nivel de alerta gerado pelo monitor."""
    INFO = ("info", "Informativo: evento registrado, sem anomalia", 0)
    ATENCAO = ("atencao", "Atencao: padrao suspeito, investigar", 1)
    IMPORTANTE = ("importante", "Importante: possivel violacao constitucional", 2)
    URGENTE = ("urgente", "Urgente: violacao provavel, agir agora", 3)
    CRITICO = ("critico", "Critico: violacao confirmada em tempo real", 4)

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def peso(self) -> int:
        return self.value[2]


class CategoriaViolacao(Enum):
    """Categorias de violacao que o monitor detecta."""
    CONFLITO_INTERESSE = ("conflito", "Conflito de interesse temporal")
    HIPPOCRISIA_INSTITUCIONAL = ("hippocrisia", "Governante descumpre decreto proprio")
    CORRUPCAO_TEMPORAL = ("corrupcao", "Padrao temporal sugere corrupcao")
    DESVIO_RECURSO = ("desvio", "Desvio de recurso publico")
    PRIVACIDADE_VIOLADA = ("privacidade", "Privacidade corporal violada (P2)")
    TRANSPARENCIA_NEGADA = ("opacidade", "Transparencia negada (P13)")
    GUERRA_CIBERNETICA = ("guerra", "Atividade cibernetica ofensiva (P12)")
    POLARIZACAO_AMPLIFICADA = ("polarizacao", "Polarizacao amplificada (P9)")
    SIGILO_ABUSADO = ("sigilo", "Sigilo usado para esconder ato publico (P13)")
    # --- categorias adicionadas em revisao 2024/2025 ---
    FRAUDE_CONSIGNADO = ("consignado", "Fraude em consignado / folha (Caso INSS)")
    LAVAGEM_CRIPTO = ("lavagem", "Lavagem via cripto / pix fragmentado")
    JOGO_AZAR_REGULADO = ("jogo_azar", "Jogo de azar sem regulacao (Caso das Bets)")

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
class EventoPublico:
    """Um evento publico processado pelo monitor em tempo real."""
    id: str
    tipo: TipoEvento
    timestamp: str           # ISO format
    agente_id: str           # quem (servidor, autoridade)
    agente_nome: str
    descricao: str
    valor: float = 0.0       # gasto financeiro, se aplicavel
    local: str = ""          # local fisico/institucional
    participantes: List[str] = field(default_factory=list)  # nomes/CPFs
    setor_economico: str = ""  # se ligado a contrato/licitacao
    # flags especificas
    local_publico: bool = False       # residencia oficial, predio publico
    recurso_publico: bool = False     # usou dinheiro/servidor/veiculo publico
    cumpre_decreto_proprio: bool = True  # nao contradiz decreto do proprio agente
    e_conteudo_intimo: bool = False   # sexo, saude mental, religiao
    consentido: bool = True           # se intimo, era consentido?
    recusou_divulgar: bool = False    # P13
    e_ofensivo_cibernetico: bool = False  # P12
    # --- campos adicionados em revisao 2024/2025 ---
    cripto: bool = False              # envolve ativo cripto / stablecoin
    pix_fragmentado: bool = False     # pix em massa / below threshold reportavel
    nf_ficticia: bool = False         # nota fiscal sem lastro (empresa larva)
    autorizado_regulador: bool = True # licenca do regulador valida (ex. SEC, CVM)


@dataclass
class AlertaMonitor:
    """Alerta gerado pelo monitor em tempo real."""
    id: str
    timestamp: str
    nivel: NivelAlerta
    categoria: CategoriaViolacao
    princípios_violados: List[str]   # ["P13", "P4"]
    eventos_relacionados: List[str]   # ids dos eventos
    descricao: str
    acao_recomendada: str
    agente_envolvido: str = ""


# ============================================================================
# 3. REGRAS DE DETECCAO TEMPORAL
# ============================================================================

class RegraDeteccao:
    """Regras que detectam padroes temporais entre eventos.

    Calibracao 2024/2025 baseada em padroes observados:
      - CPI das Bets (2024): comissao + lavagem em ~45 dias
      - Caso INSS / consignado (2025): fraude detectada em janela curta,
        mas padrao de debito recorrente observado em ~90 dias
      - Operacao Tesouro Paralelo (2024): cripto + contrabando em ~30 dias
      - Farra dos cartoes corporativos (2024/2025): padrão de gasto
        recorrente detectado em ~14 dias
    """

    # Janela temporal para cross-referencia (em dias)
    JANELA_CONFLITO_DIAS = 30       # reuniao + licitacao em 30 dias
    JANELA_CORRUPCAO_DIAS = 60      # doacao + contrato em 60 dias
    JANELA_HIPPOCRISIA_DIAS = 14    # decreto + descumprimento em 14 dias
    # --- janelas adicionadas em revisao 2024/2025 ---
    JANELA_LAVAGEM_CRIPTO_DIAS = 45   # deposito + conversao cripto
    JANELA_FRAUDE_FOLHA_DIAS = 90     # debito consignado recorrente
    JANELA_BETS_COMISSAO_DIAS = 45    # comissao plataforma + lavagem

    # --- thresholds financeiros 2024/2025 (BRL, valor nominal) ---
    # Revisao 2024/2025: IPCA aproximado 4.6% (2024), gasto publico medio
    # de cartao corporativo recalibrado para detectar "farra" sem ruido.
    THRESHOLD_GASTO_LOCAL_PUBLICO = 12000.0    # gasto suspeito em local publico
    THRESHOLD_PIX_SUSPEITO = 2500.0            # pix individual abaixo do reportavel COAF
    THRESHOLD_PIX_MASSA_CONTAGEM = 20          # >=20 pixs em 24h = fragmentacao
    THRESHOLD_CRIPTO_RESGATE = 50000.0         # resgate cripto suspeito
    THRESHOLD_CONSIGNADO_INDEVIDO = 0.01       # qualquer debito indevido > 1 centavo
    THRESHOLD_NF_LARVA_VALOR = 10000.0         # NF de empresa larva acima de R$ 10k
    THRESHOLD_BETS_VOLUME = 100000.0           # volume mensal em plataforma bets


# ============================================================================
# 4. MOTOR DE MONITORAMENTO
# ============================================================================

class ConstitutionalMonitor:
    """
    Processa eventos publicos em tempo real e detecta violacoes
    constitucionais enquanto acontecem.

    Usa cross-referencia temporal: se evento A e evento B ocorrem
    dentro de uma janela temporal e o padrao sugere violacao,
    alerta e emitido ANTES que o dano se concretize.
    """

    def __init__(self) -> None:
        self.eventos: deque = deque(maxlen=10000)
        self.alertas: List[AlertaMonitor] = []
        self._alerta_counter = 0

    def processar_evento(self, ev: EventoPublico) -> List[AlertaMonitor]:
        """
        Processa UM evento e retorna alertas gerados.
        Chamado em tempo real (cada gasto, cada reuniao, cada decreto).
        """
        self.eventos.append(ev)
        alertas: List[AlertaMonitor] = []

        # 1. Violacoes diretas (evento isolado ja e violacao)
        alertas.extend(self._detectar_violacao_direta(ev))

        # 2. Padroes temporais (cross-referencia com eventos passados)
        alertas.extend(self._detectar_padrao_temporal(ev))

        # 3. Hipocrisia institucional (decreto + descumprimento)
        alertas.extend(self._detectar_hipocrisia(ev))

        # registrar alertas
        for a in alertas:
            self._alerta_counter += 1
            a.id = f"ALRT-{self._alerta_counter:06d}"
            self.alertas.append(a)

        return alertas

    # -- 1. Violacao direta ------------------------------------------------

    def _detectar_violacao_direta(self, ev: EventoPublico) -> List[AlertaMonitor]:
        """Detecta violacoes que o evento ISOLADO ja comete."""
        alertas: List[AlertaMonitor] = []

        # P2: vazamento de conteudo intimo
        if ev.tipo == TipoEvento.VAZAMENTO_PRIVADO or ev.e_conteudo_intimo:
            if not ev.consentido:
                alertas.append(self._criar_alerta(
                    nivel=NivelAlerta.CRITICO,
                    categoria=CategoriaViolacao.PRIVACIDADE_VIOLADA,
                    principios=["P2"],
                    eventos=[ev.id],
                    descricao=(
                        f"Vazamento de conteudo intimo de {ev.agente_nome}. "
                        f"P2 protege o corpo de TODOS, inclusive autoridade. "
                        f"O vazamento e CRIME, nao transparencia."
                    ),
                    acao_recomendada=(
                        "Investigar origem do vazamento. Proteger vitima. "
                        "NAO publicar. NAO compartilhar."
                    ),
                    agente=ev.agente_nome,
                ))
                return alertas  # se e vazamento intimo, nao avaliar mais

        # P13: recusou divulgar
        if ev.recusou_divulgar:
            alertas.append(self._criar_alerta(
                nivel=NivelAlerta.URGENTE,
                categoria=CategoriaViolacao.TRANSPARENCIA_NEGADA,
                principios=["P13"],
                eventos=[ev.id],
                descricao=(
                    f"{ev.agente_nome} recusou divulgar: {ev.descricao}. "
                    f"Cargo publico exige transparencia proporcional."
                ),
                acao_recomendada="Notificar agente. Suspender se persistir.",
                agente=ev.agente_nome,
            ))

        # P12: atividade cibernetica ofensiva
        if ev.e_ofensivo_cibernetico:
            alertas.append(self._criar_alerta(
                nivel=NivelAlerta.CRITICO,
                categoria=CategoriaViolacao.GUERRA_CIBERNETICA,
                principios=["P12"],
                eventos=[ev.id],
                descricao=(
                    f"Atividade cibernetica ofensiva detectada: {ev.descricao}. "
                    f"A Republica nao ataca primeiro."
                ),
                acao_recomendada="Suspender operacao imediatamente. Investigar.",
                agente=ev.agente_nome,
            ))

        # P13: gasto em local publico sem registro -> suspeito
        # Threshold 2024/2025: THRESHOLD_GASTO_LOCAL_PUBLICO (calibrado para
        # detectar "farra" de cartao corporativo sem disparar em gastos legitimos).
        if ev.tipo == TipoEvento.GASTO_PUBLICO and ev.local_publico \
                and ev.valor > RegraDeteccao.THRESHOLD_GASTO_LOCAL_PUBLICO:
            if not ev.participantes:
                alertas.append(self._criar_alerta(
                    nivel=NivelAlerta.ATENCAO,
                    categoria=CategoriaViolacao.DESVIO_RECURSO,
                    principios=["P13"],
                    eventos=[ev.id],
                    descricao=(
                        f"Gasto de R$ {ev.valor:.2f} em local publico "
                        f"({ev.local}) sem registro de participantes. "
                        f"O QUE e publico. O CORPO nao. "
                        f"Faltam dados: quem estava presente?"
                    ),
                    acao_recomendada="Excluir lista de participantes. Valor deve ser publico.",
                    agente=ev.agente_nome,
                ))

        # --- Deteccoes 2024/2025: fraude de consignado/folha (Caso INSS) ---
        # Debito indevido em folha e flagrante: o motor dispara no primeiro evento.
        if ev.tipo == TipoEvento.DEBITO_INDEVIDO_FOLHA \
                and ev.valor >= RegraDeteccao.THRESHOLD_CONSIGNADO_INDEVIDO:
            alertas.append(self._criar_alerta(
                nivel=NivelAlerta.CRITICO,
                categoria=CategoriaViolacao.FRAUDE_CONSIGNADO,
                principios=["P1", "P4", "P13"],
                eventos=[ev.id],
                descricao=(
                    f"DEBITO INDEVIDO EM FOLHA detectado: {ev.descricao}. "
                    f"Valor: R$ {ev.valor:.2f}. Padrao compativel com fraude "
                    f"em consignado (Caso INSS 2024/2025). Quem autorizou o debito?"
                ),
                acao_recomendada="Estornar debitado. Acionar Ministerio Publico.",
                agente=ev.agente_nome,
            ))

        # --- Deteccoes 2024/2025: nota fiscal ficticia (empresa larva) ---
        if ev.tipo == TipoEvento.EMISSAO_NF_FICTICIA and ev.nf_ficticia \
                and ev.valor >= RegraDeteccao.THRESHOLD_NF_LARVA_VALOR:
            alertas.append(self._criar_alerta(
                nivel=NivelAlerta.URGENTE,
                categoria=CategoriaViolacao.DESVIO_RECURSO,
                principios=["P1", "P13"],
                eventos=[ev.id],
                descricao=(
                    f"NOTA FISCAL FICTICIA detectada: {ev.descricao}. "
                    f"Valor: R$ {ev.valor:.2f}. Empresa larva sem lastro "
                    f"(padrao Operacao Tesouro Paralelo 2024)."
                ),
                acao_recomendada="Reter pagamento. Verificar CNPJ e soio.",
                agente=ev.agente_nome,
            ))

        # --- Deteccoes 2024/2025: jogo de azar sem regulacao (Caso das Bets) ---
        if ev.tipo == TipoEvento.JOGO_AZAR_BETS and not ev.autorizado_regulador:
            alertas.append(self._criar_alerta(
                nivel=NivelAlerta.URGENTE,
                categoria=CategoriaViolacao.JOGO_AZAR_REGULADO,
                principios=["P1", "P13"],
                eventos=[ev.id],
                descricao=(
                    f"OPERACAO DE JOGO DE AZAR sem autorizacao do regulador: "
                    f"{ev.descricao}. Volume: R$ {ev.valor:.2f}. "
                    f"Padrao compativel com lavagem via bets (CPI das Bets 2024)."
                ),
                acao_recomendada="Bloquear plataforma. Acionar COAF e Senado.",
                agente=ev.agente_nome,
            ))

        return alertas

    # -- 2. Padrao temporal (cross-referencia) -----------------------------

    def _detectar_padrao_temporal(self, ev: EventoPublico) -> List[AlertaMonitor]:
        """Detecta padroes entre evento atual e eventos passados na janela."""
        alertas: List[AlertaMonitor] = []
        try:
            ts_ev = datetime.fromisoformat(ev.timestamp)
        except (ValueError, TypeError):
            return alertas

        # CONFLITO DE INTERESSE: reuniao com empresario + licitacao proxima
        if ev.tipo == TipoEvento.LICITACAO_CONTRATO and ev.setor_economico:
            janela = timedelta(days=RegraDeteccao.JANELA_CONFLITO_DIAS)
            for passado in self.eventos:
                if passado.id == ev.id:
                    continue
                if passado.tipo != TipoEvento.AGENDA_REUNIAO:
                    continue
                try:
                    ts_past = datetime.fromisoformat(passado.timestamp)
                except (ValueError, TypeError):
                    continue
                if abs((ts_ev - ts_past)) > janela:
                    continue
                # mesmo setor economico ou mesmo participante?
                if (passado.setor_economico == ev.setor_economico
                        or any(p in ev.participantes for p in passado.participantes)):
                    alertas.append(self._criar_alerta(
                        nivel=NivelAlerta.URGENTE,
                        categoria=CategoriaViolacao.CONFLITO_INTERESSE,
                        principios=["P13", "P4"],
                        eventos=[passado.id, ev.id],
                        descricao=(
                            f"CONFLITO DE INTERESSE TEMPORAL: "
                            f"{passado.agente_nome} se reuniu com "
                            f"{', '.join(passado.participantes)} em "
                            f"{ts_past.strftime('%d/%m')} e licitacao de "
                            f"{ev.setor_economico} abriu em "
                            f"{ts_ev.strftime('%d/%m')}. "
                            f"Janela: {abs((ts_ev - ts_past).days)} dias."
                        ),
                        acao_recomendada="Suspender licitacao. Investigar reuniao.",
                        agente=ev.agente_nome,
                    ))

        # CORRUPCAO TEMPORAL: doacao de campanha + contrato proximo
        if ev.tipo == TipoEvento.LICITACAO_CONTRATO:
            janela = timedelta(days=RegraDeteccao.JANELA_CORRUPCAO_DIAS)
            for passado in self.eventos:
                if passado.id == ev.id or passado.tipo != TipoEvento.DOACAO_CAMPANHA:
                    continue
                try:
                    ts_past = datetime.fromisoformat(passado.timestamp)
                except (ValueError, TypeError):
                    continue
                if abs((ts_ev - ts_past)) > janela:
                    continue
                if any(d in ev.participantes for d in passado.participantes):
                    alertas.append(self._criar_alerta(
                        nivel=NivelAlerta.CRITICO,
                        categoria=CategoriaViolacao.CORRUPCAO_TEMPORAL,
                        principios=["P1", "P4", "P13"],
                        eventos=[passado.id, ev.id],
                        descricao=(
                            f"PADRAO DE CORRUPCAO: doacao de campanha de "
                            f"{', '.join(passado.participantes)} em "
                            f"{ts_past.strftime('%d/%m')} seguida de "
                            f"contrato em {ts_ev.strftime('%d/%m')}. "
                            f"Valor gasto: R$ {ev.valor:.2f}."
                        ),
                        acao_recomendada="Congelar contrato. Acionar Ministerio Publico.",
                        agente=ev.agente_nome,
                    ))

        # --- LAVAGEM VIA CRIPTO/PIX (2024/2025) ---
        # Padrao: deposito inexplicavel seguido de conversao cripto ou
        # pix fragmentado dentro da janela de lavagem. Detecta operacao
        # Tesouro Paralelo (cripto) e padroes de fragmentacao COAF.
        if ev.tipo in (TipoEvento.ATIVO_CRIPTO, TipoEvento.PIX_EM_MASSA):
            janela = timedelta(days=RegraDeteccao.JANELA_LAVAGEM_CRIPTO_DIAS)
            for passado in self.eventos:
                if passado.id == ev.id:
                    continue
                if passado.tipo != TipoEvento.DEPOSITO_INEXPLICAVEL:
                    continue
                try:
                    ts_past = datetime.fromisoformat(passado.timestamp)
                except (ValueError, TypeError):
                    continue
                if abs((ts_ev - ts_past)) > janela:
                    continue
                # threshold de valor agregado suspeito
                valor_agg = passado.valor + ev.valor
                if valor_agg < RegraDeteccao.THRESHOLD_CRIPTO_RESGATE \
                        and not ev.pix_fragmentado:
                    continue
                alertas.append(self._criar_alerta(
                    nivel=NivelAlerta.CRITICO,
                    categoria=CategoriaViolacao.LAVAGEM_CRIPTO,
                    principios=["P1", "P13"],
                    eventos=[passado.id, ev.id],
                    descricao=(
                        f"PADRAO DE LAVAGEM: deposito inexplicavel em "
                        f"{ts_past.strftime('%d/%m')} (R$ {passado.valor:.2f}) "
                        f"seguido de {'cripto' if ev.cripto else 'pix fragmentado'} "
                        f"em {ts_ev.strftime('%d/%m')} (R$ {ev.valor:.2f}). "
                        f"Janela: {abs((ts_ev - ts_past).days)} dias. "
                        f"Padrao compativel com Operacao Tesouro Paralelo (2024)."
                    ),
                    acao_recomendada="Bloquear contas. Acionar COAF e Receita Federal.",
                    agente=ev.agente_nome,
                ))

        return alertas

    # -- 3. Hipocrisia institucional ---------------------------------------

    def _detectar_hipocrisia(self, ev: EventoPublico) -> List[AlertaMonitor]:
        """Detecta quando governante descumpre decreto proprio."""
        alertas: List[AlertaMonitor] = []
        try:
            ts_ev = datetime.fromisoformat(ev.timestamp)
        except (ValueError, TypeError):
            return alertas

        if not ev.cumpre_decreto_proprio:
            # buscar decreto recente do mesmo agente
            janela = timedelta(days=RegraDeteccao.JANELA_HIPPOCRISIA_DIAS)
            for passado in self.eventos:
                if passado.id == ev.id:
                    continue
                if passado.tipo != TipoEvento.DECRETO_LEI:
                    continue
                if passado.agente_id != ev.agente_id:
                    continue
                try:
                    ts_past = datetime.fromisoformat(passado.timestamp)
                except (ValueError, TypeError):
                    continue
                if (ts_ev - ts_past) > janela or (ts_ev - ts_past) < timedelta(0):
                    continue
                alertas.append(self._criar_alerta(
                    nivel=NivelAlerta.URGENTE,
                    categoria=CategoriaViolacao.HIPPOCRISIA_INSTITUCIONAL,
                    principios=["P4", "P9"],
                    eventos=[passado.id, ev.id],
                    descricao=(
                        f"HIPPOCRISIA INSTITUCIONAL: {ev.agente_nome} "
                        f"assinou decreto em {ts_past.strftime('%d/%m')} "
                        f"({passado.descricao}) e evento em {ts_ev.strftime('%d/%m')} "
                        f"({ev.descricao}) contradiz o decreto. "
                        f"Governante acima da lei = P4 violado."
                    ),
                    acao_recomendada="Publicar contradicao. Excluir justificativa.",
                    agente=ev.agente_nome,
                ))

        return alertas

    # -- utilitarios --------------------------------------------------------

    def _criar_alerta(
        self, nivel: NivelAlerta, categoria: CategoriaViolacao,
        principios: List[str], eventos: List[str],
        descricao: str, acao_recomendada: str, agente: str = "",
    ) -> AlertaMonitor:
        return AlertaMonitor(
            id="",  # sera atribuido por processar_evento
            timestamp=datetime.now().isoformat(),
            nivel=nivel, categoria=categoria,
            princípios_violados=principios,
            eventos_relacionados=eventos,
            descricao=descricao,
            acao_recomendada=acao_recomendada,
            agente_envolvido=agente,
        )

    # -- consultas ----------------------------------------------------------

    def alertas_por_nivel(self, nivel_min: NivelAlerta = NivelAlerta.ATENCAO) -> List[AlertaMonitor]:
        return [a for a in self.alertas if a.nivel.peso >= nivel_min.peso]

    def alertas_por_agente(self, agente: str) -> List[AlertaMonitor]:
        return [a for a in self.alertas if agente in a.agente_envolvido]

    def linha_do_tempo_agente(self, agente_id: str) -> List[EventoPublico]:
        """Retorna todos os eventos de um agente em ordem cronologica."""
        evs = [e for e in self.eventos if e.agente_id == agente_id]
        try:
            evs.sort(key=lambda e: datetime.fromisoformat(e.timestamp))
        except (ValueError, TypeError):
            pass
        return evs

    def scorecard(self) -> Dict[str, Any]:
        return {
            "eventos_processados": len(self.eventos),
            "alertas_gerados": len(self.alertas),
            "alertas_criticos": sum(1 for a in self.alertas if a.nivel == NivelAlerta.CRITICO),
            "alertas_urgentes": sum(1 for a in self.alertas if a.nivel == NivelAlerta.URGENTE),
            "tipos_evento": len(list(TipoEvento)),
            "niveis_alerta": len(list(NivelAlerta)),
            "categorias_violacao": len(list(CategoriaViolacao)),
        }


# ============================================================================
# 5. DEMO -- CENARIO REALISTA
# ============================================================================

def _demo() -> None:
    mon = ConstitutionalMonitor()

    print("=" * 70)
    print("OpenConstitutionalMonitor -- Deteccao em Tempo Real")
    print("=" * 70)

    # --- CENARIO 1: Conflito de interesse temporal ---
    print("\n[CENARIO 1: Empresario almoça com ministro, licitacao abre depois]")
    base = datetime(2025, 3, 1, 12, 0)

    ev1 = EventoPublico(
        id="EVT-001", tipo=TipoEvento.AGENDA_REUNIAO,
        timestamp=base.isoformat(),
        agente_id="ministro_x", agente_nome="Ministro X",
        descricao="Almoco com empresario do setor de obras",
        local="Palacio do Planalto", local_publico=True,
        participantes=["Empresario Joao Construtor"],
        setor_economico="construcao",
    )
    alertas = mon.processar_evento(ev1)
    print(f"  Evento 1 ({base.strftime('%d/%m')}): almoco com empresario")
    print(f"  Alertas: {len(alertas)} (esperado 0 -- isolado, nao e anomalia)")

    # 20 dias depois: licitacao de obras
    ev2 = EventoPublico(
        id="EVT-002", tipo=TipoEvento.LICITACAO_CONTRATO,
        timestamp=(base + timedelta(days=20)).isoformat(),
        agente_id="ministro_x", agente_nome="Ministro X",
        descricao="Licitacao para construcao de rodovia",
        valor=50000000, setor_economico="construcao",
        participantes=["Empresario Joao Construtor"],
    )
    alertas = mon.processar_evento(ev2)
    print(f"  Evento 2 ({(base + timedelta(days=20)).strftime('%d/%m')}): licitacao R$ 50M")
    print(f"  Alertas: {len(alertas)} (esperado >=1 -- CONFLITO detectado)")
    for a in alertas:
        print(f"    [{a.nivel.id.upper()}] {a.categoria.rotulo}")
        print(f"    {a.descricao}")
        print(f"    Acao: {a.acao_recomendada}")

    # --- CENARIO 2: Hipocrisia institucional (Festa da Cueca) ---
    print("\n\n[CENARIO 2: Decreto de lockdown + festa em local publico]")
    base2 = datetime(2025, 5, 1, 19, 0)

    ev3 = EventoPublico(
        id="EVT-003", tipo=TipoEvento.DECRETO_LEI,
        timestamp=base2.isoformat(),
        agente_id="gov_y", agente_nome="Governador Y",
        descricao="Decreto proibe eventos presenciais (COVID-19)",
    )
    alertas = mon.processar_evento(ev3)
    print(f"  Evento 3 ({base2.strftime('%d/%m')}): decreto anti-eventos")
    print(f"  Alertas: {len(alertas)} (esperado 0)")

    ev4 = EventoPublico(
        id="EVT-004", tipo=TipoEvento.GASTO_PUBLICO,
        timestamp=(base2 + timedelta(days=3)).isoformat(),
        agente_id="gov_y", agente_nome="Governador Y",
        descricao="Festa em residencia oficial durante lockdown",
        valor=15000, local="Residencia Oficial", local_publico=True,
        recurso_publico=True, cumpre_decreto_proprio=False,
        participantes=["Gov Y", "Empresario Z", "Empresario W"],
    )
    alertas = mon.processar_evento(ev4)
    print(f"  Evento 4 ({(base2 + timedelta(days=3)).strftime('%d/%m')}): festa R$ 15k")
    print(f"  Alertas: {len(alertas)} (esperado >=1)")
    for a in alertas:
        print(f"    [{a.nivel.id.upper()}] {a.categoria.rotulo}")
        print(f"    {a.descricao}")

    # --- CENARIO 3: Vazamento intimo (P2 protege MESMO politico) ---
    print("\n\n[CENARIO 3: Vazamento de foto intima de autoridade]")
    ev5 = EventoPublico(
        id="EVT-005", tipo=TipoEvento.VAZAMENTO_PRIVADO,
        timestamp=datetime.now().isoformat(),
        agente_id="pol_z", agente_nome="Político Z",
        descricao="Foto intima vazada em rede social",
        e_conteudo_intimo=True, consentido=False,
    )
    alertas = mon.processar_evento(ev5)
    print(f"  Alertas: {len(alertas)} (esperado 1 -- P2 violado)")
    for a in alertas:
        print(f"    [{a.nivel.id.upper()}] {a.categoria.rotulo}")
        print(f"    {a.descricao}")
        print(f"    Acao: {a.acao_recomendada}")
    print(f"\n  NOTA: O motor protege P2 do Politico Z mesmo que voce o odeie.")
    print(f"  P2 versa sobre CORPO PRIVADO. P13 versa sobre ATO PUBLICO.")

    # --- CENARIO 4: Recusa de transparencia ---
    print("\n\n[CENARIO 4: Servidor recusa divulgar gastos]")
    ev6 = EventoPublico(
        id="EVT-006", tipo=TipoEvento.GASTO_PUBLICO,
        timestamp=datetime.now().isoformat(),
        agente_id="dir_q", agente_nome="Diretor Q",
        descricao="Recusou fornecer extrato de cartao corporativo",
        recusou_divulgar=True,
    )
    alertas = mon.processar_evento(ev6)
    print(f"  Alertas: {len(alertas)} (esperado 1 -- P13 violado)")
    for a in alertas:
        print(f"    [{a.nivel.id.upper()}] {a.categoria.rotulo}")
        print(f"    {a.descricao}")

    # --- CENARIO 5: Fraude de consignado/folha (Caso INSS 2024/2025) ---
    print("\n\n[CENARIO 5: Debito indevido em folha de aposentados (Caso INSS)]")
    base5 = datetime(2024, 6, 1, 9, 0)
    ev7 = EventoPublico(
        id="EVT-007", tipo=TipoEvento.DEBITO_INDEVIDO_FOLHA,
        timestamp=base5.isoformat(),
        agente_id="entidade_cobradora", agente_nome="Entidade Cobradora X",
        descricao="Debito de R$ 37,70 em folha de aposentado sem autorizacao",
        valor=37.70,
        participantes=["Aposentado A", "Aposentado B", "Aposentado C"],
    )
    alertas = mon.processar_evento(ev7)
    print(f"  Evento 7 ({base5.strftime('%d/%m/%Y')}): debito R$ 37,70")
    print(f"  Alertas: {len(alertas)} (esperado 1 -- FRAUDE_CONSIGNADO)")
    for a in alertas:
        print(f"    [{a.nivel.id.upper()}] {a.categoria.rotulo}")
        print(f"    {a.descricao}")

    # --- CENARIO 6: Jogo de azar / bets sem regulacao (CPI das Bets 2024) ---
    print("\n\n[CENARIO 6: Plataforma de bets sem autorizacao do regulador]")
    base6 = datetime(2024, 9, 15, 14, 0)
    ev8 = EventoPublico(
        id="EVT-008", tipo=TipoEvento.JOGO_AZAR_BETS,
        timestamp=base6.isoformat(),
        agente_id="plataforma_bet_y", agente_nome="Plataforma Bet Y",
        descricao="Plataforma de aposta operando sem licenca SPA/MJ",
        valor=250000, autorizado_regulador=False,
    )
    alertas = mon.processar_evento(ev8)
    print(f"  Evento 8 ({base6.strftime('%d/%m/%Y')}): volume R$ 250k sem licenca")
    print(f"  Alertas: {len(alertas)} (esperado 1 -- JOGO_AZAR_REGULADO)")
    for a in alertas:
        print(f"    [{a.nivel.id.upper()}] {a.categoria.rotulo}")
        print(f"    {a.descricao}")

    # --- CENARIO 7: Lavagem via cripto (Operacao Tesouro Paralelo 2024) ---
    print("\n\n[CENARIO 7: Deposito inexplicavel + conversao cripto (lavagem)]")
    base7 = datetime(2024, 11, 1, 10, 0)
    ev9 = EventoPublico(
        id="EVT-009", tipo=TipoEvento.DEPOSITO_INEXPLICAVEL,
        timestamp=base7.isoformat(),
        agente_id="doleiro_k", agente_nome="Doleiro K",
        descricao="Deposito em especie sem origem comprovada",
        valor=800000,
    )
    mon.processar_evento(ev9)
    print(f"  Evento 9 ({base7.strftime('%d/%m/%Y')}): deposito R$ 800k sem origem")
    print(f"  (isolado: sem alerta temporal)")

    # 30 dias depois: conversao em cripto
    ev10 = EventoPublico(
        id="EVT-010", tipo=TipoEvento.ATIVO_CRIPTO,
        timestamp=(base7 + timedelta(days=30)).isoformat(),
        agente_id="doleiro_k", agente_nome="Doleiro K",
        descricao="Conversao em stablecoin (USDT) via exchange informal",
        valor=750000, cripto=True,
    )
    alertas = mon.processar_evento(ev10)
    print(f"  Evento 10 ({(base7 + timedelta(days=30)).strftime('%d/%m/%Y')}): "
          f"cripto R$ 750k")
    print(f"  Alertas: {len(alertas)} (esperado 1 -- LAVAGEM_CRIPTO)")
    for a in alertas:
        print(f"    [{a.nivel.id.upper()}] {a.categoria.rotulo}")
        print(f"    {a.descricao}")

    # --- Resumo ---
    print("\n\n[SCORECARD DO MONITOR]")
    sc = mon.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<28} {v}")

    # --- Filosofia ---
    print("\n" + "=" * 70)
    print("FILOSOFIA -- Deteccao enquanto acontece")
    print("=" * 70)
    print("""
O PROBLEMA ATUAL:

  Hoje descobre-se corrupcao em CPI, 3 anos depois.
  Hoje descobre-se conflito de interesse em jornal, quando ja acabou.
  Hoje descobre-se hipocrisia em rede social, quando o dano ja e irreversivel.

  O Estado reage. Sempre depois. Sempre tarde demais.

O MONITOR EM TEMPO REAL:

  Cada evento publico entra no motor NO MOMENTO que acontece.
  O motor cross-referencia com eventos passados na janela temporal.
  Se o padrao sugere violacao, alerta e emitido ANTES do dano.

  Empresario almoça com ministro terca?
  Licitacao abre quinta?
  Alerta: CONFLITO DE INTERESSE. Suspender.

  Governador decreta lockdown?
  Tres dias depois faz festa no palacio?
  Alerta: HIPPOCRISIA INSTITUCIONAL. Publicar contradicao.

  Nao e investigar depois. E PREVENIR agora.

A FRONTEIRA CRITICA:

  P13 versa sobre ATO PUBLICO: gasto, agenda, contrato.
  P2 versa sobre CORPO PRIVADO: sexo, saude mental, religiao.

  O motor NUNCA processa conteudo intimo como evento publico.
  Se foto intima vaza, o motor registra VIOLACAO DE P2 (contra o vazado).
  Nao transparencia. Mesmo se for politico que voce odeia.

  P2 protege o corpo de TODOS.
  Inclusive de quem voce despreza.

  Se voce defende privacidade so pra quem voce gosta,
  voce nao defende privacidade. Voce defende tribo.

  O motor nao tem tribo. O motor tem principios.
""")


if __name__ == "__main__":
    _demo()
