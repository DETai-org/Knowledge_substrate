---
type: ecosystem
classification:
  scope: Infrastructure
  context: execution-environments
  layer: architecture-and-logic
  function: index
descriptive:
  id: infrastructure-execution-environments
  version: v2
  status: active
  date_ymd: 2026-08-20
  date_update: 2026-09-07
governance:
  canonicality: canonical
  visibility: public
title: Среды исполнения
---

# Среды исполнения

Среда исполнения — это вычислительная основа, на которой запускаются компоненты
инфраструктурных систем и продуктов. Проще говоря, это машины, их операционные
системы, ресурсы и связанные с ними эксплуатационные службы.

В DETai используются два вида таких сред:

- [**Серверы**](../🌍%20Сервера/index.md) — арендованные внешние
  вычислительные узлы у разных поставщиков и в разных регионах;
- [**Home Ψ Lab**](../home-lab/index.md) — собственное оборудование и
  управляемые DETai виртуальные среды.

Среда отвечает на вопрос «где и на каких ресурсах это работает», но не «кому
принадлежит логика». Один компонент можно перенести между машинами, а на одной
машине могут одновременно работать компоненты нескольких репозиториев.

## Hosting не создаёт новую dependency boundary

Если consumer или provider физически размещён внутри конкретной среды, сама
среда не становится обязательным логическим посредником между ними.

Например, Telegram-facing компонент может сегодня работать на DETai Nexus и
использовать Network capability Psi Gateway. Архитектурно зависимость должна
оставаться зависимостью от capability contract, а не от факта размещения на
Nexus:

```text
component @ DETai Nexus
→ Network capability
→ Psi Gateway
```

а не:

```text
component
→ Nexus as owner/middleware
→ Gateway
```

Если компонент переезжает на другую execution environment, его доменная логика
и contract доступа к capability не должны переписываться только из-за смены
машины.

Подробно этот принцип раскрыт в
[«Принципах инфраструктуры»](../Infrastructure_Principles.md#5-принцип-infrastructure-capabilities-и-стабильных-контрактов).

Конкретные локации, адреса, сервисы и текущая раскладка deployment меняются и
поэтому остаются в операционной карте Infrastructure.
