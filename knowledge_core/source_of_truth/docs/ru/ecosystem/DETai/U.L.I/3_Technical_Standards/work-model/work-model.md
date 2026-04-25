---
type: ecosystem
classification:
  scope: DETai_cluster
  context: uli
  layer: technical-standards
  function: explanation
descriptive:
  id: detai-u-l-i-3-technical-standards-work-model-work-model
  version: v1
  status: active
  date_ymd: 2026-03-25
links:
  external_links:
    - type: "MkDocs_ru"
      url: "https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/work-model/work-model/"
  document_links:
    - schema: ""
      link_type: ""
      linked_document_id: ""
title: Work Model
---

> [!INFO]
Формирование этого процесса идёт в связке с Промтом
[issue_subissue_assembler](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/issue_subissue_assembler/)

# Work Model
(Epic Issue → Sub-Issue → PR)

## Purpose

Этот документ определяет переиспользуемый, нативный для платформы GitHub способ структурирования и выполнения работы с помощью чёткой иерархии:
**Epic Issue → Sub-Issue  (Work Package) → Tasks (Checklist) → Implementation Steps**.

Он спроектирован так, чтобы быть:

- переиспользуемым для любого типа проектов (код, контент, инфраструктура, исследования, продукт),
- совместимым с GitHub Issues / Sub-issues / Projects,
- agent-friendly (хорошо работает с coding agents, которые работают в branch и создают PR).

---
## Core Entities (Canonical Vocabulary)

### 1) Epic Issue

**GitHub entity:** Issue (родительский уровня Epic Issue)
**Role:** верхнеуровневое направление / крупный поток работ / цель масштаба версии
**Отвечает на вопросы:** _Зачем мы это делаем? Каково целевое состояние?_
**Содержит:** scope (область работ), стратегию, список sub-issues, критерии завершения.

**Ключевой принцип:** Epic Issue — это про **навигацию**, а не про реализацию. В целом Epic Issue описывает **вектор развития репозитория**: по завершении Epic Issue через выполнение её Sub-Issues система переходит в новое функциональное состояние —  что можно рассматривать как завершения версии проекта/репо

---

### 2) Sub-Issue (Work Package)

**GitHub entity:** Sub-issue внутри Epic Issue
**Role:** единица поставки результата, которая заканчивается **мерджем одного PR**
**Отвечает на вопрос:** _Что именно мы поставляем в этом срезе работы?_
**Содержит:** 3–7 acceptance tasks (пункты checklist), ссылки на поставку (branch/PR), заметки о проверке.

**Жёсткое правило:** **1 Work Package = 1 branch = 1 PR**.
По завершению Sub-Issue добавляется новый слой возможностей или завершается важный этап архитектуры.

---

### 3) Task (Checklist Item)

Альтернативное название Acceptance Task
**GitHub entity:** checkbox-пункт внутри Sub-Issue
**Role:** _проверяемый результат_ (а не расплывчатая активность)
**Отвечает на вопрос:** _Какой конкретный результат должен появиться?_

**Рекомендация:** 3–7 tasks на один Sub-Issue (≈ **5 ± 2**).

---

### 4) Implementation Steps (Subtasks)

_(шаги реализации / подзадачи)_

**GitHub entity:** нумерованный список (алгоритм) внутри Acceptance Task
**Role:** конкретные технические действия, из которых складывается выполнение task
**Отвечает на вопрос:** _Как именно реализовать этот task?_

Это самый нижний уровень иерархии — здесь уже нет целей, только действия

```markdown
Пример: Если Task "Подготовить ingest-модуль для чтения publish-постов из SoT"
то список внутри:

1. В коде ingest‑модуля пройти по путям SoT с постами.
2. Прочитать markdown‑файлы, извлечь frontmatter и body.
3. Отфильтровать записи: `type == "post"` и `administrative.status == "publish"`.
4. Построить `text_for_embedding`: очистить markdown, собрать `title + "\n\n" + body_text`.
5. Сформироваь объект поста с полями: id, title, authors, date\_ymd, channels, taxonomy (rubric\_ids, category\_ids), text\_for\_embedding.
6. Подготовить README/описание, если требуется контрактом.
```

**📝 Важно:**
Subtask — это не цель, а **операция**.  Acceptance Task — это **результат**, Subtask — это **шаг к результату**.
Иерархии в уровнях Epic Issue / Sub-Issue / Task / Subtask

#### Size & Cognitive Load
_(размер и когнитивная нагрузка)_

- **Work Package:** 3–7 Acceptance Tasks (идеально ~5)
- **Acceptance Task:** 3–10  (достаточно подробно, чтобы выполнить; не превращать в техдок на 10 страниц)

Почему именно так ⁉️

Здесь используется принцип из психологии памяти: **7 ± 2 элемента** — классический предел удержания в рабочей памяти.
Но так как: модель новая, задачи часто сложные, в процессе участвуют и люди, и агенты,
мы используем более консервативный стандарт:  **5 ± 2**, то есть **3–7 Acceptance Tasks** на один Work Package. Это даёт устойчивое внимание и удобный объём для одного PR.

---

## Delivery Rules (What “Done” Means)

_(правила завершения — что считается “сделано”)_

### Definition of Done (Work Package)

Work Package считается **Done** только когда:

1. все Acceptance Tasks отмечены (checklist полностью закрыт),
2. выполнена финальная проверка,

Пункт 2 — **финальная проверка** 🔎 :
Используй промт: [🔍 Финальная проверка перед merge](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Промты для Codex/#🔍 Финальная проверка перед merge)

То есть это не просто «глазом посмотрели», а: осмысленная проверка по критериям, с короткими заметками о результате.

И только после этого PR смержен в main branch и Sub-Issue выполнен ✅

---
### Epic Issue Completion

Завершение Epic Issue может идти неделями в него могут добавляться новые Sub-Issue

Epic Issue считается **Done** ✅, когда:
- все Sub-Issue завершены (смёрджены), и
- выполнены критерии завершения на уровне Epic Issue.

"При добавлении новых Sub-Issue убедись, что они соответствуют целям и остаются в рамках этой Epic Issue. Если новые Sub-Issue выходят за рамки, необходимо создать новую Epic Issue, чтобы сохранить чёткую навигацию

---

### Linking Rules 🚚

Пишем в конце  Sub-Issue

ПРИМЕР
```markdown
PR: Добавить ShareSection и синхронизировать фильтры блога personal-site [#310](https://github.com/DETai-org/sites/pull/310)

Ветка: codex/migrate-blog-card-format-to-personal-site-fgdmet
```

