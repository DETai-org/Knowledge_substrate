# notifications schema draft

`notifications` is the shared runtime schema for notification preferences,
subscriptions, dispatch planning, and delivery logs inside database
`detai_projects`.

This folder is a draft schema contour. It records the intended responsibility
boundary before production migrations are written.

## Responsibility

`notifications` answers the question: who should be notified, through which
channel, about which topic, and what happened during delivery?

It should store notification-domain data:
- user topic subscriptions;
- channel preferences;
- dispatch jobs;
- delivery attempts;
- delivery status;
- unsubscribe or mute state.

It should not store:
- event source-of-truth data;
- user identity profile fields;
- access rights;
- intake form payloads;
- bot-specific chat state unrelated to delivery.

## Draft table candidates

These names and fields are provisional and must be refined before a production
migration is created.

### topics

- `id`
- `code`
- `label`
- `description`
- `created_at`

Example topics:
- `therapy`
- `education`
- `research`
- `detai`
- `partners`
- `territory_psyche`

### subscriptions

- `id`
- `user_id`
- `topic_id`
- `channel`
- `status`
- `created_at`
- `updated_at`

Example channels:
- `telegram`
- `email`
- future account/in-app channel.

### dispatch_jobs

- `id`
- `source_kind`
- `source_id`
- `topic_id`
- `channel`
- `status`
- `scheduled_at`
- `created_at`
- `updated_at`

### delivery_attempts

- `id`
- `dispatch_job_id`
- `user_id`
- `channel`
- `destination_snapshot`
- `status`
- `provider_message_id`
- `error_code`
- `error_message`
- `attempted_at`

## Runtime interfaces

Notification workers should consume domain events such as a published
`ecosystem_events.events` record, resolve subscribers in this schema, and then
dispatch messages through Telegram, email, or future delivery channels.
