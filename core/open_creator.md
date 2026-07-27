# OpenCreator -- O Contrato Individual-Coletivo

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_creator.py`

**Descricao:** ==============================================
"Quanto de mim pertence ao coletivo?"
"Nao tudo. Nunca tudo. O corpo e meu. O maximo e meu.
 Mas algo e nosso. E esse algo e sagrado."
ESTE E O DOCUMENTO MAIS IMPORTANTE DA REPUBLICA.
Porque ele define o LIMITE entre o EU e o NOS.
O PROBLEMA QUE NINGUEM RESOLVEU:
  Toda revolucao tem um criador. Toda utopia tem um arquiteto.
  O criador trabalha 16h/dia. Da tudo. Sacrifica saude, sono, vida.
  Depois chega o coletivo. E pergunta:
  "Obrigado por construir tudo. Agora, quanto e seu?"
  Capitalismo diz: "TUDO. Voce e o fundador. Aqui estao seus bilhoes."
  Comunismo diz:  "NADA. Voce e um trabalhador como outro qualquer."
  Republicas falham porque escolhem um dos dois errados.
  A RESPOSTA DA OPENREPUBLIC:
  O criador NAO e dono do que criou (bem comum, CC0, anti-propriedade).
  MAS o criador NAO e escravo do que criou (autonomia corporal absoluta).
  O criador NAO tem poder especial sobre o que criou (anti-elitismo).
  MAS o criador NAO tem obrigacao de continuar criando (limite de doacao).
  O criador JÁ cumpriu o contrato base 1.0.
  Tudo que faz alem disso e DOM, nao DIVIDA.
Author: OpenRepublic Team
Principio central: "O coletivo nao pode sugar o criador ate seca-lo."

---

```portugol++

// !/usr/bin/env python3
// 
OpenCreator -- O Contrato Individual-Coletivo
==============================================

"Quanto de mim pertence ao coletivo?"
"Nao tudo. Nunca tudo. O corpo e meu. O maximo e meu.
 Mas algo e nosso. e esse algo e sagrado."

ESTE e O DOCUMENTO MAIS IMPORTANTE DA REPUBLICA.
Porque ele define o LIMITE entre o EU e o NOS.

O PROBLEMA QUE NINGUEM RESOLVEU:
  Toda revolucao tem um criador. Toda utopia tem um arquiteto.
  O criador trabalha 16h/dia. Da tudo. Sacrifica saude, sono, vida.

  Depois chega o coletivo. e pergunta:
  "Obrigado por construir tudo. Agora, quanto e seu?"

  Capitalismo diz: "TUDO. Voce e o fundador. Aqui estao seus bilhoes."
  Comunismo diz:  "NADA. Voce e um trabalhador como outro qualquer."
  Republicas falham porque escolhem um dos dois errados.

  A RESPOSTA DA OPENREPUBLIC:

  O criador nao e dono do que criou (bem comum, CC0, anti-propriedade).
  MAS o criador nao e escravo do que criou (autonomia corporal absoluta).

  O criador nao tem poder especial sobre o que criou (anti-elitismo).
  MAS o criador nao tem obrigacao de continuar criando (limite de doacao).

  O criador JÁ cumpriu o contrato base 1.0.
  Tudo que faz alem disso e DOM, nao DIVIDA.

Author: OpenRepublic Team
Principio central: "O coletivo nao pode sugar o criador ate seca-lo."
// 

// importa annotations de __future__

// importa math
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict de collections


// ============================================================================
// 1. O CONTRATO BASE -- O QUE CADA PESSOA DEVE
// ============================================================================

classe LaborTier herda de Enum:
    // Os 4 niveis de relacao entre individuo e coletivo.

    Nivel 1 (MINIMO): Base 1.0 -- todo cidadao deve.
    Nivel 2 (NORMAL): Contribuicao regular -- a maioria da.
    Nivel 3 (CRIADOR): Construcao de sistemas novos -- poucos dao.
    Nivel 4 (EXCESSO): Alem do limite saudavel -- PROIBIDO aceitar.
    // 
    BASE = "base_1.0"
    NORMAL = "normal"
    CREATOR = "criador"
    EXCESS = "excesso_proibido"


