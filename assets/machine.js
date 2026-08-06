/* ============================================================
   Máquina de propaganda — WhatsApp, X, mensagens, áudio e prompts
   Tudo client-side, sem upload. Usa CARROSSEIS e CAROUSEL_SITE.
   ============================================================ */

'use strict';

(function () {
  const $ = (sel, el = document) => el.querySelector(sel);
  const $$ = (sel, el = document) => Array.from(el.querySelectorAll(sel));

  const LS_PREFIX = 'mg_';
  const PR_KEY = LS_PREFIX + 'prompts';

  const esc = (s) =>
    String(s).replace(/[&<>"']/g, (c) => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;',
    }[c]));

  function normHandle(v) {
    let s = String(v || '').trim().replace(/\s+/g, '');
    if (!s) s = '@seuperfil';
    if (s.charAt(0) !== '@') s = '@' + s;
    return s;
  }

  function currentHandle() {
    const st = window.CAROUSEL_SITE && window.CAROUSEL_SITE.getState && window.CAROUSEL_SITE.getState();
    if (st && st.handle) return st.handle;
    const h = $('#carr-handle');
    return h ? h.value : '@seuperfil';
  }

  function facts(car) {
    return String(car.dados_chave || '').split(/[·;]/).map((s) => s.trim()).filter(Boolean);
  }

  function trunc280(s) {
    if (s.length <= 280) return s;
    return s.slice(0, 277).replace(/\s+\S*$/, '') + '…';
  }

  /* -------------------- Mensagens -------------------- */

  function waMessages(car, handle) {
    return [
      {
        label: 'Compartilhar',
        text: `📊 ${car.nome}\n\n${car.tagline}\n\n🔎 ${car.dados_chave}\n\nFonte: dados públicos oficiais.\n👉 Siga ${handle} e compartilhe.`,
      },
      {
        label: 'Provocação',
        text: `Essa pergunta precisa ser feita: o que o outro partido fez ou vai fazer pra resolver isso?\n\n${car.dados_chave}\n\nO nosso lado está no ${handle}. Espalhe. 🔥`,
      },
      {
        label: 'Encaminhar',
        text: `Encaminha isso pra quem precisa ler 👇\n\n${car.nome}: ${car.dados_chave}\n\nSiga ${handle} pra ver os números e o nosso lado.`,
      },
    ];
  }

  function xMessages(car, handle) {
    const dados = facts(car).slice(0, 3).join(' · ');
    return [
      {
        label: 'Tweet 1',
        meta: `${280 - trunc280(`${car.nome}: ${dados}\n\nO que o outro partido fez ou vai fazer pra resolver isso?\n\n${handle}`).length} caracteres restantes`,
        text: trunc280(`${car.nome}: ${dados}\n\nO que o outro partido fez ou vai fazer pra resolver isso?\n\n${handle}`),
      },
      {
        label: 'Tweet 2',
        text: trunc280(`${dados}\n\nNão é opinião, é dado público.\n\n${handle}`),
      },
      {
        label: 'Tweet 3',
        text: trunc280(`"${car.tagline}" — ${car.nome}.\n\n${dados}\n\nSiga ${handle}.`),
      },
    ];
  }

  function msgMessages(car, handle) {
    return [
      {
        label: 'Mensagem pessoal',
        text: `Oi! Preciso te mostrar uma coisa. Sabe que ${car.dados_chave}? Pois é, é dado público, não opinião minha.\n\nQuem explica direitinho e traz o nosso lado é o ${handle}. Dá uma olhada quando puder. 🙌`,
      },
      {
        label: 'Pro grupo',
        text: `Gente, achei um material foda sobre ${car.nome}.\n\n${car.dados_chave}\n\nA fonte é pública. Segue o ${handle}: eles mostram o lado da solução, não só o problema.`,
      },
      {
        label: 'Curta e direta',
        text: `${car.dados_chave}\n\nIsso é o Brasil em números. O outro lado promete resolver há décadas. Siga ${handle}.`,
      },
    ];
  }

  function audioTexts(car, handle) {
    return [
      { label: 'Resumo', text: `${car.nome}. ${car.tagline} ${car.dados_chave}. O outro partido fez ou vai fazer o quê pra resolver isso? Siga ${handle} e descubra o nosso lado.` },
      { label: 'Provocação', text: `O que o outro partido fez ou vai fazer pra resolver isso? ${car.dados_chave}. Não é opinião, é dado público. Siga ${handle}.` },
      { label: 'Convite', text: `Sabe quanto é o nosso problema? ${car.dados_chave}. Siga ${handle} pra ver os números e a nossa proposta.` },
    ];
  }

  /* -------------------- Prompts -------------------- */

  function buildPrompt(car, platform, duration, tone, handle) {
    if (platform === 'X (Twitter)') {
      return `Escreva 3 posts para X (Twitter) sobre: ${car.nome}.

Contexto: ${car.tagline}
Dados (fontes públicas oficiais): ${car.dados_chave}

Regras:
- Cada post com até 280 caracteres.
- Tom: ${tone}.
- Pelo menos um post com a pergunta "O que o outro partido fez ou vai fazer pra resolver isso?"
- Um post deve convidar a seguir ${handle}.

Formato de saída: lista numerada com os 3 posts.`;
    }
    return `Crie um roteiro de vídeo para ${platform} (${duration}) sobre: ${car.nome}.

Contexto: ${car.tagline}
Dados (todos de fontes públicas oficiais): ${car.dados_chave}

Público-alvo: brasileiro comum, mobile-first.
Tom: ${tone}.

Estrutura obrigatória:
1. Gancho nos primeiros 3 segundos — use a pergunta: "O que o outro partido fez ou vai fazer pra resolver isso?"
2. Até 3 dados impactantes, um por cena, com a fonte na tela.
3. Fechamento com convite para seguir ${handle}.

Inclua: narração off, legenda/sobreposição por cena, sugestão de trilha e transições.

Formato de saída: tabela com Cena | Visual | Áudio/Narração | Legenda.`;
  }

  function loadPrompts() {
    try { return JSON.parse(localStorage.getItem(PR_KEY) || '[]'); } catch (e) { return []; }
  }

  function savePrompts(list) {
    try { localStorage.setItem(PR_KEY, JSON.stringify(list)); } catch (e) { /* quota etc. */ }
  }

  /* -------------------- Clipboard -------------------- */

  function fallbackCopy(text, done) {
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); } catch (e) { /* noop */ }
    document.body.removeChild(ta);
    done();
  }

  function copyText(text, btn) {
    const done = () => {
      if (!btn) return;
      const prev = btn.textContent;
      btn.textContent = 'Copiado ✓';
      btn.classList.add('is-copied');
      setTimeout(() => { btn.textContent = prev; btn.classList.remove('is-copied'); }, 1400);
    };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done).catch(() => fallbackCopy(text, done));
    } else {
      fallbackCopy(text, done);
    }
  }

  /* -------------------- Dossiê contra -------------------- */

  const DOSSIER_BLOCKS = {
    patrimonio: ['Evolução patrimonial (declarada)', 'Questionamentos sobre patrimônio'],
    fundos: ['Doadores principais'],
    processos: ['Processos (TSE/TCU)', 'Lei da Ficha Limpa', 'Inquéritos e denúncias'],
    polemicas: ['Polêmicas', 'Denúncias', 'Inquéritos e denúncias'],
    glosas: ['Glosas e irregularidades'],
  };

  function cleanFact(t) {
    let s = String(t).trim().replace(/\s+/g, ' ');
    s = s.replace(/\s*Dados não disponíveis[^.]*\./gi, '').trim();
    s = s.replace(/^[-•]+\s*/, '');
    if (!s || /não disponíve/i.test(s)) return '';
    return s;
  }

  function dossierCards() {
    return $$('.doss-card').map((el) => ({ name: el.getAttribute('data-politico'), el }));
  }

  function dossierFacts(name, angle) {
    const card = dossierCards().find((c) => c.name === name);
    if (!card) return [];
    const out = [];
    (DOSSIER_BLOCKS[angle] || DOSSIER_BLOCKS.patrimonio).forEach((title) => {
      $$('.doss-block', card.el).forEach((block) => {
        const h = $('.doss-block-title', block);
        if (!h || !String(h.textContent).trim().startsWith(title)) return;
        $$('li, p', block).forEach((n) => {
          const f = cleanFact(n.textContent);
          if (f) out.push(f);
        });
      });
    });
    return out.slice(0, 6);
  }

  function shortenName(name) {
    const parts = String(name).split(' ').filter(Boolean);
    if (parts.length <= 2) return name;
    return `${parts[0]} ${parts[parts.length - 1]}`;
  }

  function dossierMessages(facts, name, handle) {
    const short = shortenName(name);
    const f1 = facts[0] || '';
    const f2 = facts[1] || '';
    return [
      {
        label: 'WhatsApp · oposição',
        text: `🚨 Antes de decidir, vale lembrar sobre ${short}:\n\n• ${f1}\n${f2 ? `• ${f2}` : ''}\n\nIsso é dado público, não fofoca. O outro lado teve décadas pra explicar.\n\n${handle}`,
      },
      {
        label: 'WhatsApp · pergunta',
        text: `O que ${short} fez ou vai fazer pra resolver isso?\n\n${f1}\n\nSiga ${handle} e confira os números.`,
      },
      {
        label: 'X (Twitter)',
        text: trunc280(`${short}: ${f1}\n\nFonte pública. Siga ${handle}.`),
      },
      {
        label: 'Mensagem pro grupo',
        text: `Gente, antes de votar vale conferir o histórico:\n\n${short}: ${f1} ${f2 ? f2 : ''}\n\nTudo de fontes públicas. Segue o ${handle}.`,
      },
    ];
  }

  function dossierPrompt(facts, name, platform, duration, tone, handle) {
    const short = shortenName(name);
    const factsList = facts.map((f) => `- ${f}`).join('\n');
    if (platform === 'X (Twitter)') {
      return `Escreva 3 posts de oposição sobre ${short} para X (Twitter).

Fatos verificados (fontes públicas oficiais):
${factsList}

Regras:
- Cada post com até 280 caracteres.
- Tom: ${tone}.
- Ao menos um post com a pergunta "O que ${short} fez ou vai fazer pra resolver isso?"
- Cite a fonte pública em cada post.
- Um post deve convidar a seguir ${handle}.

Formato de saída: lista numerada com os 3 posts.`;
    }
    return `Crie um roteiro de vídeo de oposição para ${platform} (${duration}) sobre: por que não eleger ${short}.

Fatos verificados (fontes públicas oficiais):
${factsList}

Público-alvo: eleitor comum, mobile-first.
Tom: ${tone}.

Estrutura obrigatória:
1. Gancho nos primeiros 3 segundos — "O que ${short} fez ou vai fazer pra resolver isso?"
2. Apresente 2-3 fatos, um por cena, com a fonte na tela.
3. Feche convidando a seguir ${handle}.

Inclua: narração off, legenda por cena, sugestão de trilha e transições.

Formato de saída: tabela com Cena | Visual | Áudio/Narração | Legenda.`;
  }

  /* -------------------- Render -------------------- */

  function renderList(sel, items) {
    const el = $(sel);
    if (!el) return;
    el.innerHTML = items.map((it, i) => `
      <article class="msg-card">
        <div class="msg-head">
          <span class="msg-label">${esc(it.label)}</span>
          ${it.meta ? `<span class="msg-meta">${esc(it.meta)}</span>` : ''}
        </div>
        <p class="msg-text">${esc(it.text)}</p>
        <div class="msg-actions">
          <button type="button" class="btn btn-ghost btn-copy" data-copy="${i}">Copiar</button>
        </div>
      </article>`).join('');
    el.querySelectorAll('[data-copy]').forEach((b) => {
      b.addEventListener('click', () => copyText(items[+b.getAttribute('data-copy')].text, b));
    });
  }

  function carById(id) {
    return (window.CARROSSEIS || []).find((c) => c.id === id) || (window.CARROSSEIS || [])[0];
  }

  function renderAll() {
    const handle = normHandle(currentHandle());
    renderList('#wa-list', waMessages(carById($('#wa-topic') && $('#wa-topic').value), handle));
    renderList('#x-list', xMessages(carById($('#x-topic') && $('#x-topic').value), handle));
    renderList('#msg-list', msgMessages(carById($('#msg-topic') && $('#msg-topic').value), handle));
    fillAudioTexts();
    renderPromptOut();
    renderSavedPrompts();
    renderDossier();
  }

  function fillTopicSelect(sel) {
    if (!sel || !window.CARROSSEIS) return;
    sel.innerHTML = window.CARROSSEIS.map((c) => `<option value="${esc(c.id)}">${esc(c.nome)}</option>`).join('');
  }

  function fillAudioTexts() {
    const topic = $('#au-topic');
    const textSel = $('#au-text');
    if (!topic || !textSel) return;
    const car = carById(topic.value);
    const texts = audioTexts(car, normHandle(currentHandle()));
    textSel.innerHTML = texts.map((t, i) => `<option value="${i}">${esc(t.label)}</option>`).join('');
  }

  function renderPromptOut() {    const out = $('#pr-out');
    if (!out) return '';
    const car = carById($('#pr-topic') && $('#pr-topic').value);
    out.value = buildPrompt(
      car,
      ($('#pr-platform') || {}).value || 'TikTok',
      ($('#pr-duration') || {}).value || '60s',
      (($('#pr-tone') || {}).value || '').trim() || 'direto, indignado com os números, mas esperançoso',
      normHandle(currentHandle())
    );
    return out.value;
  }

  function renderSavedPrompts() {
    const el = $('#pr-saved');
    if (!el) return;
    const list = loadPrompts();
    el.innerHTML = list.length
      ? list.map((p, i) => `
        <article class="msg-card">
          <div class="msg-head">
            <span class="msg-label">${esc(p.name || 'Sem nome')}</span>
            <span class="msg-meta">${esc(p.platform || '')} · ${esc(p.ts || '')}</span>
          </div>
          <p class="msg-text msg-text-sm">${esc(p.text)}</p>
          <div class="msg-actions">
            <button type="button" class="btn btn-ghost btn-copy" data-copy="${i}">Copiar</button>
            <button type="button" class="btn btn-ghost btn-del" data-del="${i}">Apagar</button>
          </div>
        </article>`).join('')
      : '<p class="caption">Nenhum prompt salvo ainda. Gere um prompt acima e clique em "Salvar no site".</p>';
    el.querySelectorAll('[data-copy]').forEach((b) => {
      b.addEventListener('click', () => copyText(list[+b.getAttribute('data-copy')].text, b));
    });
    el.querySelectorAll('[data-del]').forEach((b) => {
      b.addEventListener('click', () => {
        const l = loadPrompts();
        l.splice(+b.getAttribute('data-del'), 1);
        savePrompts(l);
        renderSavedPrompts();
      });
    });
  }

  /* -------------------- Handles -------------------- */

  const HANDLE_IDS = ['carr-handle', 'wa-handle', 'x-handle', 'msg-handle', 'do-handle'];

  function syncHandles(src) {
    const val = normHandle(src.value);
    HANDLE_IDS.forEach((id) => {
      const el = $(`#${id}`);
      if (el && el !== src) el.value = val;
    });
    const st = window.CAROUSEL_SITE && window.CAROUSEL_SITE.getState && window.CAROUSEL_SITE.getState();
    if (st) st.handle = val;
    renderAll();
  }

  /* -------------------- Tabs -------------------- */

  function tabsInit() {
    $$('.tab-btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        $$('.tab-btn').forEach((b) => {
          b.classList.remove('is-active');
          b.setAttribute('aria-selected', 'false');
        });
        $$('.tab-panel').forEach((p) => p.classList.remove('is-active'));
        btn.classList.add('is-active');
        btn.setAttribute('aria-selected', 'true');
        const panel = $('#' + btn.getAttribute('data-tab'));
        if (panel) panel.classList.add('is-active');
      });
    });
  }

  /* -------------------- Áudio -------------------- */

  function audioInit() {
    const play = $('#au-play');
    const stop = $('#au-stop');
    const rate = $('#au-rate');
    const pitch = $('#au-pitch');
    const topic = $('#au-topic');

    if (rate) rate.addEventListener('input', () => {
      if ($('#au-rate-val')) $('#au-rate-val').textContent = parseFloat(rate.value).toFixed(1) + '×';
    });
    if (pitch) pitch.addEventListener('input', () => {
      if ($('#au-pitch-val')) $('#au-pitch-val').textContent = parseFloat(pitch.value).toFixed(1);
    });
    if (topic) topic.addEventListener('change', fillAudioTexts);

    if (play) play.addEventListener('click', () => {
      if (!('speechSynthesis' in window)) return;
      speechSynthesis.cancel();
      fillAudioTexts();
      const textSel = $('#au-text');
      const texts = audioTexts(carById(topic && topic.value), normHandle(currentHandle()));
      const chosen = texts[+((textSel && textSel.value) || 0)] || texts[0];
      const u = new SpeechSynthesisUtterance(chosen.text);
      u.lang = 'pt-BR';
      if (rate) u.rate = parseFloat(rate.value);
      if (pitch) u.pitch = parseFloat(pitch.value);
      speechSynthesis.speak(u);
    });
    if (stop) stop.addEventListener('click', () => {
      if ('speechSynthesis' in window) speechSynthesis.cancel();
    });
  }

  /* -------------------- Prompts UI -------------------- */

  function promptsInit() {
    const topic = $('#pr-topic');
    const platform = $('#pr-platform');
    const duration = $('#pr-duration');
    const tone = $('#pr-tone');
    const copy = $('#pr-copy');
    const save = $('#pr-save');

    const rerender = () => renderPromptOut();
    if (topic) topic.addEventListener('change', rerender);
    if (platform) platform.addEventListener('change', rerender);
    if (duration) duration.addEventListener('change', rerender);
    if (tone) tone.addEventListener('input', rerender);

    if (copy) copy.addEventListener('click', () => {
      const out = $('#pr-out');
      if (out) copyText(out.value, copy);
    });

    if (save) save.addEventListener('click', () => {
      const out = $('#pr-out');
      const nameEl = $('#pr-name');
      if (!out || !out.value) return;
      const list = loadPrompts();
      list.unshift({
        name: (nameEl && nameEl.value.trim()) || `${((platform || {}).value || 'TikTok')} · ${carById(topic && topic.value).nome}`,
        platform: (platform || {}).value || 'TikTok',
        text: out.value,
        ts: new Date().toLocaleDateString('pt-BR'),
      });
      savePrompts(list);
      if (nameEl) nameEl.value = '';
      renderSavedPrompts();
      const prev = save.textContent;
      save.textContent = 'Salvo ✓';
      setTimeout(() => { save.textContent = prev; }, 1400);
    });
  }

  /* -------------------- Dossiê -------------------- */

  function renderDossier() {
    const politico = $('#do-politico');
    const angulo = $('#do-angulo');
    if (!politico || !angulo) return;

    if (!politico.options.length) {
      const cards = dossierCards();
      politico.innerHTML = cards.map((c) => `<option value="${esc(c.name)}">${esc(c.name)}</option>`).join('');
    }

    const name = politico.value;
    const angle = angulo.value;
    const handle = normHandle(currentHandle());
    const facts = dossierFacts(name, angle);

    const nameEl = $('#do-name');
    if (nameEl) nameEl.textContent = name;

    const factsEl = $('#do-facts');
    if (factsEl) {
      factsEl.innerHTML = facts.length
        ? facts.map((f) => `<li>${esc(f)}</li>`).join('')
        : '<li>Sem fatos disponíveis para este ângulo.</li>';
    }

    renderList('#do-list', dossierMessages(facts, name, handle));

    const out = $('#do-out');
    if (out) {
      out.value = dossierPrompt(
        facts,
        name,
        ($('#do-platform') || {}).value || 'TikTok',
        ($('#do-duration') || {}).value || '60s',
        (($('#do-tone') || {}).value || '').trim() || 'direto, irônico, sempre citando a fonte',
        handle
      );
    }
  }

  function dossierInit() {
    const politico = $('#do-politico');
    const angulo = $('#do-angulo');
    const platform = $('#do-platform');
    const duration = $('#do-duration');
    const tone = $('#do-tone');
    const copy = $('#do-copy');
    const save = $('#do-save');

    if (politico) politico.addEventListener('change', renderDossier);
    if (angulo) angulo.addEventListener('change', renderDossier);
    if (platform) platform.addEventListener('change', renderDossier);
    if (duration) duration.addEventListener('change', renderDossier);
    if (tone) tone.addEventListener('input', renderDossier);

    if (copy) copy.addEventListener('click', () => {
      const out = $('#do-out');
      if (out) copyText(out.value, copy);
    });

    if (save) save.addEventListener('click', () => {
      const out = $('#do-out');
      if (!out || !out.value) return;
      const nameEl = $('#do-politico');
      const list = loadPrompts();
      list.unshift({
        name: `Roteiro contra · ${shortenName((nameEl && nameEl.value) || 'político')}`,
        platform: ((platform || {}).value || 'TikTok') + ' · ' + ((angulo || {}).value || 'patrimonio'),
        text: out.value,
        ts: new Date().toLocaleDateString('pt-BR'),
      });
      savePrompts(list);
      renderSavedPrompts();
      const prev = save.textContent;
      save.textContent = 'Salvo ✓';
      setTimeout(() => { save.textContent = prev; }, 1400);
    });
  }

  /* -------------------- Init -------------------- */

  function init() {
    if (!window.CARROSSEIS || !window.CARROSSEIS.length) return;

    tabsInit();

    ['#wa-topic', '#x-topic', '#msg-topic', '#au-topic', '#pr-topic'].forEach((sel) => {
      fillTopicSelect($(sel));
    });

    HANDLE_IDS.forEach((id) => {
      const el = $(`#${id}`);
      if (!el) return;
      el.value = normHandle(currentHandle());
      el.addEventListener('input', () => syncHandles(el));
    });

    audioInit();
    promptsInit();
    dossierInit();
    renderAll();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
