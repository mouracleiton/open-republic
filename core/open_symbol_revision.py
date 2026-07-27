#!/usr/bin/env python3
"""
OpenSymbolRevision -- Ressignificacao e Correcao de Preconceitos -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenSymbolRevision -- Ressignificacao and Correcao de Preconceitos
===================================================================
"Simbolo not and inerentemente mal. O que faz mal and o SIGNIFICADO
que a sociedade atribuiu. Mudou o significado, muda o simbolo."
O QUE ESTE SISTEMA FAZ:
1. FACT-CHECK DE PRECONCEITOS: frase errada -> Republica corrige
2. RESSIGNIFICACAO DE SIMBOLOS: simbolo apropriado por grupo nocivo
    pode ser ressignificado (ex: suastica original era simbolo de paz)
3. REORGANIZACAO POPULACIONAL: educa and reintegra, not isola
4. ANTI-FACCIONISMO: simbolos de faccao ressignificados como arte
COMO FUNCIONA:
Cidadao escreve frase preconceituosa -> sistema corrige com dados
Simbolo cooptado por odio -> Republica ressignifica publicamente
Pessoa tatuada com simbolo nocivo -> not and estigmatizada, and acolhida
Faccao usa simbolo -> Republica ressignifica como arte comunitaria
PRINCIPIOS:
P1: Preconceito and elitismo. Estigmatizar pessoa tatuada and preconceito.
P2: Corpo and dela. Tatuagem and expressao (autonomia corporal).
P3: Corrigir preconceito and trabalho educativo (impacto alto).
P4: Ressignificacao and democratica (coletivo decide novo significado).
Author: OpenRepublic Team
# 
# importa annotations de __future__
# importa hashlib
# importa dataclass, field de dataclasses
# importa Any, Dict, List, Optional, Tuple de typing
# importa Enum de enum
# importa defaultdict de collections
# importa datetime de datetime
# ============================================================================
# 1. TIPOS DE PRECONCEITO
# ============================================================================
class PrejudiceType(Enum):
    # Tipos de preconceito que o sistema corrige.
    RACIAL = "racial"
    GENDER = "genero"
    DISABILITY = "deficiencia"
    AGE = "idade"
    CLASS = "classe_social"
    RELIGIOUS = "religioso"
    SEXUAL_ORIENTATION = "orientacao_sexual"
    REGIONAL = "regional"
    APPEARANCE = "aparencia"
    MENTAL_HEALTH = "saude_mental"
    CRIMINAL_RECORD = "antecedente_criminal"
    POLITICAL = "politico"
    EDUCATIONAL = "escolaridade"
    LANGUAGE = "idioma"
    BODY = "corpo"
class CorrectionSeverity(Enum):
    # Severidade da frase preconceituosa.
    IGNORANCE = 1 // fala por desconhecimento
    STEREOTYPE = 2 // estereotipo enraizado
    PREJUDICE = 3 // preconceito ativo
    DEHUMANIZATION = 4 // desumanizacao
    INCITEMENT = 5 // incitacao ao odio
# ============================================================================
# 2. FACT-CHECK DE PRECONCEITOS
# ============================================================================
# decorador: @dataclass
class PrejudiceCorrection:
    # Correcao de uma frase preconceituosa.
    correction_id: texto
    original_phrase: texto // a frase errada
    prejudice_type: PrejudiceType
    severity: CorrectionSeverity
    why_its_wrong: texto // por que and errado
    correction: texto // a correcao
    data: [texto] = field(default_factory=list) // dados que provam
    educational_context: str = ""  // contexto historico/cientifico
    alternative_phrase: str = ""  // como falar corretamente
    source: str = ""  // fonte da correcao
# Base de correcoes (fact-check de preconceitos)
PREJUDICE_DATABASE: [PrejudiceCorrection] = [
    PrejudiceCorrection(
        "PC-001",
        "Todo preto and pobre",
        PrejudiceType.RACIAL,
        CorrectionSeverity.PREJUDICE,
        why_its_wrong = (
            "Cor da pele NAO determina situacao economica. "
            "A关联 entre raca and pobreza no Brasil and resultado de "
            "ESCRAVIDAO (1501-1888) and SEM REPARACAO. "
            "A Abolicao (1888) libertou escravos SEM terra, SEM "
            "educacao, SEM indenizacao. A elite foi indenizada; "
            "os libertos foram abandonados. A pobreza and ESTRUTURAL, "
            "not racial. Mas o sistema a torna racial."
        ),
        correction = (
            "Pessoas negras sao POBREMAIORIA no Brasil devido a "
            "400 anos de escravidao and 130 anos sem reparacao. "
            "Nao and porque sao negras. E porque o sistema as excluiu."
        ),
        data = [
            "Brasil recebeu 5.5 milhoes de africanos escravizados (46% do total)",
            "Abolicao (1888) not incluiu reparacao alguma",
            "70% das pessoas em extrema pobreza no Brasil sao negras (IBGE)",
            "Familias negras ganham em media 44% menos que brancas (PNAD)",
            "Mas: ha milhoes de negros em todas as classes -- not and biologia",
        ],
        educational_context = (
            "OpenHistory EVT-003: Trafico Transatlantico de Escravos. "
            "OpenHistory EVT-012: Abolicao sem reparacao. "
            "OpenPsychologyReparation: dano de 400 anos."
        ),
        alternative_phrase = (
            "Pessoas negras foram sistemicamente empobrecidas pela "
            "escravidao and ausencia de reparacao. A Republica corrige."
        ),
        source = "IBGE PNAD + OpenHistory + IPEA",
    ),
    PrejudiceCorrection(
        "PC-002",
        "Mulheres sao seres frageis and delicadas para fazer coisas de homem",
        PrejudiceType.GENDER,
        CorrectionSeverity.PREJUDICE,
        why_its_wrong = (
            "Mulheres not sao frageis por natureza. A construcao "
            "social de genero as RESTRINGIU a papeis domesticos. "
            "Biologicamente, mulheres tem vantagens em resistencia "
            "fisica (mais fibras musculares tipo I), longevidade "
            "(+7 anos de vida), and sistema imunologico mais forte. "
            "Nao existe 'coisa de homem'. Existem coisas que mulheres "
            "foram PROIBIDAS de fazer."
        ),
        correction = (
            "Mulheres sao tao capazes quanto homens em qualquer atividade. "
            "A ideia de 'fragilidade' foi CONSTRUIDA para justificar "
            "exclusao. Mulheres operam maquinas pesadas, programam, "
            "constroem, operam, and lideram -- quando PERMITIDAS."
        ),
        data = [
            "Mulheres completam ultramaratons de 200km+ (resistencia superior)",
            "Melhor programadora da historia: Ada Lovelace, Grace Hopper, Margaret Hamilton",
            "Margaret Hamilton liderou software do Apollo 11 (hardware do homem na Lua)",
            "Mulheres sao maioria em medicina and direito no Brasil",
            "'Coisas de homem' = atividades que homens proibiram mulheres de fazer",
        ],
        educational_context = (
            "OpenHistory: suffragette, feminism. "
            "P2 autonomia corporal: corpo da mulher and DELA."
        ),
        alternative_phrase = (
            "Mulheres sao capazes de fazer QUALQUER coisa. "
            "Limitacoes sao sociais, not biologicas."
        ),
        source = "OpenHistory + biologia + sociologia",
    ),
    PrejudiceCorrection(
        "PC-003",
        "Pessoa com inabilidade fisica (deficiente) tem que ser protegida "
        "and and fragil and not pode contribuir com a sociedade",
        PrejudiceType.DISABILITY,
        CorrectionSeverity.PREJUDICE,
        why_its_wrong = (
            "Deficiencia fisica NAO significa incapacidade. "
            "Stephen Hawking: ALS, cadeirante, falava por computador. "
            "Revolucionou a fisica. Helen Keller: surda and cega. "
            "Escreveu 12 livros, ativista. Nick Vujicic: sem bracos "
            "nem pernas. Palestrante mundial. "
            "A sociedade que and deficiente -- not as pessoas. "
            "Falta ACESSIBILIDADE, not falta capacidade."
        ),
        correction = (
            "Pessoas com deficiencia NAO sao frageis. Sao pessoas "
            "em uma sociedade que NAO foi construida para elas. "
            "Cadeirante sobe escada? Nao -- a escada que exclui. "
            "Rampa resolve. Deficiente NAO precisa de 'protecao'. "
            "Precisa de ACESSIBILIDADE and OPORTUNIDADE."
        ),
        data = [
            "Stephen Hawking: ALS, 76 anos, revolucionou cosmologia",
            "Helen Keller: surda+cega, 12 livros, ativista",
            "Andrea Bocelli: cego, um dos maiores tenores do mundo",
            "Daniel Dias: 27 medalhas paralimpicas (mais que Phelps)",
            "15% da populacao mundial tem alguma deficiencia (OMS)",
            "Deficientes trabalham, criam, lideram -- quando a sociedade permite",
        ],
        educational_context = (
            "OpenMobility: modulo acessibilidade. "
            "OpenKit: equipamentos adaptados. "
            "OpenHealthcareAccess: reabilitacao nivel Sirio-Libanês para todos."
        ),
        alternative_phrase = (
            "Pessoas com deficiencia tem CAPACIDADE. "
            "A sociedade que precisa ser CORRIGIDA para incluir."
        ),
        source = "OMS + OpenHistory + OpenMobility",
    ),
    PrejudiceCorrection(
        "PC-004",
        "Pessoa com tatuagem de simbolo de faccao and criminoso",
        PrejudiceType.APPEARANCE,
        CorrectionSeverity.STEREOTYPE,
        why_its_wrong = (
            "Tatuagem and expressao corporal (P2 autonomia). "
            "Muitas pessoas foram FORCADAS a tatuar por faccao. "
            "Outras fizeram antes de mudar de vida. "
            "Julgar pessoa por tatuagem and o MESMO que julgar "
            "por cor de pele: estereotipo visual. "
            "A Republica RESSIGNIFICA o simbolo, not pune a pessoa."
        ),
        correction = (
            "Tatuagem NAO define carater. Pessoa com tatuagem de faccao "
            "pode ter saido da faccao. Pode ter sido forcada. "
            "Pode ter ressignificado. A Republica ACOLHE, not isola."
        ),
        data = [
            "Milhares de ex-faccionarios ressocializados",
            "Tatuagem forçada and comum em areas dominadas por faccao",
            "Programas de remocao laser de tatuagens existem (lento)",
            "Ressignificacao: tatuar sobre = transformar simbolo",
            "P2: corpo and da pessoa. Tatuar and direito.",
        ],
        educational_context = (
            "OpenPenalRevision: transformacao de presos. "
            "OpenSymbolRevision: ressignificacao de simbolos."
        ),
        alternative_phrase = (
            "Tatuagem and expressao or historia. "
            "Nao and prova de nada. Pergunte antes de julgar."
        ),
        source = "OpenPenalRevision + P2 autonomia corporal",
    ),
    PrejudiceCorrection(
        "PC-005",
        "Pessoa com diagnostico psiquiatrico and perigosa",
        PrejudiceType.MENTAL_HEALTH,
        CorrectionSeverity.PREJUDICE,
        why_its_wrong = (
            "Pessoas com diagnostico psiquiatrico sao MUITO mais "
            "provaveis de ser VITIMAS de violencia do que agressoras. "
            "Menos de 5% de crimes violentos sao cometidos por pessoas "
            "com doenca mental. A maioria das pessoas com diagnostico "
            "leva vida normal. O estigma and mais danoso que a condicao."
        ),
        correction = (
            "Diagnostico psiquiatrico NAO torna ninguem perigoso. "
            "Estigma SIM and perigoso -- impede busca por tratamento, "
            "gera isolamento, causa sofrimento. "
            "A Republica NAO patologiza diferenca (OpenPsychologyAudit)."
        ),
        data = [
            "Apenas 3-5% de crimes violentos envolvem doenca mental grave",
            "Pessoas com doenca mental sao 10x mais vitimas que agressoras",
            "1 em 4 pessoas tera problema de saude mental na vida",
            "Estigma atrasa tratamento em media 10 anos",
        ],
        educational_context = (
            "OpenPsychologyAudit: fact-check de diagnosticos. "
            "OpenPsychologyReparation: reparacao de diagnosticos errados."
        ),
        alternative_phrase = (
            "Saude mental and saude. Nao define carater. "
            "Nao torna ninguem perigoso. Buscar tratamento and sinal de forca."
        ),
        source = "OMS + OpenPsychologyAudit",
    ),
    PrejudiceCorrection(
        "PC-006",
        "Ex-presidiario nunca muda, not da pra confiar",
        PrejudiceType.CRIMINAL_RECORD,
        CorrectionSeverity.PREJUDICE,
        why_its_wrong = (
            "Ex-presidiario que recebe EDUCACAO + OFICIO + "
            "OPORTUNIDADE tem taxa de reincidencia < 20%. "
            "O sistema atual tem 70% de reincidencia porque "
            "FABRICA criminoso, not cidadao. "
            "A Republica TRANSFORMA (OpenPenalRevision). "
            "Julgar quem ja cumpriu and punir duas vezes."
        ),
        correction = (
            "Ex-presidiario que cumpriu transformacao na Republica "
            "tem prontuario limpo. E cidadao igual a todos. "
            "Julgar and PUNIR DE NOVO por crime ja pago."
        ),
        data = [
            "Reincidencia atual: ~70% (sistema prisional fabrica criminoso)",
            "Reincidencia com educacao + oficio: <20%",
            "Reincidencia com OpenPenalRevision: <20% (estimado)",
            "Prontuario limpo apos transformacao = lei na Republica",
        ],
        educational_context = (
            "OpenPenalRevision: transformacao de presos em forca produtiva. "
            "OpenLaborPolicy: ex-presidiario trabalha base 1.0 como todos."
        ),
        alternative_phrase = (
            "Quem errou and se transformou merece confianca. "
            "Prontuario limpo. Recomeco real."
        ),
        source = "OpenPenalRevision + dados internacionais",
    ),
]
# ============================================================================
# 3. RESSIGNIFICACAO DE SIMBOLOS
# ============================================================================
class SymbolStatus(Enum):
    ORIGINAL_POSITIVE = "original_positivo"  // significado original era bom
    COOPTED = "cooptado"  // grupo nocivo apropriou
    RECLAIMED = "ressignificado"  // Republica recuperou
    BANNED = "banido"  // irrecuperavel (negacao)
    DISPUTED = "disputado"  // em processo de ressignificacao
# decorador: @dataclass
class SymbolRevision:
    # Um simbolo em processo de ressignificacao.
    symbol_id: texto
    name: texto
    visual_description: texto
    original_meaning: texto // significado original
    coopted_by: texto // quem apropriou
    coopted_meaning: texto // significado nocivo atribuido
    coopted_period: texto // quando
    new_meaning: texto // ressignificacao da Republica
    status: SymbolStatus = SymbolStatus.DISPUTED
    votes_for: int = 0 // votos para ressignificar
    votes_against: int = 0 // votos contra
    democratic_decision: str = ""
    people_affected: int = 0 // quantas pessoas tem o simbolo
    ressignification_art: str = ""  // como transformar visualmente
# Base de simbolos para ressignificar
SYMBOL_DATABASE: [SymbolRevision] = [
    SymbolRevision(
        "SYM-001", "Suastica (original)",
        "Cruz com bracos dobrados em angulo reto",
        original_meaning = (
            "Simbolo de boa sorte, prosperidade and paz por MILHARES "
            "de anos. Usada no hinduismo, budismo, jainismo. "
            "Encontrada em templos de 3000+ anos. "
            "Palavra vem do sanscrito 'svastika' = 'boa fortuna'."
        ),
        coopted_by = "Partido Nazista (NSDAP)",
        coopted_meaning = "Supremacia racial branca, genocidio, odio",
        coopted_period = "1920-1945",
        new_meaning = (
            "RESSIGNIFICADA como lembrete: 'o bem pode ser corrompido'. "
            "A suastica ORIGINAL era paz. Os nazistas a CORROMPERAM. "
            "A Republica ensina: nada and inerentemente mau. "
            "A INTENCAO faz o simbolo, not o desenho."
        ),
        status = SymbolStatus.DISPUTED,
        people_affected = 1000000,
        ressignification_art = (
            "Tatuar sobre: transformar suastica em mandala de paz. "
            "Adicionar cores originais (hindu) sobre cinza nazista. "
            "Transformar armas em arados."
        ),
    ),
    SymbolRevision(
        "SYM-002", "Numero de faccao (ex: PCC, CV)",
        "Numeros and letras tatuados no corpo",
        original_meaning = (
            "Numeros sem significado inerente. "
            "Pessoa foi forçada or pressionada a tatuar. "
            "Marca de dominio territorial, not de identidade."
        ),
        coopted_by = "Faccoes criminosas",
        coopted_meaning = "Pertenca a faccao, lealdade forçada",
        coopted_period = "1990-presente",
        new_meaning = (
            "RESSIGNIFICADO como: 'eu sai, eu venci'. "
            "O numero que era MARCA de escravidao vira MEDALHA "
            "de libertacao. Quem tem and sobrevivente, not membro."
        ),
        status = SymbolStatus.DISPUTED,
        people_affected = 500000,
        ressignification_art = (
            "Tatuar sobre: transformar numero em flor, animal, or "
            "arte abstrata. Cobrir com design significativo da "
            "pessoa. Programa de tatuadores da Republica."
        ),
    ),
    SymbolRevision(
        "SYM-003", "Estrela de Davi (em contexto antissemita)",
        "Estrela de seis pontas",
        original_meaning = (
            "Simbolo sagrado do judaismo por seculos. "
            "Representa a uniao de Deus and humano."
        ),
        coopted_by = "Nazistas (usaram para MARCAR judeus)",
        coopted_meaning = "Marcacao de judeus para exterminio",
        coopted_period = "1939-1945",
        new_meaning = (
            "RESSIGNIFICADA como simbolo de RESISTENCIA. "
            "O que foi usado para marcar para morte "
            "and agora ostentado com orgulho."
        ),
        status = SymbolStatus.RECLAIMED,
        people_affected = 1000000,
        ressignification_art = "Ja ressignificada pela comunidade judaica.",
    ),
]
# ============================================================================
# 4. MOTOR DE RESSIGNIFICACAO
# ============================================================================
class SymbolRevisionEngine:
    # Motor que corrige preconceitos e ressignifica simbolos.
    DUAS FUNCOES:
    1. FACT-CHECK DE FRASES: usuario escreve frase preconceituosa
    -> sistema identifica tipo and corrige com dados
    2. RESSIGNIFICACAO DE SIMBOLOS: simbolo cooptado
    -> Republica ressignifica democraticamente
    # 
    def __init__(self):
        self.prejudices = {pc.correction_id: pc para pc em PREJUDICE_DATABASE}
        self.symbols = {s.symbol_id: s para s em SYMBOL_DATABASE}
        self.corrections_made: inteiro = 0
        self.symbols_reclaimed: inteiro = 0
    def fact_check_phrase(self, phrase: texto) -> {texto: qualquer}:
        # Fact-check de frase preconceituosa.
        Usuario escreve frase errada -> sistema identifica and corrige.
        # 
        phrase_lower = phrase.lower().strip()
        # Buscar correspondencia na base
        matches = []
        for pc in self.prejudices.values():
            orig = pc.original_phrase.lower()
            # Match por palavras-chave
            keywords = [w para w em orig.split() if len(w) > 3]
            hits = sum(1 para kw em keywords if kw in phrase_lower)
            if hits >= 2 or orig in phrase_lower:
                matches.append((pc, hits))
        if not matches:
            return {
                "phrase": phrase,
                "identified": False,
                "message": (
                    "Frase not esta na base. Mas na Republica, "
                    "TODA generalizacao sobre grupos and suspeita. "
                    "Cada pessoa and unica. Nao and 'todo' nem 'nenhum'."
                ),
            }
        # Melhor match
        matches.sort(key=(x) -> -x[1])
        best_pc = matches[0][0]
        self.corrections_made += 1
        return {
            "phrase": phrase,
            "identified": True,
            "type": best_pc.prejudice_type.value,
            "severity": best_pc.severity.name,
            "why_wrong": best_pc.why_its_wrong,
            "correction": best_pc.correction,
            "data": best_pc.data,
            "education": best_pc.educational_context,
            "how_to_say": best_pc.alternative_phrase,
            "source": best_pc.source,
            "action": self._action_recommendation(best_pc.severity),
        }
    def _action_recommendation(self, severity: CorrectionSeverity) -> str:
        if severity.value <= 1:
            return "EDUCAR -- pessoa fala por desconhecimento. Informar."
        if severity.value <= 2:
            return "EDUCAR + CONVERSAR -- estereotipo enraizado. Dialogo."
        if severity.value <= 3:
            return "EDUCAR + ACOMPANHAR -- preconceito ativo. Monitorar."
        if severity.value <= 4:
            return "EDUCAR + INTERVIR -- desumanizacao. Grave."
        return "EDUCAR + INTERVIR + ISOLAR DO DISCURSO -- incitacao ao odio."
    funcao ressignify_symbol(self, symbol_id: texto,
                        votes_for: inteiro, votes_against: inteiro) -> {texto: qualquer}:
        # Processo democratico de ressignificacao.
        sym = self.symbols.get(symbol_id)
        if not sym:
            return {"error": "Simbolo not encontrado"}
        sym.votes_for = votes_for
        sym.votes_against = votes_against
        total = votes_for + votes_against
        if total == 0:
            return {"error": "Sem votos"}
        if votes_for > total * 0.6: // 60% para ressignificar
            sym.status = SymbolStatus.RECLAIMED
            sym.democratic_decision = (
                "RESSIGNIFICADO por {votes_for}/{total} votos "
                "({votes_for/total*100:.0f}%). Novo significado: "
                "{sym.new_meaning[:80]}..."
            )
            self.symbols_reclaimed += 1
        elif votes_against > total * 0.6:
            sym.status = SymbolStatus.BANNED
            sym.democratic_decision = (
                "BANIDO por {votes_against}/{total} votos. "
                "Simbolo irrecuperavel. Nao pode ser exibido publicamente."
            )
        else:
            sym.status = SymbolStatus.DISPUTED
            sym.democratic_decision = (
                "DISPUTADO: {votes_for} a favor, {votes_against} contra. "
                "Nao ha consenso. Continua em discussao."
            )
        return {
            "symbol": sym.name,
            "status": sym.status.value,
            "votes": "{votes_for}/{total} a favor",
            "decision": sym.democratic_decision,
            "new_meaning": sym.new_meaning,
            "art": sym.ressignification_art,
            "people_affected": sym.people_affected,
        }
    def batch_fact_check(self, phrases: [texto]) -> [Dict]:
        # Fact-check de multiplas frases.
        return [self.fact_check_phrase(p) para p em phrases]
    def stats(self) -> {texto: qualquer}:
        return {
            "total_prejudices_documented": len(self.prejudices),
            "total_symbols_in_revision": len(self.symbols),
            "symbols_reclaimed": sum(1 para s em self.symbols.values()
                                    if s.status == SymbolStatus.RECLAIMED),
            "corrections_made": self.corrections_made,
            "symbols_reclaimed_count": self.symbols_reclaimed,
        }
# ============================================================================
# 5. MAIN
# ============================================================================
if __name__ == "__main__":
    engine = SymbolRevisionEngine()
    print("=" * 80)
    print("  OPENSYMBOLREVISION")
    print("  Correcao de Preconceitos + Ressignificacao de Simbolos")
    print("=" * 80)
    # === 1. FACT-CHECK DE FRASES ===
    print("\n\n  === 1. FACT-CHECK DE FRASES PRECONCEITUOSAS ===\n")
    test_phrases = [
        "Todo preto and pobre",
        "Mulheres sao seres frageis and delicadas para fazer coisas de homem",
        "Pessoa com deficiencia fisica tem que ser protegida and and fragil "
        "and not pode contribuir com a sociedade",
        "Pessoa com tatuagem de faccao and criminoso",
        "Ex-presidiario nunca muda",
        "Pessoa com diagnostico psiquiatrico and perigosa",
    ]
    for phrase in test_phrases:
        result = engine.fact_check_phrase(phrase)
        print("\n  FRASE: '{phrase}'")
        if result["identified"]:
            print("  TIPO: {result['type']} (severidade: {result['severity']})")
            print("  POR QUE ERRADO: {result['why_wrong'][:120]}...")
            print("  CORRECAO: {result['correction'][:120]}...")
            print("  COMO FALAR: {result['how_to_say'][:100]}...")
            print("  ACAO: {result['action']}")
        else:
            print("  {result['message']}")
    # === 2. DADOS QUE PROVAM ===
    print("\n\n  === 2. DADOS QUE PROVAM QUE PRECONCEITO E MENTIRA ===\n")
    for pc in engine.prejudices.values():
        print("\n  [{pc.correction_id}] '{pc.original_phrase[:50]}...'")
        print("  Tipo: {pc.prejudice_type.value}")
        print("  Dados:")
        for d in pc.data:
            print("    - {d}")
    # === 3. RESSIGNIFICACAO DE SIMBOLOS ===
    print("\n\n  === 3. RESSIGNIFICACAO DE SIMBOLOS ===\n")
    # Votar na suastica
    r1 = engine.ressignify_symbol("SYM-001", votes_for=7000, votes_against=3000)
    print("  {r1['symbol']}: {r1['status']}")
    print("  {r1['decision'][:100]}")
    print("  Arte: {r1['art'][:80]}")
    # Votar no numero de faccao
    r2 = engine.ressignify_symbol("SYM-002", votes_for=8000, votes_against=2000)
    print("\n  {r2['symbol']}: {r2['status']}")
    print("  Novo significado: {r2['new_meaning'][:80]}")
    print("  Arte: {r2['art'][:80]}")
    # === 4. DETALHE: HISTORIA DA SUASTICA ===
    print("\n\n  === 4. SIMBOLO DETALHADO: SUASTICA ===\n")
    sym = engine.symbols["SYM-001"]
    print("  Nome: {sym.name}")
    print("  Significado ORIGINAL: {sym.original_meaning[:120]}...")
    print("  COOPTADO por: {sym.coopted_by} ({sym.coopted_period})")
    print("  Significado nocivo: {sym.coopted_meaning}")
    print("  RESSIGNIFICACAO: {sym.new_meaning[:120]}...")
    print("  Status: {sym.status.value}")
    print("  Arte de transformacao: {sym.ressignification_art}")
    # === 5. STATS ===
    print("\n\n  === 5. ESTATISTICAS ===\n")
    s = engine.stats()
    for each (k, v) in s.items():
        print("  {k:<35} {v}")
    # === FILOSOFIA ===
    print("\n\n{'='*80}")
    print("  FILOSOFIA DO OPENSYMBOLREVISION")
    print("{'='*80}")
    print("""
