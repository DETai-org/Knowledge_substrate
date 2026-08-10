---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: knowledge-system
  layer: cross-cutting-system
  function: guide
  system: knowledge
  domain: system-overview
  audiences: [public, team, agents]
descriptive:
  id: knowledge-system-index
  version: v4
  status: active
  date_ymd: 2026-08-05
  date_update: 2026-08-10
governance:
  canonicality: canonical
  visibility: public
  owner_role: knowledge-architect
  approver_role: ecosystem-architect
  review_date: 2026-09-05
links:
  external_links: []
  document_links:
    - schema: ecosystem
      link_type: implements
      linked_document_id: cross-cutting-systems
    - schema: ecosystem
      link_type: contains
      linked_document_id: knowledge-publication-delivery
    - schema: ecosystem
      link_type: contains
      linked_document_id: detai-representation-model
    - schema: ecosystem
      link_type: contains
      linked_document_id: detai-object-status-model
title: Система знаний и Knowledge Substrate
---

# Система знаний и Knowledge Substrate

Система знаний — читательский контейнер для архитектуры, публикации и агентной доступности знания. Её каноническое ядро, **Knowledge Substrate**, делает устройство DETai понятным людям и доступным агентам как связный граф. Он хранит объяснения, статусы, policies, standards и отношения между системами, но не является runtime-базой всех данных экосистемы.

## Архитектура, публикация и эксплуатация

Знание должно не только храниться, но и доходить до целевого читателя. При этом важно не смешивать разные функции:

- **архитектура знания** определяет документы, metadata, связи и источники истины;
- **[публикация и доставка знаний](knowledge-delivery.md)** превращает канонический документ в доступную версию, навигацию и поисковый ответ;
- **[модель представлений](representation-model.md)** определяет разные функции сайта, документации, книги, runtime и закрытых хранилищ;
- **[модель статусов](object-status-model.md)** не позволяет смешивать зрелость документа, архитектуры, реализации и evidence.

`Infrastructure` и `Tools` имеют самостоятельные верхнеуровневые маршруты как сквозные обеспечивающие области экосистемы. При этом ответственность за конкретный инфраструктурный компонент или инструмент остаётся у его owning domain, а Corporate Vault — у Legal–Economic. Система знаний взаимодействует с ними, но не становится их общим владельцем.

## Слои знания

- **Canonical** — определения, границы, policies и утверждённые решения.
- **Operational** — задачи, incidents, reviews и текущая координация.
- **Restricted** — персональные, договорные, security и иные закрытые записи.
- **Public representation** — сайт, книга, публикации и безопасные страницы документации.

Один слой может ссылаться на другой, но не должен молча подменять его.

## Состав раздела

- [Модель документа и видимая функция](document-model.md)
- [Модель представлений сайта, документации и книги](representation-model.md)
- [Многомерная модель статуса объекта](object-status-model.md)
- [Навигация для людей и агентов](agent-navigation.md)
- [Миграция информационной архитектуры](navigation-migration.md)
- [Публикация и доставка знаний](knowledge-delivery.md)
- [Действующая политика metadata](../ecosystem/Management_layer/Docs-Ecosystem/document_metadata_policy.md)
- [Функции документов](../ecosystem/Management_layer/Docs-Ecosystem/functions_of_documents.md)
- [Документация как исполняемый интерфейс](../ecosystem/Management_layer/2_Architecture_and_Logic/docs-as-executable-interface-for-agents.md)

## Связь с репозиториями

Knowledge Substrate является каноническим публично-командным корпусом архитектуры экосистемы. Репозитории продуктов удерживают локальную реализацию; `ecosystem-runtime` — runtime state и данные в своих границах; authoring — исследовательское и повествовательное развитие книги; сайт — публичную витрину. [Рабочая среда](../start/working-environment.md) связывает эти места для участника, не меняя их принадлежность.
