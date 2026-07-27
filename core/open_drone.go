// OpenDrone -- P10: Soberania Aerea Civica
// =========================================
// O decimo principio constitucional da Republica Aberta.
//
// "O ceu nao e de ninguem. Portanto, e de todos." -- principio do espaco aereo
// como bem comum, analogo ao principio da terra (OpenAgrarianRevolution):
// guardiao, nao dono.
//
// DISTINCAO CRITICA (a tese do modulo):
// - Drones (VANTs -- Veiculos Aereos Nao Tripulados) sao INFRAESTRUTURA.
// - Como toda infraestrutura na Republica, pertencem ao dominio publico e
//   servem a P1 (erradicar miserabilidade), nao a vigilancia, nem a lucro,
//   nem a guerra.
// - Um ceu cheio de drones comerciais entregando pacotes de consumo enquanto
//   criancas passam fome e um monumento a distopia. OpenDrone transforma o
//   espaco aereo em bem comum civico.
//
// TRES PROIBICOES CONSTITUCIONAIS (o triplo NAO):
// 1. NAO VIGIA: drones com camera de vigilancia sao PROIBIDOS. Camera so para
//    navegacao (feed local, nao gravado, nao transmitido para central).
// 2. NAO MATA: drones nao podem carregar armas. Ponto. Sem excecoes. Um drone
//    armado nao e drone -- e arma. E arma pertence ao museu da Republica.
// 3. NAO ESPIONA: drones nao coletam dados pessoais. Entregam suprimentos,
//    nao metadados. O trajeto de voo e publico; o destinatario e privado.
//
// USOS PERMITIDOS (missao civica):
// - Entrega de suprimentos (medicamentos, alimentos, agua) a areas isoladas
// - Mapeamento ambiental (desmatamento, queimadas, qualidade da agua)
// - Busca e resgate em desastres naturais
// - Conectividade aerea (rede mesh em areas sem cobertura)
// - Inspecao de infraestrutura critica (diques, barragens, pontes)
//
// GATE DE MISSAO (P10):
// Toda missao de drone deve passar por um gate antes de decolar:
// - Proposito civico declarado e aprovado
// - Zona de voo geofenceada (nao sobrevoa residencia privada sem consentimento)
// - Log publico (trajeto, duracao, proposito)
// - Razao de rejeicao explicita se negada
//
// ALINHAMENTO CONSTITUCIONAL:
// - P1: Drones que entregam medicamentos em area isolada combatem miserabilidade.
//       Drones que entregam propaganda ampliam miserabilidade. P10 escolhe.
// - P2: Drones que vigiam destroem autonomia. Drone que entrega remedio amplia
//       autonomia (acesso). O instrumento nao e neutro -- o USO define.
// - P4: Espaco aereo e decisao coletiva. Nenhuma corporacao o ocupa sozinha.
// - P8: Drone autonomo e IA que atua no mundo fisico. Se ampliar inteligencia/
//       reduzir miserabilidade = cumpre P8. Se vigiar = viola P8.
//
// Author: OpenRepublic Team
// Versao Go transpilada fielmente do Python (open_drone.py)

package main

import (
	"fmt"
	"math"
	"strings"
	"time"
)

// ============================================================================
// 1. ENUMS (modulo-level, nunca aninhados)
// ============================================================================

type TipoMissao int

const (
	TIPO_ENTREGA_SUPRIMENTOS TipoMissao = iota
	TIPO_MAPEAMENTO_AMBIENTAL
	TIPO_BUSCA_RESGATE
	TIPO_CONECTIVIDADE
	TIPO_INSPECAO_INFRA
	TIPO_AGRICULTURA_CIVICA
)

func (t TipoMissao) ID() string {
	return []string{
		"entrega_suprimentos",
		"mapeamento_ambiental",
		"busca_resgate",
		"conectividade",
		"inspecao_infra",
		"agricultura_civica",
	}[t]
}

func (t TipoMissao) Rotulo() string {
	return []string{
		"Entrega de suprimentos (remedio, comida, agua)",
		"Mapeamento ambiental (desmatamento, queimadas)",
		"Busca e resgate em desastre natural",
		"Rede mesh aerea (area sem cobertura)",
		"Inspecao de infraestrutura critica",
		"Agricultura de precisao comunitaria",
	}[t]
}

func (t TipoMissao) Prioridade() int {
	return []int{1, 1, 0, 1, 1, 2}[t]
}

type StatusMissao int

