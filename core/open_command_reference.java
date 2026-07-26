// OpenCommandReference.java
// Transpilacao fiel do Python para Java
// Documentacao Acessivel de Comandos (tldr + Vosk + Output Adaptativo)
// Todos os comentarios e strings em Portugues (conforme fonte)

import java.util.*;
import java.util.stream.Collectors;
import java.time.*;

public class OpenCommandReference {

    // ========================================================================
    // 1. ENUMS
    // ========================================================================

    public enum PlataformaTldr {
        COMMON("common", "Comandos comuns a todas as plataformas (~1000)"),
        LINUX("linux", "Comandos especificos Linux (~1000)"),
        OSX("osx", "macOS (~369)"),
        WINDOWS("windows", "Windows (~301)"),
        ANDROID("android", "Android (22)"),
        SUNOS("sunos", "SunOS/Solaris (11)"),
        FREEBSD("freebsd", "FreeBSD"),
        NETBSD("netbsd", "NetBSD"),
        OPENBSD("openbsd", "OpenBSD"),
        CISCO_IOS("cisco-ios", "Cisco IOS"),
        DOS("dos", "DOS");

        private final String id;
        private final String rotulo;

        PlataformaTldr(String id, String rotulo) {
            this.id = id;
            this.rotulo = rotulo;
        }

        public String getId() { return id; }
        public String getRotulo() { return rotulo; }
    }

    public enum IdiomaTldr {
        PT_BR("pt_BR", "Portugues Brasileiro (prioridade)"),
        PT_PT("pt_PT", "Portugues de Portugal"),
        EN("en", "Ingles (fallback universal)");

        private final String id;
        private final String rotulo;

        IdiomaTldr(String id, String rotulo) {
            this.id = id;
            this.rotulo = rotulo;
        }

        public String getId() { return id; }
        public String getRotulo() { return rotulo; }
    }

    public enum MotorSTT {
        VOSK("vosk", "Vosk -- leve, ~50ms, comandos curtos e hotword"),
        WHISPER("whisper", "Whisper.cpp -- preciso, ~500ms-2s, ditado longo");

        private final String id;
        private final String rotulo;

        MotorSTT(String id, String rotulo) {
            this.id = id;
            this.rotulo = rotulo;
        }

        public String getId() { return id; }
        public String getRotulo() { return rotulo; }
    }

    public enum CanalSaida {
        IARA("iara", "Iara (Chatterbox TTS) -- voz humana natural, conversa"),
        JARVIS("jarvis", "Jarvis (espeak-ng) -- voz robotica, comando rapido"),
        ORCA("orca", "Orca (AT-SPI) -- leitor de tela, navegacao por tab"),
        BRLTTY("brltty", "Brltty -- display braille, texto tatil"),
        ALTO_CONTRASTE("alto_contraste", "Terminal alto contraste + fonte grande"),
        TERMINAL_PADRAO("terminal", "Terminal padrao (sem adaptacao)");

        private final String id;
        private final String rotulo;

        CanalSaida(String id, String rotulo) {
            this.id = id;
            this.rotulo = rotulo;
        }

        public String getId() { return id; }
        public String getRotulo() { return rotulo; }
    }

    public enum TipoConsulta {
        VOZ_VOSK("voz_vosk", "Voz via Vosk (hotword + comando)"),
        VOZ_WHISPER("voz_whisper", "Voz via Whisper (ditado longo)"),
        TEXTO("texto", "Digitado no terminal"),
        IDE("ide", "Consulta automatica da OpenInclusiveIDE");

        private final String id;
        private final String rotulo;

        TipoConsulta(String id, String rotulo) {
            this.id = id;
            this.rotulo = rotulo;
        }

        public String getId() { return id; }
        public String getRotulo() { return rotulo; }
    }

    public enum StatusIndexacao {
        PRONTO("pronto", "Indexada e busca funcionando"),
        PARCIAL("parcial", "Indexada mas sem traducao pt_BR"),
        FALLBACK_EN("fallback_en", "So existe em ingles"),
        AUSENTE("ausente", "Comando nao encontrado no tldr");

        private final String id;
        private final String rotulo;

        StatusIndexacao(String id, String rotulo) {
            this.id = id;
            this.rotulo = rotulo;
        }

        public String getId() { return id; }
        public String getRotulo() { return rotulo; }
    }

    // ========================================================================
    // 2. CLASSES DE DADOS (dataclasses)
    // ========================================================================

    public static class ExemploComando {
        public final String descricao;
        public final String comando;

        public ExemploComando(String descricao, String comando) {
            this.descricao = descricao;
            this.comando = comando;
        }
    }

    public static class CommandPage {
        public final String comando;
        public final String titulo;
        public final String descricao;
        public final String link_mais_info;
        public final PlataformaTldr plataforma;
        public final IdiomaTldr idioma;
        public final List<ExemploComando> exemplos;

        public CommandPage(String comando, String titulo, String descricao, String link_mais_info,
                           PlataformaTldr plataforma, IdiomaTldr idioma, List<ExemploComando> exemplos) {
            this.comando = comando;
            this.titulo = titulo;
            this.descricao = descricao;
            this.link_mais_info = link_mais_info;
            this.plataforma = plataforma;
            this.idioma = idioma;
            this.exemplos = exemplos != null ? exemplos : new ArrayList<>();
        }

        public int getNumExemplos() {
            return exemplos.size();
        }
    }

    public static class ConfigVosk {
        public String modelo = "vosk-model-small-pt-BR-0.3";
        public String modelo_path = "/usr/share/republica/models/vosk-pt-br";
        public int sample_rate = 16000;
        public int latencia_alvo_ms = 50;
        public String hotword = "ajuda";
        public List<String> grammar_comandos = Arrays.asList("ajuda", "parar", "repetir", "proximo", "anterior", "mais lento", "mais rapido", "exemplo");

