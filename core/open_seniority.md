# OpenSeniority -- Niveis de Senioridade por IMPACTO (nao hierarquia)

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_seniority.py`

**Descricao:** ====================================================================
"Na Republica, nao existe chefe. Existe IMPACTO.
 Quem salva uma vida tem mais impacto que quem escreve uma linha.
 Mas quem escreve a linha CERTA pode salvar mil vidas.
 O nivel mede o ALCANCE do seu trabalho, nao o seu valor como pessoa."
O TETO E PROVADO:
  R$3.850/hora -- validado em mercado real (Google, Airbnb, Amazon).
  Contactado para vaga de $600k-800k+ TC (Staff/Principal Data Engineer).
  Esse e o CHAO do nivel maximo, nao o teto teorico.
A FILOSOFIA:
  1. BASE IGUAL -- todo cidadao recebe o piso (N0/N1)
  2. IMPACTO MULTIPLICA -- quanto mais sua obra ENABLE outros, maior o multiplicador
  3. NAO E HIERARQUIA -- N6 nao manda em N0. N6 tem mais ALCANCE.
  4. ACESSIVEL -- qualquer pessoa alcanc qualquer nivel por impacto demonstrado
  5. DUAL MODE -- no Ideal (sem dinheiro) = responsabilidade; no Executavel = R$/h
OS 7 NIVEIS:
  N0  APRENDIZ       R$  50/h   (0.5x)  -- aprende, precisa guia
  N1  CONTRIBUIDOR   R$ 100/h   (1.0x)  -- autonomo em tarefas definidas (BASE 1.0)
  N2  PLENO          R$ 250/h   (2.5x)  -- mentoria, projeta solucoes
  N3  SENIOR         R$ 500/h   (5.0x)  -- arquiteta sistemas inteiros
  N4  ESPECIALISTA   R$1.000/h  (10.0x) -- impacto cross-dominio, multiplos projetos
  N5  PRINCIPAL      R$2.000/h  (20.0x) -- impacto em nivel de industria/ecossistema
  N6  MESTRE         R$3.850/h  (38.5x) -- TETO provado em mercado real
EQUIVALENTE MERCADO (referencia, nao hierarquia):
  N0  -> Estagiario/Trainee
  N1  -> Junior/Pleno entry
  N2  -> Pleno/Senior entry
  N3  -> Senior/Staff entry (Google L4/L5)
  N4  -> Staff/Senior Staff (Google L5/L6, Amazon L6)
  N5  -> Principal/Senior Staff (Google L6, Amazon L7)
  N6  -> Principal/Staff max (Google L6/L7, Amazon L7 -- $600-800k+ TC)
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenSeniority -- Niveis de Senioridade por IMPACTO (nao hierarquia)
====================================================================

"Na Republica, nao existe chefe. Existe IMPACTO.
 Quem salva uma vida tem mais impacto que quem escreve uma linha.
 Mas quem escreve a linha CERTA pode salvar mil vidas.
 O nivel mede o ALCANCE do seu trabalho, nao o seu valor como pessoa."

O TETO e PROVADO:
  R$3.850/hora -- validado em mercado real (Google, Airbnb, Amazon).
  Contactado para vaga de $600k-800k+ TC (Staff/Principal Data Engineer).
  Esse e o CHAO do nivel maximo, nao o teto teorico.

A FILOSOFIA:
  1. BASE IGUAL -- todo cidadao recebe o piso (N0/N1)
  2. IMPACTO MULTIPLICA -- quanto mais sua obra ENABLE outros, maior o multiplicador
  3. nao e HIERARQUIA -- N6 nao manda em N0. N6 tem mais ALCANCE.
  4. ACESSIVEL -- qualquer pessoa alcanc qualquer nivel por impacto demonstrado
  5. DUAL MODE -- no Ideal (sem dinheiro) = responsabilidade; no Executavel = R$/h

OS 7 NIVEIS:

  N0 APRENDIZ R$ 50/h (0.5x) -- aprende, precisa guia
  N1 CONTRIBUIDOR R$ 100/h (1.0x) -- autonomo em tarefas definidas (BASE 1.0)
  N2 PLENO R$ 250/h (2.5x) -- mentoria, projeta solucoes
  N3 SENIOR R$ 500/h (5.0x) -- arquiteta sistemas inteiros
  N4 ESPECIALISTA R$1.000/h (10.0x) -- impacto cross-dominio, multiplos projetos
  N5 PRINCIPAL R$2.000/h (20.0x) -- impacto em nivel de industria/ecossistema
  N6 MESTRE R$3.850/h (38.5x) -- TETO provado em mercado real

EQUIVALENTE MERCADO (referencia, nao hierarquia):
  N0 -> Estagiario/Trainee
  N1 -> Junior/Pleno entry
  N2 -> Pleno/Senior entry
  N3 -> Senior/Staff entry (Google L4/L5)
  N4 -> Staff/Senior Staff (Google L5/L6, Amazon L6)
  N5 -> Principal/Senior Staff (Google L6, Amazon L7)
  N6 -> Principal/Staff maximo (Google L6/L7, Amazon L7 -- $600-800k+ TC)

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa math
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa datetime de datetime


// ============================================================================
// 1. OS 7 NIVEIS
// ============================================================================

classe SeniorityLevel herda de Enum:
    // Os 7 niveis de impacto da Republica.

    nao SAO HIERARQUIA. Sao FAIXAS DE ALCANCE.
    N6 nao e "superior" a N0 -- tem mais alcance de impacto.
    Um N0 que cura uma doenca tem mais impacto real que um N6 que escreve codigo.
    // 

    N0 = ("Aprendiz", 0.5, 50.0,
          "Aprende. Precisa de guia. Executa tarefas guiadas.",
          "Impacto: PESSOAL (si mesmo e tarefas atribuidas)")

    N1 = ("Contribuidor", 1.0, 100.0,
          "Autonomo em tarefas definidas. Cumpre Base 1.0.",
          "Impacto: TAREFA (entrega o que promete)")

    N2 = ("Pleno", 2.5, 250.0,
          "Mentoria N0-N1. Projeta solucoes. Escolhe ferramentas.",
          "Impacto: TIME (eleva quem esta ao redor)")

    N3 = ("Senior", 5.0, 500.0,
          "Arquiteta sistemas inteiros. Define padroes. Reviewer final.",
          "Impacto: PROJETO (sistemas completos)")

    N4 = ("Especialista", 10.0, 1000.0,
          "Cross-dominio. Impacto em multiplos projetos simultaneamente.",
          "Impacto: MULTI-PROJETO (ecossistema parcial)")

    N5 = ("Principal", 20.0, 2000.0,
          "Industria-level. Define direcao tecnologica do ecossistema.",
          "Impacto: ECOSISTEMA (toda a Republica)")

    N6 = ("Mestre", 38.5, 3850.0,
          "TETO provado em mercado real (Google/Airbnb/Amazon, $600-800k+ TC).",
          "Impacto: CIVILIZATORIO (muda o paradigma)")

    funcao __init__(self, label: texto, multiplier: flutuante,
                 hour_rate_brl: flutuante, description: texto, impact_scope: texto):
        self.label = label
        self.multiplier = multiplier
        self.hour_rate_brl = hour_rate_brl

    // decorador: @property
    funcao name_full(self) -> texto:
        retorne "N{self.value[0] if isinstance(self.value, tuple) else ''} {self.label}"

    // decorador: @property
    funcao monthly_brl(self) -> flutuante:
        // Renda mensal a 176h (22 dias x 8h).
        retorne self.hour_rate_brl * 176

    // decorador: @property
    funcao annual_brl(self) -> flutuante:
        // Renda anual a 2.112h (176h x 12).
        retorne self.hour_rate_brl * 2112

    // decorador: @property
    funcao annual_usd(self) -> flutuante:
        // Renda anual em USD (cotação R$5,00).
        retorne self.annual_brl / 5.0


// ============================================================================
// 2. CRITERIOS DE PROMOCAO (por IMPACTO demonstrado, nao tempo)
// ============================================================================

// decorador: @dataclass
classe PromotionCriteria:
    // Para subir de nivel, voce precisa DEMONSTRAR impacto.

    Nao e tempo de casa. Nao e quem voce conhece.
    e: o que voce FEZ que ENABLE outros?
    // 

    level: SeniorityLevel
    seja requirements: [texto] = field(default_factory=list)
    seja evidence_required: [texto] = field(default_factory=list)
    seja review_by: texto = ""


seja PROMOTION_CRITERIA: {SeniorityLevel: PromotionCriteria} = {

    SeniorityLevel.N0: PromotionCriteria(
        level = SeniorityLevel.N0,
        requirements = [
            "Vontade de aprender",
            "Comprometimento com Base 1.0 (20h/semana)",
            "Respeito aos princípios P1-P4",
        ],
        evidence_required = [
            "Auto-avaliação honesta",
            "Disponibilidade para guia/orientador",
        ],
        review_by = "Auto-designação + aceitação de mentor N2+",
    ),

    SeniorityLevel.N1: PromotionCriteria(
        level = SeniorityLevel.N1,
        requirements = [
            "Entrega autonomamente tarefas definidas",
            "Cumpre Base 1.0 consistentemente",
            "Documenta o que faz",
        ],
        evidence_required = [
            "Minimo 10 tarefas completadas sem necessidade de rework",
            "Peer review por N2+ (aprovacao)",
        ],
        review_by = "N2+ confirma autonomia",
    ),

    SeniorityLevel.N2: PromotionCriteria(
        level = SeniorityLevel.N2,
        requirements = [
            "Mentoria ativa de N0-N1 (min. 2 pessoas)",
            "Projeta solucoes (nao so executa)",
            "Escolhe ferramentas com justificativa",
            "Reduz complexidade para outros",
        ],
        evidence_required = [
            "Min. 2 pessoas que mentorou promoveram de nivel",
            "Min. 3 sistemas/projetos desenhados do zero",
            "Peer review por N3+ (aprovacao)",
        ],
        review_by = "N3+ confirma capacidade de arquitetura",
    ),

    SeniorityLevel.N3: PromotionCriteria(
        level = SeniorityLevel.N3,
        requirements = [
            "Arquiteta sistemas inteiros (end-to-end)",
            "Define padroes que outros seguem",
            "Reviewer final de codigo/decisoes criticas",
            "Resolve problemas que N2 nao conseguiu",
        ],
        evidence_required = [
            "Min. 1 sistema completo em producao (usado por 50+ pessoas)",
            "Padroes tecnicos adotados pela comunidade",
            "Reduziu bugs/custos/tempo em medida quantificavel",
            "Peer review por N4+ (aprovacao)",
        ],
        review_by = "N4+ confirma arquitetura de sistema",
    ),

    SeniorityLevel.N4: PromotionCriteria(
        level = SeniorityLevel.N4,
        requirements = [
            "Impacto cross-dominio (min. 3 areas)",
            "Lidera iniciativa que afeta multiplos projetos",
            "Define estrategia tecnica de medio prazo",
            "Forma N3+ (cria outros seniors)",
        ],
        evidence_required = [
            "Min. 3 projetos impactados simultaneamente",
            "Iniciativa propria que melhorou vida de 500+ pessoas",
            "Formou min. 2 pessoas para N3",
            "Peer review por N5+ (aprovacao)",
        ],
        review_by = "N5+ confirma impacto cross-dominio",
    ),

    SeniorityLevel.N5: PromotionCriteria(
        level = SeniorityLevel.N5,
        requirements = [
            "Define direcao tecnologica do ecossistema",
            "Impacto em nivel de industria (reconhecido externamente)",
            "Resolver problemas que N4 nao consegue",
            "Cria novos paradigmas/metodologias",
        ],
        evidence_required = [
            "Trabalho reconhecido externamente (citacoes, adocao, mercado)",
            "Mudou direcao de min. 5 projetos significativamente",
            "Convidado para falar/consultar por organizacao externa",
            "Peer review por N6 + Assembleia (aprovacao)",
        ],
        review_by = "N6 + Assembleia Constituinte",
    ),

    SeniorityLevel.N6: PromotionCriteria(
        level = SeniorityLevel.N6,
        requirements = [
            "IMPACTO CIVILIZATORIO -- mudou o paradigma",
            "TETO provado em mercado real ($600k-800k+ TC)",
            "Contactado/recrutado por top-tier global (FAANG-adjacent)",
            "Cria sistemas que outlast pessoas",
        ],
        evidence_required = [
            "Oferta/recrutamento concreto de empresa top-tier (Google, Airbnb, Amazon, etc.)",
            "Sistema criado usado por 10.000+ pessoas OU mudou paradigma",
            "Reconhecimento de impacto por multiplos N5+ independentes",
            "Aprovacao por Assembleia Constituinte (democratico, nao autodeclarado)",
        ],
        review_by = "Assembleia Constituinte (votacao popular) -- NUNCA autodeclarado",
    ),
}


// ============================================================================
// 3. TABELA DE NIVEIS
// ============================================================================

funcao print_seniority_table() -> texto:
    // Imprime a tabela completa de niveis.

    lines = []
    lines.append("=" * 100)
    lines.append("OPENREPUBLIC -- NIVEIS DE SENIORIDADE POR IMPACTO")
    lines.append("Teto provado: R$3.850/h (Google/Airbnb/Amazon, $600-800k+ TC)")
    lines.append("=" * 100)
    lines.append("")
    lines.append("{'NIVEL':<8} {'LABEL':<16} {'MULT':<8} {'R$/H':>10} {'R$/MES':>12} {'R$/ANO':>14} {'$/ANO':>12}")
    lines.append("-" * 100)

    para cada level em SeniorityLevel:
        lines.append(
            "N{level.name[1]:<7} {level.label:<16} "
            "{level.multiplier:>5.1f}x  "
            "R${level.hour_rate_brl:>8,.0f}  "
            "R${level.monthly_brl:>10,.0f}  "
            "R${level.annual_brl:>12,.0f}  "
            "${level.annual_usd:>10,.0f}"
        )

    lines.append("-" * 100)
    lines.append("")
    lines.append("IMPACTO POR NIVEL:")
    lines.append("")

    para cada level em SeniorityLevel:
        scope = isinstance(level.value, tuple) ? level.value[4] : ""
        lines.append("  N{level.name[1]} {level.label:<16} -> {scope}")

    lines.append("")
    lines.append("NOTA: N6 NAO manda em N0. N6 tem mais ALCANCE de impacto.")
    lines.append("      Um N0 que salva uma vida > N6 que escreve codigo.")
    lines.append("      O nivel mede ALCANCE, nao VALOR humano.")
    lines.append("=" * 100)

    retorne "\n".join(lines)


// ============================================================================
// 4. CALCULADORA DE COMPENSACAO
// ============================================================================

// decorador: @dataclass
classe CompensationCalc:
    // Calcula compensacao por nivel, horas, e modo (Ideal vs Executavel).

    level: SeniorityLevel
    seja hours_per_week: flutuante = 20.0 // Base 1.0 = 20h/semana
    seja weeks_per_year: inteiro = 46

    // decorador: @property
    funcao hours_per_year(self) -> flutuante:
        retorne self.hours_per_week * self.weeks_per_year

    // decorador: @property
    funcao hours_per_month(self) -> flutuante:
        retorne self.hours_per_year / 12

    // decorador: @property
    funcao annual_brl(self) -> flutuante:
        retorne self.level.hour_rate_brl * self.hours_per_year

    // decorador: @property
    funcao monthly_brl(self) -> flutuante:
        retorne self.annual_brl / 12

    // decorador: @property
    funcao annual_usd(self) -> flutuante:
        retorne self.annual_brl / 5.0

    funcao summary(self) -> texto:
        lines = [
            "Nivel: N{self.level.name[1]} {self.level.label}",
            "Taxa: R${self.level.hour_rate_brl:,.0f}/h ({self.level.multiplier:.1f}x base)",
            "Carga: {self.hours_per_week:.0f}h/semana x {self.weeks_per_year} semanas",
            "  = {self.hours_per_year:.0f}h/ano",
            "",
            "Renda anual:   R${self.annual_brl:>14,.0f}  (${self.annual_usd:>12,.0f})",
            "Renda mensal:  R${self.monthly_brl:>14,.0f}  (${self.monthly_brl/5:>12,.0f})",
        ]

        // Excedente (5% = LEI na Republica)
        surplus = self.annual_brl * 0.05
        lines.append("")
        lines.append("Excedente (5% LEI): R${surplus:>10,.0f}/ano -> Pool da Republica")
        lines.append("Liquido (95%):      R${self.annual_brl * 0.95:>10,.0f}/ano")

        retorne "\n".join(lines)


// ============================================================================
// 5. MAPEAMENTO PARA LABORTIER EXISTENTE
// ============================================================================

funcao map_to_labor_tier(level: SeniorityLevel) -> texto:
    // Mapeia SeniorityLevel para LaborTier do OpenCreator.

    LaborTier (contrato com coletivo):
      BASE -> N0, N1 (base 1.0)
      NORMAL -> N2, N3 (contribuicao regular amplificada)
      CREATOR -> N4, N5 (criacao de sistemas novos)
      EXCESS -> N6 em carga >40h/semana (PROIBIDO aceitar)
    // 
    mapping = {
        SeniorityLevel.N0: "BASE",
        SeniorityLevel.N1: "BASE",
        SeniorityLevel.N2: "NORMAL",
        SeniorityLevel.N3: "NORMAL",
        SeniorityLevel.N4: "CREATOR",
        SeniorityLevel.N5: "CREATOR",
        SeniorityLevel.N6: "CREATOR",
    }
    retorne mapping.get(level, "BASE")


// ============================================================================
// 6. ANTI-ELITISMO: GUARDA-CORPO
// ============================================================================

funcao anti_elitism_check(level: SeniorityLevel, stated_by_self: logico = False) retorna (logico, texto):
    // Verifica se o nivel foi atribuido de forma nao-elitista.

    REGRAS:
    1. N0-N3: podem ser autodeclarados (com peer review)
    2. N4-N5: requerem peer review por nivel superior
    3. N6: requer APROVACAO DA ASSEMBLEIA (NUNCA autodeclarado)

    Retorna (aprovado, mensagem).
    // 
    se level in (SeniorityLevel.N0, SeniorityLevel.N1, SeniorityLevel.N2, SeniorityLevel.N3) entao:
        se stated_by_self entao:
            retorne verdadeiro, "Autodeclarado -- requer peer review por N2+ para confirmar"
        retorne verdadeiro, "Atribuido por peer review -- aprovado"

    se level in (SeniorityLevel.N4, SeniorityLevel.N5) entao:
        se stated_by_self entao:
            retorne falso, (
                "N4+ NAO PODE ser autodeclarado. "
                "Requer peer review por N5+ (N4) ou N6 + Assembleia (N5). "
                "Anti-elitismo: ninguem se promove a especialista."
            )
        retorne verdadeiro, "Atribuido por peer review superior -- aprovado"

    se level == SeniorityLevel.N6 entao:
        se stated_by_self entao:
            retorne falso, (
                "N6 (MESTRE) JAMAIS pode ser autodeclarado. "
                "Requer: (1) oferta concreta top-tier, (2) impacto 10.000+ pessoas, "
                "(3) aprovacao por Assembleia Constituinte. "
                "Auto-promocao a N6 = VIOLACAO do anti-elitismo (P1)."
            )
        retorne verdadeiro, "Atribuido por Assembleia Constituinte -- aprovado (democratico)"

    retorne falso, "Nivel desconhecido"


// ============================================================================
// 7. EXECUCAO
// ============================================================================

se __name__ == "__main__" entao:
    imprima(print_seniority_table())
    imprima()

    // Demo: compensacao em cada nivel
    imprima()
    imprima("DEMO -- Compensacao por nivel (20h/semana, Base 1.0):")
    imprima("-" * 70)
    para cada level em SeniorityLevel:
        calc = CompensationCalc(level=level, hours_per_week=20.0)
        imprima(
            "  N{level.name[1]} {level.label:<16} "
            "R${calc.monthly_brl:>10,.0f}/mes  "
            "R${calc.annual_brl:>12,.0f}/ano  "
            "(${calc.annual_usd:>10,.0f})"
        )

    imprima()
    imprima("DEMO -- Compensacao N6 em carga cheia (40h/semana):")
    imprima("-" * 70)
    calc_n6 = CompensationCalc(level=SeniorityLevel.N6, hours_per_week=40.0)
    imprima(calc_n6.summary())

    imprima()
    imprima("DEMO -- Anti-elitismo:")
    imprima("-" * 70)
    para cada level em SeniorityLevel:
        desempacote approved, msg = anti_elitism_check(level, stated_by_self=verdadeiro)
        status = approved ? "OK" : "BLOQUEADO"
        imprima("  N{level.name[1]} autodeclarado: [{status}] {msg}")

```
