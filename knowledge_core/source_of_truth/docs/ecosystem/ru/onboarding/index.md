---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: governance-operating-model
  layer: operating-model
  function: guide
  system: governance-operating-model
  domain: onboarding
  audiences: [candidates, team, managers, onboarding-coordinators, agents]
descriptive:
  id: onboarding-system
  version: v1
  status: draft
  date_ymd: 2026-08-14
governance:
  canonicality: working
  visibility: public
  owner_role: onboarding-coordinator
  approver_role: onboarding-owner
  review_date: 2026-09-14
object_state:
  architecture_status: hypothesis
  implementation_status: in-design
  evidence_status: preliminary-support
  visibility_status: public
links:
  external_links:
    - type: MkDocs_ru
      url: https://detai-org.github.io/Knowledge_substrate/ru/onboarding/
    - type: GitHub
      url: https://github.com/DETai-org/onboarding
  document_links:
    - schema: ecosystem
      link_type: implements
      linked_document_id: meaningful-participation
    - schema: ecosystem
      link_type: part-of
      linked_document_id: management-layer-2-architecture-and-logic-operating-model-detai
title: Onboarding DETai
---

# Onboarding DETai

!!! warning "Черновик для review"

    Архитектура раздела восстановлена из рабочих материалов и ожидает проверки ответственного за onboarding. До согласования страницы имеют статус `draft` и не задают окончательный регламент.

## Назначение

Onboarding — путь перехода человека от первого знакомства с DETai к осмысленному участию в экосистеме. Он помогает последовательно понять смысл и устройство системы, освоить её знания и инструменты, определить возможную роль и сделать первый реальный вклад.

Это не единый список обязательных действий и не только ввод в должность. Маршрут соединяет самостоятельное изучение, живые встречи, практику, обратную связь и постепенное расширение ответственности.

## Карта раздела

| Документ | Что в нём находится |
|---|---|
| [Путь участника](onboarding-path.md) | четыре этапа onboarding, их продолжительность, содержание и ожидаемые результаты |
| [Контуры знаний и исполнения](execution-contours.md) | роли Knowledge Substrate, GitHub, Issues, ClickUp и локальной среды Codex |
| [Сопровождение и развитие](coordination-and-evolution.md) | роль onboarding-координатора, обратная связь, сезонные итерации и архивирование маршрута |

## Четыре этапа

| Этап | Что формируется | Ориентировочная продолжительность |
|---|---|---|
| **0. Pre-Onboarding** | взаимный интерес, резонанс и готовность продолжить знакомство | 3–5 дней |
| **1. Organizational Onboarding** | общее понимание философии DET и архитектуры DETai | 2 дня |
| **2. Knowledge Immersion** | самостоятельная ориентация в знаниях и возможных ролях | 2–4 недели |
| **3. Tooling Integration + Ownership** | уверенная работа с инструментами и первый осмысленный вклад | 4–8 недель |

Полная логика и границы этапов описаны в [пути участника](onboarding-path.md). Конкретные tutorial-задачи могут меняться между итерациями и поэтому живут не на этой странице, а в рабочих контурах onboarding.

## Для кого этот раздел

- Новый участник использует раздел как карту пути и понимает, что будет происходить дальше.
- Сопровождающий видит назначение этапов и не подменяет прохождение участника ручным управлением.
- Onboarding-координатор поддерживает связность маршрута, собирает обратную связь и готовит следующую итерацию.
- Management Layer согласует маршрут с ролями, доступами и действующим Operating Model.

Для первого входа начните с [пути участника](onboarding-path.md), затем откройте [контуры знаний и исполнения](execution-contours.md).
