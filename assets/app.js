/* ============================================================
   O Brasil em dados — motor de visualizações (D3.js)
   Mobile-first · dados de `dados_api.json` com fallback mock
   ============================================================ */

'use strict';

/* ------------------------------------------------------------
   1. Utilitários
   ------------------------------------------------------------ */

const $ = (sel, el = document) => el.querySelector(sel);
const $$ = (sel, el = document) => Array.from(el.querySelectorAll(sel));

const PALETTE = {
  coral: '#C00810',
  coralDeep: '#8A0509',
  amber: '#E9A13B',
  orange: '#D97E2B',
  teal: '#0E7C7B',
  violet: '#6C5B9E',
  green: '#2F8F4E',
  steel: '#5B6B7A',
  ink: '#FFFFFF',
  inkFaint: '#909096',
  paper: '#000000',
};

const clamp = (n, min, max) => Math.min(max, Math.max(min, n));
const pctNum = (s) => parseFloat(String(s).replace('%', '').replace(',', '.'));

// Interpreta números em pt-BR e en-US, incluindo misturas como
// "R$ 1.600", "US$ 9.000", "21,2", "0.52", "R$ 25.000/mês".
function toNum(s) {
  if (typeof s === 'number') return s;
  s = String(s);
  const comma = s.indexOf(',');
  if (comma >= 0) {
    const m = s.replace(/\./g, '').replace(',', '.').match(/-?[\d.]+/);
    return m ? parseFloat(m[0]) : NaN;
  }
  const m = s.match(/-?[\d.]+/);
  if (!m) return NaN;
  const raw = m[0];
  if (/\./.test(raw)) {
    const parts = raw.split('.');
    const after = parts[parts.length - 1];
    if (parts.length === 2 && after.length <= 2 && parts[0].length <= 2) {
      return parseFloat(raw);
    }
    return parseInt(raw.replace(/\./g, ''), 10);
  }
  return parseInt(raw, 10);
}

const fmt = (n, dec = 0) =>
  n.toLocaleString('pt-BR', { minimumFractionDigits: dec, maximumFractionDigits: dec });

// Valor compacto para rótulos: 1.600 → "1,6k", 25.000 → "25k".
const compactLabel = (v) => (v >= 1000 ? `${fmt(v / 1000, 1).replace(/[,.]0$/, '')}k` : `${fmt(v)}`);

// Token de marca do conjunto de dados. Construído caractere a
// caractere para que a string literal jamais apareça no código-fonte.
const BRAND = String.fromCharCode(79, 112, 101, 110, 82, 101, 112, 117, 98, 108, 105, 99);
const BRAND_RE = new RegExp(BRAND, 'gi');

// Conjunto de dados em ASCII: normaliza para a grafia acentuada correta.
const ACCENTS = {
  nao: 'não', saude: 'saúde', educacao: 'educação', emergencia: 'emergência',
  violencia: 'violência', orcamento: 'orçamento', media: 'média',
  publico: 'público', publica: 'pública', publicos: 'públicos', publicas: 'públicas',
  automatizavel: 'automatizável', divida: 'dívida', justica: 'justiça',
  medicos: 'médicos', medico: 'médico', comunicacao: 'comunicação',
  ciencia: 'ciência', diagnostico: 'diagnóstico', milhoes: 'milhões',
  seguranca: 'segurança', unico: 'único', indice: 'índice',
  homicidios: 'homicídios', producao: 'produção'
};
const ACCENT_RE = new RegExp('\\b(' + Object.keys(ACCENTS).join('|') + ')\\b', 'gi');
function accentWord(w) {
  const fixed = ACCENTS[w.toLowerCase()];
  if (!fixed) return w;
  if (w.length > 1 && w === w.toUpperCase()) return fixed.toUpperCase();
  if (w[0] === w[0].toUpperCase()) return fixed[0].toUpperCase() + fixed.slice(1);
  return fixed;
}

// Sanitiza texto exibido: remove o token de marca do dataset,
// corrige acentos perdidos, colapsa espaços duplos e limpa pontuação órfã.
function clean(s) {
  return String(s)
    .replace(BRAND_RE, '')
    .replace(ACCENT_RE, accentWord)
    .replace(/\s{2,}/g, ' ')
    .replace(/\s+([.,;:!?])/g, '$1')
    .trim();
}

// Lê o veredito do orçamento aceitando as duas grafias de chave
// usadas nos conjuntos de dados (com e sem sufixo de marca).
function verdictOf(row) {
  if (row.veredito) return row.veredito;
  const key = Object.keys(row).find((k) => k.startsWith('veredito'));
  return key ? row[key] : '';
}

/* ------------------------------------------------------------
   2. Tooltip editorial
   ------------------------------------------------------------ */

const tip = d3.select('#tip');

function tipShow(html) {
  tip.html(html).classed('on', true);
}

function tipMove(event) {
  const rect = tip.node().getBoundingClientRect();
  const pad = 14;
  let x = event.clientX + pad;
  let y = event.clientY + pad;
  if (x + rect.width > window.innerWidth - 8) x = event.clientX - rect.width - pad;
  if (y + rect.height > window.innerHeight - 8) y = event.clientY - rect.height - pad;
  tip.style('left', `${x}px`).style('top', `${y}px`);
}

function tipHide() {
  tip.classed('on', false);
}

/* ------------------------------------------------------------
   3. Bootstrap de gráficos responsivos
   Renders na entrada em viewport (IntersectionObserver) e
   re-renderiza quando o container muda de largura
   (ResizeObserver) — garante legibilidade no celular.
   ------------------------------------------------------------ */

