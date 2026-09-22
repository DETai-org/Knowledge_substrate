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

[Storytelling](index.md) отвечает за сам публикационный процесс: как из исходного материала получается согласованная публикация и какие версии этой публикации нужны для разных площадок. Другие технические системы DETai помогают выполнить отдельные части этой работы, но не определяют содержание и редакционные решения Storytelling.

## Intelligence Runtime

Когда Storytelling использует AI для обогащения текста, перевода или другой обработки материала, он задаёт цель и правила результата. [intelligence-runtime](../Infrastructure/intelligence-runtime/index.md) выполняет техническую работу с моделями: запускает нужные шаги, проверяет формат ответа и при необходимости повторяет неудачную попытку.

Проще говоря, **Storytelling определяет, что нужно получить, а Intelligence Runtime помогает технически получить этот результат от моделей**. Финальное редакционное решение и подтверждение материала остаются внутри процесса Storytelling.

## Sites

После того как web-версия публикации подготовлена и согласована, Storytelling передаёт её проекту сайта. Дальше `sites` отвечает уже за то, чтобы материал стал web-страницей и корректно работал на сайте.

Подробно граница между подготовкой публикации и работой самого сайта описана в разделе [«Связь со Storytelling и Brand & Communications»](../DETai/Platform_DETai/E2-Brand/sites/index.md#связь-со-storytelling-и-brand-communications). Здесь важно только разделение ответственности: Storytelling готовит публикацию, а `sites` публикует её в web-среде.

## Telegram

Связь Storytelling с Telegram уже описана на основной странице проекта в разделе [«Telegram: подготовка и отправка публикации»](index.md#telegram-подготовка-и-отправка-публикации). Здесь достаточно зафиксировать общий принцип: Storytelling определяет публикационный результат, а [проект Telegram](../DETai/Platform_DETai/E2-Brand/Telegram/index.md) предоставляет техническую возможность его отправить.

## Nexus и среда исполнения

[DETai Nexus](../Infrastructure/home-lab/index.md#detai-nexus-как-среда-исполнения) — одна из сред, где могут работать технические компоненты Storytelling и связанных систем. Проще говоря, это место, где часть программ может быть запущена в реальной эксплуатации.

При этом Nexus не определяет правила Storytelling и не становится владельцем публикационного процесса. Если компонент позже будет перенесён на другую машину или сервер, смысл и логика Storytelling должны остаться теми же.

Главный принцип простой: **Storytelling определяет содержание и ход публикационной работы, а общая инфраструктура помогает технически выполнить отдельные шаги.**
