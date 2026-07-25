#!/usr/bin/env python3
"""
OpenAntiDeterminism -- O Futuro Nao Esta Escrito -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenAntiDeterminism -- O Futuro Nao Esta Escrito
====================================================
"Nao existe determinismo historico.
O que aconteceu no passado not determina o futuro.
Voce nasceu pobre? not determina que morre pobre.
Cometeu erro? not determina que and criminoso pra sempre.
Foi rotulado? not determina que and a identidade.
O passado and CONTEXTO. O futuro and ESCOLHA.
A Republica garante: TODO futuro esta aberto."
O QUE ESTE SISTEMA FAZ:
1. AFIRMA que not ha determinismo historico
2. DESCONSTRÓI cada narrativa de "destino determinado"
3. PROVA com dados que mudanca and real
4. INTEGRA com OpenPsychologyReparation, OpenDignity, OpenReintegration
AS 12 NARRATIVAS DE DETERMINISMO QUE A REPUBLICA REJEITA:
1. "Nasceu pobre, morre pobre" -> False. OpenDignity + OpenEducation mudam.
2. "Cometeu crime, sempre criminoso" -> False. OpenReintegration.
3. "Foi diagnosticado, sempre tera" -> False. Neuroplasticidade.
4. "Foi viciado, sempre sera" -> False. Tratamento funciona.
5. "Negro da periferia not sai" -> False. OpenSymbolRevision.
6. "Mulher and frágil" -> False. OpenRelationships + OpenProfessions.
7. "Deficiente not contribui" -> False. Stephen Hawking.
8. "Velho not aprende" -> False. Neuroplasticidade aos 90.
9. "Sem diploma, not and ninguem" -> False. OpenSkills > diploma.
10. "Familia desfeita, sempre sera" -> False. OpenFamilyLabor.
11. "Trauma define para sempre" -> False. Ps- trauma integra.
12. "Sua classe define seu valor" -> False. P1 anti-elitismo.
Author: OpenRepublic Team
# 
# importa annotations de __future__
# importa hashlib
# importa dataclass, field de dataclasses
# importa Any, Dict, List, Optional de typing
# importa Enum de enum
# importa datetime de datetime
# ============================================================================
# 1. NARRATIVAS DETERMINISTAS (e a verdade que as derruba)
# ============================================================================
class DeterminismType(Enum):
    ECONOMIC = "determinismo_economico"  // "nasceu pobre, morre pobre"
    CRIMINAL = "determinismo_criminal"  // "cometeu crime, sempre sera"
    MEDICAL = "determinismo_medico"  // "diagnosticado, sempre tera"
    ADDICTION = "determinismo_vicio"  // "viciado, sempre sera"
    RACIAL = "determinismo_racial"  // "raca define destino"
    GENDER = "determinismo_genero"  // "genero define capacidade"
    ABILITY = "determinismo_capacidade"  // "deficiencia define valor"
    AGE = "determinismo_idade"  // "velho not aprende"
    EDUCATIONAL = "determinismo_educacional"  // "sem diploma, not and ninguem"
    FAMILIAL = "determinismo_familiar"  // "familia desfeita, sempre sera"
    TRAUMA = "determinismo_trauma"  // "trauma define para sempre"
    CLASS = "determinismo_classe"  // "classe define valor"
# decorador: @dataclass
class DeterministicNarrative:
    # Uma narrativa determinista e a verdade que a DERRUBA.
    narrative_id: texto
    determinism_type: DeterminismType
    the_lie: texto // a mentira determinista
    the_truth: texto // a verdade que liberta
    scientific_evidence: texto // prova científica
    republic_system: texto // sistema que corrige
    real_example: str = ""  // exemplo real de mudanca
# As 12 narrativas
NARRATIVES: [DeterministicNarrative] = [
    DeterministicNarrative(
        "DN-01", DeterminismType.ECONOMIC,
        the_lie = (
            "Nasceu pobre, morre pobre. "
            "A favela and seu lugar. A riqueza and dos outros."
        ),
        the_truth = (
            "Pobreza and CONDIÇÃO, não IDENTIDADE. "
            "A Republica garante: moradia (OpenDignity), "
            "educacao (OpenUniversity), trabalho (OpenLaborRelay), "
            "saude (OpenHealth Sirio-Libanes). Tudo ZERO. "
            "Quem nasceu pobre TEM TODO o que o rico tem. "
            "A diferenca some. O futuro se abre."
        ),
        scientific_evidence = (
            "Estudo Brookings (EUA): 3 fatores quebram ciclo de pobreza: "
            "educacao + trabalho + saude. A Republica garante os 3. "
            "PNUD: investir em pobreza reduz pobreza. Sempre."
        ),
        republic_system = "OpenDignity + OpenEducation + OpenLaborRelay + OpenHealth",
        real_example = (
            "Lula: migrante nordestino, 5 anos sem saber ler, virou presidente. "
            "Seu Ze: catador de lixo, OpenRecyclers transformou em TRABALHADOR AMBIENTAL. "
            "Ana: moradora de rua, OpenDignity resgatou, hoje programa em Rust."
        ),
    ),
    DeterministicNarrative(
        "DN-02", DeterminismType.CRIMINAL,
        the_lie = (
            "Cometeu crime uma vez, sempre sera criminoso. "
            "Prontuario marca para sempre. Sociedade nunca aceita."
        ),
        the_truth = (
            "O erro NAO define a pessoa. "
            "OpenPenalRevision: transforma em forca produtiva. "
            "OpenReintegration: moradia + trabalho + mentor + comunidade. "
            "Prontuario LIMPO. Passado apagado. "
            "Ex-presidiario and CIDADAO. Igual a todos."
        ),
        scientific_evidence = (
            "Noruega: sistema prisional foca em reabilitacao. "
            "Reincidencia: 20% (vs 70% Brasil/EUA). "
            "PROVA: tratamento > punicao. Mudanca and REAL."
        ),
        republic_system = "OpenPenalRevision + OpenReintegration",
        real_example = (
            "Malcolm X: preso, virou lider. "
            "Nelson Mandela: 27 anos preso, virou presidente. "
            "Milhares de ex-presidiarios reabilitados na Noruega."
        ),
    ),
    DeterministicNarrative(
        "DN-03", DeterminismType.MEDICAL,
        the_lie = (
            "Foi diagnosticado com depressao/ansiedade/bipolar. "
            "E para sempre. Sem cura. Aprenda a conviver."
        ),
        the_truth = (
            "O cerebro and NEUROPLASTICO. Muda ate os 90 anos. "
            "Diagnostico and FERRAMENTA TEMPORARIA, not identidade. "
            "Recuperacao and POSSIVEL: 40-60% em estudos longitudinais. "
            "OpenPsychology: sem rotular. Trata CAUSA. "
            "OpenPsychologyReparation: repara diagnostico errado. "
            "OpenMentalHygiene: bloqueia 'sempre tera'."
        ),
        scientific_evidence = (
            "Eric Kandel (Nobel 2000): neuroplasticidade comprovada. "
            "Estudo WHO: 40-60% de recuperacao em saude mental. "
            "Portugal (descriminalizacao + tratamento): uso caiu, suicidio caiu."
        ),
        republic_system = "OpenPsychology + OpenPsychologyReparation + OpenMentalHygiene",
        real_example = (
            "Milhares superaram depressao com terapia + exercicio + mudanca de vida. "
            "Veteranos de guerra com TEPT recuperados com psilocibina (Johns Hopkins). "
            "Neuroplasticidade: pacientes de AVC recuperam movimento anos depois."
        ),
    ),
    DeterministicNarrative(
        "DN-04", DeterminismType.ADDICTION,
        the_lie = (
            "Viciado uma vez, sempre sera. "
            "Recuperacao and impossivel. Reaida sempre."
        ),
        the_truth = (
            "Vicio and DOENCA, not destino. "
            "Tratamento funciona. Recuperacao and REAL. "
            "OpenDignity: colonia de tratamento (moradia + comunidade + oficio). "
            "OpenHealth: tratamento nivel Sirio-Libanes. "
            "Recuperacao and PROCESSO. Reaida not and fracasso -- and parte. "
            "A Republica NUNCA desiste."
        ),
        scientific_evidence = (
            "NIDA (EUA): taxa de recuperacao com tratamento = 40-60%. "
            "Portugal: descriminalizacao + tratamento -> uso caiu 20%. "
            "AA/NA: milhoes em recuperacao duradoura."
        ),
        republic_system = "OpenDignity + OpenHealth + OpenReintegration",
        real_example = (
            "Eric Clapton: viciado em heroina, recuperado ha 30+ anos. "
            "Robert Downey Jr.: preso por drogas, virou maior ator. "
            "Milhares anonimos recuperados em comunidades terapeuticas."
        ),
    ),
    DeterministicNarrative(
        "DN-05", DeterminismType.RACIAL,
        the_lie = (
            "Negro da periferia not tem chance. "
            "Raca define destino. Sistema and branco."
        ),
        the_truth = (
            "Cor de pele NAO define capacidade. "
            "OpenSymbolRevision: corrige preconceito. "
            "OpenHistory: registra verdade (escravidao sem reparacao). "
            "P1 anti-elitismo: TODOS iguais. Mesmo acesso. "
            "O SISTEMA and que era racista. A Republica NAO and. "
            "OpenDignity: resgata de qualquer condicao. "
            "OpenEducation: universidade para TODOS."
        ),
        scientific_evidence = (
            "Genetica: 99.9% do DNA and identico entre racas. "
            "Diferenca racial and SOCIAL (escravidao, segregacao), not biologica. "
            "Estudo Harvard: quando controle socioeconomico and igual, "
            "diferenca de desempenho entre racas DESAPARECE."
        ),
        republic_system = "OpenSymbolRevision + OpenHistory + OpenDignity + P1",
        real_example = (
            "Machado de Assis: neto de escravos, maior escritor do Brasil. "
            "Barack Obama: filho de africano, presidente dos EUA. "
            "Zumbi dos Palmares: liderou resistencia. "
            "Carolina de Jesus: catadora de papel, virou escritora reconhecida."
        ),
    ),
    DeterministicNarrative(
        "DN-06", DeterminismType.GENDER,
        the_lie = (
            "Mulher and frágil. Nao consegue fazer o que homem faz. "
            "Lugar de mulher and em casa."
        ),
        the_truth = (
            "Genero NAO define capacidade. NENHUMA. "
            "OpenProfessions: competencia > genero. "
            "OpenRelationships: corpo and dela. P2. "
            "P1: todos iguais. Sem hierarquia de genero. "
            "Mulheres fazem TUDO que homens fazem (quando permitidas)."
        ),
        scientific_evidence = (
            "Estudo meta-analise (10.000+ estudos): nenhuma diferenca "
            "cognitiva significativa entre generos. "
            "Diferenca de desempenho and CULTURAL, not biologica. "
            "Paises com mais igualdade de genero: diferenca some."
        ),
        republic_system = "OpenProfessions + OpenRelationships + P1 + P2",
        real_example = (
            "Margaret Hamilton: liderou software Apollo 11. "
            "Marie Curie: duas vezes Nobel. "
            "Ada Lovelance: primeira programadora. "
            "Dilma Rousseff: torturada, virou presidente."
        ),
    ),
    DeterministicNarrative(
        "DN-07", DeterminismType.ABILITY,
        the_lie = (
            "Deficiente not contribui. Precisa de caridade. "
            "Nao tem capacidade."
        ),
        the_truth = (
            "Deficiencia NAO significa incapacidade. "
            "Stephen Hawking: ALS, cadeirante, revolucionou fisica. "
            "Daniel Dias: 27 medalhas paralimpicas. "
            "A sociedade que and deficiente -- falta ACESSIBILIDADE. "
            "OpenMobility: acessibilidade total. "
            "OpenKit: equipamentos adaptados. "
            "P1: TODO cidadao contribui. Cada um no que PODE."
        ),
        scientific_evidence = (
            "OMS: 15% da populacao tem alguma deficiencia. "
            "Estudos: pessoas com deficiencia tem desempenho IGUAL or SUPERIOR "
            "quando barreiras arquitetonicas/atitudinais removidas. "
            "Diversidade cognitiva: autismos em alguns contextos sao VANTAGEM."
        ),
        republic_system = "OpenMobility + OpenKit + OpenVision + OpenProfessions",
        real_example = (
            "Stephen Hawking: ALS, 76 anos, cosmologia revolucionaria. "
            "Helen Keller: surda+cega, 12 livros. "
            "Andrea Bocelli: cego, tenor mundial. "
            "Nick Vujicic: sem membros, palestrante global."
        ),
    ),
    DeterministicNarrative(
        "DN-08", DeterminismType.AGE,
        the_lie = (
            "Velho not aprende. Passou da idade. "
            "Cérebro endurece."
        ),
        the_truth = (
            "Neuroplasticidade CONTINUA ate os 90 anos. "
            "O cerebro CRIA novas conexoes enquanto aprende. "
            "OpenEducation: sem idade limite. "
            "OpenUniversity: todos cursam. "
            "OpenGamesRealistic: aprender jogando, qualquer idade. "
            "P1: ninguem and 'velho demais'. Aprendizado and DIREITO."
        ),
        scientific_evidence = (
            "Eric Kandel (Nobel 2000): neuroplasticidade em idosos comprovada. "
            "Estudo Lancet: adultos que aprendem skill nova tem "
            "melhor cognicao and menor risco de demencia. "
            "Bilinguismo tardio protege cerebro."
        ),
        republic_system = "OpenEducation + OpenUniversity + OpenGamesRealistic",
        real_example = (
            "Tobias (68 anos): aprendeu Rust no OpenTerminal. "
            "Dona Rita (72): aprendeu costura no OpenGamesRealistic. "
            "Ken Doherty: PhD aos 87 anos. "
            "Tao Porchon-Lynch: yoga teacher aos 101 anos."
        ),
    ),
    DeterministicNarrative(
        "DN-09", DeterminismType.EDUCATIONAL,
        the_lie = (
            "Sem diploma, voce not and ninguem. "
            "Sem faculdade, not consegue nada."
        ),
        the_truth = (
            "Diploma NAO define competencia. "
            "OpenSkills: SISTEMA COMPROVA, not papel. "
            "Maria costureira PLENO sem curso (competencia real). "
            "Joao programador PLENO sem faculdade (3 sistemas da Republica). "
            "P1: COMPETENCIA > TITULO. Sempre."
        ),
        scientific_evidence = (
            "Estudo McKinsey: 40% dos empregadores dizem "
            "diploma not prediz desempenho. "
            "Silicon Valley: Andreessen Horowitz removeu requisito de diploma. "
            "Google: 14% das contratacoes not tem faculdade. "
            "Competencia real > papel."
        ),
        republic_system = "OpenSkills + OpenProfessions + OpenLegoCode",
        real_example = (
            "Bill Gates: largou Harvard. "
            "Steve Jobs: largou Reed College. "
            "Joao (pedreiro OpenSkills): 20 anos pratica > engenheiro recem-formado. "
            "Maria (costureira): vestido de noiva melhor que atelier."
        ),
    ),
    DeterministicNarrative(
        "DN-10", DeterminismType.FAMILIAL,
        the_lie = (
            "Familia desfeita, sempre sera. "
            "Pais separados = filho problematico."
        ),
        the_truth = (
            "Familia NAO and destino. E CONTEXTO. "
            "OpenFamilyLabor: familia se reorganiza. "
            "OpenRelationships: respeito, sem possessao. "
            "Filho de pais separados PODE ter vida excelente. "
            "Filho de familia 'intacta' PODE ter problemas. "
            "O que define NAO and a estrutura familiar. "
            "E o AMOR, o APOIO, a COMUNIDADE."
        ),
        scientific_evidence = (
            "Estudo APA (American Psychological Association): "
            "filhos de divorcio SAO BEM quando: "
            "(1) sem conflito entre pais, (2) apoio emocional, "
            "(3) estabilidade. "
            "DIVORCIO CONFLITUOSO and pior que divorcio pacifico."
        ),
        republic_system = "OpenFamilyLabor + OpenRelationships + OpenEducation",
        real_example = (
            "Obama: pai ausente, criado pela mae and avos, virou presidente. "
            "J.K. Rowling: mae solteira, dependente de assistencia, "
            "escreveu Harry Potter, virou bilhonaria. "
            "Milhoes de filhos de pais separados bem-sucedidos."
        ),
    ),
    DeterministicNarrative(
        "DN-11", DeterminismType.TRAUMA,
        the_lie = (
            "Sofreu trauma, esta quebrado para sempre. "
            "Passado doloroso define o futuro."
        ),
        the_truth = (
            "Trauma NAO define. Pode ser INTEGRADO. "
            "Ps-intumo and crescimento (PTG): milhoes crescem APOS trauma. "
            "OpenPsychology: terapia sem rotular. "
            "OpenMentalHygiene: bloqueia 'vitima eterna'. "
            "Cicatriz != ferida aberta. "
            "O passado doi. Mas not DICTA."
        ),
        scientific_evidence = (
            "Post-Traumatic Growth (PTG): Tedeschi & Calhoun. "
            "Estudo: 50-70% de sobreviventes de trauma relatam "
            "CRESCIMENTO pessoal (empatia, resiliencia, proposito). "
            "Trauma pode ser INTEGRADO, not so superado."
        ),
        republic_system = "OpenPsychology + OpenMentalHygiene + OpenMartialArts",
        real_example = (
            "Viktor Frankl: sobreviveu Holocausto, escreveu 'Em Busca de Sentido'. "
            "Malala: baleada na cabeca, virou Nobel da Paz. "
            "Nelson Mandela: 27 anos preso, liderou reconciliacao."
        ),
    ),
    DeterministicNarrative(
        "DN-12", DeterminismType.CLASS,
        the_lie = (
            "Classe social define valor. "
            "Rico vale mais. Pobre vale menos."
        ),
        the_truth = (
            "Classe NAO define valor. NADA define valor. "
            "P1 anti-elitismo: TODOS valem o mesmo. "
            "Base 1.0. Mesmo crédito. Mesmo acesso. "
            "Diferenca so por IMPACTO (trabalho real), not por nascer em berco. "
            "Na Republica: classe NAO EXISTE. Todo mundo and cidadao."
        ),
        scientific_evidence = (
            "Estudo Piketty: desigualdade and CONSTRUCAO INSTITUCIONAL, "
            "not natural. Mudou regras -> mudou distribuicao. "
            "Dinamarca/Suecia: igualdade alta -> indicadores melhores em TUDO. "
            "Desigualdade NAO and natural. E ESCOLHA politica."
        ),
        republic_system = "P1 anti-elitismo + OpenCredit + OpenLaborPolicy",
        real_example = (
            "Dinamarca: igualdade -> felicidade, saude, educacao melhores. "
            "Cleiton (fundador): 4000h/ano trabalhando, mesmo voto que todos. "
            "Maria (medica): mesmo crédito que Tobias (aposentado). "
            "Na Republica: NAO HA CLASSE."
        ),
    ),
]
# ============================================================================
# 2. MOTOR ANTI-DETERMINISMO
# ============================================================================
class AntiDeterminismEngine:
    # Motor que destrói determinismo histórico.
    PRINCIPIO:
    O passado and CONTEXTO. O futuro and ESCOLHA.
    A Republica garante que TODO futuro esta aberto.
    Nenhuma historia determina destino.
    COMO FUNCIONA:
    1. IDENTIFICA narrativa determinista ("voce sempre sera X")
    2. MOSTRA a verdade (ciência + dados + exemplos)
    3. CONECTA com sistema da Republica que quebra o ciclo
    4. AFIRMA: futuro aberto. Sempre.
    O QUE O SISTEMA not FAZ:
    - Nega que o passado INFLUENCIA (influencia, sim)
    - Nega que trauma DOE (doi, sim)
    - Promete que mudar and facil (not and -- mas and POSSIVEL)
    O QUE O SISTEMA FAZ:
    - Afirma que influencia != determinacao
    - Afirma que dor != destino
    - Afirma que mudar and dificil mas POSSIVEL
    - Garante que a Republica DA as condicoes para mudar
    # 
    def __init__(self):
        self.narratives: {texto: DeterministicNarrative} = {
            n.narrative_id: n para n em NARRATIVES
        }
    def fact_check_determinism(self, phrase: texto) -> {texto: qualquer}:
        # Verifica se frase e determinista e corrige.
        phrase_lower = phrase.lower()
        for narrative in self.narratives.values():
            lie_keywords = [w para w em narrative.the_lie.lower().split()
                        if len(w) > 4]
            hits = sum(1 para kw em lie_keywords if kw in phrase_lower)
            if hits >= 3 or any(kw in phrase_lower para kw em [
                "sempre sera", "nunca vai", "not tem como",
                "destino", "nasceu assim", "para sempre",
                "not adianta", "perdido",
            ]):
                return {
                    "identified": True,
                    "determinism_type": narrative.determinism_type.value,
                    "the_lie": narrative.the_lie[:80],
                    "the_truth": narrative.the_truth[:120],
                    "evidence": narrative.scientific_evidence[:80],
                    "republic_system": narrative.republic_system,
                    "example": narrative.real_example[:80],
                    "message": (
                        "DETERMINISMO IDENTIFICADO: {narrative.determinism_type.value}. "
                        "A Republica DIZ: o passado NAO determina. "
                        "Ciencia prova. Sistema garante. Futuro aberto."
                    ),
                }
        return {
            "identified": False,
            "message": (
                "Frase sem determinismo identificado. "
                "Mas lembre: nenhum passado define futuro."
            ),
        }
    def get_narrative(self, determinism_type: DeterminismType) -> {texto: qualquer}:
        # Retorna a verdade sobre um tipo de determinismo.
        for n in self.narratives.values():
            if n.determinism_type == determinism_type:
                return {
                    "type": n.determinism_type.value,
                    "lie": n.the_lie,
                    "truth": n.the_truth,
                    "evidence": n.scientific_evidence,
                    "system": n.republic_system,
                    "example": n.real_example,
                }
        return {"error": "Tipo not encontrado"}
    def all_narratives(self) -> [Dict]:
        return [
            {
                "id": n.narrative_id,
                "type": n.determinism_type.value,
                "lie": n.the_lie[:60],
                "truth": n.the_truth[:60],
                "system": n.republic_system,
            }
            para n in self.narratives.values()
        ]
    def stats(self) -> {texto: qualquer}:
        return {
            "narrativas_derrubadas": len(self.narratives),
            "principio": "O passado and contexto. O futuro and escolha.",
            "sistemas_integrados": len(set(
                n.republic_system para n em self.narratives.values())),
        }
# ============================================================================
# 3. MAIN
# ============================================================================
if __name__ == "__main__":
    engine = AntiDeterminismEngine()
    print("=" * 80)
    print("  OPENANTIDETERMINISM -- O FUTURO NAO ESTA ESCRITO")
    print("  O passado and contexto. O futuro and escolha.")
    print("=" * 80)
    # === 1. AS 12 MENTIRAS DETERMINISTAS ===
    print("\n\n  === 12 NARRATIVAS DETERMINISTAS DERRUBADAS ===\n")
    for n in NARRATIVES:
        print("\n  [{n.narrative_id}] {n.determinism_type.value.upper()}")
        print("  A MENTIRA: {n.the_lie[:70]}...")
        print("  A VERDADE: {n.the_truth[:70]}...")
        print("  CIENCIA: {n.scientific_evidence[:70]}...")
        print("  SISTEMA: {n.republic_system}")
        print("  EXEMPLO: {n.real_example[:70]}...")
    # === 2. FACT-CHECK DE FRASES DETERMINISTAS ===
    print("\n\n  === FACT-CHECK DE DETERMINISMO ===\n")
    test_phrases = [
        "Ele nasceu na favela, sempre vai ser pobre, not tem como mudar",
        "Foi preso uma vez, sempre sera criminoso, not adianta",
        "Tem depressao, para sempre, not tem cura, aprenda a conviver",
        "E viciado em crack, perdido, nunca vai recuperar",
        "Velho demais pra aprender programacao",
        "Sem diploma not and ninguem, not consegue nada",
    ]
    for phrase in test_phrases:
        result = engine.fact_check_determinism(phrase)
        icon = result["identified"] ? "DETERMINISMO" : "OK"
        print("\n  [{icon}] '{phrase[:50]}...'")
        if result["identified"]:
            print("  Tipo: {result['determinism_type']}")
            print("  Verdade: {result['the_truth'][:70]}...")
    # === 3. STATS ===
    print("\n\n  === ESTATISTICAS ===\n")
    s = engine.stats()
    for each (k, v) in s.items():
        print("  {k:<35} {v}")
    # === FILOSOFIA ===
    print("\n\n{'='*80}")
    print("  FILOSOFIA: ANTI-DETERMINISMO")
    print("{'='*80}")
    print("""
