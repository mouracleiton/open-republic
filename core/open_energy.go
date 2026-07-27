// open_energy.go
// Transpilacao fiel de open_energy.py para Go
// OpenEnergy -- Energia Gratuita para Todo e Qualquer Uso
// Comentarios e strings em Portugues (conforme fonte)

package main

import (
	"fmt"
	"time"
)

// ============================================================================
// 1. ENUMS (const iota + maps) - transpilacao fiel completa
// ============================================================================

type FonteEnergia int

const (
	FONTE_SOLAR FonteEnergia = iota
	FONTE_EOLICA
	FONTE_HIDRO
	FONTE_GEOTERMICA
	FONTE_BIOMASSA
	FONTE_MARES
	FONTE_NUCLEAR
	FONTE_FUSAO
)

var fontesInfo = map[FonteEnergia]struct {
	rotulo   string
	renovavel bool
}{
	FONTE_SOLAR:     {"Solar fotovoltaica", true},
	FONTE_EOLICA:    {"Eolica (vento)", true},
	FONTE_HIDRO:     {"Hidroeletrica", true},
	FONTE_GEOTERMICA: {"Geotermica", true},
	FONTE_BIOMASSA:  {"Biomassa", true},
	FONTE_MARES:     {"Das mars e correntes", true},
	FONTE_NUCLEAR:   {"Nuclear (fissao)", false},
	FONTE_FUSAO:     {"Fusao nuclear (futura)", true},
}

type TipoConsumo int

const (
	CONSUMO_ESSENCIAL_VIDA TipoConsumo = iota
	CONSUMO_SAUDE
	CONSUMO_COMUNICACAO
	CONSUMO_EDUCACAO
	CONSUMO_MOBILIDADE
	CONSUMO_PRODUCAO_ALIMENTOS
	CONSUMO_INFRAESTRUTURA_COMUM
	CONSUMO_PRODUCAO_BENS
	CONSUMO_CULTURA_LAZER
	CONSUMO_PESQUISA_INOVACAO
	CONSUMO_RESIDENCIAL_EXCEDENTE
)

var consumosInfo = map[TipoConsumo]struct {
	rotulo     string
	prioridade int
}{
	CONSUMO_ESSENCIAL_VIDA:       {"Essencial a vida (cozinhar, aquecer, iluminar, agua)", 1},
	CONSUMO_SAUDE:                {"Saude (hospitais, clinicas, equipamentos medicos)", 1},
	CONSUMO_COMUNICACAO:          {"Comunicacao (internet, telefone, radio)", 1},
	CONSUMO_EDUCACAO:             {"Educacao (escolas, bibliotecas, laboratorios)", 2},
	CONSUMO_MOBILIDADE:           {"Mobilidade (transporte publico, veiculos)", 2},
	CONSUMO_PRODUCAO_ALIMENTOS:   {"Producao de alimentos (irrigacao, processamento)", 2},
	CONSUMO_INFRAESTRUTURA_COMUM: {"Infraestrutura comum (agua, esgoto, iluminacao publica)", 2},
	CONSUMO_PRODUCAO_BENS:        {"Producao de bens (fabril, artesanal)", 3},
	CONSUMO_CULTURA_LAZER:        {"Cultura e lazer (teatro, musica, esporte)", 3},
	CONSUMO_PESQUISA_INOVACAO:    {"Pesquisa e inovacao (laboratorios, computacao)", 3},
	CONSUMO_RESIDENCIAL_EXCEDENTE: {"Residencial excedente (alem do essencial)", 4},
}

type TipoArmazenamento int

const (
	ARMAZ_BATERIA_LITIO TipoArmazenamento = iota
	ARMAZ_BATERIA_SODIO
	ARMAZ_BATERIA_FLUXO
	ARMAZ_HIDRO_BOMBEADA
	ARMAZ_GRAVIDADE
	ARMAZ_HIDROGENIO
	ARMAZ_AR_COMPRIMIDO
	ARMAZ_TERMICO
)

