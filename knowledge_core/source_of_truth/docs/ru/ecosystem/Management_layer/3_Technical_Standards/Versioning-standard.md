---
type: ecosystem
classification:
  scope: ecosystem
  context: management-layer
  layer: technical-standards
  function: standard
descriptive:
  id: management-layer-3-technical-standards-versioning-standard
  version: v1
  status: draft
  date_ymd: 2026-03-25
links:
  external_links:
    - type: "MkDocs_ru"
      url: "https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Management_layer/3_Technical_Standards/Versioning-standard/"
  document_links:
    - schema: ""
      link_type: ""
      linked_document_id: ""
title: Versioning Standard
---

# Versioning Standard  
  
Этот документ устанавливает **форматы версий**, используемые в экосистеме DET / DETai.  
  
---  
  
# 1. Версии проектов  
  
Для проектов используется двухуровневая модель версии:  MAJOR.MINOR

Примеры:  
```
0.1  
0.2  
1.0
```
  
Версия проекта отражает **завершённый этап развития системы**.  
  
Основные стадии:  

0.x → проект находится в стадии формирования  
1.0 → проект признан зрелым и стабильным
  
Версия не обязана доходить до `0.9` перед переходом на `1.0`. 
  
Переход к версии `1.0` означает:  
  
- проект выполняет свою ключевую функцию  
- система признана устойчивой  
- проект начинает приносить ожидаемый ресурс  
  
---  
  
# 2. Версии документов  
  
Для большинства документов используется одноуровневая модель:  
```
v1  
v2  
v3
```
  
Эта модель применяется для документов типов:  
  
- Explanation  
- Standard  
- Policy  
- Tutorial  
  
Каждая новая версия означает новую редакцию документа.  


Для документов у которых: 

**layer: Philosophy** или **Документов уровня Governance**

используется модель **Edition**.  
  
Пример:  
```
1st-edition  
2nd-edition  
3rd-edition 
```
---  
  
# 4. Повышение версии  
  
Версия повышается при завершении логического этапа развития.  
  
Это означает:  
  
- изменение архитектуры  
- появление нового уровня зрелости  
- изменение правил системы  
  
Версия отражает **состояние  и влияние на систему**, а не просто изменение её элементов.  
  
---  
  
# Связанные документы  
  
- [♻️ Процесс версионности](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Management_layer/2_Architecture_and_Logic/Versioning-process/)
- [Документационная архитектура экосистемы](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Management_layer/Docs-Ecosystem/documentation-architecture/)  
- [Политика метаданных документов](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Archive/document_metadata_policy/)
