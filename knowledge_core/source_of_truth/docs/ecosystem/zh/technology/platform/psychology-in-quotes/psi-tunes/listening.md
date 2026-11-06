---
title: "ΨTunes — 收听"
description: "ΨTunes — 图书与播客 — product guide (in development)."
lang: zh
translation_of: /ru/technology/platform/psychology-in-quotes/psi-tunes/listening/
---

# 收听与保存重要片段

[← ΨTunes](index.md)

ΨTunes 将播放进度绑定到指定文本和音频版本。章节与传输音频片段的边界可能不同；正常切换时不应需要重新点击 Play。

> **状态：**后台播放受到 Telegram、WebView、设备及网络环境的影响。本说明**不承诺永久离线播放**。

播放器的设计包括暂停、速度调整、跳转、章节目录和保存播放位置。**书签**可以一键保存时刻，无须填写评论；之后可返回书中位置，或创建附带来源的引文。

收听期间，应用会尝试预加载有限量的后续音频。网络短暂中断时，缓冲中的内容可能继续播放；缓冲耗尽后，播放器会尝试恢复连接并从保存的位置继续。用户主动暂停或关闭后，不应自动重新播放。

**音频服务**暂时不可用并不代表设备没有互联网。要求点击 **Play** 可能是浏览器对用户操作的限制。访问期限结束属于另一种状态；书签和进度仍与相应版本关联。可采取的操作以实际产品界面为准。

[导入](import.md) · [播客](podcasts.md)