        public boolean isAtivo() {
            return true;
        }
    }

    public static class ConfigWhisperFallback {
        public String modelo = "ggml-base.pt-BR.bin";
        public String modelo_path = "/usr/share/republica/models/whisper-pt-br";
        public int latencia_alvo_ms = 2000;
        public List<String> ativa_em = Arrays.asList("vosk_falhou", "ditado_longo", "transcricao_audio", "transcricao_video");
    }

    public static class ResultadoBusca {
        public final String query;
        public final boolean encontrou;
        public final CommandPage pagina;
        public final StatusIndexacao status;
        public final List<String> alternativas;
        public final IdiomaTldr idioma_usado;

        public ResultadoBusca(String query, boolean encontrou, CommandPage pagina, StatusIndexacao status,
                              List<String> alternativas, IdiomaTldr idioma_usado) {
            this.query = query;
            this.encontrou = encontrou;
            this.pagina = pagina;
            this.status = status;
            this.alternativas = alternativas != null ? alternativas : new ArrayList<>();
            this.idioma_usado = idioma_usado;
        }
    }

    public static class EntregaOutput {
        public final List<CanalSaida> canais_ativos;
        public final TipoConsulta tipo_consulta;
        public final MotorSTT motor_stt;
        public final int latencia_ms;
        public final String texto_entregue;

        public EntregaOutput(List<CanalSaida> canais_ativos, TipoConsulta tipo_consulta,
                             MotorSTT motor_stt, int latencia_ms, String texto_entregue) {
            this.canais_ativos = canais_ativos != null ? canais_ativos : new ArrayList<>();
            this.tipo_consulta = tipo_consulta;
            this.motor_stt = motor_stt;
            this.latencia_ms = latencia_ms;
            this.texto_entregue = texto_entregue != null ? texto_entregue : "";
        }
    }

    public static class PerfilSaidaUsuario {
        public boolean cego = false;
        public boolean surdo = false;
        public boolean baixa_visao = false;
        public boolean tetraplegico = false;
        public boolean usa_braille = false;
        public boolean prefere_voz_humana = true;
        public IdiomaTldr idioma_pref = IdiomaTldr.PT_BR;

        public List<CanalSaida> canais() {
            List<CanalSaida> canais = new ArrayList<>();
            if (cego && usa_braille) {
                canais.add(CanalSaida.IARA);
                canais.add(CanalSaida.BRLTTY);
            } else if (cego) {
                canais.add(CanalSaida.IARA);
                canais.add(CanalSaida.ORCA);
            }
            if (surdo || baixa_visao) {
                canais.add(CanalSaida.ALTO_CONTRASTE);
            }
            if (tetraplegico && usa_braille) {
                canais.add(CanalSaida.BRLTTY);
            }
            if (canais.isEmpty()) {
                canais.add(CanalSaida.TERMINAL_PADRAO);
            }
            if (cego && !prefere_voz_humana) {
                canais.remove(CanalSaida.IARA);
                canais.add(0, CanalSaida.JARVIS);
            }
            return new ArrayList<>(new LinkedHashSet<>(canais));
        }
    }

    // ========================================================================
    // 3. DADOS SAMPLE E METODOS AUXILIARES
    // ========================================================================

