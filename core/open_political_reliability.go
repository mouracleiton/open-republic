// OpenPoliticalReliability -- Simulacao de Confiabilidade do Sujeito Politico
// =============================================================================
// "O poder nao se mede pela quantidade de votos, mas pela qualidade do processo."

// A Republica NAO confia em sujeitos politicos. Confia em PROCESSOS.
// Mas para AUDITAR processos, precisa avaliar a CONFIABILIDADE dos sujeitos
// que operam dentro deles.

// Este modulo e um SIMULADOR de confiabilidade politica. NAO e tribunal.
// NAO condena. AVALIA com base em indicadores verificaveis e produz um
// SCORE de confiabilidade que a assembleia pode usar para decidir se um
// sujeito pode operar dentro das instituicoes da Republica.

// PRINCIPIO (P4): A transparencia e radical. Se um sujeito opera no poder,
// todo seu historico e auditavel. Nao existe "privacidade politica" para
// quem exerce poder publico -- poder publico e PUBLICO.

// O QUE O SIMULADOR MEDE:
// 1. USO DE APARELHO PUBLICO para beneficio eleitoral
// 2. COMPRA DE VOTO (clientelismo, bolsa, promessa)
// 3. CONTINUIDADE NO PODER (quantos mandatos, indicio de perpetuacao)
// 4. DESMANCHE DE ALTERNATIVAS (impede novas candidaturas no proprio campo)
// 5. CORRUPCAO SISTEMICA (e caso isolado ou padrao?)
// 6. MANIPULACAO DE INFORMACAO (bots, redes, narrativa fabricada)
// 7. TRANSPARENCIA (abre dados ou esconde?)
// 8. RENOVACAO DE ELITES (treina sucessores ou se torna insubstituivel?)

// ALINHAMENTO CONSTITUCIONAL:
// - P1: Confianca politica nao heranca. Cada mandato auditado.
// - P4: Democracia radical exige sujeitos confiaveis. Processo corrompido = vitro eleitoral.
// - P9: Sujeito que polariza para perpetuar VIOLA o P9 (Estado nao polariza).

// Author: OpenRepublic Team

package main

import (
	"fmt"
	"math"
)

// ============================================================================
// 1. ENUMS (modulo-level)
// ============================================================================

type TipoIndicador int

const (
	TIPO_USO_APARELHO_PUBLICO TipoIndicador = iota
	TIPO_COMPRA_VOTO
	TIPO_CONTINUIDADE_PODER
	TIPO_DESMANCHE_ALTERNATIVAS
	TIPO_CORRUPCAO_SISTEMICA
	TIPO_MANIPULACAO_INFORMACAO
	TIPO_OPACIDADE
	TIPO_PERSONALISMO
	TIPO_VIOLACAO_PRINCIPIOS
	TIPO_MILITANCIA_FINANCEIRA
)

var TipoIndicador_id = []string{
	"uso_aparelho", "compra_voto", "continuidade", "desmanche", "corrupcao",
	"manipulacao_info", "opacidade", "personalismo", "violacao_principios", "militancia_fin",
}
var TipoIndicador_rotulo = []string{
	"Uso de aparelho de Estado para fim eleitoral",
	"Compra de voto / clientelismo / bolsa-eleicao",
	"Perpetuacao no poder (mandatos sucessivos)",
	"Desmanche de novas candidaturas no proprio campo",
	"Corrupcao sistemica (padrao, nao caso isolado)",
	"Manipulacao de informacao (bots, narrativa fabricada)",
	"Falta de transparencia / esconda dados publicos",
	"Personalismo (se torna insubstituivel, sem sucessor)",
	"Violacao de principios constitucionais",
	"Militancia comprada (cargo em troca de apoio)",
}
var TipoIndicador_peso = []int{10, 10, 8, 7, 10, 8, 6, 7, 9, 7}

type NivelConfiabilidade int

const (
	NIVEL_CONFIGAVEL NivelConfiabilidade = iota
	NIVEL_ACEITAVEL
	NIVEL_PREOCUPANTE
	NIVEL_ALTO_RISCO
	NIVEL_INACEITAVEL
)

