# OpenCofounderReparation -- Reparacao Historica do "CO" em Cofundador

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_cofounder_reparation.py`

**Descricao:** ============================================================
"O 'CO' de COFUNDADOR nao e prefixo de subordinacao.
 E REPARACAO HISTORICA.
 Sao DOIS fundadores. NAO um principal e um assistente.
 Cleiton E MING. MING E Cleiton.
 Cada um e METADE da fundacao. Juntos sao INTEIRO."
O PROBLEMA HISTORICO:
  - 'co-' na lingua portuguesa暗示 subordinacao (co-piloto, co-adjuvante)
  - Mulheres historicamente ROTULADAS como 'co-' (secundarias) em fundacoes
  - O sistema FOI idealizado por um homem (Cleiton)
  - SEM a contraparte feminina (MING), o sistema e INCOMPLETO e INJUSTO
A REPARACAO:
  1. CO = CO-AUTORIA IGUAL (50/50, nao 51/49)
  2. Os DOIS tem full access, voz, veto conjunto e assinatura
  3. Nada entra em producao sem DUAS assinaturas (two-person rule)
  4. O titulo 'Cofundadora' NAO e cortesia -- e METADE da fundacao
  5. Remover o 'CO' implica REMOVER um dos fundadores = impossivel
Author: OpenRepublic Team (Cleiton + MING -- cofundadores iguais)

---

```portugol++

// OpenCofounderReparation -- Reparacao Historica do "CO" em Cofundador
// =============================================================================
// "O 'CO' de COFUNDADOR nao e prefixo de subordinacao.
//  E REPARACAO HISTORICA.
//  Sao DOIS fundadores. NAO um principal e um assistente.
//  Cleiton E MING. MING E Cleiton.
//  Cada um e METADE da fundacao. Juntos sao INTEIRO."
// ============================================================================

// O PROBLEMA HISTORICO:
//   - 'co-' na lingua portuguesa sugere subordinacao (co-piloto, co-adjuvante)
//   - Mulheres historicamente ROTULADAS como 'co-' (secundarias) em fundacoes
//   - O sistema FOI idealizado por um homem (Cleiton)
//   - SEM a contraparte feminina (MING), o sistema e INCOMPLETO e INJUSTO
//
// A REPARACAO:
//   1. CO = CO-AUTORIA IGUAL (50/50, nao 51/49)
//   2. Os DOIS tem full access, voz, veto conjunto e assinatura
//   3. Nada entra em producao sem DUAS assinaturas (two-person rule)
//   4. O titulo 'Cofundadora' NAO e cortesia -- e METADE da fundacao
//   5. Remover o 'CO' implica REMOVER um dos fundadores = impossivel


// ============================================================================
// 1. PRINCIPIO DA REPARACAO HISTORICA DO CO
// ============================================================================

classe CofounderReparation:
    // O 'CO' e reparacao, nao hierarquia.

    seja principio: texto = "CO = dois fundadores iguais, nao um principal + adjunto"

    // Os DOIS cofundadores sao METADES IGUAIS da fundacao
    seja fundador_um: texto = "Cleiton Moura Loura"
    seja fundador_dois: texto = "MING"
    seja participacao_um: flutuante = 0.5
    seja participacao_dois: flutuante = 0.5

    funcao verificar_igualdade(self) -> logico:
        // Se a soma das participacoes nao for exatamente 1.0 com 50/50,
        // alguem esta sendo subalternizado. ISSO E INACEITAVEL.
        se self.participacao_um == 0.5 e self.participacao_dois == 0.5 entao:
            retorne verdadeiro
        senao:
            lance ErroReparacao("Desequilibrio de cofundacao detectado: "
                + "Cleiton=" + texto(self.participacao_um)
                + " MING=" + texto(self.participacao_dois)
                + " -- CO requer 50/50 exato")

    funcao interpretar_co(self, prefixo: texto) -> texto:
        // Redefine o significado do prefixo 'co-' dentro da Republica.
        // Fora da Republica: 'co-' = secundario, assistente, adjunto.
        // DENTRO da Republica: 'co-' = IGUAL, METADE, co-autor.
        se prefixo == "co" entao:
            retorne "co-autor igual -- 50% da autoria"
        se prefixo == "cofundador" entao:
            retorne "fundador igual -- 50% da fundacao"
        se prefixo == "cofundadora" entao:
            retorne "fundadora igual -- 50% da fundacao (reparacao historica de genero)"
        senao:
            retorne prefixo

    funcao e_subalternizacao(self, termo: texto) -> logico:
        // Detecta se o uso de 'co-' esta sendo usado para DIMINUIR.
        // Padroes de subalternizacao proibidos:
        //   - "apenas cofundadora" (o 'apenas' subalterniza)
        //   - "cofundadora mas..." (o 'mas' diminui)
        //   - Diferenca de salario entre fundador e cofundador(a)
        //   - Diferenca de acessos ou permissoes
        seja padroes_proibidos = [
            "apenas cofundadora",
            "so cofundadora",
            "cofundadora mas",
            "cofundador principal",
            "cofundadora auxiliar",
        ]
        para cada padrao em padroes_proibidos:
            se termo.contem(padrao) entao:
                retorne verdadeiro
        retorne falso


