---
type: ecosystem
classification:
  scope: Tools
  context: codex-gpt
  layer: integration
  function: explanation
descriptive:
  id: tools-codex-team-os-mcp
  version: v2
  status: active
  date_ymd: 2026-10-05
links:
  external_links:
    - type: MkDocs_ru
      url: https://docs.detai-x.com/ru/ecosystem/Tools/🧭Codex/team-os-mcp/
    - type: GitHub
      url: https://github.com/DETai-org/team-os
  document_links:
    - schema: ecosystem
      link_type: part-of
      linked_document_id: tools-codex-index
    - schema: ecosystem
      link_type: interfaces-with
      linked_document_id: detai-platform-detai-e3-infra-team-os-index
title: Team OS MCP
---

# Team OS MCP

**Team OS MCP — production-интерфейс доступа ChatGPT к операционному ядру Team OS.**

Он находится в разделе Codex / GPT, потому что его пользовательский смысл — дать ChatGPT разрешённые операции над Team OS так же, как подключённый коннектор сегодня даёт доступ к внешнему сервису.

Сам MCP **не является Team OS**. [Team OS](../../DETai/Platform_DETai/E3-Infra/team-os/index.md) — самостоятельный E3-проект с собственной моделью данных, API и runtime. MCP — один из его интерфейсов.

## Что даёт MCP

Production-контракт позволяет ChatGPT:

- получать Space, Folder и List;
- находить и читать WorkItem v0.2;
- создавать WorkItem;
- изменять разрешённые поля WorkItem с optimistic version gate;
- работать со state, priority, dates, labels и bound custom properties;
- получать ReportRecord и другие разрешённые operational views.

Пример целевого взаимодействия:

> «Покажи незавершённые задачи Management Layer»
> → ChatGPT вызывает Team OS MCP
> → MCP обращается к Team OS API
> → пользователь получает данные из того же operational core, которое показывает web-интерфейс.

## Архитектурная граница

Production path:

    ChatGPT
          ↓
    Team OS plugin
          ↓
    OpenAI Secure MCP Tunnel
          ↓
    tunnel-client on London
          ↓
    private SSH loopback
          ↓
    Team OS MCP on Nexus
          ↓
    Team OS Core API
          ↓
    PostgreSQL team_os

MCP и Core API остаются loopback-only на Nexus. Публичный MCP endpoint не создаётся. London хранит только tunnel-client, runtime credential и loopback-конец private SSH-forward; operational data остаются на Nexus.

MCP не создаёт параллельную бизнес-логику или собственную копию состояния. Проверка прав, инварианты и запись остаются внутри Team OS Core API.

## Чтение и запись

Read и write capabilities разделены по разрешениям.

Production-контракт сохраняет:

- минимально необходимые scopes;
- явные ограничения на bulk/destructive writes;
- подтверждение чувствительных действий;
- аудит изменений;
- сохранение стабильных Team OS IDs;
- external source IDs только как provenance metadata.

## Связь с ChatGPT Space и Sites

MCP даёт доступ к данным и действиям, но не определяет визуальное представление.

- **Space / Pages** могут использовать данные Team OS для совместного анализа, обсуждения и временных trackers;
- **Sites** или собственный web-интерфейс могут строить устойчивые dashboards и приложения;
- все такие поверхности должны читать один operational core через разрешённый контракт.

## Текущий статус

На 5 октября 2026 года Team OS MCP является принятой production-интеграцией.

Release [Team OS v0.2.0](https://github.com/DETai-org/team-os/releases/tag/v0.2.0) включает WorkItem v0.2 и приватную ChatGPT integration. Подключённый plugin `Team OS` использует тот же production Core API, что и web-интерфейс; live read/write acceptance выполнен с confirmation/version gate.

Проектная архитектура и текущий production status описаны на странице [Team OS](../../DETai/Platform_DETai/E3-Infra/team-os/index.md). Governance-правила работы с вкладом и персональными данными описаны отдельно в [Team OS — governance и модель вклада](../../../governance/team-os.md).
