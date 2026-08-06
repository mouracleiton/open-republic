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
  function renderCard(p) {
    var nome = p.nome || '—';
    var cargo = p.cargo_atual || '';
    var partido = p.partido_atual || '';
    var estado = p.estado || '';
    var html = '<details class="doss-card" data-politico="' + esc(nome) + '">';
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
        // Lista de strings ou objetos
        if (val.length === 0) continue;
        html += '<div class="doss-block">';
        html += '<h4 class="doss-block-title">' + esc(title) + '</h4>';
        html += '<ul class="doss-list">';
        val.forEach(function (item) {
          if (typeof item === 'string') {
            html += '<li>' + esc(item) + '</li>';
          } else if (typeof item === 'object' && item !== null) {
            // Objeto: serializa campos em linha
            var parts = [];
            for (var k in item) {
              if (Object.prototype.hasOwnProperty.call(item, k) && typeof item[k] !== 'object') {
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
    var html = '';
    politicos.forEach(function (p) {
      html += renderCard(p);
    });
    grid.innerHTML = html;

    // Atualiza a legenda com a contagem
    var cap = document.getElementById('cap-dossies');
    if (cap) {
      var detalhados = politicos.filter(function (p) {
        return p.perfil_trajetoria || p.bens_patrimonio;
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