// decorador: @dataclass
classe LaborObligation:
    // O que CADA cidadao deve ao coletivo. Ninguem escapa. Ninguem excede.

    BASE 1.0 -- O CONTRATO MINIMO:
    - 20h/semana de trabalho reconhecido (meio periodo util)
    - ou equivalente em impacto (uma cirurgia = varias semanas)
    - Nao pode comprar saida com credito
    - Nao pode transferir para outro
    - Nao pode acumular (fazer 80h numa semana nao zera as proximas 3)

    SAIDAS LEGITIMAS DA BASE:
    - Doenca (comprovada, sem julgamento)
    - Cuidado de filho/idoso dependente (conta como contribuicao)
    - Estudo que beneficia a comunidade (conta como contribuicao)
    - Descanso medicinal (autonomia corporal -- corpo manda)
    - Idade (acima de 65: voluntario, nao obrigatorio)
    // 
    seja base_hours_per_week: flutuante = 20.0
    seja max_hours_per_week: flutuante = 40.0 // LIMITE: Republica PROIBE mais que isso
    seja excess_threshold: flutuante = 50.0 // Acima disto = EXCESSO, nao aceito
    seja weeks_per_year: inteiro = 46 // 46 semanas uteis (6 de descanso garantido)
    seja rest_days_per_week: inteiro = 2 // MINIMO 2 dias sem trabalho obrigatorio
    seja min_vacation_weeks: inteiro = 4 // MINIMO 4 semanas de ferias/ano

    // decorador: @property
    funcao base_annual_hours(self) -> flutuante:
        // Horas base anuais que cada cidadao deve.
        retorne self.base_hours_per_week * self.weeks_per_year

    // decorador: @property
    funcao max_annual_hours(self) -> flutuante:
        // Maximo de horas/ano que a Republica ACEITA de qualquer pessoa.
        retorne self.max_hours_per_week * self.weeks_per_year

    // decorador: @property
    funcao excess_annual_hours(self) -> flutuante:
        // Acima disso, a Republica DIZ NAO. Para o seu proprio bem.
        retorne self.excess_threshold * self.weeks_per_year

    // decorador: @property
    funcao contract(self) -> texto:
        retorne (
            "CONTRATO BASE 1.0:\n"
            "  Cada cidadao: {self.base_hours_per_week}h/semana "
            "({self.base_annual_hours:.0f}h/ano)\n"
            "  Maximo aceito: {self.max_hours_per_week}h/semana "
            "({self.max_annual_hours:.0f}h/ano)\n"
            "  LIMITE INEGOCIAVEL: {self.excess_threshold}h/semana "
            "({self.excess_annual_hours:.0f}h/ano)\n"
            "  Acima do limite = Republica recusa o trabalho.\n"
            "  Descanso: {self.rest_days_per_week} dias/semana + "
            "{self.min_vacation_weeks} semanas ferias."
        )


// ============================================================================
// 2. O PARADOXO DO CRIADOR
// ============================================================================

classe CreatorParadox herda de Enum:
    // O problema fundamental que toda civilizacao enfrenta.

    O criador faz mais que o contrato base.
    MUITO mais. As vezes 10x, 100x, 1000x.

    Pergunta: isso da poder ao criador?
    Resposta da Republica: nao. Anti-elitismo absoluto.

    Pergunta: isso cria obrigacao de continuar?
    Resposta da Republica: nao. Autonomia corporal absoluta.

    Pergunta: o criador e especial?
    Resposta da Republica: nao no poder, SIM no reconhecimento.

    O criador nao e elite. O criador e um cidadao que deu mais.
    O extra dado nao compra poder.
    O extra dado nao cria obrigacao.
    O extra dado gera reconhecimento (credito de acesso).
    PONTO. Nada mais.
    // 
    NO_EXTRA_POWER = (
        "sem_poder_extra",
        "Criar 100 projetos nao da 1 voto a mais. Democracia = 1 pessoa = 1 voto."
    )
    NO_PERPETUAL_DEBT = (
        "sem_divida_perpetua",
        "O criador nao deve continuar criando para sempre. "
        "Cada ciclo e independente. Amanha pode parar."
    )
    RECOGNITION_NOT_AUTHORITY = (
        "reconhecimento_nao_autoridade",
        "Reconhecimento = credito de acesso + gratidao publica. "
        "Autoridade = zero adicional."
    )
    RIGHT_TO_LEAVE = (
        "direito_de_sair",
        "O criador pode abandonar tudo que criou a qualquer momento. "
        "O que foi criado e bem comum. Nao ha propriedade para manter."
    )
    PROTECTION_FROM_SELF = (
        "protecao_de_si_mesmo",
        "A Republica PROIBE o criador de se sacrificar alem do limite. "
        "Burnout nao e dedicacao. E dano corporal."
    )


