---
type: ecosystem
classification:
  scope: Infrastructure
  context: ecosystem-runtime
  layer: architecture-and-logic
  function: explanation
  domain: commerce
  audiences: [public, team, product, developers, agents]
descriptive:
  id: infrastructure-commerce-core
  version: v2
  status: draft
  date_ymd: 2026-11-02
  date_update: 2026-11-13
governance:
  canonicality: working
  visibility: public
links:
  external_links:
    - type: MkDocs_ru
      url: https://docs.detai-x.com/ru/company-and-economy/commerce-core/
  document_links:
    - schema: ecosystem
      link_type: part-of
      linked_document_id: infrastructure-ecosystem-runtime
    - schema: ecosystem
      link_type: related-to
      linked_document_id: company-economy-index
title: Commerce Core
---

# Commerce Core

**Commerce Core — единый технический центр коммерческих операций DETai.**
Он связывает предложения разных продуктов с заказами, подтверждёнными платежами,
подписками и возвратами. Единые контракты позволяют продуктам работать
с разными способами оплаты через общий коммерческий контур.

## Место в архитектуре

Техническая реализация Commerce Core — часть
[ecosystem-runtime](../infrastructure/ecosystem-runtime/index.md), общей системы
[Infrastructure](../infrastructure/index.md). Здесь находятся серверная логика,
платёжные интеграции и работа с коммерческими данными.

Связь технической работы и экономической стороны коммерческой деятельности
показана в [таблице разделения ответственности](../management-layer/index.md#разделение-ответственности).

## Идентичность, коммерческие факты и доступ

- `identity` определяет пользователя;
- `commerce` хранит коммерческие факты;
- `access` хранит основания доступа;
- соответствующий продукт определяет доступные пользователю возможности и ограничения.

Способ оплаты не меняет принадлежность продукта и его правил.

## PsyTok и услуги продуктов

[PsyTok](psytok.md) — единая расчётная единица для подключённых услуг экосистемы.
Общий баланс связан с DETai Account; включённые начисления сохраняют ограничения
своего тарифа. Коммерческий контур учитывает приобретение, резервирование,
списание и освобождение средств. Продукт определяет приобретаемый результат
и правила доступа, включая допустимое использование уже подготовленного материала.

## Финансовый вклад и учёт

Финансовый вклад продуктов — часть общей
[модели ресурсов экосистемы](../management-layer/ecosystem-resources.md),
находящейся в Management Layer. Учёт коммерческих событий не заменяет
бухгалтерский учёт и юридическое оформление обязательств.
