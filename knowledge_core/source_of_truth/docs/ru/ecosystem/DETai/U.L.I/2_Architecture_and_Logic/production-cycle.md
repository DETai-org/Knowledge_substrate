---
type: ecosystem
classification:
  scope: DETai_cluster
  context: uli
  layer: architecture-and-logic
  function: explanation
descriptive:
  id: production-cycle
  version: v1
  status: active
  date_ymd: 2026-04-29
  date_update: 2026-04-30
links:
  external_links:
    - type: "MkDocs_ru"
      url: "https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/2_Architecture_and_Logic/production-cycle/"
  document_links:
    - schema: ""
      link_type: ""
      linked_document_id: ""
title: Производственный цикл проектов и карта ролей вокруг него
---

# Производственный цикл проектов и карта ролей вокруг него

Этот документ описывает полный производственный цикл DETai: как мысль превращается в проектное намерение, затем в работу, реализацию, релизную фиксацию и документационную обвязку.

Короткая формула цикла:

```text
мысль/идея -> план проекта -> Epic Issue -> Work Package -> код / результат -> версия -> документационная обвязка -> новый смысл
```

## 1. Project Intent

На первом этапе появляется мысль, наблюдение или возможность, которая постепенно оформляется в проектное намерение.

Здесь важно понять:

- что именно должно измениться;
- зачем это изменение нужно;
- какой новый смысл или ресурс оно может дать экосистеме;
- готова ли мысль стать проектом или пока должна остаться в пространстве наблюдений.

Если идея ещё не созрела, она фиксируется как импульс. Для этого в нашей системе есть место, оно называется "🧠 Еще мысль", это материал/хаб для будущего развития. Если из неё уже сформировался вектор, он может перейти в Epic Issue.

Смысловую методологию этого перехода описывает документ [Методология проектного цикла DETai](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/2_Architecture_and_Logic/metodologiya-proyektnogo-tsikla-detai/).

## 2. Work Model Planning

На втором этапе проектное намерение переводится в четкий план.

Здесь формируются:

- Epic Issue как блок смысла и навигации;
- Sub-Issue / Work Package как поставляемые фрагменты результата;
- Acceptance Tasks как проверяемые результаты;
- критерии завершения и связи с будущим PR.

Этот этап уже относится к Work Model. Производственный цикл только показывает место этапа в общей траектории, а конкретные правила структуры задаются связкой [Модель работы](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/work-model/) и [Work Model](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/work-model/work-model/).

## 3. Implementation

На третьем этапе Work Package выполняется.

Типичная форма выполнения:

```text
Work Package -> branch -> PR -> проверка -> merge
```

На этом уровне Codex или другой исполнитель работает внутри заданного Epic Issue, выполняет Sub-Issue / Work Package / checklist, фиксирует важные решения и доводит результат до проверяемого состояния.

Этот этап также регулируется Work Model: именно там описаны роли Epic Issue, Work Package, Acceptance Tasks, Implementation Steps, PR и финальной проверки.

## 4. Release Fixation

Release Fixation отвечает за момент, когда результат работы перестаёт быть набором изменений и становится зафиксированным состоянием проекта, репозитория или документационной системы.

На этом этапе уточняется:

- какая версия или состояние завершены;
- какие PR, решения и документы входят в итог;
- что должно быть отражено в changelog, release notes или release summary.

Этот этап описан отдельным стандартом [Release Fixation Standard](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/release-fixation-standard/) и не смешивается с Work Model.

## 5. Documentation Architecture

На пятом этапе результат цикла связывается с Knowledge Substrate и другими документальными слоями.

Здесь определяется:

- какие документы нужно обновить;
- какие новые документы нужно создать;
- какие старые документы стали устаревшими;
- какие статусы и версии должны измениться;
- какие элементы должны перейти в ClickUp-лист «Новые версии документов».

Этот этап закрывает цикл: результат становится частью знания экосистемы и может породить новые мысли, наблюдения и будущие проектные намерения.

## Распределение документов по этапам

| Этап производственного цикла | Основной вопрос | Документ / связка |
| --- | --- | --- |
| 1. Project Intent | Как мысль становится проектным намерением? | Методология проектного цикла DETai |
| 2. Work Model Planning | Как намерение разложить на структуру работы? | Модель работы и Work Model |
| 3. Implementation | Как выполнить Work Package через branch, PR и проверку? | Work Model, Epic Issue Contract, Sub-Issue (Work Package) Contract |
| 4. Release Fixation | Как зафиксировать достигнутое состояние? | Release Fixation Standard, ♻️ Процесс версионности в U.L.I. |
| 5. Documentation Architecture | Как результат становится частью Knowledge Substrate? | Versioning Standard, ♻️ Процесс версионности, Политика metadata документов |

## Роли и skills

Производственный цикл может поддерживаться разными ролями и Codex skills.

На уровне Project Intent skill может выполнять роль фасилитатора и сверять идею с тем, какой ресурс эта идея может принести и в каком из эшелонов он может быть будущий проект.

На уровне Work Model Planning и Implementation ключевым становится агент, который умеет работать внутри Epic Issue / Work Package, удерживать scope, выполнять checklist и готовить PR.

## Граница документа

Этот документ отвечает за карту цикла и распределение ответственности между этапами.

Он не должен подробно описывать:

- внутреннюю механику Acceptance Tasks и PR;
- правила повышения версий документов;
- конкретный формат release notes;
- политику metadata;
- правила публикации Knowledge Substrate.

Эти темы должны жить в соответствующих стандартах и процессных документах, а производственный цикл должен связывать их в одну понятную траекторию.

## Связанные документы

- [Методология проектного цикла DETai](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/2_Architecture_and_Logic/metodologiya-proyektnogo-tsikla-detai/) — объясняет переход от мысли к проектному намерению.
- [Модель работы](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/work-model/) — индекс связки Work Model.
- [Work Model](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/work-model/work-model/) — процесс этапов Work Model Planning и Implementation.
- [Release Fixation Standard](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/release-fixation-standard/) — стандарт фиксации версии проекта.
- [Versioning Standard](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Management_layer/3_Technical_Standards/Versioning-standard/) — стандарт версионности документов.
- [♻️ Процесс версионности](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Management_layer/2_Architecture_and_Logic/Versioning-process/) — объяснение процесса версионности.