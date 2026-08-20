---
type: ecosystem
classification:
  scope: Infrastructure
  context: Knowledge_Substrate
  layer: null
  function: index
descriptive:
  id: infrastructure-knowledge-substrate-index
  version: v2
  status: active
  date_ymd: 2026-08-20
links:
  external_links:
    - type: "MkDocs_ru"
      url: "https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Infrastructure/Knowledge_Substrate/"
  document_links:
    - schema: ""
      link_type: ""
      linked_document_id: ""
title: Knowledge Substrate
---

# Knowledge Substrate

**Knowledge Substrate** — инфраструктурная система канонического знания DETai.
Её [самостоятельный репозиторий](https://github.com/DETai-org/Knowledge_substrate)
хранит исходные документы, metadata и процессы, которые превращают знание в
доступные человеку и машине представления.

Сайт, который вы сейчас читаете, — одно из таких представлений. Он не исчерпывает
систему: тот же источник может подготавливаться для поиска, retrieval,
индексации и работы через `detai_core`.

## Что принадлежит системе

- канонические и объясняющие документы экосистемы;
- структура, metadata и связи между документами;
- ingest и materialization knowledge-данных;
- retrieval-ready представления и knowledge/query-контур `detai_core`.

Knowledge Substrate не владеет живыми заявками, событиями и уведомлениями — это
область [ecosystem-runtime](../ecosystem-runtime/index.md). Она также не
выбирает модели и не исполняет LLM-сценарии — это область
[intelligence-runtime](../intelligence-runtime/index.md).

Infrastructure может размещать knowledge-компоненты на разных вычислительных
узлах, включая [Home Ψ Lab](../home-lab/index.md), но место развёртывания не
меняет владельца знания и его версию.

