# Hermes Agent — Plugin System

**Documentação em Português (OpenRepublic)**

---

## 1. Arquitetura de Plugins

O sistema de plugins do Hermes é baseado em **descoberta por convenção** + **interfaces abstratas (ABC)**.

### Como funciona

1. **Registro**: Plugins são pastas sob `plugins/<categoria>/<nome>/`.
2. **Descoberta**: O core importa dinamicamente `plugins.<categoria>.<nome>` quando o nome é selecionado em config/env.
3. **Carregamento**: Cada categoria define uma ABC (`MemoryProvider`, `WebSearchProvider`, `PlatformAdapter`, etc.). O plugin implementa a classe concreta.
4. **Extensão sem modificar o core**: Plugins nunca editam `agent/`, `cli.py` ou `tools/`. Eles apenas implementam a interface e são referenciados por string (ex: `memory: mem0`, `web: tavily`).

### Padrão comum de um plugin

```python
from agent.<base>_provider import <Base>Provider

class MeuProvider(<Base>Provider):
    @property
    def name(self) -> str:
        return "meu-nome"

    def is_available(self) -> bool:
        ...

    # métodos da interface...
```

O core faz algo como:

```python
from importlib import import_module
mod = import_module(f"plugins.{cat}.{name}")
provider = mod.<ClassName>()
```

---

## 2. Categorias de Plugins

| Categoria          | Diretório                        | Quantidade | Interface Principal          | Propósito |
|--------------------|----------------------------------|------------|------------------------------|---------|
| model-providers    | `plugins/model-providers/`       | 30+        | LLM provider (OpenAI compat) | Modelos de linguagem |
| platforms          | `plugins/platforms/`             | 20+        | PlatformAdapter              | Gateways (Telegram, Slack, etc.) |
| memory             | `plugins/memory/`                | 7          | MemoryProvider               | Armazenamento de memória |
| web                | `plugins/web/`                   | 8          | WebSearchProvider            | Busca web + extração |
| browser            | `plugins/browser/`               | 3          | BrowserProvider              | Automação de browser |
| image_gen          | `plugins/image_gen/`             | 7          | ImageGenProvider             | Geração de imagens |
| video_gen          | `plugins/video_gen/`             | 3          | VideoGenProvider             | Geração de vídeo |
| observability      | `plugins/observability/`         | 2          | ObservabilityProvider        | Tracing / métricas |

---

## 3. Lista Completa de Providers

### 3.1 Model Providers (30+)

| Provider              | Pasta                        | Config principal          | Notas |
|-----------------------|------------------------------|---------------------------|-------|
| openai                | model-providers/openai       | OPENAI_API_KEY            | GPT-4o, o1, etc. |
| anthropic             | model-providers/anthropic    | ANTHROPIC_API_KEY         | Claude 3.5/4 |
| gemini                | model-providers/gemini       | GEMINI_API_KEY            | Google Gemini |
| xai                   | model-providers/xai          | XAI_API_KEY               | Grok models |
| deepseek              | model-providers/deepseek     | DEEPSEEK_API_KEY          | DeepSeek-V3/R1 |
| qwen-oauth            | model-providers/qwen-oauth   | QWEN_OAUTH                | Alibaba Qwen via OAuth |
| alibaba               | model-providers/alibaba      | ALIBABA_API_KEY           | Alibaba Cloud |
| fireworks             | model-providers/fireworks    | FIREWORKS_API_KEY         | Fireworks AI |
| together (via openrouter) | —                        | —                         | Via OpenRouter |
| openrouter            | model-providers/openrouter   | OPENROUTER_API_KEY        | Agregador |
| ollama-cloud          | model-providers/ollama-cloud | OLLAMA_CLOUD_KEY          | Ollama Cloud |
| vertex                | model-providers/vertex       | GOOGLE_APPLICATION_CREDENTIALS | GCP Vertex |
| bedrock               | model-providers/bedrock      | AWS creds                 | Amazon Bedrock |
| azure-foundry         | model-providers/azure-foundry| AZURE_ vars               | Azure AI Foundry |
| huggingface           | model-providers/huggingface  | HF_TOKEN                  | HF Inference |
| nvidia                | model-providers/nvidia       | NVIDIA_API_KEY            | NVIDIA NIM |
| arcee                 | model-providers/arcee        | ARCEE_API_KEY             | Arcee AI |
| minimax               | model-providers/minimax      | MINIMAX_API_KEY           | MiniMax |
| stepfun               | model-providers/stepfun      | STEPFUN_API_KEY           | StepFun |
| upstage               | model-providers/upstage      | UPSTAGE_API_KEY           | Upstage Solar |
| nous                  | model-providers/nous         | NOUS_API_KEY              | Nous Research |
| deepinfra             | model-providers/deepinfra    | DEEPINFRA_API_KEY         | DeepInfra |
| kilocode              | model-providers/kilocode     | KILOCODE_KEY              | KiloCode |
| copilot               | model-providers/copilot      | COPILOT_ vars             | GitHub Copilot |
| copilot-acp           | model-providers/copilot-acp  | —                         | ACP variant |
| openai-codex          | model-providers/openai-codex | —                         | Codex via OpenAI |
| alibaba-coding-plan   | model-providers/alibaba-coding-plan | —                  | Alibaba coding |
| kimi-coding           | model-providers/kimi-coding  | —                         | Moonshot Kimi |
| opencode-zen          | model-providers/opencode-zen | —                         | OpenCode Zen |
| gmi                   | model-providers/gmi          | —                         | GMI Cloud |
| novita                | model-providers/novita       | NOVITA_API_KEY            | Novita AI |
| zai                   | model-providers/zai          | —                         | Z.ai |
| xiaomi                | model-providers/xiaomi       | —                         | Xiaomi |

