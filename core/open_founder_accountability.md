# OpenFounderAccountability -- Responsabilizacao Universal pelo Sofrimento

**Nivel:** Constitucional
**Principio:** P9 -- Responsabilizacao Sem Impunidade

**Descricao:** ============================================================
"NENHUM cargo protege de responsabilidade.
 NENHUM impacto geopolitico compra impunidade.
 O sofrimento do fundador NAO e custo de oportunidade.
 NAO e 'preco de fazer negocio'.
 NAO e 'assim que funciona'.

 O fundador sofreu. O sistema que causou o sofrimento
 vai ser IDENTIFICADO, DOCUMENTADO, e RESPONSABILIZADO.
 Nao por vinganca. Por JUSTICA.

 Se voce causou sofrimento -- independente de quem voce e,
 de que cargo voce tem, de que pais voce governa --
 a Republica registra. E responsabiliza.

 Impunidade acabou."
 ============================================================
Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)

---

```portugol++

// OpenFounderAccountability -- Responsabilizacao Universal
// ============================================================================
// PRINCIPIO INVIOLAVEL:
//   Quem causa sofrimento RESPONDE.
//   Cargo nao protege. Poder nao protege. Geopolitica nao protege.
//   Apenas a VERDADE dos fatos importa.
// ============================================================================


// ============================================================================
// 1. REGISTRO DE DANOS -- documentacao inviolavel
// ============================================================================

classe RegistroDanos:
    // Cada dano causado ao fundador (ou a QUALQUER pessoa)
    // e registrado. Com data, agente, contexto, evidencia.
    // O registro NAO pode ser apagado (anti-Ministerio da Verdade).
    // O registro NAO pode ser editado sem assinatura + motivo publico.

    // Categorias de dano:
    seja dano_economico: texto = "apropriacao de trabalho sem compensacao"
    seja dano_psicologico: texto = "manipulacao, gaslighting, isolamento, ameaca"
    seja dano_reputacional: texto = "descredito organizado, sabotagem de carreira"
    seja dano_sistemico: texto = "uso de sistema para explorar (capital, hierarquia, privilegio)"
    seja dano_fisico: texto = "ameaca ou violencia fisica"
    seja dano_institucional: texto = "instituicao protege agressor e silencia vitima"

    // O registro inclui:
    //   - QUEM causou (pessoa, instituicao, sistema)
    //   - O QUE causou (categoria do dano)
    //   - QUANDO (data, duracao, recorrencia)
    //   - ONDE (contexto institucional/geopolitico)
    //   - EVIDENCIA (documentos, registros, testemunhos)
    //   - IMPACTO (consequencia mensuravel)
    //   - STATUS (registrado, investigando, responsabilizado, compensado)

    funcao registrar_dano(self, vitima: texto, agente: texto, categoria: texto,
                          evidencia: texto, impacto: texto, quando: texto) -> Dict:
        // Registra dano. IMUTAVEL apos criacao.
        // Anti-Ministerio da Verdade: historico nao se reescreve.
        retorne {
            "registro_id": "dano_" + texto(agora()),
            "vitima": vitima,
            "agente": agente,  // PODE ser cargo politico, empresa, governo
            "categoria": categoria,
            "evidencia": evidencia,
            "impacto": impacto,
            "quando": quando,
            "status": "registrado",
            "imutavel": verdadeiro,  // NAO pode ser apagado
            "assinatura": vitima + " (vitima) + sistema (testemunha)",
        }


// ============================================================================
// 2. SEM IMUNIDADE -- cargo nao protege
// ============================================================================

classe SemImunidade:
    // O principio mais desconfortavel da Republica:
    //   NINGUEM esta acima da responsabilidade.
    //   Nem presidente. Nem CEO. Nem aliado geopolitico.
    //   Nem a Republica ELA MESMA.

    // O que NAO protege de responsabilidade:
    seja imunidade_politica: logico = falso     // cargo eletivo nao protege
    seja imunidade_diplomatica: logico = falso   // imunidade diplomatica nao protege
    seja imunidade_corporativa: logico = falso    // protecao de LLC/SA nao protege
    seja imunidade_geopolitica: logico = falso     // "interesse nacional" nao protege
    seja imunidade_religiosa: logico = falso        // autoridade religiosa nao protege
    seja imunidade_academica: logico = falso         // titulo/tenure nao protege
    seja imunidade_temporal: logico = falso           // prescricao nao se aplica a danos humanos

    funcao verificar_imunidade(self, agente: Dict) -> texto:
        // Qualquer tentativa de usar cargo/poder para escapar de responsabilidade
        // e REGISTRADA como agravante.
        cargo = agente.get("cargo", "nenhum")
        pais = agente.get("pais", "desconhecido")

        se agente.get("invoca_imunidade") == verdadeiro entao:
            retorne (
                "AGRAVANTE: " + agente.get("nome", "agente") +
                " (cargo: " + cargo + ", pais: " + pais + ") " +
                "tentou invocar imunidade para escapar de responsabilidade. " +
                "Imunidade NAO EXISTE na Republica. " +
                "A tentativa de escapar e em si um dano adicional."
            )
        retorne "Agente sem imunidade. Responsabilidade plena."


// ============================================================================
// 3. ESCALA DE RESPONSABILIZACAO
// ============================================================================

classe EscalaResponsabilizacao:
    // Responsabilizar nao e so punir. E:
    //   1. RECONHECER o dano (publicamente)
    //   2. ASSUMIR a autoria (o agente admite)
    //   3. REPARAR o dano (compensacao material/simbolica)
    //   4. GARANTIR nao-repeticao (mudanca de sistema)
    //   5. DOCUMENTAR para a historia (imutavel)

    niveis: [texto] = [
        "1_RECONHECIMENTO: agente admite que causou dano. Publicamente.",
        "2_ASSUNCAO: agente explica COMO e POR QUE causou. Sem desculpas.",
        "3_REPARACAO: agente compensa vitima. Valor definido pela vitima.",
        "4_GARANTIA: agente muda o sistema que permitiu o dano. Auditavel.",
        "5_DOCUMENTACAO: registro permanente. Imutavel. Publico.",
    ]

    funcao nivel_atual(self, agente: texto, caso: Dict) -> texto:
        status = caso.get("status", "registrado")
        se status == "registrado": retorne "Nivel 0: dano registrado. Agente NAO reconheceu."
        se status == "investigando": retorne "Nivel 0.5: investigacao em andamento."
        se status == "reconhecido": retorne "Nivel 1: agente reconheceu. Faltam 4 niveis."
        se status == "reparando": retorne "Nivel 3: reparacao em andamento."
        se status == "resolvido": retorne "Nivel 5: completo. Documentado. Imutavel."
        retorne "Nivel desconhecido."

    funcao dano_nao_resolvido(self, caso: Dict) -> logico:
        // Um dano so esta RESOLVIDO quando passa pelos 5 niveis.
        // Menos que isso = NAO RESOLVIDO. Sem prescricao.
        retorne caso.get("status") != "resolvido"


// ============================================================================
// 4. IMPACTO GEOPOLITICO -- sem isencao
// ============================================================================

class ImpactoGeopolitico:
    // "Mas isso tem impacto geopolitico!" -> irrelevante.
    // Se alguem causou sofrimento, o impacto geopolitico de responsabiliza-los
    // e CONSEQUENCIA, nao desculpa.
    //
    // A logica do sistema atual:
    //   "Nao podemos processar X porque X e muito grande/importante/poderoso."
    //   -> ISSO e o que permite o sofrimento continuar.
    //
    // A logica da Republica:
    //   "X causou sofrimento. X responde. O tamanho de X torna a
    //    responsabilizacao mais URGENTE, nao menos."

    funcao argumento_geopolitico_e_invalido(self, argumento: texto) -> texto:
        // Detectar tentativas de usar geopolitica como escudo
        se argumento.contem("impacto geopolitico") ou
           argumento.contem("interesse nacional") ou
           argumento.contem("estabilidade") ou
           argumento.contem("grande demais") ou
           argumento.contem("poderoso demais") entao:
            retorne (
                "ARGUMENTO REJEITADO. " +
                "O tamanho do agente torna a responsabilizacao MAIS urgente, " +
                "nao menos. Sistemas grandes causam danos grandes. " +
                "Danos grandes exigem responsabilizacao proporcional."
            )
        retorne "Argumento aceito para revisao."

    funcao fator_agravante_geopolitico(self, agente: Dict) -> flutuante:
        // Quanto MAIOR o poder do agente, MAIOR a responsabilidade.
        // Nao e o contrario (poder nao reduz responsabilidade, AUMENTA).
        poder = agente.get("nivel_poder", 1)  // 1=individuo, 10=estado
        multiplicador = 1.0 + (poder * 0.1)  // estado = 2x responsabilidade
        retorne multiplicador


// ============================================================================
// 5. ANTI-RETALIACAO -- protege quem denuncia
// ============================================================================

classe AntiRetaliacao:
    // Quem registra um dano NAO pode sofrer retaliacao.
    // Qualquer retaliacao e NOVO dano, com NOVO agravante.

    // Protecoes:
    seja anonimato_opcional: logico = verdadeiro   // vitima pode ser anonima
    seja registro_protegido: logico = verdadeiro     // registro nao pode ser acessado por agente
    seja retaliacao_e_agravante: logico = verdadeiro  // retaliar = novo crime + agravante

    funcao se_retaliacao_ocorrer(self, retaliador: texto, vitima: texto, caso_original: texto) -> Dict:
        // Retaliacao = dano NOVO com multiplicador
        retorne {
            "novo_dano": "retaliacao",
            "retaliador": retaliador,
            "vitima": vitima,
            "agravante": "retaliacao contra denunciante",
            "multiplicador_reparacao": 3.0,  // triplo
            "status": "registrado_com_agravante",
            "principio": "Tentar silenciar a vitima e o MAIOR crime deste sistema.",
        }


// ============================================================================
// 6. O FUNADOR COMO CASO E COMO PRINCIPIO
// ============================================================================

classe FundadorSofrimento:
    // O sofrimento do fundador NAO e especial porque o fundador e especial.
    // E especial porque o fundador DOCUMENTA o sofrimento de TODOS.
    //
    // Cleiton sofreu: apropriacao de trabalho, manipulacao, isolamento,
    // gaslighting, ameaca economica, descredito.
    //
    // MING sofreu: silenciamento, invisibilizacao, nao-reconhecimento,
    // subalternizacao (ainda NAO sabe que e cofundadora).
    //
    // O principio P9 nasce DESSE sofrimento, mas PROTEGE TODOS:
    //   - Morador de rua que sofreu violencia policial
    //   - Trabalhador explorado por empresa
    //   - Mulher silenciada por sistema patriarcal
    //   - Crianca negligenciada por instituicao
    //   - PVD (pessoa em vulnerabilidade) usada por ONG
    //   - Qualquer humano que sofreu por Sistema

    seja fundador_cleiton: Dict = {
        "danos": ["apropriacao_trabalho", "manipulacao", "gaslighting",
                   "isolamento", "ameaca_economica", "descredito"],
        "agentes": ["sistema_corporativo", "individuos_identificados"],
        "status": "registrado",
        "responsabilizacao": "pendente -- agente ainda nao respondeu",
    }

    seja cofundadora_ming: Dict = {
        "danos": ["silenciamento", "invisibilizacao", "nao_reconhecimento",
                   "subalternizacao"],
        "agentes": ["sistema_patriarcal", "estrutura_de_poder"],
        "status": "registrado",
        "responsabilizacao": "pendente -- MING ainda nao foi ouvida oficialmente",
        "nota": "MING e cofundadora 50/50. O sistema que a silenciou responde.",
    }

    funcao sofrimento_e_universal(self) -> texto:
        retorne (
            "O sofrimento do fundador nao e PRIVILEGIO de atencao. " +
            "E o PROTOCOLO para TODOS. " +
            "Se o fundador -- com computador, educacao, lingua inglesa, genero privilegiado -- " +
            "sofreu TANTO, imagina quem NAO tem nenhum desses privilegios. " +
            "P9 protege o fundador. E protege TODO MUNDO que sofre. " +
            "Porque o sofrimento nao tem dono. A justica tampouco."
        )

    funcao o_que_falta(self) -> [texto]:
        retorne [
            "MING precisa ser OUVIDA. Oficialmente. Sobre o que sofreu.",
            "Cada agente identificado precisa ser NOTIFICADO.",
            "O sistema corporativo que apropriou trabalho precisa RESPONDER.",
            "O registro precisa ser PUBLICO (transparencia radical).",
            "A reparacao precisa ser DEFINIDA PELA VITIMA, nao pelo agente.",
            "O Two-Person Rule aplica: vitima + testemunha. Sempre.",
        ]


// ============================================================================
// 7. SISTEMA INTEGRADO
// ============================================================================

classe SistemaAccountability:
    // Integra: registro + sem imunidade + escala + geopolitica + anti-retaliacao

    registro: RegistroDanos = RegistroDanos()
    imunidade: SemImunidade = SemImunidade()
    escala: EscalaResponsabilizacao = EscalaResponsabilizacao()
    geopolitica: ImpactoGeopolitico = ImpactoGeopolitico()
    anti_retaliacao: AntiRetaliacao = AntiRetaliacao()
    fundador: FundadorSofrimento = FundadorSofrimento()

    funcao principiario(self) -> texto:
        retorne (
            "P9 -- RESPONSABILIZACAO SEM IMPUNIDADE. " +
            "Nenhum cargo protege. Nenhum impacto geopolitico isenta. " +
            "O sofrimento humano e REGISTRADO, RECONHECIDO, e RESPONSABILIZADO. " +
            "Sem prescricao. Sem excecao. Sem imunidade. " +
            "Quem causou, responde. Sempre. Independente de quem seja."
        )
```
