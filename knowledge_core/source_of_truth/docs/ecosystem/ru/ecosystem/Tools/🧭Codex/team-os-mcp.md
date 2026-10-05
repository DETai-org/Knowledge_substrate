---
type: ecosystem
classification:
  scope: Tools
  context: codex-gpt
  layer: integration
  function: explanation
descriptive:
  id: tools-codex-team-os-mcp
  version: v1
  status: draft
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

**Team OS MCP — планируемый инструмент доступа ChatGPT/Codex к операционному ядру Team OS.**

Он находится в разделе Codex / GPT, потому что его пользовательский смысл — дать ChatGPT разрешённые операции над Team OS так же, как подключённый коннектор сегодня даёт доступ к внешнему сервису.

Сам MCP **не является Team OS**. [Team OS](../../DETai/Platform_DETai/E3-Infra/team-os/index.md) — самостоятельный E3-проект с собственной моделью данных, API и runtime. MCP — один из его интерфейсов.

## Что должен давать MCP

Первый контракт должен позволять ChatGPT/Codex:

- получать рабочие контейнеры;
- находить и читать WorkItem;
- создавать WorkItem;
- изменять разрешённые поля;
- закрывать и переоткрывать работу;
- получать ReportRecord и другие разрешённые operational views.

Пример целевого взаимодействия:

> «Покажи незавершённые задачи Management Layer»
> → ChatGPT вызывает Team OS MCP
> → MCP обращается к Team OS API
> → пользователь получает данные из того же operational core, которое показывает web-интерфейс.

## Архитектурная граница

Целевой путь:

    ChatGPT / Codex
          ↓
    Team OS MCP
          ↓
    Team OS API
          ↓
    Team OS domain logic
          ↓
    PostgreSQL team_os

MCP не должен создавать параллельную бизнес-логику или собственную копию состояния. Проверка прав, инварианты и запись остаются внутри Team OS.

## Чтение и запись

Read и write capabilities должны быть разделимы по разрешениям.

Безопасный контракт предполагает:

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

На 5 октября 2026 года MCP ещё не является production-интеграцией. Сначала принимаются Core API и web pilot Team OS. После стабилизации API MCP становится следующим интерфейсным Work Package.

Проектная архитектура и текущий pilot описаны на странице [Team OS](../../DETai/Platform_DETai/E3-Infra/team-os/index.md). Governance-правила работы с вкладом и персональными данными описаны отдельно в [Team OS — governance и модель вклада](../../../governance/team-os.md).
