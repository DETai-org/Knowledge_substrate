---
type: ecosystem
title: Team OS
classification:
  scope: DETai_ecosystem
  context: governance-operating-model
  layer: operating-model
  function: index
  system: governance-operating-model
  domain: team-os
  audiences: [public, team, managers, agents]
descriptive:
  id: detai-platform-detai-e3-infra-team-os-index
  version: v4
  status: active
  date_ymd: 2026-10-23
  date_update: 2026-10-23
links:
  external_links:
    - type: MkDocs_ru
      url: https://docs.detai-x.com/ru/ecosystem/DETai/Platform_DETai/E3-Infra/team-os/
  document_links:
    - schema: ecosystem
      link_type: part-of
      linked_document_id: management-layer-index
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

Это **один технологический проект** экосистемы, объединяющий Core/API, Web, MCP и общие компоненты; отдельные пользовательские интерфейсы развиваются и выпускаются независимо.

## Два интерфейса одной системы

| Интерфейс | Для чего нужен |
| --- | --- |
| **[Team OS Web](web.md)** | [Сайт команды](https://team.detai-x.com/): задачи, проекты, заметки, рабочие журналы, команда и личная работа |
| **[Team OS Plugin](plugin.md)** | Работа с теми же данными через ChatGPT: разрешённые действия на естественном языке и продолжение рабочего контекста |

Web и Plugin читают и меняют **один operational state**. При этом каждый интерфейс соблюдает права конкретного участника. Новые интерфейсы, например мобильное приложение, могут появиться без создания нового источника рабочих данных.

## Что хранит Team OS

- **Рабочая структура:** Scope → Folder / Project → List. Проект является самостоятельной сущностью внутри Scope; папки группируют работу без проектного паспорта. Lists хранят задачи, заметки или рабочие журналы.
- **Знания о работе:** Notes и WorkLogs — мысли, материалы и проверяемые итоги действий.
- **Участие и права:** члены команды, организационные и локальные роли, отдельные границы закрытых проектов.
- **Личный контекст:** Home, фокус, ориентиры и контрольные точки, позволяющие продолжать работу.
- **Отчёты и представления:** согласованные внутренние данные и разрешённые публичные проекции.

Team OS хранит operational state в PostgreSQL. Сайт обращается к Core API; плагин — к нему через разрешённый MCP-интерфейс. ClickUp Mirror остаётся историческим источником миграции, а не текущим источником истины.

## Место в экосистеме

Team OS принадлежит [Management Layer](../../../../Management_layer/index.md): это внутренняя управленческая система для работы обоих слоёв DETai. Её рабочий Scope определяется этой ответственностью, а E3 описывает обеспечивающий вклад в экосистему. Технологическая реализация не делает систему частью Platform DETai или Scope Infrastructure.

Team OS может быть оформлена как внутренний продукт по [модели продуктового объекта](../../../../../product-market/product-object-model.md), когда явно определены аудитория, обещанный результат, поддержка, наблюдение и стабильное поставляемое состояние. Перемещение между Scope и уточнение E3 сами по себе не меняют продуктовый статус.

[U.L.I.](../../../U.L.I/index.md) обеспечивает процесс технического создания и развития системы. Решения о полномочиях, оценке вклада и вознаграждении остаются у ответственных людей.

Путь страницы и стабильный document ID сохранены для совместимости ссылок. Исторический сегмент `Platform_DETai/E3-Infra` не определяет текущего владельца системы.

Эти правила определяются отдельно: [Governance и модель вклада](../../../../../governance/team-os.md) · [Роли, права и возможности](../../../../../governance/team-os/access.md).

[Team OS MCP в контуре ChatGPT/Codex](../../../../Tools/🧭Codex/team-os-mcp.md) — короткая техническая точка входа, а не вторая полная документация плагина.

## Актуальность

Публичные страницы объясняют **устойчивое назначение, пользовательские возможности и принципы**, а не историю разработки. Доступность инструментов и конкретные ограничения следует сверять с работающими Web и Plugin; их версии могут различаться.
