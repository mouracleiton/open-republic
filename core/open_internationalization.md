# OpenInternationalization (OpenI18n) -- Automacao Total de Internacionalizacao

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_internationalization.py`

**Descricao:** ==============================================================================
"O OpenRepublic nasce no Brasil. Mas e para a HUMANIDADE.
 Software que automatiza TRADUCAO, CULTURA e ADAPTACAO.
 Quem esta no Japao usa em japones. Na Africa, em swahili.
 Tudo automatico. Tudo CC0."
O QUE AUTOMATIZA:
  1. TRADUCAO: IA traduz TODO sistema para qualquer idioma
  2. CULTURA: adapta formato de data, moeda, calendario, saudacao
  3. LEGAL: adapta para leis locais (durante transicao)
  4. ACESSIBILIDADE: TTS em qualquer idioma, Braille, contraste
  5. RTL: arabe/hebraico (direita-esquerda)
  6. L10N COMPLETA: Localizacao total (nao so traducao)
AUTOMACAO MAXIMA:
  - IA detecta strings nao traduzidas -> traduz automaticamente
  - Comunidade revisa (opcional)
  - Novo idioma adicionado em HORAS (nao meses)
  - 100+ idiomas suportados
  - Dialeto regional (pt-BR vs pt-PT)
  - Neologismos da Republica (Laborante, Assembleia, etc.)
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenInternationalization (OpenI18n) -- Automacao Total de Internacionalizacao
==============================================================================

"O OpenRepublic nasce no Brasil. Mas e para a HUMANIDADE.
 Software que automatiza TRADUCAO, CULTURA e ADAPTACAO.
 Quem esta no Japao usa em japones. Na Africa, em swahili.
 Tudo automatico. Tudo CC0."

O QUE AUTOMATIZA:
  1. TRADUCAO: IA traduz TODO sistema para qualquer idioma
  2. CULTURA: adapta formato de data, moeda, calendario, saudacao
  3. LEGAL: adapta para leis locais (durante transicao)
  4. ACESSIBILIDADE: TTS em qualquer idioma, Braille, contraste
  5. RTL: arabe/hebraico (direita-esquerda)
  6. L10N COMPLETA: Localizacao total (nao so traducao)

AUTOMACAO MAXIMA:
  - IA detecta strings nao traduzidas -> traduz automaticamente
  - Comunidade revisa (opcional)
  - Novo idioma adicionado em HORAS (nao meses)
  - 100+ idiomas suportados
  - Dialeto regional (pt-BR vs pt-PT)
  - Neologismos da Republica (Laborante, Assembleia, etc.)

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa hashlib
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional de typing
// importa Enum de enum
// importa defaultdict de collections
// importa datetime de datetime


// ============================================================================
// 1. IDIOMAS SUPORTADOS
// ============================================================================

classe LanguageRegion herda de Enum:
    // Idioma + regiao (locale completo).
    PT_BR = ("pt-BR", "Portugues (Brasil)", "Ameri...[truncated]")
    PT_PT = ("pt-PT", "Portugues (Portugal)")
    EN_US = ("en-US", "English (USA)")
    EN_GB = ("en-GB", "English (UK)")
    ES_ES = ("es-ES", "Espanhol (Espanha)")
    ES_MX = ("es-MX", "Espanhol (Mexico)")
    ES_AR = ("es-AR", "Espanhol (Argentina)")
    FR_FR = ("fr-FR", "Frances")
    DE_DE = ("de-DE", "Alemao")
    IT_IT = ("it-IT", "Italiano")
    JA_JP = ("ja-JP", "Japones")
    ZH_CN = ("zh-CN", "Chines (Simplificado)")
    KO_KR = ("ko-KR", "Coreano")
    AR_SA = ("ar-SA", "Arabe (RTL)")
    HE_IL = ("he-IL", "Hebraico (RTL)")
    HI_IN = ("hi-IN", "Hindi")
    RU_RU = ("ru-RU", "Russo")
    SW_KE = ("sw-KE", "Swahili")
    YO_NG = ("yo-NG", "Yoruba")
    QU_PE = ("qu-PE", "Quechua")
    TY_BR = ("ty-BR", "Tupi (revitalizado)")
    GN_PY = ("gn-PY", "Guarani")

    // decorador: @property
    funcao code(self) -> texto:
        retorne self.value[0]

    // decorador: @property
    funcao name_native(self) -> texto:
        retorne self.value[1]

    // decorador: @property
    funcao is_rtl(self) -> logico:
        retorne self.code in ("ar-SA", "he-IL")


// ============================================================================
// 2. STRING TRADUZIDA
// ============================================================================

// decorador: @dataclass
classe TranslatedString:
    // Uma string do sistema traduzida para multiplos idiomas.
    string_id: texto                     // ex: "welcome_message"
    source_text: texto // texto original (pt-BR)
    seja translations: {texto: texto} = field(default_factory=dict) // locale -> traducao
    seja context: texto = ""  // contexto (ajuda IA)
    seja auto_translated: logico = falso // IA traduziu?
    seja reviewed: logico = falso // humano revisou?


// ============================================================================
// 3. ADAPTACAO CULTURAL
// ============================================================================

// decorador: @dataclass
classe CulturalAdaptation:
    // Adaptacao cultural para um locale.
    locale: texto
    seja date_format: texto = ""  // ex: DD/MM/YYYY
    seja time_format: texto = ""  // ex: 24h ou 12h AM/PM
    seja first_day_of_week: inteiro = 0 // 0=domingo, 1=segunda
    seja calendar_system: texto = "gregoriano"  // ou "islamico", "chines"
    seja greeting_formal: texto = ""
    seja greeting_informal: texto = ""
    seja number_format: texto = ""  // ex: 1.000,00 (BR) vs 1,000.00 (US)
    seja text_direction: texto = "ltr"  // ltr ou rtl
    seja color_cultural: {texto: texto} = field(default_factory=dict) // cores com significado


seja CULTURAL_DATA: {texto: CulturalAdaptation} = {
    "pt-BR": CulturalAdaptation(
        "pt-BR", "DD/MM/YYYY", "24h", 0, "gregoriano",
        "Ola", "Oi", "1.000,00", "ltr",
        {"verde": "esperanca", "amarelo": "alegria"},
    ),
    "en-US": CulturalAdaptation(
        "en-US", "MM/DD/YYYY", "12h", 0, "gregoriano",
        "Hello", "Hi", "1,000.00", "ltr",
        {"verde": "money", "vermelho": "perigo"},
    ),
    "ja-JP": CulturalAdaptation(
        "ja-JP", "YYYY/MM/DD", "24h", 1, "gregoriano",
        "Konnichiwa", "Yaho", "1,000", "ltr",
        {"branco": "luto"},
    ),
    "ar-SA": CulturalAdaptation(
        "ar-SA", "DD/MM/YYYY", "12h", 6, "islamico",
        "Assalamu alaikum", "Ahlan", "١٬٠٠٠٫٠٠", "rtl",
        {"verde": "sagrado"},
    ),
    "sw-KE": CulturalAdaptation(
        "sw-KE", "DD/MM/YYYY", "24h", 1, "gregoriano",
        "Jambo", "Mambo", "1,000.00", "ltr",
        {},
    ),
    "gn-PY": CulturalAdaptation(
        "gn-PY", "DD/MM/YYYY", "24h", 0, "gregoriano",
        "Mba'eichapa", "Iporane", "1.000", "ltr",
        {},
    ),
}


// ============================================================================
// 4. NEOLOGISMOS DA REPUBLICA
// ============================================================================

seja REPUBLIC_NEOLOGISMS: Dict[texto, {texto: texto}] = {
    "laborante": {
        "pt-BR": "Laborante",
        "en-US": "Laborer (citizen who works)",
        "es-ES": "Laborante",
        "ja-JP": "Raborento",
        "ar-SA": "Amil",
        "sw-KE": "Mfanyikazi",
        "gn-PY": "Mba'apoohara",
    },
    "assembleia": {
        "pt-BR": "Assembleia Constituinte",
        "en-US": "Constituent Assembly",
        "es-ES": "Asamblea Constituyente",
        "ja-JP": "Minshu Kaigi",
        "ar-SA": "Al-Jam'iya",
        "sw-KE": "Mkutano Mkuu",
        "gn-PY": "Aty Guasu",
    },
    "credito": {
        "pt-BR": "Credito de Acesso",
        "en-US": "Access Credit",
        "es-ES": "Credito de Acceso",
        "ja-JP": "Akusesu Kurejitto",
        "ar-SA": "Risana",
        "sw-KE": "Mkopo wa Ufikiaji",
        "gn-PY": "Kuemyriri",
    },
    "open": {
        "pt-BR": "Aberto (Open)",
        "en-US": "Open",
        "es-ES": "Abierto",
        "ja-JP": "Opun (Hirakareta)",
        "ar-SA": "Maftuh",
        "sw-KE": "Wazi",
        "gn-PY": "Pyahu",
    },
    "republica": {
        "pt-BR": "Republica",
        "en-US": "Republic",
        "es-ES": "Republica",
        "ja-JP": "Kyouwa-koku",
        "ar-SA": "Al-Jumhuriyya",
        "sw-KE": "Jamhuri",
        "gn-PY": "Tetapyrenda",
    },
    "fablab": {
        "pt-BR": "FabLab (Laboratorio de Fabricacao)",
        "en-US": "FabLab (Fabrication Lab)",
        "es-ES": "FabLab (Lab de Fabricacion)",
        "ja-JP": "FabLab (Seisaku Kenkyuusho)",
        "ar-SA": "Maktab Al-Tasnia",
        "sw-KE": "Maabara ya Ubunifu",
        "gn-PY": "Kuemyrykuaa",
    },
}


// ============================================================================
// 5. MOTOR DE INTERNACIONALIZACAO
// ============================================================================

classe I18nEngine:
    // Motor que automatiza internacionalizacao COMPLETA.

    COMO FUNCIONA:
    1. SCAN: escaneia TODOS os arquivos do repositorio principal
    2. EXTRACT: extrai todas as strings de texto
    3. TRANSLATE: IA traduz cada string para 100+ idiomas
    4. ADAPT: adapta cultura (data, moeda, calendario, direcao)
    5. REVIEW: comunidade revisa (opcional)
    6. DEPLOY: substitui no sistema automaticamente
    7. MONITOR: novas strings? IA traduz automaticamente

    AUTOMACAO MAXIMA:
    - Novo sistema adicionado? IA detecta strings novas.
    - IA traduz para TODOS os idiomas configurados.
    - Comunidade revisa SE QUISER (nao obrigatorio).
    - Novo idioma? IA traduz TODO o sistema em horas.
    - Neologismos da Republica tem traducao especial.
    // 

    funcao __init__(self):
        self.strings: {texto: TranslatedString} = {}
        self.supported_locales: [LanguageRegion] = list(LanguageRegion)
        self.cultural_data: {texto: CulturalAdaptation} = CULTURAL_DATA
        self.neologisms: Dict[texto, {texto: texto}] = REPUBLIC_NEOLOGISMS
        self.total_strings: inteiro = 0
        self.total_translations: inteiro = 0
        self.auto_translated: inteiro = 0

    funcao scan_and_extract(self, file_content: texto,
                         seja file_path: texto = "") -> {texto: qualquer}:
        // Escaneia arquivo e extrai strings para traduzir.

        Em producao: AST parser que encontra todas as strings.
        Aqui: simulacao de extracao.
        // 
        // Simular: pegar todas as strings entre aspas
        // importa re
        strings_found = re.findall(r'"([^"]{3,})"', file_content)
        strings_found = strings_found + re.findall(r"'([^']{3,})'", file_content)

        extracted = []
        para cada s em set(strings_found):
            sid = hashlib.md5(s[:20].encode()).hexdigest()[:8]
            se sid nao in self.strings entao:
                ts = TranslatedString(
                    string_id = sid, source_text=s,
                    context = file_path,
                )
                self.strings[sid] = ts
                extracted.append(sid)
            self.total_strings += 1

        retorne {
            "file": file_path,
            "strings_found": tamanho(strings_found),
            "new_strings": tamanho(extracted),
            "total_strings": tamanho(self.strings),
            "message": (
                "Escaneado {file_path}: {len(extracted)} strings novas. "
                "IA vai traduzir automaticamente."
            ),
        }

    funcao auto_translate(self, string_id: texto,
                       seja target_locales: [texto] = nulo) -> {texto: qualquer}:
        // IA traduz string para todos os idiomas.
        ts = self.strings.get(string_id)
        se nao ts entao:
            retorne {"error": "String nao encontrada"}

        locales = target_locales ou [lr.code para lr em self.supported_locales]

        // Simular traducao IA
        source = ts.source_text
        para cada locale em locales:
            se locale nao in ts.translations entao:
                // IA traduz (simulado)
                ts.translations[locale] = "[{locale}] {source}"
                self.total_translations += 1

        ts.auto_translated = verdadeiro
        self.auto_translated += 1

        retorne {
            "string_id": string_id,
            "source": source[:40],
            "translated_to": tamanho(ts.translations),
            "locales": locales,
            "auto": verdadeiro,
            "message": "IA traduziu '{source[:30]}' para {len(ts.translations)} idiomas.",
        }

    funcao batch_translate_all(self) -> {texto: qualquer}:
        // Traduz TODAS as strings pendentes.
        pending = [sid para sid, ts in self.strings.items()
                   if nao ts.auto_translated]
        para cada sid em pending:
            self.auto_translate(sid)

        retorne {
            "translated": tamanho(pending),
            "total_strings": tamanho(self.strings),
            "total_translations": self.total_translations,
            "message": "IA traduziu {len(pending)} strings para todos os idiomas.",
        }

    funcao add_locale(self, locale_code: texto, locale_name: texto,
                   seja rtl: logico = falso) -> {texto: qualquer}:
        // Adiciona novo idioma. IA traduz tudo automaticamente.
        // IA traduz TODAS as strings existentes para o novo idioma
        para cada (sid, ts) em self.strings.items():
            ts.translations[locale_code] = "[{locale_code}] {ts.source_text}"
            self.total_translations += 1

        retorne {
            "added": verdadeiro,
            "locale": locale_code,
            "name": locale_name,
            "rtl": rtl,
            "strings_translated": tamanho(self.strings),
            "time_to_add": "~{len(self.strings) // 1000} horas (IA automatico)",
            "message": (
                "Idioma '{locale_name}' ({locale_code}) adicionado. "
                "IA traduziu {len(self.strings)} strings automaticamente. "
                "Comunidade pode revisar."
            ),
        }

    funcao get_translation(self, string_id: texto, locale: texto) -> texto:
        // Retorna string traduzida para um locale.
        ts = self.strings.get(string_id)
        se nao ts entao:
            retorne "[missing: {string_id}]"
        retorne ts.translations.get(locale, ts.source_text)

    funcao get_cultural(self, locale: texto) -> {texto: texto}:
        // Retorna adaptacao cultural para um locale.
        data = self.cultural_data.get(locale, self.cultural_data.get("pt-BR"))
        retorne {
            "date_format": data.date_format,
            "time_format": data.time_format,
            "first_day_of_week": data.first_day_of_week,
            "calendar": data.calendar_system,
            "greeting_formal": data.greeting_formal,
            "greeting_informal": data.greeting_informal,
            "number_format": data.number_format,
            "text_direction": data.text_direction,
        }

    funcao get_neologism(self, term: texto, locale: texto) -> texto:
        // Traduz neologismo da Republica.
        neo = self.neologisms.get(term.lower(), {})
        retorne neo.get(locale, neo.get("en-US", term))

    funcao stats(self) -> {texto: qualquer}:
        retorne {
            "total_strings": tamanho(self.strings),
            "total_translations": self.total_translations,
            "idiomas_suportados": tamanho(self.supported_locales),
            "auto_translated_pct": "{self.auto_translated / max(len(self.strings), 1) * 100:.0f}%",
            "neologismos": tamanho(self.neologisms),
            "automacao": "MAXIMA (IA traduz automaticamente)",
        }


// ============================================================================
// 6. MAIN
// ============================================================================

se __name__ == "__main__" entao:
    engine = I18nEngine()

    imprima("=" * 80)
    imprima("  OPENINTERNATIONALIZATION -- AUTOMACAO TOTAL DE I18N")
    imprima("  IA traduz tudo. 100+ idiomas. Adicionar em horas.")
    imprima("=" * 80)

    // === 1. IDIOMAS SUPORTADOS ===
    imprima("\n\n  === 1. IDIOMAS SUPORTADOS ({len(engine.supported_locales)}) ===\n")
    para cada lr em engine.supported_locales:
        rtl = lr.is_rtl ? " [RTL]" : ""
        imprima("  {lr.code:<8} {lr.name_native:<30}{rtl}")

    // === 2. ADAPTACAO CULTURAL ===
    imprima("\n\n  === 2. ADAPTACAO CULTURAL ===\n")
    para cada locale em ["pt-BR", "en-US", "ja-JP", "ar-SA", "sw-KE", "gn-PY"]:
        data = engine.get_cultural(locale)
        imprima("\n  {locale}:")
        imprima("    Data: {data['date_format']}  Hora: {data['time_format']}")
        imprima("    Saudacao: {data['greeting_informal']} / {data['greeting_formal']}")
        imprima("    Calendario: {data['calendar']}  Direcao: {data['text_direction']}")

    // === 3. NEOLOGISMOS DA REPUBLICA ===
    imprima("\n\n  === 3. NEOLOGISMOS DA REPUBLICA ===\n")
    para cada term em ["laborante", "assembleia", "credito", "open", "republica", "fablab"]:
        translations = engine.neologisms.get(term, {})
        imprima("  {term}:")
        para cada (locale, translation) em list(translations.items())[:4]:
            imprima("    {locale}: {translation}")

    // === 4. SCAN E EXTRACAO ===
    imprima("\n\n  === 4. SCAN E EXTRACAO DE STRINGS ===\n")
    sample_file = '''
    imprima("Bem-vindo a Republica")
    message = "Desenvolva o OpenHealth"
    error = "Erro: arquivo nao encontrado"
    // 
    scan = engine.scan_and_extract(sample_file, "open_health.py")
    imprima("  {scan['message']}")

    // === 5. AUTO-TRADUCAO IA ===
    imprima("\n\n  === 5. AUTO-TRADUCAO POR IA ===\n")
    batch = engine.batch_translate_all()
    imprima("  {batch['message']}")
    imprima("  Total de traducoes: {batch['total_translations']}")

    // === 6. ADICIONAR NOVO IDIOMA ===
    imprima("\n\n  === 6. ADICIONAR NOVO IDIOMA (Tupi) ===\n")
    new_lang = engine.add_locale("ty-BR", "Tupi (revitalizado)")
    imprima("  {new_lang['message']}")

    // === 7. EXEMPLO DE TRADUCAO ===
    imprima("\n\n  === 7. EXEMPLO: 'Bem-vindo a Republica' em varios idiomas ===\n")
    // Encontrar string
    para cada (sid, ts) em engine.strings.items():
        se "Bem-vindo" in ts.source_text entao:
            para cada locale em ["pt-BR", "en-US", "ja-JP", "ar-SA", "sw-KE", "ty-BR"]:
                translation = engine.get_translation(sid, locale)
                imprima("  {locale}: {translation}")
            interrompa

    // === 8. STATS ===
    imprima("\n\n  === 8. ESTATISTICAS ===\n")
    s = engine.stats()
    para cada (k, v) em s.items():
        imprima("  {k:<30} {v}")

    imprima("\n{'='*80}")
    imprima("  OpenI18n: {s['total_strings']} strings, {s['total_translations']} traducoes, "
          "{s['idiomas_suportados']} idiomas.")
    imprima("  Automacao: {s['automacao']}.")
    imprima("{'='*80}")

```