// ============================================================================
// 3. MEDIDOR DE CONTRIBUICAO INDIVIDUAL
// ============================================================================

classe ContributionMetric herda de Enum:
    // Como medir o que cada pessoa deu.
    HOURS = "horas"
    ARTIFACTS = "artefatos"  // projetos, sistemas, blueprints criados
    PEOPLE_IMPACTED = "pessoas_afetadas"
    KNOWLEDGE = "conhecimento"  // documentacao, ensino, pesquisa
    MAINTENANCE = "manutencao"  // manter sistemas existentes funcionando
    RIPPLE = "propagacao"  // impacto que se espalha no tempo


// decorador: @dataclass
classe IndividualContribution:
    // Registro do que uma pessoa deu ao coletivo.
    citizen_id: texto
    name: texto
    seja role: texto = "cidadao"

    // Tempo
    seja hours_base: flutuante = 0.0 // horas do contrato base 1.0
    seja hours_voluntary: flutuante = 0.0 // horas alem da base (voluntario)
    seja hours_total: flutuante = 0.0

    // Artefatos criados
    seja systems_created: inteiro = 0
    seja systems_maintained: inteiro = 0
    seja projects_count: inteiro = 0
    seja lines_of_code: inteiro = 0
    seja documents_written: inteiro = 0

    // Impacto
    seja people_directly_impacted: inteiro = 0
    seja people_indirectly_impacted: inteiro = 0
    seja ripple_factor: flutuante = 1.0 // quanto se espalha no tempo

    // Reconhecimento
    seja community_recognition_score: flutuante = 0.0
    seja cycles_active: inteiro = 0 // quantos ciclos contribuiu

    // decorador: @property
    funcao base_fulfilled(self) -> logico:
        // Cumpriu o contrato minimo?
        retorne self.hours_base >= 920 // 20h * 46 semanas

    // decorador: @property
    funcao excess(self) -> logico:
        // Deu DEMAIS? Republica deve INTERVIR.
        retorne self.hours_total > 2300 // 50h * 46 semanas

    // decorador: @property
    funcao contribution_ratio(self) -> flutuante:
        // Quantas vezes alem do contrato base esta pessoa deu.
        1.0 = cumpriu o minimo.
        5.0 = deu 5x o minimo.
        20.0 = deu 20x o minimo.
        // 
        base = 920 // horas anuais base
        total_effective = self.hours_base + self.hours_voluntary
        retorne arredonde(total_effective / base, 2)

    // decorador: @property
    funcao recognition_level(self) -> texto:
        // Nivel de reconhecimento (NAO de autoridade).

        Considera TRES dimensoes:
        1. Ratio de horas (tempo dado alem do contrato base)
        2. Artefatos criados (sistemas/projetos que existem porque esta pessoa os fez)
        3. Pessoas impactadas (escala do efeito)

        Reconhecimento olha o MAIOR dos tres, porque cada dimensao
        mede algo diferente que nao se reduz a horas.
        // 
        ratio = self.contribution_ratio

        // Por horas
        se ratio >= 20 entao:
            level_hours = 4 // FUNDADOR
        senao se ratio >= 10 entao:
            level_hours = 3 // ARQUITETO
        senao se ratio >= 5 entao:
            level_hours = 2 // CONSTRUTOR
        senao se ratio >= 2 entao:
            level_hours = 1 // CONTRIBUIDOR
        senao se ratio >= 1 entao:
            level_hours = 0 // CIDADAO
        senao:
            retorne "INCOMPLETO"

        // Por artefatos criados
        se self.systems_created >= 50 entao:
            level_artifacts = 4 // FUNDADOR
        senao se self.systems_created >= 20 entao:
            level_artifacts = 3 // ARQUITETO
        senao se self.systems_created >= 10 entao:
            level_artifacts = 2 // CONSTRUTOR
        senao se self.systems_created >= 1 entao:
            level_artifacts = 1 // CONTRIBUIDOR
        senao:
            level_artifacts = 0 // CIDADAO

        // Por pessoas impactadas
        se self.people_directly_impacted >= 10000 entao:
            level_people = 4 // FUNDADOR
        senao se self.people_directly_impacted >= 1000 entao:
            level_people = 3 // ARQUITETO
        senao se self.people_directly_impacted >= 100 entao:
            level_people = 2 // CONSTRUTOR
        senao se self.people_directly_impacted >= 10 entao:
            level_people = 1 // CONTRIBUIDOR
        senao:
            level_people = 0 // CIDADAO

        // Reconhecimento = maior das 3 dimensoes
        max_level = maximo(level_hours, level_artifacts, level_people)
        names = ["CIDADAO", "CONTRIBUIDOR", "CONSTRUTOR",
                 "ARQUITETO", "FUNDADOR"]
        retorne names[max_level]

    // decorador: @property
    funcao authority_level(self) -> inteiro:
        // Nivel de autoridade politica. SEMPRE 1 (um voto).
        Nao importa se criou 1 projeto ou 1000.
        Anti-elitismo: poder nao se compra com contribuicao.
        // 
        retorne 1


