/* ============================================================
   Central de downloads — micro-carrosseis de Instagram
   Renderiza slides em canvas, gera ZIP por postagem e aplica
   customização (@ handle, logo, cores). Sem dependências.
   ============================================================ */

'use strict';

(function () {
  const CARROSSEIS = window.CARROSSEIS || [];
  let DOSSIER_CARS = [];
  const $ = (sel, el) => (el || document).querySelector(sel);
  const $$ = (sel, el) => Array.from((el || document).querySelectorAll(sel));

  const LS_PREFIX = 'carr_';
  const ls = {
    get(key, fallback) {
      try {
        const v = localStorage.getItem(LS_PREFIX + key);
        return v === null ? fallback : v;
      } catch (e) { return fallback; }
    },
    set(key, value) {
      try { localStorage.setItem(LS_PREFIX + key, value); } catch (e) { /* quota etc. */ }
    },
  };

  const FORMATS = {
    square: { w: 1080, h: 1080, label: '1080×1080 (quadrado)' },
    vertical: { w: 1080, h: 1350, label: '1080×1350 (4:5 retrato)' },
  };

  const state = {
    handle: ls.get('handle', '@seuperfil'),
    format: ls.get('format', 'square'),
    colors: {},          // id -> cor customizada
  };

  /* -------------------- Cores / utilidades -------------------- */

  function hexToRgb(hex) {
    const m = String(hex).replace('#', '');
    const full = m.length === 3 ? m.split('').map((c) => c + c).join('') : m;
    const n = parseInt(full, 16);
    return { r: (n >> 16) & 255, g: (n >> 8) & 255, b: n & 255 };
  }

  function rgba(hex, a) {
    const { r, g, b } = hexToRgb(hex);
    return `rgba(${r}, ${g}, ${b}, ${a})`;
  }

  function isLight(hex) {
    const { r, g, b } = hexToRgb(hex);
    return (0.299 * r + 0.587 * g + 0.114 * b) > 160;
  }

  function normalizeHandle(h) {
    let s = String(h || '').trim().replace(/\s+/g, '');
    if (!s) s = '@seuperfil';
    if (s.charAt(0) !== '@') s = '@' + s;
    return s;
  }

  function esc(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function wrapText(ctx, text, maxW) {
    const words = String(text).split(/\s+/);
    const lines = [];
    let cur = '';
    const push = (w) => {
      const test = cur ? cur + ' ' + w : w;
      if (ctx.measureText(test).width > maxW && cur) {
        lines.push(cur);
        cur = w;
      } else {
        cur = test;
      }
    };
    for (let w of words) {
      // quebra palavras mais largas que a área disponível
      while (w && ctx.measureText(w).width > maxW && w.length > 1) {
        let lo = 1;
        let hi = w.length;
        while (lo < hi) {
          const mid = (lo + hi + 1) >> 1;
          if (ctx.measureText(w.slice(0, mid)).width <= maxW) lo = mid;
          else hi = mid - 1;
        }
        push(w.slice(0, lo));
        w = w.slice(lo);
      }
      if (w) push(w);
    }
    if (cur) lines.push(cur);
    return lines;
  }

  function roundRect(ctx, x, y, w, h, r) {
    r = Math.min(r, w / 2, h / 2);
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.arcTo(x + w, y, x + w, y + h, r);
    ctx.arcTo(x + w, y + h, x, y + h, r);
    ctx.arcTo(x, y + h, x, y, r);
    ctx.arcTo(x, y, x + w, y, r);
    ctx.closePath();
  }

  function centeredText(ctx, text, cx, y, maxW) {
    const lines = wrapText(ctx, text, maxW);
    lines.forEach((ln, i) => ctx.fillText(ln, cx, y + i * ctx.fontSize * 1.06));
    return lines.length;
  }

  /* -------------------- ZIP (store, sem compressão) -------------------- */

  const CRC_TABLE = (() => {
    const t = new Uint32Array(256);
    for (let n = 0; n < 256; n++) {
      let c = n;
      for (let k = 0; k < 8; k++) c = c & 1 ? 0xedb88320 ^ (c >>> 1) : c >>> 1;
      t[n] = c >>> 0;
    }
    return t;
  })();

  function crc32(bytes) {
    let c = 0xffffffff;
    for (let i = 0; i < bytes.length; i++) c = CRC_TABLE[(c ^ bytes[i]) & 0xff] ^ (c >>> 8);
    return (c ^ 0xffffffff) >>> 0;
  }

  // files: [{name, data: Uint8Array}]
  function buildZip(files) {
    const enc = new TextEncoder();
    const parts = [];
    const central = [];
    let offset = 0;
    const now = new Date();
    const dosTime = ((now.getHours() << 11) | (now.getMinutes() << 5) | (now.getSeconds() >> 1)) & 0xffff;
    const dosDate = (((now.getFullYear() - 1980) << 9) | ((now.getMonth() + 1) << 5) | now.getDate()) & 0xffff;

    for (const f of files) {
      const name = enc.encode(f.name);
      const crc = crc32(f.data);
      const local = new Uint8Array(30 + name.length + f.data.length);
      const dv = new DataView(local.buffer);
      dv.setUint32(0, 0x04034b50, true);          // local file header
      dv.setUint16(4, 20, true);                   // version
      dv.setUint16(6, 0, true);                    // flags
      dv.setUint16(8, 0, true);                    // method: store
      dv.setUint16(10, dosTime, true);
      dv.setUint16(12, dosDate, true);
      dv.setUint32(14, crc, true);
      dv.setUint32(18, f.data.length, true);       // compressed
      dv.setUint32(22, f.data.length, true);       // uncompressed
      dv.setUint16(26, name.length, true);
      dv.setUint16(28, 0, true);                   // extra len
      local.set(name, 30);
      local.set(f.data, 30 + name.length);
      parts.push(local);
      central.push({ name, crc, size: f.data.length, offset });
      offset += local.length;
    }

    const cdStart = offset;
    for (const c of central) {
      const rec = new Uint8Array(46 + c.name.length);
      const dv = new DataView(rec.buffer);
      dv.setUint32(0, 0x02014b50, true);           // central dir header
      dv.setUint16(4, 20, true);
      dv.setUint16(6, 20, true);
      dv.setUint16(8, 0, true);
      dv.setUint16(10, 0, true);
      dv.setUint16(12, dosTime, true);
      dv.setUint16(14, dosDate, true);
      dv.setUint32(16, c.crc, true);
      dv.setUint32(20, c.size, true);
      dv.setUint32(24, c.size, true);
      dv.setUint16(28, c.name.length, true);
      dv.setUint16(30, 0, true);
      dv.setUint16(32, 0, true);
      dv.setUint16(34, 0, true);
      dv.setUint16(36, 0, true);
      dv.setUint32(38, 0, true);                   // external attrs
      dv.setUint32(42, c.offset, true);
      rec.set(c.name, 46);
      parts.push(rec);
      offset += rec.length;
    }
    const cdSize = offset - cdStart;

    const eocd = new Uint8Array(22);
    const dv = new DataView(eocd.buffer);
    dv.setUint32(0, 0x06054b50, true);
    dv.setUint16(4, 0, true);
    dv.setUint16(6, 0, true);
    dv.setUint16(8, files.length, true);
    dv.setUint16(10, files.length, true);
    dv.setUint32(12, cdSize, true);
    dv.setUint32(16, cdStart, true);
    dv.setUint16(20, 0, true);
    parts.push(eocd);

    const total = parts.reduce((n, p) => n + p.length, 0);
    const out = new Uint8Array(total);
    let o = 0;
    for (const p of parts) { out.set(p, o); o += p.length; }
    return out;
  }

  /* -------------------- Renderização de slides -------------------- */

  const FONT_DISP = '"Space Grotesk", Inter, system-ui, sans-serif';
  const UP_RED = '#C00810';
  const FONT_SANS = 'Inter, system-ui, sans-serif';

  function drawLogo(ctx, x, y, size, bg) {
    // Sem logo de partido — sistema multi-partidário.
    // Mantida a assinatura para não quebrar callers existentes.
  }

  function drawHandleFooter(ctx, W, H) {
    const size = Math.round(W * 0.055);
    ctx.fillStyle = '#F5F5F6';
    ctx.font = `700 ${Math.round(W * 0.045)}px ${FONT_DISP}`;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    const label = normalizeHandle(state.handle);
    ctx.fillText(label, W / 2, H - size * 1.5);
    // linha fina de acento vermelho
    ctx.fillStyle = '#C00810';
    const w = ctx.measureText(label).width;
    ctx.fillRect(W / 2 - w / 2, H - size * 2.15, w, Math.max(2, size * 0.05));
  }

  function drawWatermark(ctx, W, H, bg) {
    // Sem watermark de marca — sistema multi-partidário.
  }

  function drawCoverSlide(ctx, car, i, total, opts) {
    const W = ctx.canvas.width;
    const H = ctx.canvas.height;
    const color = opts.color;

    // fundo preto com gradiente sutil
    const g = ctx.createLinearGradient(0, 0, W, H);
    g.addColorStop(0, '#000000');
    g.addColorStop(1, '#16161B');
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, W, H);

    // barra de acento vermelha no topo
    ctx.fillStyle = color;
    ctx.fillRect(0, 0, W, Math.max(10, W * 0.02));

    const pad = W * 0.08;
    const logoSize = W * 0.13;
    drawLogo(ctx, pad, pad, logoSize, '#000000');

    ctx.fillStyle = color;
    ctx.font = `700 ${Math.round(W * 0.05)}px ${FONT_SANS}`;
    ctx.textAlign = 'right';
    ctx.textBaseline = 'middle';
    ctx.fillText(`CARROSSEL ${i + 1}/${total}`, W - pad, pad + logoSize / 2);

    // título
    ctx.fillStyle = '#F5F5F6';
    ctx.font = `700 ${Math.round(W * 0.085)}px ${FONT_DISP}`;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    let y = H * 0.44;
    const titleLines = wrapText(ctx, car.nome, W - pad * 2);
    titleLines.forEach((ln) => {
      ctx.fillText(ln, W / 2, y);
      y += W * 0.095;
    });

    // tagline
    ctx.font = `500 ${Math.round(W * 0.042)}px ${FONT_SANS}`;
    ctx.fillStyle = '#9A9AA3';
    y += W * 0.04;
    wrapText(ctx, car.tagline, W - pad * 1.5).forEach((ln) => {
      ctx.fillText(ln, W / 2, y);
      y += W * 0.05;
    });

    // dados_chave como chips (empilham em linhas quando faltar espaço)
    const chips = String(car.dados_chave || '').split(/[·;]/).map((s) => s.trim()).filter(Boolean).slice(0, 3);
    if (chips.length) {
      const maxW = W - pad * 2;
      let chipFont = Math.round(W * 0.032);
      let chipH = W * 0.075;
      const gapX = W * 0.02;
      let gapY = W * 0.03;
      ctx.font = `600 ${chipFont}px ${FONT_SANS}`;
      const footerLimit = H - W * 0.135;
      // compacta chips até caber acima do rodapé
      let widths;
      let rows;
      for (let attempt = 0; attempt < 4; attempt++) {
        widths = chips.map((c) => Math.min(ctx.measureText(c).width + W * 0.05, maxW));
        // empacota em linhas de largura <= maxW
        rows = [];
        let row = [];
        let rowW = 0;
        chips.forEach((c, ci) => {
          const w = widths[ci];
          if (row.length && rowW + gapX + w > maxW) {
            rows.push(row);
            row = [];
            rowW = 0;
          }
          row.push(ci);
          rowW += w + (row.length > 1 ? gapX : 0);
        });
        if (row.length) rows.push(row);
        const blockBottom = y + rows.length * (chipH + gapY) - gapY + chipH / 2;
        if (blockBottom <= footerLimit) break;
        chipFont = Math.round(chipFont * 0.86);
        chipH *= 0.86;
        gapY *= 0.86;
        ctx.font = `600 ${chipFont}px ${FONT_SANS}`;
      }

      y += W * 0.05;
      rows.forEach((r, ri) => {
        const rw = r.reduce((a, ci) => a + widths[ci], 0) + gapX * (r.length - 1);
        let x = W / 2 - rw / 2;
        const cy = y + ri * (chipH + gapY);
        r.forEach((ci) => {
          ctx.fillStyle = 'rgba(255,255,255,0.06)';
          roundRect(ctx, x, cy - chipH / 2, widths[ci], chipH, chipH / 2);
          ctx.fill();
          ctx.strokeStyle = 'rgba(255,255,255,0.25)';
          ctx.lineWidth = Math.max(2, W * 0.004);
          ctx.stroke();
          ctx.fillStyle = color;
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillText(chips[ci], x + widths[ci] / 2, cy + 1);
          x += widths[ci] + gapX;
        });
      });
    }

    drawHandleFooter(ctx, W, H);
    drawWatermark(ctx, W, H, '#000000');
  }

  function drawContentSlide(ctx, car, slide, i, total, opts) {
    const W = ctx.canvas.width;
    const H = ctx.canvas.height;
    const color = opts.color;
    const pad = W * 0.08;
    const footerH = W * 0.14;
    const bodyTop = H * 0.16;
    const bodyBottom = H - footerH - W * 0.02;
    const maxBody = bodyBottom - bodyTop;
    const maxW = W - pad * 2;

    ctx.fillStyle = '#0B0B0F';
    ctx.fillRect(0, 0, W, H);

    // barra superior
    ctx.fillStyle = color;
    ctx.fillRect(0, 0, W, Math.max(10, W * 0.02));

    // pill
    if (slide.pill) {
      ctx.font = `700 ${Math.round(W * 0.036)}px ${FONT_SANS}`;
      const pw = Math.min(ctx.measureText(slide.pill).width + W * 0.06, maxW);
      const ph = W * 0.08;
      ctx.fillStyle = color;
      roundRect(ctx, pad, pad + W * 0.02, pw, ph, ph / 2);
      ctx.fill();
      ctx.fillStyle = isLight(color) ? '#18181B' : '#fff';
      ctx.textAlign = 'left';
      ctx.textBaseline = 'middle';
      ctx.fillText(slide.pill, pad + W * 0.03, pad + W * 0.02 + ph / 2);
    }

    ctx.fillStyle = '#8A8A91';
    ctx.font = `600 ${Math.round(W * 0.03)}px ${FONT_SANS}`;
    ctx.textAlign = 'right';
    ctx.textBaseline = 'middle';
    ctx.fillText(`CARROSSEL ${i + 1}/${total}`, W - pad, pad);

    // blocos de conteúdo
    const blocks = [];
    if (slide.titulo) blocks.push({ text: slide.titulo, size: W * 0.062, weight: 700, family: FONT_DISP, fill: '#F5F5F6', lh: 1.14, gap: W * 0.015 });
    if (slide.stat) blocks.push({ text: slide.stat, size: W * 0.135, weight: 700, family: FONT_DISP, fill: color, lh: 1.08, gap: W * 0.005 });
    if (slide.statLabel) blocks.push({ text: slide.statLabel, size: W * 0.036, weight: 700, family: FONT_SANS, fill: '#F5F5F6', lh: 1.15, gap: W * 0.012 });
    if (slide.texto) blocks.push({ text: slide.texto, size: W * 0.038, weight: 500, family: FONT_SANS, fill: '#B4B4BC', lh: 1.28, gap: W * 0.014 });
    if (slide.gap) blocks.push({ text: '“' + slide.gap + '”', size: W * 0.034, weight: 600, family: FONT_SANS, fill: color, lh: 1.24, gap: W * 0.016 });

    // mede altura necessária em uma dada escala
    const heightAt = (scale) => {
      let y = 0;
      for (const b of blocks) {
        ctx.font = `${b.weight} ${Math.round(b.size * scale)}px ${b.family}`;
        const n = wrapText(ctx, b.text, maxW).length;
        y += n * b.size * scale * b.lh;
        if (n) y += b.gap * scale;
      }
      return y;
    };

    // reduz a escala até caber no corpo disponível
    let scale = 1;
    for (let k = 0; k < 12; k++) {
      if (heightAt(scale) <= maxBody) break;
      scale *= 0.9;
    }

    // altura total na escala final (para centralizar verticalmente)
    const totalH = heightAt(scale);
    let y = bodyTop + (maxBody - totalH) / 2;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'top';
    for (const b of blocks) {
      const size = Math.round(b.size * scale);
      ctx.fillStyle = b.fill;
      ctx.font = `${b.weight} ${size}px ${b.family}`;
      const lines = wrapText(ctx, b.text, maxW);
      for (const ln of lines) {
        ctx.fillText(ln, W / 2, y);
        y += size * b.lh;
      }
      if (lines.length) y += b.gap * scale;
    }

    // rodapé: handle + logo
    ctx.fillStyle = isLight(color) ? 'rgba(255,255,255,0.05)' : 'rgba(255,255,255,0.07)';
    ctx.fillRect(0, H - footerH, W, footerH);
    drawLogo(ctx, pad, H - footerH / 2 - W * 0.05, W * 0.1, '#0B0B0F');
    ctx.fillStyle = '#8A8A91';
    ctx.font = `700 ${Math.round(W * 0.035)}px ${FONT_DISP}`;
    ctx.textAlign = 'right';
    ctx.textBaseline = 'middle';
    ctx.fillText(normalizeHandle(state.handle), W - pad, H - footerH / 2);
    drawWatermark(ctx, W, H, '#0B0B0F');
  }

  function drawCtaSlide(ctx, car, i, total, opts) {
    const W = ctx.canvas.width;
    const H = ctx.canvas.height;
    const color = opts.color;

    // fundo preto com gradiente sutil
    const g = ctx.createLinearGradient(0, 0, W, H);
    g.addColorStop(0, '#000000');
    g.addColorStop(1, '#16161B');
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, W, H);

    // barra de acento vermelha no topo
    ctx.fillStyle = color;
    ctx.fillRect(0, 0, W, Math.max(10, W * 0.02));

    const cx = W / 2;
    const pad = W * 0.08;
    const logoSize = W * 0.16;
    drawLogo(ctx, cx - logoSize * (1080 / 592.1) / 2, H * 0.17, logoSize, '#000000');

    ctx.fillStyle = color;
    ctx.font = `700 ${Math.round(W * 0.045)}px ${FONT_SANS}`;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(`CARROSSEL ${i + 1}/${total}`, cx, H * 0.10);

    // pergunta provocadora: o que o outro lado faz pra resolver
    ctx.fillStyle = '#F5F5F6';
    ctx.font = `700 ${Math.round(W * 0.048)}px ${FONT_DISP}`;
    const question = 'O QUE O OUTRO PARTIDO FEZ OU VAI FAZER PRA RESOLVER ISSO?';
    const qLines = wrapText(ctx, question, W - pad * 1.4);
    qLines.forEach((ln, li) => {
      ctx.fillText(ln, cx, H * 0.40 + li * W * 0.075);
    });

    // chamada para seguir o nosso lado
    ctx.fillStyle = color;
    ctx.font = `700 ${Math.round(W * 0.042)}px ${FONT_SANS}`;
    ctx.fillText('SE QUER SABER O NOSSO LADO, NOS SIGA.', cx, H * 0.57);

    ctx.fillStyle = '#F5F5F6';
    ctx.font = `700 ${Math.round(W * 0.09)}px ${FONT_DISP}`;
    ctx.fillText(normalizeHandle(state.handle), cx, H * 0.70);

    ctx.fillStyle = color;
    ctx.font = `700 ${Math.round(W * 0.04)}px ${FONT_SANS}`;
    ctx.fillText('SIGA E COMPARTILHE', cx, H * 0.80);

    ctx.font = `500 ${Math.round(W * 0.032)}px ${FONT_SANS}`;
    ctx.fillStyle = '#9A9AA3';
    ctx.fillText('SALVE · COMPARTILHE · ESPALHE', cx, H * 0.855);

    drawHandleFooter(ctx, W, H);
    drawWatermark(ctx, W, H, '#000000');
  }

  function renderSlide(car, slide, i, total, opts) {
    const fmt = FORMATS[state.format] || FORMATS.square;
    const canvas = document.createElement('canvas');
    canvas.width = fmt.w;
    canvas.height = fmt.h;
    const ctx = canvas.getContext('2d');
    if (slide.tipo === 'cta') drawCtaSlide(ctx, car, i, total, opts);
    else if (slide.tipo === 'content') drawContentSlide(ctx, car, slide, i, total, opts);
    else drawCoverSlide(ctx, car, i, total, opts);
    return canvas;
  }

  /* -------------------- Download -------------------- */

  function triggerDownload(blob, filename) {
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    setTimeout(() => { URL.revokeObjectURL(url); a.remove(); }, 1000);
  }

  async function downloadPost(id, btn) {
    const car = CARROSSEIS.find((c) => c.id === id) || DOSSIER_CARS.find((c) => c.id === id);
    if (!car) return;
    if (document.fonts && document.fonts.ready) await document.fonts.ready;
    const opts = { color: state.colors[id] || UP_RED };
    if (btn) { btn.disabled = true; btn.textContent = 'Gerando…'; }
    try {
      const files = [];
      for (let i = 0; i < car.slides.length; i++) {
        const canvas = renderSlide(car, car.slides[i], i, car.slides.length, opts);
        const blob = await new Promise((res, rej) => canvas.toBlob((b) => (b ? res(b) : rej(new Error('toBlob falhou'))), 'image/png'));
        const buf = new Uint8Array(await blob.arrayBuffer());
        files.push({ name: `${car.id}-slide-${String(i + 1).padStart(2, '0')}.png`, data: buf });
      }
      const zip = buildZip(files);
      triggerDownload(new Blob([zip], { type: 'application/zip' }), `${car.id}.zip`);
    } catch (e) {
      console.warn('[download]', e);
    } finally {
      if (btn) { btn.disabled = false; btn.textContent = 'Baixar post (.zip)'; }
    }
  }

  /* -------------------- Carrosséis de dossiês -------------------- */

  const DOSSIER_PILLS = [
    ['Evolução patrimonial (declarada)', 'PATRIMÔNIO'],
    ['Questionamentos sobre patrimônio', 'PATRIMÔNIO QUESTIONADO'],
    ['Doadores principais', 'QUEM PAGOU'],
    ['Processos (TSE/TCU)', 'PROCESSOS'],
    ['Lei da Ficha Limpa', 'FICHA LIMPA'],
    ['Inquéritos e denúncias', 'INQUÉRITOS'],
    ['Glosas e irregularidades', 'GLOSAS'],
    ['Polêmicas', 'POLÊMICAS'],
  ];

  function dossierBlockFacts(el, title) {
    const out = [];
    $$('.doss-block', el).forEach((block) => {
      const h = $('.doss-block-title', block);
      if (!h || !String(h.textContent).trim().startsWith(title)) return;
      $$('li, p', block).forEach((n) => {
        let s = String(n.textContent).trim().replace(/\s+/g, ' ');
        s = s.replace(/\s*Dados não disponíveis[^.]*\./gi, '').trim();
        s = s.replace(/^[-•]+\s*/, '');
        if (!s || /não disponíve/i.test(s)) return;
        out.push(s);
      });
    });
    return out;
  }

  function shortHeadline(s) {
    const words = String(s).split(/\s+/).slice(0, 5).join(' ');
    const t = words.replace(/[,;:]/g, '').toUpperCase();
    return t.length > 36 ? t.slice(0, 35) + '…' : t;
  }

  function dossierSlug(name) {
    return 'doss_' + String(name).toLowerCase()
      .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
      .replace(/[^a-z0-9]+/g, '_').replace(/^_+|_+$/g, '');
  }

  function buildDossierCars() {
    return $$('.doss-card[data-politico]').map((el) => {
      const name = el.getAttribute('data-politico');
      const slides = [{ tipo: 'cover' }];
      const chips = [];
      DOSSIER_PILLS.forEach(([title, pill]) => {
        dossierBlockFacts(el, title).slice(0, 1).forEach((f) => {
          slides.push({ tipo: 'content', pill, titulo: shortHeadline(f), texto: f });
          chips.push(shortHeadline(f));
        });
      });
      // Pula políticos sem nenhum fato público — o carrossel só mostra quem tem dados.
      if (slides.length === 1) return null;
      slides.push({ tipo: 'cta' });
      return {
        id: dossierSlug(name),
        nome: String(name).toUpperCase(),
        tagline: 'Dossiê com fontes públicas oficiais.',
        dados_chave: chips.slice(0, 3).join(' · '),
        slides,
      };
    }).filter(Boolean);
  }

  /* -------------------- Galeria -------------------- */

  function cardHTML(car) {
    const color = state.colors[car.id] || UP_RED;
    return `
      <article class="carr-card" data-id="${esc(car.id)}">
        <div class="carr-preview">
          <canvas data-canvas="${esc(car.id)}" width="1080" height="${FORMATS[state.format].h}"></canvas>
        </div>
        <div class="carr-meta">
          <h3 class="carr-nome">${esc(car.nome)}</h3>
          <p class="carr-tagline">${esc(car.tagline || '')}</p>
          <p class="carr-info">${car.slides.length} slides · ${FORMATS[state.format].label}</p>
        </div>
        <div class="carr-actions">
          <label class="carr-color">
            Cor
            <input type="color" data-color="${esc(car.id)}" value="${esc(color)}" aria-label="Cor do carrossel ${esc(car.nome)}">
          </label>
          <button class="btn btn-download" data-post="${esc(car.id)}">Baixar post (.zip)</button>
        </div>
      </article>`;
  }

  function renderGallery(gridSel, cars) {
    const grid = $(gridSel);
    if (!grid) return;
    grid.innerHTML = cars.map(cardHTML).join('');

    // previews (cover em tamanho reduzido)
    cars.forEach((car) => {
      const canvas = $(`[data-canvas="${car.id}"]`, grid);
      if (!canvas) return;
      const opts = { color: state.colors[car.id] || UP_RED };
      canvas.width = 540;
      canvas.height = Math.round(540 * (FORMATS[state.format].h / FORMATS[state.format].w));
      const ctx = canvas.getContext('2d');
      drawCoverSlide(ctx, car, 0, car.slides.length, opts);
    });

    grid.querySelectorAll('[data-post]').forEach((btn) => {
      btn.addEventListener('click', () => downloadPost(btn.getAttribute('data-post'), btn));
    });
    grid.querySelectorAll('[data-color]').forEach((input) => {
      input.addEventListener('input', () => {
        state.colors[input.getAttribute('data-color')] = input.value;
        renderGrids();
      });
    });
  }

  function renderGrids() {
    renderGallery('#carr-grid', CARROSSEIS);
    DOSSIER_CARS = buildDossierCars();
    renderGallery('#doss-grid', DOSSIER_CARS);
    const cap = $('#doss-caption');
    if (cap) cap.textContent = `${DOSSIER_CARS.length} carrosséis de dossiê · um por político com fatos públicos oficiais citados, sem inventar · PNG 1080px por slide, baixados em um ZIP por postagem.`;
  }

  /* -------------------- Painel de customização -------------------- */

  function restoreDefaults() {
    state.handle = '@seuperfil';
    state.format = 'square';
    state.colors = {};
    ls.set('handle', state.handle);
    ls.set('format', 'square');
    ls.set('colors', '');
    const handle = $('#carr-handle');
    if (handle) handle.value = state.handle;
    const format = $('#carr-format');
    if (format) format.value = state.format;
    renderGrids();
  }

  function bindPanel() {
    const handle = $('#carr-handle');
    if (handle) {
      handle.value = state.handle;
      handle.addEventListener('input', () => {
        state.handle = normalizeHandle(handle.value);
        ls.set('handle', state.handle);
        renderGrids();
      });
    }

    const format = $('#carr-format');
    if (format) {
      format.value = state.format;
      format.addEventListener('change', () => {
        state.format = format.value;
        ls.set('format', state.format);
        renderGrids();
      });
    }

    const reset = $('#carr-reset');
    if (reset) reset.addEventListener('click', restoreDefaults);
  }

  /* -------------------- Init -------------------- */

  function init() {
    try {
      state.colors = JSON.parse(ls.get('colors', '{}') || '{}');
    } catch (e) {
      state.colors = {};
    }
    if (!CARROSSEIS.length) return;
    bindPanel();
    renderGrids();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Re-renderiza quando os carrosséis chegam do JSON (carregamento assíncrono)
  document.addEventListener('carrosseis-loaded', function () {
    if (typeof CARROSSEIS !== 'undefined' && window.CARROSSEIS) {
      // Atualiza a referência local
      // (carousel-site.js lê window.CARROSSEIS no init; se já passou, re-renderiza)
      renderGrids();
      console.log('[carousel-site] Re-renderizado com dados do JSON');
    }
  });

  window.CAROUSEL_SITE = {
    buildZip,
    crc32,
    renderSlide,
    downloadPost,
    getState: () => state,
    getDossierCars: () => DOSSIER_CARS,
  };
})();
