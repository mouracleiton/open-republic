# Hermes Agent -- Engenharia Reversa Caixa-Branca

## Documento 01: Arquitetura Geral e Mapa do Sistema

> Fonte: github.com/NousResearch/hermes-agent (Jul 2026)
> Metodo: analise estatica do codigo-fonte
> Escala: 1.647.405 linhas Python em 3.402 arquivos + 446 arquivos TypeScript/TSX

---

## 1. Entry Points

Tres pontos de entrada definidos em `pyproject.toml`:

```
[project.scripts]
hermes       = "hermes_cli.main:main"      # CLI principal (hermes chat, hermes gateway, etc)
hermes-agent = "run_agent:main"             # Agente programatico (API)
hermes-acp   = "acp_adapter.entry:main"    # Servidor ACP (IDE integration: VS Code, Zed, JetBrains)
```

### Fluxo de startup

```
Usuario digita "hermes"
       |
       v
hermes_cli/main.py:main()           # argparse dispatcher
       |
       +-- cmd_chat()               # modo padrao (conversa)
       +-- cmd_gateway()            # modo gateway (messaging platforms)
       +-- cmd_proxy()              # proxy OpenAI-compatible
       +-- cmd_doctor()             # diagnostico
       +-- cmd_setup()              # wizard de configuracao
       +-- ...20+ outros subcomandos
              |
              v
       hermes_bootstrap.py          # harden_import_path, UTF-8, platform quirks
              |
              v
       cli.py:HermesCLI             # interface interativa (prompt_toolkit)
              |
              v
       run_agent.py:AIAgent         # motor do agente
              |
              v
       agent/conversation_loop.py   # loop de conversacao
              |
              v
       model_tools.py               # tool dispatch
              |
              v
       LLM (OpenAI/Anthropic/xAI/etc)
```

---

## 2. Modulos Core (mapa de 3402 arquivos)

### Hierarquia de diretorios