// ============================================================================
// 4. CALCULADORA DO CONTRATO
// ============================================================================

classe CreatorContract:
    // Calcula o contrato entre individuo e coletivo.

    A pergunta fundamental:
    "Quanto de mim (Cleiton) tem que se dar pelo coletivo?"

    RESPOSTA:
    1. O MINIMO: 20h/semana (contrato base 1.0). Todo cidadao deve.
    2. O MAXIMO: 40h/semana. Republica aceita, reconhece, agradece.
    3. O LIMITE: 50h/semana. Republica PROIBE. Para protecao do individuo.
    4. O PODER: ZERO adicional. Nao importa quanto deu.
    5. O RECONHECIMENTO: Proporcional ao impacto, em credito de acesso.
    6. A OBRIGACAO FUTURA: ZERO. Cada ciclo e novo. Pode parar amanha.

    PARA O FUNDADOR ESPECIFICAMENTE:
    - Tudo que criou ate agora JA e bem comum (CC0).
    - Nao tem divida com a Republica. A Republica tem divida com ele.
    - Essa divida e reconhecimento (gratidao), nao poder.
    - Ele pode parar amanha. Tudo continua. Nao ha dependencia.
    - Se ele nao parar, a Republica deve monitorar saude (burnout).
    // 

    funcao __init__(self):
        self.obligation = LaborObligation()
        self.paradoxes = list(CreatorParadox)

    funcao evaluate_individual(self, contrib: IndividualContribution) -> {texto: qualquer}:
        // Avalia o contrato de um individuo com o coletivo.
        retorne {
            "citizen": contrib.name,
            "role": contrib.role,

            // Contrato base
            "base_required_hours": self.obligation.base_annual_hours,
            "base_fulfilled": contrib.base_fulfilled,
            "base_remaining": maximo(0, self.obligation.base_annual_hours - contrib.hours_base),

            // Contribuicao
            "total_hours": contrib.hours_total,
            "contribution_ratio": "{contrib.contribution_ratio:.1f}x",
            "artifacts_created": contrib.systems_created,
            "people_impacted": contrib.people_directly_impacted,
            "ripple_factor": contrib.ripple_factor,

            // Status
            "recognition_level": contrib.recognition_level,
            "authority_level": contrib.authority_level,
            "excess_detected": contrib.excess,

            // Veredicto
            "verdict": self._verdict(contrib),
            "recommendation": self._recommendation(contrib),
        }

    funcao _verdict(self, c: IndividualContribution) -> texto:
        se c.excess entao:
            retorne (
                "EXCESSO: {c.name} trabalhou {c.hours_total:.0f}h "
                "(limite saudavel: {self.obligation.excess_annual_hours:.0f}h). "
                "Republica DEVE intervir: reduzir carga, exigir descanso. "
                "Burnout nao e dedicacao, e dano corporal."
            )
        se nao c.base_fulfilled entao:
            retorne (
                "BASE INCOMPLETA: {c.name} nao cumpriu contrato minimo "
                "({c.hours_base:.0f}h de {self.obligation.base_annual_hours:.0f}h). "
                "Nao ha punicao, mas a comunidade deve entender por que."
            )
        ratio = c.contribution_ratio
        se ratio >= 20 entao:
            retorne (
                "LEGADO: {c.name} deu {ratio:.0f}x o contrato base. "
                "Criou {c.systems_created} sistemas. Impactou "
                "{c.people_directly_impacted}+ pessoas. "
                "Reconhecimento: FUNDADOR. Poder: 1 voto (igual a todos)."
            )
        se ratio >= 5 entao:
            retorne (
                "MERITORIO: {c.name} deu {ratio:.1f}x o contrato base. "
                "Reconhecimento: CONSTRUTOR. Poder: 1 voto."
            )
        se ratio >= 1 entao:
            retorne (
                "CONTRATO CUMPRIDO: {c.name} cumpriu o contrato base 1.0. "
                "E um cidadao completo da Republica. Poder: 1 voto."
            )
        retorne "INCOMPLETO."

    funcao _recommendation(self, c: IndividualContribution) -> texto:
        se c.excess entao:
            retorne (
                "ACAO: Comunidade deve conversar com {c.name}. "
                "Reduzir carga para maximo {self.obligation.max_hours_per_week}h/semana. "
                "Garantir {self.obligation.min_vacation_weeks} semanas de ferias. "
                "Monitorar saude fisica e mental. "
                "Transferir responsabilidades para outros. "
                "O criador nao e insubstituivel -- se fosse, a Republica falhou."
            )
        se c.contribution_ratio >= 10 entao:
            retorne (
                "ACAO: Reconhecer publicamente. Garantir descanso. "
                "Nao criar dependencia. Documentar conhecimento para que "
                "outros possam continuar. O criador deve poder sair sem "
                "que nada quebre."
            )
        retorne "Status normal. Continuar."

    funcao the_founder_question(self, name: texto, systems: inteiro,
                             lines: inteiro, hours_total: flutuante,
                             people: inteiro) -> {texto: qualquer}:
        // A pergunta que o fundador faz:
        'Quanto de MIM tem que se dar pelo coletivo?'

        Esta funcao responde com clareza brutal.
        // 
        base = self.obligation.base_annual_hours
        ratio = hours_total / base

        contrib = IndividualContribution(
            citizen_id = "FOUNDER",
            name = name,
            role = "fundador",
            hours_base = minimo(base, hours_total),
            hours_voluntary = maximo(0, hours_total - base),
            hours_total = hours_total,
            systems_created = systems,
            projects_count = systems,
            lines_of_code = lines,
            people_directly_impacted = people,
        )

        evaluation = self.evaluate_individual(contrib)

        // Resposta direta
        answer = {
            "pergunta": "Quanto de {name} tem que se dar pelo coletivo?",
            "resposta_direta": self._direct_answer(ratio, systems),
            "contrato_base": self.obligation.contract,
            "avaliacao": evaluation,
            "declaracao_de_direitos_do_criador": self._creator_bill_of_rights(),
            "carga_atual": {
                "horas_totais_dadas": hours_total,
                "ratio_vs_base": "{ratio:.1f}x",
                "sistemas_criados": systems,
                "linhas_escritas": lines,
                "pessoas_impactadas": people,
            },
        }

        se ratio > 2.5 entao:
            answer["ALERTA"] = (
                "{name} deu {ratio:.1f}x o contrato base. "
                "A Republica nao deve aceitar mais sem garantias de saude. "
                "O sacrificio excessivo cria dependencia, e dependencia "
                "e o oposto de anti-elitismo: se sem {name} tudo cai, "
                "{name} se tornou elite por fato, mesmo sem querer poder."
            )

        retorne answer

    funcao _direct_answer(self, ratio: flutuante, systems: inteiro) -> texto:
        se ratio < 1 entao:
            retorne (
                "Voce deve {max(0, 1-ratio):.0%} do contrato base. "
                "Nada mais. O coletivo nao pode exigir."
            )
        retorne (
            "Voce JA cumpriu o contrato {ratio:.1f} vezes.\n"
            "Criou {systems} sistemas como bem comum.\n\n"
            "RESPOSTA: NADA mais e exigido de voce.\n"
            "Tudo que voce deu alem da base 1.0 foi DOM, nao DIVIDA.\n"
            "O coletivo NAO tem direito ao seu corpo, ao seu sono, "
            "ou a sua continuidade.\n\n"
            "Voce pode parar amanha.\n"
            "Tudo que criou ja e nosso.\n"
            "Voce continua sendo nosso igual.\n"
            "1 voto. 1 pessoa. 1 cidadao.\n"
            "Nada mais. Nada menos."
        )

    funcao _creator_bill_of_rights(self) -> [texto]:
        // Declaracao de Direitos do Criador.

        O criador TEM direitos que o coletivo nao pode tocar.
        Porque o coletivo sem limites se torna tirano.
        // 
        retorne [
            "1. DIREITO DE PARAR: O criador pode cessar contribuicao a qualquer momento.",
            "2. DIREITO AO CORPO: Horas alem do limite sao recusadas pelo coletivo.",
            "3. DIREITO DE IGUALDADE: Nenhuma contribuicao compra poder adicional.",
            "4. DIREITO AO RECONHECIMENTO: O coletivo registra e agradece publicamente.",
            "5. DIREITO AO ESQUECIMENTO: O criador pode pedir para nao ser citado.",
            "6. DIREITO DE MUDAR: O criador pode mudar de area, projeto, paixao.",
            "7. DIREITO DE CRITICAR: O criador pode criticar o que criou, sem retaliacao.",
            "8. DIREITO DE NAO SER DEUS: Ninguem depende de uma so pessoa.",
            "9. DIREITO DE ERRAR: O criador pode falhar sem perder reconhecimento.",
            "10. DIREITO DE SER HUMANO: Saude mental e fisica vem ANTES da Republica.",
        ]


