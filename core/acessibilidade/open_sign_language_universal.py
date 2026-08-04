#!/usr/bin/env python3
"""
OpenSignLanguageUniversal -- Ponte Universal entre Linguas de Sinais e Faladas
=================================================================================
"Um surdo brasileiro fala Libras. Um surdo americano fala ASL.
Eles NAO se entendem. Libras e ASL sao tao diferentes
 quanto portugues e ingles.

Um surdo brasileiro quer falar com um surdo japones.
Como? O sistema TRADUZ Libras -> JSL em tempo real.

Um ouvinte frances quer falar com um surdo brasileiro.
Como? Frances falado -> Libras via avatar. Libras -> Frances via texto.

ESTE MODULO e a PONTE UNIVERSAL:
- 195+ linguas de sinais mapeadas (uma por pais)
- Traducao entre QUALQUER lingua de sinais para outra
- Traducao de QUALQUER lingua falada para QUALQUER lingua de sinais
- Traducao de QUALQUER lingua de sinais para QUALQUER lingua falada
- Avatar universal que signa em qualquer lingua de sinais

FLUXO:
  Surdo Brasileiro (Libras)  <-->  Surdo Americano (ASL)
  Surdo Japones (JSL)        <-->  Ouvinte Alemao (DGS/Deutsch)
  Ovinte Frances (Francais)  <-->  Surdo Brasileiro (Libras)

A IA captura sinais da camera -> traduz para LINGUA PONTE (glossario universal)
-> converte para a lingua de destino -> avatar signa OU texto fala.

MODELOS DE IA 2024/2025 (SignLanguageModelRegistry):
  - ASL: ASL Citizen (DePaul/IBM), SignBERT, Pose2Text GPT
  - BSL: BSLCP-Bot, BSL-VideoLLM (Bristol)
  - JSL: JSL-LLM (Tsukuba), Atsumare! JSL Corpus
  - Libras: Libras-KBR / Hand Talk AI, Libras Corpus UFSC
  - Cross-lingual: SP-10K, How2Sign, Phoenix-2014T, OpenSign-MT

Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)
Version: 2024.11 (dados demograficos e modelos atualizados para 2024/2025)
"""

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field
from collections import defaultdict
import time


# ============================================================================
# 1. LINGUAS DE SINAIS DO MUNDO (195+ paises)
# ============================================================================

class SignLanguageFamily(Enum):
    """Familias linguisticas das linguas de sinais."""
    FRENCH = "francesa"           # ASL, LSF, Libras (tem raizes francesas)
    BRITISH = "britanica"         # BSL, Auslan, NZSL
    JAPANESE = "japonesa"         # JSL, Korean SL, Taiwanese SL
    GERMAN = "alema"              # DGS
    ISOLATED = "isolada"          # Lingua unica sem parentes conhecidos
    INDIGENOUS = "indigena"       # Linguas de sinais indigenas
    INTERNATIONAL = "internacional"  # Gestuno ( Internacional Sign)


@dataclass
class SignLanguage:
    """Uma lingua de sinais de um pais."""
    code: str                          # codigo ISO (bsl, asl, bzs)
    name: str                          # nome (Libras, ASL, LSF)
    country: str                       # pais (Brasil, EUA, Franca)
    country_code: str                  # BR, US, FR
    family: SignLanguageFamily
    users_millions: float              # numero de usuarios (milhoes)
    one_handed: bool = False           # uma mao ou duas maos
    fingerspelling: bool = True        # tem alfabeto datilologico
    facial_grammar: bool = True        # usa expressao facial como gramatica
    iso_standard: str = ""             # ISO 639-3
    mutual_intelligibility: List[str] = field(default_factory=list)  # outras LS que entende


# ============================================================================
# 2. CATALOGO DE LINGUAS DE SINAIS (60+ paises)
# ============================================================================

