---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: governance-operating-model
  layer: architecture-and-logic
  function: explanation
  system: governance-operating-model
  domain: team-os
  audiences: [team, managers, agents]
descriptive:
  id: team-os-contribution-ledger
  version: v3
  status: draft
  date_ymd: 2026-08-05
  date_update: 2026-10-05
governance:
  canonicality: working
  visibility: public
  owner_role: operating-model-owner
  approver_role: founder
  review_date: 2026-10-20
links:
  external_links:
    - type: MkDocs_ru
      url: https://docs.detai-x.com/ru/governance/team-os/
  document_links:
    - schema: ecosystem
      link_type: part-of
      linked_document_id: governance-operating-model-index
    - schema: ecosystem
      link_type: governs
      linked_document_id: detai-platform-detai-e3-infra-team-os-index
    - schema: ecosystem
      link_type: interfaces-with
      linked_document_id: storytelling-index
title: Team OS — governance и модель вклада
---

# Team OS — governance и модель вклада

Эта страница описывает **не техническую архитектуру Team OS, а правила управления людьми, вкладом, видимостью и правами внутри этой системы**.

Сам Team OS как технологический E3-проект описан отдельно: [Team OS в Platform DETai](../ecosystem/DETai/Platform_DETai/E3-Infra/team-os/index.md).

Разделение принципиально: интерфейс, база данных или конкретная технология могут меняться, но правила оценки вклада, доступа и human accountability не должны незаметно следовать за технической реализацией.

## Четыре разных уровня

1. **Activity Ledger** — факты действий: задачи, changes, документы, занятия, исследования и координация.
2. **Contribution Assessment** — проверка результата и его значения в конкретном контексте.
3. **Recognition and Reputation** — история ролей, доверия, ответственности и выбранных достижений.
4. **Economic Rights** — зарплата, fee, bonus, profit sharing, option или share по отдельной policy и соглашению.

Ни один уровень не выводится из предыдущего автоматически.

Например, большое количество activity не означает автоматически высокий contribution score, высокий contribution score не создаёт автоматически reputation, а recognition не создаёт автоматически economic right.

## Human accountability

Team OS может собирать evidence, считать агрегаты, предлагать интерпретации и помогать сравнивать периоды. Он не должен самостоятельно принимать решения, которые требуют человеческой или юридической ответственности.

К таким решениям относятся:

- полномочия и изменение роли человека;
- дисциплинарные решения;
- размер вознаграждения;
- доля, option или иное экономическое право;
- профессиональная аттестация;
- разрешение существенного dispute.

AI-analysis может быть входом для решения, но не заменяет уполномоченную роль.

## Публичное и приватное

Публично с согласия участника могут показываться:

- роли и зоны ответственности;
- проекты;
- выбранные подтверждённые результаты;
- агрегированные показатели команды или экосистемы.

В защищённом контуре должны оставаться:

- детальные персональные оценки;
- внутренние комментарии и disputes;
- финансовые значения;
- чувствительные персональные метрики;
- AI-analysis, который не прошёл человеческую проверку;
- данные, доступ к которым ограничен отдельными policy или соглашениями.

Публичная и внутренняя проекции могут строиться из одного объекта, но доступ к полям определяется правилами visibility, а не наличием двух независимых копий данных.

## Activity не равна Contribution

Team OS должен различать:

- **факт действия**;
- **результат**;
- **влияние результата**;
- **признание**;
- **экономическое последствие**.

GitHub commit, закрытая задача, публикация или проведённое занятие являются evidence активности. Их смысл оценивается в контексте проекта, роли, качества и достигнутого состояния.

Эта граница нужна, чтобы система не превращала счётчик действий в рейтинг людей.

## Связь с Work Management

Work Management может быть одним из модулей Team OS и со временем интегрировать либо заменить внешний task-сервис. Это техническое и продуктовое решение самого [E3-проекта Team OS](../ecosystem/DETai/Platform_DETai/E3-Infra/team-os/index.md).

Настоящая governance-страница не фиксирует конкретный UI или vendor. Она задаёт правила, которые должны сохраняться независимо от того, где человек ставит статус задачи или открывает dashboard.

## Связь с U.L.I.

U.L.I. может предоставлять проверяемые технические события и результаты производственного цикла. Team OS объединяет evidence из технологических, институциональных и управленческих доменов.

Поэтому Team OS не является частью U.L.I.: U.L.I. описывает Human–AI среду создания, а Team OS удерживает operational state, участие и связанные представления.

## Связь со Storytelling и отчётами

Team OS может связывать участников, проекты и activity с публикационными событиями Storytelling, но не хранит публикационную бизнес-логику и не публикует материалы вместо Storytelling.

Месячные и другие отчёты могут использовать один operational ReportRecord с разными уровнями disclosure. Публичная проекция не должна раскрывать защищённые поля только потому, что внутренний отчёт построен из того же объекта.

## Инструментальный доступ

ChatGPT/Codex должен работать с Team OS через ограниченный интерфейс, а не через произвольный прямой доступ к базе данных.

Целевой инструмент описан отдельно: [Team OS MCP](../ecosystem/Tools/🧭Codex/team-os-mcp.md).

## Ворота развития governance

До использования contribution-механик для чувствительных решений должны быть отдельно определены и приняты:

- visibility policy;
- модель ролей и decision rights;
- правила исправления неверного evidence;
- appeal/dispute process;
- human accountability;
- retention и audit requirements;
- Economic Participation Policy.

Техническая готовность Team OS сама по себе не означает готовность этих governance-механик.