```
hermes-agent/
|
|-- run_agent.py              # AIAgent class (entry point do agente)
|-- cli.py                    # HermesCLI (interface CLI, 780KB!)
|-- model_tools.py            # Tool definitions e dispatch
|-- toolsets.py               # Toolset registry
|-- hermes_state.py           # SessionDB (SQLite + FTS5, 487KB)
|-- hermes_constants.py       # Paths, constantes, HERMES_HOME
|-- hermes_bootstrap.py       # Startup hardening
|-- mcp_serve.py              # MCP server mode
|-- batch_runner.py           # Batch execution
|
|-- agent/                    # 162 arquivos, 114K linhas
|   |-- conversation_loop.py  # Loop principal (378KB!)
|   |-- agent_init.py         # Inicializacao (134KB)
|   |-- auxiliary_client.py   # Modelos auxiliares (392KB!)
|   |-- context_compressor.py # Compressao de contexto (276KB)
|   |-- chat_completion_helpers.py  # Helpers LLM (199KB)
|   |-- agent_runtime_helpers.py    # Runtime (167KB)
|   |-- tool_executor.py      # Execucao de tools (87KB)
|   |-- curator.py            # Skill lifecycle (87KB)
|   |-- prompt_builder.py     # Assembly do system prompt (103KB)
|   |-- model_metadata.py     # Metadados de modelos (129KB)
|   |-- credential_pool.py    # Rotacao de credenciais (130KB)
|   |-- anthropic_adapter.py  # Adapter Anthropic (129KB)
|   |-- conversation_compression.py  # Compressao (130KB)
|   |-- moa_loop.py           # Mixture-of-Agents (105KB)
|   |-- display.py            # Output formatting (57KB)
|   |-- memory_manager.py     # Memoria persistente (50KB)
|   |-- insights.py           # Analytics (46KB)
|   |-- usage_pricing.py      # Pricing/cost tracking (53KB)
|   |-- turn_context.py       # Contexto por turno (59KB)
|   |-- error_classifier.py   # Classificacao de erros (73KB)
|   |-- skill_utils.py        # Skill loading (32KB)
|   |-- redact.py             # Secret redaction (39KB)
|   |-- ...+130 outros
|
|-- tools/                    # 118 arquivos, 102K linhas
|   |-- registry.py           # Registro central de tools
|   |-- browser_tool.py       # Browser automation
|   |-- code_execution_tool.py # Sandboxed Python
|   |-- computer_use_tool.py  # Desktop control
|   |-- cronjob_tools.py      # Cron job management
|   |-- mcp_tool.py           # MCP client integration
|   |-- ...+110 outros
|
|-- gateway/                  # 80 arquivos, 92K linhas
|   |-- run.py                # GatewayRunner (245KB!)
|   |-- platforms/base.py     # Base adapter
|   |-- platforms/            # Adapters nativos
|   |-- authz_mixin.py        # Autorizacao
|   |-- config.py             # Config do gateway
|
|-- cron/                     # 11 arquivos, 9K linhas
|   |-- scheduler.py          # Scheduler principal (198KB!)
|   |-- jobs.py               # Job management (106KB)
|   |-- executions.py         # Execution tracking
|   |-- lifecycle_guard.py   # Gateway lifecycle protection
|
|-- hermes_cli/               # 216 arquivos, 185K linhas
|   |-- main.py               # CLI dispatcher (174KB)
|   |-- config.py             # DEFAULT_CONFIG (95KB)
|   |-- auth.py               # OAuth + credential pools (89KB)
|   |-- commands.py           # Slash command registry
|   |-- kanban_db.py          # Kanban SQLite (98KB)
|   |-- web_server.py         # Dashboard web (203KB)
|   |-- curator.py            # Skill curator CLI
|   |-- gateway.py            # Gateway CLI
|
|-- plugins/                  # 188 arquivos, 117K linhas
|   |-- model-providers/      # 30+ LLM providers
|   |-- platforms/            # 20+ messaging platforms
|   |-- memory/               # 7 memory backends
|   |-- browser/              # Browser providers
|   |-- web/                  # Web search providers
|   |-- image_gen/            # Image generation
|   |-- video_gen/            # Video generation
|   |-- observability/        # Langfuse, Nemo
|
|-- skills/                   # 67 arquivos (bundled skills)
|-- acp_adapter/              # 11 arquivos (IDE integration)
|-- tui_gateway/              # 16 arquivos (TUI server)
|-- ui-tui/                   # 421 arquivos TS/TSX (Ink React TUI)
|-- website/                  # Docusaurus docs (368 paginas)
|-- tests/                    # Suite de testes
```

---

## 3. Arquitetura em Camadas

```
+------------------------------------------------------------------+
|                     SURFACES (interfaces)                         |
|  CLI (cli.py)  |  TUI (ui-tui/)  |  Desktop (Electron)           |
|  Gateway (Telegram, Discord, Slack, +20)  |  ACP (IDE)            |
+------------------------------------------------------------------+
                              |
+------------------------------------------------------------------+
|                    AGENT CORE (run_agent.py)                      |
|  AIAgent class                                                   |
|  |-- conversation_loop.py (message -> LLM -> tool -> response)   |
|  |-- context_compressor.py (automatic context compression)       |
|  |-- prompt_builder.py (system prompt assembly)                  |
|  |-- tool_executor.py (tool dispatch + execution)                |
|  |-- credential_pool.py (multi-key rotation)                    |
|  |-- memory_manager.py (persistent memory)                      |
+------------------------------------------------------------------+
                              |
          +-------------------+-------------------+
          |                                       |
+-------------------+              +---------------------------+
|  TOOL SYSTEM      |              |  STATE MANAGEMENT         |
|  model_tools.py   |              |  hermes_state.py          |
|  toolsets.py      |              |  SQLite + FTS5            |
|  tools/*.py (118) |              |  SessionDB / AsyncSessionDB|
|  registry.py      |              |  WAL mode, JSON snapshots |
+-------------------+              +---------------------------+
          |
+------------------------------------------------------------------+
|                     PLUGIN SYSTEM                                 |
|  model-providers/ (30+)  |  platforms/ (20+)  |  memory/ (7)     |
|  browser/ (4)  |  web/ (8)  |  image_gen/ (7)  |  observability/ |
+------------------------------------------------------------------+
                              |
+------------------------------------------------------------------+
|                    INFRASTRUCTURE                                 |
|  cron/ (scheduler)  |  config.yaml  |  auth.json (OAuth)         |
|  ~/.hermes/ (home)  |  skills/  |  state.db (sessions)           |
+------------------------------------------------------------------+
```

