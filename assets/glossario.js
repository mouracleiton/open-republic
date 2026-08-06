/* ============================================================
   GLOSSÁRIO COMUNISTA — JavaScript
   Acordeão expansível (toque no termo para abrir/fechar) + busca
   em tempo real. Todos os IDs prefixados com "gl-".
   ============================================================ */

(function () {
  'use strict';

  var root = document.getElementById('gl-root');
  if (!root) return;

  var items = root.querySelectorAll('.gl-item');

  /* ---------- Acordeão: clicar no <dt> abre/fecha o <dd> ---------- */
  items.forEach(function (item) {
    var dt = item.querySelector('dt');
    dt.addEventListener('click', function () {
      item.classList.toggle('open');
    });
    // Acessibilidade: teclado
    dt.setAttribute('tabindex', '0');
    dt.setAttribute('role', 'button');
    dt.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        item.classList.toggle('open');
      }
    });
  });

  /* ---------- Busca em tempo real ---------- */
  var search = document.getElementById('gl-search');
  search.addEventListener('input', function () {
    var q = this.value.trim().toLowerCase();
    items.forEach(function (item) {
      var term = (item.getAttribute('data-term') || '').toLowerCase();
      var text = item.textContent.toLowerCase();
      if (q === '' || term.indexOf(q) !== -1 || text.indexOf(q) !== -1) {
        item.classList.remove('hidden');
      } else {
        item.classList.add('hidden');
        item.classList.remove('open');
      }
    });
  });

})();
