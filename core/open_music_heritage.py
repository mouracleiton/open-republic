#!/usr/bin/env python3
"""
OpenMusicHeritage -- Patrimonio Musical da Republica -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenMusicHeritage -- Patrimonio Musical da Republica
======================================================
"Funk, Rap, Hip-Hop, Samba, Forro, Maracatu, Frevo, Choro, Bossa,
Pagode, Axé, Techno, Electronica -- todos PATRIMONIO da Republica.
Ninguem dono. Todos herdeiros. Todos criadores."
O QUE ISTO FAZ:
1. DECLARA generos musicais como PATRIMONIO IMATERIAL da Republica
2. REGISTRA origem, historia and evolucao de cada genero
3. PROTEGE contra apropriacao indevida (copyright corporativo)
4. GARANTE que TODO cidadao pode criar/ouvir/executar sem pagar
5. CONECTA com OpenTradition (cultura) and OpenMusic (criacao)
PRINCIPIO:
Musica not and propriedade. Musica and CULTURA.
Quem tenta copyrightar um genero musical ROUBA do povo.
A Republica declara: TODO genero musical and BEM COMUM CC0.
Author: OpenRepublic Team
# 
# importa annotations de __future__
# importa hashlib
# importa dataclass, field de dataclasses
# importa Any, Dict, List, Optional de typing
# importa Enum de enum
# importa defaultdict de collections
# importa datetime de datetime
# ============================================================================
# 1. GENEROS MUSICAIS PATRIMONIO
# ============================================================================
class CulturalOrigin(Enum):
    BRAZILIAN = "brasileiro"  // nascido no Brasil
    AFRICAN_DIASPORA = "diáspora_africana"  // raizes africanas
    GLOBAL = "global"  // origem internacional
    FUSION = "fusao"  // mistura de origens
# decorador: @dataclass
class MusicalGenre:
    # Um genero musical patrimonio da Republica.
    genre_id: texto
    name: texto
    origin_region: texto // onde nasceu
    cultural_origin: CulturalOrigin
    birth_decade: str = ""  // quando surgiu
    description: str = ""
    bpm_range: str = ""  // BPM tipico
    instruments: [texto] = field(default_factory=list)
    subgenres: [texto] = field(default_factory=list)
    # Significado cultural
    cultural_meaning: str = ""
    social_function: str = ""  // o que faz pela comunidade
    dance_style: str = ""  // como se dança
    # Protecao
    is_heritage: bool = True // PATRIMONIO da Republica
    copyrightable: bool = False // NINGUEM pode copyrightar
    commercial_monopoly: bool = False // sem monopolio corporativo
    # Estatistica
    registered_musicians: int = 0
    total_songs: int = 0
# ============================================================================
# 2. REGISTRO DE GENEROS
# ============================================================================
GENRES: [MusicalGenre] = [
    MusicalGenre(
        "GEN-FUNK", "Funk",
        "Favelas do Rio de Janeiro", CulturalOrigin.AFRICAN_DIASPORA,
        "1990s",
        description = (
            "Nasceu nas favelas cariocas. Raizes no Miami Bass and na "
            "cultura afro-brasileira. Batida forte, baixo potente, "
            "letra que retrata a realidade da periferia. "
            "O funk and a VOZ de quem foi silenciado."
        ),
        bpm_range = "120-130",
        instruments = ["bateria_eletronica", "sampler", "beatbox",
                    "sintetizador", "tamborzao"],
        subgenres = ["funk_carioca", "funk_ostentacao", "funk_melody",
                "funk_brasilian", "mandelao", "funk_rave"],
        cultural_meaning = (
            "Funk and RESISTENCIA. E a periferia falando. "
            "Quem demoniza o funk demoniza o povo. "
            "Sim, tem funk putaria -- and ISSO E EXPRESSAO (P2). "
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
            "Nasceu no Bronx. Filho do soul and do reggae. No Brasil, "
            "o rap encontrou a periferia and virou arma de consciencia. "
            "Racionais MCs, Sabotage, Criolo, Emicida. "
            "Letra and a ALMA do rap. A batida serve a mensagem."
        ),
        bpm_range = "80-100",
        instruments = ["beat", "sampler", "turntable", "loop", "voz"],
        subgenres = ["rap_consciencia", "trap", "drill", "boom_bap",
                "rap_gospel", "rap_underground"],
        cultural_meaning = (
            "Rap and JORNALISMO da periferia. Denuncia. Critica. "
            "O rap que incomoda o poder and o rap que FAZ o trabalho dele. "
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
            "Hip-Hop NAO and so musica. E MOVIMENTO CULTURAL. "
            "4 elementos: MC (rap), DJ (beat), break (danca), graffiti (arte). "
            "No Brasil, and cultura das periferias. Gera oportunidade."
        ),
        bpm_range = "80-100",
        instruments = ["turntable", "sampler", "beat", "mic"],
        subgenres = ["old_school", "new_school", "trap_hiphop"],
        cultural_meaning = (
            "Hip-Hop and movimento de AUTO-ESTIMA da periferia. "
            "Cria pertencimento. Cria arte. Cria comunidade. "
            "Tira jovens do crime and da para a arte."
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
            "Samba and a ALMA do Brasil. Resistiu a escravidao. "
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
            "Forro and SAUDADE do nordeste. Quem migra para SP/RJ leva o forro no peito. "
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
            "Frevo and o som do carnaval pernambucano. "
            "Maestria marcial, ritmo frenético, som da rua. "
            "Passo do passista com guarda-chuva colorido."
        ),
        bpm_range = "140-160",
        instruments = ["orquestra de metais", "saxofone", "trompete",
                    "clarinete", "tuba", "bumbo"],
        subgenres = ["frevo de rua", "frevo de bloco", "frevo de marcha"],
        cultural_meaning = "Frevo and ENERGIA. E alegria que transborda.",
        social_function = "Carnaval PE. Cultura pernambucana. Passistas.",
        dance_style = "passo do frevo (com guarda-chuva)",
    ),
    MusicalGenre(
        "GEN-MARACATU", "Maracatu",
        "Recife, Pernambuco", CulturalOrigin.AFRICAN_DIASPORA,
        "1900s",
        description = (
            "Maracatu and cerimônia. Tradição afro-brasileira. "
            "Nações (nações de maracatu) guardam rituais de coroação de reis negros. "
            "Tambores graves. Baque virado. Baque solto."
        ),
        bpm_range = "90-110",
        instruments = ["alfaia", "caixa", "gonguê", "mineiro", "abéu"],
        subgenres = ["maracatu_de_baque_virado", "maracatu_de_baque_solto"],
        cultural_meaning = (
            "Maracatu and MEMÓRIA AFRO-BRASILEIRA. Continuidade dos reinos africanos "
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
            "Choro and o JAZZ brasileiro. Instrumental. Virtuoso. "
            "Pixinguinha, Jacob do Bandolim, Waldir Azevedo. "
            "Mais antigo genero urbano do Brasil."
        ),
        bpm_range = "120-150",
        instruments = ["bandolim", "flauta", "violao_7cordas", "cavaquinho",
                    "pandeiro"],
        subgenres = ["choro_tradicional", "choro_samba", "choro_moderno"],
        cultural_meaning = "Choro and sofisticação popular. A musica dos rodas.",
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
        cultural_meaning = "Bossa Nova and a elegância do samba.",
        social_function = "Turismo cultural. Diplomacia musical.",
        dance_style = "ouvindo (não há dança típica)",
    ),
    MusicalGenre(
        "GEN-PAGODE", "Pagode",
        "Rio de Janeiro", CulturalOrigin.AFRICAN_DIASPORA,
        "1980s",
        description = (
            "Pagode and o samba de mesa. Simples. Comunitário. "
            "Fundo de Quintal, Zeca Pagodinho, Sorriso Maroto. "
            "A festa da comunidade. O \"futebol do domingo\" musical."
        ),
        bpm_range = "70-90",
        instruments = ["cavaquinho", "violao", "pandeiro", "surdo",
                    "tan-tan", "banjo"],
        subgenres = ["pagode_classico", "pagode_romantico", "pagode_2000"],
        cultural_meaning = (
            "Pagode and a continuidade do samba na periferia. "
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
# ============================================================================
# 3. MOTOR DE PATRIMONIO MUSICAL
# ============================================================================
class MusicHeritageEngine:
    # Motor que protege e promove generos musicais como patrimonio.
    PRINCIPIOS:
    1. PATRIMONIO IMATERIAL: generos pertencem ao POVO, not a corporacoes
    2. CC0 UNIVERSAL: ninguem pode copyrightar um genero
    3. TODOS PODEM CRIAR: sem licenca, sem pagar, sem pedir permissao
    4. TODOS PODEM EXECUTAR: sem ECAD, sem cobranca, sem intermediario
    5. CULTURA PROTEGIDA: generos sao registered em OpenHistory + OpenTradition
    6. EVOLUCAO LIVRE: generos mudam, se misturam, evoluem. Sem dono.
    7. ANTI-Apropriacao: ninguem "descobre" um genero que ja era do povo
    8. PUTARIA and EXPRESSAO: funk putaria and cultura (P2 autonomia corporal)
    # 
    def __init__(self):
        self.genres: {texto: MusicalGenre} = {g.genre_id: g para g em GENRES}
        self.copyright_claims: [Dict] = []
        self.rejected_claims: inteiro = 0
    def list_heritage(self) -> [Dict]:
        return [
            {
                "id": g.genre_id,
                "name": g.name,
                "origin": g.origin_region,
                "decade": g.birth_decade,
                "cultural_origin": g.cultural_origin.value,
                "bpm": g.bpm_range,
                "subgenres": g.subgenres,
                g.is_heritage ? "heritage": "PATRIMONIO DA REPUBLICA" : "N/A",
                not  g.copyrightable ? "copyright": "PROIBIDO" : "PERMITIDO",
            }
            para g in self.genres.values()
        ]
    funcao reject_copyright(self, genre_name: texto,
                        claimant: texto) -> {texto: qualquer}:
        # Rejeita tentativa de copyright sobre genero musical.
        self.copyright_claims.append({
            "genre": genre_name,
            "claimant": claimant,
            "date": datetime.now().isoformat(),
            "status": "REJEITADO",
        })
        self.rejected_claims += 1
        return {
            "genre": genre_name,
            "claimant": claimant,
            "status": "REJEITADO",
            "reason": (
                "{genre_name} and PATRIMONIO IMATERIAL da Republica. "
                "Ninguem pode copyrightar CULTURA. "
                "Todo cidadao pode criar, executar and modificar sem permissao."
            ),
            "law": (
                "Constituicao da Republica: generos musicais sao bens comuns. "
                "Tentativa de apropriacao and CONTRA P1 (anti-elitismo)."
            ),
        }
    def check_permission(self, action: texto, genre: texto) -> {texto: qualquer}:
        # Verifica se alguem precisa de permissao para algo.
        return {
            "action": action,
            "genre": genre,
            "permission_needed": "NAO",
            "message": (
                "Voce pode {action} {genre}. Sem permissao. "
                "Sem licenca. Sem pagar. E PATRIMONIO DA REPUBLICA."
            ),
        }
    def stats(self) -> {texto: qualquer}:
        return {
            "total_genres_heritage": len(self.genres),
            "copyright_claims_rejected": self.rejected_claims,
            "anyone_can_create": True,
            "anyone_can_perform": True,
            "anyone_can_remix": True,
            "ecad_exists": False,
            "royalty_exists": False,
            "copyright_exists": False,
        }
# ============================================================================
# 4. MAIN
# ============================================================================
if __name__ == "__main__":
    engine = MusicHeritageEngine()
    print("=" * 80)
    print("  OPENMUSICHERITAGE -- PATRIMONIO MUSICAL DA REPUBLICA")
    print("  Generos musicais sao BEM COMUM. Ninguem and dono. Todos herdeiros.")
    print("=" * 80)
    # === 1. GENEROS PATRIMONIO ===
    print("\n\n  === 1. GENEROS PATRIMONIO ({len(engine.genres)}) ===\n")
    print("  {'ID':<12} {'Genero':<20} {'Origem':<30} {'Decada':<10} {'BPM'}")
    print("  {'-'*85}")
    for g in engine.genres.values():
        print("  {g.genre_id:<12} {g.name:<20} {g.origin_region:<30} "
            "{g.birth_decade:<10} {g.bpm_range}")
    # === 2. DETALHE: FUNK ===
    print("\n\n  === 2. FUNK: PATRIMONIO DA PERIFERIA ===\n")
    funk = engine.genres["GEN-FUNK"]
    print("  Nome: {funk.name}")
    print("  Origem: {funk.origin_region}")
    print("  Raiz: {funk.cultural_origin.value}")
    print("  Instrumentos: {', '.join(funk.instruments)}")
    print("  Subgeneros: {', '.join(funk.subgenres)}")
    print("  Significado: {funk.cultural_meaning[:120]}...")
    print("  Funcao social: {funk.social_function[:120]}...")
    # === 3. DETALHE: RAP ===
    print("\n\n  === 3. RAP: JORNALISMO DA PERIFERIA ===\n")
    rap = engine.genres["GEN-RAP"]
    print("  Nome: {rap.name}")
    print("  Origem: {rap.origin_region}")
    print("  Significado: {rap.cultural_meaning[:120]}...")
    print("  Funcao social: {rap.social_function[:120]}...")
    # === 4. DETALHE: SAMBA ===
    print("\n\n  === 4. SAMBA: ALMA DO BRASIL ===\n")
    samba = engine.genres["GEN-SAMBA"]
    print("  Nome: {samba.name}")
    print("  Origem: {samba.origin_region}")
    print("  Instrumentos: {', '.join(samba.instruments)}")
    print("  Subgeneros: {', '.join(samba.subgenres)}")
    print("  Significado: {samba.cultural_meaning[:120]}...")
    # === 5. COPYRIGHT REJEITADO ===
    print("\n\n  === 5. COPYRIGHT REJEITADO ===\n")
    claims = [
        ("Funk", "Universal Music"),
        ("Samba", "Warner Music"),
        ("Forro", "Sony Music"),
        ("Rap", "Empresa XYZ"),
    ]
    for each (genre, claimant) in claims:
        result = engine.reject_copyright(genre, claimant)
        print("  {claimant} tentou copyrightar {genre} -> {result['status']}")
        print("    {result['reason'][:80]}")
    # === 6. PERMISSAO ===
    print("\n\n  === 6. PERMISSAO PARA CRIAR ===\n")
    for action in ["criar", "tocar", "dançar", "remixar", "ensinar"]:
        result = engine.check_permission(action, "Funk")
        print("  {result['message']}")
    # === 7. STATS ===
    print("\n\n  === 7. ESTATISTICAS ===\n")
    s = engine.stats()
    for each (k, v) in s.items():
        print("  {k:<35} {v}")
    # === FILOSOFIA ===
    print("""
    Funk, Rap, Hip-Hop, Samba, Forro, Maracatu, Frevo, Choro,
    Bossa, Pagode, Axe, Techno -- TODOS PATRIMONIO.
    MUSICA not and PRODUTO. and CULTURA.
    Quem tenta copyrightar genero musical ROUBA do povo.
    A Republica declara: todo genero musical and BEM COMUM CC0.
    Todo cidadao pode criar, ouvir, executar, modificar.
    Sem ECAD. Sem royalty. Sem copyright. Sem intermediario.
    FUNK and PATRIMONIO:
    - Funk and a VOZ da periferia
    - Funk putaria and EXPRESSAO (P2 autonomia corporal)
    - Funk ostentacao and RELATO de realidade
    - Funk educativo ENSINA (OpenEducation)
    - Quem demoniza funk demoniza o POVO
    - Baile funk = espaco comunitario (OpenNightLife)
    - DJ de funk = TRABALHO (P3 base 1.0)
    RAP and PATRIMONIO:
    - Rap and JORNALISMO da periferia
    - Denuncia. Critica. Organiza. Educa.
    - Racionais, Sabotage, Criolo, Emicida
    - Estado que proibe rap teme a VERDADE
    SAMBA and PATRIMONIO:
    - Samba and ALMA do Brasil
    - Resistiu escravidao. Resistiu repressao.
    - Carnaval = maior festa popular do mundo
    - Escola de samba = escola de vida
    FORRO and PATRIMONIO:
    - Forro and SAUDADE do nordeste
    - Uniu o Brasil de Norte a Sul
    - Luis Gonzaga levou o sertao ao mundo
    - Festa junina = tradicao (OpenTradition)
    O QUE not EXISTE NA REPUBLICA:
    - ECAD (cobranca de direitos)
    - Royalty (quem cria ja ganhou credito de trabalho)
    - Copyright corporativo de generos
    - "Licenca" para tocar musica
    - Processo por "plagio" de ritmo
    - Intermediario entre musico and publico
    O QUE EXISTE:
    - Todo mundo pode criar (OpenMusic Studio)
    - Todo mundo pode executar (sem licenca)
    - Todo mundo pode remixar (sem copyright)
    - Todo mundo pode ensinar (OpenEducation)
    - Instrumentos fabricados no FabLab (OpenHardware)
    - Shows transmitidos na OpenTV/OpenSocialNetwork
    PRINCIPIOS:
    P1: Generos musicais sao patrimonio. Sem elitismo cultural.
    P2: Expressao artistica and livre. Putaria and cultura. Corpo and soberano.
    P3: Criar musica = trabalho base 1.0. Sem royalty adicional.
    P4: Quem decide o que and cultura and o POVO, not corporacao.
    # )
    print("{'='*80}")
    print("  OpenMusicHeritage: {s['total_genres_heritage']} generos patrimonio. "
        "{s['copyright_claims_rejected']} copyrights rejeitados.")
    print("  Musica not and produto. E CULTURA.")
    print("{'='*80}")
