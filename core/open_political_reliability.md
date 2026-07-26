# OpenPoliticalReliability -- Simulacao de Confiabilidade do Sujeito Politico

**Arquivo original:** `open-republic/core/open_political_reliability.py`

**Descricao:** =============================================================================
"O poder nao se mede pela quantidade de votos, mas pela qualidade do processo."
A Republica NAO confia em sujeitos politicos. Confia em PROCESSOS.
Mas para AUDITAR processos, precisa avaliar a CONFIABILIDADE dos sujeitos
que operam dentro deles.
Este modulo e um SIMULADOR de confiabilidade politica. NAO e tribunal.
NAO condena. AVALIA com base em indicadores verificaveis e produz um
SCORE de confiabilidade que a assembleia pode usar para decidir se um
sujeito pode operar dentro das instituicoes da Republica.
PRINCIPIO (P4): A transparencia e radical. Se um sujeito opera no poder,
todo seu historico e auditavel. Nao existe "privacidade politica" para
quem exerce poder publico -- poder publico e PUBLICO.
O QUE O SIMULADOR MEDE:
1. USO DE APARELHO PUBLICO para beneficio eleitoral
2. COMPRA DE VOTO (clientelismo, bolsa, promessa)
3. CONTINUIDADE NO PODER (quantos mandatos, indicio de perpetuacao)
4. DESMANCHE DE ALTERNATIVAS (impede novas candidaturas no proprio campo)
5. CORRUPCAO SISTEMICA (e caso isolado ou padrao?)
6. MANIPULACAO DE INFORMACAO (bots, redes, narrativa fabricada)
7. TRANSPARENCIA (abre dados ou esconde?)
8. RENOVACAO DE ELITES (treina sucessores ou se torna insubstituivel?)
ALINHAMENTO CONSTITUCIONAL:
- P1: Confianca politica nao heranca. Cada mandato auditado.
- P4: Democracia radical exige sujeitos confiaveis. Processo corrompido = vitro eleitoral.
- P9: Sujeito que polariza para perpetuar VIOLA o P9 (Estado nao polariza).
Author: OpenRepublic Team

---

