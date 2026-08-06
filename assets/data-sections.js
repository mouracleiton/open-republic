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
      lede: 'Manifesto, critérios para candidatos, frente comunista unida e propostas executáveis com Gate WO.',
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
      lede: 'Quem passa no corte 4.0, quem está em análise, quem está bloqueado. Dinheiro público, patrimônio e desvios.',
      sections: ['rankings_politicos', 'ranking_dinheiro_publico', 'dados_eleitorais'],
      special: 'rankings',
    },
    {
      no: 'D',
      kicker: 'Vidas em risco',
      title: 'Saúde e educação',
      lede: 'SUS subfinanciado, PISA 377, analfabetismo funcional. Rankings por estado, desigualdade racial, indicadores críticos.',
      sections: ['saude_detalhada', 'educacao_detalhada'],
    },
    {
      no: 'E',
      kicker: 'Direitos e dignidade',
      title: 'Direitos humanos e moradia',
      lede: 'Feminicídio, violência LGBTQIA+, racismo estrutural, déficit habitacional, saneamento e favelas.',
      sections: ['direitos_humanos', 'moradia_cidades'],
    },
    {
      no: 'F',
      kicker: 'Terra, energia e ambiente',
      title: 'Recursos e território',
      lede: 'Concentração fundiária, matriz elétrica, desmatamento, agrotóxicos, pré-sal e povos originários.',
      sections: ['ambiente_detalhado', 'reforma_agraria', 'energia_detalhada', 'povos_originarios'],
    },
    {
      no: 'G',
      kicker: 'Sistema e poder',
      title: 'Justiça, drogas e militarismo',
      lede: 'Morosidade, encarceramento seletivo, redução de danos, gastos militares e polícia que mata.',
      sections: ['sistema_justica', 'drogas_reducao_danos', 'militarismo'],
    },
    {
      no: 'H',
      kicker: 'Dinheiro e poder',
      title: 'Impostos, transporte e comunicação',
      lede: 'Carga tributária regressiva, tarifa de ônibus que rouba o salário, concentração de mídia e exclusão digital.',
      sections: ['tributacao', 'transporte_mobilidade', 'midia_comunicacao'],
    },
    {
      no: 'I',
      kicker: 'Quem manda no Congresso',
      title: 'Bancadas, ciência e cultura',
      lede: 'Bancada ruralista, evangélica e da bala. Ciência cortada. Cultura no osso. Movimentos sociais.',
      sections: ['bancadas_parlamentares', 'ciencia_tecnologia', 'cultura', 'movimentos_sociais'],
    },
    {
      no: 'J',
      kicker: 'Brasil no mundo',
      title: 'Imigrantes e história',
      lede: 'Refugiados venezuelanos, operação acolhida. 524 anos de Brasil em eras: extrativo, escravidão, ditadura.',
      sections: ['imigrantes_refugiados', 'historia_brasil_524_anos'],
    },
    {
      no: 'K',
      kicker: 'Ferramentas de ação',
      title: 'Frases, hashtags e manchetes',
      lede: 'Munição pronta para debate, redes sociais e imprensa. Hashtags oficiais do movimento. Carrosséis para Instagram.',
      sections: ['dados_para_acao', 'carrosseis_instagram'],
      special: 'acao',
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
        return !(v !== null && typeof v === 'object');
      })
      .map(function (e) {
        var k = e[0], v = e[1];
        return (
          '<div class="ds-stat">' +
          '<div class="ds-stat-label">' + humanize(k) + '</div>' +
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
      .map(function (k) { return '<th>' + humanize(k) + '</th>'; })
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
            '<h4 class="ds-sub-title">' + humanize(key) + '</h4>' +
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
    if (!v && section.resumo) v = section.resumo.veredito_openrepublic;
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
            html += '<h4 class="ds-sub-title">' + humanize(sk) + '</h4>';
            html += renderTable(sv, 15);
          }
        } else if (sv !== null && typeof sv === 'object') {
          // Dict aninhado → sub-bloco
          var hasOnlyScalars = Object.values(sv).every(function (v) {
            return v === null || typeof v !== 'object';
          });
          if (hasOnlyScalars) {
            html += '<div class="ds-sub-block"><h4 class="ds-sub-title">' + humanize(sk) + '</h4>' + renderStatGrid(sv) + '</div>';
          } else {
            html += '<div class="ds-sub-block"><h4 class="ds-sub-title">' + humanize(sk) + '</h4>' + renderSubBlocks(sv);
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
