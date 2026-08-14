---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: knowledge-system
  layer: technical-standards
  function: policy
  system: knowledge
  domain: document-metadata
  audiences: [team, editors, developers, agents]
descriptive:
  id: management-layer-docs-ecosystem-document-metadata-policy
  version: v5
  status: active
  date_ymd: 2026-08-14
governance:
  canonicality: canonical
  visibility: public
  owner_role: knowledge-architect
  approver_role: ecosystem-architect
  review_date: 2026-09-05
object_state:
  architecture_status: canonical
  implementation_status: operational
  evidence_status: not-applicable
  visibility_status: public
links:
  external_links:
    - type: MkDocs_ru
      url: https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Management_layer/Docs-Ecosystem/document_metadata_policy/
  document_links:
    - schema: ecosystem
      link_type: implements
      linked_document_id: knowledge-document-model
    - schema: ecosystem
      link_type: governs
      linked_document_id: management-layer-docs-ecosystem-metadata-schema-registry
title: Политика metadata документов
---

# Политика metadata документов

Metadata делает документ частью управляемой системы знаний: показывает его предмет, функцию, статус, каноничность, видимость, владельца и связи. Порядок пунктов в меню и расположение файла не заменяют эти сведения.

Политика определяет общие правила metadata и управляет contracts зарегистрированных типов. Поля конкретного типа, их обязательность и допустимые значения задаёт [реестр metadata schemas](metadata_schema_registry.md). Старые документы мигрируют только после содержательного review; неизвестное значение не заполняется предположением.

## Полный целевой блок

```yaml
---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: technology-layer
  layer: architecture-and-logic
  function: explanation
  system: technology
  domain: uli-platform-interface
  audiences: [public, team, agents]
descriptive:
  id: stable-document-id
  version: v1
  status: active
  date_ymd: 2026-08-05
governance:
  canonicality: canonical
  visibility: public
  owner_role: technical-lead
  approver_role: ecosystem-architect
  review_date: 2026-09-05
object_state:
  architecture_status: canonical
  implementation_status: operational
  evidence_status: not-applicable
  visibility_status: public
links:
  external_links:
    - type: MkDocs_ru
      url: https://example.org/path/
  document_links:
    - schema: ecosystem
      link_type: implements
      linked_document_id: another-stable-id
title: Человекочитаемое название
---
```

## Идентичность

### `type`

Определяет schema metadata. Общие правила идентичности, классификации, связей и честного заполнения задаёт эта политика; типовые поля и ограничения — [реестр metadata schemas](metadata_schema_registry.md).

Сейчас зарегистрированы contracts `ecosystem` и `log-summary`. Для книг, публикаций, проектов и runtime-объектов используются собственные зарегистрированные contracts. Значение `type` нельзя вводить только в отдельном документе или prompt: оно сначала добавляется в реестр.

### `title`

Человекочитаемое название. Оно должно совпадать по смыслу с H1, но может быть короче. Техническое имя файла не считается заголовком.

### `descriptive.id`

Стабильный уникальный идентификатор. Не меняется при переименовании файла или URL. Повторное использование ID для другой сущности запрещено.

## Предметная классификация

### `classification.scope`

Граница действия документа. Базовое значение общего канона — `DETai_ecosystem`; более узкие значения вводятся реестром соответствующей schema, а не свободно. Например, contract `log-summary` регистрирует операционные области `Tools`, `Infrastructure` и `Governance`.

### `classification.context`

Среда или конкретный контейнер, к которому относится документ. Contract определяет кардинальность поля. Для `ecosystem` это одно значение вроде `ecosystem-architecture`, `technology-layer`, `governance-operating-model`, `product-market-system` или `knowledge-system`. Для `log-summary` это один конкретный контекст Folder/List, например `codex` или `onboarding`.

### `classification.system`

Система-владелец предмета. Базовые значения текущей архитектуры:

- `architecture`;
- `method-institution`;
- `technology`;
- `governance-operating-model`;
- `product-market`;
- `legal-economic`;
- `trust`;
- `evidence`;
- `knowledge`.

Новое значение добавляется только вместе с определением границы системы.

### `classification.domain`

Уточняет предмет внутри system. Значение должно иметь owner role и использоваться последовательно в связанных документах.

### `classification.layer`

Показывает архитектурный слой знания: например `principles`, `architecture-and-logic`, `operating-model`, `technical-standards`, `cross-cutting-system` или `public-interface`.

