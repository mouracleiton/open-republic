# Hermes Agent — Config, Auth e CLI (Documentação de Engenharia Reversa)

**Fonte:** `/tmp/hermes-agent-src/`
- `hermes_cli/config.py` (9 493 linhas) — DEFAULT_CONFIG + load/save
- `hermes_cli/auth.py` (8 855 linhas) — OAuth + credential pools
- `hermes_cli/main.py` (17 445 linhas) — CLI dispatcher
- `cli.py` (16 818 linhas) — HermesCLI
- `hermes_cli/commands.py` — slash commands registry

**Idioma:** Português (OpenRepublic)

---

## 1. Configuração (`config.yaml`)

**Localização:** `~/.hermes/config.yaml`

**DEFAULT_CONFIG** (fonte única da verdade):

### Raiz
| Chave | Default | Descrição |
|-------|---------|-----------|
| `model` | `""` | Modelo ativo global |
| `providers` | `{}` | Providers customizados |
| `fallback_providers` | `[]` | Fallback chain |
| `credential_pool_strategies` | `{}` | Estratégias de pool por provider |
| `toolsets` | `["hermes-cli"]` | Toolsets carregados |
| `max_concurrent_sessions` | `null` | Limite global de sessões |
| `max_live_sessions` | `16` | LRU de sessões em memória |

### `agent`
- `max_turns`: 90
- `gateway_timeout`: 1800s
- `restart_drain_timeout`: 0
- `build_wait_timeout`: 600s
- `api_max_retries`: 3
- `service_tier`: ""
- `tool_use_enforcement`: "auto"
- `intent_ack_continuation`: "auto"
- `task_completion_guidance`: true
- `parallel_tool_call_guidance`: true
- `environment_probe`: true
- `environment_hint`: ""
- `coding_context`: "auto"
- `coding_instructions`: ""
- `verify_guidance`: true
- `max_verify_nudges`: 3
- `verify_on_stop`: "auto"
- `gateway_timeout_warning`: 900s
- `clarify_timeout`: 3600s
- `gateway_notify_interval`: 180s
- `gateway_auto_continue_freshness`: 3600s
- `local_stream_stale_timeout`: 900s
- `image_input_mode`: "auto"
- `disabled_toolsets`: []
- `reasoning_overrides`: {}

### `terminal`
- `backend`: "local"
- `modal_mode`: "auto"
- `cwd`: "."
- `timeout`: 180s
- `daemon_term_grace_seconds`: 2.0
- `env_passthrough`: []
- `home_mode`: "auto"
- `shell_init_files`: []
- `auto_source_bashrc`: true
- `docker_image`: "nikolaik/python-nodejs:python3.11-nodejs20"
- ... (docker_*, singularity_*, modal_*, daytona_*, container_*)

### `web`, `browser`, `checkpoints`, `mcp`, `tool_output`, `tool_loop_guardrails`, `compression`, `kanban`, `prompt_caching`, `openrouter`, `bedrock`, `auxiliary.*`, `display.*`, `dashboard.*`, `privacy`, `tts.*`, `stt.*`, `voice`, `human_delay`, `context`, `memory`, `delegation`, `goals`, `moa`, `skills`, `curator`

(Ver DEFAULT_CONFIG completo no source para todas as sub-chaves.)

**Comandos CLI de config:**
- `hermes config`
- `hermes config edit`
- `hermes config get <key>`
- `hermes config set <key> <value>`
- `hermes config unset <key>`
- `hermes config wizard`

---

## 2. Sistema de Autenticação (`auth.py`)

**Arquivo de estado:** `~/.hermes/auth.json` (com file locking)

### Providers suportados
- **OAuth Device Code Flow**: Nous Portal (principal), OpenAI Codex (futuro)
- **API Keys**: OpenRouter, custom endpoints, Bedrock, etc.

### Arquitetura
- `ProviderConfig` registry
- `resolve_provider()` — priority chain
- `resolve_*_runtime_credentials()` — refresh de tokens
- `logout_command()` — limpeza de credenciais

### JWT (Nous)
- Preferred path: `access_token` scoped diretamente para inference.

---

## 3. Rotação de Credenciais

- `credential_pool_strategies` no config.yaml permite definir estratégias por provider.
- `auth.py` implementa pools + rotação automática via `resolve_*_runtime_credentials`.
- Suporte a múltiplas chaves por provider com fallback e rotação.

---

## 4. CLI Subcommands (main.py + cli.py)

**HermesCLI** (`cli.py`) é o dispatcher principal.

**Subcomandos principais identificados:**
- `hermes chat`, `hermes run`, `hermes tui`
- `hermes config` (ver seção 1)
- `hermes doctor`
- `hermes setup`
- `hermes model` (list/set)
- `hermes auth/login/logout`
- `hermes checkpoints`, `hermes skills`, `hermes curator`
- Gateway commands (`hermes gateway start/stop/restart`)
- `hermes update`, `hermes version`

---

## 5. Slash Commands Registry (`commands.py`)

Registry dinâmico de comandos internos do agente (ex.: `/attach`, `/rollback`, `/doctor`, `/model`, etc.).

Carregados via `hermes-cli` toolset + extensões de skills.

---

## 6. Perfis (Profiles)

- `~/.hermes/profiles/<name>/`
- Cada perfil tem seu próprio `config.yaml`, `auth.json`, `skills/`, `plugins/`, `memories/`
- Isolamento completo entre perfis.
- Seleção via `--profile` ou variável de ambiente.

---

## 7. Comandos Específicos

### `hermes doctor`
- Verificação de ambiente, dependências, permissões, config corrompida, auth state.

### `hermes setup`
- Wizard interativo que gera `config.yaml` + `auth.json`.

### `hermes model`
- Lista modelos disponíveis, define modelo ativo, mostra providers.

---

**Notas de engenharia reversa:**
- Toda a configuração parte de `DEFAULT_CONFIG` (deep-merge com overrides do usuário).
- `load_config()` faz fallback silencioso para defaults em caso de YAML inválido (com backup `.bak`).
- Auth é cross-process safe via file locking.
- CLI é extremamente extensível via toolsets e slash commands.

---

*Documento gerado automaticamente para OpenRepublic — 26/07/2026*