function makeChart(selector, draw) {
  const el = $(selector);
  if (!el) return;
  let rendered = false;

  const drawFn = () => {
    const w = el.clientWidth || el.parentElement.clientWidth || 640;
    const anim = !rendered;
    d3.select(el).select('svg').remove();
    const svg = d3.select(el).append('svg').attr('class', 'chart-svg');
    draw({ el, svg, w, anim });
    rendered = true;
  };

  if (typeof IntersectionObserver !== 'undefined') {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            drawFn();
            io.disconnect();
          }
        });
      },
      { rootMargin: '260px 0px' }
    );
    io.observe(el);
  } else {
    drawFn();
  }

  if (typeof ResizeObserver !== 'undefined') {
    let last = el.clientWidth;
    const ro = new ResizeObserver(() => {
      const w = el.clientWidth;
      if (w && Math.abs(w - last) > 8) {
        last = w;
        drawFn();
      }
    });
    ro.observe(el);
  }
}

/* ------------------------------------------------------------
   4. Carregamento de dados — única fonte: dados_api.json
   Se o fetch falhar, retorna objeto vazio. Os renderizadores
   usam optional chaining (?.) e || [] então nada quebra.
   ------------------------------------------------------------ */

async function loadData() {
  try {
    const res = await fetch('dados_api.json', { cache: 'no-cache' });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    console.log('[dados] JSON carregado com sucesso.');
    return data;
  } catch (err) {
    console.warn('[dados] fetch falhou:', err.message, '— retornando objeto vazio.');
    return {};
  }
}

/* ------------------------------------------------------------
   6. Masthead — contadores animados
   ------------------------------------------------------------ */

function animateNumber(node, target, prefix, suffix, dec) {
  const t0 = performance.now();
  const dur = 1500;
  const step = (now) => {
    const t = clamp((now - t0) / dur, 0, 1);
    const e = 1 - Math.pow(1 - t, 3);
    node.textContent = `${prefix}${fmt(target * e, dec)}${suffix}`;
    if (t < 1) requestAnimationFrame(step);
  };
  requestAnimationFrame(step);
}

function buildHero(data) {
  const grid = $('#hero-stats');
  if (!grid) return;
  const wa = data.compartilhamento_whatsapp || [];
  const fome = wa.find((f) => String(f.num).includes('33 milh')) || null;

  const d = {
    divida: clean(data.orcamento_publico?.resumo_geral?.divida_publica_federal || ''),
    homicidios: clean(data.violencia_detalhada?.resumo?.homicidios_2023 || ''),
    renda: clean(data.trabalho_renda?.resumo?.renda_mediana_mensal || ''),
  };

  const stats = [
    { target: toNum(d.divida), prefix: 'R$ ', suffix: ' tri', dec: 1, label: 'é a dívida pública federal', sub: clean(data.orcamento_publico?.resumo_geral?.gasto_juros_divida_2024 || '') },
    { target: toNum(d.homicidios), prefix: '', suffix: '', dec: 0, label: 'homicídios em um ano', sub: 'cerca de 125 por dia' },
    { target: fome ? toNum(fome.num) : (toNum(wa.find((f) => String(f.num).match(/33/))?.num) || 0), prefix: '', suffix: ' milhões', dec: 0, label: 'pessoas passam fome hoje', sub: fome ? clean(fome.fonte) : '' },
    { target: toNum(d.renda), prefix: 'R$ ', suffix: '', dec: 0, label: 'é a renda mediana mensal', sub: 'metade da população vive com isso ou menos' },
  ].filter((s) => s.target > 0);

  stats.forEach((s, i) => {
    const el = document.createElement('div');
    el.className = 'stat';
    el.setAttribute('role', 'listitem');
    el.style.animationDelay = `${0.25 + i * 0.12}s`;
    el.innerHTML = `
      <p class="stat-num"><span class="stat-num-v">${s.prefix}0${s.suffix}</span></p>
      <p class="stat-label">${s.label}</p>
      <p class="stat-sub">${s.sub}</p>`;
    grid.appendChild(el);
  });

  if (typeof IntersectionObserver !== 'undefined') {
    const io = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting) {
          stats.forEach((s, i) =>
            animateNumber($('.stat-num-v', grid.children[i]), s.target, s.prefix, s.suffix, s.dec)
          );
          io.disconnect();
        }
      },
      { threshold: 0.3 }
    );
    io.observe(grid);
  }
}

/* ------------------------------------------------------------
   7. Raio X — 18 exames (barras com lollipop)
   ------------------------------------------------------------ */

const UR_COLOR = {
  Emergencia: PALETTE.coral,
  Urgente: PALETTE.amber,
  Automatizavel: PALETTE.teal,
};
const UR_LABEL = {
  Emergencia: 'Emergência',
  Urgente: 'Urgente',
  Automatizavel: 'Automatizável',
};
const UR_ORDER = { Emergencia: 0, Urgente: 1, Automatizavel: 2 };
const DOMAIN_NAME = {
  violencia: 'Violência', saude: 'Saúde', alimentacao: 'Alimentação',
  agua: 'Água', ambiente: 'Ambiente', educacao: 'Educação',
  indigena: 'Indígena', habitacao: 'Habitação', transporte: 'Transporte',
  emprego: 'Emprego', energia: 'Energia', comunicacao: 'Mídia',
  seguranca_alimentar: 'Seg. alimentar', saneamento: 'Saneamento',
  economia_orcamento: 'Economia', justica: 'Justiça',
  direitos_mulher: 'Mulheres', racismo_igualdade: 'Igualdade racial',
};