not EXISTE DETERMINISMO HISTORICO.
    O que aconteceu no passado not determina o futuro.
    O passado INFLUENCIA. Mas not DETERMINA.
    Influencia != determinacao.
AS 12 MENTIRAS:
    1. "Nasceu pobre, morre pobre" -> OpenDignity muda
    2. "Cometeu crime, sempre sera" -> OpenReintegration muda
    3. "Diagnosticado, sempre tera" -> Neuroplasticidade muda
    4. "Viciado, sempre sera" -> Tratamento muda
    5. "Raca define destino" -> OpenSymbolRevision muda
    6. "Genero define capacidade" -> OpenProfessions muda
    7. "Deficiencia define valor" -> Stephen Hawking muda
    8. "Velho not aprende" -> Neuroplasticidade aos 90 muda
    9. "Sem diploma, not and ninguem" -> OpenSkills muda
    10. "Familia desfeita, sempre sera" -> OpenFamilyLabor muda
    11. "Trauma define para sempre" -> Ps-crescimento muda
    12. "Classe define valor" -> P1 anti-elitismo muda
A DIFERENCA ENTRE INFLUENCIA and DETERMINACAO:
    Influencia: o passado deixa MARCA. Doe. Afeta.
    Determinacao: o passado FIXA o futuro. Imutavel.
    A Republica reconhece influencia. REJEITA determinacao.
    Trauma DOI? Sim. Mas not DICTA.
    Pobreza AFETA? Sim. Mas not DESTINA.
    Erro MARCA? Sim. Mas not DEFINE.
