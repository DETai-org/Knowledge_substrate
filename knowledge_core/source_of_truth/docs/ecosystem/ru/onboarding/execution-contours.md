---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: onboarding-runtime
  layer: operating-model
  function: architecture
  system: governance-operating-model
  domain: onboarding
  audiences: [team, managers, onboarding-coordinators, agents]
descriptive:
  id: onboarding-execution-contours
  version: v1
  status: draft
  date_ymd: 2026-08-14
governance:
  canonicality: working
  visibility: public
  owner_role: onboarding-coordinator
  approver_role: onboarding-owner
  review_date: 2026-09-14
object_state:
  architecture_status: hypothesis
  implementation_status: in-design
  evidence_status: preliminary-support
  visibility_status: public
title: Контуры знаний и исполнения
---

# Контуры знаний и исполнения

!!! warning "Черновик для review"

    Распределение ответственности между контурами ожидает проверки ответственного за onboarding.

Onboarding использует несколько связанных контейнеров. Ни один из них не заменяет остальные: каждый отвечает за свой тип знания или действия.

| Контур | Роль |
|---|---|
| **Knowledge Substrate — этот раздел** | объясняет назначение, этапы, границы и архитектуру onboarding |
| [GitHub-репозиторий onboarding](https://github.com/DETai-org/onboarding) | хранит общие материалы, файловые представления Issues и командные Codex Skills |
| [GitHub Issues](https://github.com/DETai-org/onboarding/issues) | содержит действующие tutorials, how-to, обсуждение и обратную связь |
| [ClickUp Space `Onboarding`](https://app.clickup.com/90152202658/v/s/90159899687) | показывает участнику задачи маршрута и его текущий прогресс |
| [Folder `Management Layer / Onboarding`](https://app.clickup.com/90152202658/v/f/901517320188/901511102975) | используется для проектирования, обновления и координации маршрута |

## Knowledge Substrate

Knowledge Substrate хранит публичную модель: что такое onboarding, из каких этапов он состоит и как связаны рабочие контуры. Здесь не ведётся персональный прогресс и не копируются изменяемые operational ID.

## GitHub-репозиторий и Issues

Вкладка Issues является частью репозитория, но выполняет отдельную роль. В Issues живут актуальные tutorial-задачи, вопросы участников и история обсуждения; в файловой части репозитория находятся материалы, архивные представления и инструменты для сопровождающей команды.

- [`.codex-skills/`](https://github.com/DETai-org/onboarding/tree/main/.codex-skills) хранит общий для экосистемы версионированный реестр Codex Skills и manifest установки. Определение skills дано в документе [Codex Skills](../ecosystem/Tools/🧭Codex/codex-skills.md).
- `archive/issues/<season>/` хранит датированный Markdown-snapshot завершённой итерации Issues для сравнения изменений и поиска регрессий.
- Изменение архивного или локального Markdown-файла само по себе не обновляет действующую Issue: актуальная задача изменяется отдельно.

## Два ClickUp-контура

### Space `Onboarding` — прохождение участником

[Space `Onboarding`](https://app.clickup.com/90152202658/v/s/90159899687) — рабочее место нового участника. Здесь выдаётся необходимый ранний доступ, видны задачи маршрута и сохраняется прогресс прохождения.

### Folder `Management Layer / Onboarding` — управление маршрутом

[Folder `Management Layer / Onboarding`](https://app.clickup.com/90152202658/v/f/901517320188/901511102975) — рабочий контур onboarding-координаторов. Здесь проектируются tutorials, обновляются материалы, согласуются доступы и фиксируются улучшения процесса.

Участническое исполнение и изменение самой системы onboarding являются разными потоками. Если результат затрагивает оба потока, он фиксируется в каждом соответствующем контуре со взаимными ссылками.

## Локальная среда Codex

Onboarding-координатор может клонировать репозиторий onboarding и открыть его как отдельный Codex project. Repository-level `AGENTS.md` связывает публичную архитектуру, GitHub Issues, локальные материалы и operational navigation map ClickUp.

Следующий документ: [Сопровождение и развитие](coordination-and-evolution.md).