---

## 4. AIAgent Class (run_agent.py)

A classe central que orquestra tudo.

### Metodos principais

| Metodo | Funcao |
|--------|--------|
| `switch_model()` | Troca modelo/provider mid-conversation |
| `interrupt()` | Interrompe geracao atual (stop button) |
| `reset_session_state()` | Reseta estado da sessao |
| `_run_codex_stream()` | Streaming com OpenAI Codex |
| `_anthropic_messages_create()` | Adapter Anthropic Messages API |
| `_interruptible_api_call()` | Chamada de API com suporte a interrupt |
| `_get_transport()` | Obtem cliente HTTP (httpx) |
| `_persist_session()` | Salva sessao no SQLite |
| `_save_trajectory()` | Salva trajectory para replay/debug |
| `_invalidate_system_prompt()` | Forca rebuild do prompt |

### Fluxo de uma mensagem

```
1. Usuario envia mensagem (CLI/Gateway/TUI)
2. HermesCLI.process_input() recebe
3. AIAgent recebe mensagem + history
4. run_conversation() em agent/conversation_loop.py:
   a. Build system prompt (prompt_builder.py)
      - Constitutional rules
      - Tool schemas
      - Memory injection
      - Skill content
      - Environment hints
   b. Call LLM (OpenAI-format messages + tools)
   c. If tool_calls in response:
      - model_tools.handle_function_call() dispatches
      - tool_executor.py runs each tool
      - Results appended to history
      - Go to (b) -- loop
   d. If text response (no tool calls):
      - Return response
      - Persist to SQLite
      - Display to user
5. Context compression triggers near token limit
```

---

## 5. 33 Toolsets Disponiveis

Cada toolset agrupa tools relacionados. Plataformas habilitam/desabilitam toolsets.

| Toolset | Categoria | Descricao |
|---------|-----------|-----------|
| `file` | Core | Read/write/search/patch files |
| `terminal` | Core | Shell commands, process management |
| `code_execution` | Core | Sandboxed Python execution |
| `web` | Core | Web search + content extraction |
| `search` | Core | Web search subset |
| `browser` | Core | Browser automation |
| `vision` | Core | Image analysis |
| `tts` | Core | Text-to-speech |
| `memory` | Core | Persistent cross-session memory |
| `skills` | Core | Skill browsing and management |
| `session_search` | Core | FTS5 past conversation search |
| `delegation` | Core | Subagent task delegation |
| `cronjob` | Core | Scheduled task management |
| `clarify` | Core | Ask user clarifying questions |
| `todo` | Core | In-session task tracking |
| `computer_use` | Desktop | Desktop control (click, type) |
| `image_gen` | Media | AI image generation |
| `video` | Media | Video analysis |
| `video_gen` | Media | Video generation |
| `x_search` | Social | X/Twitter search |
| `spotify` | Music | Spotify playback control |
| `homeassistant` | IoT | Smart home control |
| `discord` | Social | Discord integration |
| `discord_admin` | Social | Discord moderation |
| `feishu_doc` | Enterprise | Feishu documents |
| `feishu_drive` | Enterprise | Feishu drive |
| `yuanbao` | Enterprise | Yuanbao integration |
| `kanban` | Multi-agent | Work queue board |
| `debugging` | Dev | Debug/introspection tools |
| `safe` | Dev | Minimal low-risk toolset |
| `coding` | Dev | Code-focused tools |
| `project` | Dev | Project management |
| `context_engine` | Dev | Context engine plugin |

---

## 6. Agent Module (162 arquivos)

O diretorio `agent/` e o cerebro. Modulos criticos:

