# OpenPropagation -- Estrategia de Divulgacao Massiva

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_propagation.py`

**Descricao:** =====================================================
"O melhor sistema do mundo nao serve se ninguem sabe que existe.
 116 sistemas. 91k linhas. ZERO se ninguem VE.
 A estrategia nao e'gritar. E' DEMONSTRAR.
 Mostrar funcionando. Deixar resultado falar."
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenPropagation -- Estrategia de Divulgacao Massiva
=====================================================

"O melhor sistema do mundo nao serve se ninguem sabe que existe.
 116 sistemas. 91k linhas. ZERO se ninguem VE.
 A estrategia nao e'gritar. E' DEMONSTRAR.
 Mostrar funcionando. Deixar resultado falar."

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa dataclass, field de dataclasses
// importa Any, Dict, List de typing
// importa Enum de enum
// importa defaultdict de collections


// ============================================================================
// 1. ESTRATEGIA EM 5 FRENTES
// ============================================================================

classe PropagationFront herda de Enum:
    DEMONSTRACAO = "demonstracao_real"  // piloto funcionando
    CONTEUDO = "conteudo_viral"  // X/Twitter, video, texto
    COMUNIDADES = "comunidades_reais"  // quilombo, favela, sertao
    ALIANCAS = "aliancas_estrategicas"  // influenciadores, ONGs
    PRODUTO = "produto_publico"  // app/ferramenta usavel


// ============================================================================
// 2. FRENTE 1: DEMONSTRACAO REAL (a que MATA)
// ============================================================================

// decorador: @dataclass
classe DemoPilot:
    // Cada piloto real e' a maior propaganda da Republica.
    name: texto
    location: texto
    community_type: texto
    population: inteiro
    what_demonstrates: texto
    expected_impact: texto
    cost: texto
    timeline: texto
    viral_potential: texto // quao viralizavel e'
    documentation: texto // como documentar (video, dados, relatorio)


seja PILOTS: [DemoPilot] = [
    DemoPilot(
        name = "Piloto Agua no Sertao",
        location = "Poco Redondo, SE",
        community_type = "sertao",
        population = 200,
        what_demonstrates = "Cisterna + poco solar + dessalinizador = agua o ano todo",
        expected_impact = "200 pessoas com agua garantida pela 1a vez",
        cost = "R$ 50.000 (1 comunidade)",
        timeline = "30 dias",
        viral_potential = "ALTISSIMO. Antes/depois dramatico. Imprensa nacional.",
        documentation = "Video 3min: 'Essa comunidade tinha sede. Agora nao.'",
    ),
    DemoPilot(
        name = "Piloto Saude na Favela",
        location = "Capao Redondo, SP",
        community_type = "favela",
        population = 5000,
        what_demonstrates = "Clinica comunitaria + telemedicina = fila zero",
        expected_impact = "UPA de 8h -> 0min na propria favela",
        cost = "R$ 100.000 (1 clinica)",
        timeline = "60 dias",
        viral_potential = "ALTISSIMO. Fila de UPA e' pauta nacional.",
        documentation = "Time-lapse: fila UPA vs clinica comunitaria 0min",
    ),
    DemoPilot(
        name = "Piloto Solar no Quilombo",
        location = "Eldorado, SP",
        community_type = "quilombo",
        population = 150,
        what_demonstrates = "Painel solar = energia pela 1a vez",
        expected_impact = "12 casas sem luz -> 12 casas com luz",
        cost = "R$ 15.000 (12 kits)",
        timeline = "7 dias",
        viral_potential = "ALTO. Visual: escuridao -> luz.",
        documentation = "Video noturno: acendendo luz pela 1a vez",
    ),
    DemoPilot(
        name = "Piloto Credito Sem Juros",
        location = "Cidade Baixa, Salvador",
        community_type = "favela",
        population = 3000,
        what_demonstrates = "OpenCredit: empreendedor da favela sem juros",
        expected_impact = "100 microempreendedores sem agiota/banco",
        cost = "R$ 30.000 (estrutura + capital inicial)",
        timeline = "90 dias",
        viral_potential = "ALTISSIMO. 'O banco que nao cobra' noticia nacional.",
        documentation = "Doc: empreendedor antes (juros 730%) vs depois (0%)",
    ),
    DemoPilot(
        name = "Piloto Acai Solar Ribeirinho",
        location = "Silves, AM",
        community_type = "ribeirinho",
        population = 80,
        what_demonstrates = "Freezer solar = acai nao estraga mais",
        expected_impact = "Perda de 60% -> 0%. Renda 5x maior.",
        cost = "R$ 20.000",
        timeline = "45 dias",
        viral_potential = "ALTO. Amazonia + sustentabilidade = midia global.",
        documentation = "Video: acai estragando vs acai congelado solar",
    ),
]


// ============================================================================
// 3. FRENTE 2: CONTEUDO VIRAL
// ============================================================================

// decorador: @dataclass
classe ContentPiece:
    // Cada peca de conteudo projetada para viralizar.
    piece_id: texto
    format: texto // thread X, video curto, infografico
    topic: texto
    hook: texto // primeira frase (CRITICA)
    target_audience: texto
    emotional_trigger: texto
    platform: texto
    call_to_action: texto
    expected_reach: texto
    frequency: texto // diario, semanal


seja CONTENT: [ContentPiece] = [
    // === X/TWITTER (foco principal do usuario) ===
    ContentPiece(
        "CT-01", "thread X", "5% vs 90%",
        hook = "Voce produz R$ 100. Recebe R$ 10. Dono leva R$ 90. Por que?",
        target_audience = "trabalhador CLT geral",
        emotional_trigger = "indignacao (justa)",
        platform = "X/Twitter @clouramlearning",
        call_to_action = "Leia a simulacao completa no repositorio",
        expected_reach = "100k+ (se pegar)",
        frequency = "1x/semana",
    ),
    ContentPiece(
        "CT-02", "thread X", "LASIK gratuito",
        hook = "Voce usa oculos ha 20 anos. 15 minutos resolvia. Por que nao?",
        target_audience = "80% da populacao que usa oculos",
        emotional_trigger = "surpresa + curiosidade",
        platform = "X/Twitter",
        call_to_action = "Exija do seu representante. #OpenHealth",
        expected_reach = "200k+",
        frequency = "1x/semana",
    ),
    ContentPiece(
        "CT-03", "video curto", "simulacao salario real",
        hook = "Pedreiro produz R$ 18.000/mes. Recebe R$ 2.800. Vem ver.",
        target_audience = "classe C/D trabalhadora",
        emotional_trigger = "choque de realidade",
        platform = "X + TikTok + Instagram",
        call_to_action = "Calcula o teu: link para simulador",
        expected_reach = "500k+",
        frequency = "1x/2 semanas",
    ),
    ContentPiece(
        "CT-04", "infografico", "cadeia de valor visual",
        hook = "Onde vai cada R$ 100 que voce produz [infografico]",
        target_audience = "geral",
        emotional_trigger = "clareza visual (entende em 3s)",
        platform = "X + Instagram",
        call_to_action = "Compartilha. Todo mundo precisa ver.",
        expected_reach = "300k+",
        frequency = "1x/mes",
    ),
    ContentPiece(
        "CT-05", "thread X", "comunidade real funcionando",
        hook = "Essa comunidade no sertao nao tem sede ha 200 anos. Em 30 dias, teve.",
        target_audience = "geral + imprensa",
        emotional_trigger = "emocao + prova real",
        platform = "X + video YouTube",
        call_to_action = "Republica funciona. Nao e'teoria.",
        expected_reach = "1M+ (se virar noticia)",
        frequency = "a cada piloto concluido",
    ),
    ContentPiece(
        "CT-06", "thread X", "saude mental sem rotular",
        hook = "'Voce sempre tera depressao.' Mentira. Cerebro muda ate os 90.",
        target_audience = "jovens + profissionais da saude",
        emotional_trigger = "esperanca + ciencia",
        platform = "X + Instagram",
        call_to_action = "Neuroplasticidade. Le o Kandel, Nobel 2000.",
        expected_reach = "150k+",
        frequency = "1x/2 semanas",
    ),
    ContentPiece(
        "CT-07", "video curto", "OpenRepair: nada se joga fora",
        hook = "Fone quebrou? Conserta. Nao compra. [mostra conserto]",
        target_audience = "jovem urbano",
        emotional_trigger = "praticidade + anti-consumismo",
        platform = "X + TikTok",
        call_to_action = "FabLab mais proximo: link",
        expected_reach = "200k+",
        frequency = "1x/semana",
    ),
    ContentPiece(
        "CT-08", "thread X", "sem spam telefonico",
        hook = "Assembleia votou: 94% quer proibir telemarketing. Vai virar lei.",
        target_audience = "TODO mundo (ninguem gosta de spam)",
        emotional_trigger = "alivio universal",
        platform = "X",
        call_to_action = "Cobra do deputado. #ParaDeMeEncherOSaco",
        expected_reach = "viral (pauta universal)",
        frequency = "1x/mes",
    ),
    ContentPiece(
        "CT-09", "infografico", "12 mentiras do determinismo",
        hook = "'Nasceu pobre morre pobre' -- 12 mentiras que a ciencia destruiu",
        target_audience = "jovem periferia",
        emotional_trigger = "empoderamento + ciencia",
        platform = "X + Instagram",
        call_to_action = "O passado e'contexto. O futuro e'escolha.",
        expected_reach = "300k+",
        frequency = "1x/mes",
    ),
    ContentPiece(
        "CT-10", "video curto", "musica da Republica",
        hook = "Funk e'patrimonio. Rap e'jornalismo. Samba e'alma. Sem ECAD.",
        target_audience = "musico + cultura",
        emotional_trigger = "orgulho cultural",
        platform = "X + Instagram + TikTok",
        call_to_action = "Cria, toca, compartilha. CC0.",
        expected_reach = "500k+ (cultura viraliza)",
        frequency = "1x/2 semanas",
    ),
    // === VIDEO LONGO ===
    ContentPiece(
        "CT-11", "video YouTube 15min", "documento piloto",
        hook = "Botamos OpenRepublic pra funcionar de verdade. Ve o resultado.",
        target_audience = "geral",
        emotional_trigger = "prova real + emocao",
        platform = "YouTube + X",
        call_to_action = "A Republica nao e'teoria. E'resultado.",
        expected_reach = "500k+ (se bom)",
        frequency = "1 por piloto",
    ),
    ContentPiece(
        "CT-12", "thread X", "comparacao Noruega vs Brasil",
        hook = "Noruega: 20% reincidencia. Brasil: 70%. O que eles fazem diferente?",
        target_audience = "geral + politico",
        emotional_trigger = "vergonha + curiosidade",
        platform = "X",
        call_to_action = "OpenPenalRevision. Tratar > punir.",
        expected_reach = "200k+",
        frequency = "1x/mes",
    ),
]


// ============================================================================
// 4. FRENTE 3: COMUNIDADES REAIS
// ============================================================================

// decorador: @dataclass
classe CommunityPropagation:
    // Como o modelo espalha de comunidade em comunidade.
    strategy: texto
    target_communities: [texto]
    method: texto
    expansion_factor: texto // quantas comunidades cada uma gera


seja COMMUNITY_STRATEGY: [CommunityPropagation] = [
    CommunityPropagation(
        strategy = "Rede Quilombola (CONAQ)",
        target_communities = ["quilombos certificados"],
        method = "1 quilombo funcionando -> CONAQ espalha para 5.000+",
        expansion_factor = "1 -> 100 (via CONAQ)",
    ),
    CommunityPropagation(
        strategy = "Rede MST (assentamentos)",
        target_communities = ["assentamentos rurais"],
        method = "1 assentamento com OpenTrator -> MST espalha para 1.500+",
        expansion_factor = "1 -> 50 (via setores MST)",
    ),
    CommunityPropagation(
        strategy = "Rede Favela (CUFA/G10/Redes da Maré)",
        target_communities = ["favelas urbanas"],
        method = "1 favela com OpenCredit -> G10 Banc espalha para 17M moradores",
        expansion_factor = "1 -> 100 (via G10/CUFA)",
    ),
    CommunityPropagation(
        strategy = "Rede Sertao (ASA/Articulacao Semi-Arido)",
        target_communities = ["comunidades do semi-arido"],
        method = "1 cisterna OpenRepublic -> ASA espalha para milhares",
        expansion_factor = "1 -> 1000 (via ASA ja tem rede)",
    ),
    CommunityPropagation(
        strategy = "Rede Ribeirinha (CNSI/Comites Amazonia)",
        target_communities = ["ribeirinhos Amazonia"],
        method = "1 comunidade com freezer solar -> CNSI espalha via radio",
        expansion_factor = "1 -> 50 (via CNSI)",
    ),
]


// ============================================================================
// 5. FRENTE 4: ALIANCAS
// ============================================================================

// decorador: @dataclass
classe Alliance:
    // Cada alianca que amplifica o alcance.
    ally_type: texto
    who: texto
    what_they_gain: texto
    what_republica_gains: texto
    priority: texto


seja ALLIANCES: [Alliance] = [
    Alliance(
        "influencer", "Criador de conteudo de economia pessoal",
        "Conteudo original (simulacao salario real) que viraliza",
        "Alcance para 1M+ seguidores",
        "ALTA",
    ),
    Alliance(
        "ong", "Banco Palmas (Fortaleza)",
        "Tecnologia OpenCredit + OpenERP para escalar",
        "Validacao real de 20 anos em credito comunitario",
        "ALTISSIMA",
    ),
    Alliance(
        "ong", "Medicos Sem Fronteiras (operacao Brasil)",
        "OpenHealth em comunidades isoladas (modelos validados)",
        "Credibilidade + operacao em campo",
        "ALTA",
    ),
    Alliance(
        "influencer", "Artista funk/rap/samba",
        "Plataforma OpenMusic sem ECAD (100% fica com artista)",
        "Reaches milhoes de fas. Cultura viraliza.",
        "ALTISSIMA",
    ),
    Alliance(
        "academia", "Professor universitario (USP/UNICAMP/UFRJ)",
        "Dados reais para pesquisa + publicacao",
        "Validacao academica (combate 'nao e'cientifico')",
        "ALTA",
    ),
    Alliance(
        "jornalista", "Reporter investigativo (agencia/fiipe",
        "Historia: 'comunidade que resolveu o que governo nao resolveu'",
        "Midia nacional. Imprensa nao paga, mas legitima.",
        "ALTISSIMA",
    ),
    Alliance(
        "youtuber", "Canal de tecnologia (5M+ inscritos)",
        "Exclusiva: '116 sistemas open-source que mudam o Brasil'",
        "1 video = 1M+ visualizacoes",
        "ALTA",
    ),
    Alliance(
        "politico", "Vereador/deputado alinhado (EXISTE?)",
        "Politica real (LASIK gratuito, 5% lei, etc)",
        "Implementacao em escala municipal/estadual",
        "MEDIA (raro encontrar)",
    ),
    Alliance(
        "movimento", "MST (reforma agraria)",
        "OpenTrator + OpenAgrarian + OpenCredit para assentamentos",
        "1.500 assentamentos. 1M+ pessoas.",
        "ALTISSIMA",
    ),
    Alliance(
        "movimento", "MTST (moradia)",
        "OpenDignity + OpenCivilConstruction para ocupacoes",
        "500k+ familias sem moradia adequada",
        "ALTA",
    ),
]


// ============================================================================
// 6. FRENTE 5: PRODUTO PUBLICO USAVEL
// ============================================================================

// decorador: @dataclass
classe PublicProduct:
    // Ferramenta que QUALQUER pessoa pode usar HOJE.
    name: texto
    what: texto
    why_viral: texto
    platform: texto
    status: texto


seja PUBLIC_PRODUCTS: [PublicProduct] = [
    PublicProduct(
        "Simulador de Salario",
        "Voce entra salario. Sistema mostra quanto produz vs recebe.",
        "TODO trabalhador quer saber. Compartilha com colega.",
        "Web (HTML simples). Link no X.",
        "FAZER AGORA",
    ),
    PublicProduct(
        "Calculadora 5%",
        "Voce entra valor produzido. Mostra quanto dono/banco suga.",
        "Choque visual. Viraliza em grupo de WhatsApp.",
        "Web + bot Telegram.",
        "FAZER AGORA",
    ),
    PublicProduct(
        "Landing Page",
        "1 pagina: o que e', como comeca, onde baixa.",
        "Ponto de entrada. Link para tudo.",
        "Web (1 HTML). GitHub Pages.",
        "FAZER AGORA",
    ),
    PublicProduct(
        "Bot X @OpenRepublic",
        "Bot no X que responde perguntas sobre a Republica.",
        "Interativo. Pessoas perguntam 'como funciona X?'",
        "API X + Python.",
        "FAZER (precisa OAuth X)",
    ),
    PublicProduct(
        "App OpenRepair Finder",
        "Acha FabLab/tecnico mais proximo pra consertar.",
        "Pratico. Todo mundo precisa um dia.",
        "Web + mobile.",
        "FAZER DEPOIS",
    ),
    PublicProduct(
        "App OpenCredit Local",
        "App de moeda social para seu grupo de amigos/comunidade.",
        "Pratico. Usa hoje. Sem banco.",
        "Mobile + Web.",
        "FAZER DEPOIS",
    ),
]


// ============================================================================
// 7. MOTOR DE PROPAGACAO
// ============================================================================

classe PropagationEngine:
    // Motor que executa a estrategia de divulgacao.

    PRINCIPIO FUNDAMENTAL:
    nao GRITE. DEMONSTRE.

    A Republica nao precisa de marketing.
    Precisa de PROVA. Um piloto funcionando vale mais que 1000 threads.
    Mas 1000 threads sobre um piloto funcionando vale MILHOES.

    ORDEM DE EXECUCAO:
    1. FAZER piloto (agua no sertao, saude na favela)
    2. DOCUMENTAR piloto (video + dados + antes/depois)
    3. VIRALIZAR documentacao (X, video, imprensa)
    4. CONSTRUIR ferramenta publica (simulador, landing page)
    5. ALIANCAS amplificam (artistas, ONGs, jornalistas)
    6. COMUNIDADES espalham (CONAQ, MST, G10, ASA)

    CRONOGRAMA:
    Semana 1-2: Landing page + simulador + thread de lancamento
    Mes 1: Piloto // 1 (agua ou saude) + documentacao + viralizacao
    Mes 2-3: Piloto // 2 + aliancas + content continuo no X
    Mes 4-6: 3+ pilotos + imprensa + expansao comunitaria
    Mes 6-12: Escala nacional + reconhecimento
    // 

    funcao __init__(self):
        self.pilots = PILOTS
        self.content = CONTENT
        self.communities = COMMUNITY_STRATEGY
        self.alliances = ALLIANCES
        self.products = PUBLIC_PRODUCTS

    funcao execution_plan(self) -> [Dict]:
        // Plano de execucao cronologico.
        retorne [
            {
                "fase": "SEMANA 1-2: PREPARACAO",
                "acoes": [
                    "Landing page (1 HTML, GitHub Pages, CC0)",
                    "Simulador de salario (web, compartilhavel)",
                    "Calculadora 5% (web, compartilhavel)",
                    "Repositorio publico (GitHub, organizado, com README)",
                    "Thread de lancamento no X (@clouramlearning)",
                    "Reunir 5-10 pessoas (nucleo fundador)",
                ],
                "custo": "R$ 0",
                "resultado": "Republica visivel na internet. Ponto de entrada.",
            },
            {
                "fase": "MES 1: PILOTO #1",
                "acoes": [
                    "Escolher 1 comunidade (sertao=agua OU favela=saude)",
                    "Implementar 1 solucao (cisterna OU clinica)",
                    "Documentar TUDO (video 3min + dados + antes/depois)",
                    "Thread no X: 'Fizemos X acontecer. Ve o resultado.'",
                    "Enviar para jornalistas (Folha, G1, UOL, Intercept)",
                    "Enviar para youtubers (Tecnicas, Nostalgia, etc)",
                ],
                "custo": "R$ 15.000-100.000 (1 piloto)",
                "resultado": "1 comunidade real funcionando. Prova.",
            },
            {
                "fase": "MES 2-3: VIRALIZACAO + PILOTO #2",
                "acoes": [
                    "Piloto #2 (tipo diferente: favela ou ribeirinho)",
                    "Conteudo no X: 2 threads/semana (dados + emocao)",
                    "Video YouTube: documento de 15min do piloto #1",
                    "Contatar artistas (funk/rap) para OpenMusic",
                    "Contatar ONGs (Palmas, ASA, CONAQ)",
                    "Simulador atingindo 100k usuarios",
                ],
                "custo": "R$ 20.000-50.000",
                "resultado": "2 comunidades. Alcance 500k+. Primeiras aliancas.",
            },
            {
                "fase": "MES 4-6: ESCALA",
                "acoes": [
                    "3+ pilotos em tipos diferentes",
                    "Cada piloto gera 10x conteudo",
                    "Imprensa nacional (se piloto for forte)",
                    "Artista lanca musica na plataforma OpenMusic",
                    "CONAQ/MST/G10/ASA recebem toolkit",
                    "Simulador atingindo 1M usuarios",
                ],
                "custo": "R$ 50.000-200.000",
                "resultado": "5+ comunidades. Alcance 5M+. Movimento real.",
            },
            {
                "fase": "MES 6-12: MOVIMENTO NACIONAL",
                "acoes": [
                    "Politico proposta (LASIK gratuito, 5% lei, etc)",
                    "Imprensa internacional (BBC, NYT, Al Jazeera)",
                    "Documentario (Netflix ou YouTube)",
                    "10+ comunidades em rede",
                    "OpenCredit operando em 3+ cidades",
                    "App mobile lancado",
                ],
                "custo": "R$ 200.000-500.000",
                "resultado": "Movimento nacional. Republica nao e mais teoria.",
            },
        ]

    funcao content_calendar(self) -> [Dict]:
        // Calendario de conteudo semanal no X.
        retorne [
            {"dia": "Segunda", "tipo": "Thread de dados",
             "exemplo": "Simulacao salario real (pedreiro/medico/cozinheira)"},
            {"dia": "Terca", "tipo": "Video curto",
             "exemplo": "OpenRepair: conserto em 2 min"},
            {"dia": "Quarta", "tipo": "Thread de ciencia",
             "exemplo": "Neuroplasticidade. Antideterminismo. Saude mental."},
            {"dia": "Quinta", "tipo": "Piloto/casoreal",
             "exemplo": "Comunidade que implementou. Antes/depois."},
            {"dia": "Sexta", "tipo": "Pauta universal",
             "exemplo": "Spam telefonico proibido (94% apoiam)"},
            {"dia": "Sabado", "tipo": "Cultura",
             "exemplo": "Funk/Rap/Samba patrimonio. Sem ECAD."},
            {"dia": "Domingo", "tipo": "OpenWololo",
             "exemplo": "Responde duvidas/criticas. Demonstra."},
        ]

    funcao key_metrics(self) -> [Dict]:
        // Metricas para medir se a estrategia funciona.
        retorne [
            {"metrica": "Seguidores X (@clouramlearning)",
             "meta_3meses": "10.000",
             "meta_6meses": "50.000",
             "meta_12meses": "200.000"},
            {"metrica": "Comunidades com piloto",
             "meta_3meses": "3",
             "meta_6meses": "10",
             "meta_12meses": "50"},
            {"metrica": "Usuarios simulador",
             "meta_3meses": "50.000",
             "meta_6meses": "500.000",
             "meta_12meses": "5.000.000"},
            {"metrica": "Pessoas em OpenCredit",
             "meta_3meses": "100",
             "meta_6meses": "5.000",
             "meta_12meses": "50.000"},
            {"metrica": "Materias imprensa",
             "meta_3meses": "5",
             "meta_6meses": "20",
             "meta_12meses": "100"},
            {"metrica": "Artistas na plataforma",
             "meta_3meses": "5",
             "meta_6meses": "50",
             "meta_12meses": "500"},
            {"metrica": "Contribuidores repositorio",
             "meta_3meses": "10",
             "meta_6meses": "100",
             "meta_12meses": "1.000"},
        ]

    funcao what_NOT_to_do(self) -> [texto]:
        // Erros que matam a estrategia.
        retorne [
            "NAO gritar teoria antes de ter prova (ninguem ouve)",
            "NAO atacar sistema atual sem ter alternativa rodando",
            "NAO pedir dinheiro sem mostrar resultado",
            "NAO falar para politico antes de ter comunidade funcionando",
            "NAO postar 20x/dia (saturacao). 1-2x/dia com qualidade",
            "NAO usar jargao ('Republica', 'P1-P4') sem contexto",
            "NAO discutir com haters (OpenWololo: demonstrar, nao debater)",
            "NAO prometer o que nao tem (ex: 'imortalidade') antes do basico",
            "NAO esquecer: 1 comunidade real > 1000 linhas de teoria",
            "NAO ignorar X (e o canal principal do fundador)",
        ]

    funcao stats(self) -> {texto: qualquer}:
        retorne {
            "pilotos_planejados": tamanho(self.pilots),
            "pecas_conteudo": tamanho(self.content),
            "estrategias_comunitarias": tamanho(self.communities),
            "aliancas_potenciais": tamanho(self.alliances),
            "produtos_publicos": tamanho(self.products),
            "principio": "Nao grite. Demonstre. 1 prova > 1000 teorias.",
        }


// ============================================================================
// 8. MAIN
// ============================================================================

se __name__ == "__main__" entao:
    engine = PropagationEngine()

    imprima("=" * 80)
    imprima("  OPENPROPAGATION -- ESTRATEGIA DE DIVULGACAO MASSIVA")
    imprima("  Nao grite. Demonstre. 1 prova > 1000 teorias.")
    imprima("=" * 80)

    // === 1. AS 5 FRENTES ===
    imprima("\n\n  === AS 5 FRENTES DE PROPAGACAO ===\n")
    imprima("  1. DEMONSTRACAO REAL (piloto funcionando) -- A QUE MATRIA")
    imprima("  2. CONTEUDO VIRAL (X/Twitter, video, infografico)")
    imprima("  3. COMUNIDADES REAIS (CONAQ, MST, G10, ASA)")
    imprima("  4. ALIANCAS (artistas, ONGs, jornalistas)")
    imprima("  5. PRODUTO PUBLICO (simulador, app, landing page)")

    // === 2. PILOTOS ===
    imprima("\n\n  === PILOTOS REAIS ({len(engine.pilots)}) ===\n")
    para cada p em engine.pilots:
        imprima("\n  {p.name} ({p.location})")
        imprima("    Demonstra: {p.what_demonstrates}")
        imprima("    Impacto: {p.expected_impact}")
        imprima("    Custo: {p.cost}")
        imprima("    Prazo: {p.timeline}")
        imprima("    Viral: {p.viral_potential}")
        imprima("    Doc: {p.documentation}")

    // === 3. CONTEUDO ===
    imprima("\n\n  === CONTEUDO VIRAL ({len(engine.content)}) ===\n")
    para cada c em engine.content:
        imprima("\n  [{c.format}] {c.topic}")
        imprima("    Hook: '{c.hook}'")
        imprima("    Plataforma: {c.platform}")
        imprima("    CTA: {c.call_to_action}")
        imprima("    Esperado: {c.expected_reach}")

    // === 4. COMUNIDADES ===
    imprima("\n\n  === EXPANSAO COMUNITARIA ({len(engine.communities)}) ===\n")
    para cada c em engine.communities:
        imprima("  {c.strategy}")
        imprima("    Metodo: {c.method}")
        imprima("    Fator: {c.expansion_factor}")

    // === 5. ALIANCAS ===
    imprima("\n\n  === ALIANCAS ({len(engine.alliances)}) ===\n")
    para cada a em engine.alliances:
        imprima("  [{a.priority}] {a.ally_type}: {a.who}")
        imprima("    Eles ganham: {a.what_they_gain[:60]}")
        imprima("    Republica ganha: {a.what_republica_gains[:60]}")

    // === 6. PRODUTOS PUBLICOS ===
    imprima("\n\n  === PRODUTOS PUBLICOS USAVEIS ({len(engine.products)}) ===\n")
    para cada p em engine.products:
        imprima("  [{p.status}] {p.name}")
        imprima("    O que: {p.what}")
        imprima("    Viraliza porque: {p.why_viral}")

    // === 7. PLANO DE EXECUCAO ===
    imprima("\n\n  === PLANO DE EXECUCAO ===\n")
    plan = engine.execution_plan()
    para cada fase em plan:
        imprima("\n  {fase['fase']}:")
        para cada acao em fase["acoes"]:
            imprima("    -> {acao}")
        imprima("    Custo: {fase['custo']}")
        imprima("    Resultado: {fase['resultado']}")

    // === 8. CALENDARIO ===
    imprima("\n\n  === CALENDARIO DE CONTEUDO (X/Twitter) ===\n")
    cal = engine.content_calendar()
    para cada day em cal:
        imprima("  {day['dia']:<12} {day['tipo']}: {day['exemplo']}")

    // === 9. METRICAS ===
    imprima("\n\n  === METRICAS ===\n")
    para cada m em engine.key_metrics():
        imprima("  {m['metrica']}")
        imprima("    3 meses: {m['meta_3meses']}")
        imprima("    6 meses: {m['meta_6meses']}")
        imprima("    12 meses: {m['meta_12meses']}")

    // === 10. O QUE NAO FAZER ===
    imprima("\n\n  === O QUE NAO FAZER (ERROS QUE MATAM) ===\n")
    para cada dont em engine.what_NOT_to_do():
        imprima("  X {dont}")

    // === STATS ===
    imprima("\n\n  === ESTATISTICAS ===\n")
    s = engine.stats()
    para cada (k, v) em s.items():
        imprima("  {k:<30} {v}")

    imprima("\n{'='*80}")
    imprima("  OpenPropagation: {s['pilotos_planejados']} pilotos, "
          "{s['pecas_conteudo']} pecas de conteudo, "
          "{s['aliancas_potenciais']} aliancas.")
    imprima("  {s['principio']}")
    imprima("{'='*80}")

```
