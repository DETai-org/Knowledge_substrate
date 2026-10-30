---
type: ecosystem
classification:
  scope: Tools
  context: github
  layer: null
  function: how-to
descriptive:
  id: tools-github-how-to-remove-secrets-from-config
  version: v2
  status: active
  date_ymd: 2026-03-25
  date_update: 2026-10-30
links:
  external_links:
    - type: MkDocs_ru
      url: https://docs.detai-x.com/ru/ecosystem/Tools/🛠GitHub/how-to-remove-secrets-from-config/
title: Как отделить секреты от конфигурации
---

# Как отделить секреты от конфигурации

**Функция:** `how-to`. Цель: оставить несекретные режимы и настройки доступными для ревью, но **не хранить реальные credentials в Git**. Для Telegram-ботов действует [общий стандарт декларативной конфигурации DETai](../../DETai/U.L.I/3_Technical_Standards/Telegram_Bots/configuration-standard.md).

## 1. Определи, что является секретом

| Несекретная конфигурация (JSON/TOML) | Приватные credentials (секретный ENV) |
| --- | --- |
| Имя и Telegram Bot ID, профиль DEV/Production, аудитория `pilot/public`, публичный URL, технические feature flags | Bot token, API keys, SQL-пароль/полный connection URL с credentials, Commerce signing/service tokens, OAuth secrets |
| Режим и списки допуска **в приватном owning repository** с ограниченным доступом | Секреты **никогда** не становятся содержимым versioned JSON или README |

Telegram ID или username участника — это не пароль, но идентификатор человека. Их нельзя автоматически публиковать в открытом репозитории или MkDocs.

## 2. Загрузчик: никакого fallback к секрету в JSON

Плохая схема: `os.getenv("API_KEY") or config_json["api_key"]`. Она позволяет «временно» вернуть ключ в Git и оставляет два источника.

Python-пример чтения **уже загруженной** переменной:

```python
import os

def required_secret(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"Missing required secret: {name}")
    return value
```

Для TypeScript/Node.js принцип тот же: один централизованный загрузчик проверяет обязательные ключи для **конкретного процесса**. JSON/TOML отдельно проходят валидацию схемы, типов и выбранного профиля. Если секрет отсутствует, защищённую операцию нельзя продолжать со случайным fallback.

## 3. Один источник секретов на окружение продукта

- **Локально:** ignored `config/secrets.env` и tracked `config/secrets.env.example` с пустыми или явно фиктивными значениями.
- **На сервере:** один приватный файл секретов на окружение продукта **вне checkout**, с минимально необходимыми правами доступа. Секретные значения не вписывают напрямую в `systemd` unit или командную строку.
- **В CI:** используется защищённое хранилище secrets самого CI, передаваемое только нужному job. Не предполагайте, что какие-то ключи там уже настроены: проверяйте фактическое подключение.
- **Несколько процессов:** единый физический файл bot/API/worker/Commerce допустим, но процесс должен получать только нужный набор ключей. Если все процессы имеют OS-доступ к общему файлу, это **одна граница доверия**; allowlist переменных сам по себе не обеспечивает OS-изоляцию.

Пример **шаблона**, не настоящих значений:

```dotenv
TELEGRAM_BOT_TOKEN=REPLACE_PRIVATELY
DATABASE_URL=REPLACE_PRIVATELY
OPENAI_API_KEY=REPLACE_PRIVATELY
```

Списки участников, режимы и Bot ID размещаются в реальной несекретной декларативной конфигурации; `secrets.env` не превращается в огромный второй `config.json`.

## 4. Переход без второго источника

1. Найдите все реальные чтения старых JSON/ENV и распределите поля по `secret`, `profile selector`, `non-secret`, `retired`.
2. Подключите новый загрузчик и шаблон, оставив реальные секреты **вне** Git. Убедитесь, что по завершении миграции нет второго приоритета из cwd/`.env.local` и неиспользуемого JSON.
3. Проверьте недостающий/неверный секрет, соответствие Telegram `getMe` ожидаемому Bot ID, выбранный профиль и безопасное прекращение запуска. Никогда не проверяйте работу путём публикации реального ключа в логе.
4. Отдельно подтвердите операторский cutover/restart в owning repository. Merge сам по себе не переносит секреты и не меняет работающий сервис.

**Не копируйте в чат или PR содержимое приватных ENV, токены, платежные квитанции, дампы БД и полные системные журналы.** Для совместной диагностики достаточно имён ключей, маскированных свидетельств, состояний и проверяемого SHA конфигурации без приватных значений.
