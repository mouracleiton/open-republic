# OpenEnergy -- Energia Gratuita para Todo e Qualquer Uso

**Arquivo original:** `open-republic/core/open_energy.py`

**Descricao:** =========================================================
A Republica ABOLI a energia como mercadoria.
Assim como a Revolucao Agraria extinguiu a propriedade da terra,
a Revolucao Energetica extingue o conceito de "conta de luz".
Energia nao se compra. Nao se vende. Nao se mede para cobrar.
Nao gera divida. Nao corta. Nao raciona por dinheiro.
ENERGIA E DIREITO. PONTO.
PRINCIPIO: "Para todo e qualquer uso."
A Republica nao pergunta PARA QUE voce precisa de energia.
Assim como nao pergunta para que voce precisa de ar.
Energia e condicao de vida moderna: cozinhar, aquecer, iluminar,
comunicar, curar, estudar, trabalhar, criar.
MAS COMO ISSO FUNCIONA SEM TRAGEDIA DOS COMUNS?
A logica capital diz: se energia e gratis, todo mundo desperdica.
Falso. A logica capital projeta o COMPORTAMENTO DO CAPITALISTA
para dentro do cidadao. O capitalista desperdica porque desperdico
e EXTERNO ao seu lucro. O cidadao da Republica SABE que a energia
que ele desperdica e a que falta para o vizinho.
A Republica nao resolve abundancia com ESCASSEZ ARTIFICIAL (preco).
Resolve com GERACAO DISTRIBUIDA: cada comunidade gera a propria energia.
Quanto mais gera, mais independente. Quanto mais eficiente, mais excedente
para doar. Eficiencia nao economiza dinheiro -- LIBERTA capacidade.
O UNICO MOMENTO DE ESCASSEZ (e como se resolve):
Quando geracao nao cobre demanda (seca extrema, falha de infraestrutura),
a assembleia decide alocacao -- NUNCA o preco. Hospitais e essenciais
primeiro. Depois, rotacao democratica. Ninguem fica sem energia por dinheiro.
ALINHAMENTO CONSTITUCIONAL:
- P1: Energia como mercadoria exclui quem nao tem dinheiro. Abolir = anti-elitismo.
- P2: Autonomia energetica = autonomia corporal (corpo precisa de calor, comida, luz).
- P3: Trabalho igual, diferenca so por impacto. Consumir energia nao e trabalho.
  Quem consome mais NAO recebe mais credito por isso.
- P4: Assembleia decide alocacao em escassez, nao o mercado.
- P6: Acesso universal = energia e direito, como conhecimento.
Author: OpenRepublic Team

---

