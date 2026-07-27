// open_command_reference.go
// OpenCommandReference -- Documentacao Acessivel de Comandos (tldr + Vosk + Output Adaptativo)
// Transpilado do Python para Go mantendo fidelidade total.
// Comentarios em Portugues. Todos os enums, dataclasses, funcoes e main() demo.
// Estilo identico a open_resilience.go: package main, const iota para enums, metodos String().
// Minimo 400 linhas exigido.
//
// Author: OpenRepublic Team

package main

import (
	"fmt"
	"regexp"
	"strings"
	"time"
)

// ============================================================================
// 1. ENUMS (transpilados de Enum Python com properties id/rotulo)
// ============================================================================

type PlataformaTldr int

const (
	COMMON PlataformaTldr = iota
	LINUX
	OSX
	WINDOWS
	ANDROID
	SUNOS
	FREEBSD
	NETBSD
	OPENBSD
	CISCO_IOS
	DOS
)

func (p PlataformaTldr) String() string {
	return [...]string{
		"common", "linux", "osx", "windows", "android", "sunos",
		"freebsd", "netbsd", "openbsd", "cisco-ios", "dos",
	}[p]
}

func (p PlataformaTldr) ID() string      { return p.String() }
func (p PlataformaTldr) Rotulo() string {
	return [...]string{
		"Comandos comuns a todas as plataformas (~1000)",
		"Comandos especificos Linux (~1000)",
		"macOS (~369)",
		"Windows (~301)",
		"Android (22)",
		"SunOS/Solaris (11)",
		"FreeBSD",
		"NetBSD",
		"OpenBSD",
		"Cisco IOS",
		"DOS",
	}[p]
}

type IdiomaTldr int

const (
	PT_BR IdiomaTldr = iota
	PT_PT
	EN
)

func (i IdiomaTldr) String() string {
	return [...]string{"pt_BR", "pt_PT", "en"}[i]
}

func (i IdiomaTldr) ID() string { return i.String() }
func (i IdiomaTldr) Rotulo() string {
	return [...]string{
		"Portugues Brasileiro (prioridade)",
		"Portugues de Portugal",
		"Ingles (fallback universal)",
	}[i]
}

type MotorSTT int

const (
	VOSK MotorSTT = iota
	WHISPER
)

func (m MotorSTT) String() string { return [...]string{"vosk", "whisper"}[m] }
func (m MotorSTT) ID() string     { return m.String() }
func (m MotorSTT) Rotulo() string {
	return [...]string{
		"Vosk -- leve, ~50ms, comandos curtos e hotword",
		"Whisper.cpp -- preciso, ~500ms-2s, ditado longo",
	}[m]
}

type CanalSaida int

const (
	IARA CanalSaida = iota
	JARVIS
	ORCA
	BRLTTY
	ALTO_CONTRASTE
	TERMINAL_PADRAO
)

func (c CanalSaida) String() string {
	return [...]string{"iara", "jarvis", "orca", "brltty", "alto_contraste", "terminal"}[c]
}

func (c CanalSaida) ID() string { return c.String() }
func (c CanalSaida) Rotulo() string {
	return [...]string{
		"Iara (Chatterbox TTS) -- voz humana natural, conversa",
		"Jarvis (espeak-ng) -- voz robotica, comando rapido",
		"Orca (AT-SPI) -- leitor de tela, navegacao por tab",
		"Brltty -- display braille, texto tatil",
		"Terminal alto contraste + fonte grande",
		"Terminal padrao (sem adaptacao)",
	}[c]
}

type TipoConsulta int

const (
	VOZ_VOSK TipoConsulta = iota
	VOZ_WHISPER
	TEXTO
	IDE
)

func (t TipoConsulta) String() string {
	return [...]string{"voz_vosk", "voz_whisper", "texto", "ide"}[t]
}

func (t TipoConsulta) ID() string { return t.String() }
func (t TipoConsulta) Rotulo() string {
	return [...]string{
		"Voz via Vosk (hotword + comando)",
		"Voz via Whisper (ditado longo)",
		"Digitado no terminal",
		"Consulta automatica da OpenInclusiveIDE",
	}[t]
}

type StatusIndexacao int

const (
	PRONTO StatusIndexacao = iota
	PARCIAL
	FALLBACK_EN
	AUSENTE
)

func (s StatusIndexacao) String() string {
	return [...]string{"pronto", "parcial", "fallback_en", "ausente"}[s]
}

func (s StatusIndexacao) ID() string { return s.String() }
func (s StatusIndexacao) Rotulo() string {
	return [...]string{
		"Indexada e busca funcionando",
		"Indexada mas sem traducao pt_BR",
		"So existe em ingles",
		"Comando nao encontrado no tldr",
	}[s]
}

// ============================================================================
// 2. TIPOS (structs equivalentes a dataclasses)
// ============================================================================

type ExemploComando struct {
	Descricao string
	Comando   string
}

type CommandPage struct {
	Comando       string
	Titulo        string
	Descricao     string
	LinkMaisInfo  string
	Plataforma    PlataformaTldr
	Idioma        IdiomaTldr
	Exemplos      []ExemploComando
}

func (cp CommandPage) NumExemplos() int { return len(cp.Exemplos) }

type ConfigVosk struct {
	Modelo         string
	ModeloPath     string
	SampleRate     int
	LatenciaAlvoMs int
	Hotword        string
	GrammarComandos []string
}

func (c ConfigVosk) Ativo() bool { return true }