var armazenamentosInfo = map[TipoArmazenamento]string{
	ARMAZ_BATERIA_LITIO:    "Bateria de litio-ion",
	ARMAZ_BATERIA_SODIO:    "Bateria de sodio (mais barato, menos denso)",
	ARMAZ_BATERIA_FLUXO:    "Bateria de fluxo redox (escala grid)",
	ARMAZ_HIDRO_BOMBEADA:   "Hidroeletrica reversivel (bombeada)",
	ARMAZ_GRAVIDADE:        "Armazenamento por gravidade (pesos)",
	ARMAZ_HIDROGENIO:       "Hidrogenio verde (eletrolise)",
	ARMAZ_AR_COMPRIMIDO:    "Ar comprimido (CAES)",
	ARMAZ_TERMICO:          "Armazenamento termico (sal fundido, agua quente)",
}

type StatusCenario int

const (
	CENARIO_ABUNDANCIA StatusCenario = iota
	CENARIO_EQUILIBRIO
	CENARIO_ATENCAO
	CENARIO_ESCASSEZ
	CENARIO_EMERGENCIA
)

var cenariosInfo = map[StatusCenario]string{
	CENARIO_ABUNDANCIA: "Abundancia: geracao supera demanda",
	CENARIO_EQUILIBRIO: "Equilibrio: geracao = demanda",
	CENARIO_ATENCAO:    "Atencao: margem baixa (<10%)",
	CENARIO_ESCASSEZ:   "Escassez: demanda supera geracao",
	CENARIO_EMERGENCIA: "Emergencia: deficit critico, assembleia decide",
}

type StatusInterconexao int

const (
	INTER_ILHADO StatusInterconexao = iota
	INTER_CONECTADO
	INTER_EXPORTANDO
	INTER_IMPORTANDO
	INTER_MANUTENCAO
)

var interconexoesInfo = map[StatusInterconexao]string{
	INTER_ILHADO:      "Ilhado: microgrid autonomo (sem conexao externa)",
	INTER_CONECTADO:   "Conectado a rede regional",
	INTER_EXPORTANDO:  "Exportando excedente (doacao)",
	INTER_IMPORTANDO:  "Importando (recebendo doacao)",
	INTER_MANUTENCAO:  "Em manutencao",
}

// ============================================================================
// 2. DATACLASSES (structs)
// ============================================================================

type UnidadeGeracao struct {
	ID                 string
	Fonte              FonteEnergia
	CapacidadeKW       float64
	ProducaoAtualKW    float64
	ComunidadeID       string
	Status             string
	SustentabilidadePct float64
}

type UnidadeArmazenamento struct {
	ID            string
	Tipo          TipoArmazenamento
	CapacidadeKWH float64
	CargaAtualKWH float64
	ComunidadeID  string
	CiclosVida    int
}

type ConsumoRegistrado struct {
	ID              string
	ComunidadeID    string
	Tipo            TipoConsumo
	ConsumoKW       float64
	Timestamp       string
	CidadaoOuSetor  string
}

type Microgrid struct {
	ID                    string
	Nome                  string
	ComunidadeID          string
	UnidadesGeracao       []string
	UnidadesArmazenamento []string
	Interconexao          StatusInterconexao
	AutonomiaHoras        float64
	GeracaoTotalKW        float64
	DemandaTotalKW        float64
	Cenario               StatusCenario
}

type AlocacaoEscassez struct {
	ID                      string
	MicrogridID             string
	DeficitKW               float64
	TiposPriorizados        []TipoConsumo
	TiposRotacionados       []TipoConsumo
	TiposSuprimidos         []TipoConsumo
	DuracaoEstimadaH        float64
	AprovadoEmAssembleia    bool
	Justificativa           string
}

// ============================================================================
// 3. ENGINE (struct + metodos receiver)
// ============================================================================

type EnergiaEngine struct {
	geracao       map[string]UnidadeGeracao
	armazenamento map[string]UnidadeArmazenamento
	consumos      []ConsumoRegistrado
	microgrids    map[string]Microgrid
	alocacoes     map[string]AlocacaoEscassez
	genID         int
	armID         int
	consID        int
	mgID          int
	alocID        int
}

func NewEnergiaEngine() *EnergiaEngine {
	return &EnergiaEngine{
		geracao:       make(map[string]UnidadeGeracao),
		armazenamento: make(map[string]UnidadeArmazenamento),
		microgrids:    make(map[string]Microgrid),
		alocacoes:     make(map[string]AlocacaoEscassez),
	}
}

