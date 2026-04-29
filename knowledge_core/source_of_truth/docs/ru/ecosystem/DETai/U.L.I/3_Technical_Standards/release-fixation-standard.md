---
type: ecosystem
classification:
  scope: DETai_cluster
  context: uli
  layer: technical-standards
  function: standard
descriptive:
  id: detai-u-l-i-3-technical-standards-release-fixation-standard
  version: v1
  status: draft
  date_ymd: 2026-03-25
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

_(стандарт фиксации перехода версии и архивирования состояния системы)_

---

## Purpose

Этот стандарт задаёт единый и воспроизводимый способ фиксировать **переход проекта/репозитория в новое состояние зрелости** через версию.

В экосистеме DET / DETai версия повышается **не в процессе работы**, а только в момент, когда завершён целостный логический этап и принято управленческое решение: «это состояние достаточно устойчиво, чтобы его зафиксировать».  
В этот момент:

- формируется архивный `Epic_issue` файл, фиксирующий достигнутое состояние и закрывается соответствующий этап работы (как завершённый переход состояния),
    
- создаётся Git-тег,
    
- публикуется GitHub Release,
    
- обновляется блок версии в README,
    
Версия — это **точка фиксации состояния системы**, к которой можно вернуться и которую можно сравнивать с другими такими точками в будущем.

Связанные документы:  
— [♻️ Процесс версионности в U.L.I.](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/Versioning-in-U.L.I/)  
— [Work Model](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/work-model/work-model/)  
— [issue-contract](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/work-model/issue-contract/)  

---

## 1️⃣ Контекст в системе работы

В рамках [Work Model](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/work-model/work-model/) сложная работа организуется как:

Epic Issue → Sub-Issue → PR → новое функциональное состояние.

Завершение Epic Issue означает **переход системы в новое состояние**, и в зависимости от контекста этот переход может быть зафиксирован как новая версия.

Release Fixation Standard описывает правила фиксации этого перехода как версии — так, чтобы история развития проекта сохранялась однотипно и оставалась анализируемой через годы.

---

## 2️⃣ Два режима фиксации

### 2.1 Living Epic (режим выполнения)

Epic Issue ведётся как рабочий процесс в GitHub и оформляется по стандарту [issue-contract](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/work-model/issue-contract/).  
Epic дробится на Sub-Issue (Work Packages) по стандарту [sub-issue-contract](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/work-model/sub-issue-contract/).

Это режим, в котором работа выполняется, расширяется, уточняется, и заканчивается мерджами PR.
### 2.2 Release Fixation (режим архивирования)

После того как достигнуто целевое состояние Epic (переход системы завершён), создаётся отдельный архивный `Epic_issue` файл в папке `issue/`, к


---

## 3️⃣ Обязательная цепочка фиксации

Каждый переход версии проекта должен следовать одной и той же последовательности:

1. `Epic_issue` файл оформлен.
    
2. Epic Issue закрыт.
    
3. Создан Git-тег (`vX.Y`).
    
4. Опубликован GitHub Release.
    
5. README обновлён (версия, статус, даты).
    

Принцип: одна и та же цепочка каждый раз.

---

## 4️⃣ Источники истины при фиксации версии

При создании `Epic_issue` файла используются два источника:

**A) закрытые Sub-Issue**

**B) Фактическое состояние репозитория**

Если работа шла без полного разворачивания Epic → Sub-Issue, архивный `Epic_issue` файл всё равно создаётся и опирается на репозиторий как на фактический срез состояния.

---

## 5️⃣ Структура Epic_issue файла (обязательная)

Структура `Epic_issue` файла задаётся отдельным шаблоном и должна строго соответствовать формату 

Рекомендуемый объём: 1–2 страницы Markdown.

Вот формат
```md

# Epic Issue vX.Y: <Название этапа> 

<Epic Issue Title>


## 🎯 Goal (Target State)

Что система уже реально умеет делать в этой версии.  
Фокус — на функциональном состоянии, а не на списке изменений.
Что стало «целостным»
Ключевые пользовательские сценарии (Маршруты или действия)
Ключевые страницы / разделы / модули / скрипты /Компоненты / утилиты 
Короткая тех-фиксация (если применимо но без количественных метрик ради метрик)

---

## 📦 Scope (Frame of Change)
**In scope:** …
**Out of scope:** …

___

## Sub-Issue 

Тут фиксируем:

1. Чекбоксы отражают факт достижения результата один чекбокс на один закрытый sub-issue, 

2. DoD (чеклист) на основе анализа репозитория и выявление тех моментов которые не были зафиксированы в Sub-Issue

---

## Мостик к следующему Epic

Краткое описание следующего целевого состояния. Опираясь на текущее состояние, логично описать  какие есть явные недочёты в текущей структуре, которые требуют доработки в дальнейшем, и так далее. Это проводится на основе "🧠Еще мысль", либо на основе строгого анализа репозитория. 

---

## Ссылки

Минимальный блок ссылок:

- README  
- Git-тег (после создания)
- Последний PR
  
```
🫱 *Нужно следить, чтобы этот шаблон соответствовал той структуре, которая указана в стандарте* [issue-contract](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/work-model/issue-contract/)
*Но при этом данная структура может расширять ту структуру, потому что исторически этот стандарт подводит итог, а не создает основу.*

---

## 8️⃣ Автоматизация

Для ускорения создания `Epic_issue` файла используется промпт: [Create Epic Issue Release](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Tools/🧭Codex/create-epic-issue-release/)

Промпт должен:

- анализировать закрытые Sub-Issue (если они есть),
    
- анализировать текущее состояние репозитория,
    
- собирать итоговый `Epic_issue` файл в соответствии с настоящим стандартом и утверждённой структурой.


