# OpenAgrarianRevolution -- A Terra e de Quem a Cuida

**Arquivo original:** `open-republic/core/open_agrarian_revolution.py`

**Descricao:** =====================================================
A Revolucao Agraria da Republica Aberta vai alem da "reforma agraria" classica.
Nao redistribui propriedade. ABOLI a propriedade da terra como mercadoria.
A terra nao se compra, nao se vende, nao se herda, nao se acumula.
A terra se CUIDA. Quem cuida, colhe o fruto. Quem abandona, devolve.
ALINHAMENTO CONSTITUCIONAL:
- P1 (Anti-elitismo): Latifundio = mecanismo original de elite. Concentrar
  terra = concentrar vida. A Republica extingue a raiz da desigualdade rural.
- P2 (Autonomia corporal): Quem trabalha a terra tem direito ao fruto do
  trabalho. Ninguem morre de fome cercando terra que nao cultiva.
- P3 (Trabalho igual): Crislto vem de IMPACTO (alimentar gente), nao de
  aluguel de terra. Latifundio improdutivo = roubo sistêmico.
- P4 (Democracia radical): Assembleia local decide o uso da terra. Nao
  existe "dono". Existe GUARDIAO com mandato revogavel.
OS 5 PILARES DA REVOLUCAO AGRARIA:
1. ABOLICAO da propriedade privada da terra (ninguem "possui" hectares)
2. GUARDIAO em vez de dono (quem cultiva cuida, mandato revogavel)
3. FUNCAO SOCIAL obrigatoria (terra ociosa = devolvida)
4. COOPERATIVISMO (nenhuma familia sozinha; mutirao como padrao)
5. AGROLOGIA (agricultura que regenera o solo, nao que o exaure)
Author: OpenRepublic Team

---