func (e *EnergiaEngine) genNovoID() string {
	e.genID++
	return fmt.Sprintf("GEN-%04d", e.genID)
}
func (e *EnergiaEngine) armNovoID() string {
	e.armID++
	return fmt.Sprintf("ARM-%04d", e.armID)
}
func (e *EnergiaEngine) consNovoID() string {
	e.consID++
	return fmt.Sprintf("CON-%04d", e.consID)
}
func (e *EnergiaEngine) mgNovoID() string {
	e.mgID++
	return fmt.Sprintf("GRID-%04d", e.mgID)
}
func (e *EnergiaEngine) alocNovoID() string {
	e.alocID++
	return fmt.Sprintf("ALOC-%04d", e.alocID)
}

// Cadastros
func (e *EnergiaEngine) CadastrarGeracao(fonte FonteEnergia, capacidadeKW, producaoAtualKW float64, comunidadeID string, sustentabilidadePct float64) UnidadeGeracao {
	u := UnidadeGeracao{
		ID:                 e.genNovoID(),
		Fonte:              fonte,
		CapacidadeKW:       capacidadeKW,
		ProducaoAtualKW:    producaoAtualKW,
		ComunidadeID:       comunidadeID,
		Status:             "operacional",
		SustentabilidadePct: sustentabilidadePct,
	}
	e.geracao[u.ID] = u
	return u
}

func (e *EnergiaEngine) CadastrarArmazenamento(tipo TipoArmazenamento, capacidadeKWH, cargaAtualKWH float64, comunidadeID string, ciclosVida int) UnidadeArmazenamento {
	a := UnidadeArmazenamento{
		ID:            e.armNovoID(),
		Tipo:          tipo,
		CapacidadeKWH: capacidadeKWH,
		CargaAtualKWH: cargaAtualKWH,
		ComunidadeID:  comunidadeID,
		CiclosVida:    ciclosVida,
	}
	e.armazenamento[a.ID] = a
	return a
}

func (e *EnergiaEngine) RegistrarConsumo(comunidadeID string, tipo TipoConsumo, consumoKW float64, cidadaoOuSetor string) ConsumoRegistrado {
	c := ConsumoRegistrado{
		ID:             e.consNovoID(),
		ComunidadeID:   comunidadeID,
		Tipo:           tipo,
		ConsumoKW:      consumoKW,
		Timestamp:      time.Now().Format(time.RFC3339),
		CidadaoOuSetor: cidadaoOuSetor,
	}
	e.consumos = append(e.consumos, c)
	return c
}

func (e *EnergiaEngine) CriarMicrogrid(nome, comunidadeID string, unidadesGeracao, unidadesArmazenamento []string, interconexao StatusInterconexao) Microgrid {
	mg := Microgrid{
		ID:                    e.mgNovoID(),
		Nome:                  nome,
		ComunidadeID:          comunidadeID,
		UnidadesGeracao:       append([]string{}, unidadesGeracao...),
		UnidadesArmazenamento: append([]string{}, unidadesArmazenamento...),
		Interconexao:          interconexao,
	}
	e.microgrids[mg.ID] = mg
	e.atualizarMetricasMicrogrid(mg.ID)
	return mg
}

