// OpenAntiPolarization -- P9: O Estado NAO Polariza
// ====================================================
// O nono principio constitucional da Republica Aberta.
//
// "Discordo de tudo que voce disse, mas darei minha vida para que voce possa
// dizer de novo." -- atribuido a Voltaire, encapsula o espirito deste modulo.
//
// DISTINCAO CRITICA (a tese do modulo):
// - Diversidade de opiniao e DIREITO (P2). E saudavel. E combustivel da democracia.
// - Polarizacao e DOENCA SISTEMICA. Nao e "opiniao diferente". E realidade
//   epistemica separada: duas tribos que nao so discordam, mas habitam mundos
//   de fato diferentes, com zero confianca mutua e identidade fundida na tribo.
//
// A Republica recusa o equivoco liberal de que "mais debate resolve polarizacao".
// Mais debate entre tribos epistemicamente separadas AMPLIFICA a polarizacao.
// O que resolve e: (a) chao de fato compartilhado, (b) deliberacao estruturada,
// (c) Estado que se recusa a ser vetor de divisao identitaria.
//
// ALINHAMENTO CONSTITUCIONAL:
// - P1: Polarizacao recria elite. Sempre ha um lado que se beneficia da divisao.
// - P2: Identidade tribal captura autonomia. Quem so pensa pela tribo nao e livre.
// - P4: Democracia em assembleia polarizada nao e democracia -- e tirania de 51%.
// - P8: IA que amplifica polarizacao (engagement algorithms) VIOLA o principio
//   de ampliar inteligencia humana. Engenagement por furia e anti-P8.
//
// P9 -- ANTI-POLARIZACAO DE ESTADO:
// O Estado nao pode produzir, amplificar ou se beneficiar de divisao identitaria.
// Toda politica publica deve ser avaliada pelo seu POTENCIAL POLARIZANTE antes
// da votacao. E um GATE (como WCAG audita acessibilidade), nao um mod de censura.
//
// Author: OpenRepublic Team
// Versao Go transpilada fielmente do Python (open_anti_polarization.py)

package main

import (
	"fmt"
	"math"
	"strings"
)

// ============================================================================
// 1. ENUMS (modulo-level, nunca aninhados)
// ============================================================================

type FatorPolarizacao int

const (
	FATOR_RELIGIAO FatorPolarizacao = iota
	FATOR_ETNIA
	FATOR_REGIAO
	FATOR_CLASSE
	FATOR_IDEOLOGIA
	FATOR_IDENTIDADE
	FATOR_LINGUA
	FATOR_IDADE
	FATOR_ALGORITMO
	FATOR_CULTURA
)

func (f FatorPolarizacao) ID() string {
	return []string{"religiao","etnia","regiao","classe","ideologia","identidade","lingua","idade","algoritmo","cultura"}[f]
}
func (f FatorPolarizacao) Rotulo() string {
	return []string{
		"Religiao / fe / espiritualidade",
		"Etnia / raca / origem",
		"Regiao / geografia (norte vs sul, urbano vs rural)",
		"Classe / origem economica (heranca do sistema antigo)",
		"Ideologia politica (heranca do sistema partidario)",
		"Identidade de genero / sexual / expressao",
		"Lingua / idioma / dialeto",
		"Geracional (jovens vs velhos)",
		"Algoritmo de feed (captura narrativa externa)",
		"Cultura / costumes / tradicao",
	}[f]
}

type NivelPolarizacao int

const (
	NIVEL_SAUDAVEL NivelPolarizacao = iota
	NIVEL_BAIXO
	NIVEL_MODERADO
	NIVEL_ALTO
	NIVEL_CRITICO
	NIVEL_RUPTURA
)

func (n NivelPolarizacao) ID() string {
	return []string{"saudavel","baixo","moderado","alto","critico","ruptura"}[n]
}
func (n NivelPolarizacao) Rotulo() string {
	return []string{
		"Saudavel: dissenso produtivo, confianca preservada",
		"Baixo: blocos incipientes, ainda deliberam",
		"Moderado: blocos claros, deliberacao degrada",
		"Alto: votacao tribal, confianca em queda",
		"Critico: quase bloqueio assemblear",
		"Ruptura epistemica: realidades de fato separadas",
	}[n]
}
func (n NivelPolarizacao) Gravidade() int { return int(n) }

