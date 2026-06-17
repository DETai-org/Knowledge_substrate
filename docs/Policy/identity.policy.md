# Policy: identity schema draft

## Назначение

Эта политика относится к будущей PostgreSQL schema `identity` внутри database
`detai_projects`.

`identity` отвечает за общий слой пользовательской идентичности экосистемы
DET / DETai. Эта schema должна отвечать на вопрос: кто этот человек в системе?

## Граница ответственности

`identity` хранит стабильные и сквозные данные пользователя:
- внутренний user id экосистемы;
- email и состояние подтверждения email;
- Telegram user id / username linkage;
- отображаемое имя;
- способы связи;
- базовые согласия пользователя;
- статус аккаунта.

`identity` не должна хранить:
- права доступа и подписки;
- содержимое заявок;
- регистрации на события;
- настройки конкретных проектов;
- delivery-log уведомлений;
- product-specific артефакты.

Связанные доменные записи должны ссылаться на пользователя из `identity`, а не
копировать пользовательскую модель внутрь каждой project schema.

## Номинальные поля и сущности

Это черновой список, не production-контракт.

### `identity.users`

- `id`
- `public_id`
- `display_name`
- `primary_email`
- `status`
- `created_at`
- `updated_at`

### `identity.user_identities`

- `id`
- `user_id`
- `provider`
- `provider_user_id`
- `provider_username`
- `metadata_json`
- `created_at`
- `updated_at`

Примеры provider:
- `email`;
- `telegram`;
- future OAuth providers.

### `identity.contact_methods`

- `id`
- `user_id`
- `kind`
- `value`
- `is_primary`
- `is_verified`
- `verified_at`
- `created_at`
- `updated_at`

### `identity.email_verifications`

- `id`
- `user_id`
- `email`
- `token_hash`
- `status`
- `expires_at`
- `consumed_at`
- `created_at`

### `identity.consents`

- `id`
- `user_id`
- `consent_kind`
- `status`
- `source_surface`
- `granted_at`
- `revoked_at`
- `metadata_json`

## Инварианты черновика

1. Один пользователь экосистемы должен иметь один canonical record в
   `identity.users`.
2. Project schemas не должны создавать собственную независимую user-модель как
   долгосрочный источник истины.
3. Project-specific данные должны ссылаться на `identity.users`.
4. Schema должна проектироваться так, чтобы в будущем ее можно было вынести в
   отдельную database без переписывания всей runtime-модели.

## Открытые вопросы

- Финальная auth-модель: email-first, Telegram-first или hybrid.
- Стратегия lightweight user для заявок без полного аккаунта.
- Минимальный набор consent-сущностей для WP10 legal/cookie/account launch.
- Правила миграции из project-local users, например
  `psychology_in_quotes.users`.
