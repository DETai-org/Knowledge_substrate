---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: knowledge-system
  layer: technical-standards
  function: register
  system: knowledge
  domain: document-metadata
  audiences: [team, editors, developers, agents]
descriptive:
  id: management-layer-docs-ecosystem-metadata-schema-registry
  version: v1
  status: active
  date_ymd: 2026-08-14
governance:
  canonicality: canonical
  visibility: public
  owner_role: knowledge-architect
  approver_role: ecosystem-architect
  review_date: 2026-09-14
object_state:
  architecture_status: canonical
  implementation_status: operational
  evidence_status: not-applicable
  visibility_status: public
links:
  external_links:
    - type: MkDocs_ru
      url: https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Management_layer/Docs-Ecosystem/metadata_schema_registry/
  document_links:
    - schema: ecosystem
      link_type: implements
      linked_document_id: management-layer-docs-ecosystem-document-metadata-policy
    - schema: ecosystem
      link_type: defines
      linked_document_id: management-layer-docs-ecosystem-functions-of-documents
title: Реестр metadata schemas
---

# Реестр metadata schemas

Реестр фиксирует contracts зарегистрированных `type`. Общие правила metadata, изменения схем и честного заполнения определяет [политика metadata документов](document_metadata_policy.md); этот документ не создаёт вторую policy.

## Зарегистрированные типы

| `type` | Назначение | Физический контейнер | Contract |
|---|---|---|---|
| `ecosystem` | канонические и объясняющие документы экосистемы | Markdown в Knowledge Substrate | [Contract `ecosystem`](#contract-ecosystem) |
| `log-summary` | короткий датированный итог выполненной работы | task в Folder-local ClickUp List `logs` | [Contract `log-summary`](#contract-log-summary) |

Новый тип добавляется через review этого реестра. Локальный prompt, skill, AGENTS.md или интеграция могут применять зарегистрированный contract, но не расширять его самостоятельно.

## Contract `ecosystem`

Полный целевой блок, правила governance, object state и связей определены в [политике metadata документов](document_metadata_policy.md). Базовый `classification.scope` — `DETai_ecosystem`; допустимые `context`, `system`, `domain`, `layer` и `function` выбираются по предмету документа.

## Contract `log-summary`

`log-summary` — переносимый тип дневного операционного документа. ClickUp сейчас является его контейнером, но не частью идентичности schema.

### Минимальный metadata-блок

```yaml
type: log-summary
classification:
  scope: Tools
  context: codex
  function: log-summary
descriptive:
  id: log-summary-<clickup-list-id>-<YYYY-MM-DD>
  status: draft
  date_ymd: YYYY-MM-DD
provenance:
  performed_by:
    person_id: 12345678
    display_name: Антон
    github_username: Anton-Psy
    clickup_username: Anton-Psy
  recorded_by: Codex
links:
  related_logs: []
```

Metadata размещается в начале ClickUp description как YAML-блок, пригодный для экспорта в Markdown без потери имён полей и значений. Содержимое description передаётся через Markdown-aware интерфейс ClickUp; визуальное форматирование не должно заменять сам переносимый блок.

### Идентичность и дата

- В одном Folder-local List `logs` существует не более одной task `Logs DD.MM.YYYY` на календарную дату.
- `descriptive.id` стабилен внутри List и включает List ID и дату в ISO-формате.
- `descriptive.status: draft` означает промежуточное дополнение в течение дня; `final` — закрытый итог дня.
- `descriptive.date_ymd` хранит дату записи в `YYYY-MM-DD`.

### Классификация и маршрутизация

`classification.scope` выбирается только из зарегистрированных областей. `classification.context` всегда содержит ровно одно значение и обозначает конкретный предметный контейнер, в чей List `logs` записан итог.

Начальный реестр областей и контекстов:

| `scope` | Допустимый смысл `context` | Примеры |
|---|---|---|
| `Tools` | конкретный командный инструмент | `codex`, `github`, `clickup` |
| `Infrastructure` | конкретный инфраструктурный контур | `home-psi-lab`, `proxmox`, `vpn-psi` |
| `Governance` | конкретный governance- или delivery-контур | `onboarding`, `management-layer` |
| `Projects` | стабильный идентификатор конкретного проекта | `storytelling`, `sites` |

Новое значение `scope` или новый класс `context` добавляется в этот реестр. Конкретный project-level `AGENTS.md` или route configuration должен фиксировать известные `list_id`, `scope` и `context`, чтобы skill не искал основной контейнер по всему ClickUp.

Если работа дала самостоятельный результат в соседнем проекте или инструменте:

1. каждый результат записывается в дневной лог своего Folder-local List;
2. записи не смешивают несколько `context` в одном metadata-блоке;
3. связанные записи указывают друг на друга в `links.related_logs`;
4. отсутствие маршрута к соседнему List не разрешает подменять его локальным Markdown-файлом.

Обзор всей структуры ClickUp может использоваться как fallback для cross-project маршрута, но не заменяет локально известный основной List.

### Provenance

`provenance` обязателен только для `log-summary` и фиксирует человека, выполнившего работу, и агента, записавшего итог.

- `performed_by.person_id` — numeric GitHub user ID;
- `display_name` — подтверждённое отображаемое имя;
- `github_username` — GitHub login;
- `clickup_username` — соответствующий ClickUp username;
- `recorded_by` — `Codex`, когда запись сформировал Codex.

GitHub username является основой машинного сопоставления, а ClickUp username — перекрёстной проверкой. Skill не угадывает identity по тексту разговора: он читает подтверждённый локальный профиль участника. В видимой части лога username может показываться просто как `@username`.

Токены, email, cookies, пароли и другие секреты в metadata не сохраняются.

### Содержание

После metadata-блока следует компактный итог только своего контекста: обычно 1–3 пункта, ссылки на изменённые артефакты и незакрытый следующий шаг, если он есть. Техническая инвентаризация, конфигурация и поддерживаемая reference-информация остаются в своих owning artifacts и не копируются в дневной лог.
