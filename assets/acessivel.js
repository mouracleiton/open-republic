/* ============================================================
   Bootstrap da página "Pra Vovó Entender" (acessivel.html)
   Carrega o JSON (por padrão assets/dados-exemplo.json, ou o
   arquivo indicado por ?dados=caminho) e monta os cartões.
   ============================================================ */
(function () {
  'use strict';

  var M = window.Metaforas;
  var params = new URLSearchParams(window.location.search);
  var arquivo = params.get('dados') || 'assets/dados-exemplo.json';

  var cartoesEl = document.getElementById('cartoes');
  var btnTudo = document.getElementById('btn-ouvir-tudo');
  var btnTudoTexto = document.getElementById('btn-ouvir-tudo-texto');
  var fonteEl = document.getElementById('pagina-fonte');
  var rodapeEl = document.getElementById('rodape-leitura');

  var itens = [];
  var elementos = [];
  var narrando = false;

  function contarVozes() {
    return M.vozPT() ? 'voz disponível' : 'voz indisponível (abra no Chrome, Edge ou Safari)';
  }

  function iniciar() {
    carregar();
    btnTudo.addEventListener('click', function () {
      if (narrando) {
        M.pararFala();
        setNarrando(false);
        return;
      }
      setNarrando(true);
      var fila = [{ texto: window.__intro || 'Aqui está o resumo das coisas.', el: null }];
      itens.forEach(function (d, i) {
        var m = M.resolveMetafora(d.metafora || M.inferirMetafora(d.tema)) || M.resolveMetafora('pote_agua');
        var txt = M.textoDoCartao(d, i, m);
        fila.push({ texto: txt, el: elementos[i] });
      });
      narrarLista(fila, 0);
    });
  }

  function carregar() {
    fonteEl.textContent = 'Lendo dados de: ' + arquivo + ' · ' + contarVozes();
    M.carregarJSON(arquivo)
      .then(function (json) {
        itens = M.extrairItens(json);
        if (json.titulo_pagina) document.getElementById('pagina-titulo').textContent = json.titulo_pagina;
        if (json.intro_audio) window.__intro = json.intro_audio;
        if (json._meta && json._meta.atualizacao) {
          fonteEl.textContent = 'Lendo dados de: ' + arquivo + ' · ' + json._meta.atualizacao + ' · ' + contarVozes();
        }
        renderizar();
      })
      .catch(function (err) {
        fonteEl.textContent = 'Não consegui abrir ' + arquivo + '. ' + err.message;
        cartoesEl.innerHTML =
          '<article class="cartao"><h2 class="titulo-secção">Não consegui ler os dados</h2>' +
          '<p class="texto-grande">Não achei o arquivo de dados. Peça pra alguém conferir e tente de novo.</p></article>';
      });
  }

  function renderizar() {
    cartoesEl.textContent = '';
    elementos = [];
    if (!itens.length) {
      cartoesEl.innerHTML =
        '<article class="cartao"><h2 class="titulo-secção">Nada pra mostrar</h2>' +
        '<p class="texto-grande">O arquivo veio sem itens de dados.</p></article>';
      rodapeEl.textContent = 'Nenhum item encontrado em ' + arquivo + '.';
      return;
    }
    itens.forEach(function (d, i) {
      var el = M.renderCartao(d, i);
      cartoesEl.appendChild(el);
      elementos.push(el);
    });
    rodapeEl.textContent = itens.length + ' assuntos lidos de ' + arquivo + '. Toque em "Ouvir tudo" pra escutar de ponta a ponta.';
  }

  function narrarLista(lista, i) {
    if (i >= lista.length) {
      setNarrando(false);
      return;
    }
    var item = lista[i];
    if (item.el) {
      destacarCartao(item.el);
    }
    M.falar(item.texto, {
      rate: 0.95,
      pitch: 1.05,
      onFim: function () {
        if (item.el) item.el.classList.remove('narrando');
        if (i + 1 < lista.length) narrarLista(lista, i + 1);
        else setNarrando(false);
      },
    });
  }

  function destacarCartao(el) {
    document.querySelectorAll('.cartao-metafora.narrando').forEach(function (c) {
      c.classList.remove('narrando');
    });
    el.classList.add('narrando');
    el.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  function setNarrando(v) {
    narrando = v;
    btnTudo.classList.toggle('narrando', v);
    btnTudoTexto.textContent = v ? '■ Parar de falar' : '▶ Ouvir tudo';
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', iniciar);
  } else {
    iniciar();
  }
})();
