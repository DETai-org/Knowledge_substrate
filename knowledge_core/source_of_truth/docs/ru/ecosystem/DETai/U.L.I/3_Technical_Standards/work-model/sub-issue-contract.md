---
type: ecosystem
classification:
  scope: DETai_cluster
  context: uli
  layer: technical-standards
  function: explanation
descriptive:
  id: detai-u-l-i-3-technical-standards-work-model-sub-issue-contract
  version: v1
  status: active
  date_ymd: 2026-03-25
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

Тип документа: Standard
v1.0
___

# Sub-Issue (Work Package) Contract
_(контракт для GitHub Sub-Issue, когда Sub-Issue состоит из Tasks (Checklist))_

## Purpose

Этот документ задаёт правила заполнения и ведения **GitHub Sub-Issue**

---

## 0) Канон имени для файла Sub-Issue

Формат имени файла Sub-Issue (Work Package):

`<number>-sub-issue-<mechanism>-<entity>.md`

👉 **Базовый slug механизма** получается удалением префикса `<number>-sub-issue-`:

Именно этот slug используется для поиска и создания связанных документов в папках
docs/guides/
docs/ADR/
docs/Policy/
Некоторые типы связанных документов по архитектуре системы могут находиться **в других хранилищах** (см.🐝 Архитектура U.L.I. [Документационная архитектура U.L.I.](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/2_Architecture_and_Logic/documentation-architecture-U-L-I/))

Базовый `slug` в именах связанных документов **не обязан совпадать посимвольно** с именем Sub-Issue, но должен быть **достаточно близким по смыслу и формулировке**, чтобы по нему можно было однозначно распознать, что все эти файлы относятся к одному и тому же процессу работы.

## 1) Обязательная структура Sub-Issue (Work Package)

### 1.1 Title
Название результата (deliverable),

### 1.2 Purpose
1–3 предложения:
- какой результат появляется после мерджа,
- как это продвигает Goal родительской Epic Issue.

---
## 2) Tasks (checklist внутри Sub-Issue)

Внутри Sub-Issue Acceptance Tasks оформляются как **чекбоксы**.

Каждый чекбокс представляет собой **один Acceptance Task** — проверяемый результат,
который должен быть достигнут в рамках данного Work Package (Sub-Issue).
### 2.2 Шаблон одного Sub-Issue (Work Package)

```markdown
- [ ] <Acceptance Task #1 — проверяемый результат>
  1. <Implementation Step 1>
  2. <Implementation Step 2>

- [ ] <Acceptance Task #2 — проверяемый результат>
  1. <Implementation Step 1>
  2. <Implementation Step 2>

- [ ] <Acceptance Task #3 — проверяемый результат>
  1. <Implementation Step 1>
  2. <Implementation Step 2>

- [ ] <Acceptance Task #4 — проверяемый результат>
```

ПРИМЕР одного Acceptance Task 📃:
```markdown
- [ ] Реализовать расчёт эмбеддингов и построение semantic graph
1. Использовать `knowledge.embeddings` для doc‑level embeddings (upsert по `(doc_id, model)`), без чанков.
2. Создать индекс для pgvector (ivfflat или hnsw) и выполнять top‑K поиск.
3. Фильтровать по `min_similarity`.
4. Нормализовать направление ребра (source\_id < target\_id), сохранять в `knowledge.similarity_edges`, обновлять `updated_at`.
5. Исключить дубликаты (UNIQUE по (source\_id, target\_id, doc\_type, method)).
```

Правила:

- каждый чекбокс = **один Acceptance Task**,
- весь Sub-Issue целиком = **один Work Package**,
- рекомендуется 3–7 Acceptance Tasks на один Sub-Issue,
- внутри одного Acceptance Task рекомендуется 3–7 Implementation Steps,
- под чекбоксом допускаются Notes или короткие Implementation Steps,
___

## 3) Verification Notes (обязательно при закрытии)

Sub-Issue (Work Package) считается завершённым только после выполнения
финальной проверки результата.

> [!TIP] Проверка должна отвечать на вопрос:
> *«Привели ли выполненные Acceptance Tasks к реальному достижению заявленного результата?»*

Завершение означает, что подтверждено не только выполнение задач,
но и достижение итогового результата, ради которого они выполнялись.

Маленький, практичный Prompt для агента Codex/Copilot:

```Copy
Verification Prompt
```


## 4) Delivery

В конце Sub-Issue всегда держи блок поставки:

🚚 Delivery
Branch: `<branch-name>`
PR: `<#id or link>`