// Atualizacao de metricas (logica completa)
func (e *EnergiaEngine) atualizarMetricasMicrogrid(mgID string) {
	mg, ok := e.microgrids[mgID]
	if !ok {
		return
	}
	geracao := 0.0
	for _, gid := range mg.UnidadesGeracao {
		if g, exists := e.geracao[gid]; exists {
			geracao += g.ProducaoAtualKW
		}
	}
	demanda := 0.0
	for _, c := range e.consumos {
		if c.ComunidadeID == mg.ComunidadeID {
			demanda += c.ConsumoKW
		}
	}
	mg.GeracaoTotalKW = float64(int(geracao*100)) / 100
	mg.DemandaTotalKW = float64(int(demanda*100)) / 100
	if demanda == 0 {
		mg.Cenario = CENARIO_ABUNDANCIA
		e.microgrids[mgID] = mg
		return
	}
	margem := (geracao - demanda) / demanda
	if margem >= 0.2 {
		mg.Cenario = CENARIO_ABUNDANCIA
	} else if margem >= 0.0 {
		mg.Cenario = CENARIO_EQUILIBRIO
	} else if margem >= -0.1 {
		mg.Cenario = CENARIO_ATENCAO
	} else if margem >= -0.3 {
		mg.Cenario = CENARIO_ESCASSEZ
	} else {
		mg.Cenario = CENARIO_EMERGENCIA
	}
	armazenamentoTotal := 0.0
	for _, aid := range mg.UnidadesArmazenamento {
		if a, exists := e.armazenamento[aid]; exists {
			armazenamentoTotal += a.CargaAtualKWH
		}
	}
	if demanda > 0 {
		mg.AutonomiaHoras = float64(int((armazenamentoTotal/demanda)*100)) / 100
	} else {
		mg.AutonomiaHoras = 0
	}
	e.microgrids[mgID] = mg
}

// Diagnostico completo
func (e *EnergiaEngine) DiagnosticarMicrogrid(mgID string) (StatusCenario, map[string]interface{}) {
	e.atualizarMetricasMicrogrid(mgID)
	mg, ok := e.microgrids[mgID]
	if !ok {
		return CENARIO_EQUILIBRIO, map[string]interface{}{"erro": "Microgrid nao encontrada"}
	}
	deficit := 0.0
	if mg.DemandaTotalKW > mg.GeracaoTotalKW {
		deficit = mg.DemandaTotalKW - mg.GeracaoTotalKW
	}
	excedente := 0.0
	if mg.GeracaoTotalKW > mg.DemandaTotalKW {
		excedente = mg.GeracaoTotalKW - mg.DemandaTotalKW
	}
	renovavel := 0.0
	for _, gid := range mg.UnidadesGeracao {
		if g, exists := e.geracao[gid]; exists && fontesInfo[g.Fonte].renovavel {
			renovavel += g.ProducaoAtualKW
		}
	}
	pctRenovavel := 0.0
	if mg.GeracaoTotalKW > 0 {
		pctRenovavel = float64(int((renovavel/mg.GeracaoTotalKW*100)*10)) / 10
	}
	info := map[string]interface{}{
		"geracao_kw":    mg.GeracaoTotalKW,
		"demanda_kw":    mg.DemandaTotalKW,
		"deficit_kw":    float64(int(deficit*100)) / 100,
		"excedente_kw":  float64(int(excedente*100)) / 100,
		"autonomia_h":   mg.AutonomiaHoras,
		"pct_renovavel": pctRenovavel,
		"interconexao":  interconexoesInfo[mg.Interconexao],
	}
	return mg.Cenario, info
}

// Propor alocacao em escassez (logica completa)
func (e *EnergiaEngine) ProporAlocacaoEscassez(mgID string, duracaoEstimadaH float64) *AlocacaoEscassez {
	mg, ok := e.microgrids[mgID]
	if !ok {
		return nil
	}
	e.atualizarMetricasMicrogrid(mgID)
	if mg.Cenario != CENARIO_ESCASSEZ && mg.Cenario != CENARIO_EMERGENCIA {
		return nil
	}
	deficit := mg.DemandaTotalKW - mg.GeracaoTotalKW
	if deficit <= 0 {
		return nil
	}
	consumoPorTipo := make(map[TipoConsumo]float64)
	for _, c := range e.consumos {
		if c.ComunidadeID == mg.ComunidadeID {
			consumoPorTipo[c.Tipo] += c.ConsumoKW
		}
	}
	// Ordenar por prioridade
	var tiposOrdenados []TipoConsumo
	for p := 1; p <= 4; p++ {
		for t := CONSUMO_ESSENCIAL_VIDA; t <= CONSUMO_RESIDENCIAL_EXCEDENTE; t++ {
			if consumosInfo[t].prioridade == p {
				if _, has := consumoPorTipo[t]; has {
					tiposOrdenados = append(tiposOrdenados, t)
				}
			}
		}
	}
	geracaoDisponivel := mg.GeracaoTotalKW
	var priorizados, rotacionados, suprimidos []TipoConsumo
	for _, tipo := range tiposOrdenados {
		cons := consumoPorTipo[tipo]
		if geracaoDisponivel >= cons {
			priorizados = append(priorizados, tipo)
			geracaoDisponivel -= cons
		} else if geracaoDisponivel > 0 {
			rotacionados = append(rotacionados, tipo)
			geracaoDisponivel = 0
		} else {
			suprimidos = append(suprimidos, tipo)
		}
	}
	aloc := &AlocacaoEscassez{
		ID:                   e.alocNovoID(),
		MicrogridID:          mgID,
		DeficitKW:            float64(int(deficit*100)) / 100,
		TiposPriorizados:     priorizados,
		TiposRotacionados:    rotacionados,
		TiposSuprimidos:      suprimidos,
		DuracaoEstimadaH:     duracaoEstimadaH,
		AprovadoEmAssembleia: false,
		Justificativa:        fmt.Sprintf("Deficit de %.1f kW. Geracao alocada por prioridade: essenciais garantidos, nao-essenciais em rodizio/corte. Ninguem fica sem energia essencial por dinheiro (P1).", deficit),
	}
	e.alocacoes[aloc.ID] = *aloc
	return aloc
}

