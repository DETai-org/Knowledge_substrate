---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: infrastructure
  layer: infrastructure
  function: index
  domain: infrastructure-foundation
descriptive:
  id: detai-platform-technology-foundation
  version: v3
  status: active
  date_ymd: 2026-11-01
  date_update: 2026-11-01
governance:
  canonicality: canonical
  visibility: public
links:
  external_links:
    - type: MkDocs_ru
      url: https://docs.detai-x.com/ru/technology/platform/infrastructure-foundation/
  document_links:
    - schema: ecosystem
      link_type: part-of
      linked_document_id: infrastructure-index
    - schema: ecosystem
      link_type: related-to
      linked_document_id: detai-platform-detai-index
title: Infrastructure Foundation
---

# Infrastructure Foundation

**Infrastructure Foundation — инфраструктурная основа всей экосистемы DETai:** общие API, исполнение LLM-сценариев и система канонических знаний. Эти возможности предоставляет [Infrastructure](../../../infrastructure/index.md); здесь показано, как их используют проекты Platform DETai.

Она состоит из трёх самостоятельных инфраструктурных систем:

- [ecosystem-runtime](../../../infrastructure/ecosystem-runtime/index.md) предоставляет общий backend DETai: API, Telegram-ботов, фоновые процессы и runtime-данные;
- [intelligence-runtime](../../../infrastructure/intelligence-runtime/index.md) выполняет многошаговые LLM-сценарии по правилам подключённого проекта и возвращает проверяемый результат;
- [Knowledge Substrate](../../../infrastructure/knowledge-substrate/index.md) хранит канонические документы, описывающие экосистему, и собирает из них этот сайт MK Docs и машинные представления.

Организационно каждый контур развивается как самостоятельный внутренний проект с собственным репозиторием, версиями и циклом развития. По своей обеспечивающей роли это проекты [E3](../../logic-of-echelons.md).

Архитектурно результат такого проекта — **инфраструктурная система**, которая предоставляет повторно используемые возможности нескольким потребителям. Эти системы составляют отдельный инфраструктурный пласт и относятся к **Infrastructure**. Пункт в меню Platform DETai показывает зависимость платформенных проектов от этого пласта; общая инфраструктура обслуживает всю экосистему.

Полная граница между системами описана в каноническом разделе [«Инфраструктурные системы»](../../../infrastructure/infrastructure-systems/index.md). Здесь она не пересказывается: эта страница показывает только то, почему Platform DETai от них зависит.

## Как это выглядит в конкретном проекте

На примере [Storytelling](../storytelling/infrastructure-and-delivery.md) можно увидеть, как предметная производственная система сохраняет собственные правила публикации, а intelligence-runtime берёт на себя только техническое исполнение LLM-шагов.

[Psychology in Quotes](../psychology-in-quotes/architecture-and-trust.md) использует ecosystem-runtime для общей идентичности DETai Account и коммерческого учёта в Commerce Core: предложений, платежей и подписок. Возможности продукта, недельные лимиты, работа с цитатами и пользовательские сценарии остаются ответственностью PiQ.