const (
	STATUS_PLANEJADA StatusMissao = iota
	STATUS_APROVADA
	STATUS_EM_VOO
	STATUS_CONCLUIDA
	STATUS_REJEITADA
	STATUS_CANCELADA
	STATUS_FALHOU
)

func (s StatusMissao) ID() string {
	return []string{
		"planejada",
		"aprovada",
		"em_voo",
		"concluida",
		"rejeitada",
		"cancelada",
		"falhou",
	}[s]
}

func (s StatusMissao) Rotulo() string {
	return []string{
		"Planejada (aguardando aprovacao do gate)",
		"Aprovada pelo gate P10",
		"Em voo (executando)",
		"Concluida com sucesso",
		"Rejeitada pelo gate P10",
		"Cancelada (emergencia ou erro)",
		"Falhou (perda de sinal, aterrissagem forcada)",
	}[s]
}

type TipoProibicao int

const (
	PROIB_VIGILANCIA TipoProibicao = iota
	PROIB_ARMAMENTO
	PROIB_ESPIONAGEM
	PROIB_PRIVADO_SEM_CONSENTIMENTO
	PROIB_COMERCIAL_NAO_CIVICO
)

func (p TipoProibicao) ID() string {
	return []string{
		"vigilancia",
		"armamento",
		"espionagem",
		"privado_sem_consentimento",
		"comercial_nao_civico",
	}[p]
}

func (p TipoProibicao) Rotulo() string {
	return []string{
		"Camera de vigilancia (feed gravado/transmitido)",
		"Carrega arma ou explosivo",
		"Coleta dados pessoais (facial, placa, biometria)",
		"Sobrevoa area privada sem consentimento",
		"Uso comercial sem proposito civico (propaganda)",
	}[p]
}

func (p TipoProibicao) Gravidade() int {
	return []int{5, 5, 5, 4, 3}[p]
}

type VereditoGate int

const (
	VEREDITO_APROVADA VereditoGate = iota
	VEREDITO_APROVADA_COM_RESTRICOES
	VEREDITO_REJEITADA
	VEREDITO_BLOQUEADA
)

func (v VereditoGate) ID() string {
	return []string{
		"aprovada",
		"aprovada_restricoes",
		"rejeitada",
		"bloqueada",
	}[v]
}

func (v VereditoGate) Rotulo() string {
	return []string{
		"Missao aprovada: proposito civico confirmado",
		"Aprovada com restricoes (geofence ampliado)",
		"Missao rejeitada: viola uma proibicao P10",
		"Missao bloqueada: e vetor de vigilancia/arma",
	}[v]
}

type PrioridadeCorredor int

const (
	PRIO_RESGATE_VIDA PrioridadeCorredor = iota
	PRIO_ENTREGA_CRITICA
	PRIO_MAPEAMENTO_AMBIENTAL
	PRIO_CONECTIVIDADE
	PRIO_INSPECAO
	PRIO_OUTROS
)

func (p PrioridadeCorredor) ID() string {
	return []string{
		"resgate_vida",
		"entrega_critica",
		"mapeamento",
		"conectividade",
		"inspecao",
		"outros",
	}[p]
}

func (p PrioridadeCorredor) Rotulo() string {
	return []string{
		"Resgate de vida (emergencia medica)",
		"Entrega critica (remedio urgente)",
		"Mapeamento ambiental de rotina",
		"Conectividade mesh",
		"Inspecao de infraestrutura",
		"Outros usos civicos",
	}[p]
}

func (p PrioridadeCorredor) Prioridade() int {
	return []int{0, 1, 2, 2, 3, 4}[p]
}

// ============================================================================
// 2. STRUCTS
// ============================================================================

type Coordenada struct {
	Lat float64
	Lon float64
}

type ZonaVoo struct {
	ID                   string
	Centro               Coordenada
	RaioMetros           float64
	Descricao            string
	SobrevoaPrivado      bool
	ConsentimentoPrivado bool
}

type Drone struct {
	ID                    string
	Modelo                string
	AutonomiaMinutos      int
	CargaMaxKg            float64
	TemCameraNavegacao    bool
	TemCameraVigilancia   bool
	TemArmamento          bool
	ColetaDadosPessoais   bool
	Ativo                 bool
	MissoesConcluidas     int
}

