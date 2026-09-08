---
type: ecosystem
classification:
  scope: DETai_cluster
  context: platform
  layer: architecture-and-logic
  function: explanation
descriptive:
  id: detai-platform-telegram-account-manager-explanation
  version: v2
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

**Telegram Account Manager** — внутренний командный слой, который ведёт жизненный цикл управляемых Telegram-аккаунтов. Этот документ описывает именно устройство системы: какие объекты она хранит, как проходит добавление аккаунта, где заканчивается её ответственность и какие другие контуры используют результат.

Философское основание — зачем команде вообще нужен такой слой и что считается разрешённым ресурсом — вынесено отдельно: [«Разрешённый ресурс и стартовый импульс»](account-manager-philosophy.md).

## Managed account как объект

Managed account — устойчивый внутренний объект, а не просто `.session`-файл. Для него система связывает:

- командный профиль владельца;
- стабильное `session_name`;
- Telegram `user_id` и доступные профильные данные;
- каноническую automation session;
- закреплённый Network Profile;
- состояние Visual Profile;
- readiness и операционное состояние.

Номер телефона может сохраняться как закрытое служебное поле managed account. Одноразовые коды подтверждения и 2FA-пароли постоянными данными системы не являются.

## Жизненный цикл

У Account Manager есть три входных сценария.

### Есть доступ к существующему Telegram

Бот создаёт каноническую Telethon-session через тот login-flow, который фактически разрешает Telegram: QR, код в уже авторизованном клиенте, SMS, звонок или другой доступный способ. Конкретный канал доставки нельзя обещать заранее — его определяет Telegram.

### Есть только доступ к номеру

Если доступного авторизованного клиента нет, Account Manager начинает code-flow и показывает реальную цепочку способов подтверждения, которую возвращает Telegram. Если выясняется, что для номера нужен другой официальный клиентский flow, пользователь может перейти к Desktop без создания нового managed account с нуля.

### Telegram ещё не создан

Для нового номера подготавливается изолированный официальный Telegram Desktop в registration workspace. Network Profile резервируется до создания Telegram identity, чтобы ручная регистрация и последующая automation session проходили в одном сетевом контексте.

Если в Desktop обнаруживается, что аккаунт на номере уже существует, тот же onboarding переключается в сценарий существующего аккаунта и сохраняет выбранный `session_name` и Network reservation.

## Automation session и Visual Profile

У одного managed account могут существовать два независимых интерфейса.

**Telethon-session** — канонический программный интерфейс для автоматизированных действий и проверок.

**Visual Profile** — отдельный официальный Telegram Desktop, изолированный для этого managed account на текущем execution node. Он нужен для действий, которые удобнее выполнять через обычный Telegram UI.

Telethon-session не копируется в Desktop. Для уже авторизованного аккаунта Visual Profile по возможности получает отдельную Desktop-авторизацию через официальный Telegram QR-login, подтверждённый существующей Telethon-session.

Название execution node — runtime-данные. Сегодня это может быть `Nexus`, завтра другой сервер; пользовательские тексты не должны делать имя конкретной машины частью бизнес-логики.

## Network Profile

При первой авторизации managed account получает **sticky Network Profile**.

Telegram отвечает за свою policy и assignment:

- priority;
- capacity;
- закрепление аккаунта за логическим профилем.

Infrastructure Network Provider отвечает за:

- endpoint;
- фактическую location;
- health;
- реализацию сетевого маршрута.

Изменение capacity влияет на размещение новых аккаунтов, но не означает автоматическую миграцию существующих.

## Роли внутри команды

**Участник команды** работает со своими managed accounts и получает короткий повседневный маршрут: подключить публичные каналы DETai, исключить managed activity из производных метрик Архивариуса и при необходимости создать Visual Profile.

**Командный администратор** получает дополнительные служебные возможности: Network settings, диагностику, bulk/external operations, административный visual access и восстановление после инфраструктурных ошибок.

Такое разделение удерживает техническую сложность вне обычного пользовательского маршрута.

## Account Manager и UserControl

Account Manager отвечает за подготовку и состояние аккаунтов. **UserControl** и другие Telegram-workflow используют уже подготовленные аккаунты для конкретных действий.

```text
Team identity
     ↓
Managed accounts
     ↓
Telethon sessions + Visual Profiles
     ↓
UserControl / channel actions / other Telegram workflows
```

Reaction, comment, publish, DM или moderation относятся к прикладным workflow, а не к модели managed account. Это позволяет менять и добавлять действия, не переделывая фундамент авторизации и хранения аккаунтов.

## Граница с Infrastructure

Telegram не владеет VPN, Xray, VNC ingress или физическими egress endpoint. Он потребляет соответствующие Infrastructure capabilities.

Со стороны Telegram остаются Telegram-specific policy, managed-account identity, Desktop profile и авторизация. Со стороны Infrastructure — сетевой provider и безопасная операционная точка доступа к execution environment.