    private static List<CommandPage> initComandosSample() {
        List<CommandPage> cmds = new ArrayList<>();

        cmds.add(new CommandPage("tar", "# tar", "Utilidade de arquivamento. Combinado com gzip ou bzip2 para compressao.",
                "https://www.gnu.org/software/tar/manual/tar.html", PlataformaTldr.COMMON, IdiomaTldr.PT_BR,
                Arrays.asList(
                        new ExemploComando("[c]riar um arquivo e salva-lo em um [f]icheiro:", "tar cf {{caminho/para/destino.tar}} {{caminho/para/arquivo1 caminho/para/arquivo2 ...}}"),
                        new ExemploComando("[c]riar um arquivo g[z]ippado:", "tar czf {{caminho/para/destino.tar.gz}} {{caminho/para/arquivo1 caminho/para/arquivo2 ...}}"),
                        new ExemploComando("E[x]trair um arquivo (comprimido) no diretorio atual [v]erbosamente:", "tar xvf {{caminho/para/origem.tar[.gz|.bz2|.xz]}}"),
                        new ExemploComando("E[x]trair um arquivo no diretorio de destino:", "tar xf {{caminho/para/origem.tar}} -C {{caminho/para/diretorio}}"),
                        new ExemploComando("Lis[t]ar o conteudo de um arquivo tar [v]erbosamente:", "tar tvf {{caminho/para/origem.tar}}")
                )));

        cmds.add(new CommandPage("git-commit", "# git commit", "Registra alteracoes no repositorio.",
                "https://git-scm.com/docs/git-commit", PlataformaTldr.COMMON, IdiomaTldr.PT_BR,
                Arrays.asList(
                        new ExemploComando("Abre um editor para escrever a mensagem e commita arquivos stageados:", "git commit"),
                        new ExemploComando("Commita arquivos stageados com uma mensagem especifica:", "git commit -m {{\"mensagem\"}}"),
                        new ExemploComando("Auto-stageia arquivos modificados/deletados e commita:", "git commit -a -m {{\"mensagem\"}}"),
                        new ExemploComando("Atualiza o ultimo commit adicionando alteracoes atuais:", "git commit --amend")
                )));

        cmds.add(new CommandPage("nmap", "# nmap", "Scanner de rede. Descobre hosts, portas abertas, servicos e sistema operacional.",
                "https://nmap.org/", PlataformaTldr.LINUX, IdiomaTldr.PT_BR,
                Arrays.asList(
                        new ExemploComando("Escaneia as 1000 portas mais comuns de um host:", "nmap {{host_exemplo.com}}"),
                        new ExemploComando("Detecta servico e versao nas portas abertas:", "nmap -sV {{host_exemplo.com}}"),
                        new ExemploComando("Escaneia uma faixa de IPs (subnet):", "nmap {{192.168.1.0/24}}"),
                        new ExemploComando("Detecta sistema operacional do alvo:", "nmap -O {{host_exemplo.com}}"),
                        new ExemploComando("Escaneio rapido de portas (top 100):", "nmap -F {{host_exemplo.com}}"),
                        new ExemploComando("Escaneio agressivo (OS + versao + scripts + traceroute):", "nmap -A {{host_exemplo.com}}")
                )));

        cmds.add(new CommandPage("ffmpeg", "# ffmpeg", "Conversor de video/audio. Grava, transmite, processa multimidia.",
                "https://ffmpeg.org/ffmpeg.html", PlataformaTldr.COMMON, IdiomaTldr.PT_BR,
                Arrays.asList(
                        new ExemploComando("Extrai audio de um video:", "ffmpeg -i {{video.mp4}} {{audio.mp3}}"),
                        new ExemploComando("Converte video para outro formato:", "ffmpeg -i {{entrada.avi}} {{saida.mp4}}"),
                        new ExemploComando("Redimensiona video para 1280x720:", "ffmpeg -i {{entrada.mp4}} -s 1280x720 {{saida.mp4}}"),
                        new ExemploComando("Corta os primeiros 60 segundos de um video:", "ffmpeg -ss 00:01:00 -i {{entrada.mp4}} {{saida.mp4}}"),
                        new ExemploComando("Grava a tela do computador (Linux):", "ffmpeg -f x11grab -i :0.0 {{saida.mp4}}")
                )));

        cmds.add(new CommandPage("find", "# find", "Busca arquivos e diretorios por nome, tipo, tamanho, data.",
                "https://www.gnu.org/software/findutils/", PlataformaTldr.COMMON, IdiomaTldr.PT_BR,
                Arrays.asList(
                        new ExemploComando("Busca arquivos por nome em um diretorio:", "find {{caminho/para/diretorio}} -name {{\"*.txt\"}}"),
                        new ExemploComando("Busca arquivos modificados nos ultimos N dias:", "find {{caminho/para/diretorio}} -mtime -{{N}}"),
                        new ExemploComando("Busca arquivos maiores que um tamanho:", "find {{caminho/para/diretorio}} -size +{{100M}}"),
                        new ExemploComando("Busca e executa um comando em cada resultado:", "find {{caminho/para/diretorio}} -name {{\"*.py\"}} -exec wc -l {} \\;"),
                        new ExemploComando("Apaga arquivos encontrados (pede confirmacao):", "find {{caminho/para/diretorio}} -name {{\"*.tmp\"}} -delete")
                )));

        cmds.add(new CommandPage("grep", "# grep", "Busca padroes de texto dentro de arquivos.",
                "https://www.gnu.org/software/grep/", PlataformaTldr.COMMON, IdiomaTldr.PT_BR,
                Arrays.asList(
                        new ExemploComando("Busca por um padrao em um arquivo:", "grep {{\"padrao_de_busca\"}} {{caminho/para/arquivo}}"),
                        new ExemploComando("Busca sem distinguir maiusculas/minusculas:", "grep -i {{\"padrao\"}} {{caminho/para/arquivo}}"),
                        new ExemploComando("Busca recursivamente em todos os arquivos:", "grep -r {{\"padrao\"}} {{caminho/para/diretorio}}"),
                        new ExemploComando("Mostra apenas o trecho correspondente (sem a linha inteira):", "grep -o {{\"padrao\"}} {{caminho/para/arquivo}}"),
                        new ExemploComando("Mostra linhas ANTES e DEPOIS do contexto:", "grep -C {{3}} {{\"padrao\"}} {{caminho/para/arquivo}}")
                )));

        cmds.add(new CommandPage("ssh", "# ssh", "Cliente SSH para acesso remoto seguro a outra maquina.",
                "https://www.openssh.com/", PlataformaTldr.COMMON, IdiomaTldr.PT_BR,
                Arrays.asList(
                        new ExemploComando("Conecta a um servidor remoto:", "ssh {{usuario}}@{{host}}"),
                        new ExemploComando("Conecta usando uma porta especifica:", "ssh -p {{2222}} {{usuario}}@{{host}}"),
                        new ExemploComando("Copia chave publica para o servidor (passwordless):", "ssh-copy-id {{usuario}}@{{host}}"),
                        new ExemploComando("Encaminha porta local para o servidor (tunnel):", "ssh -L {{8080}}:localhost:80 {{usuario}}@{{host}}"),
                        new ExemploComando("Executa um comando no servidor sem abrir shell:", "ssh {{usuario}}@{{host}} {{comando}}")
                )));

        cmds.add(new CommandPage("systemctl", "# systemctl", "Gerencia servicos do systemd (init do Linux).",
                "https://www.freedesktop.org/software/systemd/man/systemctl.html", PlataformaTldr.LINUX, IdiomaTldr.PT_BR,
                Arrays.asList(
                        new ExemploComando("Verifica se um servico esta ativo:", "systemctl status {{servico}}"),
                        new ExemploComando("Inicia um servico:", "sudo systemctl start {{servico}}"),
                        new ExemploComando("Habilita um servico para iniciar no boot:", "sudo systemctl enable {{servico}}"),
                        new ExemploComando("Reinicia um servico (apos config change):", "sudo systemctl restart {{servico}}"),
                        new ExemploComando("Lista todos os servicos ativos:", "systemctl list-units --type=service --state=running")
                )));

        cmds.add(new CommandPage("apt", "# apt", "Gerenciador de pacotes do Debian/Ubuntu/Kali.",
                "https://wiki.debian.org/Apt", PlataformaTldr.LINUX, IdiomaTldr.PT_BR,
                Arrays.asList(
                        new ExemploComando("Atualiza a lista de pacotes disponiveis:", "sudo apt update"),
                        new ExemploComando("Instala um pacote:", "sudo apt install {{pacote}}"),
                        new ExemploComando("Remove um pacote:", "sudo apt remove {{pacote}}"),
                        new ExemploComando("Atualiza todos os pacotes do sistema:", "sudo apt full-upgrade"),
                        new ExemploComando("Busca um pacote por nome:", "apt search {{palavra_chave}}"),
                        new ExemploComando("Mostra detalhes de um pacote:", "apt show {{pacote}}")
                )));

        cmds.add(new CommandPage("docker", "# docker", "Gerencia containers de aplicacao isolados.",
                "https://docs.docker.com/", PlataformaTldr.COMMON, IdiomaTldr.PT_BR,
                Arrays.asList(
                        new ExemploComando("Lista containers em execucao:", "docker ps"),
                        new ExemploComando("Inicia um container a partir de uma imagem:", "docker run {{imagem}}"),
                        new ExemploComando("Para um container em execucao:", "docker stop {{container_id}}"),
                        new ExemploComando("Baixa uma imagem do Docker Hub:", "docker pull {{imagem}}"),
                        new ExemploComando("Constroi uma imagem a partir de um Dockerfile:", "docker build -t {{nome_imagem}} {{caminho/para/Dockerfile}}")
                )));

        cmds.add(new CommandPage("chmod", "# chmod", "Modifica permissoes de arquivos e diretorios.",
                "https://www.gnu.org/software/coreutils/chmod", PlataformaTldr.COMMON, IdiomaTldr.PT_BR,
                Arrays.asList(
                        new ExemploComando("Da permissao de execucao ao dono:", "chmod u+x {{caminho/para/arquivo}}"),
                        new ExemploComando("Define permissoes para dono, grupo e outros (octal):", "chmod 755 {{caminho/para/arquivo}}"),
                        new ExemploComando("Remove permissoes de escrita do grupo e outros:", "chmod go-w {{caminho/para/arquivo}}"),
                        new ExemploComando("Aplica permissoes recursivamente em um diretorio:", "chmod -R 755 {{caminho/para/diretorio}}")
                )));

        return cmds;
    }

