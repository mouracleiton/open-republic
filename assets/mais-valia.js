/* ============================================================
   CALCULADORA DE MAIS-VALIA — JavaScript
   Todos os IDs estão prefixados com "mv-" para não colidir com
   o restante do site. Cada fórmula está comentada e referenciada
   ao conceito teórico marxista.
   ============================================================
   VARIÁVEIS (padrão do prompt):
     S = Salário mensal bruto (R$)
     V = Valor produzido pelo trabalhador no mês (R$)
     J = Jornada total trabalhada no mês (horas)
   ============================================================ */

(function () {
  'use strict';

  // Só executa se a seção da calculadora existir na página
  var root = document.getElementById('mv-root');
  if (!root) return;

  /* ---------- Helpers de formato pt-BR ---------- */

  // Aceita tanto "2000" quanto "2.000,00" e "2000,00" (vírgula decimal BR)
  function parseBR(str) {
    if (str === null || str === undefined) return NaN;
    str = String(str).trim();
    if (str === '') return NaN;
    // remove espaços e qualquer caractere que não seja dígito, vírgula, ponto ou sinal
    str = str.replace(/[^\d.,-]/g, '');
    if (str === '' || str === '-' || str === '.' || str === ',') return NaN;
    // Se há vírgula, ela é o separador decimal (pt-BR); pontos são separadores de milhar
    if (str.indexOf(',') !== -1) {
      str = str.replace(/\./g, '').replace(',', '.');
    }
    var n = parseFloat(str);
    return n;
  }

  // Formata número como moeda BR: R$ 1.234,56
  function fmtMoeda(n) {
    return n.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL', minimumFractionDigits: 2, maximumFractionDigits: 2 });
  }

  // Formata número com N casas decimais BR: 34,09
  function fmtNum(n, dec) {
    return n.toLocaleString('pt-BR', { minimumFractionDigits: dec, maximumFractionDigits: dec });
  }

  // Converte horas fracionárias para o formato "Xh Ymin"
  // tempoNecessario_h = 58,666... -> "58h 40min"
  function horasParaHM(valorHoras) {
    var h = Math.floor(valorHoras + 1e-9);   // +1e-9 corrige erro de float em .999...
    var min = Math.round((valorHoras - h) * 60);
    if (min === 60) { h += 1; min = 0; }      // arredondamento que vira hora cheia
    return h + 'h ' + min + 'min';
  }

  /* ---------- DOM (IDs prefixados com mv-) ---------- */
  var $ = function (id) { return document.getElementById(id); };

  /* ---------- Alternância de modo de jornada ---------- */
  var modoJornada = 'detalhe'; // 'detalhe' | 'total'

  $('mv-btn-jornada-detalhe').addEventListener('click', function () {
    modoJornada = 'detalhe';
    this.classList.add('active'); this.setAttribute('aria-pressed', 'true');
    $('mv-btn-jornada-total').classList.remove('active'); $('mv-btn-jornada-total').setAttribute('aria-pressed', 'false');
    $('mv-jornada-detalhe').style.display = 'grid';
    $('mv-jornada-total').style.display = 'none';
    $('mv-horas-mes').value = '';
  });
  $('mv-btn-jornada-total').addEventListener('click', function () {
    modoJornada = 'total';
    this.classList.add('active'); this.setAttribute('aria-pressed', 'true');
    $('mv-btn-jornada-detalhe').classList.remove('active'); $('mv-btn-jornada-detalhe').setAttribute('aria-pressed', 'false');
    $('mv-jornada-total').style.display = 'block';
    $('mv-jornada-detalhe').style.display = 'none';
    $('mv-horas-dia').value = ''; $('mv-dias-semana').value = '';
  });
  // estado inicial: detalhe visível, total oculto
  $('mv-jornada-total').style.display = 'none';

  /* ---------- Alternância de modo de valor produzido ---------- */
  var modoValor = 'direto'; // 'direto' | 'estimativa'

  $('mv-btn-valor-direto').addEventListener('click', function () {
    modoValor = 'direto';
    this.classList.add('active'); this.setAttribute('aria-pressed', 'true');
    $('mv-btn-valor-estimativa').classList.remove('active'); $('mv-btn-valor-estimativa').setAttribute('aria-pressed', 'false');
    $('mv-valor-direto').style.display = 'block';
    $('mv-valor-estimativa').style.display = 'none';
  });
  $('mv-btn-valor-estimativa').addEventListener('click', function () {
    modoValor = 'estimativa';
    this.classList.add('active'); this.setAttribute('aria-pressed', 'true');
    $('mv-btn-valor-direto').classList.remove('active'); $('mv-btn-valor-direto').setAttribute('aria-pressed', 'false');
    $('mv-valor-estimativa').style.display = 'block';
    $('mv-valor-direto').style.display = 'none';
  });

  /* ---------- Alertas ---------- */
  function mostrarErro(msg) {
    var el = $('mv-alerta');
    el.textContent = msg;
    el.classList.add('show');
    $('mv-alerta-aviso').classList.remove('show');
    $('mv-results').classList.remove('show');
  }
  function mostrarAviso(msg) {
    var el = $('mv-alerta-aviso');
    el.innerHTML = msg;
    el.classList.add('show');
  }
  function limparAlertas() {
    $('mv-alerta').classList.remove('show');
    $('mv-alerta-aviso').classList.remove('show');
  }

  /* ============================================================
     FUNÇÕES PRINCIPAIS DE CÁLCULO
     ============================================================ */

  /**
   * Calcula todos os indicadores a partir de S, V, J.
   *
   * FÓRMULAS (teoria marxista da mais-valia):
   *
   *  valorPorHora     = V / J
   *    -> quanto de valor (R$) o trabalhador produz a cada hora.
   *
   *  maisValia        = V - S
   *    -> a parte do valor produzido que NÃO volta como salário.
   *       É o "trabalho de graça" apropriado pelo capitalista.
   *
   *  taxaDeMaisValia  = ((V - S) / S) * 100
   *    -> razão entre mais-valia e salário, em %.
   *       Mede o GRAU de exploração. 200% = para cada R$1 de salário,
   *       o patrão embolsa R$2 de mais-valia.
   *
   *  tempoNecessario_h = (S * J) / V
   *    -> proporção da jornada gasta em produzir o equivalente ao
   *       salário. Como S/V é a fração do dia que "se paga",
   *       multiplicamos pela jornada total J.
   *       É o tempo que o trabalhador trabalha "para si".
   *
   *  tempoExcedente_h = J - tempoNecessario_h
   *    -> o resto da jornada, onde se gera a mais-valia.
   *       É o tempo trabalhado "de graça" para o patrão.
   */
  function calcular(S, V, J) {
    var valorPorHora = V / J;
    var maisValia = V - S;
    var taxaDeMaisValia = ((V - S) / S) * 100;
    var tempoNecessario_h = (S * J) / V;
    var tempoExcedente_h = J - tempoNecessario_h;

    return {
      valorPorHora: valorPorHora,
      maisValia: maisValia,
      taxaDeMaisValia: taxaDeMaisValia,
      tempoNecessario_h: tempoNecessario_h,
      tempoExcedente_h: tempoExcedente_h
    };
  }

  /**
   * Interpretação automática da taxa de mais-valia.
   * "200% significa: a cada 3 horas trabalhadas, 1 é sua e 2 vão para o patrão."
   *
   * Lógica: se a taxa = t%, então para cada (1 + t/100) horas,
   * 1 hora é "sua" e (t/100) horas são do patrão.
   * Ex: 200% -> 1 + 2 = 3 horas totais; 1 sua, 2 do patrão.
   */
  function interpretarTaxa(taxa) {
    var fracaoPatrao = taxa / 100;           // ex: 2.0 para 200%
    var total = 1 + fracaoPatrao;            // ex: 3
    // Se a fração do patrão for inteira, usamos direto; senão arredondamos o total
    if (Number.isInteger(fracaoPatrao)) {
      return 'A cada ' + total + ' horas trabalhadas, <strong>1 é sua</strong> e <strong class="patrao">' + fracaoPatrao + ' vão para o patrão</strong>.';
    }
    // Para taxas não inteiras, arredondamos para facilitar a leitura
    var totalArred = Math.round(total);
    var deleArred = totalArred - 1;
    return 'A cada ' + totalArred + ' horas trabalhadas, <strong>1 é sua</strong> e <strong class="patrao">' + deleArred + ' vão para o patrão</strong>.';
  }

  /**
   * Relógio da exploração.
   * Mostra a que horas do dia o trabalhador para de trabalhar para si
   * e começa a trabalhar de graça.
   *
   * Lógica: numa jornada diária de H horas, a fração necessária é
   * tempoNecessario_h / J. O tempo necessário em escala de um dia é:
   *   horasNecessariasDia = (tempoNecessario_h / J) * H
   * Se o dia começa às 08:00, o "ponto de virada" é:
   *   08:00 + horasNecessariasDia
   */
  function relogioExploracao(tempoNecessario_h, J, horasPorDia) {
    // proporção do dia que é "pra você"
    var propNecessaria = tempoNecessario_h / J;          // 0..1
    var horasNecessariasDia = propNecessaria * horasPorDia;
    // início do expediente padrão: 08:00
    var inicioMin = 8 * 60; // 480 min
    var viradaMin = inicioMin + Math.round(horasNecessariasDia * 60);
    var h = Math.floor(viradaMin / 60);
    var m = viradaMin % 60;
    var horaStr = String(h).padStart(2, '0') + ':' + String(m).padStart(2, '0');
    return {
      horaStr: horaStr,
      horasNecessariasDia: horasNecessariasDia,
      horasExcedentesDia: horasPorDia - horasNecessariasDia
    };
  }

  /* ============================================================
     FLUXO PRINCIPAL
     ============================================================ */

  $('mv-btn-calcular').addEventListener('click', function () {
    limparAlertas();

    /* --- 1. SALÁRIO (S) --- */
    var S = parseBR($('mv-salario').value);
    if (isNaN(S) || S === 0) {
      mostrarErro('⚠️ Informe seu salário bruto mensal. Não pode estar vazio ou zero.');
      return;
    }
    if (S < 0) {
      mostrarErro('⚠️ O salário não pode ser negativo.');
      return;
    }

    /* --- 2. JORNADA (J) em horas/mês --- */
    var J;
    if (modoJornada === 'detalhe') {
      var hDia = parseBR($('mv-horas-dia').value);
      var dSemana = parseBR($('mv-dias-semana').value);
      if (isNaN(hDia) || hDia === 0 || isNaN(dSemana) || dSemana === 0) {
        mostrarErro('⚠️ Informe as horas por dia e os dias por semana (ou use o modo "Total de horas/mês").');
        return;
      }
      if (hDia < 0 || dSemana < 0) {
        mostrarErro('⚠️ Horas por dia e dias por semana não podem ser negativos.');
        return;
      }
      // J = h/dia * dias/semana * (52 semanas / 12 meses) ~ 4,333 semanas/mês
      J = hDia * dSemana * (52 / 12);
    } else {
      J = parseBR($('mv-horas-mes').value);
      if (isNaN(J) || J === 0) {
        mostrarErro('⚠️ Informe o total de horas trabalhadas no mês. Não pode ser zero.');
        return;
      }
      if (J < 0) {
        mostrarErro('⚠️ A jornada não pode ser negativa.');
        return;
      }
    }

    /* --- 3. VALOR PRODUZIDO (V) --- */
    var V;
    var ehEstimativa = false;
    if (modoValor === 'direto') {
      V = parseBR($('mv-valor-produzido').value);
      if (isNaN(V) || V === 0) {
        mostrarErro('⚠️ Informe o valor que você produz no mês (ou use o modo estimativa).');
        return;
      }
      if (V < 0) {
        mostrarErro('⚠️ O valor produzido não pode ser negativo.');
        return;
      }
    } else {
      var markup = parseBR($('mv-markup').value);
      if (isNaN(markup) || markup === 0) {
        mostrarErro('⚠️ Informe o markup de exploração em % (ex: 150, 200, 300).');
        return;
      }
      if (markup < 0) {
        mostrarErro('⚠️ O markup não pode ser negativo.');
        return;
      }
      // V = S * (1 + markup/100)   -> markup 200% e S=2000 => V=6000
      V = S * (1 + markup / 100);
      ehEstimativa = true;
    }

    /* --- 4. CÁLCULOS --- */
    var r = calcular(S, V, J);

    /* --- 5. CASO DE BORDA: V <= S (sem mais-valia) --- */
    if (V <= S) {
      mostrarAviso('⚠️ O valor que você informou produzir (' + fmtMoeda(V) + ') é menor ou igual ao seu salário (' + fmtMoeda(S) + '). Isso significa que "não há mais-valia" — o que é incomum no capitalismo e pode indicar que os dados estão incompletos. Os números abaixo assumem tempo excedente zero.');
      // Forçar tempo excedente a 0 (não negativo) e refazer display
      r.tempoExcedente_h = 0;
      r.maisValia = 0;
      r.taxaDeMaisValia = 0;
    }

    /* --- 6. RENDERIZAR RESULTADOS --- */
    renderizar(r, S, V, J, ehEstimativa);

    if (ehEstimativa) {
      mostrarAviso('ⓘ O valor que você produz é uma <strong>estimativa</strong> baseada no markup informado. Se souber o valor real, use o modo "Eu sei o valor" para um cálculo mais preciso.');
    }

    // scroll suave até os resultados
    $('mv-results').scrollIntoView({ behavior: 'smooth', block: 'start' });
  });

  /* ---------- Renderização ---------- */

  function renderizar(r, S, V, J, ehEstimativa) {
    $('mv-results').classList.add('show');

    /* Taxa de mais-valia em destaque */
    $('mv-r-taxa').innerHTML = fmtNum(r.taxaDeMaisValia, 0) + '<small>%</small>';
    $('mv-r-taxa-interp').innerHTML = interpretarTaxa(r.taxaDeMaisValia);

    /* Barra proporcional */
    var pctVoce = (r.tempoNecessario_h / J) * 100;
    var pctPatrao = (r.tempoExcedente_h / J) * 100;
    if (pctPatrao < 0) pctPatrao = 0;
    if (pctVoce > 100) pctVoce = 100;
    $('mv-r-seg-voce').style.width = pctVoce.toFixed(2) + '%';
    $('mv-r-seg-patrao').style.width = pctPatrao.toFixed(2) + '%';
    $('mv-r-lbl-voce').textContent = 'Tempo pra você · ' + pctVoce.toFixed(0) + '%';
    $('mv-r-lbl-patrao').textContent = pctPatrao.toFixed(0) + '% · Tempo pro patrão';
    $('mv-r-tempo-voce').textContent = horasParaHM(r.tempoNecessario_h) + ' / mês pra você';
    $('mv-r-tempo-patrao').textContent = horasParaHM(r.tempoExcedente_h) + ' / mês pro patrão';

    /* Relógio da exploração */
    // descobrir horas/dia: se veio do modo detalhe, usamos hDia; senão estimamos
    var horasPorDia;
    if (modoJornada === 'detalhe') {
      horasPorDia = parseBR($('mv-horas-dia').value);
    } else {
      // estimativa: horas/mês dividido por ~4,33 semanas, dividido por 5 dias (média)
      horasPorDia = J / (52 / 12) / 5;
    }
    var relogio = relogioExploracao(r.tempoNecessario_h, J, horasPorDia);
    if (r.tempoExcedente_h <= 0) {
      $('mv-r-relogio').innerHTML = 'No seu caso, você trabalha <strong>o dia inteiro para você</strong>. Não há tempo excedente.';
      $('mv-r-relogio-sub').textContent = 'Isso é raro no capitalismo — confira seus dados.';
    } else {
      $('mv-r-relogio').innerHTML = 'Você trabalha para <strong>VOCÊ</strong> até as <strong>' + relogio.horaStr + '</strong>. Depois disso, é tudo <span class="patrao">pro patrão</span>.';
      $('mv-r-relogio-sub').textContent = 'Numa jornada de ' + fmtNum(horasPorDia, 1).replace('.', ',') + 'h por dia, você "se paga" em ' + horasParaHM(relogio.horasNecessariasDia) + '.';
    }

    /* Números */
    $('mv-r-mv-mes').textContent = fmtMoeda(r.maisValia);
    // mais-valia por dia: dividir por dias/mês (~ J / horasPorDia)
    var diasMes = J / horasPorDia;
    $('mv-r-mv-dia').textContent = fmtMoeda(r.maisValia / diasMes);
    $('mv-r-mv-hora').textContent = fmtMoeda(r.maisValia / J);
    $('mv-r-valor-hora').textContent = fmtMoeda(r.valorPorHora);
    $('mv-r-tn').textContent = horasParaHM(r.tempoNecessario_h);
    $('mv-r-te').textContent = horasParaHM(r.tempoExcedente_h);

    /* Guarda resumo p/ compartilhamento */
    estadoResumo = {
      S: S, V: V, J: J,
      taxa: r.taxaDeMaisValia,
      mvMes: r.maisValia,
      tn: r.tempoNecessario_h,
      te: r.tempoExcedente_h,
      relogio: relogio.horaStr,
      ehEstimativa: ehEstimativa
    };
  }

  /* ---------- Compartilhar ---------- */
  var estadoResumo = null;

  $('mv-btn-share').addEventListener('click', function () {
    if (!estadoResumo) return;
    var e = estadoResumo;
    var txt = '🚩 Calculadora de Mais-Valia\n\n' +
      'Salário: ' + fmtMoeda(e.S) + '\n' +
      'Valor que produzo: ' + fmtMoeda(e.V) + (e.ehEstimativa ? ' (estimado)' : '') + '\n' +
      'Jornada: ' + fmtNum(e.J, 0) + 'h/mês\n\n' +
      '🔴 Taxa de exploração: ' + fmtNum(e.taxa, 0) + '%\n' +
      '💰 Mais-valia (pro patrão): ' + fmtMoeda(e.mvMes) + '/mês\n' +
      '⏰ Começo a trabalhar de graça a partir das ' + e.relogio + '\n' +
      '✅ Tempo pra mim: ' + horasParaHM(e.tn) + '/mês\n' +
      '❌ Tempo pro patrão: ' + horasParaHM(e.te) + '/mês\n\n' +
      'Descubra a sua: ferramenta gratuita de letramento político.';

    function sucesso() {
      var btn = $('mv-btn-share');
      var old = btn.textContent;
      btn.textContent = '✅ Copiado! Cole no WhatsApp ou rede social.';
      btn.classList.add('copied');
      setTimeout(function () { btn.textContent = old; btn.classList.remove('copied'); }, 3500);
    }
    function falha() {
      // fallback: seleciona um textarea temporário
      var ta = document.createElement('textarea');
      ta.value = txt;
      ta.style.position = 'fixed';
      ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      try { document.execCommand('copy'); sucesso(); } catch (err) {
        alert('Não foi possível copiar automaticamente. Selecione e copie o texto:\n\n' + txt);
      }
      document.body.removeChild(ta);
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(txt).then(sucesso, falha);
    } else {
      falha();
    }
  });

  /* ============================================================
     TESTE DE VERIFICAÇÃO INTERNO (executa no console do navegador)
     Entradas: S=2000, V=6000, J=176
     Saídas esperadas conforme especificação:
       valorPorHora     = 34,09
       maisValia        = 4000
       taxaDeMaisValia  = 200%
       tempoNecessario  = 58h 40min
       tempoExcedente   = 117h 20min
       (58h40 + 117h20 = 176h)
     ============================================================ */
  if (window.console && window.console.log) {
    var _t = calcular(2000, 6000, 176);
    window.console.log('%c[TESTE Calculadora de Mais-Valia] S=2000 V=6000 J=176', 'color:#E9A13B;font-weight:bold');
    window.console.log('  valorPorHora     =', fmtNum(_t.valorPorHora, 2), '(esperado 34,09)');
    window.console.log('  maisValia        =', fmtMoeda(_t.maisValia), '(esperado R$ 4.000,00)');
    window.console.log('  taxaDeMaisValia  =', fmtNum(_t.taxaDeMaisValia, 0) + '%', '(esperado 200%)');
    window.console.log('  tempoNecessario  =', horasParaHM(_t.tempoNecessario_h), '(esperado 58h 40min)');
    window.console.log('  tempoExcedente   =', horasParaHM(_t.tempoExcedente_h), '(esperado 117h 20min)');
    window.console.log('  soma TN+TE       =', fmtNum(_t.tempoNecessario_h + _t.tempoExcedente_h, 0) + 'h', '(esperado 176h)');
  }

})();
