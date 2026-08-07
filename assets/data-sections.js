/* ============================================================
   DATA-SECTIONS — Renderizador genérico de capítulos de dados
   ------------------------------------------------------------
   Lê as 34 seções orfãs do JSON e cria capítulos dinamicamente,
   sem precisar de HTML manual para cada uma. Cada seção vira um
   bloco visual com: resumo (dict), tabelas (list), e veredito.

   Todos os IDs/classes prefixados com "ds-" para não colidir.
   ============================================================ */

(function () {
  'use strict';

  // Agrupamento das 34 seções orfãs em capítulos temáticos.
  // Cada capítulo recebe um número, título e lista de seções JSON.
  var CHAPTERS = [
    {
      no: 'A',
      kicker: 'Programa e método',
      title: 'O sistema OpenRepublic',
      lede: 'O programa completo: o manifesto, o que se exige de um candidato, a frente comunista unida e propostas prontas para executar.',
      sections: ['manifesto', 'requisitos_politico', 'frente_comunista_unida', 'propostas_executaveis', 'procura_se_candidatos'],
    },
    {
      no: 'B',
      kicker: '27 estados, 27 realidades',
      title: 'Mapa do Brasil',
      lede: 'Cada estado com seu inferno: população, renda mediana, emergências e desafios de governar e legislar.',
      sections: ['mapa_estados'],
      special: 'mapa',
    },
    {
      no: 'C',
      kicker: 'Políticos sob medição',
      title: 'Rankings e dossiês',
      lede: 'Quem passa no corte, quem está em análise, quem está bloqueado. Quanto dinheiro público cada um mexe, quanto tem de patrimônio e onde há desvio.',
      sections: ['rankings_politicos', 'ranking_dinheiro_publico', 'dados_eleitorais'],
      special: 'rankings',
    },
    {
      no: 'D',
      kicker: 'Vidas em risco',
      title: 'Saúde e educação',
      lede: 'Hospital sem dinheiro, aluno sem aprender, 1 em cada 4 adultos que não entende o que lê. Estado por estado e por cor, para você ver a diferença.',
      sections: ['saude_detalhada', 'educacao_detalhada'],
    },
    {
      no: 'E',
      kicker: 'Direitos e dignidade',
      title: 'Direitos humanos e moradia',
      lede: 'Mulher morta por ser mulher, violência contra LGBTQIA+, racismo no dia a dia, falta de casa, falta de esgoto e favela.',
      sections: ['direitos_humanos', 'moradia_cidades'],
    },
    {
      no: 'F',
      kicker: 'Terra, energia e ambiente',
      title: 'Recursos e território',
      lede: 'Poucas famílias com quase toda a terra, floresta queimada, veneno na comida, pré-sal e povos que o Brasil esquece.',
      sections: ['ambiente_detalhado', 'reforma_agraria', 'energia_detalhada', 'povos_originarios'],
    },
    {
      no: 'G',
      kicker: 'Sistema e poder',
      title: 'Justiça, drogas e militarismo',
      lede: 'Justiça que nunca chega, prisão cheia de pobre e negro, droga tratada como doença, dinheiro em arma e polícia que mata.',
      sections: ['sistema_justica', 'drogas_reducao_danos', 'militarismo'],
    },
    {
      no: 'H',
      kicker: 'Dinheiro e poder',
      title: 'Impostos, transporte e comunicação',
      lede: 'Pobre paga mais imposto que rico, a tarifa de ônibus come o seu salário, poucos grupos mandam na informação e meio país segue sem internet.',
      sections: ['tributacao', 'transporte_mobilidade', 'midia_comunicacao'],
    },
    {
      no: 'I',
      kicker: 'Quem manda no Congresso',
      title: 'Bancadas, ciência e cultura',
      lede: 'Quem manda no Congresso: a bancada do campo, a bancada da fé e a bancada da bala. Ciência sem verba, cultura no osso — e quem resiste.',
      sections: ['bancadas_parlamentares', 'ciencia_tecnologia', 'cultura', 'movimentos_sociais'],
    },
    {
      no: 'J',
      kicker: 'Brasil no mundo',
      title: 'Imigrantes e história',
      lede: 'Quem chega fugindo de guerra, os 524 anos de Brasil em eras — exploração, escravidão, ditadura — e o que sobrou de cada uma.',
      sections: ['imigrantes_refugiados', 'historia_brasil_524_anos'],
    },
    {
      no: 'K',
      kicker: 'Ferramentas de ação',
      title: 'Frases, hashtags e manchetes',
      lede: 'Frases prontas para debate, hashtags, manchetes e carrosséis. Pega, personaliza e espalha.',
      sections: ['dados_para_acao', 'carrosseis_instagram'],
      special: 'acao',
    },
    {
      no: 'L',
      kicker: 'Estratégia de poder',
      title: 'Mapa de contrapoder',
      lede: 'Sem a presidência, onde o contrapoder dá retorno? Não é chegando em segundo — é travando Congresso, governadorias estratégicas e narrativa ao mesmo tempo. O mapa de onde construir poder efetivo.',
      sections: ['mapa_contrapoder'],
    },
  ];

  // Mapa de títulos amigáveis para cada seção do JSON
  var SECTION_TITLES = {
    manifesto: 'Manifesto',
    requisitos_politico: 'Requisitos para político',
    frente_comunista_unida: 'Frente Comunista Unida',
    propostas_executaveis: 'Propostas executáveis',
    procura_se_candidatos: 'Procura-se candidatos',
    mapa_estados: '27 estados',
    rankings_politicos: 'Ranking de políticos',
    ranking_dinheiro_publico: 'Dinheiro público',
    dados_eleitorais: 'Dados eleitorais',
    dossie_politicos: 'Dossiês de políticos',
    saude_detalhada: 'Saúde',
    educacao_detalhada: 'Educação',
    direitos_humanos: 'Direitos humanos',
    moradia_cidades: 'Moradia e cidades',
    ambiente_detalhado: 'Ambiente',
    reforma_agraria: 'Reforma agrária',
    energia_detalhada: 'Energia',
    povos_originarios: 'Povos originários',
    sistema_justica: 'Sistema de justiça',
    drogas_reducao_danos: 'Drogas e redução de danos',
    militarismo: 'Militarismo',
    tributacao: 'Tributação',
    transporte_mobilidade: 'Transporte e mobilidade',
    midia_comunicacao: 'Mídia e comunicação',
    bancadas_parlamentares: 'Bancadas parlamentares',
    ciencia_tecnologia: 'Ciência e tecnologia',
    cultura: 'Cultura',
    movimentos_sociais: 'Movimentos sociais',
    imigrantes_refugiados: 'Imigrantes e refugiados',
    historia_brasil_524_anos: '524 anos de Brasil',
    dados_para_acao: 'Dados para ação',
    mapa_contrapoder: 'Mapa de contrapoder',
  };

  // ============================================================
  // HELPERS
  // ============================================================

  function esc(s) {
    if (s === null || s === undefined) return '';
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  // Converte underscore_case para texto legível
  function humanize(key) {
    return key
      .replace(/_/g, ' ')
      .replace(/\b\w/g, function (c) { return c.toUpperCase(); });
  }

  // Rótulos simples (linguagem do dia a dia) para as chaves técnicas das
  // grades de resumo. Se a chave não estiver aqui, usa humanize().
  var STAT_LABELS = {
    gasto_pct_pib: 'Gasto com saúde (do PIB)',
    gasto_per_capita_anual: 'Gasto com saúde por pessoa, por ano',
    medicos_por_mil_habitantes: 'Médicos por mil habitantes',
    enfermeiros_por_mil: 'Enfermeiros por mil habitantes',
    leitos_sus_por_mil: 'Leitos do SUS por mil habitantes',
    cobertura_atencao_basica: 'Pessoas com posto de saúde perto',
    ideb_brasil_2023: 'Nota do ensino básico (Ideb 2023)',
    meta_ideb_2023: 'Meta para o Ideb 2023',
    pisa_brasil: 'Nota no teste internacional (PISA)',
    gasto_por_aluno_ano: 'Gasto por aluno, por ano',
    analfabetismo_absoluto: 'Adultos que não sabem ler nem escrever',
    analfabetismo_funcional: 'Adultos que não entendem o que leem',
    criancas_fora_escola: 'Crianças fora da escola',
    evasao_ensino_medio: 'Jovens que abandonam o ensino médio',
    homicidios_2023: 'Homicídios em 2023',
    taxa_homicidios_2023: 'Taxa de homicídios (por 100 mil)',
    taxa_2017_pico: 'Pior momento já medido (2017)',
    feminicidio_2023: 'Mulheres mortas por serem mulheres',
    morte_por_policia_2023: 'Mortes causadas pela polícia',
    morte_de_policiais_2023: 'Policiais mortos',
    estupro_2023: 'Estupros registrados (2023)',
    encarceramento: 'Pessoas presas',
    desemprego_2025: 'Desemprego (2025)',
    informalidade: 'Trabalhadores sem carteira e sem direitos',
    renda_mediana_mensal: 'Renda do meio do país (mediana)',
    renda_p10: 'Renda dos 10% mais pobres',
    renda_p99: 'Renda do 1% mais rico',
    trabalho_infantil: 'Crianças em trabalho infantil',
    trabalho_escravo_estimado: 'Pessoas em trabalho escravo (estimativa)',
    trabalho_escravo_resgatado_2023: 'Resgatadas em 2023',
    desmatamento_amazonia_2023: 'Desmatamento na Amazônia (2023)',
    desmatamento_amazonia_2024_tendencia: 'Desmatamento na Amazônia (tendência 2024)',
    desmatamento_cerrado_2023: 'Desmatamento no Cerrado (2023)',
    desmatamento_pantanal: 'Desmatamento no Pantanal',
    queimadas_focos_2024: 'Focos de queimada (2024)',
    agrotoxicos_uso_2023: 'Veneno na lavoura, por ano',
    brasil_pct_agrotoxicos_mundial: 'Brasil no consumo mundial de veneno',
    deficit_habitacional: 'Falta de moradia (déficit)',
    sem_teto: 'Pessoas sem casa',
    favelas_habitantes: 'Moradores de favela',
    sem_agua_tratada: 'Sem água tratada em casa',
    sem_esgoto: 'Sem coleta de esgoto',
    sem_coleta_lixo: 'Sem coleta de lixo',
    aluguel_pct_renda_periferia: 'Da renda da periferia gasta com aluguel',
    idh_brasil: 'Qualidade de vida (IDH)',
    pib_mundial_rank: 'Economia no ranking mundial',
    gini_brasil: 'Desigualdade (Gini)',
    percepcao_corrupcao_rank: 'Posição no ranking de corrupção',
    violencia_rank: 'Posição no ranking de violência',
    pisa_rank: 'Posição na educação (PISA)',
    matriz_energetica_renovavel_pct: 'Energia renovável (toda a matriz)',
    matriz_eletrica_renovavel_pct: 'Energia elétrica renovável',
    hidreletrica_pct_geracao: 'Das hidrelétricas',
    eolica_pct: 'Dos ventos (eólica)',
    solar_pct: 'Do sol (solar)',
    gas_carvao_termica_pct: 'De gás e carvão',
    nuclear_pct: 'Nuclear',
    sem_acesso_energia_eletrica: 'Pessoas sem luz em casa',
    pre_sal_producao_barris_dia: 'Barris de petróleo do pré-sal por dia',
    concentracao_fundiaria_gini: 'Concentração de terra (Gini)',
    latifundios_1000_plus_hectares_pct_fazendas: 'Fazendas gigantes (mais de 1.000 hectares)',
    latifundios_controlam_terra_pct: 'Da terra nas mãos dessas fazendas',
    minifundios_pct_fazendas: 'Pequenas propriedades',
    minifundios_controlam_terra_pct: 'Da terra nas mãos das pequenas',
    assentamentos_incra: 'Assentamentos criados',
    familias_assentadas: 'Famílias assentadas',
    conflitos_campo_2023: 'Conflitos no campo (2023)',
    assassinatos_campo_2023: 'Assassinatos no campo (2023)',
    processos_em_andamento: 'Processos na Justiça',
    taxa_litigiosidade: 'Ações por 100 mil habitantes',
    tempo_medio_processo: 'Tempo médio de um processo',
    presos_provisorios_pct: 'Presos sem julgamento',
    populacao_prisional: 'População presa',
    presos_sem_defensoria: 'Presos sem defensor',
    usuarios_cocaina_estimado: 'Usuários de cocaína (estimativa)',
    usuarios_crack_estimado: 'Usuários de crack',
    mortalidade_usuarios_crack_5anos: 'Morte entre usuários de crack em 5 anos',
    estupro_relacao_drogas: 'Estupros ligados a drogas',
    prisoes_drogas_pct_total: 'Prisões por tráfico de drogas',
    orcamento_defesa_2025: 'Orçamento da Defesa (2025)',
    efetivo_total: 'Militares no total',
    ranking_mundial_gasto: 'Posição mundial em gasto militar',
    gasto_militar_pct_pib: 'Do PIB em gasto militar',
    pensions_militares_anual: 'Pensões militares por ano',
    militares_na_politica_pos_1964: 'Militares na política desde 1964',
    refugiados_reconhecidos: 'Refugiados reconhecidos',
    solicitantes_refugio: 'Pedidos de refúgio',
    venezuelanos_acolhidos: 'Venezuelanos acolhidos',
    venezuelanos_interiorizados: 'Venezuelanos levados a outras cidades',
    haitianos: 'Haitianos',
    carga_tributaria_pct_pib: 'Impostos sobre tudo que o país produz',
    ranking_mundial_carga: 'Posição mundial em carga de imposto',
    arrecadacao_total_2024: 'Arrecadação total (2024)',
    sistema: 'Sistema tributário',
    impostos_consumo_pct: 'Impostos sobre o que se compra',
    impostos_renda_pct: 'Impostos sobre o que se ganha',
    impostos_patrimonio_pct: 'Impostos sobre o que se tem',
    tarifa_media_onibus_capitais: 'Tarifa média de ônibus nas capitais',
    tarifa_pct_renda_media_capitais: 'Da renda gasta com a tarifa',
    extensao_metro_km: 'Extensão de metrô',
    cidades_com_metro: 'Cidades com metrô',
    frota_veiculos_milhoes: 'Frota de veículos',
    mortes_transito_ano: 'Mortes no trânsito por ano',
    investimento_necessario_mobilidade_2042: 'O que falta investir em mobilidade até 2042',
    congresso_total_parlamentares: 'Parlamentares no total',
    bancada_ruralista: 'Bancada do campo (ruralista)',
    bancada_evangelica: 'Bancada evangélica',
    bancada_da_bala: 'Bancada da bala (segurança)',
    sobreposicao: 'Parlamentares em mais de uma bancada',
    orcamento_mcti_2025: 'Orçamento da ciência (2025)',
    orcamento_cnpq_bolsas_2021: 'Bolsas do CNPq (2021)',
    bolsas_aprovadas_vs_pagas_2021: 'Bolsas aprovadas que foram pagas (2021)',
    orcamento_capes_cortes_2026: 'Corte na Capes (2026)',
    fuga_cerebros: 'Cientistas que vão embora',
    investimento_pct_pib: 'Do PIB investido em ciência',
    orcamento_ministerio_cultura_2025: 'Orçamento do Ministério da Cultura (2025)',
    lei_rouanet_2024: 'Dinheiro da Lei Rouanet (2024)',
    lei_rouanet_2025_estimado: 'Lei Rouanet (estimativa 2025)',
    pct_renuncia_fiscal_cultura: 'Do orçamento aberto mão para a cultura',
    pib_cultural_pct: 'Da economia vem da cultura',
    empregos_cultura_milhoes: 'Empregos na cultura',
    populacao_indigena_2022: 'Indígenas no Brasil (2022)',
    '305_etnias': 'Etnias',
    '274_linguas': 'Línguas',
    terras_indigenas_demarcadas: 'Terras indígenas demarcadas',
    terras_em_processo_demarcacao: 'Terras em processo de demarcação',
    criancas_yanomami_mortas_2_anos: 'Crianças Yanomami mortas em 2 anos',
    demarcacoes_2023_2024: 'Demarcações feitas em 2023-2024',
    total_avaliados: 'Políticos avaliados',
    aprovados_score_4plus: 'Aprovados (nota 4,0 ou mais)',
    em_analise: 'Em análise',
    bloqueados_wo: 'Bloqueados (sem proposta)',
    taxa_aprovacao: 'Taxa de aprovação',
    congresso_score_medio: 'Nota média do Congresso',
    principio: 'O princípio',
    taxa: 'Taxa',
    estado: 'Estado',
    ranking: 'Posição',
    populacao: 'População',
    p50: 'Renda do meio do estado',
    ideb: 'Nota do ensino',
    nota: 'Nota',
    variacao: 'Mudança',
    desmatamento_km2: 'Desmatamento (km²)',
    pct_negro: 'Negros entre as vítimas',
    total: 'Total',
    nome: 'Nome',
    partido: 'Partido',
    cargo: 'Cargo',
    ano: 'Ano',
    cidade: 'Cidade',
    regiao: 'Região',
    sexo: 'Sexo',
    raca: 'Raça',
    idade: 'Idade',
    poder: 'Poder',
    custo_disputa: 'Custo de disputa',
    atual_situacao: 'Situação atual',
    valor_estrategico: 'Valor estratégico',
    instrumento: 'Instrumento',
    frente: 'Frente',
    exemplo_projeto: 'Exemplo / referência',
    estrategia: 'Estratégia',
    tamanho_necessario: 'Tamanho necessário',
    senadores_necessarios: 'Senadores necessários',
    o_que_trava: 'O que trava',
    custo_estimado: 'Custo estimado',
    retorno: 'Retorno',
    cargo: 'Cargo',
    poder_constitucional: 'Poder constitucional',
    poder_real: 'Poder real',
    custo_conquistar: 'Custo de conquistar',
    mandato: 'Mandato',
    base_eleitoral: 'Base eleitoral',
    dificuldade: 'Dificuldade',
    papel_no_contrapoder: 'Papel no contrapoder',
    posicao: 'Posição',
    ator: 'Ator',
    por_que: 'Por quê',
    tese: 'A tese',
    meta_congresso: 'Meta no Congresso',
    meta_governadorias: 'Meta nas governadorias',
    meta_narrativa: 'Meta na narrativa',
    custo_presidencial_vs_congresso: 'Presidência vs. Congresso (custo)',
  };

  // Títulos simples para os sub-blocos das seções (chaves aninhadas).
  var SUB_LABELS = {
    indicadores_criticos: 'O que está crítico',
    desigualdade_racial_saude: 'Cor e saúde: quem morre mais',
    ranking_mortalidade_infantil_por_estado_top5: 'Onde mais bebês morrem (5 estados)',
    ranking_ideb_anos_finais_2023_top5: 'Melhores notas do ensino (Ideb, 5 estados)',
    ranking_ideb_anos_finais_2023_bottom5: 'Piores notas do ensino (Ideb, 5 estados)',
    desigualdade_racial_educacao: 'Cor e escola: quem fica para trás',
    perfil_das_vitimas: 'Quem são as vítimas',
    encarceramento: 'Quem está preso',
    racismo_estrutural_violencia: 'A violência e o racismo',
    distribuicao_renda_decil: 'A escada da renda, degrau por degrau',
    desigualdade_racial_renda: 'Cor e renda',
    trabalho_infantil: 'Crianças trabalhando',
    trabalho_escravo: 'Trabalho escravo',
    ranking_desemprego_por_estado: 'Desemprego por estado',
    desmatamento_por_bioma: 'Desmatamento por bioma',
    agrotoxicos: 'Veneno na lavoura',
    ranking_desmatamento_amazonia_por_estado: 'Desmatamento da Amazônia por estado',
    violencia_contra_mulher: 'Violência contra a mulher',
    violencia_lgbtqia: 'Violência contra LGBTQIA+',
    racismo_estrutural: 'O racismo no dia a dia',
    povos_tradicionais: 'Povos tradicionais',
    pessoas_com_deficiencia: 'Pessoas com deficiência',
    populacao_rua: 'Gente morando na rua',
    saneamento: 'Água e esgoto',
    favelas: 'Favelas',
    ranking_deficit_habitacional_por_estado: 'Falta de casa por estado',
    concentracao: 'Poucos grupos mandam na mídia',
    exclusao_digital: 'Quem fica sem internet',
    radio_comunitaria: 'Rádio comunitária',
    desinformacao: 'Mentira espalhada',
    brasil_vs_ocde: 'Brasil contra os países ricos',
    brasil_vs_america_latina: 'Brasil contra a América Latina',
    brasil_vs_pares_emergentes: 'Brasil contra outros países emergentes',
    matriz_eletrica_2024: 'De onde vem a luz (2024)',
    petroleo_pre_sal: 'O pré-sal',
    acesso_energia: 'Quem fica sem luz',
    transicao_energetica: 'Trocar o petróleo por energia limpa',
    concentracao_fundiaria: 'Poucos donos de muita terra',
    reforma_agraria_historico: 'Reforma agrária na história',
    violencia_campo: 'Violência no campo',
    agricultura_familiar: 'Quem alimenta o Brasil',
    morosidade: 'Justiça que demora',
    encarceramento_seletivo: 'Prisão que escolhe',
    impunidade_corrupcao: 'Corrupção sem punição',
    seletividade_racial: 'A cor da cadeia',
    crack_no_brasil: 'O crack no Brasil',
    reducao_de_danos: 'Tratar em vez de prender',
    guerra_as_drogas: 'A guerra às drogas',
    gastos_militares: 'Gasto com militares',
    militares_na_politica: 'Militares na política',
    policia_militar: 'A polícia que mata',
    operacao_acolhida: 'Operação Acolhida',
    refugiados_por_origem: 'Refugiados por país de origem',
    xenofobia_e_racismo: 'Medo do diferente',
    regressividade: 'Quem mais paga imposto',
    reforma_tributaria_2024: 'A reforma tributária (2024)',
    ranking_carga_tributaria_internacional: 'Imposto pelo mundo',
    tarifa_vs_renda: 'A tarifa contra o salário',
    metros_do_brasil: 'Os metrôs do Brasil',
    mortalidade_transito: 'Morte no trânsito',
    tarifa_zero: 'Tarifa zero',
    bancada_ruralista: 'Bancada do campo',
    bancada_evangelica: 'Bancada evangélica',
    bancada_da_bala: 'Bancada da bala',
    parlamento_x_populacao: 'Congresso contra a população',
    cortes_orcamentarios: 'Cortes no orçamento',
    fuga_de_cérebros: 'Cientistas que vão embora',
    comparativo_internacional_ciencia: 'Ciência pelo mundo',
    inovacao_e_tecnologia: 'Inovação e tecnologia',
    leis_de_incentivo: 'Lei Rouanet e incentivos',
    desmonte_cultural_2019_2022: 'O desmonte da cultura (2019-2022)',
    concentracao_regional_cultural: 'Cultura concentrada em poucos estados',
    cultura_popular_tradicional: 'A cultura do povo',
    maiores_povos: 'Os maiores povos',
    crise_yanomami: 'A crise Yanomami',
    demarcacao_de_terras: 'Demarcação de terras',
    violencia_contra_indigenas: 'Violência contra indígenas',
    agentes_saude_indigena: 'Saúde indígena',
    movimentos_de_destaque: 'Movimentos que fazem a diferença',
    pilares: 'Os pilares',
    requisitos: 'Requisitos',
    coalizao: 'A coalizão',
    stats: 'Números',
    nos_de_poder: 'Os nós de poder',
    alvos_congresso: 'Alvos no Congresso',
    alvos_governadores: 'Alvos nas governadorias',
    alvos_narrativa: 'Frente de narrativa',
    hierarquia_poder: 'Hierarquia do poder',
    presidencia: 'Presidência',
    congresso: 'Congresso',
    governadores: 'Governadores',
    judiciario: 'Judiciário',
    sociedade_civil: 'Sociedade civil',
    cargo: 'Cargo',
    poder_constitucional: 'Poder constitucional',
    poder_real: 'Poder real',
    custo_conquistar: 'Custo de conquistar',
    mandato: 'Mandato',
    base_eleitoral: 'Base eleitoral',
    dificuldade: 'Dificuldade',
    papel_no_contrapoder: 'Papel no contrapoder',
    estrategia: 'Estratégia',
    tamanho_necessario: 'Tamanho necessário',
    senadores_necessarios: 'Senadores necessários',
    o_que_trava: 'O que trava',
    custo_estimado: 'Custo estimado',
    retorno: 'Retorno',
    valor_estrategico: 'Valor estratégico',
    custo_disputa: 'Custo de disputa',
    atual_situacao: 'Situação atual',
    instrumento: 'Instrumento',
    meta: 'Meta',
    exemplo_projeto: 'Exemplo / referência',
    frente: 'Frente',
    ranking_poder_de_fato: 'Ranking de poder de fato',
    posicao: 'Posição',
    ator: 'Ator',
    por_que: 'Por quê',
    tese: 'A tese',
    meta_congresso: 'Meta no Congresso',
    meta_governadorias: 'Meta nas governadorias',
    meta_narrativa: 'Meta na narrativa',
    custo_presidencial_vs_congresso: 'Presidência vs. Congresso (custo)',
  };

  // Chaves que não são números e não devem virar cartão na grade.
  var STAT_SKIP = { fonte: true, fontes: true, veredito: true, veredito_openrepublic: true };

  // Formata valor para exibição (string, número, etc.)
  function fmtVal(val) {
    if (val === null || val === undefined) return '<span class="ds-na">—</span>';
    if (typeof val === 'number') return val.toLocaleString('pt-BR');
    if (typeof val === 'boolean') return val ? 'Sim' : 'Não';
    var s = String(val).trim();
    if (s === '') return '<span class="ds-na">—</span>';
    return esc(s);
  }

  // ============================================================
  // RENDERIZADORES DE TIPOS DE DADOS
  // ============================================================

  // Renderiza um sub-objeto (dict de chave→valor) como grade de stats
  function renderStatGrid(obj, maxItems) {
    var entries = Object.entries(obj);
    if (maxItems) entries = entries.slice(0, maxItems);
    var cards = entries
      .filter(function (e) {
        var v = e[1];
        return !(v !== null && typeof v === 'object') && !STAT_SKIP[e[0]];
      })
      .map(function (e) {
        var k = e[0], v = e[1];
        return (
          '<div class="ds-stat">' +
          '<div class="ds-stat-label">' + (STAT_LABELS[k] || humanize(k)) + '</div>' +
          '<div class="ds-stat-val">' + fmtVal(v) + '</div>' +
          '</div>'
        );
      })
      .join('');
    return cards ? '<div class="ds-stat-grid">' + cards + '</div>' : '';
  }

  // Renderiza uma lista de objetos como tabela
  function renderTable(list, maxRows) {
    if (!list || !list.length) return '';
    var rows = list;
    if (maxRows) rows = rows.slice(0, maxRows);
    // Pega as chaves do primeiro item
    var keys = Object.keys(list[0]);

    var head = keys
      .map(function (k) { return '<th>' + (STAT_LABELS[k] || humanize(k)) + '</th>'; })
      .join('');

    var body = rows
      .map(function (item) {
        var tds = keys
          .map(function (k) { return '<td>' + fmtVal(item[k]) + '</td>'; })
          .join('');
        return '<tr>' + tds + '</tr>';
      })
      .join('');

    return (
      '<div class="ds-table-wrap">' +
      '<table class="ds-table"><thead><tr>' + head + '</tr></thead><tbody>' + body + '</tbody></table>' +
      '</div>'
    );
  }

  // Renderiza sub-dicts aninhados como blocos
  function renderSubBlocks(obj) {
    var html = '';
    for (var key in obj) {
      if (!Object.prototype.hasOwnProperty.call(obj, key)) continue;
      var val = obj[key];
      if (val !== null && typeof val === 'object' && !Array.isArray(val)) {
        var subGrid = renderStatGrid(val);
        if (subGrid) {
          html += '<div class="ds-sub-block">' +
            '<h4 class="ds-sub-title">' + (SUB_LABELS[key] || humanize(key)) + '</h4>' +
            subGrid + '</div>';
        }
      }
    }
    return html;
  }

  // Renderiza veredito OpenRepublic em destaque
  function renderVeredito(section) {
    if (!section || typeof section !== 'object') return '';
    var v = section.veredito_openrepublic;
    if (!v && section.resumo) v = section.resumo.veredito_openrepublic || section.resumo.veredito;
    if (!v) return '';
    return '<div class="ds-veredito"><span class="ds-veredito-tag">Veredito</span><p>' + esc(v) + '</p></div>';
  }

  // ============================================================
  // RENDERIZADOR GENÉRICO DE UMA SEÇÃO
  // ============================================================
  function renderSection(key, data) {
    var section = data[key];
    if (!section) return '<p class="ds-empty">Seção "' + esc(key) + '" não encontrada no JSON.</p>';

    var html = '<div class="ds-section" id="ds-' + esc(key) + '">';
    html += '<h3 class="ds-section-title">' + (SECTION_TITLES[key] || humanize(key)) + '</h3>';

    // Metodologia (se existir) — pequena nota
    if (section.metodologia && section.metodologia.fontes) {
      var fontes = section.metodologia.fontes;
      if (Array.isArray(fontes)) fontes = fontes.join(' · ');
      html += '<p class="ds-fontes">Fontes: ' + esc(fontes) + '</p>';
    }

    // Renderiza conforme o tipo
    if (Array.isArray(section)) {
      // Lista simples (ex: compartilhamento_whatsapp já consumido, mas carrosseis)
      html += renderTable(section, 50);
    } else if (typeof section === 'object') {
      // 1. Resumo como stat grid
      if (section.resumo || section.resumiso) {
        var resumo = section.resumo || section.resumiso;
        html += renderStatGrid(resumo);
      }

      // 2. Percorre todas as chaves em ordem
      for (var sk in section) {
        if (!Object.prototype.hasOwnProperty.call(section, sk)) continue;
        if (sk === 'metodologia' || sk === 'resumo' || sk === 'resumiso') continue;

        var sv = section[sk];

        if (Array.isArray(sv)) {
          // Lista → tabela
          if (sv.length && typeof sv[0] === 'object') {
            html += '<h4 class="ds-sub-title">' + (SUB_LABELS[sk] || humanize(sk)) + '</h4>';
            html += renderTable(sv, 15);
          }
        } else if (sv !== null && typeof sv === 'object') {
          // Dict aninhado → sub-bloco
          var hasOnlyScalars = Object.values(sv).every(function (v) {
            return v === null || typeof v !== 'object';
          });
          if (hasOnlyScalars) {
            html += '<div class="ds-sub-block"><h4 class="ds-sub-title">' + (SUB_LABELS[sk] || humanize(sk)) + '</h4>' + renderStatGrid(sv) + '</div>';
          } else {
            html += '<div class="ds-sub-block"><h4 class="ds-sub-title">' + (SUB_LABELS[sk] || humanize(sk)) + '</h4>' + renderSubBlocks(sv);
            // Tabelas dentro de sub-objects
            for (var ssk in sv) {
              if (Array.isArray(sv[ssk]) && sv[ssk].length && typeof sv[ssk][0] === 'object') {
                html += renderTable(sv[ssk], 10);
              }
            }
            html += '</div>';
          }
        }
      }
    }

    // Veredito
    html += renderVeredito(section);

    html += '</div>';
    return html;
  }

  // ============================================================
  // RENDERIZADORES ESPECIAIS
  // ============================================================

  // Mapa de estados — grid de cartões coloridos por status
  function renderMapa(data) {
    var estados = data.mapa_estados;
    if (!estados) return '';
    var html = '<div class="ds-section" id="ds-mapa-estados">';
    html += '<h3 class="ds-section-title">27 estados</h3>';

    var statusOrder = { CRITICO: 0, ALERTA: 1, OK: 2 };
    var ufs = Object.keys(estados).sort(function (a, b) {
      return (statusOrder[estados[a].status] || 9) - (statusOrder[estados[b].status] || 9);
    });

    html += '<div class="ds-mapa-grid">';
    ufs.forEach(function (uf) {
      var e = estados[uf];
      var cls = 'ds-uf-' + (e.status || '').toLowerCase().replace(/[^a-z]/g, '');
      html +=
        '<div class="ds-uf-card ' + cls + '">' +
        '<div class="ds-uf-sigla">' + esc(uf) + '</div>' +
        '<div class="ds-uf-nome">' + esc(e.nome) + '</div>' +
        '<div class="ds-uf-status">' + esc(e.status) + '</div>' +
        '<div class="ds-uf-meta">Pop: ' + e.populacao + 'M · R$ ' + (e.p50 || '?') + '/mês</div>' +
        '<div class="ds-uf-econ">' + esc(e.economia || '') + '</div>' +
        (e.desafio_gov ? '<div class="ds-uf-desc"><strong>Desafio gov:</strong> ' + esc(e.desafio_gov) + '</div>' : '') +
        '</div>';
    });
    html += '</div></div>';
    return html;
  }

  // Dossiês — lista filtrável
  function renderDossie(data) {
    var dp = data.dossie_politicos;
    if (!dp || !dp.politicos) return '';
    var html = '<div class="ds-section" id="ds-dossie-politicos">';
    html += '<h3 class="ds-section-title">Dossiês · ' + dp.politicos.length + ' políticos</h3>';
    if (dp.metadados && dp.metadados.aviso) {
      html += '<p class="ds-fontes">' + esc(dp.metadados.aviso) + '</p>';
    }
    html += '<input type="text" class="ds-dossie-search" placeholder="Filtrar por nome, partido, estado..." id="ds-dossie-filter">';
    html += '<div class="ds-dossie-list" id="ds-dossie-list">';

    dp.politicos.slice(0, 50).forEach(function (p, i) {
      var id = 'ds-doss-' + i;
      html +=
        '<details class="ds-doss-item" data-search="' + esc((p.nome + ' ' + (p.partido_atual || '') + ' ' + (p.estado || '')).toLowerCase()) + '">' +
        '<summary>' +
        '<span class="ds-doss-nome">' + esc(p.nome) + '</span>' +
        '<span class="ds-doss-partido">' + esc(p.partido_atual || '') + '</span>' +
        '<span class="ds-doss-cargo">' + esc(p.cargo_atual || '') + '</span>' +
        '</summary>' +
        '<div class="ds-doss-body">';

      // Bens/patrimônio
      if (p.bens_patrimonio) {
        html += renderSubBlocks({ patrimonio: p.bens_patrimonio });
      }
      // Financiamento
      if (p.financiamento_gastos) {
        html += renderSubBlocks({ financiamento: p.financiamento_gastos });
      }
      // Questões judiciais
      if (p.questoes_judiciais_eticas) {
        html += renderSubBlocks({ juridico: p.questoes_judiciais_eticas });
      }
      // Perfil/trajetória
      if (p.perfil_trajetoria) {
        var pt = p.perfil_trajetoria;
        if (typeof pt === 'object') {
          for (var pk in pt) {
            var pv = pt[pk];
            if (typeof pv === 'string') {
              html += '<p class="ds-doss-text"><strong>' + humanize(pk) + ':</strong> ' + esc(pv) + '</p>';
            }
          }
        }
      }

      html += '</div></details>';
    });

    html += '</div></div>';
    return html;
  }

  // Dados para ação — frases e hashtags
  function renderAcao(data) {
    var d = data.dados_para_acao;
    if (!d) return '';
    var html = '<div class="ds-section" id="ds-dados-para-acao">';

    // Frases para debate
    if (d.frases_para_debate && d.frases_para_debate.length) {
      html += '<h3 class="ds-section-title">Frases para debate</h3>';
      html += '<div class="ds-frases">';
      d.frases_para_debate.forEach(function (f) {
        html +=
          '<div class="ds-frase">' +
          '<div class="ds-frase-tema">' + esc(f.tema) + '</div>' +
          '<blockquote class="ds-frase-txt">"' + esc(f.frase) + '"</blockquote>' +
          '<div class="ds-frase-fonte">' + esc(f.fonte) + '</div>' +
          '</div>';
      });
      html += '</div>';
    }

    // Hashtags
    if (d.hashtags_oficiais) {
      html += '<h3 class="ds-section-title">Hashtags oficiais</h3>';
      html += '<div class="ds-hashtags">';
      for (var cat in d.hashtags_oficiais) {
        var val = d.hashtags_oficiais[cat];
        if (Array.isArray(val)) {
          html += '<div class="ds-hashtag-group"><strong>' + humanize(cat) + ':</strong> ' +
            val.map(function (h) { return '<code>' + esc(h) + '</code>'; }).join(' ') + '</div>';
        }
      }
      html += '</div>';
    }

    // Manchetes
    if (d.manchetes_para_midia && d.manchetes_para_midia.length) {
      html += '<h3 class="ds-section-title">Manchetes para mídia</h3>';
      html += '<ol class="ds-manchetes">';
      d.manchetes_para_midia.forEach(function (m) {
        html += '<li>' + (typeof m === 'string' ? esc(m) : esc(m.titulo || m.manchete || JSON.stringify(m))) + '</li>';
      });
      html += '</ol>';
    }

    // Carrosséis para Instagram (se presente)
    if (data.carrosseis_instagram && data.carrosseis_instagram.length) {
      html += '<h3 class="ds-section-title">Carrosséis para Instagram</h3>';
      html += '<div class="ds-carrosseis">';
      data.carrosseis_instagram.forEach(function (c) {
        html += '<details class="ds-carr-item" style="border-left:4px solid ' + esc(c.cor || '#C00810') + '">';
        html += '<summary><strong>' + esc(c.nome || c.id) + '</strong>';
        if (c.dados_chave) html += ' <span class="ds-carr-keys">' + esc(c.dados_chave) + '</span>';
        html += '</summary><div class="ds-carr-body">';
        if (c.tagline) html += '<p class="ds-carr-tag">' + esc(c.tagline) + '</p>';
        if (c.slides && c.slides.length) {
          html += '<div class="ds-carr-slides">';
          c.slides.forEach(function (s, i) {
            if (s.tipo === 'cover') {
              html += '<div class="ds-slide ds-slide-cover"><span class="ds-slide-n">' + (i + 1) + '</span> Capa</div>';
            } else if (s.tipo === 'cta') {
              html += '<div class="ds-slide ds-slide-cta"><span class="ds-slide-n">' + (i + 1) + '</span> CTA</div>';
            } else {
              html += '<div class="ds-slide"><span class="ds-slide-n">' + (i + 1) + '</span>';
              if (s.pill) html += ' <span class="ds-slide-pill">' + esc(s.pill) + '</span>';
              if (s.titulo) html += ' <strong>' + esc(s.titulo) + '</strong>';
              if (s.stat) html += ' <span class="ds-slide-stat">' + esc(s.stat) + (s.statLabel ? ' (' + esc(s.statLabel) + ')' : '') + '</span>';
              if (s.texto) html += ' <span class="ds-slide-texto">' + esc(s.texto) + '</span>';
              html += '</div>';
            }
          });
          html += '</div>';
        }
        html += '</div></details>';
      });
      html += '</div>';
    }

    html += '</div>';
    return html;
  }

  // ============================================================
  // RENDERIZADOR DE CAPÍTULO
  // ============================================================
  function renderChapter(chap, data) {
    var html =
      '<section class="chapter ds-chapter" id="ds-ch-' + esc(chap.no) + '">' +
      '<div class="container">' +
      '<header class="chapter-head">' +
      '<span class="chapter-no ds-chapter-no">' + esc(chap.no) + '</span>' +
      '<p class="kicker">' + esc(chap.kicker) + '</p>' +
      '<h2>' + esc(chap.title) + '</h2>' +
      '<p class="chapter-lede">' + esc(chap.lede) + '</p>' +
      '</header>' +
      '<div class="ds-root">';

    chap.sections.forEach(function (secKey) {
      if (!data[secKey]) {
        html += '<p class="ds-empty">Seção "' + esc(secKey) + '" não encontrada.</p>';
        return;
      }
      if (chap.special === 'mapa' && secKey === 'mapa_estados') {
        html += renderMapa(data);
      } else if (chap.special === 'rankings' && secKey === 'dossie_politicos') {
        html += renderDossie(data);
      } else if (chap.special === 'acao' && secKey === 'dados_para_acao') {
        html += renderAcao(data);
      } else {
        html += renderSection(secKey, data);
      }
    });

    html += '</div></div></section>';
    return html;
  }

  // ============================================================
  // INIT — insere capítulos no container
  // ============================================================
  function initDataSections(data) {
    var container = document.getElementById('ds-container');
    if (!container) return;

    var html = '';
    CHAPTERS.forEach(function (chap) {
      html += renderChapter(chap, data);
    });
    container.innerHTML = html;

    // Busca de dossiês
    var filter = document.getElementById('ds-dossie-filter');
    if (filter) {
      filter.addEventListener('input', function () {
        var q = this.value.trim().toLowerCase();
        document.querySelectorAll('#ds-dossie-list .ds-doss-item').forEach(function (el) {
          var s = el.getAttribute('data-search') || '';
          el.style.display = q === '' || s.indexOf(q) !== -1 ? '' : 'none';
        });
      });
    }

    console.log('[data-sections] ' + CHAPTERS.length + ' capítulos renderizados a partir do JSON.');
  }

  // Exporta para init do app.js chamar
  window.initDataSections = initDataSections;
})();
