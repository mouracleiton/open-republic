# OpenHumanKnowledge -- Engenharia Reversa de IA com Verificacao Humana

**Nivel:** Constitucional
**Principio:** P8 -- Conhecimento Human-Checked

**Descricao:** ============================================================
"Toda IA erra. Nenhuma IA e fonte de verdade.
 A Republica usa TODAS as IAs como instrumento.
 Manda o mesmo prompt pra todas. Compara.
 Humano verifica. O que passa, entra.

 Nenhuma resposta de IA entra no conhecimento
 sem assinatura humana de verificacao.
 Isso e Two-Person Rule aplicada ao conhecimento:
 a IA escreve, o humano ASSINA.

 O resultado e uma base de conhecimento que:
   1. Nao depende de nenhuma IA unica
   2. Tem cada item verificado por humano
   3. Acumula verdade auditavel, nao alucinacao
   4. Cresce com cada verificacao
   5. Pertence ao PUBLICO, nao a empresa de IA"
 ============================================================
Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)

---

```portugol++

// OpenHumanKnowledge -- Engenharia Reversa de IA
// ============================================================================
// Fluxo:
//   1. PROMPT: humano faz pergunta
//   2. DISPATCH: manda pra TODAS as IAs configuradas
//   3. COMPARE: coloca respostas lado a lado
//   4. DIFF: destaca diferencas e contradicoes
//   5. VERIFY: humano aprova / rejeita / edita
//   6. STORE: verificado entra na base com assinatura
//   7. LEARN: a base cresce e fica mais inteligente
// ============================================================================


// ============================================================================
// 1. CONFIGURACAO DE FONTES DE IA
// ============================================================================

classe FonteIA:
    // Cada fonte de IA e um "consultor" -- nao um oraculo.
    // A Republica consulta varios e decide.

    nome: texto                // "GPT-4", "Claude", "Gemini", "Local"
    endpoint: texto             // URL da API
    api_key: texto              // chave (em variavel de ambiente)
    modelo: texto               // modelo especifico
    peso_confianca: flutuante   // 0.0 a 1.0 -- atualizado por performance
    custo_por_token: flutuante  // custo monetario
    latencia_media: inteiro     // ms de resposta


// ============================================================================
// 2. DISPATCH -- manda pra todos
// ============================================================================

classe MultiDispatch:
    // Manda o MESMO prompt pra todas as IAs configuradas.
    // Recolhe todas as respostas. Sem preferencia.

    fontes: [FonteIA] = []
    respostas: Dict = {}    // fonte -> resposta

    funcao dispatch(self, prompt: texto) -> Dict:
        // Manda pra todos em paralelo
        seja resultados: Dict = {}
        para cada fonte em self.fontes:
            seja resp = self._chamar_ia(fonte, prompt)
            resultados[fonte.nome] = {
                "resposta": resp,
                "tempo_ms": fonte.latencia_media,
                "modelo": fonte.modelo,
                "sucesso": resp != nulo,
            }
        retorne resultados

    funcao _chamar_ia(self, fonte: FonteIA, prompt: texto) -> texto:
        // Chamada real a API (implementado no backend Python)
        // Aqui no PP, representamos a abstracao
        retorne "[resposta da IA " + fonte.nome + "]"

    funcao custo_total(self, tokens: inteiro) -> flutuante:
        seja soma: flutuante = 0.0
        para cada fonte em self.fontes:
            soma = soma + (fonte.custo_por_token * tokens)
        retorne soma


// ============================================================================
// 3. COMPARE -- analisa divergencias
// ============================================================================

classe Comparador:
    // Coloca respostas lado a lado e destaca:
    //   - Onde TODOS concordam (alta confianca)
    //   - Onde HAVER DIVERGENCIA (baixa confianca -- precisa verificacao)
    //   - Onde UMA contradiz todas as outras (potencial alucinacao)

    funcao comparar(self, respostas: Dict) -> Dict:
        seja nomes = listas_de_chaves(respostas)
        seja textos = [respostas[n]["resposta"] para n em nomes]

        seja analise = {
            "concordancia": self._encontrar_concordancia(textos),
            "divergencia": self._encontrar_divergencia(textos),
            "contradicao": self._encontrar_contradicao(textos),
            "score_medio": self._score_consensus(textos),
            "recomendacao": "",
        }

        se analise["score_medio"] > 0.85 entao:
            analise["recomendacao"] = "ALTA CONCORDANCIA. Provavelmente correto. Verificacao rapida."
        senao se analise["score_medio"] > 0.6 entao:
            analise["recomendacao"] = "MEDIA CONCORDANCIA. Rever divergencias."
        senao:
            analise["recomendacao"] = "BAIXA CONCORDANCIA. IAs discordam. Verificacao humana obrigatoria."

        retorne analise

    funcao _encontrar_concordancia(self, textos: [texto]) -> [texto]:
        // Frases/afirmacoes presentes em TODAS as respostas
        retorne ["[pontos em comum entre todas as IAs]"]

    funcao _encontrar_divergencia(self, textos: [texto]) -> [texto]:
        // Frases presentes em ALGUMAS mas nao todas
        retorne ["[pontos onde IAs diferem]"]

    funcao _encontrar_contradicao(self, textos: [texto]) -> [texto]:
        // Uma resposta afirma X, outra afirma NOT X
        retorne ["[contradicoes diretas]"]

    funcao _score_consensus(self, textos: [texto]) -> flutuante:
        // 0.0 = total discordancia, 1.0 = identicas
        // Calculado por similaridade semantica
        retorne 0.75


// ============================================================================
// 4. VERIFY -- verificacao humana
// ============================================================================

classe VerificacaoHumana:
    // O HUMANO e o filtro. Sempre.
    // A IA pode estar certa. Mas e o HUMANO que ASSINA.
    //
    // Three states:
    //   APPROVED: humano confirma que esta correto
    //   EDITED: humano confirma mas corrige/modifica
    //   REJECTED: humano descarta (alucinacao, erro, viés)
    //
    // Toda verificacao fica registrada com:
    //   - Quem verificou (id da pessoa)
    //   - Quando (timestamp)
    //   - Qual IA produziu
    //   - Score de consensus
    //   - Versao final (aprovada ou editada)

    // Two-Person Rule aplicada ao conhecimento:
    //   IA escreve (1a "pessoa")
    //   Humano assina (2a pessoa)
    //   Sem as duas, nao entra na base

    funcao verificar(self, resposta: Dict, verificador_id: texto) -> Dict:
        retorne {
            "resposta_original": resposta,
            "verificador": verificador_id,
            "timestamp": agora(),
            "status": "pending",  // pending -> approved / edited / rejected
            "versao_final": "",
            "score_consensus": resposta.get("score", 0),
            "fonte_preferida": "",  // qual IA o humano escolheu
            "notas": "",
        }

    funcao aprovar(self, verificacao: Dict, versao: texto) -> Dict:
        verificacao["status"] = "approved"
        verificacao["versao_final"] = versao
        verificacao["timestamp_aprovacao"] = agora()
        retorne verificacao

    funcao editar_e_aprovar(self, verificacao: Dict, versao_corrigida: texto, motivo: texto) -> Dict:
        verificacao["status"] = "edited"
        verificacao["versao_final"] = versao_corrigida
        verificacao["notas"] = motivo
        verificacao["timestamp_aprovacao"] = agora()
        retorne verificacao

    funcao rejeitar(self, verificacao: Dict, motivo: texto) -> Dict:
        verificacao["status"] = "rejected"
        verificacao["notas"] = motivo
        verificacao["timestamp_rejeicao"] = agora()
        retorne verificacao


// ============================================================================
// 5. STORE -- base de conhecimento verificado
// ============================================================================

classe BaseConhecimento:
    // Cada item verificado entra na base com PROVENANCE.
    // Provenance = rastreabilidade completa.
    // Voce pode perguntar: "quem verificou isso? quando? qual IA produziu?"
    // E a base RESPONDE.

    // A base cresce com cada verificacao.
    // Cada item APPROVED ou EDITED adiciona conhecimento.
    // Cada item REJECTED melhora o filtro (sabe o que rejeitar).

    registros: [Dict] = []

    funcao armazenar(self, verificacao: Dict) -> texto:
        // Gera ID unico
        seja kid = "kh_" + texto(tamanho(self.registros) + 1)
        verificacao["knowledge_id"] = kid
        self.registros.adicione(verificacao)
        retorne kid

    funcao buscar(self, query: texto) -> [Dict]:
        // Busca na base de conhecimento verificado
        // (usa FTS5 no backend SQLite)
        seja resultados: [Dict] = []
        para cada r em self.registros:
            se r["status"] == "approved" ou r["status"] == "edited" entao:
                se r["versao_final"].contem(query) entao:
                    resultados.adicione(r)
        retorne resultados

    funcao estatisticas(self) -> Dict:
        seja approved = 0
        seja edited = 0
        seja rejected = 0
        para cada r em self.registros:
            se r["status"] == "approved": approved = approved + 1
            se r["status"] == "edited": edited = edited + 1
            se r["status"] == "rejected": rejected = rejected + 1

        retorne {
            "total": tamanho(self.registros),
            "approved": approved,
            "edited": edited,
            "rejected": rejected,
            "taxa_aprovacao": approved + edited / tamanho(self.registros) if tamanho(self.registros) > 0 else 0,
            "conhecimento_util": approved + edited,
        }


// ============================================================================
// 6. LEARN -- a base fica mais inteligente
// ============================================================================

classe AprendizadoBase:
    // A base de conhecimento verificado e usada para:
    //   1. Responder perguntas DIRETAMENTE (sem chamar IA externa)
    //   2. PRÉ-filtrar respostas de IA (se a base ja sabe, nao precisa perguntar)
    //   3. CALIBRAR pesos de confianca das fontes de IA
    //   4. DETECTAR alucinacoes (se IA diz X e base diz Y, alerta)

    funcao responder_da_base(self, query: texto, base: BaseConhecimento) -> Dict:
        // Se a base ja tem resposta verificada, retorna sem chamar IA
        seja resultados = base.buscar(query)
        se tamanho(resultados) > 0 entao:
            retorne {
                "fonte": "base_verificada",
                "resposta": resultados[0]["versao_final"],
                "verificado_por": resultados[0]["verificador"],
                "score": 1.0,  // verificacao humana = confianca maxima
                "custo": 0.0,  // gratis -- ja temos na base
            }
        retorne {"fonte": "nao_encontrado", "resposta": "", "score": 0.0}

    funcao calibrar_pesos(self, base: BaseConhecimento, fontes: [FonteIA]) -> [FonteIA]:
        // Se uma IA foi frequentemente rejeitada, seu peso cai.
        // Se foi frequentemente aprovada, seu peso sobe.
        para cada fonte em fontes:
            sea approved = 0
            sea rejected = 0
            para cada r em base.registros:
                se r.get("fonte_preferida") == fonte.nome:
                    se r["status"] == "approved": approved = approved + 1
                    se r["status"] == "rejected": rejected = rejected + 1

            se approved + rejected > 0:
                fonte.peso_confianca = approved / (approved + rejected)

        retorne fontes

    funcao detectar_alucinacao(self, resposta_ia: texto, base: BaseConhecimento) -> Dict:
        // Compara resposta de IA com base verificada.
        // Se contradiz algo verificado, ALERTA.
        retorne {
            "alucinacao_provavel": falso,
            "contradiz_base": [],
            "recomendacao": "Sem contradicoes com a base verificada.",
        }
```
