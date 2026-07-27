# OpenAntiPolarization -- P9: O Estado NAO Polariza

**Arquivo original:** `open-republic/core/open_anti_polarization.py`

**Descricao:** ====================================================
O nono principio constitucional da Republica Aberta.
"Discordo de tudo que voce disse, mas darei minha vida para que voce possa
dizer de novo." -- atribuido a Voltaire, encapsula o espirito deste modulo.
DISTINCAO CRITICA (a tese do modulo):
- Diversidade de opiniao e DIREITO (P2). E saudavel. E combustivel da democracia.
- Polarizacao e DOENCA SISTEMICA. Nao e "opiniao diferente". E realidade
  epistemica separada: duas tribos que nao so discordam, mas habitam mundos
  de fato diferentes, com zero confianca mutua e identidade fundida na tribo.
A Republica recusa o equivoco liberal de que "mais debate resolve polarizacao".
Mais debate entre tribos epistemicamente separadas AMPLIFICA a polarizacao.
O que resolve e: (a) chao de fato compartilhado, (b) deliberacao estruturada,
(c) Estado que se recusa a ser vetor de divisao identitaria.
ALINHAMENTO CONSTITUCIONAL:
- P1: Polarizacao recria elite. Sempre ha um lado que se beneficia da divisao.
- P2: Identidade tribal captura autonomia. Quem so pensa pela tribo nao e livre.
- P4: Democracia em assembleia polarizada nao e democracia -- e tirania de 51%.
- P8: IA que amplifica polarizacao (engagement algorithms) VIOLA o principio
  de ampliar inteligencia humana. Engenagement por furia e anti-P8.
P9 -- ANTI-POLARIZACAO DE ESTADO:
O Estado nao pode produzir, amplificar ou se beneficiar de divisao identitaria.
Toda politica publica deve ser avaliada pelo seu POTENCIAL POLARIZANTE antes
da votacao. E um GATE (como WCAG audita acessibilidade), nao um mod de censura.
Author: OpenRepublic Team

---

