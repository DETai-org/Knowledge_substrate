# Sub-Issue 2: Semantic Graph API (v1) & API Service Hardening

## Title
Версионированный API-сервис semantic graph для publish-постов с базовым production-контуром.

## Purpose 🎯
После мерджа в репозитории появляется устойчивый API-слой для выдачи semantic graph в формате `nodes + edges` через версионированный endpoint `/v1/graph`.  
Это завершает переход от data-pipeline (Sub-Issue 1) к потребляемому сервисному интерфейсу для сайта/клиентов и продвигает Epic к первому релизному состоянию knowledge layer.

---

## Tasks (Acceptance Checklist)

- [x] **Архитектура API-сервиса: декомпозиция FastAPI по модулям**
  1. Внутри `sql/detai_core/api/app/` выделить:
     - `main.py` (создание app + middleware + include_router),
     - `routers/health.py`,
     - `routers/graph.py`,
     - `schemas/graph.py`,
     - `services/graph_query.py`,
     - `core/config.py` (env/config),
     - `core/logging.py` (structured logging).
  2. Убрать бизнес-логику SQL из `main.py` в service-слой.
  3. Сохранить обратную совместимость `/health` (или корректно зафиксировать breaking-change в Notes).

- [x] **Спроектировать и зафиксировать каноничную модель metadata-узлов для graph API v1**
  1. Добавить в DDL новую таблицу `knowledge.doc_metadata` (или эквивалент) с `doc_id TEXT PRIMARY KEY` как canonical SoT id (`administrative.id`).
  2. Зафиксировать минимальный набор полей для фильтров v1: `year` (или `date_ymd`), `channels`, `authors`, `rubric_ids`, `category_ids`, `doc_type`, `updated_at`, `meta`.
  3. Зафиксировать типы полей (массивы `TEXT[]` или `JSONB`) и единый контракт сериализации для API.
  4. Явно задокументировать, что `knowledge.documents.id (BIGSERIAL)` не является canonical id для semantic graph.
     
____

- [x] **Ввести оркестратор ingest-пайплайна и разнести обязанности по этапам**

  1) Создать единый CLI-оркестратор
     - Добавить `knowledge_core/ingest_pipeline/run_ingest.py` (или `ingest_pipeline/run.py`) как единую точку входа.
     - Оркестратор должен уметь запускать этапы последовательно и выборочно:
       - `--stage metadata`
       - `--stage embeddings`
       - `--stage edges`
       - `--stage all` (по умолчанию)
     - Оркестратор должен возвращать ненулевой exit code при ошибке любого этапа (и печатать понятное сообщение).

  2) Выделить этап materialization metadata (SoT → Operational Store)
     - Добавить модуль `knowledge_core/ingest_pipeline/metadata/metadata_ingest.py` (или аналогичный пакет).
     - Реализовать idempotent upsert в `knowledge.doc_metadata` по ключу `doc_id = administrative.id`.
     - Маппинг без потерь:
       - `administrative.id` → `doc_id`
       - `administrative.date_ymd` → `date_ymd` (и/или вычисляемый `year`)
       - `administrative.authors` → `authors`
       - `administrative.channels` → `channels`
       - `descriptive.taxonomy.rubric_ids` → `rubric_ids`
       - `descriptive.taxonomy.category_ids` → `category_ids`
     - Валидация обязательных полей + диагностические логи по пропускам/неконсистентности.

  3) Сохранить/оформить этап embeddings
     - Этап embeddings должен быть отдельным исполняемым этапом (CLI/функция), который можно запускать независимо.
     - Он не должен отвечать за материализацию metadata (разделение ответственности).

  4) Сохранить/оформить этап построения semantic edges
     - Этап edges должен быть отдельным исполняемым этапом (CLI/функция), который можно запускать независимо.
     - Он должен использовать канонический `doc_id` (SoT administrative.id) и сохранять рёбра в `knowledge.similarity_edges`.

  5) Гарантировать независимый запуск каждого этапа + оркестрацию “all”
     - Каждый этап должен иметь собственную точку запуска (например, `python -m ... --stage X` или прямой модульный CLI).
     - Оркестратор `--stage all` должен выполнять этапы в фиксированном порядке:
       1) metadata → 2) embeddings → 3) edges
     - При необходимости Codex может разнести текущий `graph_builder/pipeline.py` (≈900 строк) на модули (`extract/transform/persist/utils`) так, чтобы:
       - логика была читаемой,
       - этапы были переиспользуемыми из оркестратора,
       - не было монолитного “всё в одном файле”.

  6) Сделать “человеческие” логи с эмоджи и контекстом (как стандарт пайплайна)
     - Ввести единый лог-хелпер (например, `ingest_pipeline/logging.py`) и обязать использовать его во всех этапах и в оркестраторе.
     - Логи должны быть понятными в терминале: краткая фраза + ключевые поля.
     - Минимальные события (с эмоджи):
       - `🚀 start` (run_id, stage)
       - `📥 read` (сколько постов/файлов)
       - `🧱 upsert` (таблица, вставлено/обновлено)
       - `🧠 embeddings` (модель, docs_count)
       - `🕸️ edges` (edges_count, параметры k/min_similarity)
       - `✅ done` (duration_ms)
       - `⚠️ warn` (skip_reason, doc_id)
       - `❌ error` (stage, doc_id/source_path, краткая причина)
     - При ошибках: печатать “что упало + на каком doc_id/файле + что делать дальше” (без простыней stacktrace по умолчанию; stacktrace — по флагу `--debug`).

  7) Документация и проверяемость
     - Обновить README с “как запустить”:
       - запуск одного этапа
       - запуск `--stage all`
       - обязательные env (DB_DSN / OPENAI_API_KEY / paths)
     - Добавить минимальные smoke-проверки (на уровне кода/скрипта):
       - `metadata` пишет строки в `knowledge.doc_metadata`
       - `embeddings` пишет строки в `knowledge.embeddings`
       - `edges` пишет строки в `knowledge.similarity_edges`