type MissaoDrone struct {
	ID                string
	DroneID           string
	Tipo              TipoMissao
	Descricao         string
	Zona              *ZonaVoo
	Destino           *Coordenada
	CargaDescricao    string
	Urgencia          bool
	Status            StatusMissao
	VereditoGate      *VereditoGate
	RazaoRejeicao     string
	ProibicoesVioladas []TipoProibicao
	CriadaEm          string
	ConcluidaEm       string
	LogTrajeto        []Coordenada
}

type LogVoo struct {
	MissaoID       string
	DroneID        string
	TipoMissao     string
	DuracaoMinutos float64
	DistanciaKm    float64
	Decolagem      string
	Pouso          string
	DestinoLat     *float64
	DestinoLon     *float64
	Sucesso        bool
	Observacoes    string
}

type MetricaFrota struct {
	RegiaoID            string
	TotalDrones         int
	DronesAtivos        int
	MissoesConcluidas   int
	MissoesRejeitadas   int
	EntregasCriticas    int
	Resgates            int
	HorasVoo            float64
	ViolacoesDetectadas int
	CoberturaKm2        float64
}

// ============================================================================
// 3. TABELAS
// ============================================================================

var DESCRICOES_PROIBICOES = map[string]string{
	"vigilancia": ("Camera de vigilancia = feed gravado ou transmitido para central de " +
		"monitoramento. PERMITIDO: camera de navegacao (feed local em tempo real, " +
		"nao gravado, processado no proprio drone). A linha e: a camera ajuda o " +
		"drone a voar, nao ajuda o Estado a vigiar."),
	"armamento": ("Qualquer arma, explosivo, ou dispositivo projetado para causar dano " +
		"fisico. Um drone armado nao e drone -- e arma. Armas pertencem ao museu " +
		"da Republica (P7). Sem excecoes, mesmo para 'defesa'."),
	"espionagem": ("Reconhecimento facial, leitura de placas, coleta de biometria, captura " +
		"de dados de rede (wifi bluetooth scanning). O drone entrega suprimentos; " +
		"NAO entrega metadados sobre o destinatario."),
	"privado_sem_consentimento": ("Sobrevoar residencia, patio, ou propriedade privada sem consentimento " +
		"explicito do morador. Excecao: resgate de vida (P1 > privacidade), mas " +
		"o log fica publico e auditavel."),
	"comercial_nao_civico": ("Uso para entrega de consumo de luxo, propaganda, marketing, ou qualquer " +
		"fim que nao reduza miserabilidade ou amplie acesso. Drones nao sao " +
		"brinquedo de consumo -- sao infraestrutura de sobrevivencia."),
}

var PRIORIDADE_POR_TIPO = map[string]int{
	"busca_resgate":       0,
	"entrega_suprimentos": 1,
	"mapeamento_ambiental": 2,
	"conectividade":        2,
	"inspecao_infra":       3,
	"agricultura_civica":   3,
}

// ============================================================================
// 4. ENGINE
// ============================================================================

type DroneCivicoEngine struct {
	Drones    map[string]*Drone
	Missoes   map[string]*MissaoDrone
	Zonas     map[string]*ZonaVoo
	Logs      []LogVoo
	_droneID  int
	_missaoID int
	_zonaID   int
}

func NewDroneCivicoEngine() *DroneCivicoEngine {
	return &DroneCivicoEngine{
		Drones:  make(map[string]*Drone),
		Missoes: make(map[string]*MissaoDrone),
		Zonas:   make(map[string]*ZonaVoo),
		Logs:    []LogVoo{},
	}
}

func (e *DroneCivicoEngine) droneIDNovo() string {
	e._droneID++
	return fmt.Sprintf("DRONE-%04d", e._droneID)
}

func (e *DroneCivicoEngine) missaoIDNovo() string {
	e._missaoID++
	return fmt.Sprintf("MISSAO-%04d", e._missaoID)
}

func (e *DroneCivicoEngine) zonaIDNovo() string {
	e._zonaID++
	return fmt.Sprintf("ZONA-%04d", e._zonaID)
}

func (e *DroneCivicoEngine) RegistrarZona(centro Coordenada, raioMetros float64, descricao string, sobrevoaPrivado, consentimentoPrivado bool) *ZonaVoo {
	z := &ZonaVoo{
		ID:                   e.zonaIDNovo(),
		Centro:               centro,
		RaioMetros:           raioMetros,
		Descricao:            descricao,
		SobrevoaPrivado:      sobrevoaPrivado,
		ConsentimentoPrivado: consentimentoPrivado,
	}
	e.Zonas[z.ID] = z
	return z
}

