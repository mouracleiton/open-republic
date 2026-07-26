// Full JS (ES6) translation of open_energy_taxonomy.py
// All 6 enums, 4 dataclasses, engine, _init functions, full demo with 10 systems.
// Runnable with node. Comments/strings in Portuguese. Equivalent output.

const TipoEnergia = {
  CELULAR: { id: "celular", rotulo: "Energia Celular (mitocondrial)", numero: 1 },
  MECANICA: { id: "mecanica", rotulo: "Energia Mecanica (muscular)", numero: 2 },
  TERMICA: { id: "termica", rotulo: "Energia Termica (metabolica)", numero: 3 },
  NEURAL: { id: "neural", rotulo: "Energia Neural (sinal)", numero: 4 },
  QUIMICA: { id: "quimica", rotulo: "Energia Quimica (sintese)", numero: 5 },
  SENSORIAL: { id: "sensorial", rotulo: "Energia Sensorial (transducao)", numero: 6 },
  COGNITIVA: { id: "cognitiva", rotulo: "Energia Cognitiva (processamento)", numero: 7 },
  ATENCIONAL: { id: "atencional", rotulo: "Energia Atencional (foco)", numero: 8 },
  EMOCIONAL: { id: "emocional", rotulo: "Energia Emocional (motivacao)", numero: 9 },
  RELACIONAL: { id: "relacional", rotulo: "Energia Relacional (social)", numero: 10 },
};

const EscalaEnergia = {
  CORPO: { id: "corpo", rotulo: "Nivel do corpo individual" },
  COMUNIDADE: { id: "comunidade", rotulo: "Nivel da comunidade/local" },
  CIVILIZACAO: { id: "civilizacao", rotulo: "Nivel da civilizacao/global" },
  PLANETA: { id: "planeta", rotulo: "Nivel planetario/biosfera" },
};

const StatusDisponibilidade = {
  ABUNDANTE: { id: "abundante", rotulo: "Abundante: excedente para doar" },
  EQUILIBRADA: { id: "equilibrada", rotulo: "Equilibrada: cobre a demanda" },
  LIMITADA: { id: "limitada", rotulo: "Limitada: alocacao necessaria" },
  CRITICA: { id: "critica", rotulo: "Critica: deficit, intervene" },
  DEPLETADA: { id: "depletada", rotulo: "Depletada: esgotada, recuperacao obrigatoria" },
};

const NivelCobertura = {
  COBERTO: { id: "coberto", rotulo: "Totalmente coberto por modulo(s) existente(s)" },
  PARCIAL: { id: "parcial", rotulo: "Parcialmente coberto -- lacunas identificadas" },
  LACUNA: { id: "lacuna", rotulo: "Lacuna: nenhum modulo cobre este tipo" },
  NAO_APLICAVEL: { id: "nao_aplicavel", rotulo: "Nao aplicavel (conceitual)" },
};

const TipoInput = {
  ALIMENTO: { id: "alimento", rotulo: "Alimento/caloria (comida, combustivel)" },
  OXIGENIO: { id: "oxigenio", rotulo: "Oxigenio/ar" },
  LUZ: { id: "luz", rotulo: "Luz/fotons" },
  SOM: { id: "som", rotulo: "Som/vibracao" },
  CALOR_AMBIENTE: { id: "calor", rotulo: "Calor ambiental" },
  PRESENCA: { id: "presenca", rotulo: "Presenca de outro ser humano" },
  INFORMACAO: { id: "informacao", rotulo: "Informacao/dados" },
  SONO: { id: "sono", rotulo: "Sono/descanso" },
  MOVIMENTO_CORPO: { id: "movimento", rotulo: "Movimento do proprio corpo" },
  VENTO_AGUA: { id: "vento_agua", rotulo: "Vento, agua, forcas naturais" },
};

const TipoResiduo = {
  CALOR: { id: "calor", rotulo: "Calor dissipado" },
  CO2: { id: "co2", rotulo: "CO2 / gases de exaustao" },
  CANSACO_FISICO: { id: "cansaco_fisico", rotulo: "Cansaco fisico / acido latico" },
  FADIGA_MENTAL: { id: "fadiga_mental", rotulo: "Fadiga mental / saturacao" },
  DESGASTE_MATERIAL: { id: "desgaste", rotulo: "Desgaste material (atriito, envelhecimento)" },
  RUIDO: { id: "ruido", rotulo: "Ruido (sonoro, visual, informational)" },
  SOLIDAO: { id: "solidao", rotulo: "Solidao (quando a conexao termina)" },
  RESIDUO_TOXICO: { id: "residuo_toxico", rotulo: "Residuo toxico (quimico, radiativo)" },
  DADOS_DESCARTADOS: { id: "dados_descartados", rotulo: "Dados descartados (log, cache)" },
};

