#!/usr/bin/env python3
"""
OpenChildFoodSecurity -- Fome Zero Infantil com Rastreio
==========================================================
"A crianca com fome precisa de comida AGORA.
 Mas como garantir que a comida CHEGOU?"
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple


# ============================================================
# ENUMS
# ============================================================

class SituacaoMoradia(Enum):
    COM_FAMILIA = "com_familia"          # mora com familia em casa/ape
    SEM_ABIGO = "sem_abrigo"             # morador de rua
    ABRIGO = "abrigo"                    # abrigo/casa de passagem
    OCUPACAO = "ocupacao"                # ocupacao/coletivo
    FOSTER = "foster"                    # acolhimento institucional

    @property
    def rotulo(self) -> str:
        return {
            "com_familia": "Mora com familia",
            "sem_abrigo": "Morador de rua (sem abrigo)",
            "abrigo": "Em abrigo / casa de passagem",
            "ocupacao": "Em ocupacao / coletivo",
            "foster": "Em acolhimento institucional (CONANDA)",
        }[self.value]


class TipoResponsavel(Enum):
    PAI_MAE = "pai_mae"
    UM_GENITOR = "um_genitor"
    AVO = "avo"
    PARENTESCO = "parentesco"     # tio, irmao maior, etc
    TUTOR = "tutor_legal"
    ESTADO = "estado"             # CONANDA / conselho tutelar
    NENHUM = "nenhum"             # crianca sozinha

    @property
    def rotulo(self) -> str:
        return {
            "pai_mae": "Pai e mae",
            "um_genitor": "Um genitor",
            "avo": "Avo(s)",
            "parentesco": "Parente (tio, irmao)",
            "tutor_legal": "Tutor legal",
            "estado": "Estado (conselho tutelar)",
            "nenhum": "Nenhum (crianca sozinha)",
        }[self.value]


class FonteRenda(Enum):
    FORMAL = "formal"              # carteira assinada
    INFORMAL = "informal"          # bico, ambulante
    BOLSA = "bolsa_familia"        # bolsa familia
    APOSENTADORIA = "aposentadoria"
    NENHUMA = "nenhuma"            # sem renda
    INDEFINIDA = "indefinida"      # nao sabe

    @property
    def rotulo(self) -> str:
        return {
            "formal": "Trabalho formal (CLT)",
            "informal": "Trabalho informal",
            "bolsa_familia": "Bolsa Familia (R$600 + R$150/crianca)",
            "aposentadoria": "Aposentadoria / BPC",
            "nenhuma": "Sem renda",
            "indefinida": "Renda indefinida",
        }[self.value]


class ProgramaAlimentacao(Enum):
    BOLSA_FAMILIA = "bolsa_familia"
    MERENDA = "merenda_escolar"
    LEITE = "programa_leite"
    MESA_BRASIL = "mesa_brasil_sesc"
    ACAO_CIDADANIA = "acao_cidadania"
    BANCO_ALIMENTOS = "banco_alimentos"
    RESTAURANTE_POPULAR = "restaurante_popular"
    COZINHA_COMUNITARIA = "cozinha_comunitaria"
    IGREJA = "igreja_ong_religiosa"
    NENHUM = "nenhum"

    @property
    def rotulo(self) -> str:
        return {
            "bolsa_familia": "Bolsa Familia (transferencia R$)",
            "merenda_escolar": "Merenda Escolar (PNAE)",
            "programa_leite": "Programa Nacional de Incentivo ao Consumo do Leite",
            "mesa_brasil_sesc": "Mesa Brasil SESC",
            "acao_cidadania": "Acao da Cidadania Contra a Fome",
            "banco_alimentos": "Banco de Alimentos (empresa/ONG)",
            "restaurante_popular": "Restaurante Popular (governo)",
            "cozinha_comunitaria": "Cozinha Comunitaria",
            "igreja_ong_religiosa": "Igreja / ONG religiosa",
            "nenhum": "Nenhum",
        }[self.value]


class TipoComprovacao(Enum):
    FOTO = "foto_prato"              # foto da comida servida
    ASSINATURA = "assinatura"        # responsavel assina que recebeu
    BIOMETRIA = "biometria"          # digital do responsavel
    GPS = "gps_entrega"              # GPS de entrega (se entrega)
    FREQUENCIA = "frequencia_escolar" # crianca foi a escola? comeu la?
    PESO = "peso_crianca"            # acompanhamento nutricional
    DEPOIMENTO = "depoimento"        # vizinho/comunidade confirma
    SENSORES = "sensor_refeicao"     # sensor de consumo (futuro)


class StatusFiscalizacao(Enum):
    CONFIRMADO = "confirmado"        # comida chegou, comprovado
    PARCIAL = "parcial"              # chegou mas parcial / atrasado
    NAO_RECEBEU = "nao_recebeu"      # nao chegou
    DESVIO = "desvio"                # comida desviada (fraude)
    SEM_DADO = "sem_dado"            # ninguem verificou


class NivelRisco(Enum):
    CRITICO = "critico"      # fome AGORA + sem rede
    ALTO = "alto"            # fome + rede parcial
    MEDIO = "medio"          # inseguranca alimentar
    BAIXO = "baixo"          # alimentado, monitorar


# ============================================================
# DATACLASSES
# ============================================================

@dataclass
class Crianca:
    """Identidade de uma crianca sob risco alimentar."""
    id: str
    idade: int
    situacao_moradia: SituacaoMoradia
    tipo_responsavel: TipoResponsavel
    fonte_renda_responsavel: FonteRenda
    renda_familiar_mensal: float  # R$
    programas_ativos: List[ProgramaAlimentacao] = field(default_factory=list)
    escola: bool = False
    peso_kg: Optional[float] = None
    altura_cm: Optional[float] = None
    bairro: str = ""
    municipio: str = ""
    uf: str = ""


@dataclass
class EntregaAlimento:
    """Registro de uma entrega/acao de alimentacao."""
    id: str
    crianca_id: str
    programa: ProgramaAlimentacao
    data: str  # ISO
    tipo: str  # "marmita", "cesta", "leite", "transferencia_R$"
    quantidade: str  # "1 prato", "5kg arroz", "R$150"
    comprovacao: List[TipoComprovacao] = field(default_factory=list)
    status: StatusFiscalizacao = StatusFiscalizacao.SEM_DADO
    hash_verificacao: str = ""
    fiscal_id: str = ""  # quem fiscalizou


@dataclass
class EntidadeExistente:
    """Entidade que JA trabalha com fome infantil hoje."""
    nome: str
    tipo: str           # "governo", "ong", "religiosa", "mista"
    escopo: str         # "nacional", "estadual", "municipal", "local"
    atendimento: str    # quantas pessoas/ano
    modelo: str         # "transferencia", "cesta", "marmita", "merenda"
    gap: str           # o que ela NAO cobre
    suficiente: bool    # e suficiente?


# ============================================================
# ENGINE
# ============================================================

class ChildFoodSecurity:
    """
    Logica: crianca -> diagnostico -> acao -> comprovacao -> fiscalizacao.

    FLUXO:
    1. IDENTIFICAR: Quem e a crianca? Onde mora? Tem responsavel?
    2. DIAGNOSTICAR: Qual o nivel de risco? Tem renda? Tem ajuda?
    3. AGIR: Qual programa atende? Comida AGORA.
    4. COMPROVAR: A comida chegou? Como sabemos?
    5. FISCALIZAR: Quem verifica? Como detectar desvio?
    """

    def __init__(self):
        self.criancas: Dict[str, Crianca] = {}
        self.entregas: List[EntregaAlimento] = []
        self.fiscalizacoes: List[Dict[str, Any]] = []

    # === 1. IDENTIFICAR ===

    def cadastrar_crianca(self, c: Crianca) -> str:
        self.criancas[c.id] = c
        return c.id

    def perfil(self, c: Crianca) -> Dict[str, Any]:
        """Monta o perfil completo da crianca."""
        tem_responsavel = c.tipo_responsavel != TipoResponsavel.NENHUM
        tem_renda = c.fonte_renda_responsavel not in [FonteRenda.NENHUMA, FonteRenda.INDEFINIDA]
        tem_programa = len(c.programas_ativos) > 0
        tem_escola = c.escola

        # Desnutricao (classificacao OMS)
        desnutricao = None
        if c.peso_kg and c.altura_cm and c.idade > 0:
            imc = c.peso_kg / ((c.altura_cm / 100) ** 2)
            if imc < 14:
                desnutricao = "severa"
            elif imc < 16:
                desnutricao = "moderada"
            elif imc < 17:
                desnutricao = "leve"
            else:
                desnutricao = "eutrofica"  # peso adequado

        return {
            "id": c.id,
            "idade": c.idade,
            "moradia": c.situacao_moradia.rotulo,
            "responsavel": c.tipo_responsavel.rotulo,
            "tem_responsavel": tem_responsavel,
            "renda": c.fonte_renda_responsavel.rotulo,
            "tem_renda_sustentavel": tem_renda,
            "renda_valor": f"R$ {c.renda_familiar_mensal:.0f}/mes",
            "programas": [p.rotulo for p in c.programas_ativos],
            "tem_programa": tem_programa,
            "escola": tem_escola,
            "desnutricao": desnutricao,
            "bairro": c.bairro,
            "municipio": c.municipio,
            "uf": c.uf,
        }

    # === 2. DIAGNOSTICAR ===

    def avaliar_risco(self, c: Crianca) -> Tuple[NivelRisco, str]:
        """
        Classifica risco e recomenda acao.

        CRITICO: fome AGORA + sem rede de apoio
        ALTO: fome + rede parcial
        MEDIO: inseguranca alimentar (nao e fome, mas incerto)
        BAIXO: alimentado, so monitorar
        """
        perfil = self.perfil(c)

        # Sem responsavel + sem abrigo = CRITICO automatico
        if c.situacao_moradia == SituacaoMoradia.SEM_ABIGO and c.tipo_responsavel == TipoResponsavel.NENHUM:
            return NivelRisco.CRITICO, (
                "Crianca em rua SEM responsavel. Acionar Conselho Tutelar "
                "(ECA Art. 98) + abrigo imediato + comida AGORA. "
                "Nenhuma burocracia pode esperar."
            )

        # Desnutricao confirmada = CRITICO
        if perfil["desnutricao"] in ("severa", "moderada"):
            return NivelRisco.CRITICO, (
                f"Desnutricao {perfil['desnutricao']} confirmada (IMC). "
                "Encaminhar ao posto de saude IMEDIATAMENTE. "
                "Suplementacao + alimentacao assistida."
            )

        # Sem renda + sem programa = CRITICO
        if not perfil["tem_renda_sustentavel"] and not perfil["tem_programa"]:
            return NivelRisco.CRITICO, (
                "Sem renda e sem nenhum programa ativo. "
                "Cadastrar no Bolsa Familia + merenda escolar + "
                "entrega de cesta/marmita IMEDIATA."
            )

        # Tem Bolsa Familia mas crianca nao vai a escola = ALTO
        if ProgramaAlimentacao.BOLSA_FAMILIA in c.programas_ativos and not c.escola:
            return NivelRisco.ALTO, (
                "Recebe Bolsa Familia mas crianca NAO esta na escola. "
                "Verificar: 1) Por que nao esta matriculada? "
                "2) Merenda escolar e a principal garantia de 1 refeicao/dia. "
                "3) Notificar Conselho Tutelar (ECA Art. 55 - direito a escola)."
            )

        # Tem renda mas baixa + sem programa = MEDIO
        if perfil["tem_renda_sustentavel"] and not perfil["tem_programa"] and c.renda_familiar_mensal < 800:
            return NivelRisco.MEDIO, (
                "Familia tem alguma renda mas abaixo de R$800/mes. "
                "Risco de inseguranca alimentar. "
                "Cadastrar em Programa Leite + Cozinha Comunitaria."
            )

        # Tem escola + tem programa = BAIXO
        if perfil["tem_programa"] and perfil["escola"]:
            return NivelRisco.BAIXO, (
                "Crianca com rede de apoio ativa (escola + programa). "
                "Monitorar peso/mes. Mander frequencia escolar."
            )

        return NivelRisco.MEDIO, "Situacao incerta. Avaliacao social necessaria."

    # === 3. AGIR ===

    def plano_acao(self, c: Crianca) -> List[Dict[str, Any]]:
        """Define o que fazer, em ordem de prioridade."""
        risco, justificativa = self.avaliar_risco(c)
        acoes: List[Dict[str, Any]] = []

        if risco == NivelRisco.CRITICO:
            if c.situacao_moradia == SituacaoMoradia.SEM_ABIGO:
                acoes.append({"prioridade": 1, "acao": "Acionar Conselho Tutelar (ECA Art. 98)", "prazo": "imediato"})
                acoes.append({"prioridade": 2, "acao": "Encaminhar a abrigo/casa de passagem", "prazo": "24h"})
                acoes.append({"prioridade": 3, "acao": "Garantir 3 refeicoes HOJE (marmita/cozinha comunitaria)", "prazo": "hoje"})
            else:
                acoes.append({"prioridade": 1, "acao": "Entregar cesta basica + marmita HOJE", "prazo": "hoje"})
                acoes.append({"prioridade": 2, "acao": "Cadastrar Bolsa Familia (se elegivel)", "prazo": "7 dias"})

            acoes.append({"prioridade": 3, "acao": "Matricular na escola (merenda = 1 refeicao garantida)", "prazo": "7 dias"})
            acoes.append({"prioridade": 4, "acao": "Encaminhar ao posto de saude (pesagem + suplemento)", "prazo": "7 dias"})

        elif risco == NivelRisco.ALTO:
            acoes.append({"prioridade": 1, "acao": "Verificar por que nao esta na escola", "prazo": "48h"})
            acoes.append({"prioridade": 2, "acao": "Matricular ou rematricular (ECA Art. 55)", "prazo": "7 dias"})
            acoes.append({"prioridade": 3, "acao": "Cozinha comunitaria ou Mesa Brasil", "prazo": "7 dias"})

        elif risco == NivelRisco.MEDIO:
            acoes.append({"prioridade": 1, "acao": "Cadastrar em Programa Leite", "prazo": "15 dias"})
            acoes.append({"prioridade": 2, "acao": "Encaminhar a Cozinha Comunitaria", "prazo": "15 dias"})

        elif risco == NivelRisco.BAIXO:
            acoes.append({"prioridade": 1, "acao": "Monitorar peso mensal", "prazo": "mensal"})
            acoes.append({"prioridade": 2, "acao": "Verificar frequencia escolar", "prazo": "mensal"})

        return acoes

    # === 4. COMPROVAR ===

    def registrar_entrega(self, e: EntregaAlimento) -> str:
        """Registra entrega de alimento com hash de verificacao."""
        dados = f"{e.crianca_id}|{e.programa.value}|{e.data}|{e.tipo}|{e.quantidade}"
        e.hash_verificacao = hashlib.sha256(dados.encode()).hexdigest()[:16]
        self.entregas.append(e)
        return e.hash_verificacao

    def tipos_comprovacao_para(self, c: Crianca) -> List[Dict[str, str]]:
        """Define como comprovar que a comida chegou, por situacao."""
        comprovacoes = []

        if c.escola:
            comprovacoes.append({
                "tipo": TipoComprovacao.FREQUENCIA.value,
                "como": "Frequencia escolar registra se crianca comeu merenda. Se faltou, nao comeu la.",
                "fiabilidade": "alta",
            })

        if c.situacao_moradia in (SituacaoMoradia.COM_FAMILIA, SituacaoMoradia.OCUPACAO):
            comprovacoes.append({
                "tipo": TipoComprovacao.ASSINATURA.value,
                "como": "Responsavel assina digital (app) confirmando recebimento da cesta/marmita.",
                "fiabilidade": "media",
            })
            comprovacoes.append({
                "tipo": TipoComprovacao.FOTO.value,
                "como": "Foto da comida servida (nao da entrega -- da REFEICAO servida no prato).",
                "fiabilidade": "alta",
            })

        if c.situacao_moradia == SituacaoMoradia.ABRIGO:
            comprovacoes.append({
                "tipo": TipoComprovacao.BIOMETRIA.value,
                "como": "Digital do responsavel do abrigo + frequencia da crianca no refeitorio.",
                "fiabilidade": "alta",
            })

        comprovacoes.append({
            "tipo": TipoComprovacao.PESO.value,
            "como": "Pesagem mensal da crianca. Se peso cai, comida nao esta chegando (ou nao esta absorvendo).",
            "fiabilidade": "alta",
        })

        comprovacoes.append({
            "tipo": TipoComprovacao.DEPOIMENTO.value,
            "como": "Vizinho ou lider comunitario confirma. Sempre cruzar com outro metodo.",
            "fiabilidade": "baixa",
        })

        return comprovacoes

    # === 5. FISCALIZAR ===

    def fiscalizar_entrega(self, entrega_id: str, fiscal_id: str,
                           status: StatusFiscalizacao, observacao: str = "") -> Dict[str, Any]:
        """Registra fiscalizacao de uma entrega."""
        e = next((x for x in self.entregas if x.id == entrega_id), None)
        if not e:
            return {"erro": "entrega nao encontrada"}

        reg = {
            "entrega_id": entrega_id,
            "crianca_id": e.crianca_id,
            "fiscal_id": fiscal_id,
            "status": status.value,
            "observacao": observacao,
            "data": datetime.now().isoformat(),
        }
        self.fiscalizacoes.append(reg)
        e.status = status
        return reg

    def detectar_desvio(self) -> List[Dict[str, Any]]:
        """
        Heuristica para detectar desvio de alimentos.

        PADROES SUSPEITOS:
        - Entrega marcada como "confirmada" mas peso da crianca caiu
        - Mesma assinatura em multiplas criancas (uma pessoa assinando por todas)
        - Entregas sem foto e sem biometria
        - Frequencia de entrega nao bate com estoque do programa
        """
        alertas = []

        # Agrupar entregas por programa
        por_programa: Dict[str, List[EntregaAlimento]] = {}
        for e in self.entregas:
            key = e.programa.value
            if key not in por_programa:
                por_programa[key] = []
            por_programa[key].append(e)

        for prog, entregas in por_programa.items():
            sem_comprovacao = [e for e in entregas if not e.comprovacao]
            if sem_comprovacao:
                pct_sem = len(sem_comprovacao) / len(entregas) * 100
                if pct_sem > 40:
                    alertas.append({
                        "tipo": "sem_comprovacao",
                        "programa": prog,
                        "pct": f"{pct_sem:.0f}%",
                        "alerta": f"{len(sem_comprovacao)} de {len(entregas)} entregas sem nenhuma comprovacao. Possivel desvio.",
                    })

            nao_recebeu = [e for e in entregas if e.status == StatusFiscalizacao.NAO_RECEBEU]
            if nao_recebeu:
                alertas.append({
                    "tipo": "nao_recebeu",
                    "programa": prog,
                    "qtd": len(nao_recebeu),
                    "alerta": f"{len(nao_recebeu)} entregas confirmadas como NAO recebidas pela familia.",
                })

            desviado = [e for e in entregas if e.status == StatusFiscalizacao.DESVIO]
            if desviado:
                alertas.append({
                    "tipo": "desvio_confirmado",
                    "programa": prog,
                    "qtd": len(desviado),
                    "alerta": f"DESVIOS CONFIRMADOS: {len(desviado)} entregas. Acionar denuncia (P13).",
                })

        return alertas

    # === ENTIDADES EXISTENTES ===

    def entidades_existentes(self) -> List[EntidadeExistente]:
        """Quem JA faz isso hoje no Brasil. E suficiente?"""
        return [
            EntidadeExistente(
                nome="Bolsa Familia",
                tipo="governo",
                escopo="nacional",
                atendimento="~21 milhoes de familias (~55 milhoes de pessoas)",
                modelo="Transferencia de renda (R$600 + R$150/crianca ate 7 anos)",
                gap="NAO garante que o dinheiro vire comida. ~17% das familias beneficiarias "
                    "continuam em inseguranca alimentar. Nao tem fiscalizacao nutricional.",
                suficiente=False,
            ),
            EntidadeExistente(
                nome="PNAE (Merenda Escolar)",
                tipo="governo",
                escopo="nacional",
                atendimento="~40 milhoes de alunos (educacao basica)",
                modelo="1 refeicao/dia na escola (R$0.36/aluno/dia)",
                gap="NAO atende crianca FORA da escola. 1.6 milhoes de criancas nao matriculadas. "
                    "Merenda e terceirizada em 70% dos municipios -- qualidade duvidosa. "
                    "Crianca que falta aula nao come.",
                suficiente=False,
            ),
            EntidadeExistente(
                nome="Mesa Brasil SESC",
                tipo="ong",
                escopo="nacional",
                atendimento="~3 milhoes de pessoas/ano",
                modelo="Doacao de alimentos + educacao nutricional",
                gap="Cobertura regional desigual. Foco em areas urbanas. "
                    "Nao atende criancas em rua. Volume insuficiente vs demanda.",
                suficiente=False,
            ),
            EntidadeExistente(
                nome="Acao da Cidadadia Contra a Fome",
                tipo="ong",
                escopo="nacional",
                atendimento="~2 milhoes de pessoas/ano",
                modelo="Cestas basicas + cozinhas comunitarias",
                gap="Depende de doacao privada. Sazonal (pico em campanhas, seca no resto). "
                    "Sem acompanhamento individualizado por crianca.",
                suficiente=False,
            ),
            EntidadeExistente(
                nome="Banco de Alimentos (Global FoodBanking)",
                tipo="ong",
                escopo="estadual/municipal",
                atendimento="~500 mil pessoas/ano",
                modelo="Redistribui alimentos que seriam descartados",
                gap="Cobertura limitada a ~50 municipios. Nao chega ao interior/sertao. "
                    "Sem controle individualizado de quem recebe.",
                suficiente=False,
            ),
            EntidadeExistente(
                nome="Restaurantes Populares",
                tipo="governo",
                escopo="municipal",
                atendimento="~1.5 milhoes de pessoas/ano",
                modelo="Refeicao por R$1-2",
                gap="Existe em pouquissimos municipios (~30 cidades). "
                    "Crianca de rua nao tem R$1. Nao atende quem nao pode sair de casa.",
                suficiente=False,
            ),
            EntidadeExistente(
                nome="Cozinhas Comunitarias",
                tipo="mista",
                escopo="local",
                atendimento="~800 mil pessoas/ano",
                modelo="Cozinha no bairro serve refeicoes a preco social",
                gap="Iniciativa dispersa, sem coordenacao nacional. "
                    "Depende de lideranca local. ~500 cozinhas no Brasil todo (precisaria 5000).",
                suficiente=False,
            ),
            EntidadeExistente(
                nome="Igrejas / ONGs religiosas",
                tipo="religiosa",
                escopo="local",
                atendimento="indeterminado (~5 milhoes estimado)",
                modelo="Sopas, marmitas, cestas (Caritas, MVBR, batista, evangelica)",
                gap="Sem dados oficiais. Sem fiscalizacao nutricional. "
                    "Depende de voluntario. Pode condicionar ajuda a religiao.",
                suficiente=False,
            ),
        ]

    def veredito_suficiencia(self) -> Dict[str, Any]:
        """Resumo: as entidades existentes sao suficientes?"""
        ents = self.entidades_existentes()
        total_atendido = "~70-80 milhoes de atendimentos/ano (com sobreposicao)"
        total_necessario = "~125 milhoes (inseguranca alimentar, VIGISAN 2022)"

        return {
            "entidades_cadastradas": len(ents),
            "suficientes": sum(1 for e in ents if e.suficiente),
            "insuficientes": sum(1 for e in ents if not e.suficiente),
            "atendimento_total_estimado": total_atendido,
            "demanda_total": total_necessario,
            "gap": "~45-55 milhoes de pessoas NAO atendidas consistentemente",
            "problema_principal": (
                "Nenhuma entidade faz RASTREIO INDIVIDUAL por crianca. "
                "Todas trabalham por volume/territorio. "
                "Uma crianca pode receber de 3 entidades num mes e de nenhuma no mes seguinte. "
                "Ninguem sabe se a comida chegou ao prato."
            ),
        }

    # === SCORECARD ===

    def scorecard(self) -> Dict[str, Any]:
        return {
            "modulo": "open_child_food_security",
            "versao": "0.1.0-spec",
            "fluxo": "identificar -> diagnosticar -> agir -> comprovar -> fiscalizar",
            "niveis_risco": len(NivelRisco),
            "programas": len(ProgramaAlimentacao),
            "tipos_comprovacao": len(TipoComprovacao),
            "entidades_mapeadas": len(self.entidades_existentes()),
            "suficiencia": "0 de 8 entidades sao suficientes",
            "principio_constitucional": "P6 (acesso universal) + Triage VIDA",
            "fundamentacao_legal": "ECA Arts. 4, 55, 98 (direito a alimentacao + escola + protecao)",
        }


# ============================================================
# DEMO
# ============================================================

def _demo():
    fs = ChildFoodSecurity()

    print("=" * 65)
    print("OPEN CHILD FOOD SECURITY")
    print("Fome Zero Infantil com Rastreio")
    print("=" * 65)

    # --- CASO 1: Crianca em rua, sem responsavel ---
    c1 = Crianca(
        id="c1", idade=8,
        situacao_moradia=SituacaoMoradia.SEM_ABIGO,
        tipo_responsavel=TipoResponsavel.NENHUM,
        fonte_renda_responsavel=FonteRenda.NENHUMA,
        renda_familiar_mensal=0,
        programas_ativos=[],
        escola=False,
        bairro="Centro", municipio="Sao Paulo", uf="SP",
    )
    fs.cadastrar_crianca(c1)
    risco1, just1 = fs.avaliar_risco(c1)
    print(f"\n[CASO 1] Crianca 8 anos, rua, sem responsavel")
    print(f"  Risco: {risco1.value.upper()}")
    print(f"  Acao: {just1}")
    print(f"  Plano:")
    for a in fs.plano_acao(c1):
        print(f"    {a['prioridade']}. {a['acao']} ({a['prazo']})")
    print(f"  Comprovacao:")
    for cp in fs.tipos_comprovacao_para(c1):
        print(f"    - {cp['tipo']}: {cp['como']}")

    # --- CASO 2: Crianca com familia, BF, mas nao vai a escola ---
    c2 = Crianca(
        id="c2", idade=10,
        situacao_moradia=SituacaoMoradia.COM_FAMILIA,
        tipo_responsavel=TipoResponsavel.UM_GENITOR,
        fonte_renda_responsavel=FonteRenda.BOLSA,
        renda_familiar_mensal=750,
        programas_ativos=[ProgramaAlimentacao.BOLSA_FAMILIA],
        escola=False,
        bairro="Brasilia Teimosa", municipio="Recife", uf="PE",
    )
    fs.cadastrar_crianca(c2)
    risco2, just2 = fs.avaliar_risco(c2)
    print(f"\n[CASO 2] Crianca 10 anos, mae solo, Bolsa Familia, SEM escola")
    print(f"  Risco: {risco2.value.upper()}")
    print(f"  Acao: {just2}")

    # --- CASO 3: Crianca desnutrida ---
    c3 = Crianca(
        id="c3", idade=5,
        situacao_moradia=SituacaoMoradia.COM_FAMILIA,
        tipo_responsavel=TipoResponsavel.PAI_MAE,
        fonte_renda_responsavel=FonteRenda.INFORMAL,
        renda_familiar_mensal=500,
        programas_ativos=[ProgramaAlimentacao.MERENDA],
        escola=True,
        peso_kg=12.5, altura_cm=100,
        bairro="Sertao", municipio="Taua", uf="CE",
    )
    fs.cadastrar_crianca(c3)
    risco3, just3 = fs.avaliar_risco(c3)
    print(f"\n[CASO 3] Crianca 5 anos, 12.5kg/100cm (desnutrida)")
    print(f"  Risco: {risco3.value.upper()}")
    print(f"  Acao: {just3}")

    # --- CASO 4: Crianca com rede ativa ---
    c4 = Crianca(
        id="c4", idade=12,
        situacao_moradia=SituacaoMoradia.COM_FAMILIA,
        tipo_responsavel=TipoResponsavel.PAI_MAE,
        fonte_renda_responsavel=FonteRenda.FORMAL,
        renda_familiar_mensal=1800,
        programas_ativos=[ProgramaAlimentacao.MERENDA, ProgramaAlimentacao.BOLSA_FAMILIA],
        escola=True,
        peso_kg=35, altura_cm=145,
        bairro="Centro", municipio="Florianopolis", uf="SC",
    )
    fs.cadastrar_crianca(c4)
    risco4, just4 = fs.avaliar_risco(c4)
    print(f"\n[CASO 4] Crianca 12 anos, escola + BF, CLT")
    print(f"  Risco: {risco4.value.upper()}")
    print(f"  Acao: {just4}")

    # --- ENTIDADES ---
    print(f"\n{'=' * 65}")
    print("ENTIDADES EXISTENTES (quem JA faz isso hoje)")
    print(f"{'=' * 65}")
    for e in fs.entidades_existentes():
        flag = "OK" if e.suficiente else "INSUFICIENTE"
        print(f"\n  [{flag}] {e.nome} ({e.tipo})")
        print(f"        Atende: {e.atendimento}")
        print(f"        Modelo: {e.modelo}")
        print(f"        GAP: {e.gap}")

    # --- VEREDITO ---
    print(f"\n{'=' * 65}")
    print("VEREDITO DE SUFICIENCIA")
    print(f"{'=' * 65}")
    v = fs.veredito_suficiencia()
    for k, val in v.items():
        print(f"  {k}: {val}")

    # --- SCORECARD ---
    print(f"\n{'=' * 65}")
    print("SCORECARD")
    print(f"{'=' * 65}")
    for k, val in fs.scorecard().items():
        print(f"  {k}: {val}")


if __name__ == "__main__":
    _demo()