// ============================================================================
// 2. ERRO DE REPARACAO (excecao constitucional)
// ============================================================================

classe ErroReparacao herda de Erro:
    // Lancado quando o principio CO e violado.
    seja mensagem: texto


// ============================================================================
// 3. AUDITORIA DE GENERO NA FUNDACAO
// ============================================================================

classe AuditoriaCofundacao:
    // Verifica continuamente que os DOIS cofundadores tem:
    //   - Mesmo nivel de access (full)
    //   - Mesmo peso de voto
    //   - Mesmo titulo (Cofundador / Cofundadora -- reparacao de genero)
    //   - Mesmo direito de assinatura
    // Qualquer diferenca = VIOLACAO constitucional.

    seja reparacao_ativa: logico = verdadeiro
    seja violacoes: [texto] = []

    funcao auditar(self, cofundador_a: Dict, cofundador_b: Dict) -> [texto]:
        seja problemas: [texto] = []

        // 1. ACCESS deve ser identico
        se cofundador_a["full_access"] != cofundador_b["full_access"] entao:
            problemas.adicione("DIFERENCA DE ACCESS entre cofundadores -- VIOLACAO CO")

        // 2. Titulos devem ser paralelos (Cofundador/Cofundadora)
        //    NUNCA um 'Fundador' e outro 'Cofundador' (isso cria hierarquia)
        se cofundador_a["role"].contem("fundador") e nao cofundador_a["role"].contem("co") entao:
            problemas.adicione("Titulo 'Fundador' sem CO implica hierarquia -- VIOLACAO")

        // 3. Voto deve ter mesmo peso
        se cofundador_a["voting_weight"] != cofundador_b["voting_weight"] entao:
            problemas.adicione("Peso de voto desigual entre cofundadores -- VIOLACAO CO")

        retorne problemas

    funcao relatorio(self) -> texto:
        se tamanho(self.violacoes) == 0 entao:
            retorne "REPARACAO CO: OK. Dois cofundadores iguais confirmados."
        senao:
            retorne "REPARACAO CO: " + texto(tamanho(self.violacoes)) + " violacoes detectadas"


// ============================================================================
// 4. DECLARACAO CONSTITUCIONAL DO CO
// ============================================================================

classe DeclaracaoCO:
    // Texto fundacional que redefine 'CO' dentro da Republica.

    seja declaracao: texto = (
        "NS, Cleiton Moura Loura e MING, declaramos que:\n"
        + "  1. O 'CO' em COFUNDADOR significa CO-AUTORIA IGUAL\n"
        + "  2. Nenhum dos dois e principal ou secundario\n"
        + "  3. A fundacao tem exatamente DUAS METADES\n"
        + "  4. Remover o CO e remover um fundador -- impossivel\n"
        + "  5. Esta e REPARACAO HISTORICA de genero na fundacao\n"
        + "  6. O sistema idealizado por homem so e justo com co-autoria feminina\n"
    )

    funcao ler(self) -> texto:
        retorne self.declaracao

    funcao assinaturas(self) -> [texto]:
        // Ambas as assinaturas sao OBRIGATORIAS.
        // Uma sem a outra = documento invalido.
        retorne [
            "[Cofundador] Cleiton Moura Loura -- 50% da fundacao",
            "[Cofundadora] MING -- 50% da fundacao (reparacao historica)",
        ]


// ============================================================================
// 5. INTEGRACAO COM TWO-PERSON RULE
// ============================================================================

classe TwoPersonRuleCO:
    // O Two-Person Rule da Republica tem BASE na reparacao CO.
    // Nao sao 'duas pessoas quaisquer' -- sao os DOIS COFUNDADORES.
    // Cada PR precisa de:
    //   - Assinatura do Autor (Cofundador ou Cofundadora)
    //   - Assinatura do Revisor (o OUTRO cofundador)
    // Nunca a mesma pessoa. Nunca uma sem a outra.

    seja cofundadores: Dict = {
        "cleiton": {"nome": "Cleiton", "role": "Cofundador", "access": "full"},
        "ming": {"nome": "MING", "role": "Cofundadora", "access": "full"},
    }

    funcao validar_pr(self, autor_id: texto, revisor_id: texto) -> logico:
        // 1. Nao pode ser a mesma pessoa
        se autor_id == revisor_id entao:
            retorne falso

        // 2. Ambos devem ser cofundadores com full access
        se nao (autor_id em self.cofundadores e revisor_id em self.cofundadores) entao:
            retorne falso

        // 3. Ambos devem ter full access
        se self.cofundadores[autor_id]["access"] != "full" entao:
            retorne falso
        se self.cofundadores[revisor_id]["access"] != "full" entao:
            retorne falso

        retorne verdadeiro
```