class FluxoEnergetico {
  constructor() {
    this.inputs = [];
    this.conversao = "";
    this.output = "";
    this.residuos = [];
    this.eficiencia_pct = 100.0;
  }
}

class SistemaEnergetico {
  constructor() {
    this.tipo = null;
    this.nome = "";
    this.analogia_corpo = "";
    this.analogia_civilizacao = "";
    this.escala = null;
    this.fluxo = new FluxoEnergetico();
    this.consumo_corpo_pct = 0.0;
    this.observacao = "";
  }
}

class CoberturaRepublica {
  constructor() {
    this.tipo = null;
    this.nivel = null;
    this.modulos = [];
    this.lacunas = [];
  }
}

class DiagnosticoEnergetico {
  constructor() {
    this.entidade = "";
    this.status_por_tipo = {};
    this.tipos_em_deficit = [];
    this.tipos_abundantes = [];
    this.veredito = "";
  }
}

function _init_sistemas() {
  const sistemas = [];

  // 1. CELULAR
  const s1 = new SistemaEnergetico();
  s1.tipo = TipoEnergia.CELULAR;
  s1.nome = "Mitocondrial";
  s1.analogia_corpo = "Mitocondrias convertem glicose + oxigenio em ATP. ATP e a MOEDA energetica da celula -- todo trabalho celular paga em ATP. Sem ATP, a celula morre em segundos.";
  s1.analogia_civilizacao = "A rede eletrica. A tomada e o ATP da civilizacao. Todo aparelho, toda maquina, todo servo consome eletricidade. OpenEnergy cobre este sistema.";
  s1.escala = EscalaEnergia.CIVILIZACAO;
  s1.fluxo.inputs = [TipoInput.ALIMENTO, TipoInput.OXIGENIO];
  s1.fluxo.conversao = "Glicose + O2 -> ATP (fosforilacao oxidativa)";
  s1.fluxo.output = "ATP (trifosfato de adenosina) / Eletricidade";
  s1.fluxo.residuos = [TipoResiduo.CO2, TipoResiduo.CALOR];
  s1.fluxo.eficiencia_pct = 40.0;
  s1.consumo_corpo_pct = 0.0;
  s1.observacao = "Sistema base. Todos os outros dependem deste. OpenEnergy = cobertura total deste nivel.";
  sistemas.push(s1);

  // 2. MECANICA
  const s2 = new SistemaEnergetico();
  s2.tipo = TipoEnergia.MECANICA;
  s2.nome = "Muscular / Motora";
  s2.analogia_corpo = "ATP -> miosina/actina -> contracao muscular -> MOVIMENTO. O corpo faz TRABALHO FISICO sobre o mundo. Cada passo, cada gesto, cada levantamento de peso.";
  s2.analogia_civilizacao = "Transporte, maquinas, ferramentas, robos. O motor de carro, o braco robotico, a bicicleta. Todo trabalho fisico ja existiu como energia muscular antes de ser externalizado para maquinas.";
  s2.escala = EscalaEnergia.CIVILIZACAO;
  s2.fluxo.inputs = [TipoInput.ALIMENTO, TipoInput.MOVIMENTO_CORPO];
  s2.fluxo.conversao = "ATP -> forca mecanica (contracao / combustao / eletricidade)";
  s2.fluxo.output = "Movimento, forca, deslocamento";
  s2.fluxo.residuos = [TipoResiduo.CANSACO_FISICO, TipoResiduo.CALOR, TipoResiduo.CO2];
  s2.fluxo.eficiencia_pct = 25.0;
  s2.consumo_corpo_pct = 30.0;
  s2.observacao = "OpenAthlete cobre o lado humano (esporte, treino). Transporte publico (OpenMobility) cobre o lado civilizacional.";
  sistemas.push(s2);

  // 3. TERMICA
  const s3 = new SistemaEnergetico();
  s3.tipo = TipoEnergia.TERMICA;
  s3.nome = "Metabolica / Calorica";
  s3.analogia_corpo = "O metabolismo produz calor como subproduto. O corpo GASTA energia mantendo 36,5C -- termorregulacao. Tremer de frio e gerar calor muscular. Suar e dissipar.";
  s3.analogia_civilizacao = "Aquecimento, cozimento, refrigeracao. O FOGO foi a primeira energia externa que o humano dominou (1 milhao de anos antes da eletricidade). Cozinhar e PRE-DIGERIR com energia termica externa -- libera energia celular que iria pra digestao.";
  s3.escala = EscalaEnergia.CIVILIZACAO;
  s3.fluxo.inputs = [TipoInput.ALIMENTO, TipoInput.CALOR_AMBIENTE];
  s3.fluxo.conversao = "Metabolismo / combustao / compressao -> calor";
  s3.fluxo.output = "Calor (manutencao de temperatura / cozimento)";
  s3.fluxo.residuos = [TipoResiduo.CALOR, TipoResiduo.CO2];
  s3.fluxo.eficiencia_pct = 60.0;
  s3.consumo_corpo_pct = 50.0;
  s3.observacao = "Metabolismo basal: 50% do gasto energetico do corpo em repouso e so para manter a temperatura. O cozimento de alimentos foi a REVOLUCAO ENERGETICA original da humanidade.";
  sistemas.push(s3);

  // 4. NEURAL
  const s4 = new SistemaEnergetico();
  s4.tipo = TipoEnergia.NEURAL;
  s4.nome = "Sistema Nervoso / Comunicacao";
  s4.analogia_corpo = "Neuronios disparam potenciais de acao -- sinais eletricos. O corpo tem uma REDE de comunicacao interna (87 bilhoes de neuronios). Consome 20W, incrivelmente eficiente. O cerebro pesa 2% do corpo mas consome 20% da energia.";
  s4.analogia_civilizacao = "Internet, telecomunicacoes, radio. A internet e o SISTEMA NERVO da civilizacao. Cada mensagem, cada video, cada chamada e um potencial de acao em escala planetaria. Banda = largura de axonio.";
  s4.escala = EscalaEnergia.PLANETA;
  s4.fluxo.inputs = [TipoInput.INFORMACAO, TipoInput.LUZ];
  s4.fluxo.conversao = "Sinal eletrico / optico -> transmissao";
  s4.fluxo.output = "Comunicacao / sinal / dados transmitidos";
  s4.fluxo.residuos = [TipoResiduo.RUIDO, TipoResiduo.CALOR, TipoResiduo.DADOS_DESCARTADOS];
  s4.fluxo.eficiencia_pct = 35.0;
  s4.consumo_corpo_pct = 20.0;
  s4.observacao = "LACUNA CRITICA: a Republica NAO tem OpenNetwork/OpenInternet. Quem controla a rede controla o sistema nervoso. Banda gratuita e NECESSARIA (energia neural = direito).";
  sistemas.push(s4);

  // 5. QUIMICA
  const s5 = new SistemaEnergetico();
  s5.tipo = TipoEnergia.QUIMICA;
  s5.nome = "Sintese / Ligacoes";
  s5.analogia_corpo = "O corpo SINTETIZA moleculas -- proteinas, hormonios, enzimas. Ligacoes quimicas ARMAZENAM energia. Digestao = quebrar ligacoes para liberar. Sintese = gastar energia para construir.";
  s5.analogia_civilizacao = "Industria quimica, baterias, combustiveis, farmacia. Toda manufatura e energia quimica direcionada. FarmLab opera aqui -- sintese de medicamentos e energia quimica a servico da vida.";
  s5.escala = EscalaEnergia.CIVILIZACAO;
  s5.fluxo.inputs = [TipoInput.ALIMENTO];
  s5.fluxo.conversao = "Reacao quimica (sintese / decomposicao)";
  s5.fluxo.output = "Moleculas / materiais / medicamentos";
  s5.fluxo.residuos = [TipoResiduo.RESIDUO_TOXICO, TipoResiduo.CALOR];
  s5.fluxo.eficiencia_pct = 30.0;
  s5.consumo_corpo_pct = 10.0;
  s5.observacao = "FarmLab cobre farmacia. OpenChemistry cobre industria quimica.";
  sistemas.push(s5);

  // 6. SENSORIAL
  const s6 = new SistemaEnergetico();
  s6.tipo = TipoEnergia.SENSORIAL;
  s6.nome = "Transducao / Percepcao";
  s6.analogia_corpo = "Olhos capturam FOTONS. Ouvidos capturam VIBRACOES. Pele captura CALOR. O corpo e um RECEPTOR de energia -- converte formas externas em sinais internos. Cada sentido e um TRANSDUTOR energetico.";
  s6.analogia_civilizacao = "Cameras, microfones, sensores, instrumentos cientificos. OpenTelefonista opera aqui -- o smartphone como CORPO ESTENDIDO captura energia do ambiente (luz, som, posicao) e converte em percepcao. Cego ve obstaculos. Surdo le labios.";
  s6.escala = EscalaEnergia.CORPO;
  s6.fluxo.inputs = [TipoInput.LUZ, TipoInput.SOM, TipoInput.CALOR_AMBIENTE];
  s6.fluxo.conversao = "Transducao sensorial (foton/fonon -> sinal neural)";
  s6.fluxo.output = "Percepcao / dados sensoriais";
  s6.fluxo.residuos = [TipoResiduo.RUIDO, TipoResiduo.FADIGA_MENTAL];
  s6.fluxo.eficiencia_pct = 70.0;
  s6.consumo_corpo_pct = 5.0;
  s6.observacao = "OpenTelefonista cobre (smartphone como corpo estendido). OpenInclusiveHardware (44 dispositivos) amplia. OpenInclusiveIDE integra para desenvolvimento.";
  sistemas.push(s6);

  // 7. COGNITIVA
  const s7 = new SistemaEnergetico();
  s7.tipo = TipoEnergia.COGNITIVA;
  s7.nome = "Cerebro / Processamento";
  s7.analogia_corpo = "O cerebro CONSOME 20% da energia do corpo pesando 2%. PENSAR E CARO energeticamente. O cansaco mental e real -- e gasto energetico, nao frescura. Resolver um problema matematico gasta mais glicose que assistir TV.";
  s7.analogia_civilizacao = "Computacao, IA, analise de dados. Um data center consome tanta energia quanto uma cidade. Processar informacao TEM CUSTO ENERGETICO -- nao e gratuito. P8: IA amplifica inteligencia humana, NAO substitui. Mas o custo de computar e REAL e precisa alocacao.";
  s7.escala = EscalaEnergia.CIVILIZACAO;
  s7.fluxo.inputs = [TipoInput.INFORMACAO, TipoInput.ALIMENTO];
  s7.fluxo.conversao = "Processamento (neural / digital)";
  s7.fluxo.output = "Decisao / calculo / conhecimento";
  s7.fluxo.residuos = [TipoResiduo.FADIGA_MENTAL, TipoResiduo.CALOR, TipoResiduo.DADOS_DESCARTADOS];
  s7.fluxo.eficiencia_pct = 15.0;
  s7.consumo_corpo_pct = 20.0;
  s7.observacao = "HumanKnowledge (multi-AI + verificacao) cobre parcialmente. P8 define o principio (IA = instrumento). Custo computacional como recurso a alocar = LACUNA.";
  sistemas.push(s7);

  // 8. ATENCIONAL
  const s8 = new SistemaEnergetico();
  s8.tipo = TipoEnergia.ATENCIONAL;
  s8.nome = "Foco / Atencao";
  s8.analogia_corpo = "A atencao e FINITA. Voce nao consegue focar em tudo. Focar GASTA energia cognitiva. O cerebro tem um BUDGET de atencao -- distribui entre tarefas. Dormir mal = budget de atencao menor no dia seguinte.";
  s8.analogia_civilizacao = "A energia que FocusGuard protege. O scroll infinito DRENA energia atencional. A 'economia da atencao' e a forma mais NOVA de exploracao energetica -- plataformas capturam sua atencao e vendem. P8 exige proteger esta energia. AntiSpamCall protege parcialmente.";
  s8.escala = EscalaEnergia.CORPO;
  s8.fluxo.inputs = [TipoInput.SONO, TipoInput.INFORMACAO];
  s8.fluxo.conversao = "Filtro atencional (top-down + bottom-up)";
  s8.fluxo.output = "Foco / atencao direcionada";
  s8.fluxo.residuos = [TipoResiduo.FADIGA_MENTAL, TipoResiduo.RUIDO];
  s8.fluxo.eficiencia_pct = 10.0;
  s8.consumo_corpo_pct = 0.0;
  s8.observacao = "FocusGuard (overlay IDE) cobre parcialmente. AntiSpamCall ('para de me encher o saco') protege. OpenContentPolicy (midia, ruido) protege. Politica mais ampla de atencao como recurso energetico finito = LACUNA.";
  sistemas.push(s8);

  // 9. EMOCIONAL
  const s9 = new SistemaEnergetico();
  s9.tipo = TipoEnergia.EMOCIONAL;
  s9.nome = "Motivacao / Drive";
  s9.analogia_corpo = "Motivacao, drive, vontade. Em termos fisicos: dopamina, noradrenalina, cortisol -- moleculas que MODULAM quanto de outras energias o corpo vai despender. Sem dopamina, o corpo tem ATP mas nao se MOVE. A depressao e crise energetica emocional -- o combustivel existe, mas o motor nao liga.";
  s9.analogia_civilizacao = "O kaizen (1% ao dia) opera aqui. Curiosidade, progresso, desafio, recompensa, pertencimento -- os 5 gatilhos psicologicos sao GERADORES de energia emocional. O Huxley soma (dopamina artificial do scroll) e o SEQUESTRO desta energia -- drena ao inves de gerar.";
  s9.escala = EscalaEnergia.COMUNIDADE;
  s9.fluxo.inputs = [TipoInput.PRESENCA, TipoInput.SONO, TipoInput.INFORMACAO];
  s9.fluxo.conversao = "Modulacao neuroquimica (dopamina/serotonina/cortisol)";
  s9.fluxo.output = "Motivacao / drive / vontade de agir";
  s9.fluxo.residuos = [TipoResiduo.SOLIDAO, TipoResiduo.FADIGA_MENTAL];
  s9.fluxo.eficiencia_pct = 20.0;
  s9.consumo_corpo_pct = 0.0;
  s9.observacao = "LACUNA CRITICA: nenhum modulo trata saude mental como INFRAESTRUTURA ENERGETICA. Depressao = deficit energetico. Burnout = deplecao. Kaizen e gerador, mas falta sistema.";
  sistemas.push(s9);

  // 10. RELACIONAL
  const s10 = new SistemaEnergetico();
  s10.tipo = TipoEnergia.RELACIONAL;
  s10.nome = "Social / Conexao";
  s10.analogia_corpo = "O ser humano isolado DEGRADA. Solidao cronica aumenta mortalidade em 26%. O corpo PRECISA de conexao para funcionar bem -- nao e luxo, e necessidade energetica. Oxitocina, espelhamento neural, co-regulacao.";
  s10.analogia_civilizacao = "A assembleia, o mutirao, a cooperativa. O Two-Person Rule nao e so procedimento -- e ARQUITETURA ENERGETICA. Duas pessoas juntas fazem mais que duas separadas. A energia social e SINERGICA: 1+1 > 2. Quando a assembleia polariza (P9), e esta energia que se GASTA em atrito em vez de gerar valor.";
  s10.escala = EscalaEnergia.COMUNIDADE;
  s10.fluxo.inputs = [TipoInput.PRESENCA];
  s10.fluxo.conversao = "Co-regulacao neuroquimica + espelhamento neural";
  s10.fluxo.output = "Cooperacao / sinergia / vinculo";
  s10.fluxo.residuos = [TipoResiduo.SOLIDAO];
  s10.fluxo.eficiencia_pct = 80.0;
  s10.consumo_corpo_pct = 0.0;
  s10.observacao = "OpenCommunities (6 adaptacoes) cobre parcialmente. OpenConstituentAssembly (governanca) cobre parcialmente. OpenCrowdsourcing (ajuda mutua) cobre parcialmente. P9 (anti-polarizacao) PROTEGE esta energia. Tratar conexao como recurso energetico mensuravel = LACUNA.";
  sistemas.push(s10);

  return sistemas;
}