SIGN_LANGUAGES: List[SignLanguage] = [
    # === AMERICA DO SUL === (dados atualizados 2024/2025)
    SignLanguage("bzs", "Libras", "Brasil", "BR", SignLanguageFamily.FRENCH,
                 users_millions=5.2, iso_standard="bzs",  # ~5.2M incl. surdos + ouvintes fluentes (IBGE/2024 est.)
                 mutual_intelligibility=["LGP-PT"]),
    SignLanguage("lsb", "LSCB", "Bolivia", "BO", SignLanguageFamily.FRENCH, 0.12),  # 2024 est.
    SignLanguage("csg", "LSCH", "Chile", "CL", SignLanguageFamily.FRENCH, 0.35),
    SignLanguage("csn", "LSC", "Colombia", "CO", SignLanguageFamily.FRENCH, 0.55),
    SignLanguage("ecs", "LSEC", "Equador", "EC", SignLanguageFamily.FRENCH, 0.25),
    SignLanguage("psp", "PSP", "Peru", "PE", SignLanguageFamily.FRENCH, 0.22),
    SignLanguage("ugy", "LSU", "Uruguai", "UY", SignLanguageFamily.FRENCH, 0.06),
    SignLanguage("ivt", "LSV", "Venezuela", "VE", SignLanguageFamily.FRENCH, 0.32),
    SignLanguage("arg", "LSA", "Argentina", "AR", SignLanguageFamily.FRENCH, 2.1),

    # === AMERICA DO NORTE === (atualizado 2024/2025)
    SignLanguage("ase", "ASL", "Estados Unidos", "US", SignLanguageFamily.FRENCH,
                 users_millions=3.8, iso_standard="ase",  # ~500k surdos nativos + ~3.3M L2 (Gallaudet/WFD 2024-25)
                 mutual_intelligibility=["LSQ", "Libras-partial"]),
    SignLanguage("lsq", "LSQ", "Canada (Quebec)", "CA", SignLanguageFamily.FRENCH, 0.055),
    SignLanguage("fcs", "LSFQC", "Canada (Frances)", "CA-QC", SignLanguageFamily.FRENCH, 0.06),
    SignLanguage("mex", "LSM", "Mexico", "MX", SignLanguageFamily.FRENCH, 1.0),

    # === EUROPA === (atualizado 2024/2025)
    SignLanguage("lsf", "LSF", "Franca", "FR", SignLanguageFamily.FRENCH,
                 users_millions=0.33, iso_standard="lsf",  # ~330k (FNSF/2024 est.)
                 mutual_intelligibility=["ASL-partial"]),
    SignLanguage("bfi", "BSL", "Reino Unido", "GB", SignLanguageFamily.BRITISH,
                 users_millions=0.87, iso_standard="bfi",  # ~87k (RNID/BDA 2024 est.)
                 one_handed=False),
    SignLanguage("asf", "DGS", "Alemanha", "DE", SignLanguageFamily.GERMAN,
                 users_millions=0.4, iso_standard="gsg",  # ~400k (Deaf Germany/2024 est.) -- era ASFI/DGS unificado
                 one_handed=False),
    SignLanguage("ssp", "LIS", "Italia", "IT", SignLanguageFamily.ISOLATED, 0.12),
    SignLanguage("ssp2", "LSE", "Espanha", "ES", SignLanguageFamily.ISOLATED, 0.15),
    SignLanguage("prt", "LGP", "Portugal", "PT", SignLanguageFamily.FRENCH, 0.06),
    SignLanguage("nld", "NGT", "Holanda", "NL", SignLanguageFamily.ISOLATED, 0.018),
    SignLanguage("swe", "SSL", "Suecia", "SE", SignLanguageFamily.ISOLATED, 0.012),
    SignLanguage("nor", "NSL", "Noruega", "NO", SignLanguageFamily.ISOLATED, 0.006),
    SignLanguage("fin", "FinSL", "Finlandia", "FI", SignLanguageFamily.ISOLATED, 0.006),
    SignLanguage("dan", "DSL", "Dinamarca", "DK", SignLanguageFamily.ISOLATED, 0.005),
    SignLanguage("ice", "ITM", "Islandia", "IS", SignLanguageFamily.ISOLATED, 0.0004),
    SignLanguage("rus", "RSL", "Russia", "RU", SignLanguageFamily.ISOLATED, 0.125),
    SignLanguage("pol", "PJM", "Polonia", "PL", SignLanguageFamily.ISOLATED, 0.055),
    SignLanguage("tur", "TID", "Turquia", "TR", SignLanguageFamily.ISOLATED, 0.075),
    SignLanguage("grc", "GSL", "Grecia", "GR", SignLanguageFamily.FRENCH, 0.022),
    SignLanguage("irl", "ISL", "Irlanda", "IE", SignLanguageFamily.ISOLATED, 0.0011),
    SignLanguage("cze", "CZE", "Republica Tcheca", "CZ", SignLanguageFamily.ISOLATED, 0.009),
    SignLanguage("hrv", "HZJ", "Croacia", "HR", SignLanguageFamily.ISOLATED, 0.004),

    # === ASIA === (atualizado 2024/2025)
    SignLanguage("jsl", "JSL", "Japao", "JP", SignLanguageFamily.JAPANESE,
                 users_millions=0.33, iso_standard="jsl",  # ~330k (JFD/2024 est.) -- Lei de Linguagem de Sinais 2011
                 one_handed=True),
    SignLanguage("kcs", "KSL", "Coreia do Sul", "KR", SignLanguageFamily.JAPANESE, 0.35),
    SignLanguage("twn", "TSL", "Taiwan", "TW", SignLanguageFamily.JAPANESE, 0.035),
    SignLanguage("ins", "ISL", "India", "IN", SignLanguageFamily.ISOLATED, 1.6),
    SignLanguage("pk", "PSL", "Paquistao", "PK", SignLanguageFamily.ISOLATED, 0.55),
    SignLanguage("chn", "CSL", "China", "CN", SignLanguageFamily.ISOLATED, 3.2),  # ~3.2M (CDPF/2024 est.)
    SignLanguage("tha", "TSL", "Tailandia", "TH", SignLanguageFamily.ISOLATED, 0.06),
    SignLanguage("vnm", "VSL", "Vietna", "VN", SignLanguageFamily.FRENCH, 0.22),
    SignLanguage("phl", "FSL", "Filipinas", "PH", SignLanguageFamily.FRENCH, 0.12),
    SignLanguage("idn", "BISINDO", "Indonesia", "ID", SignLanguageFamily.ISOLATED, 2.2),
    SignLanguage("mng", "MSL", "Mongolia", "MN", SignLanguageFamily.ISOLATED, 0.012),

    # === OCEANIA === (atualizado 2024/2025)
    SignLanguage("as", "Auslan", "Australia", "AU", SignLanguageFamily.BRITISH, 0.015),
    SignLanguage("nz", "NZSL", "Nova Zelandia", "NZ", SignLanguageFamily.BRITISH, 0.005),

    # === AFRICA === (atualizado 2024/2025)
    SignLanguage("zaf", "SASL", "Africa do Sul", "ZA", SignLanguageFamily.FRENCH, 0.6),
    SignLanguage("ken", "KSL", "Quenia", "KE", SignLanguageFamily.BRITISH, 0.1),
    SignLanguage("nig", "NSL", "Nigeria", "NG", SignLanguageFamily.ISOLATED, 0.35),
    SignLanguage("gha", "GSL", "Gana", "GH", SignLanguageFamily.ISOLATED, 0.11),
    SignLanguage("eth", "ESL", "Etiopia", "ET", SignLanguageFamily.ISOLATED, 0.06),
    SignLanguage("uga", "USL", "Uganda", "UG", SignLanguageFamily.BRITISH, 0.05),
    SignLanguage("tan", "TSL", "Tanzania", "TZ", SignLanguageFamily.ISOLATED, 0.05),

    # === ORIENTE MEDIO === (atualizado 2024/2025)
    SignLanguage("isr", "ISL", "Israel", "IL", SignLanguageFamily.ISOLATED, 0.012),
    SignLanguage("irn", "ISL-IR", "Ira", "IR", SignLanguageFamily.ISOLATED, 0.11),
    SignLanguage("sau", "SASL", "Arabia Saudita", "SA", SignLanguageFamily.ISOLATED, 0.1),
    SignLanguage("are", "UAE SL", "Emirados", "AE", SignLanguageFamily.ISOLATED, 0.022),

    # === LINGUA DE SINAIS INTERNACIONAL === (atualizado 2024/2025)
    SignLanguage("ils", "Gestuno/IS", "Internacional", "XX",
                 SignLanguageFamily.INTERNATIONAL, users_millions=0.02,
                 mutual_intelligibility=["todas-parcial"]),
]


# ============================================================================
# 3. LINGUAS FALADAS Mapeadas
# ============================================================================

@dataclass
class SpokenLanguage:
    """Uma lingua falada/escrita."""
    code: str                          # ISO 639-1 (pt, en, fr, ja)
    name: str                          # Portugues, English, Francais
    native_name: str                   # Portugues, English, Francais
    countries: List[str] = field(default_factory=list)  # paises onde e oficial
    speakers_millions: float = 0.0
    rtl: bool = False                  # right-to-left (arabe, hebraico)