    private static Map<String, List<String>> initKeywords() {
        Map<String, List<String>> kw = new HashMap<>();
        kw.put("arquivar", Arrays.asList("tar", "zip"));
        kw.put("compactar", Arrays.asList("tar", "gzip"));
        kw.put("extrair", Arrays.asList("tar", "unzip"));
        kw.put("commitar", Arrays.asList("git-commit"));
        kw.put("git", Arrays.asList("git-commit"));
        kw.put("rede", Arrays.asList("nmap", "ssh"));
        kw.put("scanear", Arrays.asList("nmap"));
        kw.put("portas", Arrays.asList("nmap"));
        kw.put("audio", Arrays.asList("ffmpeg"));
        kw.put("video", Arrays.asList("ffmpeg"));
        kw.put("converter", Arrays.asList("ffmpeg"));
        kw.put("buscar", Arrays.asList("find", "grep"));
        kw.put("encontrar", Arrays.asList("find"));
        kw.put("arquivo", Arrays.asList("find"));
        kw.put("texto", Arrays.asList("grep"));
        kw.put("remoto", Arrays.asList("ssh"));
        kw.put("servidor", Arrays.asList("ssh", "systemctl"));
        kw.put("servico", Arrays.asList("systemctl"));
        kw.put("iniciar", Arrays.asList("systemctl"));
        kw.put("pacote", Arrays.asList("apt"));
        kw.put("instalar", Arrays.asList("apt"));
        kw.put("atualizar", Arrays.asList("apt"));
        kw.put("container", Arrays.asList("docker"));
        kw.put("permissao", Arrays.asList("chmod"));
        return kw;
    }

    // ========================================================================
    // 4. PARSER
    // ========================================================================

    public static CommandPage parseTldrMarkdown(String conteudo, PlataformaTldr plataforma, IdiomaTldr idioma) {
        String[] linhas = conteudo.trim().split("\n");
        String titulo = "";
        List<String> descricaoParts = new ArrayList<>();
        String link = "";
        List<ExemploComando> exemplos = new ArrayList<>();

        for (int i = 0; i < linhas.length; i++) {
            String linha = linhas[i].trim();
            if (linha.startsWith("# ")) {
                titulo = linha;
            } else if (linha.startsWith("> ")) {
                String texto = linha.substring(2);
                java.util.regex.Matcher m = java.util.regex.Pattern.compile("<(https?://[^>]+)>").matcher(texto);
                if (m.find()) {
                    link = m.group(1);
                    texto = texto.replaceAll("<https?://[^>]+>", "").trim();
                }
                if (!texto.isEmpty()) descricaoParts.add(texto);
            } else if (linha.startsWith("- ")) {
                String desc = linha.substring(2);
                if (i + 1 < linhas.length && linhas[i + 1].trim().startsWith("`")) {
                    String cmd = linhas[i + 1].trim().replace("`", "");
                    exemplos.add(new ExemploComando(desc, cmd));
                    i++;
                }
            }
        }

        String nomeCmd = titulo.replace("# ", "").replace(" ", "-");
        return new CommandPage(nomeCmd, titulo, String.join(" ", descricaoParts), link, plataforma, idioma, exemplos);
    }