function _init_coberturas() {
  const coberturas = [];

  const c1 = new CoberturaRepublica();
  c1.tipo = TipoEnergia.CELULAR; c1.nivel = NivelCobertura.COBERTO;
  c1.modulos = ["open-energy", "open-agrarian-revolution", "open-credit"];
  coberturas.push(c1);

  const c2 = new CoberturaRepublica();
  c2.tipo = TipoEnergia.MECANICA; c2.nivel = NivelCobertura.PARCIAL;
  c2.modulos = ["open-athlete", "open-martial-arts"];
  c2.lacunas = ["sistema de transporte publico gratuito (OpenMobility)"];
  coberturas.push(c2);

  const c3 = new CoberturaRepublica();
  c3.tipo = TipoEnergia.TERMICA; c3.nivel = NivelCobertura.PARCIAL;
  c3.modulos = ["open-energy"];
  c3.lacunas = ["politica de cozimento comunitario", "aquecimento como direito"];
  coberturas.push(c3);

  const c4 = new CoberturaRepublica();
  c4.tipo = TipoEnergia.NEURAL; c4.nivel = NivelCobertura.LACUNA;
  c4.lacunas = [
    "OpenNetwork/OpenInternet -- banda gratuita como direito",
    "sistema nervoso da civilizacao sem dono",
    "neutralidade de rede como P1 (anti-elitismo)"
  ];
  coberturas.push(c4);

  const c5 = new CoberturaRepublica();
  c5.tipo = TipoEnergia.QUIMICA; c5.nivel = NivelCobertura.PARCIAL;
  c5.modulos = ["open-chemistry", "open-physics"];
  c5.lacunas = ["FarmLab completo (sintese CC0 de medicamentos)"];
  coberturas.push(c5);

  const c6 = new CoberturaRepublica();
  c6.tipo = TipoEnergia.SENSORIAL; c6.nivel = NivelCobertura.COBERTO;
  c6.modulos = ["open-telefonista", "open-inclusive-hardware", "open-inclusive-ide"];
  coberturas.push(c6);

  const c7 = new CoberturaRepublica();
  c7.tipo = TipoEnergia.COGNITIVA; c7.nivel = NivelCobertura.PARCIAL;
  c7.modulos = ["open-human-knowledge", "open-human-amplification"];
  c7.lacunas = ["alocacao de custo computacional como recurso energetico"];
  coberturas.push(c7);

  const c8 = new CoberturaRepublica();
  c8.tipo = TipoEnergia.ATENCIONAL; c8.nivel = NivelCobertura.PARCIAL;
  c8.modulos = ["open-focus-guard", "open-anti-spam-call", "open-content-policy"];
  c8.lacunas = ["politica ampla de atencao como recurso energetico finito"];
  coberturas.push(c8);

  const c9 = new CoberturaRepublica();
  c9.tipo = TipoEnergia.EMOCIONAL; c9.nivel = NivelCobertura.LACUNA;
  c9.lacunas = [
    "OpenMentalHealth -- saude mental como INFRAESTRUTURA ENERGETICA",
    "sistema de deteccao de deplecao emocional (burnout/depressao)",
    "geradores de energia emocional (kaizen, pertencimento, proposito)"
  ];
  coberturas.push(c9);

  const c10 = new CoberturaRepublica();
  c10.tipo = TipoEnergia.RELACIONAL; c10.nivel = NivelCobertura.PARCIAL;
  c10.modulos = ["open-communities", "open-constituent-assembly", "open-anti-polarization"];
  c10.lacunas = ["conexao como recurso energetico mensuravel e protegido"];
  coberturas.push(c10);

  return coberturas;
}

