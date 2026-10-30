---
type: ecosystem
classification:
  scope: DETai_cluster
  context: uli
  layer: null
  function: index
descriptive:
  id: detai-u-l-i-3-technical-standards-telegram-bots-index
  version: v1
  status: active
  date_ymd: 2026-03-25
links:
  external_links:
    - type: "MkDocs_ru"
      url: "https://docs.detai-x.com/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/Telegram_Bots/"
  document_links:
    - schema: ""
      link_type: ""
      linked_document_id: ""
title: Telegram Bots Documentation
---

# Telegram Bots Documentation

Этот раздел содержит документы, описывающие стандарты и подходы для создания Telegram-ботов в рамках экосистемы DETai. 

Эти документы важны для обеспечения согласованности, безопасности и удобства в разработке Telegram-ботов в экосистеме DETai.

## Архитектура и конфигурация

- [Декларативная конфигурация и секреты](configuration-standard.md) — где лежат JSON/TOML, профили, списки допуска и приватный ENV; проверка реального применения.
- [Стандарт создания Telegram-ботов](telegram-bot-creation-standard.md) — модульность и разделение ответственности независимо от языка.

## Межботовые контракты

- [Стандарт передачи языка и цели перехода](language-handover.md) — общая норма приоритета языка, безопасный формат Telegram `start` и границы Identity.