```portugol

// !/usr/bin/env python3
// 
OpenPoliticalReliability -- Simulacao de Confiabilidade do Sujeito Politico
=============================================================================
"O poder nao se mede pela quantidade de votos, mas pela qualidade do processo."

A Republica NAO confia em sujeitos politicos. Confia em PROCESSOS.
Mas para AUDITAR processos, precisa avaliar a CONFIABILIDADE dos sujeitos
que operam dentro deles.

Este modulo e um SIMULADOR de confiabilidade politica. NAO e tribunal.
NAO condena. AVALIA com base em indicadores verificaveis e produz um
SCORE de confiabilidade que a assembleia pode usar para decidir se um
sujeito pode operar dentro das instituicoes da Republica.

PRINCIPIO (P4): A transparencia e radical. Se um sujeito opera no poder,
todo seu historico e auditavel. Nao existe "privacidade politica" para
quem exerce poder publico -- poder publico e PUBLICO.

O QUE O SIMULADOR MEDE:
1. USO DE APARELHO PUBLICO para beneficio eleitoral
2. COMPRA DE VOTO (clientelismo, bolsa, promessa)
3. CONTINUIDADE NO PODER (quantos mandatos, indicio de perpetuacao)
4. DESMANCHE DE ALTERNATIVAS (impede novas candidaturas no proprio campo)
5. CORRUPCAO SISTEMICA (e caso isolado ou padrao?)
6. MANIPULACAO DE INFORMACAO (bots, redes, narrativa fabricada)
7. TRANSPARENCIA (abre dados ou esconde?)
8. RENOVACAO DE ELITES (treina sucessores ou se torna insubstituivel?)

ALINHAMENTO CONSTITUCIONAL:
- P1: Confianca politica nao heranca. Cada mandato auditado.
- P4: Democracia radical exige sujeitos confiaveis. Processo corrompido = vitro eleitoral.
- P9: Sujeito que polariza para perpetuar VIOLA o P9 (Estado nao polariza).

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

classe TipoIndicador herda de Enum:
    // Dimensoes de avaliacao da confiabilidade politica.
    USO_APARELHO_PUBLICO <- ("uso_aparelho", "Uso de aparelho de Estado para fim eleitoral", 10)
    COMPRA_VOTO <- ("compra_voto", "Compra de voto / clientelismo / bolsa-eleicao", 10)
    CONTINUIDADE_PODER <- ("continuidade", "Perpetuacao no poder (mandatos sucessivos)", 8)
    DESMANCHE_ALTERNATIVAS <- ("desmanche", "Desmanche de novas candidaturas no proprio campo", 7)
    CORRUPCAO_SISTEMICA <- ("corrupcao", "Corrupcao sistemica (padrao, nao caso isolado)", 10)
    MANIPULACAO_INFORMACAO <- ("manipulacao_info", "Manipulacao de informacao (bots, narrativa fabricada)", 8)
    OPACIDADE <- ("opacidade", "Falta de transparencia / esconda dados publicos", 6)
    PERSONALISMO <- ("personalismo", "Personalismo (se torna insubstituivel, sem sucessor)", 7)
    VIOLACAO_PRINCIPIOS <- ("violacao_principios", "Violacao de principios constitucionais", 9)
    MILITANCIA_FINANCEIRA <- ("militancia_fin", "Militancia comprada (cargo em troca de apoio)", 7)

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]

    // decorador: @property
    funcao peso(self) retorna int:
        // Peso do indicador no score (1-10, 10=maximo impacto negativo).
        retorne self.value[2]


classe NivelConfiabilidade herda de Enum:
    // Niveis de confiabilidade politica do sujeito.
    CONFIGAVEL <- ("confiavel", "Confiavel: sem indicadores graves, processo transparente", 100, 80)
    ACEITAVEL <- ("aceitavel", "Aceitavel: indicadores leves, monitorar", 79, 60)
    PREOCUPANTE <- ("preocupante", "Preocupante: multiplos indicadores, assembleia avalia", 59, 40)
    ALTO_RISCO <- ("alto_risco", "Alto risco: padrao de manipulacao sistêmica", 39, 20)
    INACEITAVEL <- ("inaceitavel", "Inaceitavel: processo corrompido, nao opera na Republica", 19, 0)

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]

    // decorador: @property
    funcao score_max(self) retorna int:
        retorne self.value[2]

    // decorador: @property
    funcao score_min(self) retorna int:
        retorne self.value[3]


classe MetodoManipulacao herda de Enum:
    // Metodos de manipulacao do processo politico.
    BOTS_REDES <- ("bots_redes", "Bots e operacao de redes sociais")
    APARELHO_ELEITORAL <- ("aparelho_eleitoral", "Maquina publica a servico de candidatura")
    CLIENTELISMO <- ("clientelismo", "Troca de beneficio por voto")
    CARGOS_TROCA <- ("cargos_troca", "Distribuicao de cargos em troca de apoio")
    NARRATIVA_FABRICADA <- ("narrativa_fabricada", "Construcao de narrativa falsa")
    IMPEDIR_CANDIDATURA <- ("impedir_candidatura", "Impedir surgimento de novas candidaturas")
    JUDICIALIZACAO_ARMA <- ("judicializacao_arma", "Usar sistema judicial contra oponentes")
    MIDIA_COMPRADA <- ("midia_comprada", "Comprar cobertura midiatica")
    FINANCIAMENTO_OCULTO <- ("financiamento_oculto", "Caixa 2 / financiamento nao declarado")
    MEDO_E_AMEACA <- ("medo_ameaca", "Gerar medo na populacao para colher votos")

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]


classe GraveEvidencia herda de Enum:
    // Grau de evidencia de um indicador (principio: sem provas nao condena).
    COMPROVADO_JUDICIAL <- ("comprovado_judicial", "Comprovado judicialmente (sentenca transitada)", 1.0)
    INVESTIGACAO_OFICIAL <- ("investigacao_oficial", "Investigacao oficial em curso", 0.7)
    EVIDENCIA_JORNALISTICA <- ("evidencia_jornalistica", "Evidencia jornalistica consistente", 0.6)
    INDICIO_FORTE <- ("indicio_forte", "Indicio forte (multiplos sinais convergentes)", 0.5)
    DENUNCIA <- ("denuncia", "Denuncia formal sem comprovacao", 0.3)
    SUSPEITA <- ("suspeita", "Suspeita / opiniao publica sem comprovacao", 0.1)

    // decorador: @property
    funcao id(self) retorna str:
        retorne self.value[0]

    // decorador: @property
    funcao rotulo(self) retorna str:
        retorne self.value[1]

    // decorador: @property
    funcao fator_confianca(self) retorna float:
        // Quanto este grau de evidencia contribui (0-1). Sem prova, nao condena.
        retorne self.value[2]


classe StatusVeredito herda de Enum:
    // Veredito da simulacao de confiabilidade.
    APROVADO <- ("aprovado", "Sujeito pode operar na Republica")
    MONITORAR <- ("monitorar", "Pode operar com monitoramento continuo")
    RESTRITO <- ("restrito", "Operacao restrita (sem cargo de poder decisiorio)")
    SUSPEITO <- ("suspeito", "Suspeito: assembleia decide caso a caso")
    VETADO <- ("vetado", "Vetado: processo corrompido, nao exerce poder na Republica")

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
classe IndicadorPolitico:
    // Um indicador de (in)confiabilidade do sujeito politico.
    tipo: TipoIndicador
    descricao: str
    grau_evidencia: GraveEvidencia
    declare ocorrencias: int  <- 1  // quantas vezes detectado
    declare periodo: str  <- ""  // "2003-2022", "eleicao 2022", etc.
    declare metodos: List[MetodoManipulacao]  <- field(default_factory=list)
    declare detalhe: str  <- ""


// decorador: @dataclass
classe EventoPolitico:
    // Um evento verificavel na trajetoria do sujeito.
    id: str
    ano: str
    descricao: str
    tipo: str                      // "eleicao", "investigacao", "denuncia", "politica publica"
    declare impacto_confiabilidade: int  <- 0  // -10 a +10 (negativo=reduz, positivo=aumenta)
    declare evidencia: GraveEvidencia  <- GraveEvidencia.SUSPEITA


// decorador: @dataclass
classe AvaliacaoConfiabilidade:
    // Resultado completo da avaliacao de um sujeito politico.
    sujeito: str
    cargo: str
    mandatos: int
    score: int                     // 0-100 (100=maxima confiabilidade)
    nivel: NivelConfiabilidade
    veredito: StatusVeredito
    declare indicadores: List[IndicadorPolitico]  <- field(default_factory=list)
    declare pontos_forte: List[str]  <- field(default_factory=list)
    declare pontos_fraco: List[str]  <- field(default_factory=list)
    declare recomendacoes: List[str]  <- field(default_factory=list)
    declare justificativa: str  <- ""


// decorador: @dataclass
classe SimulacaoCenario:
    // Simulacao de cenario: o que acontece se o sujeito continuar no poder.
    cenario: str
    probabilidade_pct: float       // 0-100
    impacto_democracia: str        // descricao do impacto no processo democratico
    impacto_republica: str         // descricao do impacto se integrar a Republica
    declare acao_recomendada: str  <- ""


// ============================================================================
// 3. ENGINE
// ============================================================================

classe ConfiabilidadeEngine:
    // Motor de simulacao de confiabilidade politica.

    funcao __init__(self) retorna None:
        self.eventos: List[EventoPolitico] = []
        self._ev_id = 0

    funcao _ev_novo_id(self) retorna str:
        self._ev_id += 1
        retorne f"EV-{self._ev_id:04d}"

    def registrar_evento(
        self,
        ano: str,
        descricao: str,
        tipo: str,
        declare impacto: int  <- 0,
        declare evidencia: GraveEvidencia  <- GraveEvidencia.SUSPEITA,
    ) -> EventoPolitico:
        ev <- EventoPolitico(
            id <- self._ev_novo_id(),
            ano <- ano,
            descricao <- descricao,
            tipo <- tipo,
            impacto_confiabilidade <- impacto,
            evidencia <- evidencia,
        )
        self.eventos.append(ev)
        retorne ev

    // -- avaliacao ---------------------------------------------------------

    def avaliar(
        self,
        sujeito: str,
        cargo: str,
        mandatos: int,
        indicadores: List[IndicadorPolitico],
        declare eventos: Optional[List[EventoPolitico]]  <- nulo,
    ) -> AvaliacaoConfiabilidade:
        // 
        Avalia a confiabilidade de um sujeito politico.
        Score comeca em 100 e cada indicador REDUZ proporcionalmente.
        // 
        score <- 100
        declare pontos_fraco: List[str]  <- []
        declare pontos_forte: List[str]  <- []

        para cada ind em indicadores:
            // penalidade = peso do indicador * fator de evidencia * sqrt(ocorrencias)
            // importa math
            penalidade <- ind.tipo.peso * ind.grau_evidencia.fator_confianca * math.sqrt(ind.ocorrencias)
            penalidade <- min(penalidade, 25)  // teto por indicador
            score <- score - penalidade
            pontos_fraco.append(
                f"[{ind.tipo.rotulo}] {ind.descricao} "
                f"(evidencia: {ind.grau_evidencia.rotulo}, ocorrencias: {ind.ocorrencias})"
            )

        // penalidade por perpetuacao
        se mandatos >= 4 entao:
            score <- score - 10
            pontos_fraco.append(f"Perpetuacao: {mandatos} mandatos (risco de insubstituibilidade).")
        senao se mandatos >= 3 entao:
            score <- score - 5
            pontos_fraco.append(f"Continuidade: {mandatos} mandatos (monitorar renovacao).")

        // eventos adicionais (se houver)
        se eventos entao:
            para cada ev em eventos:
                se ev.impacto_confiabilidade < 0 entao:
                    score <- score + ev.impacto_confiabilidade  // impacto negativo reduz score
                    pontos_fraco.append(f"{ev.ano}: {ev.descricao} ({ev.evidencia.rotulo})")
                senao se ev.impacto_confiabilidade > 0 entao:
                    score <- min(100, score + ev.impacto_confiabilidade)
                    pontos_forte.append(f"{ev.ano}: {ev.descricao}")

        score <- max(0, min(100, int(round(score))))

        // classificar nivel
        nivel <- self._classificar_nivel(score)

        // veredito
        veredito <- self._veredito_por_nivel(nivel, mandatos)

        // recomendacoes
        recomendacoes <- self._gerar_recomendacoes(indicadores, nivel, mandatos)

        // justificativa
        justificativa <- self._gerar_justificativa(sujeito, score, nivel, indicadores, mandatos)

        retorne AvaliacaoConfiabilidade(
            sujeito <- sujeito,
            cargo <- cargo,
            mandatos <- mandatos,
            score <- score,
            nivel <- nivel,
            veredito <- veredito,
            indicadores <- indicadores,
            pontos_forte <- pontos_forte,
            pontos_fraco <- pontos_fraco,
            recomendacoes <- recomendacoes,
            justificativa <- justificativa,
        )

    funcao _classificar_nivel(self, score: int) retorna NivelConfiabilidade:
        para cada n em NivelConfiabilidade:
            se n.score_min <= score <= n.score_max entao:
                retorne n
        retorne NivelConfiabilidade.INACEITAVEL

    funcao _veredito_por_nivel(self, nivel: NivelConfiabilidade, mandatos: int) retorna StatusVeredito:
        se nivel == NivelConfiabilidade.CONFIGAVEL entao:
            retorne StatusVeredito.APROVADO
        se nivel == NivelConfiabilidade.ACEITAVEL entao:
            retorne StatusVeredito.MONITORAR
        se nivel == NivelConfiabilidade.PREOCUPANTE entao:
            retorne StatusVeredito.RESTRITO
        se nivel == NivelConfiabilidade.ALTO_RISCO entao:
            retorne StatusVeredito.SUSPEITO
        retorne StatusVeredito.VETADO

    def _gerar_recomendacoes(
        self, indicadores: List[IndicadorPolitico], nivel: NivelConfiabilidade, mandatos: int
    ) -> List[str]:
        declare recs: List[str]  <- []
        // verificar se ha uso de aparelho publico
        tipos_ativos <- {ind.tipo for ind in indicadores}
        se TipoIndicador.USO_APARELHO_PUBLICO in tipos_ativos entao:
            recs.append("Auditar uso de recursos publicos em periodo eleitoral (OpenPublicAudit).")
        se TipoIndicador.COMPRA_VOTO in tipos_ativos entao:
            recs.append("Implementar OpenVoteIntegrity: rastrear fluxo de beneficios antes de eleicao.")
        se TipoIndicador.MANIPULACAO_INFORMACAO in tipos_ativos entao:
            recs.append("Auditar bots e operacao de redes (P9: Estado nao polariza via algoritmo).")
        se TipoIndicador.DESMANCHE_ALTERNATIVAS in tipos_ativos entao:
            recs.append("Proteger pluralismo interno: assembleia garante direito a candidatura alternativa.")
        se TipoIndicador.PERSONALISMO in tipos_ativos  OU  mandatos >= 3 entao:
            recs.append("Exigir plano de successao: sujeito treina substituto ou nao exerce novo mandato.")
        se TipoIndicador.CORRUPCAO_SISTEMICA in tipos_ativos entao:
            recs.append("Investigacao independente (OpenJudicialAudit) antes de qualquer integracao.")
        se nivel in (NivelConfiabilidade.ALTO_RISCO, NivelConfiabilidade.INACEITAVEL) entao:
            recs.append("VETAR exercicio de cargo com poder decisiorio ate restaurar processo.")
            recs.append("Assembleia avalia se o SUJEITO ou o SISTEMA esta corrompido (P4).")
        retorne recs

    def _gerar_justificativa(
        self, sujeito: str, score: int, nivel: NivelConfiabilidade,
        indicadores: List[IndicadorPolitico], mandatos: int,
    ) -> str:
        count <- len(indicadores)
        graves <- sum(1 for i in indicadores if i.grau_evidencia.fator_confianca >= 0.5)
        retorne (
            f"Sujeito '{sujeito}' avaliado com score {score}/100 ({nivel.rotulo}). "
            f"{count} indicadores detectados, {graves} com evidencia forte ou superior. "
            f"{mandatos} mandatos. Veredito baseado em indicadores verificaveis, "
            f"nao em opiniao. A assembleia tem autoridade final (P4)."
        )

    // -- simulacao de cenarios ---------------------------------------------

    def simular_cenarios(
        self, avaliacao: AvaliacaoConfiabilidade
    ) -> List[SimulacaoCenario]:
        // Simula o que acontece em diferentes cenarios.
        declare cenarios: List[SimulacaoCenario]  <- []
        score <- avaliacao.score

        // Cenario 1: sujeito continua no poder
        se score < 40 entao:
            prob <- 85
            impacto_dem <- "Processo democratico degenerado: voto e transacao, nao deliberacao."
            impacto_rep <- "Se integrar a Republica, corrompe o processo. Assembleia capturada."
        senao se score < 60 entao:
            prob <- 60
            impacto_dem <- "Erosao da confianca institucional. Alternativas sufocadas."
            impacto_rep <- "Integracao arriscada. Monitoramento continuo necessario."
        senao:
            prob <- 25
            impacto_dem <- "Risco baixo de degeneracao. Renovacao possivel."
            impacto_rep <- "Integracao com salvaguardas."
        cenarios.append(SimulacaoCenario(
            cenario <- "Sujeito continua exercendo poder (status quo)",
            probabilidade_pct <- prob,
            impacto_democracia <- impacto_dem,
            impacto_republica <- impacto_rep,
            acao_recomendada <- "Votar limitacao de mandatos + auditoria continua." if score < 60 else "Monitorar.",
        ))

        // Cenario 2: sujeito e substituido por sucessor treinado
        cenarios.append(SimulacaoCenario(
            cenario <- "Sujeito e substituido por sucessor da mesma equipe",
            probabilidade_pct <- 70 if avaliacao.mandatos >= 3 else 40,
            impacto_democracia <- (
                "Equipe perpetua sem a 'cara'. Pode ser pior (menos escrutinio) ou melhor (renovacao)."
            ),
            impacto_republica <- "Avaliar a EQUIPE, nao so o sujeito. Se a equipe corrompeu o processo, trocar a cara nao resolve.",
            acao_recomendada <- "Auditar a EQUIPE (OpenTeamAudit), nao so o sujeito.",
        ))

        // Cenario 3: nova candidatura surge (sem a maquina)
        cenarios.append(SimulacaoCenario(
            cenario <- "Nova candidatura emerge fora da maquina",
            probabilidade_pct <- 30 if score < 40 else 50,
            impacto_democracia <- "Renovacao democratica real. Risco de ser destruida pela maquina instalada.",
            impacto_republica <- "Oportunidade de integrar sujeito sem divida com aparelho corrompido.",
            acao_recomendada <- "PROTEGER a nova candidatura (P4: democracia radical exige pluralismo real).",
        ))

        // Cenario 4: processo e reestruturado (sem o sujeito)
        cenarios.append(SimulacaoCenario(
            cenario <- "Processo politico reestruturado (Nova Republica)",
            probabilidade_pct <- 100,  // e a proposta da propria Republica
            impacto_democracia <- "Fim do ciclo de manipulacao. Voto = deliberacao, nao transacao.",
            impacto_republica <- "O sujeito e avaliado em processo NOVO. Divida com o sistema antigo documentada, nao ignorada.",
            acao_recomendada <- "Assembleia constituinte decide: reintegrar com restricoes ou comecar do zero.",
        ))

        retorne cenarios

    // -- comparacao: sujeito A vs sujeito B --------------------------------

    def comparar_sujeitos(
        self, a: AvaliacaoConfiabilidade, b: AvaliacaoConfiabilidade
    ) -> str:
        // Compara dois sujeitos politicos.
        diff <- a.score - b.score
        se abs(diff) < 5 entao:
            relacao <- "equivalentes em confiabilidade"
        senao se diff > 0 entao:
            relacao <- f"'{a.sujeito}' mais confiavel por {diff} pontos"
        senao:
            relacao <- f"'{b.sujeito}' mais confiavel por {abs(diff)} pontos"
        retorne (
            f"COMPARACAO:\n"
            f"  {a.sujeito}: score {a.score} ({a.nivel.rotulo})\n"
            f"  {b.sujeito}: score {b.score} ({b.nivel.rotulo})\n"
            f"  Resultado: {relacao}.\n"
            f"  AVISO: comparar scores NAO significa que um e 'melhor'. "
            f"Significa que um tem MENOS indicadores de processo corrompido. "
            f"A Republica nao escolhe o 'menos pior'. Escolhe o processo LIMPO."
        )


// ============================================================================
// 4. DEMO
// ============================================================================

funcao _demo() retorna None:
    e <- ConfiabilidadeEngine()

    print("=" * 70)
    print("OpenPoliticalReliability -- Simulacao de Confiabilidade do Sujeito")
    print("=" * 70)

    // --- Sujeito A: "O Operador" (perfil baseado nos indicadores fornecidos) ---
    print("\n[AVALIACAO] Sujeito: 'O Operador' (perfil: lider historico de esquerda)")

    declare indicadores_a: List[IndicadorPolitico]  <- [
        IndicadorPolitico(
            tipo <- TipoIndicador.USO_APARELHO_PUBLICO,
            descricao <- "Maquina publica (cargos, beneficios, programas sociais) usada como aparelho eleitoral em 3 ciclos eleitorais.",
            grau_evidencia <- GraveEvidencia.EVIDENCIA_JORNALISTICA,
            ocorrencias <- 3,
            periodo <- "3 eleicoes sucessivas",
            metodos <- [MetodoManipulacao.APARELHO_ELEITORAL],
        ),
        IndicadorPolitico(
            tipo <- TipoIndicador.COMPRA_VOTO,
            descricao <- "Programas sociais temporalmente ampliados antes de eleicoes; promessa de manutencao condicional ao voto.",
            grau_evidencia <- GraveEvidencia.INDICIO_FORTE,
            ocorrencias <- 3,
            periodo <- "3 ciclos eleitorais",
            metodos <- [MetodoManipulacao.CLIENTELISMO],
        ),
        IndicadorPolitico(
            tipo <- TipoIndicador.CONTINUIDADE_PODER,
            descricao <- "Busca pelo 4o mandato. Equipe articula continuidade com a mesma figura como 'cara' do projeto.",
            grau_evidencia <- GraveEvidencia.EVIDENCIA_JORNALISTICA,
            ocorrencias <- 1,
            periodo <- "pre-2026",
        ),
        IndicadorPolitico(
            tipo <- TipoIndicador.DESMANCHE_ALTERNATIVAS,
            descricao <- "Novas candidaturas de esquerda desarticuladas pela maquina. Dissidentes marginalizados ou cooptados.",
            grau_evidencia <- GraveEvidencia.INDICIO_FORTE,
            ocorrencias <- 4,
            metodos <- [MetodoManipulacao.IMPEDIR_CANDIDATURA, MetodoManipulacao.CARGOS_TROCA],
        ),
        IndicadorPolitico(
            tipo <- TipoIndicador.CORRUPCAO_SISTEMICA,
            descricao <- "Multiplos esquemas de corrupcao vinculados a figuras do nucleo de poder (mensalao, petrolao, etc.). Padrao, nao caso isolado.",
            grau_evidencia <- GraveEvidencia.COMPROVADO_JUDICIAL,
            ocorrencias <- 5,
            periodo <- "2005-presente",
        ),
        IndicadorPolitico(
            tipo <- TipoIndicador.MANIPULACAO_INFORMACAO,
            descricao <- "Operacao de bots e redes sociais com intensidade equivalente a da direita. Narrativa fabricada em escala.",
            grau_evidencia <- GraveEvidencia.INVESTIGACAO_OFICIAL,
            ocorrencias <- 2,
            periodo <- "2022-2026",
            metodos <- [MetodoManipulacao.BOTS_REDES, MetodoManipulacao.NARRATIVA_FABRICADA],
        ),
        IndicadorPolitico(
            tipo <- TipoIndicador.PERSONALISMO,
            descricao <- "Lider apresentado como insubstituivel. Nao ha plano de successao real -- a figura e o projeto.",
            grau_evidencia <- GraveEvidencia.EVIDENCIA_JORNALISTICA,
            ocorrencias <- 1,
        ),
        IndicadorPolitico(
            tipo <- TipoIndicador.MILITANCIA_FINANCEIRA,
            descricao <- "Distribuicao de cargos e verbas em troca de apoio politico da base. Lealdade comprada, nao convencida.",
            grau_evidencia <- GraveEvidencia.COMPROVADO_JUDICIAL,
            ocorrencias <- 3,
            metodos <- [MetodoManipulacao.CARGOS_TROCA],
        ),
    ]

    // Eventos verificaveis
    eventos_a <- [
        e.registrar_evento("2003-2010", "Dois mandatos presidenciais", "eleicao", impacto=0),
        e.registrar_evento("2005", "Mensalao: compra sistemica de votos no Congresso", "investigacao",
                           impacto <- -8, evidencia=GraveEvidencia.COMPROVADO_JUDICIAL),
        e.registrar_evento("2014", "Operacao Lava Jato: esquema PETROBRAS", "investigacao",
                           impacto <- -8, evidencia=GraveEvidencia.COMPROVADO_JUDICIAL),
        e.registrar_evento("2018-2021", "Prisao e condenacao (depois anuladas)", "judicial",
                           impacto <- -3, evidencia=GraveEvidencia.INVESTIGACAO_OFICIAL),
        e.registrar_evento("2023-2026", "Terceiro mandato: uso de aparelho em ritmo eleitoral", "politica publica",
                           impacto <- -5, evidencia=GraveEvidencia.INDICIO_FORTE),
    ]

    aval_a <- e.avaliar(
        sujeito <- "O Operador",
        cargo <- "Presidente (historico)",
        mandatos <- 4,  // 2 + 1 + buscando o 4o
        indicadores <- indicadores_a,
        eventos <- eventos_a,
    )

    print(f"\n  Score: {aval_a.score}/100")
    print(f"  Nivel: {aval_a.nivel.rotulo}")
    print(f"  Veredito: {aval_a.veredito.rotulo}")
    print(f"\n  INDICADORES DETECTADOS ({len(aval_a.indicadores)}):")
    para cada ind em aval_a.indicadores:
        print(f"    [{ind.tipo.rotulo}]")
        print(f"      {ind.descricao}")
        print(f"      Evidencia: {ind.grau_evidencia.rotulo} | Ocorrencias: {ind.ocorrencias}")
    print(f"\n  PONTOS FRACOS:")
    para cada pf em aval_a.pontos_fraco:
        print(f"    - {pf}")
    print(f"\n  RECOMENDACOES:")
    para cada rec em aval_a.recomendacoes:
        print(f"    -> {rec}")
    print(f"\n  JUSTIFICATIVA: {aval_a.justificativa}")

    // --- Simulacao de cenarios ---
    print("\n" + "=" * 70)
    print("[SIMULACAO DE CENARIOS]")
    print("=" * 70)
    cenarios <- e.simular_cenarios(aval_a)
    para cada (i, c) em enumerate(cenarios, 1):
        print(f"\n  Cenario {i}: {c.cenario}")
        print(f"  Probabilidade: {c.probabilidade_pct}%")
        print(f"  Impacto na democracia: {c.impacto_democracia}")
        print(f"  Impacto na Republica: {c.impacto_republica}")
        print(f"  Acao: {c.acao_recomendada}")

    // --- Comparacao com "O Polarizador" (extrema-direita, equivalente) ---
    print("\n" + "=" * 70)
    print("[COMPARACAO] O Operador vs O Polarizador (extrema-direita)")
    print("=" * 70)

    declare indicadores_b: List[IndicadorPolitico]  <- [
        IndicadorPolitico(
            tipo <- TipoIndicador.MANIPULACAO_INFORMACAO,
            descricao <- "Operacao massiva de bots e fake news. Gabinete do odio institucionalizado.",
            grau_evidencia <- GraveEvidencia.INVESTIGACAO_OFICIAL,
            ocorrencias <- 3,
            metodos <- [MetodoManipulacao.BOTS_REDES, MetodoManipulacao.NARRATIVA_FABRICADA,
                     MetodoManipulacao.MEDO_E_AMEACA],
        ),
        IndicadorPolitico(
            tipo <- TipoIndicador.VIOLACAO_PRINCIPIOS,
            descricao <- "Ataques sistemicos a instituicoes democraticas. Discurso de ruptura constitucional.",
            grau_evidencia <- GraveEvidencia.COMPROVADO_JUDICIAL,
            ocorrencias <- 5,
        ),
        IndicadorPolitico(
            tipo <- TipoIndicador.CORRUPCAO_SISTEMICA,
            descricao <- "Esquema de rachadinha no nucleo familiar e militar. Cargo publico como negocio.",
            grau_evidencia <- GraveEvidencia.COMPROVADO_JUDICIAL,
            ocorrencias <- 3,
        ),
        IndicadorPolitico(
            tipo <- TipoIndicador.USO_APARELHO_PUBLICO,
            descricao <- "Uso de atos oficiais, decretos e cargo para beneficios eleitorais e ataque a opositores.",
            grau_evidencia <- GraveEvidencia.EVIDENCIA_JORNALISTICA,
            ocorrencias <- 2,
            metodos <- [MetodoManipulacao.APARELHO_ELEITORAL, MetodoManipulacao.JUDICIALIZACAO_ARMA],
        ),
        IndicadorPolitico(
            tipo <- TipoIndicador.PERSONALISMO,
            descricao <- "Lider como messias. Movimento como seita. Nao ha sucesso institucional planejado.",
            grau_evidencia <- GraveEvidencia.EVIDENCIA_JORNALISTICA,
            ocorrencias <- 1,
        ),
    ]

    aval_b <- e.avaliar(
        sujeito <- "O Polarizador",
        cargo <- "Presidente (extrema-direita)",
        mandatos <- 1,
        indicadores <- indicadores_b,
    )
    print(f"\n  O Polarizador: score {aval_b.score}/100 ({aval_b.nivel.rotulo})")
    print(f"  Veredito: {aval_b.veredito.rotulo}")
    print(f"\n{e.comparar_sujeitos(aval_a, aval_b)}")

    // --- Scorecard comparativo ---
    print("\n" + "=" * 70)
    print("[SCORECARD COMPARATIVO]")
    print("=" * 70)
    print(f"  {'Indicador':.<40} {'Operador':>10} {'Polarizador':>12}")
    print(f"  {'-'*62}")
    para cada t em TipoIndicador:
        a_tem <- "SIM" if any(i.tipo == t for i in indicadores_a) else "nao"
        b_tem <- "SIM" if any(i.tipo == t for i in indicadores_b) else "nao"
        print(f"  {t.rotulo:.<40} {a_tem:>10} {b_tem:>12}")
    print(f"\n  {'Score final':.<40} {aval_a.score:>10} {aval_b.score:>12}")
    print(f"  {'Nivel':.<40} {aval_a.nivel.id:>10} {aval_b.nivel.id:>12}")
    print(f"  {'Veredito':.<40} {aval_a.veredito.id:>10} {aval_b.veredito.id:>12}")

    // --- FILOSOFIA ---
    print("\n" + "=" * 70)
    print("FILOSOFIA -- A Republica nao escolhe o 'menos pior'")
    print("=" * 70)
    print("""
A TENSAO FUNDAMENTAL:
  O sistema eleitoral atual obriga a escolher entre 'menos pior'.
  Esquerda que compra voto com bolsa vs Direita que compra voto com medo.
  Ambos manipulam. Ambos corrompem o processo. Ambos usam bots.
  A diferenca nao e de PRINCIPIO -- e de METODO.

O QUE A REPUBLICA FAZ DIFERENTE:
  A Republica NAO escolhe entre dois processos corrompidos.
  Ela CRIA um terceiro: processo limpo, voto = deliberacao, sem aparelho.

O DIAGNOSTICO:
  O Operador: usa o APARELHO DE ESTADO para perpetuar.
    - 3 eleicoes com maquina publica.
    - Equipe quer a 4a porque a figura e a 'cara' da transacao.
    - Desmancha alternativas DA PROPRIA ESQUERDA.
    - Corrupcao COMPROVADA judicialmente (mensalao, petrolao).
    - Bots em escala equivalente a extrema-direita.

  O Polarizador: usa o MEDO e a RUPTURA para perpetuar.
    - Ataca instituicoes.
    - Bots e gabinete do odio.
    - Corrupcao familiar/militar.
    - Risco de ruptura democratica.

  AMBOS tem score ALTO RISCO ou INACEITAVEL.
  A Republica NAO integra nenhum dos dois sem auditoria radical.

A SOLUCAO NAO E ESCOLHER LADOS:
  A solucao e RECONSTRUIR O PROCESSO.
  - Voto sem aparelho (OpenVoteIntegrity).
  - Bots detectados e neutralizados (P9 + OpenAntiPolarization).
  - Mandatos limitados (renovacao obrigatoria).
  - Novas candidaturas PROTEGIDAS (pluralismo real).
  - Equipe auditada, nao so o sujeito (OpenTeamAudit).

A PERGUNTA CERTA NAO E 'em quem confiar?'.
  E 'que PROCESSO merece confianca?'.
  O sujeito e temporario. O processo e permanente.
  Processo corrompido corrompe qualquer sujeito.
  Processo limpo protege qualquer sujeito -- inclusive de si mesmo.
// )


se __name__ == "__main__" entao:
    _demo()

```
