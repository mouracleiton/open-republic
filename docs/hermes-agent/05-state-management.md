# Hermes State Management

**Arquivo fonte:** `/tmp/hermes-agent-src/hermes_state.py` (10.850 linhas)  
**Classes principais:** `SessionDB` e `AsyncSessionDB`  
**Objetivo:** Documentação do sistema de persistência SQLite do Hermes Agent (OpenRepublic — português)

---

## 1. Visão Geral

O módulo `hermes_state.py` implementa o armazenamento persistente de sessões do Hermes Agent usando **SQLite** com:

- WAL mode para leitores concorrentes + um escritor
- FTS5 para busca textual completa em mensagens
- Compressão de sessões com encadeamento via `parent_session_id`
- Suporte a múltiplas fontes (`cli`, `telegram`, `discord`, etc.)
- Snapshots JSON e `workspace_key`

---

## 2. Schema SQLite Completo

### 2.1 Tabelas Principais

```sql
CREATE TABLE IF NOT EXISTS schema_version (
    version INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS sessions (
    id TEXT PRIMARY KEY,
    source TEXT NOT NULL,
    user_id TEXT,
    session_key TEXT,
    chat_id TEXT,
    chat_type TEXT,
    thread_id TEXT,
    display_name TEXT,
    origin_json TEXT,
    expiry_finalized INTEGER DEFAULT 0,
    model TEXT,
    model_config TEXT,
    system_prompt TEXT,
    parent_session_id TEXT,
    started_at REAL NOT NULL,
    ended_at REAL,
    end_reason TEXT,
    message_count INTEGER DEFAULT 0,
    tool_call_count INTEGER DEFAULT 0,
    input_tokens INTEGER DEFAULT 0,
    output_tokens INTEGER DEFAULT 0,
    cache_read_tokens INTEGER DEFAULT 0,
    cache_write_tokens INTEGER DEFAULT 0,
    reasoning_tokens INTEGER DEFAULT 0,
    cwd TEXT,
    git_branch TEXT,
    git_repo_root TEXT,
    billing_provider TEXT,
    billing_base_url TEXT,
    billing_mode TEXT,
    estimated_cost_usd REAL,
    actual_cost_usd REAL,
    cost_status TEXT,
    cost_source TEXT,
    pricing_version TEXT,
    title TEXT,
    api_call_count INTEGER DEFAULT 0,
    handoff_state TEXT,
    handoff_platform TEXT,
    handoff_error TEXT,
    compression_failure_cooldown_until REAL,
    compression_failure_error TEXT,
    compression_fallback_streak INTEGER NOT NULL DEFAULT 0,
    compression_ineffective_count INTEGER NOT NULL DEFAULT 0,
    profile_name TEXT,
    rewind_count INTEGER NOT NULL DEFAULT 0,
    archived INTEGER NOT NULL DEFAULT 0,
    pinned INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (parent_session_id) REFERENCES sessions(id)
);

CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT NOT NULL REFERENCES sessions(id),
    role TEXT NOT NULL,
    content TEXT,
    tool_call_id TEXT,
    tool_calls TEXT,
    tool_name TEXT,
    effect_disposition TEXT,
    timestamp REAL NOT NULL,
    token_count INTEGER,
    finish_reason TEXT,
    reasoning TEXT,
    reasoning_content TEXT,
    reasoning_details TEXT,
    codex_reasoning_items TEXT,
    codex_message_items TEXT,
    platform_message_id TEXT,
    observed INTEGER DEFAULT 0,
    active INTEGER NOT NULL DEFAULT 1,
    compacted INTEGER NOT NULL DEFAULT 0,
    api_content TEXT,
    display_kind TEXT,
    display_metadata TEXT
);

CREATE TABLE IF NOT EXISTS session_model_usage (
    session_id TEXT NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,
    model TEXT NOT NULL,
    billing_provider TEXT NOT NULL DEFAULT '',
    billing_base_url TEXT NOT NULL DEFAULT '',
    billing_mode TEXT NOT NULL DEFAULT '',
    task TEXT NOT NULL DEFAULT '',
    api_call_count INTEGER NOT NULL DEFAULT 0,
    input_tokens INTEGER NOT NULL DEFAULT 0,
    output_tokens INTEGER NOT NULL DEFAULT 0,
    cache_read_tokens INTEGER NOT NULL DEFAULT 0,
    cache_write_tokens INTEGER NOT NULL DEFAULT 0,
    reasoning_tokens INTEGER NOT NULL DEFAULT 0,
    estimated_cost_usd REAL NOT NULL DEFAULT 0,
    actual_cost_usd REAL NOT NULL DEFAULT 0,
    cost_status TEXT,
    cost_source TEXT,
    first_seen REAL,
    last_seen REAL,
    PRIMARY KEY (session_id, model, billing_provider, billing_base_url, billing_mode, task)
);

CREATE TABLE IF NOT EXISTS state_meta (
    key TEXT PRIMARY KEY,
    value TEXT
);

CREATE TABLE IF NOT EXISTS gateway_routing (
    scope TEXT NOT NULL DEFAULT '',
    session_key TEXT NOT NULL,
    entry_json TEXT NOT NULL,
    updated_at REAL NOT NULL,
    PRIMARY KEY (scope, session_key)
);

CREATE TABLE IF NOT EXISTS compression_locks (
    session_id TEXT PRIMARY KEY,
    holder TEXT NOT NULL,
    acquired_at REAL NOT NULL,
    expires_at REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS async_delegations (
    delegation_id TEXT PRIMARY KEY,
    origin_session TEXT NOT NULL,
    origin_ui_session_id TEXT NOT NULL DEFAULT '',
    parent_session_id TEXT,
    state TEXT NOT NULL,
    dispatched_at REAL NOT NULL,
    completed_at REAL,
    updated_at REAL NOT NULL,
    event_json TEXT,
    result_json TEXT,
    delivery_state TEXT NOT NULL DEFAULT 'pending',
    delivery_attempts INTEGER NOT NULL DEFAULT 0,
    delivered_at REAL,
    owner_pid INTEGER,
    owner_started_at INTEGER,
    task_json TEXT,
    delivery_claim TEXT,
    delivery_claimed_at REAL
);
```

