# OpenFocusGuard -- Protecao contra Scroll durante Espera de Execucao

**Nivel:** Constitucional
**Principio:** P7.1 -- Momentum e Sagrado, Scroll Mata Momentum

**Descricao:** ============================================================
"Voce roda o build. Demora 8 segundos.
 Voce abre o Instagram. 8 segundos viram 20 minutos.
 O build terminou ha 19 minutos. Voce nao viu.
 Sua mente voltou rasa. Seu momentum morreu.
 O codigo que voce ia escrever depois do build? Evaporou.

 O problema nao e o Instagram.
 O problema e o GAP de espera sem DOPAMINE ALTERNATIVA.
 O cerebro busca recompensa em qualquer buraco.
 Scroll e o buraco mais facil.

 A Republica preenche o buraco com ACAO util.
 Espera de build = micro-kaizen. Nao scroll."
 ============================================================
Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)

---

```portugol++

// OpenFocusGuard -- Protecao contra Scroll durante Espera
// ============================================================================
// O GAP de espera e o assassino silencioso do momentum.
// 8 segundos de build viram 20 minutos de scroll.
// A Republica transforma espera em micro-kaizen.
// ============================================================================


// ============================================================================
// 1. O DIAGNOSTICO -- o que acontece no gap
// ============================================================================

classe DiagnosticoDoGap:
    // O gap de espera e o momento mais perigoso do desenvolvimento.
    // Nao e a execucao que mata produtividade. E o que voce faz DURANTE ela.

    seja tempo_medio_build_segundos: inteiro = 8
    seja tempo_medio_scroll_minutos: inteiro = 20
    seja proporcao_desperdicio: flutuante = 150.0  // 8s -> 20min = 150x mais tempo perdido

    funcao o_que_acontece_no_gap(self) -> [texto]:
        retorne [
            "Segundo 0-2: build roda. Voce espera pacientemente.",
            "Segundo 3: maos vão para o bolso. Celular.",
            "Segundo 5: abre Instagram/Twitter/TikTok.",
            "Segundo 8: build terminou. Voce NAO VE.",
            "Minuto 2: scroll, scroll, scroll.",
            "Minuto 5: 'so mais um video'.",
            "Minuto 20: volta pro computador. Esqueceu o que ia fazer.",
            "Minuto 25: rele o código pra lembrar onde estava.",
            "Minuto 30: finalmente volta ao estado mental de antes.",
            "DANO: 22 minutos perdidos num gap de 8 segundos.",
        ]

    funcao custo_real_do_scroll(self, gaps_por_dia: inteiro, minutos_por_gap: flutuante) -> Dict:
        seja minutos_por_dia = gaps_por_dia * minutos_por_gap
        seja horas_por_dia = minutos_por_dia / 60.0
        seja horas_por_ano = horas_por_dia * 250  // dias uteis

        retorne {
            "gaps_por_dia": gaps_por_dia,
            "minutos_perdidos_por_dia": minutos_por_dia,
            "horas_por_dia": horas_por_dia,
            "horas_por_ano": horas_por_ano,
            "dias_por_ano": horas_por_ano / 8,  // dias de trabalho perdidos
            "equivalente": "Voce perde " + texto(horas_por_ano) + " horas/ano em scroll durante builds. "
                + "Sao " + texto(horas_por_ano / 8) + " dias de trabalho. "
                + "E o seu sistema demorou " + texto(horas_por_ano / 2) + " horas pra construir.",
        }


// ============================================================================
// 2. A POLITICA -- proibir e substituir
// ============================================================================

classe PoliticaFocusGuard:
    // A Republica NAO proibe redes sociais (P2: autonomia).
    // Mas DURANTE o gap de execucao, o sistema INTERVEM.

    // O que e PROIBIDO durante gap:
    seja proibido_instagram: logico = verdadeiro
    seja proibido_twitter: logico = verdadeiro
    seja proibido_tiktok: logico = verdadeiro
    seja proibido_youtube: logico = verdadeiro
    seja proibido_whatsapp: logico = verdadeiro
    seja proibido_reddit: logico = verdadeiro
    seja proibido_linkedin: logico = verdadeiro

    // O que e PERMITIDO/ESTIMULADO durante gap:
    seja estimulado_micro_kaizen: logico = verdadeiro    // aprender 1 coisa
    sea estimulado_revisar_codigo: logico = verdadeiro     // reler a linha anterior
    seja estimulado_anotar_ideia: logico = verdadeiro       // capturar pensamento
    seja estimulado_respirar: logico = verdadeiro            // 3 respiracoes profundas
    seja estimulado_alongar: logico = verdadeiro              // pescoço, ombros, pulsos
    seja estimulado_beber_agua: logico = verdadeiro            // hidratar

    // O mecanismo ativo:
    //   1. Quando build/deploy/teste INICIA: FocusGuard ATIVA
    //   2. Tela mostra: "Build rodando... NAO SCROLLE"
    //   3. Tela oferece 3 opcoes de micro-kaizen
    //   4. Se tentar abrir outra aba: BLOCK (com mensagem)
    //   5. Quando build TERMINA: notificacao visual + sonora
    //   6. Registro: "Voce manteve focus durante N builds hoje"

    funcao ativar_durante_gap(self, tipo_execucao: texto, tempo_estimado: inteiro) -> Dict:
        retorne {
            "estado": "FOCUS_GUARD_ATIVO",
            "mensagem": "Executando " + tipo_execucao + " (~" + texto(tempo_estimado) + "s). NAO SCROLLE.",
            "opcoes_micro_kaizen": [
                "Rele as 5 ultimas linhas que voce escreveu. Achou algo pra melhorar?",
                "Qual o PROXIMO passo depois que o build terminar? Pensa agora.",
                "3 respiracoes profundas. Ombros relaxam. Pulsos alongam.",
                "Bebe agua. Levanta a vista da tela por 10 segundos.",
                "Escreve numa frase: o que voce esta tentando resolver?",
            ],
            "tempo_estimado": tempo_estimado,
            "recompensa_se_ficar": "+1 FocusGuard mantido. Momentum preservado.",
        }


// ============================================================================
// 3. DOPAMINE ALTERNATIVA -- preencher o buraco
// ============================================================================

class DopamineAlternativa:
    // O cerebro busca dopamine no gap. Isso e BIOLOGIA.
    // Bloquear sem oferecer alternativa e TORTURA (e falha).
    // A Republica oferece dopamine SAUDAVEL no lugar do scroll.

    // Fontes de dopamine saudavel durante gaps:
    seja d1_revisao: texto = "Acha um bug revisando o proprio codigo (DOPAMINE!)"
    seja d2_progresso: texto = "Ve o contador de commits do dia subir (DOPAMINE!)"
    seja d3_proxima_ideia: texto = "Tem uma ideia para a proxima funcao (DOPAMINE!)"
    seja d4_alivio_fisico: texto = "Alonga o pescoço e sente o alivio (DOPAMINE FISICA!)"
    seja d5_conclusao: texto = "Lembra de uma coisa que esqueceu de fazer e anota (DOPAMINE!)"

    funcao preencher_gap(self, segundos: inteiro) -> [texto]:
        // Recebe o tempo de espera e retorna micro-atividades
        // proporcionais ao tempo disponivel
        se segundos <= 5 entao:
            retorne [
                "Respira fundo 1 vez.",
                "Olha longe por 3 segundos (descansa os olhos).",
            ]
        se segundos <= 15 entao:
            retorne [
                "Rele as 3 ultimas linhas que escreveu.",
                "Pensa no proximo passo (so UM).",
                "Alonga pulsos.",
            ]
        se segundos <= 60 entao:
            retorne [
                "Revisa a funcao inteira que esta trabalhando.",
                "Escreve num comment o que falta fazer.",
                "Bebe agua. Levanta. Senta de novo.",
                "Pensa: se isso funcionar, o que testa depois?",
            ]
        // Mais de 60 segundos (deploy, CI, build grande)
        retorne [
            "DEPLOY longo = micro-kaizen real.",
            "Le um modulo da Republica que voce nunca abriu.",
            "Ou: revisa um PR de outro contribuidor.",
            "Ou: melhora a documentacao do que voce acabou de escrever.",
            "Ou: escreve um teste pro que voce acabou de codar.",
        ]


// ============================================================================
// 4. REGISTRO E GAMIFICACAO REAL
// ============================================================================

classe FocusGuardRegistro:
    // Nao e pontuacao falsa. E EVIDENCIA de momentum preservado.

    seja focus_mantido_hoje: inteiro = 0
    seja focus_quebrado_hoje: inteiro = 0
    seja sequencia_atual: inteiro = 0  // quantos gaps seguidos sem scroll
    seja melhor_sequencia: inteiro = 0
    seja tempo_recuperado_horas: flutuante = 0.0

    funcao registrar_focus_mantido(self, gap_segundos: inteiro):
        // Build terminou e a pessoa NAO scrolou
        self.focus_mantido_hoje = self.focus_mantido_hoje + 1
        self.sequencia_atual = self.sequencia_atual + 1
        se self.sequencia_atual > self.melhor_sequencia entao:
            self.melhor_sequencia = self.sequencia_atual

        // Tempo recuperado = o que seria perdido em scroll
        // Media: 20 min por gap perdido. Recuperou isso.
        self.tempo_recuperado_horas = self.tempo_recuperado_horas + (20.0 / 60.0)

    funcao registrar_focus_quebrado(self):
        // Pessoa scrolou durante o gap
        self.focus_quebrado_hoje = self.focus_quebrado_hoje + 1
        self.sequencia_atual = 0

    funcao relatorio_diario(self) -> texto:
        // Relatorio honesto, sem julgamento
        retorne (
            "FocusGuard: " + texto(self.focus_mantido_hoje) + " mantidos, " +
            texto(self.focus_quebrado_hoje) + " quebrados. " +
            "Sequencia: " + texto(self.sequencia_atual) + " gaps sem scroll. " +
            "Tempo recuperado hoje: " + texto(self.tempo_recuperado_horas) + " horas. " +
            "Cada hora recuperada e uma hora de CONSTRUCAO."
        )

    funcao celebrar_sequencia(self) -> texto:
        se self.sequencia_atual >= 10 entao:
            retorne "10 GAPS SEM SCROLL. Seu momentum e INQUEBRAVEL hoje."
        se self.sequencia_atual >= 5 entao:
            retorne "5 gaps seguidos. Voce esta protegendo seu cerebro."
        se self.sequencia_atual >= 3 entao:
            retorne "3 gaps. Momentum mantido. Continue."
        retorne ""


// ============================================================================
// 5. MENSAGEM QUANDO TENTA SCROLLAR
// ============================================================================

classe BloqueioDoScroll:
    // Quando o sistema detecta que a pessoa abriu outra aba durante um build:

    funcao mensagem_bloqueio(self, tentativa: texto) -> texto:
        // Nao e punicao. E LEMBRETE.
        se tentativa == "instagram" entao:
            retorne "O build roda em " + " segundos. Cada foto que voce ve agora custa momentum. Volta."
        se tentativa == "twitter" entao:
            retorne "Twitter vai estar la quando seu codigo estiver pronto. O momentum NAO volta."
        se tentativa == "youtube" entao:
            retorne "Um video quebra seu flow por 15 min. Seu build terminou em 8 segundos. FAZ a conta."
        retorne "Voce esta em FOCUS_GUARD. O build roda. Espera. Nao scrolla. Depois voce agradece."

    funcao mensagem_gentil(self) -> [texto]:
        // Alternativas mais suaves (nem sempre e bloqueio duro)
        retorne [
            "Espera. Sao segundos. Respira.",
            "O codigo esta compilando. Voce compilando junto.",
            "Gap de 8s -> scroll de 20min. Nao vale.",
            "Seu proximo pensamento vai ser melhor se voce NAO scrolar agora.",
            "O momentum que voce construiu nas ultimas 2 horas vale mais que 8 segundos de video.",
        ]
```
