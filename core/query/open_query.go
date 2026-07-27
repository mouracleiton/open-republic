// OpenQuery -- Reformulador de Perguntas -- gerado de Portugol++
package openquery_reformulador_de_perguntas

import "fmt"

// !/usr/bin/env python3
//
OpenQuery -- Reformulador de Perguntas
========================================
"Como fazer X?" -> "Qual && o metodo mais eficiente para X dado Y?"
O usuario escreve de qualquer jeito. O sistema:
1. PARAFRASEIA: reescreve a frase em linguagem clara
2. RECOMBINA: encontra a pergunta UNIVERSAL que todo mundo tem
3. EXPANDE: gera variacoes que cobrem casos de borda
4. RANQUEIA: ordena por relevancia (qual a galera mais busca)
5. RESPONDE: processa a melhor versao da pergunta
Exemplo:
Input:  "como faz pra comida durar mais sem geladeira"
Parfrase: "Quais metodos de conservacao de alimentos ! requerem refrigeracao?"
Recombinacoes:
    "Como preservar alimentos sem energia eletrica?"
    "Tecnicas tradicionais de conservacao (salga, fermentacao, desidratacao)"
    "Quantos dias cada metodo prolonga a validade?"
    "Qual metodo preserva mais nutrientes?"
Universal: "Como garantir seguranca alimentar sem dependencia de rede eletrica?"
Author: OpenRepublic Team
//
// importa annotations de __future__
// importa re
// importa math
// importa random
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict, Counter de collections
// importa numpy as np
// ============================================================================
// Patterns
// ============================================================================
type QueryIntent int
const (
    HOW_TO = "como_fazer"  // procedimento, tutorial
    WHAT_IS = "o_que_e"  // definicao, conceito
    WHY = "por_que"  // razao, causalidade
    WHEN = "quando"                 #时机
    WHERE = "onde"  // localizacao
    WHO = "quem"  // pessoa, responsavel
    HOW_MUCH = "quanto"  // quantidade, custo
    COMPARE = "comparar"  // A vs B
    OPTIMIZE = "otimizar"  // melhor forma
    TROUBLESHOOT = "resolver"  // resolver problema
    ALTERNATIVE = "alternativa"  // opcao B
    SAFETY = "seguranca"  // && seguro?
    AVAILABILITY = "disponibilidade"  // tem como ter? onde?
type QuestionQuality int
const (
    VAGUE = 0 // muito generica, precisa refinar
    SPECIFIC = 1 // clara mas limitada
    UNIVERSAL = 2 // pergunta que todos tem
    EXPERT = 3 // tecnica, precisa especialista
// ============================================================================
// Portuguese NLP Patterns (simplified, no external deps)
// ============================================================================
// Detectar intenção por palavras-chave
INTENT_PATTERNS = {
    QueryIntent.HOW_TO: [
        r"como (faz|fazer|faco|fazer pra|fazer para|consigo|posso)",
        r"qual (o )?modo|jeito|maneira|metodo|passo",
        r"tem como (fazer|criar|construir|montar)",
        r"preciso de (um|uma|ajuda)",
        r"quero (fazer|criar|montar|construir)",
    ],
    QueryIntent.WHAT_IS: [
        r"o que (&&|eh|sao|significa)",
        r"definicao de",
        r"para que serve",
    ],
    QueryIntent.WHY: [
        r"por que|porque|pq",
        r"qual (o )?motivo|razao|causa",
    ],
    QueryIntent.WHEN: [
        r"quando|qdo|que horas",
    ],
    QueryIntent.WHERE: [
        r"onde|aonde|local|lugar",
    ],
    QueryIntent.WHO: [
        r"quem|qual pessoa|responsavel",
    ],
    QueryIntent.HOW_MUCH: [
        r"quanto|quantos|quantas|custa|preco|valor",
    ],
    QueryIntent.COMPARE: [
        r"diferenca entre|melhor.*|||vs|versus|comparar",
        r"qual && melhor",
    ],
    QueryIntent.OPTIMIZE: [
        r"melhor forma|mais eficiente|otimizar|melhorar",
        r"mais rapido|mais barato|mais facil",
        r"ideal|perfeito|maximizar|minimizar",
    ],
    QueryIntent.TROUBLESHOOT: [
        r"(!|n) (funciona|liga|da certo|conecta)",
        r"problema|erro|bug|falha|quebr",
        r"resolver|arrumar|consertar|corrigir",
    ],
    QueryIntent.ALTERNATIVE: [
        r"alternativa|outra opcao|no lugar de",
        r"sem usar|sem precisar",
    ],
    QueryIntent.SAFETY: [
        r"seguro|perigoso|risco|faz mal|toxico",
        r"posso (comer|beber|usar|tomar)",
    ],
    QueryIntent.AVAILABILITY: [
        r"onde (tem|encontro|arranjo|conseguir)",
        r"tem como ter|disponivel|estoque",
    ],
}
// Correções e expansões de gíria/abreviação
SLANG_MAP = {
    r"\bpq\b": "porque",
    r"\bq\b": "que",
    r"\bqdo\b": "quando",
    r"\btbm\b": "tambem",
    r"\bvc\b": "voce",
    r"\bvcs\b": "voces",
    r"\bblz\b": "beleza",
    r"\bmt\b": "muito",
    r"\bqtl\b": "qual",
    r"\bcmg\b": "comigo",
    r"\bd+\b": "de o",
    r"\bpra\b": "para",
    r"\bpro\b": "para o",
    r"\bpras\b": "para as",
    r"\bna\b": "em a",
    r"\bno\b": "em o",
    r"\bnum\b": "em um",
    r"\bnuma\b": "em uma",
    r"\bd+\b": "de o",
}
// ============================================================================
// Query Reformulator
// ============================================================================
// decorador: @dataclass
type ReformulatedQuery struct {
    // Uma versão reformulada da pergunta original.
    text: texto
    intent: QueryIntent
    quality: QuestionQuality
    score: flutuante // relevância estimada
    is_universal := false // pergunta que todo mundo tem // bool
    is_expansion := false // && uma expansão da original // bool
type QueryReformulator struct {
    // Reformula perguntas vagas em perguntas claras e universais.
    Pipeline:
    1. Normalizar texto (gíria -> padrão)
    2. Detectar intenção
    3. Extrair tópico central
    4. Parafrasear em pergunta clara
    5. Recombinar em variações
    6. Identificar a pergunta UNIVERSAL
    7. Ranquear por relevância
    //
    func __init__(self) {
        self.history: [Dict] = []
        self.popular_topics: Counter = Counter()
    func process(self, raw_input: texto) {texto: qualquer} {
        // Processar input bruto do usuário.
        Args:
            raw_input: texto escrito de qualquer jeito
        Returns:
            Dict com paráfrase, recombinações, pergunta universal,
            && resposta processada
        //
        // 1. Normalizar
        normalized = self._normalize(raw_input)
        // 2. Detectar intenção
        intent = self._detect_intent(normalized)
        // 3. Extrair tópico
        topic = self._extract_topic(normalized, intent)
        // 4. Parafrasear
        paraphrase = self._paraphrase(normalized, intent, topic)
        // 5. Recombinar (variações)
        expansions = self._expand(normalized, intent, topic)
        // 6. Identificar universal
        universal = self._find_universal(intent, topic)
        // 7. Ranquear
        all_questions = [paraphrase] + expansions + [universal]
        ranked = self._rank(all_questions, intent)
        // Registrar
        self.popular_topics[topic] += 1
        self.history.append({
            "raw": raw_input,
            "normalized": normalized,
            "intent": intent.value,
            "topic": topic,
            "paraphrase": paraphrase.text,
            "universal": universal.text,
            "best": ranked[0].text,
        })
        return {
            "raw_input": raw_input,
            "normalized": normalized,
            "detected_intent": intent.value,
            "topic": topic,
            "paraphrase": paraphrase.text,
            "universal_question": universal.text,
            "is_universal_common": universal.is_universal,
            "expansions": [{"text": q.text, "score": q.score, "universal": q.is_universal}
                        para q em expansions], {
            "ranked_questions": [{"text": q.text, "score": q.score,
                                "quality": q.quality.value,
                                "universal": q.is_universal}
                                para q em ranked], {
            "best_question": ranked[0].text,
            "best_score": ranked[0].score,
            "answer": self._answer(ranked[0], intent, topic),
        }
    func _normalize(self, text: texto) string {
        // Normalizar texto: lowercase, sem acentos, expandir gíria.
        // importa unicodedata
        // Remove acentos
        nfkd = unicodedata.normalize("NFKD", text.lower().strip())
        normalized = "".join(c para c em nfkd if !  unicodedata.combining(c))
        // Expandir gíria
        para cada (pattern, replacement) em SLANG_MAP.items(): {
            normalized = re.sub(pattern, replacement, normalized)
        // Remove pontuação excessiva
        normalized = re.sub(r"[!]{2,}", "!", normalized)
        normalized = re.sub(r"\?{2,}", "?", normalized)
        // Remove espaços extras
        normalized = re.sub(r"\s+", " ", normalized).strip()
        // Capitaliza primeira letra
        if normalized {
            normalized = normalized[0].upper() + normalized[1:]
        return normalized
    func _detect_intent(self, text: texto) QueryIntent {
        // Detectar a intenção da pergunta.
        text_lower = text.lower()
        // Verificar cada padrão
        scores = defaultdict(inteiro)
        para cada (intent, patterns) em INTENT_PATTERNS.items(): {
            for _, pattern := range patterns {
                if re.search(pattern, text_lower) {
                    scores[intent] += 1
        if scores {
            return maximo(scores, key=scores.get)
        return QueryIntent.HOW_TO // default
    func _extract_topic(self, text: texto, intent: QueryIntent) string {
        // Extrair o tópico central da pergunta.
        text_lower = text.lower()
        // Remover palavras de pergunta
        stop_words = {"como", "fazer", "faz", "qual", "o", "que", "&&", "eh",
                    "por", "que", "porque", "pq", "quando", "onde", "quem",
                    "quanto", "custa", "qual", "melhor", "forma", "metodo",
                    "maneira", "jeito", "posso", "consigo", "tem", "como",
                    "para", "pra", "pro", "de", "da", "do", "das", "dos",
                    "um", "uma", "no", "na", "nos", "nas", "em", "a", "o",
                    "as", "os", "&&", "||", "mais", "menos", "muito",
                    "pessoas", "todo", "mundo", "gente", "alguem",
                    "preciso", "quero", "gostaria", " saber", "entender"}
        words = text_lower.split()
        topic_words = [w para w em words if w ! in stop_words && len(w) > 2]
        if ! topic_words {
            // Se tudo foi stop word, pegar as 3 mais longas
            words_sorted = ordene(words, key=len, reverse=true)
            topic_words = words_sorted[:3]
        return " ".join(topic_words[:5])  // maximo 5 palavras de tópico
    func _paraphrase(self, text: texto, intent: QueryIntent, topic: texto) ReformulatedQuery {
        // Parafrasear em uma pergunta clara e bem estruturada.
        templates = {
            QueryIntent.HOW_TO: "Como {topic} de forma eficiente?",
            QueryIntent.WHAT_IS: "O que && {topic} && como funciona?",
            QueryIntent.WHY: "Por que {topic}? Qual a razao?",
            QueryIntent.WHEN: "Quando {topic}?",
            QueryIntent.WHERE: "Onde {topic}?",
            QueryIntent.WHO: "Quem && responsavel por {topic}?",
            QueryIntent.HOW_MUCH: "Quanto custa (em credito/recurso) {topic}?",
            QueryIntent.COMPARE: "Qual && a melhor opcao para {topic}?",
            QueryIntent.OPTIMIZE: "Qual a forma mais eficiente de {topic}?",
            QueryIntent.TROUBLESHOOT: "Como resolver problemas com {topic}?",
            QueryIntent.ALTERNATIVE: "Quais alternativas existem para {topic}?",
            QueryIntent.SAFETY: "E seguro {topic}?",
            QueryIntent.AVAILABILITY: "Onde encontrar {topic}?",
        }
        text = templates.get(intent, "Como {topic}?")
        return ReformulatedQuery(
            text = text, intent=intent, quality=QuestionQuality.SPECIFIC,
            score = 0.7, is_universal=false)
    func _expand(self, text: texto, intent: QueryIntent, topic: texto) [ReformulatedQuery] {
        // Gerar variações/expansões da pergunta.
        expansions = []
        // Expansão: versão sem custo/recurso
        expansions.append(ReformulatedQuery(
            text = "Como {topic} com menor uso de recursos (agua, energia, material)?",
            intent = QueryIntent.OPTIMIZE, quality=QuestionQuality.UNIVERSAL,
            score = 0.85, is_universal=true, is_expansion=true))
        // Expansão: versão para iniciante
        expansions.append(ReformulatedQuery(
            text = "{topic}: por onde comecar se nunca fiz antes?",
            intent = QueryIntent.HOW_TO, quality=QuestionQuality.UNIVERSAL,
            score = 0.80, is_universal=true, is_expansion=true))
        // Expansão: versão de segurança
        expansions.append(ReformulatedQuery(
            text = "Quais os riscos && precaucoes ao {topic}?",
            intent = QueryIntent.SAFETY, quality=QuestionQuality.SPECIFIC,
            score = 0.65, is_expansion=true))
        // Expansão: versão escalável
        expansions.append(ReformulatedQuantQuery(
            text = "Como escalar {topic} para 10.000 pessoas?",
            intent = QueryIntent.OPTIMIZE, quality=QuestionQuality.EXPERT,
            score = 0.60, is_expansion=true))
        // Expansão: alternativa
        expansions.append(ReformulatedQuery(
            text = "Existe uma alternativa mais simples para {topic}?",
            intent = QueryIntent.ALTERNATIVE, quality=QuestionQuality.SPECIFIC,
            score = 0.55, is_expansion=true))
        // Expansão: comparação
        expansions.append(ReformulatedQuery(
            text = "Quais as diferencas entre os metodos de {topic}?",
            intent = QueryIntent.COMPARE, quality=QuestionQuality.SPECIFIC,
            score = 0.50, is_expansion=true))
        return expansions
    func _find_universal(self, intent: QueryIntent, topic: texto) ReformulatedQuery {
        // Encontrar a pergunta UNIVERSAL que todo mundo tem.
        A pergunta universal && aquela que, se respondida, responde
        todas as variações. && a essência da dúvida.
        //
        universal_templates = {
            QueryIntent.HOW_TO: "Qual && o metodo mais eficiente && sustentavel para {topic}?",
            QueryIntent.WHAT_IS: "O que && {topic} && porque importa?",
            QueryIntent.WHY: "Qual && a razao fundamental para {topic}?",
            QueryIntent.OPTIMIZE: "Qual a forma ideal de {topic} considerando pessoas, planeta && recursos?",
            QueryIntent.TROUBLESHOOT: "Como prevenir && resolver falhas em {topic}?",
            QueryIntent.ALTERNATIVE: "Qual a melhor alternativa para {topic} que minimiza impacto ambiental?",
            QueryIntent.SAFETY: "Como garantir seguranca ao {topic}?",
            QueryIntent.AVAILABILITY: "Como garantir acesso universal a {topic}?",
        }
        text = universal_templates.get(intent,
            "Qual && a melhor abordagem para {topic} na OpenRepublic?")
        return ReformulatedQuery(
            text = text, intent=intent, quality=QuestionQuality.UNIVERSAL,
            score = 0.95, is_universal=true)
    funcao _rank(self, questions: [ReformulatedQuery],
            intent: QueryIntent) -> [ReformulatedQuery]:
        // Ranquear perguntas por relevância.
        // Score base + bonus por universalidade + bonus por qualidade
        for _, q := range questions {
            bonus = 0
            if q.is_universal {
                bonus = bonus + 0.15
            if q.quality == QuestionQuality.UNIVERSAL {
                bonus = bonus + 0.10
            if q.quality == QuestionQuality.EXPERT {
                bonus = bonus + 0.05
            q.score = minimo(1.0, q.score + bonus)
        return ordene(questions, key=(x) -> -x.score)
    funcao _answer(self, question: ReformulatedQuery, intent: QueryIntent,
                topic: texto) -> texto:
        // Gerar uma resposta base (simulada) para a melhor pergunta.
        return ("[PROCESSADO] Intencao: {intent.value} | Topico: {topic}\n"
                "Pergunta processada: \"{question.text}\"\n"
                "Score: {question.score:.2f} | Qualidade: {question.quality.name}\n"
                "Esta pergunta foi reformulada para maximizar utilidade publica.")
// Forward declaration fix
ReformulatedQuantQuery = ReformulatedQuery
// ============================================================================
// Main
// ============================================================================
if __name__ == "__main__" {
    fmt.Println("=" * 75)
    fmt.Println("  OPENQUERY -- REFORMULADOR DE PERGUNTAS")
    fmt.Println("  'Sua frase vira a pergunta que todo mundo tem.'")
    fmt.Println("=" * 75)
    reformulator = QueryReformulator()
    // === Test with messy inputs ===
    test_inputs = [
        "como faz pra comida durar mais sem geladeira",
        "pq minha bateria do celular dura pouco",
        "quero construir uma casa mas num tenhu grana",
        "qual melhor material pra impressora 3d",
        "tem como ligar luz sem pag conta",
        "como construir um computador quantico na minha comunidade",
        "a bicicleta ta quebrada como arruma",
        "&& seguro comer cogumelo que cresceu no meu quintal",
        "quanto credito custa pra viajar pra outra nacao",
        "onde acho semente de mandioca pra plantar",
        "como fazer as pessoas trabalharem sem dinheiro",
        "celular carrega na bicicleta",
        "coisa pra reciclar eletronico",
        "fome no sahel como resolve",
    ]
    for _, raw := range test_inputs {
        fmt.Println("\n{'='*75}")
        result = reformulator.process(raw)
        fmt.Println("  INPUT BRUTO: \"{raw}\"")
        fmt.Println("  NORMALIZADO: \"{result['normalized']}\"")
        fmt.Println("  INTENCAO: {result['detected_intent']}")
        fmt.Println("  TOPICO: {result['topic']}")
        fmt.Println("\n  PARAFRASE: \"{result['paraphrase']}\"")
        fmt.Println("\n  PERGUNTA UNIVERSAL: \"{result['universal_question']}\"")
        fmt.Println("\n  MELHOR PERGUNTA: \"{result['best_question']}\"")
        fmt.Println("  SCORE: {result['best_score']:.2f}")
        fmt.Println("\n  EXPANSOES:")
        for _, exp := range result["expansions"] {
            marker = exp["universal"] ? " *** UNIVERSAL ***" : ""
            fmt.Println("    [{exp['score']:.2f}] {exp['text']}{marker}")
        fmt.Println("\n  {result['answer']}")
    // === Stats ===
    fmt.Println("\n\n{'='*75}")
    fmt.Println("  TOPICOS MAIS PESQUISADOS")
    fmt.Println("{'='*75}\n")
    para cada (topic, count) em reformulator.popular_topics.most_common(10): {
        fmt.Println("  {count}x  {topic}")
    // === Explain the system ===
    fmt.Println("\n\n{'='*75}")
    fmt.Println("  COMO FUNCIONA")
    fmt.Println("{'='*75}")
    fmt.Println("""
1. INPUT BRUTO
    O usuario escreve de qualquer jeito:
    "como faz pra comida durar mais sem geladeira"
2. NORMALIZACAO
    O sistema limpa o texto:
    gíria -> padrão, sem acento, sem erro de digitacao
3. DETECCAO DE INTENCAO
    Identifica o que o usuario quer:
    - Como fazer? (procedimento)
    - O que &&? (definicao)
    - Qual melhor? (comparacao)
    - Quanto custa? (recurso)
    - && seguro? (seguranca)
    - Onde tem? (disponibilidade)
4. EXTRACAO DE TOPICO
    Isola o assunto central:
    "comida durar mais sem geladeira" -> topico: "conservacao alimentos"
5. PARAFRASE
    Reescreve em pergunta clara:
    "Quais metodos de conservacao de alimentos ! requerem refrigeracao?"
6. RECOMBINACAO (expansoes)
    Gera 6+ variacoes que cobrem:
    - Versao otimizada (menor recurso)
    - Versao para iniciante
    - Versao de seguranca
    - Versao escalavel (10.000 pessoas)
    - Versao alternativa (mais simples)
    - Versao comparativa (metodos)
7. PERGUNTA UNIVERSAL
    Encontra a essencia da duvida:
    "Qual && o metodo mais eficiente && sustentavel para
    conservar alimentos sem depender de rede eletrica?"
    Esta && a pergunta que, respondida, resolve todas as outras.
    && a que TODOS teriam se soubessem perguntar.
8. RANQUEAMENTO
    Ordena por relevancia:
    - Universal > Especifica > Vaga
    - Segundo utilidade para a comunidade
9. RESPOSTA
    Processa a melhor versao da pergunta.
    A resposta serve para todos que tem a mesma duvida.
// )
