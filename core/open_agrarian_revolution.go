// OpenAgrarianRevolution -- A Terra e de Quem a Cuida
// ============================================================
// A Revolucao Agraria da Republica Aberta vai alem da "reforma agraria" classica.
// Nao redistribui propriedade. ABOLI a propriedade da terra como mercadoria.
// A terra nao se compra, nao se vende, nao se herda, nao se acumula.
// A terra se CUIDA. Quem cuida, colhe o fruto. Quem abandona, devolve.
//
// ALINHAMENTO CONSTITUCIONAL:
// - P1 (Anti-elitismo): Latifundio = mecanismo original de elite. Concentrar
//   terra = concentrar vida. A Republica extingue a raiz da desigualdade rural.
// - P2 (Autonomia corporal): Quem trabalha a terra tem direito ao fruto do
//   trabalho. Ninguem morre de fome cercando terra que nao cultiva.
// - P3 (Trabalho igual): Crislto vem de IMPACTO (alimentar gente), nao de
//   aluguel de terra. Latifundio improdutivo = roubo sistêmico.
// - P4 (Democracia radical): Assembleia local decide o uso da terra. Nao
//   existe "dono". Existe GUARDIAO com mandato revogavel.
//
// OS 5 PILARES DA REVOLUCAO AGRARIA:
// 1. ABOLICAO da propriedade privada da terra (ninguem "possui" hectares)
// 2. GUARDIAO em vez de dono (quem cultiva cuida, mandato revogavel)
// 3. FUNCAO SOCIAL obrigatoria (terra ociosa = devolvida)
// 4. COOPERATIVISMO (nenhuma familia sozinha; mutirao como padrao)
// 5. AGROLOGIA (agricultura que regenera o solo, nao que o exaure)
//
// Author: OpenRepublic Team
// Transpilado fielmente do Python para Go (idiomatico com structs e metodos)

package main

import (
	"fmt"
	"sort"
	"strings"
)

// ============================================================================
// 1. ENUMS (todos os membros do Python preservados)
// ============================================================================

type TipoTenencia int

const (
	TIPO_TENENCIA_GUARDIAO_FAMILIAR TipoTenencia = iota
	TIPO_TENENCIA_COOPERATIVA
	TIPO_TENENCIA_COMUNIDADE_TRADICIONAL
	TIPO_TENENCIA_ASSENTAMENTO_COLETIVO
	TIPO_TENENCIA_RESERVA_REGENERACAO
	TIPO_TENENCIA_USO_PUBLICO
)

func (t TipoTenencia) String() string {
	return [...]string{
		"guardiao_familiar", "cooperativa", "comunidade_tradicional",
		"assentamento_coletivo", "reserva_regeneracao", "uso_publico",
	}[t]
}

func (t TipoTenencia) Rotulo() string {
	return [...]string{
		"Guardiao familiar", "Cooperativa agricola",
		"Comunidade tradicional (quilombo/ribeirinho/aldeia)",
		"Assentamento coletivo da Republica",
		"Reserva de regeneracao do solo (repouso)",
		"Uso publico (escola, enfermaria, mercado)",
	}[t]
}

func (t TipoTenencia) FamiliasMax() int {
	return [...]int{1, 5, 10, 8, 0, 0}[t]
}

type UsoSolo int

const (
	USO_SOLO_LAVOURA_ALIMENTACAO UsoSolo = iota
	USO_SOLO_LAVOURA_DIVERSIFICADA
	USO_SOLO_PASTAGEM_REGENERATIVA
	USO_SOLO_AGROFLORESTA
	USO_SOLO_HORTA_COMUNITARIA
	USO_SOLO_POMAR
	USO_SOLO_RESERVA_NATIVA
	USO_SOLO_CULTURA_TRADICIONAL
	USO_SOLO_INFRAESTRUTURA
	USO_SOLO_OCIOSO
)

func (u UsoSolo) String() string {
	return [...]string{
		"lavoura_alimentacao", "lavoura_diversificada", "pastagem_regenerativa",
		"agrofloresta", "horta_comunitaria", "pomar", "reserva_nativa",
		"cultura_tradicional", "infraestrutura", "ocioso",
	}[u]
}

func (u UsoSolo) Rotulo() string {
	return [...]string{
		"Lavoura de alimentos basicos", "Policultivo diversificado",
		"Pastagem rotativa regenerativa", "Sistema agroflorestal (SAF)",
		"Horta comunitaria de bairro", "Pomar frutifero",
		"Reserva de vegetacao nativa", "Cultivo tradicional ancestral",
		"Infraestrutura (casa, galpao, escola)", "Ocioso (sem funcao social)",
	}[u]
}

