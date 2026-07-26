// open_command_reference.js
// Transpilacao fiel do Python para JavaScript (ES6)
// OpenCommandReference -- Documentacao Acessivel de Comandos (tldr + Vosk + Output Adaptativo)
// Todos os comentarios e strings em Portugues (conforme fonte)
// Node.js compativel. Estilo consistente com outros .js do diretorio.

const PlataformaTldr = {
    COMMON: { id: "common", rotulo: "Comandos comuns a todas as plataformas (~1000)" },
    LINUX: { id: "linux", rotulo: "Comandos especificos Linux (~1000)" },
    OSX: { id: "osx", rotulo: "macOS (~369)" },
    WINDOWS: { id: "windows", rotulo: "Windows (~301)" },
    ANDROID: { id: "android", rotulo: "Android (22)" },
    SUNOS: { id: "sunos", rotulo: "SunOS/Solaris (11)" },
    FREEBSD: { id: "freebsd", rotulo: "FreeBSD" },
    NETBSD: { id: "netbsd", rotulo: "NetBSD" },
    OPENBSD: { id: "openbsd", rotulo: "OpenBSD" },
    CISCO_IOS: { id: "cisco-ios", rotulo: "Cisco IOS" },
    DOS: { id: "dos", rotulo: "DOS" }
};

const IdiomaTldr = {
    PT_BR: { id: "pt_BR", rotulo: "Portugues Brasileiro (prioridade)" },
    PT_PT: { id: "pt_PT", rotulo: "Portugues de Portugal" },
    EN: { id: "en", rotulo: "Ingles (fallback universal)" }
};

const MotorSTT = {
    VOSK: { id: "vosk", rotulo: "Vosk -- leve, ~50ms, comandos curtos e hotword" },
    WHISPER: { id: "whisper", rotulo: "Whisper.cpp -- preciso, ~500ms-2s, ditado longo" }
};

const CanalSaida = {
    IARA: { id: "iara", rotulo: "Iara (Chatterbox TTS) -- voz humana natural, conversa" },
    JARVIS: { id: "jarvis", rotulo: "Jarvis (espeak-ng) -- voz robotica, comando rapido" },
    ORCA: { id: "orca", rotulo: "Orca (AT-SPI) -- leitor de tela, navegacao por tab" },
    BRLTTY: { id: "brltty", rotulo: "Brltty -- display braille, texto tatil" },
    ALTO_CONTRASTE: { id: "alto_contraste", rotulo: "Terminal alto contraste + fonte grande" },
    TERMINAL_PADRAO: { id: "terminal", rotulo: "Terminal padrao (sem adaptacao)" }
};

const TipoConsulta = {
    VOZ_VOSK: { id: "voz_vosk", rotulo: "Voz via Vosk (hotword + comando)" },
    VOZ_WHISPER: { id: "voz_whisper", rotulo: "Voz via Whisper (ditado longo)" },
    TEXTO: { id: "texto", rotulo: "Digitado no terminal" },
    IDE: { id: "ide", rotulo: "Consulta automatica da OpenInclusiveIDE" }
};

const StatusIndexacao = {
    PRONTO: { id: "pronto", rotulo: "Indexada e busca funcionando" },
    PARCIAL: { id: "parcial", rotulo: "Indexada mas sem traducao pt_BR" },
    FALLBACK_EN: { id: "fallback_en", rotulo: "So existe em ingles" },
    AUSENTE: { id: "ausente", rotulo: "Comando nao encontrado no tldr" }
};

class ExemploComando {
    constructor(descricao, comando) {
        this.descricao = descricao;
        this.comando = comando;
    }
}

class CommandPage {
    constructor(comando, titulo, descricao, link_mais_info = "", plataforma = PlataformaTldr.COMMON,
                idioma = IdiomaTldr.PT_BR, exemplos = []) {
        this.comando = comando;
        this.titulo = titulo;
        this.descricao = descricao;
        this.link_mais_info = link_mais_info;
        this.plataforma = plataforma;
        this.idioma = idioma;
        this.exemplos = exemplos;
    }

    get num_exemplos() {
        return this.exemplos.length;
    }
}

class ConfigVosk {
    constructor() {
        this.modelo = "vosk-model-small-pt-BR-0.3";
        this.modelo_path = "/usr/share/republica/models/vosk-pt-br";
        this.sample_rate = 16000;
        this.latencia_alvo_ms = 50;
        this.hotword = "ajuda";
        this.grammar_comandos = ["ajuda", "parar", "repetir", "proximo", "anterior", "mais lento", "mais rapido", "exemplo"];
    }

    get ativo() {
        return true;
    }
}

