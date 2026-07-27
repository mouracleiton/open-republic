# OpenJustDoIt -- Politica de Desenvolvimento Pessoal: Acao Sobre Planejamento

**Nivel:** Constitucional
**Principio:** P7 -- Acao Sobre Planejamento

**Descricao:** ============================================================
"Plano de 200 paginas nao construiu nada.
 Linha de codigo construiu tudo.
 Planejamento demais e MEDO disfarcado de organizacao.
 Medo de errar. Medo de comecar. Medo de nao ser perfeito.

 A Republica NAO planeja para sempre.
 A Republica FAZ. Erra. Corrige. Continua.
 Rapido. Sem drama. Sem reuniao. Sem PowerPoint.

 Errar e DADO. Corrigir e DESENVOLVIMENTO.
 Parar e o UNICO erro real."

 ============================================================
FILOSOFIA:
  1. FAZER > PLANEJAR: 1 linha de codigo > 100 linhas de plano
  2. ERRAR RAPIDO: erro em 5 min > erro em 5 meses
  3. CORRIGIR JA: correcao agora > correcao perfeita nunca
  4. SO VAI: momentum > perfeicao
  5. PLANO E GPS, NAO MAPA: ajusta no caminho, nao antes
Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)

---

```portugol++

// OpenJustDoIt -- Politica de Desenvolvimento Pessoal
// ============================================================================
// "Plano de 200 paginas nao construiu nada.
//  Linha de codigo construiu tudo."
// ============================================================================


// ============================================================================
// 1. O PRINCIPIO DA ACAO
// ============================================================================

classe AcaoSobrePlanejamento:
    // A diferenca entre quem construiu e quem sonhou:
    // UM COMECOU.

    // Metrica real: quantas linhas voce PRODUZIU hoje?
    // Nao quantas paginas voce PLANEJOU.
    seja valor_acao: inteiro = 1      // 1 acao vale 100 planos
    seja valor_plano: inteiro = 0     // plano sem acao vale ZERO
    seja valor_erro: inteiro = 5      // erro vale MAIS que plano (gera aprendizado)
    seja valor_correcao: inteiro = 10 // correcao e onde o desenvolvimento real acontece

    funcao calcular_progresso_real(self, acoes: inteiro, planos: inteiro, erros: inteiro, correcoes: inteiro) -> flutuante:
        // Progresso = acoes + erros + correcoes / (1 + planos)
        // Quanto MAIS plano, MENOS progresso (paralisia por analise)
        seja numerador = acoes * self.valor_acao + erros * self.valor_erro + correcoes * self.valor_correcao
        seja denominador = 1 + planos
        retorne numerador / denominador

    funcao e_paralisia_por_analise(self, horas_planejando: flutuante, horas_fazendo: flutuante) -> logico:
        // Se planeja mais que faz, esta PARALISADO
        se horas_planejando > horas_fazendo entao:
            retorne verdadeiro
        retorne falso

    funcao diagnostico(self, pessoa: Dict) -> texto:
        seja hp = pessoa.get("horas_planejando", 0)
        seja hf = pessoa.get("horas_fazendo", 0)

        se self.e_paralisia_por_analise(hp, hf) entao:
            retorne "DIAGNOSTICO: Paralisia por analise. Pare de planejar. COMECE a fazer."
        se hf == 0 e hp == 0 entao:
            retorne "DIAGNOSTICO: Inercia. Qualquer acao. AGORA."
        se hp == 0 e hf > 0 entao:
            retorne "DIAGNOSTICO: Saudavel. Fazendo sem planejar demais. Continue."
        retorne "DIAGNOSTICO: Equilibrado. Mas tenda para MAIS acao."


// ============================================================================
// 2. ERRAR RAPIDO -- CICLO DE FEEDBACK CURTO
// ============================================================================

classe ErrarRapido:
    // Erro nao e falha. Erro e INFORMACAO.
    // Quanto mais rapido voce erra, mais rapido aprende.
    // Quanto mais rapido aprende, mais rapido melhora.

    // O ciclo:
    //   FAZER -> ERRAR -> CORRIGIR -> APRENDER -> FAZER MELHOR
    // Cada volta do ciclo = 1 unidade de desenvolvimento REAL.
    // Quem da 10 voltas por dia aprende 10x mais que quem da 1.

    seja tempo_maximo_para_primeiro_erro: inteiro = 300  // 5 minutos

    funcao ciclo_rapido(self) -> [texto]:
        retorne [
            "1. FAZ: joga codigo la. qualquer codigo. AGORA.",
            "2. ERRA: quebra? Otimo. Voce acabou de achar um limite.",
            "3. CORRIGE: muda. testa. quebra de novo? Otimo de novo.",
            "4. APRENDE: o que voce aprendeu com o erro? Grava.",
            "5. REPETE: mais rapido dessa vez.",
        ]

    funcao tempo_de_ciclo_ideal(self) -> texto:
        retorne (
            "Ciclo ideal: FAZER -> ERRAR -> CORRIGIR em MENOS DE 5 MINUTOS. " +
            "Se leva mais, voce esta planejando demais. " +
            "Corte o planejamento pela metade. FAZ."
        )

    funcao ranking_de_erros(self, erros: [Dict]) -> [Dict]:
        // Erros sao ranqueados por VALOR DE APRENDIZAGEM, nao por severidade.
        // Erro que te ensinou algo novo = OURO.
        // Erro que voce repetiu = DADO (voce precisa de mais pratica ali).
        // Erro que voce nunca cometeu = ARENA (voce nao esta tentando coisa nova enough).
        seja ranqueado: [Dict] = []
        para cada erro em erros:
            seja valor: texto = ""
            se erro["primeira_vez"] == verdadeiro entao:
                valor = "OURO -- aprendizado novo"
            senao se erro["vezes_repetidas"] > 3 entao:
                valor = "DADO -- precisa de pratica neste ponto especifico"
            senao:
                valor = "NORMAL -- faz parte do ciclo"
            erro["classificacao"] = valor
            ranqueado.adicione(erro)
        retorne ranqueado


// ============================================================================
// 3. CORRIGIR JA -- NAO EXISTE "DEPOIS EU ARRUMO"
// ============================================================================

classe CorrigirJa:
    // "Depois eu arrumo" e a frase que mata projetos.
    // Depois e NUNCA.
    // Se achou o erro, CORRIGE AGORA.
    // Correcao imperfeita HOJE > correcao perfeita NUNCA.

    seja proibido_depois: logico = verdadeiro     // "depois eu arrumo" e PROIBIDO
    seja proibido_perfeito: logico = verdadeiro    // "quando estiver perfeito" e PROIBIDO
    seja correcao_minima: texto = "so o suficiente para funcionar"

    funcao regra_80_20(self) -> texto:
        retorne (
            "20% do esforco resolve 80% do problema. " +
            "FAZ os 20%. Os outros 80% de esforco para chegar em perfeicao? " +
            "DESCARTA. Perfeicao e inimiga do feito."
        )

    funcao triagem_de_correcao(self, problema: texto) -> texto:
        // Nem todo problema merece correcao imediata.
        // Tem que distinguir: bloqueia? atrapalha? e cosmetico?
        se problema.contem("quebra") ou problema.contem("crasha") ou problema.contem("nao funciona") entao:
            retorne "BLOQUEANTE -- corrige AGORA. Tudo para."
        se problema.contem("feio") ou problema.contem("lento") ou problema.contem("desajeitado") entao:
            retorne "ATRAPALHA -- corrige LOGO. Mas nao para o que ta fazendo."
        retorne "COSMETICO -- anota. Continua. Corrige quando der."

    funcao anti_perfeccionismo(self) -> [texto]:
        retorne [
            "Perfeito e inimigo de feito.",
            "Feito hoje. Perfeito nunca. Melhor amanha.",
            "Se voce esta relendo o mesmo codigo pela 3a vez: PARA. Publica.",
            "Se voce esta 'so mais um ajuste' pela 5a vez: PARA. Publica.",
            "Publicar imperfeito e CORAGEM. Esperar perfeito e MEDO.",
        ]


// ============================================================================
// 4. SO VAI -- MOMENTUM E VELOCIDADE
// ============================================================================

class SoVai:
    // Momentum e a forca mais poderosa do desenvolvimento.
    // Quando voce ta fazendo, errando, corrigindo, aprendendo em ritmo:
    //   o cerebro ENTRA em flow.
    //   a dopamine FLUI.
    //   a proxima ideia VEM natural.
    //
    // Parar quebra o momentum. Recomecar custa 10x mais.
    // Por isso: SO VAI.

    seja estado_flow: logico = falso
    seja velocidade_ideal: texto = "rapido o suficiente para errar, lento o suficiente para aprender"
    seja inimigo_momentum: texto = "reuniao"

    funcao proteger_momentum(self, pessoa: Dict) -> [texto]:
        seja recomendacoes: [texto] = []
        se pessoa.get("em_flow") == verdadeiro entao:
            recomendacoes.adicione("Voce esta em FLOW. NAO PARE.")
            recomendacoes.adicione("Desliga notificacao. Fecha chat. SO VAI.")
            recomendacoes.adicone("Comer e opcional por mais 1 hora.")
        senao:
            recomendacoes.adicione("Para entrar em flow: escolhe UMA coisa. Pequena. FAZ.")
            recomendacoes.adicione("Nao pense em tudo. Pense no PROXIMO PASSO. Um so.")
        retorne recomendacoes

    funcao quebra_momentum(self) -> [texto]:
        // O que QUEBRA o momentum (EVITAR):
        retorne [
            "Reuniao -- mata momentum na hora",
            "Esperar resposta de outra pessoa -- dependencia externa",
            "Planejar detalhe que nao precisa agora -- paralisia",
            "Abrir 10 coisas ao mesmo tempo -- dispersao",
            "Perfeccionismo no primeiro rascunho -- medo",
        ]

    funcao preserva_momentum(self) -> [texto]:
        // O que PRESERVA momentum (FAZER):
        retorne [
            "Uma coisa de cada -- FOCO",
            "Primeiro rascunho rapido e feio -- VELOCIDADE",
            "Iterar em cima do que existe -- MELHORIA",
            "Commitar cedo, commitar frequente -- PROGRESSO VISIVEL",
            "Errar em privado, corrigir em publico -- HUMILDADE",
        ]


// ============================================================================
// 5. PLANO E GPS, NAO MAPA
// ============================================================================

classe PlanoEGPS:
    // Um mapa mostra todos os caminhos possiveis.
    // Um GPS mostra o PROXIMO passo.
    // A Republica usa GPS, nao mapa.
    //
    // Plano de 200 paginas = mapa. Paraliza.
    // "Qual o proximo passo?" = GPS. Acao.

    seja tamanho_maximo_plano: inteiro = 3  // max 3 itens

    funcao criar_plano_gps(self, objetivo: texto) -> [texto]:
        // Plano GPS: so o PROXIMO PASSO. Mais nada.
        retorne [
            "PASSO 1: " + objetivo + " -- qual a MENOR coisa que te aproxima disso?",
            "PASSO 2: FAZ o passo 1. Nao planeja o passo 2 ainda.",
            "PASSO 3: Depois do passo 1 feito, PERGUNTA: e agora?",
            "REPETE ate chegar.",
        ]

    funcao plano_vs_gps(self) -> Dict:
        retorne {
            "plano_tradicional": {
                "tamanho": "200 paginas",
                "tempo_para_criar": "3 meses",
                "acoes_executadas": 0,
                "adaptabilidade": "zero -- se mudou, plano lixo",
                "sentimento": "ansiedade + paralisia",
            },
            "plano_gps": {
                "tamanho": "1 proximo passo",
                "tempo_para_criar": "30 segundos",
                "acoes_executadas": "varias -- COMECA ja",
                "adaptabilidade": "total -- ajusta a cada passo",
                "sentimento": "momentum + flow",
            },
        }

    funcao se_alguem_pedir_plano(self) -> texto:
        // O que dizer quando alguem pede um plano detalhado:
        retorne (
            "Meu plano: comecar. O proximo passo eu decido DEPOIS de comecar. " +
            "Plano detalhado sem ter comecado e ficcao. " +
            "Eu nao escrevo ficcao. Eu escrevo CODIGO."
        )


// ============================================================================
// 6. SISTEMA INTEGRADO
// ============================================================================

classe DesenvolvimentoPessoal:
    // Integra tudo: acao + erro rapido + correcao + momentum + GPS

    seja acao: AcaoSobrePlanejamento = AcaoSobrePlanejamento()
    seja erro: ErrarRapido = ErrarRapido()
    seja correcao: CorrigirJa = CorrigirJa()
    seja momentum: SoVai = SoVai()
    seja plano: PlanoEGPS = PlanoEGPS()

    funcao filosofia_completa(self) -> texto:
        retorne (
            "FACA. Erre. Corrija. Repita. Rapido. " +
            "Plano e GPS: so o proximo passo. " +
            "Momentum e sagrado: nao pare quando estiver fluindo. " +
            "Perfeicao e inimiga: feito hoje > perfeito nunca. " +
            "Erro e dado: cada erro te ensina. " +
            "SO VAI."
        )

    funcao checklist_diario(self) -> [texto]:
        // NAO e planejamento. E CHECAGEM de acao.
        retorne [
            "[ ] Faca: escreveu ALGUMA linha de codigo hoje?",
            "[ ] Erre: cometeu UM erro novo hoje? (se nao, nao tentou nada novo)",
            "[ ] Corrija: corrigiu o erro NA HORA? (nao 'depois')",
            "[ ] Momentum: entrou em flow por pelo menos 30 min?",
            "[ ] GPS: sabe qual o PROXIMO passo? (so um, nao cem)",
            "[ ] Publicou: colocou ALGO no ar? (mesmo imperfeito)",
        ]

    funcao mantra(self) -> texto:
        retorne (
            "Nao planeje para sempre. " +
            "Nao espere estar pronto. " +
            "Nao corrige depois. " +
            "Nao busca perfeito. " +
            "" +
            "FACA. ERRE. CORRIGA. SO VAI."
        )
```