var NivelConfiabilidade_id = []string{"confiavel", "aceitavel", "preocupante", "alto_risco", "inaceitavel"}
var NivelConfiabilidade_rotulo = []string{
	"Confiavel: sem indicadores graves, processo transparente",
	"Aceitavel: indicadores leves, monitorar",
	"Preocupante: multiplos indicadores, assembleia avalia",
	"Alto risco: padrao de manipulacao sistemica",
	"Inaceitavel: processo corrompido, nao opera na Republica",
}
var NivelConfiabilidade_score_max = []int{100, 79, 59, 39, 19}
var NivelConfiabilidade_score_min = []int{80, 60, 40, 20, 0}

type MetodoManipulacao int

const (
	METODO_BOTS_REDES MetodoManipulacao = iota
	METODO_APARELHO_ELEITORAL
	METODO_CLIENTELISMO
	METODO_CARGOS_TROCA
	METODO_NARRATIVA_FABRICADA
	METODO_IMPEDIR_CANDIDATURA
	METODO_JUDICIALIZACAO_ARMA
	METODO_MIDIA_COMPRADA
	METODO_FINANCIAMENTO_OCULTO
	METODO_MEDO_E_AMEACA
)

var MetodoManipulacao_id = []string{
	"bots_redes", "aparelho_eleitoral", "clientelismo", "cargos_troca", "narrativa_fabricada",
	"impedir_candidatura", "judicializacao_arma", "midia_comprada", "financiamento_oculto", "medo_ameaca",
}
var MetodoManipulacao_rotulo = []string{
	"Bots e operacao de redes sociais",
	"Maquina publica a servico de candidatura",
	"Troca de beneficio por voto",
	"Distribuicao de cargos em troca de apoio",
	"Construcao de narrativa falsa",
	"Impedir surgimento de novas candidaturas",
	"Usar sistema judicial contra oponentes",
	"Comprar cobertura midiatica",
	"Caixa 2 / financiamento nao declarado",
	"Gerar medo na populacao para colher votos",
}

type GraveEvidencia int

const (
	EVIDENCIA_COMPROVADO_JUDICIAL GraveEvidencia = iota
	EVIDENCIA_INVESTIGACAO_OFICIAL
	EVIDENCIA_EVIDENCIA_JORNALISTICA
	EVIDENCIA_INDICIO_FORTE
	EVIDENCIA_DENUNCIA
	EVIDENCIA_SUSPEITA
)

var GraveEvidencia_id = []string{
	"comprovado_judicial", "investigacao_oficial", "evidencia_jornalistica",
	"indicio_forte", "denuncia", "suspeita",
}
var GraveEvidencia_rotulo = []string{
	"Comprovado judicialmente (sentenca transitada)",
	"Investigacao oficial em curso",
	"Evidencia jornalistica consistente",
	"Indicio forte (multiplos sinais convergentes)",
	"Denuncia formal sem comprovacao",
	"Suspeita / opiniao publica sem comprovacao",
}
var GraveEvidencia_fator_confianca = []float64{1.0, 0.7, 0.6, 0.5, 0.3, 0.1}

type StatusVeredito int

const (
	STATUS_APROVADO StatusVeredito = iota
	STATUS_MONITORAR
	STATUS_RESTRITO
	STATUS_SUSPEITO
	STATUS_VETADO
)

var StatusVeredito_id = []string{"aprovado", "monitorar", "restrito", "suspeito", "vetado"}
var StatusVeredito_rotulo = []string{
	"Sujeito pode operar na Republica",
	"Pode operar com monitoramento continuo",
	"Operacao restrita (sem cargo de poder decisiorio)",
	"Suspeito: assembleia decide caso a caso",
	"Vetado: processo corrompido, nao exerce poder na Republica",
}

// ============================================================================
// 2. STRUCTS (dataclasses)
// ============================================================================

