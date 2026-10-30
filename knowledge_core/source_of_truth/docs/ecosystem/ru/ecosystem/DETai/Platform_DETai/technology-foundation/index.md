---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: platform
  layer: technology
  function: index
  domain: technology-foundation
descriptive:
  id: detai-platform-technology-foundation
  version: v2
  status: active
  date_ymd: 2026-08-20
  date_update: 2026-10-30
governance:
  canonicality: canonical
  visibility: public
title: Технологическая основа
---

# Технологическая основа

Продукты и производственные системы Platform DETai не должны заново создавать общие API, техническое исполнение LLM-сценариев и систему канонических знаний. Эти возможности предоставляет технологическая основа экосистемы.

Она состоит из трёх самостоятельных инфраструктурных систем:

- [ecosystem-runtime](../../../Infrastructure/ecosystem-runtime/index.md) предоставляет общий backend DETai: API, Telegram-ботов, фоновые процессы и runtime-данные;
- [intelligence-runtime](../../../Infrastructure/intelligence-runtime/index.md) выполняет многошаговые LLM-сценарии по правилам подключённого проекта и возвращает проверяемый результат;
- [Knowledge Substrate](../../../Infrastructure/Knowledge_Substrate/index.md) хранит канонические документы, описывающие экосистему, и собирает из них этот сайт MK Docs и машинные представления.

Это не три продукта внутри Platform DETai. Организационно каждый контур развивается как проект с собственным репозиторием, версиями и циклом развития. Архитектурно результат такого проекта является **инфраструктурной системой** — общей повторно используемой технической возможностью, которая обслуживает несколько продуктов или производственных систем и не принадлежит одному предметному процессу.

Полная граница между системами описана в каноническом разделе [«Инфраструктурные системы»](../../../Infrastructure/infrastructure-systems/index.md). Здесь она не пересказывается: эта страница показывает только то, почему Platform DETai от них зависит.

## Как это выглядит в конкретном проекте

На примере [Storytelling](../../../STORYTELLING/technology-foundation.md) можно увидеть, как предметная производственная система сохраняет собственные правила публикации, а intelligence-runtime берёт на себя только техническое исполнение LLM-шагов.

[Psychology in Quotes](../products/psychology-in-quotes/architecture-and-trust.md) использует ecosystem-runtime для общей идентичности DETai Account и коммерческого учёта в Commerce Core: предложений, платежей и подписок. Возможности продукта, недельные лимиты, работа с цитатами и пользовательские сценарии остаются ответственностью PiQ.