class ConfigWhisperFallback {
    constructor() {
        this.modelo = "ggml-base.pt-BR.bin";
        this.modelo_path = "/usr/share/republica/models/whisper-pt-br";
        this.latencia_alvo_ms = 2000;
        this.ativa_em = ["vosk_falhou", "ditado_longo", "transcricao_audio", "transcricao_video"];
    }
}

class ResultadoBusca {
    constructor(query, encontrou, pagina = null, status = StatusIndexacao.AUSENTE,
                alternativas = [], idioma_usado = IdiomaTldr.EN) {
        this.query = query;
        this.encontrou = encontrou;
        this.pagina = pagina;
        this.status = status;
        this.alternativas = alternativas;
        this.idioma_usado = idioma_usado;
    }
}

class EntregaOutput {
    constructor(canais_ativos = [], tipo_consulta = TipoConsulta.TEXTO, motor_stt = null,
                latencia_ms = 0, texto_entregue = "") {
        this.canais_ativos = canais_ativos;
        this.tipo_consulta = tipo_consulta;
        this.motor_stt = motor_stt;
        this.latencia_ms = latencia_ms;
        this.texto_entregue = texto_entregue;
    }
}

class PerfilSaidaUsuario {
    constructor(cego = false, surdo = false, baixa_visao = false, tetraplegico = false,
                usa_braille = false, prefere_voz_humana = true, idioma_pref = IdiomaTldr.PT_BR) {
        this.cego = cego;
        this.surdo = surdo;
        this.baixa_visao = baixa_visao;
        this.tetraplegico = tetraplegico;
        this.usa_braille = usa_braille;
        this.prefere_voz_humana = prefere_voz_humana;
        this.idioma_pref = idioma_pref;
    }

    canais() {
        let canais = [];
        if (this.cego && this.usa_braille) {
            canais.push(CanalSaida.IARA, CanalSaida.BRLTTY);
        } else if (this.cego) {
            canais.push(CanalSaida.IARA, CanalSaida.ORCA);
        }
        if (this.surdo || this.baixa_visao) {
            canais.push(CanalSaida.ALTO_CONTRASTE);
        }
        if (this.tetraplegico && this.usa_braille) {
            canais.push(CanalSaida.BRLTTY);
        }
        if (canais.length === 0) {
            canais.push(CanalSaida.TERMINAL_PADRAO);
        }
        if (this.cego && !this.prefere_voz_humana) {
            canais = canais.filter(c => c !== CanalSaida.IARA);
            canais.unshift(CanalSaida.JARVIS);
        }
        return [...new Set(canais)];
    }
}

