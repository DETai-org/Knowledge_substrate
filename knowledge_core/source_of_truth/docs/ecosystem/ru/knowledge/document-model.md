---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: knowledge-system
  layer: technical-standards
  function: standard
  system: knowledge
  domain: document-model
  audiences: [team, editors, developers, agents]
descriptive:
  id: knowledge-document-model
  version: v2
  status: active
  date_ymd: 2026-08-05
governance:
  canonicality: canonical
  visibility: public
  owner_role: knowledge-architect
  approver_role: ecosystem-architect
  review_date: 2026-08-20
links:
  external_links: []
  document_links:
    - schema: ecosystem
      link_type: part-of
      linked_document_id: knowledge-system-index
title: Модель документа и видимая функция
---

# Модель документа и видимая функция

Навигация отвечает на вопрос «к какой системе относится знание?». Metadata отвечает на вопросы «что это за документ, насколько он обязателен, кому виден и кто за него отвечает?». Поэтому функция документа не должна определять верхний уровень меню.

## Два независимых измерения

**Принадлежность:** system, domain, layer и связи с объектами.

**Функция:** philosophy, principle, guide, explanation, standard, policy, reference, register, decision record или иной допустимый тип.

Философский текст может находиться внутри Governance; standard — внутри U.L.I.; guide — внутри Product–Market. Пользователь сначала выбирает предмет, а затем видит функцию.

## Документ и описываемый объект

Жизненный цикл документа и состояние описываемой сущности также независимы. Действующий документ может описывать гипотезу, прототип или approved target. Для этого используется [многомерная модель статуса объекта](object-status-model.md).

## Видимая карточка документа

На странице должны отображаться как минимум:

- функция;
- canonicality;
- status и version;
- visibility;
- owner role;
- дата обновления или следующего review;
- принадлежность к system / domain.
- при наличии `object_state`: архитектурный, реализационный, доказательный и visibility-статусы объекта.

Это представление генерируется из front matter и не требует дублировать служебные поля вручную в тексте.

## Каноничность

- `canonical` — обязательный источник определения или правила;
- `working` — используемая рабочая модель, открытая для изменения;
- `reference` — справочный материал или проекция другого источника;
- `historical` — сохранённый контекст, не выражающий текущую позицию.

`status: active` не означает автоматически `canonicality: canonical`.

## Обязательное поведение при изменении

Если меняются статус, версия, связи, владелец или следующий шаг, обновляются front matter и связанные реестры. Если документ заменяет прежний, связь `supersedes / superseded-by` должна быть явной.
