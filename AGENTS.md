# AGENT Instructions — Knowledge_substrate

## Общий контекст
Этот репозиторий — каноническая база знаний экосистемы DET / DETai.
Главная особенность: **папка `knowledge_core/source_of_truth/docs/` — это источник дополнительных контекстов**.
Если входные данные пользователя недостаточно ясны, **разрешено и рекомендуется** уточнять контекст, опираясь на документы из `docs/ecosystem/ru/ecosystem/`.

## Операционный log-summary

```yaml
log_summary:
  list_id: "901523604300"
  list_url: "https://app.clickup.com/90152202658/v/li/901523604300"
  scope: Infrastructure
  context: knowledge-substrate
  navigation_key: knowledge_substrate
  global_navigation: D:\dev\DETai-org\Management_Layer\docs\clickup-navigation\index.yaml
```

Основной маршрут — живой List `logs` в Folder `📦 Knowledge Substrate`
в Space `Infrastructure`. Не используй одноимённую удалённую Folder из
Space `Projects` и её List `901523603652`. Датированные итоги записывай только
в ClickUp через skill `log-summary`; локальные `*log-summary.md` не создавай.

## Правила работы со ссылками на базу знаний (MkDocs)

Если в файлах репозитория встречается ссылка на документацию в формате публичного URL MkDocs (https://detai-org.github.io/), агент может получать её содержимое двумя способами: открывая страницу по указанному адресу или обращаясь к соответствующему файлу внутри репозитория.\
Поскольку база знаний MkDocs собирается из файлов, находящихся в папке `knowledge_core/source_of_truth/docs/ecosystem/`, такую ссылку можно рассматривать как указатель не только на внешнюю веб-страницу, но и на путь к документу внутри этой папки, при сохранении остальной структуры URL.
Рекомендуется использовать тот способ доступа, который в конкретной ситуации оказывается быстрее и продуктивнее для получения нужной информации.

## Правило внесения правок в документы экосистемы

Если задача требует добавить, изменить или уточнить файлы внутри `knowledge_core/source_of_truth/docs/ecosystem/ru/ecosystem/*`, правки сначала вносятся в сборочную ветку `docs/ecosystem`, связанную с pull request `#217 Docs/ecosystem`.

Не вносить такие изменения напрямую в `main`: сначала переключиться на `docs/ecosystem`, перенести или выполнить правки там, а уже затем готовить их к публикации через соответствующий pull request.