```portugol

// !/usr/bin/env python3
// 
OpenAgrarianRevolution -- A Terra e de Quem a Cuida
=====================================================
A Revolucao Agraria da Republica Aberta vai alem da "reforma agraria" classica.
Nao redistribui propriedade. ABOLI a propriedade da terra como mercadoria.
A terra nao se compra, nao se vende, nao se herda, nao se acumula.
A terra se CUIDA. Quem cuida, colhe o fruto. Quem abandona, devolve.

ALINHAMENTO CONSTITUCIONAL:
- P1 (Anti-elitismo): Latifundio = mecanismo original de elite. Concentrar
  terra <- concentrar vida. A Republica extingue a raiz da desigualdade rural.
- P2 (Autonomia corporal): Quem trabalha a terra tem direito ao fruto do
  trabalho. Ninguem morre de fome cercando terra que nao cultiva.
- P3 (Trabalho igual): Crislto vem de IMPACTO (alimentar gente), nao de
  aluguel de terra. Latifundio improdutivo = roubo sistêmico.
- P4 (Democracia radical): Assembleia local decide o uso da terra. Nao
  existe "dono". Existe GUARDIAO com mandato revogavel.

OS 5 PILARES DA REVOLUCAO AGRARIA:
1. ABOLICAO da propriedade privada da terra (ninguem "possui" hectares)
2. GUARDIAO em vez de dono (quem cultiva cuida, mandato revogavel)
3. FUNCAO SOCIAL obrigatoria (terra ociosa = devolvida)
4. COOPERATIVISMO (nenhuma familia sozinha; mutirao como padrao)
5. AGROLOGIA (agricultura que regenera o solo, nao que o exaure)

Author: OpenRepublic Team
// 
// importa annotations de __future__
// importa Any, Dict, List, Optional, Tuple, Set de typing
// importa Enum de enum
// importa dataclass, field de dataclasses
// importa defaultdict de collections
// importa datetime de datetime


// ============================================================================
// 1. ENUMS (modulo-level, nunca aninhados)
// ============================================================================

classe TipoTenencia herda de Enum:
    // Como a terra e cuidada na Republica (depois da abolicao da propriedade).
    GUARDIAO_FAMILIAR <- ("guardiao_familiar", "Guardiao familiar", 1)
    COOPERATIVA <- ("cooperativa", "Cooperativa agricola", 5)
    COMUNIDADE_TRADICIONAL <- ("comunidade_tradicional", "Comunidade tradicional (quilombo/ribeirinho/aldeia)", 10)
    ASSENTAMENTO_COLETIVO <- ("assentamento_coletivo", "Assentamento coletivo da Republica", 8)
    RESERVA_REGENERACAO <- ("reserva_regeneracao", "Reserva de regeneracao do solo (repouso)", 0)
    USO_PUBLICO <- ("uso_publico", "Uso publico (escola, enfermaria, mercado)", 0)

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]

    // decorador: @property
    funcao familias_max(self) retorna int:
        retorne self.value[2]


classe UsoSolo herda de Enum:
    // Categorias de uso da terra.
    LAVOURA_ALIMENTACAO <- ("lavoura_alimentacao", "Lavoura de alimentos basicos")
    LAVOURA_DIVERSIFICADA <- ("lavoura_diversificada", "Policultivo diversificado")
    PASTAGEM_REGENERATIVA <- ("pastagem_regenerativa", "Pastagem rotativa regenerativa")
    AGROFLORESTA <- ("agrofloresta", "Sistema agroflorestal (SAF)")
    HORTA_COMUNITARIA <- ("horta_comunitaria", "Horta comunitaria de bairro")
    POMAR <- ("pomar", "Pomar frutifero")
    RESERVA_NATIVA <- ("reserva_nativa", "Reserva de vegetacao nativa")
    CULTURA_TRADICIONAL <- ("cultura_tradicional", "Cultivo tradicional ancestral")
    INFRAESTRUTURA <- ("infraestrutura", "Infraestrutura (casa, galpao, escola)")
    OCIOSO <- ("ocioso", "Ocioso (sem funcao social)")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe StatusReforma herda de Enum:
    // Estagio da revolucao agraria num territorio.
    DIAGNOSTICO <- ("diagnostico", "Diagnostico fundiario em curso")
    NOTIFICACAO <- ("notificacao", "Latifundio notificado (funcao social cobrada)")
    DESAPROPRIACAO <- ("desapropriacao", "Desapropriacao decidida em assembleia")
    ASSENTAMENTO <- ("assentamento", "Familias assentadas como guardias")
    REGULARIZACAO <- ("regularizacao", "Regularizacao cooperativa ativa")
    CONSOLIDADO <- ("consolidado", "Territorio consolidado (auto-gestionario)")
    CONFLITO <- ("conflito", "Conflito fundiario ativo (grileiro/invasao)")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe TipoConflito herda de Enum:
    // Tipos de conflito fundiario que a Republica precisa resolver.
    GRILAGEM <- ("grilagem", "Grilagem (falsificacao de titulo)")
    INVASAO_LATIFUNDIO <- ("invasao_latifundio", "Trabalhador expulso por latifundio")
    TRABALHO_ESCRAVO <- ("trabalho_escravo", "Trabalho analogo a escravidao")
    DESPEJO <- ("despejo", "Despejo de familia guardi")
    CONFLITO_FRONTEIRA <- ("conflito_fronteira", "Disputa de fronteira entre comunidades")
    MINERACAO_ILEGAL <- ("mineracao_ilegal", "Mineracao/predacao ilegal em terra guardia")
    AGROTOXICO <- ("agrotoxico", "Contaminacao por agrotoxico vizinho")
    QUEIMADA_CRIMINOSA <- ("queimada_criminosa", "Queimada criminosa / desmatamento")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]

    // decorador: @property
    funcao gravidade(self) retorna int:
        retorne {
            "grilagem": 4,
            "invasao_latifundio": 5,
            "trabalho_escravo": 5,
            "despejo": 4,
            "conflito_fronteira": 2,
            "mineracao_ilegal": 4,
            "agrotoxico": 3,
            "queimada_criminosa": 4,
        }[self.value[0]]


classe TamanhoImovel herda de Enum:
    // Faixas de area (modulo fiscal referencia: ~50 ha em media).
    MINIFUNDIO <- ("minifundio", "Minifundio (insuficiente, < 1 modulo)", 0, 50)
    PEQUENO <- ("pequeno", "Pequena area (1-4 modulos)", 50, 200)
    MEDIO <- ("medio", "Media area (4-15 modulos)", 200, 750)
    LATIFUNDIO_DIMENSAO <- ("latifundio_dimensao", "Latifundio por dimensao (>15 modulos)", 750, 99999)
    LATIFUNDIO_EXPLORACAO <- ("latifundio_exploracao", "Latifundio por exploracao (ocioso/grilado)", 0, 99999)

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]

    // decorador: @property
    funcao area_min(self) retorna float:
        retorne self.value[2]

    // decorador: @property
    funcao area_max(self) retorna float:
        retorne self.value[3]


classe FuncaoSocialStatus herda de Enum:
    // Cumprimento da funcao social da terra (Art. 186 CF/88, radicalizado).
    CUMPRE <- ("cumpre", "Cumpre funcao social")
    PARCIAL <- ("parcial", "Cumpre parcialmente")
    DESCUMPRE <- ("descumpre", "Descumpre funcao social")

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe PlanoAgrologia herda de Enum:
    // Praticas regenerativas (a Republica PROIBE agricultura que exaure solo).
    PLANTIO_DIRETO <- ("plantio_direto", "Plantio direto (nao revolver solo)")
    ADUBACAO_VERDE <- ("adubacao_verde", "Adubacao verde (leguminosas)")
    COMPOSTAGEM <- ("compostagem", "Compostagem comunitaria")
    ROTACAO_CULTURAS <- ("rotacao_culturas", "Rotacao de culturas")
    CICLO_FECHADO <- ("ciclo_fechado", "Ciclo fechado (zero insumo externo)")
    AGROFLORESTA_SUCSSIONAL <- ("agrofloresta_sucessional", "Agrofloresta sucessional")
    CAPTACAO_CHUVA <- ("captacao_chuva", "Captacao de agua de chuva")
    BIOINSUMOS <- ("bioinsumos", "Bioinsumos (proibido agrotoxico sintetico)")
    INTEGRACAO_ANIMAL <- ("integracao_animal", "Integracao lavoura-pecuaria-floresta")

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
classe ImovelRural:
    // Um imovel rural no cadastro da Republica (depois da abolicao, e 'terra guardia').
    id: str
    nome: str
    area_hectares: float
    municipio: str
    bioma: str
    tipo_tenencia: TipoTenencia
    declare usos_solo: List[UsoSolo]  <- field(default_factory=list)
    declare familias_guardias: int  <- 0
    declare funcao_social: FuncaoSocialStatus  <- FuncaoSocialStatus.DESCUMPRE
    declare produtividade_pct: float  <- 0.0  // 0-100, vs potencial do bioma
    declare plano_agrologia: List[PlanoAgrologia]  <- field(default_factory=list)
    declare status: StatusReforma  <- StatusReforma.DIAGNOSTICO
    declare historico_antigo: str  <- ""  // quem "possuia" antes (registro historico, nao direito)


// decorador: @dataclass
classe FamiliaGuardia:
    // Uma familia que cuida de uma parcela de terra.
    id: str
    nome_referencia: str
    pessoas: int
    parcela_hectares: float
    declare cooperativa_id: Optional[str]  <- nulo
    declare chegada_de: str  <- ""  // origem: "assentamento", "tradicional", "despejado", "voluntario"
    declare conhecimento_tradicional: bool  <- FALSO


// decorador: @dataclass
classe ConflitoFundiario:
    // Conflito que a Republica precisa resolver para a revolucao avancar.
    id: str
    tipo: TipoConflito
    territorio_id: str
    declare vitimas: int  <- 0
    declare familias_afetadas: int  <- 0
    declare descricao: str  <- ""
    declare resolucao_proposta: str  <- ""
    declare resolvido: bool  <- FALSO


// decorador: @dataclass
classe CooperativaAgricola:
    // Unidade cooperativa de familias guardias (mutirao como padrao).
    id: str
    nome: str
    declare familia_ids: List[str]  <- field(default_factory=list)
    declare territorio_ids: List[str]  <- field(default_factory=list)
    declare excedente_destino: str  <- ""  // para onde vai o excedente (mercado aberto, outra comunidade)
    declare ferramentas_compartilhadas: List[str]  <- field(default_factory=list)


// decorador: @dataclass
classe DiagnosticoFundiario:
    // Snapshot da concentracao de terra num territorio.
    territorio: str
    total_area: float
    num_imoveis: int
    indice_gini: float   // 0=igualdade, 1=concentracao absoluta
    pct_area_latifundio: float   // % da area em maos de <10% dos "ex-donos"
    familias_sem_terra: int
    familias_guardias: int
    declare veredito: str  <- ""  // DiagnosticoEngine preenche


// ============================================================================
// 3. ENGINE
// ============================================================================

classe ReformaAgrariaEngine:
    // Motor da Revolucao Agraria: diagnostica, redistribui, cuida, audita.

    funcao __init__(self) retorna None:
        self.imoveis: Dict[str, ImovelRural] = {}
        self.familias: Dict[str, FamiliaGuardia] = {}
        self.cooperativas: Dict[str, CooperativaAgricola] = {}
        self.conflitos: Dict[str, ConflitoFundiario] = {}
        self._im_id = 0
        self._fam_id = 0
        self._coop_counter = 0
        self._conf_id = 0

    // -- cadastro ----------------------------------------------------------

    funcao _imovel_id(self) retorna str:
        self._im_id += 1
        retorne f"TER-{self._im_id:04d}"

    funcao _familia_id(self) retorna str:
        self._fam_id += 1
        retorne f"FAM-{self._fam_id:04d}"

    funcao _coop_id(self) retorna str:
        self._coop_counter += 1
        retorne f"COOP-{self._coop_counter:04d}"

    funcao _conflito_id(self) retorna str:
        self._conf_id += 1
        retorne f"CONF-{self._conf_id:04d}"

    def cadastrar_imovel(
        self,
        nome: str,
        area_hectares: float,
        municipio: str,
        bioma: str,
        tipo_tenencia: TipoTenencia,
        declare usos_solo: Optional[List[UsoSolo]]  <- nulo,
        declare familias_guardias: int  <- 0,
        declare funcao_social: FuncaoSocialStatus  <- FuncaoSocialStatus.DESCUMPRE,
        declare produtividade_pct: float  <- 0.0,
        declare plano: Optional[List[PlanoAgrologia]]  <- nulo,
        declare status: StatusReforma  <- StatusReforma.DIAGNOSTICO,
        declare historico_antigo: str  <- "",
    ) -> ImovelRural:
        im <- ImovelRural(
            id <- self._imovel_id(),
            nome <- nome,
            area_hectares <- area_hectares,
            municipio <- municipio,
            bioma <- bioma,
            tipo_tenencia <- tipo_tenencia,
            usos_solo <- usos_solo  OU  [],
            familias_guardias <- familias_guardias,
            funcao_social <- funcao_social,
            produtividade_pct <- produtividade_pct,
            plano_agrologia <- plano  OU  [],
            status <- status,
            historico_antigo <- historico_antigo,
        )
        self.imoveis[im.id] = im
        retorne im

    def cadastrar_familia(
        self,
        nome_referencia: str,
        pessoas: int,
        parcela_hectares: float,
        declare cooperativa_id: Optional[str]  <- nulo,
        declare chegada_de: str  <- "voluntario",
        declare conhecimento_tradicional: bool  <- FALSO,
    ) -> FamiliaGuardia:
        f <- FamiliaGuardia(
            id <- self._familia_id(),
            nome_referencia <- nome_referencia,
            pessoas <- pessoas,
            parcela_hectares <- parcela_hectares,
            cooperativa_id <- cooperativa_id,
            chegada_de <- chegada_de,
            conhecimento_tradicional <- conhecimento_tradicional,
        )
        self.familias[f.id] = f
        retorne f

    def criar_cooperativa(
        self,
        nome: str,
        familia_ids: List[str],
        territorio_ids: List[str],
        declare excedente_destino: str  <- "mercado_aberto",
        declare ferramentas: Optional[List[str]]  <- nulo,
    ) -> CooperativaAgricola:
        c <- CooperativaAgricola(
            id <- self._coop_id(),
            nome <- nome,
            familia_ids <- list(familia_ids),
            territorio_ids <- list(territorio_ids),
            excedente_destino <- excedente_destino,
            ferramentas_compartilhadas <- ferramentas  OU  [],
        )
        self.cooperativas[c.id] = c
        // vincular familias a coop
        para cada fid em familia_ids:
            se fid in self.familias entao:
                self.familias[fid].cooperativa_id = c.id
        retorne c

    def registrar_conflito(
        self,
        tipo: TipoConflito,
        territorio_id: str,
        declare vitimas: int  <- 0,
        declare familias_afetadas: int  <- 0,
        declare descricao: str  <- "",
    ) -> ConflitoFundiario:
        c <- ConflitoFundiario(
            id <- self._conflito_id(),
            tipo <- tipo,
            territorio_id <- territorio_id,
            vitimas <- vitimas,
            familias_afetadas <- familias_afetadas,
            descricao <- descricao,
        )
        self.conflitos[c.id] = c
        retorne c

    // -- diagnostico -------------------------------------------------------

    funcao classificar_tamanho(self, area: float, ocioso: bool = False) retorna TamanhoImovel:
        // Classifica imovel por area e exploracao.
        se ocioso  E  area >= TamanhoImovel.PEQUENO.area_min entao:
            retorne TamanhoImovel.LATIFUNDIO_EXPLORACAO
        for t in [TamanhoImovel.MINIFUNDIO, TamanhoImovel.PEQUENO,
                  TamanhoImovel.MEDIO, TamanhoImovel.LATIFUNDIO_DIMENSAO]:
            se t.area_min <= area < t.area_max entao:
                retorne t
        retorne TamanhoImovel.LATIFUNDIO_DIMENSAO

    funcao indice_gini_areas(self) retorna float:
        // Gini de concentracao de area entre imoveis (0=igual, 1=concentrado).
        areas <- sorted(im.area_hectares for im in self.imoveis.values())
        n <- len(areas)
        se n == 0 entao:
            retorne 0.0
        total <- sum(areas)
        se total == 0 entao:
            retorne 0.0
        cum <- 0.0
        soma_pond <- 0.0
        para cada (i, a) em enumerate(areas, start=1):
            soma_pond <- soma_pond + i * a
        gini <- (2 * soma_pond) / (n * total) - (n + 1) / n
        retorne round(gini, 4)

    funcao diagnosticar(self, territorio: str) retorna DiagnosticoFundiario:
        // Produz o diagnostico fundiario de um territorio.
        ims <- [im for im in self.imoveis.values() if im.municipio == territorio]
        total_area <- sum(im.area_hectares for im in ims)
        num <- len(ims)
        se num == 0 entao:
            retorne DiagnosticoFundiario(
                territorio <- territorio,
                total_area <- 0.0,
                num_imoveis <- 0,
                indice_gini <- 0.0,
                pct_area_latifundio <- 0.0,
                familias_sem_terra <- 0,
                familias_guardias <- 0,
                veredito <- "Territorio vazio no cadastro.",
            )
        gini <- self.indice_gini_areas()
        // % da area em maos de latifundios
        area_lat <- sum(
            im.area_hectares for im in ims
            if self.classificar_tamanho(im.area_hectares, ocioso=(im.funcao_social == FuncaoSocialStatus.DESCUMPRE))
            in (TamanhoImovel.LATIFUNDIO_DIMENSAO, TamanhoImovel.LATIFUNDIO_EXPLORACAO)
        )
        pct_lat <- (area_lat / total_area * 100.0) if total_area else 0.0
        familias_guardias <- sum(im.familias_guardias for im in ims)
        familias_sem_terra <- max(0, int((pct_lat / 100.0) * familias_guardias / 4) if familias_guardias else 0)

        se gini > 0.7  OU  pct_lat > 50 entao:
            veredito <- "CONCENTRACAO CRITICA: revolicao agraria URGENTE."
        senao se gini > 0.4  OU  pct_lat > 25 entao:
            veredito <- "CONCENTRACAO ALTA: notificar latifundios, cobrar funcao social."
        senao se gini > 0.2 entao:
            veredito <- "CONCENTRACAO MODERADA: regularizar e cooperativizar."
        senao:
            veredito <- "TERRITORIO EQUITATIVO: consolidar cooperativas."

        retorne DiagnosticoFundiario(
            territorio <- territorio,
            total_area <- total_area,
            num_imoveis <- num,
            indice_gini <- gini,
            pct_area_latifundio <- round(pct_lat, 1),
            familias_sem_terra <- familias_sem_terra,
            familias_guardias <- familias_guardias,
            veredito <- veredito,
        )

    // -- funcao social -----------------------------------------------------

    funcao auditar_funcao_social(self, imovel_id: str) retorna Tuple[FuncaoSocialStatus, List[str]]:
        // Verifica os 4 requisitos radicais da funcao social.
        im <- self.imoveis.get(imovel_id)
        se im e nulo entao:
            retorne FuncaoSocialStatus.DESCUMPRE, ["Imovel nao encontrado."]
        declare faltas: List[str]  <- []
        // 1. aproveitamento racional
        se im.produtividade_pct < 40 entao:
            faltas.append(f"Produtividade baixa ({im.produtividade_pct:.0f}% do potencial).")
        // 2. uso adequado dos recursos naturais (agrologia)
        se NAO  im.plano_agrologia entao:
            faltas.append("Sem plano de agrologia (solo sendo exaurido).")
        // 3. observancia da legislacao trabalhista (sem trabalho escravo)
        // conflitos do tipo TRABALHO_ESCRAVO no territorio = descumpre
        para cada conf em self.conflitos.values():
            if (conf.tipo == TipoConflito.TRABALHO_ESCRAVO
                     E  conf.territorio_id == im.id  E  NAO  conf.resolvido):
                faltas.append("Trabalho analogo a escravidao detectado (BLOQUEANTE).")
                interrompa
        // 4. bem-estar de quem trabalha (densidade de familias razoavel)
        se im.familias_guardias == 0  E  im.tipo_tenencia != TipoTenencia.RESERVA_REGENERACAO entao:
            faltas.append("Nenhuma familia guardia: terra abandonada.")
        se faltas entao:
            im.funcao_social = FuncaoSocialStatus.PARCIAL if len(faltas) == 1 else FuncaoSocialStatus.DESCUMPRE
        senao:
            im.funcao_social = FuncaoSocialStatus.CUMPRE
        retorne im.funcao_social, faltas

    // -- revolucao (pipeline) ----------------------------------------------

    funcao notificar_latifundio(self, imovel_id: str) retorna Optional[str]:
        // Notifica um latifundio: cumpra funcao social ou sera devolvido.
        im <- self.imoveis.get(imovel_id)
        se im e nulo entao:
            retorne nulo
        tam <- self.classificar_tamanho(im.area_hectares, ocioso=(im.funcao_social == FuncaoSocialStatus.DESCUMPRE))
        se tam NAO  in (TamanhoImovel.LATIFUNDIO_DIMENSAO, TamanhoImovel.LATIFUNDIO_EXPLORACAO) entao:
            retorne f"{im.id} nao e latifundio ({tam.rotulo})."
        desempacote status, faltas <- self.auditar_funcao_social(im.id)
        se status == FuncaoSocialStatus.CUMPRE entao:
            im.status = StatusReforma.REGULARIZACAO
            retorne f"{im.id} cumpre funcao social -> regularizar como cooperativa."
        im.status = StatusReforma.NOTIFICACAO
        retorne (f"NOTIFICADO {im.id} ({tam.rotulo}, {im.area_hectares:.0f} ha). "
                f"Faltas: {'; '.join(faltas) if faltas else 'none'}. Prazo para regularizar.")

    funcao desaproropriar(self, imovel_id: str, familias_assentar: List[str]) retorna Optional[str]:
        // Desapropria (assembleia decide) e assenta familias guardias.
        im <- self.imoveis.get(imovel_id)
        se im e nulo entao:
            retorne nulo
        se im.status NAO  in (StatusReforma.NOTIFICACAO, StatusReforma.DIAGNOSTICO) entao:
            retorne f"{im.id} em status {im.status.rotulo} -- nao elegivel para desapropriacao agora."
        // parar de reconhecer o "ex-dono": a terra volta ao territorio
        im.historico_antigo = im.historico_antigo  OU  im.nome
        im.nome = f"Territorio Livre {im.id}"
        im.tipo_tenencia = TipoTenencia.ASSENTAMENTO_COLETIVO
        // parcelar entre familias
        se familias_assentar entao:
            parcela <- im.area_hectares / len(familias_assentar)
            para cada fid em familias_assentar:
                fam <- self.familias.get(fid)
                se fam entao:
                    fam.parcela_hectares = round(parcela, 2)
                    fam.chegada_de = "assentamento"
            im.familias_guardias = len(familias_assentar)
        im.status = StatusReforma.ASSENTAMENTO
        im.funcao_social = FuncaoSocialStatus.PARCIAL
        retorne (f"DESAPROPRIVADO {im.id}: {len(familias_assentar)} familias guardias assentadas, "
                f"{im.area_hectares:.0f} ha sob cuidado coletivo.")

    def consolidar_cooperativa(
        self,
        nome: str,
        territorio_ids: List[str],
        familias_ids: List[str],
        declare excedente: str  <- "mercado_aberto",
        declare ferramentas: Optional[List[str]]  <- nulo,
    ) -> CooperativaAgricola:
        // Transforma assentamento em cooperativa auto-gestionaria.
        coop <- self.criar_cooperativa(nome, familias_ids, territorio_ids, excedente, ferramentas)
        para cada tid em territorio_ids:
            im <- self.imoveis.get(tid)
            se im entao:
                im.tipo_tenencia = TipoTenencia.COOPERATIVA
                im.status = StatusReforma.CONSOLIDADO
                im.funcao_social = FuncaoSocialStatus.CUMPRE
        retorne coop

    // -- resolucao de conflitos --------------------------------------------

    funcao conflitos_por_gravidade(self) retorna List[ConflitoFundiario]:
        retorne sorted(
            self.conflitos.values(),
            key <- funcao anonima(c): (-c.tipo.gravidade, -c.familias_afetadas),
        )

    funcao resolver_conflito(self, conflito_id: str, resolucao: str) retorna bool:
        c <- self.conflitos.get(conflito_id)
        se c e nulo entao:
            retorne FALSO
        c.resolucao_proposta = resolucao
        c.resolvido = VERDADEIRO
        retorne VERDADEIRO

    // -- metricas ----------------------------------------------------------

    funcao area_total(self) retorna float:
        retorne sum(im.area_hectares for im in self.imoveis.values())

    funcao area_ociosa(self) retorna float:
        retorne sum(
            im.area_hectares for im in self.imoveis.values()
            if im.funcao_social == FuncaoSocialStatus.DESCUMPRE
        )

    funcao familias_atendidas(self) retorna int:
        retorne sum(im.familias_guardias for im in self.imoveis.values())

    funcao pessoas_atendidas(self) retorna int:
        ids <- {f.id: f for f in self.familias.values()}
        total <- 0
        para cada im em self.imoveis.values():
            total <- total + im.familias_guardias * 4  // media 4 pessoas/familia
        retorne total

    funcao scorecard(self) retorna Dict[str, Any]:
        retorne {
            "imoveis_cadastrados": len(self.imoveis),
            "area_total_ha": round(self.area_total(), 1),
            "area_ociosa_ha": round(self.area_ociosa(), 1),
            "pct_ociosa": round(self.area_ociosa() / self.area_total() * 100, 1) if self.area_total() else 0.0,
            "familias_guardias": self.familias_atendidas(),
            "cooperativas": len(self.cooperativas),
            "conflitos_abertos": sum(1 for c in self.conflitos.values() if NAO  c.resolvido),
            "indice_gini": self.indice_gini_areas(),
            "consolidados": sum(1 for im in self.imoveis.values() if im.status == StatusReforma.CONSOLIDADO),
        }


// ============================================================================
// 4. DEMO
// ============================================================================

funcao _demo() retorna None:
    e <- ReformaAgrariaEngine()

    print("=" * 70)
    print("OpenAgrarianRevolution -- A Terra e de Quem a Cuida")
    print("=" * 70)

    // --- Contexto: territorio "Sertao do Sao Francisco" ---
    // Cadastro: um latifundio ocioso (caso classico), uma reserva, pequenas areas
    latif <- e.cadastrar_imovel(
        nome <- "Fazenda Boa Vista (ex-latifundio)",
        area_hectares <- 2500.0,
        municipio <- "Sertao do Sao Francisco",
        bioma <- "caatinga",
        tipo_tenencia <- TipoTenencia.GUARDIAO_FAMILIAR,  // ainda herdado do antigo
        usos_solo <- [UsoSolo.PASTAGEM_REGENERATIVA, UsoSolo.OCIOSO],
        familias_guardias <- 3,
        funcao_social <- FuncaoSocialStatus.DESCUMPRE,
        produtividade_pct <- 15.0,
        plano <- [],  // sem agrologia
        historico_antigo <- "Familia herdeira de titulo duvidoso",
    )

    pequeno_a <- e.cadastrar_imovel(
        nome <- "Sitio Aconchego",
        area_hectares <- 30.0,
        municipio <- "Sertao do Sao Francisco",
        bioma <- "caatinga",
        tipo_tenencia <- TipoTenencia.GUARDIAO_FAMILIAR,
        usos_solo <- [UsoSolo.LAVOURA_ALIMENTACAO, UsoSolo.POMAR],
        familias_guardias <- 1,
        funcao_social <- FuncaoSocialStatus.PARCIAL,
        produtividade_pct <- 70.0,
        plano <- [PlanoAgrologia.COMPOSTAGEM, PlanoAgrologia.ROTACAO_CULTURAS],
    )

    reserva <- e.cadastrar_imovel(
        nome <- "Reserva Caatinga Viva",
        area_hectares <- 800.0,
        municipio <- "Sertao do Sao Francisco",
        bioma <- "caatinga",
        tipo_tenencia <- TipoTenencia.RESERVA_REGENERACAO,
        usos_solo <- [UsoSolo.RESERVA_NATIVA],
        familias_guardias <- 0,
        funcao_social <- FuncaoSocialStatus.CUMPRE,
        produtividade_pct <- 0.0,
        plano <- [PlanoAgrologia.CICLO_FECHADO],
    )

    // --- Diagnostico ---
    diag <- e.diagnosticar("Sertao do Sao Francisco")
    print(f"\n[DIAGNOSTICO] {diag.territorio}")
    print(f"  Area total: {diag.total_area:.0f} ha | Imoveis: {diag.num_imoveis}")
    print(f"  Indice de Gini: {diag.indice_gini:.3f} (0=igual, 1=concentrado)")
    print(f"  % area em latifundios: {diag.pct_area_latifundio:.1f}%")
    print(f"  Familias guardias: {diag.familias_guardias}")
    print(f"  VEREDITO: {diag.veredito}")

    // --- Notificar latifundio ---
    print("\n[NOTIFICACAO]")
    msg <- e.notificar_latifundio(latif.id)
    print(f"  {msg}")

    // --- Auditar funcao social ---
    print("\n[AUDITORIA DE FUNCAO SOCIAL]")
    para cada iid em [latif.id, pequeno_a.id, reserva.id]:
        desempacote status, faltas <- e.auditar_funcao_social(iid)
        im <- e.imoveis[iid]
        print(f"  {iid} ({im.nome[:30]}): {status.rotulo}")
        para cada f em faltas:
            print(f"      - {f}")

    // --- Conflito: trabalho escravo detectado no latifundio ---
    conflito <- e.registrar_conflito(
        tipo <- TipoConflito.TRABALHO_ESCRAVO,
        territorio_id <- latif.id,
        vitimas <- 2,
        familias_afetadas <- 8,
        descricao <- "Trabalhadores resgatados em condicoes analogas a escravidao.",
    )
    print(f"\n[CONFLITO REGISTRADO] {conflito.id}: {conflito.tipo.rotulo}")
    print(f"  Gravidade: {conflito.tipo.gravidade}/5 | Familias afetadas: {conflito.familias_afetadas}")

    // --- Desapropriar: assembleia decide ---
    print("\n[DESAPROPRIACAO POR ASSEMBLEIA]")
    fams <- [
        e.cadastrar_familia("Familia Maria das Dores", 5, 0.0, chegada_de="despejado"),
        e.cadastrar_familia("Familia Jose Pereira", 4, 0.0, chegada_de="despejado"),
        e.cadastrar_familia("Familia Ana Beatriz", 6, 0.0, chegada_de="voluntario"),
        e.cadastrar_familia("Familia Severino", 5, 0.0, chegada_de="despejado", conhecimento_tradicional=VERDADEIRO),
    ]
    res <- e.desaproropriar(latif.id, [f.id for f in fams])
    print(f"  {res}")

    // Resolver o conflito de trabalho escravo
    e.resolver_conflito(conflito.id, "Ex-dono removido; familias guardias assumem; recuperacao das vitimas via OpenPsychologyReparation.")
    print(f"  Conflito {conflito.id} resolvido: {conflito.resolucao_proposta}")

    // --- Consolidar cooperativa ---
    print("\n[CONSOLIDACAO COOPERATIVA]")
    coop <- e.consolidar_cooperativa(
        nome <- "Cooperativa Terra Livre Sertao",
        territorio_ids <- [latif.id],
        familias_ids <- [f.id for f in fams],
        excedente <- "mercado_aberto",
        ferramentas <- ["trator_compartilhado", "casa_de_farinha", "cisterna_coletiva"],
    )
    print(f"  {coop.id}: {coop.nome}")
    print(f"  Familias: {len(coop.familia_ids)} | Territorios: {len(coop.territorio_ids)}")
    print(f"  Ferramentas compartilhadas: {', '.join(coop.ferramentas_compartilhadas)}")

    // --- Plano de agrologia no novo territorio livre ---
    latif.usos_solo = [UsoSolo.AGROFLORESTA, UsoSolo.LAVOURA_DIVERSIFICADA, UsoSolo.POMAR]
    latif.plano_agrologia = [
        PlanoAgrologia.AGROFLORESTA_SUCSSIONAL,
        PlanoAgrologia.CAPTACAO_CHUVA,
        PlanoAgrologia.BIOINSUMOS,
        PlanoAgrologia.CICLO_FECHADO,
    ]
    latif.produtividade_pct = 65.0
    desempacote status_final, _ <- e.auditar_funcao_social(latif.id)
    print(f"\n[POS-REVOLUCAO] {latif.id} funcao social: {status_final.rotulo}")
    print(f"  Status: {latif.status.rotulo} | Tenencia: {latif.tipo_tenencia.rotulo}")

    // --- Scorecard final ---
    print("\n" + "=" * 70)
    print("[SCORECARD DA REVOLUCAO AGRARIA]")
    print("=" * 70)
    sc <- e.scorecard()
    para cada (k, v) em sc.items():
        print(f"  {k:.<28} {v}")

    // --- Conflitos ordenados por gravidade ---
    print("\n[CONFLITOS POR GRAVIDADE]")
    para cada c em e.conflitos_por_gravidade():
        flag <- "OK" if c.resolvido else "ABERTO"
        print(f"  [{flag}] {c.id} {c.tipo.rotulo} (grav={c.tipo.gravidade}) "
              f"vitimas={c.vitimas} familias={c.familias_afetadas}")

    // --- FILOSOFIA ---
    print("\n" + "=" * 70)
    print("FILOSOFIA -- Por que a Republica ABOLI a propriedade da terra")
    print("=" * 70)
    print("""
P1 (Anti-elitismo): O latifundio e o mecanismo ORIGINAL de elite.
   Antes do banco, antes da empresa, antes da midia: a TERRA.
   Quem cerca a terra cerca a VIDA de quem precisa dela pra comer.
   Abolir a propriedade da terra <- extirpar a raiz da desigualdade.

P2 (Autonomia): Quem planta colhe. Quem cuida decide.
   Ninguem morre de fome vigiando cerca de terra que nao cultiva.
   O corpo que sua na roca e dono do fruto -- nao de hectares.

P3 (Trabalho = impacto): "Dono de terra" nao e trabalho. E RENDA.
   Renda de propriedade e extrativismo puro: tirar sem botar.
   A Republica so reconhece credito por IMPACTO (alimentar gente).
   Latifundio improdutivo e roubo sistemico, nao "investimento".

P4 (Democracia): A assembleia do territorio decide o uso da terra.
   Nao ha "dono" para negociar as escuras com madeireira/mineradora.
   O guardiao tem MANDATO REVOGAVEL: abandona, devolve.
   Ninguem herda hectares. Herda-se o oficio, nao a propriedade.

A REVOLUCAO AGRARIA NAO E "REFORMA". E ABOLICAO.
Reforma distribui propriedade. Abolicao extingue a categoria.
A terra volta a ser o que sempre foi: CONDICAO DE VIDA,
nao ativo no balanco patrimonial de ninguem.
// )


se __name__ == "__main__" entao:
    _demo()

```