    // ========================================================================
    // 5. ENGINE
    // ========================================================================

    public static class CommandReferenceEngine {
        public List<CommandPage> comandos;
        private Map<String, CommandPage> indiceNome;
        private Map<String, CommandPage> indiceNomeCanonico;
        public Map<String, List<String>> keywords;
        public ConfigVosk voskConfig;
        public ConfigWhisperFallback whisperConfig;

        public CommandReferenceEngine() {
            this.comandos = initComandosSample();
            this.indiceNome = new HashMap<>();
            this.indiceNomeCanonico = new HashMap<>();
            for (CommandPage c : comandos) {
                indiceNome.put(c.comando.toLowerCase(), c);
                indiceNomeCanonico.put(c.comando.toLowerCase().replace("-", " "), c);
                indiceNomeCanonico.put(c.comando.toLowerCase().replace("-", "-"), c);
            }
            this.keywords = initKeywords();
            this.voskConfig = new ConfigVosk();
            this.whisperConfig = new ConfigWhisperFallback();
        }

        public ResultadoBusca buscar(String query, IdiomaTldr idiomaPref) {
            String q = query.trim().toLowerCase();

            if (indiceNome.containsKey(q)) {
                CommandPage p = indiceNome.get(q);
                return new ResultadoBusca(query, true, p, StatusIndexacao.PRONTO, new ArrayList<>(), p.idioma);
            }

            String qCanon = q.replace(" ", "-");
            if (indiceNome.containsKey(qCanon)) {
                CommandPage p = indiceNome.get(qCanon);
                return new ResultadoBusca(query, true, p, StatusIndexacao.PRONTO, new ArrayList<>(), p.idioma);
            }

            if (keywords.containsKey(q)) {
                List<String> alts = keywords.get(q);
                for (String alt : alts) {
                    if (indiceNome.containsKey(alt)) {
                        CommandPage p = indiceNome.get(alt);
                        return new ResultadoBusca(query, true, p, StatusIndexacao.PRONTO, new ArrayList<>(), p.idioma);
                    }
                }
                return new ResultadoBusca(query, false, null, StatusIndexacao.AUSENTE, alts, IdiomaTldr.EN);
            }

            List<String> matches = comandos.stream()
                    .filter(c -> c.comando.toLowerCase().startsWith(q))
                    .map(c -> c.comando).limit(5).collect(Collectors.toList());
            if (!matches.isEmpty()) {
                return new ResultadoBusca(query, false, null, StatusIndexacao.AUSENTE, matches, IdiomaTldr.EN);
            }

            return new ResultadoBusca(query, false, null, StatusIndexacao.AUSENTE, new ArrayList<>(), IdiomaTldr.EN);
        }

        public List<ResultadoBusca> buscarMultipla(List<String> termos) {
            List<ResultadoBusca> res = new ArrayList<>();
            for (String t : termos) res.add(buscar(t, IdiomaTldr.PT_BR));
            return res;
        }

        public List<String> todosComandos() {
            return comandos.stream().map(c -> c.comando).sorted().collect(Collectors.toList());
        }

        public List<CommandPage> comandosPorPlataforma(PlataformaTldr plat) {
            return comandos.stream().filter(c -> c.plataforma == plat).collect(Collectors.toList());
        }

        public Object[] processarComandoVoz(String textoReconhecido, PerfilSaidaUsuario perfil) {
            Instant inicio = Instant.now();
            String texto = textoReconhecido.trim().toLowerCase();
            String hotword = voskConfig.hotword.toLowerCase();

            String query;
            if (texto.startsWith(hotword)) {
                query = texto.substring(hotword.length()).trim();
            } else if (texto.contains(hotword)) {
                int idx = texto.indexOf(hotword);
                query = texto.substring(idx + hotword.length()).trim();
            } else {
                query = texto;
            }

            if (query.isEmpty()) {
                ResultadoBusca r = new ResultadoBusca("", false, null, StatusIndexacao.AUSENTE, new ArrayList<>(), IdiomaTldr.EN);
                EntregaOutput e = new EntregaOutput(perfil.canais(), TipoConsulta.VOZ_VOSK, MotorSTT.VOSK, 0, "Nenhum comando reconhecido apos hotword.");
                return new Object[]{r, e};
            }

            ResultadoBusca resultado = buscar(query, perfil.idioma_pref);
            String textoSaida = formatarSaida(resultado, perfil);
            long lat = Duration.between(inicio, Instant.now()).toMillis();

            EntregaOutput entrega = new EntregaOutput(perfil.canais(), TipoConsulta.VOZ_VOSK, MotorSTT.VOSK, (int) lat, textoSaida);
            return new Object[]{resultado, entrega};
        }

        public String formatarSaida(ResultadoBusca resultado, PerfilSaidaUsuario perfil) {
            if (!resultado.encontrou || resultado.pagina == null) {
                if (!resultado.alternativas.isEmpty()) {
                    return "Nao encontrei '" + resultado.query + "'. Comandos parecidos: " + String.join(", ", resultado.alternativas);
                }
                return "Nao encontrei '" + resultado.query + "'.";
            }

            CommandPage pg = resultado.pagina;
            StringBuilder sb = new StringBuilder();
            sb.append("Comando: ").append(pg.comando).append("\n");
            sb.append("Para que serve: ").append(pg.descricao).append("\n");
            if (!pg.link_mais_info.isEmpty()) sb.append("Saiba mais: ").append(pg.link_mais_info).append("\n");
            sb.append("\n");
            sb.append("Exemplos (").append(pg.getNumExemplos()).append("):\n");
            int i = 1;
            for (ExemploComando ex : pg.exemplos) {
                sb.append("  ").append(i).append(". ").append(ex.descricao).append("\n");
                sb.append("     ").append(ex.comando).append("\n\n");
                i++;
            }
            return sb.toString();
        }

