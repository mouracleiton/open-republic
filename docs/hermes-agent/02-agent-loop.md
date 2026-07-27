# Hermes Agent Loop - Documentação Técnica

**Arquivo fonte:** `/tmp/hermes-agent-src/run_agent.py` (7.005 linhas, classe `AIAgent`)  
**Arquivo fonte:** `/tmp/hermes-agent-src/agent/conversation_loop.py` (6.698 linhas, função `run_conversation`)  
**Data:** 26 de julho de 2026  
**Contexto:** Engenharia reversa caixa-branca para OpenRepublic

---

## 1. Visão Geral da Arquitetura

O loop do agente Hermes é implementado em duas camadas:

1. **`AIAgent`** (`run_agent.py:406`) — classe pública que expõe `run_conversation()`
2. **`run_conversation`** (`conversation_loop.py`) — função de ~3.900 linhas que contém o núcleo do loop

A chamada em `run_agent.py:6705` é apenas um *forwarder* que injeta contexto de contabilidade e portal antes de delegar para `agent.conversation_loop.run_conversation`.

---

## 2. Fluxo Completo: Mensagem do Usuário → Resposta do LLM

```
Usuário
   │
   ▼
run_conversation(user_message)                    # run_agent.py:6705
   │
   ├── build_turn_context()                       # turn_context.py
   ├── preflight compression (se necessário)
   │
   ▼
while iteration_budget.has_budget():             # iteration_budget.py
   │
   ├── compose_user_api_content()
   ├── apply_anthropic_cache_control()
   │
   ▼
   LLM Call (OpenAI-compatible client)
   │   ├── streaming ou não-streaming
   │   └── handle_function_call() para tool calls
   │
   ▼
   Tool Execution (paralelo/sequencial)
   │
   ▼
   Append tool results → conversation_history
   │
   ▼
   (loop até LLM não retornar mais tool calls)
```

**Referências principais:**
- `run_agent.py:6705` (entry point)
- `conversation_loop.py:1` (docstring do módulo)
- `turn_context.py:44` (`build_turn_context`)

---

## 3. Como Tools São Chamadas Dentro do Loop

O mecanismo de tool calling é automático e iterativo:

1. O LLM retorna `tool_calls` na resposta.
2. `handle_function_call` (ou equivalente em `conversation_loop`) é invocado.
3. Cada tool é executada com retry e sanitização de argumentos (`_repair_tool_call_arguments`).
4. Resultados são anexados como mensagens `tool` no histórico.
5. O loop continua até o LLM retornar apenas conteúdo textual (sem `tool_calls`).

**Controles:**
- `max_iterations=90` (padrão em `AIAgent.__init__:440`)
- `IterationBudget` (`agent/iteration_budget.py`)

---

## 4. Sistema de Context Compression

Hermes possui um sistema sofisticado de compressão de contexto:

- **Módulos:**
  - `agent/conversation_compression.py`
  - `agent/turn_context.py` (`_compression_warrants_another_preflight_pass`)
  - `agent/context_engine.py` (`automatic_compaction_status_message`)

- **Triggers:**
  - Tokens próximos do limite do modelo
  - Erros `context_length_exceeded`
  - `PRE_API_COMPRESSION_STATUS_TEMPLATE`

- **Comportamento:**
  - Compressão *preflight* antes da chamada LLM
  - Recuperação de sessões rotacionadas (`recover_rotated_compression_session`)
  - Status messages específicas para retries de compressão

---

## 5. max_turns e Controle de Iterações

- Parâmetro: `max_iterations: int = 90` (`run_agent.py:440`)
- Classe `IterationBudget` controla o orçamento por turno.
- O loop principal em `run_conversation` verifica `has_budget()` a cada iteração.
- Interrupção por orçamento esgotado é tratada como falha controlada.

---

## 6. Como Streaming Funciona

- `stream_callback: Optional[callable]` é passado para `run_conversation`.
- Quando presente, o cliente OpenAI é chamado com `stream=True`.
- Tokens são entregues incrementalmente via callback.
- `PARTIAL_STREAM_STUB_ID` (`hermes_constants`) é usado para chunks parciais.
- KawaiiSpinner (`agent/display.py`) é usado para feedback visual durante streaming.

---

## 7. Interrupt / Stop Mechanism

- `INTERRUPT_WAITING_FOR_MODEL_PREFIX` (`conversation_loop.py:94`)
- `_set_interrupt` (patchável via `_ra()`)
- `close_interrupted_tool_sequence` (`message_sanitization.py`)
- Quando interrompido durante espera do modelo, emite mensagem especial que ACP/TUI reconhecem como metadado de cancelamento.

---

## 8. Model Switching Mid-Conversation

- Suporte a múltiplos provedores (`providers_allowed`, `providers_order`, `provider_sort`).
- `classify_api_error` + `FailoverReason` permitem fallback automático.
- `model_switch` pode ocorrer por:
  - Erro de contexto
  - Sobrecarga de provedor (`zai_coding_overload_retry_ceiling`)
  - Configuração explícita via MoA (`moa_config`)

---

## Tabela Resumo de Componentes

| Componente                    | Arquivo                              | Linha(s)     | Função Principal                     |
|------------------------------|--------------------------------------|--------------|--------------------------------------|
| `AIAgent`                    | `run_agent.py`                       | 406          | Classe principal do agente           |
| `run_conversation`           | `conversation_loop.py`               | (core)       | Loop principal (~3900 linhas)        |
| `IterationBudget`            | `agent/iteration_budget.py`          | —            | Controle de iterações                |
| `build_turn_context`         | `agent/turn_context.py`              | 46           | Preparação do turno + compressão     |
| `conversation_compression`   | `agent/conversation_compression.py`  | —            | Compressão de histórico              |
| `handle_function_call`       | `run_agent.py` (via _ra)             | —            | Execução de tool calls               |
| `classify_api_error`         | `agent/error_classifier.py`          | —            | Classificação de erros para failover |

---

## Diagrama ASCII do Loop Principal

```
[Usuário] → run_conversation()
                │
                ▼
        ┌───────────────┐
        │ build_turn_   │◄── compression preflight
        │ context()     │
        └───────┬───────┘
                ▼
        while budget.has_budget():
                │
                ▼
        LLM.call(stream=...)
                │
        ┌───────┴───────┐
        │ tool_calls?   │
        └───────┬───────┘
            Sim │ Não
                ▼
        execute_tools()
                │
                ▼
        append tool results
                │
                ▼
        (volta ao while)
```

---

**Fim do documento**