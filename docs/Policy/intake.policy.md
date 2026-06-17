# Policy: intake schema draft

## Назначение

Эта политика относится к будущей PostgreSQL schema `intake` внутри database
`detai_projects`.

`intake` отвечает за входящие формы, заявки, регистрации, предложения и жалобы.
Эта schema должна отвечать на вопрос: что пользователь или внешний участник
отправил в экосистему?

## Граница ответственности

`intake` хранит:
- заявки на психотерапию;
- регистрации на события;
- заявки на образовательные форматы;
- партнёрские обращения;
- предложения;
- жалобы;
- waitlist entries;
- статусы обработки и внутренние заметки.

`intake` не должна хранить:
- canonical profile пользователя;
- права доступа и подписки;
- source-of-truth событий;
- notification delivery logs;
- техническое состояние ботов.

## Номинальные поля и сущности

Это черновой список, не production-контракт.

### `intake.submissions`

- `id`
- `user_id`
- `kind`
- `source_channel`
- `source_app`
- `source_surface`
- `target_key`
- `locale`
- `status`
- `payload_json`
- `contact_snapshot`
- `consent`
- `created_at`
- `updated_at`

### `intake.event_registrations`

- `id`
- `submission_id`
- `event_id`
- `attendance_mode`
- `registration_status`
- `created_at`
- `updated_at`

### `intake.therapy_requests`

- `id`
- `submission_id`
- `therapy_direction`
- `request_context`
- `previous_therapy_experience`
- `preferred_contact`
- `contact_comment`
- `request_status`
- `created_at`
- `updated_at`

### `intake.processing_notes`

- `id`
- `submission_id`
- `actor_user_id`
- `actor_source`
- `note_text`
- `visibility`
- `created_at`

## First runtime migration

The first runtime migration is:

```txt
sql/detai_projects/intake/migrations/0001_intake_runtime.sql
```

It creates:

- `intake.submissions` — common envelope for all public and future account
  intake records;
- `intake.therapy_requests` — typed detail row for `kind = therapy_request`;
- `intake.processing_notes` — internal notes for staff processing.

`created_at` and `updated_at` are database/server-side timestamps. Clients may
send source and payload context, but they must not be trusted as the submission
time source of truth.

## Intake Form Presets

Intake forms should share one common submission model and differ by preset.
Each preset defines:

- `kind` — domain type of the submission;
- `source_channel` — website, telegram, future account/in-app surface;
- `source_app` — concrete app that created the submission, for example
  `detai-site` or future `public-bot`;
- `source_surface` — page, bot menu, or account surface where it was created;
- `target_key` — concrete direction, event, section, or team context;
- `locale` — language of the form shown to the user;
- `contact_snapshot` — temporary contact fields for non-authenticated users;
- `payload_json` — answers to preset-specific questions;
- `consent` — explicit processing consent for this submission.

Runtime submission time should be written server-side. The UI may send context,
but `submitted_at` / `created_at` must not rely on a client-side timestamp as the
source of truth.

Labels, help text and option titles must be stored with multilingual keys where
the preset is user-facing.

Draft locale keys:

- `ru`
- `en`
- `es`
- `fr`
- `de`

Minimal label shape:

```json
{
  "field_key": "professional_context",
  "label_i18n": {
    "ru": "Профессиональный контекст",
    "en": "Professional context",
    "es": "",
    "fr": "",
    "de": ""
  }
}
```

### Shared field types

- `text` — short text;
- `textarea` — long answer;
- `select` — one option from a longer list;
- `radio` — one option from a short list;
- `multiselect` — several options;
- `checkbox` — boolean value or consent;
- `contact` — name, email, Telegram, preferred contact channel;
- `country_city` — country/city or free-form location;
- `conditional_group` — fields shown only after a previous answer.

### Shared audience/context fields

These fields may be reused across therapy, education, section and team
application presets:

- `country`
- `city`
- `professional_role`
- `education_stage`
- `field_of_study`
- `is_practicing_psychotherapist`
- `professional_context`
- `experience_background`

## Draft Presets

### `therapy_request`

Purpose: request contact about individual or group psychotherapy.

Suggested fields:
- `therapy_direction` — radio: individual, group, not sure;
- `request_context` — textarea;
- `previous_therapy_experience` — radio: yes, no, prefer not to answer;
- `country_city` — country/city;
- `contact` — name, email, Telegram, preferred contact channel;
- `contact_comment` — textarea;
- `personal_data_consent` — checkbox.

### `education_interest`

Purpose: collect interest in workshops, seminars, courses, networking or other
educational formats.

Suggested fields:
- `education_format` — multiselect: workshop, seminar, course, networking,
  not sure, other;
- `attendance_mode` — select: offline in Saint Petersburg, online, either;
- `topics_of_interest` — textarea;
- `professional_role` — select: psychotherapist, psychologist, bachelor,
  specialist, master, postgraduate, researcher, educator,
  technical_specialist, other;
- `education_background` — text, free-form education/professional background
  such as psychologist, psychology student, doctor, educator, economist;
- `field_of_study` — text;
- `country_city` — country/city;
- `contact` — name, email, Telegram, preferred contact channel;
- `personal_data_consent` — checkbox.

### `event_registration`

Purpose: register for a concrete event.

Suggested fields:
- `attendance_mode` — radio: offline, online, either;
- `professional_context` — textarea;
- `country_city` — country/city;
- `contact` — name, email, Telegram, preferred contact channel;
- `personal_data_consent` — checkbox.

### `section_participation`

Purpose: collect applications for a professional section.

Suggested fields:
- `participation_role` — radio: listener, speaker;
- `attendance_mode` — radio: offline, online, either;
- `professional_role` — select;
- `country_city` — country/city;

