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
  version: v5
  status: draft
  date_ymd: 2026-10-13
  date_update: 2026-10-13
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

**Team OS — внутренняя операционная система DETai:** здесь команда организует задачи, работу по направлениям, сохраняет результаты и индивидуальный вклад.

Эта страница описывает **не устройство сайта, а правила ответственности, участия, видимости и принятия решений**. Конкретные полномочия участников Team OS объясняются отдельно в [«Роли, права и возможности»](team-os/access.md) — эту справку можно открыть и из профиля участника. [Политика видимости данных](team-os/profile-data-and-visibility.md) отдельно определяет правила командного, AI- и публичного использования профиля.

Как устроена сама система и как ею пользоваться: [обзор Team OS](../ecosystem/DETai/Platform_DETai/E3-Infra/team-os/index.md), [сайт Web](../ecosystem/DETai/Platform_DETai/E3-Infra/team-os/web.md) и [Plugin для ChatGPT](../ecosystem/DETai/Platform_DETai/E3-Infra/team-os/plugin.md).

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

Уровни доступа команды и Scope, ограничения личного пространства и права
настройки дерева описаны в [«Team OS — роли, права и возможности»](team-os/access.md).

ChatGPT/Codex должен работать с Team OS через ограниченный интерфейс, а не через произвольный прямой доступ к базе данных.

Возможности работы через AI описаны в [Team OS Plugin](../ecosystem/DETai/Platform_DETai/E3-Infra/team-os/plugin.md); техническая точка входа в разделе Codex — [Team OS MCP](../ecosystem/Tools/🧭Codex/team-os-mcp.md).

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