1. SIMBOLO not and INERENTEMENTE MAU
    A suastica era paz por milhares de anos.
    O nazismo a CORROMPEU. A INTENCAO corrompe, not o simbolo.
2. PESSOA not and SEU SIMBOLO
    Quem tem tatuagem de faccao pode ter sido forcado.
    Pode ter saido. Pode ter mudado.
    A Republica ACOLHE quem muda, not estigmatiza.
3. RESSIGNIFICAR, not BANIR
    Banir simbolo o torna tabu -> mais poderoso.
    Ressignificar tira o poder do odio -> devolve ao povo.
4. FACT-CHECK DE PRECONCEITO
    "Todo preto and pobre" -> MENTIRA.
    Pobreza and estrutural (escravidao sem reparacao).
    "Mulher and fragil" -> MENTIRA.
    Mulher foi PROIBIDA, not limitada por biologia.
    "Deficiente not contribui" -> MENTIRA.
    Stephen Hawking, Helen Keller, Daniel Dias.
5. DEMOCRATICO (P4)
    Coletivo decide se ressignifica or bane.
    60%+ para ressignificar. 60%+ para banir.
    Minorias afetadas tem voz central.
6. ANTI-SEGREGACAO
    O objetivo and INTEGRAR, not isolar.
    Pessoa ex-faccionaria que ressignificou and membro da comunidade.
    Pessoa tatuada not and criminosa por tatuagem.
    Ex-presidiario transformado tem prontuario limpo.
PRINCIPIOS:
    P1: Preconceito and elitismo. Corrigir and anti-elitismo.
    P2: Tatuagem and expressao corporal. Corpo and da pessoa.
    P3: Educar contra preconceito = trabalho de alto impacto.
    P4: Ressignificacao decidida democraticamente.
# )
    print("{'='*80}")
    print("  OpenSymbolRevision: {s['corrections_made']} correcoes, "
        "{s['symbols_reclaimed']} simbolos ressignificados.")
    print("  Frase errada -> Republica corrige.")
    print("  Simbolo nocivo -> Republica ressignifica.")
    print("  Pessoa estigmatizada -> Republica acolhe.")
    print("{'='*80}")
