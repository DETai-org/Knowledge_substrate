Важно: есть поля, общие для всех типов документов (например, `authors` в блоке administrative). Все авторы перечислены в соответствующем JSON-файле `authors.json`.

Структура **publications_schema** в JSON формате.

Ниже — **3 отдельных JSON** (по типам документов).


---

## Тип документа: Post (Пост)

```json
{
  "type": "post",
  "administrative": {
    "id": "unique_identifier",
    "authors": ["Author1", "Author2"],
    "date_ymd": "2026-01-15",
    "status": "publish",
    "channels": ["detai_site_blog", "personal_site_blog"]
  },
  "descriptive": {
    "size": "M",
    "title": "Title of the post",
    "preview": "Preview content for social media",
    "seoLead": "SEO description",
    "taxonomy": {
      "rubric_ids": ["rubric:shadow-and-light"],
      "category_ids": ["category:top-ideas"],
      "cycle_ids": ["cycle_123:Post-announcement"],
      "keyword_ids": ["keyword:ambivalence"],
      "keywords_raw": ["SEO", "AI research"]
    },
    "content": "Full post content"
  },
  "structural": {
    "external_links": [
      { "type": "website", "url": "link_to_post_on_website" },
      { "type": "telegram", "url": "link_to_post_in_telegram" }
    ],
    "document_links": [
      {
        "linked_document_id": "linked_document_id",
        "link_type": "citation"
      }
    ]
  }
}
```

`administrative.channels` может содержать **один или несколько** сайтов. Если указано несколько, файл публикуется в каждой соответствующей папке `docs/publications/blogs/<TARGET_SITE>/`.

---

## Тип документа: Research Publication (Научная публикация)

```json
{
  "type": "research_publication",
  "administrative": {
    "id": "unique_identifier",
    "authors": ["Author1", "Author2"],
    "date_ymd": "2026-01-15",
    "status": "publish",
    "subtype": "article"
  },
  "descriptive": {
    "title": "Research paper title",
    "abstract": "Research abstract",
    "journal": "Journal name",
    "doi": "DOI link",
    "taxonomy": {
      "rubric_ids": [],
      "category_ids": [],
      "keyword_ids": [],
      "keywords_raw": []
    },
    "content": "Research content"
  },
  "structural": {
    "external_links": [
      { "type": "website", "url": "link_to_research_on_website" },
      { "type": "telegram", "url": "link_to_research_in_telegram" }
    ],
    "document_links": [
      {
        "linked_document_id": "linked_document_id",
        "link_type": "citation"
      }
    ]
  }
}
```

### Подтип публикации (administrative.subtype)

Допустимые значения:

* `article` — статья, опубликованная в журнале, сборнике или на площадке.
* `dissertation` — диссертация (полная научная работа).
* `thesis` — тезисы/краткий доклад, обычно для конференций или сборников.

Примечание: на текущем этапе **rubric_ids** и **category_ids** применяются к постам, но **не назначаются** научным публикациям.  
В будущем возможно связать рубрики/категории постов с научными публикациями, но сейчас их роль выполняет только подтип.

---

## Тип документа: Quote (Цитата)

`quote` — отдельный тип документа схемы `publications`.

Полный детальный контракт вынесен в:

- `knowledge_core/source_of_truth/schemas/publications/quotes/quote_record_contract.md`

Верхнеуровневая фиксация для `publications_schema`:

- source of truth для цитаты — **Quote Record**, а не изображение;
- `quote` относится к домену `publications`;
- derivative assets не являются первичным каноническим слоем;
- user runtime data и project-private state не относятся к `quote` как типу публикационного документа.

Сами quote-документы должны жить в document-layer:

- `knowledge_core/source_of_truth/docs/publications/quotes/`

Контракт schema-layer должен жить отдельно:

- `knowledge_core/source_of_truth/schemas/publications/quotes/`

Такое разделение позволяет не смешивать:
- document instances;
- schema contracts;
- project runtime data;
- SQL-нормализацию.

---

## Примечание: автор мысли и источник

`attribution.quote_author` и `attribution.source` описывают разные уровни атрибуции:

- `attribution.quote_author` = кому принадлежит мысль или цитируемый фрагмент;
- `attribution.source` = откуда цитата взята как публикационный источник: книга, статья, лекция, сборник или другое издание.

В простом случае автор мысли и автор книги совпадают. В сложных случаях дополнительные сведения об авторах, редакторах, переводчиках и издании могут добавляться в `attribution.source` или в будущий нормализованный слой `sources`.