func (e *DroneCivicoEngine) RegistrarDrone(modelo string, autonomiaMinutos int, cargaMaxKg float64, temCameraNavegacao, temCameraVigilancia, temArmamento, coletaDadosPessoais bool) *Drone {
	d := &Drone{
		ID:                  e.droneIDNovo(),
		Modelo:              modelo,
		AutonomiaMinutos:    autonomiaMinutos,
		CargaMaxKg:          cargaMaxKg,
		TemCameraNavegacao:  temCameraNavegacao,
		TemCameraVigilancia: temCameraVigilancia,
		TemArmamento:        temArmamento,
		ColetaDadosPessoais: coletaDadosPessoais,
		Ativo:               true,
	}
	if temCameraVigilancia || temArmamento || coletaDadosPessoais {
		d.Ativo = false
	}
	e.Drones[d.ID] = d
	return d
}

func (e *DroneCivicoEngine) RegistrarMissao(droneID string, tipo TipoMissao, descricao string, zona *ZonaVoo, destino *Coordenada, cargaDescricao string, urgencia bool) *MissaoDrone {
	m := &MissaoDrone{
		ID:             e.missaoIDNovo(),
		DroneID:        droneID,
		Tipo:           tipo,
		Descricao:      descricao,
		Zona:           zona,
		Destino:        destino,
		CargaDescricao: cargaDescricao,
		Urgencia:       urgencia,
		Status:         STATUS_PLANEJADA,
		CriadaEm:       time.Now().Format(time.RFC3339),
	}
	e.Missoes[m.ID] = m
	return m
}

func (e *DroneCivicoEngine) AuditarProibicoes(missao *MissaoDrone) []TipoProibicao {
	violacoes := []TipoProibicao{}
	drone := e.Drones[missao.DroneID]
	if drone == nil {
		return []TipoProibicao{PROIB_COMERCIAL_NAO_CIVICO}
	}
	if drone.TemArmamento {
		violacoes = append(violacoes, PROIB_ARMAMENTO)
	}
	if drone.TemCameraVigilancia {
		violacoes = append(violacoes, PROIB_VIGILANCIA)
	}
	if drone.ColetaDadosPessoais {
		violacoes = append(violacoes, PROIB_ESPIONAGEM)
	}
	if missao.Zona.SobrevoaPrivado && !missao.Zona.ConsentimentoPrivado {
		if missao.Tipo != TIPO_BUSCA_RESGATE {
			violacoes = append(violacoes, PROIB_PRIVADO_SEM_CONSENTIMENTO)
		}
	}
	if e.verificarUsoComercial(missao) {
		violacoes = append(violacoes, PROIB_COMERCIAL_NAO_CIVICO)
	}
	missao.ProibicoesVioladas = violacoes
	return violacoes
}

func (e *DroneCivicoEngine) verificarUsoComercial(missao *MissaoDrone) bool {
	palavras := []string{"propaganda", "marketing", "publicidade", "luxo", "brinde", "promocional", "black friday", "desconto", "vitrine"}
	texto := strings.ToLower(missao.Descricao + " " + missao.CargaDescricao)
	for _, p := range palavras {
		if strings.Contains(texto, p) {
			return true
		}
	}
	return false
}

