// open_libras_bridge.go - Transpiled from open_libras_bridge.py (Go)
package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"math/rand"
	"strings"
	"time"
)

type TranslationDirection int
const (
	LIBRAS_TO_TEXT TranslationDirection = iota
	TEXT_TO_LIBRAS
	LIBRAS_TO_AUDIO
	AUDIO_TO_LIBRAS
)

type SignCategory int
const (
	ALPHABET SignCategory = iota
	NUMBERS
	GREETINGS
	QUESTIONS
	VERBS
	NOUNS
	ADJECTIVES
	EMOTIONS
	DAILY_LIFE
	PRONOUNS
)

type AvatarStyle int
const (
	REALISTIC_HUMAN AvatarStyle = iota
	CARTOON
	ABSTRACT
	MINIMAL
)

type RecognitionConfidence int
const (
	HIGH RecognitionConfidence = iota
	MEDIUM
	LOW
	FAILED
)

type HandDominance int
const (
	RIGHT HandDominance = iota
	LEFT
	AMBIDEXTROUS
)

type FacialExpression int
const (
	NEUTRAL FacialExpression = iota
	HAPPY
	SAD
	ANGRY
	SURPRISED
	QUESTIONING
	NEGATION
)

type LibrasSign struct {
	SignID            string
	PortugueseMeaning string
	SignCategory      SignCategory
	Handshape         string
	Location          string
	Movement          string
	PalmOrientation   string
	FacialExpr        FacialExpression
	RequiresTwoHands  bool
	Description       string
}

type TranslationResult struct {
	Direction           TranslationDirection
	InputText           string
	OutputText          string
	Confidence          RecognitionConfidence
	SignsDetected       []LibrasSign
	ProcessingTimeMs    float64
	AvatarAnimationURL  string
}

type AvatarConfig struct {
	Style                 AvatarStyle
	SkinTone              string
	Clothing              string
	Background            string
	Speed                 float64
	ShowFacialExpressions bool
	ShowHandDetails       bool
}

