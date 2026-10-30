---
title: "Psychology in Quotes — Architecture and Trust"
description: "How PiQ fits into DETai and how its accounts, API, privacy and publishing responsibilities are separated."
lang: en
translation_of: /ru/ecosystem/DETai/Platform_DETai/products/psychology-in-quotes/architecture-and-trust/
---

# How the product works and what makes it trustworthy

## Where PiQ fits within DETai

- **DETai** is an ecosystem spanning psychotherapy, research, education, technology and community.
- **Platform DETai** is its product-and-technology layer and connected digital environment.
- **Psychology in Quotes** is a digital education and knowledge-sharing product (its primary user function), with publishing and creative work as additional functions. Its **E2 Brand** role is to spread psychological knowledge and strengthen awareness and trust.
- **DETai Account** provides a shared identity across the website and linked Telegram, but registration alone does not confer rights to other people's quotes.

[DETai ecosystem](../../../index.md) · [Platform DETai](../../index.md) · [PiQ product page](https://detai-x.com/en/technology/platform/psychology-in-quotes).

## Two independent dimensions of positioning

| Question | PiQ's answer |
| --- | --- |
| What value does a person receive? | Self-directed education through psychological ideas, reading and meaningful preservation of quotations |
| What else can they do? | Create quote cards and Stories, publish and share material |
| What is its main contribution to DETai? | Knowledge dissemination, trust and recognition — **E2 Brand** |
| What does PiQ not promise? | A formal educational programme, certification, diagnosis or psychotherapy |

This distinction is defined in the [product object model](../../../../../product-market/product-object-model.md) and the [echelon model](../../../logic-of-echelons.md). An educational user function does not automatically reclassify a project as E1.

## Separation of responsibilities

| Surface | Responsible for | Not a source of |
| --- | --- | --- |
| Website `detai-x.com` | Public presentation, web account, quotes, catalogue, SEO and legal documents | Independent plan entitlements or a private SQL database |
| PiQ Telegram bot | Quote creation wizard, collections, interactions and publishing | Separate commercial rules or DETai Account registration |
| DETai Hub | Choosing to create or connect an Account, verifying Telegram linkage and managing Hub's language | Independent PiQ Accounts or its plan entitlements |
| PiQ API and product server policy | Quote obtain rights, current plans, quotas, statuses, PNG readiness and public addresses | Policies governing the whole ecosystem |
| Knowledge Substrate | Public definitions, instructions, documentation links and standards | A live user database, secrets or payment checkout |
| DETai Account / Identity | Linking a person's identity between products | Automatically obtaining quotes |

**How the handoff works:** PiQ sends Hub the purpose (“create or connect an Account”) and a hint about interface language. Hub first checks whether Telegram is linked to a shared DETai Account. If so, it displays that account; otherwise, it offers account creation in Telegram or connection to an existing website account through a verified link. Hub's previously saved language preference is preserved. The handoff does not create an Account automatically or grant Plus/Pro.

The shared [language-handoff rules](https://docs.detai-x.com/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/Telegram_Bots/language-handover/) and [configuration standard](https://docs.detai-x.com/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/Telegram_Bots/configuration-standard/) are documented separately (currently in Russian). This page explains the product's user-facing boundaries, not internal development procedures.

This documentation describes **stable user-facing principles and responsibilities**. Internal work-in-progress files and operational settings are not part of the public guide.

## Quote content and provenance

A quote is more than a picture. It has a persistent `quoteId`, the author of the quoted words, a bibliographic source, text and revision, the language of the submitted passage and, when known, the original work, plus prepared translations, images, verification and publishing states.

**The author of the quoted words ≠ the card creator ≠ necessarily the author of the original source work.** Metadata is entered only on the basis of verified sources; AI translations may contain errors. Translation readiness, image preparation and authorisation for publication are separate states.

[Attribution and usage rules](https://detai-x.com/en/technology/platform/psychology-in-quotes/terms).

## Privacy and boundaries of use

- Drafts and “My quotes” are private by default. Inclusion in the catalogue requires a publishing procedure.
- Public previews of other people's images remain watermarked.
- Obtaining a quote grants an **entitlement within PiQ**, not copyright in the literary work.
- PiQ does not provide psychotherapy or diagnostic services.
- Account data, technical events and connected services are governed by the [product's privacy notice](https://detai-x.com/en/technology/platform/psychology-in-quotes/privacy).
- To protect personal information, do not include private quote text, tokens or health information in public support pages or requests to external AI.

## For support teams and AI agents

**Support route:** [getting started](getting-started.md) → [entitlement model](collection-and-plans.md) → [common issues](help-and-troubleshooting.md) → [current PiQ product page](https://detai-x.com/en/technology/platform/psychology-in-quotes). This does not authorise operations on behalf of an unverified user.

When answering a screenshot, an AI assistant must distinguish what the documentation establishes, what the screen actually shows and what cannot be established without the current Account or backend. Do not guess about payments, entitlements, why a PNG is missing or whether sending succeeded.

**Updated:** 30 October 2026. **Availability:** production pilot; Telegram Stars is available only within a closed pilot, not for public purchases. Binding legal terms and dynamic limits always prevail over outdated copies of user guidance.

[← Overview](index.md) · [Collection and plans](collection-and-plans.md)
