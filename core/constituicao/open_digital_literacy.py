#!/usr/bin/env python3
"""
OpenDigitalLiteracy -- P11: Letramento Digital como Constituinte da Cidadania
==============================================================================
"Exigir smartphone para exercer direito e o novo imposto de votacao."

TESE:
  O Estado brasileiro digitalizou serviços sem digitalizar cidadãos (dados TIC Domicílios 2023 / CGI.br e PNAD 2023/2024 IBGE).
  Em 2023: ~84.7% dos domicílios com internet (IBGE); ~15-20% ainda com exclusão significativa.
  Em 2024/2025: penetração de smartphone ~85-88% (adultos), mas letramento funcional baixo (~25-35% da população enfrenta barreiras em serviços complexos como gov.br).
  Resultado: gov.br (60M+ contas ativas), e-CAC, Detran online, app Caixa, Concurso via app.
  Cada um exige: smartphone + internet + leitura + cadastro + 2FA/SMS/biometria.

  Quem não tem acesso ou letramento é EXCLUÍDO DA DEMOCRACIA DIGITAL.
  Não porque não quer participar.
  Porque o Estado COLOCOU uma barreira digital entre o cidadão e seus direitos.

  Isso é ANTI-DEMOCRÁTICO (dados atualizados 2024/2025).

O PRINCIPIO (P11):

  Letramento digital nao e REQUISITO para cidadania.
  E CONSTITUINTE da cidadania.

  Significa: o Estado nao pode EXIGIR letramento digital para
  que o cidadao acesse seus direitos. Se o Estado digitaliza um
  servico, DEVE fornecer letramento digital gratuito como PARTE
  daquele servico.

  Nao e "o cidadao se adapta ao digital". E "o digital serve ao cidadao".

COMO OBRIGACAO DO ESTADO:

  Se o Estado digitaliza servico X, entao o Estado DEVE:
  1. Manter canal NAO-DIGITAL funcional (presencial, telefone, papel)
  2. Fornecer letramento digital gratuito para X
  3. Garantir acesso a hardware minimo (telefone publico, quiosque)
  4. Garantir conectividade gratuita (wifi publico, 4G zero-rating gov.br)
  4. Garantir assistencia humana (atendente que ensina, nao so executa)
  5. Medir e publicar exclusao digital (transparencia, P5)

A METAFORA DO IMPOSTO DE VOTACAO:

  Antes da Republica, so votava quem pagava imposto.
  O "imposto de votacao" (poll tax) foi abolido porque e anti-democratico.
  Exigir letramento digital e o NOVO imposto de votacao.
  Exclui quem nao tem dinheiro para smartphone, internet, educacao.
  Nao por maldade -- por NEGLIGENCIA do Estado.

TIPOS DE EXCLUSAO DIGITAL (6):

  1. HARDWARE: nao tem smartphone/computador
  2. CONECTIVIDADE: nao tem internet ou e lenta/cara
  3. LETRAMENTO: nao sabe usar tecnologia
  4. IDIOMA: interface so em portugues escrito (analfabeto, imigrante)
  5. DEFICIENCIA: interface nao e acessivel (cego, surdo, tetraplegico)
  6. CONFIANCA: nao confia no sistema (e cético, com razao)

Cada tipo exige mitigacao ESPECIFICA. Nao basta "dar curso de informatica".

A CONTRADICAO DO GOVERNO DIGITAL BRASILEIRO:

  gov.br exige: conta gov, senha, 2FA (SMS/app), CPF, biometria facial (2024).
  Para renovar CNH: app/site Detran + pagamento PIX + agendamento online (exclusão ~20-30% idosos/rurais).
  Para Auxílio/Bolsa Família: app Caixa Tem + conta digital + selfie (dados 2024 mostram ~18% exclusão inicial).
  Para marcação SUS: apps + login gov.br.
  TIC 2023/2024: 84.7% domicílios com internet; mas letramento digital funcional estimado em 60-70% (barreira real para serviços complexos).

  Cada passo exclui milhões (dados IBGE/PNAD 2023-2025).
  E o Estado se gaba de “modernização”.
  Modernização sem letramento = EXCLUSÃO com UI bonita (atualizado 2024/2025).

O QUE A REPUBLICA FAZ (politicas):

  1. CANAL ANALOGICO ETERNO: nenhum servico e 100% digital.
     Se o Estado oferece online, DEVE oferecer presencial/telefone.
  2. LETRAMENTO EMBEDDING: o sistema ENSINA enquanto usa.
     Nao "curso separado". O proprio gov.br ensina o cidadao a usar gov.br.
  3. ACESSO UNIVERSAL: wifi publico gratuito, quiosques em praca.
  4. ASSISTENTE HUMANA: atendente que ENSINA, nao so executa.
  5. MEDICAO DE EXCLUSAO: todo servico digital mede e publica % de exclusao.
  6. REVERSAO: se servico digital exclui >10%, e SUSPENSO ate correcao.

INTEGRACAO CONSTITUCIONAL:

  - P1: Exclusao digital recria elite (so digitais participam).
  - P4: Processo democratico (P4) exige que todos possam participar.
  - P6: Acesso universal ao conhecimento (P6) -- letramento e conhecimento.
  - P2: Autonomia do cidadao sobre seu corpo/dados.
  - P9: Exclusao digital e uma forma de polarizacao (digitais vs analogicos).

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field
from collections import defaultdict
from datetime import datetime


# ============================================================================
# 1. ENUMS
# ============================================================================

class TipoExclusaoDigital(Enum):
    """Os 6 tipos de exclusao digital que o Estado pode causar."""
    HARDWARE = ("hardware", "Falta de smartphone/computador adequado")
    CONECTIVIDADE = ("conectividade", "Sem internet, ou internet lenta/cara")
    LETRAMENTO = ("letramento", "Nao sabe usar a tecnologia necessaria")
    IDIOMA = ("idioma", "Interface so em portugues escrito (analfabeto, imigrante)")
    DEFICIENCIA = ("deficiencia", "Interface nao e acessivel (cego, surdo, tetra)")
    CONFIANCA = ("confianca", "Nao confia no sistema digital (celetico, com razao)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class NivelExclusao(Enum):
    """Nivel de exclusao causado por um servico digital."""
    NENHUMA = ("nenhuma", "Servico nao exclui", 0)
    BAIXA = ("baixa", "Exclui < 5% do publico-alvo", 1)
    MEDIA = ("media", "Exclui 5-15% do publico-alvo", 2)
    ALTA = ("alta", "Exclui 15-30% do publico-alvo", 3)
    CRITICA = ("critica", "Exclui > 30% do publico-alvo", 4)

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def peso(self) -> int:
        return self.value[2]


class TipoObrigacaoEstado(Enum):
    """Obrigacoes do Estado quando digitaliza um servico."""
    CANAL_ANALOGICO = ("analogico", "Manter canal nao-digital (presencial/telefone/papel)")
    LETRAMENTO_EMBEDDED = ("letramento", "Ensinar o cidadao DENTRO do servico")
    HARDWARE_PUBLICO = ("hardware", "Fornecer hardware publico (quiosque, telefone)")
    CONECTIVIDADE_PUBLICA = ("conectividade", "Wifi/4G publico gratuito para servicos gov")
    ASSISTENTE_HUMANA = ("humana", "Atendente que ENSINA, nao so executa")
    MEDICAO_EXCLUSAO = ("medicao", "Medir e publicar % de exclusao digital")
    REVERSAO_SUSPENSAO = ("reversao", "Se exclusao > 10%, suspender ate correcao")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class StatusServicoDigital(Enum):
    """Status de um servico digital governamental."""
    CONFORME = ("conforme", "Conforme com P11: oferece mitigacoes")
    REVISAO = ("revisao", "Precisa revisao (exclusao nao mitigada)")
    SUSPENSO = ("suspenso", "Exclusao > 10%, SUSPENSO ate correcao")
    BANIDO = ("banido", "Servico 100% digital sem alternativa = banido")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoCanalAcesso(Enum):
    """Canais de acesso que um servico DEVE oferecer."""
    DIGITAL = ("digital", "Site/app (canal primario)")
    PRESENCIAL = ("presencial", "Atendimento presencial em local fisico")
    TELEFONE = ("telefone", "Atendimento por telefone (humano, nao URA)")
    PAPEL = ("papel", "Formulario fisico enviavel por correio")
    VOZ = ("voz", "Acesso por voz (telefone + Vosk/Iara)")
    COMUNITARIO = ("comunitario", "Agente comunitario vai ate o cidadao")

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
class ExclusaoDetectada:
    """Uma fonte de exclusao digital num servico."""
    tipo: TipoExclusaoDigital
    descricao: str
    publico_afetado_pct: float  # 0-100, % do publico-alvo excluido
    mitigacao_existente: bool = False
    mitigacao_descricao: str = ""


@dataclass
class ServicoDigital:
    """Um servico governamental digitalizado."""
    id: str
    nome: str
    orgao: str
    # o que exige do cidadao
    exige_smartphone: bool = False
    exige_internet: bool = False
    exige_cadastro: bool = False
    exige_2fa_sms: bool = False
    exige_leitura: bool = False  # texto escrito sem audio
    exige_biometria: bool = False
    # canais oferecidos
    canais: List[TipoCanalAcesso] = field(default_factory=list)
    # letramento embedded
    ensina_dentro: bool = False  # ensina enquanto usa?
    tem_assistente_humana: bool = False
    tem_curso_separado: bool = False  # curso externo (nao embedded)
    # metricas de exclusao
    exclusoes: List[ExclusaoDetectada] = field(default_factory=list)
    # dados (preenchados pela engine)
    nivel_exclusao: Optional[NivelExclusao] = None
    status: Optional[StatusServicoDigital] = None


# ============================================================================
# 3. ENGINE
# ============================================================================

class DigitalLiteracyEngine:
    """
    Avalia servicos digitais governamentais contra P11.

    Se o Estado digitaliza um servico, este motor verifica:
    1. Que tipos de exclusao o servico causa?
    2. O Estado cumpriu suas obrigacoes de mitigacao?
    3. Qual o nivel de exclusao resultante?
    4. O servico deve ser conforme, revisado, suspenso ou banido?
    """

    LIMITE_SUSPENSAO_PCT = 10.0  # >10% exclusao = suspenso
    LIMITE_BANIDO_PCT = 30.0     # >30% = banido
    LIMITE_REVISAO_PCT = 5.0     # >5% = revisao

    def __init__(self) -> None:
        self.servicos: Dict[str, ServicoDigital] = {}

    def registrar(self, servico: ServicoDigital) -> None:
        self.servicos[servico.id] = servico

    def avaliar_servico(self, servico_id: str) -> Dict[str, Any]:
        """Avalia UM servico contra P11."""
        s = self.servicos.get(servico_id)
        if s is None:
            return {"erro": f"Servico nao encontrado: {servico_id}"}

        # 1. Detectar fontes de exclusao
        exclusoes: List[ExclusaoDetectada] = []
        if s.exige_smartphone and TipoCanalAcesso.PRESENCIAL not in s.canais:
            exclusoes.append(ExclusaoDetectada(
                tipo=TipoExclusaoDigital.HARDWARE,
                descricao="Exige smartphone sem canal presencial alternativo",
                publico_afetado_pct=20.0,
                mitigacao_existente=False,
            ))
        if s.exige_internet and not any(
            c in [TipoCanalAcesso.PRESENCIAL, TipoCanalAcesso.TELEFONE]
            for c in s.canais
        ):
            exclusoes.append(ExclusaoDetectada(
                tipo=TipoExclusaoDigital.CONECTIVIDADE,
                descricao="Exige internet sem canal analogico",
                publico_afetado_pct=15.0,
                mitigacao_existente=False,
            ))
        if s.exige_leitura and not s.ensina_dentro:
            exclusoes.append(ExclusaoDetectada(
                tipo=TipoExclusaoDigital.LETRAMENTO,
                descricao="Exige leitura sem letramento embedded",
                publico_afetado_pct=25.0,
                mitigacao_existente=False,
            ))
        if s.exige_2fa_sms and not s.tem_assistente_humana:
            exclusoes.append(ExclusaoDetectada(
                tipo=TipoExclusaoDigital.CONFIANCA,
                descricao="Exige 2FA SMS sem assistente humana",
                publico_afetado_pct=10.0,
                mitigacao_existente=False,
            ))
        # Adicionar qualquer exclusao explicita do servico
        for ex in s.exclusoes:
            if ex not in exclusoes:
                exclusoes.append(ex)

        # 2. Calcular % total de exclusao (com overlap, pegar max)
        # Simplificacao: soma, capado em 100
        pct_total = min(100.0, sum(e.publico_afetado_pct for e in exclusoes))

        # 3. Nivel
        if pct_total == 0:
            nivel = NivelExclusao.NENHUMA
        elif pct_total < self.LIMITE_REVISAO_PCT:
            nivel = NivelExclusao.BAIXA
        elif pct_total < self.LIMITE_SUSPENSAO_PCT:
            nivel = NivelExclusao.MEDIA
        elif pct_total < self.LIMITE_BANIDO_PCT:
            nivel = NivelExclusao.ALTA
        else:
            nivel = NivelExclusao.CRITICA

        # 4. Status
        # Verificar obrigacoes cumpridas
        obrigacoes_cumpridas = self._contar_obrigacoes(s)
        obrigacoes_necessarias = 6  # total de TipoObrigacaoEstado
        cobertura = obrigacoes_cumpridas / obrigacoes_necessarias

        if pct_total == 0:
            status = StatusServicoDigital.CONFORME
        elif pct_total > self.LIMITE_BANIDO_PCT:
            status = StatusServicoDigital.BANIDO
        elif pct_total > self.LIMITE_SUSPENSAO_PCT:
            status = StatusServicoDigital.SUSPENSO
        elif cobertura >= 0.8:
            status = StatusServicoDigital.CONFORME
        else:
            status = StatusServicoDigital.REVISAO

        s.exclusoes = exclusoes
        s.nivel_exclusao = nivel
        s.status = status

        return {
            "servico_id": s.id,
            "servico_nome": s.nome,
            "orgao": s.orgao,
            "pct_exclusao": round(pct_total, 1),
            "nivel_exclusao": nivel.rotulo,
            "obrigacoes_cumpridas": f"{obrigacoes_cumpridas}/{obrigacoes_necessarias}",
            "status": status.rotulo,
            "exclusoes_detectadas": [
                {
                    "tipo": e.tipo.id,
                    "descricao": e.descricao,
                    "pct_afetado": e.publico_afetado_pct,
                    "mitigado": e.mitigacao_existente,
                }
                for e in exclusoes
            ],
            "timestamp": datetime.now().isoformat(),
        }

    def _contar_obrigacoes(self, s: ServicoDigital) -> int:
        """Conta quantas das 7 obrigacoes do Estado o servico cumpre."""
        c = 0
        # 1. Canal analogico
        if any(ch in [TipoCanalAcesso.PRESENCIAL, TipoCanalAcesso.TELEFONE,
                       TipoCanalAcesso.PAPEL, TipoCanalAcesso.COMUNITARIO]
               for ch in s.canais):
            c += 1
        # 2. Letramento embedded
        if s.ensina_dentro:
            c += 1
        # 3. Hardware publico (presencial = quiosque)
        if TipoCanalAcesso.PRESENCIAL in s.canais:
            c += 1
        # 4. Conectividade publica (presencial = wifi no local)
        if TipoCanalAcesso.PRESENCIAL in s.canais:
            c += 1
        # 5. Assistente humana
        if s.tem_assistente_humana:
            c += 1
        # 6. Medicao de exclusao (se tem exclusoes explicitas, mede)
        if s.exclusoes or s.nivel_exclusao is not None:
            c += 1
        return c

    def avaliar_todos(self) -> Dict[str, Any]:
        resultados = {}
        for sid in self.servicos:
            resultados[sid] = self.avaliar_servico(sid)
        conforme = sum(
            1 for r in resultados.values()
            if isinstance(r, dict) and r.get("status", "").startswith("Conforme")
        )
        total = len(resultados)
        pct = (conforme / total * 100) if total else 0
        return {
            "total_servicos": total,
            "conformes": conforme,
            "suspensos": sum(
                1 for r in resultados.values()
                if isinstance(r, dict) and "Susp" in r.get("status", "")
            ),
            "banidos": sum(
                1 for r in resultados.values()
                if isinstance(r, dict) and "banido" in r.get("status", "")
            ),
            "taxa_conformidade": f"{conforme}/{total} ({pct:.0f}%)",
            "resultados": resultados,
        }

    def scorecard(self) -> Dict[str, Any]:
        return {
            "servicos_avaliados": len(self.servicos),
            "tipos_exclusao": len(list(TipoExclusaoDigital)),
            "obrigacoes_estado": len(list(TipoObrigacaoEstado)),
            "limite_suspensao_pct": self.LIMITE_SUSPENSAO_PCT,
            "limite_banido_pct": self.LIMITE_BANIDO_PCT,
            "principio": "P11 -- Letramento Digital como Constituinte",
        }


# ============================================================================
# 4. DEMO
# ============================================================================

def _demo() -> None:
    eng = DigitalLiteracyEngine()

    print("=" * 70)
    print("OpenDigitalLiteracy -- P11: Letramento como Constituinte")
    print("=" * 70)

    # --- Cenarios brasileiros reais ---
    print("\n[CENARIOS BRASILEIROS REAIS]")

    # gov.br login
    eng.registrar(ServicoDigital(
        id="gov_br", nome="gov.br Login", orgao="Governo Federal",
        exige_smartphone=True, exige_internet=True, exige_cadastro=True,
        exige_2fa_sms=True, exige_leitura=True,
        canais=[TipoCanalAcesso.DIGITAL],
        ensina_dentro=False, tem_assistente_humana=False,
    ))

    # Renovacao CNH online
    eng.registrar(ServicoDigital(
        id="cnh_online", nome="Renovacao CNH Detran-SP", orgao="Detran-SP",
        exige_smartphone=True, exige_internet=True, exige_leitura=True,
        exige_cadastro=True,
        canais=[TipoCanalAcesso.DIGITAL, TipoCanalAcesso.PRESENCIAL],
        ensina_dentro=False, tem_assistente_humana=True,
    ))

    # Auxilio Emergencial via app Caixa
    eng.registrar(ServicoDigital(
        id="auxilio_caixa", nome="Auxilio via App Caixa", orgao="Caixa",
        exige_smartphone=True, exige_internet=True, exige_cadastro=True,
        exige_leitura=True,
        canais=[TipoCanalAcesso.DIGITAL],
        ensina_dentro=False, tem_assistente_humana=False,
    ))

    # SUS: marca consulta por voz ( Republica ideal)
    eng.registrar(ServicoDigital(
        id="sus_voz", nome="SUS por Voz (Republica ideal)", orgao="SUS",
        exige_internet=False, exige_smartphone=False, exige_leitura=False,
        canais=[TipoCanalAcesso.DIGITAL, TipoCanalAcesso.PRESENCIAL,
                TipoCanalAcesso.TELEFONE, TipoCanalAcesso.VOZ,
                TipoCanalAcesso.COMUNITARIO],
        ensina_dentro=True, tem_assistente_humana=True,
    ))

    # Concurso publico via app
    eng.registrar(ServicoDigital(
        id="concurso_app", nome="Concurso Publico via App", orgao="CESPE",
        exige_smartphone=True, exige_internet=True, exige_cadastro=True,
        exige_leitura=True,
        canais=[TipoCanalAcesso.DIGITAL],
        ensina_dentro=False, tem_assistente_humana=False,
    ))

    # --- Avaliar ---
    print("\n[AVALIACAO DE SERVICOS REAIS]")
    resultado = eng.avaliar_todos()
    print(f"\n  Taxa de conformidade: {resultado['taxa_conformidade']}")
    print(f"  Conformes: {resultado['conformes']}")
    print(f"  Suspensos: {resultado['suspensos']}")
    print(f"  Banidos: {resultado['banidos']}")

    print("\n[DETALHES POR SERVICO]")
    for sid, res in resultado["resultados"].items():
        if not isinstance(res, dict):
            continue
        print(f"\n  {res['servico_nome']} ({res['orgao']})")
        print(f"    Status: {res['status']}")
        print(f"    Exclusao: {res['pct_exclusao']}% -- {res['nivel_exclusao']}")
        print(f"    Obrigacoes: {res['obrigacoes_cumpridas']}")
        print(f"    Exclusoes detectadas:")
        for ex in res.get("exclusoes_detectadas", []):
            mitig = "[MITIGADO]" if ex["mitigado"] else "[SEM MITIGACAO]"
            print(f"      {mitig} {ex['tipo']}: {ex['descricao']} ({ex['pct_afetado']}%)")

    # --- Os 6 tipos de exclusao ---
    print("\n\n[OS 6 TIPOS DE EXCLUSAO DIGITAL]")
    for t in TipoExclusaoDigital:
        print(f"  {t.id:<16} {t.rotulo}")

    # --- As 7 obrigacoes do Estado ---
    print("\n[AS 7 OBRIGACOES DO ESTADO AO DIGITALIZAR]")
    for o in TipoObrigacaoEstado:
        print(f"  {o.id:<16} {o.rotulo}")

    # --- Filosofia ---
    print("\n" + "=" * 70)
    print("FILOSOFIA -- Letramento como Constituinte")
    print("=" * 70)
    print("""