### Comunicacao com LLM

| Modulo | Tamanho | Funcao |
|--------|---------|--------|
| `conversation_loop.py` | 378KB | Loop principal: message -> LLM -> tools -> response |
| `chat_completion_helpers.py` | 199KB | Helpers para OpenAI-compatible chat completions |
| `anthropic_adapter.py` | 129KB | Adapter para Anthropic Messages API |
| `bedrock_adapter.py` | 65KB | Adapter AWS Bedrock |
| `gemini_native_adapter.py` | 39KB | Adapter Google Gemini |
| `vertex_adapter.py` | 9KB | Adapter Google Vertex AI |
| `codex_runtime.py` | 59KB | OpenAI Codex integration |
| `moa_loop.py` | 105KB | Mixture-of-Agents (multi-model) |

### Contexto e Prompts

| Modulo | Tamanho | Funcao |
|--------|---------|--------|
| `prompt_builder.py` | 103KB | Assembly do system prompt |
| `system_prompt.py` | 28KB | Constitutional rules, identity |
| `context_compressor.py` | 276KB | Compressao automatica de contexto |
| `conversation_compression.py` | 130KB | Compressao de conversa |
| `turn_context.py` | 59KB | Contexto por turno |
| `coding_context.py` | 40KB | Contexto de codigo (para dev) |
| `context_references.py` | 22KB | Referencias no contexto |
| `context_engine.py` | 22KB | Plugin de context engine |

### Tools e Execucao

| Modulo | Tamanho | Funcao |
|--------|---------|--------|
| `tool_executor.py` | 87KB | Executa tools chamadas pelo LLM |
| `tool_dispatch_helpers.py` | 24KB | Helpers de dispatch |
| `tool_guardrails.py` | 18KB | Guardrails de seguranca |
| `tool_result_classification.py` | 1KB | Classifica resultados |

### Credenciais e Pricing

| Modulo | Tamanho | Funcao |
|--------|---------|--------|
| `credential_pool.py` | 130KB | Rotacao de API keys (pool) |
| `credential_sources.py` | 18KB | Fontes de credenciais |
| `credential_persistence.py` | 5KB | Persistencia de credenciais |
| `usage_pricing.py` | 53KB | Tracking de custo por request |
| `credits_tracker.py` | 39KB | Tracker de creditos |
| `account_usage.py` | 36KB | Uso por conta |

### Memoria e Skills

| Modulo | Tamanho | Funcao |
|--------|---------|--------|
| `memory_manager.py` | 50KB | Memoria persistente cross-session |
| `curator.py` | 87KB | Lifecycle de skills (archive, prune) |
| `curator_backup.py` | 28KB | Backup de skills |
| `skill_utils.py` | 32KB | Loading de skills |
| `skill_commands.py` | 32KB | Slash commands de skills |
| `skill_bundles.py` | 15KB | Bundles de skills |
| `skill_preprocessing.py` | 5KB | Preprocessamento |
| `learning_graph.py` | 11KB | Grafo de aprendizado |

### Seguranca

| Modulo | Tamanho | Funcao |
|--------|---------|--------|
| `redact.py` | 39KB | Redacao de secrets em output |
| `file_safety.py` | 29KB | Seguranca de arquivos |
| `secret_scope.py` | 10KB | Escopo de secrets |
| `ssl_guard.py` | 3KB | Guard de SSL |
| `ssl_verify.py` | 2KB | Verificacao SSL |
| `message_sanitization.py` | 19KB | Saneamento de mensagens |

---

## 7. Cron System

| Modulo | Tamanho | Funcao |
|--------|---------|--------|
| `scheduler.py` | 198KB | Scheduler principal (duração, cron, ISO) |
| `jobs.py` | 106KB | CRUD de jobs, store paths |
| `blueprint_catalog.py` | 28KB | Automation blueprints |
| `scheduler_provider.py` | 15KB | CronScheduler (in-process ou externo) |
| `executions.py` | 9KB | Tracking de execucoes |
| `lifecycle_guard.py` | 6KB | Protege lifecycle do gateway |
| `suggestions.py` | 9KB | Sugestoes de cron |

