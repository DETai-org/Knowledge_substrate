---
type: ecosystem
classification:
  scope: Infrastructure
  context: infrastructure-systems
  layer: architecture-and-logic
  function: index
descriptive:
  id: infrastructure-systems
  version: v1
  status: active
  date_ymd: 2026-08-20
governance:
  canonicality: canonical
  visibility: public
title: Инфраструктурные системы
---

# Инфраструктурные системы

Инфраструктурная система — это самостоятельный технический контур со своим
GitHub-репозиторием, границей ответственности и историей версий. Такой контур
развивается как отдельная система, но не является продуктовым проектом на
платформе DETai.

## Три системы

| Система | За что отвечает |
| --- | --- |
| [ecosystem-runtime](../ecosystem-runtime/index.md) | Общие живые процессы: API, боты, workers и runtime-данные |
| [intelligence-runtime](../intelligence-runtime/index.md) | Повторно используемое исполнение LLM-сценариев |
| [Knowledge Substrate](../Knowledge_Substrate/index.md) | Каноническое знание и его машинные представления |

Их репозитории могут взаимодействовать и развёртываться рядом, но не
поглощают друг друга. Каждая система остаётся владельцем своей логики и данных.
Страницы ниже раскрывают эти границы по отдельности, не привязывая их к
конкретной машине.
