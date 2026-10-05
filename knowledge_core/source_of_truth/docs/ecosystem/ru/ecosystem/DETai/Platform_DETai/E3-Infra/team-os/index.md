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
  version: v1
  status: active
  date_ymd: 2026-10-05
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
      link_type: governed-by
      linked_document_id: team-os-contribution-ledger
    - schema: ecosystem
      link_type: interfaces-with
      linked_document_id: tools-codex-team-os-mcp
---

# Team OS

**Team OS — внутренний E3-Infra проект DETai и суверенный операционный слой, который должен хранить состояние работы экосистемы независимо от конкретного внешнего task-сервиса.**

Проект развивается как собственная система с репозиторием, версией, API и моделью данных. Его задача — не воспроизвести ClickUp или Notion один в один, а дать DETai устойчивое operational core, к которому могут подключаться разные интерфейсы: web, ChatGPT/Codex через MCP, агенты и будущие представления.

Технический источник: [DETai-org/team-os](https://github.com/DETai-org/team-os).

## Почему Team OS относится к E3

[E3-Infra](../../../logic-of-echelons.md) объединяет проекты, создающие общую технологическую основу для других проектов и продуктов. Team OS относится именно сюда, потому что его основной результат — повторно используемая операционная возможность для всей экосистемы:

- проекты, рабочие элементы и их состояние;
- роли и назначения;
- activity и evidence;
- внутренние отчёты и аналитические проекции;
- API для автоматизаций и агентов;
- единая точка доступа к рабочему состоянию для разных интерфейсов.

Team OS функционально используется как инструмент, но архитектурно уже является проектом: у него есть собственная логика, интерфейсы, API, data model и самостоятельный жизненный цикл.

## Операционное ядро и интерфейсы

Проект разделяет **ядро** и **представления**.

Операционное ядро владеет устойчивыми сущностями и связями. Первый pilot использует отдельную PostgreSQL schema team_os внутри общей operational database detai_projects; локальная разработка работает с detai_projects_dev.

Поверх ядра могут существовать разные интерфейсы:

- team.detai-x.com — целевой web-интерфейс команды;
- ChatGPT/Codex — естественно-языковой интерфейс через [Team OS MCP](../../../../Tools/🧭Codex/team-os-mcp.md);
- ChatGPT Space и Pages — совместная среда анализа и временных представлений;
- ChatGPT Sites или собственные web-поверхности — устойчивые визуальные dashboards и приложения;
- другие агенты и сервисы — через API и разрешённые интеграции.

Ни один из этих интерфейсов не должен становиться вторым источником истины для тех же operational objects.

## Базовая модель пилота

Первый vertical slice фиксирует минимальные сущности:

- **Container** — иерархический рабочий контейнер;
- **WorkItem** — единица работы, не привязанная по смыслу к конкретному SaaS;
- **ReportRecord** — единый отчёт, из которого строятся разные представления.

ClickUp Mirror используется как источник первичной миграции Management Layer. ClickUp ID и metadata сохраняются как external source references, но после импорта Team OS должен владеть своими объектами и не зависеть от ClickUp как от канонического runtime.

## Отчёты как проекции состояния

Месячный отчёт не является отдельной параллельной системой. Team OS хранит один ReportRecord, у которого могут быть разные уровни раскрытия:

- authenticated/internal projection для команды;
- public projection для сайта DETai;
- представление для Telegram;
- визуальный dashboard или ChatGPT Site.

Публичная web-проекция относится к существующему Events-контуру сайта, например /ru/events/reports/2026-09. Публикационный lifecycle и доставка остаются ответственностью Storytelling и owning surfaces; Team OS не подменяет их.

## Граница с Governance

Эта страница описывает **Team OS как технологический E3-проект**.

Правила оценки вклада, публичности и приватности, recognition, economic rights и human accountability описываются отдельно на странице [Team OS — governance и модель вклада](../../../../../governance/team-os.md).

Такое разделение важно: технология может меняться, а правила обращения с людьми, вкладом и чувствительными данными не должны незаметно следовать за технической реализацией.

## Граница с U.L.I.

[U.L.I.](../../../U.L.I/index.md) — среда Human–AI создания и развития технологических проектов. Team OS — operational system, которая хранит и показывает состояние работы, результаты и связи между объектами.

U.L.I. отвечает на вопрос **«как люди и AI создают?»**, Team OS — **«что сейчас существует, делается и изменилось?»**.

## Текущий этап

На 5 октября 2026 года Team OS находится в активном pilot-развитии.

Первый pilot:

1. импортирует Management Layer из ClickUp Mirror;
2. хранит объекты в собственной PostgreSQL schema;
3. даёт CRUD API и web-представление;
4. использует сентябрьский ecosystem report как первый ReportRecord;
5. после стабилизации API должен получить [MCP-интерфейс для ChatGPT/Codex](../../../../Tools/🧭Codex/team-os-mcp.md);
6. затем может быть развёрнут на Nexus и получить team.detai-x.com.

До production acceptance ClickUp остаётся действующим operational source для существующих процессов, а Team OS развивается как его будущая суверенная замена/надстройка, а не объявляется внедрённым заранее.