        public Map<String, String> entregar(String texto, List<CanalSaida> canais) {
            Map<String, String> entregas = new LinkedHashMap<>();
            for (CanalSaida canal : canais) {
                if (canal == CanalSaida.IARA) {
                    entregas.put(canal.getId(), "[IARA TTS -- voz humana Chatterbox] Processando texto para sintese de voz natural...\n  -> piper --model pt-BR --text \"" + texto.substring(0, Math.min(80, texto.length())) + "...\"\n  [Voz natural falando: \"" + texto.substring(0, Math.min(120, texto.length())) + "...\"]");
                } else if (canal == CanalSaida.JARVIS) {
                    entregas.put(canal.getId(), "[JARVIS -- espeak-ng voz robotica]\n  -> espeak-ng -v pt-BR \"" + texto.substring(0, Math.min(80, texto.length())) + "...\"\n  [Voz robotica falando: \"" + texto.substring(0, Math.min(120, texto.length())) + "...\"]");
                } else if (canal == CanalSaida.ORCA) {
                    entregas.put(canal.getId(), "[ORCA -- leitor de tela via AT-SPI]\n  -> Texto exposto na arvore AT-SPI\n  -> Orca le com navegacao por tab/setas");
                } else if (canal == CanalSaida.BRLTTY) {
                    entregas.put(canal.getId(), "[BRLTTY -- display braille]\n  -> Texto enviado para display braille\n  -> Linha tatil atualizada");
                } else if (canal == CanalSaida.ALTO_CONTRASTE) {
                    entregas.put(canal.getId(), "[TERMINAL ALTO CONTRASTE]\n  Fundo preto, fonte amarela 24pt\n  " + texto);
                } else {
                    entregas.put(canal.getId(), texto);
                }
            }
            return entregas;
        }

        public MotorSTT selecionarMotorStt(double duracaoAudioSec, boolean temHotword) {
            if (temHotword && duracaoAudioSec < 5.0) return MotorSTT.VOSK;
            if (duracaoAudioSec > 10.0) return MotorSTT.WHISPER;
            return MotorSTT.WHISPER;
        }

        public String instrucoesInstalacaoTldr() {
            return "INSTALACAO DO TLDR-PAGES NO OPENBIGLINUX:\n\n1. Clonar o repo:\n   sudo git clone --depth 1 https://github.com/tldr-pages/tldr.git /usr/share/republica/tldr\n\n2. Indexar (parser converte markdown -> CommandPage):\n   republica-tldr-index --src /usr/share/republica/tldr/pages\n   republica-tldr-index --src /usr/share/republica/tldr/pages.pt_BR\n\n3. Instalar cliente tldr (opcional, para terminal):\n   sudo apt install tldr   # ou: cargo install tlrc\n\n4. Instalar Vosk + modelo pt-BR:\n   sudo apt install python3-vosk\n   sudo republica-vosk-setup --model pt-BR-small\n   # Baixa vosk-model-small-pt-BR-0.3 (~40MB)\n\n5. Testar:\n   ajuda tar          (texto)\n   ajuda nmap         (texto)\n   (diga) \"ajuda git\"  (voz via Vosk)\n\n6. O sistema responde no canal certo:\n   - Cego: Iara fala + Orca expoe via AT-SPI\n   - Surdo: terminal alto contraste\n   - Tetraplegico: brltty exibe + Vosk escuta\n\nCOMANDO INTEGRADOR:\n   apt install republica-command-reference\n   # Instala: tldr-pages + vosk + parser + lancador 'ajuda'";
        }

        public Map<String, Object> scorecard() {
            Map<String, Object> sc = new LinkedHashMap<>();
            sc.put("comandos_indexados", comandos.size());
            sc.put("plataformas_cobertas", comandos.stream().map(c -> c.plataforma).distinct().count());
            sc.put("exemplos_totais", comandos.stream().mapToInt(CommandPage::getNumExemplos).sum());
            sc.put("keywords_mapeadas", keywords.size());
            sc.put("motores_stt", MotorSTT.values().length);
            sc.put("canais_saida", CanalSaida.values().length);
            sc.put("vosk_latencia_alvo_ms", voskConfig.latencia_alvo_ms);
            sc.put("whisper_latencia_alvo_ms", whisperConfig.latencia_alvo_ms);
            sc.put("hotword", voskConfig.hotword);
            return sc;
        }
    }

    // ========================================================================
    // 6. DEMO (main)
    // ========================================================================