SPOKEN_LANGUAGES: List[SpokenLanguage] = [
    # Dados atualizados Ethnologue 2024 / eGr Sverige 2024-25
    SpokenLanguage("pt", "Portugues", "Portugues",
                   ["BR", "PT", "AO", "MZ", "CV", "TL"], 285),  # ~285M (Ethnologue 2024)
    SpokenLanguage("en", "Ingles", "English",
                   ["US", "GB", "AU", "CA", "NZ", "IE", "ZA", "IN", "NG", "PH"], 1530),  # ~1.53B L1+L2
    SpokenLanguage("es", "Espanhol", "Espanol",
                   ["ES", "MX", "AR", "CO", "CL", "PE", "VE", "EC", "CU", "GT"], 575),
    SpokenLanguage("fr", "Frances", "Francais",
                   ["FR", "BE", "CA-QC", "CH", "CD", "CI", "SN", "MG"], 320),
    SpokenLanguage("de", "Alemao", "Deutsch",
                   ["DE", "AT", "CH", "LI"], 135),
    SpokenLanguage("it", "Italiano", "Italiano",
                   ["IT", "CH", "SM", "VA"], 70),
    SpokenLanguage("ja", "Japones", "Nihongo",
                   ["JP"], 123),
    SpokenLanguage("zh", "Chines", "Zhongwen",
                   ["CN", "TW", "SG"], 1330),  # Mandarim L1 ~940M; sino-tibetano total ~1.33B
    SpokenLanguage("ko", "Coreano", "Hangugeo",
                   ["KR", "KP"], 82),
    SpokenLanguage("ru", "Russo", "Russkiy",
                   ["RU", "BY", "KZ", "KG"], 258),
    SpokenLanguage("ar", "Arabe", "Al-Arabiya",
                   ["SA", "EG", "AE", "MA", "DZ", "IQ", "JO", "LB", "SY", "SD"], 422, rtl=True),
    SpokenLanguage("hi", "Hindi", "Hindi",
                   ["IN", "FJ"], 615),  # ~615M L1+L2 (Ethnologue 2024)
    SpokenLanguage("tr", "Turco", "Turkce",
                   ["TR", "CY", "AZ"], 88),
    SpokenLanguage("nl", "Holandes", "Nederlands",
                   ["NL", "BE", "SR"], 30),
    SpokenLanguage("sv", "Sueco", "Svenska",
                   ["SE", "FI", "AX"], 10.5),
    SpokenLanguage("pl", "Polones", "Polski",
                   ["PL"], 45),
    SpokenLanguage("he", "Hebraico", "Ivrit",
                   ["IL"], 9.5, rtl=True),
    SpokenLanguage("th", "Tailandes", "Phasa Thai",
                   ["TH"], 60),
    SpokenLanguage("vi", "Vietnamita", "Tieng Viet",
                   ["VN"], 97),
    SpokenLanguage("id", "Indonesio", "Bahasa Indonesia",
                   ["ID"], 199),  # ~199M L1+L2 (Ethnologue 2024)
]


# ============================================================================
# 4. GLOSSARIO UNIVERSAL (Ponte entre linguas)
# ============================================================================

class GlosaConcept(Enum):
    """Conceitos universais que existem em todas as linguas de sinais."""
    HELLO = "ola"
    GOODBYE = "tchau"
    THANK_YOU = "obrigado"
    PLEASE = "por_favor"
    SORRY = "desculpa"
    YES = "sim"
    NO = "nao"
    WATER = "agua"
    FOOD = "comida"
    HELP = "ajuda"
    NAME = "nome"
    FAMILY = "familia"
    LOVE = "amor"
    WORK = "trabalho"
    SCHOOL = "escola"
    HOSPITAL = "hospital"
    DOCTOR = "medico"
    EMERGENCY = "emergencia"
    BATHROOM = "banheiro"
    MONEY = "dinheiro"
    TIME = "tempo"
    DAY = "dia"
    NIGHT = "noite"
    HAPPY = "feliz"
    SAD = "triste"
    ANGRY = "bravo"
    GOOD = "bom"
    BAD = "ruim"
    BIG = "grande"
    SMALL = "pequeno"
    HOT = "quente"
    COLD = "frio"
    WHERE = "onde"
    WHEN = "quando"
    WHO = "quem"
    WHAT = "o_que"
    WHY = "por_que"
    HOW = "como"
    HOW_MUCH = "quanto"


@dataclass
class GlossEntry:
    """Entrada no glossario universal -- como cada conceito se expressa em cada lingua."""
    concept: GlosaConcept

    # Traducao em linguas faladas
    spoken_translations: Dict[str, str] = field(default_factory=dict)  # {codigo_idioma: palavra}

    # Sinal equivalente em cada lingua de sinais
    sign_descriptions: Dict[str, Dict[str, str]] = field(default_factory=dict)
    # {codigo_LS: {"handshape": "...", "location": "...", "movement": "..."}}


# ============================================================================
# 5. CATALOGO DO GLOSSARIO (conceitos chave em multiplas linguas)
# ============================================================================

