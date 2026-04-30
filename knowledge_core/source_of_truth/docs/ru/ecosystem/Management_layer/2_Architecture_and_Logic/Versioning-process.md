---
type: ecosystem
classification:
  scope: ecosystem
  context: management-layer
  layer: architecture-and-logic
  function: explanation
descriptive:
  id: management-layer-2-architecture-and-logic-versioning-process
  version: v2
  status: active
  date_ymd: 2026-03-25
  date_update: 2026-04-30
links:
  external_links:
    - type: "MkDocs_ru"
      url: "https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Management_layer/2_Architecture_and_Logic/Versioning-process/"
  document_links:
    - schema: ""
      link_type: ""
      linked_document_id: ""
title: ♻️ Процесс версионности
---

# ♻️ Процесс версионности

Версионность — это способ фиксировать состояние системы во времени.

Она помогает участникам экосистемы понимать:

- какой этап развития уже достигнут и какие правила и подходы действуют сейчас;
- где находится новая редакция, если документ уже вынесен на пересмотр.

## Что такое SemVer в классическом понимании

В индустрии разработки программного обеспечения широко используется Semantic Versioning.

Классическая версия записывается так:

```text
MAJOR.MINOR.PATCH -> например, 1.4.2
```

В DET / DETai эта идея используется не буквально, а как отправная точка. Нам важно не только техническое изменение, но и изменение состояния проекта, документа, правила или процесса.

## Как версионность работает в DET / DETai

Экосистема DET / DETai версионирует не только код.

Версия может фиксировать:

- состояние проекта;
- состояние документа;
- состояние правила;
- состояние процесса;
- состояние смысловой рамки, по которой работают люди и AI-агенты.

Практические форматы версий и обязательные правила повышения версии описывает [Versioning Standard](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Management_layer/3_Technical_Standards/Versioning-standard/).

Проектная логика версий описана отдельно в [♻️ Процесс версионности в U.L.I.](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/Versioning-in-U.L.I/).

## Версия как этап развития

Ключевой принцип:

> версия повышается не автоматически, а по управленческому решению.

Это означает:

- завершён логический этап развития;
- система достигла устойчивого состояния;
- команда признаёт этот этап завершённым;
- новая версия может стать точкой отсчёта для следующего цикла.

Для проекта версия фиксирует состояние системы. Для документа версия фиксирует состояние знания или правила, по которому система действует.

## Версионность как форма обучения

Каждый документ — это часть обучающего цикла экосистемы.

Когда процесс или структура больше не соответствуют реальной практике, мы обновляем документацию, а значит обновляем контекст, по которому дальше будут действовать люди, Codex, Custom GPT и другие AI-агенты.

Пока документ находится в пересмотре, его metadata-статус в Knowledge Substrate становится `draft`. Когда новая версия зафиксирована и перенесена обратно в Knowledge Substrate, статус становится `active`.

## Два слоя статусов

В работе с документами есть два разных слоя статусов.

Первый слой — metadata Knowledge Substrate. Он отвечает на вопрос: можно ли считать этот Markdown текущим каноническим источником истины?

Второй слой — ClickUp workflow в листе `Новые версии документов` папки `Management Layer`. Он отвечает на вопрос: на каком этапе находится работа над новой версией документа?

| Слой | Статус | Где используется | Что значит |
| --- | --- | --- | --- |
| Knowledge Substrate metadata | `active` | YAML front matter Markdown-документа | Документ является текущим каноническим источником истины. |
| Knowledge Substrate metadata | `draft` | YAML front matter Markdown-документа | Документ находится в пересмотре или новая версия ещё не зафиксирована. |
| ClickUp workflow | `BASELINE` | Лист `Новые версии документов` | Слепок текущего канона; его не редактируют. |
| ClickUp workflow | `NEW DOC` | Лист `Новые версии документов` | Новый документ, которого ещё нет в Knowledge Substrate. |
| ClickUp workflow | `DRAFT` | Лист `Новые версии документов` | Рабочая новая версия документа. |
| ClickUp workflow | `IN REVIEW` | Лист `Новые версии документов` | Текст собран и проходит проверку. |
| ClickUp workflow | `READY FOR PUBLICATION` | Лист `Новые версии документов` | Версия готова к переносу обратно в Knowledge Substrate. |
| ClickUp workflow | `ACTIVE` | Лист `Новые версии документов` | Документ опубликован в Knowledge Substrate. |
| ClickUp workflow | `ARCHIVED` | Лист `Новые версии документов` | Старая версия сохранена как исторический след. |

## Как выглядит цикл пересмотра

Когда существующий документ нужно обновить, текущая опубликованная версия сначала становится baseline.

Затем создаётся рабочая draft-копия. После проверки новая версия становится готовой к публикации и возвращается в Knowledge Substrate как active.

Так Knowledge Substrate остаётся местом текущего канона, а ClickUp — местом версионной работы и истории редакций.

## Связанные документы

- [Versioning Standard](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Management_layer/3_Technical_Standards/Versioning-standard/)
- [Документационная архитектура экосистемы](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Management_layer/Docs-Ecosystem/documentation-architecture/)
- [Политика metadata документов](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Management_layer/Docs-Ecosystem/document_metadata_policy/)
- [♻️ Процесс версионности в U.L.I.](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/Versioning-in-U.L.I/)