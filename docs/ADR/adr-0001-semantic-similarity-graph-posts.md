# ADR-0001: Semantic Similarity Graph for Posts (Publish Only)

## Status

Accepted

## Date

2026-02-03

---

## Context

* В экосистеме DET / DETai существует канонический Source of Truth (SoT) для публикаций типа `post` в формате Markdown + frontmatter.
* На уровне сайта уже реализована фильтрация и навигация по метаданным (рубрики, категории, годы, авторы).
* Требуется получить семантическую карту смысловой близости опубликованных постов для:

  * выявления кластеров смыслов и центральных узлов,
  * формулирования постулатов и опорных концепций DET,
  * демонстрации концептуальной структуры проекта.
* Контракты и реализация других типов документов (quote, research_publication и др.) ещё не готовы.
* Решение должно быть минимальным по сложности, но расширяемым на будущие типы документов.

---

## Decision

1. **Scope:** строить семантический граф только для документов типа `post` со статусом `publish`.
2. **Source:** использовать тексты напрямую из Source of Truth (Markdown + frontmatter).
3. **Storage:** сохранять embeddings и similarity edges в Operational Store (PostgreSQL) и предоставлять доступ через API.
4. **Embeddings strategy:** использовать document-level embeddings (1 embedding на 1 пост).
5. **Graph construction strategy:** строить граф по подходу Top-K для каждого документа с дополнительным порогом `min_similarity`.
6. **API contract:** добавить endpoint (например `/graph`) для выдачи графа в формате `nodes + edges`, фильтруя только publish-посты.
7. **Execution model:** исполнять pipeline на self-hosted runner в том же контуре, что и PostgreSQL (не на GitHub-hosted runner).

---

## Rationale

* Document-level embeddings достаточны для задачи «пост ↔ пост» и позволяют избежать сложности чанкинга.
* Top-K гарантирует связность графа и снижает риск получения пустого или чрезмерно разреженного результата.
* Хранение в PostgreSQL упрощает обновление данных, фильтрацию и интеграцию с API и UI.
* Использование self-hosted runner необходимо из-за недоступности локальной БД из GitHub-hosted окружения.
* Ограничение scope только publish-постами позволяет получить практический результат без ожидания готовности всех контрактов.

---

## Consequences

### Positive

* Быстро появляется рабочий семантический граф постов на сайте.
* Архитектура расширяема на другие типы документов без переписывания базового решения.
* Обновление графа может быть идемпотентным и привязанным к изменениям SoT.

### Negative / Trade-offs

* На старте граф охватывает только тип `post`.
* Появляется дополнительный слой сложности: embeddings и similarity edges.
* Top-K может создавать «вынужденные» связи, что компенсируется порогом `min_similarity`.

---

## Alternatives Considered

* **Threshold-only graph (similarity ≥ T):** отклонено из-за риска пустого или чрезмерно разреженного графа.
* **Chunk embeddings:** отклонено как избыточное для задачи «пост ↔ пост» и усложняющее pipeline.
* **Хранение графа как JSON-файла:** отклонено из-за слабой масштабируемости и неудобства для API и фильтрации.

---

## Follow-up

* Выбрать конкретную модель embeddings.
* Реализовать pipeline: parse SoT → embed → build edges → persist.
* Реализовать API `/graph` и страницу визуализации в Next.js.

---

## Связанные документы
- Guide: [Semantic Similarity Graph for Posts](../guides/guide-semantic-graph-posts.md)