Conditional fields for `participation_role = speaker`:
- `speaker_current_status` — select: bachelor, specialist, master,
  postgraduate, educator, researcher, psychotherapist, technical_specialist,
  other;
- `speaker_status_other` — text, shown when speaker status is other;
- `speaker_bachelor_course` — select: 1, 2, 3, 4;
- `speaker_specialist_course` — select: 1, 2, 3, 4, 5, 6;
- `speaker_master_course` — select: 1, 2;
- `speaker_postgraduate_course` — select: 1, 2, 3;
- `speaker_research_area` — textarea, shown when speaker is researcher;
- `speaker_psychotherapy_format` — select: private_practice, organization,
  both, other;
- `speaker_psychotherapy_organization` — text, shown when psychotherapy format
  involves organization or other;
- `speaker_technical_area` — textarea, shown for technical / AI specialists;
- `speaker_affiliation` — text, organization / university / professional
  environment where relevant;
- `speaker_specialization` — text;
- `talk_topic` — textarea;
- `talk_summary` — textarea;
- `speaker_background` — textarea.

Conditional fields for `participation_role = listener`:
- `professional_role` — select: bachelor, specialist, master, postgraduate,
  educator, researcher, psychotherapist, psychologist, technical_specialist,
  other;
- `professional_role_other` — text, shown when professional role is other;
- `bachelor_course` — select: 1, 2, 3, 4;
- `specialist_course` — select: 1, 2, 3, 4, 5, 6;
- `master_course` — select: 1, 2;
- `postgraduate_course` — select: 1, 2, 3;
- `listener_research_area` — textarea, shown when listener is researcher;
- `listener_psychotherapy_format` — select: private_practice, organization,
  both, other;
- `listener_psychotherapy_organization` — text, shown when psychotherapy
  format involves organization or other;
- `listener_technical_area` — textarea, shown for technical / AI specialists;
- `field_of_study` — text;
- `listener_expectations` — textarea;
- `referral_source` — text.

Shared closing fields:
- `contact` — name, email, Telegram, preferred contact channel;
- `personal_data_consent` — checkbox.

### `team_application`

Purpose: collect applications for joining ecosystem work.

Suggested fields:
- `participation_area` — multiselect;
- `competencies` — textarea;
- `experience_background` — textarea;
- `links` — textarea;
- `motivation` — textarea;
- `country_city` — country/city;
- `contact` — name, email, Telegram, preferred contact channel;
- `personal_data_consent` — checkbox.

### `partner_request`

Purpose: collect partner or institutional collaboration requests.

Suggested fields:
- `organization_name` — text;
- `organization_type` — text/select;
- `collaboration_context` — textarea;
- `country_city` — country/city;
- `contact` — name, email, Telegram, preferred contact channel;
- `personal_data_consent` — checkbox.

### `feedback`

Purpose: collect questions, suggestions and complaints.

Suggested fields:
- `feedback_type` — radio: question, suggestion, complaint, other;
- `message` — textarea;
- `country_city` — country/city optional;
- `contact` — name, email, Telegram, preferred contact channel;
- `personal_data_consent` — checkbox.

## Current website preset mapping

These are current `detai-site` UI surfaces aligned with the draft presets.

| Page | `kind` | `source_app` | `source_surface` | `target_key` |
| --- | --- | --- | --- | --- |
| `/det/therapy` | `therapy_request` | `detai-site` | `/det/therapy` | `det:therapy:individual`, `det:therapy:group`, `det:therapy:not-sure` |
| `/det/education` | `education_interest` | `detai-site` | `/det/education` | `det:education` |
| `/events/psychology-ai-section-opening` | `event_registration` | `detai-site` | `/events/psychology-ai-section-opening` | `events:psychology-ai-section-opening` |
| `/partners/ai-psychology-section` | `section_participation` | `detai-site` | `/partners/ai-psychology-section` | `partners:ai-psychology-section` |
| `/about/onboarding` | `team_application` | `detai-site` | `/about/onboarding` | `about:onboarding` |
| `/contacts` | `feedback` | `detai-site` | `/contacts` | `contacts:general-feedback` |
| `/contacts` | `partner_request` | `detai-site` | `/contacts` | `contacts:partner-request` |

## Notifications boundary

Intake forms must not include notification subscription choices such as
"receive announcements". Notification preferences belong to the `notifications`
schema and should be managed through a separate subscription flow.

## Website wizard boundary

The current `detai-site` implementation may render intake presets as wizard
steps. This is a UI flow only. It must not change the canonical submission
envelope:

- `kind`
- `source_channel`
- `source_app`
- `source_surface`
- `target_key`
- `locale`
- `payload_json`
- `contact_snapshot`
- `consent`

Conditional fields that are hidden in the current UI path should not be included
as meaningful answers in `payload_json`.

## Инварианты черновика

1. `intake` принимает записи и с сайта, и из публичного бота, и из future account
   surfaces.
2. Если пользователь известен, запись должна ссылаться на `identity.users`.
3. Если пользователь ещё не зарегистрирован, запись может временно хранить
   contact snapshot для soft-launch сценариев.
4. Заявка не должна храниться внутри `identity`, потому что она является
   процессной записью, а не свойством пользователя.

## Example: `/det/therapy`

Форма на странице `/det/therapy` должна создавать запись в `intake`, а не в
`identity`.

Ожидаемая цепочка:

```txt
sites:/det/therapy
→ ecosystem-runtime apps/api
→ identity.users / identity.contact_methods
→ intake.submissions
→ intake.therapy_requests
```

Номинальные значения:
- `kind = therapy_request`;
- `source_channel = website`;
- `source_surface = /det/therapy`;
- `target_key = det:therapy:individual` или `det:therapy:group`.