class EnergyTaxonomyEngine {
  constructor() {
    this.sistemas = _init_sistemas();
    this.coberturas = _init_coberturas();
    this.diagnosticos = {};
  }

  listar_sistemas() {
    return [...this.sistemas].sort((a, b) => a.tipo.numero - b.tipo.numero);
  }

  sistema_por_tipo(tipo) {
    return this.sistemas.find(s => s.tipo === tipo) || null;
  }

  coberturas_por_nivel(nivel) {
    return this.coberturas.filter(c => c.nivel === nivel);
  }

  lacunas_identificadas() {
    return this.coberturas
      .filter(c => c.nivel === NivelCobertura.LACUNA || c.nivel === NivelCobertura.PARCIAL)
      .map(c => ({ tipo: c.tipo, lacunas: c.lacunas }));
  }

  diagnosticar(entidade, status) {
    const diag = new DiagnosticoEnergetico();
    diag.entidade = entidade;
    for (const [t, st] of Object.entries(status)) {
      diag.status_por_tipo[t.id] = st;
    }
    for (const [t, st] of Object.entries(status)) {
      if ([StatusDisponibilidade.LIMITADA, StatusDisponibilidade.CRITICA, StatusDisponibilidade.DEPLETADA].includes(st)) {
        diag.tipos_em_deficit.push(t);
      } else if (st === StatusDisponibilidade.ABUNDANTE) {
        diag.tipos_abundantes.push(t);
      }
    }
    if (diag.tipos_em_deficit.length >= 4) {
      diag.veredito = "CRITICO: multiplas deficiencias energeticas. Intervencao sistemica.";
    } else if (diag.tipos_em_deficit.length >= 2) {
      diag.veredito = "ATENCAO: deficiencias energeticas em sistemas chave.";
    } else if (diag.tipos_em_deficit.length > 0) {
      const nomes = diag.tipos_em_deficit.map(t => t.rotulo.split("(")[0].trim()).join(", ");
      diag.veredito = `DEFICIT LOCAL: ${nomes}. Tratar antes de propagar.`;
    } else {
      diag.veredito = "SAUDAVEL: todos os sistemas energeticos em equilibrio ou abundancia.";
    }
    this.diagnosticos[entidade] = diag;
    return diag;
  }