____
     
- [x] **Зафиксировать и внедрить каноничный join для графа: `similarity_edges -> doc_metadata`**
  1. В service-слое `/v1/graph` использовать `source_id/target_id` из `knowledge.similarity_edges` как `doc_id` для join с `knowledge.doc_metadata`.
  2. Описать SQL-стратегию выборки: фильтрация doc_id по metadata -> выборка рёбер только между отфильтрованными doc_id -> сборка `nodes + edges + meta`.
  3. Добавить проверку консистентности: рёбра без соответствующей metadata-ноды не попадают в выдачу и логируются как data-gap.
  4. Явно исключить зависимость фильтров v1 от `knowledge.documents.meta`, если она не материализована и не гарантирована.

- [x] **Добавить производственные индексы для быстрых фильтров graph API v1**
  1. Добавить индекс по `year` (или `date_ymd`) в `knowledge.doc_metadata`.
  2. Добавить GIN-индексы по коллекциям фильтров (`channels`, `authors`, `rubric_ids`, `category_ids`) в выбранном формате хранения.
  3. Проверить, что текущие индексы `knowledge.similarity_edges` (`source_id`, `target_id`, `weight`) используются в конечной стратегии запроса.
  4. Зафиксировать безопасные ограничения `limit_nodes` и поведение `truncated` при больших выборках.

- [x] **Единый data-contract ingest ↔ API для v1 (без двойной трактовки DoD)**
  1. Собрать и зафиксировать единый список результатов:
     - mapping полей `knowledge.similarity_edges` + `knowledge.doc_metadata` → API `nodes/edges`,
     - ограничения версии `v1`,
     - fallback при неполной metadata,
     - план эволюции `v1.1+`.
  2. Зафиксировать строгий API-контракт `v1` с edge-case правилами и без разночтений между ingest/API/OpenAPI.
  3. Синхронизировать формулировки между implementation notes и каноничными документами.

  → Policy: [Semantic Graph API v1 (инварианты и правила)](../docs/Policy/semantic-graph-api-v1.policy.md)
  → Guide: [Semantic Graph API v1 (использование и примеры)](../docs/guides/semantic-graph-api-v1.guide.md)

