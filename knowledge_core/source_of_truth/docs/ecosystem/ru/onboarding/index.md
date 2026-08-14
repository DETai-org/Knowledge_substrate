---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: governance-operating-model
  layer: operating-model
  function: guide
  system: governance-operating-model
  domain: onboarding
  audiences: [candidates, team, managers, onboarding-owners, agents]
descriptive:
  id: onboarding-system
  version: v1
  status: active
  date_ymd: 2026-08-14
governance:
  canonicality: canonical
  visibility: public
  owner_role: onboarding-owner
  approver_role: operating-model-owner
  review_date: 2026-09-14
object_state:
  architecture_status: canonical
  implementation_status: operational
  evidence_status: not-applicable
  visibility_status: public
links:
  external_links:
    - type: MkDocs_ru
      url: https://detai-org.github.io/Knowledge_substrate/ru/onboarding/
    - type: GitHub
      url: https://github.com/DETai-org/onboarding
  document_links:
    - schema: ecosystem
      link_type: implements
      linked_document_id: meaningful-participation
    - schema: ecosystem
      link_type: part-of
      linked_document_id: management-layer-2-architecture-and-logic-operating-model-detai
title: Onboarding DETai
---

# Onboarding DETai

## Назначение

Onboarding — сквозная функция перехода человека от первого доступа к осмысленному участию в DETai. Он связывает понимание экосистемы, настройку рабочей среды, освоение инструментов, прохождение tutorial-задач, обратную связь и переход к реальной роли.

Onboarding не является только папкой инструкций или списком обязательных действий. Он реализует принцип [осмысленного участия](../governance/meaningful-participation.md): новый участник должен понимать, куда он входит, зачем выполняет шаг, где задавать вопросы, как увидеть прогресс и как повлиять на следующую версию маршрута.

## Аудитория и владельцы

| Перспектива | Потребность или ответственность |
|---|---|
| кандидат или новый участник | получить ранний доступ, понять целое, настроить среду и пройти подходящие tutorials |
| действующий участник | вернуться к маршруту при освоении новой роли, системы или инструмента |
| mentor / сопровождающий | помочь пройти маршрут, увидеть затруднение и направить обратную связь |
| onboarding owner | проектировать последовательность, поддерживать tutorials и принимать улучшения |
| Management Layer | согласовывать onboarding с ролями, доступами, рабочими системами и действующим Operating Model |

Владельцы управляют качеством маршрута, но не подменяют участника в прохождении. Участнический прогресс и работа над самой системой onboarding являются разными потоками.

## Где живут знания и исполнение

| Контур | Роль |
|---|---|
| Knowledge Substrate | канонически объясняет назначение, границы и архитектуру onboarding |
| [GitHub-репозиторий onboarding](https://github.com/DETai-org/onboarding) | хранит tutorial issues, общие материалы, командные Codex skills и локально доступные представления |
| GitHub Issues | действующие tutorials и how-to, их обсуждение, обратная связь и история изменений |
| ClickUp Space `Onboarding` | выдача раннего доступа, участническое прохождение и видимый прогресс нового участника |
| Folder `Management Layer / Onboarding` | проектирование, обновление и координация onboarding владельцами процесса |

Ни один контейнер не заменяет остальные: Knowledge Substrate не ведёт персональный прогресс, GitHub repository не становится task runtime, а ClickUp не является каноническим источником концептуальной модели.

## Фактическая структура репозитория

Публичный источник материалов: [DETai-org/onboarding](https://github.com/DETai-org/onboarding).

- GitHub Issues содержат живые tutorials и how-to. Комментарии участника являются частью обратной связи и помогают улучшать маршрут.
- `.codex-skills/` хранит версионированный командный реестр Codex skills и manifest их установки.
- `archive/issues/spring-2026/` хранит датированный Markdown-snapshot существовавших GitHub Issues по состоянию на 2026-06-02, включая issue body, metadata и комментарии. Это локально читаемое и редактируемое архивное представление, а не автоматически синхронизируемая копия текущего состояния Issues.
- `Sandbox/` используется для учебных проектов; `Obsidian/` содержит материалы и заготовки локальной рабочей среды.

Изменение snapshot-файла не следует считать изменением действующего tutorial без отдельной синхронизации с GitHub Issue.

## Два ClickUp-контура

### Прохождение участником

Space `Onboarding` предназначен новому участнику. Здесь ему можно выдать ограниченный ранний доступ, назначить маршрут, увидеть прохождение и зафиксировать участнический результат.

Лог этого контура использует:

```yaml
classification:
  scope: Onboarding
  context: participant-onboarding
```

### Управление onboarding

Folder `Management Layer / Onboarding` предназначена onboarding owners и сопровождающим. Здесь проектируют tutorials, обновляют prompts и материалы, координируют доступы и улучшают процесс по обратной связи.

Лог этого контура использует:

```yaml
classification:
  scope: Governance
  context: onboarding-management
```

Lists `logs` этих контуров не взаимозаменяемы. Участническое исполнение записывается в participant-контейнер, а изменение системы onboarding — в management-контейнер. Если одно materially связано с другим, создаются две короткие записи в соответствующих дневных логах и добавляются взаимные ссылки.

Конкретные ClickUp ID хранятся в operational navigation map и локальных routes, а не на этой концептуальной странице. Общий metadata contract определён в [реестре schemas](../ecosystem/Management_layer/Docs-Ecosystem/metadata_schema_registry.md#contract-log-summary).

## Локальный Codex workspace владельца

Владелец может клонировать onboarding repository и открыть его как отдельный локальный Codex project. Repository-level `AGENTS.md` служит исполняемым мостом между четырьмя источниками:

1. этой канонической страницей Knowledge Substrate;
2. GitHub repository и Issues;
3. operational navigation map ClickUp;
4. основным Folder-local маршрутом `log-summary` для management-работы.

Основной List задаётся локально, поэтому обычная запись лога не требует сканировать весь ClickUp. Глобальная navigation map используется только при реальном cross-project результате. AGENTS.md может содержать operational ID и локальные пути; публичная архитектура фиксирует их назначение и отношения, но не копирует изменяемые идентификаторы.

## Цикл развития

```text
владелец проектирует маршрут
→ участник получает доступ и проходит tutorials
→ вопросы и обратная связь возвращаются в Issues
→ владелец обновляет материалы и последовательность
→ изменения фиксируются в management log
→ следующая итерация onboarding становится понятнее
```

Для первого входа продолжите с [маршрутами по ролям](../start/role-routes.md), [рабочей средой](../start/working-environment.md) и [Operating Model DETai](../ecosystem/Management_layer/2_Architecture_and_Logic/operating-model-detai.md).