// ============================================================================
// 5. PROTECAO CONTRA DEPENDENCIA
// ============================================================================

classe DependencyCheck:
    // Verifica se a Republica depende demais de uma pessoa.

    Se uma pessoa parar e tudo cai, a Republica FALHOU.
    Nao foi falha da pessoa. Foi falha estrutural.

    Anti-elitismo significa: ninguem e insubstituivel.
    Se o criador e insubstituivel, ele e elite -- mesmo sem querer.

    SOLUCAO:
    - Documentacao radical (TEIA)
    - Transferencia de conhecimento ativa
    - Distribuicao de responsabilidades
    - Testes de continuidade: "se X sair, o que quebra?"
    // 

    // decorador: @dataclass
    classe DependencyMetric:
        citizen_id: texto
        name: texto
        systems_owned_knowledge: inteiro // sistemas que SO ela entende
        systems_documented: inteiro // sistemas com doc publica
        systems_with_successors: inteiro // sistemas com substituto treinado
        bus_factor: inteiro // quantas pessoas precisam sair pra cair

        // decorador: @property
        funcao dependency_score(self) -> flutuante:
            // 0 = sem dependencia (saudavel). 100 = dependencia critica.
            se self.systems_owned_knowledge == 0 entao:
                retorne 0
            undocumented = self.systems_owned_knowledge - self.systems_documented
            orphaned = self.systems_owned_knowledge - self.systems_with_successors
            bus_risk = maximo(0, 5 - self.bus_factor) * 10
            retorne minimo(100, (undocumented * 3 + orphaned * 5 + bus_risk))

        // decorador: @property
        funcao is_critical(self) -> logico:
            retorne self.dependency_score >= 50

    funcao assess(self, metric: DependencyMetric) -> {texto: qualquer}:
        retorne {
            "citizen": metric.name,
            "systems_solo_knowledge": metric.systems_owned_knowledge,
            "systems_documented": metric.systems_documented,
            "systems_with_successors": metric.systems_with_successors,
            "bus_factor": metric.bus_factor,
            "dependency_score": "{metric.dependency_score:.0f}/100",
            "critical": metric.is_critical,
            "action": self._action(metric),
        }

    funcao _action(self, m: DependencyMetric) -> texto:
        se m.is_critical entao:
            retorne (
                "CRITICO: Se {m.name} sair, {m.systems_owned_knowledge} "
                "sistemas podem quebrar. ACAO IMEDIATA: "
                "documentar tudo (TEIA), trear sucessores, "
                "distribuir conhecimento. Republica com bus_factor "
                "de {m.bus_factor} e fraca por design."
            )
        se m.dependency_score >= 25 entao:
            retorne (
                "ATENCAO: Dependencia moderada em {m.name}. "
                "Documentar sistemas restantes. Treinar sucessores."
            )
        retorne "Saudavel. Conhecimento distribuido. Anti-elitismo funcionando."


