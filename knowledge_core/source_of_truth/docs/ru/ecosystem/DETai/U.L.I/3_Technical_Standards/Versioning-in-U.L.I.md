---
type: ecosystem
classification:
  scope: DETai_cluster
  context: uli
  layer: technical-standards
  function: explanation
descriptive:
  id: detai-u-l-i-3-technical-standards-versioning-in-u-l-i
  version: v2
  status: active
  date_ymd: 2026-03-25
  date_update: 2026-04-30
links:
  external_links:
    - type: "MkDocs_ru"
      url: "https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/Versioning-in-U.L.I/"
  document_links:
    - schema: ""
      link_type: ""
      linked_document_id: ""
title: ♻️ Процесс версионности в U.L.I.
---

# ♻️ Процесс версионности в U.L.I.

Этот документ объясняет, как в U.L.I. понимается и применяется версионность проектов.

Он не описывает версионность документов Knowledge Substrate. Для документов используются отдельные документы Management Layer: [Versioning Standard](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Management_layer/3_Technical_Standards/Versioning-standard/) и [♻️ Процесс версионности](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Management_layer/2_Architecture_and_Logic/Versioning-process/).

В U.L.I. версия проекта фиксирует не просто набор изменений, а новое устойчивое состояние проекта, репозитория или продукта.

## 1. Версия как состояние проекта

Версия проекта означает, что завершён целостный логический этап развития.

Она фиксирует:

- какое новое состояние достигнуто;
- какие возможности, исправления или архитектурные изменения вошли в этот этап;
- какой ресурс или вклад проект начал давать экосистеме сильнее, чем раньше.

Версия не повышается автоматически из-за количества PR, закрытых задач или прошедшего времени. Повышение версии — это решение о зрелости состояния.

## 2. Связь с производственным циклом

В производственном цикле проекта версия появляется после прохождения этапов:

```text
Project Intent -> Work Model Planning -> Implementation -> Release Fixation
```

На этапах Work Model Planning и Implementation работа структурируется и выполняется через Epic Issue, Work Package, branch и PR.

На этапе Release Fixation проверяется, можно ли признать результат новой версией.

Только после успешной Release Fixation версия фиксируется через Git tag, GitHub Release, release summary и связанные материалы, если они применимы к проекту.

## 3. Семантика версий

Типичная логика:

- `v0.1`, `v0.2`, `v0.x` — проект находится в стадии формирования, но уже проходит завершённые циклы развития;
- `v1.0` — проект признан стабильным и готовым к публичной ответственности;
- `v1.x` и выше — развитие стабильного проекта через новые возможности, улучшения, исправления и архитектурные усиления.

Переход к `v1.0` не требует прохождения всех промежуточных значений до `v0.9`.

## 4. Когда повышается версия

Версия повышается, когда завершён новый логический этап и результат прошёл Release Fixation Standard.

Примеры оснований:

- завершена базовая архитектура проекта;
- закрыт важный Epic Issue;
- появился новый устойчивый пользовательский сценарий;
- проект стал выполнять ключевую функцию;
- устранён критический разрыв, который раньше мешал стабильности;
- проект начал приносить новый или усиленный ресурс экосистеме.

## 5. Release Fixation

Release Fixation — это стандартный gate перед признанием новой версии.

Он отвечает на вопрос: можно ли действительно считать текущее состояние проекта новой устойчивой версией?

Подробные правила описаны в [Release Fixation Standard](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/release-fixation-standard/).

## 6. Где фиксируется версия

В проектах U.L.I. версия обычно фиксируется через:

- Git tag;
- GitHub Release;
- release summary;
- README, release notes, если они используются в проекте.

## 7. Версия, стратегия и ресурсы

Новая версия проекта формируется на пересечении внутренней логики развития самого проекта и текущего направления развития экосистемы.

Новая версия проекта должна быть связана с тем, какой ресурс экосистемы она усиливает: продуктовый, технический, инфраструктурный, образовательный, управленческий или иной.

## 8. Практический принцип

Версия в U.L.I. — это не просто число. Она означает завершение этапа развития, признание нового устойчивого состояния и точку, от которой можно строить следующий цикл.

Для проектов и репозиториев применяется двухуровневая модель:

```text
MAJOR.MINOR
```

Примеры:

```text
0.1
1.0
```

Здесь версия отражает завершённый логический этап развития проекта.

Повышение версии происходит только после завершения запланированного этапа, а не в процессе работы. В этот момент создаётся Git-тег, публикуется Release в GitHub, фиксируется завершение Epic Issue.

Версия в данном случае — это одновременно:

- 🧠 управленческое решение;
- 🤝 коммуникационный сигнал команде;
- 🔒 техническая фиксация состояния системы.

## Связанные документы

- [Производственный цикл проектов и карта ролей вокруг него](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/2_Architecture_and_Logic/production-cycle/) — описывает полный цикл от идеи до документационной обвязки.
- [Work Model](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/work-model/work-model/) — описывает этапы Work Model Planning и Implementation.
- [Release Fixation Standard](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/release-fixation-standard/) — задаёт gate и порядок фиксации версии проекта.
- [Versioning Standard](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Management_layer/3_Technical_Standards/Versioning-standard/) — описывает общий стандарт версионности, включая документы.