```portugol

// !/usr/bin/env python3
// 
OpenAntiPolarization -- P9: O Estado NAO Polariza
====================================================
O nono principio constitucional da Republica Aberta.

"Discordo de tudo que voce disse, mas darei minha vida para que voce possa
dizer de novo." -- atribuido a Voltaire, encapsula o espirito deste modulo.

DISTINCAO CRITICA (a tese do modulo):
- Diversidade de opiniao e DIREITO (P2). E saudavel. E combustivel da democracia.
- Polarizacao e DOENCA SISTEMICA. Nao e "opiniao diferente". E realidade
  epistemica separada: duas tribos que nao so discordam, mas habitam mundos
  de fato diferentes, com zero confianca mutua e identidade fundida na tribo.

A Republica recusa o equivoco liberal de que "mais debate resolve polarizacao".
Mais debate entre tribos epistemicamente separadas AMPLIFICA a polarizacao.
O que resolve e: (a) chao de fato compartilhado, (b) deliberacao estruturada,
(c) Estado que se recusa a ser vetor de divisao identitaria.

ALINHAMENTO CONSTITUCIONAL:
- P1: Polarizacao recria elite. Sempre ha um lado que se beneficia da divisao.
- P2: Identidade tribal captura autonomia. Quem so pensa pela tribo nao e livre.
- P4: Democracia em assembleia polarizada nao e democracia -- e tirania de 51%.
- P8: IA que amplifica polarizacao (engagement algorithms) VIOLA o principio
  de ampliar inteligencia humana. Engenagement por furia e anti-P8.

P9 -- ANTI-POLARIZACAO DE ESTADO:
O Estado nao pode produzir, amplificar ou se beneficiar de divisao identitaria.
Toda politica publica deve ser avaliada pelo seu POTENCIAL POLARIZANTE antes
da votacao. E um GATE (como WCAG audita acessibilidade), nao um mod de censura.

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

classe FatorPolarizacao herda de Enum:
    // Vetores que destilam divisao identitaria numa assembleia.
    RELIGIAO <- ("religiao", "Religiao / fe / espiritualidade")
    ETNIA <- ("etnia", "Etnia / raca / origem")
    REGIAO <- ("regiao", "Regiao / geografia (norte vs sul, urbano vs rural)")
    CLASSE <- ("classe", "Classe / origem economica (heranca do sistema antigo)")
    IDEOLOGIA <- ("ideologia", "Ideologia politica (heranca do sistema partidario)")
    IDENTIDADE <- ("identidade", "Identidade de genero / sexual / expressao")
    LINGUA <- ("lingua", "Lingua / idioma / dialeto")
    IDADE <- ("idade", "Geracional (jovens vs velhos)")
    ALGORITMO <- ("algoritmo", "Algoritmo de feed (captura narrativa externa)")
    CULTURA <- ("cultura", "Cultura / costumes / tradicao")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe NivelPolarizacao herda de Enum:
    // Grau de polarizacao medido numa assembleia ou territorio.
    SAUDAVEL <- ("saudavel", "Saudavel: dissenso produtivo, confianca preservada", 0)
    BAIXO <- ("baixo", "Baixo: blocos incipientes, ainda deliberam", 1)
    MODERADO <- ("moderado", "Moderado: blocos claros, deliberacao degrada", 2)
    ALTO <- ("alto", "Alto: votacao tribal, confianca em queda", 3)
    CRITICO <- ("critico", "Critico: quase bloqueio assemblear", 4)
    RUPTURA <- ("ruptura", "Ruptura epistemica: realidades de fato separadas", 5)

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]

    // decorador: @property
    funcao gravidade(self) retorna int:
        retorne self.value[2]


classe TaticaPolarizante herda de Enum:
    // Taticas que destilam divisao. O Estado as audita nas proprias politicas.
    OUTGROUP_DEHUMANIZATION <- ("outgroup_dehumanization", "Desumanizacao do outro lado", 5)
    FALSE_DICHOTOMY <- ("false_dichotomy", "Falsa dicotomia (ou nos ou eles)", 4)
    WHATABOUTISM <- ("whataboutism", "Whataboutism (desvia com 'mas eles tambem')", 3)
    FEAR_MONGERING <- ("fear_mongering", "Alarmismo / medo fabricado", 4)
    IDENTITY_BAITING <- ("identity_baiting", "Isca de identidade (forca tribalismo)", 5)
    EPISTEMIC_BALKANIZATION <- ("epistemic_balkanization", "Balkanizacao epistemica (fatos tribais)", 5)
    BOTH_SIDES_FALLACY <- ("both_sides_fallacy", "Falsa simetria (os dois lados sao iguais)", 3)
    STRAWMAN <- ("strawman", "Espantalho (deturpa para atacar)", 2)
    DOG_WHISTLE <- ("dog_whistle", "Dog whistle (codigo tribal implicito)", 4)
    VIRTUE_SIGNALING <- ("virtue_signaling", "Sinalizacao virtuosa (pertence vs exclui)", 2)

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]

    // decorador: @property
    funcao gravidade(self) retorna int:
        retorne self.value[2]


classe StatusBloqueio herda de Enum:
    // Resposta do protocolo anti-bloqueio assemblear.
    NENHUM <- ("nenhum", "Nenhum: assembleia delibera normalmente", 0)
    ALERTA <- ("alerta", "Alerta: moderador sinaliza polarizacao", 1)
    DELIBERACAO_ESTRUTURADA <- ("deliberacao_estruturada", "Deliberacao estruturada obrigatoria", 2)
    MEDIACAO_OBRIGATORIA <- ("mediacao_obrigatoria", "Mediacao obrigatoria antes de votar", 3)
    SUSPENDER_VOTACAO <- ("suspender_votacao", "Votacao suspensa (bloqueio ativo)", 4)
    ASSEMBLEIA_PAUSA <- ("assembleia_pausa", "Pausa assemblear (resfriamento obrigatorio)", 5)

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]

    // decorador: @property
    funcao prioridade(self) retorna int:
        retorne self.value[2]


classe VereditoAuditoria herda de Enum:
    // Resultado do gate anti-polarizacao numa politica publica.
    APROVADA <- ("aprovada", "Politica aprovada: baixo potencial polarizante")
    APROVADA_COM_RESSALVAS <- ("ressalvas", "Aprovada com ressalvas (mitigacoes exigidas)")
    REJEITADA <- ("rejeitada", "Politica rejeitada: potencial polarizante alto")
    BLOQUEADA <- ("bloqueada", "Politica bloqueada: e vetor de divisao identitaria")

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
classe VotoCidadao:
    // Um voto individual numa proposta de assembleia.
    cidadao_id: str
    proposta_id: str
    a_favor: bool
    declare justificativa: str  <- ""


// decorador: @dataclass
classe PropostaAssembleia:
    // Uma proposta posta a votacao.
    id: str
    titulo: str
    declare descricao: str  <- ""
    declare fator_aparente: Optional[FatorPolarizacao]  <- nulo
    declare votacao_encerrada: bool  <- FALSO


// decorador: @dataclass
classe BlocoVotante:
    // Cluster de cidadaos que votam sistematicamente juntos.
    id: str
    declare membros: List[str]  <- field(default_factory=list)
    declare coesao: float  <- 0.0  // 0-1, quao alinhado vota o bloco
    declare fator_dominante: Optional[FatorPolarizacao]  <- nulo


// decorador: @dataclass
classe MetricaPolarizacao:
    // Snapshot da polarizacao numa assembleia.
    assembleia_id: str
    num_cidadaos: int
    num_blocos: int
    indice_divisao: float   // 0-1, quao rachada esta a votacao
    indice_tribalismo: float   // 0-1, quao identica e a tribo a votacao
    indice_ruptura_epistemica: float   // 0-1, sinais de realidades de fato separadas
    declare nivel: NivelPolarizacao  <- NivelPolarizacao.SAUDAVEL
    declare veredito: str  <- ""


// decorador: @dataclass
classe AuditoriaPolitica:
    // Resultado do gate P9 numa politica publica.
    politica_id: str
    veredito: VereditoAuditoria
    declare taticas_detectadas: List[TaticaPolarizante]  <- field(default_factory=list)
    declare fatores_acionados: List[FatorPolarizacao]  <- field(default_factory=list)
    declare score_polarizante: float  <- 0.0  // 0-100
    declare mitigacoes: List[str]  <- field(default_factory=list)
    declare justificativa: str  <- ""


// ============================================================================
// 3. TABELA DE SINAIS DE BALKANIZACAO EPISTEMICA
// ============================================================================

// Sinais de que a polarizacao passou de "discordo" para "realidade separada"
declare SINAIS_RUPTURA_EPISTEMICA: Dict[str, str]  <- {
    "fontes_exclusivas": "Cada bloco cita fontes que o outro bloco considera falsas por principio",
    "vocabulario_incomum": "Cada bloco usa vocabulario que o outro nao entende ou rejeita",
    "desumanizacao": "Membros de um bloco descrevem o outro como inimigo, nao como cidadao",
    "voto_identidade": "Voto decidido por identidade tribal, nao por merito da proposta",
    "zero_trust": "Nenhuma afirmacao do outro lado e aceita mesmo quando factualmente correta",
    "purity_test": "Membros sao punidos por reconhecer merito em argumento do outro lado",
    "conspiracy_default": "Derrota politica e automaticamente atribuida a conspiracao",
    "violencia_normalizada": "Violencia contra o outro bloco e tratada como legítima",
}


// ============================================================================
// 4. ENGINE
// ============================================================================

classe AntiPolarizacaoEngine:
    // Motor do P9: detecta polarizacao, audita politicas, previne bloqueio.

    funcao __init__(self) retorna None:
        self.propostas: Dict[str, PropostaAssembleia] = {}
        self.votos: List[VotoCidadao] = []
        self.blocos: Dict[str, BlocoVotante] = {}
        self.auditorias: Dict[str, AuditoriaPolitica] = {}
        self._prop_id = 0
        self._bloco_id = 0

    // -- cadastro ----------------------------------------------------------

    funcao _prop_id_novo(self) retorna str:
        self._prop_id += 1
        retorne f"PROP-{self._prop_id:04d}"

    funcao _bloco_id_novo(self) retorna str:
        self._bloco_id += 1
        retorne f"BLOCO-{self._bloco_id:04d}"

    def registrar_proposta(
        self,
        titulo: str,
        declare descricao: str  <- "",
        declare fator_aparente: Optional[FatorPolarizacao]  <- nulo,
    ) -> PropostaAssembleia:
        p <- PropostaAssembleia(
            id <- self._prop_id_novo(),
            titulo <- titulo,
            descricao <- descricao,
            fator_aparente <- fator_aparente,
        )
        self.propostas[p.id] = p
        retorne p

    def registrar_voto(
        self,
        cidadao_id: str,
        proposta_id: str,
        a_favor: bool,
        declare justificativa: str  <- "",
    ) -> VotoCidadao:
        v <- VotoCidadao(
            cidadao_id <- cidadao_id,
            proposta_id <- proposta_id,
            a_favor <- a_favor,
            justificativa <- justificativa,
        )
        self.votos.append(v)
        retorne v

    funcao registrar_votacao_em_lote(self, votacoes: List[Tuple[str, str, bool]]) retorna None:
        // Registra varios votos: (cidadao_id, proposta_id, a_favor).
        for cid, pid, fav in votacoes:
            self.registrar_voto(cid, pid, fav)

    funcao encerrar_proposta(self, proposta_id: str) retorna None:
        se proposta_id in self.propostas entao:
            self.propostas[proposta_id].votacao_encerrada = VERDADEIRO

    // -- deteccao de blocos ------------------------------------------------

    funcao detectar_blocos(self, num_propostas_min: int = 3) retorna List[BlocoVotante]:
        // 
        Detecta clusters de cidadaos que votam sistematicamente juntos.
        Algoritmo simples: agrupa por padrao de voto (assinatura binaria).
        // 
        self.blocos.clear()
        // construir assinatura de voto por cidadao
        declare assinaturas: Dict[str, List[bool]]  <- defaultdict(list)
        prop_ids_ordenadas <- sorted(self.propostas.keys())
        para cada pid em prop_ids_ordenadas:
            votos_prop <- {v.cidadao_id: v.a_favor for v in self.votos if v.proposta_id == pid}
            para cada cid em votos_prop:
                assinaturas[cid].append(votos_prop[cid])
        // so analisa cidadaos com votos suficientes
        cidadaos_validos <- {c: s for c, s in assinaturas.items() if len(s) >= num_propostas_min}
        se NAO  cidadaos_validos entao:
            retorne []
        // agrupar por assinatura identica (simplificado)
        declare grupos: Dict[Tuple[bool, ...], List[str]]  <- defaultdict(list)
        para cada (cid, sig) em cidadaos_validos.items():
            grupos[tuple(sig)].append(cid)
        // criar blocos para grupos com >= 2 membros
        declare blocos_criados: List[BlocoVotante]  <- []
        para cada (sig, membros) em grupos.items():
            se len(membros) >= 2 entao:
                coesao <- 1.0  // grupo por assinatura identica tem coesao maxima
                b <- BlocoVotante(
                    id <- self._bloco_id_novo(),
                    membros <- list(membros),
                    coesao <- coesao,
                )
                self.blocos[b.id] = b
                blocos_criados.append(b)
        // se ha exatamente 2 blocos com tamanhos similares, e polarizacao classica
        se len(blocos_criados) == 2 entao:
            tamanhos <- sorted(len(b.membros) for b in blocos_criados)
            razao <- tamanhos[0] / tamanhos[1] if tamanhos[1] else 0
            if razao >= 0.4:   // 40-60 split indica polarizacao, nao minoria marginal
                blocos_criados[0].fator_dominante = FatorPolarizacao.IDEOLOGIA
                blocos_criados[1].fator_dominante = FatorPolarizacao.IDEOLOGIA
        retorne blocos_criados

    // -- metricas ----------------------------------------------------------

    funcao indice_divisao(self) retorna float:
        // 0=consenso, 1=rachura 50-50 em todas as propostas.
        se NAO  self.propostas entao:
            retorne 0.0
        prop_ids <- sorted(self.propostas.keys())
        soma <- 0.0
        count <- 0
        para cada pid em prop_ids:
            votos_prop <- [v.a_favor for v in self.votos if v.proposta_id == pid]
            se NAO  votos_prop entao:
                continue
            favor <- sum(1 for x in votos_prop if x)
            contra <- len(votos_prop) - favor
            total <- len(votos_prop)
            // divisao = 1 - |favor - contra| / total (0=unanimidade, 1=racha perfeita)
            d <- 1.0 - abs(favor - contra) / total
            soma <- soma + d
            count <- count + 1
        retorne round(soma / count, 3) if count else 0.0

    funcao indice_tribalismo(self) retorna float:
        // 0=voto por merito, 1=voto 100% determinado por bloco tribal.
        So conta como tribal se houver 2+ blocos OPOSTOS (votacao tribal de
        verdade). Um bloco unico de consenso nao e tribalismo -- e acordo."""
        blocos <- self.detectar_blocos()
        se len(blocos) < 2 entao:
            retorne 0.0
        // fracao de votos que sao "tribais" (cidadao esta num bloco)
        declare cids_em_blocos: Set[str]  <- set()
        para cada b em blocos:
            cids_em_blocos.update(b.membros)
        votos_tribais <- sum(1 for v in self.votos if v.cidadao_id in cids_em_blocos)
        total_votos <- len(self.votos)
        retorne round(votos_tribais / total_votos, 3) if total_votos else 0.0

    funcao indice_ruptura_epistemica(self, sinais_observados: List[str]) retorna float:
        // 0=realidade compartilhada, 1=ruptura epistemica total.
        se NAO  sinais_observados entao:
            retorne 0.0
        sinais_validos <- [s for s in sinais_observados if s in SINAIS_RUPTURA_EPISTEMICA]
        total_sinais <- len(SINAIS_RUPTURA_EPISTEMICA)
        retorne round(len(sinais_validos) / total_sinais, 3)

    funcao classificar_nivel(self, sinais_observados: Optional[List[str]] = None) retorna NivelPolarizacao:
        // Combina os 3 indices (+ sinais qualitativos) num nivel.
        div <- self.indice_divisao()
        trib <- self.indice_tribalismo()
        rupt <- self.indice_ruptura_epistemica(sinais_observados  OU  [])
        // ruptura epistemica e bloqueante
        se rupt >= 0.5 entao:
            retorne NivelPolarizacao.RUPTURA
        se div >= 0.8  E  trib >= 0.7 entao:
            retorne NivelPolarizacao.CRITICO
        se div >= 0.6  E  trib >= 0.5 entao:
            retorne NivelPolarizacao.ALTO
        se div >= 0.4 entao:
            retorne NivelPolarizacao.MODERADO
        se div >= 0.2 entao:
            retorne NivelPolarizacao.BAIXO
        retorne NivelPolarizacao.SAUDAVEL

    def medir_polarizacao(
        self,
        declare assembleia_id: str  <- "default",
        declare sinais_observados: Optional[List[str]]  <- nulo,
    ) -> MetricaPolarizacao:
        // Produz o snapshot completo de polarizacao da assembleia.
        blocos <- self.detectar_blocos()
        div <- self.indice_divisao()
        trib <- self.indice_tribalismo()
        rupt <- self.indice_ruptura_epistemica(sinais_observados  OU  [])
        nivel <- self.classificar_nivel(sinais_observados)
        cidadaos_unicos <- {v.cidadao_id for v in self.votos}
        se nivel == NivelPolarizacao.RUPTURA entao:
            veredito <- ("RUPTURA EPISTEMICA: realidades de fato separadas. "
                        "Assembleia nao pode deliberar ate restaurar chao de fato compartilhado.")
        senao se nivel == NivelPolarizacao.CRITICO entao:
            veredito <- ("CRITICO: votacao tribal dominante. Mediacao obrigatoria antes de qualquer nova votacao.")
        senao se nivel == NivelPolarizacao.ALTO entao:
            veredito <- "ALTO: confianca em queda. Deliberacao estruturada exigida."
        senao se nivel == NivelPolarizacao.MODERADO entao:
            veredito <- "MODERADO: blocos claros. Monitorar e facilitar dialogo."
        senao se nivel == NivelPolarizacao.BAIXO entao:
            veredito <- "BAIXO: dissenso saudavel com sinal de alinhamento tribal incipiente."
        senao:
            veredito <- "SAUDAVEL: dissenso produtivo, confianca preservada."
        retorne MetricaPolarizacao(
            assembleia_id <- assembleia_id,
            num_cidadaos <- len(cidadaos_unicos),
            num_blocos <- len(blocos),
            indice_divisao <- div,
            indice_tribalismo <- trib,
            indice_ruptura_epistemica <- rupt,
            nivel <- nivel,
            veredito <- veredito,
        )

    // -- GATE P9: auditoria de politica ------------------------------------

    def auditar_politica(
        self,
        politica_id: str,
        titulo: str,
        descricao: str,
        declare taticas_detectadas: Optional[List[TaticaPolarizante]]  <- nulo,
        declare fatores_acionados: Optional[List[FatorPolarizacao]]  <- nulo,
        declare sinais_ruptura: Optional[List[str]]  <- nulo,
    ) -> AuditoriaPolitica:
        // 
        GATE P9: toda politica publica deve passar por aqui antes da votacao.
        Avalia o potencial polarizante da politica, nao seu conteudo substantivo.
        // 
        taticas <- taticas_detectadas  OU  []
        fatores <- fatores_acionados  OU  []
        // score: soma ponderada de taticas (0-100)
        score_taticas <- min(100.0, sum(t.gravidade * 12 for t in taticas))
        // penalidade por fator identitario acionado (divisao identitaria e pior)
        fatores_identitarios <- {FatorPolarizacao.RELIGIAO, FatorPolarizacao.ETNIA,
                                FatorPolarizacao.IDENTIDADE, FatorPolarizacao.CULTURA}
        penalidade_fator <- sum(8 if f in fatores_identitarios else 4 for f in fatores)
        score <- min(100.0, score_taticas + penalidade_fator)
        // ruptura epistemica na assembleia agrava
        se sinais_ruptura entao:
            rupt <- self.indice_ruptura_epistemica(sinais_ruptura)
            score <- min(100.0, score + rupt * 30)

        declare mitigacoes: List[str]  <- []
        se TaticaPolarizante.OUTGROUP_DEHUMANIZATION in taticas entao:
            mitigacoes.append("Remover linguagem que desumaniza cidadaos do outro lado.")
        se TaticaPolarizante.FALSE_DICHOTOMY in taticas entao:
            mitigacoes.append("Apresentar 3+ opcoes, nao binomio nos-vs-eles.")
        se TaticaPolarizante.FEAR_MONGERING in taticas entao:
            mitigacoes.append("Substituir alarmismo por dados verificaveis e calmos.")
        se TaticaPolarizante.IDENTITY_BAITING in taticas entao:
            mitigacoes.append("Desacoplar a politica de identidade tribal (P9: Estado nao polariza).")
        se TaticaPolarizante.EPISTEMIC_BALKANIZATION in taticas entao:
            mitigacoes.append("Citar fontes reconhecidas por AMBOS os blocos (chao de fato compartilhado).")
        se any(f in fatores_identitarios for f in fatores) entao:
            mitigacoes.append("Reescrever sem apelar a divisao identitaria (religiao/etnia/identidade).")
        se score >= 40  E  score < 70 entao:
            mitigacoes.append("Submeter a deliberacao estruturada antes da votacao.")
        se score >= 70 entao:
            mitigacoes.append("Politica deve ser fundamentalmente reformulada.")

        se score >= 75 entao:
            veredito <- VereditoAuditoria.BLOQUEADA
            justif <- ("P9 VIOLADO: a politica e vetor de divisao identitaria. "
                      "Reescrever do zero sem acionar tribo.")
        senao se score >= 50 entao:
            veredito <- VereditoAuditoria.REJEITADA
            justif <- ("Potencial polarizante alto. Rejeitada ate mitigacoes aplicadas.")
        senao se score >= 25 entao:
            veredito <- VereditoAuditoria.APROVADA_COM_RESSALVAS
            justif <- ("Aprovada condicionalmente. Mitigacoes exigidas antes da votacao.")
        senao:
            veredito <- VereditoAuditoria.APROVADA
            justif <- "Baixo potencial polarizante. Livre para votacao."

        aud <- AuditoriaPolitica(
            politica_id <- politica_id,
            veredito <- veredito,
            taticas_detectadas <- taticas,
            fatores_acionados <- fatores,
            score_polarizante <- round(score, 1),
            mitigacoes <- mitigacoes,
            justificativa <- justif,
        )
        self.auditorias[politica_id] = aud
        retorne aud

    // -- protocolo de bloqueio assemblear ----------------------------------

    funcao protocolo_bloqueio(self, metrica: MetricaPolarizacao) retorna StatusBloqueio:
        // Define a resposta do sistema ao nivel de polarizacao detectado.
        se metrica.nivel == NivelPolarizacao.RUPTURA entao:
            retorne StatusBloqueio.ASSEMBLEIA_PAUSA
        se metrica.nivel == NivelPolarizacao.CRITICO entao:
            retorne StatusBloqueio.SUSPENDER_VOTACAO
        se metrica.nivel == NivelPolarizacao.ALTO entao:
            retorne StatusBloqueio.MEDIACAO_OBRIGATORIA
        se metrica.nivel == NivelPolarizacao.MODERADO entao:
            retorne StatusBloqueio.DELIBERACAO_ESTRUTURADA
        se metrica.nivel == NivelPolarizacao.BAIXO entao:
            retorne StatusBloqueio.ALERTA
        retorne StatusBloqueio.NENHUM

    funcao recomendacoes_mediacao(self, metrica: MetricaPolarizacao) retorna List[str]:
        // Acoes concretas para reduzir polarizacao, por nivel.
        declare recs: List[str]  <- []
        n <- metrica.nivel
        se n == NivelPolarizacao.SAUDAVEL entao:
            recs.append("Manter: dissenso produtivo e saudavel (P2).")
            retorne recs
        se n in (NivelPolarizacao.BAIXO, NivelPolarizacao.MODERADO) entao:
            recs.append("Facilitar dialogo estruturado entre blocos (nao debate livre -- agrava).")
            recs.append("Identificar o chao de fato compartilhado antes de divergir.")
            recs.append("Rotular taticas polarizantes quando aparecerem (metacognicao assemblear).")
        se n in (NivelPolarizacao.ALTO, NivelPolarizacao.CRITICO) entao:
            recs.append("Mediador profissional obrigatoria (OpenCommunityLeaders).")
            recs.append("Votacao adiada ate confianca minima restaurada.")
            recs.append("Deliberacao em sub-grupos mistos (quebra de bloco tribal).")
            recs.append("Auditar algoritmos de feed que podem estar amplificando (P8).")
        se n == NivelPolarizacao.RUPTURA entao:
            recs.append("EMERGENCIA: assembleia em pausa. Nao votar.")
            recs.append("Restaurar chao de fato: comissao de verificacao (HumanKnowledge).")
            recs.append("Dialogo individual antes de coletivo (quebra de tribalismo).")
            recs.append("Investigar captura narrativa externa (algoritmo, ator malicioso).")
            recs.append("Considerar OpenWololo se a divisao for irreparavel (separar, nao subjugar).")
        retorne recs

    // -- scorecard ---------------------------------------------------------

    funcao scorecard(self) retorna Dict[str, Any]:
        blocos <- self.detectar_blocos()
        retorne {
            "propostas_registradas": len(self.propostas),
            "votos_registrados": len(self.votos),
            "cidadaos_ativos": len({v.cidadao_id for v in self.votos}),
            "blocos_detectados": len(blocos),
            "indice_divisao": self.indice_divisao(),
            "indice_tribalismo": self.indice_tribalismo(),
            "politicas_auditadas": len(self.auditorias),
            "politicas_bloqueadas": sum(1 for a in self.auditorias.values()
                                        if a.veredito == VereditoAuditoria.BLOQUEADA),
            "politicas_aprovadas": sum(1 for a in self.auditorias.values()
                                       if a.veredito in (VereditoAuditoria.APROVADA,
                                                         VereditoAuditoria.APROVADA_COM_RESSALVAS)),
        }


// ============================================================================
// 5. DEMO
// ============================================================================

funcao _demo() retorna None:
    e <- AntiPolarizacaoEngine()

    print("=" * 70)
    print("OpenAntiPolarization -- P9: O Estado NAO Polariza")
    print("=" * 70)

    // --- Cenario 1: assembleia saudavel ---
    print("\n[CENARIO 1] Assembleia saudavel (dissenso produtivo)")
    p1 <- e.registrar_proposta("Construir escola no norte", fator_aparente=FatorPolarizacao.REGIAO)
    p2 <- e.registrar_proposta("Ampliar enfermaria central")
    p3 <- e.registrar_proposta("Importar capoeira como educacao fisica")
    // votacao dispersa (nao tribal) -- majoritario com dissenso minoritario
    e.registrar_votacao_em_lote([
        ("cid_01", p1.id, VERDADEIRO), ("cid_02", p1.id, VERDADEIRO), ("cid_03", p1.id, VERDADEIRO),
        ("cid_04", p1.id, VERDADEIRO), ("cid_05", p1.id, FALSO),
        ("cid_01", p2.id, VERDADEIRO), ("cid_02", p2.id, VERDADEIRO), ("cid_03", p2.id, VERDADEIRO),
        ("cid_04", p2.id, VERDADEIRO), ("cid_05", p2.id, VERDADEIRO),
        ("cid_01", p3.id, VERDADEIRO), ("cid_02", p3.id, VERDADEIRO), ("cid_03", p3.id, VERDADEIRO),
        ("cid_04", p3.id, FALSO), ("cid_05", p3.id, VERDADEIRO),
    ])
    m1 <- e.medir_polarizacao("assembleia_norte_v1")
    print(f"  Divisao: {m1.indice_divisao:.2f} | Tribalismo: {m1.indice_tribalismo:.2f}")
    print(f"  Nivel: {m1.nivel.rotulo}")
    print(f"  Veredito: {m1.veredito}")
    print(f"  Protocolo: {e.protocolo_bloqueio(m1).rotulo}")

    // --- Cenario 2: assembleia polarizada (2 blocos tribais) ---
    print("\n[CENARIO 2] Assembleia polarizada (votacao tribal)")
    e2 <- AntiPolarizacaoEngine()
    pa <- e2.registrar_proposta("Politica A", fator_aparente=FatorPolarizacao.IDEOLOGIA)
    pb <- e2.registrar_proposta("Politica B", fator_aparente=FatorPolarizacao.IDEOLOGIA)
    pc <- e2.registrar_proposta("Politica C", fator_aparente=FatorPolarizacao.IDEOLOGIA)
    pd <- e2.registrar_proposta("Politica D", fator_aparente=FatorPolarizacao.IDEOLOGIA)
    // Bloco X (5 cidadaos) vota SIM em tudo; Bloco Y (5 cidadaos) vota NAO em tudo
    bloco_x <- [f"x_{i:02d}" for i in range(5)]
    bloco_y <- [f"y_{i:02d}" for i in range(5)]
    para cada prop em [pa, pb, pc, pd]:
        para cada cid em bloco_x:
            e2.registrar_voto(cid, prop.id, VERDADEIRO)
        para cada cid em bloco_y:
            e2.registrar_voto(cid, prop.id, FALSO)
    m2 <- e2.medir_polarizacao("assembleia_polarizada",
                              sinais_observados <- ["voto_identidade", "zero_trust"])
    print(f"  Divisao: {m2.indice_divisao:.2f} | Tribalismo: {m2.indice_tribalismo:.2f}")
    print(f"  Ruptura epistemica: {m2.indice_ruptura_epistemica:.2f}")
    print(f"  Nivel: {m2.nivel.rotulo}")
    print(f"  Veredito: {m2.veredito}")
    print(f"  Protocolo: {e2.protocolo_bloqueio(m2).rotulo}")
    print(f"  Blocos detectados: {m2.num_blocos}")
    print(f"  Recomendacoes:")
    para cada r em e2.recomendacoes_mediacao(m2):
        print(f"    - {r}")

    // --- Cenario 3: ruptura epistemica (realidades separadas) ---
    print("\n[CENARIO 3] Ruptura epistemica (EMERGENCIA)")
    e3 <- AntiPolarizacaoEngine()
    para cada i em range(5):
        p <- e3.registrar_proposta(f"Proposta {i}")
    todos_sinais <- list(SINAIS_RUPTURA_EPISTEMICA.keys())
    // votacao tribal
    para cada prop em list(e3.propostas.values()):
        para cada j em range(6):
            e3.registrar_voto(f"tribo_a_{j}", prop.id, VERDADEIRO)
            e3.registrar_voto(f"tribo_b_{j}", prop.id, FALSO)
    m3 <- e3.medir_polarizacao("assembleia_ruptura", sinais_observados=todos_sinais)
    print(f"  Ruptura epistemica: {m3.indice_ruptura_epistemica:.2f}")
    print(f"  Nivel: {m3.nivel.rotulo}")
    print(f"  Protocolo: {e3.protocolo_bloqueio(m3).rotulo}")
    print(f"  RECOMENDACOES DE EMERGENCIA:")
    para cada r em e3.recomendacoes_mediacao(m3):
        print(f"    - {r}")

    // --- GATE P9: auditoria de politicas ---
    print("\n" + "=" * 70)
    print("[GATE P9] Auditoria de politicas publicas")
    print("=" * 70)

    // Politica 1: aprovada (baixo potencial polarizante)
    a1 <- e.auditar_politica(
        "pol-escola", "Construir escola no norte",
        "Politica de infraestrutura educacional sem apelo identitario.",
        taticas_detectadas <- [],
        fatores_acionados <- [FatorPolarizacao.REGIAO],
    )
    print(f"\n  [{a1.politica_id}] {a1.veredito.rotulo} (score={a1.score_polarizante})")
    print(f"    {a1.justificativa}")

    // Politica 2: aprovada com ressalvas
    a2 <- e.auditar_politica(
        "pol-saude", "Reforma do sistema de saude",
        "Politica com algum alarmismo na apresentacao.",
        taticas_detectadas <- [TaticaPolarizante.FEAR_MONGERING],
        fatores_acionados <- [],
    )
    print(f"\n  [{a2.politica_id}] {a2.veredito.rotulo} (score={a2.score_polarizante})")
    print(f"    {a2.justificativa}")
    para cada mit em a2.mitigacoes:
        print(f"    Mitigacao: {mit}")

    // Politica 3: rejeitada (potencial alto)
    a3 <- e.auditar_politica(
        "pol-seguranca", "Lei de seguranca publica",
        "Politica apresentada com falsa dicotomia e alarmismo.",
        taticas_detectadas <- [TaticaPolarizante.FALSE_DICHOTOMY, TaticaPolarizante.FEAR_MONGERING],
        fatores_acionados <- [FatorPolarizacao.IDEOLOGIA],
    )
    print(f"\n  [{a3.politica_id}] {a3.veredito.rotulo} (score={a3.score_polarizante})")
    print(f"    {a3.justificativa}")
    para cada mit em a3.mitigacoes:
        print(f"    Mitigacao: {mit}")

    // Politica 4: BLOQUEADA (vetor de divisao identitaria)
    a4 <- e.auditar_politica(
        "pol-identidade", "Declaracao sobre valores culturais",
        "Politica que aciona divisao religiosa e identitaria explicita.",
        taticas_detectadas <- [TaticaPolarizante.IDENTITY_BAITING,
                            TaticaPolarizante.OUTGROUP_DEHUMANIZATION,
                            TaticaPolarizante.EPISTEMIC_BALKANIZATION],
        fatores_acionados <- [FatorPolarizacao.RELIGIAO, FatorPolarizacao.IDENTIDADE],
        sinais_ruptura <- ["zero_trust", "purity_test"],
    )
    print(f"\n  [{a4.politica_id}] {a4.veredito.rotulo} (score={a4.score_polarizante})")
    print(f"    {a4.justificativa}")
    para cada mit em a4.mitigacoes:
        print(f"    Mitigacao: {mit}")

    // --- Scorecard ---
    print("\n" + "=" * 70)
    print("[SCORECARD P9]")
    print("=" * 70)
    sc <- e.scorecard()
    para cada (k, v) em sc.items():
        print(f"  {k:.<28} {v}")

    // --- Catalogo de taticas ---
    print("\n[CATALOGO DE TATICAS POLARIZANTES AUDITADAS PELO ESTADO]")
    para cada t em TaticaPolarizante:
        print(f"  [{t.gravidade}] {t.rotulo}")

    // --- Sinais de ruptura epistemica ---
    print("\n[SINAIS DE RUPTURA EPISTEMICA (monitoramento continuo)]")
    para cada (chave, desc) em SINAIS_RUPTURA_EPISTEMICA.items():
        print(f"  {chave}: {desc}")

    // --- FILOSOFIA ---
    print("\n" + "=" * 70)
    print("FILOSOFIA -- P9: Por que o Estado nao pode polarizar")
    print("=" * 70)
    print("""
DISTINCAO FUNDAMENTAL:
  Diversidade de opiniao e DIREITO (P2). E saudavel. E combustivel da democracia.
  Polarizacao e DOENCA. Nao e "opiniao diferente". E realidade epistemica
  separada: duas tribos que nao so discordam, mas habitam mundos de fato
  diferentes, com zero confianca mutua e identidade fundida na tribo.

O ERRO LIBERAL:
  O liberalismo assume que "mais debate resolve polarizacao". Falso.
  Mais debate entre tribos epistemicamente separadas AMPLIFICA a polarizacao.
  O que resolve: (a) chao de fato compartilhado, (b) deliberacao estruturada,
  (c) Estado que se recusa a ser vetor de divisao identitaria.

POR QUE O ESTADO ESPECIFICAMENTE:
  O Estado tem monopolio da forca coercitiva. Se o Estado polariza, ele nao
  so reflete a divisao -- ele a INSTITUCIONALIZA. Politica publica que aciona
  tribo vira lei. Lei que aciona tribo perpertua a divisao por geracoes.
  P9 e a proibicao constitucional de o Estado ser vetor de divisao.

P9 NAO E CENSURA:
  P9 nao proibe discurso (isso violaria P2). P9 obriga o ESTADO a auditar
  suas proprias politicas quanto ao efeito polarizante. E um gate, como WCAG
  audita acessibilidade. Cidadao pode dizer o que quiser. O Estado nao pode
  GOVERNAR com divisao identitaria.

A CONEXAO COM P8 (IA):
  Algoritmos de feed que otimizam engajamento amplificam furia, nao verdade.
  Isso e a anti-tese do P8 (IA que amplia inteligencia humana). Engagement
  por furia e captura narrativa. P9 exige que o Estado audite algoritmos
  que afetam a assembleia -- nao para censurar, mas para nao ser capturado.

A UNICA SAIDA QUANDO A DIVISAO E IRREPARAVEL:
  Se duas comunidades habitam realidades epistemicas irrecuperavelmente
  separadas, a Republica nao as obriga a coexistir sob a mesma lei (isso
  recriaria coercicao). OpenWololo permite separar com dignidade -- duas
  assembleias, dois territorios, zero subordinacao. Melhor separar do que
  subjugar. Mas P9 trabalha para que isso seja ultimo recurso, nao rotina.
// )


se __name__ == "__main__" entao:
    _demo()

```
