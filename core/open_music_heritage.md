# OpenMusicHeritage -- Patrimonio Musical da Republica

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_music_heritage.py`

**Descricao:** ======================================================
"Funk, Rap, Hip-Hop, Samba, Forro, Maracatu, Frevo, Choro, Bossa,
 Pagode, Axé, Techno, Electronica -- todos PATRIMONIO da Republica.
 Ninguem dono. Todos herdeiros. Todos criadores."
O QUE ISTO FAZ:
  1. DECLARA generos musicais como PATRIMONIO IMATERIAL da Republica
  2. REGISTRA origem, historia e evolucao de cada genero
  3. PROTEGE contra apropriacao indevida (copyright corporativo)
  4. GARANTE que TODO cidadao pode criar/ouvir/executar sem pagar
  5. CONECTA com OpenTradition (cultura) e OpenMusic (criacao)
PRINCIPIO:
  Musica NAO e propriedade. Musica e CULTURA.
  Quem tenta copyrightar um genero musical ROUBA do povo.
  A Republica declara: TODO genero musical e BEM COMUM CC0.
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenMusicHeritage -- Patrimonio Musical da Republica
======================================================

"Funk, Rap, Hip-Hop, Samba, Forro, Maracatu, Frevo, Choro, Bossa,
 Pagode, Axé, Techno, Electronica -- todos PATRIMONIO da Republica.
 Ninguem dono. Todos herdeiros. Todos criadores."

O QUE ISTO FAZ:
  1. DECLARA generos musicais como PATRIMONIO IMATERIAL da Republica
  2. REGISTRA origem, historia e evolucao de cada genero
  3. PROTEGE contra apropriacao indevida (copyright corporativo)
  4. GARANTE que TODO cidadao pode criar/ouvir/executar sem pagar
  5. CONECTA com OpenTradition (cultura) e OpenMusic (criacao)

PRINCIPIO:
  Musica nao e propriedade. Musica e CULTURA.
  Quem tenta copyrightar um genero musical ROUBA do povo.
  A Republica declara: TODO genero musical e BEM COMUM CC0.

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
// 1. GENEROS MUSICAIS PATRIMONIO
// ============================================================================

classe CulturalOrigin herda de Enum:
    BRAZILIAN = "brasileiro"  // nascido no Brasil
    AFRICAN_DIASPORA = "diáspora_africana"  // raizes africanas
    GLOBAL = "global"  // origem internacional
    FUSION = "fusao"  // mistura de origens


// decorador: @dataclass
classe MusicalGenre:
    // Um genero musical patrimonio da Republica.
    genre_id: texto
    name: texto
    origin_region: texto // onde nasceu
    cultural_origin: CulturalOrigin
    seja birth_decade: texto = ""  // quando surgiu
    seja description: texto = ""
    seja bpm_range: texto = ""  // BPM tipico
    seja instruments: [texto] = field(default_factory=list)
    seja subgenres: [texto] = field(default_factory=list)

    // Significado cultural
    seja cultural_meaning: texto = ""
    seja social_function: texto = ""  // o que faz pela comunidade
    seja dance_style: texto = ""  // como se dança

    // Protecao
    seja is_heritage: logico = verdadeiro // PATRIMONIO da Republica
    seja copyrightable: logico = falso // NINGUEM pode copyrightar
    seja commercial_monopoly: logico = falso // sem monopolio corporativo

    // Estatistica
    seja registered_musicians: inteiro = 0
    seja total_songs: inteiro = 0


// ============================================================================
// 2. REGISTRO DE GENEROS
// ============================================================================

seja GENRES: [MusicalGenre] = [
    MusicalGenre(
        "GEN-FUNK", "Funk",
        "Favelas do Rio de Janeiro", CulturalOrigin.AFRICAN_DIASPORA,
        "1990s",
        description = (
            "Nasceu nas favelas cariocas. Raizes no Miami Bass e na "
            "cultura afro-brasileira. Batida forte, baixo potente, "
            "letra que retrata a realidade da periferia. "
            "O funk e a VOZ de quem foi silenciado."
        ),
        bpm_range = "120-130",
        instruments = ["bateria_eletronica", "sampler", "beatbox",
                     "sintetizador", "tamborzao"],
        subgenres = ["funk_carioca", "funk_ostentacao", "funk_melody",
                   "funk_brasilian", "mandelao", "funk_rave"],
        cultural_meaning = (
            "Funk e RESISTENCIA. E a periferia falando. "
            "Quem demoniza o funk demoniza o povo. "
            "Sim, tem funk putaria -- e ISSO E EXPRESSAO (P2). "
            "Sim, tem funk que fala de realidade -- E CULTURA."
        ),
        social_function = (
            "Comunidade se reconhece. Periferia se escuta. "
            "Baile funk = espaco comunitario (OpenNightLife). "
            "Funk educativo ensina (OpenMusic + OpenEducation)."
        ),
        dance_style = "passinho, danca sensual, circo (competicao de passos)",
    ),
    MusicalGenre(
        "GEN-RAP", "Rap",
        "Bronx, Nova York / Brasil periferia", CulturalOrigin.AFRICAN_DIASPORA,
        "1970s",
        description = (
            "Nasceu no Bronx. Filho do soul e do reggae. No Brasil, "
            "o rap encontrou a periferia e virou arma de consciencia. "
            "Racionais MCs, Sabotage, Criolo, Emicida. "
            "Letra e a ALMA do rap. A batida serve a mensagem."
        ),
        bpm_range = "80-100",
        instruments = ["beat", "sampler", "turntable", "loop", "voz"],
        subgenres = ["rap_consciencia", "trap", "drill", "boom_bap",
                   "rap_gospel", "rap_underground"],
        cultural_meaning = (
            "Rap e JORNALISMO da periferia. Denuncia. Critica. "
            "O rap que incomoda o poder e o rap que FAZ o trabalho dele. "
            "O estado que proibe rap teme a verdade."
        ),
        social_function = (
            "Educa politicamente. Critica o sistema. Organiza a comunidade. "
            "Conecta jovens com historia de luta."
        ),
        dance_style = "passo de rap (freestyle, sem coreografia fixa)",
    ),
    MusicalGenre(
        "GEN-HIPHOP", "Hip-Hop",
        "Bronx, Nova York", CulturalOrigin.AFRICAN_DIASPORA,
        "1970s",
        description = (
            "Hip-Hop NAO e so musica. E MOVIMENTO CULTURAL. "
            "4 elementos: MC (rap), DJ (beat), break (danca), graffiti (arte). "
            "No Brasil, e cultura das periferias. Gera oportunidade."
        ),
        bpm_range = "80-100",
        instruments = ["turntable", "sampler", "beat", "mic"],
        subgenres = ["old_school", "new_school", "trap_hiphop"],
        cultural_meaning = (
            "Hip-Hop e movimento de AUTO-ESTIMA da periferia. "
            "Cria pertencimento. Cria arte. Cria comunidade. "
            "Tira jovens do crime e da para a arte."
        ),
        social_function = "Ocupacao de espacos. Cultura alternativa. Identidade.",
        dance_style = "breakdance (b-boy, b-girl)",
    ),
    MusicalGenre(
        "GEN-SAMBA", "Samba",
        "Rio de Janeiro / Bahia", CulturalOrigin.AFRICAN_DIASPORA,
        "1910s",
        description = (
            "Nasceu dos escravizados africanos no Brasil. Raiz afro-brasileira. "
            "Samba de roda (BA) -> Samba carioca -> Samba de enredo (carnaval). "
            "O genero que DEFINE a identidade brasileira. "
            "Cartola, Nelson Cavaquinho, Bezerra da Silva, Zé Pelintú. "
            "A. A. A. "
            "Tiririca, Fundo de Quintal, Adoniran Barbosa."
        ),
        bpm_range = "50-70",
        instruments = ["cavaquinho", "violao", "pandeiro", "surdo",
                     "tan-tan", "reco-reco", "cuica", "agogo"],
        subgenres = ["samba_de_roda", "samba_carioca", "samba_enredo",
                   "samba_pagode", "choro", "partido_alto", "samba_reggae"],
        cultural_meaning = (
            "Samba e a ALMA do Brasil. Resistiu a escravidao. "
            "Resistiu a repressao policial. Resistiu a criminalizacao. "
            "Quem canta samba conta a historia do povo."
        ),
        social_function = (
            "Carnaval = maior festa popular do mundo (OpenTradition). "
            "Roda de samba = comunidade (OpenNightLife). "
            "Escola de samba = escola de vida."
        ),
        dance_style = "samba no pe, roda de samba",
    ),
    MusicalGenre(
        "GEN-FORRO", "Forro",
        "Nordeste do Brasil", CulturalOrigin.BRAZILIAN,
        "1910s",
        description = (
            "Musica do nordeste. Luiz Gonzaga ('O Gonzagão') levou o forro "
            "para todo Brasil. Sanfona, zabumba, triângulo. "
            "Fala do sertão, do amor, da seca, do migrante. "
            "A musica que faz o coração nordestino bater."
        ),
        bpm_range = "90-130",
        instruments = ["sanfona", "zabumba", "triangulo", "violao"],
        subgenres = ["forro_tradicional", "baião", "xote", "xaxado",
                   "forro_eletronico", "forro_estilizado"],
        cultural_meaning = (
            "Forro e SAUDADE do nordeste. Quem migra para SP/RJ leva o forro no peito. "
            "Fala do sertão, da vida simples, do amor sincero. "
            "A musica que UNE o Brasil de Norte a Sul."
        ),
        social_function = (
            "Junina = festa tradicional (OpenTradition). "
            "Forro de parede = comunidade (OpenNightLife). "
            "Aprendizado de instrumentos (OpenEducation)."
        ),
        dance_style = "pas de deux (par enlaçado)",
    ),
    MusicalGenre(
        "GEN-FREVO", "Frevo",
        "Recife, Pernambuco", CulturalOrigin.BRAZILIAN,
        "1910s",
        description = (
            "Frevo e o som do carnaval pernambucano. "
            "Maestria marcial, ritmo frenético, som da rua. "
            "Passo do passista com guarda-chuva colorido."
        ),
        bpm_range = "140-160",
        instruments = ["orquestra de metais", "saxofone", "trompete",
                     "clarinete", "tuba", "bumbo"],
        subgenres = ["frevo de rua", "frevo de bloco", "frevo de marcha"],
        cultural_meaning = "Frevo e ENERGIA. E alegria que transborda.",
        social_function = "Carnaval PE. Cultura pernambucana. Passistas.",
        dance_style = "passo do frevo (com guarda-chuva)",
    ),
    MusicalGenre(
        "GEN-MARACATU", "Maracatu",
        "Recife, Pernambuco", CulturalOrigin.AFRICAN_DIASPORA,
        "1900s",
        description = (
            "Maracatu e cerimônia. Tradição afro-brasileira. "
            "Nações (nações de maracatu) guardam rituais de coroação de reis negros. "
            "Tambores graves. Baque virado. Baque solto."
        ),
        bpm_range = "90-110",
        instruments = ["alfaia", "caixa", "gonguê", "mineiro", "abéu"],
        subgenres = ["maracatu_de_baque_virado", "maracatu_de_baque_solto"],
        cultural_meaning = (
            "Maracatu e MEMÓRIA AFRO-BRASILEIRA. Continuidade dos reinos africanos "
            "no Brasil. Resistência cultural de 400 anos."
        ),
        social_function = "Preservação cultural (OpenTradition). Comunidade.",
        dance_style = "coroação, dança dos caboclos",
    ),
    MusicalGenre(
        "GEN-CHORO", "Choro",
        "Rio de Janeiro", CulturalOrigin.BRAZILIAN,
        "1870s",
        description = (
            "Choro e o JAZZ brasileiro. Instrumental. Virtuoso. "
            "Pixinguinha, Jacob do Bandolim, Waldir Azevedo. "
            "Mais antigo genero urbano do Brasil."
        ),
        bpm_range = "120-150",
        instruments = ["bandolim", "flauta", "violao_7cordas", "cavaquinho",
                     "pandeiro"],
        subgenres = ["choro_tradicional", "choro_samba", "choro_moderno"],
        cultural_meaning = "Choro e sofisticação popular. A musica dos rodas.",
        social_function = "Roda de choro = escola de musica popular.",
        dance_style = "valsa lenta, polca brasileira",
    ),
    MusicalGenre(
        "GEN-BOSSA", "Bossa Nova",
        "Rio de Janeiro", CulturalOrigin.BRAZILIAN,
        "1950s",
        description = (
            "João Gilberto, Tom Jobim, Vinicius de Moraes. "
            "Samba encontra jazz. Minimalista. Cool. Elegante. "
            "Levou a musica brasileira ao mundo."
        ),
        bpm_range = "80-120",
        instruments = ["violao", "piano", "bateria_escova", "contrabaixo"],
        subgenres = ["bossa_clássica", "bossa_samba", "bossa_jazz"],
        cultural_meaning = "Bossa Nova e a elegância do samba.",
        social_function = "Turismo cultural. Diplomacia musical.",
        dance_style = "ouvindo (não há dança típica)",
    ),
    MusicalGenre(
        "GEN-PAGODE", "Pagode",
        "Rio de Janeiro", CulturalOrigin.AFRICAN_DIASPORA,
        "1980s",
        description = (
            "Pagode e o samba de mesa. Simples. Comunitário. "
            "Fundo de Quintal, Zeca Pagodinho, Sorriso Maroto. "
            "A festa da comunidade. O \"futebol do domingo\" musical."
        ),
        bpm_range = "70-90",
        instruments = ["cavaquinho", "violao", "pandeiro", "surdo",
                     "tan-tan", "banjo"],
        subgenres = ["pagode_classico", "pagode_romantico", "pagode_2000"],
        cultural_meaning = (
            "Pagode e a continuidade do samba na periferia. "
            "Festa comunitaria. Mesa de cerveja. Conversa. Vida."
        ),
        social_function = (
            "Roda de pagode = comunidade (OpenNightLife). "
            "Aprendizado de instrumentos (OpenEducation)."
        ),
        dance_style = "samba no pe, roda",
    ),
    MusicalGenre(
        "GEN-AXE", "Axe",
        "Salvador, Bahia", CulturalOrigin.AFRICAN_DIASPORA,
        "1980s",
        description = (
            "Axé é o som da Bahia. Eletro-percussão. Bloco de trio. "
            "Daniela Mercury, Ivete Sangalo, Chiclete com Banana. "
            "Som que faz o carnaval baiano ser o MAIOR do mundo."
        ),
        bpm_range = "110-130",
        instruments = ["guitarra", "bateria", "percussao", "sintetizador",
                     "trio_eletrico"],
        subgenres = ["axe_classico", "axe_mercado", "axe_elétrico"],
        cultural_meaning = (
            "Axé é a Bahia transbordando. "
            "Sincretismo cultural afro-brasileiro em som."
        ),
        social_function = "Carnaval BA. Trios elétricos. Turismo cultural.",
        dance_style = "pulando, em bloco",
    ),
    MusicalGenre(
        "GEN-TECHNO", "Techno / Electronic",
        "Detroit / Global", CulturalOrigin.GLOBAL,
        "1980s",
        description = (
            "Techno nasceu em Detroit, filho de operários negros. "
            "Música de MÁQUINAS. Industrial. Repetitiva. Hipnótica. "
            "No Brasil: Detroit Connection, Mau Mau, Mochakk."
        ),
        bpm_range = "120-150",
        instruments = ["synth", "drum_machine", "sequencer", "computer"],
        subgenres = ["detroit_techno", "minimal", "acid", "industrial",
                   "house", "drum_n_bass", "dubstep"],
        cultural_meaning = (
            "Techno é o futuro que já chegou. "
            "Festa = comunidade (rave). "
            "PLUR: Peace Love Unity Respect."
        ),
        social_function = (
            "Raves = espaço seguro (OpenNightLife). "
            "Produção eletrônica = skill (OpenMusic Studio)."
        ),
        dance_style = "freestyle, shuffle, glow sticks",
    ),
]


// ============================================================================
// 3. MOTOR DE PATRIMONIO MUSICAL
// ============================================================================

classe MusicHeritageEngine:
    // Motor que protege e promove generos musicais como patrimonio.

    PRINCIPIOS:
    1. PATRIMONIO IMATERIAL: generos pertencem ao POVO, nao a corporacoes
    2. CC0 UNIVERSAL: ninguem pode copyrightar um genero
    3. TODOS PODEM CRIAR: sem licenca, sem pagar, sem pedir permissao
    4. TODOS PODEM EXECUTAR: sem ECAD, sem cobranca, sem intermediario
    5. CULTURA PROTEGIDA: generos sao registered em OpenHistory + OpenTradition
    6. EVOLUCAO LIVRE: generos mudam, se misturam, evoluem. Sem dono.
    7. ANTI-Apropriacao: ninguem "descobre" um genero que ja era do povo
    8. PUTARIA e EXPRESSAO: funk putaria e cultura (P2 autonomia corporal)
    // 

    funcao __init__(self):
        self.genres: {texto: MusicalGenre} = {g.genre_id: g para g em GENRES}
        self.copyright_claims: [Dict] = []
        self.rejected_claims: inteiro = 0

    funcao list_heritage(self) -> [Dict]:
        retorne [
            {
                "id": g.genre_id,
                "name": g.name,
                "origin": g.origin_region,
                "decade": g.birth_decade,
                "cultural_origin": g.cultural_origin.value,
                "bpm": g.bpm_range,
                "subgenres": g.subgenres,
                g.is_heritage ? "heritage": "PATRIMONIO DA REPUBLICA" : "N/A",
                nao  g.copyrightable ? "copyright": "PROIBIDO" : "PERMITIDO",
            }
            para g em self.genres.values()
        ]

    funcao reject_copyright(self, genre_name: texto,
                         claimant: texto) -> {texto: qualquer}:
        // Rejeita tentativa de copyright sobre genero musical.
        self.copyright_claims.append({
            "genre": genre_name,
            "claimant": claimant,
            "date": datetime.now().isoformat(),
            "status": "REJEITADO",
        })
        self.rejected_claims += 1

        retorne {
            "genre": genre_name,
            "claimant": claimant,
            "status": "REJEITADO",
            "reason": (
                "{genre_name} e PATRIMONIO IMATERIAL da Republica. "
                "Ninguem pode copyrightar CULTURA. "
                "Todo cidadao pode criar, executar e modificar sem permissao."
            ),
            "law": (
                "Constituicao da Republica: generos musicais sao bens comuns. "
                "Tentativa de apropriacao e CONTRA P1 (anti-elitismo)."
            ),
        }

    funcao check_permission(self, action: texto, genre: texto) -> {texto: qualquer}:
        // Verifica se alguem precisa de permissao para algo.
        retorne {
            "action": action,
            "genre": genre,
            "permission_needed": "NAO",
            "message": (
                "Voce pode {action} {genre}. Sem permissao. "
                "Sem licenca. Sem pagar. E PATRIMONIO DA REPUBLICA."
            ),
        }

    funcao stats(self) -> {texto: qualquer}:
        retorne {
            "total_genres_heritage": tamanho(self.genres),
            "copyright_claims_rejected": self.rejected_claims,
            "anyone_can_create": verdadeiro,
            "anyone_can_perform": verdadeiro,
            "anyone_can_remix": verdadeiro,
            "ecad_exists": falso,
            "royalty_exists": falso,
            "copyright_exists": falso,
        }


// ============================================================================
// 4. MAIN
// ============================================================================

se __name__ == "__main__" entao:
    engine = MusicHeritageEngine()

    imprima("=" * 80)
    imprima("  OPENMUSICHERITAGE -- PATRIMONIO MUSICAL DA REPUBLICA")
    imprima("  Generos musicais sao BEM COMUM. Ninguem e dono. Todos herdeiros.")
    imprima("=" * 80)

    // === 1. GENEROS PATRIMONIO ===
    imprima("\n\n  === 1. GENEROS PATRIMONIO ({len(engine.genres)}) ===\n")
    imprima("  {'ID':<12} {'Genero':<20} {'Origem':<30} {'Decada':<10} {'BPM'}")
    imprima("  {'-'*85}")
    para cada g em engine.genres.values():
        imprima("  {g.genre_id:<12} {g.name:<20} {g.origin_region:<30} "
              "{g.birth_decade:<10} {g.bpm_range}")

    // === 2. DETALHE: FUNK ===
    imprima("\n\n  === 2. FUNK: PATRIMONIO DA PERIFERIA ===\n")
    funk = engine.genres["GEN-FUNK"]
    imprima("  Nome: {funk.name}")
    imprima("  Origem: {funk.origin_region}")
    imprima("  Raiz: {funk.cultural_origin.value}")
    imprima("  Instrumentos: {', '.join(funk.instruments)}")
    imprima("  Subgeneros: {', '.join(funk.subgenres)}")
    imprima("  Significado: {funk.cultural_meaning[:120]}...")
    imprima("  Funcao social: {funk.social_function[:120]}...")

    // === 3. DETALHE: RAP ===
    imprima("\n\n  === 3. RAP: JORNALISMO DA PERIFERIA ===\n")
    rap = engine.genres["GEN-RAP"]
    imprima("  Nome: {rap.name}")
    imprima("  Origem: {rap.origin_region}")
    imprima("  Significado: {rap.cultural_meaning[:120]}...")
    imprima("  Funcao social: {rap.social_function[:120]}...")

    // === 4. DETALHE: SAMBA ===
    imprima("\n\n  === 4. SAMBA: ALMA DO BRASIL ===\n")
    samba = engine.genres["GEN-SAMBA"]
    imprima("  Nome: {samba.name}")
    imprima("  Origem: {samba.origin_region}")
    imprima("  Instrumentos: {', '.join(samba.instruments)}")
    imprima("  Subgeneros: {', '.join(samba.subgenres)}")
    imprima("  Significado: {samba.cultural_meaning[:120]}...")

    // === 5. COPYRIGHT REJEITADO ===
    imprima("\n\n  === 5. COPYRIGHT REJEITADO ===\n")
    claims = [
        ("Funk", "Universal Music"),
        ("Samba", "Warner Music"),
        ("Forro", "Sony Music"),
        ("Rap", "Empresa XYZ"),
    ]
    para cada (genre, claimant) em claims:
        result = engine.reject_copyright(genre, claimant)
        imprima("  {claimant} tentou copyrightar {genre} -> {result['status']}")
        imprima("    {result['reason'][:80]}")

    // === 6. PERMISSAO ===
    imprima("\n\n  === 6. PERMISSAO PARA CRIAR ===\n")
    para cada action em ["criar", "tocar", "dançar", "remixar", "ensinar"]:
        result = engine.check_permission(action, "Funk")
        imprima("  {result['message']}")

    // === 7. STATS ===
    imprima("\n\n  === 7. ESTATISTICAS ===\n")
    s = engine.stats()
    para cada (k, v) em s.items():
        imprima("  {k:<35} {v}")

    // === FILOSOFIA ===
    imprima("""
    Funk, Rap, Hip-Hop, Samba, Forro, Maracatu, Frevo, Choro,
    Bossa, Pagode, Axe, Techno -- TODOS PATRIMONIO.

    MUSICA nao e PRODUTO. e CULTURA.
    Quem tenta copyrightar genero musical ROUBA do povo.
    A Republica declara: todo genero musical e BEM COMUM CC0.
    Todo cidadao pode criar, ouvir, executar, modificar.
    Sem ECAD. Sem royalty. Sem copyright. Sem intermediario.

    FUNK e PATRIMONIO:
    - Funk e a VOZ da periferia
    - Funk putaria e EXPRESSAO (P2 autonomia corporal)
    - Funk ostentacao e RELATO de realidade
    - Funk educativo ENSINA (OpenEducation)
    - Quem demoniza funk demoniza o POVO
    - Baile funk = espaco comunitario (OpenNightLife)
    - DJ de funk = TRABALHO (P3 base 1.0)

    RAP e PATRIMONIO:
    - Rap e JORNALISMO da periferia
    - Denuncia. Critica. Organiza. Educa.
    - Racionais, Sabotage, Criolo, Emicida
    - Estado que proibe rap teme a VERDADE

    SAMBA e PATRIMONIO:
    - Samba e ALMA do Brasil
    - Resistiu escravidao. Resistiu repressao.
    - Carnaval = maior festa popular do mundo
    - Escola de samba = escola de vida

    FORRO e PATRIMONIO:
    - Forro e SAUDADE do nordeste
    - Uniu o Brasil de Norte a Sul
    - Luis Gonzaga levou o sertao ao mundo
    - Festa junina = tradicao (OpenTradition)

    O QUE nao EXISTE NA REPUBLICA:
    - ECAD (cobranca de direitos)
    - Royalty (quem cria ja ganhou credito de trabalho)
    - Copyright corporativo de generos
    - "Licenca" para tocar musica
    - Processo por "plagio" de ritmo
    - Intermediario entre musico e publico

    O QUE EXISTE:
    - Todo mundo pode criar (OpenMusic Studio)
    - Todo mundo pode executar (sem licenca)
    - Todo mundo pode remixar (sem copyright)
    - Todo mundo pode ensinar (OpenEducation)
    - Instrumentos fabricados no FabLab (OpenHardware)
    - Shows transmitidos na OpenTV/OpenSocialNetwork

    PRINCIPIOS:
    P1: Generos musicais sao patrimonio. Sem elitismo cultural.
    P2: Expressao artistica e livre. Putaria e cultura. Corpo e soberano.
    seja P3: Criar musica = trabalho base 1.0. Sem royalty adicional.
    P4: Quem decide o que e cultura e o POVO, nao corporacao.
    // )
    imprima("{'='*80}")
    imprima("  OpenMusicHeritage: {s['total_genres_heritage']} generos patrimonio. "
          "{s['copyright_claims_rejected']} copyrights rejeitados.")
    imprima("  Musica nao e produto. E CULTURA.")
    imprima("{'='*80}")

```
