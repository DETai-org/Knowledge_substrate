# Policy: notifications schema draft

## Назначение

Эта политика относится к будущей PostgreSQL schema `notifications` внутри
database `detai_projects`.

`notifications` отвечает за подписки, предпочтения каналов, dispatch jobs и
delivery logs. Эта schema должна отвечать на вопрос: кому, куда и как сообщить
о событии или другом runtime-сигнале?

## Граница ответственности

`notifications` хранит:
- notification topics;
- пользовательские подписки;
- предпочтения каналов;
- задания на отправку;
- попытки доставки;
- статусы delivered/failed/skipped;
- mute/unsubscribe state.

`notifications` не должна хранить:
- source-of-truth событий;
- профиль пользователя;
- права доступа;
- payload заявок;
- техническое состояние бота, не связанное с доставкой.

## Номинальные поля и сущности

Это черновой список, не production-контракт.

### `notifications.topics`

- `id`
- `code`
- `label`
- `description`
- `created_at`

### `notifications.subscriptions`

- `id`
- `user_id`
- `topic_id`
- `channel`
- `status`
- `created_at`
- `updated_at`

### `notifications.dispatch_jobs`

- `id`
- `source_kind`
- `source_id`
- `topic_id`
- `channel`
- `status`
- `scheduled_at`
- `created_at`
- `updated_at`

### `notifications.delivery_attempts`

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

## Инварианты черновика

1. Событие может существовать без уведомления.
2. Одно событие может породить много delivery attempts.
3. Notification channel не должен ограничиваться Telegram: Telegram, email и
   future account/in-app delivery должны использовать общую модель.
4. Telegram bot может отправлять сообщения, но не должен владеть подписками как
   своим закрытым хранилищем.