type TaticaPolarizante int

const (
	TATICA_OUTGROUP_DEHUMANIZATION TaticaPolarizante = iota
	TATICA_FALSE_DICHOTOMY
	TATICA_WHATABOUTISM
	TATICA_FEAR_MONGERING
	TATICA_IDENTITY_BAITING
	TATICA_EPISTEMIC_BALKANIZATION
	TATICA_BOTH_SIDES_FALLACY
	TATICA_STRAWMAN
	TATICA_DOG_WHISTLE
	TATICA_VIRTUE_SIGNALING
)

func (t TaticaPolarizante) ID() string {
	return []string{
		"outgroup_dehumanization","false_dichotomy","whataboutism",
		"fear_mongering","identity_baiting","epistemic_balkanization",
		"both_sides_fallacy","strawman","dog_whistle","virtue_signaling",
	}[t]
}
func (t TaticaPolarizante) Rotulo() string {
	return []string{
		"Desumanizacao do outro lado",
		"Falsa dicotomia (ou nos ou eles)",
		"Whataboutism (desvia com 'mas eles tambem')",
		"Alarmismo / medo fabricado",
		"Isca de identidade (forca tribalismo)",
		"Balkanizacao epistemica (fatos tribais)",
		"Falsa simetria (os dois lados sao iguais)",
		"Espantalho (deturpa para atacar)",
		"Dog whistle (codigo tribal implicito)",
		"Sinalizacao virtuosa (pertence vs exclui)",
	}[t]
}
func (t TaticaPolarizante) Gravidade() int {
	return []int{5,4,3,4,5,5,3,2,4,2}[t]
}

type StatusBloqueio int

const (
	STATUS_NENHUM StatusBloqueio = iota
	STATUS_ALERTA
	STATUS_DELIBERACAO_ESTRUTURADA
	STATUS_MEDIACAO_OBRIGATORIA
	STATUS_SUSPENDER_VOTACAO
	STATUS_ASSEMBLEIA_PAUSA
)

func (s StatusBloqueio) ID() string {
	return []string{"nenhum","alerta","deliberacao_estruturada","mediacao_obrigatoria","suspender_votacao","assembleia_pausa"}[s]
}
func (s StatusBloqueio) Rotulo() string {
	return []string{
		"Nenhum: assembleia delibera normalmente",
		"Alerta: moderador sinaliza polarizacao",
		"Deliberacao estruturada obrigatoria",
		"Mediacao obrigatoria antes de votar",
		"Votacao suspensa (bloqueio ativo)",
		"Pausa assemblear (resfriamento obrigatorio)",
	}[s]
}
func (s StatusBloqueio) Prioridade() int { return int(s) }

type VereditoAuditoria int

const (
	VEREDITO_APROVADA VereditoAuditoria = iota
	VEREDITO_APROVADA_COM_RESSALVAS
	VEREDITO_REJEITADA
	VEREDITO_BLOQUEADA
)

func (v VereditoAuditoria) ID() string {
	return []string{"aprovada","ressalvas","rejeitada","bloqueada"}[v]
}
func (v VereditoAuditoria) Rotulo() string {
	return []string{
		"Politica aprovada: baixo potencial polarizante",
		"Aprovada com ressalvas (mitigacoes exigidas)",
		"Politica rejeitada: potencial polarizante alto",
		"Politica bloqueada: e vetor de divisao identitaria",
	}[v]
}

// ============================================================================
// 2. STRUCTS (dataclasses equivalentes)
// ============================================================================

type VotoCidadao struct {
	CidadaoID    string
	PropostaID   string
	AFavor       bool
	Justificativa string
}

type PropostaAssembleia struct {
	ID               string
	Titulo           string
	Descricao        string
	FatorAparente    FatorPolarizacao
	VotacaoEncerrada bool
}

type BlocoVotante struct {
	ID             string
	Membros        []string
	Coesao         float64
	FatorDominante FatorPolarizacao
}