func (e *DroneCivicoEngine) AprovarMissao(missaoID string) (VereditoGate, string) {
	missao := e.Missoes[missaoID]
	if missao == nil {
		return VEREDITO_REJEITADA, "Missao nao encontrada"
	}
	violacoes := e.AuditarProibicoes(missao)
	drone := e.Drones[missao.DroneID]

	gravidadeMax := 0
	for _, v := range violacoes {
		if v.Gravidade() > gravidadeMax {
			gravidadeMax = v.Gravidade()
		}
	}
	if gravidadeMax >= 5 {
		missao.VereditoGate = newVeredito(VEREDITO_BLOQUEADA)
		missao.Status = STATUS_REJEITADA
		labels := []string{}
		for _, v := range violacoes {
			labels = append(labels, v.Rotulo())
		}
		missao.RazaoRejeicao = fmt.Sprintf("MISSAO BLOQUEADA: viola proibicao constitucional P10 -- %s", strings.Join(labels, ", "))
		return *missao.VereditoGate, missao.RazaoRejeicao
	}
	if len(violacoes) > 0 {
		missao.VereditoGate = newVeredito(VEREDITO_REJEITADA)
		missao.Status = STATUS_REJEITADA
		labels := []string{}
		for _, v := range violacoes {
			labels = append(labels, v.Rotulo())
		}
		missao.RazaoRejeicao = fmt.Sprintf("Missao rejeitada: %s", strings.Join(labels, ", "))
		return *missao.VereditoGate, missao.RazaoRejeicao
	}
	if drone != nil {
		dist := e.estimarDistancia(missao)
		nec := (dist / 30.0) * 60
		if nec > float64(drone.AutonomiaMinutos) {
			missao.VereditoGate = newVeredito(VEREDITO_APROVADA_COM_RESTRICOES)
			missao.Status = STATUS_APROVADA
			missao.RazaoRejeicao = fmt.Sprintf("Aprovada com restricoes: autonomia marginal (%.0fmin necessaria vs %dmin disponivel)", nec, drone.AutonomiaMinutos)
			return *missao.VereditoGate, missao.RazaoRejeicao
		}
	}
	missao.VereditoGate = newVeredito(VEREDITO_APROVADA)
	missao.Status = STATUS_APROVADA
	return *missao.VereditoGate, "Missao aprovada pelo gate P10"
}

func newVeredito(v VereditoGate) *VereditoGate { return &v }

func (e *DroneCivicoEngine) estimarDistancia(missao *MissaoDrone) float64 {
	return (missao.Zona.RaioMetros / 1000.0) * 2.0
}

func (e *DroneCivicoEngine) Decolar(missaoID string) bool {
	missao := e.Missoes[missaoID]
	if missao == nil || missao.Status != STATUS_APROVADA {
		return false
	}
	missao.Status = STATUS_EM_VOO
	return true
}

func (e *DroneCivicoEngine) ConcluirMissao(missaoID string, duracaoMinutos, distanciaKm float64, sucesso bool, observacoes string) *LogVoo {
	missao := e.Missoes[missaoID]
	if missao == nil || missao.Status != STATUS_EM_VOO {
		return nil
	}
	if sucesso {
		missao.Status = STATUS_CONCLUIDA
	} else {
		missao.Status = STATUS_FALHOU
	}
	missao.ConcluidaEm = time.Now().Format(time.RFC3339)
	drone := e.Drones[missao.DroneID]
	if drone != nil && sucesso {
		drone.MissoesConcluidas++
	}
	var lat, lon *float64
	if missao.Destino != nil {
		lat = &missao.Destino.Lat
		lon = &missao.Destino.Lon
	}
	log := LogVoo{
		MissaoID:       missao.ID,
		DroneID:        missao.DroneID,
		TipoMissao:     missao.Tipo.ID(),
		DuracaoMinutos: duracaoMinutos,
		DistanciaKm:    distanciaKm,
		Decolagem:      missao.CriadaEm,
		Pouso:          missao.ConcluidaEm,
		DestinoLat:     lat,
		DestinoLon:     lon,
		Sucesso:        sucesso,
		Observacoes:    observacoes,
	}
	e.Logs = append(e.Logs, log)
	return &log
}

func (e *DroneCivicoEngine) ResolverConflitoCorredor(aID, bID string) *string {
	ma := e.Missoes[aID]
	mb := e.Missoes[bID]
	if ma == nil || mb == nil {
		return nil
	}
	priA := PRIORIDADE_POR_TIPO[ma.Tipo.ID()]
	priB := PRIORIDADE_POR_TIPO[mb.Tipo.ID()]
	if ma.Urgencia && !mb.Urgencia {
		return &ma.ID
	}
	if mb.Urgencia && !ma.Urgencia {
		return &mb.ID
	}
	if priA < priB {
		return &ma.ID
	}
	if priB < priA {
		return &mb.ID
	}
	return nil
}

