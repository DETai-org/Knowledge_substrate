# Quotes

`docs/publications/quotes/` — место для канонических quote-документов домена `publications`.

Здесь должны жить **сами Quote Records** и их derivative publication assets, если они переводятся в общий canonical layer Knowledge Substrate.

## Canonical Layout

Для каждой цитаты используется отдельная директория публикационной единицы:

```text
knowledge_core/source_of_truth/docs/publications/quotes/<quoteId>/
  record.json
  assets/
    <lang>/
      <template>.png
      <template>.webp
```

Главный объект данных:

```text
knowledge_core/source_of_truth/docs/publications/quotes/<quoteId>/record.json
```

Это layout, согласованный с operational storage model проекта `psychology-in-quotes` в ветке `Release-Fixation`.

## Storage Semantics

- `record.json` — primary source для publication unit;
- `assets/<lang>/...` — derivative artifacts, связанные с этой же цитатой;
- одна цитата = одна директория;
- runtime/private state сюда не относится.

На текущем этапе основной file-based derivative layer здесь — это image assets (`png`, `webp`).
Дополнительные platform-specific refs, например `telegramFileId`, могут жить в самом `record.json` как часть asset metadata.

Это не место для:
- user runtime data;
- brand kits;
- bot settings;
- SQL runtime state;
- системных bot defaults.

Производные binary artifacts допустимы здесь как часть publication unit, но не как primary source вместо `record.json`.

Схема и контракт этого типа документа находятся в:
- `knowledge_core/source_of_truth/schemas/publications/quotes/quote_record_contract.md`
