---
type: ecosystem
classification:
  scope: DETai_cluster
  context: platform
  layer: null
  function: index
descriptive:
  id: detai-platform-detai-e3-infra-gpt-promt-engine-index
  version: v1
  status: active
  date_ymd: 2026-03-25
links:
  external_links:
    - type: "MkDocs_ru"
      url: "https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/Platform_DETai/E3-Infra/gpt_promt_engine/"
  document_links:
    - schema: ""
      link_type: ""
      linked_document_id: ""
title: gpt_promt_engine
---

# gpt_promt_engine


`gpt_promt_engine/` — это автономный модуль для генерации и сборки промтов, реализованный как независимый и масштабируемый процессор.

Директория отвечает за формирование финального запроса к языковой модели на основе нескольких уровней входных данных: глобальных настроек, кастомных параметров, user- и channel-промтов. В процессе сборки поддерживаются стилизация, переопределения (overrides), корректировки и скриптовые замены.

Архитектура модуля спроектирована таким образом, чтобы быть отделённой от конкретных проектов (например, Telegram-ботов или Chain-систем) и позволять подключение внешних систем через единую точку входа `boss_manager_prompt.py`.

Проект ориентирован на модульность, расширяемость и повторное использование в различных сценариях автоматизированной генерации промтов.


Находится в репозитории https://github.com/DETai-org/projects