func (e *EnergiaEngine) AprovarAlocacao(alocID string) bool {
	if a, ok := e.alocacoes[alocID]; ok {
		a.AprovadoEmAssembleia = true
		e.alocacoes[alocID] = a
		return true
	}
	return false
}

// Doacao P2P
func (e *EnergiaEngine) DoarExcedente(mgOrigemID, mgDestinoID string) float64 {
	e.atualizarMetricasMicrogrid(mgOrigemID)
	e.atualizarMetricasMicrogrid(mgDestinoID)
	origem := e.microgrids[mgOrigemID]
	destino := e.microgrids[mgDestinoID]
	excedente := origem.GeracaoTotalKW - origem.DemandaTotalKW
	deficit := destino.DemandaTotalKW - destino.GeracaoTotalKW
	if excedente <= 0 || deficit <= 0 {
		return 0
	}
	doado := excedente
	if deficit < doado {
		doado = deficit
	}
	origem.Interconexao = INTER_EXPORTANDO
	destino.Interconexao = INTER_IMPORTANDO
	origem.GeracaoTotalKW = float64(int((origem.GeracaoTotalKW - doado)*100)) / 100
	destino.GeracaoTotalKW = float64(int((destino.GeracaoTotalKW + doado)*100)) / 100
	e.microgrids[mgOrigemID] = origem
	e.microgrids[mgDestinoID] = destino
	e.atualizarMetricasMicrogrid(mgOrigemID)
	e.atualizarMetricasMicrogrid(mgDestinoID)
	return float64(int(doado*10)) / 10
}

// Auditoria de eficiencia
func (e *EnergiaEngine) AuditoriaEficiencia(comunidadeID string) map[string]interface{} {
	consumosCom := []ConsumoRegistrado{}
	for _, c := range e.consumos {
		if c.ComunidadeID == comunidadeID {
			consumosCom = append(consumosCom, c)
		}
	}
	if len(consumosCom) == 0 {
		return map[string]interface{}{"comunidade": comunidadeID, "consumo_total_kw": 0, "alertas": []string{}}
	}
	consumoTotal := 0.0
	for _, c := range consumosCom {
		consumoTotal += c.ConsumoKW
	}
	consumoPorTipo := make(map[TipoConsumo]float64)
	for _, c := range consumosCom {
		consumoPorTipo[c.Tipo] += c.ConsumoKW
	}
	alertas := []string{}
	for t, val := range consumoPorTipo {
		if t == CONSUMO_RESIDENCIAL_EXCEDENTE && val > consumoTotal*0.3 {
			alertas = append(alertas, fmt.Sprintf("Consumo residencial excedente alto (%.1f kW, %.0f%% do total). Lembrar: eficiencia liberta capacidade para a comunidade.", val, val/consumoTotal*100))
		}
		if t == CONSUMO_PRODUCAO_BENS && val > consumoTotal*0.4 {
			alertas = append(alertas, fmt.Sprintf("Producao de bens consome %.1f kW. Otimizar processos = mais capacidade para saude e educacao.", val))
		}
	}
	porTipoStr := map[string]float64{}
	for t, v := range consumoPorTipo {
		porTipoStr[consumosInfo[t].rotulo] = float64(int(v*10)) / 10
	}
	return map[string]interface{}{
		"comunidade":          comunidadeID,
		"consumo_total_kw":    float64(int(consumoTotal*100)) / 100,
		"consumo_por_tipo":    porTipoStr,
		"alertas_eficiencia":  alertas,
		"mensagem":            "Energia e gratuita. Eficiencia nao economiza dinheiro -- LIBERTA capacidade para quem precisa. E kaizen civico.",
	}
}

