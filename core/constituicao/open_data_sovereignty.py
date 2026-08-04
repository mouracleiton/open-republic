#!/usr/bin/env python3
"""
OpenDataSovereignty -- P14: Soberania de Dados do Cidadao
==========================================================
"Voce gerou, e seu. Quem coletou e custodiante revogavel, nao dono."

TESE:
  O povo e a maior PRODUTORA de dados da historia.
  E a menor DETENTORA.

  Cada clic, passo, compra, batimento, frase -- tudo vira dado.
  O dado sai do cidadao e vai para cima: Estado e empresa acumulam.
  O cidadao nao tem copia. Nao tem acesso. Nao tem controle.
  Nao tem nem o direito de saber QUEM tem o seu dado.

  Isso e EXTRACAO. O cidadao e a mina. A mineradora e quem coleta.

  P13 sem P14 e fiscal com olhos vendados:
  Como o cidadao vigia o Estado se nem o PROPRIO dado ele controla?

O PRINCIPIO (P14):

  Dados pessoais sao PRODUTOS do cidadao. Nao propriedade de quem coletou.
  Quem coleta (Estado, empresa, app) e CUSTODIANTE TEMPORARIO REVOGAVEL.
  O cidadao e o DONO. Sempre.

  Direitos derivados do dominio:
  1. ACESSO: cidadao tem copia integral de tudo que coletaram dele.
  2. PORTABILIDADE: cidadao leva seus dados para onde quiser.
  3. REVOGACAO: cidadao manda apagar. O custodiante obedece. Sem "backup".
  4. TRANSPARENCIA DE USO: cidadao sabe EXATAMENTE quem usou, quando, pra que.
  5. AUDITORIA: cidadao ve o log de acesso ao seu proprio dado.
  6. COMPENSACAO: se o dado gerou lucro, o cidadao recebe parte.

O FLUXO INVERTIDO:

  Hoje (extração):
    Cidadao produz -> App coleta -> Empresa agrega -> Estado acessa
    Cidadao recebe: ZERO. Nao tem copia. Nao tem controle. Nao tem poder.

  Republica (inversao):
    Cidadao produz -> Cidadao DETEM -> Custodiante temporario -> Revogavel
    Cidadao recebe: copia + log + poder de revogar + compensacao.

A DISTINCAO CRITICA:

  NAO e "proteger dados" (LGPD/GDPR fazem isso e falham).
  E DEVOLVER dados ao cidadao.

  LGPD diz: "empresa nao pode usar sem consentimento."
  P14 diz: "empresa que usou tem que DEVOLVER com log de uso."

  LGPD protege o dado NA empresa. P14 devolve o dado AO cidadao.

  A diferenca e de poder. LGPD mantem o dado com quem coletou.
  P14 transfere o poder de volta a quem produziu.

COMO P14 FAZ P13 FUNCIONAR:

  P13 diz: "cidadao vigia Estado proporcionalmente ao poder."

  Mas o cidadao vigia com QUAL dado?
  - Sem P14: o cidadao nao tem nem o SEU dado. Como vigia o Estado?
  - Com P14: o cidadao detem copia de tudo que gerou. Cruzamento possivel.

  P14 e o COMBUSTIVEL de P13. Sem combustivel, P13 e lei sem execucao.

OS 6 DIREITOS DE CUSTODIA (detalhados):

  D1. DIREITO DE COPIA:
     Tudo que coletaram do cidadao, o cidadao tem copia.
     Formato aberto (JSON, CSV). Nao proprietario.
     Atualizacao automatica (nao por pedido, por fluxo continuo).

  D2. DIREITO DE PORTABILIDADE:
     Cidadao leva dados para outro servico sem depender do atual.
     Formato padrao. Interoperabilidade obrigatoria.
     Nao ha "lock-in" de dados.

  D3. DIREITO DE REVOGACAO:
     "Apaga tudo." O custodiante apaga. SEM excecao.
     Sem "backup para seguranca nacional". Sem "retemos metadata".
     Revogacao e absoluta. Se duvida, revoga.

  D4. DIREITO DE LOG DE USO:
     Quem acessou meu dado? Quando? Pra que?
     O log e do CIDADAO, nao do custodiante.
     Se o custodiante usou, o cidadao sabe.

  D5. DIREITO DE AUDITORIA:
     Cidadao (ou cidadao fiscalizador eleito) audita o custodiante.
     O custodiante prova que cumpre D1-D4.
     Onus da prova e do CUSTODIANTE, nao do cidadao.

  D6. DIREITO DE COMPENSACAO:
     Se o dado gerou lucro (Big Tech, bancos, corretores de dado),
     o cidadao recebe parte. O dado nao e "gratis". E trabalho do cidadao.

O PROBLEMA DA AGREGACAO:

  O poder do dado nao esta no individual. Esta no AGREGADO.
  200 milhoes de historicos de GPS valem bilhoes. 1 historico nao.

  P14 resolve:
  - Dados AGREGADOS anonimizados sao patrimônio PUBLICO (P5).
  - Dados INDIVIDUAIS sao patrimônio do CIDADAO (P14).
  - A empresa que agrega PAGA pelo direito de agregar (D6).
  - O cidadao fiscalizador pode auditar SE a agregacao e realmente anonima.

O QUE P14 PROIBE:

  1. NAO COLETA SEM COPIA: coletou sem devolver copia? Crime.
  2. NAO RETEM SEM LOG: reteve sem logar acesso? Crime.
  3. NAO USA SEM COMPENSAR: lucrou com dado do cidadao sem pagar? Crime.
  4. NAO BLOQUEIA PORTABILIDADE: impediu cidadao de levar? Crime.
  5. NAO IGNORA REVOGACAO: cidadao mandou apagar e reteve? Crime.

A METAFORA DA MINA:

  O cidadao e a mina de dados mais rica do planeta.
  Hoje a mineradora (Big Tech + Estado) entra, extrai, leva.
  O cidadao recebe um "servico gratuito" que nao e gratuito.
  O servico e o PRECO que o cidadao paga com o proprio dado.

  P14 diz: a mina e do cidadao. A mineradora paga licenca.
  A licenca e revogavel. O extrativo devolve. O lucro compartilha.

Constituicao: P2 (autonomia do corpo, agora do dado),
P5 (transparencia), P13 (contravigilancia reciproca).

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime
from collections import defaultdict


# ============================================================================
# 1. ENUMS
# ============================================================================

class DireitoCustodia(Enum):
    """Os 6 direitos de custodia do cidadao sobre seu dado."""
    D1_COPIA = ("copia", "Copia integral em formato aberto, fluxo continuo")
    D2_PORTABILIDADE = ("portabilidade", "Portabilidade sem lock-in, formato padrao")
    D3_REVOGACAO = ("revogacao", "Revogacao absoluta: apaga tudo, sem excecao")
    D4_LOG_USO = ("log_uso", "Log de uso: quem acessou, quando, pra que")
    D5_AUDITORIA = ("auditoria", "Auditoria: custodiante prova que cumpre")
    D6_COMPENSACAO = ("compensacao", "Compensacao: se lucrou com dado, paga")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoCustodiante(Enum):
    """Quem custodia dados do cidadao."""
    EMPRESA = ("empresa", "Empresa privada (Big Tech, banco, corretor de dados)")
    ESTADO = ("estado", "Estado (orgao publico, agencia, sistema gov)")
    TERCEIRO = ("terceiro", "Terceiro (app gratuito, SDK, parceria de dados)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoDadoPessoal(Enum):
    """Categorias de dado pessoal que o cidadao produz."""
    LOCALIZACAO = ("localizacao", "GPS, antena celular, WiFi scan")
    COMUNICACAO = ("comunicacao", "Mensagens, emails, ligacoes, metadados")
    FINANCEIRO = ("financeiro", "Transacoes, saldos, historico de compra")
    BIOMETRICO = ("biometrico", "Digital, facial, voz, iris")
    NAVEGACAO = ("navegacao", "Historico, cookies, fingerprint")
    SOCIAL = ("social", "Grafo de relacoes, contatos, interacoes")
    SAUDE = ("saude", "Batimento, ciclo, sono, diagnostico")
    CONTEUDO = ("conteudo", "Fotos, videos, textos, buscas")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class StatusCustodia(Enum):
    """Status da conformidade de um custodiante com P14."""
    CONFORME = ("conforme", "Cumpre os 6 direitos de custodia")
    REVISAO = ("revisao", "Faltam direitos garantidos")
    SUSPENSO = ("suspenso", "Reteve dado apos revogacao = suspenso")
    BANIDO = ("banido", "Coletou sem copia/log/compensacao = banido")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class ViolacaoP14(Enum):
    """As 5 proibicoes de P14."""
    COLETA_SEM_COPIA = ("sem_copia", "Coletou sem devolver copia ao cidadao")
    RETEM_SEM_LOG = ("sem_log", "Reteve dado sem logar acesso")
    LUCRO_SEM_COMPENSAR = ("sem_comp", "Lucrou com dado sem compensar cidadao")
    BLOQUEIA_PORTABILIDADE = ("sem_port", "Impediu portabilidade (lock-in)")
    IGNORA_REVOGACAO = ("ignora_revog", "Cidadao revogou, custodiante reteve")

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
class EntradaLogAcesso:
    """Uma entrada no log de acesso ao dado do cidadao."""
    timestamp: str
    acessado_por: str       # nome do sistema/pessoa que acessou
    tipo_dado: TipoDadoPessoal
    proposito: str          # pra que usou
    cidadao_notificado: bool = False


@dataclass
class Custodiante:
    """Um custodiante de dados pessoais avaliado contra P14."""
    id: str
    nome: str
    tipo: TipoCustodiante
    # tipos de dado que coleta
    dados_coletados: List[TipoDadoPessoal] = field(default_factory=list)
    # direitos cumpridos
    fornece_copia: bool = False          # D1
    formato_aberto: bool = False         # D1 (JSON/CSV, nao proprietario)
    fluxo_continuo: bool = False         # D1 (nao por pedido)
    permite_portabilidade: bool = False  # D2
    sem_lock_in: bool = False            # D2
    permite_revogacao: bool = False      # D3
    revogacao_absoluta: bool = False     # D3 (sem "backup")
    mantem_log_acesso: bool = False      # D4
    log_e_do_cidadao: bool = False       # D4 (nao so do custodiante)
    permite_auditoria: bool = False      # D5
    onus_prova_custodiante: bool = False  # D5
    compensa_lucro: bool = False         # D6
    # violacoes
    coletou_sem_copia: bool = False
    reteve_sem_log: bool = False
    lucrou_sem_compensar: bool = False
    bloqueia_portabilidade: bool = False
    ignorou_revogacao: bool = False
    # metadata
    faturamento_anual_dados: float = 0.0  # quanto lucra com dados
    status: Optional[StatusCustodia] = None


@dataclass
class PedidoRevogacao:
    """Um pedido de revogacao de dados feito pelo cidadao."""
    id: str
    cidadao_id: str
    custodiante_id: str
    timestamp: str
    cumprido: bool = False
    cumprido_em: str = ""


# ============================================================================
# 3. ENGINE
# ============================================================================

class DataSovereigntyEngine:
    """
    Avalia custodiantes de dados contra P14 (soberania de dados do cidadao).

    O cidadao e DONO. O custodiante e TEMPORARIO REVOGAVEL.
    """

    def __init__(self) -> None:
        self.custodiantes: Dict[str, Custodiante] = {}
        self.revogacoes: List[PedidoRevogacao] = []

    def registrar(self, c: Custodiante) -> None:
        self.custodiantes[c.id] = c

    # -- avaliar custodiante -----------------------------------------------

    def avaliar(self, custodiante_id: str) -> Dict[str, Any]:
        """Avalia se um custodiante cumpre os 6 direitos de P14."""
        c = self.custodiantes.get(custodiante_id)
        if c is None:
            return {"erro": f"Custodiante nao encontrado: {custodiante_id}"}

        # Mapear direitos cumpridos
        # D6 (compensacao) so se aplica se o custodiante lucra com dados
        aplica_d6 = c.faturamento_anual_dados > 0
        direitos_map = {
            DireitoCustodia.D1_COPIA: c.fornece_copia and c.formato_aberto and c.fluxo_continuo,
            DireitoCustodia.D2_PORTABILIDADE: c.permite_portabilidade and c.sem_lock_in,
            DireitoCustodia.D3_REVOGACAO: c.permite_revogacao and c.revogacao_absoluta,
            DireitoCustodia.D4_LOG_USO: c.mantem_log_acesso and c.log_e_do_cidadao,
            DireitoCustodia.D5_AUDITORIA: c.permite_auditoria and c.onus_prova_custodiante,
            DireitoCustodia.D6_COMPENSACAO: (c.compensa_lucro if aplica_d6 else True),
        }
        cumpridos = [d for d, ok in direitos_map.items() if ok]
        # faltantes exclui D6 se nao se aplica
        faltantes = [d for d, ok in direitos_map.items()
                     if not ok and not (d == DireitoCustodia.D6_COMPENSACAO and not aplica_d6)]

        # Violacoes explicitas
        violacoes: List[str] = []
        if c.coletou_sem_copia:
            violacoes.append(f"{ViolacaoP14.COLETA_SEM_COPIA.rotulo}. CRIME.")
        if c.reteve_sem_log:
            violacoes.append(f"{ViolacaoP14.RETEM_SEM_LOG.rotulo}. CRIME.")
        if c.lucrou_sem_compensar:
            lucro = c.faturamento_anual_dados
            violacoes.append(
                f"{ViolacaoP14.LUCRO_SEM_COMPENSAR.rotulo}. "
                f"Lucro de R$ {lucro:,.0f}/ano com dado do cidadao sem pagar."
            )
        if c.bloqueia_portabilidade:
            violacoes.append(f"{ViolacaoP14.BLOQUEIA_PORTABILIDADE.rotulo}. CRIME.")
        if c.ignorou_revogacao:
            violacoes.append(
                f"{ViolacaoP14.IGNORA_REVOGACAO.rotulo}. CRIME. "
                f"Dado retido apos cidadao mandar apagar."
            )

        # Status
        if violacoes and any("CRIME" in v and "sem compensar" not in v for v in violacoes):
            status = StatusCustodia.BANIDO
        elif c.ignorou_revogacao:
            status = StatusCustodia.SUSPENSO
        elif faltantes:
            status = StatusCustodia.REVISAO
        else:
            status = StatusCustodia.CONFORME

        c.status = status

        pct = (len(cumpridos) / 6 * 100)

        return {
            "custodiante_id": c.id,
            "custodiante_nome": c.nome,
            "tipo": c.tipo.rotulo,
            "dados_coletados": [d.rotulo for d in c.dados_coletados],
            "direitos_cumpridos": [d.id for d in cumpridos],
            "direitos_faltantes": [d.id for d in faltantes],
            "pct_conformidade": round(pct, 1),
            "violacoes": violacoes,
            "faturamento_dados": c.faturamento_anual_dados,
            "status": f"{status.id} -- {status.rotulo}",
            "timestamp": datetime.now().isoformat(),
        }

    def avaliar_todos(self) -> Dict[str, Any]:
        resultados = {}
        for cid in self.custodiantes:
            resultados[cid] = self.avaliar(cid)
        conforme = sum(1 for r in resultados.values()
                       if isinstance(r, dict) and "conforme" in r.get("status", "").lower())
        total = len(resultados)
        return {
            "total_custodiantes": total,
            "conformes": conforme,
            "banidos": sum(1 for r in resultados.values()
                           if isinstance(r, dict) and "banido" in r.get("status", "").lower()),
            "suspensos": sum(1 for r in resultados.values()
                             if isinstance(r, dict) and "suspenso" in r.get("status", "").lower()),
            "resultados": resultados,
        }

    # -- revogacao ----------------------------------------------------------

    def registrar_revogacao(
        self, cidadao_id: str, custodiante_id: str,
    ) -> PedidoRevogacao:
        """Cidadao pede revogacao. Custodiante tem 72h para cumprir."""
        if custodiante_id not in self.custodiantes:
            # mesmo assim registra
            pass
        ped = PedidoRevogacao(
            id=f"REV-{len(self.revogacoes) + 1:06d}",
            cidadao_id=cidadao_id, custodiante_id=custodiante_id,
            timestamp=datetime.now().isoformat(),
        )
        self.revogacoes.append(ped)
        return ped

    def cumprir_revogacao(self, revogacao_id: str) -> bool:
        """Marca revogacao como cumprida."""
        for p in self.revogacoes:
            if p.id == revogacao_id:
                p.cumprido = True
                p.cumprido_em = datetime.now().isoformat()
                return True
        return False

    def revogacoes_pendentes(self) -> List[Dict[str, Any]]:
        return [
            {"id": p.id, "cidadao": p.cidadao_id, "custodiante": p.custodiante_id,
             "timestamp": p.timestamp}
            for p in self.revogacoes if not p.cumprido
        ]

    # -- calculo de compensacao --------------------------------------------

    def calcular_compensacao_devida(
        self, custodiante_id: str, num_cidadaos: int,
    ) -> Dict[str, Any]:
        """
        Calcula quanto o custodiante deve a cada cidadao por uso de dados.
        Base: 30% do faturamento com dados dividido pelo numero de cidadaos.
        """
        c = self.custodiantes.get(custodiante_id)
        if c is None or num_cidadaos == 0:
            return {"erro": "Custodiante ou cidadaos invalidos"}
        faturamento = c.faturamento_anual_dados
        compensacao_total = faturamento * 0.30
        por_cidadao = compensacao_total / num_cidadaos
        return {
            "custodiante": c.nome,
            "faturamento_dados_anual": faturamento,
            "compensacao_total_30pct": round(compensacao_total, 2),
            "num_cidadaos": num_cidadaos,
            "por_cidadao_anual": round(por_cidadao, 2),
            "por_cidadao_mensal": round(por_cidadao / 12, 2),
        }

    # -- scorecard ----------------------------------------------------------

    def scorecard(self) -> Dict[str, Any]:
        return {
            "custodiantes_avaliados": len(self.custodiantes),
            "direitos_custodia": len(list(DireitoCustodia)),
            "tipos_dado_pessoal": len(list(TipoDadoPessoal)),
            "tipos_custodiante": len(list(TipoCustodiante)),
            "violacoes_p14": len(list(ViolacaoP14)),
            "revogacoes_registradas": len(self.revogacoes),
            "revogacoes_pendentes": sum(1 for r in self.revogacoes if not r.cumprido),
            "principio": "P14 -- Soberania de Dados do Cidadao",
        }


# ============================================================================
# 4. DEMO
# ============================================================================

def _demo() -> None:
    eng = DataSovereigntyEngine()

    print("=" * 70)
    print("OpenDataSovereignty -- P14: O Dado e do Cidadao")
    print("=" * 70)

    # --- Os 6 direitos ---
    print(f"\n[OS {len(list(DireitoCustodia))} DIREITOS DE CUSTODIA]")
    for d in DireitoCustodia:
        print(f"  D{d.name.split('_')[0][-1]} ({d.id}) -- {d.rotulo}")

    # --- Custodiantes de teste ---
    print("\n\n[AVALIACAO DE CUSTODIANTES]")

    # Google-like: coleta tudo, nao devolve copia, lucra sem compensar
    eng.registrar(Custodiante(
        id="big_tech", nome="Big Tech Inc (hipotetico)",
        tipo=TipoCustodiante.EMPRESA,
        dados_coletados=[TipoDadoPessoal.LOCALIZACAO, TipoDadoPessoal.COMUNICACAO,
                         TipoDadoPessoal.NAVEGACAO, TipoDadoPessoal.SOCIAL,
                         TipoDadoPessoal.CONTEUDO],
        fornece_copia=True, formato_aberto=False, fluxo_continuo=False,
        permite_portabilidade=True, sem_lock_in=False,
        permite_revogacao=True, revogacao_absoluta=False,
        mantem_log_acesso=False, log_e_do_cidadao=False,
        permite_auditoria=False, onus_prova_custodiante=False,
        compensa_lucro=False,
        coletou_sem_copia=False,
        lucrou_sem_compensar=True,
        bloqueia_portabilidade=False,
        ignorou_revogacao=False,
        faturamento_anual_dados=200_000_000_000,  # R$ 200 bi
    ))

    # Banco: reteve sem log
    eng.registrar(Custodiante(
        id="banco_x", nome="Banco X (hipotetico)",
        tipo=TipoCustodiante.EMPRESA,
        dados_coletados=[TipoDadoPessoal.FINANCEIRO, TipoDadoPessoal.COMUNICACAO],
        mantem_log_acesso=False,
        reteve_sem_log=True,
        faturamento_anual_dados=50_000_000,
    ))

    # App gratuito: coletou sem copia nenhuma
    eng.registrar(Custodiante(
        id="app_gratis", nome="App Gratis Spyware (hipotetico)",
        tipo=TipoCustodiante.TERCEIRO,
        dados_coletados=[TipoDadoPessoal.LOCALIZACAO, TipoDadoPessoal.BIOMETRICO,
                         TipoDadoPessoal.CONTEUDO],
        coletou_sem_copia=True,
        faturamento_anual_dados=5_000_000,
    ))

    # Estado: ignora revogacao (sigilo eterno)
    eng.registrar(Custodiante(
        id="estado_sigilo", nome="Agencia Estatal Sigilo (hipotetico)",
        tipo=TipoCustodiante.ESTADO,
        dados_coletados=[TipoDadoPessoal.COMUNICACAO, TipoDadoPessoal.LOCALIZACAO,
                         TipoDadoPessoal.BIOMETRICO],
        ignorou_revogacao=True,
        permite_revogacao=False,
    ))

    # Conforme (Republica ideal)
    eng.registrar(Custodiante(
        id="conforme", nome="Servico da Republica (ideal)",
        tipo=TipoCustodiante.ESTADO,
        dados_coletados=[TipoDadoPessoal.LOCALIZACAO, TipoDadoPessoal.FINANCEIRO],
        fornece_copia=True, formato_aberto=True, fluxo_continuo=True,
        permite_portabilidade=True, sem_lock_in=True,
        permite_revogacao=True, revogacao_absoluta=True,
        mantem_log_acesso=True, log_e_do_cidadao=True,
        permite_auditoria=True, onus_prova_custodiante=True,
        compensa_lucro=False,  # estado nao lucra
    ))

    resultado = eng.avaliar_todos()
    print(f"\n  Conformes: {resultado['conformes']}")
    print(f"  Suspensos: {resultado['suspensos']}")
    print(f"  Banidos: {resultado['banidos']}")

    print("\n[DETALHES POR CUSTODIANTE]")
    for cid, res in resultado["resultados"].items():
        if not isinstance(res, dict):
            continue
        print(f"\n  {res['custodiante_nome']} ({res['tipo']})")
        print(f"    Status: {res['status']}")
        print(f"    Conformidade: {res['pct_conformidade']}%")
        print(f"    Dados coletados: {', '.join(res['dados_coletados'])}")
        if res["direitos_faltantes"]:
            print(f"    Direitos faltantes: {', '.join(res['direitos_faltantes'])}")
        if res["violacoes"]:
            for v in res["violacoes"]:
                print(f"    VIOLACAO: {v}")
        if res["faturamento_dados"] > 0:
            print(f"    Faturamento com dados: R$ {res['faturamento_dados']:,.0f}/ano")

    # --- Compensacao ---
    print("\n\n[CALCULO DE COMPENSACAO DEVIDA]")
    comp = eng.calcular_compensacao_devida("big_tech", 200_000_000)
    print(f"\n  {comp['custodiante']}")
    print(f"    Faturamento anual com dados: R$ {comp['faturamento_dados_anual']:,.0f}")
    print(f"    Compensacao total (30%): R$ {comp['compensacao_total_30pct']:,.0f}")
    print(f"    Cidadaos: {comp['num_cidadaos']:,}")
    print(f"    Por cidadao/ano: R$ {comp['por_cidadao_anual']:,.2f}")
    print(f"    Por cidadao/mes: R$ {comp['por_cidadao_mensal']:,.2f}")

    # --- Revogacao ---
    print("\n\n[REVOGACAO DE DADOS]")
    rev = eng.registrar_revogacao("cidadao_123", "big_tech")
    print(f"  Pedido: {rev.id}")
    print(f"  Cidadao: {rev.cidadao_id} -> Custodiante: {rev.custodiante_id}")
    print(f"  Cumprido: {rev.cumprido}")
    pendentes = eng.revogacoes_pendentes()
    print(f"  Pendentes: {len(pendentes)}")

    # --- Os 5 proibidos ---
    print("\n\n[OS 5 PROIBIDOS DE P14]")
    for v in ViolacaoP14:
        print(f"  {v.rotulo}")

    # --- Scorecard ---
    print("\n\n[SCORECARD]")
    sc = eng.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<28} {v}")

    # --- Filosofia ---
    print("\n" + "=" * 70)
    print("FILOSOFIA -- A Mina e do Cidadao")
    print("=" * 70)
    print("""