### `classification.function`

Функция документа: `index`, `philosophy`, `principle`, `guide`, `explanation`, `standard`, `policy`, `reference`, `register`, `decision-record`, `tutorial`, `how-to`, `runbook`, `brief`, `note` или `log-summary`.

Функция отображается в карточке страницы, но не определяет верхний уровень навигации. Значения подробно раскрыты в [реестре функций](functions_of_documents.md).

### `classification.audiences`

Список предполагаемых читателей или потребителей. Он помогает формировать role views, но не заменяет access control.

## Состояние документа

### `descriptive.version`

Версия содержательного состояния документа. Изменение формулировок, статуса, связей или правил требует обновить версию по применяемому versioning standard.

### `descriptive.status`

Стадия жизненного цикла. Базовые значения:

- `concept` — сформулирован объект, но модель ещё не применяется;
- `draft` — рабочий текст для review;
- `active` — действующая версия;
- `deprecated` — использование прекращается;
- `superseded` — заменён указанным документом;
- `archived` — сохранён как завершённая история.

### `descriptive.date_ymd`

Дата текущей содержательной версии в `YYYY-MM-DD`. Механическое форматирование не требует менять дату.

## Состояние описываемого объекта

`descriptive.status` относится к самому документу. Если страница описывает управляемую сущность, после содержательного review может добавляться отдельный блок `object_state`:

- `architecture_status` — `canonical`, `approved-target`, `experiment`, `hypothesis`, `deprecated` или `retired`;
- `implementation_status` — `not-started`, `in-design`, `prototype`, `controlled-pilot`, `commercial-beta`, `operational`, `paused` или `closed`;
- `evidence_status` — `untested`, `preliminary-support`, `supported`, `validated-within-scope`, `contested`, `contradicted` или `not-applicable`;
- `visibility_status` — `public`, `team`, `restricted`, `legal-privileged` или `personal-data`.

Действующий документ может честно описывать гипотезу или прототип. Поля не выводятся автоматически из `descriptive.status`; полная логика задана в [многомерной модели статуса](../../../knowledge/object-status-model.md).

## Governance

### `governance.canonicality`

- `canonical` — определяет обязательное понятие, правило или границу;
- `working` — используется как рабочая модель и ожидает решения;
- `reference` — объясняет или проецирует другой источник;
- `historical` — сохраняет прежнюю позицию.

`status: active` не делает документ каноническим автоматически.

### `governance.visibility`

- `public` — допустим в открытой публикации;
- `team` — предназначен только команде;
- `restricted` — доступ по назначенным ролям;
- `secret` — факт существования и доступ минимизируются.

Поле классифицирует документ, но само по себе не обеспечивает техническую защиту.

### `owner_role`, `approver_role`, `review_date`

`owner_role` отвечает за актуальность, `approver_role` — за придание требуемой силы, `review_date` — за обязательный следующий пересмотр. Используются роли, а не имена людей; фактическое назначение хранится в operational system.

## Связи

### `external_links`

Содержит официальные публичные или внешние представления. URL обновляется при миграции маршрута.

### `document_links`

Каждая связь содержит schema, тип отношения и стабильный ID цели. Базовые отношения:

- `defines`, `implements`, `governs`, `constrains`;
- `part-of`, `depends-on`, `produces-evidence-for`, `reviewed-by`;
- `supersedes`, `superseded-by`, `contradicts`;
- `projects-to`, `routes`, `explains`.

Путь в Markdown помогает читателю; `document_links` строит устойчивый агентный граф.

## Видимая карточка

MkDocs должен выводить из metadata компактную карточку: system, domain, function, document status, version, canonicality, visibility, owner role и review date. При наличии `object_state` карточка отдельно показывает четыре статуса объекта. Цвет используется только вместе с текстом. Неизвестное или отсутствующее поле отображается честно и не генерируется моделью автоматически.

## Миграция старого корпуса

1. Определить предмет и владельца документа.
2. Проверить актуальность содержания и терминов.
3. Назначить stable ID, system, domain, function и audiences.
4. Определить статус, каноничность и видимость.
5. Добавить реальные связи.
6. Обновить заголовок, версию и дату.
7. Проверить сборку, карточку, поиск и входящие ссылки.

Массовое добавление формально корректного YAML без содержательного review запрещено: оно создаёт ложную уверенность в состоянии знания.
