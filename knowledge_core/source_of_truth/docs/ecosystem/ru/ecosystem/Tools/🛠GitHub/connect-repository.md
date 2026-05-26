---
type: ecosystem
classification:
  scope: Tools
  context: github
  layer: null
  function: explanation
descriptive:
  id: tools-github-connect-repository
  version: v1
  status: active
  date_ymd: 2026-03-25
links:
  external_links:
    - type: "MkDocs_ru"
      url: "https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Tools/🛠GitHub/connect-repository/"
  document_links:
    - schema: ""
      link_type: ""
      linked_document_id: ""
title: Подключить репозиторий
---

# Подключить репозиторий

Инструкция описывает ручное подключение нового репозитория к GitHub и локальной рабочей машине.

Старая схема фоновой автосинхронизации GitHub ↔ сервер выведена из активного контура. Новая практика: работаем осознанно в локальном репозитории, делаем явные коммиты и пушим изменения в GitHub.

---

## Перед началом

Убедись, что:

- на рабочей машине настроен доступ к GitHub;
- выбран корректный локальный каталог проекта;
- в репозиторий не попадут секреты, `.env`, session-файлы, runtime-state и приватные ключи.

Проверить SSH-доступ:

```bash
ssh -T git@github.com
```

Если GitHub отвечает успешной аутентификацией, доступ готов.

---

## Создать репозиторий

На GitHub:

- создай репозиторий в организации `DETai-org`;
- не добавляй стартовые `README.md` и `.gitignore`, если локальный проект уже содержит файлы;
- выбери `private`, если проект содержит внутреннюю логику, операционные инструкции или чувствительные данные.

---

## Подключить локальную папку

В локальной папке проекта:

```bash
git init
git branch -M main
git remote add origin git@github.com:DETai-org/ИМЯ_РЕПОЗИТОРИЯ.git
git status
```

Проверь `.gitignore`, затем:

```bash
git add .
git commit -m "Initial project import"
git push -u origin main
```

Если репозиторий на GitHub уже содержит историю:

```bash
git pull origin main --allow-unrelated-histories
```

После ручного разрешения конфликтов снова выполни commit и push.

---

## Проверка

После push проверь:

- GitHub показывает актуальные файлы;
- `git status` локально чистый;
- секреты и runtime-артефакты не отслеживаются;
- README содержит команды запуска и путь к server-local env, если проект деплоится на сервер.

---

## Сервер

Если проект нужен на сервере, клонируй его явно:

```bash
cd /home/psy-ru
git clone git@github.com:DETai-org/ИМЯ_РЕПОЗИТОРИЯ.git
```

Секреты хранятся вне git, например в:

```bash
/home/psy-ru/server-operations/env
```

Автоматический фоновый sync больше не является стандартом подключения репозитория.