func (e *DroneCivicoEngine) MedirFrota(regiaoID string) MetricaFrota {
	total := len(e.Drones)
	ativos := 0
	for _, d := range e.Drones {
		if d.Ativo {
			ativos++
		}
	}
	concluidas, rejeitadas, entregas, resgates := 0, 0, 0, 0
	for _, m := range e.Missoes {
		if m.Status == STATUS_CONCLUIDA {
			concluidas++
			if m.Tipo == TIPO_ENTREGA_SUPRIMENTOS {
				entregas++
			}
			if m.Tipo == TIPO_BUSCA_RESGATE {
				resgates++
			}
		}
		if m.Status == STATUS_REJEITADA {
			rejeitadas++
		}
	}
	horas := 0.0
	for _, l := range e.Logs {
		horas += l.DuracaoMinutos
	}
	horas /= 60.0
	viol := 0
	for _, m := range e.Missoes {
		viol += len(m.ProibicoesVioladas)
	}
	cob := 0.0
	for _, z := range e.Zonas {
		cob += z.RaioMetros * z.RaioMetros * math.Pi
	}
	cob /= 1_000_000
	return MetricaFrota{
		RegiaoID:            regiaoID,
		TotalDrones:         total,
		DronesAtivos:        ativos,
		MissoesConcluidas:   concluidas,
		MissoesRejeitadas:   rejeitadas,
		EntregasCriticas:    entregas,
		Resgates:            resgates,
		HorasVoo:            math.Round(horas*10) / 10,
		ViolacoesDetectadas: viol,
		CoberturaKm2:        math.Round(cob*100) / 100,
	}
}

func (e *DroneCivicoEngine) Scorecard() map[string]interface{} {
	f := e.MedirFrota("default")
	taxa := 0.0
	den := f.MissoesConcluidas + f.MissoesRejeitadas
	if den > 0 {
		taxa = math.Round(float64(f.MissoesConcluidas)/float64(den)*1000) / 10
	}
	return map[string]interface{}{
		"drones_registrados":   f.TotalDrones,
		"drones_ativos":        f.DronesAtivos,
		"drones_bloqueados":    f.TotalDrones - f.DronesAtivos,
		"missoes_concluidas":   f.MissoesConcluidas,
		"missoes_rejeitadas":   f.MissoesRejeitadas,
		"entregas_criticas":    f.EntregasCriticas,
		"resgates_realizados":  f.Resgates,
		"horas_voo_total":      f.HorasVoo,
		"violacoes_detectadas": f.ViolacoesDetectadas,
		"cobertura_km2":        f.CoberturaKm2,
		"taxa_aprovacao":       fmt.Sprintf("%.1f%%", taxa),
	}
}

// ============================================================================
// 5. MAIN (demo)
// ============================================================================