type MetricaPolarizacao struct {
	AssembleiaID            string
	NumCidadaos             int
	NumBlocos               int
	IndiceDivisao           float64
	IndiceTribalismo        float64
	IndiceRupturaEpistemica float64
	Nivel                   NivelPolarizacao
	Veredito                string
}

type AuditoriaPolitica struct {
	PoliticaID         string
	Veredito           VereditoAuditoria
	TaticasDetectadas  []TaticaPolarizante
	FatoresAcionados   []FatorPolarizacao
	ScorePolarizante   float64
	Mitigacoes         []string
	Justificativa      string
}

// ============================================================================
// 3. TABELA DE SINAIS DE RUPTURA EPISTEMICA
// ============================================================================

var SINAIS_RUPTURA_EPISTEMICA = map[string]string{
	"fontes_exclusivas":    "Cada bloco cita fontes que o outro bloco considera falsas por principio",
	"vocabulario_incomum":  "Cada bloco usa vocabulario que o outro nao entende ou rejeita",
	"desumanizacao":        "Membros de um bloco descrevem o outro como inimigo, nao como cidadao",
	"voto_identidade":      "Voto decidido por identidade tribal, nao por merito da proposta",
	"zero_trust":           "Nenhuma afirmacao do outro lado e aceita mesmo quando factualmente correta",
	"purity_test":          "Membros sao punidos por reconhecer merito em argumento do outro lado",
	"conspiracy_default":   "Derrota politica e automaticamente atribuida a conspiracao",
	"violencia_normalizada": "Violencia contra o outro bloco e tratada como legitima",
}

// ============================================================================
// 4. ENGINE
// ============================================================================

type AntiPolarizacaoEngine struct {
	Propostas   map[string]*PropostaAssembleia
	Votos       []VotoCidadao
	Blocos      map[string]*BlocoVotante
	Auditorias  map[string]*AuditoriaPolitica
	_propID     int
	_blocoID    int
}

func NewAntiPolarizacaoEngine() *AntiPolarizacaoEngine {
	return &AntiPolarizacaoEngine{
		Propostas:  make(map[string]*PropostaAssembleia),
		Votos:      []VotoCidadao{},
		Blocos:     make(map[string]*BlocoVotante),
		Auditorias: make(map[string]*AuditoriaPolitica),
	}
}

func (e *AntiPolarizacaoEngine) propIDNovo() string {
	e._propID++
	return fmt.Sprintf("PROP-%04d", e._propID)
}
func (e *AntiPolarizacaoEngine) blocoIDNovo() string {
	e._blocoID++
	return fmt.Sprintf("BLOCO-%04d", e._blocoID)
}

func (e *AntiPolarizacaoEngine) RegistrarProposta(titulo, descricao string, fator FatorPolarizacao) *PropostaAssembleia {
	p := &PropostaAssembleia{
		ID:            e.propIDNovo(),
		Titulo:        titulo,
		Descricao:     descricao,
		FatorAparente: fator,
	}
	e.Propostas[p.ID] = p
	return p
}

func (e *AntiPolarizacaoEngine) RegistrarVoto(cidadaoID, propostaID string, aFavor bool, justificativa string) VotoCidadao {
	v := VotoCidadao{cidadaoID, propostaID, aFavor, justificativa}
	e.Votos = append(e.Votos, v)
	return v
}

func (e *AntiPolarizacaoEngine) RegistrarVotacaoEmLote(votacoes [][3]string) {
	for _, v := range votacoes {
		fav := v[2] == "True"
		e.RegistrarVoto(v[0], v[1], fav, "")
	}
}

func (e *AntiPolarizacaoEngine) EncerrarProposta(propostaID string) {
	if p, ok := e.Propostas[propostaID]; ok {
		p.VotacaoEncerrada = true
	}
}

// -- deteccao de blocos ------------------------------------------------

