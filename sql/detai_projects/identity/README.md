# identity schema draft

`identity` is the shared runtime schema for ecosystem user identity inside
database `detai_projects`.

This folder is a draft schema contour. It records the intended responsibility
boundary before production migrations are written.

## Responsibility

`identity` answers the question: who is this person in the DET / DETai
ecosystem?

It should store stable, cross-project user identity data:
- ecosystem user id;
- email address and verification state;
- Telegram user id / username linkage;
- display name;
- contact methods;
- consent baseline;
- account lifecycle status.

It should not store:
- product-specific settings;
- project-owned artifacts;
- paid product access state;
- event registrations;
- therapy or education requests;
- notification delivery logs.

Those records should reference `identity.users` from their own runtime schemas.

## Draft table candidates

These names and fields are provisional and must be refined before a production
migration is created.

### users

- `id`
- `public_id`
- `display_name`
- `primary_email`
- `status`
- `created_at`
- `updated_at`

### user_identities

External identity bindings for login and bot surfaces.

- `id`
- `user_id`
- `provider`
- `provider_user_id`
- `provider_username`
- `metadata_json`
- `created_at`
- `updated_at`

Example providers:
- `email`
- `telegram`
- future OAuth providers.

### contact_methods

- `id`
- `user_id`
- `kind`
- `value`
- `is_primary`
- `is_verified`
- `verified_at`
- `created_at`
- `updated_at`

### email_verifications

- `id`
- `user_id`
- `email`
- `token_hash`
- `status`
- `expires_at`
- `consumed_at`
- `created_at`

### consents

- `id`
- `user_id`
- `consent_kind`
- `status`
- `source_surface`
- `granted_at`
- `revoked_at`
- `metadata_json`

## Evolution note

`identity` should be designed so it can later be moved from `detai_projects` to
a dedicated database if privacy, compliance, access-control, or scaling
requirements make that necessary.