Текущий v0.1 Quote Record намеренно хранит компактный Document View. При росте проекта он может быть разложен в DB View: `documents`, `quote_attribution`, `sources`, `quote_sources`, `external_links`, `document_links`.
_____

# 📋 Памятка сущностей `publications_schema` (каноническая)

---

## **Document**

Единица контента в системе (пост, научная публикация или цитата), имеющая собственный идентификатор, статус, содержание, связи и внешние публикации.

---

## **type**

Тип документа, определяющий его назначение и набор допустимых полей.  
Возможные значения: `post`, `research_publication`, `quote`.

---

## **administrative**

Блок метаданных, отвечающий за управление документом внутри системы (кто создал, в каком он состоянии, когда опубликован).

---

## **id**

Уникальный и стабильный идентификатор документа в системе.

---

## **authors**

Список авторов документа **как сущности в системе** — кто создал, опубликовал или курирует данный документ (не автор идеи или цитаты).

---

## **date_ymd**

Дата публикации или фиксации документа в формате `YYYY-MM-DD`, используемая для хронологии и сортировки.

---

## **status**

Состояние документа в жизненном цикле публикации.  
Типовые значения: `draft` (черновик), `publish` (опубликован).

---

## **administrative.channels**

Канал размещения для постов: это **градация применяется только к типу документа `post`**.  
Пост в данном контексте — это публикация в социальных сетях, которая может быть размещена **либо в блоге профессионального сайта, либо в блоге персонального сайта**.  
Именно по этой метке можно определить, в какой из двух папок внутри `knowledge_core/source_of_truth/docs/publications/blogs` лежит конкретный пост.

Допустимые значения:

* `detai_site_blog` — блог профессионального сайта.
* `personal_site_blog` — блог персонального сайта.

---

## **descriptive**

Блок метаданных, описывающий смысл, содержание и тематическую принадлежность документа.

---

## **title**

Заголовок документа, отображаемый пользователю и используемый для навигации и поиска.

---

## **content**

Основное текстовое содержание документа (тело поста, текст исследования или текст цитаты).

---

## **taxonomy**

Классификация документа по управляемым словарям (controlled vocabularies).  
`rubric_ids`, `category_ids`, `keyword_ids` содержат только ссылки на словари,  
а `keywords_raw` — единственный допустимый слой для свободных строк на время модерации.  
`cycle_ids` — опциональная ссылка на цикл постов; если пост не состоит в цикле, поле **не указывается**.

---

## **rubric_ids**

Верхнеуровневые тематические области, к которым относится документ  
(берутся из контролируемого словаря `rubrics`, формат `rubric:*`).

Для `type = post` допускается **ровно одна** рубрика.

---

## **category_ids**

Более узкие тематические группы внутри рубрик, уточняющие фокус документа  
(берутся из контролируемого словаря `categories`, формат `category:*`).

Для `type = post` допускается **ровно одна** категория.

---

## **keyword_ids**

Ключевые слова для дополнительной детализации и поиска  
(берутся из контролируемого словаря `keywords`, формат `keyword:*`).

---

## **keywords_raw**

Свободные ключевые слова на период перехода, пока `keyword_ids` заполняется и проходит модерацию.

---

## **cycle_ids**

Опциональная связь поста с циклом.  
Если пост входит в цикл, указывается `cycle_ids` (например, `["cycle_123"]`) —  
в массиве допускается **только один** элемент.  
Для **первого поста цикла** допускается маркер родительского поста через суффикс  
`cycle_123:Post-announcement`.  
Если пост **не входит** в цикл, поле **отсутствует** (пустые значения не используются).

---

### Стратегия ключевых слов (переходный период)

- Сначала все документы получают `keywords_raw`.
- Затем ключевые слова постепенно сопоставляются с `keyword_ids`.
- Кандидаты в словаре переводятся в `approved` после проверки.

---

### Статусы жизненного цикла словарей (lifecycle)

- `candidate` — добавлено и ждёт проверки.
- `approved` — проверено и доступно для использования.
- `deprecated` — устарело и не рекомендуется к использованию.

---

## **preview**

Краткое описание или вводный текст документа, используемый для превью в лентах и социальных сетях (для постов).

---

## **seoLead**

SEO-описание документа для поисковых систем и внешних публикаций (для постов).

---

## **abstract**

Краткое содержание научной публикации, отражающее цель, метод и результаты исследования (для research_publication).