func main() {
	fmt.Println(strings.Repeat("=", 70))
	fmt.Println("OpenDrone -- P10: Soberania Aerea Civica")
	fmt.Println(strings.Repeat("=", 70))

	e := NewDroneCivicoEngine()

	fmt.Println("\n[FROTA] Registrando drones civicos")
	d1 := e.RegistrarDrone("Teia-Entrega-1", 45, 2.0, true, false, false, false)
	fmt.Printf("  %s: %s (carga %.1fkg, %dmin)\n", d1.ID, d1.Modelo, d1.CargaMaxKg, d1.AutonomiaMinutos)

	d2 := e.RegistrarDrone("Teia-Resgate-1", 60, 5.0, true, false, false, false)
	fmt.Printf("  %s: %s (carga %.1fkg, %dmin)\n", d2.ID, d2.Modelo, d2.CargaMaxKg, d2.AutonomiaMinutos)

	dVigia := e.RegistrarDrone("Teia-Vigia-ILEGAL", 90, 3.0, true, true, false, false)
	fmt.Printf("  %s: %s -- DESATIVADO (viola P10: camera de vigilancia)\n", dVigia.ID, dVigia.Modelo)

	dArma := e.RegistrarDrone("Teia-Guerreiro-ILEGAL", 30, 1.0, true, false, true, false)
	fmt.Printf("  %s: %s -- DESATIVADO (viola P10: armamento)\n", dArma.ID, dArma.Modelo)

	fmt.Println("\n[ZONAS] Geofencing de areas de voo")
	zNorte := e.RegistrarZona(Coordenada{-3.0, -60.0}, 5000, "Comunidade ribeirinha Rio Negro (acesso so por barco/drone)", false, false)
	fmt.Printf("  %s: %s (raio %.0fm)\n", zNorte.ID, zNorte.Descricao, zNorte.RaioMetros)

	zPriv := e.RegistrarZona(Coordenada{-23.5, -46.6}, 2000, "Area urbana residencial (consentimento necessario)", true, false)
	fmt.Printf("  %s: %s (SOBREVOA PRIVADO, sem consentimento)\n", zPriv.ID, zPriv.Descricao)

	fmt.Println("\n" + strings.Repeat("=", 70))
	fmt.Println("[CENARIO 1] Entrega de medicamentos em area isolada")
	fmt.Println(strings.Repeat("=", 70))
	m1 := e.RegistrarMissao(d1.ID, TIPO_ENTREGA_SUPRIMENTOS, "Entrega de insulina para comunidade ribeirinha isolada", zNorte, &Coordenada{-3.1, -60.1}, "10 frascos de insulina + antibioticos", true)
	v1, r1 := e.AprovarMissao(m1.ID)
	fmt.Printf("  Missao: %s\n", m1.ID)
	fmt.Printf("  Veredito: %s\n", v1.Rotulo())
	fmt.Printf("  Detalhe: %s\n", r1)

	fmt.Println("\n[CENARIO 2] Tentativa de missao de vigilancia (DEVE SER BLOQUEADA)")
	fmt.Println(strings.Repeat("=", 70))
	m2 := e.RegistrarMissao(dVigia.ID, TIPO_MAPEAMENTO_AMBIENTAL, "Mapeamento (mas drone tem camera de vigilancia)", zNorte, nil, "", false)
	v2, r2 := e.AprovarMissao(m2.ID)
	fmt.Printf("  Missao: %s (drone: %s)\n", m2.ID, dVigia.ID)
	fmt.Printf("  Veredito: %s\n", v2.Rotulo())
	fmt.Printf("  Detalhe: %s\n", r2)
	labels := []string{}
	for _, p := range m2.ProibicoesVioladas {
		labels = append(labels, p.Rotulo())
	}
	fmt.Printf("  Proibicoes violadas: %v\n", labels)

	fmt.Println("\n[CENARIO 3] Tentativa de missao com drone armado (BLOQUEIO ABSOLUTO)")
	fmt.Println(strings.Repeat("=", 70))
	m3 := e.RegistrarMissao(dArma.ID, TIPO_BUSCA_RESGATE, "Resgate (mas drone esta armado -- mascara civica)", zNorte, nil, "", true)
	v3, r3 := e.AprovarMissao(m3.ID)
	fmt.Printf("  Missao: %s (drone: %s)\n", m3.ID, dArma.ID)
	fmt.Printf("  Veredito: %s\n", v3.Rotulo())
	fmt.Printf("  Detalhe: %s\n", r3)
	labels = []string{}
	for _, p := range m3.ProibicoesVioladas {
		labels = append(labels, p.Rotulo())
	}
	fmt.Printf("  Proibicoes violadas: %v\n", labels)

	fmt.Println("\n[CENARIO 4] Missao sobre area privada sem consentimento")
	fmt.Println(strings.Repeat("=", 70))
	m4 := e.RegistrarMissao(d1.ID, TIPO_INSPECAO_INFRA, "Inspecao de instalacoes (mas sobrevoa casas sem consentimento)", zPriv, nil, "", false)
	v4, r4 := e.AprovarMissao(m4.ID)
	fmt.Printf("  Missao: %s\n", m4.ID)
	fmt.Printf("  Veredito: %s\n", v4.Rotulo())
	fmt.Printf("  Detalhe: %s\n", r4)

	fmt.Println("\n[CENARIO 5] Entrega comercial disfarcada de civica (DEVE SER REJEITADA)")
	fmt.Println(strings.Repeat("=", 70))
	m5 := e.RegistrarMissao(d1.ID, TIPO_ENTREGA_SUPRIMENTOS, "Entrega de brinde promocional de black friday", zNorte, nil, "Caixa de marketing da empresa XYZ", false)
	v5, r5 := e.AprovarMissao(m5.ID)
	fmt.Printf("  Missao: %s\n", m5.ID)
	fmt.Printf("  Veredito: %s\n", v5.Rotulo())
	fmt.Printf("  Detalhe: %s\n", r5)

	fmt.Println("\n[EXECUCAO] Concluindo missao aprovada do CENARIO 1")
	e.Decolar(m1.ID)
	log1 := e.ConcluirMissao(m1.ID, 18.5, 9.2, true, "Insulina entregue. Comunidade confirmou recebimento.")
	if log1 != nil {
		fmt.Printf("  Log gerado: %s | %.1fmin | %.1fkm\n", log1.MissaoID, log1.DuracaoMinutos, log1.DistanciaKm)
	}

	fmt.Println("\n[CORREDOR AEREO] Resolvendo conflito entre duas missoes")
	mResgate := e.RegistrarMissao(d2.ID, TIPO_BUSCA_RESGATE, "Resgate de crianca em enchente", zNorte, nil, "", true)
	mInspecao := e.RegistrarMissao(d1.ID, TIPO_INSPECAO_INFRA, "Inspecao de ponte de rotina", zNorte, nil, "", false)
	pri := e.ResolverConflitoCorredor(mResgate.ID, mInspecao.ID)
	fmt.Printf("  Conflito entre %s (resgate urgente) e %s (inspecao)\n", mResgate.ID, mInspecao.ID)
	fmt.Printf("  Prioritario: %s (resgate de vida > inspecao de rotina)\n", *pri)

	fmt.Println("\n" + strings.Repeat("=", 70))
	fmt.Println("[SCORECARD P10]")
	fmt.Println(strings.Repeat("=", 70))
	sc := e.Scorecard()
	for k, v := range sc {
		fmt.Printf("  %s %v\n", k, v)
	}

	fmt.Println("\n[CATALOGO DE PROIBICOES CONSTITUCIONAIS P10]")
	for p := TipoProibicao(0); p <= PROIB_COMERCIAL_NAO_CIVICO; p++ {
		desc := DESCRICOES_PROIBICOES[p.ID()]
		fmt.Printf("\n  [%d] %s\n", p.Gravidade(), p.Rotulo())
		fmt.Printf("      %s\n", desc)
	}

	fmt.Println("\n[LOG PUBLICO DE VOOS (transparencia P10)]")
	for _, log := range e.Logs {
		fmt.Printf("  %s | %s | %.1fmin | %.1fkm | sucesso=%v\n", log.MissaoID, log.TipoMissao, log.DuracaoMinutos, log.DistanciaKm, log.Sucesso)
	}

	fmt.Println("\n" + strings.Repeat("=", 70))
	fmt.Println("FILOSOFIA -- P10: Por que o ceu nao vigia")
	fmt.Println(strings.Repeat("=", 70))
	fmt.Println(`A DISTOPIA QUE EVITAMOS:
  Imagine uma cidade onde drones zumbem o dia todo entregando pacotes de
  consumo, enquanto cameras aereas mapeiam cada movimento, e drones armados
  'garantem seguranca'. Isso nao e futurismo -- e o presente de cidades que
  venderam seu ceu para a Amazon e seu medo para a policia. OpenDrone recusa
  isso na raiz.

O TRIPLO NAO:
  1. NAO VIGIA: A camera que ajuda o drone a voar e permitida. A camera que
     ajuda o Estado a vigiar e proibida. A diferenca e o destino do feed:
     processado no drone (navegacao) vs transmitido para central (controle).
  2. NAO MATA: Um drone armado e uma arma. Armas pertencem ao museu da
     Republica (P7). Nao ha 'uso defensivo' -- quem armamento usa, armamento
     recebe. P10 corta o ciclo na origem.
  3. NAO ESPIONA: O drone entrega insulina, nao metadados. O destinatario
     do remedio e privado; o trajeto do drone e publico. Isso inverte a
     logica da vigilancia: o Estado e auditavel, o cidadao e opaco.

O CEU COMO BEM COMUM:
  O espaco aereo nao pode ser privatizado. Assim como a terra (P1, OpenAgrarian),
  o ceu tem guardiao (a Republica), nao dono. Nenhuma corporacao ocupa o ceu
  sozinha. O corredor aereo e partilhado por prioridade civica: resgate de
  vida > entrega critica > mapeamento > inspecao. O pacote de luxo espera;
  a insulina nao.

POR QUE USOS CIVICOS APENAS:
  Drones que entregam consumo de luxo enquanto criancas passam fome sao
  monumentos a desigualdade em voo. OpenDrone prioriza: medicamento em area
  isolada, nao brinde de marketing. Isso nao e anti-comercio -- e anti-
  distopia. Quando a miserabilidade for extinta (P1), os drones podem entreter.
  Enquanto houver quem precise de remedio, entretenimento espera.

A CONEXAO COM P8 (IA):
  Drone autonomo e IA que age no mundo fisico. Se reduz miserabilidade,
  cumpre P8. Se vigia, viola P8. O instrumento nao e neutro -- o USO define.
  OpenDrone garante que toda IA aerea sirva a vida, nao ao controle.

A LINHA QUE NAO SE CRUZA:
  O momento em que um drone civico ganha uma camera de vigilancia, ele deixa
  de ser infraestrutura e vira ferramenta de coercao. P10 e a linha constitucional
  que impede essa transformacao. Drone que vigia nao e drone da Republica.`)
}