---
type: ecosystem
classification:
  scope: DETai_cluster
  context: uli
  layer: technical-standards
  function: standard
descriptive:
  id: detai-u-l-i-3-technical-standards-release-fixation-standard
  version: v2
  status: active
  date_ymd: 2026-03-25
  date_update: 2026-04-30
links:
  external_links:
    - type: "MkDocs_ru"
      url: "https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/release-fixation-standard/"
  document_links:
    - schema: ""
      link_type: ""
      linked_document_id: ""
title: Release Fixation Standard
---

# Release Fixation Standard

Release Fixation Standard задаёт обязательный порядок проверки и фиксации новой версии проекта или репозитория в U.L.I.

Это стандарт 4-го этапа производственного цикла проектов: он применяется после выполнения Work Package и перед переходом к Documentation Architecture.

Release Fixation подводит итог уже выполненной работе. Он не создаёт основу цикла, а проверяет, можно ли признать достигнутое состояние устойчивой версией.

## 1. Purpose

Release Fixation фиксирует момент, когда результат Epic Issue или другого завершённого цикла работы может быть признан новой версией проекта / репозитория.

Версия не повышается автоматически после merge. Она фиксируется только после проверки, что фактическое состояние проекта соответствует заявленному результату и не содержит известных блокирующих рисков.

Implementation завершает работу; Release Fixation подтверждает, что результат можно признать версией.

## 2. Место в производственном цикле

Release Fixation находится между этапами:

```text
3. Implementation -> 4. Release Fixation -> 5. Documentation Architecture
```

На этапе Implementation команда или Codex выполняет Work Package, закрывает checklist и готовит PR.

На этапе Release Fixation проверяется весь достигнутый результат в целом: не только то, что было запланировано, но и то, что стало видно после реализации.

## 3. Release Gate

Версия может быть зафиксирована только если:

- Scope Epic Issue или релизного цикла выполнен либо отклонения явно зафиксированы.
- Все обязательные Work Package закрыты, смёрджены или явно сняты с текущего релиза.
- Фактическое состояние репозитория соответствует заявленному target state.
- Нет известных критических багов, security, data integrity или architecture integrity рисков.
- Проверено, что реализация не оставила незавершённых обязательных зависимостей.
- README, changelog, release notes или другие release-facing материалы готовы к обновлению либо явно не требуются.
- Понятно, какие документы должны перейти на этап Documentation Architecture.

## 4. Источники истины

При фиксации версии используются:

- Epic Issue или другой верхнеуровневый контейнер релизного цикла;
- закрытые Sub-Issue / Work Package;
- связанные PR и merge history;
- фактическое состояние репозитория;
- README, changelog, release notes и другая проектная документация;
- результаты финальной проверки;
- выявленные расхождения между планом и реальностью.

Если между закрытыми задачами и фактическим состоянием репозитория есть расхождение, приоритет имеет фактическое состояние.

## 5. Возможные решения gate

### 5.1 Release Approved

Релиз одобрен, если достигнутое состояние соответствует заявленному результату и нет блокирующих рисков.

### 5.2 Release Blocked

Релиз блокируется, если обнаружена проблема, без исправления которой нельзя честно признать версию устойчивой.

Если блокирующую проблему обнаруживает Codex-агент, он должен создать GitHub Issue в соответствующем репозитории с типом Bug.

### 5.3 Release With Known Limitations

Релиз может быть одобрен с known limitations, если ограничения не являются критическими и не противоречат заявленному target state.

## 6. Release Summary

Каждая фиксация версии должна иметь краткий release summary.

Минимальная структура:

```markdown
# Release Summary vX.Y: <название версии / этапа>

## Target State
Кратко: какое устойчивое состояние проекта достигнуто.

## What Changed
Что вошло в релиз: ключевые изменения, PR, Work Package.

## Verification
Что было проверено перед фиксацией версии.

## Known Limitations
Что известно, но не блокирует релиз.

## Carried Forward
Что переносится в следующий цикл.

## Links
- Epic Issue / release cycle
- PR
- Git tag
- GitHub Release
- README / changelog / release notes
```

Release Summary должен подводить итог фактическому состоянию, а не пересказывать план в Epic Issue.

## 7. Outputs

Успешная Release Fixation обычно создаёт или обновляет:

- Git tag;
- GitHub Release;
- release summary;
- README, release notes, если применимо;
- ссылки на Epic Issue, Work Package и PR;
- список документов, которые нужно обновить на этапе Documentation Architecture.

## Связанные документы

- [Производственный цикл проектов и карта ролей вокруг него](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/2_Architecture_and_Logic/production-cycle/) — показывает место Release Fixation как 4-го этапа цикла.
- [Work Model](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/work-model/work-model/) — описывает выполнение Work Package до этапа фиксации релиза.
- [♻️ Процесс версионности в U.L.I.](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/Versioning-in-U.L.I/) — объясняет смысл версий проектов в U.L.I.