- [x] **Контракт и endpoint `GET /v1/graph`**
  1. Реализовать endpoint `GET /v1/graph`.
  2. Поддержать query-параметры: `channels`, `year_from`, `year_to`, `rubric_ids`, `category_ids`, `authors`, `limit_nodes`.
  3. Зафиксировать коды ответов (`200`, `400/422`, `500`) и причины.
  4. Зафиксировать response-контракт: `nodes`, `edges`, `meta` (+ JSON-схема `meta.filters_applied`).
  5. Зафиксировать детерминизм выборки: сортировка `nodes/edges`, правила пустого результата, `truncated=true`, policy по дублям рёбер.
  6. Держать 1–2 каноничных примера запроса/ответа в guide-документе (без дублирования в sub-issue).

  → Policy: [Semantic Graph API v1 (инварианты и правила)](../docs/Policy/semantic-graph-api-v1.policy.md)
  → Guide: [Semantic Graph API v1 (использование и примеры)](../docs/guides/semantic-graph-api-v1.guide.md)

- [x] **API hardening: CORS, ошибки, логирование**
  1. Подключить CORS с allowlist черз env (`API_CORS_ORIGINS`), запрет wildcard по умолчанию.
  2. Ввести единый формат ошибок (`HTTPException` + domain errors + понятный `detail` без утечки внутренних stack traces).
  3. Включить structured logs (json или key-value) минимум с полями:
     `timestamp`, `level`, `event`, `request_id`, `path`, `status_code`, `duration_ms`.
  4. Для `/v1/graph` логировать число узлов/рёбер и признак truncation.

- [x] **Runtime и локальный запуск**
  1. Добавить `Makefile` в `sql/detai_core/` с минимумом целей:
     - `make api` (локальный запуск uvicorn),
     - `make lint` (если линтер уже используется в проекте),
     - `make format` (опционально, если уже есть formatter-стандарт).
  2. Добавить `sql/detai_core/api/Dockerfile` для сервиса API.
  3. Добавить/обновить `docker-compose.yml` (в корне или в `sql/detai_core/`) с сервисами API + Postgres (или подключение к существующему контейнеру БД).
  4. Обновить `README` с инструкцией «как поднять API локально», обязательными env и примером запроса к `/v1/graph`.

- [x] **Тестируемость и контрактная верификация**
  1. Добавить минимальные API-тесты (unit/integration на уровень endpoint + schema validation):
     - happy-path `/v1/graph`,
     - фильтрация по `channels`,
     - `limit_nodes` truncation,
     - невалидные query-параметры (400/422),
     - health-check.
  2. Зафиксировать пример OpenAPI-схемы и пример ответа в документации.
  3. Проверить, что контракт потребляется фронтом (или зафиксировать mock-клиент в репозитории).

---

## Verification Notes
Sub-Issue считается выполненным, когда:
- `/health` и `/v1/graph` доступны в локальном запуске;
- `/v1/graph` возвращает валидный контракт `nodes + edges + meta` и корректно фильтрует publish-граф;
- CORS ограничен allowlist-ом;
- API запускается через `make api` и через Docker/Compose;
- базовые тесты endpoint проходят;
- README и OpenAPI отражают фактический контракт.

## Document package
- ADR: 
- Guide: [Semantic Graph API v1 — Guide](../docs/guides/semantic-graph-api-v1.guide.md)
- Policy: [Semantic Graph API v1 — Policy](../docs/Policy/semantic-graph-api-v1.policy.md)

## 🚚 Delivery
Branch: `codex/complete-current-sub-issue`
PR: [Codex-generated pull request#152](https://github.com/DETai-org/Knowledge_substrate/pull/152)

- [ ] **[AUDIT] Зафиксировать обязательный шаг применения миграций перед запуском API (compose/local)**
  1. В `sql/detai_core/README.md` явно добавить шаг применения SQL-миграций (`0001...0006`) до первого вызова `/health` и `/v1/graph`.
  2. Для `docker-compose` зафиксировать способ применения миграций (скрипт/команда) и порядок запуска.
  3. Добавить короткую smoke-проверку, подтверждающую наличие таблиц `knowledge.doc_metadata` и `knowledge.similarity_edges`.

- [x] **[AUDIT] Зафиксировать воспроизводимое окружение зависимостей API/тестов**
  1. Добавить manifest зависимостей API (`requirements.txt` или эквивалент) с пакетами, которые уже используются в коде и тестах.
  2. Перевести `Dockerfile` и локальные команды (`make`) на этот manifest, чтобы исключить расхождения версий.
  3. В README добавить одну команду bootstrap зависимостей для локального запуска и тестов.

