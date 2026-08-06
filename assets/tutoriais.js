/* ============================================================
   TUTORIAIS — Manuais práticos de organização popular
   ------------------------------------------------------------
   4 tutoriais: (1) Como se unir, (2) Como organizar greves,
   (3) Como produzir conteúdo, (4) Como letrar presencialmente.
   Dados embutidos, renderizados dinamicamente no #tut-container.
   ============================================================ */

(function () {
  'use strict';

  var container = document.getElementById('tut-container');
  if (!container) return;

  var TUTORIAIS = [
    {
      id: 'unir',
      icone: '✊',
      titulo: 'Como se unir',
      subtitulo: 'Sindicato, associação, coletivo — organize-se',
      intro: 'Sozinho você é um salário. Organizado, você é uma força. O sistema conta com seu isolamento. A organização é a arma principal da classe trabalhadora.',
      passos: [
        { titulo: 'Converse com seus colegas', desc: 'Comece pequeno. Converse nos intervalos, no WhatsApp do setor, na saída. Identifique as queixas comuns: salário atrasado, condições ruins, sobrecarga. Onde há queixa, há potencial de organização.' },
        { titulo: 'Identifique líderes naturais', desc: 'Em todo grupo há pessoas que os outros respeitam e ouvem. São elas os primeiros contatos. Não precisa ser o mais graduado — muitas vezes é quem trabalha na ponta, que conhece a realidade do chão de fábrica.' },
        { titulo: 'Filie-se ao sindicato da categoria', desc: 'Todo trabalhador tem direito constitucional de se filiar a um sindicato (CF Art. 8º). A filiação é livre e ninguém pode ser demitido por se sindicalizar (CF Art. 8º, VIII — estabilidade sindical). Se o sindicato não representa, mude a diretoria — você pode ser candidato.' },
        { titulo: 'Se não houver sindicato, crie uma associação', desc: 'Se sua categoria ou local de trabalho não tem sindicato, você pode criar uma associação profissional. Reúna pelo menos 15 pessoas, redija um estatuto, eleja uma diretoria e registre em cartório. É gratuito e previsto em lei.' },
        { titulo: 'Articule com outros locais de trabalho', desc: 'Um sindicato por empresa é fraco. A força vem da articulação entre categorias e entre empresas. Participe das reuniões da central sindical (CUT, CTB, Intersindical, etc.) e das federações da sua categoria.' },
        { titulo: 'Mantenha assembleias regulares', desc: 'O sindicato é da base, não da diretoria. Assembleias mensais mantêm o controle nas mãos dos trabalhadores. Decisões importantes (greve, acordo coletivo) SEMPRE devem passar por assembleia.' },
      ],
      leis: [
        { lei: 'CF/88 Art. 8º', desc: 'É livre a associação profissional ou sindical. Ninguém é obrigado a filiar-se ou manter-se filiado.' },
        { lei: 'CF/88 Art. 8º, VIII', desc: 'Estabilidade sindical: empregado sindicalizado não pode ser demitido desde o registro de candidatura até 1 ano após o mandato.' },
        { lei: 'Lei 8.213/1991', desc: 'Previdência social. Filiação sindical não afeta direitos previdenciários.' },
        { lei: 'CLT Art. 543', desc: 'O sindicato é a entidade representativa dos trabalhadores. A filiação não pode ser objeto de qualquer constrangimento.' },
        { lei: 'CLT Art. 545', desc: 'Contribuição sindical é facultativa após a Reforma Trabalhista (Lei 13.467/2017). A filiação e a contribuição associativa são decididas em assembleia.' },
      ],
      dicas: [
        'Comece pelo diálogo informal. Não use documentos ou panfletos no primeiro contato — o medo de retaliação é real.',
        'Documente tudo: reuniões, decisões, assembleias. Se a diretoria do sindicato não cumpre, o registro é sua prova.',
        'O WhatsApp é ferramenta de organização, mas NÃO é seguro. Para decisões sensíveis, use reuniões presenciais. Para mobilização rápida, crie grupos com nomes neutros.',
        'Não espere o sindicato agir. A base organizada empurra a diretoria. Se a diretoria não atende, mude a diretoria.',
      ],
    },
    {
      id: 'greve',
      icone: '🔥',
      titulo: 'Como organizar greves',
      subtitulo: 'O direito de greve na lei brasileira',
      intro: 'A greve é direito constitucional (CF Art. 9º). Mas para ser LEGAL e efetiva, precisa seguir a Lei 7.783/1989. Greve desorganizada pode ser revertida na Justiça e gerar demissões. Greve organizada é a maior arma do trabalhador.',
      passos: [
        { titulo: 'Diagnóstico: por que parar?', desc: 'Antes de parar, defina claramente as pautas: atraso de salário, condições inseguras, descumprimento de acordo coletivo, reajuste. Sem pauta clara, a greve perde apoio e legitimidade.' },
        { titulo: 'Negocie primeiro (obrigatório)', desc: 'A lei EXIGE tentativa de negociação antes da greve (Lei 7.783/89 Art. 3º). Sem isso, a greve é considerada abusiva. Documente: reuniões, propostas, respostas do empregador.' },
        { titulo: 'Convoque a assembleia', desc: 'A decisão de greve deve ser aprovada em assembleia da categoria (Lei 7.783/89 Art. 4º). A assembleia define: pauta, data de início, duração prevista, serviços mínimos. Lavre ATA com todos os detalhes.' },
        { titulo: 'Aviso prévio de 48 horas', desc: 'Avise o empregador com MÍNIMO de 48 horas de antecedência (Lei 7.783/89 Art. 3º). Em serviços essenciais, são 72 horas (Art. 13). O aviso deve ser por escrito e arquivado.' },
        { titulo: 'Defina serviços mínimos', desc: 'A lei exige manutenção das "necessidades inadiáveis da comunidade" (Art. 3º, parágrafo único). Em serviços essenciais (saúde, energia, água, transporte coletivo), o atendimento mínimo é obrigatório. Acordo sobre mínimos deve ser firmado — evita dissídios.' },
        { titulo: 'Mantenha a greve pacífica', desc: 'A lei define greve legítima como "suspensão coletiva, temporária e PACÍFICA" (Art. 2º). Violência, depredação e intimidação de não-grevistas são ABUSOS (Art. 6º, §1º) e transformam a greve em ilícito. O piquete deve ser INFORMATIVO, não coativo.' },
        { titulo: 'Durante a greve: comunicação e caixa', desc: 'Mantenha informação constante aos grevistas e à população. Crie uma comissão de comunicação. Monte um caixa de solidariedade (cota dos grevistas) para apoiar quem não tem reserva. A greve é sustentada pela solidariedade.' },
        { titulo: 'Negocie o fim da greve', desc: 'A greve termina com acordo coletivo ou decisão em assembleia. Não aceite voltar sem conquistas concretas. Documente tudo o que foi acordado — é base para fiscalizar o cumprimento.' },
      ],
      leis: [
        { lei: 'CF/88 Art. 9º', desc: 'Cabe aos trabalhadores decidir sobre a oportunidade de exercer o direito de greve, competindo aos mesmos, nos termos da lei, definir os serviços ou atividades essenciais.' },
        { lei: 'Lei 7.783/1989 Art. 2º', desc: 'Para os fins desta Lei, considera-se legítimo exercício do direito de greve a suspensão coletiva, temporária e pacífica, total ou parcial, de prestação pessoal de serviços a empregador.' },
        { lei: 'Lei 7.783/1989 Art. 3º', desc: 'Os trabalhadores deverão participar de tentativa de negociação e comunicarão a decisão de greve aos empregadores com antecedência mínima de 48 (quarenta e oito) horas.' },
        { lei: 'Lei 7.783/1989 Art. 11', desc: 'Nos serviços ou atividades essenciais, os sindicatos deverão comunicar a greve aos empregadores e aos usuários com 72 horas de antecedência.' },
        { lei: 'Lei 7.783/1989 Art. 14', desc: 'Constitui abuso do direito de greve a inobservância das normas contidas na presente Lei, bem como a manutenção da paralisação após acordo ou decisão da Justiça do Trabalho.' },
        { lei: 'Lei 7.783/1989 Art. 10', desc: 'São serviços essenciais: tratamento e abastecimento de água, produção e distribuição de energia elétrica, gás e combustíveis, assistência médica e hospitalar, distribuição de medicamentos, coleta e tratamento de esgoto e lixo, telecomunicações, transporte coletivo, captação e tratamento de água, guarda de valores, transporte ferroviário e marítimo, tráfego aéreo, compensação bancária.' },
        { lei: 'CLT Art. 652', desc: 'As atribuições dos sindicatos incluem a representação dos trabalhadores em negociações coletivas e a defesa de direitos.' },
      ],
      dicas: [
        'NUNCA greve sem assembleia. A assembleia é sua base legal. Sem ela, a empresa pode pedir a reintegração na Justiça.',
        'Piquete é INFORMATIVO: cartazes, faixas, panfletos explicando a pauta. Piquete que IMPEDE entrada é considerado abuso e pode gerar demissão por justa causa.',
        'O empregador pode contrar o Dissídio Coletivo (Dissídio de Greve) na Justiça do Trabalho. Se o juiz decidir que há abuso, os grevistas podem perder os dias parados e, em casos extremos, serem demitidos.',
        'Servidores públicos: a Lei 7.783/89 NÃO se aplica integralmente. O STF entende que greve do servidor público exige lei específica (ainda pendente). Mas o direito existe (CF Art. 37, VII) e greves de servidores são comuns e têm sido reconhecidas.',
        'A greve não quebra o contrato de trabalho (Lei 7.783/89 Art. 7º). A empresa pode descontar os dias parados, mas NÃO pode demitir pelo exercício do direito de greve.',
        'Documente TODAS as assembleias em ATA: data, horário, local, número de presentes, pauta, votação (resultado numérico). A ATA é seu documento legal.',
      ],
    },
    {
      id: 'conteudo',
      icone: '📱',
      titulo: 'Como produzir conteúdo',
      subtitulo: 'Para WhatsApp, Instagram, TikTok e X',
      intro: 'Conteúdo é munição. Mas conteúdo bom é conteúdo VERDADEIRO, com FONTE, que toca quem lê. A direita tem dinheiro e mídia. A esquerda tem a verdade e o povo. O conteúdo é o que conecta os dois.',
      passos: [
        { titulo: '1. Comece pelo FATO, não pela opinião', desc: 'Todo post precisa de um número, uma data, um fato verificável. "33 milhões passam fome" (VIGISAN). "45.747 homicídios em 2023" (FBSP). O dado é a âncora. A opinião vem depois.' },
        { titulo: '2. Um número = um post', desc: 'Não jogue vários dados de uma vez. Escolha UM número de impacto. Escreva a manchete. Adicione o contexto. Adicione a fonte. Pronto. Simplicidade vence complexidade.' },
        { titulo: '3. Manchete que PARA o scroll', desc: 'Os primeiros 3 segundos decidem. A manchete deve ser curta, direta e provocativa. "Você sabia que 33 milhões passam fome?" funciona. "Análise sobre a insegurança alimentar no Brasil" não funciona.' },
        { titulo: '4. Formato por plataforma', desc: 'WhatsApp: texto curto + imagem (carrossel). Instagram: carrossel visual (até 10 slides). TikTok: vídeo vertical 9:16, 15-60s, com legenda grande. X (Twitter): texto + imagem ou thread. Cada plataforma tem sua linguagem.' },
        { titulo: '5. Identidade visual', desc: 'Use cores da marca (vermelho, preto, amarelo). Fonte grande e legível. Contraste alto. Logo da organização. O conteúdo precisa ser RECONHECÍVEL no feed. Não precisa ser profissional — precisa ser consistente.' },
        { titulo: '6. Legenda = acessibilidade', desc: 'SEMPRE legende vídeos. 80% dos vídeos no celular são assistidos sem som. Sem legenda, você perde 80% do alcance. Ferramenta gratuita: CapCut (legendas automáticas) ou a própria ferramenta do TikTok/Reels.' },
        { titulo: '7. CTA — Chamada para ação', desc: 'Todo post precisa terminar com uma ação. "Compartilhe", " marque quem precisa ver isso", "venha para a rua dia X", "filie-se ao sindicato". Sem CTA, o conteúdo é informação morta. Com CTA, é organização.' },
        { titulo: '8. Calendário e constância', desc: 'Poste regularmente. Um post por dia é melhor que cinco no mesmo dia. O algoritmo premia constância. Use a ferramenta de agendamento do Meta Business Suite (gratuito) para Instagram e Facebook.' },
        { titulo: '9. Hash tags estratégicas', desc: 'Use 3-5 hashtags por post. Misture amplas (#Brasil, #política) com específicas (#ReformaAgraria, #DireitosTrabalhistas). Não use 30 hashtags — o algoritmo pune.' },
        { titulo: '10. Mensure e adapte', desc: 'Olhe as métricas: quais posts tiveram mais alcance? Mais compartilhamentos? Mais comentários? Repita o que funciona. Pare de fazer o que não funciona. O algoritmo é seu professor.' },
      ],
      ferramentas: [
        { nome: 'Canva (gratuito)', para: 'Carrosséis, gráficos, imagens', link: 'Editor visual online. Templates prontos. Aprendizado: 30 min.' },
        { nome: 'CapCut (gratuito)', para: 'Edição de vídeo, legendas automáticas', link: 'Editor de vídeo para celular. Legendas automáticas em português.' },
        { nome: 'Meta Business Suite', para: 'Agendamento Instagram/Facebook', link: 'Agende posts para a semana. Analíticos incluídos.' },
        { nome: 'InShot (gratuito)', para: 'Edição rápida de vídeo no celular', link: 'Corte, legenda, música. Simples e rápido.' },
        { nome: 'Remove.bg (gratuito)', para: 'Remover fundo de imagens', link: 'Tira o fundo de fotos em 1 clique. Útil para criar avatares.' },
        { nome: 'Google Drive / OneDrive', para: 'Armazenar e compartilhar materiais', link: 'Banco de imagens, logos, templates para a equipe usar.' },
      ],
      dicas: [
        'FONTE SEMPRE. Sem fonte, é boato. Com fonte, é dado. Dado convence. Boato descredibiliza.',
        'Não complique. Um número, uma manchete, uma fonte. Isso é um post.',
        'Em vídeo, fale para a CÂMERA como se falasse para um amigo. Naturalidade vence roteiro rígido.',
        'Use oTikTok e Reels mesmo que pareça bobo. É onde a juventude operária está. Se você não chegar lá, a direita chega.',
        'Crie uma "biblioteca de conteúdo": pastas organizadas com imagens, números, fontes, logos. Reduz o tempo de produção de 2h para 15min por post.',
        'O melhor conteúdo é o que faz a pessoa PARAR, LER, SENTIR e COMPARTILHAR. Em 3 segundos.',
      ],
    },
    {
      id: 'letrar',
      icone: '📚',
      titulo: 'Como letrar presencialmente',
      subtitulo: 'Formação política de porta em porta',
      intro: 'O digital organiza quem já está convencido. O presencial convence quem ainda não está. Nenhum post substitui a conversa de olho no olho. O letramento político presencial é lento, mas é o único que muda voto e muda vida.',
      passos: [
        { titulo: '1. Estude ANTES de ir para a rua', desc: 'Você não pode ensinar o que não sabe. Antes de qualquer atividade presencial, estude os dados-chave: renda mediana, taxa de homicídios, gasto com saúde vs juros, PISA. Tenha 5-10 números na ponta da língua. O site é sua fonte.' },
        { titulo: '2. Conheça o território', desc: 'Antes de chegar, saiba: quem é o vereador, qual o IDH do bairro, quais os problemas locais. Falar de "reforma agrária" num bairro urbano pode não conectar. Falar de tarifa de ônibus, aluguel, saúde do posto — conecta.' },
        { titulo: '3. A abordagem: escute primeiro', desc: 'Não chegue falando. Pergunte: "Como está sendo para você o custo de vida?", "O que mais te preocupa hoje?". ESCUTE. A pessoa vai dar a você a chave de como conectar a pauta política com a vida dela.' },
        { titulo: '4. Conecte o local com o nacional', desc: 'Se a pessoa fala do posto de saúde lotado, conecte: "Sabe por que está lotado? Saúde recebe só 4% do PIB. A OCDE gasta 8%. O governo escolhe onde botar o dinheiro. Isso é política." O dado local abre a porta para a análise estrutural.' },
        { titulo: '5. Use materiais físicos', desc: 'Leve panfletos, cartões, zines. O panfleto continua após a conversa. Um cartão com 3 números-chave + QR code para o site é mais efetivo que 10 minutos de palestra. O material físico é a extensão da conversa.' },
        { titulo: '6. Convide para a próxima ação', desc: 'Toda conversa precisa terminar com um convite: "Tem reunião do sindicato quinta", "Tem ato no dia 20", "Entra no grupo de WhatsApp". Sem convite, a conversa morre. Com convite, ela vira organização.' },
        { titulo: '7. Anote contatos', desc: 'Pegue nome, telefone, bairro. Sem isso, a conversa se perde. Crie uma planilha simples. Dê retorno em 48h. O retorno demonstra seriedade e constrói confiança.' },
        { titulo: '8. Faça círculos de estudo', desc: 'O passo seguinte à abordagem é o estudo coletivo. Reúna 5-10 pessoas para estudar textos curtos: Manifesto Comunista (resumo), artigos de jornal, dados do site. Encontro semanal de 1h. É a semente do coletivo.' },
        { titulo: '9. Forme multiplicadores', desc: 'O objetivo não é você chegar a mil pessoas. É formar 10 pessoas que cheguem a 100 cada. Ensine o que você faz. Repasse os materiais. A formação política se multiplica.' },
        { titulo: '10. Avalie e ajuste', desc: 'Após cada atividade, avalie: o que funcionou? Quais números geraram mais reação? Qual abordagem abriu mais portas? Anote e melhore. A prática sem teoria é cega; a teoria sem prática é vazia.' },
      ],
      materiais: [
        { nome: 'Cartão de bolso (9x5cm)', desc: 'Frente: 5 números-chave do estado/município. Verso: QR code para o site + contatos do coletivo/sindicato. Impressão: gráfica rápida, ~R$ 50 o milheiro.' },
        { nome: 'Panfleto A6 (1/4 de A4)', desc: 'Uma pauta por folha. Ex: "Por que a tarifa come seu salário?". Texto curto, número grande, fonte, CTA. Distribuir em portas de estação, feiras, portas de fábrica.' },
        { nome: 'Zine (8 páginas A5)', desc: 'Dobradiura de uma folha A4 em 8 páginas. Tema único (ex: "O que é mais-valia?"). Texto simples, desenhos. A zine é leitura para levar e guardar.' },
        { nome: 'Banner de rua (2x1m)', desc: 'Para atos e ocupações. Uma manchete, um número, uma hashtag. Contraste alto. Ler a 10 metros de distância.' },
        { nome: 'Crachá / adesivo', desc: 'Identifica o militante na atividade. Adesivo com logo/slogan é propaganda portátil — a pessoa cola em caderno, geladeira, capacete.' },
      ],
      dicas: [
        'Não desanime com a rejeição. A cada 10 abordagens, 7 dizem "não tenho tempo". 2 param e ouvem. 1 se engaja. Essa 1 pessoa vale o esforço.',
        'A melhor hora para abordar: início da manhã (transporte), horário de almoço (porta de empresa), fim de tarde (retorno para casa). Evite horários de pressa.',
        'Vá em dupla ou trio. Um conversa, o outro distribui material. Mais seguro, mais efetivo, menos intimidador.',
        'Vista-se como o público. Terno em favela aliena. Camiseta de movimento em condomínio de elite também. Adapte o visual ao território.',
        'O objetivo NÃO é converter na primeira conversa. É plantar uma semente, deixar um material, agendar um retorno. Conversão é processo, não evento.',
        'Registre tudo em relatório simples: data, local, abordagens feitas, contatos coletados, reações. Dados melhoram a estratégia.',
      ],
    },
  ];

  function esc(s) {
    if (s === null || s === undefined) return '';
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function render() {
    var html = '';
    TUTORIAIS.forEach(function (t, idx) {
      var num = idx + 1;
      html += '<details class="tut-item" id="tut-' + esc(t.id) + '">';
      html += '<summary class="tut-summary">';
      html += '<span class="tut-icone" aria-hidden="true">' + t.icone + '</span>';
      html += '<span class="tut-titulo-wrap">';
      html += '<span class="tut-num">Manual ' + num + '</span>';
      html += '<span class="tut-titulo">' + esc(t.titulo) + '</span>';
      html += '<span class="tut-sub">' + esc(t.subtitulo) + '</span>';
      html += '</span>';
      html += '<span class="tut-chevron" aria-hidden="true">+</span>';
      html += '</summary>';

      html += '<div class="tut-body">';

      // Intro
      html += '<p class="tut-intro">' + esc(t.intro) + '</p>';

      // Passos
      if (t.passos && t.passos.length) {
        html += '<h4 class="tut-section-title">Passo a passo</h4>';
        html += '<ol class="tut-passos">';
        t.passos.forEach(function (p) {
          html += '<li class="tut-passo">';
          html += '<strong class="tut-passo-titulo">' + esc(p.titulo) + '</strong>';
          html += '<span class="tut-passo-desc">' + esc(p.desc) + '</span>';
          html += '</li>';
        });
        html += '</ol>';
      }

      // Leis (se houver)
      if (t.leis && t.leis.length) {
        html += '<h4 class="tut-section-title">Base legal</h4>';
        html += '<div class="tut-leis">';
        t.leis.forEach(function (l) {
          html += '<div class="tut-lei">';
          html += '<code class="tut-lei-ref">' + esc(l.lei) + '</code>';
          html += '<p class="tut-lei-desc">' + esc(l.desc) + '</p>';
          html += '</div>';
        });
        html += '</div>';
      }

      // Ferramentas (se houver)
      if (t.ferramentas && t.ferramentas.length) {
        html += '<h4 class="tut-section-title">Ferramentas gratuitas</h4>';
        html += '<div class="tut-ferramentas">';
        t.ferramentas.forEach(function (f) {
          html += '<div class="tut-ferr">';
          html += '<strong>' + esc(f.nome) + '</strong>';
          html += '<span class="tut-ferr-para">' + esc(f.para) + '</span>';
          html += '<p class="tut-ferr-link">' + esc(f.link) + '</p>';
          html += '</div>';
        });
        html += '</div>';
      }

      // Materiais (se houver)
      if (t.materiais && t.materiais.length) {
        html += '<h4 class="tut-section-title">Materiais para imprimir</h4>';
        html += '<div class="tut-materiais">';
        t.materiais.forEach(function (m) {
          html += '<div class="tut-mat">';
          html += '<strong>' + esc(m.nome) + '</strong>';
          html += '<p>' + esc(m.desc) + '</p>';
          html += '</div>';
        });
        html += '</div>';
      }

      // Dicas
      if (t.dicas && t.dicas.length) {
        html += '<h4 class="tut-section-title">Dicas de quem já errou</h4>';
        html += '<ul class="tut-dicas">';
        t.dicas.forEach(function (d) {
          html += '<li>' + esc(d) + '</li>';
        });
        html += '</ul>';
      }

      html += '</div>'; // tut-body
      html += '</details>';
    });
    container.innerHTML = html;
    console.log('[tutoriais] ' + TUTORIAIS.length + ' tutoriais renderizados.');
  }

  render();
})();
