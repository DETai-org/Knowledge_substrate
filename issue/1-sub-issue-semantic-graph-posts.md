# Sub-Issue 1: Semantic Graph (Postgres + Ingest + Embeddings)

## Title
Семантический граф для publish‑постов: база, ingest и построение графа.

## Purpose 🎯
Собрать полный технический контур семантического графа publish‑постов: от подготовки
БД‑схемы и ingest‑извлечения до расчёта эмбеддингов и построения similarity‑графа.
В результате должен появиться устойчивый контур данных, готовый к интеграции с
API‑слоем и визуализацией.

---

## Tasks (Acceptance Checklist)

- [x] DB migrations: pgvector + similarity_edges
  1. Подготовить безопасные и идемпотентные SQL‑миграции, которые включают pgvector,
     создают таблицу similarity‑графа и расширяют embeddings без ломки совместимости.
  2. Включить pgvector (CREATE EXTENSION IF NOT EXISTS vector).
  3. Создать knowledge.similarity_edges с обязательными полями и CHECK (source_id < target_id).
  4. Добавить CHECK (weight в диапазоне 0..1) и UNIQUE (source_id, target_id, doc_type, method).
  5. Добавить индексы: source_id, target_id, weight DESC.
  6. Добавить FK на knowledge.documents(id) с ON DELETE CASCADE (если таблица/тип подходят), иначе описать причину отсутствия FK.
  7. Проверить/создать knowledge.embeddings для doc‑level embeddings без ломки совместимости.
  8. Обновить sql/detai_core/workspace/db/README.md (pgvector, similarity_edges, undirected constraints).

---

- [x] Extract publish-posts from SoT
  1. Извлечь все опубликованные документы типа post из Source of Truth (Markdown + frontmatter)
     и привести их к единому структурированному формату для дальнейших этапов
     (embeddings → similarity graph → DB/API).
  2. Пройти по путям SoT с постами, считать markdown‑файлы, извлечь frontmatter и body.
  3. Отфильтровать только publish‑посты (type == "post", administrative.status == "publish").
  4. Построить text_for_embedding (очистка markdown, title + "\n\n" + body_text).
  5. Сформировать объект поста (id, title, authors, date_ymd, channels, taxonomy, text_for_embedding).

---

- [x] Embeddings & Graph Builder
  1. Построить семантический граф смысловой близости для опубликованных документов типа `post`:
     - рассчитать **document-level embeddings** (1 вектор на пост);
     - на их основе построить **undirected weighted similarity graph**;
     - сохранить embeddings и рёбра графа в **Operational Store (Postgres)**.
  2. Использовать граф для выявления смысловых кластеров, визуализации связей между постами
     и дальнейшего формирования постулатов **DET**.
  3. Добавить config.json и поддержать приоритет CLI → config → env → defaults.
  4. Обеспечить runnable CLI entrypoint и корректные логи по количеству постов/embeddings/edges.
  5. Реализовать устойчивость: retry с backoff, снижение batch и лимит длины текста.
  6. Добавить preflight, dry-run и структурные логи с run_id/stage.
  7. Добавить GitHub Actions workflow для self-hosted runner.
  8. Зафиксировать в README, что секреты идут через env (локально и Actions).

---

- [x] Исключение README и косметика логов
  1. Исключить служебные README.md из извлечения постов и привести логи пайплайна к
     читаемому виду с визуальными маркерами успеха/ошибок, чтобы диагностика была проще.
  2. Исключить README.md из обхода markdown-файлов в источнике публикаций.
  3. Снизить уровень логирования дубликатов постов и добавить информативный эмодзи.
  4. Добавить визуальные маркеры в логи этапов/ошибок пайплайна.
  5. Разделить preflight-проверку OpenAI на формат и фактическую доступность.

---

- [x] Дополнительные задачи после основного контура
  1. Укрепить preflight‑проверки и снизить риск дублей publish‑постов.
  2. Ослабить preflight‑проверку DATABASE_URL в пользу полного DSN.
  3. Сделать OPENAI_API_KEY условной проверкой (dry‑run / non‑openai).
  4. Добавить structured log для ошибок preflight.
  5. Добавить дедупликацию publish‑постов по administrative.id с prefer_channel.

## Verification Notes
Подтверждено, что publish‑посты корректно добавляются в базу данных
и доступны для последующей выдачи в API‑слое.

## Document package
- ADR: [ADR-0001: Semantic Similarity Graph for Posts](../docs/ADR/adr-0001-semantic-similarity-graph-posts.md)
- Guide: [Guide: Semantic Similarity Graph for Posts](../docs/guides/guide-semantic-graph-posts.md)
- Policy: [Policy: Semantic Graph for Posts](../docs/Policy/policy-semantic-graph-posts.md)

## 🚚 Delivery
Branch: `<branch-name>`
PR: [#95](https://github.com/DETai-org/Knowledge_substrate/pull/95)