Scheduler suporta:
- Duracao: `"30m"`, `"2h"`
- Cron 5-field: `"0 9 * * *"`
- ISO timestamp: one-shot
- `context_from`: encadeia jobs (output de A -> input de B)
- `no_agent=True` + `script`: job puro sem LLM (watchdog)

---

## 8. UI Layer

### TUI (Terminal UI) -- ui-tui/ (421 arquivos TypeScript/TSX)

Ink (React para terminal) TUI. Monorepo com packages:
- `hermes-ink/`: Componente principal
- Streaming chat, session list, drag-drop files
- Cmd+K palette, status bar
- Themes (VS Code Marketplace)

### TUI Gateway -- tui_gateway/ (16 arquivos Python)

Servidor que conecta a TUI ao agente:
- `server.py`: WebSocket server
- `render.py`: Renderizacao
- `project_tree.py`: Arvore de projeto
- `git_probe.py`: Git status

### ACP Adapter -- acp_adapter/ (11 arquivos)

Agent Client Protocol para IDEs:
- `server.py`: Servidor ACP
- `session.py`: Sessao IDE
- `auth.py`: Auth IDE
- `permissions.py`: Permissoes
- Suporta: VS Code, Zed, JetBrains

---

## 9. Escala do Projeto

| Metrica | Valor |
|---------|-------|
| Arquivos Python | 3.402 |
| Linhas Python | 1.647.405 |
| Arquivos TypeScript/TSX | 446 |
| Modulos agent/ | 162 arquivos |
| Modulos tools/ | 118 arquivos |
| Modulos gateway/ | 80 arquivos |
| Modulos hermes_cli/ | 216 arquivos |
| Modulos plugins/ | 188 arquivos |
| Providers LLM | 30+ |
| Plataformas messaging | 20+ |
| Backends de memoria | 7 |
| Toolsets | 33 |
| Skills bundled | 67 |
| Docs publicas | 368 |
| Maior arquivo | cli.py (780KB / 16.818 linhas) |
| Maior modulo agent/ | auxiliary_client.py (392KB) |
| Maiar modulo cron/ | scheduler.py (198KB) |

---

## 10. Fluxo de Dados (visao geral)

```
Usuario (CLI/TUI/Gateway/IDE)
    |
    | mensagem
    v
HermesCLI / GatewayRunner
    |
    | user_message + history
    v
AIAgent.run_conversation()
    |
    +-- prompt_builder.build()
    |       |-- system_prompt (identity, rules)
    |       |-- tool schemas (model_tools)
    |       |-- memory injection (memory_manager)
    |       |-- skill content (skill_utils)
    |       |-- env hints (OS, cwd, shell)
    |       |-- AGENTS.md / .hermes.md (project context)
    |
    +-- LLM call (OpenAI/Anthropic/xAI/...)
    |       |-- credential_pool picks key
    |       |-- stream_callback for streaming
    |       |-- interrupt check
    |
    +-- if tool_calls:
    |       |-- model_tools.handle_function_call()
    |       |-- tool_executor runs each tool
    |       |-- redact.py strips secrets from output
    |       |-- results -> history
    |       |-- loop back to LLM
    |
    +-- if text response:
    |       |-- display to user
    |       |-- persist to SQLite (hermes_state.py)
    |       |-- update memory
    |       |-- TTS if voice mode
    |
    +-- context compression (if near token limit)
            |-- context_compressor identifies compressable
            |-- conversation_compression summarizes
            |-- prompt_caching preserves cacheable parts
```

---

## Documentos seguintes

- `02-agent-loop.md` -- Loop de conversacao detalhado
- `03-tool-system.md` -- Sistema de tools e toolsets
- `04-gateway-messaging.md` -- Gateway e plataformas
- `05-state-management.md` -- SQLite, FTS5, sessoes
- `06-plugin-system.md` -- Plugins (providers, platforms, memory)
- `07-config-auth-cli.md` -- Config, OAuth, CLI commands