    public static void main(String[] args) {
        CommandReferenceEngine e = new CommandReferenceEngine();

        System.out.println("=".repeat(70));
        System.out.println("OpenCommandReference -- Documentacao Acessivel de Comandos");
        System.out.println("tldr-pages + Vosk dual-STT + Output Adaptativo");
        System.out.println("=".repeat(70));

        System.out.println("\n[ARQUITETURA -- 3 CAMADAS]");
        System.out.println("  1. INDEXACAO: tldr-pages (~6000 comandos) clonado em /usr/share/republica/tldr/\n     Parser markdown -> CommandPage. Prioridade pt_BR, fallback en.\n\n  2. INPUT DUAL-STT:\n     Vosk (50ms): hotword \"ajuda\" + comando curto. LEVE. Sem GPU.\n     Whisper.cpp (500ms-2s): ditado longo, transcricao. PRECISO. Opcional GPU.\n\n  3. OUTPUT ADAPTATIVO: mesmo resultado, multiplos canais simultaneos\n     IARA (Chatterbox): voz humana natural -- conversa\n     JARVIS (espeak-ng): voz robotica -- comando rapido\n     ORCA (AT-SPI): leitor de tela -- navegacao por tab\n     BRLTTY: display braille -- texto tatil\n     ALTO_CONTRASTE: terminal preto/amarelo fonte 24pt\n");

        System.out.println("[COMANDOS INDEXADOS (" + e.comandos.size() + ")]");
        for (CommandPage c : e.comandos) {
            System.out.printf("  %-20s | %-8s | %d exemplos | %s%n", c.comando, c.plataforma.getId(), c.getNumExemplos(), c.descricao.substring(0, Math.min(50, c.descricao.length())));
        }

        System.out.println("\n[BUSCA POR NOME -- 'tar']");
        ResultadoBusca r = e.buscar("tar", IdiomaTldr.PT_BR);
        System.out.println("  Encontrou: " + r.encontrou);
        if (r.pagina != null) {
            System.out.println("  Comando: " + r.pagina.comando);
            System.out.println("  Descricao: " + r.pagina.descricao);
            System.out.println("  Exemplos (" + r.pagina.getNumExemplos() + "):");
            for (ExemploComando ex : r.pagina.exemplos) {
                System.out.println("    " + ex.descricao);
                System.out.println("    -> " + ex.comando);
            }
        }

        System.out.println("\n[BUSCA POR KEYWORD -- 'arquivar']");
        r = e.buscar("arquivar", IdiomaTldr.PT_BR);
        System.out.println("  Keyword mapeada para: " + (r.alternativas.isEmpty() ? "N/A" : String.join(", ", r.alternativas)));
        if (r.pagina != null) {
            System.out.println("  Resultado: " + r.pagina.comando + " -- " + r.pagina.descricao.substring(0, Math.min(60, r.pagina.descricao.length())));
        }

        System.out.println("\n" + "=".repeat(70));
        System.out.println("[CENARIO 1 -- CEGO USA VOZ]");
        System.out.println("=".repeat(70));
        PerfilSaidaUsuario perfilCego = new PerfilSaidaUsuario();
        perfilCego.cego = true;
        perfilCego.usa_braille = false;
        perfilCego.prefere_voz_humana = true;
        System.out.println("  Perfil: cego, prefere voz humana (Iara)");
        System.out.println("  Canais ativos: " + perfilCego.canais().stream().map(CanalSaida::getId).collect(Collectors.toList()));
        System.out.println("  Usuario diz: 'ajuda tar'");
        System.out.println("  Vosk reconhece: 'ajuda tar' (latencia alvo: " + e.voskConfig.latencia_alvo_ms + "ms)");
        Object[] res1 = e.processarComandoVoz("ajuda tar", perfilCego);
        ResultadoBusca r1 = (ResultadoBusca) res1[0];
        EntregaOutput entrega1 = (EntregaOutput) res1[1];
        System.out.println("  Motor STT: " + (entrega1.motor_stt != null ? entrega1.motor_stt.getRotulo() : "N/A"));
        System.out.println("  Latencia: " + entrega1.latencia_ms + "ms");
        System.out.println("  Canais entrega: " + entrega1.canais_ativos.stream().map(CanalSaida::getId).collect(Collectors.toList()));
        System.out.println("\n  --- ENTREGA ---");
        for (Map.Entry<String, String> entry : e.entregar(entrega1.texto_entregue, entrega1.canais_ativos).entrySet()) {
            System.out.println("\n  [" + entry.getKey() + "]");
            for (String linha : entry.getValue().split("\n")) {
                System.out.println("    " + linha);
            }
        }

        System.out.println("\n" + "=".repeat(70));
        System.out.println("[CENARIO 2 -- SURDO DIGITA NO TERMINAL]");
        System.out.println("=".repeat(70));
        PerfilSaidaUsuario perfilSurdo = new PerfilSaidaUsuario();
        perfilSurdo.surdo = true;
        perfilSurdo.baixa_visao = true;
        System.out.println("  Perfil: surdo, baixa visao");
        System.out.println("  Canais ativos: " + perfilSurdo.canais().stream().map(CanalSaida::getId).collect(Collectors.toList()));
        ResultadoBusca r2 = e.buscar("git-commit", IdiomaTldr.PT_BR);
        String texto2 = e.formatarSaida(r2, perfilSurdo);
        System.out.println("\n  --- ENTREGA ---");
        for (Map.Entry<String, String> entry : e.entregar(texto2, perfilSurdo.canais()).entrySet()) {
            System.out.println("\n  [" + entry.getKey() + "]");
            for (String linha : entry.getValue().split("\n")) {
                System.out.println("    " + linha);
            }
        }

        System.out.println("\n" + "=".repeat(70));
        System.out.println("[CENARIO 3 -- TETRAPLEGICO USA VOZ + BRAILLE]");
        System.out.println("=".repeat(70));
        PerfilSaidaUsuario perfilTetra = new PerfilSaidaUsuario();
        perfilTetra.tetraplegico = true;
        perfilTetra.usa_braille = true;
        perfilTetra.prefere_voz_humana = false;
        System.out.println("  Perfil: tetraplegico, usa braille, prefere Jarvis (espeak)");
        System.out.println("  Canais ativos: " + perfilTetra.canais().stream().map(CanalSaida::getId).collect(Collectors.toList()));
        System.out.println("  Usuario diz: 'ajuda nmap'");
        Object[] res3 = e.processarComandoVoz("ajuda nmap", perfilTetra);
        EntregaOutput entrega3 = (EntregaOutput) res3[1];
        System.out.println("  Motor STT: " + (entrega3.motor_stt != null ? entrega3.motor_stt.getRotulo() : "N/A"));
        System.out.println("\n  --- ENTREGA ---");
        for (Map.Entry<String, String> entry : e.entregar(entrega3.texto_entregue, entrega3.canais_ativos).entrySet()) {
            System.out.println("\n  [" + entry.getKey() + "]");
            for (String linha : entry.getValue().split("\n")) {
                System.out.println("    " + linha);
            }
        }

        System.out.println("\n[DUAL-STT -- SELECAO DE MOTOR]");
        Object[][] cenarios = {
                {"Comando curto com hotword", 2.0, true},
                {"Comando curto sem hotword", 3.0, false},
                {"Ditado medio (5-10s)", 7.0, false},
                {"Ditado longo (>10s)", 30.0, false},
                {"Transcricao de reuniao (5min)", 300.0, false}
        };
        for (Object[] cen : cenarios) {
            MotorSTT m = e.selecionarMotorStt((Double) cen[1], (Boolean) cen[2]);
            System.out.printf("  %-40s -> %-8s (%s)%n", cen[0], m.getId(), m.getRotulo());
        }

        System.out.println("\n[INSTALACAO NO OPENBIGLINUX]");
        System.out.println(e.instrucoesInstalacaoTldr());

        System.out.println("\n[SCORECARD]");
        for (Map.Entry<String, Object> entry : e.scorecard().entrySet()) {
            System.out.printf("  %.<30s %s%n", entry.getKey() + " ", entry.getValue());
        }

        System.out.println("\n[PARSER TLDR MARKDOWN]");
        String sampleMd = "# tar\n\n> Archiving utility.\n> More information: <https://www.gnu.org/software/tar/manual/tar.html>.\n\n- [c]reate an archive and write it to a [f]ile:\n\n`tar cf {{path/to/target.tar}} {{path/to/file1 path/to/file2 ...}}`\n\n- E[x]tract a (compressed) archive [f]ile:\n\n`tar xf {{path/to/source.tar[.gz|.bz2|.xz]}}`";
        CommandPage pg = parseTldrMarkdown(sampleMd, PlataformaTldr.COMMON, IdiomaTldr.EN);
        System.out.println("  Input: markdown bruto (8 linhas)");
        System.out.println("  Output: CommandPage(comando='" + pg.comando + "', descricao='" + pg.descricao.substring(0, Math.min(40, pg.descricao.length())) + "...', exemplos=" + pg.getNumExemplos() + ")");
        for (ExemploComando ex : pg.exemplos) {
            System.out.println("    " + ex.descricao.substring(0, Math.min(60, ex.descricao.length())));
            System.out.println("    -> " + ex.comando);
        }

        System.out.println("\n" + "=".repeat(70));
        System.out.println("FILOSOFIA -- Documentacao como direito, nao privilegio");
        System.out.println("=".repeat(70));
        System.out.println("POR QUE SUBSTITUIR MAN PAGES:\n\n  man tar tem 2000+ linhas. Orca le por 40 minutos.\n  tldr tar tem 8 exemplos curtos. Iara le em 30 segundos.\n\n  O cidadao nao precisa saber TUDO sobre tar.\n  Precisa saber o ENESSIMO exemplo que resolve o problema AGORA.\n\n  man pages sao para ESPECIALISTAS.\n  tldr e para CIDADAOS.\n\nDUAL-STT (VOSK + WHISPER):\n\n  Vosk e LEVE. Roda em Raspberry Pi. Roda em maquina doada.\n  Latencia de 50ms. Suficiente para \"ajuda tar\".\n\n  Whisper e PRECISO. Mas pesado. Precisa de CPU decente.\n  Latencia de 500ms-2s. Para ditado longo e transcricao.\n\n  A Republica usa OS DOIS. Cada um no seu lugar:\n  - Vosk no GATILHO (hotword + comando). Sempre on.\n  - Whisper no aprofundamento. Sob demanda.\n\n  Ninguem precisa escolher entre rapido e preciso.\n  O sistema escolhe sozinho baseado no contexto.\n\nOUTPUT ADAPTATIVO:\n\n  O MESMO conhecimento. Entregue de N formas.\n  Cego OUVE (Iara). Surdo VE (terminal alto contraste).\n  Tetraplegico TATEIA (braille). Baixa visao LE (fonte grande).\n\n  O conhecimento nao muda. O canal muda.\n  Porque o DIREITO ao conhecimento e o mesmo (P6).\n  O que muda e como cada corpo o recebe (P2).\n\nVOZ HUMANA vs VOZ ROBOTICA:\n\n  Iara (Chatterbox) = voz humana. Para CONVERSA.\n  Jarvis (espeak) = voz robotica. Para COMANDO.\n\n  Quando o cidadao pergunta \"ajuda tar\", e uma CONVERSA.\n  Iara responde natural: \"Tar e para arquivar. Quer os exemplos?\"\n\n  Quando o cidadao diz \"parar audio\", e um COMANDO.\n  Jarvis responde rapido: \"OK\" (voz robotica, sem frescura).\n\n  A Republica nao usa voz robotica para conversa.\n  A Republica nao usa voz humana para comando.\n  Cada voz no seu lugar. Como na vida.\n\nO PRINCIPIO FINAL:\n\n  Documentacao acessivel nao e \"feature\". E DIREITO.\n  Um cidadao que nao sabe usar o sistema e UM REFEM.\n  Um cidadao que sabe e LIVRE.\n\n  man pages fazem refens (so especialistas leem).\n  tldr + Vosk + Iara libertam (todos entendem).\n\n  P1: Ninguem excluido. Nem por deficiencia. Nem por documento-ao.\n  P6: Conhecimento para todos. Sem excecao. Sem nuvem. Sem Big Tech.\n");
    }
}