type IndicadorPolitico struct {
	Tipo          TipoIndicador
	Descricao     string
	GrauEvidencia GraveEvidencia
	Ocorrencias   int
	Periodo       string
	Metodos       []MetodoManipulacao
	Detalhe       string
}

type EventoPolitico struct {
	ID                    string
	Ano                   string
	Descricao             string
	Tipo                  string
	ImpactoConfiabilidade int
	Evidencia             GraveEvidencia
}

type AvaliacaoConfiabilidade struct {
	Sujeito         string
	Cargo           string
	Mandatos        int
	Score           int
	Nivel           NivelConfiabilidade
	Veredito        StatusVeredito
	Indicadores     []IndicadorPolitico
	PontosForte     []string
	PontosFraco     []string
	Recomendacoes   []string
	Justificativa   string
}

type SimulacaoCenario struct {
	Cenario            string
	ProbabilidadePct   float64
	ImpactoDemocracia  string
	ImpactoRepublica   string
	AcaoRecomendada    string
}

// ============================================================================
// 3. ENGINE
// ============================================================================

type ConfiabilidadeEngine struct {
	Eventos []*EventoPolitico
	_evID   int
}

func NewConfiabilidadeEngine() *ConfiabilidadeEngine {
	return &ConfiabilidadeEngine{Eventos: []*EventoPolitico{}, _evID: 0}
}

func (e *ConfiabilidadeEngine) novoID() string {
	e._evID++
	return fmt.Sprintf("EV-%04d", e._evID)
}

func (e *ConfiabilidadeEngine) RegistrarEvento(ano, descricao, tipo string, impacto int, evidencia GraveEvidencia) *EventoPolitico {
	ev := &EventoPolitico{
		ID:                    e.novoID(),
		Ano:                   ano,
		Descricao:             descricao,
		Tipo:                  tipo,
		ImpactoConfiabilidade: impacto,
		Evidencia:             evidencia,
	}
	e.Eventos = append(e.Eventos, ev)
	return ev
}

func (e *ConfiabilidadeEngine) classificarNivel(score int) NivelConfiabilidade {
	if score >= 80 {
		return NIVEL_CONFIGAVEL
	} else if score >= 60 {
		return NIVEL_ACEITAVEL
	} else if score >= 40 {
		return NIVEL_PREOCUPANTE
	} else if score >= 20 {
		return NIVEL_ALTO_RISCO
	}
	return NIVEL_INACEITAVEL
}

func (e *ConfiabilidadeEngine) vereditoPorNivel(nivel NivelConfiabilidade, mandatos int) StatusVeredito {
	if nivel == NIVEL_CONFIGAVEL {
		return STATUS_APROVADO
	} else if nivel == NIVEL_ACEITAVEL {
		return STATUS_MONITORAR
	} else if nivel == NIVEL_PREOCUPANTE {
		return STATUS_RESTRITO
	} else if nivel == NIVEL_ALTO_RISCO {
		return STATUS_SUSPEITO
	}
	return STATUS_VETADO
}

func (e *ConfiabilidadeEngine) gerarRecomendacoes(inds []IndicadorPolitico, nivel NivelConfiabilidade, mandatos int) []string {
	recs := []string{}
	tiposAtivos := make(map[TipoIndicador]bool)
	for _, ind := range inds {
		tiposAtivos[ind.Tipo] = true
	}
	if tiposAtivos[TIPO_USO_APARELHO_PUBLICO] {
		recs = append(recs, "Auditar uso de recursos publicos em periodo eleitoral (OpenPublicAudit).")
	}
	if tiposAtivos[TIPO_COMPRA_VOTO] {
		recs = append(recs, "Implementar OpenVoteIntegrity: rastrear fluxo de beneficios antes de eleicao.")
	}
	if tiposAtivos[TIPO_MANIPULACAO_INFORMACAO] {
		recs = append(recs, "Auditar bots e operacao de redes (P9: Estado nao polariza via algoritmo).")
	}
	if tiposAtivos[TIPO_DESMANCHE_ALTERNATIVAS] {
		recs = append(recs, "Proteger pluralismo interno: assembleia garante direito a candidatura alternativa.")
	}
	if tiposAtivos[TIPO_PERSONALISMO] || mandatos >= 3 {
		recs = append(recs, "Exigir plano de successao: sujeito treina substituto ou nao exerce novo mandato.")
	}
	if tiposAtivos[TIPO_CORRUPCAO_SISTEMICA] {
		recs = append(recs, "Investigacao independente (OpenJudicialAudit) antes de qualquer integracao.")
	}
	if nivel == NIVEL_ALTO_RISCO || nivel == NIVEL_INACEITAVEL {
		recs = append(recs, "VETAR exercicio de cargo com poder decisiorio ate restaurar processo.")
		recs = append(recs, "Assembleia avalia se o SUJEITO ou o SISTEMA esta corrompido (P4).")
	}
	return recs
}