### 2.2 Índices

```sql
CREATE INDEX IF NOT EXISTS idx_sessions_source ON sessions(source);
CREATE INDEX IF NOT EXISTS idx_sessions_source_id ON sessions(source, id);
CREATE INDEX IF NOT EXISTS idx_sessions_parent ON sessions(parent_session_id);
CREATE INDEX IF NOT EXISTS idx_sessions_started ON sessions(started_at DESC);
CREATE INDEX IF NOT EXISTS idx_messages_session ON messages(session_id, timestamp);
CREATE INDEX IF NOT EXISTS idx_compression_locks_expires ON compression_locks(expires_at);
CREATE INDEX IF NOT EXISTS idx_session_model_usage_session ON session_model_usage(session_id);
CREATE INDEX IF NOT EXISTS idx_session_model_usage_model ON session_model_usage(model);
CREATE INDEX IF NOT EXISTS idx_async_delegations_delivery ON async_delegations(delivery_state, completed_at);

-- Índices adiados (após _reconcile_columns)
CREATE INDEX IF NOT EXISTS idx_messages_session_active ON messages(session_id, active, timestamp);
CREATE INDEX IF NOT EXISTS idx_messages_active_null ON messages(active) WHERE active IS NULL;
CREATE INDEX IF NOT EXISTS idx_sessions_session_key ON sessions(session_key, started_at DESC);
CREATE INDEX IF NOT EXISTS idx_sessions_gateway_peer ON sessions(source, user_id, chat_id, chat_type, thread_id, started_at DESC);
CREATE INDEX IF NOT EXISTS idx_sessions_handoff_state ON sessions(handoff_state, started_at);
```

### 2.3 FTS5 Full-Text Search

```sql
-- Tabela FTS5 principal
CREATE VIRTUAL TABLE IF NOT EXISTS messages_fts USING fts5(
    content,
    tool_name,
    tool_calls,
    content='messages',
    content_rowid='id'
);

-- Triggers de sincronização
CREATE TRIGGER IF NOT EXISTS messages_fts_insert AFTER INSERT ON messages ...;
CREATE TRIGGER IF NOT EXISTS messages_fts_delete AFTER DELETE ON messages ...;
CREATE TRIGGER IF NOT EXISTS messages_fts_update AFTER UPDATE ON messages ...;

-- View para trigram (exclui role='tool')
CREATE VIEW IF NOT EXISTS messages_fts_trigram_src AS
    SELECT id, role, content, tool_name, tool_calls
    FROM messages
    WHERE role <> 'tool';

CREATE VIRTUAL TABLE IF NOT EXISTS messages_fts_trigram USING fts5(
    content, tool_name, tool_calls,
    content='messages_fts_trigram_src',
    content_rowid='id',
    tokenize='trigram'
);

-- Triggers trigram (apenas role <> 'tool')
```

---

## 3. WAL Mode e Configurações SQLite

- **WAL mode** habilitado para permitir leitores concorrentes + um escritor (essencial para gateway multi-plataforma).
- `journal_mode=WAL`, `synchronous=NORMAL`, `busy_timeout` configurado.
- Função `_is_sqlite_wal_reset_vulnerable` detecta vulnerabilidades de reset do WAL.
- Uso de `PRAGMA` para integridade e performance.

---

## 4. Armazenamento e Recuperação de Sessões

- Cada sessão é identificada por `id` (PK) e `session_key`.
- Mensagens são armazenadas na tabela `messages` com `session_id` como FK.
- Recuperação via `get_session`, `list_sessions`, `search_messages` (FTS5).
- `workspace_key` (derivado de `cwd` + `git_repo_root`) usado para agrupar sessões por workspace.
- `profile_name` permite isolamento por perfil Hermes.

---

## 5. Session Lifecycle

### 5.1 Criação
- `create_session(source, ...)` → insere em `sessions` + primeira mensagem.

### 5.2 Resume
- `resume_session(session_id)` ou busca por `session_key` + `source`.

### 5.3 Compressão
- `conversation_compression` + `compression_locks`.
- Sessões comprimidas geram nova sessão com `parent_session_id`.
- `compression_failure_cooldown_until`, `compression_fallback_streak`.

### 5.4 Deleção
- `delete_sessions(...)` → remove mensagens + sessão (CASCADE).
- `parent_session_id` é limpo antes da deleção.

---

## 6. JSON Snapshots

- `origin_json` armazena metadados originais da sessão.
- `model_config`, `system_prompt`, `event_json`, `result_json`, `task_json` guardam estado serializado.
- `gateway_routing.entry_json` armazena rotas de gateway.

---

## 7. workspace_key

- Derivado de `cwd` + `git_repo_root` (ou `session_key`).
- Usado em `idx_sessions_session_key` e filtros de gateway.
- Permite agrupamento lógico de sessões por diretório/projeto.

---

## 8. Sistema de Migração

- Tabela `schema_version` controla versão atual.
- Função `_reconcile_columns()` adiciona colunas novas em DBs legados.
- `DEFERRED_INDEX_SQL` é executado após reconciliação.
- `fts_rebuild_high_water` / `fts_rebuild_progress` (state_meta) controlam rebuilds de FTS5.
- Migrações são aplicadas em `_ensure_schema()` e `_open_db()`.

---

**Fim do documento**