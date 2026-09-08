---
type: ecosystem
classification:
  scope: DETai_cluster
  context: platform
  layer: architecture-and-logic
  function: explanation
descriptive:
  id: detai-platform-telegram-account-manager-explanation
  version: v1
  status: active
  date_ymd: 2026-09-08
links:
  external_links:
    - type: MkDocs_ru
      url: https://docs.detai-x.com/ru/ecosystem/DETai/Platform_DETai/E2-Brand/Telegram/account-manager/
  document_links:
    - schema: ecosystem
      link_type: parent
      linked_document_id: detai-platform-detai-e2-brand-telegram-index
    - schema: ecosystem
      link_type: complements
      linked_document_id: detai-platform-telegram-account-manager-philosophy
title: Telegram Account Manager — как устроена система
---

# Telegram Account Manager — как устроена система

**Telegram Account Manager** — внутренний командный слой управления авторизованными Telegram-аккаунтами. Он превращает отдельные session-файлы и ручные действия на сервере в управляемый жизненный цикл: аккаунт можно добавить через бота, закрепить за командным профилем, безопасно авторизовать, проверить, открыть визуально и затем использовать в разрешённых Telegram-workflow.

## Managed account как объект

Managed account — это не просто `.session`-файл. Система знает как минимум:

- командный профиль владельца;
- стабильное имя managed account;
- Telegram `user_id` и доступные профильные данные;
- каноническую automation session;
- закреплённый Network Profile;
- наличие Visual Profile;
- операционное состояние и readiness.

Номер телефона нужен для авторизации и может храниться как служебное поле аккаунта, но коды подтверждения и 2FA не являются постоянными данными системы.

## Два пути добавления аккаунта

### Существующий Telegram-аккаунт

Если Telegram уже существует, бот помогает создать каноническую Telethon-session через доступный Telegram login-flow: QR, код в уже авторизованном клиенте, SMS или другой способ, который в конкретной попытке разрешает Telegram. Бот не должен обещать способ доставки, которого Telegram не предложил.

### Новый Telegram-аккаунт

Если номер ещё не зарегистрирован в Telegram, сначала используется официальный Telegram Desktop в изолированном registration workspace. После завершения регистрации бот создаёт каноническую Telethon automation session через тот же закреплённый Network Profile.

Если в процессе выясняется, что аккаунт на номере уже существует, flow должен продолжиться как авторизация существующего аккаунта, а не заставлять человека начинать весь managed-account onboarding заново.

## Automation session и Visual Profile

У одного managed account могут существовать два разных способа работы.

**Telethon-session** — канонический программный интерфейс. Через неё выполняются автоматизированные Telegram-действия и проверки.

**Visual Profile** — отдельный официальный Telegram Desktop, изолированный для этого managed account на текущем execution node. Он нужен, когда удобнее воспользоваться обычным интерфейсом Telegram. Telethon-session не копируется в Desktop; при возможности Desktop авторизуется официальным QR-login через уже существующую Telethon-session.

Название execution node всегда является runtime-данными. Сегодня таким узлом может быть `Nexus`, завтра — другой сервер; тексты бота и документация не должны жёстко пришивать Visual Profile к одному имени машины.

## Network Profile

Каждый managed account получает **sticky Network Profile** при первой авторизации. Telegram хранит assignment и свою policy — priority и capacity. Infrastructure Network Provider владеет endpoint, фактической location и health.

Sticky означает, что уже созданную сессию не следует без необходимости переносить между Network Profile. Изменение capacity влияет на распределение новых аккаунтов, но не является командой мигрировать существующие.

## Роли внутри команды

Account Manager — внутренний инструмент, поэтому доступ строится не как «публичный пользователь против администратора», а как распределение командной ответственности.

**Участник команды** работает со своими managed accounts и после создания аккаунта получает понятный основной маршрут: подключить каналы DETai, исключить managed activity из производных метрик Архивариуса и подготовить Visual Profile.

**Командный администратор** отвечает за более техническую часть: настройки Network, диагностику, служебные действия, доступ к административной workstation и восстановление после инфраструктурных ошибок. Эти экраны не должны перегружать обычного участника.

## Связь с UserControl и другими workflow

Account Manager создаёт и поддерживает ресурс. UserControl и другие Telegram-workflow этот ресурс потребляют.

```text
Team identity
     ↓
Managed accounts
     ↓
Canonical sessions + Visual Profiles
     ↓
Telegram workflows
```

Поэтому reaction, comment, publish или DM не являются «свойством сессии». Это отдельные действия над авторизованным ресурсом. Такая граница позволяет добавлять новые workflow без переделки фундаментального слоя аккаунтов.

## Граница с Infrastructure

Telegram не владеет VPN/Xray/egress как инфраструктурой. Он потребляет Network Provider capability и владеет только Telegram-specific policy и assignment. Visual access также разделён: Telegram владеет профилем Desktop и авторизацией, Infrastructure — безопасной операционной точкой доступа к приватному desktop/VNC контуру.