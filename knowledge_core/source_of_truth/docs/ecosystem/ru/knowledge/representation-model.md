---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: knowledge-system
  layer: architecture-and-logic
  function: standard
  system: knowledge
  domain: representation-model
  audiences: [public, team, editors, agents]
descriptive:
  id: detai-representation-model
  version: v1
  status: active
  date_ymd: 2026-08-05
governance:
  canonicality: canonical
  visibility: public
  owner_role: knowledge-architect
  approver_role: ecosystem-architect
  review_date: 2026-09-05
object_state:
  architecture_status: canonical
  implementation_status: in-design
  evidence_status: not-applicable
  visibility_status: public
links:
  external_links: []
  document_links:
    - schema: ecosystem
      link_type: implements
      linked_document_id: source-of-truth-map
    - schema: ecosystem
      link_type: governs
      linked_document_id: knowledge-publication-delivery
title: Модель представлений DETai
---

# Модель представлений DETai

Одна идея может присутствовать на сайте, в Knowledge Substrate и книге. Это не дублирование, если у каждого представления своя интеллектуальная функция, а канонический источник и статус остаются явными.

## Функции основных сред

| Среда | Главная функция | Что человек должен получить | Что там не хранится как источник истины |
|---|---|---|---|
| Основной сайт | объяснить, показать, заинтересовать и направить | ясный образ целого, продукты, люди, визуальные связи и следующий шаг | полные policies, runtime-state и неподтверждённые claims |
| Knowledge Substrate | определить, разграничить, связать и версионировать | канон, статусы, owners, policies, standards, safe summaries и маршруты | задачи, персональные данные, договорные оригиналы и raw runtime |
| Книга | раскрыть происхождение, аргументацию и человеческий смысл | последовательное понимание, исторический контекст и narrative целого | текущие назначения, cap table, CRM и быстро меняющиеся требования |
| Management runtime | организовать исполнение | приоритеты, задачи, owners, сроки, decisions и progress | конкурирующие определения архитектуры |
| Product/runtime systems | исполнять продукт и хранить его состояние | пользовательский результат, техническая и операционная реальность | общая философия экосистемы как копия |
| Corporate Vault | хранить ограниченные оригиналы | юридически и финансово значимые records | публичная интерпретация |

## Правило трёх публичных форм

Для значимой темы допускаются три связанные версии:

1. **сайт** — краткий смысл, визуализация, актуальное обещание и переход глубже;
2. **документация** — определение, границы, статус, владелец, связи и безопасная детализация;
3. **книга** — почему эта сущность возникла, какую проблему решает и что означает для человека и психотерапии.

Текст может совпадать дословно, если функция фрагмента действительно одинакова. Однако полные страницы не копируются автоматически: меняются контекст, глубина, доказательная нагрузка и срок жизни.

## Переходы

- сайт ссылается на каноническое объяснение, evidence или подробную пользовательскую документацию;
- Knowledge Substrate ссылается на публичную витрину, owning runtime и книжный раздел, когда он опубликован;
- книжный чанк ссылается на датируемые цифровые досье для изменяемых сведений;
- агент использует stable ID и `document_links`, а не только URL или похожий заголовок.

## Видимость решений

Актуальное решение формулируется на основной странице системы. Decision record хранит контекст, альтернативы и основания, но не является обязательным тайным маршрутом к действующей позиции. Открытая гипотеза маркируется как гипотеза во всех представлениях.