O QUE A REPUBLICA FAZ:
    not promete que mudar and facil. Mudar and DIFICIL.
    MAS garante que mudar and POSSIVEL.
    and garante as CONDICOES para mudar:
    - Moradia (OpenDignity)
    - Tratamento (OpenHealth)
    - Educacao (OpenUniversity)
    - Trabalho (OpenLaborRelay)
    - Comunidade (OpenNightLife + OpenSocialNetwork)
    - Mentor (OpenProfessions)
    - Skills comprovadas (OpenSkills)
    - Prontuario limpo (OpenReintegration)
    Com essas condicoes, MUDANCA and REAL.
    Sem essas condicoes, determinismo se CUMPRE.
    A Republica garante as condicoes. Sempre.
A CIENCIA PROVA:
    Neuroplasticidade: cerebro muda (Kandel, Nobel 2000)
    Recuperacao em saude mental: 40-60% (WHO)
    Reabilitacao prisional: Noruega 20% reincidencia (vs 70%)
    Ps-crescimento: 50-70% relatam crescimento apos trauma
    Desigualdade and CONSTRUCAO, not natural (Piketty)
PRINCIPIOS:
    P1: Nenhum passado define valor. Todos iguais.
    P2: Corpo and mente soberanos. Podem mudar.
    P3: Dar condicoes para mudar = trabalho de impacto max.
    P4: Assembleia garante: futuro aberto para todos.
# )
    print("{'='*80}")
    print("  OpenAntiDeterminism: {s['narrativas_derrubadas']} narrativas derrubadas.")
    print("  {s['principio']}")
    print("{'='*80}")
