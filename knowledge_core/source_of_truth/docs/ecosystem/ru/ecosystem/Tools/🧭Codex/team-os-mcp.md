---
type: ecosystem
classification:
  scope: Tools
  context: codex-gpt
  layer: integration
  function: explanation
descriptive:
  id: tools-codex-team-os-mcp
  version: v3
  status: active
  date_ymd: 2026-10-12
  date_update: 2026-10-12
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
    - schema: ecosystem
      link_type: interfaces-with
      linked_document_id: detai-platform-team-os-plugin
title: Team OS MCP
---

# Team OS MCP

**Team OS MCP — способ подключения ChatGPT к Team OS через плагин команды DETai.** Здесь он представлен как часть инструментов GPT/Codex; основное описание возможностей вынесено в [Team OS Plugin](../../DETai/Platform_DETai/E3-Infra/team-os/plugin.md).

MCP даёт AI разрешённые операции чтения и изменения рабочих данных. Он не является самостоятельной базой данных и не выдаёт дополнительных прав: полномочия проверяет Core Team OS в рамках персонального подключения.

**Что где читать:**

- [Team OS — обзор проекта](../../DETai/Platform_DETai/E3-Infra/team-os/index.md): зачем существует система и как связаны её интерфейсы.
- [Team OS Plugin](../../DETai/Platform_DETai/E3-Infra/team-os/plugin.md): как участник работает с ChatGPT, MCP и Skills.
- [Team OS Web](../../DETai/Platform_DETai/E3-Infra/team-os/web.md): сайт, на котором человек работает с теми же объектами.
- [Роли и права](../../../governance/team-os/access.md): границы командного и личного доступа.
- [Исходники MCP и актуальные контракты](https://github.com/DETai-org/team-os/tree/main/packages/mcp): точные инструменты и особенности реализации.

Актуальная схема MCP и ответы Core имеют приоритет при выполнении операций. Публичная документация поясняет смысл, а не заменяет проверки доступа или подтверждение записи.