func (e *ConfiabilidadeEngine) gerarJustificativa(sujeito string, score int, nivel NivelConfiabilidade, inds []IndicadorPolitico, mandatos int) string {
	graves := 0
	for _, i := range inds {
		if GraveEvidencia_fator_confianca[i.GrauEvidencia] >= 0.5 {
			graves++
		}
	}
	return fmt.Sprintf("Sujeito '%s' avaliado com score %d/100 (%s). %d indicadores detectados, %d com evidencia forte ou superior. %d mandatos. Veredito baseado em indicadores verificaveis, nao em opiniao. A assembleia tem autoridade final (P4).",
		sujeito, score, NivelConfiabilidade_rotulo[nivel], len(inds), graves, mandatos)
}

func (e *ConfiabilidadeEngine) Avaliar(sujeito, cargo string, mandatos int, inds []IndicadorPolitico, eventos []*EventoPolitico) *AvaliacaoConfiabilidade {
	score := 100
	pontosFraco := []string{}
	pontosForte := []string{}

	for _, ind := range inds {
		penal := float64(TipoIndicador_peso[ind.Tipo]) * GraveEvidencia_fator_confianca[ind.GrauEvidencia] * math.Sqrt(float64(ind.Ocorrencias))
		if penal > 25 {
			penal = 25
		}
		score -= int(penal)
		pontosFraco = append(pontosFraco, fmt.Sprintf("[%s] %s (evidencia: %s, ocorrencias: %d)",
			TipoIndicador_rotulo[ind.Tipo], ind.Descricao, GraveEvidencia_rotulo[ind.GrauEvidencia], ind.Ocorrencias))
	}

	if mandatos >= 4 {
		score -= 10
		pontosFraco = append(pontosFraco, "Perpetuacao: 4 mandatos (risco de insubstituibilidade).")
	} else if mandatos >= 3 {
		score -= 5
		pontosFraco = append(pontosFraco, "Continuidade: 3 mandatos (monitorar renovacao).")
	}

	if eventos != nil {
		for _, ev := range eventos {
			if ev.ImpactoConfiabilidade < 0 {
				score += ev.ImpactoConfiabilidade
				pontosFraco = append(pontosFraco, fmt.Sprintf("%s: %s (%s)", ev.Ano, ev.Descricao, GraveEvidencia_rotulo[ev.Evidencia]))
			} else if ev.ImpactoConfiabilidade > 0 {
				if score+ev.ImpactoConfiabilidade > 100 {
					score = 100
				} else {
					score += ev.ImpactoConfiabilidade
				}
				pontosForte = append(pontosForte, fmt.Sprintf("%s: %s", ev.Ano, ev.Descricao))
			}
		}
	}

	if score < 0 {
		score = 0
	}
	if score > 100 {
		score = 100
	}

	nivel := e.classificarNivel(score)
	veredito := e.vereditoPorNivel(nivel, mandatos)
	recs := e.gerarRecomendacoes(inds, nivel, mandatos)
	just := e.gerarJustificativa(sujeito, score, nivel, inds, mandatos)

	return &AvaliacaoConfiabilidade{
		Sujeito:       sujeito,
		Cargo:         cargo,
		Mandatos:      mandatos,
		Score:         score,
		Nivel:         nivel,
		Veredito:      veredito,
		Indicadores:   inds,
		PontosForte:   pontosForte,
		PontosFraco:   pontosFraco,
		Recomendacoes: recs,
		Justificativa: just,
	}
}

