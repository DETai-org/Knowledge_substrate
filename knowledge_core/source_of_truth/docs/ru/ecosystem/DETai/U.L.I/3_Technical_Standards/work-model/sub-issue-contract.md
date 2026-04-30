---
type: ecosystem
classification:
  scope: DETai_cluster
  context: uli
  layer: technical-standards
  function: explanation
descriptive:
  id: detai-u-l-i-3-technical-standards-work-model-sub-issue-contract
  version: v2
  status: active
  date_ymd: 2026-03-25
  date_update: 2026-04-30
links:
  external_links:
    - type: "MkDocs_ru"
      url: "https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/work-model/sub-issue-contract/"
  document_links:
    - schema: ""
      link_type: ""
      linked_document_id: ""
title: Sub-Issue (Work Package) Contract
---

# Sub-Issue (Work Package) Contract

Тип документа: Standard
v2.0

(контракт для Sub-Issue / Work Package как самостоятельного проверяемого блока работы)

## Purpose

Этот документ задаёт правила заполнения и ведения Sub-Issue / Work Package.

Sub-Issue / Work Package — это ограниченный блок работы внутри Epic Issue, который имеет собственный результат, acceptance tasks, delivery-связь и verification notes.

## Operational Placement

Текущая операционная реализация Sub-Issue / Work Package для проектов DETai ведётся в ClickUp.

- Sub-Issue / Work Package оформляется как подзадача Epic Issue или как связанная задача, если структура проекта требует отдельной верхнеуровневой задачи.
- Она должна находиться в проектной папке ClickUp и в том проектном листе, который был явно передан пользователем.
- Codex или другой агент должен использовать явно переданный пользователем ID / URL листа. Если лист не указан, агент должен запросить его у пользователя перед созданием задач.
- Поле GitHub PR используется как URL-ссылка на Pull Request.
- Поле GitHub Branch используется как текстовое имя ветки.
- После завершения задача сохраняет историю выполнения через статус Complete.

GitHub остаётся code-facing delivery layer: ветка, Pull Request, review и изменения кода фиксируются там. ClickUp является operational planning layer: там фиксируются задача, статус, связи, поля и история выполнения.

## 1. Обязательная структура Sub-Issue / Work Package

### 1.1 Title

Название результата или deliverable.

### 1.2 Purpose

1–3 предложения:

- какой результат появляется после завершения;
- как это продвигает Goal родительской Epic Issue;
- какие границы работы важны, чтобы Sub-Issue / Work Package не расползался.

### 1.3 Parent Epic Issue

Sub-Issue / Work Package должна быть связана с родительской Epic Issue.

Эта связь может быть выражена через:

- ClickUp subtask relation;
- ClickUp linked task relation;
- явную ссылку на родительскую Epic Issue в описании, если техническая структура ClickUp не позволяет сделать связь иначе.

## 2. Acceptance Tasks

Внутри Sub-Issue / Work Package acceptance tasks оформляются как чекбоксы.

Каждый чекбокс представляет собой один Acceptance Task — проверяемый результат, который должен быть достигнут в рамках данного Work Package.

Правила:

- каждый чекбокс = один Acceptance Task;
- весь Sub-Issue / Work Package целиком = один Work Package;
- рекомендуется 3–7 Acceptance Tasks на один Work Package;
- внутри одного Acceptance Task рекомендуется 3–7 Implementation Steps;
- под чекбоксом допускаются notes или короткие Implementation Steps;
- acceptance task должен быть проверяемым, а не просто описывать активность.

### 2.1 Шаблон Acceptance Tasks

```markdown
- [ ] <Acceptance Task #1 — проверяемый результат>
  1. <Implementation Step 1>
  2. <Implementation Step 2>

- [ ] <Acceptance Task #2 — проверяемый результат>
  1. <Implementation Step 1>
  2. <Implementation Step 2>
```

## 3. Delivery

В конце Sub-Issue / Work Package должен быть блок поставки.

```markdown
## Delivery

Branch: `<branch-name>`
PR: `<PR URL>`
```

В ClickUp эти же значения должны быть отражены в полях:

- GitHub Branch — текстовое имя ветки;
- GitHub PR — URL-ссылка на Pull Request.

## 4. Verification Notes

Sub-Issue / Work Package считается завершённым только после финальной проверки результата.

> [!TIP]
> Проверка должна отвечать на вопрос: «Привели ли выполненные Acceptance Tasks к реальному достижению заявленного результата?»

## Related Documents

- [Work Model](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/work-model/work-model/)
- [Epic Issue Contract](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/work-model/issue-contract/)
- [Release Fixation Standard](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/release-fixation-standard/)
- [Производственный цикл проектов и карта ролей вокруг него](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/2_Architecture_and_Logic/production-cycle/)
- Migration Notice: переход Epic Issue / Sub-Issue из Markdown-файлов репозитория в ClickUp