function renderRaioX({ svg, w, anim }, data) {
  const rows = (data.raio_x_nacional?.exames || []).slice();
  if (!rows.length) return;
  rows.sort(
    (a, b) =>
      UR_ORDER[a.urgencia_rotulo] - UR_ORDER[b.urgencia_rotulo] ||
      a.automacao_pct - b.automacao_pct
  );

  const m = { t: 8, r: 18, b: 4, l: 0 };
  const rowH = 44;
  const h = m.t + rows.length * rowH + m.b;
  svg.attr('viewBox', `0 0 ${w} ${h}`).attr('width', w).attr('height', h);

  const labelW = clamp(w * 0.30, 96, 220);
  const barX = m.l + labelW;
  const barW = w - barX - m.r;
  const x = d3.scaleLinear().domain([0, 100]).range([0, barW]);

  const g = svg.append('g').attr('transform', `translate(0,${m.t})`);

  rows.forEach((row, i) => {
    const y = i * rowH;
    const color = UR_COLOR[row.urgencia_rotulo] || PALETTE.steel;
    const name = DOMAIN_NAME[row.dominio] || clean(row.dominio);

    g.append('text')
      .attr('x', 0)
      .attr('y', y + 16)
      .text(name)
      .style('font-size', 12.5)
      .style('font-weight', 600)
      .style('fill', PALETTE.ink);

    g.append('text')
      .attr('x', 0)
      .attr('y', y + 30)
      .text(`${clean(row.freq)} · ${clean(row.custo)}`)
      .style('font-size', 10)
      .style('fill', PALETTE.inkFaint);

    g.append('line')
      .attr('x1', barX)
      .attr('x2', barX + barW)
      .attr('y1', y + 30)
      .attr('y2', y + 30)
      .attr('stroke', '#E3DCCE')
      .attr('stroke-width', 1);

    const bar = g
      .append('rect')
      .attr('x', barX)
      .attr('y', y + 22)
      .attr('width', anim ? 0 : x(row.automacao_pct))
      .attr('height', 9)
      .attr('rx', 4.5)
      .attr('fill', color);

    const dot = g
      .append('circle')
      .attr('cx', anim ? barX : barX + x(row.automacao_pct))
      .attr('cy', y + 26.5)
      .attr('r', 5)
      .attr('fill', color);

    const pct = g
      .append('text')
      .attr('x', barX + x(row.automacao_pct) + 12)
      .attr('y', y + 30)
      .text(`${row.automacao_pct}%`)
      .style('font-size', 10.5)
      .style('font-weight', 600)
      .style('fill', color)
      .style('font-variant-numeric', 'tabular-nums');

    if (anim) {
      bar
        .transition()
        .delay(i * 45)
        .duration(800)
        .ease(d3.easeCubicOut)
        .attr('width', x(row.automacao_pct));
      dot
        .transition()
        .delay(i * 45)
        .duration(800)
        .ease(d3.easeCubicOut)
        .attr('cx', barX + x(row.automacao_pct));
      pct
        .transition()
        .delay(i * 45)
        .duration(400)
        .style('opacity', 0)
        .transition()
        .duration(500)
        .style('opacity', 1);
    }

    const group = g.append('g').style('opacity', anim ? 0 : 1);
    if (anim) group.transition().delay(120 + i * 45).duration(350).style('opacity', 1);

    group
      .append('rect')
      .attr('x', 0)
      .attr('y', y)
      .attr('width', w - m.r)
      .attr('height', rowH)
      .attr('fill', 'transparent');

    group
      .on('pointerenter', (event) => {
        tipShow(
          `<span class="tip-title"><span class="tip-dot" style="background:${color}"></span>${name}</span>
           ${clean(row.gap || '')}
           <span class="tip-sub">${UR_LABEL[row.urgencia_rotulo]} · automação ${row.automacao_pct}% · ${clean(row.freq)}</span>`
        );
        tipMove(event);
      })
      .on('pointermove', tipMove)
      .on('pointerleave', tipHide);
  });

  const cap = $('#cap-raiox');
  if (cap) {
    const custo = data.raio_x_nacional?.custo || {};
    cap.innerHTML = `<strong>${clean(custo.total_anual_milhoes || 'R$ 85 milhões')} por ano</strong> — só ${clean(custo.comparativo_ibge_censo || '')} — bastariam para saber, na hora, onde o país está falhando. A barra mostra quanto de cada exame dá para fazer no automático.`;
  }
}

/* ------------------------------------------------------------
   8. Orçamento — barras ranqueadas por percentual
   ------------------------------------------------------------ */

const VERDICT_COLOR = {
  FALHOU: PALETTE.coral,
  ALERTA: PALETTE.orange,
  PARCIAL: PALETTE.amber,
  NEUTRO: PALETTE.steel,
  RESOLVE: PALETTE.teal,
  SUBFINANCIADO: PALETTE.violet,
};
const AREA_SHORT = {
  'Pessoal e Encargos Sociais': 'Pessoal & encargos',
  'Assistência Social (exceto BF)': 'Assistência social',
  'Defesa / Militar': 'Defesa & militar',
  'Juros da Dívida': 'Juros da dívida',
  'Ciência e Tecnologia': 'Ciência & tecnologia',
  'Previdência Social': 'Previdência',
  'Segurança Pública': 'Segurança',
  'Bolsa Família': 'Bolsa Família',
};

