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
  version: v2
  status: active
  date_ymd: 2026-10-23
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
      url: https://docs.detai-x.com/ru/ecosystem/Management_layer/Docs-Ecosystem/metadata_schema_registry/
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
| `log-summary` | переносимые и импортированные дневные сводки | legacy ClickUp task / Markdown export | [Legacy/import contract `log-summary`](#contract-log-summary) |

Новый тип добавляется через review этого реестра. Локальный prompt, skill, AGENTS.md или интеграция могут применять зарегистрированный contract, но не расширять его самостоятельно.

## Contract `ecosystem`

Полный целевой блок, правила governance, object state и связей определены в [политике metadata документов](document_metadata_policy.md). Базовый `classification.scope` — `DETai_ecosystem`; допустимые `context`, `system`, `domain`, `layer` и `function` выбираются по предмету документа.

## Новые WorkLogs Team OS

Новые операционные сводки сохраняются как WorkLog Team OS. Проект и semantic route `logs` разрешаются через актуальную навигацию Core; целевой List должен иметь `contentKind=work_log`. Рабочая дата задаётся `workDate` и timezone. Идентичность, авторство, версия, статус draft/final и ссылки обслуживаются Core. Название записи и вручную редактируемый YAML не являются ключом или вторым источником истины; переносимый экспорт формируется из typed данных.

WorkLog — самостоятельный тип рабочей записи. К нему не применяются назначение исполнителя и task completion. Неизвестный или недоступный Logs route не разрешает создавать похожий List, писать в Task/Note List или возвращаться к ClickUp.

Назначение объясняет [Team OS Plugin](../../DETai/Platform_DETai/E3-Infra/team-os/plugin.md), а действующую процедуру и формат определяет [log-summary skill owning-репозитория](https://github.com/DETai-org/team-os/blob/main/plugins/team-os/skills/log-summary/SKILL.md). Этот раздел не регистрирует новую YAML schema с именем `work_log`: runtime-тип и тип переносимого документа различаются.

## Contract `log-summary`

### Область применения: legacy/import

Следующий contract сохраняет идентичность и интерпретацию исторических записей ClickUp и их переносимых экспортов. Он не задаёт storage schema, workflow или маршрутизацию новых WorkLogs Team OS. Legacy ID, scope/context и provenance сохраняются при чтении и контролируемом импорте; они не являются реестром действующих Scope.

Ниже описан прежний формат. Его правила создания ClickUp task не применяются к новым операционным записям.

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
    person_id: github-user-<numeric-github-id>
    display_name: Антон
    github_username: Anton-Psy
    clickup_username: Anton-Psy
  recorded_by: Codex
links:
  related_logs: []
```

В прежнем формате metadata размещалась в начале ClickUp description как YAML-блок, пригодный для экспорта в Markdown без потери имён полей и значений. При чтении и экспорте сохраняется сам переносимый блок; визуальное форматирование не заменяет его поля.

### Идентичность и дата

- В одном Folder-local List `logs` существует не более одной task `Logs DD.MM.YYYY` на календарную дату.
- `descriptive.id` стабилен внутри List и включает List ID и дату в ISO-формате.
- `descriptive.status: draft` означает промежуточное дополнение в течение дня; `final` — закрытый итог дня.
- `descriptive.date_ymd` хранит дату записи в `YYYY-MM-DD`.

### Классификация и маршрутизация

`classification.scope` выбирается только из зарегистрированных областей. `classification.context` всегда содержит ровно одно значение и обозначает конкретный предметный контейнер, в чей List `logs` записан итог.

Исторический реестр областей и контекстов:

| `scope` | Допустимый смысл `context` | Примеры |
|---|---|---|
| `Tools` | конкретный командный инструмент | `codex`, `github`, `clickup` |
| `Infrastructure` | конкретный инфраструктурный контур | `home-psi-lab`, `proxmox`, `vpn-psi` |
| `Onboarding` | прохождение onboarding новым участником | `participant-onboarding` |
| `Governance` | конкретный управляющий или delivery-контур | `onboarding-management`, `management-layer` |
| `Projects` | стабильный идентификатор конкретного проекта | `storytelling`, `sites` |

При чтении legacy-записей сохраняются исходные `scope`, `context` и source IDs. Переименование текущего Scope или перенос Project не переписывают их историческое значение. Текущие маршруты определяются Core, а не этим реестром.

Исторический формат распределённых сводок предусматривал:

1. каждый результат записывается в дневной лог своего Folder-local List;
2. записи не смешивают несколько `context` в одном metadata-блоке;
3. связанные записи указывают друг на друга в `links.related_logs`;
4. отсутствие маршрута к соседнему List не разрешает подменять его локальным Markdown-файлом.

Историческая структура ClickUp сохраняет происхождение записей и не служит fallback для новых операций Team OS.

Space `Onboarding` и Folder `Management Layer / Onboarding` являются разными контейнерами: первый использует `scope: Onboarding` / `context: participant-onboarding`, второй — `scope: Governance` / `context: onboarding-management`. Их назначение и правило раздельных логов описывает draft-документ [«Контуры знаний и исполнения»](../../../onboarding/execution-contours.md#два-clickup-контура).

### Provenance

`provenance` обязателен только для `log-summary` и фиксирует человека, выполнившего работу, и агента, записавшего итог.

- `performed_by.person_id` — стабильная namespaced-строка `github-user-<numeric-github-id>`, основанная на numeric GitHub user ID;
- `display_name` — подтверждённое отображаемое имя;
- `github_username` — GitHub login;
- `clickup_username` — соответствующий ClickUp username;
- `recorded_by` — `Codex`, когда запись сформировал Codex.

GitHub username является основой машинного сопоставления, а ClickUp username — перекрёстной проверкой. Эти legacy-поля сохраняют подтверждённое исходное авторство и не используются для угадывания текущей identity Team OS. В видимой части лога username может показываться просто как `@username`.

Токены, email, cookies, пароли и другие секреты в metadata не сохраняются.

### Содержание

После metadata-блока следует компактный итог только своего контекста: обычно 1–3 пункта, ссылки на изменённые артефакты и незакрытый следующий шаг, если он есть. Техническая инвентаризация, конфигурация и поддерживаемая reference-информация остаются в своих owning artifacts и не копируются в дневной лог.
