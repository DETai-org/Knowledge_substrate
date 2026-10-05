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
  version: v2
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

**Team OS — внутренний E3-Infra проект DETai и суверенный операционный слой, который хранит состояние работы экосистемы независимо от конкретного внешнего task-сервиса.**

Проект развивается как собственная система с репозиторием, версией, API и моделью данных. Его задача — не воспроизвести ClickUp или Notion один в один, а дать DETai устойчивое operational core, к которому могут подключаться разные интерфейсы: web, ChatGPT/Codex через MCP, агенты и будущие представления.

Технический источник: [DETai-org/team-os](https://github.com/DETai-org/team-os).

Рабочий интерфейс: [team.detai-x.com](https://team.detai-x.com/).

Текущий зафиксированный release: [Team OS v0.2.0 — First Operational Release](https://github.com/DETai-org/team-os/releases/tag/v0.2.0).

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

Операционное ядро владеет устойчивыми сущностями и связями. Production хранится в PostgreSQL schema `team_os` внутри общей operational database `detai_projects` на Nexus; локальная разработка работает с `detai_projects_dev`.

Поверх ядра существуют разные интерфейсы:

- [team.detai-x.com](https://team.detai-x.com/) — canonical operational web-интерфейс команды на Vercel;
- ChatGPT — естественно-языковой read/write интерфейс через подключённый [Team OS MCP](../../../../Tools/🧭Codex/team-os-mcp.md);
- ChatGPT Space и Pages — совместная среда анализа и временных представлений;
- ChatGPT Sites — возможные устойчивые analytical dashboards и report projections;
- другие агенты и сервисы — через API и разрешённые интеграции.

Production web обращается к защищённому Team OS API через server-side proxy. Core API и PostgreSQL находятся на Nexus; PostgreSQL не публикуется наружу.

Private ChatGPT path отделён от web: OpenAI Secure MCP Tunnel приходит в `tunnel-client` на London, затем через private SSH loopback — в Team OS MCP на Nexus, далее в Core API и PostgreSQL. London не хранит operational state и не становится вторым runtime Team OS.

Ни один из этих интерфейсов не должен становиться вторым источником истины для тех же operational objects.

## Базовая модель

Первый vertical slice закрепил минимальные сущности:

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

Внутренний сентябрьский отчёт доступен на [team.detai-x.com/reports/2026-09](https://team.detai-x.com/reports/2026-09).

Публичная web-проекция относится к существующему Events-контуру сайта, например `/ru/events/reports/2026-09`. Storytelling владеет publication lifecycle и материализует только allowlisted public projection; публичный runtime не должен получать `internalPayload` и не зависит от Team OS API.

ChatGPT Site может быть дополнительной интерактивной или аналитической проекцией того же ReportRecord, но не вторым источником истины.

## Граница с Governance

Эта страница описывает **Team OS как технологический E3-проект**.

Правила оценки вклада, публичности и приватности, recognition, economic rights и human accountability описываются отдельно на странице [Team OS — governance и модель вклада](../../../../../governance/team-os.md).

Такое разделение важно: технология может меняться, а правила обращения с людьми, вкладом и чувствительными данными не должны незаметно следовать за технической реализацией.

## Граница с U.L.I.

[U.L.I.](../../../U.L.I/index.md) — среда Human–AI создания и развития технологических проектов. Team OS — operational system, которая хранит и показывает состояние работы, результаты и связи между объектами.

U.L.I. отвечает на вопрос **«как люди и AI создают?»**, Team OS — **«что сейчас существует, делается и изменилось?»**.

## Текущий статус

На 5 октября 2026 года первый operational release Team OS зафиксирован как [v0.2.0](https://github.com/DETai-org/team-os/releases/tag/v0.2.0).

Приняты:

1. production PostgreSQL schema `team_os` на Nexus;
2. Core API v0.2;
3. Work Management Web на [team.detai-x.com](https://team.detai-x.com/);
4. приватный ChatGPT plugin `Team OS` через MCP;
5. read/write MCP v0.2 с confirmation/version gate;
6. September ReportRecord как первая внутренняя и публичная отчётная identity;
7. production backup/restore и deployment evidence;
8. вывод дублирующего standalone WorkItem v1 runtime из эксплуатации.

ClickUp Mirror остаётся import/evidence source и provenance для внешних ID, но не runtime source of truth для уже импортированных объектов Team OS.

Дальнейшее развитие относится к расширению продукта: saved views, relations/dependencies, identity/ACL, analytical projections и последующие ежемесячные отчёты.
