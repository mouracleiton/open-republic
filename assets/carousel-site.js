/* ============================================================
   Central de downloads — micro-carrosseis de Instagram
   Renderiza slides em canvas, gera ZIP por postagem e aplica
   customização (@ handle, logo, cores). Sem dependências.
   ============================================================ */

'use strict';

(function () {
  const CARROSSEIS = window.CARROSSEIS || [];
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
    logo: null,          // Image
    logoData: ls.get('logo', ''),
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

  function shade(hex, f) {
    const { r, g, b } = hexToRgb(hex);
    const c = (v) => Math.max(0, Math.min(255, Math.round(v * f)));
    return `rgb(${c(r)}, ${c(g)}, ${c(b)})`;
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
  const FONT_SANS = 'Inter, system-ui, sans-serif';

  function drawLogo(ctx, x, y, size) {
    if (state.logo) {
      const s = Math.max(size / state.logo.width, size / state.logo.height);
      const dw = state.logo.width * s;
      const dh = state.logo.height * s;
      roundRect(ctx, x, y, size, size, size * 0.22);
      ctx.save();
      ctx.clip();
      ctx.drawImage(state.logo, x - (dw - size) / 2, y - (dh - size) / 2, dw, dh);
      ctx.restore();
    } else {
      // placeholder: quadrado com arroba
      ctx.fillStyle = 'rgba(255,255,255,0.18)';
      roundRect(ctx, x, y, size, size, size * 0.22);
      ctx.fill();
      ctx.strokeStyle = 'rgba(255,255,255,0.5)';
      ctx.lineWidth = Math.max(2, size * 0.03);
      ctx.stroke();
      ctx.fillStyle = '#fff';
      ctx.font = `${size * 0.55}px ${FONT_DISP}`;
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText('@', x + size / 2, y + size / 2 + size * 0.02);
    }
  }

  function drawPage(ctx, label, cx, y) {
    ctx.font = `600 ${Math.round(ctx.canvas.width / 40)}px ${FONT_SANS}`;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillStyle = 'rgba(255,255,255,0.85)';
    ctx.fillText(label, cx, y);
  }

  function drawHandleFooter(ctx, W, H, color, light) {
    const size = Math.round(W * 0.055);
    ctx.fillStyle = light ? 'rgba(255,255,255,0.92)' : 'rgba(27,27,27,0.82)';
    ctx.font = `700 ${Math.round(W * 0.045)}px ${FONT_DISP}`;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    const label = normalizeHandle(state.handle);
    ctx.fillText(label, W / 2, H - size * 1.5);
    // linha fina
    ctx.fillStyle = light ? 'rgba(255,255,255,0.35)' : 'rgba(27,27,27,0.25)';
    const w = ctx.measureText(label).width;
    ctx.fillRect(W / 2 - w / 2, H - size * 2.15, w, Math.max(2, size * 0.05));
  }

  function drawWatermark(ctx, W, H, bg) {
    ctx.save();
    ctx.globalAlpha = 0.55;
    ctx.font = `600 ${Math.round(W * 0.026)}px ${FONT_SANS}`;
    ctx.textAlign = 'right';
    ctx.textBaseline = 'bottom';
    ctx.fillStyle = isLight(bg) ? 'rgba(27,27,27,0.6)' : 'rgba(255,255,255,0.6)';
    ctx.fillText('@professorcinza', W - W * 0.045, H - W * 0.032);
    ctx.restore();
  }

  function drawCoverSlide(ctx, car, i, total, opts) {
    const W = ctx.canvas.width;
    const H = ctx.canvas.height;
    const color = opts.color;
    const light = isLight(color);

    // fundo com gradiente
    const g = ctx.createLinearGradient(0, 0, W, H);
    g.addColorStop(0, color);
    g.addColorStop(1, shade(color, 0.78));
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, W, H);

    const pad = W * 0.08;
    const logoSize = W * 0.13;
    drawLogo(ctx, pad, pad, logoSize);

    ctx.fillStyle = light ? 'rgba(27,27,27,0.7)' : 'rgba(255,255,255,0.85)';
    ctx.font = `700 ${Math.round(W * 0.05)}px ${FONT_SANS}`;
    ctx.textAlign = 'right';
    ctx.textBaseline = 'middle';
    ctx.fillText(`CARROSSEL ${i + 1}/${total}`, W - pad, pad + logoSize / 2);

    // título
    ctx.fillStyle = light ? '#1b1b1b' : '#fff';
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
    ctx.fillStyle = light ? 'rgba(27,27,27,0.75)' : 'rgba(255,255,255,0.9)';
    y += W * 0.04;
    wrapText(ctx, car.tagline, W - pad * 1.5).forEach((ln) => {
      ctx.fillText(ln, W / 2, y);
      y += W * 0.05;
    });

    // dados_chave como chips (empilham em linhas quando faltar espaço)
    const chips = String(car.dados_chave || '').split(/[·;]/).map((s) => s.trim()).filter(Boolean).slice(0, 3);
    if (chips.length) {
      const maxW = W - pad * 2;
      ctx.font = `600 ${Math.round(W * 0.032)}px ${FONT_SANS}`;
      const chipH = W * 0.075;
      const gapX = W * 0.02;
      const gapY = W * 0.03;
      const widths = chips.map((c) => Math.min(ctx.measureText(c).width + W * 0.05, maxW));
      // empacota em linhas de largura <= maxW
      const rows = [];
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

      y += W * 0.05;
      rows.forEach((r, ri) => {
        const rw = widths.reduce((a, ci) => a + widths[ci], 0) + gapX * (r.length - 1);
        let x = W / 2 - rw / 2;
        const cy = y + ri * (chipH + gapY);
        r.forEach((ci) => {
          ctx.fillStyle = light ? 'rgba(255,255,255,0.55)' : 'rgba(255,255,255,0.16)';
          roundRect(ctx, x, cy - chipH / 2, widths[ci], chipH, chipH / 2);
          ctx.fill();
          ctx.fillStyle = light ? '#1b1b1b' : '#fff';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillText(chips[ci], x + widths[ci] / 2, cy + 1);
          x += widths[ci] + gapX;
        });
      });
    }

    drawHandleFooter(ctx, W, H, color, light);
    drawWatermark(ctx, W, H, color);
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

    ctx.fillStyle = '#fffdf8';
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
      ctx.fillStyle = isLight(color) ? '#1b1b1b' : '#fff';
      ctx.textAlign = 'left';
      ctx.textBaseline = 'middle';
      ctx.fillText(slide.pill, pad + W * 0.03, pad + W * 0.02 + ph / 2);
    }

    ctx.fillStyle = '#8a8377';
    ctx.font = `600 ${Math.round(W * 0.03)}px ${FONT_SANS}`;
    ctx.textAlign = 'right';
    ctx.textBaseline = 'middle';
    ctx.fillText(`CARROSSEL ${i + 1}/${total}`, W - pad, pad);

    // blocos de conteúdo
    const blocks = [];
    if (slide.titulo) blocks.push({ text: slide.titulo, size: W * 0.062, weight: 700, family: FONT_DISP, fill: '#1b1b1b', lh: 1.14, gap: W * 0.015 });
    if (slide.stat) blocks.push({ text: slide.stat, size: W * 0.135, weight: 700, family: FONT_DISP, fill: color, lh: 1.08, gap: W * 0.005 });
    if (slide.statLabel) blocks.push({ text: slide.statLabel, size: W * 0.036, weight: 700, family: FONT_SANS, fill: '#1b1b1b', lh: 1.15, gap: W * 0.012 });
    if (slide.texto) blocks.push({ text: slide.texto, size: W * 0.038, weight: 500, family: FONT_SANS, fill: '#5c574f', lh: 1.28, gap: W * 0.014 });
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

    // desenha
    let y = bodyTop;
    ctx.textAlign = 'left';
    ctx.textBaseline = 'top';
    for (const b of blocks) {
      const size = Math.round(b.size * scale);
      ctx.fillStyle = b.fill;
      ctx.font = `${b.weight} ${size}px ${b.family}`;
      const lines = wrapText(ctx, b.text, maxW);
      for (const ln of lines) {
        ctx.fillText(ln, pad, y);
        y += size * b.lh;
      }
      if (lines.length) y += b.gap * scale;
    }

    // rodapé: handle + logo
    ctx.fillStyle = isLight(color) ? 'rgba(27,27,27,0.06)' : 'rgba(27,27,27,0.08)';
    ctx.fillRect(0, H - footerH, W, footerH);
    drawLogo(ctx, pad, H - footerH / 2 - W * 0.05, W * 0.1);
    ctx.fillStyle = '#8a8377';
    ctx.font = `700 ${Math.round(W * 0.035)}px ${FONT_DISP}`;
    ctx.textAlign = 'right';
    ctx.textBaseline = 'middle';
    ctx.fillText(normalizeHandle(state.handle), W - pad, H - footerH / 2);
    drawWatermark(ctx, W, H, '#fffdf8');
  }

  function drawCtaSlide(ctx, car, i, total, opts) {
    const W = ctx.canvas.width;
    const H = ctx.canvas.height;
    const color = opts.color;
    const light = isLight(color);

    const g = ctx.createLinearGradient(0, 0, W, H);
    g.addColorStop(0, color);
    g.addColorStop(1, shade(color, 0.78));
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, W, H);

    const cx = W / 2;
    const pad = W * 0.08;
    const logoSize = W * 0.2;
    drawLogo(ctx, cx - logoSize / 2, H * 0.14, logoSize);

    drawPage(ctx, `CARROSSEL ${i + 1}/${total}`, cx, H * 0.11);

    ctx.fillStyle = light ? '#1b1b1b' : '#fff';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

    ctx.font = `600 ${Math.round(W * 0.045)}px ${FONT_SANS}`;
    ctx.fillText('SIGA E COMPARTILHE', cx, H * 0.5);

    ctx.font = `700 ${Math.round(W * 0.09)}px ${FONT_DISP}`;
    ctx.fillText(normalizeHandle(state.handle), cx, H * 0.62);

    ctx.font = `500 ${Math.round(W * 0.034)}px ${FONT_SANS}`;
    ctx.fillStyle = light ? 'rgba(27,27,27,0.7)' : 'rgba(255,255,255,0.85)';
    ctx.fillText('SALVE · COMPARTILHE · ESPALHE', cx, H * 0.74);

    drawHandleFooter(ctx, W, H, color, light);
    drawWatermark(ctx, W, H, color);
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
    const car = CARROSSEIS.find((c) => c.id === id);
    if (!car) return;
    if (document.fonts && document.fonts.ready) await document.fonts.ready;
    const opts = { color: state.colors[id] || car.cor };
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

  /* -------------------- Galeria -------------------- */

  function cardHTML(car) {
    const color = state.colors[car.id] || car.cor;
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

  function renderGallery() {
    const grid = $('#carr-grid');
    if (!grid) return;
    grid.innerHTML = CARROSSEIS.map(cardHTML).join('');

    // previews (cover em tamanho reduzido)
    CARROSSEIS.forEach((car) => {
      const canvas = $(`[data-canvas="${car.id}"]`, grid);
      if (!canvas) return;
      const opts = { color: state.colors[car.id] || car.cor };
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
        renderGallery();
      });
    });
  }

  /* -------------------- Painel de customização -------------------- */

  function restoreDefaults() {
    state.handle = '@seuperfil';
    state.logo = null;
    state.logoData = '';
    state.format = 'square';
    state.colors = {};
    ls.set('handle', state.handle);
    ls.set('logo', '');
    ls.set('format', 'square');
    ls.set('colors', '');
    const handle = $('#carr-handle');
    if (handle) handle.value = state.handle;
    const format = $('#carr-format');
    if (format) format.value = state.format;
    renderGallery();
  }

  function bindPanel() {
    const handle = $('#carr-handle');
    if (handle) {
      handle.value = state.handle;
      handle.addEventListener('input', () => {
        state.handle = normalizeHandle(handle.value);
        ls.set('handle', state.handle);
        renderGallery();
      });
    }

    const logo = $('#carr-logo');
    if (logo) {
      logo.addEventListener('change', () => {
        const file = logo.files && logo.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = (e) => {
          const img = new Image();
          img.onload = () => {
            state.logo = img;
            state.logoData = String(e.target.result);
            ls.set('logo', state.logoData);
            renderGallery();
          };
          img.src = String(e.target.result);
        };
        reader.readAsDataURL(file);
      });
    }

    const logoClear = $('#carr-logo-clear');
    if (logoClear) {
      logoClear.addEventListener('click', () => {
        state.logo = null;
        state.logoData = '';
        ls.set('logo', '');
        if (logo) logo.value = '';
        renderGallery();
      });
    }

    const format = $('#carr-format');
    if (format) {
      format.value = state.format;
      format.addEventListener('change', () => {
        state.format = format.value;
        ls.set('format', state.format);
        renderGallery();
      });
    }

    const reset = $('#carr-reset');
    if (reset) reset.addEventListener('click', restoreDefaults);
  }

  function restoreLogo() {
    if (!state.logoData) return;
    const img = new Image();
    img.onload = () => {
      state.logo = img;
      renderGallery();
    };
    img.src = state.logoData;
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
    renderGallery();
    restoreLogo();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  window.CAROUSEL_SITE = {
    buildZip,
    crc32,
    renderSlide,
    getState: () => state,
  };
})();
