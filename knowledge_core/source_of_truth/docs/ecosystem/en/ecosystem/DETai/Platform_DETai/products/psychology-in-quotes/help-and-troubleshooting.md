---
title: "Psychology in Quotes — Help and Troubleshooting"
description: "How to interpret PiQ screens, guest cards, watermarks, language rights and publication status."
lang: en
translation_of: /ru/ecosystem/DETai/Platform_DETai/products/psychology-in-quotes/help-and-troubleshooting/
---

# Questions, statuses and troubleshooting

This guide is for people and external AI assistants reviewing a PiQ screenshot. First establish which screen, button label, plan and exact status are involved. **Do not infer ownership of a quote from its image or watermark alone.**

## If you share a screenshot: identify the user's state

These steps also apply to GPT/AI support assistants. Do not guess the user's status from the card's colour, Telegram username or a single watermark.

1. **Surface:** the website (public catalogue or personal account area) or the PiQ Telegram bot. Someone can be signed in on the website but **not have linked Telegram** to their DETai Account.
2. **Identity:** Public means a guest without a verified shared Account; Free means someone with a shared Account and baseline access; Plus/Pro means the same participant with an extended subscription. Project administrator roles, service grants and the currently active plan are checked separately. If uncertain, ask the user to open “My subscription” — never request credentials.
3. **Object:** public catalogue, guest card/draft, “My quotes”, “Acquired”, “Favorites” and “My publications” are different data categories. Bookmarking a quote does not confer access to its clean image.
4. **Intent:** is the user trying to read, save, obtain a PNG, submit for review or publish to a channel? A published quote can be read without an Account; permanent results and quota-consuming operations require verified entitlements.
5. **Status and language:** inspect the displayed status, interface language, displayed edition language, submitted passage language, media readiness and authorisation. Changing interface language does not grant a clean-file entitlement.
6. **Next action:** suggest one specific button or navigation path. If linking is needed, explain registration and the separate Telegram connection. Do not promise instant publication or recovery of expired guest data.

