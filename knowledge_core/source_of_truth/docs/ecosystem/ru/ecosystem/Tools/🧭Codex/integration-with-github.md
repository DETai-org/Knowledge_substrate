---
type: ecosystem
classification:
  scope: Tools
  context: codex-gpt
  layer: null
  function: explanation
descriptive:
  id: tools-codex-integration-with-github
  version: v1
  status: active
  date_ymd: 2026-08-14
links:
  external_links:
    - type: "MkDocs_ru"
      url: "https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Tools/🧭Codex/integration-with-github/"
  document_links:
    - schema: ecosystem
      link_type: related-to
      linked_document_id: tools-codex-index
title: Связь Codex с GitHub
---

# Связь Codex с GitHub

GitHub хранит репозитории, Issues, Pull Requests и историю изменений. Codex помогает читать этот контекст, выполнять работу в локальной копии проекта и готовить изменения к командному ревью.

## 🧩 Основные способы работы

### Локальный репозиторий

Codex открывает проект на компьютере, читает файлы и `AGENTS.md`, создаёт правки, запускает проверки и показывает diff. Git остаётся системой версионности: ветка, commit и push выполняются как отдельные понятные действия.

### Issues и Pull Requests

Issue может служить входным контрактом задачи, а Pull Request — местом проверки и обсуждения результата. При наличии подключённого GitHub-инструмента Codex может читать доступный контекст этих сущностей и выполнять разрешённые операции.

### Параллельная работа

Несколько задач можно вести в отдельных ветках или worktree, чтобы изменения не смешивались. Итог каждой ветки всё равно проходит проверку и ревью перед объединением.

### Автоматизация и интеграции

Для повторяемых операций используются GitHub Actions, подключённые инструменты, плагины и Skills. Они расширяют возможности Codex, но не отменяют права доступа, правила репозитория и необходимость проверять внешние действия.

## 🔁 Типовой поток

```text
Issue или цель
→ локальная ветка
→ изменение файлов
→ тесты и проверка
→ commit и push
→ Pull Request
→ ревью и merge
```

## 📍 Важно понимать

Codex и GitHub не заменяют друг друга. Codex помогает понять и выполнить работу, а GitHub хранит совместную историю, обсуждение и проверяемый путь изменения проекта.

Актуальные способы подключения зависят от интерфейса и прав аккаунта; сверяйте их с [официальной документацией OpenAI](https://learn.chatgpt.com/docs) и правилами конкретной организации GitHub.
