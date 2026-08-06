/* ============================================================
   Carrosséis — carrega do JSON (única fonte de dados).
   ANTES: 20 carrosséis hardcoded (duplicava dados_api.json).
   AGORA: busca exclusivamente de dados_api.json (carrosseis_instagram).
   Se o fetch falhar, as grades ficam vazias (sem dados para mostrar).
   ============================================================ */

(function () {
  'use strict';

  // Array compartilhado — carousel-site.js lê esta referência
  window.CARROSSEIS = [];

  // Busca os carrosséis do JSON (fonte única da verdade)
  fetch('dados_api.json', { cache: 'no-cache' })
    .then(function (res) {
      if (!res.ok) throw new Error('HTTP ' + res.status);
      return res.text();
    })
    .then(function (text) {
      var start = text.indexOf('{');
      if (start < 0) throw new Error('JSON não encontrado');
      var data = JSON.parse(text.slice(start));
      if (data.carrosseis_instagram && data.carrosseis_instagram.length) {
        // Popula o array existente (referência compartilhada com carousel-site.js)
        data.carrosseis_instagram.forEach(function (c) {
          window.CARROSSEIS.push(c);
        });
        console.log('[carrosseis] ' + data.carrosseis_instagram.length + ' carrosséis carregados do JSON.');

        // Notifica o carousel-site.js para re-renderizar
        document.dispatchEvent(new CustomEvent('carrosseis-loaded'));
      } else {
        console.warn('[carrosseis] Seção carrosseis_instagram não encontrada no JSON.');
      }
    })
    .catch(function (err) {
      console.warn('[carrosseis] Falha ao carregar do JSON:', err.message);
    });

})();
