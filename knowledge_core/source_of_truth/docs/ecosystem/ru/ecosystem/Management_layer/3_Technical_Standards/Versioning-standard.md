---
type: ecosystem
classification:
  scope: ecosystem
  context: management-layer
  layer: technical-standards
  function: standard
descriptive:
  id: management-layer-3-technical-standards-versioning-standard
  version: v3
  status: active
  date_ymd: 2026-10-23
  date_update: 2026-10-23
links:
  external_links:
    - type: "MkDocs_ru"
      url: "https://docs.detai-x.com/ru/ecosystem/Management_layer/3_Technical_Standards/Versioning-standard/"
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

Проектная логика версий подробно описана в [♻️ Процесс версионности в U.L.I.](https://docs.detai-x.com/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/Versioning-in-U.L.I/).

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

## Статус документа и состояние редакционной работы

Поле `descriptive.status` описывает жизненный цикл документа: `active` — действующая редакция, `draft` — рабочий текст для review. Остальные значения определяет [политика metadata](../Docs-Ecosystem/document_metadata_policy.md). Каноническая сила задаётся отдельно через `governance.canonicality`: статус `active` сам по себе не делает рабочую модель обязательной нормой.

Редакционная работа имеет собственные стадии: исходная версия (baseline), новая редакция, review, готовность к публикации и опубликованный результат. Это смысловые стадии процесса, а не гарантированные значения статуса Task или Note в Team OS.

Рабочие материалы собираются в Note List [«Новые версии документов»](https://team.detai-x.com/task-center/lists/ccfaa624-198d-52c8-9d40-bb6c719b0833) в Management Layer. Задачи исполнения ведутся в соответствующих Task Lists; итоги — в разрешённых WorkLog Lists. Тип и маршрут проверяются по текущему Core. Исторические поля ClickUp не определяют допустимые операции с Note.

## Повышение версии существующего документа

1. Найти канонический Markdown source file в Knowledge Substrate и проверить владельца и границы документа.
2. Зафиксировать baseline ссылкой на исходный файл и неизменяемый commit SHA. Полнотекстовый дубликат в task-системе не обязателен.
3. Подготовить новую редакцию в рабочей ветке. Для корпуса `ru/ecosystem/*` действует маршрут `docs/ecosystem → main`, установленный правилами репозитория.
4. При смысловом изменении повысить `descriptive.version`, обновить дату текущей редакции и применимые связи. Сохранить stable ID.
5. Провести содержательный review и проверить metadata, ссылки, навигацию и сборку документации.
6. Опубликовать редакцию через принятый PR-процесс. До этого действующая опубликованная версия продолжает быть исходным состоянием; начало работы над PR не требует переводить её в `draft`.
7. Связать рабочие материалы и итог с PR и опубликованной версией. Предыдущая редакция остаётся доступной в Git history.

Публикация файла не повышает `draft/working` до `active/canonical` автоматически. Изменение нормативной силы требует соответствующего решения. Равным образом release проекта не определяет статус описывающего его документа.

В metadata новой содержательной версии:

```yaml
descriptive:
  version: v<N>
  status: <подтверждённый статус документа>
  date_ymd: <дата текущей содержательной версии>
  date_update: <дата обновления, если поле используется>
```

Историческая схема ClickUp с копиями BASELINE/DRAFT и переносом текста обратно в Git сохраняется как история прежнего процесса. Для новых редакций источником версий является Git, а Team OS связывает работу, материалы и результаты.

## Связанные документы

- [♻️ Процесс версионности](https://docs.detai-x.com/ru/ecosystem/Management_layer/2_Architecture_and_Logic/Versioning-process/)
- [Документационная архитектура экосистемы](https://docs.detai-x.com/ru/ecosystem/Management_layer/Docs-Ecosystem/documentation-architecture/)
- [Политика metadata документов](https://docs.detai-x.com/ru/ecosystem/Management_layer/Docs-Ecosystem/document_metadata_policy/)