  padrao_universal() {
    return "PADRAO UNIVERSAL: INPUT -> CONVERSAO -> OUTPUT -> RESIDUO\n" +
           "Nada se cria. Tudo se transforma.\n" +
           "Nao existe trabalho sem energia.\n" +
           "Nao existe energia sem input.\n" +
           "Nao existe output sem residuo.\n" +
           "A questao civilizatoria nunca foi 'como conseguir energia' -- sempre foi 'como TRANSFORMAR com justica e sem desperdiciar'.";
  }

  scorecard() {
    const total = this.sistemas.length;
    const cobertos = this.coberturas_por_nivel(NivelCobertura.COBERTO).length;
    const parciais = this.coberturas_por_nivel(NivelCobertura.PARCIAL).length;
    const lacunas = this.coberturas_por_nivel(NivelCobertura.LACUNA).length;
    const total_lacunas_itens = this.coberturas.reduce((sum, c) => sum + c.lacunas.length, 0);
    const pct_coberto = total > 0 ? Math.round((cobertos / total) * 1000) / 10 : 0;
    return {
      sistemas_total: total,
      totalmente_cobertos: cobertos,
      parcialmente_cobertos: parciais,
      lacunas_criticas: lacunas,
      itens_faltantes: total_lacunas_itens,
      pct_cobertura: pct_coberto,
      diagnosticos_realizados: Object.keys(this.diagnosticos).length,
    };
  }
}