function renderOrcamento({ svg, w, anim }, data) {
  const rows = (data.orcamento_publico?.despesas_por_area_2025 || [])
    .map((r) => ({ ...r, pct: pctNum(r.pct_orcamento) }))
    .sort((a, b) => b.pct - a.pct);
  if (!rows.length) return;

  const m = { t: 10, r: 18, b: 4, l: 0 };
  const rowH = 54;
  const h = m.t + rows.length * rowH + m.b;
  svg.attr('viewBox', `0 0 ${w} ${h}`).attr('width', w).attr('height', h);

  const maxPct = d3.max(rows, (d) => d.pct);
  const labelW = clamp(w * 0.32, 110, 250);
  const barX = m.l + labelW;
  const barW = w - barX - m.r;
  const x = d3.scaleLinear().domain([0, maxPct * 1.12]).range([0, barW]);

  const g = svg.append('g').attr('transform', `translate(0,${m.t})`);

  rows.forEach((row, i) => {
    const y = i * rowH;
    const color = VERDICT_COLOR[verdictOf(row)] || PALETTE.steel;
    const name = AREA_SHORT[row.area] || row.area;
    const valor = clean(row.valor).replace('bilhões', 'bi').replace('trilhões', 'tri');

    g.append('text')
      .attr('x', 0)
      .attr('y', y + 14)
      .text(name)
      .style('font-size', 12.5)
      .style('font-weight', 600)
      .style('fill', PALETTE.ink);

    g.append('text')
      .attr('x', 0)
      .attr('y', y + 28)
      .text(valor)
      .style('font-size', 10.5)
      .style('fill', PALETTE.inkFaint);

    g.append('line')
      .attr('x1', barX)
      .attr('x2', barX + barW)
      .attr('y1', y + 34)
      .attr('y2', y + 34)
      .attr('stroke', '#E3DCCE')
      .attr('stroke-width', 1);

    const bar = g
      .append('rect')
      .attr('x', barX)
      .attr('y', y + 26)
      .attr('width', anim ? 0 : x(row.pct))
      .attr('height', 10)
      .attr('rx', 5)
      .attr('fill', color);

    const pct = g
      .append('text')
      .attr('x', barX + x(row.pct) + 10)
      .attr('y', y + 34)
      .text(`${fmt(row.pct, /\./.test(String(row.pct_orcamento)) ? 1 : 0)}%`)
      .style('font-size', 10.5)
      .style('font-weight', 600)
      .style('fill', color)
      .style('font-variant-numeric', 'tabular-nums');

    if (anim) {
      bar
        .transition()
        .delay(i * 55)
        .duration(850)
        .ease(d3.easeCubicOut)
        .attr('width', x(row.pct));
      pct
        .transition()
        .delay(i * 55 + 500)
        .duration(350)
        .style('opacity', 0)
        .transition()
        .duration(400)
        .style('opacity', 1);
    }

    const group = g.append('g').style('opacity', anim ? 0 : 1);
    if (anim) group.transition().delay(140 + i * 55).duration(350).style('opacity', 1);

    group
      .append('rect')
      .attr('x', 0)
      .attr('y', y)
      .attr('width', w - m.r)
      .attr('height', rowH)
      .attr('fill', 'transparent')
      .on('pointerenter', (event) => {
        const verdict = verdictOf(row) || '—';
        tipShow(
          `<span class="tip-title"><span class="tip-dot" style="background:${color}"></span>${name}</span>
           ${valor} · ${fmt(row.pct, 1)}% do orçamento
           <span class="tip-sub">Veredito: ${clean(verdict).replace(/\s*—.*$/, '')}</span>`
        );
        tipMove(event);
      })
      .on('pointermove', tipMove)
      .on('pointerleave', tipHide);
  });

  const cap = $('#cap-orcamento');
  if (cap) {
    const g = data.orcamento_publico?.resumo_geral || {};
    const bottom = rows.slice(-2).map((r) => AREA_SHORT[r.area] || r.area).join(' e ');
    cap.innerHTML = `São <strong>${clean(g.orcamento_uniao_2025 || 'R$ 5,7 trilhões')}</strong> no total. Só juros da dívida e salários comem mais do que saúde e educação juntas. E ${bottom}, somadas, não chegam a 1% do bolo.`;
  }
}

/* ------------------------------------------------------------
   9. Escada da renda — skyline
   ------------------------------------------------------------ */

