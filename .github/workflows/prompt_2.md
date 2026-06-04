# 🧠 Промпт для поточной работы

## ✅ Входные данные

Название файла: 

coverImage: "/images/posts/<postId>.png/jpg"

coverLayout:

coverImageScale:

alt: 

## 🎯 Задача
Появился новый пост в хранилище блог‑постов.  Твоя задача — **инфраструктура поста** (frontmatter + конфигурация + языковые файлы), **без изменения текста поста**.

## 0) Каноничные источники

Опирайся на:

- `knowledge_core/source_of_truth/schemas/publications/post_documents/` (зеркальная копия JSON-канонов рубрик/категорий/ключей из sites)
- `knowledge_core/source_of_truth/policies/` (человекочитаемые политики)
- `knowledge_core/source_of_truth/policies/shared/post-creation-prompt.md` (инструкции и ссылки для работы с `coverImage`, `coverLayout`, `coverImageScale`, `alt`)
  

## 1) Где лежит исходный пост

Я (пользователь) **уже добавлю** исходный пост **на русском** в одну из папок:

- `docs/publications/blogs/personal_site_blog/`
    
- `docs/publications/blogs/detai_site_blog/`
    

Возможны оба варианта сразу.  
Твоя задача — **взять frontmatter оригинала** (RU) из исходного blog post document и **перенести/нормализовать** его в инфраструктуру нужного сайта(ов).

## 2) Что именно делаем

### 2.1. blog.base.ts

Для каждого задействованного сайта:

- В `personal-site/lib/blog/blog.base.ts` и/или `detai-site/lib/blog/blog.base.ts`
    
- Добавь или обнови запись поста, используя **frontmatter RU** 
    
- Поля:
    
    - `postId` = id из frontmatter RU
        
    - `publishedAt` = дата из frontmatter RU (в ISO)
        
    - `author`
        
    - `status`
        
    - `rubric`, `categories`/`category`, `keywords`, `keywordsRaw`
        
    - `coverImage` (если есть)
        
    - `coverLayout`
        
    - `contentFiles` на `ru/en/de/fi/cn`
        

### 2.2. Папка поста + языки

Создай папку:

`<site>/lib/blog/posts/<postId>/`

И файлы:

`ru.md, en.md, de.md, fi.md, cn.md`

**Важно:**

- В каждом файле должен быть **полный frontmatter**.
    
- Для **ru.md** — frontmatter из оригинала 
    
- Для **en/de/fi/cn** — переведи `title`, `preview`, `seoLead`, `keywords_raw` на соответствующий язык.
    
- Остальные поля не меняй.


### Перенос текст поста из хранилища в `ru.md`

- Перенеси полный текст поста из хранилища в `ru.md` 
- Если видишь явные ошибки в разметки в теле поста то исправь разметку в `ru.md`  


## ✅🔍 Протокол самопроверки

- Есть `<lang>.md` для всех 5 языков.
- `routeSlug` заполнен во всех языках.
- `contentFiles` корректно указывает на файлы.
- Значения ⬇️

  preview: 
  seoLead: 
    rubric_ids: 
    category_ids: 
    cycle_ids:  
    keyword_ids:
    keywords_raw:         

взяты ИСКЛЮЧИТЕЛЬНО из исходного RU-файла поста из хранилища блог-постов. 
Сохранен исходный состав и распространен на все языковые версии;

- `coverImage` заполнен или соответствует политике (см. Каноничные источники)

- Поддержаны оба сайта, если исходные посты лежали в двух папках в `docs/publications/blogs/`.
____

⚠️ Важно: В описании PR укажи magic word вида: Fixes <ID текущей задачи Linear>

Техническая информация для пользователя:
- Репозиторий: {repo}
- Коммит: {sha}
- Автор merge: {actor} 