func (e *ConfiabilidadeEngine) SimularCenarios(aval *AvaliacaoConfiabilidade) []*SimulacaoCenario {
	cenarios := []*SimulacaoCenario{}
	score := aval.Score

	// Cenario 1
	c1 := &SimulacaoCenario{Cenario: "Sujeito continua exercendo poder (status quo)"}
	if score < 40 {
		c1.ProbabilidadePct = 85
		c1.ImpactoDemocracia = "Processo democratico degenerado: voto e transacao, nao deliberacao."
		c1.ImpactoRepublica = "Se integrar a Republica, corrompe o processo. Assembleia capturada."
		c1.AcaoRecomendada = "Votar limitacao de mandatos + auditoria continua."
	} else if score < 60 {
		c1.ProbabilidadePct = 60
		c1.ImpactoDemocracia = "Erosao da confianca institucional. Alternativas sufocadas."
		c1.ImpactoRepublica = "Integracao arriscada. Monitoramento continuo necessario."
		c1.AcaoRecomendada = "Votar limitacao de mandatos + auditoria continua."
	} else {
		c1.ProbabilidadePct = 25
		c1.ImpactoDemocracia = "Risco baixo de degeneracao. Renovacao possivel."
		c1.ImpactoRepublica = "Integracao com salvaguardas."
		c1.AcaoRecomendada = "Monitorar."
	}
	cenarios = append(cenarios, c1)

	// Cenario 2
	c2 := &SimulacaoCenario{
		Cenario:           "Sujeito e substituido por sucessor da mesma equipe",
		ProbabilidadePct:  70,
		ImpactoDemocracia: "Equipe perpetua sem a 'cara'. Pode ser pior (menos escrutinio) ou melhor (renovacao).",
		ImpactoRepublica:  "Avaliar a EQUIPE, nao so o sujeito. Se a equipe corrompeu o processo, trocar a cara nao resolve.",
		AcaoRecomendada:   "Auditar a EQUIPE (OpenTeamAudit), nao so o sujeito.",
	}
	if aval.Mandatos < 3 {
		c2.ProbabilidadePct = 40
	}
	cenarios = append(cenarios, c2)

	// Cenario 3
	c3 := &SimulacaoCenario{
		Cenario:           "Nova candidatura emerge fora da maquina",
		ProbabilidadePct:  50,
		ImpactoDemocracia: "Renovacao democratica real. Risco de ser destruida pela maquina instalada.",
		ImpactoRepublica:  "Oportunidade de integrar sujeito sem divida com aparelho corrompido.",
		AcaoRecomendada:   "PROTEGER a nova candidatura (P4: democracia radical exige pluralismo real).",
	}
	if score < 40 {
		c3.ProbabilidadePct = 30
	}
	cenarios = append(cenarios, c3)

	// Cenario 4
	c4 := &SimulacaoCenario{
		Cenario:           "Processo politico reestruturado (Nova Republica)",
		ProbabilidadePct:  100,
		ImpactoDemocracia: "Fim do ciclo de manipulacao. Voto = deliberacao, nao transacao.",
		ImpactoRepublica:  "O sujeito e avaliado em processo NOVO. Divida com o sistema antigo documentada, nao ignorada.",
		AcaoRecomendada:   "Assembleia constituinte decide: reintegrar com restricoes ou comecar do zero.",
	}
	cenarios = append(cenarios, c4)

	return cenarios
}