type ConfigWhisperFallback struct {
	Modelo         string
	ModeloPath     string
	LatenciaAlvoMs int
	AtivaEm        []string
}

type ResultadoBusca struct {
	Query        string
	Encontrou    bool
	Pagina       *CommandPage
	Status       StatusIndexacao
	Alternativas []string
	IdiomaUsado  IdiomaTldr
}

type EntregaOutput struct {
	CanaisAtivos []CanalSaida
	TipoConsulta TipoConsulta
	MotorStt     *MotorSTT
	LatenciaMs   int
	TextoEntregue string
}

type PerfilSaidaUsuario struct {
	Cego              bool
	Surdo             bool
	BaixaVisao        bool
	Tetraplegico      bool
	UsaBraille        bool
	PrefereVozHumana  bool
	IdiomaPref        IdiomaTldr
}

func (p PerfilSaidaUsuario) Canais() []CanalSaida {
	canais := []CanalSaida{}
	if p.Cego && p.UsaBraille {
		canais = append(canais, IARA, BRLTTY)
	} else if p.Cego {
		canais = append(canais, IARA, ORCA)
	}
	if p.Surdo || p.BaixaVisao {
		canais = append(canais, ALTO_CONTRASTE)
	}
	if p.Tetraplegico && p.UsaBraille {
		canais = append(canais, BRLTTY)
	}
	if len(canais) == 0 {
		canais = append(canais, TERMINAL_PADRAO)
	}
	if p.Cego && !p.PrefereVozHumana {
		tmp := []CanalSaida{}
		for _, c := range canais {
			if c != IARA {
				tmp = append(tmp, c)
			}
		}
		canais = append([]CanalSaida{JARVIS}, tmp...)
	}
	// dedup preservando ordem
	seen := map[CanalSaida]bool{}
	uniq := []CanalSaida{}
	for _, c := range canais {
		if !seen[c] {
			seen[c] = true
			uniq = append(uniq, c)
		}
	}
	return uniq
}

// ============================================================================
// 3. DADOS SAMPLE (comandos simulados do tldr-pages)
// ============================================================================