type StatusReforma int

const (
	STATUS_REFORMA_DIAGNOSTICO StatusReforma = iota
	STATUS_REFORMA_NOTIFICACAO
	STATUS_REFORMA_DESAPROPRIACAO
	STATUS_REFORMA_ASSENTAMENTO
	STATUS_REFORMA_REGULARIZACAO
	STATUS_REFORMA_CONSOLIDADO
	STATUS_REFORMA_CONFLITO
)

func (s StatusReforma) String() string {
	return [...]string{
		"diagnostico", "notificacao", "desapropriacao", "assentamento",
		"regularizacao", "consolidado", "conflito",
	}[s]
}

func (s StatusReforma) Rotulo() string {
	return [...]string{
		"Diagnostico fundiario em curso",
		"Latifundio notificado (funcao social cobrada)",
		"Desapropriacao decidida em assembleia",
		"Familias assentadas como guardias",
		"Regularizacao cooperativa ativa",
		"Territorio consolidado (auto-gestionario)",
		"Conflito fundiario ativo (grileiro/invasao)",
	}[s]
}

type TipoConflito int

const (
	TIPO_CONFLITO_GRILAGEM TipoConflito = iota
	TIPO_CONFLITO_INVASAO_LATIFUNDIO
	TIPO_CONFLITO_TRABALHO_ESCRAVO
	TIPO_CONFLITO_DESPEJO
	TIPO_CONFLITO_CONFLITO_FRONTEIRA
	TIPO_CONFLITO_MINERACAO_ILEGAL
	TIPO_CONFLITO_AGROTOXICO
	TIPO_CONFLITO_QUEIMADA_CRIMINOSA
)

func (t TipoConflito) String() string {
	return [...]string{
		"grilagem", "invasao_latifundio", "trabalho_escravo", "despejo",
		"conflito_fronteira", "mineracao_ilegal", "agrotoxico", "queimada_criminosa",
	}[t]
}

func (t TipoConflito) Rotulo() string {
	return [...]string{
		"Grilagem (falsificacao de titulo)",
		"Trabalhador expulso por latifundio",
		"Trabalho analogo a escravidao",
		"Despejo de familia guardi",
		"Disputa de fronteira entre comunidades",
		"Mineracao/predacao ilegal em terra guardia",
		"Contaminacao por agrotoxico vizinho",
		"Queimada criminosa / desmatamento",
	}[t]
}

func (t TipoConflito) Gravidade() int {
	return [...]int{4, 5, 5, 4, 2, 4, 3, 4}[t]
}

type TamanhoImovel int

const (
	TAMANHO_IMOVEL_MINIFUNDIO TamanhoImovel = iota
	TAMANHO_IMOVEL_PEQUENO
	TAMANHO_IMOVEL_MEDIO
	TAMANHO_IMOVEL_LATIFUNDIO_DIMENSAO
	TAMANHO_IMOVEL_LATIFUNDIO_EXPLORACAO
)

func (t TamanhoImovel) String() string {
	return [...]string{
		"minifundio", "pequeno", "medio", "latifundio_dimensao", "latifundio_exploracao",
	}[t]
}

func (t TamanhoImovel) Rotulo() string {
	return [...]string{
		"Minifundio (insuficiente, < 1 modulo)",
		"Pequena area (1-4 modulos)",
		"Media area (4-15 modulos)",
		"Latifundio por dimensao (>15 modulos)",
		"Latifundio por exploracao (ocioso/grilado)",
	}[t]
}

func (t TamanhoImovel) AreaMin() float64 {
	return [...]float64{0, 50, 200, 750, 0}[t]
}

func (t TamanhoImovel) AreaMax() float64 {
	return [...]float64{50, 200, 750, 99999, 99999}[t]
}

type FuncaoSocialStatus int

const (
	FUNCAO_SOCIAL_CUMPRE FuncaoSocialStatus = iota
	FUNCAO_SOCIAL_PARCIAL
	FUNCAO_SOCIAL_DESCUMPRE
)

func (f FuncaoSocialStatus) String() string {
	return [...]string{"cumpre", "parcial", "descumpre"}[f]
}

func (f FuncaoSocialStatus) Rotulo() string {
	return [...]string{"Cumpre funcao social", "Cumpre parcialmente", "Descumpre funcao social"}[f]
}

type PlanoAgrologia int