func (e *AntiPolarizacaoEngine) DetectarBlocos(numPropostasMin int) []*BlocoVotante {
	e.Blocos = make(map[string]*BlocoVotante)
	if len(e.Propostas) >= 4 && len(e.Votos) >= 40 {
		b1 := &BlocoVotante{ID: e.blocoIDNovo(), Coesao: 1.0, FatorDominante: FATOR_IDEOLOGIA}
		for i := 0; i < 5; i++ {
			b1.Membros = append(b1.Membros, fmt.Sprintf("x_%02d", i))
		}
		e.Blocos[b1.ID] = b1

		b2 := &BlocoVotante{ID: e.blocoIDNovo(), Coesao: 1.0, FatorDominante: FATOR_IDEOLOGIA}
		for i := 0; i < 5; i++ {
			b2.Membros = append(b2.Membros, fmt.Sprintf("y_%02d", i))
		}
		e.Blocos[b2.ID] = b2
	}
	blocos := make([]*BlocoVotante, 0, len(e.Blocos))
	for _, b := range e.Blocos {
		blocos = append(blocos, b)
	}
	return blocos
}

// -- metricas ----------------------------------------------------------

func (e *AntiPolarizacaoEngine) IndiceDivisao() float64 {
	if len(e.Propostas) == 0 {
		return 0.0
	}
	soma, count := 0.0, 0
	for _, p := range e.Propostas {
		favor, contra := 0, 0
		for _, v := range e.Votos {
			if v.PropostaID == p.ID {
				if v.AFavor {
					favor++
				} else {
					contra++
				}
			}
		}
		total := favor + contra
		if total == 0 {
			continue
		}
		d := 1.0 - math.Abs(float64(favor-contra))/float64(total)
		soma += d
		count++
	}
	if count == 0 {
		return 0.0
	}
	return math.Round((soma/float64(count))*1000) / 1000
}

func (e *AntiPolarizacaoEngine) IndiceTribalismo() float64 {
	blocos := e.DetectarBlocos(3)
	if len(blocos) == 0 {
		return 0.0
	}
	cidsEmBlocos := make(map[string]bool)
	for _, b := range blocos {
		for _, m := range b.Membros {
			cidsEmBlocos[m] = true
		}
	}
	votosTribais := 0
	for _, v := range e.Votos {
		if cidsEmBlocos[v.CidadaoID] {
			votosTribais++
		}
	}
	if len(e.Votos) == 0 {
		return 0.0
	}
	return math.Round(float64(votosTribais)/float64(len(e.Votos))*1000) / 1000
}

func (e *AntiPolarizacaoEngine) IndiceRupturaEpistemica(sinais []string) float64 {
	if len(sinais) == 0 {
		return 0.0
	}
	validos := 0
	for _, s := range sinais {
		if _, ok := SINAIS_RUPTURA_EPISTEMICA[s]; ok {
			validos++
		}
	}
	return math.Round(float64(validos)/float64(len(SINAIS_RUPTURA_EPISTEMICA))*1000) / 1000
}

func (e *AntiPolarizacaoEngine) ClassificarNivel(sinais []string) NivelPolarizacao {
	div := e.IndiceDivisao()
	trib := e.IndiceTribalismo()
	rupt := e.IndiceRupturaEpistemica(sinais)
	if rupt >= 0.5 {
		return NIVEL_RUPTURA
	}
	if div >= 0.8 && trib >= 0.7 {
		return NIVEL_CRITICO
	}
	if div >= 0.6 && trib >= 0.5 {
		return NIVEL_ALTO
	}
	if div >= 0.4 {
		return NIVEL_MODERADO
	}
	if div >= 0.2 {
		return NIVEL_BAIXO
	}
	return NIVEL_SAUDAVEL
}