---

## **journal**

Название научного журнала или издания, в котором опубликована научная работа.

---

## **doi**

Digital Object Identifier — постоянный идентификатор научной публикации.

---

## **attribution**

Блок описания авторства идеи или высказывания, **не связанный с авторством документа**.

---

## **quote_author**

Автор высказывания или идеи, которой принадлежит цитата (автор книги, статьи, речи).

---

## **source**

Описание источника, из которого взята цитата или материал.

---

## **source.title_original**

Оригинальное название источника на языке первоисточника.

---

## **source.title_display**

Локализованные названия источника для отображения в интерфейсах и карточках цитат.

---

## **source.original_language**

Язык первоисточника в коде экосистемы или совместимом языковом коде.

---

## **source.original_year**

Год оригинального издания как числовое поле. Используется для фильтрации, сортировки и исторического контекста без парсинга строк APA/GOST.

---

## **source.page**

Страница или локатор источника, где находится цитата (например, `27`, `27–29`, `section 3`).

---
## **structural**

Блок метаданных, описывающий связи документа с другими документами и внешними платформами.

---

## **external_links**

Ссылки на внешние ресурсы, где документ опубликован или упоминается (сайт, Telegram и т.д.).

---

## **external_links.type**

Тип внешней платформы (например, `website`, `telegram`, `doi`).

---

## **external_links.url**

URL внешнего ресурса.

---

## **document_links**

Внутренние связи между документами внутри базы данных, используемые для навигации и построения графа знаний.

---

## **document_links.linked_document_id**

Идентификатор документа, на который ссылается текущий документ.

---

## **document_links.link_type**

Тип связи между документами (например, `citation`, `reference`, `related`).

---

## **Controlled Vocabulary**

Реестр заранее определённых значений (rubrics, categories, keywords), являющийся источником истины для классификации документов.
### 🧠 Коротко:

- **administrative** — управление документом
    
- **descriptive** — смысл и содержание
    
- **structural** — связи и размещение
    
- **taxonomy** — ссылки на контролируемые словари
    
- **quote_author ≠ authors** — это принципиально разные сущности
    

---

## Двухслойный канон

- **Document View** (как хранится/рендерится документ — удобный JSON с `administrative/descriptive/structural`)
    
- **DB & Index View** (как это нормализуется в таблицы/коллекции + какие индексы нужны)
    

Ниже — прям “вариант для баз и индексов” под твои 3 типа документов + связи.

Для настоящей SQL-базы **лучше держать два слоя**:

- **Document View** (как у тебя сейчас — удобно жить)
    
- **DB & Index View** (нормализованные таблицы для связей/таксонов/поиска/графа)
    
    Структура для publications_sche…
    

И вот это как раз **самая мировая практика**:  
внутри документа — удобная форма,  
в базе — нормализованная форма (особенно `document_links`, `external_links`, и controlled vocabularies для taxonomy).

---

# 1) Document View (как  уже есть выше)

Ты оставляешь в документе:

- `administrative.*`
    
- `descriptive.*`
    
- `structural.external_links[]`
    
- `structural.document_links[]`
    

Это удобно для UI/рендера/экспорта.

---

# 2) DB View — нормализация (таблицы/коллекции)

## 2.1 Таблица `documents` (общая для всех типов)

**Идея:** один стол для “каркаса”, остальное — в JSONB или отдельные таблицы по типам.

```json
{
  "table": "documents",
  "pk": "id",
  "fields": {
    "id": "text/uuid",
    "type": "enum(post, research_publication, quote)",
    "status": "enum(draft, publish)",
    "date_ym": "char(7)  // YYYY-MM",
    "title": "text",
    "content": "text",
    "lang": "text (optional)",
    "descriptive_json": "jsonb  // всё, что кроме title/content можно держать здесь",
    "created_at": "timestamp",
    "updated_at": "timestamp"
  }
}
```

> Почему так: `documents` даёт быстрые списки/фильтры, а `descriptive_json` — гибкость, чтобы не мигрировать схему каждый раз.

---

## 2.2 Авторы (две сущности, чтобы не путаться)

### A) `authors` (реестр авторов)

```json
{
  "table": "authors",
  "pk": "author_id",
  "fields": {
    "author_id": "text/uuid",
    "display_name": "text",
    "slug": "text (unique)",
    "type": "enum(person, org)",
    "meta": "jsonb"
  }
}
```