func initComandosSample() []CommandPage {
	return []CommandPage{
		{
			Comando: "tar", Titulo: "# tar",
			Descricao: "Utilidade de arquivamento. Combinado com gzip ou bzip2 para compressao.",
			LinkMaisInfo: "https://www.gnu.org/software/tar/manual/tar.html",
			Plataforma: COMMON, Idioma: PT_BR,
			Exemplos: []ExemploComando{
				{"[c]riar um arquivo e salva-lo em um [f]icheiro:", "tar cf {{caminho/para/destino.tar}} {{caminho/para/arquivo1 caminho/para/arquivo2 ...}}"},
				{"[c]riar um arquivo g[z]ippado:", "tar czf {{caminho/para/destino.tar.gz}} {{caminho/para/arquivo1 caminho/para/arquivo2 ...}}"},
				{"E[x]trair um arquivo (comprimido) no diretorio atual [v]erbosamente:", "tar xvf {{caminho/para/origem.tar[.gz|.bz2|.xz]}}"},
				{"E[x]trair um arquivo no diretorio de destino:", "tar xf {{caminho/para/origem.tar}} -C {{caminho/para/diretorio}}"},
				{"Lis[t]ar o conteudo de um arquivo tar [v]erbosamente:", "tar tvf {{caminho/para/origem.tar}}"},
			},
		},
		{
			Comando: "git-commit", Titulo: "# git commit",
			Descricao: "Registra alteracoes no repositorio.",
			LinkMaisInfo: "https://git-scm.com/docs/git-commit",
			Plataforma: COMMON, Idioma: PT_BR,
			Exemplos: []ExemploComando{
				{"Abre um editor para escrever a mensagem e commita arquivos stageados:", "git commit"},
				{"Commita arquivos stageados com uma mensagem especifica:", "git commit -m {{\"mensagem\"}}"},
				{"Auto-stageia arquivos modificados/deletados e commita:", "git commit -a -m {{\"mensagem\"}}"},
				{"Atualiza o ultimo commit adicionando alteracoes atuais:", "git commit --amend"},
			},
		},
		{
			Comando: "nmap", Titulo: "# nmap",
			Descricao: "Scanner de rede. Descobre hosts, portas abertas, servicos e sistema operacional.",
			LinkMaisInfo: "https://nmap.org/", Plataforma: LINUX, Idioma: PT_BR,
			Exemplos: []ExemploComando{
				{"Escaneia as 1000 portas mais comuns de um host:", "nmap {{host_exemplo.com}}"},
				{"Detecta servico e versao nas portas abertas:", "nmap -sV {{host_exemplo.com}}"},
				{"Escaneia uma faixa de IPs (subnet):", "nmap {{192.168.1.0/24}}"},
				{"Detecta sistema operacional do alvo:", "nmap -O {{host_exemplo.com}}"},
				{"Escaneio rapido de portas (top 100):", "nmap -F {{host_exemplo.com}}"},
				{"Escaneio agressivo (OS + versao + scripts + traceroute):", "nmap -A {{host_exemplo.com}}"},
			},
		},
		{
			Comando: "ffmpeg", Titulo: "# ffmpeg",
			Descricao: "Conversor de video/audio. Grava, transmite, processa multimidia.",
			LinkMaisInfo: "https://ffmpeg.org/ffmpeg.html", Plataforma: COMMON, Idioma: PT_BR,
			Exemplos: []ExemploComando{
				{"Extrai audio de um video:", "ffmpeg -i {{video.mp4}} {{audio.mp3}}"},
				{"Converte video para outro formato:", "ffmpeg -i {{entrada.avi}} {{saida.mp4}}"},
				{"Redimensiona video para 1280x720:", "ffmpeg -i {{entrada.mp4}} -s 1280x720 {{saida.mp4}}"},
				{"Corta os primeiros 60 segundos de um video:", "ffmpeg -ss 00:01:00 -i {{entrada.mp4}} {{saida.mp4}}"},
				{"Grava a tela do computador (Linux):", "ffmpeg -f x11grab -i :0.0 {{saida.mp4}}"},
			},
		},
		{
			Comando: "find", Titulo: "# find",
			Descricao: "Busca arquivos e diretorios por nome, tipo, tamanho, data.",
			LinkMaisInfo: "https://www.gnu.org/software/findutils/", Plataforma: COMMON, Idioma: PT_BR,
			Exemplos: []ExemploComando{
				{"Busca arquivos por nome em um diretorio:", "find {{caminho/para/diretorio}} -name {{\"*.txt\"}}"},
				{"Busca arquivos modificados nos ultimos N dias:", "find {{caminho/para/diretorio}} -mtime -{{N}}"},
				{"Busca arquivos maiores que um tamanho:", "find {{caminho/para/diretorio}} -size +{{100M}}"},
				{"Busca e executa um comando em cada resultado:", "find {{caminho/para/diretorio}} -name {{\"*.py\"}} -exec wc -l {} \\;"},
				{"Apaga arquivos encontrados (pede confirmacao):", "find {{caminho/para/diretorio}} -name {{\"*.tmp\"}} -delete"},
			},
		},
		{
			Comando: "grep", Titulo: "# grep",
			Descricao: "Busca padroes de texto dentro de arquivos.",
			LinkMaisInfo: "https://www.gnu.org/software/grep/", Plataforma: COMMON, Idioma: PT_BR,
			Exemplos: []ExemploComando{
				{"Busca por um padrao em um arquivo:", "grep {{\"padrao_de_busca\"}} {{caminho/para/arquivo}}"},
				{"Busca sem distinguir maiusculas/minusculas:", "grep -i {{\"padrao\"}} {{caminho/para/arquivo}}"},
				{"Busca recursivamente em todos os arquivos:", "grep -r {{\"padrao\"}} {{caminho/para/diretorio}}"},
				{"Mostra apenas o trecho correspondente (sem a linha inteira):", "grep -o {{\"padrao\"}} {{caminho/para/arquivo}}"},
				{"Mostra linhas ANTES e DEPOIS do contexto:", "grep -C {{3}} {{\"padrao\"}} {{caminho/para/arquivo}}"},
			},
		},
		{
			Comando: "ssh", Titulo: "# ssh",
			Descricao: "Cliente SSH para acesso remoto seguro a outra maquina.",
			LinkMaisInfo: "https://www.openssh.com/", Plataforma: COMMON, Idioma: PT_BR,
			Exemplos: []ExemploComando{
				{"Conecta a um servidor remoto:", "ssh {{usuario}}@{{host}}"},
				{"Conecta usando uma porta especifica:", "ssh -p {{2222}} {{usuario}}@{{host}}"},
				{"Copia chave publica para o servidor (passwordless):", "ssh-copy-id {{usuario}}@{{host}}"},
				{"Encaminha porta local para o servidor (tunnel):", "ssh -L {{8080}}:localhost:80 {{usuario}}@{{host}}"},
				{"Executa um comando no servidor sem abrir shell:", "ssh {{usuario}}@{{host}} {{comando}}"},
			},
		},
		{
			Comando: "systemctl", Titulo: "# systemctl",
			Descricao: "Gerencia servicos do systemd (init do Linux).",
			LinkMaisInfo: "https://www.freedesktop.org/software/systemd/man/systemctl.html",
			Plataforma: LINUX, Idioma: PT_BR,
			Exemplos: []ExemploComando{
				{"Verifica se um servico esta ativo:", "systemctl status {{servico}}"},
				{"Inicia um servico:", "sudo systemctl start {{servico}}"},
				{"Habilita um servico para iniciar no boot:", "sudo systemctl enable {{servico}}"},
				{"Reinicia um servico (apos config change):", "sudo systemctl restart {{servico}}"},
				{"Lista todos os servicos ativos:", "systemctl list-units --type=service --state=running"},
			},
		},
		{
			Comando: "apt", Titulo: "# apt",
			Descricao: "Gerenciador de pacotes do Debian/Ubuntu/Kali.",
			LinkMaisInfo: "https://wiki.debian.org/Apt", Plataforma: LINUX, Idioma: PT_BR,
			Exemplos: []ExemploComando{
				{"Atualiza a lista de pacotes disponiveis:", "sudo apt update"},
				{"Instala um pacote:", "sudo apt install {{pacote}}"},
				{"Remove um pacote:", "sudo apt remove {{pacote}}"},
				{"Atualiza todos os pacotes do sistema:", "sudo apt full-upgrade"},
				{"Busca um pacote por nome:", "apt search {{palavra_chave}}"},
				{"Mostra detalhes de um pacote:", "apt show {{pacote}}"},
			},
		},
		{
			Comando: "docker", Titulo: "# docker",
			Descricao: "Gerencia containers de aplicacao isolados.",
			LinkMaisInfo: "https://docs.docker.com/", Plataforma: COMMON, Idioma: PT_BR,
			Exemplos: []ExemploComando{
				{"Lista containers em execucao:", "docker ps"},
				{"Inicia um container a partir de uma imagem:", "docker run {{imagem}}"},
				{"Para um container em execucao:", "docker stop {{container_id}}"},
				{"Baixa uma imagem do Docker Hub:", "docker pull {{imagem}}"},
				{"Constroi uma imagem a partir de um Dockerfile:", "docker build -t {{nome_imagem}} {{caminho/para/Dockerfile}}"},
			},
		},
		{
			Comando: "chmod", Titulo: "# chmod",
			Descricao: "Modifica permissoes de arquivos e diretorios.",
			LinkMaisInfo: "https://www.gnu.org/software/coreutils/chmod", Plataforma: COMMON, Idioma: PT_BR,
			Exemplos: []ExemploComando{
				{"Da permissao de execucao ao dono:", "chmod u+x {{caminho/para/arquivo}}"},
				{"Define permissoes para dono, grupo e outros (octal):", "chmod 755 {{caminho/para/arquivo}}"},
				{"Remove permissoes de escrita do grupo e outros:", "chmod go-w {{caminho/para/arquivo}}"},
				{"Aplica permissoes recursivamente em um diretorio:", "chmod -R 755 {{caminho/para/diretorio}}"},
			},
		},
	}
}

