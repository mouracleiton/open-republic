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

const UP_LOGO_PATHS = ["M24.7,35.3c33.2,0,65.6,0,98.6,0c0,1.8,0,3.3,0,4.9c0.1,23.7,0.1,47.4,0.2,71.1\r\n\t\t\t\tc0.1,59.1,0.2,118.3,0.4,177.4c0.2,54.4,0.4,108.7,0.6,163.1c0,10.4,3.2,13.5,13.6,13.5c10,0,19.9-0.1,29.9,0.1\r\n\t\t\t\tc4.6,0.1,7.2-2,8-6.3c0.6-3.1,0.9-6.3,0.9-9.5c0-135.4,0-270.9,0-406.3c0-2.5,0-5.1,0-8c33.1,0,65.7,0,99.2,0c0,2.5,0,5,0,7.5\r\n\t\t\t\tc0,98.2,0,196.4,0,294.6c0,51.2,0.2,102.4,0.2,153.5c0,29.6-18.1,55.9-44.7,63.1c-9.6,2.6-20.1,2.5-30.1,2.6\r\n\t\t\t\tc-20.1,0.2-40.2-0.4-60.3-0.7c-19.7-0.3-39.4-0.4-59.1-0.8c-28.2-0.6-53.6-25.2-56.7-55c-0.4-3.4-0.6-6.7-0.6-10.1\r\n\t\t\t\tc0-149,0-297.9,0-446.9C24.7,40.6,24.7,38.2,24.7,35.3z","M294.5,35c3.2,0,5.6,0,8,0c55.6,0,111.1,0.5,166.7-0.2c25.6-0.3,49.3,18.2,54.5,46.6\r\n\t\t\t\tc0.8,4.5,1.1,9.1,1.1,13.7c0.1,86,0.1,172,0,258.1c0,23.6-8.8,43-29.2,56.2c-9.5,6.1-20,8.4-31.2,8.4c-28.3,0-56.5,0.2-84.8,0.4\r\n\t\t\t\tc-2,0-3.9,0-6.4,0c0,46.5,0,92.4,0,138.8c-32.3,0-64,0-96.6,0c0.5-7.6-1.5-14.9,4.3-22.6c10.4-13.6,12-30.4,13.4-47\r\n\t\t\t\tc0.4-4.6,0.3-9.2,0.3-13.7c0-143.4,0-286.7,0-430.1C294.5,40.9,294.5,38.4,294.5,35z M372,330.2c14.9,0,29.4,0,43.9,0\r\n\t\t\t\tc11.9,0,14-2,14-13.8c0-58.1,0-116.2,0-174.3c0-2.4,0-4.8-0.5-7.1c-0.9-4.5-3.6-8.1-8.3-8.2c-16.3-0.3-32.5-0.1-49.1-0.1\r\n\t\t\t\tC372,194.5,372,261.9,372,330.2z","M607.2,553.5c-29.8,0-59.2,0-89.6,0c32.4-94.2,64.8-188,97.2-282.1c2.3,1.3,4.1,2.4,7.3,4.3\r\n\t\t\t\tc-2-4.5-3.4-7.8-4.9-11c-13.6-30.1-27.1-60.2-40.9-90.1c-1.9-4.2-2.6-8.1-0.5-11.9c6.3-11.7,12.5-23.4,19.7-34.6\r\n\t\t\t\tc8.8-13.7,18.6-26.8,27.8-40.3c5.4-7.9,10.7-9,18.4-3.2c5.4,4.1,10.7,8.3,16.1,12.4c0.3,0.2,0.4,0.6,0.6,0.9\r\n\t\t\t\tc-1.5,2.2-3,4.5-4.6,6.7c0.2,0.4,0.5,0.8,0.7,1.1c1.8-0.5,4.1-0.4,5.2-1.5c3.9-4.2,7.8-2.8,11.9-0.8c6.8,3.3,13.5,6.7,20.4,9.8\r\n\t\t\t\tc3.6,1.6,4.3,4,3.7,7.6c-2.8,17.9-14.7,26.8-33.7,24.9c-12.9-1.3-23.8-6-31.2-17.3c-1.6-2.4-3.9-4.3-6-6.5c-4.1,6-4,10,0.3,15.1\r\n\t\t\t\tc2.6,3,5.6,5.7,8.3,8.6c5.8,6.3,6.1,8.9,1.7,16.3c-2.9,4.8-6.2,9.3-9.2,13.9c-1.3,2.1-2.4,4.4-3.6,6.6c0.6,0.5,1.2,1.1,1.8,1.6\r\n\t\t\t\tc3.5-3.4,7.2-6.6,10.4-10.2c2.7-3.1,4.7-6.9,7.2-10.2c0.7-0.9,2.3-1.1,3.4-1.7c0.5,1.3,1.7,2.8,1.5,4c-1.2,6.8-2.8,13.6-4.1,20.5\r\n\t\t\t\tc-0.5,2.5-0.6,5-0.9,7.5c0.6,0.3,1.2,0.6,1.9,0.9c1.9-3.2,4.2-6.2,5.7-9.6c4.1-9.4,4.6-9.7,13.9-5.3c5.9,2.8,10.5,6.8,13.8,12.7\r\n\t\t\t\tc15.2,27.3,18,56.5,13.6,86.8c-0.2,1.3-0.7,2.6-1.2,4.9c-4.2-0.8-8.2-1.5-12.2-2.5c-3.1-0.7-6.1-1.9-9.2-2.5\r\n\t\t\t\tc-4.6-0.9-6.8,0.5-7,5.8c-0.7,15.5-2.1,30.9-2.2,46.7c4-12.9,8.1-25.8,12.2-39c5.5,1.1,10.7,2,15.8,3.3c4.7,1.2,6.8-0.8,8.6-4.8\r\n\t\t\t\tc4.7-11.1,6-22.7,5.6-34.5c-0.4-11.5-2-22.9-3.1-35.2c5.5,0.6,11.4,1.3,17.9,2.1c0-4,0-7.8,0-13.3c8.8,10.2,16.5,19,24.2,27.8\r\n\t\t\t\tc0.5-0.4,1-0.7,1.5-1.1c0.7-9.5-6.7-16.5-8.6-25.5c6.2-4.3,12.7-6.3,20.1-3.2c7,2.9,13.9,2.5,20.6-1.4c6.5-3.7,13.4-6.9,21.4-11\r\n\t\t\t\tc-1.8,7.6-3.2,14-4.8,20.2c-6.7,25.4-14.9,50.3-27.2,73.7c-7.9,14.9-18.7,26.4-36.3,29c-5.2,0.8-10.6,0.1-16.5,1.4\r\n\t\t\t\tc7,2.6,14.1,5.2,22.1,8.1c-18.6,74.5-37.3,149.6-56.1,225c-11.5,0-22.7,0-34.8,0c3.2-14.5,6-28.8,9.6-42.8\r\n\t\t\t\tc14.1-54.3,28.5-108.4,42.6-162.7c0.9-3.5,0.8-7.3,1.2-11c-0.7-0.1-1.4-0.2-2.1-0.3c-2.9,10.6-5.9,21.2-8.7,31.8\r\n\t\t\t\tc-16.1,59.5-32.2,119-48,178.5c-1.5,5.5-3.8,7.5-9.3,6.8c-4.1-0.5-8.3-0.1-13.4-0.1c17.7-68,35.4-135.5,53-203\r\n\t\t\t\tc-0.6-0.2-1.1-0.3-1.7-0.5C645.5,418,626.3,485.7,607.2,553.5z","M910.9,400.4c1.9,0.9,3.1,1.5,4.6,2.2c-0.1-0.9,0-1.5-0.3-2c-11.2-24.2-22.5-48.3-33.5-72.5\r\n\t\t\t\tc-1.2-2.7-1.6-6.9-0.4-9.5c3.6-7.7,7.7-15.3,12.4-22.3c7.6-11.4,15.9-22.4,23.9-33.5c4.3-6.1,8-6.7,14-2.4\r\n\t\t\t\tc4.3,3.2,8.6,6.4,13,9.7c-1.1,1.9-2.1,3.5-3.2,5.3c0.8,0.4,1.6,0.9,1.8,0.8c5.9-5.6,11.3-1.5,16.8,0.8c1.3,0.5,2.7,1,3.7,1.8\r\n\t\t\t\tc3.3,2.4,8.9,4.8,9.1,7.6c0.5,7-2.4,13.7-9.4,17.3c-12,6.2-30.1,2.2-38.6-8.4c-1.8-2.3-3.8-4.4-6-6.9c-3.7,5-2.3,8.8,0.9,12.2\r\n\t\t\t\tc10.9,11.7,10.9,11.7,2.1,24.9c-1.7,2.6-3.3,5.3-5.4,8.8c10.1-1.8,10.6-13.2,20-16.9c-1.8,9.2-3.3,16.9-4.9,24.7\r\n\t\t\t\tc0.6,0.3,1.2,0.5,1.8,0.8c2.5-4.3,5-8.6,7.6-13.2c7.1,1.6,13.5,4.3,17.4,11c11.9,20.4,14.3,42.3,11.1,65.2\r\n\t\t\t\tc-0.6,4-2.8,4.2-5.9,3.5c-5.3-1.2-10.6-2.3-16.5-3.6c-1,13.4-1.9,25.4-2.8,37.5c0.4,0.1,0.7,0.2,1.1,0.3c2.9-9,5.9-18,8.9-27.2\r\n\t\t\t\tc2.3,0.5,4.2,1,6.1,1.4c10.7,2.6,12.1,1.9,14.8-9c3.5-13.8,2.2-27.7-0.1-41.5c-0.2-1.2-0.4-2.3-0.6-4.1c4.7,0.5,9.2,0.9,14,1.4\r\n\t\t\t\tc0-2.9,0-5.6,0-10c6.9,7.6,12.9,14.1,18.8,20.6c0.6-0.4,1.3-0.8,1.9-1.3c-2.4-5.9-4.8-11.8-7.4-18.2c4.2-2.8,8.5-5.1,13.7-3.1\r\n\t\t\t\tc7.3,2.9,13.9,2.1,20.5-1.9c4-2.4,8.3-4.2,13.7-6.8c-6.6,27.3-13.7,52.9-28.1,75.7c-8.4,13.3-19.8,17.9-36.3,17.5\r\n\t\t\t\tc5.1,1.9,10.2,3.8,16.1,5.9c-7.8,36.5-15.6,73.3-23.5,110.4c-8.7,0-17.2,0-26.6,0c1.9-10.1,3.4-20,5.6-29.8\r\n\t\t\t\tc4.9-22.1,10-44.2,15-66.3c0.6-2.5,0.5-5.1,0.8-7.6c-0.6-0.1-1.1-0.1-1.7-0.2c-8.5,34.7-17,69.3-25.5,104.1\r\n\t\t\t\tc-29.8,0-59.3,0-89.6,0C874.2,502.4,892.4,451.7,910.9,400.4z","M765.4,343.9c0.5,2.6,0.4,5.4,1.5,7.7c1,2.1,3,3.7,4.8,5.2c4.5,3.7,4.2,7.7,1.2,12\r\n\t\t\t\tc-2.4,3.5-4.7,7.1-7.1,10.7c0.6,0.5,1.2,1,1.8,1.5c3.8-4.5,7.7-9.1,11.5-13.6c0.6,0.2,1.2,0.4,1.8,0.6c-1.1,6.3-2.1,12.7-3.2,19\r\n\t\t\t\tc0.5,0.2,1,0.4,1.5,0.6c1.3-2.4,2.8-4.8,3.9-7.3c1.3-2.9,3.1-4.3,5.9-2.3c3.7,2.8,8.3,5.2,10.6,9c10.5,17.4,11.6,36.4,8.2,56.9\r\n\t\t\t\tc-5.8-1.2-11.2-2.3-17.7-3.6c-0.8,10.9-1.6,21-2.4,31.1c0.3,0.1,0.6,0.1,0.9,0.2c2.3-7.3,4.7-14.6,7.1-22.2\r\n\t\t\t\tc1.3,0.1,2.5,0.1,3.5,0.4c11,2.6,12.6,2.2,14-9.1c1.2-9.5,0.3-19.4,0.1-29.1c0-2-0.6-3.9-1-6.6c3.9,0.3,7.3,0.6,11.1,0.9\r\n\t\t\t\tc0.2-2.4,0.3-4.6,0.6-8c5.6,6.3,10.4,11.7,15.1,17.1c0.5-0.3,1-0.6,1.6-0.9c-1.9-5-3.8-10-6.2-16.3c3.9-0.7,7.8-2.6,10.6-1.5\r\n\t\t\t\tc7.6,2.8,14,0.9,20.4-2.9c2.4-1.4,4.9-2.5,8.9-4.5c-2.4,9-4,16.7-6.7,24c-4.3,11.9-8.8,23.9-14.4,35.3\r\n\t\t\t\tc-6.1,12.5-16.3,19.4-31,17.4c-0.2,0.5-0.3,1-0.5,1.4c4,1.4,8,2.8,12.7,4.4c-6.9,27.2-13.8,54.5-20.8,82.1c-7.1,0-14,0-21.9,0\r\n\t\t\t\tc6.6-25.4,13.1-50.6,19.6-75.7c-0.7-0.2-1.4-0.4-2.1-0.5c-7.4,25.4-14.8,50.7-22.2,76.2c-4.4,0-8.4,0-13,0\r\n\t\t\t\tc2.3-8.6,4.4-16.7,6.6-24.9c-0.4-0.1-0.8-0.2-1.1-0.3c-2.1,7.2-4,14.4-6.4,21.5c-0.6,1.7-3,3.8-4.5,3.8\r\n\t\t\t\tc-16.1,0.3-32.2,0.2-49.2,0.2c1-3,1.7-5.5,2.6-8c12.2-34.9,24.3-69.8,36.6-104.7c0.7-1.9,2.4-3.4,4.5-6.2\r\n\t\t\t\tc-8-17.5-16.6-36.7-25.7-55.7c-2.7-5.7-2.9-10.7,0.2-15.7c5.8-9.2,12-18.3,18.1-27.4c3.3-5,6.8-9.8,10.2-14.7\r\n\t\t\t\tc3.3-4.7,6.4-5.3,11.1-1.9c3.6,2.5,7,5.3,10.7,8.2c-0.8,1.5-1.6,3-2.4,4.5c0.6,0.2,1.2,0.6,1.3,0.5c4.5-4,8.8-1.8,13.1,0.4\r\n\t\t\t\tc1.2,0.6,2.7,1,3.7,1.8c2.8,2.1,7.5,4.3,7.6,6.7c0.3,5.7-2.1,11.3-8,14.2c-9.8,4.8-24.1,1.8-31-6.7c-1.6-2-3.3-3.8-5-5.7\r\n\t\t\t\tC766.6,343.5,766,343.7,765.4,343.9z","M686.1,103.2c4.5-10.9,8.5-21.3,13-31.3c2.3-5.2,6.8-7.4,12.3-4.8c7.9,3.7,15.6,7.7,23.5,11.5\r\n\t\t\t\tc5.8,2.8,6.9,7.5,4.8,13c-7.9,20.3-15.9,40.6-24.2,60.8c-2.6,6.2-5.9,12.2-9.1,18c-3.8,6.9-9.3,9.4-17,7.5\r\n\t\t\t\tc-7.3-1.8-14.3-4.6-21.6-6.6c-5.5-1.5-6.5-4.9-5.5-9.9c1.1-5.7,4.5-9.2,10-10.5c2.9-0.7,5.9-0.7,8.8-1.3c7-1.5,12.7-5,15.3-11.9\r\n\t\t\t\tc2.4-6.3,4.2-12.8,6.3-19.2c1.3-4.1,0-6.6-4.1-8.4C694.5,108.3,690.7,105.8,686.1,103.2z","M706,183.8c6.7-14.7,13.3-29.3,19.9-43.9c4.7-10.5,9.3-21,14-31.5c1.1-2.5,2.2-5.1,3.8-7.4\r\n\t\t\t\tc4.8-7.1,10.2-8.2,17.2-3.2c5.8,4.1,11.3,8.8,17,13.1c3.9,3,4.8,6.5,2.6,10.9c-6.2,12-12.2,24.1-18.5,36\r\n\t\t\t\tc-5.4,10.2-11,20.2-16.7,30.3c-4.1,7.2-7.7,8.1-15.3,4.9C722.7,189.9,715.2,187.3,706,183.8z","M981.3,334.8c4-9.1,7.9-18,11.9-26.8c4.6-10.1,9.6-20.1,14-30.2c4.7-10.6,9.8-12.4,19.1-5.5\r\n\t\t\t\tc16.3,12.1,15.8,9.4,6.5,27.2c-6.6,12.7-13.9,25-21,37.4c-3.8,6.7-6,7.2-13.1,4.3C993.4,339.1,988,337.3,981.3,334.8z","M794.3,191.5c1-6.4,2-12.7,3-19.1c-0.3-0.1-0.6-0.2-0.9-0.4c-3.9,7.3-8,14.5-11.5,21.9\r\n\t\t\t\tc-1.6,3.5-3.9,4.2-7.1,3.4c-2.9-0.7-5.8-1.5-8.5-2.7c-12.2-5.4-14.2-12-7.6-23.6c7.7-13.7,15-27.6,22.8-41.2\r\n\t\t\t\tc3.7-6.4,5.8-6.4,11.5-1.4c3.1,2.7,6.4,5.3,9.4,8.2c0.9,0.8,1.7,2.4,1.5,3.4c-3.4,17.3-7.1,34.5-10.6,51.7\r\n\t\t\t\tC795.7,191.7,795,191.6,794.3,191.5z","M984.5,244.6c8.4,5.1,16.1,9.4,23.2,14.6c1.2,0.9,0.6,5.8-0.5,8.3c-6.7,14.4-13.6,28.7-20.7,42.9\r\n\t\t\t\tc-2.9,5.9-6.4,11.4-9.3,17.3c-1.6,3.3-3.9,4.4-7.1,3.3c-4.5-1.4-9.2-2.6-13.4-4.8c-2.2-1.1-5.1-4.4-4.8-6.2\r\n\t\t\t\tc0.6-3.3,3.2-6.3,5.4-9.1c0.7-0.9,2.5-1,3.9-1.1c9.4-0.5,14.9-5.6,17.3-14.5c0.5-1.7,1-3.4,1.6-5.1c2.3-5.9,1.4-10.3-5.2-12.4\r\n\t\t\t\tc-5.5-1.7-6-5-3.5-9.9c2.5-4.9,3.9-10.4,6.4-15.4C979.1,249.9,981.6,247.9,984.5,244.6z","M818.1,381.5c4-8.9,8-17.7,12-26.5c3.1-6.9,6.4-13.7,9.2-20.6c3.7-8.9,8.2-10.4,15.9-4.8\r\n\t\t\t\tc12.6,9,12.7,9.1,5.4,22.7c-5.5,10.4-11.4,20.5-17,30.8c-2.8,5.2-6.3,6.5-11.7,3.7C827.9,384.6,823.5,383.5,818.1,381.5z","M808.2,331.3c2.7-6.8,5.1-13.2,7.7-19.6c1.5-3.6,4.7-4.3,8-2.8c4.8,2.3,9.8,4.5,14,7.8\r\n\t\t\t\tc1.7,1.4,2.7,6.1,1.7,8.2c-8.1,17.2-16.6,34.2-25.2,51.2c-0.6,1.2-2.9,2.4-4.1,2.1c-4-0.8-8.1-1.9-11.8-3.7c-2-1-4.6-4.1-4.3-5.8\r\n\t\t\t\tc0.4-2.7,3-5,4.9-7.4c0.4-0.5,1.4-0.6,2.2-0.8c11-2.5,16.5-9.3,16.8-20.8c0-1.2-1-2.9-2-3.7C813.9,334.4,811.4,333.1,808.2,331.3\r\n\t\t\t\tz","M693.1,66.1c1,11.6-2.7,21.1-8.1,30c-0.7,1.1-3.4,2-4.7,1.5c-14-4.8-25.7-13.1-35.6-24.1\r\n\t\t\t\tc-2.2-2.4-1.5-4.1,0.5-6c5.5-5.1,11.6-8.1,19.4-6.6C673.9,62.8,683.3,64.4,693.1,66.1z","M1049.2,340.1c0.6-4.4,1.3-8.7,1.9-13.1c-0.3-0.1-0.6-0.2-0.8-0.3c-2.6,4.8-5.4,9.5-7.7,14.5\r\n\t\t\t\tc-1.6,3.4-3.8,4.5-7.1,3.3c-3.5-1.3-7.1-2.6-10.2-4.5c-4.6-2.9-5.5-7.2-2.9-11.9c6.4-11.4,13-22.8,19.4-34.2\r\n\t\t\t\tc2.3-4.2,5-3.8,8.1-1.1c3,2.6,6,5.2,9.4,8.2c-2.8,12.8-5.7,26.1-8.5,39.4C1050.2,340.3,1049.7,340.2,1049.2,340.1z","M873.8,385.9c0.4-3.1,0.8-6.2,1.3-9.2c-0.3-0.2-0.6-0.3-0.9-0.5c-1.8,3.3-3.8,6.5-5.2,9.9\r\n\t\t\t\tc-1.7,4-4.3,4.5-8.1,3.3c-10.3-3.2-12.2-7.8-6.9-17.3c4.5-8,8.9-15.9,13.3-24c2.3-4.2,4.5-3.4,7.9-1c5.9,4,7.3,8.5,5.1,15.4\r\n\t\t\t\tc-2.5,7.7-3.5,15.8-5.1,23.7C874.7,386.1,874.2,386,873.8,385.9z","M931.8,250.9c4.5-6.3,9.5-9.1,15.9-8.3c6.7,0.8,13.4,2,19.9,3.5c1.4,0.3,2.5,2.7,3.5,4.2\r\n\t\t\t\tc0.3,0.5,0,1.5-0.1,2.3c-1.8,18.2-7.4,21.2-22.5,11.5C942.7,260.4,937.5,255.4,931.8,250.9z","M777.7,311.7c4.2-5.9,8.8-7.8,14.7-6.8c4.7,0.8,9.5,1.3,14,2.7c1.6,0.5,2.5,2.9,3.7,4.6\r\n\t\t\t\tc0.2,0.2-0.1,0.8-0.1,1.2c-2.1,15.4-6.4,17.5-19.1,9.1C786.3,319.4,782.3,315.5,777.7,311.7z"];

  function drawUpLogo(ctx, x, y, w, h, fill) {
    ctx.save();
    ctx.translate(x, y);
    ctx.scale(w / 1080, h / 592.1);
    ctx.fillStyle = fill;
    for (let i = 0; i < UP_LOGO_PATHS.length; i++) {
      ctx.fill(new Path2D(UP_LOGO_PATHS[i]));
    }
    ctx.restore();
  }

  const FONT_DISP = '"Space Grotesk", Inter, system-ui, sans-serif';
  const UP_RED = '#C00810';
  const FONT_SANS = 'Inter, system-ui, sans-serif';

  function drawLogo(ctx, x, y, size, bg) {
    // wordmark da Unidade Popular (adaptativo ao fundo)
    drawUpLogo(ctx, x, y, size * (1080 / 592.1), size, isLight(bg || '#000') ? UP_RED : '#fff');
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
    const car = CARROSSEIS.find((c) => c.id === id);
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

  function renderGallery() {
    const grid = $('#carr-grid');
    if (!grid) return;
    grid.innerHTML = CARROSSEIS.map(cardHTML).join('');

    // previews (cover em tamanho reduzido)
    CARROSSEIS.forEach((car) => {
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
        renderGallery();
      });
    });
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