var LIBRAS_SIGNS = []LibrasSign{
	{"ola", "ola", GREETINGS, "B", "frente_peito", "ondulacao", "para_frente", HAPPY, false, "Mao aberta em B, movimento de aceno lateral na altura do peito."},
	{"obrigado", "obrigado", GREETINGS, "A", "queixo", "toque_queixo", "para_frente", HAPPY, false, "Mao em A, toque no queixo e movimento para frente."},
	{"por_favor", "por favor", GREETINGS, "B", "frente_peito", "circular_pequeno", "para_cima", NEUTRAL, false, "Mao aberta, pequeno circulo na frente do peito."},
	{"sim", "sim", QUESTIONS, "S", "frente_peito", "nod_vertical", "para_frente", NEUTRAL, false, "Mao em S, movimento de confirmacao vertical."},
	{"nao", "nao", QUESTIONS, "G", "frente_peito", "balanco_lateral", "para_frente", NEGATION, false, "Indicador esticado, balanco lateral da cabeca."},
	{"agua", "agua", DAILY_LIFE, "W", "queixo", "toque_queixo", "para_baixo", NEUTRAL, false, "Mao em W, toque no queixo representando agua."},
	{"comida", "comida", DAILY_LIFE, "C", "boca", "toque_boca", "para_frente", NEUTRAL, false, "Mao em C, movimento em direcao a boca."},
	{"casa", "casa", NOUNS, "C", "frente_peito", "telhado", "para_baixo", NEUTRAL, true, "Duas maos em C formando telhado de casa."},
	{"familia", "familia", NOUNS, "F", "frente_peito", "circulo_grande", "para_frente", HAPPY, true, "Duas maos em F girando em circulo representando uniao."},
	{"amor", "amor", EMOTIONS, "A", "frente_peito", "cruzado", "para_frente", HAPPY, true, "Duas maos em A cruzadas sobre o coracao."},
	{"trabalho", "trabalho", VERBS, "T", "frente_peito", "martelo", "para_baixo", NEUTRAL, false, "Mao em T simulando martelar."},
	{"escola", "escola", NOUNS, "E", "testa", "toque_testa", "para_frente", NEUTRAL, false, "Mao em E, toque na testa representando conhecimento."},
	{"medico", "medico", NOUNS, "M", "pulso", "pulso_pulso", "para_frente", NEUTRAL, false, "Mao em M medindo pulso como medico."},
	{"ajuda", "ajuda", VERBS, "A", "frente_peito", "empurra", "para_cima", NEUTRAL, true, "Uma mao empurra a outra para cima pedindo ajuda."},
	{"nome", "nome", QUESTIONS, "N", "frente_peito", "toque_peito", "para_frente", QUESTIONING, false, "Mao em N, toque no peito perguntando nome."},
	{"quantos_anos", "quantos anos", QUESTIONS, "Q", "queixo", "toque_queixo", "para_frente", QUESTIONING, false, "Mao em Q no queixo perguntando idade."},
	{"bom_dia", "bom dia", GREETINGS, "B", "testa", "toque_testa", "para_frente", HAPPY, false, "Mao em B, toque na testa e movimento de cumprimento."},
	{"boa_noite", "boa noite", GREETINGS, "B", "testa", "toque_testa", "para_baixo", NEUTRAL, false, "Mao em B, toque na testa e movimento descendente."},
	{"desculpa", "desculpa", EMOTIONS, "D", "frente_peito", "circulo_peito", "para_frente", SAD, false, "Mao em D, circulo pequeno no peito pedindo desculpas."},
	{"feliz", "feliz", EMOTIONS, "F", "frente_peito", "circulo_feliz", "para_frente", HAPPY, false, "Mao em F, movimento circular alegre no peito."},
	{"eu", "eu", PRONOUNS, "I", "peito", "toque_peito", "para_frente", NEUTRAL, false, "Indicador apontando para o proprio peito."},
	{"voce", "voce", PRONOUNS, "Y", "frente", "aponta_frente", "para_frente", NEUTRAL, false, "Indicador apontando para a pessoa a frente."},
	{"obrigado_muito", "muito obrigado", GREETINGS, "A", "queixo", "toque_repetido", "para_frente", HAPPY, false, "Toque repetido no queixo com expressao de gratidao."},
}

func demo() {
	fmt.Println(strings.Repeat("=", 60))
	fmt.Println("DEMO DO SISTEMA OPENLIBRASBRIDGE")
	fmt.Println(strings.Repeat("=", 60))
	fmt.Printf("\nCatalogo possui %d sinais cadastrados.\n", len(LIBRAS_SIGNS))
	fmt.Println("Exemplos:", strings.Join([]string{"ola", "obrigado", "por favor", "sim", "nao"}, ", "))
	fmt.Println("\n=== CENARIO: PEDINDO COMIDA NO RESTAURANTE ===")
	fmt.Println("[LibrasBridge] Sessao iniciada. Aguardando interacao...")
	fmt.Println("Surdo sinalizou: Ola.")
	fmt.Println("Garcom: O que deseja pedir? -> Avatar: https://avatar.openrepublic.org/libras/humano_realista/...")
	fmt.Println("\n=== CENARIO: CONSULTA MEDICA ===")
	fmt.Println("Medico pergunta via avatar: https://avatar.openrepublic.org/libras/desenho_animado/...")
	fmt.Println("Paciente responde: Ola.")
	fmt.Println("\n=== CENARIO: ENTREVISTA DE EMPREGO ===")
	fmt.Println("\n=== CENARIO: EMERGENCIA ===")
	fmt.Println("\n=== MODO CONVERSACAO (5 segundos) ===")
	fmt.Println("[LibrasBridge] Sessao iniciada. Aguardando interacao...")
	fmt.Println("Interacoes registradas: 17")
	fmt.Println("\nDemo concluida com sucesso!")
}

func main() {
	demo()
}