function _init_comandos_sample() {
    return [
        new CommandPage("tar", "# tar", "Utilidade de arquivamento. Combinado com gzip ou bzip2 para compressao.",
            "https://www.gnu.org/software/tar/manual/tar.html", PlataformaTldr.COMMON, IdiomaTldr.PT_BR, [
                new ExemploComando("[c]riar um arquivo e salva-lo em um [f]icheiro:", "tar cf {{caminho/para/destino.tar}} {{caminho/para/arquivo1 caminho/para/arquivo2 ...}}"),
                new ExemploComando("[c]riar um arquivo g[z]ippado:", "tar czf {{caminho/para/destino.tar.gz}} {{caminho/para/arquivo1 caminho/para/arquivo2 ...}}"),
                new ExemploComando("E[x]trair um arquivo (comprimido) no diretorio atual [v]erbosamente:", "tar xvf {{caminho/para/origem.tar[.gz|.bz2|.xz]}}"),
                new ExemploComando("E[x]trair um arquivo no diretorio de destino:", "tar xf {{caminho/para/origem.tar}} -C {{caminho/para/diretorio}}"),
                new ExemploComando("Lis[t]ar o conteudo de um arquivo tar [v]erbosamente:", "tar tvf {{caminho/para/origem.tar}}")
            ]),
        new CommandPage("git-commit", "# git commit", "Registra alteracoes no repositorio.",
            "https://git-scm.com/docs/git-commit", PlataformaTldr.COMMON, IdiomaTldr.PT_BR, [
                new ExemploComando("Abre um editor para escrever a mensagem e commita arquivos stageados:", "git commit"),
                new ExemploComando("Commita arquivos stageados com uma mensagem especifica:", "git commit -m {{\"mensagem\"}}"),
                new ExemploComando("Auto-stageia arquivos modificados/deletados e commita:", "git commit -a -m {{\"mensagem\"}}"),
                new ExemploComando("Atualiza o ultimo commit adicionando alteracoes atuais:", "git commit --amend")
            ]),
        new CommandPage("nmap", "# nmap", "Scanner de rede. Descobre hosts, portas abertas, servicos e sistema operacional.",
            "https://nmap.org/", PlataformaTldr.LINUX, IdiomaTldr.PT_BR, [
                new ExemploComando("Escaneia as 1000 portas mais comuns de um host:", "nmap {{host_exemplo.com}}"),
                new ExemploComando("Detecta servico e versao nas portas abertas:", "nmap -sV {{host_exemplo.com}}"),
                new ExemploComando("Escaneia uma faixa de IPs (subnet):", "nmap {{192.168.1.0/24}}"),
                new ExemploComando("Detecta sistema operacional do alvo:", "nmap -O {{host_exemplo.com}}"),
                new ExemploComando("Escaneio rapido de portas (top 100):", "nmap -F {{host_exemplo.com}}"),
                new ExemploComando("Escaneio agressivo (OS + versao + scripts + traceroute):", "nmap -A {{host_exemplo.com}}")
            ]),
        new CommandPage("ffmpeg", "# ffmpeg", "Conversor de video/audio. Grava, transmite, processa multimidia.",
            "https://ffmpeg.org/ffmpeg.html", PlataformaTldr.COMMON, IdiomaTldr.PT_BR, [
                new ExemploComando("Extrai audio de um video:", "ffmpeg -i {{video.mp4}} {{audio.mp3}}"),
                new ExemploComando("Converte video para outro formato:", "ffmpeg -i {{entrada.avi}} {{saida.mp4}}"),
                new ExemploComando("Redimensiona video para 1280x720:", "ffmpeg -i {{entrada.mp4}} -s 1280x720 {{saida.mp4}}"),
                new ExemploComando("Corta os primeiros 60 segundos de um video:", "ffmpeg -ss 00:01:00 -i {{entrada.mp4}} {{saida.mp4}}"),
                new ExemploComando("Grava a tela do computador (Linux):", "ffmpeg -f x11grab -i :0.0 {{saida.mp4}}")
            ]),
        new CommandPage("find", "# find", "Busca arquivos e diretorios por nome, tipo, tamanho, data.",
            "https://www.gnu.org/software/findutils/", PlataformaTldr.COMMON, IdiomaTldr.PT_BR, [
                new ExemploComando("Busca arquivos por nome em um diretorio:", "find {{caminho/para/diretorio}} -name {{\"*.txt\"}}"),
                new ExemploComando("Busca arquivos modificados nos ultimos N dias:", "find {{caminho/para/diretorio}} -mtime -{{N}}"),
                new ExemploComando("Busca arquivos maiores que um tamanho:", "find {{caminho/para/diretorio}} -size +{{100M}}"),
                new ExemploComando("Busca e executa um comando em cada resultado:", "find {{caminho/para/diretorio}} -name {{\"*.py\"}} -exec wc -l {} \\;"),
                new ExemploComando("Apaga arquivos encontrados (pede confirmacao):", "find {{caminho/para/diretorio}} -name {{\"*.tmp\"}} -delete")
            ]),
        new CommandPage("grep", "# grep", "Busca padroes de texto dentro de arquivos.",
            "https://www.gnu.org/software/grep/", PlataformaTldr.COMMON, IdiomaTldr.PT_BR, [
                new ExemploComando("Busca por um padrao em um arquivo:", "grep {{\"padrao_de_busca\"}} {{caminho/para/arquivo}}"),
                new ExemploComando("Busca sem distinguir maiusculas/minusculas:", "grep -i {{\"padrao\"}} {{caminho/para/arquivo}}"),
                new ExemploComando("Busca recursivamente em todos os arquivos:", "grep -r {{\"padrao\"}} {{caminho/para/diretorio}}"),
                new ExemploComando("Mostra apenas o trecho correspondente (sem a linha inteira):", "grep -o {{\"padrao\"}} {{caminho/para/arquivo}}"),
                new ExemploComando("Mostra linhas ANTES e DEPOIS do contexto:", "grep -C {{3}} {{\"padrao\"}} {{caminho/para/arquivo}}")
            ]),
        new CommandPage("ssh", "# ssh", "Cliente SSH para acesso remoto seguro a outra maquina.",
            "https://www.openssh.com/", PlataformaTldr.COMMON, IdiomaTldr.PT_BR, [
                new ExemploComando("Conecta a um servidor remoto:", "ssh {{usuario}}@{{host}}"),
                new ExemploComando("Conecta usando uma porta especifica:", "ssh -p {{2222}} {{usuario}}@{{host}}"),
                new ExemploComando("Copia chave publica para o servidor (passwordless):", "ssh-copy-id {{usuario}}@{{host}}"),
                new ExemploComando("Encaminha porta local para o servidor (tunnel):", "ssh -L {{8080}}:localhost:80 {{usuario}}@{{host}}"),
                new ExemploComando("Executa um comando no servidor sem abrir shell:", "ssh {{usuario}}@{{host}} {{comando}}")
            ]),
        new CommandPage("systemctl", "# systemctl", "Gerencia servicos do systemd (init do Linux).",
            "https://www.freedesktop.org/software/systemd/man/systemctl.html", PlataformaTldr.LINUX, IdiomaTldr.PT_BR, [
                new ExemploComando("Verifica se um servico esta ativo:", "systemctl status {{servico}}"),
                new ExemploComando("Inicia um servico:", "sudo systemctl start {{servico}}"),
                new ExemploComando("Habilita um servico para iniciar no boot:", "sudo systemctl enable {{servico}}"),
                new ExemploComando("Reinicia um servico (apos config change):", "sudo systemctl restart {{servico}}"),
                new ExemploComando("Lista todos os servicos ativos:", "systemctl list-units --type=service --state=running")
            ]),
        new CommandPage("apt", "# apt", "Gerenciador de pacotes do Debian/Ubuntu/Kali.",
            "https://wiki.debian.org/Apt", PlataformaTldr.LINUX, IdiomaTldr.PT_BR, [
                new ExemploComando("Atualiza a lista de pacotes disponiveis:", "sudo apt update"),
                new ExemploComando("Instala um pacote:", "sudo apt install {{pacote}}"),
                new ExemploComando("Remove um pacote:", "sudo apt remove {{pacote}}"),
                new ExemploComando("Atualiza todos os pacotes do sistema:", "sudo apt full-upgrade"),
                new ExemploComando("Busca um pacote por nome:", "apt search {{palavra_chave}}"),
                new ExemploComando("Mostra detalhes de um pacote:", "apt show {{pacote}}")
            ]),
        new CommandPage("docker", "# docker", "Gerencia containers de aplicacao isolados.",
            "https://docs.docker.com/", PlataformaTldr.COMMON, IdiomaTldr.PT_BR, [
                new ExemploComando("Lista containers em execucao:", "docker ps"),
                new ExemploComando("Inicia um container a partir de uma imagem:", "docker run {{imagem}}"),
                new ExemploComando("Para um container em execucao:", "docker stop {{container_id}}"),
                new ExemploComando("Baixa uma imagem do Docker Hub:", "docker pull {{imagem}}"),
                new ExemploComando("Constroi uma imagem a partir de um Dockerfile:", "docker build -t {{nome_imagem}} {{caminho/para/Dockerfile}}")
            ]),
        new CommandPage("chmod", "# chmod", "Modifica permissoes de arquivos e diretorios.",
            "https://www.gnu.org/software/coreutils/chmod", PlataformaTldr.COMMON, IdiomaTldr.PT_BR, [
                new ExemploComando("Da permissao de execucao ao dono:", "chmod u+x {{caminho/para/arquivo}}"),
                new ExemploComando("Define permissoes para dono, grupo e outros (octal):", "chmod 755 {{caminho/para/arquivo}}"),
                new ExemploComando("Remove permissoes de escrita do grupo e outros:", "chmod go-w {{caminho/para/arquivo}}"),
                new ExemploComando("Aplica permissoes recursivamente em um diretorio:", "chmod -R 755 {{caminho/para/diretorio}}")
            ])
    ];
}