func (e *ConfiabilidadeEngine) CompararSujeitos(a, b *AvaliacaoConfiabilidade) string {
	diff := a.Score - b.Score
	var relacao string
	if abs(diff) < 5 {
		relacao = "equivalentes em confiabilidade"
	} else if diff > 0 {
		relacao = fmt.Sprintf("'%s' mais confiavel por %d pontos", a.Sujeito, diff)
	} else {
		relacao = fmt.Sprintf("'%s' mais confiavel por %d pontos", b.Sujeito, -diff)
	}
	return fmt.Sprintf("COMPARACAO:\n  %s: score %d (%s)\n  %s: score %d (%s)\n  Resultado: %s.\n  AVISO: comparar scores NAO significa que um e 'melhor'. Significa que um tem MENOS indicadores de processo corrompido. A Republica nao escolhe o 'menos pior'. Escolhe o processo LIMPO.",
		a.Sujeito, a.Score, NivelConfiabilidade_rotulo[a.Nivel],
		b.Sujeito, b.Score, NivelConfiabilidade_rotulo[b.Nivel], relacao)
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

// ============================================================================
// 4. DEMO (main)
// ============================================================================

func main() {
	e := NewConfiabilidadeEngine()

	fmt.Println("======================================================================")
	fmt.Println("OpenPoliticalReliability -- Simulacao de Confiabilidade do Sujeito")
	fmt.Println("======================================================================")

	// Sujeito A: O Operador
	fmt.Println("\n[AVALIACAO] Sujeito: 'O Operador' (perfil: lider historico de esquerda)")

	indsA := []IndicadorPolitico{
		{
			Tipo:          TIPO_USO_APARELHO_PUBLICO,
			Descricao:     "Maquina publica (cargos, beneficios, programas sociais) usada como aparelho eleitoral em 3 ciclos eleitorais.",
			GrauEvidencia: EVIDENCIA_EVIDENCIA_JORNALISTICA,
			Ocorrencias:   3,
			Periodo:       "3 eleicoes sucessivas",
			Metodos:       []MetodoManipulacao{METODO_APARELHO_ELEITORAL},
		},
		{
			Tipo:          TIPO_COMPRA_VOTO,
			Descricao:     "Programas sociais temporalmente ampliados antes de eleicoes; promessa de manutencao condicional ao voto.",
			GrauEvidencia: EVIDENCIA_INDICIO_FORTE,
			Ocorrencias:   3,
			Periodo:       "3 ciclos eleitorais",
			Metodos:       []MetodoManipulacao{METODO_CLIENTELISMO},
		},
		{
			Tipo:          TIPO_CONTINUIDADE_PODER,
			Descricao:     "Busca pelo 4o mandato. Equipe articula continuidade com a mesma figura como 'cara' do projeto.",
			GrauEvidencia: EVIDENCIA_EVIDENCIA_JORNALISTICA,
			Ocorrencias:   1,
			Periodo:       "pre-2026",
		},
		{
			Tipo:          TIPO_DESMANCHE_ALTERNATIVAS,
			Descricao:     "Novas candidaturas de esquerda desarticuladas pela maquina. Dissidentes marginalizados ou cooptados.",
			GrauEvidencia: EVIDENCIA_INDICIO_FORTE,
			Ocorrencias:   4,
			Metodos:       []MetodoManipulacao{METODO_IMPEDIR_CANDIDATURA, METODO_CARGOS_TROCA},
		},
		{
			Tipo:          TIPO_CORRUPCAO_SISTEMICA,
			Descricao:     "Multiplos esquemas de corrupcao vinculados a figuras do nucleo de poder (mensalao, petrolao, etc.). Padrao, nao caso isolado.",
			GrauEvidencia: EVIDENCIA_COMPROVADO_JUDICIAL,
			Ocorrencias:   5,
			Periodo:       "2005-presente",
		},
		{
			Tipo:          TIPO_MANIPULACAO_INFORMACAO,
			Descricao:     "Operacao de bots e redes sociais com intensidade equivalente a da direita. Narrativa fabricada em escala.",
			GrauEvidencia: EVIDENCIA_INVESTIGACAO_OFICIAL,
			Ocorrencias:   2,
			Periodo:       "2022-2026",
			Metodos:       []MetodoManipulacao{METODO_BOTS_REDES, METODO_NARRATIVA_FABRICADA},
		},
		{
			Tipo:          TIPO_PERSONALISMO,
			Descricao:     "Lider apresentado como insubstituivel. Nao ha plano de successao real -- a figura e o projeto.",
			GrauEvidencia: EVIDENCIA_EVIDENCIA_JORNALISTICA,
			Ocorrencias:   1,
		},
		{
			Tipo:          TIPO_MILITANCIA_FINANCEIRA,
			Descricao:     "Distribuicao de cargos e verbas em troca de apoio politico da base. Lealdade comprada, nao convencida.",
			GrauEvidencia: EVIDENCIA_COMPROVADO_JUDICIAL,
			Ocorrencias:   3,
			Metodos:       []MetodoManipulacao{METODO_CARGOS_TROCA},
		},
	}

	e.RegistrarEvento("2003-2010", "Dois mandatos presidenciais", "eleicao", 0, EVIDENCIA_SUSPEITA)
	e.RegistrarEvento("2005", "Mensalao: compra sistemica de votos no Congresso", "investigacao", -8, EVIDENCIA_COMPROVADO_JUDICIAL)
	e.RegistrarEvento("2014", "Operacao Lava Jato: esquema PETROBRAS", "investigacao", -8, EVIDENCIA_COMPROVADO_JUDICIAL)
	e.RegistrarEvento("2018-2021", "Prisao e condenacao (depois anuladas)", "judicial", -3, EVIDENCIA_INVESTIGACAO_OFICIAL)
	e.RegistrarEvento("2023-2026", "Terceiro mandato: uso de aparelho em ritmo eleitoral", "politica_publica", -5, EVIDENCIA_INDICIO_FORTE)

	avalA := e.Avaliar("O Operador", "Presidente (historico)", 4, indsA, e.Eventos[:5])

	fmt.Printf("\n  Score: %d/100\n", avalA.Score)
	fmt.Printf("  Nivel: %s\n", NivelConfiabilidade_rotulo[avalA.Nivel])
	fmt.Printf("  Veredito: %s\n", StatusVeredito_rotulo[avalA.Veredito])
	fmt.Printf("\n  INDICADORES DETECTADOS (%d):\n", len(avalA.Indicadores))
	for _, ind := range avalA.Indicadores {
		fmt.Printf("    [%s]\n", TipoIndicador_rotulo[ind.Tipo])
		fmt.Printf("      %s\n", ind.Descricao)
		fmt.Printf("      Evidencia: %s | Ocorrencias: %d\n", GraveEvidencia_rotulo[ind.GrauEvidencia], ind.Ocorrencias)
	}
	fmt.Println("\n  PONTOS FRACOS:")
	for _, pf := range avalA.PontosFraco {
		fmt.Printf("    - %s\n", pf)
	}
	fmt.Println("\n  RECOMENDACOES:")
	for _, rec := range avalA.Recomendacoes {
		fmt.Printf("    -> %s\n", rec)
	}
	fmt.Printf("\n  JUSTIFICATIVA: %s\n", avalA.Justificativa)

	// Simulacao
	fmt.Println("\n======================================================================")
	fmt.Println("[SIMULACAO DE CENARIOS]")
	fmt.Println("======================================================================")
	cenarios := e.SimularCenarios(avalA)
	for i, c := range cenarios {
		fmt.Printf("\n  Cenario %d: %s\n", i+1, c.Cenario)
		fmt.Printf("  Probabilidade: %.0f%%\n", c.ProbabilidadePct)
		fmt.Printf("  Impacto na democracia: %s\n", c.ImpactoDemocracia)
		fmt.Printf("  Impacto na Republica: %s\n", c.ImpactoRepublica)
		fmt.Printf("  Acao: %s\n", c.AcaoRecomendada)
	}

	// Sujeito B
	fmt.Println("\n======================================================================")
	fmt.Println("[COMPARACAO] O Operador vs O Polarizador (extrema-direita)")
	fmt.Println("======================================================================")

	indsB := []IndicadorPolitico{
		{
			Tipo:          TIPO_MANIPULACAO_INFORMACAO,
			Descricao:     "Operacao massiva de bots e fake news. Gabinete do odio institucionalizado.",
			GrauEvidencia: EVIDENCIA_INVESTIGACAO_OFICIAL,
			Ocorrencias:   3,
			Metodos:       []MetodoManipulacao{METODO_BOTS_REDES, METODO_NARRATIVA_FABRICADA, METODO_MEDO_E_AMEACA},
		},
		{
			Tipo:          TIPO_VIOLACAO_PRINCIPIOS,
			Descricao:     "Ataques sistemicos a instituicoes democraticas. Discurso de ruptura constitucional.",
			GrauEvidencia: EVIDENCIA_COMPROVADO_JUDICIAL,
			Ocorrencias:   5,
		},
		{
			Tipo:          TIPO_CORRUPCAO_SISTEMICA,
			Descricao:     "Esquema de rachadinha no nucleo familiar e militar. Cargo publico como negocio.",
			GrauEvidencia: EVIDENCIA_COMPROVADO_JUDICIAL,
			Ocorrencias:   3,
		},
		{
			Tipo:          TIPO_USO_APARELHO_PUBLICO,
			Descricao:     "Uso de atos oficiais, decretos e cargo para beneficios eleitorais e ataque a opositores.",
			GrauEvidencia: EVIDENCIA_EVIDENCIA_JORNALISTICA,
			Ocorrencias:   2,
			Metodos:       []MetodoManipulacao{METODO_APARELHO_ELEITORAL, METODO_JUDICIALIZACAO_ARMA},
		},
		{
			Tipo:          TIPO_PERSONALISMO,
			Descricao:     "Lider como messias. Movimento como seita. Nao ha sucesso institucional planejado.",
			GrauEvidencia: EVIDENCIA_EVIDENCIA_JORNALISTICA,
			Ocorrencias:   1,
		},
	}

	avalB := e.Avaliar("O Polarizador", "Presidente (extrema-direita)", 1, indsB, nil)
	fmt.Printf("\n  O Polarizador: score %d/100 (%s)\n", avalB.Score, NivelConfiabilidade_rotulo[avalB.Nivel])
	fmt.Printf("  Veredito: %s\n", StatusVeredito_rotulo[avalB.Veredito])
	fmt.Printf("\n%s\n", e.CompararSujeitos(avalA, avalB))

	// Scorecard
	fmt.Println("\n======================================================================")
	fmt.Println("[SCORECARD COMPARATIVO]")
	fmt.Println("======================================================================")
	fmt.Printf("  %-40s %10s %12s\n", "Indicador", "Operador", "Polarizador")
	fmt.Printf("  %s\n", "--------------------------------------------------------------")
	for t := 0; t < 10; t++ {
		aTem := "nao"
		for _, i := range indsA {
			if i.Tipo == TipoIndicador(t) {
				aTem = "SIM"
				break
			}
		}
		bTem := "nao"
		for _, i := range indsB {
			if i.Tipo == TipoIndicador(t) {
				bTem = "SIM"
				break
			}
		}
		fmt.Printf("  %-40s %10s %12s\n", TipoIndicador_rotulo[t], aTem, bTem)
	}
	fmt.Printf("  %-40s %10d %12d\n", "Score final", avalA.Score, avalB.Score)
	fmt.Printf("  %-40s %10s %12s\n", "Nivel", NivelConfiabilidade_id[avalA.Nivel], NivelConfiabilidade_id[avalB.Nivel])
	fmt.Printf("  %-40s %10s %12s\n", "Veredito", StatusVeredito_id[avalA.Veredito], StatusVeredito_id[avalB.Veredito])

	fmt.Println("\n======================================================================")
	fmt.Println("FILOSOFIA -- A Republica nao escolhe o 'menos pior'")
	fmt.Println("======================================================================")
	fmt.Println(`A TENSAO FUNDAMENTAL:
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
`)
}
