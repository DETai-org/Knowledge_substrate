---
type: ecosystem
classification:
  scope: Infrastructure
  context: servers
  layer: null
  function: index
descriptive:
  id: infrastructure-index
  version: v4
  status: active
  date_ymd: 2026-03-25
  date_update: 2026-08-20
links:
  external_links:
    - type: "MkDocs_ru"
      url: "https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Infrastructure/"
  document_links:
    - schema: ""
      link_type: ""
      linked_document_id: ""
title: Infrastructure
---

# Infrastructure

Infrastructure — это специализированная оптика, через которую экосистема
рассматривает техническую основу своей работы: исполняемый код, данные,
вычислительные среды, связи между ними и границы ответственности. Она не
подменяет продуктовую карту DETai и не превращает всё увиденное в один проект.

## Два вида объектов

Внутри этой оптики важно различать **инфраструктурные системы** и контейнер
**«Серверы и Home Ψ Lab»**.

```mermaid
flowchart TB
    infra["Infrastructure — специализированная оптика"]
    systems["Инфраструктурные системы"]
    environments["Серверы и Home Ψ Lab"]
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

Это три самостоятельные системы с собственными GitHub-репозиториями, историей
версий и границами владения:

- [ecosystem-runtime](ecosystem-runtime/index.md) обеспечивает общие живые
  процессы экосистемы: API, ботов, workers и runtime-данные;
- [intelligence-runtime](intelligence-runtime/index.md) обеспечивает
  повторно используемое исполнение LLM-сценариев;
- [Knowledge Substrate](Knowledge_Substrate/index.md) хранит и материализует
  каноническое знание экосистемы.

Слово «система» здесь намеренно. Это не продуктовые проекты платформы DETai,
хотя каждый репозиторий развивается как самостоятельный versioned-контур.

### Серверы и Home Ψ Lab

[Серверы](🌍%20Сервера/index.md) — арендованные внешние вычислительные узлы.
Они могут находиться у разных поставщиков и в разных регионах, а размещённые на
них системы могут меняться со временем.

[Home Ψ Lab](home-lab/index.md) — собственная физическая лаборатория DETai. В
ней отдельно развиваются сетевой контур Psi Gateway и вычислительная среда
DETai Nexus.

Вычислительная машина не становится владельцем размещённого в ней кода. Репозиторий
определяет систему и её версии, а Infrastructure описывает, где и как выбранная
версия запущена. Общий обзор этих двух контуров находится на странице
[«Серверы и Home Ψ Lab»](servers-and-home-lab/index.md).

## Где проходит граница

Эта база знаний объясняет устойчивую структуру и связи понятным языком.
Конкретные адреса, регионы, провайдеры, пути, сервисы, конфигурации и текущее
размещение репозиториев относятся к операционным источникам Infrastructure.
