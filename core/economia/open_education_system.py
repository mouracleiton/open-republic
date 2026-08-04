#!/usr/bin/env python3
"""
OpenEducationSystem -- L4: Sistema de Educacao Nacional
=========================================================
Spec de educacao publica redesenhada. Do.zero.

O PROBLEMA:
  Brasil gasta 6% do PIB em educacao (acima da media OCDE).
  Resultado: PISA 2018: matematica 384 (media OCDE 489).
  Dinheiro nao falta. Falta ESTRUTURA.

OS DADOS (idea_validator):
  Kerala: mais pobre que media India, IDH SUPERIOR.
  Por que? ESCOLA.
  Finlandia: #1 PISA, 0 homework ate 12 anos.
  Por que? CONFIANCA no professor.

O MODELO:
  - Curriculo civico (P1-P14 desde cedo)
  - Professor e autoridade, nao burocrata
  - Sem vestibular extorsivo
  - Escola integral (7h-18h) com comida
  - Tecnologia como ferramenta, nao substituto
  - Avaliacao por projeto, nao por prova
  - Inclusao total (deficiencia = L5 integrado)

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field


# ============================================================================
# 1. ENUMS
# ============================================================================

class NivelEnsino(Enum):
    """Niveis de ensino do sistema nacional."""
    EDUCACAO_INFANTIL = ("infantil", "0-5 anos: creche + pre-escola")
    FUNDAMENTAL_I = ("fund1", "6-10 anos: 1o ao 5o ano (alfabetizacao + base)")
    FUNDAMENTAL_II = ("fund2", "11-14 anos: 6o ao 9o ano (especializacao)")
    MEDIO = ("medio", "15-17 anos: ensino medio (tecnico + civico)")
    SUPERIOR = ("superior", "18+: universidade gratuita por merito")
    TECNICO = ("tecnico", "14+: formacao tecnica paralela")
    CONTINUADA = ("continuada", "vida toda: educacao permanente")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class EixoCurricular(Enum):
    """Os 7 eixos do curriculo nacional."""
    ALFABETIZACAO = ("alfabetizacao", "Alfabetizacao: ler, escrever, calcular")
    CIVISMO = ("civismo", "Civismo: P1-P14, direitos, deveres, alicerce etico")
    CIENCIA = ("ciencia", "Ciencia: metodo cientifico, pensamento critico")
    TECNOLOGIA = ("tecnologia", "Tecnologia: programacao, IA local, seguranca digital")
    CULTURA = ("cultura", "Cultura: cordel, samba, capoeira, antropofagia")
    CORPO = ("corpo", "Corpo: educacao fisica, saude, autonomia (P2)")
    PRATICA = ("pratica", "Pratica: projeto real, comunidade, oficio")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class MetodoAvaliacao(Enum):
    """Metodos de avaliacao (NAO sao provas)."""
    PROJETO = ("projeto", "Projeto: resolve problema real, apresenta resultado")
    PORTFOLIO = ("portfolio", "Portfolio: acumula trabalho ao longo do ano")
    RODA = ("roda", "Roda: avaliacao pelos pares, auto-avaliacao")
    DEMONSTRACAO = ("demonstracao", "Demonstracao: mostra que sabe fazer")
    NARRATIVA = ("narrativa", "Narrativa: professor descreve evolucao em texto")
    SEM_PROVA = ("sem_prova", "SEM PROVA: Finlandia nao prova ate 12 anos")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class PapelEscolar(Enum):
    """Papeis na comunidade escolar."""
    PROFESSOR = ("professor", "Professor: autoridade pedagogica, nao burocrata")
    MENTOR = ("mentor", "Mentor: profissional da comunidade que ensina oficio")
    ALUNO = ("aluno", "Aluno: protagonista, nao recipiente")
    CUIDADOR = ("cuidador", "Cuidador: saude, alimentacao, apoio emocional")
    COZINHEIRA = ("cozinha", "Cozinheira: comida de verdade, nao industrial")
    GUARDIAO = ("guardiao", "Guardiao: seguranca comunitaria, nao policial")
    FAMILIA = ("familia", "Familia: participante, nao espectador")
    COMUNIDADE = ("comunidade", "Comunidade: oferece projetos reais pra escola")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class DiaEscolar(Enum):
    """Blocos do dia escolar integral."""
    ACOlHIDA = (7, "acolhida", "7h-8h: acolhida, cafe da manha, checagem")
    BLOCO_I = (8, "bloco1", "8h-10h: bloco de aprendizagem I (ciencia/tec)")
    RECREIO = (10, "recreio", "10h-10h30: recreio, movimento")
    BLOCO_II = (10, "bloco2", "10h30-12h: bloco de aprendizagem II (cultura/corpo)")
    ALMOCO = (12, "almoco", "12h-13h: almoco com comida de verdade")
    PROJETO = (13, "projeto", "13h-15h: projeto real (eixo PRATICA)")
    OFICIO = (15, "oficio", "15h-16h: oficio/tecnico (mentoria comunitaria)")
    RODA = (16, "roda", "16h-16h30: roda de conversa (avaliacao do dia)")
    LANCHE = (16, "lanche", "16h30-17h: lanche")
    OPCIONAL = (17, "opcional", "17h-18h: opcional (esporte, arte, musica, robótica)")

    @property
    def hora(self) -> int:
        return self.value[0]

    @property
    def id(self) -> str:
        return self.value[1]

    @property
    def rotulo(self) -> str:
        return self.value[2]


# ============================================================================
# 2. DATACLASSES
# ============================================================================

@dataclass(frozen=True)
class EspecNivel:
    """Especificacao de um nivel de ensino."""
    nivel: NivelEnsino
    idade_min: int
    idade_max: int
    carga_horaria_semanal: int
    alunos_por_turma: int
    professor_por_turma: float    # pode ser 0.5 (compartilhado)
    eixos_obrigatorios: List[EixoCurricular]
    avaliacao: MetodoAvaliacao
    comida: bool
    transporte: bool
    acessibilidade_total: bool    # L5 integrado
    tecnologia_por_aluno: bool    # 1 dispositivo por aluno


@dataclass(frozen=True)
class CurriculoCivico:
    """Curriculo civico baseado nos principios da Republica."""
    principio: str
    idade_ensino: str             # "6-8", "9-11", "12-14", "15-17"
    conceito: str
    pratica: str                  # atividade pratica que demonstra o principio
    cordel: str                   # cordel que ensina (do open_cultural_constitution)


# ============================================================================
# 3. CURRICULO CIVICO (P1-P14 por faixa etaria)
# ============================================================================

def _init_curriculo_civico() -> List[CurriculoCivico]:
    return [
        CurriculoCivico(
            "P1", "6-8",
            "Ninguem manda sozinho. Decisoes sao em grupo.",
            "Votacao em sala: o que vamos fazer na aula de projeto?",
            "Ninguem manda sozinho nao / na Republica do povo",
        ),
        CurriculoCivico(
            "P2", "6-8",
            "Seu corpo e seu. Ninguem toca sem permissao.",
            "Roda de conversa: 'o que faz voce se sentir seguro?'",
            "O corpo e teu, minha gente / ninguem manda nele nao",
        ),
        CurriculoCivico(
            "P3", "9-11",
            "Todo trabalho tem valor. Faxineiro e doutor comecam em 1.0.",
            "Dia da profissao: cada aluno ensina o que um familiar faz.",
            "Trabalho e trabalho irmao / nao tem genero nem cor",
        ),
        CurriculoCivico(
            "P4", "9-11",
            "Decidir junto e melhor que decidir sozinho.",
            "Construcao de regras da turma: proposta, debate, votacao.",
            "Voto nao se compra nao / com promessa nem favor",
        ),
        CurriculoCivico(
            "P5", "12-14",
            "O que o Estado faz, voce pode ver. Caixa-preta nao.",
            "Visita a camara municipal. Pedir acesso a gastos.",
            "Caixa-preta pra que? / O que o Estado faz eu vejo",
        ),
        CurriculoCivico(
            "P6", "12-14",
            "Conhecimento e de todos. Sem paywall. Sem diploma.",
            "Projeto: ensinar algo que voce sabe pra quem nao sabe.",
            "Saber nao e de rico nao / nem de quem tem diploma",
        ),
        CurriculoCivico(
            "P7", "12-14",
            "Seguranca e cultura. Nmap e alfabetizacao, nao arma.",
            "Oficina: redes wifi, portas abertas, o que e firewall?",
            "Quem tem medo de nmap? / So quem tem porte pra esconder",
        ),
        CurriculoCivico(
            "P8", "15-17",
            "IA serve. O humano decide. Furia nao e inteligencia.",
            "Analise: qual app usa IA pra te deixar irritado?",
            "A maquina pensa? Nao. / O humano e que decide",
        ),
        CurriculoCivico(
            "P9", "12-14",
            "Estado nao divide. Diversidade e direito. Polarizar e doenca.",
            "Estudo de caso: como a noticia tenta te dividir?",
            "O Estado nao pode nao / brigar filho contra pai",
        ),
        CurriculoCivico(
            "P10", "15-17",
            "Drone nao vigia, nao mata, nao espia. Entrega e mapeia.",
            "Workshop: montar drone civico. Programar rota de mapeamento.",
            "O ceu nao e de ninguem / portanto e de todos nos",
        ),
        CurriculoCivico(
            "P11", "12-14",
            "Celular nao e requisito pra cidadania. E constituinte.",
            "Dia sem tela: como seria votar/pagar/saudade sem app?",
            "Exige celular pra que? / Pra votar, pra receitar?",
        ),
        CurriculoCivico(
            "P12", "15-17",
            "Republica nao tem exercito secreto. Defende transparente.",
            "Estudo: como Russia/China cooptam civis. Como Republica responde.",
            "Criminoso nao e amigo / nao e colega, nao e peao",
        ),
        CurriculoCivico(
            "P13", "15-17",
            "Voce vigia o Estado de volta. Quem tem poder, mostra.",
            "Projeto: pedir agenda e gastos de vereador. Publicar.",
            "Aceitou cargo, escuta / sua vida ali e nossa",
        ),
        CurriculoCivico(
            "P14", "15-17",
            "O dado e teu. Quem coletou e custodiante, nao dono.",
            "Auditoria: quais apps tem no seu celular? O que coletam?",
            "Voce gerou, e seu irmao / a empresa so pegou emprestado",
        ),
    ]


# ============================================================================
# 4. SPEC POR NIVEL
# ============================================================================

def _init_especs() -> List[EspecNivel]:
    return [
        EspecNivel(
            NivelEnsino.EDUCACAO_INFANTIL, 0, 5, 40, 12, 1.0,
            [EixoCurricular.CORPO, EixoCurricular.CULTURA, EixoCurricular.PRATICA],
            MetodoAvaliacao.NARRATIVA,
            True, True, True, False,
        ),
        EspecNivel(
            NivelEnsino.FUNDAMENTAL_I, 6, 10, 35, 24, 1.0,
            [EixoCurricular.ALFABETIZACAO, EixoCurricular.CIVISMO,
             EixoCurricular.CIENCIA, EixoCurricular.CULTURA, EixoCurricular.CORPO],
            MetodoAvaliacao.PORTFOLIO,
            True, True, True, True,
        ),
        EspecNivel(
            NivelEnsino.FUNDAMENTAL_II, 11, 14, 35, 28, 1.0,
            [EixoCurricular.ALFABETIZACAO, EixoCurricular.CIVISMO,
             EixoCurricular.CIENCIA, EixoCurricular.TECNOLOGIA,
             EixoCurricular.CULTURA, EixoCurricular.CORPO, EixoCurricular.PRATICA],
            MetodoAvaliacao.PROJETO,
            True, True, True, True,
        ),
        EspecNivel(
            NivelEnsino.MEDIO, 15, 17, 35, 30, 0.8,
            list(EixoCurricular),
            MetodoAvaliacao.PROJETO,
            True, True, True, True,
        ),
        EspecNivel(
            NivelEnsino.SUPERIOR, 18, 99, 20, 40, 0.3,
            list(EixoCurricular),
            MetodoAvaliacao.DEMONSTRACAO,
            False, False, True, True,
        ),
        EspecNivel(
            NivelEnsino.TECNICO, 14, 99, 20, 20, 0.5,
            [EixoCurricular.TECNOLOGIA, EixoCurricular.PRATICA,
             EixoCurricular.CIENCIA],
            MetodoAvaliacao.DEMONSTRACAO,
            True, True, True, True,
        ),
        EspecNivel(
            NivelEnsino.CONTINUADA, 0, 99, 4, 15, 0.2,
            list(EixoCurricular),
            MetodoAvaliacao.RODA,
            False, False, True, False,
        ),
    ]


# ============================================================================
# 5. SPEC DO SISTEMA DE EDUCACAO
# ============================================================================

class EducationSystem:
    """
    Spec do sistema de educacao nacional da Republica.

    Curriculo civico (P1-P14). Avaliacao por projeto. Escola integral.
    Professor e autoridade. Comida de verdade. Inclusao total.
    """

    NOME = "OpenEducation"
    VERSAO = "0.1.0-spec"

    PRINCIPIOS_PEDAGOGICOS = [
        "Aprender fazendo, nao ouvindo",
        "Professor e autoridade, nao burocrata",
        "Sem prova ate 12 anos (Finlandia prova que funciona)",
        "Comida de verdade: escola que alimenta aprende melhor",
        "Tecnologia serve, nao substitui o humano",
        "Cordel ensina quem nao le codigo",
        "Deficiencia nao e excecao -- e diversidade (L5)",
        "Curriculo civico desde os 6 anos (P1-P14)",
        "Avaliacao por projeto, nao por memoria",
        "Escola e comunidade, nao predio",
    ]

    def __init__(self) -> None:
        self.especs: List[EspecNivel] = _init_especs()
        self.curriculo: List[CurriculoCivico] = _init_curriculo_civico()

    # -- catalogos ---------------------------------------------------------

    def niveis(self) -> List[Dict[str, Any]]:
        return [
            {
                "nivel": e.nivel.id,
                "rotulo": e.nivel.rotulo,
                "idade": f"{e.idade_min}-{e.idade_max}",
                "carga_h": e.carga_horaria_semanal,
                "turma": e.alunos_por_turma,
                "eixos": [ax.id for ax in e.eixos_obrigatorios],
                "avaliacao": e.avaliacao.id,
                "comida": e.comida,
                "transporte": e.transporte,
                "a11y": e.acessibilidade_total,
                "tech_aluno": e.tecnologia_por_aluno,
            }
            for e in self.especs
        ]

    def curriculo_civico(self) -> List[Dict[str, str]]:
        return [
            {
                "principio": c.principio,
                "idade": c.idade_ensino,
                "conceito": c.conceito,
                "pratica": c.pratica,
                "cordel": c.cordel,
            }
            for c in self.curriculo
        ]

    def curriculo_por_idade(self, idade: int) -> List[CurriculoCivico]:
        resultado = []
        for c in self.curriculo:
            idades = c.idade_ensino.split("-")
            lo, hi = int(idades[0]), int(idades[1])
            if lo <= idade <= hi:
                resultado.append(c)
        return resultado

    # -- dia escolar ---------------------------------------------------------

    def dia_escolar(self) -> List[Dict[str, Any]]:
        return [
            {"hora": f"{d.hora}h", "bloco": d.id, "descricao": d.rotulo}
            for d in DiaEscolar
        ]

    # -- papeis --------------------------------------------------------------

    def papeis_escolares(self) -> List[Dict[str, str]]:
        return [{"id": p.id, "rotulo": p.rotulo} for p in PapelEscolar]

    # -- comparativo ---------------------------------------------------------

    def comparativo_finlandia(self) -> List[Dict[str, str]]:
        return [
            {"aspecto": "Prova antes dos 12 anos",
             "finlandia": "Nenhuma",
             "brasil_hoje": "Provinha/Prova Brasil desde 7 anos",
             "republica": "Nenhuma (Finlandia prova)"},
            {"aspecto": "Licao de casa",
             "finlandia": "Minima ate 12 anos",
             "brasil_hoje": "Excessiva desde 7 anos",
             "republica": "Minima ate 12 anos"},
            {"aspecto": "Alunos por turma",
             "finlandia": "Max 20",
             "brasil_hoje": "30-45",
             "republica": "Max 24 (fundamental)"},
            {"aspecto": "Formacao do professor",
             "finlandia": "Mestrado obrigatorio, respeitado",
             "brasil_hoje": "Licenciatura, subvalorizado",
             "republica": "Mestrado, salario digno (P3)"},
            {"aspecto": "Dia escolar",
             "finlandia": "Integral com comida",
             "brasil_hoje": "Meio periodo, sem comida em muitas",
             "republica": "Integral + comida de verdade"},
            {"aspecto": "Curriculo civico",
             "finlandia": "Cidadania desde cedo",
             "brasil_hoje": "Ensino religioso / fragmentado",
             "republica": "P1-P14 desde 6 anos"},
            {"aspecto": "Tecnologia",
             "finlandia": "1 dispositivo/aluno",
             "brasil_hoje": "Lab compartilhado quebrado",
             "republica": "1 dispositivo/aluno + IA local"},
            {"aspecto": "Inclusao",
             "finlandia": "Total (deficiencia na mesma sala)",
             "brasil_hoje": "Sala de recursos separada",
             "republica": "Total (L5 integrado)"},
        ]

    # -- custo estimado ------------------------------------------------------

    def custo_por_aluno_ano(self) -> Dict[str, Any]:
        """Custo estimado por aluno/ano (referencia Finlandia)."""
        return {
            "finlandia_usd": 12000,
            "finlandia_brl": 60000,
            "brasil_hoje_brl": 5500,
            "republica_alvo_brl": 18000,
            "republica_vs_brasil": "3.3x do atual",
            "republica_vs_finlandia": "30% da Finlandia",
            "justificativa": (
                "R$ 18k/aluno/ano. Brasil investe R$ 5.5k. "
                "A diferenca e R$ 12.5k/aluno/ano. "
                "40 milhoes de alunos = R$ 500 bi/ano adicional. "
                "Parece muito? E 1/3 do que se evadiu em impostos (R$ 1.5 tri/ano)."
            ),
        }

    # -- scorecard ----------------------------------------------------------

    def scorecard(self) -> Dict[str, Any]:
        return {
            "sistema": self.NOME,
            "versao": self.VERSAO,
            "niveis_ensino": len(self.especs),
            "eixos_curriculares": len(list(EixoCurricular)),
            "principios_civicos": len(self.curriculo),
            "metodos_avaliacao": len(list(MetodoAvaliacao)),
            "papeis_escolares": len(list(PapelEscolar)),
            "blocos_dia": len(list(DiaEscolar)),
            "principios_pedagogicos": len(self.PRINCIPIOS_PEDAGOGICOS),
        }


# ============================================================================
# 6. DEMO
# ============================================================================

def _demo() -> None:
    edu = EducationSystem()

    print("=" * 70)
    print(f"{edu.NOME} v{edu.VERSAO} -- Sistema de Educacao Nacional")
    print("=" * 70)

    # --- Principios ---
    print(f"\n[PRINCIPIOS PEDAGOGICOS ({len(edu.PRINCIPIOS_PEDAGOGICOS)})]\n")
    for i, p in enumerate(edu.PRINCIPIOS_PEDAGOGICOS, 1):
        print(f"  {i}. {p}")

    # --- Niveis ---
    print(f"\n\n[NIVEIS DE ENSINO ({len(edu.especs)})]\n")
    print(f"  {'NIVEL':<12} {'IDADE':<8} {'CARGA':>6} {'TURMA':>6} {'AVALIACAO':<16} {'COMIDA':>6} {'A11Y':>5}")
    print(f"  {'-'*65}")
    for n in edu.niveis():
        print(f"  {n['nivel']:<12} {n['idade']:<8} {n['carga_h']:>5}h {n['turma']:>6} "
              f"{n['avaliacao']:<16} {'sim' if n['comida'] else 'nao':>6} "
              f"{'sim' if n['a11y'] else 'nao':>5}")

    # --- Eixos ---
    print(f"\n\n[EIXOS CURRICULARES ({len(list(EixoCurricular))})]\n")
    for ax in EixoCurricular:
        print(f"  {ax.id:<18} {ax.rotulo}")

    # --- Curriculo civico ---
    print(f"\n\n[CURRICULO CIVICO ({len(edu.curriculo)} PRINCIPIOS)]\n")
    for c in edu.curriculo_civico():
        print(f"  [{c['principio']}] Idade {c['idade']}")
        print(f"  Conceito: {c['conceito']}")
        print(f"  Pratica: {c['pratica']}")
        print(f"  Cordel: \"{c['cordel']}\"")
        print()

    # --- Dia escolar ---
    print(f"\n[DIA ESCOLAR INTEGRAL]\n")
    for d in edu.dia_escolar():
        print(f"  {d['hora']:<6} [{d['bloco']}] {d['descricao']}")

    # --- Papeis ---
    print(f"\n\n[PAPEIS ESCOLARES ({len(list(PapelEscolar))})]\n")
    for p in edu.papeis_escolares():
        print(f"  {p['id']:<14} {p['rotulo']}")

    # --- Comparativo ---
    print("\n\n[COMPARATIVO: FINLANDIA vs BRASIL HOJE vs REPUBLICA]\n")
    print(f"  {'ASPECTO':<30} {'FINLANDIA':<25} {'BRASIL HOJE':<25} {'REPUBLICA'}")
    print(f"  {'-'*100}")
    for c in edu.comparativo_finlandia():
        print(f"  {c['aspecto']:<30} {c['finlandia']:<25} {c['brasil_hoje']:<25} {c['republica']}")

    # --- Custo ---
    print("\n\n[CUSTO POR ALUNO/ANO]\n")
    for k, v in edu.custo_por_aluno_ano().items():
        print(f"  {k}: {v}")

    # --- Scorecard ---
    print("\n\n[SCORECARD]")
    sc = edu.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<28} {v}")


if __name__ == "__main__":
    _demo()