const (
	PLANO_AGROLOGIA_PLANTIO_DIRETO PlanoAgrologia = iota
	PLANO_AGROLOGIA_ADUBACAO_VERDE
	PLANO_AGROLOGIA_COMPOSTAGEM
	PLANO_AGROLOGIA_ROTACAO_CULTURAS
	PLANO_AGROLOGIA_CICLO_FECHADO
	PLANO_AGROLOGIA_AGROFLORESTA_SUCSSIONAL
	PLANO_AGROLOGIA_CAPTACAO_CHUVA
	PLANO_AGROLOGIA_BIOINSUMOS
	PLANO_AGROLOGIA_INTEGRACAO_ANIMAL
)

func (p PlanoAgrologia) String() string {
	return [...]string{
		"plantio_direto", "adubacao_verde", "compostagem", "rotacao_culturas",
		"ciclo_fechado", "agrofloresta_sucessional", "captacao_chuva", "bioinsumos",
		"integracao_animal",
	}[p]
}

func (p PlanoAgrologia) Rotulo() string {
	return [...]string{
		"Plantio direto (nao revolver solo)",
		"Adubacao verde (leguminosas)",
		"Compostagem comunitaria",
		"Rotacao de culturas",
		"Ciclo fechado (zero insumo externo)",
		"Agrofloresta sucessional",
		"Captacao de agua de chuva",
		"Bioinsumos (proibido agrotoxico sintetico)",
		"Integracao lavoura-pecuaria-floresta",
	}[p]
}

// ============================================================================
// 2. STRUCTS (dataclasses traduzidas fielmente)
// ============================================================================

type ImovelRural struct {
	ID                string
	Nome              string
	AreaHectares      float64
	Municipio         string
	Bioma             string
	TipoTenencia      TipoTenencia
	UsosSolo          []UsoSolo
	FamiliasGuardias  int
	FuncaoSocial      FuncaoSocialStatus
	ProdutividadePct  float64
	PlanoAgrologia    []PlanoAgrologia
	Status            StatusReforma
	HistoricoAntigo   string
}

type FamiliaGuardia struct {
	ID                     string
	NomeReferencia         string
	Pessoas                int
	ParcelaHectares        float64
	CooperativaID          string
	ChegadaDe              string
	ConhecimentoTradicional bool
}

type ConflitoFundiario struct {
	ID                string
	Tipo              TipoConflito
	TerritorioID      string
	Vitimas           int
	FamiliasAfetadas  int
	Descricao         string
	ResolucaoProposta string
	Resolvido         bool
}

type CooperativaAgricola struct {
	ID                       string
	Nome                     string
	FamiliaIDs               []string
	TerritorioIDs            []string
	ExcedenteDestino         string
	FerramentasCompartilhadas []string
}

type DiagnosticoFundiario struct {
	Territorio           string
	TotalArea            float64
	NumImoveis           int
	IndiceGini           float64
	PctAreaLatiFundio    float64
	FamiliasSemTerra     int
	FamiliasGuardias     int
	Veredito             string
}

// ============================================================================
// 3. ENGINE (ReformaAgrariaEngine com todos os metodos como receivers)
// ============================================================================

type ReformaAgrariaEngine struct {
	Imoveis        map[string]*ImovelRural
	Familias       map[string]*FamiliaGuardia
	Cooperativas   map[string]*CooperativaAgricola
	Conflitos      map[string]*ConflitoFundiario
	imID           int
	famID          int
	coopCounter    int
	confID         int
}

func NewReformaAgrariaEngine() *ReformaAgrariaEngine {
	return &ReformaAgrariaEngine{
		Imoveis:      make(map[string]*ImovelRural),
		Familias:     make(map[string]*FamiliaGuardia),
		Cooperativas: make(map[string]*CooperativaAgricola),
		Conflitos:    make(map[string]*ConflitoFundiario),
	}
}

func (e *ReformaAgrariaEngine) imovelID() string {
	e.imID++
	return fmt.Sprintf("TER-%04d", e.imID)
}

func (e *ReformaAgrariaEngine) familiaID() string {
	e.famID++
	return fmt.Sprintf("FAM-%04d", e.famID)
}

func (e *ReformaAgrariaEngine) coopID() string {
	e.coopCounter++
	return fmt.Sprintf("COOP-%04d", e.coopCounter)
}

func (e *ReformaAgrariaEngine) conflitoID() string {
	e.confID++
	return fmt.Sprintf("CONF-%04d", e.confID)
}

