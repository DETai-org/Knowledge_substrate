---
type: ecosystem
classification:
  scope: Tools
  context: codex
  layer: null
  function: explanation
descriptive:
  id: tools-codex-create-epic-issue-release
  version: v1
  status: active
  date_ymd: 2026-03-25
links:
  external_links:
    - type: "MkDocs_ru"
      url: "https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Tools/🧭Codex/create-epic-issue-release/"
  document_links:
    - schema: ""
      link_type: ""
      linked_document_id: ""
title: Create Epic Issue Release
---

Промпт для создания архивного `Epic_issue-vX.Y.md` файла фиксации версии.  
Опирается на `release-fixation-standard.md`, анализирует закрытые Sub-Issue и текущее состояние репозитория, синтезирует итог перехода состояния без превращения его в аудит кода.

Связан с: [Release Fixation Standard](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/release-fixation-standard/)

---

# Create Epic Issue Release

```text
Create Epic Issue Release

Проанализируй текущий репозиторий и закрытые Sub-Issue (если они есть).

Опираясь на стандарт `release-fixation-standard.md`,
создай архивный файл фиксации версии в папке `issue/`
в формате `Epic_issue-vX.Y.md`.

Требования:

1. Строго следуй структуре, принятой для Epic_issue файлов.
2. Используй два источника:
   - закрытые Sub-Issue,
   - фактическое состояние репозитория.
1. Не превращай файл в аудит кода.
   
2. Зафиксируй:
   - достигнутое состояние,
   - In scope / Out of scope,
   - Definition of Done,
   - почему это не следующая стадия зрелости (если применимо),
   - мостик к следующему Epic.
6. Объём — 1–2 страницы.

```

---