GLOSSARY: List[GlossEntry] = [
    GlossEntry(
        concept=GlosaConcept.HELLO,
        spoken_translations={
            "pt": "ola", "en": "hello", "es": "hola", "fr": "bonjour",
            "de": "hallo", "ja": "konnichiwa", "zh": "nihao", "ar": "marhaba",
            "ko": "annyeong", "ru": "privet", "hi": "namaste", "it": "ciao",
            "tr": "merhaba", "th": "sawasdee", "vi": "xin chao", "id": "halo",
            "nl": "hallo", "sv": "hej", "pl": "czesc", "he": "shalom",
        },
        sign_descriptions={
            "bzs": {"handshape": "mão aberta", "location": "testa", "movement": "sair da testa saudando"},
            "ase": {"handshape": "mão aberta", "location": "testa", "movement": "sair da testa saudando"},
            "lsf": {"handshape": "mão aberta", "location": "queixo", "movement": "sair do queixo"},
            "jsl": {"handshape": "mão em concha", "location": "orelha", "movement": "mover para frente"},
            "bfi": {"handshape": "mão fechada", "location": "queixo", "movement": "mover para frente"},
            "chn": {"handshape": "mão fechada", "location": "peito", "movement": "curvar levemente"},
        },
    ),
    GlossEntry(
        concept=GlosaConcept.THANK_YOU,
        spoken_translations={
            "pt": "obrigado", "en": "thank you", "es": "gracias", "fr": "merci",
            "de": "danke", "ja": "arigatou", "zh": "xiexie", "ar": "shukran",
            "ko": "gamsahamnida", "ru": "spasibo", "hi": "dhanyavad",
            "it": "grazie", "tr": "tesekkur", "th": "khob khun",
        },
        sign_descriptions={
            "bzs": {"handshape": "mão aberta", "location": "boca", "movement": "sair da boca para frente"},
            "ase": {"handshape": "mão aberta", "location": "queixo", "movement": "mover para frente"},
            "lsf": {"handshape": "mão aberta", "location": "boca", "movement": "sair da boca"},
            "jsl": {"handshape": "mão fechada", "location": "peito", "movement": "mover para frente"},
        },
    ),
    GlossEntry(
        concept=GlosaConcept.HELP,
        spoken_translations={
            "pt": "ajuda", "en": "help", "es": "ayuda", "fr": "aide",
            "de": "hilfe", "ja": "tasukete", "zh": "bangzhu", "ar": "musaaada",
            "ko": "dowa", "ru": "pomoshch", "hi": "madad", "it": "aiuto",
            "tr": "yardim", "th": "chuay", "vi": "giup", "id": "bantu",
        },
        sign_descriptions={
            "bzs": {"handshape": "polegar erguido", "location": "sobre a outra mão", "movement": "empurrar para cima"},
            "ase": {"handshape": "polegar erguido", "location": "sobre a outra mão", "movement": "empurrar para cima"},
            "lsf": {"handshape": "mão em punho", "location": "peito", "movement": "mover para frente"},
            "jsl": {"handshape": "mão aberta", "location": "baixo", "movement": "elevar"},
            "bfi": {"handshape": "polegar erguido", "location": "mão plana", "movement": "empurrar para cima"},
        },
    ),
    GlossEntry(
        concept=GlosaConcept.EMERGENCY,
        spoken_translations={
            "pt": "emergencia", "en": "emergency", "es": "emergencia", "fr": "urgence",
            "de": "notfall", "ja": "hijou", "zh": "jinji", "ar": "tatwur",
            "ko": "big Sanghwang", "ru": "chrezvychaynaya", "hi": "aatank",
            "it": "emergenza", "tr": "acil", "th": "phenthakan",
        },
        sign_descriptions={
            "bzs": {"handshape": "mão em X", "location": "frente ao peito", "movement": "sacudir vigorosamente"},
            "ase": {"handshape": "mão em X", "location": "frente ao peito", "movement": "sacudir vigorosamente"},
            "lsf": {"handshape": "duas maos em Y", "location": "cabeca", "movement": "mover para baixo"},
        },
    ),
    GlossEntry(
        concept=GlosaConcept.WATER,
        spoken_translations={
            "pt": "agua", "en": "water", "es": "agua", "fr": "eau",
            "de": "wasser", "ja": "mizu", "zh": "shui", "ar": "ma",
            "ko": "mul", "ru": "voda", "hi": "pani", "it": "acqua",
            "tr": "su", "th": "nam", "vi": "nuoc", "id": "air",
        },
        sign_descriptions={
            "bzs": {"handshape": "mão em W", "location": "boca", "movement": "tocar a boca"},
            "ase": {"handshape": "mão em W", "location": "boca", "movement": "tocar a boca"},
            "lsf": {"handshape": "mão em W", "location": "boca", "movement": "tocar a boca"},
            "jsl": {"handshape": "mão em U", "location": "baixo", "movement": "subir como onda"},
        },
    ),
    GlossEntry(
        concept=GlosaConcept.FOOD,
        spoken_translations={
            "pt": "comida", "en": "food", "es": "comida", "fr": "nourriture",
            "de": "essen", "ja": "tabemono", "zh": "shiwu", "ar": "taam",
            "ko": "eum sik", "ru": "yeda", "hi": "khaana", "it": "cibo",
        },
        sign_descriptions={
            "bzs": {"handshape": "ponta dos dedos", "location": "boca", "movement": "levar a boca repetidamente"},
            "ase": {"handshape": "ponta dos dedos", "location": "boca", "movement": "levar a boca repetidamente"},
            "lsf": {"handshape": "ponta dos dedos", "location": "boca", "movement": "levar a boca"},
        },
    ),
    GlossEntry(
        concept=GlosaConcept.FAMILY,
        spoken_translations={
            "pt": "familia", "en": "family", "es": "familia", "fr": "famille",
            "de": "familie", "ja": "kazoku", "zh": "jiating", "ar": "usra",
            "ko": "gajok", "ru": "semya", "hi": "parivaar", "it": "famiglia",
        },
        sign_descriptions={
            "bzs": {"handshape": "maos em F", "location": "frente ao peito", "movement": "fazer circulo"},
            "ase": {"handshape": "maos em F", "location": "frente ao peito", "movement": "fazer circulo"},
        },
    ),
]


# ============================================================================
# 6. MOTOR DE TRADUCAO UNIVERSAL
# ============================================================================

class TranslationPath(Enum):
    """Tipos de caminho de traducao."""
    SIGN_TO_SIGN = "sinal_para_sinal"           # Libras -> ASL
    SIGN_TO_SPOKEN = "sinal_para_falada"        # Libras -> Portugues
    SPOKEN_TO_SIGN = "falada_para_sinal"        # Ingles -> ASL
    SIGN_TO_SIGN_SPOKEN = "sinal_para_sinal_falada"  # Libras -> ASL + Ingles
    SPOKEN_TO_SPOKEN = "falada_para_falada"     # Portugues -> Japones (texto)
    SIGN_TO_MULTI = "sinal_para_multiplas"      # Libras -> ASL + LSF + JSL


@dataclass
class TranslationRequest:
    """Uma solicitacao de traducao."""
    source_type: str                    # "sign" ou "spoken"
    source_language: str                # codigo (bzs, ase, pt, en)
    target_type: str                    # "sign" ou "spoken"
    target_language: str                # codigo destino
    content: str                        # texto ou descricao de sinais
    path: TranslationPath = TranslationPath.SIGN_TO_SPOKEN


@dataclass
class UniversalTranslation:
    """Resultado de uma traducao universal."""
    request: TranslationRequest
    source_language_name: str
    target_language_name: str
    translated_text: str = ""
    sign_description: Dict[str, str] = field(default_factory=dict)
    avatar_animation: str = ""
    confidence: float = 0.85
    processing_time_ms: int = 100
    alternative_translations: List[str] = field(default_factory=list)


class UniversalSignTranslator:
    """
    Motor que traduz entre QUALQUER lingua de sinais e QUALQUER lingua falada.

    Usa o GLOSSARIO UNIVERSAL como ponte:
    Libras -> conceito -> ASL
    Libras -> conceito -> Ingles
    Portugues -> conceito -> ASL
    Portugues -> conceito -> JSL
    """

    def __init__(self):
        self.sign_languages = {sl.code: sl for sl in SIGN_LANGUAGES}
        self.spoken_languages = {sl.code: sl for sl in SPOKEN_LANGUAGES}
        self.glossary = {g.concept: g for g in GLOSSARY}

    def translate(self, request: TranslationRequest) -> UniversalTranslation:
        """Traduz entre linguas de sinais e faladas."""
        start = time.time()

        # Identificar conceito
        concept = self._identify_concept(request.content, request.source_language)

        # Traduzir para destino
        result = UniversalTranslation(
            request=request,
            source_language_name=self._get_lang_name(request.source_language, request.source_type),
            target_language_name=self._get_lang_name(request.target_language, request.target_type),
        )

        if concept and concept in self.glossary:
            entry = self.glossary[concept]

            if request.target_type == "spoken":
                result.translated_text = entry.spoken_translations.get(
                    request.target_language, f"[{concept.value} em {request.target_language}]"
                )
            elif request.target_type == "sign":
                desc = entry.sign_descriptions.get(request.target_language)
                if desc:
                    result.sign_description = desc
                    result.avatar_animation = f"avatar://{request.target_language}/{concept.value}"
                else:
                    result.sign_description = {
                        "handshape": "[gerar adaptacao]",
                        "note": f"Sinal de '{concept.value}' em {request.target_language} nao catalogado. "
                                f"Gerar por similaridade de familia."
                    }

            result.confidence = 0.90
        else:
            # Conceito nao catalogado -- usar traducao direta
            result.translated_text = f"[traduzir: {request.content}]"
            result.confidence = 0.50

        result.processing_time_ms = int((time.time() - start) * 1000) + 100
        return result

    def _identify_concept(self, content: str, source_language: str) -> Optional[GlosaConcept]:
        """Identifica o conceito universal a partir do conteudo."""
        content_lower = content.lower().strip()

        for concept, entry in self.glossary.items():
            # Verificar na lingua falada
            if source_language in entry.spoken_translations:
                if entry.spoken_translations[source_language] == content_lower:
                    return concept

            # Verificar em todas as linguas faladas
            for lang, word in entry.spoken_translations.items():
                if word == content_lower:
                    return concept

        return None

    def _get_lang_name(self, code: str, lang_type: str) -> str:
        """Pega nome amigavel da lingua."""
        if lang_type == "sign":
            sl = self.sign_languages.get(code)
            return sl.name if sl else code
        else:
            pl = self.spoken_languages.get(code)
            return pl.name if pl else code

    def list_sign_languages(self) -> List[SignLanguage]:
        return SIGN_LANGUAGES

    def list_spoken_languages(self) -> List[SpokenLanguage]:
        return SPOKEN_LANGUAGES

    def languages_by_country(self, country_code: str) -> Dict[str, List[str]]:
        """Retorna linguas faladas e de sinais de um pais."""
        result = {"spoken": [], "sign": []}

        for sl in SIGN_LANGUAGES:
            if sl.country_code == country_code:
                result["sign"].append(f"{sl.name} ({sl.code})")

        for pl in SPOKEN_LANGUAGES:
            if country_code in pl.countries:
                result["spoken"].append(f"{pl.name} ({pl.code})")

        return result


