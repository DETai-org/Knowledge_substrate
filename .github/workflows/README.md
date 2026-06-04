# Автоматизации репозитория Knowledge_substrate

Здесь собраны workflow, которые обеспечивают автоматизацию в репозитории Knowledge_substrate и межрепозиторные синхронизации. Файл служит краткой навигацией по задачам сборки, деплоя и обмена данными между репозиториями.

## 🚀 Deploy Docs (`.github/workflows/docs.yml`)
- 🏗️ Собирает документацию на MkDocs при изменениях в документационных путях.
- 🌐 Публикует результат в GitHub Pages, чтобы в MkDocs отображались данные из файлов в [`knowledge_core/source_of_truth/docs/`](../../knowledge_core/source_of_truth/docs/).

## 🔁 Sync Blog Posts to Site (`.github/workflows/sync-blog-posts.yml`)
- 📦 Копирует посты из Knowledge_substrate в репозиторий `DETai-org/sites`.
- 🔄 Поддерживает синхронизацию блогов при обновлениях в целевых каталогах.

## 🗓️ Monthly Docs Snapshot (`.github/workflows/monthly-docs-snapshot.yml`)
- 🏷️ Создаёт ежемесячный аннотированный тег `docs-ecosystem-YYYY-MM` от ветки `main` как active snapshot публичного состояния `docs/ecosystem`.
- 🕛 Запускается в `23:55` по `Europe/Moscow` в последние дни месяца и реально срабатывает только в последний календарный день месяца.
- 🔎 Перед созданием тега проверяет открытые PR, связанные с `docs/ecosystem`, по label, имени ветки и документационному пути, чтобы зафиксировать незамёрженные изменения.
- 📝 Сохраняет короткую snapshot-note как artifact и в summary workflow, чтобы monthly snapshot был связан с текущим редакционным состоянием.
- 🎛️ Поддерживает `workflow_dispatch` с `force_run=true` для ручной проверки вне конца месяца.

## 🧭 Create Linear issue on merge to main (`.github/workflows/linear-create-issue-on-merge.yml`)

### Условия создания задачи
Задача создаётся только при добавлении новых файлов (A) в одном из каталогов:

docs/publications/blogs/personal_site_blog/\
docs/publications/blogs/detai_site_blog/

Дополнительно используется список `knowledge_core/source_of_truth/docs/publications/blogs/list_publication_blogs.json`: если новый файл уже есть в списке, workflow завершится без создания задачи. При успешной отправке задачи в Linear имя обнаруженного файла автоматически добавляется в JSON-список.

Помимо фиксации нового имени в списке, этот workflow обеспечивает актуализацию данных для сайта: обновлённый [`list_publication_blogs.json`](../../knowledge_core/source_of_truth/docs/publications/blogs/list_publication_blogs.json) попадает в репозиторий сайта (копируется в [`packages/blog-index/`](https://github.com/DETai-org/sites/tree/main/packages/blog-index) в рамках синхронизации блогов). Таким образом, процесс одновременно обновляет реестр публикаций и подготавливает JSON-индекс для сайта.

### Что передаётся в Linear
📌 Передаёт в Linear `LINEAR_TEAM_ID`, `LINEAR_PROJECT_ID`, `LINEAR_LABEL_ID_POST_TO_BLOG`, `LINEAR_ASSIGNEE_ID`, а также контекст `repo`, `sha`, `actor` для описания задачи.

📌 Описание создания API для Linear хранится в ClickUp: [ссылка](https://example.com)

### Create Linear issue - подставляет текст из файлов Promt:

#### promt.md
Это базовый Промт используется Когда в посте нет или очень мало цитат

#### promt_2.md  
Это  Фолбэк-вариант промпта при ошибках, связанных с авторским правом

Иногда Codex не выполняет задачу, если ему передать полный текст поста для записи в файл. В большинстве случаев это связано с нарушениями авторских прав: в тексте присутствуют цитаты современных авторов, защищённые копирайтом.

В этом случае используется альтернативный подход.  
Сначала текст поста вручную добавляется в файл без какой-либо обработки. После этого Codex получает отдельный промпт, в котором работает уже с готовым файлом и формирует все описания: SEO-поля, превью и полностью заполняет frontmatter.

Этот подход позволяет обойти ограничения, связанные с авторскими правами, и корректно завершить процесс оформления поста.

Важно про шаблон промпта
Используется шаблон .github/workflows/prompt_2.md.

В нём есть специальный маркер для имени файла:

Название файла: <<FILE_NAME>>
⚠️ Этот маркер нельзя удалять или менять — он используется для автоматической подстановки имени(имен) файлов новых постов.

## Общая таблица

| Workflow | Затрагиваемый репозиторий | Запуск |
| --- | --- | --- |
| Monthly Docs Snapshot | Knowledge_substrate | schedule 28-31 числа, реальный запуск только в последний день месяца; workflow_dispatch |
| Deploy Docs | Knowledge_substrate | push/pr в main по путям docs |
| Sync Blog Posts to Site | Knowledge_substrate → DETai-org/sites | push в main по путям blog posts |
| Create Linear issue on merge to main | Knowledge_substrate | workflow_dispatch; workflow_run после Sync Blog Posts |