### 3.2 Platforms (20+)

| Plataforma     | Pasta                    | Adapter principal          | Recursos |
|----------------|--------------------------|----------------------------|----------|
| telegram       | platforms/telegram       | TelegramAdapter            | Mensagens, voice, callbacks |
| slack          | platforms/slack          | SlackAdapter + BlockKit    | Rich blocks |
| discord        | platforms/discord        | DiscordAdapter             | Voice mixer, recovery |
| teams          | platforms/teams          | TeamsAdapter               | Microsoft Teams |
| wecom          | platforms/wecom          | WeComAdapter + Crypto      | WeChat Work |
| feishu         | platforms/feishu         | FeishuAdapter              | Meetings, comments |
| dingtalk       | platforms/dingtalk       | DingTalkAdapter            | Alibaba DingTalk |
| whatsapp       | platforms/whatsapp       | WhatsAppAdapter            | — |
| sms            | platforms/sms            | SMSAdapter                 | Twilio / etc. |
| email          | platforms/email          | EmailAdapter               | IMAP/SMTP |
| matrix         | platforms/matrix         | MatrixAdapter              | — |
| mattermost     | platforms/mattermost     | MattermostAdapter          | — |
| google_chat    | platforms/google_chat    | GoogleChatAdapter + OAuth  | — |
| homeassistant  | platforms/homeassistant  | HomeAssistantAdapter       | Smart home |
| ntfy           | platforms/ntfy           | NtfyAdapter                | Push notifications |
| irc            | platforms/irc            | IRCAdapter                 | — |
| line           | platforms/line           | LineAdapter                | — |
| simplex        | platforms/simplex        | SimplexAdapter             | — |
| raft           | platforms/raft           | RaftAdapter                | — |
| photon         | platforms/photon         | PhotonAdapter + sidecar    | — |

### 3.3 Memory Providers (7)

| Provider       | Pasta               | Modo                  | Config |
|----------------|---------------------|-----------------------|--------|
| mem0           | memory/mem0         | platform / oss        | MEM0_API_KEY + mem0.json |
| retaindb       | memory/retaindb     | —                     | — |
| holographic    | memory/holographic  | —                     | — |
| honcho         | memory/honcho       | —                     | — |
| byterover      | memory/byterover    | —                     | — |
| openviking     | memory/openviking   | —                     | — |
| supermemory    | memory/supermemory  | —                     | — |
| hindsight      | memory/hindsight    | —                     | — |

### 3.4 Web Search (8)

| Provider     | Pasta             | Capabilities          | Config |
|--------------|-------------------|-----------------------|--------|
| tavily       | web/tavily        | search + extract      | TAVILY_API_KEY |
| firecrawl    | web/firecrawl     | search + extract      | FIRECRAWL_API_KEY |
| exa          | web/exa           | search                | EXA_API_KEY |
| parallel     | web/parallel      | search                | PARALLEL_API_KEY |
| brave_free   | web/brave_free    | search                | BRAVE_API_KEY |
| ddgs         | web/ddgs          | search (DuckDuckGo)   | — |
| searxng      | web/searxng       | search                | SEARXNG_URL |
| xai          | web/xai           | search                | XAI_API_KEY |

### 3.5 Outras Categorias

- **image_gen/**: openai, xai, fal, deepinfra, openrouter, krea, openai-codex
- **video_gen/**: fal, deepinfra, xai
- **browser/**: browser_use, browserbase, firecrawl
- **observability/**: langfuse, nemo_relay

---

## 4. Como Plugins Extendem o Core sem Modificar

- Todo plugin implementa uma **ABC** definida em `agent/`.
- O core carrega o plugin via `importlib` usando o nome configurado.
- Não há monkey-patching nem edição de arquivos do core.
- Novas capacidades são adicionadas simplesmente criando uma nova pasta + classe que implementa a interface.

Exemplo de extensão:
- Adicionar novo provedor de memória → criar `plugins/memory/novo/__init__.py` implementando `MemoryProvider`.
- Adicionar nova plataforma → criar `plugins/platforms/nova/adapter.py`.

---

## 5. plugin_utils (padrões comuns)

Muitos plugins usam utilitários compartilhados:

- `get_provider_env(var)` — lê variável de ambiente com fallback de config.
- `atomic_json_write` — escrita segura de JSON de configuração.
- Circuit breaker pattern (usado em mem0).
- Lazy import de SDKs pesados (`tools.lazy_deps.ensure`).
- `save_config` + `get_config_schema` — integração com wizard `hermes <cat> setup`.

---

**Fim do documento**

*Gerado automaticamente para OpenRepublic — Engenharia Reversa do Hermes Agent*