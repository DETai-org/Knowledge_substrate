---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: brand-and-communications
  layer: technology
  function: explanation
  domain: storytelling
descriptive:
  id: storytelling-technology-foundation
  version: v2
  status: active
  date_ymd: 2026-08-20
  date_update: 2026-09-23
governance:
  canonicality: canonical
  visibility: public
title: Как Storytelling использует технологическую основу
---

# Как Storytelling использует технологическую основу

[Storytelling](index.md) владеет предметной логикой публикационного процесса, а общие технические системы предоставляют ему отдельные replaceable capabilities. Наличие интеграции не переносит ownership публикации в инфраструктуру.

## Intelligence Runtime

Storytelling определяет структуру материала, редакционную последовательность, правила enrichment и локализации, human review, Representation и delivery intent.

[intelligence-runtime](../Infrastructure/intelligence-runtime/index.md) определяет, как технически выполнить LLM-шаг: выбрать модель, проверить формат, выполнить repair/retry и вернуть trace.

```text
Storytelling rules + source
→ Intelligence Runtime execution
→ proposal + trace
→ Storytelling human review
→ approved content version
```

Модель или runtime не становятся source of truth редакционного смысла.

## Sites

Storytelling передаёт Site Representation и утверждённый destination intent. Проект `sites` владеет web-runtime: маршрутами, HTML, SEO, Open Graph, structured data и deployment. Storytelling не должен знать внутреннее устройство Next.js, а Sites не должен присваивать себе enrichment, локализацию или publication approval.

## Telegram execution

Telegram Representation и Telegram execution разделены. Storytelling владеет target, immutable artifact, approval, idempotency identity, delivery intent и выбранной logical execution identity как operator preference.

Проект [Telegram](../DETai/Platform_DETai/E2-Brand/Telegram/index.md) владеет managed accounts, authorization и sessions, Premium state, network profiles, Telegram API clients и техническим transport resolution.

Для каналов DETai Standard и Rich без Typography исполняются через Bot API, а Typography требует user execution. Storytelling не получает session-файлы, authorization key, телефон, 2FA или network credentials.

```text
Storytelling
→ exact target + immutable artifact + execution requirements
→ Telegram Service
→ identity + transport OR capability conflict
→ Telegram API
```

Это позволяет заменить Telethon или конкретный managed account без изменения Publication domain и Telegram Representation.

## Nexus и runtime

Nexus является production execution environment, а не владельцем Storytelling. Runtime-размещение и deployment не меняют ownership предметной логики.

Главный принцип: **Storytelling описывает, что должно быть создано и утверждено; инфраструктурные системы исполняют отдельные технические capabilities за явными границами.**