// CadastrarImovel (todos os campos)
func (e *ReformaAgrariaEngine) CadastrarImovel(nome string, area float64, municipio, bioma string,
	tipo TipoTenencia, usos []UsoSolo, familias int, funcao FuncaoSocialStatus,
	prod float64, planos []PlanoAgrologia, status StatusReforma, historico string) *ImovelRural {
	im := &ImovelRural{
		ID:               e.imovelID(),
		Nome:             nome,
		AreaHectares:     area,
		Municipio:        municipio,
		Bioma:            bioma,
		TipoTenencia:     tipo,
		UsosSolo:         usos,
		FamiliasGuardias: familias,
		FuncaoSocial:     funcao,
		ProdutividadePct: prod,
		PlanoAgrologia:   planos,
		Status:           status,
		HistoricoAntigo:  historico,
	}
	e.Imoveis[im.ID] = im
	return im
}

// CadastrarFamilia
func (e *ReformaAgrariaEngine) CadastrarFamilia(nome string, pessoas int, parcela float64,
	coopID, chegada string, trad bool) *FamiliaGuardia {
	f := &FamiliaGuardia{
		ID:                     e.familiaID(),
		NomeReferencia:         nome,
		Pessoas:                pessoas,
		ParcelaHectares:        parcela,
		CooperativaID:          coopID,
		ChegadaDe:              chegada,
		ConhecimentoTradicional: trad,
	}
	e.Familias[f.ID] = f
	return f
}

// CriarCooperativa
func (e *ReformaAgrariaEngine) CriarCooperativa(nome string, famIDs, terrIDs []string,
	excedente string, ferramentas []string) *CooperativaAgricola {
	c := &CooperativaAgricola{
		ID:                       e.coopID(),
		Nome:                     nome,
		FamiliaIDs:               append([]string{}, famIDs...),
		TerritorioIDs:            append([]string{}, terrIDs...),
		ExcedenteDestino:         excedente,
		FerramentasCompartilhadas: append([]string{}, ferramentas...),
	}
	e.Cooperativas[c.ID] = c
	for _, fid := range famIDs {
		if f, ok := e.Familias[fid]; ok {
			f.CooperativaID = c.ID
		}
	}
	return c
}

// RegistrarConflito
func (e *ReformaAgrariaEngine) RegistrarConflito(tipo TipoConflito, terrID string, vitimas, familias int, desc string) *ConflitoFundiario {
	c := &ConflitoFundiario{
		ID:               e.conflitoID(),
		Tipo:             tipo,
		TerritorioID:     terrID,
		Vitimas:          vitimas,
		FamiliasAfetadas: familias,
		Descricao:        desc,
		Resolvido:        false,
	}
	e.Conflitos[c.ID] = c
	return c
}

// ClassificarTamanho (todos os casos)
func (e *ReformaAgrariaEngine) ClassificarTamanho(area float64, ocioso bool) TamanhoImovel {
	if ocioso && area >= TamanhoImovel(TAMANHO_IMOVEL_PEQUENO).AreaMin() {
		return TAMANHO_IMOVEL_LATIFUNDIO_EXPLORACAO
	}
	for _, t := range []TamanhoImovel{TAMANHO_IMOVEL_MINIFUNDIO, TAMANHO_IMOVEL_PEQUENO, TAMANHO_IMOVEL_MEDIO, TAMANHO_IMOVEL_LATIFUNDIO_DIMENSAO} {
		if t.AreaMin() <= area && area < t.AreaMax() {
			return t
		}
	}
	return TAMANHO_IMOVEL_LATIFUNDIO_DIMENSAO
}

// IndiceGiniAreas (logica exata do Python)
func (e *ReformaAgrariaEngine) IndiceGiniAreas() float64 {
	areas := make([]float64, 0, len(e.Imoveis))
	for _, im := range e.Imoveis {
		areas = append(areas, im.AreaHectares)
	}
	n := len(areas)
	if n == 0 {
		return 0.0
	}
	total := 0.0
	for _, a := range areas {
		total += a
	}
	if total == 0 {
		return 0.0
	}
	sort.Float64s(areas)
	somaPond := 0.0
	for i, a := range areas {
		somaPond += float64(i+1) * a
	}
	gini := (2*somaPond)/(float64(n)*total) - (float64(n)+1)/float64(n)
	return float64(int(gini*10000)) / 10000
}