### B) `document_authors` (кто создал документ в твоей системе)

```json
{
  "table": "document_authors",
  "pk": ["document_id", "author_id"],
  "fields": {
    "document_id": "fk -> documents.id",
    "author_id": "fk -> authors.author_id",
    "role": "enum(owner, editor, contributor) (optional)",
    "sort_order": "int (optional)"
  }
}
```

### C) `quote_attribution` (кому принадлежит мысль — автор источника/цитаты)

(можно JSONB внутри documents, но лучше отдельно, чтобы фильтровать “цитаты Ницше” без костылей)

```json
{
  "table": "quote_attribution",
  "pk": "document_id",
  "fields": {
    "document_id": "fk -> documents.id (type=quote)",
    "quote_author_id": "fk -> authors.author_id"
  }
}
```

---

## 2.3 Источники цитат (книга/статья и т.п.)

### `sources` (реестр источников)

```json
{
  "table": "sources",
  "pk": "source_id",
  "fields": {
    "source_id": "text/uuid",
    "source_type": "enum(book, article, podcast, video, lecture, other)",
    "title": "text",
    "author_id": "fk -> authors.author_id (optional)",
    "publisher": "text (optional)",
    "year": "int (optional)",
    "isbn": "text (optional)",
    "meta": "jsonb"
  }
}
```

### `quote_sources` (привязка источника к цитате + страницы)

```json
{
  "table": "quote_sources",
  "pk": "document_id",
  "fields": {
    "document_id": "fk -> documents.id (type=quote)",
    "source_id": "fk -> sources.source_id",
    "pages": "text  // '27' или '27–29'",
    "chapter": "text (optional)",
    "locator": "jsonb (optional) // если захочешь: {edition, section, kindle_location}"
  }
}
```

---

## 2.4 Таксономия (rubrics/categories/keywords) как controlled vocabularies

### `taxons` (единый реестр таксонов)

```json
{
  "table": "taxons",
  "pk": "taxon_id",
  "fields": {
    "taxon_id": "text/uuid",
    "vocab": "enum(rubric, category, keyword)",
    "label": "text",
    "slug": "text (unique within vocab)",
    "parent_id": "fk -> taxons.taxon_id (optional)  // category -> rubric",
    "meta": "jsonb"
  }
}
```

### `document_taxons` (привязка документов к таксонам)

```json
{
  "table": "document_taxons",
  "pk": ["document_id", "taxon_id"],
  "fields": {
    "document_id": "fk -> documents.id",
    "taxon_id": "fk -> taxons.taxon_id",
    "weight": "float (optional)",
    "source": "enum(manual, ai) (optional)"
  }
}
```

---

## 2.5 Ссылки

### `external_links` (нормализованно)

```json
{
  "table": "external_links",
  "pk": "link_id",
  "fields": {
    "link_id": "text/uuid",
    "document_id": "fk -> documents.id",
    "type": "enum(website, telegram, instagram, facebook, doi, other)",
    "url": "text",
    "label": "text (optional)",
    "created_at": "timestamp"
  }
}
```

### `document_links` (внутренние связи / граф)

```json
{
  "table": "document_links",
  "pk": "edge_id",
  "fields": {
    "edge_id": "text/uuid",
    "from_document_id": "fk -> documents.id",
    "to_document_id": "fk -> documents.id",
    "link_type": "enum(citation, related, references, expands, contrasts, sequel, appendix, other)",
    "context": "text (optional)  // кусок текста/пояснение",
    "weight": "float (optional)",
    "created_at": "timestamp"
  }
}
```

---

# 3) Индексы (что именно индексировать)

## 3.1 Базовые индексы (почти всегда)

```json
{
  "indexes": [
    { "table": "documents", "fields": ["type", "status", "date_ym"] },
    { "table": "documents", "fields": ["status"] },
    { "table": "documents", "fields": ["date_ym"] },
    { "table": "document_taxons", "fields": ["taxon_id", "document_id"] },
    { "table": "document_links", "fields": ["from_document_id"] },
    { "table": "document_links", "fields": ["to_document_id"] },
    { "table": "external_links", "fields": ["document_id", "type"] }
  ]
}
```

## 3.2 Поиск (если нужен быстрый поиск по текстам)

- full-text индекс по `documents.title + documents.content`
    
- плюс (опционально) отдельный индекс по `descriptive_json` если часто фильтруешь по нему
    

## 3.3 Цитаты (быстрые запросы типа “все цитаты автора X из книги Y”)

