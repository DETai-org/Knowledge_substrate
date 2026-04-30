---
type: ecosystem
classification:
  scope: DETai_cluster
  context: uli
  layer: technical-standards
  function: explanation
descriptive:
  id: detai-u-l-i-3-technical-standards-work-model-work-model
  version: v2
  status: active
  date_ymd: 2026-03-25
  date_update: 2026-04-30
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

# Work Model

Work Model — это процессная модель выполнения работы в DETai: от Epic Issue и Work Package до branch, PR и проверяемого результата.

В производственном цикле проектов она покрывает этапы:

- 2. Work Model Planning — проектное намерение переводится в структуру работы;
- 3. Implementation — Work Package выполняется через branch, PR, checklist и финальную проверку.

Конкретные обязательные поля, шаблоны и форматы оформления живут в контрактах: [Epic Issue Contract](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/work-model/issue-contract/) и [Sub-Issue / Work Package Contract](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/work-model/sub-issue-contract/).

## Purpose

Этот документ определяет переиспользуемый способ структурирования и выполнения работы через иерархию:

```text
Epic Issue -> Sub-Issue / Work Package -> Acceptance Tasks -> Implementation Steps -> PR
```

Модель спроектирована так, чтобы быть:

- переиспользуемой для кода, контента, инфраструктуры, исследований и документации;
- совместимой с ClickUp-задачами, GitHub branches и Pull Requests;
- понятной для людей и agent-friendly для Codex;
- достаточно строгой, чтобы сохранять контекст между шагами, но не превращать каждую простую правку в тяжёлый процесс.

## Operational Placement (операционное размещение)

Текущая операционная реализация Work Model для проектов DETai ведётся в ClickUp.

У каждого проекта есть своя папка. Внутри папки используется проектный лист, где:

- Epic Issue оформляется как верхнеуровневая задача;
- Sub-Issue / Work Package оформляется как подзадача или связанная задача;
- статус Complete сохраняет историю завершённых Epic Issue и Sub-Issue;
- поле GitHub PR хранит URL-ссылку на соответствующий Pull Request;
- поле GitHub Branch хранит название ветки как текстовое значение;
- даты создания, статусы, комментарии и связи задач сохраняют операционный след выполнения.

Если Codex или другой агент создаёт новую проектную структуру в ClickUp, он должен использовать лист, явно указанный пользователем, либо запросить у пользователя ссылку или ID нужного листа. Нельзя создавать Epic Issue в произвольном листе только по догадке.

GitHub остаётся местом code-facing поставки результата: branch, PR, merge history, Git tag и GitHub Release. Поэтому Work Package должен сохранять ссылки на branch и PR даже тогда, когда сама структура Epic Issue / Sub-Issue ведётся в ClickUp.

## 1. Epic Issue

Role: верхнеуровневый блок смысла, направление или цель масштаба версии.

Epic Issue отвечает на вопросы: зачем мы это делаем, какое состояние должно измениться, какой переход считается успешным.

Epic Issue содержит:

- смысловой контекст;
- scope работ;
- список Sub-Issue / Work Package;
- критерии завершения;
- ссылки на связанные документы, решения и результаты.

## 2. Sub-Issue / Work Package

Role: единица поставки результата, которая обычно завершается одним PR.

Базовое правило:

```text
1 Work Package = 1 branch = 1 PR
```

Work Package содержит:

- локальный контекст;
- ожидаемый результат;
- 3–7 Acceptance Tasks;
- ссылки на branch и PR;
- заметки о проверке.

## 3. Acceptance Task

Role: проверяемый результат, а не расплывчатая активность.

Хорошая Acceptance Task формулируется как результат, который можно проверить: компонент добавлен, документ обновлён, тест проходит, сценарий работает, решение зафиксировано, ссылка или контракт приведены в соответствие.

## 4. Implementation Steps

Implementation Steps — это нижний уровень модели: последовательность действий, которую можно выполнить, проверить и связать с результатом.

Acceptance Task — это результат. Implementation Step — это шаг к результату.

## 5. Delivery Rules

Work Package считается завершённым только когда:

- все Acceptance Tasks выполнены;
- результат проверен;
- PR готов к merge или уже смержен;
- ссылки на PR, branch и важные решения зафиксированы в Sub-Issue.

## 6. Epic Issue Completion

Epic Issue считается завершённым, когда:

- все входящие Work Package закрыты или явно сняты с текущего scope;
- критерии завершения Epic Issue выполнены;
- итоговый результат зафиксирован;
- понятно, требуется ли Release Fixation и обновление документационной обвязки.

## 7. Связь с другими этапами

Work Model получает вход из этапа Project Intent: уже есть смысловой вектор, который можно структурировать.

После выполнения Work Package результат передаётся дальше:

- в Release Fixation, если нужно зафиксировать новую версию проекта или репозитория;
- в Documentation Architecture, если результат требует обновления Knowledge Substrate, стандартов, описаний, tutorials или onboarding.

Таким образом, Work Model является рабочим мостом между намерением и поставкой результата.

## Связанные документы

- [Модель работы](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/work-model/) — индекс связки Work Model.
- [Epic Issue Contract](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/work-model/issue-contract/) — контракт Epic Issue.
- [Sub-Issue / Work Package Contract](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/work-model/sub-issue-contract/) — контракт Work Package.
- [Производственный цикл проектов и карта ролей вокруг него](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/2_Architecture_and_Logic/production-cycle/) — карта полного цикла DETai.
- [Методология проектного цикла DETai](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/2_Architecture_and_Logic/metodologiya-proyektnogo-tsikla-detai/) — объясняет переход от мысли к проектному намерению.