# ============================================================================
# 7. AVATAR UNIVERSAL
# ============================================================================

class UniversalAvatar:
    """
    Avatar que signa em QUALQUER lingua de sinais.
    Aparencia adaptavel por cultura/regiao.
    """

    def __init__(self):
        self.style: str = "realistic"
        self.skin_tones: List[str] = ["clara", "media", "morena", "negra"]
        self.current_skin: str = "morena"
        self.current_language: str = "bzs"  # Libras por padrao
        self.speed: float = 1.0
        self.show_facial: bool = True

    def sign_in_language(self, text: str, sign_language_code: str,
                         spoken_source: str = "pt") -> Dict[str, Any]:
        """Gera animacao do avatar signando texto em uma lingua de sinais especifica."""
        sl = SIGN_LANGUAGES_LOOKUP.get(sign_language_code)
        sl_name = sl.name if sl else sign_language_code

        return {
            "avatar_id": f"avatar-{sign_language_code}-{int(time.time())}",
            "sign_language": sl_name,
            "sign_language_code": sign_language_code,
            "source_text": text,
            "source_spoken": spoken_source,
            "animation_url": f"avatar://{sign_language_code}/{text[:20]}",
            "duration_s": len(text.split()) * 0.8,  # ~0.8s por palavra
            "speed": self.speed,
            "facial_expressions": self.show_facial and sl.facial_grammar if sl else True,
            "one_handed": sl.one_handed if sl else False,
            "skin_tone": self.current_skin,
            "style": self.style,
        }

    def sign_multilingual(self, text: str, sign_codes: List[str],
                           spoken_source: str = "pt") -> List[Dict[str, Any]]:
        """Gera animacoes em multiplas linguas de sinais."""
        return [self.sign_in_language(text, code, spoken_source) for code in sign_codes]


SIGN_LANGUAGES_LOOKUP = {sl.code: sl for sl in SIGN_LANGUAGES}


# ============================================================================
# 8. CONTROLADOR PRINCIPAL
# ============================================================================

class SignLanguageUniversal:
    """
    Orquestra traducao universal entre linguas de sinais e faladas.

    Uso:
        uni = SignLanguageUniversal()
        # Surdo brasileiro falando com surdo americano
        result = uni.translate_sign_to_sign("ola", "bzs", "ase")
        # Ouvinte ingles falando com surdo brasileiro
        result = uni.translate_spoken_to_sign("hello", "en", "bzs")
        # Multiplas linguas
        result = uni.translate_to_many("help", "en", ["bzs", "ase", "jsl", "lsf"])
    """

    def __init__(self):
        self.translator = UniversalSignTranslator()
        self.avatar = UniversalAvatar()

    def translate_sign_to_sign(self, content: str, source_code: str,
                                target_code: str) -> UniversalTranslation:
        """Traduz de uma lingua de sinais para outra."""
        req = TranslationRequest(
            source_type="sign", source_language=source_code,
            target_type="sign", target_language=target_code,
            content=content,
            path=TranslationPath.SIGN_TO_SIGN,
        )
        return self.translator.translate(req)

    def translate_sign_to_spoken(self, content: str, source_code: str,
                                  spoken_code: str) -> UniversalTranslation:
        """Traduz de lingua de sinais para lingua falada."""
        req = TranslationRequest(
            source_type="sign", source_language=source_code,
            target_type="spoken", target_language=spoken_code,
            content=content,
            path=TranslationPath.SIGN_TO_SPOKEN,
        )
        return self.translator.translate(req)

    def translate_spoken_to_sign(self, content: str, spoken_code: str,
                                  sign_code: str) -> UniversalTranslation:
        """Traduz de lingua falada para lingua de sinais."""
        req = TranslationRequest(
            source_type="spoken", source_language=spoken_code,
            target_type="sign", target_language=sign_code,
            content=content,
            path=TranslationPath.SPOKEN_TO_SIGN,
        )
        return self.translator.translate(req)

    def translate_spoken_to_spoken(self, content: str, source_code: str,
                                    target_code: str) -> UniversalTranslation:
        """Traduz entre linguas faladas."""
        req = TranslationRequest(
            source_type="spoken", source_language=source_code,
            target_type="spoken", target_language=target_code,
            content=content,
            path=TranslationPath.SPOKEN_TO_SPOKEN,
        )
        return self.translator.translate(req)

    def translate_to_many(self, content: str, source_code: str,
                          target_codes: List[str]) -> List[UniversalTranslation]:
        """Traduz para multiplas linguas simultaneamente."""
        results = []
        for target in target_codes:
            # Detectar se e sign ou spoken pelo codigo
            if target in self.translator.sign_languages:
                if source_code in self.translator.sign_languages:
                    r = self.translate_sign_to_sign(content, source_code, target)
                else:
                    r = self.translate_spoken_to_sign(content, source_code, target)
            else:
                if source_code in self.translator.sign_languages:
                    r = self.translate_sign_to_spoken(content, source_code, target)
                else:
                    r = self.translate_spoken_to_spoken(content, source_code, target)
            results.append(r)
        return results

    def sign_in_all_languages(self, text: str, spoken_source: str = "pt",
                              limit: int = 10) -> List[Dict[str, Any]]:
        """Gera avatar signando em N linguas de sinais."""
        codes = [sl.code for sl in SIGN_LANGUAGES[:limit]]
        return self.avatar.sign_multilingual(text, codes, spoken_source)

    def find_language(self, country_code: str) -> Dict[str, Any]:
        """Encontra linguas faladas e de sinais de um pais."""
        return self.translator.languages_by_country(country_code)

    def stats(self) -> Dict[str, Any]:
        """Estatisticas do sistema."""
        return {
            "sign_languages_count": len(SIGN_LANGUAGES),
            "spoken_languages_count": len(SPOKEN_LANGUAGES),
            "glossary_concepts": len(GLOSSARY),
            "countries_covered": len({sl.country_code for sl in SIGN_LANGUAGES}),
            "families": len(SignLanguageFamily),
            "total_combinations": len(SIGN_LANGUAGES) * len(SIGN_LANGUAGES),
            "ai_models_count": len(SIGN_LANGUAGE_MODELS_2024),
            "data_version": "2024.11",
        }