[Visual comparison of Public and Account](https://detai-x.com/en/technology/platform/psychology-in-quotes#piq-access) · [Getting started](getting-started.md) · [Plans and limits](collection-and-plans.md).

**Availability:** check the running bot for guest features and restrictions, and [the website for Free / Plus / Pro limits](https://detai-x.com/en/technology/platform/psychology-in-quotes#piq-plans). When the documentation and interface differ, follow the current product state.

## Link DETai Account and Telegram without creating a second account

In a PiQ invitation, select **“Open DETai Hub”**. If Telegram is already linked to a DETai Account, Hub will show the existing account. Otherwise, it offers account creation in Hub or connection to an account already registered [on the website](https://detai-x.com/en/account), through “Connect Telegram” and a one-time link. **Opening Hub or signing in on the website does not, by itself, link Telegram.** When you return to PiQ, your next normal action checks the link automatically. You can also select “Check connection” to refresh the screen.

On handoff, Hub uses the PiQ language only when it has no saved preference. If the unexpected language appears, change it inside Hub; this does not affect quote or translation languages. See the [step-by-step guide](getting-started.md).

## What does a guest card mean, and when does it expire?

**Public:** a temporary result associated with a verifiable Telegram ID, **not** a permanent quote in the ecosystem Account. Guest cards, renders, favourites and retention are subject to limits shown in the bot. [Free / Plus / Pro plan conditions](https://detai-x.com/en/technology/platform/psychology-in-quotes#piq-plans) are published separately on the website. Guest images have a watermark and are not yet editorially reviewed. Sending a PNG to a private chat **is not the same as** publishing it to a Telegram channel or the public catalogue.

**If you see “Draft”:** choose “Continue creating” instead of making a second draft. **If the card is ready:** check its expiry and the option to save through an Account. **If it has expired:** do not expect recovery of the original guest data; a new guest cycle may be available. **If an Account was just linked:** check transfer and moderation status; saving your own record and receiving public publication approval are separate things.

**Notifications:** one-off product reminders may be sent before expiry or when a new cycle opens, subject to the agreed policy. Failed Telegram delivery or blocking the bot does not imply that data is deleted immediately. Retention TTL and the ability to opt out of proactive notifications still apply.

## What do the collection sections mean?

**My quotes** are authored by the user; **Obtained** contains other people's catalogue quotes obtained under their Account; **Favorites** are bookmarks; **My publications** records sends. The same quote may appear in several sections for different reasons.

[More about collection terminology](collection-and-plans.md#piq-collection-terms).

## My quote image is not available yet {#piq-image-not-ready}

**Meaning:** the quote text and source have been saved in PiQ, but the *current revision* does not have a confirmed, ready PNG. Other quotes in a carousel may still be accessible.

**Next step:** open “My collection” → “My quotes”, inspect the `1/N` counter and swipe through the cards. Select “Check status”. If the system genuinely offers to resume an **unfinished draft**, complete it.

**Avoid:** recreating the same quote; assuming that simply waiting will help when the rendering job was never started; using an old revision's PNG as if it were current.

**When to ask for help:** if neither a PNG nor a recovery action is available, contact support with the quote ID, time and exact status label — not your account secrets.

## Why does my image say PREVIEW or have a watermark?

**Catalogue:** public previews of other people's quotes deliberately have watermarks. Merely having a DETai Account does not remove them.

**Obtained:** after obtaining a quote is confirmed, you may download a clean file in an authorised language. On Free, this is limited to the selected language and any previously retained historical language entitlements.

**My quotes:** a verified owner with an Account may view the ready PNG of their own quote without a watermark, even on Free. A guest's trial card remains watermarked when the guest editor is available. If “My quotes” still shows PREVIEW on the website, check whether an authenticated version is available; do not obtain your own quote again.

[Obtaining rules](collection-and-plans.md).

## Why won't Language open a translation?

**Meaning:** on Free, clean versions are restricted to the selected language. Plus/Pro provide only additional languages whose files are prepared and authorised. The interface language does not affect obtain rights.

**Next step:** check “My subscription” and the translation's status. If a version is still being prepared, do not obtain the quote again. It becomes available after preparation and authorisation. You may still be able to preview it with a watermark.

## Why wasn't my publication sent?

**Meaning:** a send may be `pending`, `failed`, `cancelled`, `uncertain` or confirmed successful.

**Next step:** go to “My publications” → “Check result”. Verify that the channel is connected, the material is approved, another person's quote has already been obtained, and you have sufficient limits.

**Avoid:** retrying blindly when the status is `uncertain`. Checking the result must not trigger a second send.

## Why isn't my quote in the public catalogue?

Saving your own quote **does not automatically publish it publicly**. Review and preparation of language editions and images can take time. Pro has a trusted-approval path but does not guarantee instant publication without preparation.

## Why did my capabilities change after a subscription change?

Obtained quotes do not disappear when a plan is downgraded. Access to additional prepared languages, channels and functions may decrease. Check your entitlements and limits in “My subscription”. [Current website comparison](https://detai-x.com/en/technology/platform/psychology-in-quotes#piq-plans).

## How to ask an AI assistant for help without sharing sensitive data

You can share **a screenshot of the error and a link to this guide**, saying “I'm in … and see the message …”. Confirm current status in the live product; documentation can lag behind its interface.

**Do not share:** passwords, tokens, cookies, authorisation codes, account recovery links, private third-party texts or health information. An external AI assistant without authorised access can explain the interface but cannot verify entitlements, make a payment or change your Account.

Support contact: **detai.founder@gmail.com**. [Privacy](https://detai-x.com/en/technology/platform/psychology-in-quotes/privacy).

[← Overview](index.md) · [Architecture and trust →](architecture-and-trust.md)
