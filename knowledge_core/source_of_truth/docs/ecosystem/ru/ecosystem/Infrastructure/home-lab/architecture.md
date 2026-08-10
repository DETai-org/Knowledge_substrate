---
type: ecosystem
classification:
  scope: Infrastructure
  context: servers
  layer: architecture-and-logic
  function: explanation
descriptive:
  id: infrastructure-home-lab-architecture
  version: v1
  status: planned
  date_ymd: 2026-08-10
governance:
  canonicality: working
  visibility: public
links:
  external_links:
    - type: "MkDocs_ru"
      url: "https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Infrastructure/home-lab/architecture/"
  document_links:
    - schema: ecosystem
      link_type: belongs-to
      linked_document_id: infrastructure-home-lab
title: Архитектура и состав Home Ψ Lab
---

# Архитектура и состав Home Ψ Lab

Эта страница подготовлена для публичного описания архитектуры Home Ψ Lab по мере установки и проверки её компонентов.

## Функциональные контуры

| Контур | Назначение | Граница публичного описания |
|---|---|---|
| **Psi Gateway** | VPN, защищённый сетевой доступ и связь лаборатории с внешними инфраструктурными контурами | Назначение, принципы доступа и устойчивые связи без раскрытия сетевых реквизитов |
| **DETai Nexus** | Локальные AI-модели, знания, индексы, базы данных и подготовка агентного контекста | Логическая архитектура работы агентов со знаниями без секретов и эксплуатационной конкретики |

Названия фиксируют функции, а не конкретные виртуальные машины. Фактическая техническая компоновка появится здесь после установки и проверки.

Здесь будут фиксироваться устойчивые и несекретные сведения:

- функциональные части узла и их назначение;
- связи Home Ψ Lab с внешними инфраструктурными контурами DETai;
- архитектура доступа агентов к знаниям и контекстам;
- версии и подтверждённое состояние публичной архитектуры.

Hostnames, IP-адреса, учётные данные, точная сетевая топология, эксплуатационные команды, текущие задачи и журналы работ в публичный документ не переносятся. Эта операционная конкретика хранится во внутренних системах ClickUp и `server-operations` согласно [документационной архитектуре DETai](../../Management_layer/Docs-Ecosystem/documentation-architecture.md).
