---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: ecosystem-architecture
  layer: architecture-and-logic
  function: reference
  system: architecture
  domain: source-of-truth
  audiences: [team, agents]
descriptive:
  id: source-of-truth-map
  version: v2
  status: active
  date_ymd: 2026-08-05
governance:
  canonicality: canonical
  visibility: public
  owner_role: knowledge-architect
  approver_role: founder
  review_date: 2026-09-05
links:
  external_links: []
  document_links:
    - schema: ecosystem
      link_type: routes
      linked_document_id: ecosystem-canon
    - schema: ecosystem
      link_type: implemented-by
      linked_document_id: detai-representation-model
title: Карта источников истины
---

# Карта источников истины

## Основные формы

| Форма | Что хранит | Где живёт |
|---|---|---|
| Canonical definition | Сущность, правило, policy, standard и связи | Knowledge Substrate |
| Operational state | Задачи, назначения, сделки, метрики, состояние продукта | Management Layer, Team OS, CRM, product runtime |
| Restricted evidence | Оригиналы договоров, finance, personal data, DPIA и raw evidence | Corporate Vault и защищённые product systems |
| Public interpretation | Понятное объяснение, визуализация, продукт и CTA | основной сайт |
| Narrative source | Происхождение, аргументация и человеческий смысл | книга и авторский репозиторий |
| Role view | Отобранный путь по каноническим объектам для конкретной ответственности | маршруты по ролям и рабочая среда |

Формы не образуют иерархию «короткая — полная». Каждая отвечает на собственный вопрос и ссылается на канонический объект. Подробные правила описаны в [модели представлений](../knowledge/representation-model.md).

## По доменам

| Знание | Канон | Runtime / evidence | Публичная проекция | Книга |
|---|---|---|---|---|
| Архитектура | `/ru/architecture/` | decision records | карта DETai | часть III |
| Метод | `/ru/method/` | research/professional systems | страницы DET | часть II |
| Технология | `/ru/technology/` | U.L.I. и product repos | Platform/U.L.I. | части I и III |
| Governance | `/ru/governance/` | decisions и role assignments | governance overview | часть III |
| Product–Market | `/ru/product-market/` | CRM, pilots, analytics | products/offers | часть III и приложения |
| Legal–Economic | `/ru/legal-economic/` | Corporate Vault | company/legal pages | датированный контекст |
| Trust | `/ru/trust/` | assurance, incidents, vendors | Trust Center | этическая аргументация |
| Evidence | `/ru/evidence/` | registers и snapshots | public evidence | источники и ограничения |
| Knowledge | `/ru/knowledge/` | publication pipeline и agent indexes | поисковые и навигационные входы | цифровая архитектура книги |

## Правило синхронизации

1. Решение фиксируется в каноническом домене.
2. Реализующая система хранит ссылку на применяемую версию.
3. Публичное представление не расширяет claim самостоятельно.
4. Изменение downstream возвращается в канон только через review.
5. Историческая версия не удаляется, а получает статус `historical` или `superseded`.
6. Ролевой маршрут не копирует документ, а связывает его стабильный ID и канонический адрес.
