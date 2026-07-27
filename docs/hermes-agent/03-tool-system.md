# Hermes Tool System Documentation

**Source:** Reverse engineering of `/tmp/hermes-agent-src/`
**Files analyzed:**
- `model_tools.py` (1440 lines)
- `toolsets.py` (975 lines)  
- `tools/registry.py` (810 lines)
- 99 `.py` files in `tools/`

---

## 1. Registry.register() — How Tools Self-Register

**Location:** `tools/registry.py:217` (class `ToolRegistry`)

Every tool module calls `registry.register(...)` at **module import time** (top-level).

### Signature (inferred from usage)
```python
registry.register(
    name: str,
    toolset: str,
    schema: dict,           # OpenAI function-calling schema
    handler: Callable,
    check_fn: Optional[Callable[[], bool]] = None,
    requires_env: Optional[List[str]] = None,
    is_async: bool = False,
    description: str = "",
    emoji: str = "",
    max_result_size_chars: Optional[int] = None,
    dynamic_schema_overrides: Optional[Callable[[], dict]] = None,
)
```

### ToolEntry slots (registry.py:90-94)
```python
__slots__ = (
    "name", "toolset", "schema", "handler", "check_fn",
    "requires_env", "is_async", "description", "emoji",
    "max_result_size_chars", "dynamic_schema_overrides",
)
```

### Discovery (registry.py:67-84)
- `discover_builtin_tools()` scans `tools/*.py`
- Skips `__init__.py`, `registry.py`, `mcp_tool.py`
- Uses AST to detect top-level `registry.register(...)` calls
- Imports matching modules → triggers registration

**Result:** 74 tools registered from 34 modules.

---

## 2. Toolsets — Grouping Mechanism

**Location:** `toolsets.py`

### Core Data Structures
- `TOOLSETS: dict` — declarative definitions
- `_HERMES_CORE_TOOLS` — shared base list used by CLI/messaging
- Toolsets can reference other toolsets (composition)

### Example (toolsets.py:96+)
```python
TOOLSETS = {
    "web": {
        "description": "...",
        "tools": ["web_search", "web_extract"],
    },
    "full_stack": {
        "description": "...",
        "tools": ["web", "terminal", "code_execution", ...],  # composition
    },
    ...
}
```

### Key Functions
- `resolve_toolset(name)` — expands compositions recursively
- `get_toolset(name)` — returns raw list
- `get_all_toolsets()` — returns all defined toolsets

---

## 3. handle_function_call Flow

**Location:** `model_tools.py:13` (public API)

### High-level flow (inferred)
1. `run_agent.py` / CLI receives function call from model
2. Calls `handle_function_call(function_name, function_args, task_id, user_task)`
3. Registry lookup → `ToolEntry.handler`
4. `coerce_tool_args()` normalizes arguments
5. If `check_fn` exists → `_check_fn_cached(check_fn)` (TTL 30s + grace)
6. If async → runs on persistent event loop (`_get_tool_loop()` / worker loop)
7. Executes handler
8. Returns string result (truncated by `max_result_size_chars`)

### Async Safety (model_tools.py:52-100)
- Persistent event loops per thread (avoids "Event loop is closed")
- Worker threads (delegation) get their own `threading.local()` loop

---

## 4. check_fn and Requirements

### check_fn Caching (registry.py:120-206)
- TTL: 30 seconds
- Grace period for transient failures: 60 seconds (serves last-good `True`)
- Prevents flapping (Docker, playwright, Modal, etc.)

### TOOLSET_REQUIREMENTS (model_tools.py:15)
Exposed for `cli.py` / `doctor.py`.

Examples of gated tools:
- `computer_use` → requires `cua-driver`
- Home Assistant tools → `HASS_TOKEN`
- Kanban tools → `HERMES_KANBAN_TASK` env or profile flag
- Desktop UI tools → `HERMES_DESKTOP`

---

## 5. coerce_tool_args

**Location:** `model_tools.py` (referenced in public API)

Normalizes model-provided arguments before handler dispatch:
- Type coercion
- Default injection
- Schema validation alignment

(Exact implementation not extracted in first 100 lines; used inside `handle_function_call`.)

---

## 6. All Toolsets → Tools Mapping (Complete)

**Registry contains 74 tools across the following toolsets:**

| Toolset              | Tools |
|----------------------|-------|
| **browser**          | `browser_back`, `browser_click`, `browser_console`, `browser_get_images`, `browser_navigate`, `browser_press`, `browser_scroll`, `browser_snapshot`, `browser_type`, `browser_vision` |
| **browser-cdp**      | `browser_cdp`, `browser_dialog` |
| **clarify**          | `clarify` |
| **code_execution**   | `execute_code` |
| **computer_use**     | `computer_use` |
| **cronjob**          | `cronjob` |
| **delegation**       | `delegate_task` |
| **discord**          | `discord` |
| **discord_admin**    | `discord_admin` |
| **terminal**         | `close_terminal`, `process`, `read_terminal`, `terminal` |
| **web**              | `web_extract`, `web_search` |
| **file**             | `patch`, `read_file`, `search_files`, `write_file` |
| **vision**           | `image_generate`, `vision_analyze` |
| **skills**           | `skill_manage`, `skill_view`, `skills_list` |
| **planning**         | `todo` |
| **memory**           | `memory` |
| **session**          | `session_search` |
| **text_to_speech**   | `text_to_speech` |
| **home_assistant**   | `ha_call_service`, `ha_get_state`, `ha_list_entities`, `ha_list_services` |
| **kanban**           | `kanban_attach`, `kanban_attach_url`, `kanban_attachments`, `kanban_block`, `kanban_comment`, `kanban_complete`, `kanban_create`, `kanban_heartbeat`, `kanban_link`, `kanban_list`, `kanban_show`, `kanban_unblock` |
| **preview**          | `focus_pane`, `open_preview` |
| **webhook_safe**     | `clarify`, `vision_analyze`, `web_extract`, `web_search` (subset) |

**Additional toolsets observed in `toolsets.py`:**
- `full_stack`, `research`, `project`, `desktop`, `admin`, etc. (composed from above)

---

## Summary

- **Self-registration** via `registry.register()` at import time (AST-detected)
- **Toolsets** are declarative + composable groupings
- **check_fn** provides dynamic availability with intelligent caching
- **handle_function_call** is the single entry point for execution
- **74 tools** currently registered from 34 modules

**File written:** `/tmp/hermes-docs/03-tool-system.md`