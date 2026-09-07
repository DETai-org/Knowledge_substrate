---
type: ecosystem
classification:
  scope: Infrastructure
  context: infrastructure-systems
  layer: architecture-and-logic
  function: index
descriptive:
  id: infrastructure-systems
  version: v3
  status: active
  date_ymd: 2026-08-20
  date_update: 2026-09-07
governance:
  canonicality: canonical
  visibility: public
title: Инфраструктурные системы
---

# Инфраструктурные системы

Инфраструктурная система — общая повторно используемая техническая возможность,
которую применяют несколько продуктов или производственных систем. Она не
принадлежит одному предметному процессу и не является пользовательским
продуктом Platform DETai.

Здесь нет выбора между понятиями «проект» и «система»: они описывают объект с
разных сторон. Организационно каждый такой контур развивается как проект — со
своим GitHub-репозиторием, целью, границей ответственности, версиями и циклом
развития. Архитектурно результат этого проекта является инфраструктурной
системой. Такой проект преимущественно усиливает
[технологический ресурс](../../Management_layer/ecosystem-resource.md) и может
косвенно экономить финансовый ресурс за счёт автоматизации и снижения затрат.

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

## Repository не равен Infrastructure System

Наличие собственного Git repository не является достаточным признаком новой
инфраструктурной системы. Связь работает только в одну сторону: самостоятельная
Infrastructure System обычно имеет versioned project/repository, но любой
repository от этого автоматически системой не становится.

Поэтому `DETai-org/Infrastructure` **не является четвёртой Infrastructure
System**. Это version-controlled operational source of truth инфраструктурного
домена и его сред исполнения: место для reviewable operational inventory,
эксплуатационных артефактов, scripts и подходящих для Git частей deployment /
configuration state.

Его текущая внутренняя структура может меняться и не образует новую онтологию
экосистемы. Сам repository не становится runtime/API-системой и не получает
ownership логики только потому, что описывает или разворачивает конкретную
машину.

Это различие подробно связано с provider–consumer моделью в
[«Принципах инфраструктуры»](../Infrastructure_Principles.md#operational-source-of-truth-detai-orginfrastructure).
