---
type: ecosystem
classification:
  scope: DETai_cluster
  context: platform
  layer: architecture-and-logic
  function: explanation
descriptive:
  id: detai-platform-telegram-account-manager-explanation
  version: v3
  status: active
  date_ymd: 2026-09-11
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

**Telegram Account Manager** — внутренний командный слой, который ведёт жизненный цикл управляемых Telegram-аккаунтов. Этот документ описывает именно устройство системы: какие объекты она хранит, как проходит добавление аккаунта, как устроены доступы и приглашения, где заканчивается её ответственность и какие другие контуры используют результат.

Философское основание — зачем команде вообще нужен такой слой и что считается разрешённым ресурсом — вынесено отдельно: [«Разрешённый ресурс и стартовый импульс»](account-manager-philosophy.md).

Практическое обучение работе с текущим интерфейсом не дублируется здесь. Project-specific tutorial хранится в owning repository `DETai-org/Telegram` и служит source of truth для встроенной помощи бота.

## Managed account как объект

Managed account — устойчивый внутренний объект, а не просто `.session`-файл. Для него система связывает:

- командный scope, в котором аккаунт обслуживается;
- стабильное `session_name`;
- Telegram `user_id` и доступные профильные данные;
- каноническую automation session;
- закреплённый Network Profile;
- состояние Visual Profile;
- readiness и операционное состояние;
- provenance: кто предоставил аккаунт и какой участник команды инициировал его подключение.

Номер телефона может сохраняться как закрытое служебное поле managed account. Одноразовые коды подтверждения и 2FA-пароли постоянными данными системы не являются.

## Жизненный цикл

У Account Manager есть три технических входных сценария.

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

## Модель доступа

Доступ к боту строится как лестница возможностей и scope, а не как набор разрозненных проверок `role == ...`.

```text
Telegram event
      ↓
Identity
      ↓
Access Policy
      ↓
Capabilities + Scope
      ↓
Scenario
```

Целевая модель различает четыре уровня.

### Внешний посетитель

Пользователь без действующего внутреннего доступа получает только публичный экран DETai и ссылки на открытые ресурсы. Внешний экран не раскрывает устройство или назначение Account Manager и не содержит механизма «запросить доступ».

### Приглашённый владелец

Владелец или распорядитель аккаунта входит по персональной ссылке вида `/start invite_xxxxx`. Его capability ограничена конкретным onboarding-сценарием: он может подключить только предоставляемый им аккаунт и не получает доступа к другим managed accounts, командной статистике или внутренним данным.

Приглашение хранит как минимум:

```text
invited_by = <team member>
expires_at = <timestamp>
scope = account_onboarding
max_uses = 1
```

Срок 6/24 часа относится к приглашению и scoped-доступу, а **не к сроку существования уже подключённого managed account**. После завершения onboarding или expiry пользователь снова рассматривается как внешний посетитель.

Успешно подключённый аккаунт сохраняет provenance независимо от срока приглашения:

```text
account → provided_by_user → sponsored_by_team_member
```

Например, аккаунт может иметь внутреннее имя `Anton-Psy-12`, быть предоставлен Машей и при этом быть приглашён Севой. Эта связь нужна для аудита, статистики, ownership scope и последующего revoke.

### Участник команды

Участник команды получает рабочие capabilities: видеть управляемые в его scope аккаунты, создавать приглашения владельцам, смотреть рабочую статистику и пользоваться повседневными account workflow. Его scope ограничен аккаунтами, за которые он отвечает или подключение которых он инициировал.

Технические детали вроде Network diagnostics, Client Identity и редких служебных операций не должны перегружать его основной маршрут.

### Администратор

Администратор включает capabilities участника команды и дополнительно управляет командным registry, всеми managed accounts, доступами и техническими настройками. Административный scope — весь контур.

Для защиты от lockout один bootstrap-admin может оставаться статически заданным в конфигурации, тогда как динамический состав команды хранится в persistent Access Registry и применяется без перезапуска процесса.

## Приглашение и ownership — разные сущности

Invite — краткоживущий credential для входа в определённый сценарий. Managed account — долгоживущий доменный объект. Поэтому истечение invitation grant никогда само по себе не удаляет аккаунт, session или provenance.

Эта граница позволяет одновременно обеспечить минимальный доступ приглашённому человеку и сохранить устойчивую историю того, откуда появился ресурс и какой участник команды за него отвечает.

## Account Manager и UserControl

Account Manager отвечает за подготовку, состояние и ownership managed accounts. **UserControl** и другие Telegram-workflow используют уже подготовленные аккаунты для конкретных действий.

```text
Team scope / sponsorship
     ↓
Managed accounts
     ↓
Telethon sessions + Visual Profiles
     ↓
UserControl / channel actions / other Telegram workflows
```

Reaction, comment, publish, DM или moderation относятся к прикладным workflow, а не к модели managed account. Это позволяет менять и добавлять действия, не переделывая фундамент авторизации, provenance и хранения аккаунтов.

## Граница с Infrastructure

Telegram не владеет VPN, Xray, VNC ingress или физическими egress endpoint. Он потребляет соответствующие Infrastructure capabilities.

Со стороны Telegram остаются Telegram-specific policy, managed-account identity, Desktop profile и авторизация. Со стороны Infrastructure — сетевой provider и безопасная операционная точка доступа к execution environment.