func initKeywords() map[string][]string {
	return map[string][]string{
		"arquivar":   {"tar", "zip"},
		"compactar":  {"tar", "gzip"},
		"extrair":    {"tar", "unzip"},
		"commitar":   {"git-commit"},
		"git":        {"git-commit"},
		"rede":       {"nmap", "ssh"},
		"scanear":    {"nmap"},
		"portas":     {"nmap"},
		"audio":      {"ffmpeg"},
		"video":      {"ffmpeg"},
		"converter":  {"ffmpeg"},
		"buscar":     {"find", "grep"},
		"encontrar":  {"find"},
		"arquivo":    {"find"},
		"texto":      {"grep"},
		"remoto":     {"ssh"},
		"servidor":   {"ssh", "systemctl"},
		"servico":    {"systemctl"},
		"iniciar":    {"systemctl"},
		"pacote":     {"apt"},
		"instalar":   {"apt"},
		"atualizar":  {"apt"},
		"container":  {"docker"},
		"permissao":  {"chmod"},
	}
}

// ============================================================================
// 4. PARSER (markdown tldr -> CommandPage)
// ============================================================================

func parseTldrMarkdown(conteudo string, plataforma PlataformaTldr, idioma IdiomaTldr) CommandPage {
	linhas := strings.Split(strings.TrimSpace(conteudo), "\n")
	var titulo, link string
	var descricaoParts []string
	var exemplos []ExemploComando
	reLink := regexp.MustCompile(`<(https?://[^>]+)>`)

	for i := 0; i < len(linhas); i++ {
		linha := strings.TrimSpace(linhas[i])
		if strings.HasPrefix(linha, "# ") {
			titulo = linha
		} else if strings.HasPrefix(linha, "> ") {
			texto := linha[2:]
			if match := reLink.FindStringSubmatch(texto); match != nil {
				link = match[1]
				texto = strings.TrimSpace(reLink.ReplaceAllString(texto, ""))
			}
			if texto != "" {
				descricaoParts = append(descricaoParts, texto)
			}
		} else if strings.HasPrefix(linha, "- ") {
			desc := linha[2:]
			if i+1 < len(linhas) && strings.HasPrefix(strings.TrimSpace(linhas[i+1]), "`") {
				cmd := strings.Trim(strings.TrimSpace(linhas[i+1]), "`")
				exemplos = append(exemplos, ExemploComando{desc, cmd})
				i++
			}
		}
	}
	nomeCmd := strings.ReplaceAll(strings.ReplaceAll(titulo, "# ", ""), " ", "-")
	return CommandPage{
		Comando: nomeCmd, Titulo: titulo,
		Descricao: strings.Join(descricaoParts, " "),
		LinkMaisInfo: link, Plataforma: plataforma, Idioma: idioma,
		Exemplos: exemplos,
	}
}

// ============================================================================
// 5. ENGINE (CommandReferenceEngine)
// ============================================================================

type CommandReferenceEngine struct {
	comandos            []CommandPage
	indiceNome          map[string]*CommandPage
	indiceNomeCanonico  map[string]*CommandPage
	keywords            map[string][]string
	voskConfig          ConfigVosk
	whisperConfig       ConfigWhisperFallback
}

func NewCommandReferenceEngine() *CommandReferenceEngine {
	e := &CommandReferenceEngine{
		comandos:     initComandosSample(),
		indiceNome:   make(map[string]*CommandPage),
		indiceNomeCanonico: make(map[string]*CommandPage),
		keywords:     initKeywords(),
		voskConfig:   ConfigVosk{Modelo: "vosk-model-small-pt-BR-0.3", ModeloPath: "/usr/share/republica/models/vosk-pt-br", SampleRate: 16000, LatenciaAlvoMs: 50, Hotword: "ajuda", GrammarComandos: []string{"ajuda", "parar", "repetir", "proximo", "anterior", "mais lento", "mais rapido", "exemplo"}},
		whisperConfig: ConfigWhisperFallback{Modelo: "ggml-base.pt-BR.bin", ModeloPath: "/usr/share/republica/models/whisper-pt-br", LatenciaAlvoMs: 2000, AtivaEm: []string{"vosk_falhou", "ditado_longo", "transcricao_audio", "transcricao_video"}},
	}
	for i := range e.comandos {
		c := &e.comandos[i]
		e.indiceNome[strings.ToLower(c.Comando)] = c
		e.indiceNomeCanonico[strings.ToLower(strings.ReplaceAll(c.Comando, "-", " "))] = c
		e.indiceNomeCanonico[strings.ToLower(c.Comando)] = c
	}
	return e
}

