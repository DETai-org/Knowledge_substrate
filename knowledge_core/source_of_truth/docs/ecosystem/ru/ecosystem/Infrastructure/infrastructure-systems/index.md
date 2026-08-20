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
| [ecosystem-runtime](../ecosystem-runtime/index.md) | Общий backend DETai: API, Telegram-боты, workers и runtime-данные пользователей, доступа, событий, заявок и уведомлений |
| [intelligence-runtime](../intelligence-runtime/index.md) | Связывает правила продуктов с LLM, выполняет многошаговые сценарии, проверяет ответы и возвращает результат продукту |
| [Knowledge Substrate](../Knowledge_Substrate/index.md) | Хранит документы, описывающие экосистему DETai, и собирает из них этот сайт базы знаний на MkDocs, структурированные записи и индексы для машинной обработки |

Их репозитории могут взаимодействовать и развёртываться рядом, но не
поглощают друг друга. Каждая система остаётся владельцем своей логики и данных.
Страницы ниже раскрывают эти границы по отдельности, не привязывая их к
конкретной машине.
