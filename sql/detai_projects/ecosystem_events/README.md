# ecosystem_events schema draft

`ecosystem_events` is the shared runtime schema for events in the DET / DETai
ecosystem inside database `detai_projects`.

This folder is a draft schema contour. It records the intended responsibility
boundary before production migrations are written.

## Responsibility

`ecosystem_events` answers the question: what happens, or is planned to happen,
inside the ecosystem?

It should store event-domain data:
- event title, slug, summary, body;
- event type and ecosystem layer;
- publication status;
- date/time and location metadata;
- relationships to DET, DETai, Partners, Territory Psyche, or project surfaces;
- registration mode and public visibility state;
- admin lifecycle metadata.

It should not store:
- user profile fields;
- access rights or subscriptions;
- form payloads and request texts;
- notification delivery logs;
- Telegram chat state.

## Draft table candidates

These names and fields are provisional and must be refined before a production
migration is created.

### events

- `id`
- `slug`
- `title`
- `summary`
- `body`
- `event_type`
- `ecosystem_layer`
- `status`
- `starts_at`
- `ends_at`
- `timezone`
- `location_kind`
- `location_label`
- `registration_status`
- `created_by_user_id`
- `published_at`
- `created_at`
- `updated_at`

### event_relations

- `id`
- `event_id`
- `relation_kind`
- `relation_key`
- `created_at`

Example relations:
- `det:therapy`
- `det:education`
- `det:research`
- `detai:platform`
- `partners:ai-psychology-section`
- `territory-psyche`

### event_lifecycle_events

- `id`
- `event_id`
- `actor_user_id`
- `action`
- `payload_json`
- `created_at`

## Runtime interfaces

Events may be created or edited through an admin interface such as an admin
Telegram bot or future web admin surface. The website and notification workers
should read from this schema instead of storing their own event source of truth.