function _demo() {
  const e = new EnergyTaxonomyEngine();

  console.log("=".repeat(70));
  console.log("OpenEnergyTaxonomy -- Os 10 Sistemas Energeticos");
  console.log("Do Corpo Humano a Civilizacao");
  console.log("=".repeat(70));

  console.log("\n[OS 10 SISTEMAS ENERGETICOS]");
  for (const s of e.listar_sistemas()) {
    console.log(`\n  --- Sistema ${s.tipo.numero}: ${s.tipo.rotulo} ---`);
    console.log(`  Escala: ${s.escala.rotulo}`);
    console.log(`  CORPO: ${s.analogia_corpo}`);
    console.log(`  CIVILIZACAO: ${s.analogia_civilizacao}`);
    if (s.consumo_corpo_pct > 0) {
      console.log(`  Consumo no corpo: ${s.consumo_corpo_pct}% do orcamento energetico`);
    }
    const f = s.fluxo;
    console.log(`  FLUXO: [${f.inputs.map(i => i.rotulo).join(", ")}] -> ${f.conversao}`);
    console.log(`         -> ${f.output}`);
    console.log(`         -> RESIDUO: [${f.residuos.map(r => r.rotulo).join(", ")}]`);
    console.log(`  EFICIENCIA: ${f.eficiencia_pct}%`);
    if (s.observacao) console.log(`  OBS: ${s.observacao}`);
  }

  console.log("\n" + "=".repeat(70));
  console.log("[O PADRAO UNIVERSAL]");
  console.log("=".repeat(70));
  console.log("\n" + e.padrao_universal());

  console.log("\n[EXEMPLOS CORPO -> CIVILIZACAO]");
  for (const s of e.listar_sistemas()) {
    const corpo_curto = s.analogia_corpo.split(".")[0].trim();
    const civ_curto = s.analogia_civilizacao.split(".")[0].trim();
    console.log(`  ${String(s.tipo.numero).padStart(2, " ")}. ${s.tipo.rotulo}`);
    console.log(`      Corpo: ${corpo_curto}`);
    console.log(`      Civil: ${civ_curto}`);
  }

  console.log("\n" + "=".repeat(70));
  console.log("[COBERTURA DA REPUBLICA -- O QUE FALTA]");
  console.log("=".repeat(70));
  for (const c of e.coberturas) {
    const flagMap = { coberto: "OK", parcial: "PARCIAL", lacuna: "LACUNA", nao_aplicavel: "N/A" };
    const flag = flagMap[c.nivel.id] || "N/A";
    console.log(`\n  [${flag}] ${c.tipo.rotulo}`);
    if (c.modulos.length) console.log(`  Modulos: ${c.modulos.join(", ")}`);
    if (c.lacunas.length) {
      console.log("  LACUNAS:");
      for (const lac of c.lacunas) console.log(`    - ${lac}`);
    }
  }

  console.log("\n" + "=".repeat(70));
  console.log("[LACUNAS CRITICAS -- MODULOS QUE PRECISAM EXISTIR]");
  console.log("=".repeat(70));
  const lacunas = e.coberturas_por_nivel(NivelCobertura.LACUNA);
  for (const c of lacunas) {
    console.log(`\n  ${c.tipo.rotulo}:`);
    for (const lac of c.lacunas) console.log(`    - ${lac}`);
  }
  if (!lacunas.length) console.log("  (nenhuma lacuna critica)");

  console.log("\n" + "=".repeat(70));
  console.log("[DIAGNOSTICO ENERGETICO -- Pessoa: Maria]");
  console.log("=".repeat(70));
  const mariaStatus = {
    [TipoEnergia.CELULAR]: StatusDisponibilidade.EQUILIBRADA,
    [TipoEnergia.MECANICA]: StatusDisponibilidade.EQUILIBRADA,
    [TipoEnergia.TERMICA]: StatusDisponibilidade.ABUNDANTE,
    [TipoEnergia.NEURAL]: StatusDisponibilidade.ABUNDANTE,
    [TipoEnergia.QUIMICA]: StatusDisponibilidade.EQUILIBRADA,
    [TipoEnergia.SENSORIAL]: StatusDisponibilidade.EQUILIBRADA,
    [TipoEnergia.COGNITIVA]: StatusDisponibilidade.LIMITADA,
    [TipoEnergia.ATENCIONAL]: StatusDisponibilidade.CRITICA,
    [TipoEnergia.EMOCIONAL]: StatusDisponibilidade.DEPLETADA,
    [TipoEnergia.RELACIONAL]: StatusDisponibilidade.EQUILIBRADA,
  };
  const diag_maria = e.diagnosticar("pessoa:Maria", mariaStatus);
  console.log(`  Entidade: ${diag_maria.entidade}`);
  for (const [tid, st] of Object.entries(diag_maria.status_por_tipo).sort()) {
    console.log(`    ${tid.padEnd(20, ".")} ${st.rotulo || st}`);
  }
  console.log(`  Em deficit: [${diag_maria.tipos_em_deficit.map(t => t.rotulo.split("(")[0].trim()).join(", ")}]`);
  console.log(`  Abundantes: [${diag_maria.tipos_abundantes.map(t => t.rotulo.split("(")[0].trim()).join(", ")}]`);
  console.log(`  VEREDITO: ${diag_maria.veredito}`);

  console.log("\n[DIAGNOSTICO ENERGETICO -- Comunidade: Solar Village]");
  const svStatus = {
    [TipoEnergia.CELULAR]: StatusDisponibilidade.ABUNDANTE,
    [TipoEnergia.MECANICA]: StatusDisponibilidade.EQUILIBRADA,
    [TipoEnergia.TERMICA]: StatusDisponibilidade.ABUNDANTE,
    [TipoEnergia.NEURAL]: StatusDisponibilidade.LIMITADA,
    [TipoEnergia.QUIMICA]: StatusDisponibilidade.EQUILIBRADA,
    [TipoEnergia.SENSORIAL]: StatusDisponibilidade.EQUILIBRADA,
    [TipoEnergia.COGNITIVA]: StatusDisponibilidade.EQUILIBRADA,
    [TipoEnergia.ATENCIONAL]: StatusDisponibilidade.EQUILIBRADA,
    [TipoEnergia.EMOCIONAL]: StatusDisponibilidade.ABUNDANTE,
    [TipoEnergia.RELACIONAL]: StatusDisponibilidade.ABUNDANTE,
  };
  const diag_sv = e.diagnosticar("comunidade:solar_village", svStatus);
  console.log(`  Entidade: ${diag_sv.entidade}`);
  console.log(`  Em deficit: [${diag_sv.tipos_em_deficit.map(t => t.rotulo.split("(")[0].trim()).join(", ")}]`);
  console.log(`  Abundantes: [${diag_sv.tipos_abundantes.map(t => (t && t.rotulo ? t.rotulo.split("(")[0].trim() : "")).join(", ")}]`);
  console.log(`  VEREDITO: ${diag_sv.veredito}`);

  console.log("\n" + "=".repeat(70));
  console.log("[SCORECARD DA TAXONOMIA ENERGETICA]");
  console.log("=".repeat(70));
  const sc = e.scorecard();
  for (const [k, v] of Object.entries(sc)) {
    console.log(`  ${k.padEnd(28, ".")} ${v}`);
  }

  console.log("\n" + "=".repeat(70));
  console.log("FILOSOFIA -- Energia e a bateria do trabalho");
  console.log("=".repeat(70));
  console.log(`'Energia e a bateria do trabalho. Nosso corpo so funciona porque
temos energia. Nada foi feito na Terra por humanos sem a necessidade
de energia.'

O corpo humano nao tem UM sistema de energia. Tem DEZ.
Cada um com input, conversao, output e residuo.
A civilizacao herda essa estrutura -- somos um corpo em escala.

OpenEnergy cobre o sistema 1 (eletrico = ATP).
Mas existem outros 9 que a Republica precisa tratar:

NEURAL (sistema nervoso = internet):
  Quem controla a rede controla o sistema nervoso da civilizacao.
  Banda gratuita e NECESSARIA. A internet e o nervo. Sem nervo, paralisia.

COGNITIVA (cerebro = computacao):
  Processar informacao TEM CUSTO ENERGETICO. IA nao e gratuita.
  P8 exige que esse custo seja alocado democraticamente, nao por dinheiro.

ATENCIONAL (foco = atencao finita):
  A atencao e o recurso mais explorado do seculo XXI.
  Plataformas capturam sua atencao e vendem. Isso e EXTRATIVISMO ENERGETICO.
  FocusGuard e o comeco. Proteger atencao = proteger energia.

EMOCIONAL (motivacao = drive):
  Depressao e CRISE ENERGETICA. O combustivel existe (ATP), mas o motor
  nao liga (sem dopamina). Saude mental nao e luxo terapeutico --
  e INFRAESTRUTURA ENERGETICA. Sem motivacao, nenhuma outra energia se move.

RELACIONAL (social = conexao):
  O ser humano isolado DEGRADA. Conexao e necessidade energetica.
  A assembleia, o mutirao, a cooperativa sao GERADORES de energia relacional.
  P9 protege esta energia do atrito da polarizacao.

A LEI DE TODOS OS 10:
  INPUT -> CONVERSAO -> OUTPUT -> RESIDUO.
  Nada se cria, tudo se transforma.
  A Republica nao cria energia. TRANSFORMA.
  E transforma COM JUSTICA: sem desperdicio, sem exclusao, semElite.
`);
}

if (require.main === module) {
  _demo();
}

module.exports = { EnergyTaxonomyEngine, TipoEnergia, StatusDisponibilidade };