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
  version: v4
  status: draft
  date_ymd: 2026-11-02
  date_update: 2026-11-27
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
- `access` задаёт границу общих прав;
- соответствующий продукт определяет доступные пользователю возможности и ограничения.

Способ оплаты не меняет принадлежность продукта и его правил. Пользовательский взгляд на платёжные операции и сохранённые кошельки собран в [разделе DETai Account](../technology/platform/detai-account/payments.md). Привязка публичного адреса хранится в Identity; подтверждённый платёж относится к Commerce.

## PsyTok и услуги продуктов

[PsyTok](psytok.md) — единая расчётная единица для подключённых услуг экосистемы.
Общий баланс связан с DETai Account; включённые начисления сохраняют ограничения
своего тарифа. Коммерческий контур учитывает приобретение, резервирование,
списание и освобождение средств. Продукт определяет приобретаемый результат
и правила доступа, включая допустимое использование уже подготовленного материала.

## Как пользоваться этой справкой

Документ описывает **общий технический контур** и его границы. Он не является актуальным прайсом, подтверждением открытия продаж или сведениями о состоянии конкретного заказа.

| Вопрос | Источник |
| --- | --- |
| Что такое PsyTok и как устроены балансы | [PsyTok](psytok.md) |
| Как PsyTok используется в продукте | [Psychology in Quotes](../technology/platform/psychology-in-quotes/index.md) |
| Как приобретать и использовать книги | [ΨTunes](../technology/platform/psychology-in-quotes/psi-tunes/index.md) |
| Какие сейчас доступны цены и способы оплаты | [Действующее предложение PiQ](https://detai-x.com/ru/technology/platform/psychology-in-quotes) перед подтверждением заказа |

Для человека или AI-ассистента важно различать **архитектурную модель**, **готовящуюся возможность** и **фактически доступную покупку**. Документация не заменяет проверку актуальных условий в продукте.

## Финансовый вклад и учёт

Финансовый вклад продуктов — часть общей
[модели ресурсов экосистемы](../management-layer/ecosystem-resources.md),
находящейся в Management Layer. Учёт коммерческих событий не заменяет
бухгалтерский учёт и юридическое оформление обязательств.
