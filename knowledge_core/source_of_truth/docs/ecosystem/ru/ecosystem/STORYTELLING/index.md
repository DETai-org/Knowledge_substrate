---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: brand-and-communications
  layer: operating-model
  function: project
  system: governance-operating-model
  domain: storytelling
  audiences: [team, brand, authors, developers, agents]
descriptive:
  id: storytelling-index
  version: v5
  status: active
  date_ymd: 2026-03-25
  date_update: 2026-09-23
governance:
  canonicality: canonical
  visibility: public
  owner_role: brand-communications-owner
  approver_role: founder
  review_date: 2026-10-23
object_state:
  architecture_status: canonical
  implementation_status: operational
  evidence_status: not-applicable
  visibility_status: public
links:
  external_links:
    - type: MkDocs_ru
      url: https://docs.detai-x.com/ru/ecosystem/STORYTELLING/
    - type: GitHub
      url: https://github.com/DETai-org/Storytelling
  document_links:
    - schema: ecosystem
      link_type: part-of
      linked_document_id: brand-and-communications-domain
    - schema: ecosystem
      link_type: published-through
      linked_document_id: detai-platform-detai-e2-brand-sites-index
    - schema: ecosystem
      link_type: interfaces-with
      linked_document_id: team-os-contribution-ledger
title: Storytelling — Publication Core
---

# Storytelling — Publication Core

**Storytelling — самостоятельный редакционно-технологический проект DETai и центр подготовки публикаций с [собственным репозиторием](https://github.com/DETai-org/Storytelling). Он помогает пройти путь от исходного материала до согласованной публикации для сайта, Telegram и других площадок.**

Storytelling относится к направлению [«Бренд и внешние коммуникации»](../DETai/Platform_DETai/brand-and-external-communications/index.md) и является его внутренней производственной системой. Пользователь видит результат работы Storytelling уже на публичной площадке — например, на сайте или в Telegram.

## Место в публикационном процессе

| Уровень | Роль |
|---|---|
| **Редакционная рабочая среда** | Идея, черновик, обсуждение, автор и подготовка исходного материала |
| **Storytelling / Publication Core** | Подготовка текста и метаданных, обогащение материала, переводы, проверка человеком и подготовка к публикации |
| **Представление для площадки** | Отдельная версия одного материала для сайта, Telegram или другого канала |
| **Публичная площадка** | Сайт, Telegram и будущие B17, Instagram, YouTube или другие каналы |
| **Долговременное хранение** | Системы, которые сохраняют опубликованный результат после завершения работы Storytelling |

Текущей операционной точкой передачи исходного материала остаётся папка ClickUp [STORYTELLING (TimeOS) для текстов](https://app.clickup.com/90152202658/v/f/901515038276/901510140866). Это действующий вход в процесс, а не постоянная техническая зависимость.

## Мозаичная архитектура

Storytelling следует [мозаичному подходу DETai](../DETai/U.L.I/3_Technical_Standards/mosaic-approach.md): крупный процесс разделён на самостоятельные части, которые можно менять и развивать отдельно.

Например, одна и та же публикация может иметь отдельную версию для сайта и отдельную версию для Telegram. Внутри Telegram-версии отдельно задаются общая стратегия подготовки, формат сообщения и дополнительные возможности оформления. Благодаря этому изменение Telegram не должно случайно менять публикацию на сайте, а подключение новой площадки не требует перестраивать весь процесс.

## Full Publication и канонический материал

В процессе Full Publication основной полный вариант материала готовится для сайта. На его основе Storytelling может подготовить отдельную Telegram-версию, приспособленную к возможностям и ограничениям этой площадки.

Для человека это всё ещё одна публикация, но версии для разных площадок не обязаны быть технически одинаковыми. Они связаны общим содержанием и редакционным решением, при этом каждая площадка получает собственное представление материала.

В дальнейшем Storytelling может работать не только со статьями. Например, отдельным типом материала может быть событие: обновление одного из проектов [Platform DETai](../DETai/Platform_DETai/index.md), месячный отчёт об итогах работы команды, появление нового участника или другая новость экосистемы. Такие материалы могут появляться на сайте в [разделе новостей](https://detai-x.com/r/events) и одновременно получать отдельную Telegram-версию.

## Publication Workspace: процесс, а не архив

Пока публикация готовится, Storytelling хранит её рабочее состояние: актуальную версию материала, варианты для разных площадок, результаты согласования, рабочие изображения и сведения о попытках публикации.

Это нужно, чтобы после сбоя можно было продолжить работу с правильного места и не отправить один материал повторно. После завершения публикации Storytelling не должен превращаться в постоянный архив всего опубликованного корпуса: долговременное хранение результата относится к системам, для которых этот результат предназначен. Например, историю уже опубликованного материала может сохранять Архивариус.

## Telegram: подготовка и отправка публикации

Storytelling отвечает за то, **что именно должно быть опубликовано в Telegram, в каком виде и после чьего подтверждения**. Сам [проект Telegram](../DETai/Platform_DETai/E2-Brand/Telegram/index.md) отвечает за техническую сторону работы с Telegram-аккаунтами: их авторизацию, доступность и выполнение действий от их имени.

Обычные публикации и большинство расширенно оформленных сообщений можно отправлять через бота. Если публикация использует оформление, которое Telegram разрешает только пользовательскому Premium-аккаунту, Storytelling выбирает подходящий доступный аккаунт для отправки.


### Настройки отправки

К этому же Telegram-контуру относятся настройки, которые определяют способ технической отправки — например, через бота или подходящий пользовательский аккаунт. Они не меняют уже согласованный материал, а только определяют, каким доступным способом он будет опубликован.

## Связь с сайтом

[Сайт DETai](../DETai/Platform_DETai/E2-Brand/sites/index.md) — основная публичная web-поверхность для полных публикаций. Storytelling готовит материал и его данные для публикации, а проект `sites` превращает их в web-страницу и публикует её. Подробнее разделение ролей описано в разделе [«Связь со Storytelling и Brand & Communications»](../DETai/Platform_DETai/E2-Brand/sites/index.md#связь-со-storytelling-и-brand-communications).

## Технологическая основа

Storytelling использует общие технические системы DETai, но не передаёт им управление редакционным процессом. Например, Intelligence Runtime помогает выполнять AI-шаги, Telegram выполняет действия в Telegram, а Sites отвечает за web-публикацию. Подробно это разделение объяснено на странице [«Как Storytelling использует технологическую основу»](technology-foundation.md).

## Рабочее состояние и управление

Текущие задачи, сроки и Work Packages живут в ClickUp и management runtime. Эта страница фиксирует устойчивую модель Storytelling и его системные границы, а не текущий план разработки.