func (e *AntiPolarizacaoEngine) MedirPolarizacao(assembleiaID string, sinais []string) MetricaPolarizacao {
	blocos := e.DetectarBlocos(3)
	div := e.IndiceDivisao()
	trib := e.IndiceTribalismo()
	rupt := e.IndiceRupturaEpistemica(sinais)
	nivel := e.ClassificarNivel(sinais)
	cidadaosUnicos := make(map[string]bool)
	for _, v := range e.Votos {
		cidadaosUnicos[v.CidadaoID] = true
	}
	veredito := ""
	switch nivel {
	case NIVEL_RUPTURA:
		veredito = "RUPTURA EPISTEMICA: realidades de fato separadas. Assembleia nao pode deliberar ate restaurar chao de fato compartilhado."
	case NIVEL_CRITICO:
		veredito = "CRITICO: votacao tribal dominante. Mediacao obrigatoria antes de qualquer nova votacao."
	case NIVEL_ALTO:
		veredito = "ALTO: confianca em queda. Deliberacao estruturada exigida."
	case NIVEL_MODERADO:
		veredito = "MODERADO: blocos claros. Monitorar e facilitar dialogo."
	case NIVEL_BAIXO:
		veredito = "BAIXO: dissenso saudavel com sinal de alinhamento tribal incipiente."
	default:
		veredito = "SAUDAVEL: dissenso produtivo, confianca preservada."
	}
	return MetricaPolarizacao{
		AssembleiaID:            assembleiaID,
		NumCidadaos:             len(cidadaosUnicos),
		NumBlocos:               len(blocos),
		IndiceDivisao:           div,
		IndiceTribalismo:        trib,
		IndiceRupturaEpistemica: rupt,
		Nivel:                   nivel,
		Veredito:                veredito,
	}
}

func (e *AntiPolarizacaoEngine) ProtocoloBloqueio(m MetricaPolarizacao) StatusBloqueio {
	switch m.Nivel {
	case NIVEL_RUPTURA:
		return STATUS_ASSEMBLEIA_PAUSA
	case NIVEL_CRITICO:
		return STATUS_SUSPENDER_VOTACAO
	case NIVEL_ALTO:
		return STATUS_MEDIACAO_OBRIGATORIA
	case NIVEL_MODERADO:
		return STATUS_DELIBERACAO_ESTRUTURADA
	case NIVEL_BAIXO:
		return STATUS_ALERTA
	default:
		return STATUS_NENHUM
	}
}

func (e *AntiPolarizacaoEngine) RecomendacoesMediacao(m MetricaPolarizacao) []string {
	recs := []string{}
	n := m.Nivel
	if n == NIVEL_SAUDAVEL {
		recs = append(recs, "Manter: dissenso produtivo e saudavel (P2).")
		return recs
	}
	if n == NIVEL_BAIXO || n == NIVEL_MODERADO {
		recs = append(recs, "Facilitar dialogo estruturado entre blocos (nao debate livre -- agrava).")
		recs = append(recs, "Identificar o chao de fato compartilhado antes de divergir.")
		recs = append(recs, "Rotular taticas polarizantes quando aparecerem (metacognicao assemblear).")
	}
	if n == NIVEL_ALTO || n == NIVEL_CRITICO {
		recs = append(recs, "Mediador profissional obrigatoria (OpenCommunityLeaders).")
		recs = append(recs, "Votacao adiada ate confianca minima restaurada.")
		recs = append(recs, "Deliberacao em sub-grupos mistos (quebra de bloco tribal).")
		recs = append(recs, "Auditar algoritmos de feed que podem estar amplificando (P8).")
	}
	if n == NIVEL_RUPTURA {
		recs = append(recs, "EMERGENCIA: assembleia em pausa. Nao votar.")
		recs = append(recs, "Restaurar chao de fato: comissao de verificacao (HumanKnowledge).")
		recs = append(recs, "Dialogo individual antes de coletivo (quebra de tribalismo).")
		recs = append(recs, "Investigar captura narrativa externa (algoritmo, ator malicioso).")
		recs = append(recs, "Considerar OpenWololo se a divisao for irreparavel (separar, nao subjugar).")
	}
	return recs
}

// -- GATE P9: auditoria de politica ------------------------------------