A HISTORIA REPETE:

  O imposto de votacao (poll tax) foi inventado para excluir pobres
  e negros da democracia americana. Voce pagava para votar.
  Sem dinheiro, sem voto. Sem representacao.

  O Brasil aboliu isso na Constituicao. Mas o recriou em forma digital.

  gov.br exige smartphone. Exige internet. Exige leitura.
  Exige cadastro. Exige 2FA SMS. Exige biometria.

  Cada exigencia e um NOVO imposto de votacao.
  Cada etapa exclui milhoes.
  Nao por maldade -- por NEGLIGENCIA estrutural.

A TESE DA REPUBLICA:

  Letramento digital NAO E REQUISITO para cidadania.
  E CONSTITUINTE da cidadania.

  Constituinte significa: faz parte da cidadania.
  O Estado nao EXIGE que voce saiba para participar.
  O Estado FORNECE o saber e o acesso como PARTE do direito.

  Se o Estado digitaliza, DEVE:
  - Manter canal analogico (presencial, telefone, papel)
  - Ensinar o cidadao DENTRO do servico (nao curso separado)
  - Fornecer hardware publico (quiosque em praca)
  - Fornecer conectividade publica (wifi gov gratuito)
  - Ter atendente que ENSINA, nao so executa
  - Medir e publicar a exclusao que causa

A CONSEQUENCIA:

  Se um servico digital exclui mais de 10% do publico, e SUSPENSO.
  Nao e "modernizacao". E EXCLUSAO com interface bonita.

  "Modernizar" sem letramento e como abrir escola sem professor.
  O predio existe. A porta esta aberta. Mas ninguem aprende.
  E o Estado se gabas de ter "escola".

  A Republica ensina. O digital serve ao cidadao.
  Nao o contrario.
""")


if __name__ == "__main__":
    _demo()