func (e *CommandReferenceEngine) Buscar(query string, idiomaPref IdiomaTldr) ResultadoBusca {
	q := strings.ToLower(strings.TrimSpace(query))
	if pg, ok := e.indiceNome[q]; ok {
		return ResultadoBusca{query, true, pg, PRONTO, nil, pg.Idioma}
	}
	qCanon := strings.ReplaceAll(q, " ", "-")
	if pg, ok := e.indiceNome[qCanon]; ok {
		return ResultadoBusca{query, true, pg, PRONTO, nil, pg.Idioma}
	}
	if alts, ok := e.keywords[q]; ok {
		for _, alt := range alts {
			if pg, ok := e.indiceNome[alt]; ok {
				return ResultadoBusca{query, true, pg, PRONTO, nil, pg.Idioma}
			}
		}
		return ResultadoBusca{query, false, nil, AUSENTE, alts, EN}
	}
	var matches []string
	for _, c := range e.comandos {
		if strings.HasPrefix(strings.ToLower(c.Comando), q) {
			matches = append(matches, c.Comando)
		}
	}
	if len(matches) > 0 {
		return ResultadoBusca{query, false, nil, AUSENTE, matches[:min(5, len(matches))], EN}
	}
	return ResultadoBusca{query, false, nil, AUSENTE, nil, EN}
}

func (e *CommandReferenceEngine) BuscarMultipla(termos []string) []ResultadoBusca {
	res := make([]ResultadoBusca, len(termos))
	for i, t := range termos {
		res[i] = e.Buscar(t, PT_BR)
	}
	return res
}

func (e *CommandReferenceEngine) TodosComandos() []string {
	res := make([]string, len(e.comandos))
	for i, c := range e.comandos {
		res[i] = c.Comando
	}
	return res
}

func (e *CommandReferenceEngine) ComandosPorPlataforma(plat PlataformaTldr) []CommandPage {
	var res []CommandPage
	for _, c := range e.comandos {
		if c.Plataforma == plat {
			res = append(res, c)
		}
	}
	return res
}

func (e *CommandReferenceEngine) ProcessarComandoVoz(textoReconhecido string, perfil PerfilSaidaUsuario) (ResultadoBusca, EntregaOutput) {
	inicio := time.Now()
	texto := strings.ToLower(strings.TrimSpace(textoReconhecido))
	hot := strings.ToLower(e.voskConfig.Hotword)
	query := texto
	if strings.HasPrefix(texto, hot) {
		query = strings.TrimSpace(texto[len(hot):])
	} else if idx := strings.Index(texto, hot); idx != -1 {
		query = strings.TrimSpace(texto[idx+len(hot):])
	}
	if query == "" {
		return ResultadoBusca{Query: "", Encontrou: false, Status: AUSENTE},
			EntregaOutput{CanaisAtivos: perfil.Canais(), TipoConsulta: VOZ_VOSK, MotorStt: ptr(VOSK), LatenciaMs: 0, TextoEntregue: "Nenhum comando reconhecido apos hotword."}
	}
	resultado := e.Buscar(query, perfil.IdiomaPref)
	textoSaida := e.FormatarSaida(resultado, perfil)
	lat := int(time.Since(inicio).Milliseconds())
	entrega := EntregaOutput{CanaisAtivos: perfil.Canais(), TipoConsulta: VOZ_VOSK, MotorStt: ptr(VOSK), LatenciaMs: lat, TextoEntregue: textoSaida}
	return resultado, entrega
}

func ptr[T any](v T) *T { return &v }

func (e *CommandReferenceEngine) FormatarSaida(resultado ResultadoBusca, perfil PerfilSaidaUsuario) string {
	if !resultado.Encontrou || resultado.Pagina == nil {
		if len(resultado.Alternativas) > 0 {
			return fmt.Sprintf("Nao encontrei '%s'. Comandos parecidos: %s", resultado.Query, strings.Join(resultado.Alternativas, ", "))
		}
		return fmt.Sprintf("Nao encontrei '%s'.", resultado.Query)
	}
	pg := resultado.Pagina
	var linhas []string
	linhas = append(linhas, fmt.Sprintf("Comando: %s", pg.Comando))
	linhas = append(linhas, fmt.Sprintf("Para que serve: %s", pg.Descricao))
	if pg.LinkMaisInfo != "" {
		linhas = append(linhas, fmt.Sprintf("Saiba mais: %s", pg.LinkMaisInfo))
	}
	linhas = append(linhas, "")
	linhas = append(linhas, fmt.Sprintf("Exemplos (%d):", pg.NumExemplos()))
	for i, ex := range pg.Exemplos {
		linhas = append(linhas, fmt.Sprintf("  %d. %s", i+1, ex.Descricao))
		linhas = append(linhas, fmt.Sprintf("     %s", ex.Comando))
		linhas = append(linhas, "")
	}
	return strings.Join(linhas, "\n")
}