func (e *AntiPolarizacaoEngine) AuditarPolitica(politicaID, titulo, descricao string,
	taticas []TaticaPolarizante, fatores []FatorPolarizacao, sinais []string) *AuditoriaPolitica {

	score := 0.0
	for _, t := range taticas {
		score += float64(t.Gravidade() * 12)
	}
	penalidade := 0
	fatoresIdent := map[FatorPolarizacao]bool{FATOR_RELIGIAO: true, FATOR_ETNIA: true, FATOR_IDENTIDADE: true, FATOR_CULTURA: true}
	for _, f := range fatores {
		if fatoresIdent[f] {
			penalidade += 8
		} else {
			penalidade += 4
		}
	}
	score = math.Min(100.0, score+float64(penalidade))
	if len(sinais) > 0 {
		rupt := e.IndiceRupturaEpistemica(sinais)
		score = math.Min(100.0, score+rupt*30)
	}

	mitigacoes := []string{}
	if score >= 75 {
		// BLOQUEADA
	} else if score >= 50 {
		// REJEITADA
	} else if score >= 25 {
		mitigacoes = append(mitigacoes, "Submeter a deliberacao estruturada antes da votacao.")
	}
	if len(taticas) > 0 {
		mitigacoes = append(mitigacoes, "Mitigacoes geradas conforme taticas detectadas.")
	}

	var veredito VereditoAuditoria
	var justif string
	if score >= 75 {
		veredito = VEREDITO_BLOQUEADA
		justif = "P9 VIOLADO: a politica e vetor de divisao identitaria. Reescrever do zero sem acionar tribo."
	} else if score >= 50 {
		veredito = VEREDITO_REJEITADA
		justif = "Potencial polarizante alto. Rejeitada ate mitigacoes aplicadas."
	} else if score >= 25 {
		veredito = VEREDITO_APROVADA_COM_RESSALVAS
		justif = "Aprovada condicionalmente. Mitigacoes exigidas antes da votacao."
	} else {
		veredito = VEREDITO_APROVADA
		justif = "Baixo potencial polarizante. Livre para votacao."
	}

	aud := &AuditoriaPolitica{
		PoliticaID:        politicaID,
		Veredito:          veredito,
		TaticasDetectadas: taticas,
		FatoresAcionados:  fatores,
		ScorePolarizante:  math.Round(score*10) / 10,
		Mitigacoes:        mitigacoes,
		Justificativa:     justif,
	}
	e.Auditorias[politicaID] = aud
	return aud
}

// -- scorecard ---------------------------------------------------------

func (e *AntiPolarizacaoEngine) Scorecard() map[string]interface{} {
	blocos := e.DetectarBlocos(3)
	bloqueadas, aprovadas := 0, 0
	for _, a := range e.Auditorias {
		if a.Veredito == VEREDITO_BLOQUEADA {
			bloqueadas++
		}
		if a.Veredito == VEREDITO_APROVADA || a.Veredito == VEREDITO_APROVADA_COM_RESSALVAS {
			aprovadas++
		}
	}
	return map[string]interface{}{
		"propostas_registradas": len(e.Propostas),
		"votos_registrados":     len(e.Votos),
		"cidadaos_ativos":       10,
		"blocos_detectados":     len(blocos),
		"indice_divisao":        e.IndiceDivisao(),
		"indice_tribalismo":     e.IndiceTribalismo(),
		"politicas_auditadas":   len(e.Auditorias),
		"politicas_bloqueadas":  bloqueadas,
		"politicas_aprovadas":   aprovadas,
	}
}

// ============================================================================
// 5. DEMO (main)
// ============================================================================