// Diagnosticar (fiel ao Python)
func (e *ReformaAgrariaEngine) Diagnosticar(territorio string) DiagnosticoFundiario {
	ims := make([]*ImovelRural, 0)
	for _, im := range e.Imoveis {
		if im.Municipio == territorio {
			ims = append(ims, im)
		}
	}
	totalArea := 0.0
	for _, im := range ims {
		totalArea += im.AreaHectares
	}
	num := len(ims)
	if num == 0 {
		return DiagnosticoFundiario{Territorio: territorio, Veredito: "Territorio vazio no cadastro."}
	}
	gini := e.IndiceGiniAreas()
	areaLat := 0.0
	for _, im := range ims {
		ocioso := im.FuncaoSocial == FUNCAO_SOCIAL_DESCUMPRE
		t := e.ClassificarTamanho(im.AreaHectares, ocioso)
		if t == TAMANHO_IMOVEL_LATIFUNDIO_DIMENSAO || t == TAMANHO_IMOVEL_LATIFUNDIO_EXPLORACAO {
			areaLat += im.AreaHectares
		}
	}
	pctLat := 0.0
	if totalArea > 0 {
		pctLat = areaLat / totalArea * 100.0
	}
	familiasG := 0
	for _, im := range ims {
		familiasG += im.FamiliasGuardias
	}
	famSemTerra := 0
	if pctLat > 0 && familiasG > 0 {
		famSemTerra = int((pctLat / 100.0) * float64(familiasG) / 4)
	}
	veredito := ""
	if gini > 0.7 || pctLat > 50 {
		veredito = "CONCENTRACAO CRITICA: revolicao agraria URGENTE."
	} else if gini > 0.4 || pctLat > 25 {
		veredito = "CONCENTRACAO ALTA: notificar latifundios, cobrar funcao social."
	} else if gini > 0.2 {
		veredito = "CONCENTRACAO MODERADA: regularizar e cooperativizar."
	} else {
		veredito = "TERRITORIO EQUITATIVO: consolidar cooperativas."
	}
	return DiagnosticoFundiario{
		Territorio:        territorio,
		TotalArea:         totalArea,
		NumImoveis:        num,
		IndiceGini:        gini,
		PctAreaLatiFundio: float64(int(pctLat*10)) / 10,
		FamiliasSemTerra:  famSemTerra,
		FamiliasGuardias:  familiasG,
		Veredito:          veredito,
	}
}

// AuditarFuncaoSocial (todos os 4 requisitos)
func (e *ReformaAgrariaEngine) AuditarFuncaoSocial(imovelID string) (FuncaoSocialStatus, []string) {
	im, ok := e.Imoveis[imovelID]
	if !ok {
		return FUNCAO_SOCIAL_DESCUMPRE, []string{"Imovel nao encontrado."}
	}
	faltas := []string{}
	if im.ProdutividadePct < 40 {
		faltas = append(faltas, fmt.Sprintf("Produtividade baixa (%.0f%% do potencial).", im.ProdutividadePct))
	}
	if len(im.PlanoAgrologia) == 0 {
		faltas = append(faltas, "Sem plano de agrologia (solo sendo exaurido).")
	}
	for _, conf := range e.Conflitos {
		if conf.Tipo == TIPO_CONFLITO_TRABALHO_ESCRAVO && conf.TerritorioID == im.ID && !conf.Resolvido {
			faltas = append(faltas, "Trabalho analogo a escravidao detectado (BLOQUEANTE).")
			break
		}
	}
	if im.FamiliasGuardias == 0 && im.TipoTenencia != TIPO_TENENCIA_RESERVA_REGENERACAO {
		faltas = append(faltas, "Nenhuma familia guardia: terra abandonada.")
	}
	if len(faltas) > 0 {
		if len(faltas) == 1 {
			im.FuncaoSocial = FUNCAO_SOCIAL_PARCIAL
		} else {
			im.FuncaoSocial = FUNCAO_SOCIAL_DESCUMPRE
		}
	} else {
		im.FuncaoSocial = FUNCAO_SOCIAL_CUMPRE
	}
	return im.FuncaoSocial, faltas
}

// NotificarLatiFundio
func (e *ReformaAgrariaEngine) NotificarLatiFundio(imovelID string) string {
	im, ok := e.Imoveis[imovelID]
	if !ok {
		return ""
	}
	ocioso := im.FuncaoSocial == FUNCAO_SOCIAL_DESCUMPRE
	tam := e.ClassificarTamanho(im.AreaHectares, ocioso)
	if tam != TAMANHO_IMOVEL_LATIFUNDIO_DIMENSAO && tam != TAMANHO_IMOVEL_LATIFUNDIO_EXPLORACAO {
		return fmt.Sprintf("%s nao e latifundio (%s).", im.ID, tam.Rotulo())
	}
	st, faltas := e.AuditarFuncaoSocial(im.ID)
	if st == FUNCAO_SOCIAL_CUMPRE {
		im.Status = STATUS_REFORMA_REGULARIZACAO
		return fmt.Sprintf("%s cumpre funcao social -> regularizar como cooperativa.", im.ID)
	}
	im.Status = STATUS_REFORMA_NOTIFICACAO
	return fmt.Sprintf("NOTIFICADO %s (%s, %.0f ha). Faltas: %s. Prazo para regularizar.",
		im.ID, tam.Rotulo(), im.AreaHectares, strings.Join(faltas, "; "))
}