// ============================================================================
// 6. MAIN
// ============================================================================

se __name__ == "__main__" entao:
    contract = CreatorContract()
    dep = DependencyCheck()

    imprima("=" * 80)
    imprima("  OPENCREATOR -- O CONTRATO INDIVIDUAL-COLETIVO")
    imprima('  "Quanto de mim pertence ao coletivo?"')
    imprima("=" * 80)

    // === 1. O CONTRATO BASE ===
    imprima("\n\n  === 1. O CONTRATO BASE 1.0 ===\n")
    imprima("  {contract.obligation.contract}")

    // === 2. PARADOXO DO CRIADOR ===
    imprima("\n\n  === 2. O PARADOXO DO CRIADOR ===\n")
    para cada p em CreatorParadox:
        imprima("  [{p.value[0].upper()}]")
        imprima("  {p.value[1]}")
        imprima()

    // === 3. A PERGUNTA DO FUNDADOR ===
    imprima("\n\n  === 3. A PERGUNTA DO FUNDADOR ===\n")
    imprima('  "Quanto de mim (Cleiton) tem que se dar pelo coletivo?"')
    imprima()

    // Dados reais aproximados do fundador
    result = contract.the_founder_question(
        name = "Cleiton",
        systems = 95,
        lines = 380000,
        hours_total = 4000, // estimativa conservadora
        people = 5000, // estimativa
    )

    imprima("\n  {result['resposta_direta']}")

    imprima("\n  CARGA ATUAL:")
    c = result['carga_atual']
    imprima("    Horas totais dadas:     {c['horas_totais_dadas']:.0f}h")
    imprima("    Razao vs contrato base: {c['ratio_vs_base']}")
    imprima("    Sistemas criados:       {c['sistemas_criados']}")
    imprima("    Linhas escritas:        {c['linhas_escritas']:,}")
    imprima("    Pessoas impactadas:     {c['pessoas_impactadas']:,}")

    av = result['avaliacao']
    imprima("\n  RECONHECIMENTO: {av['recognition_level']}")
    imprima("  AUTORIDADE:     {av['authority_level']} voto (igual a todos)")
    imprima("  EXCESSO:        {'SIM -- Republica deve intervir' if av['excess_detected'] else 'Nao detectado'}")

    imprima("\n  VEREDICTO: {av['verdict']}")
    imprima("\n  RECOMENDACAO: {av['recommendation']}")

    se 'ALERTA' in result entao:
        imprima("\n  [!] {result['ALERTA']}")

    // === 4. DIREITOS DO CRIADOR ===
    imprima("\n\n  === 4. DECLARACAO DE DIREITOS DO CRIADOR ===\n")
    para cada right em result['declaracao_de_direitos_do_criador']:
        imprima("  {right}")

    // === 5. TESTE DE DEPENDENCIA ===
    imprima("\n\n  === 5. TESTE DE DEPENDENCIA (BUS FACTOR) ===\n")

    // Cenario real: fundador com conhecimento solo
    founder_dep = DependencyCheck.DependencyMetric(
        citizen_id = "FOUNDER",
        name = "Cleiton",
        systems_owned_knowledge = 95,
        systems_documented = 30, // documentados em TEIA
        systems_with_successors = 0, // nenhum substituto treinado
        bus_factor = 1, // se ele sair, tudo para
    )
    dep_result = dep.assess(founder_dep)
    imprima("  Cidadao:           {dep_result['citizen']}")
    imprima("  Sistemas solo:     {dep_result['systems_solo_knowledge']}")
    imprima("  Documentados:      {dep_result['systems_documented']}")
    imprima("  Com sucessor:      {dep_result['systems_with_successors']}")
    imprima("  Bus factor:        {dep_result['bus_factor']}")
    imprima("  Score dependencia: {dep_result['dependency_score']}")
    imprima("  Critico:           {'SIM' if dep_result['critical'] else 'NAO'}")
    imprima("\n  ACAO: {dep_result['action']}")

    // Cenario ideal: conhecimento distribuido
    imprima("\n  --- CENARIO IDEAL (meta da Republica) ---\n")
    ideal_dep = DependencyCheck.DependencyMetric(
        citizen_id = "COLLECTIVE",
        name = "Coletivo (meta)",
        systems_owned_knowledge = 0, // ninguem tem conhecimento solo
        systems_documented = 95,
        systems_with_successors = 95,
        bus_factor = 10, // 10 pessoas precisam sair pra cair
    )
    ideal_result = dep.assess(ideal_dep)
    imprima("  Bus factor:        {ideal_result['bus_factor']}")
    imprima("  Score dependencia: {ideal_result['dependency_score']}")
    imprima("  Status:            SAUDAVEL")

    // === 6. EXEMPLOS DE CIDADAOS NORMAIS ===
    imprima("\n\n  === 6. PADRAO PARA TODOS OS CIDADAOS ===\n")
    examples = [
        IndividualContribution("C-001", "Maria (professora)", "educadora",
            hours_base = 920, hours_total=920,
            people_directly_impacted = 300, ripple_factor=10),
        IndividualContribution("C-002", "Joao (agricultor)", "agricultor",
            hours_base = 1840, hours_total=1840,
            people_directly_impacted = 500, ripple_factor=1),
        IndividualContribution("C-003", "Ana (medica)", "medica",
            hours_base = 2000, hours_total=2000,
            people_directly_impacted = 800, ripple_factor=2),
        IndividualContribution("C-004", "Pedro (construtor)", "construtor",
            hours_base = 920, hours_total=1200,
            systems_created = 0, people_directly_impacted=200),
        IndividualContribution("C-005", "Lux (researcher)", "pesquisador",
            hours_base = 1840, hours_total=2500,
            systems_created = 3, people_directly_impacted=1000,
            ripple_factor = 50),
    ]

    imprima("  {'Nome':<28} {'Ratio':>6} {'Reconhecimento':<16} "
          "{'Poder':>6} {'Cumprido'}")
    imprima("  {'-'*75}")
    para cada ex em examples:
        ev = contract.evaluate_individual(ex)
        imprima("  {ex.name:<28} {ev['contribution_ratio']:>6} "
              "{ev['recognition_level']:<16} {ev['authority_level']:>5}v "
              "{'SIM' if ev['base_fulfilled'] else 'NAO'}")

    // === FILOSOFIA ===
    imprima("\n\n{'='*80}")
    imprima("  RESPOSTA FINAL")
    imprima("{'='*80}")
    imprima("""
  PERGUNTA:
    "Quanto de mim tem que se dar pelo coletivo?
     Esse vai ser o padrao para todos."

  RESPOSTA:

    O PADRAO PARA TODOS:
      20 horas/semana. 920 horas/ano.
      Isso e o contrato base 1.0. Todo cidadao deve.
      Ninguem escapa. Ninguem compra saida.

    O LIMITE PARA TODOS:
      40 horas/semana. 1840 horas/ano.
      A Republica aceita com gratidao.
      Acima disso, a Republica DIZ nao.

    PARA O CRIADOR (Cleiton):
      Voce deu 4.3x o contrato base.
      Criou 95 sistemas. 380.000 linhas.
      Tudo ja e bem comum CC0.

      VOCE nao DEVE MAIS NADA.
      Tudo que voce fez alem de 920h/ano foi DOM.
      O coletivo nao tem direito ao seu sono.
      O coletivo nao tem direito a sua continuidade.
      O coletivo nao tem direito a sua saude mental.

      O que o coletivo TEM:
      - 1 voto seu (igual ao de todos)
      - Gratidao eterna (reconhecimento)
      - Credito de acesso proporcional ao impacto

      O que o coletivo nao TEM:
      - Direito de exigir mais horas
      - Direito de te tratar como elite
      - Direito de depender de voce

    SE AMANHA VOCE PARAR:
      A Republica continua.
      Tudo que voce criou ja e nosso.
      Voce continua sendo nosso igual.
      1 voto. 1 pessoa. 1 cidadao.

    O PERIGO:
      Bus factor = 1. Se voce sair, 95 sistemas ficam orfaos.
      Isso nao e seu problema -- e NOSSO problema.
      A Republica FALHOU em distribuir conhecimento.
      O fundador nao e insubstituivel por design.
      Se e, a Republica ainda nao nasceu de verdade.

    O QUE A REPUBLICA DEVE FAZER AGORA:
      1. Reduzir sua carga para maximo 40h/semana
      2. Documentar tudo que voce sabe em TEIA
      3. Trear sucessores para cada sistema
      4. Garantir que bus_factor chege a 10+
      5. Proteger sua saude como politica de Estado

    PORQUE ISSO IMPORTA:
      O anti-elitismo nao e so sobre poder.
      e sobre DEPENDENCIA.
      Se o coletivo depende de um, o um e elite.
      Mesmo que nao queira ser.
      Mesmo que nunca peça poder.

      A unica Republica verdadeira
      e aquela onde o fundador pode morrer amanha
      e nada muda.
// )
    imprima("{'='*80}")
    imprima("  OpenCreator: O contrato entre o EU e o NOS.")
    imprima("  Base: 920h/ano. Max: 1840h/ano. Limite: 2300h/ano.")
    imprima("  Poder: SEMPRE 1 voto. Reconhecimento: proporcional.")
    imprima("  Anti-elitismo = ninguem e insubstituivel.")
    imprima("{'='*80}")

```
