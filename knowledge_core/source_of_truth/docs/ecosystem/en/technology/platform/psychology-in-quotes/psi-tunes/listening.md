---
title: "ΨTunes — Listening"
description: "Listening, bookmarks, buffering and recovery from connection interruptions in ΨTunes."
lang: en
translation_of: /ru/technology/platform/psychology-in-quotes/psi-tunes/listening/
---

# Listening and saving moments

## Listen to a sample {#first-listen}

In ΨTunes, open **Catalog**, select a book or choose **DETai podcasts**, then open **Preview** when available. Press **Play** if prompted. If the app asks you to sign in or connect Telegram, follow the link in PiQ; the catalog listing does not grant full access.

## Save and find a bookmark {#bookmark}

In an item you can listen to, open **Listen** and select **Save a bookmark** in the full player. Open **Bookmarks** for that same book or episode to return to the saved position. A bookmark does not extend listening access.

[← ΨTunes](index.md)

ΨTunes links playback to a particular text edition and audio version. A chapter and an audio delivery segment can have different boundaries: switching between them should not require pressing Play again.

> **Status:** ΨTunes was released with PiQ 2.0. Background audio is subject to Telegram, WebView, device and network limitations; this is **not a promise of permanent offline playback**.

The player is designed for pause, speed control, seeking, chapters and saving your position. A one-tap **bookmark** stores a moment without requiring a comment; from it you can return to the book or create a quotation linked to its source.

During active playback the client tries to buffer a limited amount of upcoming audio. If the network drops, buffered content may continue playing. After it runs out, the player attempts to reconnect and resume. A manual pause or closing the player must not silently restart playback.

A message about the **audio service** being unavailable does not necessarily mean the device has no internet. A request to press **Play** can indicate that the browser requires a user gesture. Access expiry is separate from connection errors; bookmarks and progress stay associated with the edition. Your available options are shown in the product.

[Import](import.md) · [Podcasts](podcasts.md)
