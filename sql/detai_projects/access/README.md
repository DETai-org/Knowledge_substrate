# access schema draft

`access` is the shared runtime schema for roles, permissions, entitlements, and
subscription states inside database `detai_projects`.

This folder is a draft schema contour. It records the intended responsibility
boundary before production migrations are written.

## Responsibility

`access` answers the question: what is this user allowed to do or use across
the DET / DETai ecosystem?

It should store mutable access state:
- ecosystem roles;
- product roles;
- product entitlements;
- subscription status;
- trial or beta access;
- admin/staff permissions;
- access audit data.

It should not store:
- email or Telegram identity data;
- personal profile fields;
- event content;
- request form payloads;
- project-owned runtime artifacts.

Access records should reference `identity.users` as the shared user source.

## Draft table candidates

These names and fields are provisional and must be refined before a production
migration is created.

### roles

- `id`
- `code`
- `label`
- `scope`
- `description`
- `created_at`

Example scopes:
- `ecosystem`
- `detai_site`
- `psychology_in_quotes`
- future project codes.

### user_roles

- `id`
- `user_id`
- `role_id`
- `status`
- `starts_at`
- `ends_at`
- `source`
- `created_at`
- `updated_at`

### entitlements

- `id`
- `code`
- `product_code`
- `label`
- `description`
- `created_at`

### user_entitlements

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

### subscription_states

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

## Evolution note

`access` is separated from `identity` because identity changes rarely, while
roles, entitlements, and subscriptions change often and carry different
security risks. The schema should still be easy to move to a dedicated database
or service later if access-control requirements grow.
