---
type: ecosystem
classification:
  scope: DETai_cluster
  context: uli
  layer: technical-standards
  function: explanation
descriptive:
  id: detai-u-l-i-3-technical-standards-work-model-issue-contract
  version: v2
  status: active
  date_ymd: 2026-03-25
  date_update: 2026-04-30
links:
  external_links:
    - type: "MkDocs_ru"
      url: "https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/work-model/issue-contract/"
  document_links:
    - schema: ""
      link_type: ""
      linked_document_id: ""
title: Epic Issue Contract
---

# Epic Issue Contract

Тип документа: Standard
v2.0

(контракт верхнеуровневой задачи, когда она используется как Epic Issue)

## Purpose

Этот документ задаёт правила заполнения и ведения Epic Issue как верхнеуровневого контейнера работы.

Epic Issue описывает качественный переход проекта: целевое состояние, границы изменений, состав Sub-Issue / Work Packages и критерии завершения. Он не является списком случайных задач и не заменяет Pull Request, документацию или release summary.

## Operational Placement

Текущая операционная реализация Epic Issue для проектов DETai ведётся в ClickUp.

- У каждого проекта есть своя папка в ClickUp.
- Внутри папки находится проектный лист, где ведутся Epic Issue и связанные с ними задачи.
- Codex или другой агент должен использовать явно переданный пользователем ID / URL листа. Если лист не указан, агент должен запросить его у пользователя перед созданием Epic Issue.
- Epic Issue оформляется как верхнеуровневая задача.
- Sub-Issue / Work Package оформляется как подзадача или связанная задача.
- После завершения Epic Issue история выполнения сохраняется в ClickUp через статус Complete.
- Поля GitHub PR и GitHub Branch используются для связи ClickUp-задачи с кодовой реализацией:
  - GitHub PR — URL-ссылка на Pull Request;
  - GitHub Branch — текстовое имя ветки.

GitHub остаётся code-facing delivery layer: там живут ветки, Pull Requests, review и история изменений кода. ClickUp является operational planning layer: там живут Epic Issue, Sub-Issue, статусы и история выполнения работы.

## 1. Обязательная структура Epic Issue

### 1.1 Title

Короткий навигационный заголовок, без деталей реализации.

### 1.2 Цель (целевое состояние) 🎯

Goal (Target State) — это 1–3 абзаца, формулирующих качественно новое состояние проекта или репозитория, которое должно быть достигнуто после полного завершения данной Epic Issue.

### 1.3 Область изменений (рамка перехода)

Scope (Frame of Change) — это описание границ допустимых изменений в рамках данной Epic Issue.

Поскольку в процессе работы в Epic Issue могут добавляться Sub-Issue / Work Packages, существует риск постепенно расширить её настолько, что она перестанет описывать единый осмысленный переход и превратится в совокупность разнородных улучшений.

Границы изменений:

```text
In scope: …
Out of scope: …
```

### 1.4 Sub-Issue / Work Packages

Epic Issue должна содержать или ссылаться на набор Sub-Issue / Work Packages, которые вместе приводят к достижению Goal.

### 1.5 Критерии завершения (определение «сделано»)

Epic Issue считается завершённой, когда:

- завершены все обязательные Sub-Issue / Work Packages;
- подтверждено, что их совокупный результат привёл к достижению целевого состояния, описанного в Goal;
- заполнены операционные поля, связывающие работу с delivery layer, если они применимы: GitHub PR и GitHub Branch;
- финальное состояние зафиксировано через Release Fixation, если работа меняет версию проекта или документации.

## Быстрый шаблон Epic Issue (Copy/Paste)

```markdown
# <Epic Issue Title>

## 🎯 Goal (Target State)

## 📦 Scope (Frame of Change)
**In scope:** …
**Out of scope:** …

## Sub-Issue / Work Packages
- [ ] …
- [ ] …
- [ ] …

## Completion Criteria
- [ ] All required Sub-Issue / Work Packages are complete
- [ ] Goal is actually achieved
- [ ] GitHub PR is linked where applicable
- [ ] GitHub Branch is filled where applicable
```

## Related Documents

- [Work Model](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/work-model/work-model/)
- [Sub-Issue (Work Package) Contract](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/work-model/sub-issue-contract/)
- [Release Fixation Standard](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/release-fixation-standard/)
- [Производственный цикл проектов и карта ролей вокруг него](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/2_Architecture_and_Logic/production-cycle/)
- Migration Notice: переход Epic Issue / Sub-Issue из Markdown-файлов репозитория в ClickUp
