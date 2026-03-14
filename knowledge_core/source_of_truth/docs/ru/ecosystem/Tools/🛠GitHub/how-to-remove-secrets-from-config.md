---
title: Как убрать секреты из config
---


# Как убрать секреты из config


Как убрать секреты из `config.json`, но сохранить их доступность и на CI, и на сервере

## 1. Изменяем код ― читаем из ENV, а файл — только резерв

```python
# UserControl/utils/secrets.py  (пример единой точки доступа)
import os, json
from pathlib import Path

_cfg = json.loads(Path("UserControl/config.json").read_text(encoding="utf-8"))

def get(name: str) -> str | None:
    """Секрет берём из переменной окружения, а если её нет — из файла."""
    return os.getenv(name) or _cfg.get(name.lower())       # api_id → API_ID
```

_Теперь любой скрипт вместо `cfg["openai_api_key"]` делает_

```python
from utils.secrets import get
openai.api_key = get("OPENAI_API_KEY")
```

## 2. Чистим `config.json`

```json
{
  "openai_api_key": "",
  "static_bot_token": "",
  "api_id": 0,
  "api_hash": "",
  "session_string": "",
  "active_accounts": []
}
```

> Всё чувствительное — пустые строки. Файл можно смело коммитить.

## 3. Где храним реальные значения

|Среда|Хранилище|Что сделать|
|---|---|---|
|**GitHub Actions**|_Settings ▸ Secrets_|Уже добавили `OPENAI_API_KEY`, `TELEGRAM_BOT_TOKEN`…|
|**Codex контейнер**|Блок **Secrets** в UI|Тоже добавили ― под теми же именами|
|**Сервер VPS**|① файл `.env` (в `/home/admin-v-rossii/Telegram`) или ② переменные в unit-файле systemd|– Создай `.env`, положи пары `KEY=value`– Добавь `.env` в `.gitignore`, чтоб не ушёл в Git|

### Пример `.env` на сервере

```
OPENAI_API_KEY=sk-...
TELEGRAM_BOT_TOKEN=123:ABC
CHAT_ID_LOGS=-10012345
```

_Установи `python -m pip install python-dotenv` (добавь в `requirements.txt`) и в `utils/secrets.py` добавь вверху:_

```python
from dotenv import load_dotenv; load_dotenv()
```

## 4. Плюсы схемы

- **Безопасность** — секреты никогда не попадают в репозиторий.
    
- **Единый код** — на CI, Codex и сервере работает одинаково.
    
- **Простота** — поменять токен = поправить `.env` или Secret, без рекоммита.
    

---
