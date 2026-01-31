# Автоматизации репозитория Knowledge_substrate

Здесь собраны workflow, которые обеспечивают автоматизацию в репозитории Knowledge_substrate и межрепозиторные синхронизации. Файл служит краткой навигацией по задачам сборки, деплоя и обмена данными между репозиториями.

## 🚀 Deploy Docs (`.github/workflows/docs.yml`)
- 🏗️ Собирает документацию на MkDocs при изменениях в документационных путях.
- 🌐 Публикует результат в GitHub Pages, чтобы в MkDocs отображались данные из файлов в [`knowledge_core/source_of_truth/docs/`](../../knowledge_core/source_of_truth/docs/).

## 🔁 Sync Blog Posts to Site (`.github/workflows/sync-blog-posts.yml`)
- 📦 Копирует посты из Knowledge_substrate в репозиторий `DETai-org/sites`.
- 🔄 Поддерживает синхронизацию блогов при обновлениях в целевых каталогах.

## 🧭 Create Linear issue on merge to main (`.github/workflows/linear-create-issue-on-merge.yml`)
- 🧩 Создаёт задачу в Linear после успешного запуска связанного workflow или вручную.
- 📌 Передаёт в Linear `LINEAR_TEAM_ID`, `LINEAR_PROJECT_ID`, `LINEAR_LABEL_ID_POST_TO_BLOG`, `LINEAR_ASSIGNEE_ID`, а также контекст `repo`, `sha`, `actor` для описания задачи.

📌 Описание создания API для Linear хранится в ClickUp: [ссылка](https://example.com)

| Workflow | Затрагиваемый репозиторий | Запуск |
| --- | --- | --- |
| Deploy Docs | Knowledge_substrate | push/pr в main по путям docs |
| Sync Blog Posts to Site | Knowledge_substrate → DETai-org/sites | push в main по путям blog posts |
| Create Linear issue on merge to main | Knowledge_substrate | workflow_dispatch; workflow_run после Sync Blog Posts |