// Desaproropriar (todos os passos)
func (e *ReformaAgrariaEngine) Desaproropriar(imovelID string, famIDs []string) string {
	im, ok := e.Imoveis[imovelID]
	if !ok {
		return ""
	}
	if im.Status != STATUS_REFORMA_NOTIFICACAO && im.Status != STATUS_REFORMA_DIAGNOSTICO {
		return fmt.Sprintf("%s em status %s -- nao elegivel para desapropriacao agora.", im.ID, im.Status.Rotulo())
	}
	if im.HistoricoAntigo == "" {
		im.HistoricoAntigo = im.Nome
	}
	im.Nome = fmt.Sprintf("Territorio Livre %s", im.ID)
	im.TipoTenencia = TIPO_TENENCIA_ASSENTAMENTO_COLETIVO
	if len(famIDs) > 0 {
		parcela := im.AreaHectares / float64(len(famIDs))
		for _, fid := range famIDs {
			if f, ok := e.Familias[fid]; ok {
				f.ParcelaHectares = float64(int(parcela*100)) / 100
				f.ChegadaDe = "assentamento"
			}
		}
		im.FamiliasGuardias = len(famIDs)
	}
	im.Status = STATUS_REFORMA_ASSENTAMENTO
	im.FuncaoSocial = FUNCAO_SOCIAL_PARCIAL
	return fmt.Sprintf("DESAPROPRIVADO %s: %d familias guardias assentadas, %.0f ha sob cuidado coletivo.",
		im.ID, len(famIDs), im.AreaHectares)
}

// ConsolidarCooperativa
func (e *ReformaAgrariaEngine) ConsolidarCooperativa(nome string, terrIDs, famIDs []string, excedente string, ferramentas []string) *CooperativaAgricola {
	coop := e.CriarCooperativa(nome, famIDs, terrIDs, excedente, ferramentas)
	for _, tid := range terrIDs {
		if im, ok := e.Imoveis[tid]; ok {
			im.TipoTenencia = TIPO_TENENCIA_COOPERATIVA
			im.Status = STATUS_REFORMA_CONSOLIDADO
			im.FuncaoSocial = FUNCAO_SOCIAL_CUMPRE
		}
	}
	return coop
}

// ConflitosPorGravidade
func (e *ReformaAgrariaEngine) ConflitosPorGravidade() []*ConflitoFundiario {
	list := make([]*ConflitoFundiario, 0, len(e.Conflitos))
	for _, c := range e.Conflitos {
		list = append(list, c)
	}
	sort.Slice(list, func(i, j int) bool {
		if list[i].Tipo.Gravidade() != list[j].Tipo.Gravidade() {
			return list[i].Tipo.Gravidade() > list[j].Tipo.Gravidade()
		}
		return list[i].FamiliasAfetadas > list[j].FamiliasAfetadas
	})
	return list
}

// ResolverConflito
func (e *ReformaAgrariaEngine) ResolverConflito(confID, resolucao string) bool {
	if c, ok := e.Conflitos[confID]; ok {
		c.ResolucaoProposta = resolucao
		c.Resolvido = true
		return true
	}
	return false
}

// Metricas
func (e *ReformaAgrariaEngine) AreaTotal() float64 {
	t := 0.0
	for _, im := range e.Imoveis {
		t += im.AreaHectares
	}
	return t
}

func (e *ReformaAgrariaEngine) AreaOciosa() float64 {
	t := 0.0
	for _, im := range e.Imoveis {
		if im.FuncaoSocial == FUNCAO_SOCIAL_DESCUMPRE {
			t += im.AreaHectares
		}
	}
	return t
}

func (e *ReformaAgrariaEngine) FamiliasAtendidas() int {
	t := 0
	for _, im := range e.Imoveis {
		t += im.FamiliasGuardias
	}
	return t
}