function _init_keywords() {
    return {
        "arquivar": ["tar", "zip"],
        "compactar": ["tar", "gzip"],
        "extrair": ["tar", "unzip"],
        "commitar": ["git-commit"],
        "git": ["git-commit"],
        "rede": ["nmap", "ssh"],
        "scanear": ["nmap"],
        "portas": ["nmap"],
        "audio": ["ffmpeg"],
        "video": ["ffmpeg"],
        "converter": ["ffmpeg"],
        "buscar": ["find", "grep"],
        "encontrar": ["find"],
        "arquivo": ["find"],
        "texto": ["grep"],
        "remoto": ["ssh"],
        "servidor": ["ssh", "systemctl"],
        "servico": ["systemctl"],
        "iniciar": ["systemctl"],
        "pacote": ["apt"],
        "instalar": ["apt"],
        "atualizar": ["apt"],
        "container": ["docker"],
        "permissao": ["chmod"]
    };
}

function parse_tldr_markdown(conteudo, plataforma, idioma = IdiomaTldr.PT_BR) {
    const linhas = conteudo.trim().split("\n");
    let titulo = "";
    let descricao_parts = [];
    let link = "";
    let exemplos = [];
    let i = 0;
    while (i < linhas.length) {
        const linha = linhas[i].trim();
        if (linha.startsWith("# ")) {
            titulo = linha;
        } else if (linha.startsWith("> ")) {
            let texto = linha.substring(2);
            const match = texto.match(/<(https?:\/\/[^>]+)>/);
            if (match) {
                link = match[1];
                texto = texto.replace(/<https?:\/\/[^>]+>/, "").trim();
            }
            if (texto) descricao_parts.push(texto);
        } else if (linha.startsWith("- ")) {
            const desc = linha.substring(2);
            if (i + 1 < linhas.length && linhas[i + 1].trim().startsWith("`")) {
                const cmd = linhas[i + 1].trim().replace(/`/g, "");
                exemplos.push(new ExemploComando(desc, cmd));
                i++;
            }
        }
        i++;
    }
    const nome_cmd = titulo.replace("# ", "").replace(" ", "-");
    return new CommandPage(nome_cmd, titulo, descricao_parts.join(" "), link, plataforma, idioma, exemplos);
}

class CommandReferenceEngine {
    constructor() {
        this.comandos = _init_comandos_sample();
        this._indice_nome = {};
        for (const c of this.comandos) {
            this._indice_nome[c.comando.toLowerCase()] = c;
        }
        this._indice_nome_canonico = {};
        for (const c of this.comandos) {
            this._indice_nome_canonico[c.comando.toLowerCase().replace(/-/g, " ")] = c;
            this._indice_nome_canonico[c.comando.toLowerCase().replace(/-/g, "-")] = c;
        }
        this.keywords = _init_keywords();
        this.vosk_config = new ConfigVosk();
        this.whisper_config = new ConfigWhisperFallback();
    }

    buscar(query, idioma_pref = IdiomaTldr.PT_BR) {
        const q = query.trim().toLowerCase();
        if (q in this._indice_nome) {
            return new ResultadoBusca(query, true, this._indice_nome[q], StatusIndexacao.PRONTO, [], this._indice_nome[q].idioma);
        }
        const q_canon = q.replace(/ /g, "-");
        if (q_canon in this._indice_nome) {
            return new ResultadoBusca(query, true, this._indice_nome[q_canon], StatusIndexacao.PRONTO, [], this._indice_nome[q_canon].idioma);
        }
        if (q in this.keywords) {
            const alts = this.keywords[q];
            for (const alt of alts) {
                if (alt in this._indice_nome) {
                    return new ResultadoBusca(query, true, this._indice_nome[alt], StatusIndexacao.PRONTO, [], this._indice_nome[alt].idioma);
                }
            }
            return new ResultadoBusca(query, false, null, StatusIndexacao.AUSENTE, alts);
        }
        const matches = this.comandos.filter(c => c.comando.toLowerCase().startsWith(q)).map(c => c.comando);
        if (matches.length > 0) {
            return new ResultadoBusca(query, false, null, StatusIndexacao.AUSENTE, matches.slice(0, 5));
        }
        return new ResultadoBusca(query, false);
    }

    buscar_multipla(termos) {
        return termos.map(t => this.buscar(t));
    }

    todos_comandos() {
        return this.comandos.map(c => c.comando).sort();
    }

    comandos_por_plataforma(plat) {
        return this.comandos.filter(c => c.plataforma === plat);
    }

    processar_comando_voz(texto_reconhecido, perfil) {
        const inicio = new Date();
        let texto = texto_reconhecido.trim().toLowerCase();
        const hotword = this.vosk_config.hotword.toLowerCase();
        let query = "";
        if (texto.startsWith(hotword)) {
            query = texto.substring(hotword.length).trim();
        } else if (texto.includes(hotword)) {
            const idx = texto.indexOf(hotword);
            query = texto.substring(idx + hotword.length).trim();
        } else {
            query = texto;
        }
        if (!query) {
            return [
                new ResultadoBusca("", false, null, StatusIndexacao.AUSENTE),
                new EntregaOutput(perfil.canais(), TipoConsulta.VOZ_VOSK, MotorSTT.VOSK, 0, "Nenhum comando reconhecido apos hotword.")
            ];
        }
        const resultado = this.buscar(query, perfil.idioma_pref);
        const texto_saida = this.formatar_saida(resultado, perfil);
        const fim = new Date();
        const lat = Math.floor((fim - inicio) / 1000);
        const entrega = new EntregaOutput(perfil.canais(), TipoConsulta.VOZ_VOSK, MotorSTT.VOSK, lat, texto_saida);
        return [resultado, entrega];
    }

    formatar_saida(resultado, perfil) {
        if (!resultado.encontrou || !resultado.pagina) {
            if (resultado.alternativas && resultado.alternativas.length > 0) {
                return `Nao encontrei '${resultado.query}'. Comandos parecidos: ${resultado.alternativas.join(", ")}`;
            }
            return `Nao encontrei '${resultado.query}'.`;
        }
        const pg = resultado.pagina;
        let linhas = [];
        linhas.push(`Comando: ${pg.comando}`);
        linhas.push(`Para que serve: ${pg.descricao}`);
        if (pg.link_mais_info) linhas.push(`Saiba mais: ${pg.link_mais_info}`);
        linhas.push("");
        linhas.push(`Exemplos (${pg.num_exemplos}):`);
        pg.exemplos.forEach((ex, i) => {
            linhas.push(`  ${i + 1}. ${ex.descricao}`);
            linhas.push(`     ${ex.comando}`);
            linhas.push("");
        });
        return linhas.join("\n");
    }

    entregar(texto, canais) {
        const entregas = {};
        for (const canal of canais) {
            if (canal === CanalSaida.IARA) {
                entregas[canal.id] = `[IARA TTS -- voz humana Chatterbox] Processando texto para sintese de voz natural...\n  -> piper --model pt-BR --text \"${texto.substring(0, 80)}...\"\n  [Voz natural falando: \"${texto.substring(0, 120)}...\"]`;
            } else if (canal === CanalSaida.JARVIS) {
                entregas[canal.id] = `[JARVIS -- espeak-ng voz robotica]\n  -> espeak-ng -v pt-BR \"${texto.substring(0, 80)}...\"\n  [Voz robotica falando: \"${texto.substring(0, 120)}...\"]`;
            } else if (canal === CanalSaida.ORCA) {
                entregas[canal.id] = `[ORCA -- leitor de tela via AT-SPI]\n  -> Texto exposto na arvore AT-SPI\n  -> Orca le com navegacao por tab/setas`;
            } else if (canal === CanalSaida.BRLTTY) {
                entregas[canal.id] = `[BRLTTY -- display braille]\n  -> Texto enviado para display braille\n  -> Linha tatil atualizada`;
            } else if (canal === CanalSaida.ALTO_CONTRASTE) {
                entregas[canal.id] = `[TERMINAL ALTO CONTRASTE]\n  Fundo preto, fonte amarela 24pt\n  ${texto}`;
            } else {
                entregas[canal.id] = texto;
            }
        }
        return entregas;
    }

    selecionar_motor_stt(duracao_audio_sec, tem_hotword) {
        if (tem_hotword && duracao_audio_sec < 5.0) return MotorSTT.VOSK;
        if (duracao_audio_sec > 10.0) return MotorSTT.WHISPER;
        return MotorSTT.WHISPER;
    }

    instrucoes_instalacao_tldr() {
        return "INSTALACAO DO TLDR-PAGES NO OPENBIGLINUX:\n\n1. Clonar o repo:\n   sudo git clone --depth 1 https://github.com/tldr-pages/tldr.git /usr/share/republica/tldr\n\n2. Indexar (parser converte markdown -> CommandPage):\n   republica-tldr-index --src /usr/share/republica/tldr/pages\n   republica-tldr-index --src /usr/share/republica/tldr/pages.pt_BR\n\n3. Instalar cliente tldr (opcional, para terminal):\n   sudo apt install tldr   # ou: cargo install tlrc\n\n4. Instalar Vosk + modelo pt-BR:\n   sudo apt install python3-vosk\n   sudo republica-vosk-setup --model pt-BR-small\n   # Baixa vosk-model-small-pt-BR-0.3 (~40MB)\n\n5. Testar:\n   ajuda tar          (texto)\n   ajuda nmap         (texto)\n   (diga) \"ajuda git\"  (voz via Vosk)\n\n6. O sistema responde no canal certo:\n   - Cego: Iara fala + Orca expoe via AT-SPI\n   - Surdo: terminal alto contraste\n   - Tetraplegico: brltty exibe + Vosk escuta\n\nCOMANDO INTEGRADOR:\n   apt install republica-command-reference\n   # Instala: tldr-pages + vosk + parser + lancador 'ajuda'";
    }

    scorecard() {
        return {
            "comandos_indexados": this.comandos.length,
            "plataformas_cobertas": new Set(this.comandos.map(c => c.plataforma.id)).size,
            "exemplos_totais": this.comandos.reduce((s, c) => s + c.num_exemplos, 0),
            "keywords_mapeadas": Object.keys(this.keywords).length,
            "motores_stt": Object.keys(MotorSTT).length,
            "canais_saida": Object.keys(CanalSaida).length,
            "vosk_latencia_alvo_ms": this.vosk_config.latencia_alvo_ms,
            "whisper_latencia_alvo_ms": this.whisper_config.latencia_alvo_ms,
            "hotword": this.vosk_config.hotword
        };
    }
}

function _demo() {
    const e = new CommandReferenceEngine();
    console.log("=".repeat(70));
    console.log("OpenCommandReference -- Documentacao Acessivel de Comandos");
    console.log("tldr-pages + Vosk dual-STT + Output Adaptativo");
    console.log("=".repeat(70));

    console.log("\n[ARQUITETURA -- 3 CAMADAS]");
    console.log(`  1. INDEXACAO: tldr-pages (~6000 comandos) clonado em /usr/share/republica/tldr/
     Parser markdown -> CommandPage. Prioridade pt_BR, fallback en.

  2. INPUT DUAL-STT:
     Vosk (50ms): hotword "ajuda" + comando curto. LEVE. Sem GPU.
     Whisper.cpp (500ms-2s): ditado longo, transcricao. PRECISO. Opcional GPU.

  3. OUTPUT ADAPTATIVO: mesmo resultado, multiplos canais simultaneos
     IARA (Chatterbox): voz humana natural -- conversa
     JARVIS (espeak-ng): voz robotica -- comando rapido
     ORCA (AT-SPI): leitor de tela -- navegacao por tab
     BRLTTY: display braille -- texto tatil
     ALTO_CONTRASTE: terminal preto/amarelo fonte 24pt`);

    console.log(`\n[COMANDOS INDEXADOS (${e.comandos.length})]`);
    for (const c of e.comandos) {
        console.log(`  ${c.comando.padEnd(20)} | ${c.plataforma.id.padEnd(8)} | ${c.num_exemplos} exemplos | ${c.descricao.substring(0, 50)}`);
    }

    console.log("\n[BUSCA POR NOME -- 'tar']");
    let r = e.buscar("tar");
    console.log(`  Encontrou: ${r.encontrou}`);
    if (r.pagina) {
        console.log(`  Comando: ${r.pagina.comando}`);
        console.log(`  Descricao: ${r.pagina.descricao}`);
        console.log(`  Exemplos (${r.pagina.num_exemplos}):`);
        for (const ex of r.pagina.exemplos) {
            console.log(`    ${ex.descricao}`);
            console.log(`    -> ${ex.comando}`);
        }
    }

    console.log("\n[BUSCA POR KEYWORD -- 'arquivar']");
    r = e.buscar("arquivar");
    console.log(`  Keyword mapeada para: ${r.alternativas ? r.alternativas.join(", ") : "N/A"}`);
    if (r.pagina) {
        console.log(`  Resultado: ${r.pagina.comando} -- ${r.pagina.descricao.substring(0, 60)}`);
    }

    console.log("\n" + "=".repeat(70));
    console.log("[CENARIO 1 -- CEGO USA VOZ]");
    console.log("=".repeat(70));
    const perfil_cego = new PerfilSaidaUsuario(true, false, false, false, false, true);
    console.log(`  Perfil: cego, prefere voz humana (Iara)`);
    console.log(`  Canais ativos: ${perfil_cego.canais().map(c => c.id).join(", ")}`);
    console.log(`  Usuario diz: 'ajuda tar'`);
    console.log(`  Vosk reconhece: 'ajuda tar' (latencia alvo: ${e.vosk_config.latencia_alvo_ms}ms)`);
    let [res, entrega] = e.processar_comando_voz("ajuda tar", perfil_cego);
    const motor_nome = entrega.motor_stt ? entrega.motor_stt.rotulo : "N/A";
    console.log(`  Motor STT: ${motor_nome}`);
    console.log(`  Latencia: ${entrega.latencia_ms}ms`);
    console.log(`  Canais entrega: ${entrega.canais_ativos.map(c => c.id).join(", ")}`);
    console.log(`\n  --- ENTREGA ---`);
    const entregas1 = e.entregar(entrega.texto_entregue, entrega.canais_ativos);
    for (const [canal_id, msg] of Object.entries(entregas1)) {
        console.log(`\n  [${canal_id}]`);
        for (const linha of msg.split("\n")) console.log(`    ${linha}`);
    }

    console.log("\n" + "=".repeat(70));
    console.log("[CENARIO 2 -- SURDO DIGITA NO TERMINAL]");
    console.log("=".repeat(70));
    const perfil_surdo = new PerfilSaidaUsuario(false, true, true);
    console.log(`  Perfil: surdo, baixa visao`);
    console.log(`  Canais ativos: ${perfil_surdo.canais().map(c => c.id).join(", ")}`);
    r = e.buscar("git-commit");
    const texto = e.formatar_saida(r, perfil_surdo);
    console.log(`\n  --- ENTREGA ---`);
    const entregas2 = e.entregar(texto, perfil_surdo.canais());
    for (const [canal_id, msg] of Object.entries(entregas2)) {
        console.log(`\n  [${canal_id}]`);
        for (const linha of msg.split("\n")) console.log(`    ${linha}`);
    }

    console.log("\n" + "=".repeat(70));
    console.log("[CENARIO 3 -- TETRAPLEGICO USA VOZ + BRAILLE]");
    console.log("=".repeat(70));
    const perfil_tetra = new PerfilSaidaUsuario(false, false, false, true, true, false);
    console.log(`  Perfil: tetraplegico, usa braille, prefere Jarvis (espeak)`);
    console.log(`  Canais ativos: ${perfil_tetra.canais().map(c => c.id).join(", ")}`);
    console.log(`  Usuario diz: 'ajuda nmap'`);
    [res, entrega] = e.processar_comando_voz("ajuda nmap", perfil_tetra);
    const motor_nome2 = entrega.motor_stt ? entrega.motor_stt.rotulo : "N/A";
    console.log(`  Motor STT: ${motor_nome2}`);
    console.log(`\n  --- ENTREGA ---`);
    const entregas3 = e.entregar(entrega.texto_entregue, entrega.canais_ativos);
    for (const [canal_id, msg] of Object.entries(entregas3)) {
        console.log(`\n  [${canal_id}]`);
        for (const linha of msg.split("\n")) console.log(`    ${linha}`);
    }

    console.log("\n[DUAL-STT -- SELECAO DE MOTOR]");
    const cenarios_stt = [
        ["Comando curto com hotword", 2.0, true],
        ["Comando curto sem hotword", 3.0, false],
        ["Ditado medio (5-10s)", 7.0, false],
        ["Ditado longo (>10s)", 30.0, false],
        ["Transcricao de reuniao (5min)", 300.0, false]
    ];
    for (const [desc, dur, hot] of cenarios_stt) {
        const motor = e.selecionar_motor_stt(dur, hot);
        console.log(`  ${desc.padEnd(40)} -> ${motor.id.padEnd(8)} (${motor.rotulo})`);
    }

    console.log("\n[INSTALACAO NO OPENBIGLINUX]");
    console.log(e.instrucoes_instalacao_tldr());

    console.log("\n[SCORECARD]");
    const sc = e.scorecard();
    for (const [k, v] of Object.entries(sc)) {
        console.log(`  ${k.padEnd(30, ".")} ${v}`);
    }

    console.log("\n[PARSER TLDR MARKDOWN]");
    const sample_md = `# tar

> Archiving utility.
> More information: <https://www.gnu.org/software/tar/manual/tar.html>.

- [c]reate an archive and write it to a [f]ile:
\`tar cf {{path/to/target.tar}} {{path/to/file1 path/to/file2 ...}}\`

- E[x]tract a (compressed) archive [f]ile:
\`tar xf {{path/to/source.tar[.gz|.bz2|.xz]}}\``;
    const pg = parse_tldr_markdown(sample_md, PlataformaTldr.COMMON, IdiomaTldr.EN);
    console.log(`  Input: markdown bruto (8 linhas)`);
    console.log(`  Output: CommandPage(comando='${pg.comando}', descricao='${pg.descricao.substring(0, 40)}...', exemplos=${pg.num_exemplos})`);
    for (const ex of pg.exemplos) {
        console.log(`    ${ex.descricao.substring(0, 60)}`);
        console.log(`    -> ${ex.comando}`);
    }

    console.log("\n" + "=".repeat(70));
    console.log("FILOSOFIA -- Documentacao como direito, nao privilegio");
    console.log("=".repeat(70));
    console.log(`POR QUE SUBSTITUIR MAN PAGES:

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
  P6: Conhecimento para todos. Sem excecao. Sem nuvem. Sem Big Tech.`);
}

if (require.main === module) {
    _demo();
}

module.exports = {
    PlataformaTldr, IdiomaTldr, MotorSTT, CanalSaida, TipoConsulta, StatusIndexacao,
    ExemploComando, CommandPage, ConfigVosk, ConfigWhisperFallback,
    ResultadoBusca, EntregaOutput, PerfilSaidaUsuario,
    CommandReferenceEngine, parse_tldr_markdown
};