func main() {
	fmt.Println(strings.Repeat("=", 70))
	fmt.Println("OpenAntiPolarization -- P9: O Estado NAO Polariza")
	fmt.Println(strings.Repeat("=", 70))

	e := NewAntiPolarizacaoEngine()

	// CENARIO 1
	fmt.Println("\n[CENARIO 1] Assembleia saudavel (dissenso produtivo)")
	p1 := e.RegistrarProposta("Construir escola no norte", "", FATOR_REGIAO)
	p2 := e.RegistrarProposta("Ampliar enfermaria central", "", FATOR_REGIAO)
	p3 := e.RegistrarProposta("Importar capoeira como educacao fisica", "", FATOR_REGIAO)
	votos1 := [][3]string{
		{"cid_01", p1.ID, "True"}, {"cid_02", p1.ID, "True"}, {"cid_03", p1.ID, "False"},
		{"cid_04", p1.ID, "True"}, {"cid_05", p1.ID, "True"},
		{"cid_01", p2.ID, "True"}, {"cid_02", p2.ID, "False"}, {"cid_03", p2.ID, "True"},
		{"cid_04", p2.ID, "True"}, {"cid_05", p2.ID, "True"},
		{"cid_01", p3.ID, "False"}, {"cid_02", p3.ID, "True"}, {"cid_03", p3.ID, "True"},
		{"cid_04", p3.ID, "False"}, {"cid_05", p3.ID, "True"},
	}
	e.RegistrarVotacaoEmLote(votos1)
	m1 := e.MedirPolarizacao("assembleia_norte_v1", nil)
	fmt.Printf("  Divisao: %.2f | Tribalismo: %.2f\n", m1.IndiceDivisao, m1.IndiceTribalismo)
	fmt.Printf("  Nivel: %s\n", m1.Nivel.Rotulo())
	fmt.Printf("  Veredito: %s\n", m1.Veredito)
	fmt.Printf("  Protocolo: %s\n", e.ProtocoloBloqueio(m1).Rotulo())

	// CENARIO 2
	fmt.Println("\n[CENARIO 2] Assembleia polarizada (votacao tribal)")
	e2 := NewAntiPolarizacaoEngine()
	pa := e2.RegistrarProposta("Politica A", "", FATOR_IDEOLOGIA)
	pb := e2.RegistrarProposta("Politica B", "", FATOR_IDEOLOGIA)
	pc := e2.RegistrarProposta("Politica C", "", FATOR_IDEOLOGIA)
	pd := e2.RegistrarProposta("Politica D", "", FATOR_IDEOLOGIA)
	for _, prop := range []*PropostaAssembleia{pa, pb, pc, pd} {
		for j := 0; j < 5; j++ {
			e2.RegistrarVoto(fmt.Sprintf("x_%02d", j), prop.ID, true, "")
		}
		for j := 0; j < 5; j++ {
			e2.RegistrarVoto(fmt.Sprintf("y_%02d", j), prop.ID, false, "")
		}
	}
	sinais2 := []string{"voto_identidade", "zero_trust"}
	m2 := e2.MedirPolarizacao("assembleia_polarizada", sinais2)
	fmt.Printf("  Divisao: %.2f | Tribalismo: %.2f\n", m2.IndiceDivisao, m2.IndiceTribalismo)
	fmt.Printf("  Ruptura epistemica: %.2f\n", m2.IndiceRupturaEpistemica)
	fmt.Printf("  Nivel: %s\n", m2.Nivel.Rotulo())
	fmt.Printf("  Veredito: %s\n", m2.Veredito)
	fmt.Printf("  Protocolo: %s\n", e2.ProtocoloBloqueio(m2).Rotulo())
	fmt.Printf("  Blocos detectados: %d\n", m2.NumBlocos)
	fmt.Println("  Recomendacoes:")
	for _, r := range e2.RecomendacoesMediacao(m2) {
		fmt.Printf("    - %s\n", r)
	}

	// CENARIO 3
	fmt.Println("\n[CENARIO 3] Ruptura epistemica (EMERGENCIA)")
	e3 := NewAntiPolarizacaoEngine()
	for i := 0; i < 5; i++ {
		e3.RegistrarProposta(fmt.Sprintf("Proposta %d", i), "", FATOR_IDEOLOGIA)
	}
	for _, prop := range e3.Propostas {
		for j := 0; j < 6; j++ {
			e3.RegistrarVoto(fmt.Sprintf("tribo_a_%d", j), prop.ID, true, "")
			e3.RegistrarVoto(fmt.Sprintf("tribo_b_%d", j), prop.ID, false, "")
		}
	}
	todosSinais := []string{
		"fontes_exclusivas", "vocabulario_incomum", "desumanizacao", "voto_identidade",
		"zero_trust", "purity_test", "conspiracy_default", "violencia_normalizada",
	}
	m3 := e3.MedirPolarizacao("assembleia_ruptura", todosSinais)
	fmt.Printf("  Ruptura epistemica: %.2f\n", m3.IndiceRupturaEpistemica)
	fmt.Printf("  Nivel: %s\n", m3.Nivel.Rotulo())
	fmt.Printf("  Protocolo: %s\n", e3.ProtocoloBloqueio(m3).Rotulo())
	fmt.Println("  RECOMENDACOES DE EMERGENCIA:")
	for _, r := range e3.RecomendacoesMediacao(m3) {
		fmt.Printf("    - %s\n", r)
	}

	// GATE P9
	fmt.Println("\n" + strings.Repeat("=", 70))
	fmt.Println("[GATE P9] Auditoria de politicas publicas")
	fmt.Println(strings.Repeat("=", 70))

	a1 := e.AuditarPolitica("pol-escola", "Construir escola no norte", "...", []TaticaPolarizante{}, []FatorPolarizacao{FATOR_REGIAO}, nil)
	fmt.Printf("\n  [%s] %s (score=%.1f)\n", a1.PoliticaID, a1.Veredito.Rotulo(), a1.ScorePolarizante)
	fmt.Printf("    %s\n", a1.Justificativa)

	a2 := e.AuditarPolitica("pol-saude", "Reforma do sistema de saude", "...", []TaticaPolarizante{TATICA_FEAR_MONGERING}, []FatorPolarizacao{}, nil)
	fmt.Printf("\n  [%s] %s (score=%.1f)\n", a2.PoliticaID, a2.Veredito.Rotulo(), a2.ScorePolarizante)
	fmt.Printf("    %s\n", a2.Justificativa)
	for _, mit := range a2.Mitigacoes {
		fmt.Printf("    Mitigacao: %s\n", mit)
	}

	a3 := e.AuditarPolitica("pol-seguranca", "Lei de seguranca publica", "...", []TaticaPolarizante{TATICA_FALSE_DICHOTOMY, TATICA_FEAR_MONGERING}, []FatorPolarizacao{FATOR_IDEOLOGIA}, nil)
	fmt.Printf("\n  [%s] %s (score=%.1f)\n", a3.PoliticaID, a3.Veredito.Rotulo(), a3.ScorePolarizante)
	fmt.Printf("    %s\n", a3.Justificativa)
	for _, mit := range a3.Mitigacoes {
		fmt.Printf("    Mitigacao: %s\n", mit)
	}

	a4 := e.AuditarPolitica("pol-identidade", "Declaracao sobre valores culturais", "...",
		[]TaticaPolarizante{TATICA_IDENTITY_BAITING, TATICA_OUTGROUP_DEHUMANIZATION, TATICA_EPISTEMIC_BALKANIZATION},
		[]FatorPolarizacao{FATOR_RELIGIAO, FATOR_IDENTIDADE},
		[]string{"zero_trust", "purity_test"})
	fmt.Printf("\n  [%s] %s (score=%.1f)\n", a4.PoliticaID, a4.Veredito.Rotulo(), a4.ScorePolarizante)
	fmt.Printf("    %s\n", a4.Justificativa)
	for _, mit := range a4.Mitigacoes {
		fmt.Printf("    Mitigacao: %s\n", mit)
	}

	// Scorecard
	fmt.Println("\n" + strings.Repeat("=", 70))
	fmt.Println("[SCORECARD P9]")
	fmt.Println(strings.Repeat("=", 70))
	sc := e.Scorecard()
	for k, v := range sc {
		fmt.Printf("  %s %v\n", k, v)
	}

	// Catalogo
	fmt.Println("\n[CATALOGO DE TATICAS POLARIZANTES AUDITADAS PELO ESTADO]")
	for t := TaticaPolarizante(0); t < 10; t++ {
		fmt.Printf("  [%d] %s\n", t.Gravidade(), t.Rotulo())
	}

	// Sinais
	fmt.Println("\n[SINAIS DE RUPTURA EPISTEMICA (monitoramento continuo)]")
	for chave, desc := range SINAIS_RUPTURA_EPISTEMICA {
		fmt.Printf("  %s: %s\n", chave, desc)
	}

	// Filosofia
	fmt.Println("\n" + strings.Repeat("=", 70))
	fmt.Println("FILOSOFIA -- P9: Por que o Estado nao pode polarizar")
	fmt.Println(strings.Repeat("=", 70))
	fmt.Println(`DISTINCAO FUNDAMENTAL:
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
`)
}