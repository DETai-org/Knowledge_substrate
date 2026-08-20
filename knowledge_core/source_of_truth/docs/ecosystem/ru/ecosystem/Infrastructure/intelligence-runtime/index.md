---
type: ecosystem
classification:
  scope: Infrastructure
  context: intelligence-runtime
  layer: architecture-and-logic
  function: explanation
descriptive:
  id: infrastructure-intelligence-runtime
  version: v1
  status: active
  date_ymd: 2026-08-20
governance:
  canonicality: canonical
  visibility: public
title: intelligence-runtime
---

# intelligence-runtime

**intelligence-runtime** — общий механизм исполнения LLM-сценариев DETai. Его
[самостоятельный репозиторий](https://github.com/DETai-org/intelligence-runtime)
соединяет правила продуктов с моделями: организует последовательность шагов,
выбирает функциональные роли моделей, выполняет технические проверки, повторы
и трассировку.

Система не принадлежит Storytelling или любому другому одному продукту. Каждый
продукт остаётся владельцем собственного смысла, структуры данных, правил и
границы human review.

## Проектные проекции

Внутри репозитория есть структура `projects/<project>`. Название папки
совпадает с подключаемым продуктом, но сама папка не является копией продукта
и не превращает его в инфраструктурный проект. Это **проектная проекция** —
технический взгляд intelligence-runtime на конкретное подключение.

Проекция может содержать:

- порядок шагов LLM-сценария;
- model roles и привязки к providers;
- технические prompts и adapters;
- retries, validators и tests;
- ссылку на owning repository продукта.

Общая техника переносится в `shared/` только тогда, когда действительно
используется несколькими проекциями. Так runtime остаётся общим, а продуктовый
смысл не дублируется.

## Связь с DETai Nexus

[DETai Nexus](../home-lab/index.md) — одна из сред, где intelligence-runtime
исполняется. В текущей архитектуре Nexus хранит и обслуживает локальные LLM,
inference runtime и изменяемое состояние запусков. Репозиторий
intelligence-runtime хранит исполняемую логику и versioned-конфигурацию, но не
веса моделей и не runtime-cache.

Конкретные семейства моделей, их количество и распределение ролей могут
меняться. Они не определяют смысл intelligence-runtime и поэтому не
фиксируются на этой канонической странице.