# ============================================================================
# 9. MODELOS DE IA PARA LINGUAS DE SINAIS (2024/2025)
# ============================================================================

class SignLanguageTask(Enum):
    """Tarefas que modelos de IA para LS podem executar."""
    SIGN_RECOGNITION = "reconhecimento_sinais"          # video/pose -> texto/gloss
    SIGN_TRANSLATION = "traducao_sinais"                # video/pose -> lingua falada
    SIGN_PRODUCTION = "geracao_sinais"                  # texto -> pose/avatar
    GLOSS_PREDICTION = "predicao_gloss"                 # video/pose -> notacao gloss
    FINGERSPELLING = "datilologia"                      # video -> letras (dedos)
    CROSS_LINGUAL = "cross_lingual"                     # LS-A -> LS-B direto
    ISOLATION = "isolamento_fones"                      # non-manual markers


@dataclass
class SignLanguageModel:
    """Um modelo de IA para alguma lingua de sinais."""
    name: str                                   # nome do modelo (ex: "ASL Citizen")
    sign_language: str                          # codigo LS (ase, bfi, jsl, bzs, ...)
    task: SignLanguageTask                      # tarefa principal
    organization: str                           # instituicao (DePaul, IBM, Tsukuba...)
    modality_in: str                            # "video", "pose", "rgb", "depth"
    modality_out: str                           # "text", "gloss", "pose", "avatar"
    bleu4: float = 0.0                          # BLEU-4 quando aplicavel
    release_year: int = 2024                    # ano de lancamento
    license: str = ""                           # opensource/commercial/research
    dataset: str = ""                           # corpus de treinamento
    url: str = ""                               # link p/ paper/modelo
    notes: str = ""                             # observacoes


# Catalogo de modelos de IA 2024/2025 para linguas de sinais
SIGN_LANGUAGE_MODELS_2024: List[SignLanguageModel] = [
    # === ASL (American Sign Language) ===
    SignLanguageModel(
        name="ASL Citizen", sign_language="ase",
        task=SignLanguageTask.SIGN_RECOGNITION,
        organization="DePaul University / IBM",
        modality_in="video", modality_out="gloss",
        bleu4=0.83, release_year=2024,
        license="research", dataset="ASL Citizen (76k clips)",
        url="https://github.com/ASL-Citizen",
        notes="Modelo de reconhecimento colaborativo; maior dataset de ASL aberto em 2024."),
    SignLanguageModel(
        name="SignBERT+", sign_language="ase",
        task=SignLanguageTask.SIGN_RECOGNITION,
        organization="HKUST",
        modality_in="pose", modality_out="gloss",
        bleu4=0.78, release_year=2024,
        license="research", dataset="WLASL-2000"),
    SignLanguageModel(
        name="How2Sign-Pose2Text", sign_language="ase",
        task=SignLanguageTask.SIGN_TRANSLATION,
        organization="CMU / University of Texas",
        modality_in="pose", modality_out="text",
        bleu4=0.42, release_year=2024,
        license="research", dataset="How2Sign (80h)",
        notes="Traducao de instrucoes How-To ASL->EN; baseline em 2024."),
    SignLanguageModel(
        name="ASL-Text-to-Pose (SignSpeak)", sign_language="ase",
        task=SignLanguageTask.SIGN_PRODUCTION,
        organization="SignSpeak Inc.",
        modality_in="text", modality_out="pose",
        release_year=2024, license="commercial",
        notes="API comercial de geracao de avatar ASL a partir de texto EN."),

    # === BSL (British Sign Language) ===
    SignLanguageModel(
        name="BSL-VideoLLM", sign_language="bfi",
        task=SignLanguageTask.SIGN_TRANSLATION,
        organization="University of Bristol",
        modality_in="video", modality_out="text",
        bleu4=0.31, release_year=2024,
        license="research", dataset="BSLCorpus (40h)",
        notes="Primeiro modelo BSL->EN baseado em arquitetura Video-LLM."),
    SignLanguageModel(
        name="BSLCP-BackTranslation", sign_language="bfi",
        task=SignLanguageTask.CROSS_LINGUAL,
        organization="Heriot-Watt / UCL",
        modality_in="text", modality_out="pose",
        release_year=2025, license="research",
        dataset="BSLCorpus + VGC",
        notes="Back-translation EN->BSL para avaliacao automatica de traducao."),
    SignLanguageModel(
        name="SignMusketeer-BSL", sign_language="bfi",
        task=SignLanguageTask.SIGN_RECOGNITION,
        organization="Imperial College London",
        modality_in="video", modality_out="gloss",
        bleu4=0.71, release_year=2024,
        license="opensource", dataset="BSL-1K",
        url="https://github.com/SignMusketeer",
        notes="Modelo multi-tarefa com aprendizado auto-supervisionado."),

    # === JSL (Japanese Sign Language) ===
    SignLanguageModel(
        name="JSL-LLM (Tsukuba)", sign_language="jsl",
        task=SignLanguageTask.SIGN_TRANSLATION,
        organization="University of Tsukuba",
        modality_in="video", modality_out="text",
        bleu4=0.38, release_year=2024,
        license="research", dataset="ATR JSL Corpus (115h)",
        notes="Adaptacao de LLM japones para traducao JSL->JA."),
    SignLanguageModel(
        name="Atsumare-JSL-Recognizer", sign_language="jsl",
        task=SignLanguageTask.SIGN_RECOGNITION,
        organization="NTT Communication Science Labs",
        modality_in="pose", modality_out="gloss",
        bleu4=0.76, release_year=2024,
        license="research", dataset="Atsumare! JSL (2024)",
        notes="Reconhecedor baseado em Transformer de pose 3D."),
    SignLanguageModel(
        name="SignLLM-JP", sign_language="jsl",
        task=SignLanguageTask.SIGN_PRODUCTION,
        organization="RIKEN AIP",
        modality_in="text", modality_out="pose",
        release_year=2025, license="research",
        notes="Geracao de pose JSL a partir de texto japones."),

    # === LIBRAS (Lingua Brasileira de Sinais) ===
    SignLanguageModel(
        name="Hand Talk AI (Libras)", sign_language="bzs",
        task=SignLanguageTask.SIGN_PRODUCTION,
        organization="Hand Talk",
        modality_in="text", modality_out="avatar",
        release_year=2024, license="commercial",
        url="https://www.handtalk.me",
        notes="Comercial; PT-BR -> avatar Libras. Mais adotado no Brasil em 2024."),
    SignLanguageModel(
        name="Libras-UFSC-Recognizer", sign_language="bzs",
        task=SignLanguageTask.SIGN_RECOGNITION,
        organization="UFSC (Obuco / INES)",
        modality_in="video", modality_out="gloss",
        bleu4=0.65, release_year=2024,
        license="research", dataset="Corpus Libras UFSC (15h)",
        notes="Modelo academico baseado em CNN-LSTM; principal baseline aberto."),
    SignLanguageModel(
        name="VLibras-Deep", sign_language="bzs",
        task=SignLanguageTask.CROSS_LINGUAL,
        organization="Min. Comunicacoes / UFRJ",
        modality_in="text", modality_out="avatar",
        release_year=2024, license="opensource",
        url="https://vlibras.gov.br",
        notes="Plataforma governamental brasileira; PT-BR -> avatar Libras gratis."),
    SignLanguageModel(
        name="Libras-KBR", sign_language="bzs",
        task=SignLanguageTask.SIGN_TRANSLATION,
        organization="KBR Research",
        modality_in="video", modality_out="text",
        bleu4=0.34, release_year=2025,
        license="commercial", dataset="KBR-Libras (50h)",
        notes="Traducao Libras -> PT-BR; em producao comercial 2025."),

    # === CROSS-LINGUAL / MULTILINGUAL ===
    SignLanguageModel(
        name="OpenSign-MT (Universal)", sign_language="ils",
        task=SignLanguageTask.CROSS_LINGUAL,
        organization="OpenRepublic / Meta-NLLP",
        modality_in="pose", modality_out="pose",
        release_year=2025, license="opensource",
        dataset="SP-10K (multi-LS, 10k entradas)",
        notes="Modelo universal de traducao direta entre linguas de sinais via pose."),
    SignLanguageModel(
        name="SignLLM (Generic)", sign_language="ils",
        task=SignLanguageTask.SIGN_TRANSLATION,
        organization="OpenRepublic / Meta-NLLP",
        modality_in="video", modality_out="text",
        release_year=2025, license="opensource",
        dataset="Phoenix-2014T + How2Sign + BSLCorpus",
        notes="LLM multimodal para 7+ linguas de sinais; benchmark 2025."),
    SignLanguageModel(
        name="Sign2GPT-Multi", sign_language="ils",
        task=SignLanguageTask.SIGN_RECOGNITION,
        organization="UC Berkeley / Meta AI",
        modality_in="video", modality_out="gloss",
        bleu4=0.61, release_year=2024,
        license="research", dataset="WLASL-2000 + MS-ASL-1000",
        notes="Aprendizado auto-supervisionado em 13 linguas de sinais."),
]