// Scorecard
func (e *EnergiaEngine) Scorecard() map[string]interface{} {
	geracaoTotal := 0.0
	renovavel := 0.0
	for _, g := range e.geracao {
		geracaoTotal += g.ProducaoAtualKW
		if fontesInfo[g.Fonte].renovavel {
			renovavel += g.ProducaoAtualKW
		}
	}
	demandaTotal := 0.0
	for _, c := range e.consumos {
		demandaTotal += c.ConsumoKW
	}
	armazenamentoTotal := 0.0
	for _, a := range e.armazenamento {
		armazenamentoTotal += a.CargaAtualKWH
	}
	doacoes := 0
	for _, mg := range e.microgrids {
		if mg.Interconexao == INTER_EXPORTANDO {
			doacoes++
		}
	}
	pctRen := 0.0
	if geracaoTotal > 0 {
		pctRen = float64(int((renovavel/geracaoTotal*100)*10)) / 10
	}
	return map[string]interface{}{
		"unidades_geracao":       len(e.geracao),
		"unidades_armazenamento": len(e.armazenamento),
		"microgrids":             len(e.microgrids),
		"geracao_total_kw":       float64(int(geracaoTotal*10)) / 10,
		"demanda_total_kw":       float64(int(demandaTotal*10)) / 10,
		"excedente_kw":           float64(int((geracaoTotal - demandaTotal)*10)) / 10,
		"pct_renovavel":          pctRen,
		"armazenamento_kwh":      float64(int(armazenamentoTotal*10)) / 10,
		"alocacoes_escassez":     len(e.alocacoes),
		"doacoes_realizadas":     doacoes,
	}
}

// ============================================================================
// 4. DEMO (main completo)
// ============================================================================

