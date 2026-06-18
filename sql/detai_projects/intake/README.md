# intake schema draft

`intake` is the shared runtime schema for incoming forms, requests,
registrations, suggestions, and complaints inside database `detai_projects`.

This folder is a draft schema contour. It records the intended responsibility
boundary before production migrations are written.

## Responsibility

`intake` answers the question: what has a person submitted to the ecosystem?

It should store incoming operational records:
- therapy requests;
- event registrations;
- education/course applications;
- partner or collaboration requests;
- suggestions and complaints;
- waitlist entries;
- processing status and internal notes.

It should not store:
- canonical user profile fields;
- product access rights;
- event source-of-truth data;
- notification delivery logs;
- bot chat state.

Records in this schema should reference `identity.users` when the submitter is
known. During a soft launch, records may also keep a contact snapshot for
submissions created before full account registration.

## Draft table candidates

These names and fields are provisional and must be refined before a production
migration is created.

### submissions

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

Example `kind` values:
- `therapy_request`
- `event_registration`
- `education_application`
- `partnership_request`
- `suggestion`
- `complaint`

### event_registrations

- `id`
- `submission_id`
- `event_id`
- `attendance_mode`
- `registration_status`
- `created_at`
- `updated_at`

### therapy_requests

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

### processing_notes

- `id`
- `submission_id`
- `actor_user_id`
- `actor_source`
- `note_text`
- `visibility`
- `created_at`

## First runtime migration

`migrations/0001_intake_runtime.sql` is the first end-to-end runtime migration.
It creates the shared submission envelope, the first typed detail table for
`therapy_request`, and internal processing notes.

Server/database time is authoritative for `created_at` and `updated_at`.
Website and bot clients send explicit source metadata and form payloads, but do
not provide canonical submission timestamps.

If the PostgreSQL role `ecosystem_runtime_api` already exists, the migration
grants it schema usage, table read/write access, and sequence usage for the
`intake` schema. Role creation and password management remain server operations,
not source-controlled SQL.

Apply only this schema on the server:

```bash
cd /srv/Knowledge_substrate/sql/detai_projects/intake
bash apply_migrations.sh
```

### form_presets

Optional future registry for schema-aware form definitions.

- `id`
- `code`
- `kind`
- `version`
- `status`
- `labels_i18n_json`
- `fields_json`
- `created_at`
- `updated_at`

The first production iteration may keep presets in application code, but the
submission payload must remain compatible with the policy model.

## Runtime interfaces

Submissions may come from the public website, a public Telegram bot, or future
account surfaces. All interfaces should write to this shared schema instead of
owning separate request stores.

## Preset boundary

The shared model supports multiple form presets:
- `therapy_request`
- `education_interest`
- `event_registration`
- `section_participation`
- `team_application`
- `partner_request`
- `feedback`

Each preset should use a common submission envelope:
- `kind`
- `source_channel`
- `source_app`
- `source_surface`
- `target_key`
- `locale`
- `contact_snapshot`
- `payload_json`
- `consent`

User-facing labels and option titles must be multilingual. Initial locale keys:
- `ru`
- `en`
- `es`
- `fr`
- `de`

Notification subscription choices do not belong to intake forms. They belong to
the `notifications` schema and should be handled by a separate subscription
flow.

## Current UI notes

The current `detai-site` intake presets are still application-code presets, not
database-stored form definitions. When they change, this schema contour and
`docs/Policy/intake.policy.md` must be updated together.

Recent field decisions:
- `education_interest.education_format` does not mention supervision or
  intervision;
- `education_interest.attendance_mode` captures offline Saint Petersburg,
  online, or either;
- `education_interest.preferred_duration` captures whether a short two-hour
  meeting, half-day format, full-day format, multi-day intensive, or undecided
  duration is preferable;
- `education_interest.learning_mode` captures whether theory, theory with
  practical cases, practical work, discussion, or an undecided mode is
  preferable;
- `education_interest.education_background` is a free-form education/profession
  field;
- `team_application.participation_area` uses user-facing ecosystem roles:
  `design_creative`, `vibe_coding`, `content_channels`, `events_education`,
  `research_methodology`, `community_operations`, or `not_sure`;
- `team_application.has_telegram_channel` and
  `team_application.telegram_channel` capture public channel context separately
  from general portfolio links;
- `team_application.motivation` may be a longer motivational letter; current
  site UI limits it to 5000 characters;
- `section_participation` uses conditional fields for `listener` and `speaker`
  roles;
- listener section fields include `professional_role`,
  `professional_role_other`, `listener_affiliation`, `listener_department`,
  `bachelor_course`, `specialist_course`, `master_course`,
  `postgraduate_course`, `listener_research_area`,
  `listener_psychotherapy_format`, `listener_psychotherapy_organization`,
  `listener_technical_area`, `field_of_study`, `listener_expectations`, and
  `referral_source`;
- speaker section fields include `speaker_current_status`,
  `speaker_status_other`, `speaker_bachelor_course`,
  `speaker_specialist_course`, `speaker_master_course`,
  `speaker_postgraduate_course`, `speaker_research_area`,
  `speaker_psychotherapy_format`, `speaker_psychotherapy_organization`,
  `speaker_technical_area`, `speaker_affiliation`, `speaker_specialization`,
  `talk_topic`, `talk_summary`, and `speaker_background`;
- `section_participation` uses a formal contact snapshot with `last_name`,
  required `name`, optional `patronymic`, `email`, `telegram`, and
  `country_city`;
- website forms may be rendered as wizard steps, but still submit one common
  `intake.submissions` envelope.
