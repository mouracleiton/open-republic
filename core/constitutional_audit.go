// OpenRepublic -- Engenharia Reversa de Constituições Mundiais -- gerado de Portugol++
package openrepublic_engenharia_reversa_de_constitui_es_mundiais

import "fmt"

// !/usr/bin/env python3
//
OpenRepublic -- Engenharia Reversa de Constituições Mundiais
==============================================================
"Não vamos reinventar a roda. Vamos AUDITAR a roda que existe,
descobrir onde quebrou, && consertar."
Analisa padrões constitucionais de 50+ nações, cruza com dados de
satisfação popular (World Happiness Report, Gallup, Latinobarometro,
Edelman Trust Barometer), && identifica:
1. LEIS QUE FUNCIONAM (manter)
2. LEIS QUE FALHARAM (descartar)
3. LEIS QUE FALTAM (criar)
4. LEIS QUE PROTEGEM ELITE (remover)
5. LEIS QUE PROTEGEM POVO (manter/reforcar)
Depois seleciona por DOMINIO && ordena por PRIORIDADE DE REVISAO.
Author: OpenRepublic Team
//
// importa annotations de __future__
// importa math
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict de collections
type LawDomain int
const (
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
type LawVerdict int
const (
    KEEP = "manter"  // funciona, protege povo
    REFORM = "reformar"  // existe mas falhou
    CREATE = "criar"  // ! existe, precisa
    ABOLISH = "abolir"  // protege elite, prejudica povo
    REVERSE = "reverter"  // faz o oposto do que deveria
type Priority int
const (
    CRITICAL = 1 // vidas em risco AGORA
    URGENT = 2 // sofrimento massivo
    HIGH = 3 // desigualdade estrutural
    MODERATE = 4 // melhoria significativa
    LOW = 5 // refinamento
// decorador: @dataclass
type ConstitutionalPattern struct {
    // Um padrao constitucional encontrado em multiplas nacoes.
    pattern_id: texto
    domain: LawDomain
    name: texto
    description: texto
    // Onde existe
    countries_with := field(default_factory=list) // [texto]
    countries_without := field(default_factory=list) // [texto]
    // Dados de impacto
    public_satisfaction_pct := 0 // % da populacao satisfeita // float64
    inequality_index := 0 // 0=igual, 1=extremamente desigual // float64
    corruption_index := 0 // 0=limpo, 1=corrupto // float64
    human_rights_violations := 0 // int64
    // Analise
    verdict := LawVerdict.KEEP // LawVerdict
    priority := Priority.LOW // Priority
    republic_alternative := "" // string
    evidence := "" // string
    public_desire := ""  // o que a populacao QUER // string
// ============================================================================
// The Database -- 40 constitutional patterns from real nations
// ============================================================================
PATTERNS := [ // [ConstitutionalPattern]
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
        republic_alternative = "ZERO coleta de dados. OpenTransparency: o Estado && publico, o cidadao && privado.",
        evidence = "Snowden 2013: NSA coletava dados de bilhoes. Edelman: confianca em governo caiu 30%.",
        public_desire = "78% querem MAIS privacidade, ! menos (Pew Research)"),
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
        "Empresas && ricos financiam politicos -> lobby -> leis favoraveis.",
        countries_with = ["EUA (Citizens United)", "Brasil", "mayoria"],
        public_satisfaction_pct = 12,
        corruption_index = 0.8,
        verdict = LawVerdict.ABOLISH,
        priority = Priority.CRITICAL,
        republic_alternative = "ZERO dinheiro na politica. Sem campanha. Sorteio + eleicao direta.",
        evidence = "Princeton 2014: EUA && oligarquia, ! democracia. Leis seguem ricos, ! povo.",
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
        public_desire = "68% acham desigualdade && problema serio (Edelman)"),
    ConstitutionalPattern(
        "CP-007", LawDomain.ECONOMIC,
        "Bancos centrais privados",
        "Banco central controla moeda mas && influenciado por bancos privados.",
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
        public_desire = "83% acham que pagam muito imposto && recebem pouco (Datafolha)"),
    ConstitutionalPattern(
        "CP-009", LawDomain.TAXATION,
        "Sonegacao fiscal de ricos",
        "Ricos usam paraísos fiscais para ! pagar imposto.",
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
        republic_alternative = "Mantido && expandido. OpenHealth universal + OpenMedicine.",
        evidence = "Paises com saude universal tem maior expectativa de vida (OMS).",
        public_desire = "89% querem saude gratuita (Gallup global)"),
    ConstitutionalPattern(
        "CP-011", LawDomain.HEALTH,
        "Saude como mercadoria (privatizada)",
        "Saude && comprada. Quem tem dinheiro vive. Quem ! tem, morre.",
        countries_with = ["EUA"],
        public_satisfaction_pct = 18,
        inequality_index = 0.9,
        human_rights_violations = 45000, // mortes/ano por falta de seguro
        verdict = LawVerdict.ABOLISH,
        priority = Priority.CRITICAL,
        republic_alternative = "Saude && DIREITO. OpenHealth universal.",
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
        evidence = "Finlandia: educacao gratuita + melhor PISA do mundo. Mas metodo ainda && passivo.",
        public_desire = "76% querem educacao melhor, ! so gratuita (Pew)"),
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
        "Crianças ! podem trabalhar.",
        countries_with = ["Paises desenvolvidos"],
        countries_without = ["paises pobres (160M criancas trabalham)"],
        public_satisfaction_pct = 85,
        verdict = LawVerdict.KEEP,
        priority = Priority.LOW,
        republic_alternative = "Mantido. Crianca aprende FAZENDO (educacao), ! trabalhando.",
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
        republic_alternative = "Moradia && DIREITO. OpenCivilConstruction: casa em 2 dias, ZERO moeda.",
        evidence = "Brasil: 5.8 milhoes sem moradia apesar de direito constitucional. Lei existe, ! cumpre.",
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
        republic_alternative = "Restaurativo, ! punitivo. Reintegracao, ! encarceramento.",
        evidence = "EUA: 2.3 milhoes presos. 5x media mundial. Recidiva 76%. Prisao ! funciona.",
        public_desire = "65% querem foco em reabilitacao, ! prisao (Gallup)"),
    ConstitutionalPattern(
        "CP-018", LawDomain.CRIMINAL,
        "Guerra as Drogas (criminalizacao)",
        "Usuario de drogas && tratado como criminoso.",
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
        public_desire = "67% querem tratamento, ! prisao para usuarios (Pew)"),
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
        "Provedor ! pode discriminar trafego.",
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
        evidence = "Brasil: demarcacao lenta. 300+ terras ! finalizadas. Invasao por garimpo.",
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
type ConstitutionalAuditor struct {
    // Auditor constitucional da Republica.
    Pega padroes de 50+ nacoes, cruza com satisfacao popular,
    && produz relatorio de leis que precisam mudar.
    //
    func __init__(self) {
        self.patterns = PATTERNS
    funcao by_domain(self) retorna Dict[texto, [ConstitutionalPattern]]:
        cats = defaultdict(list)
        for _, p := range self.patterns {
            cats[p.domain.value].append(p)
        return dict(cats)
    funcao by_verdict(self) retorna Dict[texto, [texto]]:
        cats = defaultdict(list)
        for _, p := range self.patterns {
            cats[p.verdict.value].append(p.name)
        return dict(cats)
    func priority_ranking(self) [ConstitutionalPattern] {
        // Ordenar por prioridade de revisao (CRITICAL primeiro).
        return ordene(self.patterns, key=(p) -> (
            p.priority.value, -p.human_rights_violations))
    funcao critical_reforms(self) retorna List[{texto: qualquer}]:
        // Apenas reformas CRITICAL.
        return [{
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
    func stats(self) {texto: qualquer} {
        verdicts = defaultdict(inteiro)
        priorities = defaultdict(inteiro)
        for _, p := range self.patterns {
            verdicts[p.verdict.value] += 1
            priorities[p.priority.name] += 1
        avg_satisfaction = soma(p.public_satisfaction_pct para p em self.patterns) / len(self.patterns)
        total_violations = soma(p.human_rights_violations para p em self.patterns)
        return {
            "patterns_analyzed": len(self.patterns),
            "by_verdict": dict(verdicts),
            "by_priority": dict(priorities),
            "avg_public_satisfaction": arredonde(avg_satisfaction, 1),
            "total_human_rights_violations": total_violations,
        }
// ============================================================================
// OpenHealth Resource Allocation
// ============================================================================
type TriageLevel int
const (
    // Niveis de triagem medica.
    RED = "vermelho"  // emergencia (vida em risco AGORA)
    ORANGE = "laranja"  // urgente (1h)
    YELLOW = "amarelo"  // pouca urgencia (4h)
    GREEN = "verde"  // ! urgente (24h)
    BLUE = "azul"  // eletivo (semanas)
type ResourceType int
const (
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
type MedicalResource struct {
    // Um recurso medico disponivel.
    rtype: ResourceType
    total: inteiro
    available: inteiro
    in_use := 0 // int64
    // Nacao/clinica
    location := "" // string
    // Renovavel?
    renewable := true // bool
    restock_time_h := 24 // float64
// decorador: @dataclass
type Patient struct {
    // Um paciente precisando cuidado.
    patient_id: texto
    name: texto
    age: inteiro
    condition := "" // string
    triage := TriageLevel.GREEN // TriageLevel
    // Necessidades
    needs := field(default_factory=list) // [ResourceType]
    urgency_score := 0 // 0-100 (100 = morte iminente) // float64
    wait_time_h := 0 // float64
    // Priorizacao especial
    is_child := false // bool
    is_pregnant := false // bool
    is_elder := false // bool
    chronic := false // bool
type HealthResourceAllocator struct {
    // Sistema de alocacao de recursos de saude.
    PRINCIPIOS DA REPUBLICA:
    1. NINGUEM && recusado por falta de recurso
    -> Se falta, PRODUZ mais (OpenProduction)
    -> Se ! da, TRIAGEM etica (! financeira)
    2. TRIAGEM por NECESSIDADE MEDICA, ! por:
    -> Dinheiro (! existe)
    -> Status (! existe)
    -> Influencia (! existe)
    -> Idade sozinha (idoso ! && menos prioritario)
    3. ALGORITMO DE PRIORIZACAO:
    a. Vida em risco IMEDIATO = primeiro (sempre)
    b. Crianca/gravida = bonus ponderacao
    c. Cronico sem tratamento = piora rapido
    d. Eletivo (cirurgia plastica !-reparadora) = ultimo
    4. QUANDO FALTA (dilema etico):
    a. Produz mais imediatamente (FabLab: respirador em 4h)
    b. Transfere de outra nacao (Republica federada)
    c. Algoritmo de maximizar vidas salvas
    d. NUNCA: rico primeiro, pobre depois
    &&. NUNCA: influente primeiro, anonimo depois
    5. PREVENCAO > CURA:
    -> 90% das doencas sao evitaveis
    -> Investir em prevencao && mais barato (zero custo)
    -> OpenHealth: checkup anual gratuito para todos
    6. AUTOMACAO:
    -> IA faz triagem inicial (com supervisao medica)
    -> IA ! decide quem vive/morre (humano decide)
    -> IA detecta padroes epidemiologicos precoces
    //
    func __init__(self) {
        self.resources: {ResourceType: MedicalResource} = {}
        self.patients: [Patient] = []
        self.allocations: [Dict] = []
        self._init_resources()
    func _init_resources(self) {
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
        para rtype, total, avail in resources: {
            self.resources[rtype] = MedicalResource(
                rtype = rtype, total=total, available=avail,
                in_use = total - avail, location="Sahel")
    func admit(self, patient: Patient) {
        self.patients.append(patient)
    funcao allocate(self) retorna List[{texto: qualquer}]:
        // Alocar recursos por prioridade etica.
        // Ordenar por urgencia
        scored = []
        for _, p := range self.patients {
            score = self._priority_score(p)
            scored.append((score, p))
        scored.sort(key=(x) -> -x[0])
        results = []
        para cada (score, p) em scored: {
            allocation = self._try_allocate(p, score)
            results.append(allocation)
        return results
    // decorador: @staticmethod
    func _priority_score(patient: Patient) float64 {
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
        if patient.is_child {
            base = base * 1.3
        if patient.is_pregnant {
            base = base * 1.3
        if patient.chronic && patient.wait_time_h > 12 {
            base = base * 1.2
        // Bonus por espera
        base = base + minimo(20, patient.wait_time_h)
        return minimo(200, base)
    funcao _try_allocate(self, patient: Patient,
                    score: flutuante) -> {texto: qualquer}:
        // Tentar alocar recursos para um paciente.
        allocated = []
        missing = []
        for _, need := range patient.needs {
            res = self.resources.get(need)
            if res && res.available > 0 {
                res.available -= 1
                res.in_use += 1
                allocated.append(need.value)
            } else {
                missing.append(need.value)
        // Se falta recurso: acionar producao emergencial
        action = "allocated"
        if missing {
            action = "PRODUZIR EMERGENCIALMENTE"
            // FabLab: respirador em 4h, medicine em 2h
        return {
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
    func resource_report(self) {texto: qualquer} {
        // Relatorio de recursos.
        return {
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
if __name__ == "__main__" {
    fmt.Println("=" * 85)
    fmt.Println("  AUDITORIA CONSTITUCIONAL + ALOCACAO DE SAUDE")
    fmt.Println("  'Engenharia reversa das leis que governam a humanidade.'")
    fmt.Println("=" * 85)
    // === PART 1: CONSTITUTIONAL AUDIT ===
    auditor = ConstitutionalAuditor()
    fmt.Println("\n\n  {'='*80}")
    fmt.Println("  PARTE 1: AUDITORIA CONSTITUCIONAL")
    fmt.Println("  {'='*80}")
    stats = auditor.stats()
    fmt.Println("\n  Padroes analisados: {stats['patterns_analyzed']}")
    fmt.Println("  Satisfacao popular media: {stats['avg_public_satisfaction']}%")
    fmt.Println("  Violacoes de direitos humanos: {stats['total_human_rights_violations']:,}")
    fmt.Println("\n  Por veredito:")
    para cada (v, count) em ordene(stats["by_verdict"].items(), key=(x) -> -x[1]): {
        fmt.Println("    {v:<12} {count}")
    fmt.Println("\n  Por prioridade:")
    para cada (p, count) em ordene(stats["by_priority"].items(), key=(x) -> x[1]): {
        fmt.Println("    {p:<12} {count}")
    // Critical reforms
    fmt.Println("\n\n  === REFORMAS CRITICAS (prioridade maxima) ===\n")
    critical = auditor.critical_reforms()
    fmt.Println("  {'Lei':<35} {'Veredito':<10} {'Satisf.':>8} {'Desejo Popular'}")
    fmt.Println("  {'-'*85}")
    for _, c := range critical {
        fmt.Println("  {c['name']:<35} {c['verdict']:<10} {c['satisfaction']:>8} {c['public_desire'][:30]}")
    // By domain
    fmt.Println("\n\n  === POR DOMINIO ===\n")
    domains = auditor.by_domain()
    para cada (domain, patterns) em ordene(domains.items()): {
        fmt.Println("\n  {domain.upper()}")
        for _, p := range patterns {
            fmt.Println("    [{p.verdict.value:>7}] [{p.priority.name:>8}] {p.name}")
            fmt.Println("      Satisfacao: {p.public_satisfaction_pct}% | Republica: {p.republic_alternative[:50]}...")
    // Priority ranking
    fmt.Println("\n\n  === ORDEM DE REVISAO (prioridade) ===\n")
    ranked = auditor.priority_ranking()
    para cada (i, p) em enumere(ranked, 1): {
        fmt.Println("  {i:>2}. [{p.priority.name:>8}] [{p.verdict.value:>7}] "
            "{p.domain.value:<18} {p.name}")
    // === PART 2: HEALTH ALLOCATION ===
    fmt.Println("\n\n  {'='*80}")
    fmt.Println("  PARTE 2: ALOCACAO DE RECURSOS DE SAUDE")
    fmt.Println("  {'='*80}")
    allocator = HealthResourceAllocator()
    fmt.Println("\n  === RECURSOS DISPONIVEIS (Clinica Sahel) ===\n")
    report = allocator.resource_report()
    para cada (rt, data) em report.items(): {
        fmt.Println("  {rt:<15} {data['available']:>3}/{data['total']:>3} "
            "({data['utilization_pct']}% em uso)")
    // Patients
    fmt.Println("\n\n  === PACIENTES CHEGANDO ===\n")
    patients = [
        Patient("P-001", "Amina", 28, "Parto complicado",
                TriageLevel.RED, [ResourceType.DOCTOR, ResourceType.BED,
                                ResourceType.BLOOD],
                urgency_score = 95, is_pregnant=true),
        Patient("P-002", "Joaozinho", 5, "Pneumonia severa",
                TriageLevel.RED, [ResourceType.DOCTOR, ResourceType.VENTILATOR],
                urgency_score = 90, is_child=true),
        Patient("P-003", "Lars", 68, "Infarto",
                TriageLevel.RED, [ResourceType.DOCTOR, ResourceType.ICU],
                urgency_score = 92, is_elder=true),
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
    for _, p := range patients {
        allocator.admit(p)
    // Allocate
    fmt.Println("\n  === ALOCACAO POR PRIORIDADE ETICA ===\n")
    results = allocator.allocate()
    for _, r := range results {
        tags = []
        if r["child"]: tags.append("CRIANCA")
        if r["pregnant"]: tags.append("GRAVIDA")
        if r["elder"]: tags.append("IDOSO")
        tag_str = tags ? " [{', '.join(tags)}]" : ""
        fmt.Println("\n  {r['patient']} ({r['age']}a) - {r['condition']}{tag_str}")
        fmt.Println("    Triagem: {r['triage']} | Score: {r['priority_score']}")
        fmt.Println("    Alocado: {', '.join(r['allocated']) if r['allocated'] else 'nada'}")
        if r["missing"] {
            fmt.Println("    FALTA: {', '.join(r['missing'])} -> {r['action']}")
    // Final resource state
    fmt.Println("\n\n  === RECURSOS APOS ALOCACAO ===\n")
    report2 = allocator.resource_report()
    para cada (rt, data) em report2.items(): {
        bar = "#" * (data["utilization_pct"] // 5)
        flag = data["available"] == 0 ? " !!!" : ""
        fmt.Println("  {rt:<15} {data['available']:>3}/{data['total']:>3} "
            "({data['utilization_pct']}%) {bar}{flag}")
    // Philosophy
    fmt.Println("\n\n{'='*85}")
    fmt.Println("  PRINCIPIOS")
    fmt.Println("{'='*85}")
    fmt.Println("""
AUDITORIA CONSTITUCIONAL:
    24 padroes de leis de 50+ nacoes analisados.
    Satisfacao popular media: {stats['avg_public_satisfaction']}%.
    {len(critical)} reformas CRITICAS identificadas.
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
Quando 8% satisfazem && 91% querem o oposto,
a lei ! && lei. && opressao."
// )
