# Hermes Agent -- Engenharia Reversa Caixa-Branca

## Indice Master

> Fonte: github.com/NousResearch/hermes-agent (Jul 2026)
> Metodo: analise estatica do codigo-fonte Python (1.6M linhas, 3402 arquivos)
> Objetivo: documentacao completa para OpenRepublic理解 e extensao

---

## Documentos

| # | Documento | Topico | Linhas |
|---|-----------|--------|--------|
| 01 | [arquitetura-geral.md](01-arquitetura-geral.md) | Mapa do sistema, entry points, camadas, escala | 490 |
| 02 | [agent-loop.md](02-agent-loop.md) | Loop de conversacao, streaming, compression, interrupts | 181 |
| 03 | [tool-system.md](03-tool-system.md) | Registry, toolsets, dispatch, 118 tools | 177 |
| 04 | [gateway-messaging.md](04-gateway-messaging.md) | Gateway, 20+ plataformas, routing, approvals | 165 |
| 05 | [state-management.md](05-state-management.md) | SQLite, FTS5, sessoes, WAL, migrations | 291 |
| 06 | [plugin-system.md](06-plugin-system.md) | 30+ providers, plataformas, memory, observability | 185 |
| 07 | [config-auth-cli.md](07-config-auth-cli.md) | Config, OAuth, credential pools, CLI, slash commands | 166 |

**Total:** 1.655 linhas de documentacao tecnica

---

## Como usar esta documentacao

1. **Para entender a arquitetura:** Comece pelo doc 01 (visao geral)
2. **Para desenvolver tools:** Leia doc 03 (tool system)
3. **Para configurar messaging:** Leia doc 04 (gateway)
4. **Para criar plugins:** Leia doc 06 (plugin system)
5. **Para migrar/forkar:** Leia TODOS em sequencia

## Descobertas chave

- Hermes tem **1.647.405 linhas Python** em 3.402 arquivos
- O maior arquivo unico e cli.py com **780KB** (16.818 linhas)
- O maior modulo agent/ e auxiliary_client.py com **392KB**
- Existem **33 toolsets** agrupando **118+ tools**
- **30+ LLM providers** suportados via plugin
- **20+ plataformas de messaging** via gateway
- **7 backends de memoria** (Honcho, Mem0, etc)
- Cron scheduler sozinho tem **198KB** (scheduler.py)
- State management usa SQLite com FTS5 full-text search
- UI TUI e feita em Ink (React para terminal) -- 421 arquivos TS/TSX