```portugol

// !/usr/bin/env python3
// 
OpenEnergy -- Energia Gratuita para Todo e Qualquer Uso
=========================================================
A Republica ABOLI a energia como mercadoria.

Assim como a Revolucao Agraria extinguiu a propriedade da terra,
a Revolucao Energetica extingue o conceito de "conta de luz".

Energia nao se compra. Nao se vende. Nao se mede para cobrar.
Nao gera divida. Nao corta. Nao raciona por dinheiro.

ENERGIA E DIREITO. PONTO.

PRINCIPIO: "Para todo e qualquer uso."
A Republica nao pergunta PARA QUE voce precisa de energia.
Assim como nao pergunta para que voce precisa de ar.
Energia e condicao de vida moderna: cozinhar, aquecer, iluminar,
comunicar, curar, estudar, trabalhar, criar.

MAS COMO ISSO FUNCIONA SEM TRAGEDIA DOS COMUNS?

A logica capital diz: se energia e gratis, todo mundo desperdica.
Falso. A logica capital projeta o COMPORTAMENTO DO CAPITALISTA
para dentro do cidadao. O capitalista desperdica porque desperdico
e EXTERNO ao seu lucro. O cidadao da Republica SABE que a energia
que ele desperdica e a que falta para o vizinho.

A Republica nao resolve abundancia com ESCASSEZ ARTIFICIAL (preco).
Resolve com GERACAO DISTRIBUIDA: cada comunidade gera a propria energia.
Quanto mais gera, mais independente. Quanto mais eficiente, mais excedente
para doar. Eficiencia nao economiza dinheiro -- LIBERTA capacidade.

O UNICO MOMENTO DE ESCASSEZ (e como se resolve):
Quando geracao nao cobre demanda (seca extrema, falha de infraestrutura),
a assembleia decide alocacao -- NUNCA o preco. Hospitais e essenciais
primeiro. Depois, rotacao democratica. Ninguem fica sem energia por dinheiro.

ALINHAMENTO CONSTITUCIONAL:
- P1: Energia como mercadoria exclui quem nao tem dinheiro. Abolir = anti-elitismo.
- P2: Autonomia energetica = autonomia corporal (corpo precisa de calor, comida, luz).
- P3: Trabalho igual, diferenca so por impacto. Consumir energia nao e trabalho.
  Quem consome mais NAO recebe mais credito por isso.
- P4: Assembleia decide alocacao em escassez, nao o mercado.
- P6: Acesso universal = energia e direito, como conhecimento.

Author: OpenRepublic Team
// 
// importa annotations de __future__
// importa Any, Dict, List, Optional, Tuple, Set de typing
// importa Enum de enum
// importa dataclass, field de dataclasses
// importa defaultdict de collections
// importa datetime de datetime


// ============================================================================
// 1. ENUMS (modulo-level)
// ============================================================================

classe FonteEnergia herda de Enum:
    // Fontes de geracao de energia na Republica.
    SOLAR <- ("solar", "Solar fotovoltaica", VERDADEIRO)  // renovavel
    EOLICA <- ("eolica", "Eolica (vento)", VERDADEIRO)  // renovavel
    HIDRO <- ("hidro", "Hidroeletrica", VERDADEIRO)  // renovavel
    GEOTERMICA <- ("geotermica", "Geotermica", VERDADEIRO)  // renovavel
    BIOMASSA <- ("biomassa", "Biomassa", VERDADEIRO)  // renovavel
    MARES <- ("mares", "Das mars e correntes", VERDADEIRO)  // renovavel
    NUCLEAR <- ("nuclear", "Nuclear (fissao)", FALSO)  // nao-renovavel, controversial
    FUSAO <- ("fusao", "Fusao nuclear (futura)", VERDADEIRO)  // renovavel (tecnologica)

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]

    // decorador: @property
    funcao renovavel(self) retorna bool:
        retorne self.value[2]


classe TipoConsumo herda de Enum:
    // Categorias de consumo de energia (para alocacao em escassez, NAO para cobrar).
    ESSENCIAL_VIDA <- ("essencial_vida", "Essencial a vida (cozinhar, aquecer, iluminar, agua)", 1)
    SAUDE <- ("saude", "Saude (hospitais, clinicas, equipamentos medicos)", 1)
    COMUNICACAO <- ("comunicacao", "Comunicacao (internet, telefone, radio)", 1)
    EDUCACAO <- ("educacao", "Educacao (escolas, bibliotecas, laboratorios)", 2)
    MOBILIDADE <- ("mobilidade", "Mobilidade (transporte publico, veiculos)", 2)
    PRODUCAO_ALIMENTOS <- ("producao_alimentos", "Producao de alimentos (irrigacao, processamento)", 2)
    INFRAESTRUTURA_COMUM <- ("infraestrutura", "Infraestrutura comum (agua, esgoto, iluminacao publica)", 2)
    PRODUCAO_BENS <- ("producao_bens", "Producao de bens (fabril, artesanal)", 3)
    CULTURA_LAZER <- ("cultura_lazer", "Cultura e lazer (teatro, musica, esporte)", 3)
    PESQUISA_INOVACAO <- ("pesquisa", "Pesquisa e inovacao (laboratorios, computacao)", 3)
    RESIDENCIAL_EXCEDENTE <- ("residencial_excedente", "Residencial excedente (alem do essencial)", 4)

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]

    // decorador: @property
    funcao prioridade(self) retorna int:
        // 1=maxima prioridade (essencial), 4=minima. So usado em escassez real.
        retorne self.value[2]


classe TipoArmazenamento herda de Enum:
    // Metodos de armazenamento de energia.
    BATERIA_LITIO <- ("bateria_litio", "Bateria de lítio-ion")
    BATERIA_SODIO <- ("bateria_sodio", "Bateria de sodio (mais barato, menos denso)")
    BATERIA_FLUXO <- ("bateria_fluxo", "Bateria de fluxo redox (escala grid)")
    HIDRO_BOMBEADA <- ("hidro_bombeada", "Hidroeletrica reversivel (bombeada)")
    GRAVIDADE <- ("gravidade", "Armazenamento por gravidade (pesos)")
    HIDROGENIO <- ("hidrogenio", "Hidrogenio verde (eletrolise)")
    AR_COMPRIMIDO <- ("ar_comprimido", "Ar comprimido (CAES)")
    TERMICO <- ("termico", "Armazenamento termico (sal fundido, agua quente)")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe StatusCenario herda de Enum:
    // Cenarios de equilibrio entre oferta e demanda.
    ABUNDANCIA <- ("abundancia", "Abundancia: geracao supera demanda")
    EQUILIBRIO <- ("equilibrio", "Equilibrio: geracao = demanda")
    ATENCAO <- ("atencao", "Atencao: margem baixa (<10%)")
    ESCASSEZ <- ("escassez", "Escassez: demanda supera geracao")
    EMERGENCIA <- ("emergencia", "Emergencia: deficit critico, assembleia decide")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe StatusInterconexao herda de Enum:
    // Estado da conexao entre microgrids.
    ILHADO <- ("ilhado", "Ilhado: microgrid autonomo (sem conexao externa)")
    CONECTADO <- ("conectado", "Conectado a rede regional")
    EXPORTANDO <- ("exportando", "Exportando excedente (doacao)")
    IMPORTANDO <- ("importando", "Importando (recebendo doacao)")
    MANUTENCAO <- ("manutencao", "Em manutencao")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


// ============================================================================
// 2. DATACLASSES
// ============================================================================

// decorador: @dataclass
classe UnidadeGeracao:
    // Uma unidade de geracao de energia numa comunidade.
    id: str
    fonte: FonteEnergia
    capacidade_kw: float           // capacidade nominal
    declare producao_atual_kw: float  <- 0.0  // producao real no momento
    declare comunidade_id: str  <- ""
    declare status: str  <- "operacional"  // operacional, manutencao, offline
    declare sustentabilidade_pct: float  <- 100.0  // impacto ambiental (100=zero impacto)


// decorador: @dataclass
classe UnidadeArmazenamento:
    // Bateria ou reserva de energia.
    id: str
    tipo: TipoArmazenamento
    capacidade_kwh: float
    declare carga_atual_kwh: float  <- 0.0
    declare comunidade_id: str  <- ""
    declare ciclos_vida: int  <- 0  // ciclos restantes (degradacao)


// decorador: @dataclass
classe ConsumoRegistrado:
    // Um registro de consumo (NAO para cobrar -- para PLANEJAR geracao).
    id: str
    comunidade_id: str
    tipo: TipoConsumo
    consumo_kw: float
    declare timestamp: str  <- ""
    declare cidadao_ou_setor: str  <- ""  // quem consumiu (anonimizado se pessoal)


// decorador: @dataclass
classe Microgrid:
    // Uma microgrid comunitaria auto-suficiente.
    id: str
    nome: str
    comunidade_id: str
    declare unidades_geracao: List[str]  <- field(default_factory=list)
    declare unidades_armazenamento: List[str]  <- field(default_factory=list)
    declare interconexao: StatusInterconexao  <- StatusInterconexao.ILHADO
    declare autonomia_horas: float  <- 0.0  // quantas horas sobrevive ilhado
    // metricas (calculadas pelo engine)
    declare geracao_total_kw: float  <- 0.0
    declare demanda_total_kw: float  <- 0.0
    declare cenario: StatusCenario  <- StatusCenario.EQUILIBRIO


// decorador: @dataclass
classe AlocacaoEscassez:
    // Decisao democratica de alocacao em momento de escassez.
    id: str
    microgrid_id: str
    deficit_kw: float
    declare tipos_priorizados: List[TipoConsumo]  <- field(default_factory=list)
    declare tipos_rotacionados: List[TipoConsumo]  <- field(default_factory=list)  // rodizio
    declare tipos_suprimidos: List[TipoConsumo]  <- field(default_factory=list)  // cortados
    declare duracao_estimada_h: float  <- 0.0
    declare aprovado_em_assembleia: bool  <- FALSO
    declare justificativa: str  <- ""


// ============================================================================
// 3. ENGINE
// ============================================================================

classe EnergiaEngine:
    // Motor da Revolucao Energetica: geracao distribuida, armazenamento, alocacao democratica.

    funcao __init__(self) retorna None:
        self.geracao: Dict[str, UnidadeGeracao] = {}
        self.armazenamento: Dict[str, UnidadeArmazenamento] = {}
        self.consumos: List[ConsumoRegistrado] = []
        self.microgrids: Dict[str, Microgrid] = {}
        self.alocacoes: Dict[str, AlocacaoEscassez] = {}
        self._gen_id = 0
        self._arm_id = 0
        self._cons_id = 0
        self._mg_id = 0
        self._aloc_id = 0

    // -- IDs ---------------------------------------------------------------

    funcao _gen_novo_id(self) retorna str:
        self._gen_id += 1
        retorne f"GEN-{self._gen_id:04d}"

    funcao _arm_novo_id(self) retorna str:
        self._arm_id += 1
        retorne f"ARM-{self._arm_id:04d}"

    funcao _cons_novo_id(self) retorna str:
        self._cons_id += 1
        retorne f"CON-{self._cons_id:04d}"

    funcao _mg_novo_id(self) retorna str:
        self._mg_id += 1
        retorne f"GRID-{self._mg_id:04d}"

    funcao _aloc_novo_id(self) retorna str:
        self._aloc_id += 1
        retorne f"ALOC-{self._aloc_id:04d}"

    // -- cadastro ----------------------------------------------------------

    def cadastrar_geracao(
        self,
        fonte: FonteEnergia,
        capacidade_kw: float,
        declare producao_atual_kw: float  <- 0.0,
        declare comunidade_id: str  <- "",
        declare sustentabilidade_pct: float  <- 100.0,
    ) -> UnidadeGeracao:
        u <- UnidadeGeracao(
            id <- self._gen_novo_id(),
            fonte <- fonte,
            capacidade_kw <- capacidade_kw,
            producao_atual_kw <- producao_atual_kw,
            comunidade_id <- comunidade_id,
            sustentabilidade_pct <- sustentabilidade_pct,
        )
        self.geracao[u.id] = u
        retorne u

    def cadastrar_armazenamento(
        self,
        tipo: TipoArmazenamento,
        capacidade_kwh: float,
        declare carga_atual_kwh: float  <- 0.0,
        declare comunidade_id: str  <- "",
        declare ciclos_vida: int  <- 10000,
    ) -> UnidadeArmazenamento:
        a <- UnidadeArmazenamento(
            id <- self._arm_novo_id(),
            tipo <- tipo,
            capacidade_kwh <- capacidade_kwh,
            carga_atual_kwh <- carga_atual_kwh,
            comunidade_id <- comunidade_id,
            ciclos_vida <- ciclos_vida,
        )
        self.armazenamento[a.id] = a
        retorne a

    def registrar_consumo(
        self,
        comunidade_id: str,
        tipo: TipoConsumo,
        consumo_kw: float,
        declare cidadao_ou_setor: str  <- "",
    ) -> ConsumoRegistrado:
        c <- ConsumoRegistrado(
            id <- self._cons_novo_id(),
            comunidade_id <- comunidade_id,
            tipo <- tipo,
            consumo_kw <- consumo_kw,
            cidadao_ou_setor <- cidadao_ou_setor,
            timestamp <- datetime.now().isoformat(),
        )
        self.consumos.append(c)
        retorne c

    def criar_microgrid(
        self,
        nome: str,
        comunidade_id: str,
        unidades_geracao: List[str],
        unidades_armazenamento: List[str],
        declare interconexao: StatusInterconexao  <- StatusInterconexao.ILHADO,
    ) -> Microgrid:
        mg <- Microgrid(
            id <- self._mg_novo_id(),
            nome <- nome,
            comunidade_id <- comunidade_id,
            unidades_geracao <- list(unidades_geracao),
            unidades_armazenamento <- list(unidades_armazenamento),
            interconexao <- interconexao,
        )
        self.microgrids[mg.id] = mg
        self._atualizar_metricas_microgrid(mg.id)
        retorne mg

    // -- calculo de equilibrio --------------------------------------------

    funcao _atualizar_metricas_microgrid(self, mg_id: str) retorna None:
        mg <- self.microgrids.get(mg_id)
        se mg e nulo entao:
            retorne nulo
        geracao <- sum(
            self.geracao[gid].producao_atual_kw
            for gid in mg.unidades_geracao
            if gid in self.geracao
        )
        demanda <- sum(
            c.consumo_kw for c in self.consumos
            if c.comunidade_id == mg.comunidade_id
        )
        mg.geracao_total_kw = round(geracao, 2)
        mg.demanda_total_kw = round(demanda, 2)
        // calcular cenario
        se demanda == 0 entao:
            mg.cenario = StatusCenario.ABUNDANCIA
            retorne nulo
        margem <- (geracao - demanda) / demanda
        se margem >= 0.2 entao:
            mg.cenario = StatusCenario.ABUNDANCIA
        senao se margem >= 0.0 entao:
            mg.cenario = StatusCenario.EQUILIBRIO
        senao se margem >= -0.1 entao:
            mg.cenario = StatusCenario.ATENCAO
        senao se margem >= -0.3 entao:
            mg.cenario = StatusCenario.ESCASSEZ
        senao:
            mg.cenario = StatusCenario.EMERGENCIA
        // autonomia (baseada em armazenamento)
        armazenamento_total <- sum(
            self.armazenamento[aid].carga_atual_kwh
            for aid in mg.unidades_armazenamento
            if aid in self.armazenamento
        )
        mg.autonomia_horas = round(armazenamento_total / demanda, 2) if demanda > 0 else 0.0

    funcao diagnosticar_microgrid(self, mg_id: str) retorna Tuple[StatusCenario, Dict[str, Any]]:
        // Produz diagnostico completo do equilibrio energetico.
        self._atualizar_metricas_microgrid(mg_id)
        mg <- self.microgrids.get(mg_id)
        se mg e nulo entao:
            retorne StatusCenario.EQUILIBRIO, {"erro": "Microgrid nao encontrada"}
        deficit <- max(0.0, mg.demanda_total_kw - mg.geracao_total_kw)
        excedente <- max(0.0, mg.geracao_total_kw - mg.demanda_total_kw)
        // mix energetico (renovavel vs nao-renovavel)
        renovable <- sum(
            self.geracao[gid].producao_atual_kw
            for gid in mg.unidades_geracao
            if gid in self.geracao  E  self.geracao[gid].fonte.renovavel
        )
        pct_renovavel <- (renovable / mg.geracao_total_kw * 100) if mg.geracao_total_kw else 0.0
        info <- {
            "geracao_kw": mg.geracao_total_kw,
            "demanda_kw": mg.demanda_total_kw,
            "deficit_kw": round(deficit, 2),
            "excedente_kw": round(excedente, 2),
            "autonomia_h": mg.autonomia_horas,
            "pct_renovavel": round(pct_renovavel, 1),
            "interconexao": mg.interconexao.rotulo,
        }
        retorne mg.cenario, info

    // -- alocacao democratica em escassez ---------------------------------

    def propor_alocacao_escassez(
        self,
        mg_id: str,
        declare duracao_estimada_h: float  <- 24.0,
    ) -> Optional[AlocacaoEscassez]:
        // 
        Quando geracao nao cobre demanda, a assembleia precisa decidir.
        Este metodo PROPOE a alocacao baseada em prioridade.
        A assembleia precisa APROVAR (P4).
        // 
        mg <- self.microgrids.get(mg_id)
        se mg e nulo entao:
            retorne nulo
        self._atualizar_metricas_microgrid(mg_id)
        se mg.cenario NAO  in (StatusCenario.ESCASSEZ, StatusCenario.EMERGENCIA) entao:
            retorne nulo
        deficit <- mg.demanda_total_kw - mg.geracao_total_kw
        se deficit <= 0 entao:
            retorne nulo
        // agrupar consumo por tipo nesta comunidade
        declare consumo_por_tipo: Dict[TipoConsumo, float]  <- defaultdict(float)
        para cada c em self.consumos:
            se c.comunidade_id == mg.comunidade_id entao:
                consumo_por_tipo[c.tipo] += c.consumo_kw
        // ordenar por prioridade (1=essencial primeiro)
        tipos_ordenados <- sorted(consumo_por_tipo.keys(), key=funcao anonima(t): t.prioridade)
        // alocar geracao disponivel por prioridade
        geracao_disponivel <- mg.geracao_total_kw
        declare priorizados: List[TipoConsumo]  <- []
        declare rotacionados: List[TipoConsumo]  <- []
        declare suprimidos: List[TipoConsumo]  <- []
        para cada tipo em tipos_ordenados:
            consumo_tipo <- consumo_por_tipo[tipo]
            se geracao_disponivel >= consumo_tipo entao:
                priorizados.append(tipo)
                geracao_disponivel <- geracao_disponivel - consumo_tipo
            senao se geracao_disponivel > 0 entao:
                // geracao parcial -- rotacionar (rodizio)
                rotacionados.append(tipo)
                geracao_disponivel <- 0
            senao:
                suprimidos.append(tipo)
        aloc <- AlocacaoEscassez(
            id <- self._aloc_novo_id(),
            microgrid_id <- mg_id,
            deficit_kw <- round(deficit, 2),
            tipos_priorizados <- priorizados,
            tipos_rotacionados <- rotacionados,
            tipos_suprimidos <- suprimidos,
            duracao_estimada_h <- duracao_estimada_h,
            aprovado_em_assembleia <- FALSO,
            justificativa <- (
                f"Deficit de {deficit:.1f} kW. Geracao alocada por prioridade: "
                f"essenciais garantidos, nao-essenciais em rodizio/corte. "
                f"Ninguem fica sem energia essencial por dinheiro (P1)."
            ),
        )
        self.alocacoes[aloc.id] = aloc
        retorne aloc

    funcao aprovar_alocacao(self, aloc_id: str) retorna bool:
        // A assembleia aprova a proposta de alocacao (P4).
        a <- self.alocacoes.get(aloc_id)
        se a e nulo entao:
            retorne FALSO
        a.aprovado_em_assembleia = VERDADEIRO
        retorne VERDADEIRO

    // -- doacao de excedente (P2P) ----------------------------------------

    funcao doar_excedente(self, mg_origem_id: str, mg_destino_id: str) retorna Optional[float]:
        // Microgrid com excedente doa para microgrid com deficit (P2P, sem dinheiro).
        self._atualizar_metricas_microgrid(mg_origem_id)
        self._atualizar_metricas_microgrid(mg_destino_id)
        origem <- self.microgrids.get(mg_origem_id)
        destino <- self.microgrids.get(mg_destino_id)
        se origem e nulo  OU  destino e nulo entao:
            retorne nulo
        excedente <- origem.geracao_total_kw - origem.demanda_total_kw
        deficit <- destino.demanda_total_kw - destino.geracao_total_kw
        se excedente <= 0  OU  deficit <= 0 entao:
            retorne nulo
        doado <- min(excedente, deficit)
        origem.interconexao = StatusInterconexao.EXPORTANDO
        destino.interconexao = StatusInterconexao.IMPORTANDO
        // simular transferencia
        origem.geracao_total_kw = round(origem.geracao_total_kw - doado, 2)
        destino.geracao_total_kw = round(destino.geracao_total_kw + doado, 2)
        self._atualizar_metricas_microgrid(mg_origem_id)
        self._atualizar_metricas_microgrid(mg_destino_id)
        retorne round(doado, 2)

    // -- eficiencia como dever civico (kaizen) ----------------------------

    funcao auditoria_eficiencia(self, comunidade_id: str) retorna Dict[str, Any]:
        // 
        Eficiencia energetica NAO economiza dinheiro (energia e gratis).
        Eficiencia LIBERTA capacidade para outros. E dever civico (kaizen).
        // 
        consumos_com <- [c for c in self.consumos if c.comunidade_id == comunidade_id]
        se NAO  consumos_com entao:
            retorne {"comunidade": comunidade_id, "consumo_total_kw": 0, "alertas": []}
        consumo_total <- sum(c.consumo_kw for c in consumos_com)
        // identificar consumos potencialmente otimizaveis
        declare alertas: List[str]  <- []
        declare consumo_por_tipo: Dict[TipoConsumo, float]  <- defaultdict(float)
        para cada c em consumos_com:
            consumo_por_tipo[c.tipo] += c.consumo_kw
        para cada (tipo, val) em consumo_por_tipo.items():
            // heuristicas simples de desperdicio
            se tipo == TipoConsumo.RESIDENCIAL_EXCEDENTE  E  val > consumo_total * 0.3 entao:
                alertas.append(
                    f"Consumo residencial excedente alto ({val:.1f} kW, "
                    f"{val/consumo_total*100:.0f}% do total). "
                    f"Lembrar: eficiencia liberta capacidade para a comunidade."
                )
            se tipo == TipoConsumo.PRODUCAO_BENS  E  val > consumo_total * 0.4 entao:
                alertas.append(
                    f"Producao de bens consome {val:.1f} kW. "
                    f"Otimizar processos = mais capacidade para saude e educacao."
                )
        retorne {
            "comunidade": comunidade_id,
            "consumo_total_kw": round(consumo_total, 2),
            "consumo_por_tipo": {t.rotulo: round(v, 1) for t, v in consumo_por_tipo.items()},
            "alertas_eficiencia": alertas,
            "mensagem": (
                "Energia e gratuita. Eficiencia nao economiza dinheiro -- "
                "LIBERTA capacidade para quem precisa. E kaizen civico."
            ),
        }

    // -- scorecard global --------------------------------------------------

    funcao scorecard(self) retorna Dict[str, Any]:
        geracao_total <- sum(g.producao_atual_kw for g in self.geracao.values())
        renovavel <- sum(g.producao_atual_kw for g in self.geracao.values() if g.fonte.renovavel)
        demanda_total <- sum(c.consumo_kw for c in self.consumos)
        armazenamento_total <- sum(a.carga_atual_kwh for a in self.armazenamento.values())
        retorne {
            "unidades_geracao": len(self.geracao),
            "unidades_armazenamento": len(self.armazenamento),
            "microgrids": len(self.microgrids),
            "geracao_total_kw": round(geracao_total, 1),
            "demanda_total_kw": round(demanda_total, 1),
            "excedente_kw": round(max(0, geracao_total - demanda_total), 1),
            "pct_renovavel": round(renovavel / geracao_total * 100, 1) if geracao_total else 0.0,
            "armazenamento_kwh": round(armazenamento_total, 1),
            "alocacoes_escassez": len(self.alocacoes),
            "doacoes_realizadas": sum(
                1 for mg in self.microgrids.values()
                if mg.interconexao == StatusInterconexao.EXPORTANDO
            ),
        }


// ============================================================================
// 4. DEMO
// ============================================================================

funcao _demo() retorna None:
    e <- EnergiaEngine()

    print("=" * 70)
    print("OpenEnergy -- Energia Gratuita para Todo e Qualquer Uso")
    print("=" * 70)

    // --- Comunidade 1: Solar Village (abundancia) ---
    print("\n[CENARIO 1] Solar Village -- abundancia (geracao > demanda)")
    // geracao
    g1 <- e.cadastrar_geracao(FonteEnergia.SOLAR, 500.0, 480.0, "solar_village")
    g2 <- e.cadastrar_geracao(FonteEnergia.EOLICA, 300.0, 250.0, "solar_village")
    // armazenamento
    a1 <- e.cadastrar_armazenamento(TipoArmazenamento.BATERIA_LITIO, 2000.0, 1500.0, "solar_village")
    a2 <- e.cadastrar_armazenamento(TipoArmazenamento.BATERIA_FLUXO, 5000.0, 4000.0, "solar_village")
    // consumo (qualquer uso, sem restricao)
    for tipo, kw in [
        (TipoConsumo.ESSENCIAL_VIDA, 120.0),
        (TipoConsumo.SAUDE, 40.0),
        (TipoConsumo.COMUNICACAO, 30.0),
        (TipoConsumo.EDUCACAO, 50.0),
        (TipoConsumo.CULTURA_LAZER, 80.0),
        (TipoConsumo.RESIDENCIAL_EXCEDENTE, 100.0),
    ]:
        e.registrar_consumo("solar_village", tipo, kw)
    mg1 <- e.criar_microgrid(
        "Solar Village Grid", "solar_village",
        [g1.id, g2.id], [a1.id, a2.id],
        interconexao <- StatusInterconexao.CONECTADO,
    )
    desempacote cenario1, info1 <- e.diagnosticar_microgrid(mg1.id)
    print(f"  Geracao: {info1['geracao_kw']} kW | Demanda: {info1['demanda_kw']} kW")
    print(f"  Excedente: {info1['excedente_kw']} kW | Renovavel: {info1['pct_renovavel']}%")
    print(f"  Autonomia (ilhado): {info1['autonomia_h']}h")
    print(f"  Cenario: {cenario1.rotulo}")
    print(f"  Energia para QUALQUER uso: sim, sem conta, sem medidor de cobranca.")

    // --- Comunidade 2: Vale Seco (escassez) ---
    print("\n[CENARIO 2] Vale Seco -- escassez (seca reduziu hidro)")
    g3 <- e.cadastrar_geracao(FonteEnergia.HIDRO, 400.0, 150.0, "vale_seco")  // seca!
    g4 <- e.cadastrar_geracao(FonteEnergia.SOLAR, 200.0, 180.0, "vale_seco")
    a3 <- e.cadastrar_armazenamento(TipoArmazenamento.HIDROGENIO, 3000.0, 800.0, "vale_seco")
    for tipo, kw in [
        (TipoConsumo.ESSENCIAL_VIDA, 100.0),
        (TipoConsumo.SAUDE, 60.0),
        (TipoConsumo.COMUNICACAO, 20.0),
        (TipoConsumo.EDUCACAO, 40.0),
        (TipoConsumo.PRODUCAO_BENS, 80.0),
        (TipoConsumo.CULTURA_LAZER, 50.0),
    ]:
        e.registrar_consumo("vale_seco", tipo, kw)
    mg2 <- e.criar_microgrid(
        "Vale Seco Grid", "vale_seco",
        [g3.id, g4.id], [a3.id],
        interconexao <- StatusInterconexao.CONECTADO,
    )
    desempacote cenario2, info2 <- e.diagnosticar_microgrid(mg2.id)
    print(f"  Geracao: {info2['geracao_kw']} kW | Demanda: {info2['demanda_kw']} kW")
    print(f"  Deficit: {info2['deficit_kw']} kW | Cenario: {cenario2.rotulo}")
    print(f"  Autonomia: {info2['autonomia_h']}h")

    // --- Alocacao democratica em escassez ---
    print("\n[ALOCACAO DEMOCRATICA EM ESCASSEZ]")
    aloc <- e.propor_alocacao_escassez(mg2.id, duracao_estimada_h=48.0)
    se aloc entao:
        print(f"  Proposta {aloc.id} (assembleia precisa aprovar):")
        print(f"  Deficit: {aloc.deficit_kw} kW | Duracao estimada: {aloc.duracao_estimada_h}h")
        print(f"  GARANTIDOS (prioridade): {[t.rotulo for t in aloc.tipos_priorizados]}")
        print(f"  EM RODIZIO: {[t.rotulo for t in aloc.tipos_rotacionados]}")
        print(f"  SUPRIMIDOS: {[t.rotulo for t in aloc.tipos_suprimidos]}")
        print(f"  Justificativa: {aloc.justificativa}")
        e.aprovar_alocacao(aloc.id)
        print(f"  Aprovado em assembleia: {aloc.aprovado_em_assembleia}")

    // --- Doacao P2P: Solar Village -> Vale Seco ---
    print("\n[DOACAO P2P] Solar Village doe excedente para Vale Seco")
    doado <- e.doar_excedente(mg1.id, mg2.id)
    se doado entao:
        print(f"  {doado:.1f} kW doados (sem dinheiro, sem cobranca).")
        desempacote _, info2_pos <- e.diagnosticar_microgrid(mg2.id)
        print(f"  Vale Seco pos-doacao: geracao={info2_pos['geracao_kw']} kW, "
              f"deficit={info2_pos['deficit_kw']} kW, cenario={info2_pos['interconexao']}")

    // --- Auditoria de eficiencia (kaizen civico) ---
    print("\n[AUDITORIA DE EFICIENCIA -- dever civico, nao economia]")
    aud <- e.auditoria_eficiencia("solar_village")
    print(f"  Comunidade: {aud['comunidade']}")
    print(f"  Consumo total: {aud['consumo_total_kw']} kW")
    para cada (tipo, val) em aud["consumo_por_tipo"].items():
        print(f"    {tipo}: {val} kW")
    para cada alerta em aud["alertas_eficiencia"]:
        print(f"  ALERTA: {alerta}")
    print(f"  {aud['mensagem']}")

    // --- Scorecard global ---
    print("\n" + "=" * 70)
    print("[SCORECARD ENERGETICO DA REPUBLICA]")
    print("=" * 70)
    sc <- e.scorecard()
    para cada (k, v) em sc.items():
        print(f"  {k:.<28} {v}")

    // --- Catalogo de fontes ---
    print("\n[FONTES DE ENERGIA DA REPUBLICA]")
    para cada f em FonteEnergia:
        flag <- "renovavel" if f.renovavel else "NAO-renovavel"
        print(f"  {f.rotulo:.<30} [{flag}]")

    // --- FILOSOFIA ---
    print("\n" + "=" * 70)
    print("FILOSOFIA -- Por que energia e gratuita para todo e qualquer uso")
    print("=" * 70)
    print("""
ENERGIA NAO E MERCADORIA. E CONDICAO DE VIDA.
Cozinhar precisa de energia. Aquecer precisa de energia.
Curar precisa de energia. Comunicar precisa de energia.
Estudar precisa de energia. Criar precisa de energia.
Cobrar por energia e cobrar por EXISTIR.

O ARGUMENTO DA ESCASSEZ (e por que e falso):
O capitalismo diz: "se energia e gratis, todos desperdicam."
Falso. O capitalista desperdica porque o custo e EXTERNO ao lucro.
O cidadao da Republica SABE que a energia que desperdica falta para o vizinho.
Eficiencia nao economiza dinheiro -- LIBERTA capacidade para a comunidade.

A UNICA ESCASSEZ REAL (e como se resolve):
Quando a geracao nao cobre a demanda (seca, falha), a assembleia decide:
1. Essenciais (vida, saude, comunicacao) SEMPRE garantidos.
2. Nao-essenciais em rodizio democratico.
3. Ninguem fica sem energia por DINHEIRO. So por PRIORIDADE civica.
4. A solucao de longo prazo e GERAR MAIS, nao racionar.
O capitalismo raciona por preco (quem tem dinheiro usa, quem nao tem corta).
A Republica aloca por prioridade (todos tem o essencial, o resto e civico).

A REVOLUCAO ENERGETICA:
1. Cada comunidade gera a propria energia (geracao distribuida).
2. Excedente e DOADO, nao vendido (P2P, sem intermediario).
3. Armazenamento comunitario (baterias compartilhadas).
4. 100% renovavel (a Republica respeita o planeta que a sustenta).
5. Nucleo essencial garantido para TODOS, sem excecao, sem condicao.
6. "Para todo e qualquer uso" -- a Republica nao pergunta PARA QUE.
   Pergunta quanto voce PRECISA, e garante que tem.

A ENERGIA E O AR DA CIVILIZACAO.
Ninguem cobra pelo ar. Ninguem deve cobrar pela energia.
// )


se __name__ == "__main__" entao:
    _demo()

```
