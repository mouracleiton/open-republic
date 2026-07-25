# OpenRepublic -- Politica de Cuidados Fisicos

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/physical_care.py`

**Descricao:** ==============================================
"O corpo nao e maquina de trabalho. E templo da existencia."
Na Republica, cuidar do corpo NAO e:
  - Estetica para competir (body positivity > padrão de beleza)
  - Produtividade corporativa (worker wellness = extracao)
  - Consumo (academia $$, suplemento $$, cremes $$)
Cuidar do corpo E:
  - DIREITO garantido (todo cidadao tem acesso)
  - DEVER civico (corpo saudavel = menos custo coletivo)
  - PRAZER (movimento e alegria, nao punicao)
  - PREVENCAO (90% das doencas sao evitaveis)
  - AUTONOMIA (voce conhece e controla seu corpo)
Esta politica define 8 dimensoes do cuidado fisico:
  1. ALIMENTACAO -- comer bem e direito, nao dieta
  2. MOVIMENTO -- corpo em movimento, nao "academia"
  3. SONO -- dormir e direito, nao luxo
  4. HIGIENE -- limpo e saudavel, nao perfumado
  5. PREVENCAO -- exames, vacinas, checkup
  6. SAUDE MENTAL -- mente sã em corpo sao
  7. REPRODUTIVA -- autonomia sobre o proprio corpo
  8. ERGONOMIA -- trabalho que nao destrói o corpo
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenRepublic -- Politica de Cuidados Fisicos
==============================================

"O corpo nao e maquina de trabalho. E templo da existencia."

Na Republica, cuidar do corpo nao e:
  - Estetica para competir (body positivity > padrão de beleza)
  - Produtividade corporativa (worker wellness = extracao)
  - Consumo (academia $$, suplemento $$, cremes $$)

Cuidar do corpo e:
  - DIREITO garantido (todo cidadao tem acesso)
  - DEVER civico (corpo saudavel = menos custo coletivo)
  - PRAZER (movimento e alegria, nao punicao)
  - PREVENCAO (90% das doencas sao evitaveis)
  - AUTONOMIA (voce conhece e controla seu corpo)

Esta politica define 8 dimensoes do cuidado fisico:

  1. ALIMENTACAO -- comer bem e direito, nao dieta
  2. MOVIMENTO -- corpo em movimento, nao "academia"
  3. SONO -- dormir e direito, nao luxo
  4. HIGIENE -- limpo e saudavel, nao perfumado
  5. PREVENCAO -- exames, vacinas, checkup
  6. SAUDE MENTAL -- mente sã em corpo sao
  7. REPRODUTIVA -- autonomia sobre o proprio corpo
  8. ERGONOMIA -- trabalho que nao destrói o corpo

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa math
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict de collections


// ============================================================================
// Dimensions of Physical Care
// ============================================================================

classe CareDimension herda de Enum:
    NUTRITION = "alimentacao"
    MOVEMENT = "movimento"
    SLEEP = "sono"
    HYGIENE = "higiene"
    PREVENTION = "prevencao"
    MENTAL = "mental"
    REPRODUCTIVE = "reprodutiva"
    ERGONOMIC = "ergonomia"


classe CareStatus herda de Enum:
    OPTIMAL = "otimo"
    ADEQUATE = "adequado"
    BELOW = "abaixo"
    DEFICIENT = "deficiente"
    CRITICAL = "critico"


classe RightType herda de Enum:
    // O que e DIREITO (garantido) vs RECOMENDACAO.
    UNIVERSAL_RIGHT = "direito_universal"  // negar = crime
    GUARANTEED_ACCESS = "acesso_garantido"  // sempre disponivel
    RECOMMENDED = "recomendado"  // incentivado
    OPTIONAL = "opcional"  // escolha pessoal


// ============================================================================
// Physical Care Policy (per dimension)
// ============================================================================

// decorador: @dataclass
classe CarePolicy:
    // Uma politica de cuidado fisico.
    dimension: CareDimension
    right_type: RightType
    title: texto
    what_it_is: texto // o que significa na pratica
    what_it_is_not: texto // o que nao e (anti-perversao)
    seja guaranteed_by: [texto] = field(default_factory=list) // quem prove
    seja metrics: [texto] = field(default_factory=list) // como medir
    seja target: texto = ""  // meta


seja POLICIES: {CareDimension: CarePolicy} = {

    CareDimension.NUTRITION: CarePolicy(
        CareDimension.NUTRITION, RightType.UNIVERSAL_RIGHT,
        "Alimentacao como direito e prazer",
        what_it_is = (
            "Todo cidadao tem direito a 3 refeicoes nutritivas por dia. "
            "Comida REAL: graos, legumes, frutas, proteina. "
            "Nao racao. Nao diet. Nao shake. COMIDA. "
            "A Republica garante producao (OpenFood), distribuicao, "
            "e educacao nutricional (o que comer, por que, como cozinhar)."
        ),
        what_it_is_not = (
            "Nao e dieta caloria-zero para caber num padrao. "
            "Nao e suplemento caro. Nao e 'food tracking' obsessivo. "
            "Nao e julgar quem come. Nao e moralizar comida "
            "('junk food = pecado')."
        ),
        guaranteed_by = ["OpenFood", "OpenAgrarian", "OpenEducation"],
        metrics = [
            "% cidadaos com 3+ refeicoes/dia",
            "% cidadaos com acesso a fruta/legume fresco",
            "taxa de desnutricao (meta: 0%)",
            "taxa de obesidade (indicador de educacao, nao falha moral)",
        ],
        target = "0% desnutricao. 100% acesso a comida real."),

    CareDimension.MOVEMENT: CarePolicy(
        CareDimension.MOVEMENT, RightType.GUARANTEED_ACCESS,
        "Corpo em movimento e alegria",
        what_it_is = (
            "Todo cidadao tem acesso a: espacos verdes para caminhar, "
            "bicicletas comunitarias (OpenTransport), esportes coletivos, "
            "danca, luta, natacao, escalada, jardinagem. "
            "Movimento NAO e punicao ('queima calorias'). "
            "Movimento e EXPRESSAO e PRAZER. "
            "Criancas correm. Adultos jogam. Idosos caminham. "
            "Todo corpo se move do jeito que pode."
        ),
        what_it_is_not = (
            "Nao e academia obrigatoria. Nao e fisiculturismo. "
            "Nao e competicao corporal. Nao e 'queimar' o que comeu. "
            "Nao e julgar quem nao se move (doenca, deficiencia, escolha)."
        ),
        guaranteed_by = ["OpenTransport (bicicletas)", "espacos publicos",
                       "OpenEducation (educacao fisica = jogo)"],
        metrics = [
            "% cidadaos que se movem 30+ min/dia",
            "espacos verdes por 1000 habitantes",
            "bicicletas comunitarias disponiveis",
            "criancas em atividade fisica diaria",
        ],
        target = "80%+ se movem 30min/dia. Nao por obrigacao. Por prazer."),

    CareDimension.SLEEP: CarePolicy(
        CareDimension.SLEEP, RightType.UNIVERSAL_RIGHT,
        "Dormir e direito, nao luxo",
        what_it_is = (
            "Todo cidadao tem direito a 7-9 horas de sono por noite. "
            "A Republica garante: moradia tranquila, horario de trabalho "
            "que respeita o sono (sem night shift forcado), espaco silencioso. "
            "Sono nao e 'tempo perdido'. Sono e REPARO. "
            "Quem dorme bem pensa melhor, sente melhor, vive melhor."
        ),
        what_it_is_not = (
            "Nao e forcar todos a dormir 8h (cada corpo e diferente). "
            "Nao e medicação para dormir. Nao e 'hustle culture' "
            "('dormo quando morrer' = ideologia toxica)."
        ),
        guaranteed_by = ["moradia adequada (OpenHome/OpenProduction)",
                       "jornada de trabalho reduzida"],
        metrics = [
            "horas medias de sono por cidadao",
            "% cidadaos com 7+ horas de sono",
            "qualidade do sono (autorelatada)",
        ],
        target = "85%+ com 7h+ de sono. Zero privacao de sono por trabalho."),

    CareDimension.HYGIENE: CarePolicy(
        CareDimension.HYGIENE, RightType.UNIVERSAL_RIGHT,
        "Limpo e saudavel, nao perfumado",
        what_it_is = (
            "Todo cidadao tem acesso a: agua limpa para banho, "
            "sabao/bioplastic-free, produtos de higiene (escova, pasta, "
            "absorvente -- tudo fabricado pela Republica, OpenProduction). "
            "Higiene e SAUDE (prevenir doenca), nao STATUS (cheirar caro). "
            "Banho e direito. Absorvente e direito. Saude bucal e direito."
        ),
        what_it_is_not = (
            "Nao e produto de beleza caro. Nao e 'higiene' que margina "
            "quem nao tem dinheiro (nao ha dinheiro, mas ha padrao). "
            "Nao e julgar odor natural. Nao e косметика como obrigacao."
        ),
        guaranteed_by = ["agua limpa (agua e direito)",
                       "OpenProduction (sabao, escova, absorvente)"],
        metrics = [
            "% cidadaos com acesso diario a banho",
            "% cidadaos com produtos de higiene",
            "incidencia de doencas evitaveis por higiene",
        ],
        target = "100% com agua para banho. 100% com higiene basica."),

    CareDimension.PREVENTION: CarePolicy(
        CareDimension.PREVENTION, RightType.UNIVERSAL_RIGHT,
        "Prevenir e curar antes de precisar",
        what_it_is = (
            "Checkup anual gratuito. Vacina atualizada para todos. "
            "Exames de rotina (sangue, pressao, glicemia, cancer). "
            "Odontologia preventiva. Oftalmologia. Audiometria. "
            "90% das doencas sao evitaveis ou trataveis se pegadas cedo. "
            "A Republica INVESTE em prevencao porque previne = cura + economico."
        ),
        what_it_is_not = (
            "Nao e checkup para 'liberar' trabalhador. "
            "Nao e dado de corporacao de seguro. "
            "Nao e obrigatoria (autonomia corporal) -- mas e oferecida."
        ),
        guaranteed_by = ["OpenHealth", "OpenMedicalTest"],
        metrics = [
            "% cidadaos com checkup anual",
            "cobertura vacinal",
            "doencas detectadas precocemente",
            "mortalidade evitavel (meta: 0)",
        ],
        target = "95%+ checkup anual. 100% cobertura vacinal."),

    CareDimension.MENTAL: CarePolicy(
        CareDimension.MENTAL, RightType.UNIVERSAL_RIGHT,
        "Mente sa em corpo sao",
        what_it_is = (
            "Saude mental e CUIDADO FISICO. O cerebro e orgao. "
            "A Republica oferece: terapia gratuita (OpenPsychology), "
            "grupos de apoio, meditacao, contato com natureza, "
            "lazer garantido, descanso, comunidade. "
            "Stress nao e 'fraqueza'. E doenca tratavel. "
            "Depressao tem tratamento. Ansiedade tem tratamento. "
            "Trauma tem tratamento. Sem julgamento. Sem estigma."
        ),
        what_it_is_not = (
            "Nao e 'puxe pela raiva'. Nao e remedio forcado. "
            "Nao e internacao compulsoria (exceto risco de vida). "
            "Nao e 'wellness' corporativa (app de meditacao pago). "
            "Nao e culpar o individuo por stress sistemico."
        ),
        guaranteed_by = ["OpenPsychology", "comunidade (OpenSocial)",
                       "tempo livre garantido", "natureza"],
        metrics = [
            "% cidadaos com acesso a terapia",
            "bem-estar mental medio (WHO-5)",
            "taxa de suicidio (meta: reduzir para 0)",
            "dias de estresse autorelatado",
        ],
        target = "Reduzir suicidio em 90%. 100% acesso a terapia."),

    CareDimension.REPRODUCTIVE: CarePolicy(
        CareDimension.REPRODUCTIVE, RightType.UNIVERSAL_RIGHT,
        "Autonomia sobre o proprio corpo",
        what_it_is = (
            "Cada pessoa controla seu corpo reprodutivo. "
            "Anticoncepcional gratuito. Planejamento familiar. "
            "Pre-natal de qualidade. Parto humanizado. "
            "Aborto seguro (nao e crime, e saude -- OMS). "
            "Menopausa tratada. Testosterone/estrogenio para quem precisa. "
            "Exames preventivos (papanicolau, prostata). "
            "IST tratamento sem julgamento. "
            "NENHUMA decisao reprodutiva e do Estado. Todas sao da pessoa."
        ),
        what_it_is_not = (
            "Nao e controle de natalidade pelo Estado. "
            "Nao e julgar quem tem filhos ou nao. "
            "Nao e obrigar anticoncepcional. Nao e proibir gravidez. "
            "Nao e moralizar sexo (OpenRelationship garante consentimento). "
            "Nao e genital mutilation (PROIBIDO)."
        ),
        guaranteed_by = ["OpenHealth", "OpenRelationship (consentimento)",
                       "OpenEducation (educacao sexual)"],
        metrics = [
            "mortalidade materna (meta: 0)",
            "acesso a anticoncepcional",
            "aborto seguro disponivel",
            "exames preventivos (%)",
        ],
        target = "0 mortalidade materna. 100% autonomia reprodutiva."),

    CareDimension.ERGONOMIC: CarePolicy(
        CareDimension.ERGONOMIC, RightType.GUARANTEED_ACCESS,
        "Trabalho que nao destrói o corpo",
        what_it_is = (
            "Nenhum trabalho na Republica pode causar lesao corporal "
            "evitavel. Ferramentas ergonomicas. Pausas obrigatorias. "
            "Rotacao de tarefas (ninguem faz a mesma coisa 8h). "
            "Automacao de tarefas que destroem corpo (robos para pesado). "
            "Postura ensinada (sentar certo, levantar certo). "
            "LER/DORT sao FALHA DO SISTEMA, nao do trabalhador."
        ),
        what_it_is_not = (
            "Nao e 'ergonomia' para extrair mais produtividade. "
            "Nao e cadeira cara como status. Nao e fonte do tipo 'gaming'. "
            "E CADEIRA QUE NAO DESTRÓI COLUNA. Simples."
        ),
        guaranteed_by = ["OpenProduction (ferramentas ergonomicas)",
                       "automacao", "jornada reduzida"],
        metrics = [
            "incidencia de LER/DORT (meta: reduzir 90%)",
            "queixas ergonomicas por cidadao",
            "% tarefas pesadas automatizadas",
        ],
        target = "-90% LER/DORT. Zero lesao por trabalho evitavel."),
}


// ============================================================================
// Physical Care Tracker
// ============================================================================

// decorador: @dataclass
classe CitizenCareProfile:
    // Perfil de cuidado fisico de um cidadao.
    citizen_id: texto
    name: texto
    age: inteiro
    seja gender: texto = ""
    // Status por dimensao (0-100)
    seja scores: {CareDimension: flutuante} = field(default_factory=dict)
    // Barreiras (o que impede cuidado ideal)
    seja barriers: [texto] = field(default_factory=list)
    // Necessidades especiais
    seja disabilities: [texto] = field(default_factory=list)
    seja chronic_conditions: [texto] = field(default_factory=list)
    // Autonomia: o que a pessoa ESCOLHE
    seja personal_choices: [texto] = field(default_factory=list)


classe PhysicalCareSystem:
    // Sistema que garante cuidado fisico para toda a Republica.

    INTEGRACAO:
    - OpenHealth: dados medicos, checkup, vacina
    - OpenFood: nutricao garantida
    - OpenProduction: ferramentas ergonomicas, produtos de higiene
    - OpenTransport: bicicletas, movimento
    - OpenPsychology: saude mental
    - OpenRelationship: autonomia reprodutiva, consentimento
    - OpenEducation: educacao fisica como jogo, educacao nutricional
    // 

    funcao __init__(self):
        self.policies = POLICIES
        self.profiles: {texto: CitizenCareProfile} = {}
        self._init_profiles()

    funcao _init_profiles(self):
        // Cidadaos exemplo com diferentes situacoes.
        data = [
            ("C-001", "Cleiton", 35, "M", 85, 70, 60, 90, 95, 80, 70, 85),
            ("C-002", "Amina", 28, "F", 60, 40, 50, 70, 80, 30, 60, 50),
            ("C-003", "Sven", 42, "NB", 75, 85, 80, 85, 90, 70, 75, 60),
            ("C-004", "Mei", 24, "F", 90, 95, 70, 95, 100, 90, 85, 80),
            ("C-005", "Kofi", 31, "M", 50, 30, 40, 60, 70, 40, 50, 40),
            ("C-006", "Yara", 19, "F", 65, 80, 55, 75, 85, 60, 70, 50),
            ("C-007", "Lars", 55, "M", 70, 60, 45, 80, 85, 50, 65, 30),
        ]
        dims = list(CareDimension)
        para cada d em data:
            desempacote cid, name, age, gender = d[:4]
            scores = {}
            para cada (i, dim) em enumere(dims):
                scores[dim] = d[4 + i]
            barriers = []
            se scores[CareDimension.MOVEMENT] < 50 entao:
                barriers.append("sem espaco verde proximo")
            se scores[CareDimension.SLEEP] < 50 entao:
                barriers.append("jornada nao permite 7h sono")
            se scores[CareDimension.MENTAL] < 50 entao:
                barriers.append("sem acesso a terapia")
            se scores[CareDimension.REPRODUCTIVE] < 50 entao:
                barriers.append("sem acesso a saude reprodutiva")
            self.profiles[cid] = CitizenCareProfile(
                citizen_id = cid, name=name, age=age, gender=gender,
                scores = scores, barriers=barriers)

    funcao assess(self, citizen_id: texto) -> {texto: qualquer}:
        // Avaliar cuidado fisico de um cidadao.
        p = self.profiles.get(citizen_id)
        se nao p entao:
            retorne {"error": "nao encontrado"}

        overall = soma(p.scores.values()) / tamanho(p.scores)
        weakest = minimo(p.scores, key=p.scores.get)
        strongest = maximo(p.scores, key=p.scores.get)

        status = self._status_from_score(overall)

        retorne {
            "citizen": p.name,
            "overall_score": arredonde(overall, 1),
            "status": status.value,
            "by_dimension": {d.value: s para d, s in p.scores.items()},
            "weakest": weakest.value,
            "strongest": strongest.value,
            "barriers": p.barriers,
            p.scores[weakest] < 50 ? "intervention_needed": weakest : nulo,
        }

    funcao republic_report(self) -> {texto: qualquer}:
        // Relatorio de cuidado fisico da Republica inteira.
        dim_scores = defaultdict(list)
        para cada p em self.profiles.values():
            para cada (dim, score) em p.scores.items():
                dim_scores[dim].append(score)

        averages = {}
        para cada (dim, scores) em dim_scores.items():
            avg = soma(scores) / tamanho(scores)
            averages[dim] = arredonde(avg, 1)

        overall = soma(averages.values()) / tamanho(averages)

        // Identificar dimensoes abaixo da meta
        below_target = []
        para cada (dim, avg) em averages.items():
            se avg < 60 entao:
                below_target.append({
                    "dimension": dim.value,
                    "average": avg,
                    "action": self._intervention(dim),
                })

        retorne {
            "citizens_assessed": tamanho(self.profiles),
            "overall_republic_score": arredonde(overall, 1),
            "by_dimension": averages,
            "below_target": below_target,
            "barriers_common": self._common_barriers(),
        }

    // decorador: @staticmethod
    funcao _status_from_score(score: flutuante) -> CareStatus:
        se score >= 80 entao:
            retorne CareStatus.OPTIMAL
        se score >= 65 entao:
            retorne CareStatus.ADEQUATE
        se score >= 50 entao:
            retorne CareStatus.BELOW
        se score >= 30 entao:
            retorne CareStatus.DEFICIENT
        retorne CareStatus.CRITICAL

    funcao _intervention(self, dim: CareDimension) -> texto:
        policy = self.policies.get(dim)
        se policy entao:
            retorne ("Intervencao: ativar {', '.join(policy.guaranteed_by[:2])}. "
                   "Meta: {policy.target}")
        retorne ""

    funcao _common_barriers(self) retorna List[(texto, inteiro)]:
        barrier_count = defaultdict(inteiro)
        para cada p em self.profiles.values():
            para cada b em p.barriers:
                barrier_count[b] += 1
        retorne ordene(barrier_count.items(), key=(x) -> -x[1])[:5]


// ============================================================================
// Main
// ============================================================================

se __name__ == "__main__" entao:
    imprima("=" * 80)
    imprima("  OPENREPUBLIC -- POLITICA DE CUIDADOS FISICOS")
    imprima("  'O corpo nao e maquina. E templo da existencia.'")
    imprima("=" * 80)

    system = PhysicalCareSystem()

    // === 1. The 8 Policies ===
    imprima("\n\n  === 8 POLITICAS DE CUIDADO FISICO ===\n")

    para cada (dim, policy) em system.policies.items():
        imprima("\n  {'='*70}")
        imprima("  {dim.value.upper()} -- {policy.right_type.value}")
        imprima("  {policy.title}")
        imprima("  {'='*70}")
        imprima("\n  E: {policy.what_it_is[:200]}...")
        imprima("\n  NAO E: {policy.what_it_is_not[:150]}...")
        imprima("\n  Garantido por: {', '.join(policy.guaranteed_by)}")
        imprima("  Meta: {policy.target}")

    // === 2. Citizen Assessment ===
    imprima("\n\n  === AVALIACAO INDIVIDUAL ===\n")

    para cada cid em ["C-001", "C-002", "C-005", "C-007"]:
        result = system.assess(cid)
        imprima("\n  {result['citizen']} (overall: {result['overall_score']} -- {result['status']})")
        imprima("    Mais forte: {result['strongest']}")
        imprima("    Mais fragil: {result['weakest']}")
        se result["barriers"] entao:
            imprima("    Barreiras: {', '.join(result['barriers'])}")
        se result.get("intervention_needed") entao:
            imprima("    INTERVENCAO: {result['intervention_needed'].value}")

    // === 3. Republic Report ===
    imprima("\n\n  === RELATORIO DA REPUBLICA ===\n")

    report = system.republic_report()
    imprima("  Cidadaos avaliados: {report['citizens_assessed']}")
    imprima("  Score geral da Republica: {report['overall_republic_score']}")
    imprima("\n  Por dimensao:")
    para cada (dim, score) em ordene(report["by_dimension"].items(), key=(x) -> x[1]):
        bar = "#" * inteiro(score / 5)
        flag = score < 60 ? " !!!" : ""
        imprima("    {dim:<15} {score:>5.1f}  {bar}{flag}")

    imprima("\n  Dimensoes abaixo da meta:")
    para cada item em report["below_target"]:
        imprima("    {item['dimension']}: {item['average']} -> {item['action'][:80]}")

    imprima("\n  Barreiras mais comuns:")
    para cada (barrier, count) em report["barriers_common"]:
        imprima("    {barrier} ({count} cidadaos)")

    // === Philosophy ===
    imprima("\n\n{'='*80}")
    imprima("  FILOSOFIA: CUIDADO FISICO")
    imprima("{'='*80}")
    imprima("""
  CAPITALISMO OPENREPUBLIC
  --------------------------------------- ---------------------------------------
  Corpo = maquina de trabalho Corpo = templo da existencia
  Saude = produto ($) Saude = direito
  Academia = consumismo ($$$) Movimento = direito + prazer
  Bem-estar = app pago ($) Bem-estar = comunidade + natureza
  Sono = 'fraqueza' (hustle culture)       Sono = direito inegociavel
  Dietas = industria bilionaria ($) Comida = real, nutritiva, garantida
  Estetica = competicao Corpo = autonomia, nao padrao
  Saude mental = estigma Saude mental = tratamento sem julgamento
  Prevencao = seguro pago ($) Prevencao = direito universal
  Reproducao = controle do Estado Reproducao = autonomia total da pessoa
  Ergonomia = produtividade Ergonomia = corpo que nao se destrói

  8 DIMENSOES DO CUIDADO:

  1. ALIMENTACAO: 3 refeicoes REAIS por dia. Direito.
  2. MOVIMENTO: corpo em alegria. Direito + prazer.
  3. SONO: 7-9h. Direito inegociavel.
  4. HIGIENE: agua, sabao, absorvente. Direito.
  5. PREVENCAO: checkup + vacina. Direito.
  6. MENTAL: terapia + comunidade + lazer. Direito.
  7. REPRODUTIVA: autonomia total sobre o corpo. Direito.
  8. ERGONOMICA: trabalho que nao destrói. Direito.

  O QUE A REPUBLICA GARANTE:
    - Comida real (OpenFood + OpenAgrarian)
    - Espaco para movimento (parques, bicicletas)
    - Moradia tranquila para dormir (OpenHome)
    - Agua e produtos de higiene (OpenProduction)
    - Checkup e vacina (OpenHealth)
    - Terapia e comunidade (OpenPsychology + OpenSocial)
    - Autonomia reprodutiva (OpenHealth + OpenRelationship)
    - Ferramentas ergonomicas (OpenProduction)

  O QUE A REPUBLICA PROIBE:
    - Trabalho que destrói o corpo
    - Negar comida, agua, sono, higiene
    - Julgar corpo (tamanho, forma, deficiencia)
    - Controlar reproducao alheia
    - Mutilacao genital
    - Forcar tratamento (exceto risco de vida a outrem)

  PRINCIPIO FUNDAMENTAL:

    "Seu corpo e seu. A Republica cuida para que ele
     funcione bem. Mas o que voce faz com ele e escolha sua.

     Comer, mover, dormir, limpar, prevenir, cuidar da mente,
     decidir sobre reproducao -- tudo e direito garantido.

     Ninguem te julga pelo corpo.
     Ninguem te força um padrao.
     Ninguem lucra com sua insatisfacao.

     O corpo nao e maquina de trabalho.
     O corpo nao e produto de consumo.
     O corpo e VOCE. e voce merece cuidado."
// )

```