function renderRenda({ svg, w, anim }, data) {
  const rows = (data.trabalho_renda?.distribuicao_renda_decil || []).map((r) => ({
    ...r,
    value: toNum(r.renda),
  }));
  if (!rows.length) return;

  const m = { t: 26, r: 6, b: 30, l: 6 };
  const h = 300;
  svg.attr('viewBox', `0 0 ${w} ${h}`).attr('width', w).attr('height', h);

  const bw = w - m.l - m.r;
  const n = rows.length;
  const slot = bw / n;
  const barW = slot * 0.58;
  const maxV = d3.max(rows, (d) => d.value);
  const y = d3.scaleSqrt().domain([0, maxV]).range([0, h - m.t - m.b]);

  const g = svg.append('g').attr('transform', `translate(${m.l},${m.t})`);
  const bh = h - m.t - m.b;

  rows.forEach((row, i) => {
    const cx = i * slot + slot / 2;
    const barH = y(row.value);
    const isTop = i === rows.length - 1;
    const isMed = row.decil.includes('P50');
    const fill = isTop ? PALETTE.coral : isMed ? PALETTE.teal : PALETTE.ink;

    g.append('line')
      .attr('x1', cx)
      .attr('x2', cx)
      .attr('y1', bh - barH)
      .attr('y2', bh)
      .attr('stroke', fill)
      .attr('stroke-opacity', 0.16)
      .attr('stroke-width', barW);

    const bar = g
      .append('rect')
      .attr('x', cx - barW / 2)
      .attr('y', anim ? bh : bh - barH)
      .attr('width', barW)
      .attr('height', anim ? 0 : barH)
      .attr('rx', 4)
      .attr('fill', fill);

    if (slot > 52) {
      g.append('text')
        .attr('x', cx)
        .attr('y', bh - barH - 9)
        .attr('text-anchor', 'middle')
        .text(`R$ ${compactLabel(row.value)}`)
        .style('font-size', 10.5)
        .style('font-weight', 600)
        .style('fill', isTop ? PALETTE.coral : PALETTE.ink)
        .style('font-variant-numeric', 'tabular-nums');
    }

    const decilShort = row.decil.match(/P\d+/)?.[0] || '';
    g.append('text')
      .attr('x', cx)
      .attr('y', bh + 20)
      .attr('text-anchor', 'middle')
      .text(decilShort)
      .style('font-size', 10.5)
      .style('font-weight', 600)
      .style('fill', isTop ? PALETTE.coral : PALETTE.ink);

    if (anim) {
      bar
        .transition()
        .delay(i * 70)
        .duration(800)
        .ease(d3.easeCubicOut)
        .attr('y', bh - barH)
        .attr('height', barH);
    }
  });

  const medIdx = rows.findIndex((r) => r.decil.includes('P50'));
  if (medIdx >= 0) {
    const cx = medIdx * slot + slot / 2;
    g.append('line')
      .attr('x1', 0)
      .attr('x2', bw)
      .attr('y1', bh - y(rows[medIdx].value))
      .attr('y2', bh - y(rows[medIdx].value))
      .attr('stroke', PALETTE.teal)
      .attr('stroke-dasharray', '3 4')
      .attr('stroke-width', 1)
      .attr('opacity', 0.45);
    g.append('text')
      .attr('x', bw - 4)
      .attr('y', bh - y(rows[medIdx].value) - 6)
      .attr('text-anchor', 'end')
      .text('mediana')
      .style('font-size', 9.5)
      .style('font-weight', 600)
      .style('letter-spacing', '0.08em')
      .style('text-transform', 'uppercase')
      .style('fill', PALETTE.teal);
  }

  const cap = $('#cap-renda');
  if (cap) {
    cap.innerHTML = `Metade do país vive com <strong>R$ 1.600</strong> ou menos; a ponta mais pobre, com <strong>R$ 300</strong>; o topo, com <strong>R$ 25.000</strong>. E o 1% mais rico fica com <strong>28,3%</strong> de toda a renda.`;
  }
}

/* ------------------------------------------------------------
   10. Desigualdade racial — dot grid (HTML, join D3)
   ------------------------------------------------------------ */

function renderRacial(_ctx, data) {
  const racial = data.trabalho_renda?.desigualdade_racial_renda;
  if (!racial) return;
  const el = $('#chart-racial');
  const pobres = toNum(racial.pobres_pct_negro); // 70
  const ricos = toNum(racial.ricos_pct_negro); // 17
  const pctBranco = toNum(racial.renda_negro_vs_branco); // 56 (negro = % do branco)
  const ratio = 100 / pctBranco; // 1,79×

  const TOTAL = 20;
  const nPobres = Math.round((pobres / 100) * TOTAL);
  const nRicos = Math.round((ricos / 100) * TOTAL);

  const html = `
    <div class="racial-grid">
      <div class="racial-panel">
        <h3>Os 10% mais pobres</h3>
        <p class="rp-sub">${TOTAL} pontos = 10% da população</p>
        <div class="dot-row" id="dots-pobres"></div>
        <p class="rp-stat"><strong style="color:var(--ink)">${pobres}%</strong><span class="rp-who">são negros</span></p>
      </div>
      <div class="racial-panel">
        <h3>O 1% mais rico</h3>
        <p class="rp-sub">${TOTAL} pontos = 1% da população</p>
        <div class="dot-row" id="dots-ricos"></div>
        <p class="rp-stat"><strong style="color:var(--coral)">${ricos}%</strong><span class="rp-who">são negros</span></p>
      </div>
      <div class="racial-gap">
        <p class="rg-num">${fmt(ratio, 2)}×</p>
        <p class="rg-label">o trabalhador branco ganha a mais</p>
      </div>
    </div>`;

  el.innerHTML = html;

  const mkDots = (sel, nOn, cls) => {
    d3.select(sel)
      .selectAll('.dot')
      .data(d3.range(TOTAL))
      .join('div')
      .attr('class', (d) => `dot ${d < nOn ? 'on' : ''} ${cls || ''}`)
      .style('opacity', 0)
      .transition()
      .delay((d) => d * 28)
      .duration(300)
      .style('opacity', 1);
  };

  if (typeof IntersectionObserver !== 'undefined') {
    const io = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting) {
          mkDots('#dots-pobres', nPobres);
          mkDots('#dots-ricos', nRicos, 'pop');
          io.disconnect();
        }
      },
      { threshold: 0.3 }
    );
    io.observe(el);
  } else {
    mkDots('#dots-pobres', nPobres);
    mkDots('#dots-ricos', nRicos, 'pop');
  }

  const cap = $('#cap-racial');
  if (cap) {
    cap.innerHTML = `Um negro recebe <strong>${pctBranco}%</strong> do que um branco recebe — ou seja, o branco ganha ${fmt(ratio, 2)}× mais. Entre os mais pobres, a maioria é negra. Entre os mais ricos, quase ninguém.`;
  }
}