O POVO PRODUZ. O PODER ACUMULA.

  O cidadao e a maior produtora de dados da historia.
  Cada clic, passo, compra, batimento, frase -- tudo vira dado.
  Mas o cidadao nao detem o dado. Detem quem COLETOU.

  Google tem 10 anos da sua localizacao. Voce nao tem a copia.
  Banco tem 20 anos de transacoes. Voce nao tem consolidado.
  Meta tem seu grafo social. Voce nao tem o SEU grafo.
  Estado tem seus metadados. Voce nao sabe nem QUEM acessou.

  O dado saiu de voce. Voltou em forma de poder CONTRA voce.

A INVERSAO (P14):

  Dados pessoais sao PRODUTOS do cidadao.
  Nao propriedade de quem coletou.
  Quem coleta e CUSTODIANTE TEMPORARIO REVOGAVEL.
  O cidadao e o DONO. Sempre.

  D1. Copia integral em formato aberto.
  D2. Portabilidade sem lock-in.
  D3. Revogacao absoluta. Apaga tudo. Sem "backup".
  D4. Log de uso: quem acessou, quando, pra que.
  D5. Auditoria: custodiante prova que cumpre.
  D6. Compensacao: se lucrou, paga.

LGPD vs P14:

  LGPD protege o dado NA empresa.
  P14 devolve o dado AO cidadao.

  LGPD: "empresa nao pode usar sem consentimento."
  P14: "empresa que usou tem que DEVOLVER com log."

  A diferenca e de poder.
  LGPD mantem o dado com quem coletou.
  P14 transfere o poder de volta a quem produziu.

P14 E O COMBUSTIVEL DE P13:

  P13 diz: "cidadao vigia Estado proporcionalmente ao poder."
  Mas o cidadao vigia com QUAL dado?

  Sem P14: o cidadao nao tem nem o SEU dado.
  Como vigia o Estado se nao vigia a si mesmo?

  Com P14: o cidadao detem copia de tudo que gerou.
  Cruzamento possivel. Fiscalizacao real.

A METAFORA DA MINA:

  O cidadao e a mina de dados mais rica do planeta.
  Hoje a mineradora entra, extrai, leva.
  O cidadao recebe um "servico gratuito" que nao e gratuito.
  O servico e o PRECO que o cidadao paga com o proprio dado.

  P14 diz: a mina e do cidadao.
  A mineradora paga licenca.
  A licenca e revogavel.
  O extrativo devolve.
  O lucro compartilha.
""")


if __name__ == "__main__":
    _demo()