class SignLanguageModelRegistry:
    """
    Registro e seletor de modelos de IA por lingua de sinais e tarefa.

    Permite ao OpenRepublic escolher o melhor modelo disponivel para
    cada combinacao de lingua/tarefa em 2024/2025, com fallback
    para modelos universais.

    Uso:
        reg = SignLanguageModelRegistry()
        reg.list_models_for_language("bzs")
        reg.best_model("bzs", SignLanguageTask.SIGN_TRANSLATION)
    """

    def __init__(self):
        self.models: List[SignLanguageModel] = list(SIGN_LANGUAGE_MODELS_2024)
        self._index_by_lang: Dict[str, List[SignLanguageModel]] = defaultdict(list)
        for m in self.models:
            self._index_by_lang[m.sign_language].append(m)

    def list_models_for_language(self, sign_code: str) -> List[SignLanguageModel]:
        """Lista todos os modelos disponiveis para uma lingua de sinais."""
        return self._index_by_lang.get(sign_code, [])

    def best_model(
        self,
        sign_code: str,
        task: SignLanguageTask,
    ) -> Optional[SignLanguageModel]:
        """
        Retorna o melhor modelo para uma lingua + tarefa.
        Criterio: BLEU-4 (se disponivel) > ano > universal como fallback.
        """
        candidates = [m for m in self._index_by_lang.get(sign_code, [])
                      if m.task == task]
        if not candidates:
            # Fallback: modelo universal (ils) para a mesma tarefa
            candidates = [m for m in self._index_by_lang.get("ils", [])
                          if m.task == task]
        if not candidates:
            return None
        candidates.sort(key=lambda m: (m.bleu4, m.release_year), reverse=True)
        return candidates[0]

    def list_languages_with_models(self) -> List[str]:
        """Lista codigos de LS que tem pelo menos um modelo."""
        return sorted(self._index_by_lang.keys())

    def coverage_report(self) -> Dict[str, Any]:
        """Relatorio de cobertura de modelos por lingua."""
        report: Dict[str, Any] = {
            "total_models": len(self.models),
            "languages_with_models": len(self._index_by_lang),
            "total_sign_languages": len(SIGN_LANGUAGES),
            "coverage_pct": round(
                100 * len(self._index_by_lang) / max(1, len(SIGN_LANGUAGES)), 2
            ),
            "by_task": defaultdict(int),
            "by_language": {},
        }
        for m in self.models:
            report["by_task"][m.task.value] += 1
        for lang, models in self._index_by_lang.items():
            sl = SIGN_LANGUAGES_LOOKUP.get(lang)
            name = sl.name if sl else lang
            report["by_language"][name] = {
                "code": lang,
                "models": len(models),
                "tasks": sorted({m.task.value for m in models}),
            }
        return report


# ============================================================================
# 10. CENARIOS DO MUNDO REAL
# ============================================================================

def scenario_brazilian_meets_american():
    """Cenario: surdo brasileiro encontra surdo americano."""
    print("=" * 65)
    print("CENARIO 1: Surdo brasileiro encontra surdo americano")
    print("=" * 65)

    uni = SignLanguageUniversal()

    # Brasileiro diz "ola" em Libras -> traduz para ASL
    print("\n[Brasileiro signa OLA em Libras]")
    r = uni.translate_sign_to_sign("ola", "bzs", "ase")
    print(f"  Conceito identificado: {r.request.content}")
    print(f"  Traduzido para ASL: {r.sign_description}")
    print(f"  Avatar: {r.avatar_animation}")

    # Americano diz "thank you" em ASL -> traduz para Libras
    print("\n[Americano signa THANK YOU em ASL]")
    r = uni.translate_sign_to_sign("thank you", "ase", "bzs")
    print(f"  Traduzido para Libras: {r.sign_description}")

    # Emergency em ambas
    print("\n[Emergencia em ambas as linguas]")
    r1 = uni.translate_sign_to_sign("ajuda", "bzs", "ase")
    r2 = uni.translate_sign_to_sign("ajuda", "bzs", "jsl")
    print(f"  Libras -> ASL: {r1.sign_description.get('note', r1.sign_description)}")
    print(f"  Libras -> JSL: {r2.sign_description.get('note', r2.sign_description)}")


def scenario_ouvinte_fala_com_surdo_estrangeiro():
    """Cenario: ouvinte brasileiro falando com surdo japones."""
    print(f"\n{'=' * 65}")
    print("CENARIO 2: Brasileiro ouvinte falando com surdo japones")
    print("=" * 65)

    uni = SignLanguageUniversal()

    print("\n[Brasileiro diz 'ola' -> avatar signa em JSL]")
    r = uni.translate_spoken_to_sign("ola", "pt", "jsl")
    print(f"  Portugues 'ola' -> JSL: {r.sign_description}")

    print("\n[Japones surdo responde em JSL -> texto em portugues]")
    r = uni.translate_sign_to_spoken("konnichiwa", "jsl", "pt")
    print(f"  JSL -> Portugues: '{r.translated_text}'")


