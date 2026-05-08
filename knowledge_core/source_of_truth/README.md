# Source of Truth (SoT)

**Source of Truth** экосистемы **DET / DETai** хранит:
- канонические Markdown-документы;
- их frontmatter и связанные metadata-контракты;
- controlled vocabularies;
- схемы и политики, по которым эти документы затем попадают в SQL, graph и agent-facing слои.

## Три зоны ответственности

### 1. `docs/` — канон самих документов

`docs/` хранит **экземпляры знаний и публикаций**.

- `docs/ecosystem/{lang}/ecosystem/` — документы домена `ecosystem`.
- `docs/publications/` — документы домена `publications`.

Важно: языковые папки `ru/`, `en/`, `de/`, `fi/`, `cn/` не являются отдельными доменами знания.
Это presentation/localization rails внутри `docs/ecosystem/`.

### 2. `schemas/` — контракты, политики и naming rules

`schemas/` хранит **не сами документы**, а правила:
- какие типы сущностей существуют;
- как они именуются;
- какие поля у них допустимы;
- как они связываются между собой;
- какие controlled vocabularies применяются.

Домены в `schemas/` зеркалят домены в `docs/`:
- `schemas/ecosystem/`
- `schemas/publications/`

### 3. `assets/` — технический слой витрины

`assets/` хранит только технические файлы MkDocs:
- JS;
- CSS;
- overrides;
- hooks.

`assets/` не является knowledge-layer и не является SQL-layer.

## Как это связано с SQL

SoT не равен SQL-базе напрямую.

Корректная цепочка такая:

```text
source_of_truth/docs     -> canonical documents
source_of_truth/schemas  -> contracts and policies
SQL layers               -> operational/query representations
```

Это означает:
- `docs/` отвечает за материал;
- `schemas/` отвечает за контракт;
- SQL отвечает за производное operational/query-представление.

## Правило

Материалы Source of Truth используются как единый фундамент для:
- публикации через MkDocs Material;
- индексации и структурирования данных в SQL/Cloud SQL;
- построения knowledge graph;
- работы интеллектуальных агентов.

## MkDocs и публичность

- навигация MkDocs автогенерируется из структуры файлов;
- `docs/ecosystem/` публикуется как knowledge-витрина;
- `docs/publications/` остаётся частью канона и не входит в MkDocs-сборку;
- документ может существовать в каноне и использоваться системой, даже если он не показывается в публичной MkDocs-навигации.