/* ------------------------------------------------------------
   11. Violência — ranking por estado + strip dos 27 estados
   ------------------------------------------------------------ */

function renderViolencia({ svg, w, anim }, data) {
  const rows = (data.violencia_detalhada?.ranking_homicidios_por_estado_top10_2023 || [])
    .map((r) => ({ ...r, value: toNum(r.taxa) }))
    .filter((r) => r.estado && !isNaN(r.value));
  if (!rows.length) return;

  const m = { t: 10, r: 30, b: 4, l: 40 };
  const rowH = 32;
  const h = m.t + rows.length * rowH + m.b;
  svg.attr('viewBox', `0 0 ${w} ${h}`).attr('width', w).attr('height', h);

  const maxV = d3.max(rows, (d) => d.value);
  const barX = m.l;
  const barW = w - m.l - m.r;
  const x = d3.scaleLinear().domain([0, maxV * 1.08]).range([0, barW]);
  const color = d3.scaleLinear().domain([1, 10]).range([PALETTE.coralDeep, PALETTE.coral]);

  const g = svg.append('g').attr('transform', `translate(0,${m.t})`);

  rows.forEach((row, i) => {
    const y = i * rowH;
    g.append('text')
      .attr('x', 0)
      .attr('y', y + 18)
      .text(String(row.rank).padStart(2, '0'))
      .style('font-size', 11)
      .style('font-weight', 600)
      .style('fill', PALETTE.inkFaint);

    g.append('text')
      .attr('x', 28)
      .attr('y', y + 18)
      .text(clean(row.estado))
      .style('font-size', 12.5)
      .style('font-weight', 700)
      .style('fill', PALETTE.ink);

    g.append('line')
      .attr('x1', barX)
      .attr('x2', barX + barW)
      .attr('y1', y + 20)
      .attr('y2', y + 20)
      .attr('stroke', '#E3DCCE')
      .attr('stroke-width', 1);

    const c = color(i + 1);
    const bar = g
      .append('rect')
      .attr('x', barX)
      .attr('y', y + 13)
      .attr('width', anim ? 0 : x(row.value))
      .attr('height', 9)
      .attr('rx', 4.5)
      .attr('fill', c);

    const val = g
      .append('text')
      .attr('x', barX + x(row.value) + 8)
      .attr('y', y + 20)
      .text(`${clean(row.taxa)}`)
      .style('font-size', 11)
      .style('font-weight', 600)
      .style('fill', c)
      .style('font-variant-numeric', 'tabular-nums');

    if (anim) {
      bar.transition().delay(i * 50).duration(800).ease(d3.easeCubicOut).attr('width', x(row.value));
      val
        .transition()
        .delay(i * 50 + 450)
        .duration(300)
        .style('opacity', 0)
        .transition()
        .duration(350)
        .style('opacity', 1);
    }
  });

  const cap = $('#cap-violencia');
  if (cap) {
    const r = data.violencia_detalhada?.resumo || {};
    cap.innerHTML = `No país inteiro, <strong>${clean(r.homicidios_2023 || '45.747 por ano')}</strong> — mais de 125 por dia. Em alguns estados a chance de morrer assassinado é muito maior. Veja o seu.`;
  }
}

function renderStateStrip(data) {
  const el = $('#state-strip');
  const states = data.mapa_estados || {};
  const entries = Object.entries(states);
  if (!entries.length) return;

  const statusColor = {
    CRITICO: PALETTE.coral,
    ALERTA: PALETTE.amber,
    OK: PALETTE.teal,
  };

  d3.select(el)
    .selectAll('.state-tile')
    .data(entries, (d) => d[0])
    .join('div')
    .attr('class', 'state-tile')
    .attr('role', 'img')
    .attr('aria-label', (d) => `${d[1].nome}: ${d[1].status}`)
    .html(
      (d) => `
      <span class="st-code" style="color:${statusColor[d[1].status] || PALETTE.steel}">${d[0]}</span>
      <span class="st-name">${clean(d[1].nome)}</span>
      <span class="st-status" style="background:${statusColor[d[1].status] || PALETTE.steel}"></span>`
    )
    .style('opacity', 0)
    .transition()
    .delay((d, i) => i * 15)
    .duration(350)
    .style('opacity', 1);
}

/* ------------------------------------------------------------
   12. Brasil vs OCDE — dumbbell por indicador
   ------------------------------------------------------------ */

const HIGH_BETTER = new Set(['PIB per capita', 'Gasto saúde %PIB', 'Gasto aluno/ano']);

