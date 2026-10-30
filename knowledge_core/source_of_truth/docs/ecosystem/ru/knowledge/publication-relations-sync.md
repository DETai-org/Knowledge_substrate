---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: knowledge-system
  layer: technical-standards
  function: reference
  system: knowledge
  domain: publication-relations-sync
  audiences: [team, developers, agents]
descriptive:
  id: knowledge-publication-relations-sync
  version: v1
  status: active
  date_ymd: 2026-09-19
governance:
  canonicality: reference
  visibility: public
  owner_role: knowledge-architect
  approver_role: ecosystem-architect
  review_date: 2026-10-19
links:
  external_links:
  document_links:
    - schema: ecosystem
      link_type: part-of
      linked_document_id: knowledge-system-index
    - schema: ecosystem
      link_type: interfaces-with
      linked_document_id: storytelling-index
    - schema: ecosystem
      link_type: interfaces-with
      linked_document_id: detai-platform-detai-e2-brand-sites-index
title: Связи публикаций с Knowledge Substrate
---

# Связи публикаций с Knowledge Substrate

Этот документ — **точка входа со стороны Knowledge Substrate** в процесс автоматической проекции связей опубликованных материалов. Он не дублирует owning contracts.

Редакционные критерии связи публикации с базой знаний определяются владельцами публикационного процесса и согласованными правилами сайта.

Точный жизненный цикл, разрешение идентификаторов, сверка и автоматизация принадлежат редакционно-техническому контуру Storytelling; эта публичная страница фиксирует их назначение, а не внутреннюю реализацию.

## Общая схема

```text
Full Publication authoring
→ canonical RU structural
→ Site PR
→ Site merge + production verification
→ Storytelling Knowledge Relations Sync
→ machine-managed relation в Knowledge Substrate
```

Публикация остаётся собственностью Site / Storytelling corpus. Knowledge Substrate хранит не копию поста, а разрешимую связь с ним.

Для Site publication используется stable identity:

```text
site:<detai|personal>:id:<postId>
```

Например:

```yaml
links:
  document_links:
    - schema: site-publication
      link_type: related-publication
      linked_document_id: site:detai:id:site-b0337ebc25e34117
```

`schema: site-publication` означает, что identity разрешается owning Site resolver через `DETai-org/sites/packages/blog-index`, а не через locale URL.

## Почему relation хранится здесь

Knowledge document может быть target публикационного relation даже тогда, когда сам пост физически живёт в другом репозитории. Machine-managed projection позволяет будущему knowledge graph и SQL/vector ingestion увидеть incoming relation без повторного анализа prose.

Projection является производной и восстанавливаемой: canonical relation set остаётся в опубликованном Site post, а Storytelling sync идемпотентно добавляет или удаляет соответствующую запись здесь.

Будущий SQL/vector ingestion должен импортировать как Knowledge Substrate documents, так и Site publications по их stable identities; SQL не становится source of truth.
