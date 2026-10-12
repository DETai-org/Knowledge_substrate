---
type: ecosystem
title: Team OS Plugin — работа с ChatGPT
classification:
  scope: DETai_ecosystem
  context: platform
  layer: technology
  function: explanation
  system: technology
  domain: team-os-plugin
  audiences: [public, team, agents]
descriptive:
  id: detai-platform-team-os-plugin
  version: v1
  status: draft
  date_ymd: 2026-10-12
  date_update: 2026-10-12
governance:
  canonicality: working
  visibility: public
  owner_role: platform-owner
  approver_role: founder
links:
  external_links:
    - type: MkDocs_ru
      url: https://docs.detai-x.com/ru/ecosystem/DETai/Platform_DETai/E3-Infra/team-os/plugin/
  document_links:
    - schema: ecosystem
      link_type: part-of
      linked_document_id: detai-platform-detai-e3-infra-team-os-index
---

# Team OS Plugin — работа с ChatGPT

**Team OS Plugin позволяет участнику DETai взаимодействовать с рабочей системой через ChatGPT на обычном языке.** Плагин подключает AI к тем же данным Team OS, с которыми человек работает на [сайте Team OS](https://team.detai-x.com/).

## Для чего нужен плагин

Через подключение можно попросить AI найти разрешённые задачи, разобраться в текущем состоянии проекта, подготовить заметку, зафиксировать итоги работы или изменить запись в пределах собственных прав.

Отдельная возможность Team OS — **непрерывность рабочего контекста**. Персональный Home, текущий фокус, ориентиры, рекомендации и контрольные точки помогают возвращаться к делу в следующих разговорах, не создавая вторую копию данных. Это не означает, что агент должен автоматически читать всё личное пространство.

## Как это устроено

- **MCP (Model Context Protocol)** предоставляет ChatGPT описания доступных инструментов для чтения и записи. Их параметры и ограничения определяются актуальным серверным контрактом.
- **Skills** помогают AI применять инструменты в типовых сценариях, например при начале работы или подготовке WorkLog.
- **Публичная документация** объясняет назначение Team OS и её принципы. Её можно открыть по ссылке для уточнения общего контекста, но она не заменяет актуальные данные или права.

Права определяются персональным подключением и проверяются сервером. Публичный текст или инструкция внутри найденной записи не расширяет полномочия AI. Факт изменения должен подтверждаться ответом Team OS.

## Связанные страницы

[← Обзор проекта Team OS](index.md) · [Team OS Web — сайт](web.md) · [Как устроен MCP в контуре ChatGPT/Codex](../../../../Tools/🧭Codex/team-os-mcp.md)

Технические детали, перечень инструментов, навыки и ограничения конкретной сборки живут в [репозитории Team OS](https://github.com/DETai-org/team-os/tree/main/plugins/team-os); публичная статья намеренно не копирует их.
