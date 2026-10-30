---
title: "Psychology in Quotes — 架构与信任"
description: "了解 PiQ 在 DETai 中的定位，以及账户、API、隐私与发布的责任边界。"
lang: zh
translation_of: /ru/ecosystem/DETai/Platform_DETai/products/psychology-in-quotes/architecture-and-trust/
---

# 产品如何运作，以及为什么值得信任

## PiQ 在 DETai 中的位置

- **DETai：**涵盖心理治疗、研究、教育、技术及社群的生态系统。
- **Platform DETai：**连接各数字产品的技术与产品层。
- **Psychology in Quotes：**以教育和知识传播为主要用户功能、以发布与数字创作为附加功能的数字产品。其 **E2 Brand** 角色是传播心理学知识、建立知名度与信任。
- **DETai Account：**为网站和已绑定的 Telegram 提供统一用户身份，但注册账户本身不会赋予获取他人语录的权限。

[DETai 生态系统](../../../index.md) · [Platform DETai](../../index.md) · [PiQ 产品页面](https://detai-x.com/zh/technology/platform/psychology-in-quotes)。

## 产品定位的两个独立维度

| 问题 | PiQ 的回答 |
| --- | --- |
| 用户获得什么价值？ | 通过接触心理学思想、阅读及有意义地保存语录开展自主学习 |
| 还可以做什么？ | 创建语录卡片和 Stories，发布与分享内容 |
| 对 DETai 的主要贡献是什么？ | 传播知识、建立信任和知名度，即 **E2 Brand** |
| PiQ 不承诺什么？ | 正式教育课程、资质证书、心理诊断或心理治疗 |

这种区分见于[产品对象模型](../../../../../product-market/product-object-model.md)及[梯队逻辑](../../../logic-of-echelons.md)。主要功能属于教育，并不意味着该项目自动划入 E1。

## 职责边界

| 系统或界面 | 负责 | 不负责作为何种信息来源 |
| --- | --- | --- |
| `detai-x.com` 网站 | 产品介绍、网站账户、语录、目录、SEO、法律文件 | 独立的套餐权限或私有 SQL 数据 |
| PiQ Telegram 机器人 | 创建向导、收藏、互动和发布 | 独立商业政策或 DETai Account 注册 |
| DETai Hub | 新建或连接 Account 的选择、验证 Telegram 绑定、Hub 的语言设置 | 独立 PiQ 账户或套餐权限 |
| PiQ API 与 PostgreSQL `psychology_in_quotes` | 语录获取权、有效套餐、额度、状态、PNG 准备情况、公开地址 | 整个生态系统的统一治理规则 |
| Knowledge Substrate | 公开定义、使用说明、文档关联及标准 | 实时用户数据库、机密或付款结算 |
| DETai Account / Identity | 关联不同产品中的用户身份 | 自动获取语录 |

**跳转如何完成：**PiQ 向 Hub 传递目标（“创建或连接 Account”）及界面语言提示。Hub 首先检查 Telegram 是否已经绑定统一 DETai Account：若已绑定则显示该账户，否则提供在 Telegram 创建账户，或通过可验证链接连接网站现有账户两种选择。Hub 先前保存的语言偏好不会被覆盖。此过程不会自动创建账户，也不会授予 Plus/Pro 权限。

对于开发者，通用的[机器人间语言传递规范](https://docs.detai-x.com/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/Telegram_Bots/language-handover/)和[声明式配置标准](https://docs.detai-x.com/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/Telegram_Bots/configuration-standard/)（当前仅有俄语版本）与 PiQ 自己的路径和文件分开管理。有通用规范并不能证明 PiQ 的配置加载器迁移已完成。

实际运行的契约和产品改动位于 [PiQ 代码仓库](https://github.com/DETai-org/psychology-in-quotes)：`contracts/piq-product/`、`config/piq-policy.v1.json`、`db/psychology_in_quotes/`、`docs/ADR/`。此处向用户和 AI 提供的是**权威模型的导航**，并非 Nexus 私有配置的副本。

## 语录内容与来源

语录不只是一张图片。它包含永久 `quoteId`、被引用文字的作者、书目来源、文本及修订版本、提交片段的语言、可确认时的原著语言、现成译文、图片、审核状态和发布状态。

**被引文字的作者 ≠ 卡片制作人 ≠ 在所有情况下都等于原著作者。**只有基于已核实资料才能填写元数据；AI 译文可能出现错误。译文准备、图片生成和发布授权是三种不同状态。

[署名与使用规则](https://detai-x.com/zh/technology/platform/psychology-in-quotes/terms)。

## 隐私与使用边界

- 草稿和“我的语录”默认保密；进入公共目录需要经过发布流程。
- 他人语录的公开预览图片继续带水印。
- 获取语录授予的是 **PiQ 内部的使用权限**，不是文学作品的著作权。
- PiQ 不提供心理治疗或诊断服务。
- Account 数据、技术事件和关联服务受[产品隐私声明](https://detai-x.com/zh/technology/platform/psychology-in-quotes/privacy)约束。
- 为保护个人信息，不应将私人语录文本、令牌或健康资料放入公开帮助文档或发给外部 AI。

## 供支持团队和 AI 助手使用

**支持路径：**[开始使用](getting-started.md) → [权限模型](collection-and-plans.md) → [常见问题](help-and-troubleshooting.md) → [实际生效的 API/政策](https://github.com/DETai-org/psychology-in-quotes)。此路径不授权任何人替未经验证的用户执行操作。

AI 解读截图时，必须区分文档能够证明的事实、屏幕上实际显示的信息，以及没有当前 Account 或后端数据就无法确认的事项。不要猜测付款、权限、PNG 缺失原因或发送是否成功。

**更新日期：2026 年 10 月 30 日。****可用状态：**生产环境试点。Telegram Stars 仅供封闭试点使用，公众尚不能购买。具有约束力的法律条款及动态限额，始终优先于过时的帮助文档副本。

[← 产品概览](index.md) · [收藏与套餐](collection-and-plans.md)
