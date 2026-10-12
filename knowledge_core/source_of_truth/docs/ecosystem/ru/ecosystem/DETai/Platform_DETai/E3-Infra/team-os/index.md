---
type: ecosystem
title: Team OS
classification:
  scope: DETai_ecosystem
  context: platform
  layer: technology
  function: index
descriptive:
  id: detai-platform-detai-e3-infra-team-os-index
  version: v3
  status: active
  date_ymd: 2026-10-12
  date_update: 2026-10-12
links:
  external_links:
    - type: MkDocs_ru
      url: https://docs.detai-x.com/ru/ecosystem/DETai/Platform_DETai/E3-Infra/team-os/
    - type: GitHub
      url: https://github.com/DETai-org/team-os
  document_links:
    - schema: ecosystem
      link_type: part-of
      linked_document_id: detai-platform-detai-index
    - schema: ecosystem
      link_type: contains
      linked_document_id: detai-platform-team-os-web
    - schema: ecosystem
      link_type: contains
      linked_document_id: detai-platform-team-os-plugin
    - schema: ecosystem
      link_type: governed-by
      linked_document_id: team-os-contribution-ledger
    - schema: ecosystem
      link_type: interfaces-with
      linked_document_id: tools-codex-team-os-mcp
---

# Team OS — операционная среда DETai

**Team OS — внутренняя операционная система DETai для совместной работы людей и AI-агентов.** Она помогает превращать планы в задачи и действия, сохранять рабочий контекст и видеть результаты.

Это **один технологический проект** экосистемы, а не набор независимых сервисов. [Репозиторий Team OS](https://github.com/DETai-org/team-os) объединяет Core/API, Web, MCP и общие библиотеки; отдельные интерфейсы развиваются и выпускаются независимо.

## Два интерфейса одной системы

| Интерфейс | Для чего нужен |
| --- | --- |
| **[Team OS Web](web.md)** | [Сайт команды](https://team.detai-x.com/): задачи, проекты, заметки, рабочие журналы, команда и личная работа |
| **[Team OS Plugin](plugin.md)** | Работа с теми же данными через ChatGPT: разрешённые действия на естественном языке и продолжение рабочего контекста |

Web и Plugin читают и меняют **один operational state**. При этом каждый интерфейс соблюдает права конкретного участника. Новые интерфейсы, например мобильное приложение, могут появиться без создания нового источника рабочих данных.

## Что хранит Team OS

- **Рабочая структура:** Scope → Folder → List; задачи, подзадачи, статусы, назначения, сроки и дополнительные поля.
- **Знания о работе:** Notes и WorkLogs — мысли, материалы и проверяемые итоги действий.
- **Участие и права:** члены команды, организационные и локальные роли, отдельные границы закрытых проектов.
- **Личный контекст:** Home, фокус, ориентиры и контрольные точки, позволяющие продолжать работу.
- **Отчёты и представления:** согласованные внутренние данные и разрешённые публичные проекции.

Team OS хранит operational state в PostgreSQL. Сайт обращается к Core API; плагин — к нему через разрешённый MCP-интерфейс. ClickUp Mirror остаётся историческим источником миграции, а не текущим источником истины.

## Место в экосистеме

Как E3-Infra проект Team OS создаёт общую технологическую возможность для других направлений DETai. Она **не заменяет** [U.L.I.](../../../U.L.I/index.md) как среду разработки и **не подменяет** решения людей о полномочиях, вкладе или вознаграждении.

Эти правила определяются отдельно: [Governance и модель вклада](../../../../../governance/team-os.md) · [Роли, права и возможности](../../../../../governance/team-os/access.md).

[Team OS MCP в контуре ChatGPT/Codex](../../../../Tools/🧭Codex/team-os-mcp.md) — короткая техническая точка входа, а не вторая полная документация плагина.

## Актуальность

Публичные страницы объясняют **устойчивое назначение и принципы**, а не каждый пункт текущего UI. Источником точных инструментов, API-контрактов и производственных изменений остаётся [репозиторий Team OS](https://github.com/DETai-org/team-os). История выпусков публикуется в [GitHub Releases](https://github.com/DETai-org/team-os/releases), где Web и Plugin могут иметь собственные версии.