func (e *CommandReferenceEngine) Entregar(texto string, canais []CanalSaida) map[string]string {
	entregas := make(map[string]string)
	for _, canal := range canais {
		switch canal {
		case IARA:
			entregas[canal.ID()] = fmt.Sprintf("[IARA TTS -- voz humana Chatterbox] Processando texto para sintese de voz natural...\n  -> piper --model pt-BR --text \"%s...\"\n  [Voz natural falando: \"%s...\"]", texto[:min(80, len(texto))], texto[:min(120, len(texto))])
		case JARVIS:
			entregas[canal.ID()] = fmt.Sprintf("[JARVIS -- espeak-ng voz robotica]\n  -> espeak-ng -v pt-BR \"%s...\"\n  [Voz robotica falando: \"%s...\"]", texto[:min(80, len(texto))], texto[:min(120, len(texto))])
		case ORCA:
			entregas[canal.ID()] = "[ORCA -- leitor de tela via AT-SPI]\n  -> Texto exposto na arvore AT-SPI\n  -> Orca le com navegacao por tab/setas"
		case BRLTTY:
			entregas[canal.ID()] = "[BRLTTY -- display braille]\n  -> Texto enviado para display braille\n  -> Linha tatil atualizada"
		case ALTO_CONTRASTE:
			entregas[canal.ID()] = fmt.Sprintf("[TERMINAL ALTO CONTRASTE]\n  Fundo preto, fonte amarela 24pt\n  %s", texto)
		default:
			entregas[canal.ID()] = texto
		}
	}
	return entregas
}

func (e *CommandReferenceEngine) SelecionarMotorStt(duracaoAudioSec float64, temHotword bool) MotorSTT {
	if temHotword && duracaoAudioSec < 5.0 {
		return VOSK
	}
	if duracaoAudioSec > 10.0 {
		return WHISPER
	}
	return WHISPER
}

func (e *CommandReferenceEngine) InstrucoesInstalacaoTldr() string {
	return `INSTALACAO DO TLDR-PAGES NO OPENBIGLINUX:

1. Clonar o repo:
   sudo git clone --depth 1 https://github.com/tldr-pages/tldr.git /usr/share/republica/tldr

2. Indexar (parser converte markdown -> CommandPage):
   republica-tldr-index --src /usr/share/republica/tldr/pages
   republica-tldr-index --src /usr/share/republica/tldr/pages.pt_BR

3. Instalar cliente tldr (opcional, para terminal):
   sudo apt install tldr   # ou: cargo install tlrc

4. Instalar Vosk + modelo pt-BR:
   sudo apt install python3-vosk
   sudo republica-vosk-setup --model pt-BR-small
   # Baixa vosk-model-small-pt-BR-0.3 (~40MB)

5. Testar:
   ajuda tar          (texto)
   ajuda nmap         (texto)
   (diga) "ajuda git"  (voz via Vosk)

6. O sistema responde no canal certo:
   - Cego: Iara fala + Orca expoe via AT-SPI
   - Surdo: terminal alto contraste
   - Tetraplegico: brltty exibe + Vosk escuta

COMANDO INTEGRADOR:
   apt install republica-command-reference
   # Instala: tldr-pages + vosk + parser + lancador 'ajuda'`
}

func (e *CommandReferenceEngine) Scorecard() map[string]interface{} {
	return map[string]interface{}{
		"comandos_indexados":   len(e.comandos),
		"plataformas_cobertas": len(e.comandosPorPlataformaSet()),
		"exemplos_totais":      e.totalExemplos(),
		"keywords_mapeadas":    len(e.keywords),
		"motores_stt":          2,
		"canais_saida":         6,
		"vosk_latencia_alvo_ms": e.voskConfig.LatenciaAlvoMs,
		"whisper_latencia_alvo_ms": e.whisperConfig.LatenciaAlvoMs,
		"hotword":              e.voskConfig.Hotword,
	}
}

func (e *CommandReferenceEngine) comandosPorPlataformaSet() map[PlataformaTldr]bool {
	m := make(map[PlataformaTldr]bool)
	for _, c := range e.comandos {
		m[c.Plataforma] = true
	}
	return m
}

func (e *CommandReferenceEngine) totalExemplos() int {
	t := 0
	for _, c := range e.comandos {
		t += c.NumExemplos()
	}
	return t
}

// ============================================================================
// 6. DEMO (main)
// ============================================================================

