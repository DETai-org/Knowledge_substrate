---
type: ecosystem
classification:
  scope: Infrastructure
  context: infrastructure
  layer: infrastructure
  function: index
descriptive:
  id: infrastructure-index
  version: v7
  status: active
  date_ymd: 2026-11-01
  date_update: 2026-11-01
links:
  external_links:
    - type: "MkDocs_ru"
      url: "https://docs.detai-x.com/ru/infrastructure/"
  document_links:
    - schema: ecosystem
      link_type: related-to
      linked_document_id: detai-platform-detai-index
title: Infrastructure
---

# Infrastructure

**Infrastructure — самостоятельный инфраструктурный пласт экосистемы DETai,
предоставляющий общие обеспечивающие системы и среды исполнения.** Он объединяет
исполняемый код, данные, вычислительные среды, связи между ними и границы
ответственности. Его возможности служат основой работы разных направлений экосистемы.

## Основные направления

Внутри этого контура есть два больших направления: **инфраструктурные системы**
и **среды исполнения**. Эта группировка пока не охватывает все проекты:
место Архивариуса в ней ещё предстоит определить.

```mermaid
flowchart TB
    infra["Infrastructure — инфраструктурный пласт"]
    systems["Инфраструктурные системы"]
    environments["Среды исполнения"]
    ecosystem["ecosystem-runtime"]
    intelligence["intelligence-runtime"]
    knowledge["Knowledge Substrate"]
    servers["Арендованные серверные узлы"]
    home["Home Ψ Lab"]

    infra --> systems
    infra --> environments
    systems --> ecosystem
    systems --> intelligence
    systems --> knowledge
    environments --> servers
    environments --> home
```

### Инфраструктурные системы

Это самостоятельные versioned-контуры, которые владеют технической логикой и
данными. В текущей архитектуре таких систем три:

- [ecosystem-runtime](ecosystem-runtime/index.md) содержит общий backend DETai:
  API, Telegram-ботов, фоновые workers и схемы runtime-данных для пользователей,
  доступа, событий, заявок и уведомлений;
- [intelligence-runtime](intelligence-runtime/index.md) подключает правила
  продуктов к LLM: проводит запрос через нужные шаги, проверяет и исправляет
  технические ошибки ответа, записывает ход выполнения и возвращает результат;
- [Knowledge Substrate](knowledge-substrate/index.md) хранит канонические
  документы, которые описывают экосистему DETai — включая страницу, которую вы
  сейчас читаете, — и собирает из них этот сайт базы знаний на MkDocs, а также
  структурированные записи и индексы для машинной обработки.

Их общая граница раскрыта в разделе
[«Инфраструктурные системы»](infrastructure-systems/index.md).

### Среды исполнения

Это вычислительные машины и операционные контуры, где запускается код. DETai
использует арендованные внешние серверы и собственную Home Ψ Lab. Их различие
и общая эксплуатационная граница раскрыты в разделе
[«Среды исполнения»](execution-environments/index.md).

## Архивариус: категория пока открыта

[Архивариус](arhivarius/index.md) — проект исторической памяти экосистемы,
относящийся к [эшелону E3](../technology/logic-of-echelons.md). Он сохраняет
наблюдаемые события и архивные данные; сейчас тесно связан с Telegram,
включая статистику публичных каналов. Его точная архитектурная категория
пока не определена, поэтому он представлен отдельным пунктом Infrastructure.

## Инфраструктурные системы как проекты E3

ecosystem-runtime, intelligence-runtime и Knowledge Substrate организационно
развиваются как самостоятельные внутренние проекты: у них есть репозитории,
версии и производственные циклы. Их обеспечивающую роль описывает
[эшелон E3](../technology/logic-of-echelons.md).

Результат такого проекта — общая инфраструктурная система, предоставляющая
возможности другим проектам и направлениям. Проектная форма описывает способ
её развития, а инфраструктурная принадлежность — место в архитектуре и ответственность.
Эти системы относятся к Infrastructure и обеспечивают работу всей экосистемы.

В [Platform DETai](../technology/platform/index.md) видно, как инфраструктурные
возможности используются цифровыми проектами. Страница
[Infrastructure Foundation](../technology/platform/infrastructure-foundation/index.md)
связывает платформенный портфель с каноническими описаниями обеспечивающих систем.
Предметные правила и назначение каждого проекта сохраняются у его команды,
а инфраструктура предоставляет общие возможности через согласованные интерфейсы.

## Capabilities как связи между владельцами

Разделение инфраструктурных систем и сред исполнения само по себе не
описывает зависимости между ними. Для этого
используется понятие **Infrastructure Capability**: стабильная техническая
возможность, которую provider предоставляет consumer через контракт.

Capability не является третьим типом машины или новой организационной
иерархией. Это способ описать зависимость так, чтобы consumer зависел от смысла
и интерфейса возможности, а не от конкретного host, proxy stack или другой
сменяемой реализации.

Например, Psi Gateway может предоставлять reusable Network capability, которую
используют Telegram-facing runtime и другие компоненты. То, что consumer сегодня
размещён на DETai Nexus, не делает Nexus обязательным логическим посредником и
не передаёт ему ownership consumer-логики.

Подробно provider–consumer pattern, logical Network Profile, разделение policy
и роль operational repository описаны в
[«Принципах инфраструктуры»](principles.md#5-принцип-infrastructure-capabilities-и-стабильных-контрактов).

## Канон и operational source of truth

Эта база знаний хранит устойчивую концептуальную модель Infrastructure.
Отдельный `DETai-org/Infrastructure` repository является version-controlled
**operational source of truth** инфраструктурного домена: в нём могут храниться
reviewable operational-карты, инвентаризация, scripts, эксплуатационная
документация и подходящие для Git deployment/configuration assets.

Сам факт существования этого repository не создаёт четвёртую Infrastructure
System. Repository и Linux machine — разные объекты, так же как repository и
runtime system — не синонимы.

## Где проходит граница

Эта база знаний объясняет устойчивую структуру и связи понятным языком.
Конкретные адреса, регионы, провайдеры, пути, сервисы, конфигурации и текущее
размещение репозиториев относятся к операционным источникам Infrastructure.
Текущая внутренняя структура `DETai-org/Infrastructure` также является
изменяемой implementation detail и не канонизируется как вечное дерево.
