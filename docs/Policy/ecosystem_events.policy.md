# Policy: ecosystem_events schema draft

## Назначение

Эта политика относится к будущей PostgreSQL schema `ecosystem_events` внутри
database `detai_projects`.

`ecosystem_events` отвечает за календарный и событийный слой экосистемы
DET / DETai. Эта schema должна отвечать на вопрос: что происходит или будет
происходить в экосистеме?

## Граница ответственности

`ecosystem_events` хранит:
- события экосистемы;
- статусы публикации событий;
- дату, время и место проведения;
- тип события;
- связь события с DET, DETai, Partners, Territory Psyche или project surfaces;
- lifecycle metadata события.

`ecosystem_events` не должна хранить:
- профильные данные пользователей;
- подписки и права доступа;
- payload заявок;
- delivery-log уведомлений;
- техническое состояние Telegram-ботов.

## Номинальные поля и сущности

Это черновой список, не production-контракт.

### `ecosystem_events.events`

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

### `ecosystem_events.event_relations`

- `id`
- `event_id`
- `relation_kind`
- `relation_key`
- `created_at`

### `ecosystem_events.event_lifecycle_events`

- `id`
- `event_id`
- `actor_user_id`
- `action`
- `payload_json`
- `created_at`

## Инварианты черновика

1. Сайт `/events` должен читать события из `ecosystem_events`, а не иметь
   отдельный source of truth.
2. Admin bot или future admin surface могут создавать события, но не должны
   владеть отдельным event-store.
3. Уведомления должны ссылаться на событие, а не копировать его как primary
   data.
4. Событие должно иметь lifecycle status, например draft/review/published/
   archived.