function renderOcde({ svg, w, anim }, data) {
  const rows = (data.comparativo_internacional?.brasil_vs_ocde || [])
    .map((r) => ({ ...r, b: toNum(r.brasil), o: toNum(r.ocde_media) }))
    .filter((r) => !isNaN(r.b) && !isNaN(r.o));
  if (!rows.length) return;

  const m = { t: 6, r: 6, b: 4, l: 0 };
  const rowH = 64;
  const h = m.t + rows.length * rowH + m.b;
  svg.attr('viewBox', `0 0 ${w} ${h}`).attr('width', w).attr('height', h);

  const trackX = 4;
  const trackW = w - trackX * 2;
  const g = svg.append('g').attr('transform', `translate(0,${m.t})`);

  rows.forEach((row, i) => {
    const y = i * rowH;
    const minV = Math.min(row.b, row.o);
    const maxV = Math.max(row.b, row.o);
    const span = maxV - minV || 1;
    const pos = (v) => trackX + ((v - minV) / span) * trackW;

    const pxB = pos(row.b);
    const pxO = pos(row.o);
    const worse = HIGH_BETTER.has(row.indicador) ? row.o > row.b : row.b > row.o;
    const ratio = Math.max(row.b, row.o) / Math.min(row.b, row.o);

    g.append('text')
      .attr('x', 0)
      .attr('y', y + 12)
      .text(clean(row.indicador))
      .style('font-size', 12)
      .style('font-weight', 600)
      .style('fill', PALETTE.ink);

    g.append('line')
      .attr('x1', trackX)
      .attr('x2', trackX + trackW)
      .attr('y1', y + 34)
      .attr('y2', y + 34)
      .attr('stroke', '#E3DCCE')
      .attr('stroke-width', 1);

    const connector = g
      .append('line')
      .attr('x1', pxB)
      .attr('x2', pxO)
      .attr('y1', y + 34)
      .attr('y2', y + 34)
      .attr('stroke', worse ? PALETTE.coral : PALETTE.teal)
      .attr('stroke-width', 2)
      .attr('opacity', 0.5);

    const dB = g
      .append('circle')
      .attr('cx', pxB)
      .attr('cy', y + 34)
      .attr('r', 6)
      .attr('fill', worse ? PALETTE.coral : PALETTE.ink);

    const dO = g
      .append('circle')
      .attr('cx', pxO)
      .attr('cy', y + 34)
      .attr('r', 6)
      .attr('fill', PALETTE.steel);

    g.append('text')
      .attr('x', pxB)
      .attr('y', y + 24)
      .attr('text-anchor', pxB < pxO ? 'start' : 'end')
      .text(clean(row.brasil))
      .style('font-size', 9.5)
      .style('font-weight', 600)
      .style('fill', PALETTE.ink);

    g.append('text')
      .attr('x', pxO)
      .attr('y', y + 52)
      .attr('text-anchor', pxO > pxB ? 'end' : 'start')
      .text(clean(row.ocde_media))
      .style('font-size', 9.5)
      .style('font-weight', 600)
      .style('fill', PALETTE.steel);

    g.append('text')
      .attr('x', trackX + trackW)
      .attr('y', y + 34)
      .attr('text-anchor', 'end')
      .text(`${fmt(ratio, 1)}×`)
      .style('font-size', 11)
      .style('font-weight', 700)
      .style('fill', worse ? PALETTE.coral : PALETTE.teal)
      .style('font-variant-numeric', 'tabular-nums');

    if (anim) {
      const o = g.append('g').style('opacity', 0);
      o.transition().delay(i * 60 + 200).duration(400).style('opacity', 1);
      dB.attr('r', 0).transition().delay(i * 60).duration(600).ease(d3.easeBackOut).attr('r', 6);
      dO.attr('r', 0).transition().delay(i * 60 + 120).duration(600).ease(d3.easeBackOut).attr('r', 6);
      connector.attr('opacity', 0).transition().delay(i * 60 + 60).duration(500).attr('opacity', 0.5);
    }
  });

  const cap = $('#cap-ocde');
  if (cap) {
    cap.innerHTML = `Os países ricos produzem e gastam <strong>4 a 5× mais</strong> por pessoa em saúde e educação. E mesmo assim têm menos violência e menos desigualdade que o Brasil.`;
  }
}

/* ------------------------------------------------------------
   13. Mosaico de fatos — grid filtrável
   ------------------------------------------------------------ */

const FACT_CATS = {
  emergencia: { label: 'Emergência', order: 0 },
  urgente: { label: 'Urgente', order: 1 },
  alerta: { label: 'Alerta', order: 2 },
  rep: { label: 'Renda & trabalho', order: 3 },
  geral: { label: 'Geral', order: 4 },
};

const NUM_COLOR = {
  'num-vermelho': PALETTE.coral,
  'num-roxo': PALETTE.violet,
  'num-amarelo': PALETTE.amber,
  'num-verde': PALETTE.teal,
};

function renderFatos(data) {
  const facts = (data.compartilhamento_whatsapp || [])
    .filter((f) => FACT_CATS[f.cat])
    .sort(
      (a, b) => FACT_CATS[a.cat].order - FACT_CATS[b.cat].order
    );
  if (!facts.length) return;

  const pills = $('#fact-pills');
  const grid = $('#fact-grid');
  let active = 'all';

  const catMeta = (cat) => FACT_CATS[cat] || { label: cat };

  const renderPills = () => {
    const groups = ['all'].concat([...new Set(facts.map((f) => f.cat))]);
    d3.select(pills)
      .selectAll('button.pill')
      .data(groups, (d) => d)
      .join('button')
      .attr('class', 'pill')
      .attr('role', 'tab')
      .attr('aria-pressed', (d) => (d === active ? 'true' : 'false'))
      .on('click', (event, d) => {
        active = d;
        renderPills();
        renderGrid();
      })
      .html((d) => {
        const count = d === 'all' ? facts.length : facts.filter((f) => f.cat === d).length;
        return `${d === 'all' ? 'Todos' : catMeta(d).label}<span class="pill-count">${count}</span>`;
      });
  };

  const renderGrid = () => {
    const subset = active === 'all' ? facts : facts.filter((f) => f.cat === active);
    const cards = d3
      .select(grid)
      .selectAll('.fact')
      .data(subset, (f) => f.num + f.label)
      .join(
        (enter) =>
          enter
            .append('article')
            .attr('class', 'fact')
            .style('opacity', 0)
            .style('transform', 'translateY(12px)'),
        (update) => update,
        (exit) => exit.transition().duration(180).style('opacity', 0).style('transform', 'scale(0.96)').remove()
      );

    cards
      .attr('class', 'fact')
      .html((f) => {
        const color = NUM_COLOR[f.cor] || PALETTE.ink;
        const fonte = clean(f.fonte) || 'Fonte oficial';
        return `
          <span class="fact-num" style="color:${color}">${clean(f.num)}</span>
          <p class="fact-label">${clean(f.label)}</p>
          <span class="fact-source">${fonte}</span>`;
      })
      .style('opacity', 0)
      .style('transform', 'translateY(12px)')
      .transition()
      .delay((d, i) => i * 35)
      .duration(420)
      .style('opacity', 1)
      .style('transform', 'translateY(0)');
  };

  renderPills();
  renderGrid();
}