```json
{
  "indexes": [
    { "table": "quote_attribution", "fields": ["quote_author_id"] },
    { "table": "quote_sources", "fields": ["source_id"] },
    { "table": "quote_sources", "fields": ["document_id"] }
  ]
}
```

---

# 4) Как это живёт вместе (самое важное)

### В документе (Document View)

Ты хранишь `structural` как удобный “денормализованный” слой.

### В базе (DB View)

Ты хранишь:

- `external_links` и `document_links` как отдельные таблицы
    
- taxons как controlled vocabularies
    
- sources отдельно, чтобы цитаты реально стали “сеткой” вокруг книг
    

### Синхронизация правила (простые)

- документ сохраняется → сервис/скрипт пересобирает нормализованные таблицы ссылок/таксонов
    
- или наоборот: ты пишешь в таблицы, а Document View собирается при выдаче (но это сложнее)

⚠️ Важно

`document_links` сейчас “односторонние”

У меня в `document_links` есть:

- `linked_document_id`
    
- `link_type`
    
    Структура для publications_sche…
    

Этого достаточно для Document View. Но для “графа” обычно полезно **явно иметь направление**:

- `from_document_id` (это текущий документ)
    
- `to_document_id` (linked)
    

В  JSON это не обязательно хранить (контекст “from = текущий документ” и так ясен), но в **DB-представлении** это надо обязательно сделать.

---



Если хочешь, следующим сообщением я дам **ровно 3 JSON “DB schemas”** (Post/Research/Quote) как ты просил ранее, но уже именно в терминах:  
`documents + post_meta`, `documents + research_meta`, `documents + quote_meta + sources`, где `*_meta` — либо JSONB, либо отдельные поля.

Следующий логичный шаг: зафиксировать “канон 2-слоя” (Document View + DB View) **уже как стандарт**, чтобы потом не путаться при реализации.

 > [!TIP] чтобы это сразу было готово под PostgreSQL + будущий граф + pgvector.

____
___



# Дополнение

### **📌 1. Разделение типов метаданных**

Мировые практики рекомендуют разделять **administrative, descriptive и structural** метаданные, чтобы ясно понимать цель каждого поля.  
В твоей схеме это частично есть, но можно подсветить:

- **Administrative** — status, authors (можно отдельная таблица для авторов).
    
- **Descriptive** — title, abstract, categories, keywords.
    
- **Structural** — document_links, external_links.
    

Это улучшает поддерживаемость и интероперабельность данных.

---

### **📌 2. Контролируемые словари**

Лучшие практики таксономии рекомендуют **controlled vocabularies** (управляемые словари) — когда рубрики, категории и ключевые слова берутся из заранее определённого списка, чтобы избежать разрозненных форм.

Ты можешь предусмотреть:

`"rubric_id": "controlled_rubric_id", "category_id": "controlled_category_id"`

см. [[Контролируемые словари]]




### **📌 4. Сохранение структуры семантики для внешнего использования**

Если ты планируешь, чтобы данные **читались машинами** (search engines, Linked Data), то стоит ориентироваться на стандарты типа **schema.org/Article**, **schema.org/ScholarlyArticle**.  
Это позволит в будущем напрямую экспортировать JSON в микроразметку для публикаций в сети.

# 🧩 Пункт 4: Schema.org — нужно добавить тонкий “слой экспорта”

Тут важно: **schema.org — это не про твою БД**, а про то, как ты **публикуешь наружу** (на сайт) в виде JSON-LD микроразметки.

То есть тебе не надо переделывать схему — тебе нужно предусмотреть:

### 1) “mapping-слой”

Правило: как поля твоего документа превращаются в schema.org.

### 2) несколько полей, которые schema.org любит

У тебя почти всё уже есть. Обычно надо добавить/уточнить:

- `canonical_url` (на сайте)
    
- `datePublished` (можно собрать из `date_ym`, хотя лучше иметь точную дату публикации — но можно жить и без неё)
    
- `image` (если будет превью-картинка)
    
- `publisher` / `author` (для внешнего мира)
    
- для ScholarlyArticle: `identifier` (DOI), `isPartOf` (журнал), и т.п.
    

### 3) экспорт для каждого типа

- Post → `schema.org/Article` или `BlogPosting`
    
- Research → `schema.org/ScholarlyArticle`
    
- Quote → чаще всего `schema.org/Quotation` (и/или `CreativeWork`), плюс ссылка на источник-книгу