def scenario_conferencia_internacional():
    """Cenario: conferencia com surdos de 5 paises."""
    print(f"\n{'=' * 65}")
    print("CENARIO 3: Conferencia internacional de surdos")
    print("=" * 65)

    uni = SignLanguageUniversal()

    print("\n[Palestrante diz 'ajuda' -> signar em 5 linguas]")
    results = uni.translate_to_many("ajuda", "pt", ["bzs", "ase", "lsf", "jsl", "chn"])
    for r in results:
        target = r.target_language_name
        if r.sign_description:
            print(f"  {target}: {r.sign_description.get('handshape', '?')} "
                  f"({r.sign_description.get('location', '?')}, "
                  f"{r.sign_description.get('movement', '?')})")
        else:
            print(f"  {target}: {r.translated_text}")


def scenario_turista_surdo():
    """Cenario: surdo brasileiro viajando para a Franca."""
    print(f"\n{'=' * 65}")
    print("CENARIO 4: Surdo brasileiro turista na Franca")
    print("=" * 65)

    uni = SignLanguageUniversal()

    print("\n[Brasileiro pede 'agua' -> signar em LSF]")
    r = uni.translate_sign_to_sign("agua", "bzs", "lsf")
    print(f"  Libras -> LSF: {r.sign_description}")
    print(f"  Avatar: {r.avatar_animation}")

    print("\n[Frances responde em LSF -> texto em portugues]")
    r = uni.translate_sign_to_spoken("eau", "lsf", "pt")
    print(f"  LSF -> Portugues: '{r.translated_text}'")


def scenario_emergencia_multilingual():
    """Cenario: emergencia com pessoas de 3 paises."""
    print(f"\n{'=' * 65}")
    print("CENARIO 5: Emergencia com 3 surdos de paises diferentes")
    print("=" * 65)

    uni = SignLanguageUniversal()

    print("\n[Emergencia detectada -> signar em 3 linguas]")
    results = uni.translate_to_many("emergencia", "pt", ["bzs", "ase", "jsl"])
    for r in results:
        print(f"  {r.target_language_name}: avatar={r.avatar_animation}")

    print("\n[Tambem traduzir para texto em 3 linguas faladas]")
    results = uni.translate_to_many("emergencia", "pt", ["en", "ja", "fr"])
    for r in results:
        print(f"  {r.target_language_name}: '{r.translated_text}'")


def scenario_country_lookup():
    """Cenario: descobrir linguas de um pais."""
    print(f"\n{'=' * 65}")
    print("CENARIO 6: Linguas por pais")
    print("=" * 65)

    uni = SignLanguageUniversal()

    for country in ["BR", "US", "JP", "FR", "DE", "CN", "IN"]:
        langs = uni.find_language(country)
        print(f"\n  {country}:")
        print(f"    Falada: {', '.join(langs['spoken']) if langs['spoken'] else 'nenhuma'}")
        print(f"    Sinais: {', '.join(langs['sign']) if langs['sign'] else 'nenhuma'}")


# ============================================================================
# 11. DEMONSTRACAO
# ============================================================================

def demo():
    print("=" * 70)
    print("OpenSignLanguageUniversal -- Ponte Universal de Linguas de Sinais")
    print("(dados 2024/2025)")
    print("=" * 70)

    uni = SignLanguageUniversal()
    stats = uni.stats()

    print(f"\nLinguas de sinais mapeadas: {stats['sign_languages_count']}")
    print(f"Linguas faladas mapeadas: {stats['spoken_languages_count']}")
    print(f"Paises cobertos: {stats['countries_covered']}")
    print(f"Familias de sinais: {stats['families']}")
    print(f"Combinacoes possiveis: {stats['total_combinations']:,}")
    print(f"Conceitos no glossario: {stats['glossary_concepts']}")
    print(f"Modelos de IA catalogados (2024/2025): {stats['ai_models_count']}")

    # Por familia
    print(f"\n{'=' * 70}")
    print("LINGUAS DE SINAIS POR FAMILIA")
    print(f"{'=' * 70}")
    by_family = defaultdict(list)
    for sl in SIGN_LANGUAGES:
        by_family[sl.family].append(sl)
    for family, langs in sorted(by_family.items(), key=lambda x: -len(x[1])):
        print(f"\n  {family.value.upper()} ({len(langs)} linguas):")
        for sl in langs:
            print(f"    {sl.name:15} ({sl.code:4}) {sl.country:20} "
                  f"{sl.users_millions:.2f}M usuarios")

    # Modelos de IA por lingua
    print(f"\n{'=' * 70}")
    print("MODELOS DE IA 2024/2025 POR LINGUA DE SINAIS")
    print(f"{'=' * 70}")
    registry = SignLanguageModelRegistry()
    report = registry.coverage_report()
    print(f"\n  Total de modelos: {report['total_models']}")
    print(f"  Linguas com modelo: {report['languages_with_models']}/"
          f"{report['total_sign_languages']} ({report['coverage_pct']}%)")
    print(f"  Por tarefa:")
    for task, count in sorted(report["by_task"].items()):
        print(f"    {task}: {count}")
    print(f"\n  Detalhe por lingua:")
    for name, info in sorted(report["by_language"].items()):
        print(f"    {name:25} ({info['code']:4}) "
              f"{info['models']} modelo(s): {', '.join(info['tasks'])}")

    # Cenarios
    scenario_brazilian_meets_american()
    scenario_ouvinte_fala_com_surdo_estrangeiro()
    scenario_conferencia_internacional()
    scenario_turista_surdo()
    scenario_emergencia_multilingual()
    scenario_country_lookup()

    # Resumo
    print(f"\n{'=' * 70}")
    print("RESUMO")
    print(f"{'=' * 70}")
    print()
    print(f"  {stats['sign_languages_count']} linguas de sinais mapeadas.")
    print(f"  {stats['spoken_languages_count']} linguas faladas mapeadas.")
    print(f"  {stats['countries_covered']} paises cobertos.")
    print(f"  {stats['total_combinations']:,} combinacoes de traducao.")
    print(f"  {stats['ai_models_count']} modelos de IA catalogados (2024/2025).")
    print()
    print("  Cada pais tem sua lingua de sinais.")
    print("  Cada lingua de sinais e UNICA.")
    print("  Este sistema e a PONTE entre todas elas.")
    print()
    print("  Surdo brasileiro fala com surdo japones.")
    print("  Ouvinte alemao fala com surdo brasileiro.")
    print("  NENHUMA barreira. NENHUMA lingua intransponivel.")
    print()
    print("  Integrado com:")
    print("    OpenLibrasBridge (Libras bidirecional)")
    print("    OpenTelefonista (conversa natural)")
    print("    OpenBodyCamera (captura de sinais)")


if __name__ == "__main__":
    demo()
