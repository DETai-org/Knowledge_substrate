---
type: ecosystem
classification:
  scope: ecosystem
  context: management-layer
  layer: technical-standards
  function: standard
descriptive:
  id: management-layer-3-technical-standards-versioning-standard
  version: v2
  status: active
  date_ymd: 2026-03-25
  date_update: 2026-04-30
links:
  external_links:
    - type: "MkDocs_ru"
      url: "https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Management_layer/3_Technical_Standards/Versioning-standard/"
  document_links:
    - schema: ""
      link_type: ""
      linked_document_id: ""
title: Versioning Standard
---

# Versioning Standard

Этот документ устанавливает форматы версий и обязательные правила повышения версии в экосистеме DET / DETai.

Версия фиксирует не просто изменение текста, файла или задачи, а новое устойчивое состояние документа, проекта или процесса. У нас чуть отличаются правила для версий проектов и версий документов.

## Версии проектов

Проектная логика версий подробно описана в [♻️ Процесс версионности в U.L.I.](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/Versioning-in-U.L.I/).

## Версии документов

Для большинства документов используется одноуровневая модель:

```text
v1
v2
v3
```

Эта модель применяется для документов типов: `explanation`, `standard`, `policy`, `tutorial`, `guide`, `how-to`, `reference`.

Каждая новая версия означает новую редакцию документа. Небольшие исправления опечаток, форматирования или ссылок не требуют повышения версии, если они не меняют смысл документа.

## Edition для философских и governance-документов

Для документов, у которых `layer: philosophy`, или для governance-документов с характером принципов, концепции или доктрины, может использоваться модель edition: `1st-edition`, `2nd-edition`, `3rd-edition`.

## Metadata-статусы Knowledge Substrate

В YAML front matter Knowledge Substrate поле `descriptive.status` описывает состояние канонического Markdown-документа.

| Metadata status | Значение |
| --- | --- |
| `active` | Документ является текущим каноническим источником истины. |
| `draft` | Документ находится в пересмотре или новая версия ещё не зафиксирована. |

## ClickUp-статусы новых версий документов

Для работы над новыми версиями документов используется ClickUp-лист `Новые версии документов` в папке `Management Layer`.

| ClickUp status | Тип статуса | Значение |
| --- | --- | --- |
| `BASELINE` | Not started | Существующий документ из Knowledge Substrate вынесен как точка сравнения перед новой редакцией. |
| `NEW DOC` | Not started | Новый документ, которого ещё нет в Knowledge Substrate. |
| `DRAFT` | Active | Рабочая новая версия документа. |
| `IN REVIEW` | Active | Текст собран и проходит проверку. |
| `READY FOR PUBLICATION` | Active | Версия готова к переносу обратно в Knowledge Substrate. |
| `ACTIVE` | Done | Документ опубликован в Knowledge Substrate. |
| `ARCHIVED` | Closed | Старая версия сохранена как исторический след. |

## Повышение версии существующего документа

Когда существующий документ Knowledge Substrate нуждается в новой версии, используется цепочка:

```text
ACTIVE -> BASELINE -> DRAFT -> IN REVIEW -> READY FOR PUBLICATION -> ACTIVE
```

Обязательный порядок действий:

1. Найти канонический Markdown source file в Knowledge Substrate.
2. Перевести в Knowledge Substrate только `descriptive.status` документа в `draft`.
3. Создать задачу в ClickUp-листе `Новые версии документов` со статусом `BASELINE`.
4. Перенести полный текущий Markdown документа, включая YAML front matter и body.
5. Создать дубликат baseline-задачи для новой версии и перевести его в `DRAFT`.
6. В `DRAFT` вносить содержательные правки.
7. После сборки текста перевести задачу в `IN REVIEW`.
8. После проверки перевести задачу в `READY FOR PUBLICATION`.
9. После публикации новой версии в Knowledge Substrate перевести опубликованную задачу в `ACTIVE`.
10. Старую baseline-задачу перевести в `ARCHIVED`.

В Knowledge Substrate новая опубликованная версия получает:

```yaml
descriptive:
  version: v<N>
  status: active
  date_ymd: <дата публикации>
  date_update: <дата загрузки в Knowledge Substrate>
```

## Связанные документы

- [♻️ Процесс версионности](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Management_layer/2_Architecture_and_Logic/Versioning-process/)
- [Документационная архитектура экосистемы](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Management_layer/Docs-Ecosystem/documentation-architecture/)
- [Политика metadata документов](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Management_layer/Docs-Ecosystem/document_metadata_policy/)