func main() {
	e := NewEnergiaEngine()
	fmt.Println("======================================================================")
	fmt.Println("OpenEnergy -- Energia Gratuita para Todo e Qualquer Uso")
	fmt.Println("======================================================================")

	// CENARIO 1
	fmt.Println("\n[CENARIO 1] Solar Village -- abundancia (geracao > demanda)")
	g1 := e.CadastrarGeracao(FONTE_SOLAR, 500.0, 480.0, "solar_village", 100.0)
	g2 := e.CadastrarGeracao(FONTE_EOLICA, 300.0, 250.0, "solar_village", 100.0)
	a1 := e.CadastrarArmazenamento(ARMAZ_BATERIA_LITIO, 2000.0, 1500.0, "solar_village", 10000)
	a2 := e.CadastrarArmazenamento(ARMAZ_BATERIA_FLUXO, 5000.0, 4000.0, "solar_village", 10000)
	e.RegistrarConsumo("solar_village", CONSUMO_ESSENCIAL_VIDA, 120.0, "")
	e.RegistrarConsumo("solar_village", CONSUMO_SAUDE, 40.0, "")
	e.RegistrarConsumo("solar_village", CONSUMO_COMUNICACAO, 30.0, "")
	e.RegistrarConsumo("solar_village", CONSUMO_EDUCACAO, 50.0, "")
	e.RegistrarConsumo("solar_village", CONSUMO_CULTURA_LAZER, 80.0, "")
	e.RegistrarConsumo("solar_village", CONSUMO_RESIDENCIAL_EXCEDENTE, 100.0, "")
	mg1 := e.CriarMicrogrid("Solar Village Grid", "solar_village", []string{g1.ID, g2.ID}, []string{a1.ID, a2.ID}, INTER_CONECTADO)
	c1, info1 := e.DiagnosticarMicrogrid(mg1.ID)
	fmt.Printf("  Geracao: %.2f kW | Demanda: %.2f kW\n", info1["geracao_kw"], info1["demanda_kw"])
	fmt.Printf("  Excedente: %.2f kW | Renovavel: %.1f%%\n", info1["excedente_kw"], info1["pct_renovavel"])
	fmt.Printf("  Autonomia (ilhado): %.2fh\n", info1["autonomia_h"])
	fmt.Printf("  Cenario: %s\n", cenariosInfo[c1])
	fmt.Println("  Energia para QUALQUER uso: sim, sem conta, sem medidor de cobranca.")

	// CENARIO 2
	fmt.Println("\n[CENARIO 2] Vale Seco -- escassez (seca reduziu hidro)")
	g3 := e.CadastrarGeracao(FONTE_HIDRO, 400.0, 150.0, "vale_seco", 100.0)
	g4 := e.CadastrarGeracao(FONTE_SOLAR, 200.0, 180.0, "vale_seco", 100.0)
	a3 := e.CadastrarArmazenamento(ARMAZ_HIDROGENIO, 3000.0, 800.0, "vale_seco", 10000)
	e.RegistrarConsumo("vale_seco", CONSUMO_ESSENCIAL_VIDA, 100.0, "")
	e.RegistrarConsumo("vale_seco", CONSUMO_SAUDE, 60.0, "")
	e.RegistrarConsumo("vale_seco", CONSUMO_COMUNICACAO, 20.0, "")
	e.RegistrarConsumo("vale_seco", CONSUMO_EDUCACAO, 40.0, "")
	e.RegistrarConsumo("vale_seco", CONSUMO_PRODUCAO_BENS, 80.0, "")
	e.RegistrarConsumo("vale_seco", CONSUMO_CULTURA_LAZER, 50.0, "")
	mg2 := e.CriarMicrogrid("Vale Seco Grid", "vale_seco", []string{g3.ID, g4.ID}, []string{a3.ID}, INTER_CONECTADO)
	c2, info2 := e.DiagnosticarMicrogrid(mg2.ID)
	fmt.Printf("  Geracao: %.2f kW | Demanda: %.2f kW\n", info2["geracao_kw"], info2["demanda_kw"])
	fmt.Printf("  Deficit: %.2f kW | Cenario: %s\n", info2["deficit_kw"], cenariosInfo[c2])
	fmt.Printf("  Autonomia: %.2fh\n", info2["autonomia_h"])

	// ALOCACAO
	fmt.Println("\n[ALOCACAO DEMOCRATICA EM ESCASSEZ]")
	aloc := e.ProporAlocacaoEscassez(mg2.ID, 48.0)
	if aloc != nil {
		fmt.Printf("  Proposta %s (assembleia precisa aprovar):\n", aloc.ID)
		fmt.Printf("  Deficit: %.2f kW | Duracao estimada: %.1fh\n", aloc.DeficitKW, aloc.DuracaoEstimadaH)
		fmt.Print("  GARANTIDOS (prioridade): ")
		for _, t := range aloc.TiposPriorizados {
			fmt.Printf("%s; ", consumosInfo[t].rotulo)
		}
		fmt.Print("\n  EM RODIZIO: ")
		for _, t := range aloc.TiposRotacionados {
			fmt.Printf("%s; ", consumosInfo[t].rotulo)
		}
		fmt.Print("\n  SUPRIMIDOS: ")
		for _, t := range aloc.TiposSuprimidos {
			fmt.Printf("%s; ", consumosInfo[t].rotulo)
		}
		fmt.Printf("\n  Justificativa: %s\n", aloc.Justificativa)
		e.AprovarAlocacao(aloc.ID)
		fmt.Printf("  Aprovado em assembleia: %v\n", aloc.AprovadoEmAssembleia)
	}

	// DOACAO P2P
	fmt.Println("\n[DOACAO P2P] Solar Village doe excedente para Vale Seco")
	doado := e.DoarExcedente(mg1.ID, mg2.ID)
	if doado > 0 {
		fmt.Printf("  %.1f kW doados (sem dinheiro, sem cobranca).\n", doado)
		_, infoPos := e.DiagnosticarMicrogrid(mg2.ID)
		fmt.Printf("  Vale Seco pos-doacao: geracao=%.2f kW, deficit=%.2f kW, cenario=%s\n", infoPos["geracao_kw"], infoPos["deficit_kw"], infoPos["interconexao"])
	}

	// AUDITORIA
	fmt.Println("\n[AUDITORIA DE EFICIENCIA -- dever civico, nao economia]")
	aud := e.AuditoriaEficiencia("solar_village")
	fmt.Printf("  Comunidade: %s\n", aud["comunidade"])
	fmt.Printf("  Consumo total: %.2f kW\n", aud["consumo_total_kw"])
	for k, v := range aud["consumo_por_tipo"].(map[string]float64) {
		fmt.Printf("    %s: %.1f kW\n", k, v)
	}
	for _, alerta := range aud["alertas_eficiencia"].([]string) {
		fmt.Printf("  ALERTA: %s\n", alerta)
	}
	fmt.Println("  ", aud["mensagem"])

	// SCORECARD
	fmt.Println("\n" + "======================================================================")
	fmt.Println("[SCORECARD ENERGETICO DA REPUBLICA]")
	fmt.Println("======================================================================")
	sc := e.Scorecard()
	for k, v := range sc {
		fmt.Printf("  %s %v\n", k, v)
	}

	// FONTES
	fmt.Println("\n[FONTES DE ENERGIA DA REPUBLICA]")
	for f := FONTE_SOLAR; f <= FONTE_FUSAO; f++ {
		flag := "renovavel"
		if !fontesInfo[f].renovavel {
			flag = "NAO-renovavel"
		}
		fmt.Printf("  %s [ %s ]\n", fontesInfo[f].rotulo, flag)
	}

	// FILOSOFIA
	fmt.Println("\n" + "======================================================================")
	fmt.Println("FILOSOFIA -- Por que energia e gratuita para todo e qualquer uso")
	fmt.Println("======================================================================")
	fmt.Println(`ENERGIA NAO E MERCADORIA. E CONDICAO DE VIDA.
Cozinhar precisa de energia. Aquecer precisa de energia.
Curar precisa de energia. Comunicar precisa de energia.
Estudar precisa de energia. Criar precisa de energia.
Cobrar por energia e cobrar por EXISTIR.

O ARGUMENTO DA ESCASSEZ (e por que e falso):
O capitalismo diz: "se energia e gratis, todos desperdicam."
Falso. O capitalista desperdica porque o custo e EXTERNO ao lucro.
O cidadao da Republica SABE que a energia que desperdica falta para o vizinho.
Eficiencia nao economiza dinheiro -- LIBERTA capacidade para a comunidade.

A UNICA ESCASSEZ REAL (e como se resolve):
Quando a geracao nao cobre a demanda (seca, falha), a assembleia decide:
1. Essenciais (vida, saude, comunicacao) SEMPRE garantidos.
2. Nao-essenciais em rodizio democratico.
3. Ninguem fica sem energia por DINHEIRO. So por PRIORIDADE civica.
4. A solucao de longo prazo e GERAR MAIS, nao racionar.
O capitalismo raciona por preco (quem tem dinheiro usa, quem nao tem corta).
A Republica aloca por prioridade (todos tem o essencial, o resto e civico).

A REVOLUCAO ENERGETICA:
1. Cada comunidade gera a propria energia (geracao distribuida).
2. Excedente e DOADO, nao vendido (P2P, sem intermediario).
3. Armazenamento comunitario (baterias compartilhadas).
4. 100% renovavel (a Republica respeita o planeta que a sustenta).
5. Nucleo essencial garantido para TODOS, sem excecao, sem condicao.
6. "Para todo e qualquer uso" -- a Republica nao pergunta PARA QUE.
   Pergunta quanto voce PRECISA, e garante que tem.

A ENERGIA E O AR DA CIVILIZACAO.
Ninguem cobra pelo ar. Ninguem deve cobrar pela energia.
`)
}