---
type: ecosystem
classification:
  scope: Tools
  context: codex
  layer: null
  function: explanation
descriptive:
  id: tools-codex-interaction-with-codex
  version: v1
  status: active
  date_ymd: 2026-03-25
links:
  external_links:
    - type: "MkDocs_ru"
      url: "https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Tools/🧭Codex/interaction-with-codex/"
  document_links:
    - schema: ""
      link_type: ""
      linked_document_id: ""
title: 🤝 Взаимодействие с Codex
---

# 🤝 Взаимодействие с Codex

> [!NOTE] 📘 Введение  
> Этот документ фиксирует **принципы и структуру нашего взаимодействия с Codex-агентом**, включая стиль задач, этапность, сопровождение через GPT и то, как сохраняется история пулов.


Сейчас текущая взаимодействие хорошо описано в [Work Model](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/work-model/work-model/)



## ⚠️ Частые ошибки и способы их избежать


Codex строго следует путям и структурам. Вот типичные ошибки:

- ❌ Указан путь с капслоком или транслитерацией — файл не найден.
    
- ❌ В `requirements.txt` не хватает утилит (`xxd`, `mock`, `dotenv` и пр.) — Codex падает на setup.
    
- ❌ Отсутствует `AGENT.md` — Codex теряет "якорь".
    
- ❌ В задачах не указаны директории — Codex может действовать вне нужного контекста.


## 🧰 Утилиты и зависимости Codex

Файл описывает утилиты, библиотеки и системные зависимости, которые Codex будут полезны в среде выполнения (особенно при работе в CI, на сервере или в Docker-контейнере).
