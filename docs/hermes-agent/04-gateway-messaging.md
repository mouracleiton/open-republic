# Hermes Gateway / Messaging — Documentação Técnica

**Fonte:** Engenharia reversa de `/tmp/hermes-agent-src/gateway/run.py` (24.512 linhas) e `/tmp/hermes-agent-src/gateway/platforms/base.py`.

---

## 1. Arquitetura do Gateway

### GatewayRunner (classe principal)

Localização: `gateway/run.py:3260`

```python
class GatewayRunner(
    GatewayAuthorizationMixin,
    GatewayKanbanWatchersMixin,
    GatewaySlashCommandsMixin
):
```

O `GatewayRunner` é o núcleo do sistema de mensageria. Responsabilidades:

- Inicialização e ciclo de vida de todos os adapters de plataforma
- Multiplexação de conexões (múltiplas plataformas simultâneas)
- Roteamento de mensagens entre sessões e plataformas
- Gerenciamento de sessões (`session_context.py`, `session.py`)
- Integração com approval system, kanban watchers e slash commands

### Componentes chave

| Arquivo | Função |
|---------|--------|
| `run.py` | GatewayRunner + start_gateway() |
| `session.py` / `session_context.py` | Mapeamento sessão ↔ plataforma |
| `platform_registry.py` | Registro dinâmico de adapters |
| `profile_routing.py` | Roteamento por perfil Hermes |
| `stream_consumer.py` / `stream_dispatch.py` | Consumo de streams de eventos |
| `slash_commands.py` | 243k linhas de handlers de comandos |
| `kanban_watchers.py` | 72k linhas de watchers Kanban |
| `authz_mixin.py` | Sistema de autorização/approval |

### Multiplex, Routing e Session Mapping

- Cada plataforma adapter roda de forma independente (polling, webhook ou Socket Mode)
- Mensagens são normalizadas para um formato interno (`event`)
- `session_context` mapeia `(platform, chat_id/thread_id)` → sessão Hermes ativa
- `profile_routing` permite múltiplos perfis Hermes no mesmo gateway
- Respostas do agente são roteadas de volta via o adapter original usando `thread_id` / `message_thread_id`

---

## 2. Plataformas e Adapters

### Plataformas disponíveis (`plugins/platforms/`)

```
dingtalk/  discord/  email/  feishu/  google_chat/
homeassistant/  irc/  line/  matrix/  mattermost/
ntfy/  photon/  raft/  simplex/  slack/
sms/  teams/  telegram/  wecom/  whatsapp/
```

### Implementações em `gateway/platforms/`

- `base.py` — `BasePlatformAdapter` (ABC, ~6.060 linhas)
- `signal.py` + `signal_format.py` + `signal_rate_limit.py`
- `whatsapp_cloud.py` + `whatsapp_common.py`
- `weixin.py` (WeChat)
- `yuanbao.py` + `yuanbao_proto.py` + `yuanbao_media.py` + `yuanbao_sticker.py`
- `bluebubbles.py` (iMessage via BlueBubbles)
- `webhook.py` + `webhook_filters.py`
- `msgraph_webhook.py` (Microsoft Teams/Graph)
- `qqbot/` (subdiretório)

### Como funciona um Adapter (BasePlatformAdapter)

Métodos abstratos principais:

- `connect()` / `start_polling()` / `start_webhook()`
- `send_message()`, `send_media()`, `send_audio_as_voice()`
- `handle_incoming_update()` → normaliza para evento interno
- `_resolve_thread_ts()` / `_thread_metadata_for_source()` — suporte a threads/tópicos
- `should_send_media_as_audio()` — lógica específica por plataforma (Telegram só aceita MP3/M4A para áudio)

Cada adapter herda de `BasePlatformAdapter` e implementa o protocolo da plataforma (Telegram Bot API, Discord.py, Slack Bolt, WhatsApp Cloud API, Signal CLI, etc.).

---

## 3. Approval System (comandos perigosos)

Implementado em `GatewayAuthorizationMixin` (`authz_mixin.py`) e integrado no `GatewayRunner`.

Fluxo:

1. Comando perigoso detectado (ex: `execute_code`, shell, deleções)
2. Gateway pausa execução e envia mensagem de aprovação
3. Usuário responde com:
   - `/approve`
   - `/approve session`
   - `/approve always`
   - texto simples: `approve`, `yes`, `ok`, `👍`
4. Handlers em `run.py` processam `_handle_approve_command`
5. Execução é liberada ou negada permanentemente para a sessão

Palavras de aprovação reconhecidas: `approve`, `yes`, `ok`, `okay`, `confirm`, `y`, `👍`

---

## 4. Slash Commands no Gateway

Mixin: `GatewaySlashCommandsMixin` (importado de `gateway/slash_commands.py`)

- Comandos registrados dinamicamente via decorators ou registro central
- Suporte a menções no Telegram (`/cmd@bot`)
- Handlers para `/approve`, `/deny`, `/usage`, etc.
- Integração profunda com Kanban watchers e approval flow
- Mais de 243 mil linhas dedicadas a parsers, validadores e executores de comandos

---

## 5. Kanban Watchers

Mixin: `GatewayKanbanWatchersMixin`

Arquivo principal: `gateway/kanban_watchers.py` (72.676 linhas)

Funcionalidades:

- Monitoramento de boards Kanban (provavelmente GitHub Projects, Linear, etc.)
- watchers por sessão/perfil
- Notificações automáticas de mudanças de status
- Integração com o sistema de entrega de mensagens do gateway

---

## 6. Webhook Handling

Arquivos principais:

- `gateway/platforms/webhook.py`
- `gateway/platforms/webhook_filters.py`
- `gateway/platforms/msgraph_webhook.py`

Suporte a:

- Webhooks genéricos com filtros
- Microsoft Graph webhooks (Teams)
- Validação de assinatura e rate limiting
- Conversão de payload de webhook em eventos internos do Hermes

---

## Resumo da Arquitetura

```
GatewayRunner
├── Multiplex de Adapters (Telegram, Discord, WhatsApp, Signal, WeChat, Yuanbao, Slack...)
├── Session Mapping (platform + chat_id/thread_id → sessão)
├── Profile Routing
├── AuthorizationMixin → Approval flow (/approve, texto livre)
├── SlashCommandsMixin → 243k linhas de comandos
├── KanbanWatchersMixin → 72k linhas de watchers
└── Webhook infrastructure
```

Documento gerado automaticamente via engenharia reversa — 26 de julho de 2026.