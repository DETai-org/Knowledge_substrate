# Policy: access schema draft

## Назначение

Эта политика относится к будущей PostgreSQL schema `access` внутри database
`detai_projects`.

`access` отвечает за общий слой прав, ролей, подписок и доступов пользователя в
экосистеме DET / DETai. Эта schema должна отвечать на вопрос: что этому
пользователю разрешено делать или использовать?

## Граница ответственности

`access` хранит mutable access state:
- роли пользователя в экосистеме;
- роли пользователя в отдельных продуктах;
- product entitlements;
- статусы подписок;
- trial / beta access;
- admin / staff permissions;
- audit access-изменений.

`access` не должна хранить:
- email, Telegram id или профильные данные пользователя;
- payload заявок и форм;
- содержимое событий;
- notification delivery logs;
- project-owned артефакты.

Все записи access-слоя должны ссылаться на canonical user record из
`identity.users`.

## Номинальные поля и сущности

Это черновой список, не production-контракт.

### `access.roles`

- `id`
- `code`
- `label`
- `scope`
- `description`
- `created_at`

Примеры scope:
- `ecosystem`;
- `detai_site`;
- `psychology_in_quotes`;
- future project codes.

### `access.user_roles`

- `id`
- `user_id`
- `role_id`
- `status`
- `starts_at`
- `ends_at`
- `source`
- `created_at`
- `updated_at`

### `access.entitlements`

- `id`
- `code`
- `product_code`
- `label`
- `description`
- `created_at`

### `access.user_entitlements`

- `id`
- `user_id`
- `entitlement_id`
- `status`
- `starts_at`
- `ends_at`
- `source`
- `metadata_json`
- `created_at`
- `updated_at`

### `access.subscription_states`

- `id`
- `user_id`
- `product_code`
- `plan_code`
- `status`
- `provider`
- `provider_subscription_id`
- `current_period_starts_at`
- `current_period_ends_at`
- `created_at`
- `updated_at`

## Инварианты черновика

1. `access` не является profile-хранилищем пользователя.
2. Все права и подписки должны быть привязаны к `identity.users`.
3. Access-state должен быть историзируемым или аудируемым, потому что ошибки в
   правах доступа являются security-рискoм.
4. Schema должна проектироваться так, чтобы ее можно было вынести в отдельную
   database или сервис, если требования к security/compliance вырастут.

## Открытые вопросы

- Финальная модель ролей: role-based, entitlement-based или hybrid.
- Как разделить paid subscriptions, manual access и beta access.
- Нужен ли отдельный billing/payment слой или пока достаточно
  `subscription_states`.
- Как мигрировать существующие project-local планы, например
  `psychology_in_quotes.user_plans`.
