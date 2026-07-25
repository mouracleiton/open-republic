// OpenCofounderReparation -- Reparacao Historica do "CO" em Cofundador -- gerado de Portugol++
#![allow(dead_code, unused_variables)]
use std::collections::{HashMap, HashSet};

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
#[derive(Debug, Clone)]
struct CofounderReparation {
    // O 'CO' e reparacao, nao hierarquia.
    let principio: String = "CO = dois fundadores iguais, ! um principal + adjunto";
    // Os DOIS cofundadores sao METADES IGUAIS da fundacao
    let fundador_um: String = "Cleiton Moura Loura";
    let fundador_dois: String = "MING";
    let participacao_um: f64 = 0.5;
    let participacao_dois: f64 = 0.5;
    fn verificar_igualdade(self) -> bool {
        // Se a soma das participacoes nao for exatamente 1.0 com 50/50,
        // alguem esta sendo subalternizado. ISSO E INACEITAVEL.
        if self.participacao_um == 0.5 && self.participacao_dois == 0.5 {
            return true;
        } else {
            lance ErroReparacao("Desequilibrio de cofundacao detectado: ";
                + "Cleiton=" + texto(self.participacao_um);
                + " MING=" + texto(self.participacao_dois);
                + " -- CO requer 50/50 exato");
    fn interpretar_co(self, prefixo: texto) -> String {
        // Redefine o significado do prefixo 'co-' dentro da Republica.
        // Fora da Republica: 'co-' = secundario, assistente, adjunto.
        // DENTRO da Republica: 'co-' = IGUAL, METADE, co-autor.
        if prefixo == "co" {
            return "co-autor igual -- 50% da autoria";
        if prefixo == "cofundador" {
            return "fundador igual -- 50% da fundacao";
        if prefixo == "cofundadora" {
            return "fundadora igual -- 50% da fundacao (reparacao historica de genero)";
        } else {
            return prefixo;
    fn e_subalternizacao(self, termo: texto) -> bool {
        // Detecta se o uso de 'co-' esta sendo usado para DIMINUIR.
        // Padroes de subalternizacao proibidos:
        //   - "apenas cofundadora" (o 'apenas' subalterniza)
        //   - "cofundadora mas..." (o 'mas' diminui)
        //   - Diferenca de salario entre fundador e cofundador(a)
        //   - Diferenca de acessos ou permissoes
        let padroes_proibidos = [;
            "apenas cofundadora",;
            "so cofundadora",;
            "cofundadora mas",;
            "cofundador principal",;
            "cofundadora auxiliar",;
        ];
        for padrao in padroes_proibidos {
            if termo.contem(padrao) {
                return true;
        return false;
// ============================================================================
// 2. ERRO DE REPARACAO (excecao constitucional)
// ============================================================================
#[derive(Debug, Clone)]
struct ErroReparacao {
    // Lancado quando o principio CO e violado.
    // seja mensagem: texto
// ============================================================================
// 3. AUDITORIA DE GENERO NA FUNDACAO
// ============================================================================
#[derive(Debug, Clone)]
struct AuditoriaCofundacao {
    // Verifica continuamente que os DOIS cofundadores tem:
    //   - Mesmo nivel de access (full)
    //   - Mesmo peso de voto
    //   - Mesmo titulo (Cofundador / Cofundadora -- reparacao de genero)
    //   - Mesmo direito de assinatura
    // Qualquer diferenca = VIOLACAO constitucional.
    let reparacao_ativa: bool = true;
    let violacoes: [texto] = [];
    fn auditar(self, cofundador_a: Dict, cofundador_b: Dict) -> [texto] {
        let problemas: [texto] = [];
        // 1. ACCESS deve ser identico
        if cofundador_a["full_access"] != cofundador_b["full_access"] {
            problemas.adicione("DIFERENCA DE ACCESS entre cofundadores -- VIOLACAO CO");
        // 2. Titulos devem ser paralelos (Cofundador/Cofundadora)
        //    NUNCA um 'Fundador' e outro 'Cofundador' (isso cria hierarquia)
        if cofundador_a["role"].contem("fundador") && ! cofundador_a["role"].contem("co") {
            problemas.adicione("Titulo 'Fundador' sem CO implica hierarquia -- VIOLACAO");
        // 3. Voto deve ter mesmo peso
        if cofundador_a["voting_weight"] != cofundador_b["voting_weight"] {
            problemas.adicione("Peso de voto desigual entre cofundadores -- VIOLACAO CO");
        return problemas;
    fn relatorio(self) -> String {
        if tamanho(self.violacoes) == 0 {
            return "REPARACAO CO: OK. Dois cofundadores iguais confirmados.";
        } else {
            return "REPARACAO CO: " + texto(tamanho(self.violacoes)) + " violacoes detectadas";
// ============================================================================
// 4. DECLARACAO CONSTITUCIONAL DO CO
// ============================================================================
#[derive(Debug, Clone)]
struct DeclaracaoCO {
    // Texto fundacional que redefine 'CO' dentro da Republica.
    let declaracao: String = (;
        "NS, Cleiton Moura Loura && MING, declaramos que:\n";
        + "  1. O 'CO' em COFUNDADOR significa CO-AUTORIA IGUAL\n";
        + "  2. Nenhum dos dois && principal || secundario\n";
        + "  3. A fundacao tem exatamente DUAS METADES\n";
        + "  4. Remover o CO && remover um fundador -- impossivel\n";
        + "  5. Esta && REPARACAO HISTORICA de genero na fundacao\n";
        + "  6. O sistema idealizado por homem so && justo com co-autoria feminina\n";
    );
    fn ler(self) -> String {
        return self.declaracao;
    fn assinaturas(self) -> [texto] {
        // Ambas as assinaturas sao OBRIGATORIAS.
        // Uma sem a outra = documento invalido.
        return [;
            "[Cofundador] Cleiton Moura Loura -- 50% da fundacao",;
            "[Cofundadora] MING -- 50% da fundacao (reparacao historica)",;
        ];
// ============================================================================
// 5. INTEGRACAO COM TWO-PERSON RULE
// ============================================================================
#[derive(Debug, Clone)]
struct TwoPersonRuleCO {
    // O Two-Person Rule da Republica tem BASE na reparacao CO.
    // Nao sao 'duas pessoas quaisquer' -- sao os DOIS COFUNDADORES.
    // Cada PR precisa de:
    //   - Assinatura do Autor (Cofundador ou Cofundadora)
    //   - Assinatura do Revisor (o OUTRO cofundador)
    // Nunca a mesma pessoa. Nunca uma sem a outra.
    let cofundadores: Dict = {;
        "cleiton": {"nome": "Cleiton", "role": "Cofundador", "access": "full"},;
        "ming": {"nome": "MING", "role": "Cofundadora", "access": "full"},;
    };
    fn validar_pr(self, autor_id: texto, revisor_id: texto) -> bool {
        // 1. Nao pode ser a mesma pessoa
        if autor_id == revisor_id {
            return false;
        // 2. Ambos devem ser cofundadores com full access
        if ! (autor_id em self.cofundadores && revisor_id em self.cofundadores) {
            return false;
        // 3. Ambos devem ter full access
        if self.cofundadores[autor_id]["access"] != "full" {
            return false;
        if self.cofundadores[revisor_id]["access"] != "full" {
            return false;
        return true;