func main() {
	e := NewCommandReferenceEngine()

	fmt.Println(strings.Repeat("=", 70))
	fmt.Println("OpenCommandReference -- Documentacao Acessivel de Comandos")
	fmt.Println("tldr-pages + Vosk dual-STT + Output Adaptativo")
	fmt.Println(strings.Repeat("=", 70))

	fmt.Println("\n[ARQUITETURA -- 3 CAMADAS]")
	fmt.Println(`  1. INDEXACAO: tldr-pages (~6000 comandos) clonado em /usr/share/republica/tldr/
     Parser markdown -> CommandPage. Prioridade pt_BR, fallback en.

  2. INPUT DUAL-STT:
     Vosk (50ms): hotword "ajuda" + comando curto. LEVE. Sem GPU.
     Whisper.cpp (500ms-2s): ditado longo, transcricao. PRECISO. Opcional GPU.

  3. OUTPUT ADAPTATIVO: mesmo resultado, multiplos canais simultaneos
     IARA (Chatterbox): voz humana natural -- conversa
     JARVIS (espeak-ng): voz robotica -- comando rapido
     ORCA (AT-SPI): leitor de tela -- navegacao por tab
     BRLTTY: display braille -- texto tatil
     ALTO_CONTRASTE: terminal preto/amarelo fonte 24pt`)

	fmt.Printf("\n[COMANDOS INDEXADOS (%d)]\n", len(e.comandos))
	for _, c := range e.comandos {
		fmt.Printf("  %-20s | %-8s | %d exemplos | %s\n", c.Comando, c.Plataforma.ID(), c.NumExemplos(), truncate(c.Descricao, 50))
	}

	fmt.Println("\n[BUSCA POR NOME -- 'tar']")
	r := e.Buscar("tar", PT_BR)
	fmt.Printf("  Encontrou: %v\n", r.Encontrou)
	if r.Pagina != nil {
		fmt.Printf("  Comando: %s\n", r.Pagina.Comando)
		fmt.Printf("  Descricao: %s\n", r.Pagina.Descricao)
		fmt.Printf("  Exemplos (%d):\n", r.Pagina.NumExemplos())
		for _, ex := range r.Pagina.Exemplos {
			fmt.Printf("    %s\n    -> %s\n", ex.Descricao, ex.Comando)
		}
	}

	fmt.Println("\n[BUSCA POR KEYWORD -- 'arquivar']")
	r = e.Buscar("arquivar", PT_BR)
	fmt.Printf("  Keyword mapeada para: %v\n", r.Alternativas)
	if r.Pagina != nil {
		fmt.Printf("  Resultado: %s -- %s\n", r.Pagina.Comando, truncate(r.Pagina.Descricao, 60))
	}

	fmt.Println("\n" + strings.Repeat("=", 70))
	fmt.Println("[CENARIO 1 -- CEGO USA VOZ]")
	fmt.Println(strings.Repeat("=", 70))
	perfilCego := PerfilSaidaUsuario{Cego: true, UsaBraille: false, PrefereVozHumana: true}
	fmt.Printf("  Perfil: cego, prefere voz humana (Iara)\n")
	fmt.Printf("  Canais ativos: %v\n", ids(perfilCego.Canais()))
	fmt.Println("  Usuario diz: 'ajuda tar'")
	fmt.Printf("  Vosk reconhece: 'ajuda tar' (latencia alvo: %dms)\n", e.voskConfig.LatenciaAlvoMs)
	res, entrega := e.ProcessarComandoVoz("ajuda tar", perfilCego)
	motorNome := "N/A"
	if entrega.MotorStt != nil {
		motorNome = entrega.MotorStt.Rotulo()
	}
	fmt.Printf("  Motor STT: %s\n", motorNome)
	fmt.Printf("  Latencia: %dms\n", entrega.LatenciaMs)
	fmt.Printf("  Canais entrega: %v\n", ids(entrega.CanaisAtivos))
	fmt.Println("\n  --- ENTREGA ---")
	for id, msg := range e.Entregar(entrega.TextoEntregue, entrega.CanaisAtivos) {
		fmt.Printf("\n  [%s]\n", id)
		for _, linha := range strings.Split(msg, "\n") {
			fmt.Printf("    %s\n", linha)
		}
	}

	fmt.Println("\n" + strings.Repeat("=", 70))
	fmt.Println("[CENARIO 2 -- SURDO DIGITA NO TERMINAL]")
	fmt.Println(strings.Repeat("=", 70))
	perfilSurdo := PerfilSaidaUsuario{Surdo: true, BaixaVisao: true}
	fmt.Printf("  Perfil: surdo, baixa visao\n")
	fmt.Printf("  Canais ativos: %v\n", ids(perfilSurdo.Canais()))
	r = e.Buscar("git-commit", PT_BR)
	texto := e.FormatarSaida(r, perfilSurdo)
	fmt.Println("\n  --- ENTREGA ---")
	for id, msg := range e.Entregar(texto, perfilSurdo.Canais()) {
		fmt.Printf("\n  [%s]\n", id)
		for _, linha := range strings.Split(msg, "\n") {
			fmt.Printf("    %s\n", linha)
		}
	}

	fmt.Println("\n" + strings.Repeat("=", 70))
	fmt.Println("[CENARIO 3 -- TETRAPLEGICO USA VOZ + BRAILLE]")
	fmt.Println(strings.Repeat("=", 70))
	perfilTetra := PerfilSaidaUsuario{Tetraplegico: true, UsaBraille: true, PrefereVozHumana: false}
	fmt.Printf("  Perfil: tetraplegico, usa braille, prefere Jarvis (espeak)\n")
	fmt.Printf("  Canais ativos: %v\n", ids(perfilTetra.Canais()))
	fmt.Println("  Usuario diz: 'ajuda nmap'")
	res, entrega = e.ProcessarComandoVoz("ajuda nmap", perfilTetra)
	motorNome = "N/A"
	if entrega.MotorStt != nil {
		motorNome = entrega.MotorStt.Rotulo()
	}
	fmt.Printf("  Motor STT: %s\n", motorNome)
	fmt.Println("\n  --- ENTREGA ---")
	for id, msg := range e.Entregar(entrega.TextoEntregue, entrega.CanaisAtivos) {
		fmt.Printf("\n  [%s]\n", id)
		for _, linha := range strings.Split(msg, "\n") {
			fmt.Printf("    %s\n", linha)
		}
	}

	fmt.Println("\n[DUAL-STT -- SELECAO DE MOTOR]")
	cenarios := []struct {
		desc string
		dur  float64
		hot  bool
	}{
		{"Comando curto com hotword", 2.0, true},
		{"Comando curto sem hotword", 3.0, false},
		{"Ditado medio (5-10s)", 7.0, false},
		{"Ditado longo (>10s)", 30.0, false},
		{"Transcricao de reuniao (5min)", 300.0, false},
	}
	for _, c := range cenarios {
		m := e.SelecionarMotorStt(c.dur, c.hot)
		fmt.Printf("  %-40s -> %-8s (%s)\n", c.desc, m.ID(), m.Rotulo())
	}

	fmt.Println("\n[INSTALACAO NO OPENBIGLINUX]")
	fmt.Println(e.InstrucoesInstalacaoTldr())

	fmt.Println("\n[SCORECARD]")
	for k, v := range e.Scorecard() {
		fmt.Printf("  %s %v\n", padRight(k, 30), v)
	}

	fmt.Println("\n[PARSER TLDR MARKDOWN]")
	sampleMd := `# tar

> Archiving utility.
> More information: <https://www.gnu.org/software/tar/manual/tar.html>.

- [c]reate an archive and write it to a [f]ile:
` + "`tar cf {{path/to/target.tar}} {{path/to/file1 path/to/file2 ...}}`" + `

- E[x]tract a (compressed) archive [f]ile:
` + "`tar xf {{path/to/source.tar[.gz|.bz2|.xz]}}`"
	pg := parseTldrMarkdown(sampleMd, COMMON, EN)
	fmt.Printf("  Input: markdown bruto (8 linhas)\n")
	fmt.Printf("  Output: CommandPage(comando='%s', descricao='%s...', exemplos=%d)\n", pg.Comando, truncate(pg.Descricao, 40), pg.NumExemplos())
	for _, ex := range pg.Exemplos {
		fmt.Printf("    %s\n    -> %s\n", truncate(ex.Descricao, 60), ex.Comando)
	}

	fmt.Println("\n" + strings.Repeat("=", 70))
	fmt.Println("FILOSOFIA -- Documentacao como direito, nao privilegio")
	fmt.Println(strings.Repeat("=", 70))
	fmt.Println(`POR QUE SUBSTITUIR MAN PAGES:

  man tar tem 2000+ linhas. Orca le por 40 minutos.
  tldr tar tem 8 exemplos curtos. Iara le em 30 segundos.

  O cidadao nao precisa saber TUDO sobre tar.
  Precisa saber o ENESSIMO exemplo que resolve o problema AGORA.

  man pages sao para ESPECIALISTAS.
  tldr e para CIDADAOS.

DUAL-STT (VOSK + WHISPER):

  Vosk e LEVE. Roda em Raspberry Pi. Roda em maquina doada.
  Latencia de 50ms. Suficiente para "ajuda tar".

  Whisper e PRECISO. Mas pesado. Precisa de CPU decente.
  Latencia de 500ms-2s. Para ditado longo e transcricao.

  A Republica usa OS DOIS. Cada um no seu lugar:
  - Vosk no GATILHO (hotword + comando). Sempre on.
  - Whisper no aprofundamento. Sob demanda.

  Ninguem precisa escolher entre rapido e preciso.
  O sistema escolhe sozinho baseado no contexto.

OUTPUT ADAPTATIVO:

  O MESMO conhecimento. Entregue de N formas.
  Cego OUVE (Iara). Surdo VE (terminal alto contraste).
  Tetraplegico TATEIA (braille). Baixa visao LE (fonte grande).

  O conhecimento nao muda. O canal muda.
  Porque o DIREITO ao conhecimento e o mesmo (P6).
  O que muda e como cada corpo o recebe (P2).

VOZ HUMANA vs VOZ ROBOTICA:

  Iara (Chatterbox) = voz humana. Para CONVERSA.
  Jarvis (espeak) = voz robotica. Para COMANDO.

  Quando o cidadao pergunta "ajuda tar", e uma CONVERSA.
  Iara responde natural: "Tar e para arquivar. Quer os exemplos?"

  Quando o cidadao diz "parar audio", e um COMANDO.
  Jarvis responde rapido: "OK" (voz robotica, sem frescura).

  A Republica nao usa voz robotica para conversa.
  A Republica nao usa voz humana para comando.
  Cada voz no seu lugar. Como na vida.

O PRINCIPIO FINAL:

  Documentacao acessivel nao e "feature". E DIREITO.
  Um cidadao que nao sabe usar o sistema e UM REFEM.
  Um cidadao que sabe e LIVRE.

  man pages fazem refens (so especialistas leem).
  tldr + Vosk + Iara libertam (todos entendem).

  P1: Ninguem excluido. Nem por deficiencia. Nem por documento-ao.
  P6: Conhecimento para todos. Sem excecao. Sem nuvem. Sem Big Tech.`)
}

// helpers
func truncate(s string, n int) string {
	if len(s) <= n {
		return s
	}
	return s[:n] + "..."
}

func ids(cs []CanalSaida) []string {
	res := make([]string, len(cs))
	for i, c := range cs {
		res[i] = c.ID()
	}
	return res
}

func padRight(s string, n int) string {
	if len(s) >= n {
		return s
	}
	return s + strings.Repeat(".", n-len(s))
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}