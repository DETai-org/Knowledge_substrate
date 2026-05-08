# Quote Record Contract

`quote` — документная сущность схемы `publications`.

Source of truth для цитаты — не изображение, а **Quote Record**: текст, языковые версии, атрибуция, источник, цитирование, таксономия и ссылки на производные assets.

## Минимальный контракт v0.1

```json
{
  "type": "quote",
  "id": "q_1",
  "administrative": {
    "curated_by": "Anton",
    "date_ymd": "2026-05-02",
    "status": "draft"
  },
  "texts": {
    "ru": {
      "text": "Любовь и труд неразделимы: мы любим то, над чем трудимся, и трудимся над тем, что любим.",
      "highlight": "Любовь и труд неразделимы",
      "status": "source"
    }
  },
  "taxonomy": {
    "rubric_ids": [],
    "category_ids": [],
    "keyword_ids": [],
    "keywords_raw": []
  },
  "attribution": {
    "quote_author": {
      "canonical_name": "Erich Fromm",
      "display_name": {
        "ru": "Эрих Фромм",
        "en": "Erich Fromm"
      }
    },
    "source": {
      "title_original": "The Art of Loving: An Enquiry into the Nature of Love",
      "title_display": {
        "ru": "Искусство любить",
        "en": "The Art of Loving"
      },
      "original_language": "en",
      "original_year": 1956,
      "publisher": "Harper & Brothers",
      "page": "56"
    },
    "source_display": {
      "ru": "Эрих Фромм, Искусство любить, с. 56"
    },
    "citations": {
      "apa": "Fromm, E. (1956). The art of loving: An enquiry into the nature of love. Harper & Brothers.",
      "gost": ""
    }
  },
  "assets": {
    "ru": {
      "white": {
        "webp": "content/quotes/assets/q_1/ru/white.webp",
        "png": "content/quotes/assets/q_1/ru/white.png"
      }
    }
  },
  "external_links": [
    {
      "type": "website",
      "url": ""
    },
    {
      "type": "telegram",
      "url": ""
    }
  ]
}
```

## Пояснение по полям

- `texts` хранит языковые версии цитаты. Поддерживаемые языки экосистемы: `ru`, `en`, `de`, `fi`, `cn`.
- `highlight` используется для визуального акцента в рендерах.
- `taxonomy` хранит ссылки на controlled vocabularies и переходный слой `keywords_raw`.
- `attribution.quote_author` отвечает на вопрос, кому принадлежит мысль.
- `attribution.source` описывает первоисточник или используемое издание.
- `attribution.source_display` хранит короткую человекочитаемую подпись для конкретного языка.
- `attribution.citations` хранит готовые строки для научного цитирования и экспорта.
- `assets` хранит ссылки на производные изображения по языку и шаблону.
- `external_links` хранит ссылки на опубликованные представления цитаты.

## Принципиальные границы

- Quote Record является canonical document data.
- Изображения являются derivative assets.
- Product output не должен становиться primary SQL binary layer.
- User runtime data проекта не относятся к Quote Record contract.

## Зоны ответственности репозиториев

- `DETai-org/Knowledge_substrate` хранит каноническую схему и политику типа документа `quote`.
- `DETai-org/psychology-in-quotes` может производить и обслуживать operational quote workflow.
- site-facing контуры потребляют Quote Records и assets как производные данные.