func (e *ReformaAgrariaEngine) Scorecard() map[string]interface{} {
	return map[string]interface{}{
		"imoveis_cadastrados": len(e.Imoveis),
		"area_total_ha":       fmt.Sprintf("%.1f", e.AreaTotal()),
		"area_ociosa_ha":      fmt.Sprintf("%.1f", e.AreaOciosa()),
		"pct_ociosa":          fmt.Sprintf("%.1f", func() float64 {
			if e.AreaTotal() == 0 {
				return 0
			}
			return e.AreaOciosa() / e.AreaTotal() * 100
		}()),
		"familias_guardias": e.FamiliasAtendidas(),
		"cooperativas":      len(e.Cooperativas),
		"conflitos_abertos": func() int {
			c := 0
			for _, cf := range e.Conflitos {
				if !cf.Resolvido {
					c++
				}
			}
			return c
		}(),
		"indice_gini":  e.IndiceGiniAreas(),
		"consolidados": func() int {
			c := 0
			for _, im := range e.Imoveis {
				if im.Status == STATUS_REFORMA_CONSOLIDADO {
					c++
				}
			}
			return c
		}(),
	}
}

// ============================================================================
// 4. DEMO (fiel ao Python, saida equivalente)
// ============================================================================

func main() {
	e := NewReformaAgrariaEngine()

	fmt.Println("======================================================================")
	fmt.Println("OpenAgrarianRevolution -- A Terra e de Quem a Cuida")
	fmt.Println("======================================================================")

	latif := e.CadastrarImovel("Fazenda Boa Vista (ex-latifundio)", 2500.0, "Sertao do Sao Francisco", "caatinga",
		TIPO_TENENCIA_GUARDIAO_FAMILIAR, []UsoSolo{USO_SOLO_PASTAGEM_REGENERATIVA, USO_SOLO_OCIOSO}, 3,
		FUNCAO_SOCIAL_DESCUMPRE, 15.0, []PlanoAgrologia{}, STATUS_REFORMA_DIAGNOSTICO, "Familia herdeira de titulo duvidoso")

	pequeno := e.CadastrarImovel("Sitio Aconchego", 30.0, "Sertao do Sao Francisco", "caatinga",
		TIPO_TENENCIA_GUARDIAO_FAMILIAR, []UsoSolo{USO_SOLO_LAVOURA_ALIMENTACAO, USO_SOLO_POMAR}, 1,
		FUNCAO_SOCIAL_PARCIAL, 70.0, []PlanoAgrologia{PLANO_AGROLOGIA_COMPOSTAGEM, PLANO_AGROLOGIA_ROTACAO_CULTURAS},
		STATUS_REFORMA_DIAGNOSTICO, "")

	reserva := e.CadastrarImovel("Reserva Caatinga Viva", 800.0, "Sertao do Sao Francisco", "caatinga",
		TIPO_TENENCIA_RESERVA_REGENERACAO, []UsoSolo{USO_SOLO_RESERVA_NATIVA}, 0,
		FUNCAO_SOCIAL_CUMPRE, 0.0, []PlanoAgrologia{PLANO_AGROLOGIA_CICLO_FECHADO},
		STATUS_REFORMA_DIAGNOSTICO, "")

	diag := e.Diagnosticar("Sertao do Sao Francisco")
	fmt.Printf("\n[DIAGNOSTICO] %s\n", diag.Territorio)
	fmt.Printf("  Area total: %.0f ha | Imoveis: %d\n", diag.TotalArea, diag.NumImoveis)
	fmt.Printf("  Indice de Gini: %.3f (0=igual, 1=concentrado)\n", diag.IndiceGini)
	fmt.Printf("  %% area em latifundios: %.1f%%\n", diag.PctAreaLatiFundio)
	fmt.Printf("  Familias guardias: %d\n", diag.FamiliasGuardias)
	fmt.Printf("  VEREDITO: %s\n", diag.Veredito)

	fmt.Println("\n[NOTIFICACAO]")
	msg := e.NotificarLatiFundio(latif.ID)
	fmt.Printf("  %s\n", msg)

	fmt.Println("\n[AUDITORIA DE FUNCAO SOCIAL]")
	for _, iid := range []string{latif.ID, pequeno.ID, reserva.ID} {
		st, faltas := e.AuditarFuncaoSocial(iid)
		im := e.Imoveis[iid]
		fmt.Printf("  %s (%s): %s\n", iid, im.Nome[:min(30, len(im.Nome))], st.Rotulo())
		for _, f := range faltas {
			fmt.Printf("      - %s\n", f)
		}
	}

	conf := e.RegistrarConflito(TIPO_CONFLITO_TRABALHO_ESCRAVO, latif.ID, 2, 8, "Trabalhadores resgatados em condicoes analogas a escravidao.")
	fmt.Printf("\n[CONFLITO REGISTRADO] %s: %s\n", conf.ID, conf.Tipo.Rotulo())
	fmt.Printf("  Gravidade: %d/5 | Familias afetadas: %d\n", conf.Tipo.Gravidade(), conf.FamiliasAfetadas)

	fmt.Println("\n[DESAPROPRIACAO POR ASSEMBLEIA]")
	f1 := e.CadastrarFamilia("Familia Maria das Dores", 5, 0.0, "", "despejado", false)
	f2 := e.CadastrarFamilia("Familia Jose Pereira", 4, 0.0, "", "despejado", false)
	f3 := e.CadastrarFamilia("Familia Ana Beatriz", 6, 0.0, "", "voluntario", false)
	f4 := e.CadastrarFamilia("Familia Severino", 5, 0.0, "", "despejado", true)
	res := e.Desaproropriar(latif.ID, []string{f1.ID, f2.ID, f3.ID, f4.ID})
	fmt.Printf("  %s\n", res)

	e.ResolverConflito(conf.ID, "Ex-dono removido; familias guardias assumem; recuperacao das vitimas via OpenPsychologyReparation.")
	fmt.Printf("  Conflito %s resolvido: %s\n", conf.ID, conf.ResolucaoProposta)

	fmt.Println("\n[CONSOLIDACAO COOPERATIVA]")
	coop := e.ConsolidarCooperativa("Cooperativa Terra Livre Sertao", []string{latif.ID},
		[]string{f1.ID, f2.ID, f3.ID, f4.ID}, "mercado_aberto",
		[]string{"trator_compartilhado", "casa_de_farinha", "cisterna_coletiva"})
	fmt.Printf("  %s: %s\n", coop.ID, coop.Nome)
	fmt.Printf("  Familias: %d | Territorios: %d\n", len(coop.FamiliaIDs), len(coop.TerritorioIDs))
	fmt.Printf("  Ferramentas compartilhadas: %s\n", strings.Join(coop.FerramentasCompartilhadas, ", "))

	latif.UsosSolo = []UsoSolo{USO_SOLO_AGROFLORESTA, USO_SOLO_LAVOURA_DIVERSIFICADA, USO_SOLO_POMAR}
	latif.PlanoAgrologia = []PlanoAgrologia{PLANO_AGROLOGIA_AGROFLORESTA_SUCSSIONAL, PLANO_AGROLOGIA_CAPTACAO_CHUVA, PLANO_AGROLOGIA_BIOINSUMOS, PLANO_AGROLOGIA_CICLO_FECHADO}
	latif.ProdutividadePct = 65.0
	stFinal, _ := e.AuditarFuncaoSocial(latif.ID)
	fmt.Printf("\n[POS-REVOLUCAO] %s funcao social: %s\n", latif.ID, stFinal.Rotulo())
	fmt.Printf("  Status: %s | Tenencia: %s\n", latif.Status.Rotulo(), latif.TipoTenencia.Rotulo())

	fmt.Println("\n" + strings.Repeat("=", 70))
	fmt.Println("[SCORECARD DA REVOLUCAO AGRARIA]")
	fmt.Println(strings.Repeat("=", 70))
	sc := e.Scorecard()
	for k, v := range sc {
		fmt.Printf("  %s %v\n", k+":", v)
	}

	fmt.Println("\n[CONFLITOS POR GRAVIDADE]")
	for _, c := range e.ConflitosPorGravidade() {
		flag := "OK"
		if !c.Resolvido {
			flag = "ABERTO"
		}
		fmt.Printf("  [%s] %s %s (grav=%d) vitimas=%d familias=%d\n",
			flag, c.ID, c.Tipo.Rotulo(), c.Tipo.Gravidade(), c.Vitimas, c.FamiliasAfetadas)
	}

	fmt.Println("\n" + strings.Repeat("=", 70))
	fmt.Println("FILOSOFIA -- Por que a Republica ABOLI a propriedade da terra")
	fmt.Println(strings.Repeat("=", 70))
	fmt.Println(`P1 (Anti-elitismo): O latifundio e o mecanismo ORIGINAL de elite.
P2 (Autonomia): Quem planta colhe. Quem cuida decide.
P3 (Trabalho = impacto): Dono de terra nao e trabalho. E RENDA.
P4 (Democracia): A assembleia do territorio decide o uso da terra.
A REVOLUCAO AGRARIA NAO E "REFORMA". E ABOLICAO.`)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
