/* ============================================================
   DOSSIÊS — Renderiza os 525 políticos a partir do JSON.
   Substitui 1.1MB de HTML hardcoded por renderização dinâmica.
   Lê de dossie_politicos.politicos em dados_api.json (via app.js).
   ============================================================ */

(function () {
  'use strict';

  function esc(s) {
    if (s === null || s === undefined) return '';
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  // Renderiza um político como doss-card
  function renderCard(p, apoio) {
    var nome = p.nome || '—';
    var cargo = p.cargo_atual || '';
    var partido = p.partido_atual || '';
    var estado = p.estado || '';
    var cardClass = 'doss-card';
    if (apoio && apoio[nome]) cardClass += ' doss-card--apoio';
    var html = '<details class="' + cardClass + '" data-politico="' + esc(nome) + '">';
    html += '<summary>';
    html += '<span class="doss-chev" aria-hidden="true"></span>';
    html += '<span class="doss-main">';
    html += '<span class="doss-name">' + esc(nome) + '</span>';
    if (cargo) html += '<span class="doss-cargo">' + esc(cargo) + '</span>';
    html += '</span>';
    html += '<span class="doss-badges">';
    if (partido) html += '<span class="doss-badge">' + esc(partido) + '</span>';
    if (estado) html += '<span class="doss-badge doss-badge-uf">' + esc(estado) + '</span>';
    html += '</span>';
    html += '</summary>';

    // Corpo — só se houver dados detalhados
    var hasDetail = p.perfil_trajetoria || p.bens_patrimonio || p.financiamento_gastos ||
      p.questoes_judiciais_eticas || p.atuacao_legislativa;

    if (hasDetail) {
      html += '<div class="doss-body">';

      // Perfil e trajetória
      if (p.perfil_trajetoria) {
        var pt = p.perfil_trajetoria;
        html += renderBlocks(pt);
      }

      // Bens / patrimônio
      if (p.bens_patrimonio) {
        html += renderBlocks(p.bens_patrimonio);
      }

      // Financiamento / gastos
      if (p.financiamento_gastos) {
        html += renderBlocks(p.financiamento_gastos);
      }

      // Atuação legislativa
      if (p.atuacao_legislativa) {
        html += renderBlocks(p.atuacao_legislativa);
      }

      // Questões judiciais e ética
      if (p.questoes_judiciais_eticas) {
        html += renderBlocks(p.questoes_judiciais_eticas);
      }

      // Alianças e bases
      if (p.aliancas_bases) {
        html += renderBlocks(p.aliancas_bases);
      }

      // Relevância e imagem pública
      if (p.relevancia_imagem_publica) {
        html += renderBlocks(p.relevancia_imagem_publica);
      }

      html += '</div>';
    }

    html += '</details>';
    return html;
  }

  // Renderiza sub-blocos de um objeto (chave -> string ou lista)
  function renderBlocks(obj) {
    var html = '';
    for (var key in obj) {
      if (!Object.prototype.hasOwnProperty.call(obj, key)) continue;
      var val = obj[key];
      var title = humanize(key);

      if (Array.isArray(val)) {
        // Lista de strings ou objetos — filtra items ND
        var filtered = val.filter(function (item) {
          if (typeof item === 'string') return !isNd(item);
          return true;
        });
        if (filtered.length === 0) continue;
        html += '<div class="doss-block">';
        html += '<h4 class="doss-block-title">' + esc(title) + '</h4>';
        html += '<ul class="doss-list">';
        filtered.forEach(function (item) {
          if (typeof item === 'string') {
            html += '<li>' + esc(item) + '</li>';
          } else if (typeof item === 'object' && item !== null) {
            // Objeto: serializa campos em linha (filtra valores ND)
            var parts = [];
            for (var k in item) {
              if (Object.prototype.hasOwnProperty.call(item, k) && typeof item[k] !== 'object') {
                if (isNd(item[k])) continue;
                parts.push(item[k]);
              }
            }
            if (parts.length) {
              html += '<li>' + parts.map(function (p) { return esc(p); }).join(' — ') + '</li>';
            }
          }
        });
        html += '</ul></div>';
      } else if (typeof val === 'string' && val.trim()) {
        if (isNd(val)) continue;
        html += '<div class="doss-block">';
        html += '<h4 class="doss-block-title">' + esc(title) + '</h4>';
        html += '<p class="doss-text">' + esc(val) + '</p>';
        html += '</div>';
      } else if (typeof val === 'object' && val !== null) {
        // Sub-objeto aninhado
        var subHasContent = false;
        var subHtml = renderBlocks(val);
        if (subHtml) {
          html += '<div class="doss-block">';
          html += '<h4 class="doss-block-title">' + esc(title) + '</h4>';
          html += subHtml;
          html += '</div>';
        }
      }
    }
    return html;
  }

  function humanize(key) {
    return key.replace(/_/g, ' ').replace(/\b\w/g, function (c) { return c.toUpperCase(); });
  }

  // Detecta campos placeholder ("Dados não disponíveis...")
  function isNd(s) {
    if (typeof s !== 'string') return false;
    return s.indexOf('Dados não disponíveis') !== -1;
  }

  // Cruza dossiês com rankings_politicos para identificar candidatos à
  // reeleição com "possibilidade de apoio popular": ficha limpa + sem
  // processos + relevância alta (score >= 3.5 com etiquetas positivas).
  // Retorna um Set de nomes qualificados.
  function buildApoioMap(data) {
    var ranked = {};
    var rk = data.rankings_politicos;
    if (rk) {
      ['aprovados', 'em_analise'].forEach(function (k) {
        (rk[k] || []).forEach(function (r) {
          ranked[r.nome] = r;
        });
      });
    }

    var politicos = data.dossie_politicos && data.dossie_politicos.politicos;
    if (!politicos) return {};

    var apoio = {};
    politicos.forEach(function (p) {
      // 1. Candidato à reeleição?
      //    Dossiês compilados têm "reeleição" em cargos_publicos/cargo_atual.
      //    Dossiês detalhados (texto real) podem não ter a palavra — se estão
      //    no ranking, são candidatos 2026.
      var pt = p.perfil_trajetoria;
      if (!pt || typeof pt !== 'object') return;
      var cps = pt.cargos_publicos || [];
      var cargoAtual = p.cargo_atual || '';
      var isReelec = cps.some(function (cp) {
        return typeof cp === 'string' && cp.toLowerCase().indexOf('reeleição') !== -1;
      });
      if (!isReelec && cargoAtual.toLowerCase().indexOf('reeleição') !== -1) isReelec = true;
      if (!isReelec && ranked[p.nome]) {
        // Detalhado no ranking = candidato 2026 com mandato actual
        var cargoLower = cargoAtual.toLowerCase();
        if (cargoLower.indexOf('deputad') !== -1 || cargoLower.indexOf('senador') !== -1 ||
            cargoLower.indexOf('governador') !== -1) {
          isReelec = true;
        }
      }
      if (!isReelec) return;

      // 2. Ficha limpa?
      var qj = p.questoes_judiciais_eticas;
      if (!qj || typeof qj !== 'object') return;
      var fl = qj.ficha_limpa || '';
      if (typeof fl !== 'string' || fl.indexOf('Sem registros') === -1) return;

      // 3. Sem processos reais (não-ND, não-"não localizado", não-autora)?
      var hasRealProc = false;
      ['processos_tse_tcu', 'inqueritos_denuncias'].forEach(function (k) {
        var arr = qj[k];
        if (!Array.isArray(arr)) return;
        arr.forEach(function (item) {
          if (typeof item !== 'string') return;
          if (isNd(item)) return;
          var lower = item.toLowerCase();
          // "não localizado" = ficha limpa confirmada
          if (lower.indexOf('não localizado') !== -1) return;
          // "autora de ações" = a parlamentar move ações, não é ré
          if (lower.indexOf('autora') !== -1) return;
          hasRealProc = true;
        });
      });
      if (hasRealProc) return;

      // 4. Relevância alta no ranking?
      var r = ranked[p.nome];
      if (!r) return;
      var score = r.score || 0;
      var posEtiquetas = r.etiquetas_positivas || [];
      if (score < 3.5 || posEtiquetas.length === 0) return;

      apoio[p.nome] = true;
    });
    return apoio;
  }

  // Renderiza todos os políticos no grid
  function renderDossies(data) {
    var grid = document.getElementById('dossier-grid');
    if (!grid) return;

    var politicos = data.dossie_politicos && data.dossie_politicos.politicos;
    if (!politicos || !politicos.length) {
      grid.innerHTML = '<p class="caption">Nenhum dossiê disponível.</p>';
      return;
    }

    // Renderiza todos (525)
    var apoio = buildApoioMap(data);
    var html = '';
    politicos.forEach(function (p) {
      html += renderCard(p, apoio);
    });
    grid.innerHTML = html;

    // Atualiza a legenda com a contagem
    var cap = document.getElementById('cap-dossies');
    if (cap) {
      var detalhados = politicos.filter(function (p) {
        return p.perfil_trajetoria &&
          typeof p.perfil_trajetoria.origem === 'string' &&
          p.perfil_trajetoria.origem.indexOf('Dados não disponíveis') === -1;
      }).length;
      var minimal = politicos.length - detalhados;
      cap.innerHTML = '<strong>' + politicos.length + ' dossiês</strong> (' +
        detalhados + ' detalhados + ' + minimal +
        ' em compilação) — Informações podem desatualizar. Verifique sempre a fonte primária antes de qualquer uso.';
    }

    console.log('[dossies] ' + politicos.length + ' políticos renderizados do JSON.');
  }

  // Exporta para app.js chamar na init
  window.renderDossies = renderDossies;
})();
