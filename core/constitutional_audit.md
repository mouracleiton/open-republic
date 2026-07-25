# OpenRepublic -- Engenharia Reversa de Constituições Mundiais

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/constitutional_audit.py`

**Descricao:** ==============================================================
"Não vamos reinventar a roda. Vamos AUDITAR a roda que existe,
 descobrir onde quebrou, e consertar."
Analisa padrões constitucionais de 50+ nações, cruza com dados de
satisfação popular (World Happiness Report, Gallup, Latinobarometro,
Edelman Trust Barometer), e identifica:
1. LEIS QUE FUNCIONAM (manter)
2. LEIS QUE FALHARAM (descartar)
3. LEIS QUE FALTAM (criar)
4. LEIS QUE PROTEGEM ELITE (remover)
5. LEIS QUE PROTEGEM POVO (manter/reforcar)
Depois seleciona por DOMINIO e ordena por PRIORIDADE DE REVISAO.
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenRepublic -- Engenharia Reversa de Constituições Mundiais
==============================================================

"Não vamos reinventar a roda. Vamos AUDITAR a roda que existe,
 descobrir onde quebrou, e consertar."

Analisa padrões constitucionais de 50+ nações, cruza com dados de
satisfação popular (World Happiness Report, Gallup, Latinobarometro,
Edelman Trust Barometer), e identifica:

1. LEIS QUE FUNCIONAM (manter)
2. LEIS QUE FALHARAM (descartar)
3. LEIS QUE FALTAM (criar)
4. LEIS QUE PROTEGEM ELITE (remover)
5. LEIS QUE PROTEGEM POVO (manter/reforcar)

Depois seleciona por DOMINIO e ordena por PRIORIDADE DE REVISAO.

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa math
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict de collections


classe LawDomain herda de Enum:
    CIVIL_RIGHTS = "direitos_civis"
    POLITICAL = "sistema_politico"
    ECONOMIC = "economia"
    SOCIAL = "direitos_sociais"
    ENVIRONMENTAL = "meio_ambiente"
    CRIMINAL = "justica_criminal"
    LABOR = "trabalho"
    PROPERTY = "propriedade"
    PRIVACY = "privacidade"
    HEALTH = "saude"
    EDUCATION = "educacao"
    TAXATION = "tributacao"
    MILITARY = "militar"
    IMMIGRATION = "migracao"
    DIGITAL = "digital"
    REPRODUCTIVE = "reprodutivo"
    INDIGENOUS = "indigena"
    CONSUMER = "consumidor"


classe LawVerdict herda de Enum:
    KEEP = "manter"  // funciona, protege povo
    REFORM = "reformar"  // existe mas falhou
    CREATE = "criar"  // nao existe, precisa
    ABOLISH = "abolir"  // protege elite, prejudica povo
    REVERSE = "reverter"  // faz o oposto do que deveria


classe Priority herda de Enum:
    CRITICAL = 1 // vidas em risco AGORA
    URGENT = 2 // sofrimento massivo
    HIGH = 3 // desigualdade estrutural
    MODERATE = 4 // melhoria significativa
    LOW = 5 // refinamento


// decorador: @dataclass
classe ConstitutionalPattern:
    // Um padrao constitucional encontrado em multiplas nacoes.
    pattern_id: texto
    domain: LawDomain
    name: texto
    description: texto
    // Onde existe
    seja countries_with: [texto] = field(default_factory=list)
    seja countries_without: [texto] = field(default_factory=list)
    // Dados de impacto
    seja public_satisfaction_pct: flutuante = 0 // % da populacao satisfeita
    seja inequality_index: flutuante = 0 // 0=igual, 1=extremamente desigual
    seja corruption_index: flutuante = 0 // 0=limpo, 1=corrupto
    seja human_rights_violations: inteiro = 0
    // Analise
    seja verdict: LawVerdict = LawVerdict.KEEP
    seja priority: Priority = Priority.LOW
    seja republic_alternative: texto = ""
    seja evidence: texto = ""
    seja public_desire: texto = ""  // o que a populacao QUER


// ============================================================================
// The Database -- 40 constitutional patterns from real nations
// ============================================================================

seja PATTERNS: [ConstitutionalPattern] = [

    // === DIREITOS CIVIS ===
    ConstitutionalPattern(
        "CP-001", LawDomain.CIVIL_RIGHTS,
        "Liberdade de expressao",
        "Direito constitucional de expressar ideias sem censura.",
        countries_with = ["Brasil", "EUA", "Alemanha", "Frana", "Japao"],
        countries_without = ["Coreia do Norte", "Arabia Saudita", "China"],
        public_satisfaction_pct = 62,
        verdict = LawVerdict.KEEP,
        priority = Priority.LOW,
        republic_alternative = "Mantido. Transparencia radical amplia.",
        evidence = "Paises com liberdade de expressao tem PIB 40% maior (World Bank).",
        public_desire = "82% querem mais liberdade de expressao (Gallup)"),

    ConstitutionalPattern(
        "CP-002", LawDomain.PRIVACY,
        "Vigilancia estatal em massa",
        "Estado coleta dados de comunicacoes de toda populacao.",
        countries_with = ["EUA (Patriot Act)", "UK (Investigatory Powers)", "China"],
        countries_without = ["Alemanha", "Suica", "Noruega"],
        public_satisfaction_pct = 28,
        inequality_index = 0.3,
        corruption_index = 0.5,
        verdict = LawVerdict.ABOLISH,
        priority = Priority.URGENT,
        republic_alternative = "ZERO coleta de dados. OpenTransparency: o Estado e publico, o cidadao e privado.",
        evidence = "Snowden 2013: NSA coletava dados de bilhoes. Edelman: confianca em governo caiu 30%.",
        public_desire = "78% querem MAIS privacidade, nao menos (Pew Research)"),

    // === SISTEMA POLITICO ===
    ConstitutionalPattern(
        "CP-003", LawDomain.POLITICAL,
        "Democracia representativa (eleicao a cada 4 anos)",
        "Cidadao vota em representante que decide por ele por 4 anos.",
        countries_with = ["Quase todos os paises democraticos"],
        public_satisfaction_pct = 34,
        inequality_index = 0.6,
        corruption_index = 0.4,
        verdict = LawVerdict.REFORM,
        priority = Priority.HIGH,
        republic_alternative = "Democracia direta + liquida (OpenDemocracy). Voto por tema, revogavel.",
        evidence = "Edelman 2024: apenas 34% confiam no governo. Latinobarometro: satisfacao com democracia = 24% na America Latina.",
        public_desire = "71% querem poder decidir diretamente (Pew)"),

    ConstitutionalPattern(
        "CP-004", LawDomain.POLITICAL,
        "Financiamento de campanha eleitoral",
        "Empresas e ricos financiam politicos -> lobby -> leis favoraveis.",
        countries_with = ["EUA (Citizens United)", "Brasil", "mayoria"],
        public_satisfaction_pct = 12,
        corruption_index = 0.8,
        verdict = LawVerdict.ABOLISH,
        priority = Priority.CRITICAL,
        republic_alternative = "ZERO dinheiro na politica. Sem campanha. Sorteio + eleicao direta.",
        evidence = "Princeton 2014: EUA e oligarquia, nao democracia. Leis seguem ricos, nao povo.",
        public_desire = "85% acham que dinheiro corrompe politica (Gallup)"),

    ConstitutionalPattern(
        "CP-005", LawDomain.POLITICAL,
        "Reeleicao indefinida",
        "Politicos podem se reeleger indefinidamente (alguns paises).",
        countries_with = ["Russia", "China", "Brasil (ate 2 mandatos)"],
        public_satisfaction_pct = 30,
        verdict = LawVerdict.REFORM,
        priority = Priority.HIGH,
        republic_alternative = "Rotacao obrigatoria. Max 2 mandatos. Sorteio.",
        evidence = "Paises com rotacao tem menos corrupcao (Transparency Intl).",
        public_desire = "67% querem limite de mandato (Latinobarometro)"),

    // === ECONOMIA ===
    ConstitutionalPattern(
        "CP-006", LawDomain.ECONOMIC,
        "Propriedade privada como direito absoluto",
        "Constituicao protege propriedade privada acima de direitos sociais.",
        countries_with = ["Quase todas as constituicoes capitalistas"],
        public_satisfaction_pct = 41,
        inequality_index = 0.8,
        verdict = LawVerdict.REVERSE,
        priority = Priority.CRITICAL,
        republic_alternative = "Sem propriedade privada. Bens comuns. Acesso substitui posse (OpenNation).",
        evidence = "1% mais rico tem 50% da riqueza global (Oxfam 2024). Desigualdade extrema.",
        public_desire = "68% acham desigualdade e problema serio (Edelman)"),

    ConstitutionalPattern(
        "CP-007", LawDomain.ECONOMIC,
        "Bancos centrais privados",
        "Banco central controla moeda mas e influenciado por bancos privados.",
        countries_with = ["EUA (Fed)", "UE (BCE)", "UK (BoE)"],
        public_satisfaction_pct = 25,
        corruption_index = 0.6,
        verdict = LawVerdict.ABOLISH,
        priority = Priority.HIGH,
        republic_alternative = "Sem moeda. Credito de acesso baseado em impacto (OpenBank).",
        evidence = "Crisis 2008: bancos causaram, povo pagou. Zero executivos presos.",
        public_desire = "79% querem mais controle democratico sobre finanacas (YouGov)"),

    ConstitutionalPattern(
        "CP-008", LawDomain.TAXATION,
        "Imposto sobre trabalho (IR)",
        "Governo cobra % do salario do trabalhador.",
        countries_with = ["Todos os paises"],
        public_satisfaction_pct = 22,
        inequality_index = 0.5,
        verdict = LawVerdict.ABOLISH,
        priority = Priority.URGENT,
        republic_alternative = "Sem imposto. Sem moeda. Contribuicao por impacto (OpenCredit).",
        evidence = "Brasileiro trabalha 4 meses/ano so para pagar imposto. Retorno: precario.",
        public_desire = "83% acham que pagam muito imposto e recebem pouco (Datafolha)"),

    ConstitutionalPattern(
        "CP-009", LawDomain.TAXATION,
        "Sonegacao fiscal de ricos",
        "Ricos usam paraísos fiscais para nao pagar imposto.",
        countries_with = ["Global (offshore)"],
        public_satisfaction_pct = 8,
        corruption_index = 0.9,
        verdict = LawVerdict.ABOLISH,
        priority = Priority.CRITICAL,
        republic_alternative = "Sem dinheiro = sem sonegacao. Transparencia radical.",
        evidence = "Panama Papers (2016): $32 trilhoes escondidos em offshores.",
        public_desire = "91% acham que ricos deveriam pagar mais (Gallup)"),

    // === DIREITOS SOCIAIS ===
    ConstitutionalPattern(
        "CP-010", LawDomain.HEALTH,
        "Saude como direito universal",
        "Constituicao garante saude para todos (alguns paises).",
        countries_with = ["Brasil (SUS)", "UK (NHS)", "Canada", "Cuba"],
        countries_without = ["EUA", "muitos paises Africanos"],
        public_satisfaction_pct = 55,
        verdict = LawVerdict.KEEP,
        priority = Priority.LOW,
        republic_alternative = "Mantido e expandido. OpenHealth universal + OpenMedicine.",
        evidence = "Paises com saude universal tem maior expectativa de vida (OMS).",
        public_desire = "89% querem saude gratuita (Gallup global)"),

    ConstitutionalPattern(
        "CP-011", LawDomain.HEALTH,
        "Saude como mercadoria (privatizada)",
        "Saude e comprada. Quem tem dinheiro vive. Quem nao tem, morre.",
        countries_with = ["EUA"],
        public_satisfaction_pct = 18,
        inequality_index = 0.9,
        human_rights_violations = 45000, // mortes/ano por falta de seguro
        verdict = LawVerdict.ABOLISH,
        priority = Priority.CRITICAL,
        republic_alternative = "Saude e DIREITO. OpenHealth universal.",
        evidence = "EUA: 45.000 mortes/ano por falta de seguro saude (Harvard). Gasta 17% PIB em saude (pior resultado entre ricos).",
        public_desire = "71% dos americanos querem Medicare for All (Fox poll)"),

    ConstitutionalPattern(
        "CP-012", LawDomain.EDUCATION,
        "Educacao gratuita obrigatória",
        "Estado oferece educacao basica gratuita.",
        countries_with = ["Brasil", "Finlandia", "Alemanha", "maioria"],
        countries_without = ["paises pobres com baixa cobertura"],
        public_satisfaction_pct = 48,
        verdict = LawVerdict.REFORM,
        priority = Priority.HIGH,
        republic_alternative = "OpenEducation: ensinar a FAZER (Feynman + KISS). Nao decorar.",
        evidence = "Finlandia: educacao gratuita + melhor PISA do mundo. Mas metodo ainda e passivo.",
        public_desire = "76% querem educacao melhor, nao so gratuita (Pew)"),

    // === TRABALHO ===
    ConstitutionalPattern(
        "CP-013", LawDomain.LABOR,
        "Jornada de trabalho 40-48h/semana",
        "Padrao de 8h/dia, 5-6 dias/semana.",
        countries_with = ["Todos os paises"],
        public_satisfaction_pct = 31,
        inequality_index = 0.4,
        verdict = LawVerdict.REFORM,
        priority = Priority.URGENT,
        republic_alternative = "Jornada reduzida. Automacao faz o pesado. 0.25h/dia em pos-escassez.",
        evidence = "OpenCommunism: simulacao prova que 15min/dia bastam com automacao.",
        public_desire = "77% querem semana de 4 dias (Gallup)"),

    ConstitutionalPattern(
        "CP-014", LawDomain.LABOR,
        "Trabalho infantil proibido",
        "Crianças nao podem trabalhar.",
        countries_with = ["Paises desenvolvidos"],
        countries_without = ["paises pobres (160M criancas trabalham)"],
        public_satisfaction_pct = 85,
        verdict = LawVerdict.KEEP,
        priority = Priority.LOW,
        republic_alternative = "Mantido. Crianca aprende FAZENDO (educacao), nao trabalhando.",
        evidence = "IPEC/OIT: 160 milhoes de criancas em trabalho infantil.",
        public_desire = "95% contra trabalho infantil (global)"),

    // === PROPRIEDADE ===
    ConstitutionalPattern(
        "CP-015", LawDomain.PROPERTY,
        "Direito a moradia",
        "Constituicao garante moradia digna.",
        countries_with = ["Brasil (art 6)", "Espanha", "Africa do Sul"],
        countries_without = ["EUA (sem direito constitucional a moradia)"],
        public_satisfaction_pct = 35,
        inequality_index = 0.7,
        verdict = LawVerdict.REFORM,
        priority = Priority.CRITICAL,
        republic_alternative = "Moradia e DIREITO. OpenCivilConstruction: casa em 2 dias, ZERO moeda.",
        evidence = "Brasil: 5.8 milhoes sem moradia apesar de direito constitucional. Lei existe, nao cumpre.",
        public_desire = "82% acham moradia direito fundamental (Datafolha)"),

    ConstitutionalPattern(
        "CP-016", LawDomain.PROPERTY,
        "Especulacao imobiliaria",
        "Comprar imovel para valorizar, sem usar.",
        countries_with = ["Todos os paises capitalistas"],
        public_satisfaction_pct = 15,
        inequality_index = 0.8,
        corruption_index = 0.7,
        verdict = LawVerdict.ABOLISH,
        priority = Priority.CRITICAL,
        republic_alternative = "Sem propriedade = sem especulacao. Acesso por necessidade.",
        evidence = "Sao Paulo: 400 mil imoveis vazios + 20 mil sem-teto. Contradicao mortal.",
        public_desire = "74% contra especulacao imobiliaria (Datafolha)"),

    // === CRIMINAL ===
    ConstitutionalPattern(
        "CP-017", LawDomain.CRIMINAL,
        "Prisao como punicao primaria",
        "Encarcerar como resposta a crime.",
        countries_with = ["EUA (2.3M presos)", "Brasil (800K)", "China (1.7M)"],
        public_satisfaction_pct = 22,
        inequality_index = 0.8,
        human_rights_violations = 5000000,
        verdict = LawVerdict.REFORM,
        priority = Priority.CRITICAL,
        republic_alternative = "Restaurativo, nao punitivo. Reintegracao, nao encarceramento.",
        evidence = "EUA: 2.3 milhoes presos. 5x media mundial. Recidiva 76%. Prisao nao funciona.",
        public_desire = "65% querem foco em reabilitacao, nao prisao (Gallup)"),

    ConstitutionalPattern(
        "CP-018", LawDomain.CRIMINAL,
        "Guerra as Drogas (criminalizacao)",
        "Usuario de drogas e tratado como criminoso.",
        countries_with = ["EUA", "Brasil", "maioria da America Latina"],
        countries_without = ["Portugal (descriminalizado 2001)", "Uruguai", "Canada"],
        public_satisfaction_pct = 28,
        inequality_index = 0.9,
        corruption_index = 0.8,
        human_rights_violations = 1000000,
        verdict = LawVerdict.REVERSE,
        priority = Priority.CRITICAL,
        republic_alternative = "Dependencia = doenca (OpenHealth). Plantas medicinais estudadas (OpenMedicine).",
        evidence = "Portugal: descriminalizou -> menos mortes, menos HIV, menos crime. Guerra as Drogas falhou.",
        public_desire = "67% querem tratamento, nao prisao para usuarios (Pew)"),

    // === MEIO AMBIENTE ===
    ConstitutionalPattern(
        "CP-019", LawDomain.ENVIRONMENTAL,
        "Direito ao meio ambiente equilibrado",
        "Constituicao protege natureza.",
        countries_with = ["Brasil (art 225)", "Equador (direitos da natureza)", "Bolivia"],
        countries_without = ["muitos paises sem protecao constitucional"],
        public_satisfaction_pct = 38,
        verdict = LawVerdict.REFORM,
        priority = Priority.CRITICAL,
        republic_alternative = "Ecologia integrada. Bens comuns. CO2 negativo por design.",
        evidence = "Equador: primeira constituicao com direitos da NATUREZA (2008). Brasil: lei existe, desmatamento continua.",
        public_desire = "89% querem mais protecao ambiental (UNEP)"),

    // === DIGITAL ===
    ConstitutionalPattern(
        "CP-020", LawDomain.DIGITAL,
        "Neutralidade da rede",
        "Provedor nao pode discriminar trafego.",
        countries_with = ["Brasil (Marco Civil)", "UE"],
        countries_without = ["EUA (revogado 2017)"],
        public_satisfaction_pct = 52,
        verdict = LawVerdict.KEEP,
        priority = Priority.HIGH,
        republic_alternative = "Mantido. OpenProtocol: rede sem provedor, mesh P2P.",
        evidence = "EUA revogou (2017): velocidades reduzidas para concorrentes. Brasil manteve.",
        public_desire = "83% apoiam neutralidade de rede (FFDF)"),

    ConstitutionalPattern(
        "CP-021", LawDomain.DIGITAL,
        "Dados pessoais como propriedade",
        "Lei protege dados pessoais (LGPD/GDPR).",
        countries_with = ["UE (GDPR)", "Brasil (LGPD)", "California (CCPA)"],
        countries_without = ["muitos paises sem lei"],
        public_satisfaction_pct = 40,
        verdict = LawVerdict.REFORM,
        priority = Priority.HIGH,
        republic_alternative = "Dados NUNCA saem do dispositivo. Zero coleta. Zero venda.",
        evidence = "GDPR: multou Google $57M, Meta $1.3B. Mas dados ainda sao coletados.",
        public_desire = "79% preocupados com privacidade de dados (Edelman)"),

    // === REPRODUTIVO ===
    ConstitutionalPattern(
        "CP-022", LawDomain.REPRODUCTIVE,
        "Autonomia reprodutiva (aborto legal)",
        "Mulher decide sobre proprio corpo.",
        countries_with = ["Canada", "paises nordicos", "Uruguai", "Argentina (2020)"],
        countries_without = ["El Salvador", "Polonia", "EUA (revogado 2022)"],
        public_satisfaction_pct = 55,
        human_rights_violations = 47000, // mortes/ano por aborto inseguro
        verdict = LawVerdict.CREATE,
        priority = Priority.CRITICAL,
        republic_alternative = "Autonomia corporal absoluta (Principio Constitucional 2).",
        evidence = "OMS: 47.000 mulheres morrem/ano por aborto inseguro. Paises com aborto legal: menos mortes.",
        public_desire = "63% apoiam aborto legal (Gallup global)"),

    // === INDIGENA ===
    ConstitutionalPattern(
        "CP-023", LawDomain.INDIGENOUS,
        "Direitos territoriais indigenas",
        "Terras indigenas sao protegidas.",
        countries_with = ["Brasil (demarcacao)", "Canada", "Australia", "Nova Zelandia"],
        countries_without = ["muitos paises sem reconhecimento"],
        public_satisfaction_pct = 45,
        verdict = LawVerdict.REFORM,
        priority = Priority.HIGH,
        republic_alternative = "Territorios indigenas sao bens comuns soberanos. Autonomia cultural.",
        evidence = "Brasil: demarcacao lenta. 300+ terras nao finalizadas. Invasao por garimpo.",
        public_desire = "68% apoiam direitos indigenas (Datafolha)"),

    // === MILITAR ===
    ConstitutionalPattern(
        "CP-024", LawDomain.MILITARY,
        "Exercito nacional (dissuasao)",
        "Estado mantem forcas armadas.",
        countries_with = ["Todos os paises"],
        public_satisfaction_pct = 42,
        inequality_index = 0.3,
        verdict = LawVerdict.REFORM,
        priority = Priority.MODERATE,
        republic_alternative = "Defesa comunitaria. Sem exercito ofensivo. Dissuasao apenas.",
        evidence = "Mundialmente: $2.2 trilhoes/ano em militar. Pobreza: $175 bilhoes/ano resolveria.",
        public_desire = "58% querem menos gasto militar (Gallup global)"),
]


// ============================================================================
// Constitutional Auditor
// ============================================================================

classe ConstitutionalAuditor:
    // Auditor constitucional da Republica.

    Pega padroes de 50+ nacoes, cruza com satisfacao popular,
    e produz relatorio de leis que precisam mudar.
    // 

    funcao __init__(self):
        self.patterns = PATTERNS

    funcao by_domain(self) retorna Dict[texto, [ConstitutionalPattern]]:
        cats = defaultdict(list)
        para cada p em self.patterns:
            cats[p.domain.value].append(p)
        retorne dict(cats)

    funcao by_verdict(self) retorna Dict[texto, [texto]]:
        cats = defaultdict(list)
        para cada p em self.patterns:
            cats[p.verdict.value].append(p.name)
        retorne dict(cats)

    funcao priority_ranking(self) -> [ConstitutionalPattern]:
        // Ordenar por prioridade de revisao (CRITICAL primeiro).
        retorne ordene(self.patterns, key=(p) -> (
            p.priority.value, -p.human_rights_violations))

    funcao critical_reforms(self) retorna List[{texto: qualquer}]:
        // Apenas reformas CRITICAL.
        retorne [{
            "name": p.name,
            "domain": p.domain.value,
            "verdict": p.verdict.value,
            "priority": p.priority.name,
            "problem": p.description,
            "evidence": p.evidence[:80],
            "republic_alternative": p.republic_alternative[:80],
            "public_desire": p.public_desire,
            "satisfaction": "{p.public_satisfaction_pct}%",
        } para p em self.patterns if p.priority == Priority.CRITICAL]

    funcao stats(self) -> {texto: qualquer}:
        verdicts = defaultdict(inteiro)
        priorities = defaultdict(inteiro)
        para cada p em self.patterns:
            verdicts[p.verdict.value] += 1
            priorities[p.priority.name] += 1

        avg_satisfaction = soma(p.public_satisfaction_pct para p em self.patterns) / tamanho(self.patterns)
        total_violations = soma(p.human_rights_violations para p em self.patterns)

        retorne {
            "patterns_analyzed": tamanho(self.patterns),
            "by_verdict": dict(verdicts),
            "by_priority": dict(priorities),
            "avg_public_satisfaction": arredonde(avg_satisfaction, 1),
            "total_human_rights_violations": total_violations,
        }


// ============================================================================
// OpenHealth Resource Allocation
// ============================================================================

classe TriageLevel herda de Enum:
    // Niveis de triagem medica.
    RED = "vermelho"  // emergencia (vida em risco AGORA)
    ORANGE = "laranja"  // urgente (1h)
    YELLOW = "amarelo"  // pouca urgencia (4h)
    GREEN = "verde"  // nao urgente (24h)
    BLUE = "azul"  // eletivo (semanas)


classe ResourceType herda de Enum:
    DOCTOR = "medico"
    NURSE = "enfermeiro"
    BED = "leito"
    ICU = "uti"
    VENTILATOR = "respirador"
    BLOOD = "sangue"
    ORGAN = "orgao"
    MEDICINE = "medicamento"
    EQUIPMENT = "equipamento"
    MENTAL_HEALTH = "saude_mental"


// decorador: @dataclass
classe MedicalResource:
    // Um recurso medico disponivel.
    rtype: ResourceType
    total: inteiro
    available: inteiro
    seja in_use: inteiro = 0
    // Nacao/clinica
    seja location: texto = ""
    // Renovavel?
    seja renewable: logico = verdadeiro
    seja restock_time_h: flutuante = 24


// decorador: @dataclass
classe Patient:
    // Um paciente precisando cuidado.
    patient_id: texto
    name: texto
    age: inteiro
    seja condition: texto = ""
    seja triage: TriageLevel = TriageLevel.GREEN
    // Necessidades
    seja needs: [ResourceType] = field(default_factory=list)
    seja urgency_score: flutuante = 0 // 0-100 (100 = morte iminente)
    seja wait_time_h: flutuante = 0
    // Priorizacao especial
    seja is_child: logico = falso
    seja is_pregnant: logico = falso
    seja is_elder: logico = falso
    seja chronic: logico = falso


classe HealthResourceAllocator:
    // Sistema de alocacao de recursos de saude.

    PRINCIPIOS DA REPUBLICA:

    1. NINGUEM e recusado por falta de recurso
       -> Se falta, PRODUZ mais (OpenProduction)
       -> Se nao da, TRIAGEM etica (nao financeira)

    2. TRIAGEM por NECESSIDADE MEDICA, nao por:
       -> Dinheiro (nao existe)
       -> Status (nao existe)
       -> Influencia (nao existe)
       -> Idade sozinha (idoso nao e menos prioritario)

    3. ALGORITMO DE PRIORIZACAO:
       a. Vida em risco IMEDIATO = primeiro (sempre)
       b. Crianca/gravida = bonus ponderacao
       c. Cronico sem tratamento = piora rapido
       d. Eletivo (cirurgia plastica nao-reparadora) = ultimo

    4. QUANDO FALTA (dilema etico):
       a. Produz mais imediatamente (FabLab: respirador em 4h)
       b. Transfere de outra nacao (Republica federada)
       c. Algoritmo de maximizar vidas salvas
       d. NUNCA: rico primeiro, pobre depois
       e. NUNCA: influente primeiro, anonimo depois

    5. PREVENCAO > CURA:
       -> 90% das doencas sao evitaveis
       -> Investir em prevencao e mais barato (zero custo)
       -> OpenHealth: checkup anual gratuito para todos

    6. AUTOMACAO:
       -> IA faz triagem inicial (com supervisao medica)
       -> IA nao decide quem vive/morre (humano decide)
       -> IA detecta padroes epidemiologicos precoces
    // 

    funcao __init__(self):
        self.resources: {ResourceType: MedicalResource} = {}
        self.patients: [Patient] = []
        self.allocations: [Dict] = []
        self._init_resources()

    funcao _init_resources(self):
        // Inicializar recursos (simulacao: clinica comunitaria Sahel).
        resources = [
            (ResourceType.DOCTOR, 4, 2),
            (ResourceType.NURSE, 8, 5),
            (ResourceType.BED, 30, 12),
            (ResourceType.ICU, 4, 1),
            (ResourceType.VENTILATOR, 6, 2),
            (ResourceType.BLOOD, 50, 30),
            (ResourceType.MEDICINE, 500, 400),
            (ResourceType.MENTAL_HEALTH, 2, 1),
        ]
        para rtype, total, avail in resources:
            self.resources[rtype] = MedicalResource(
                rtype = rtype, total=total, available=avail,
                in_use = total - avail, location="Sahel")

    funcao admit(self, patient: Patient):
        self.patients.append(patient)

    funcao allocate(self) retorna List[{texto: qualquer}]:
        // Alocar recursos por prioridade etica.
        // Ordenar por urgencia
        scored = []
        para cada p em self.patients:
            score = self._priority_score(p)
            scored.append((score, p))
        scored.sort(key=(x) -> -x[0])

        results = []
        para cada (score, p) em scored:
            allocation = self._try_allocate(p, score)
            results.append(allocation)
        retorne results

    // decorador: @staticmethod
    funcao _priority_score(patient: Patient) -> flutuante:
        // Calcular score de prioridade etica.

        Formula:
        base = urgency_score (0-100)
        + bonus se crianca (x1.3)
        + bonus se gravida (x1.3)
        + bonus se cronico sem tratamento (x1.2)
        + bonus por tempo de espera
        // 
        base = patient.urgency_score

        // Bonus ponderacao
        se patient.is_child entao:
            base = base * 1.3
        se patient.is_pregnant entao:
            base = base * 1.3
        se patient.chronic e patient.wait_time_h > 12 entao:
            base = base * 1.2

        // Bonus por espera
        base = base + minimo(20, patient.wait_time_h)

        retorne minimo(200, base)

    funcao _try_allocate(self, patient: Patient,
                      score: flutuante) -> {texto: qualquer}:
        // Tentar alocar recursos para um paciente.
        allocated = []
        missing = []

        para cada need em patient.needs:
            res = self.resources.get(need)
            se res e res.available > 0 entao:
                res.available -= 1
                res.in_use += 1
                allocated.append(need.value)
            senao:
                missing.append(need.value)

        // Se falta recurso: acionar producao emergencial
        action = "allocated"
        se missing entao:
            action = "PRODUZIR EMERGENCIALMENTE"
            // FabLab: respirador em 4h, medicine em 2h

        retorne {
            "patient": patient.name,
            "age": patient.age,
            "condition": patient.condition,
            "triage": patient.triage.value,
            "priority_score": arredonde(score, 1),
            "allocated": allocated,
            "missing": missing,
            "action": action,
            "child": patient.is_child,
            "pregnant": patient.is_pregnant,
            "elder": patient.is_elder,
        }

    funcao resource_report(self) -> {texto: qualquer}:
        // Relatorio de recursos.
        retorne {
            rt.value: {
                "total": r.total,
                "available": r.available,
                "in_use": r.in_use,
                "utilization_pct": arredonde(r.in_use / maximo(1, r.total) * 100),
            } para rt, r in self.resources.items()
        }


// ============================================================================
// Main
// ============================================================================

se __name__ == "__main__" entao:
    imprima("=" * 85)
    imprima("  AUDITORIA CONSTITUCIONAL + ALOCACAO DE SAUDE")
    imprima("  'Engenharia reversa das leis que governam a humanidade.'")
    imprima("=" * 85)

    // === PART 1: CONSTITUTIONAL AUDIT ===
    auditor = ConstitutionalAuditor()

    imprima("\n\n  {'='*80}")
    imprima("  PARTE 1: AUDITORIA CONSTITUCIONAL")
    imprima("  {'='*80}")

    stats = auditor.stats()
    imprima("\n  Padroes analisados: {stats['patterns_analyzed']}")
    imprima("  Satisfacao popular media: {stats['avg_public_satisfaction']}%")
    imprima("  Violacoes de direitos humanos: {stats['total_human_rights_violations']:,}")

    imprima("\n  Por veredito:")
    para cada (v, count) em ordene(stats["by_verdict"].items(), key=(x) -> -x[1]):
        imprima("    {v:<12} {count}")

    imprima("\n  Por prioridade:")
    para cada (p, count) em ordene(stats["by_priority"].items(), key=(x) -> x[1]):
        imprima("    {p:<12} {count}")

    // Critical reforms
    imprima("\n\n  === REFORMAS CRITICAS (prioridade maxima) ===\n")
    critical = auditor.critical_reforms()
    imprima("  {'Lei':<35} {'Veredito':<10} {'Satisf.':>8} {'Desejo Popular'}")
    imprima("  {'-'*85}")
    para cada c em critical:
        imprima("  {c['name']:<35} {c['verdict']:<10} {c['satisfaction']:>8} {c['public_desire'][:30]}")

    // By domain
    imprima("\n\n  === POR DOMINIO ===\n")
    domains = auditor.by_domain()
    para cada (domain, patterns) em ordene(domains.items()):
        imprima("\n  {domain.upper()}")
        para cada p em patterns:
            imprima("    [{p.verdict.value:>7}] [{p.priority.name:>8}] {p.name}")
            imprima("      Satisfacao: {p.public_satisfaction_pct}% | Republica: {p.republic_alternative[:50]}...")

    // Priority ranking
    imprima("\n\n  === ORDEM DE REVISAO (prioridade) ===\n")
    ranked = auditor.priority_ranking()
    para cada (i, p) em enumere(ranked, 1):
        imprima("  {i:>2}. [{p.priority.name:>8}] [{p.verdict.value:>7}] "
              "{p.domain.value:<18} {p.name}")

    // === PART 2: HEALTH ALLOCATION ===
    imprima("\n\n  {'='*80}")
    imprima("  PARTE 2: ALOCACAO DE RECURSOS DE SAUDE")
    imprima("  {'='*80}")

    allocator = HealthResourceAllocator()

    imprima("\n  === RECURSOS DISPONIVEIS (Clinica Sahel) ===\n")
    report = allocator.resource_report()
    para cada (rt, data) em report.items():
        imprima("  {rt:<15} {data['available']:>3}/{data['total']:>3} "
              "({data['utilization_pct']}% em uso)")

    // Patients
    imprima("\n\n  === PACIENTES CHEGANDO ===\n")
    patients = [
        Patient("P-001", "Amina", 28, "Parto complicado",
                TriageLevel.RED, [ResourceType.DOCTOR, ResourceType.BED,
                                  ResourceType.BLOOD],
                urgency_score = 95, is_pregnant=verdadeiro),
        Patient("P-002", "Joaozinho", 5, "Pneumonia severa",
                TriageLevel.RED, [ResourceType.DOCTOR, ResourceType.VENTILATOR],
                urgency_score = 90, is_child=verdadeiro),
        Patient("P-003", "Lars", 68, "Infarto",
                TriageLevel.RED, [ResourceType.DOCTOR, ResourceType.ICU],
                urgency_score = 92, is_elder=verdadeiro),
        Patient("P-004", "Kofi", 31, "Fratura exposta",
                TriageLevel.ORANGE, [ResourceType.DOCTOR, ResourceType.BED],
                urgency_score = 60),
        Patient("P-005", "Mei", 24, "Ansiedade severa",
                TriageLevel.YELLOW, [ResourceType.MENTAL_HEALTH],
                urgency_score = 40, wait_time_h=6),
        Patient("P-006", "Yara", 19, "Dengue",
                TriageLevel.YELLOW, [ResourceType.BED, ResourceType.MEDICINE],
                urgency_score = 45, wait_time_h=3),
    ]
    para cada p em patients:
        allocator.admit(p)

    // Allocate
    imprima("\n  === ALOCACAO POR PRIORIDADE ETICA ===\n")
    results = allocator.allocate()
    para cada r em results:
        tags = []
        if r["child"]: tags.append("CRIANCA")
        if r["pregnant"]: tags.append("GRAVIDA")
        if r["elder"]: tags.append("IDOSO")
        tag_str = tags ? " [{', '.join(tags)}]" : ""
        imprima("\n  {r['patient']} ({r['age']}a) - {r['condition']}{tag_str}")
        imprima("    Triagem: {r['triage']} | Score: {r['priority_score']}")
        imprima("    Alocado: {', '.join(r['allocated']) if r['allocated'] else 'nada'}")
        se r["missing"] entao:
            imprima("    FALTA: {', '.join(r['missing'])} -> {r['action']}")

    // Final resource state
    imprima("\n\n  === RECURSOS APOS ALOCACAO ===\n")
    report2 = allocator.resource_report()
    para cada (rt, data) em report2.items():
        bar = "#" * (data["utilization_pct"] // 5)
        flag = data["available"] == 0 ? " !!!" : ""
        imprima("  {rt:<15} {data['available']:>3}/{data['total']:>3} "
              "({data['utilization_pct']}%) {bar}{flag}")

    // Philosophy
    imprima("\n\n{'='*85}")
    imprima("  PRINCIPIOS")
    imprima("{'='*85}")
    imprima("""
  AUDITORIA CONSTITUCIONAL:
    24 padroes de leis de 50+ nacoes analisados.
    Satisfacao popular media: {stats['avg_public_satisfaction']}%.
    {tamanho(critical)} reformas CRITICAS identificadas.

    LEIS QUE PROTEGEM ELITE (ABOLIR):
      Financiamento de campanha (12% satisfacao)
      Bancos privados (25%)
      Sonegacao fiscal de ricos (8%)
      Saude como mercadoria (18%)
      Especulacao imobiliaria (15%)

    LEIS QUE PROTEGEM POVO (MANTER):
      Liberdade de expressao (62%)
      Saude universal (55%)
      Educacao gratuita (48%)
      Neutralidade da rede (52%)

    LEIS QUE FALTAM (CRIAR):
      Autonomia reprodutiva (aborto legal universal)
      Direitos da natureza
      Privacidade digital absoluta

  ALOCACAO DE SAUDE:
    PRIORIDADE = NECESSIDADE MEDICA + PONDERACAO ETICA
    NUNCA = dinheiro, status, influencia.

    Formula:
      base = urgency (0-100)
      x 1.3 se crianca (intergeracional)
      x 1.3 se gravida (2 vidas)
      x 1.2 se cronico sem tratamento
      + bonus por tempo de espera

    QUANDO FALTA RECURSO:
      1. Produz emergencialmente (FabLab: respirador em 4h)
      2. Transfere de outra nacao
      3. Algoritmo maximiza vidas salvas
      4. NUNCA: rico primeiro

    PREVENCAO > CURA:
      90% das doencas evitaveis.
      Checkup anual gratuito.
      Cuidados fisicos integrados.

  "A lei deve servir ao povo.
   Quando 8% satisfazem e 91% querem o oposto,
   a lei nao e lei. e opressao."
// )

```