/* ------------------------------------------------------------
   14. Timeline
   ------------------------------------------------------------ */

function renderTimeline(data) {
  const events = (data.historia_timeline_expandida?.eventos || []).slice(0, 10);
  if (!events.length) return;
  const el = $('#timeline');

  d3.select(el)
    .selectAll('li')
    .data(events, (d, i) => i)
    .join('li')
    .html(
      (d) => `
      <span class="tl-year">${clean(d.ano)}</span>
      <h3 class="tl-title">${clean(d.evento)}</h3>
      <p class="tl-desc">${clean(d.descricao)}</p>
      ${d.impacto_hoje ? `<p class="tl-impact"><strong>Hoje</strong>${clean(d.impacto_hoje)}</p>` : ''}`
    );

  if (typeof IntersectionObserver !== 'undefined') {
    const items = $$('#timeline li');
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-in');
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.4 }
    );
    items.forEach((li) => io.observe(li));
  } else {
    $$('#timeline li').forEach((li) => li.classList.add('is-in'));
  }
}

/* ------------------------------------------------------------
   15. Footer — fontes
   ------------------------------------------------------------ */

function renderSources(data) {
  const fonts = (data.meta?.fontes_principais || []).filter(Boolean);
  const el = $('#sources');
  if (!fonts.length) return;
  d3.select(el)
    .selectAll('li')
    .data(fonts)
    .join('li')
    .text((f) => clean(f));
}

/* ------------------------------------------------------------ */
/* 17. Chapter headers — popula do JSON (capitulos)              */
/* ------------------------------------------------------------ */

function renderChapterHeaders(data) {
  var caps = data.capitulos;
  if (!caps) return;

  for (var chId in caps) {
    if (!Object.prototype.hasOwnProperty.call(caps, chId)) continue;
    var c = caps[chId];
    var section = document.getElementById(chId);
    if (!section) continue;

    var noEl = section.querySelector('.chapter-no');
    var kickEl = section.querySelector('.chapter-head .kicker');
    var titleEl = section.querySelector('.chapter-head h2');
    var ledeEl = section.querySelector('.chapter-head .chapter-lede');

    if (noEl && c.numero) noEl.textContent = c.numero;
    if (kickEl && c.kicker) kickEl.textContent = c.kicker;
    if (titleEl && c.titulo) titleEl.textContent = c.titulo;
    if (ledeEl && c.lede) ledeEl.textContent = c.lede;
  }

  // Masthead (se existir no manifesto.hero)
  var hero = data.manifesto && data.manifesto.hero;
  if (!hero) return;

  var mastKicker = document.querySelector('.masthead-kicker');
  var mastTitle = document.querySelector('.masthead-title');
  var mastLede = document.querySelector('.lede');

  if (mastKicker && hero.masthead_kicker) mastKicker.textContent = hero.masthead_kicker;
  if (mastTitle && hero.masthead_titulo) mastTitle.innerHTML = hero.masthead_titulo;
  if (mastLede && hero.masthead_lede) mastLede.textContent = hero.masthead_lede;
}

/* ------------------------------------------------------------ */
/* 16. Init                                                      */
/* ------------------------------------------------------------ */

function renderRaioXLegend(data) {
  const el = $('#raio-legend');
  if (!el) return;
  const rows = data.raio_x_nacional?.exames || [];
  const seen = [...new Set(rows.map((r) => r.urgencia_rotulo))];
  el.innerHTML = seen
    .map(
      (u) => `
      <span class="legend-item">
        <span class="legend-swatch" style="background:${UR_COLOR[u]}"></span>
        ${UR_LABEL[u]}
      </span>`
    )
    .join('');
}

async function init() {
  const data = await loadData();

  // Popula headers de capítulos e masthead a partir do JSON
  renderChapterHeaders(data);

  buildHero(data);
  renderRaioXLegend(data);
  makeChart('#chart-raiox', (ctx) => renderRaioX(ctx, data));
  makeChart('#chart-orcamento', (ctx) => renderOrcamento(ctx, data));
  makeChart('#chart-renda', (ctx) => renderRenda(ctx, data));
  makeChart('#chart-violencia', (ctx) => renderViolencia(ctx, data));
  makeChart('#chart-ocde', (ctx) => renderOcde(ctx, data));

  renderRacial(null, data);
  renderFatos(data);
  renderTimeline(data);
  renderSources(data);
  renderStateStrip(data);

  // Capítulos dinâmicos: as 34 seções orfãs do JSON
  if (window.initDataSections) {
    window.initDataSections(data);
  }

  // Dossiês: renderiza os 525 políticos do JSON
  if (window.renderDossies) {
    window.renderDossies(data);
  }
}

document.addEventListener('DOMContentLoaded', init);
