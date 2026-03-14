---
title: Документация как исполняемый интерфейс для агентов и людей
date_ymd: 2026-03-07
type: explanation
layer: architecture-and-logic
scope: ecosystem
authority: governing
context: management-layer
version: v1
status: active
---
# Документация как исполняемый интерфейс для агентов и людей

Фраза **“docs as executable interface for agents”** — это не официальный стандарт с одним каноническим названием, а скорее **удачная формулировка для реально складывающегося паттерна**: документация перестаёт быть просто текстом “для людей” и становится **операционной средой для агентов** — источником правил, контекста, схем действий и ограничений. Это хорошо бьётся с тем, куда в 2025–2026 уехал рынок: OpenAI прямо продвигает agents, structured outputs, tool use и production best practices; Anthropic отдельно пишет уже не только про prompt engineering, а про **context engineering**; а MCP оформился как стандартный способ подключать данные, инструменты и workflow к AI-системам. ([OpenAI](https://openai.com/index/new-tools-for-building-agents/?utm_source=chatgpt.com "New tools for building agents"))

# 🧠 В чём сама идея

Раньше документация в основном отвечала на вопрос:  
**“Как человеку понять систему?”**

Теперь всё чаще нужен второй вопрос:  
**“Как агенту безопасно и предсказуемо действовать внутри системы?”**

Когда агент получает доступ к tools, API, файловой системе, GitHub, браузеру или CRM, ему уже мало “просто знаний”. Ему нужны: чёткие инструкции, иерархия правил, допустимые действия, форматы входа/выхода, критерии завершения задачи, маршруты эскалации и проверяемые ограничения. Именно поэтому OpenAI в материалах по агентам делает акцент на structured outputs, defined tools и guardrails, а Anthropic — на качественную организацию контекста. ([OpenAI Разработчики](https://developers.openai.com/cookbook/topic/agents/?utm_source=chatgpt.com "Agents • Cookbook"))

# ⚙️ Что меняется по сути

Когда документация хороша только “для чтения”, агент вынужден импровизировать.  
Когда документация структурирована, версиями закреплена и привязана к инструментам, она начинает работать как:

**docs → policy → action surface**

То есть документ уже не просто объясняет, а задаёт:  
какие инструменты можно вызвать, в какой последовательности, с какими параметрами, при каких условиях, и что считать корректным результатом. MCP здесь особенно показателен: он стандартизирует подключение AI-приложений к внешним данным и инструментам, а tools в MCP описываются через схемы и метаданные, чтобы модель могла вызывать их предсказуемо. Это очень близко к идее “док как интерфейс”. ([anthropic.com](https://www.anthropic.com/news/model-context-protocol?utm_source=chatgpt.com "Introducing the Model Context Protocol"))

# 📚 Почему это похоже на то, что строим МЫ

Потому что у нас уже есть почти все ключевые кирпичи этой архитектуры:

**1. Source of Truth**  
Мы не относимся к текстам как к “заметкам ради заметок”. У нас документы, схемы, frontmatter, статусы, рубрики, governance-слой, management-слой и публикационные сущности уже строятся как система, а не как хаос. Именно такой подход нужен агентам: им нужен канонический источник, а не десять противоречащих друг другу текстов. Это совпадает с best practices OpenAI по production и с идеей governed agents. ([OpenAI Разработчики](https://developers.openai.com/api/docs/guides/production-best-practices/?utm_source=chatgpt.com "Production best practices | OpenAI API")) 

**2. Версионность**  
Мы  думаем в логике v0.1, v0.2, стандартов, evolving docs. Это критично, потому что агент должен знать не просто “правило”, а **какая версия правила сейчас действующая**. OpenAI отдельно рекомендует pinning и evals при изменении моделей и промптов, а это та же логика: поведение системы должно быть воспроизводимым и управляемым по версиям. 

Мировой тренд смотри в ([OpenAI Разработчики](https://developers.openai.com/api/docs/guides/prompt-engineering/?utm_source=chatgpt.com "Prompt engineering | OpenAI API")) 
У нас смотри в [[Versioning-in-U.L.I|♻️ Процесс версионности в U.L.I.]]

**3. Таксономия и схемы**  
Наши distinctions между document / concept / rubric / category / schema — это не бюрократия. Для агента это способ понять, что перед ним: policy, reference, workflow, draft, canonical definition, publication metadata или operational playbook. Чем яснее тип сущности, тем лучше agent routing и меньше галлюцинаций на уровне процесса. Это согласуется с общим движением в сторону structured outputs, tool schemas и context engineering.

Мировой тренд смотри в ([OpenAI Разработчики](https://developers.openai.com/tracks/building-agents/?utm_source=chatgpt.com "Building agents"))
У нас смотри в [[documentation-architecture-U-L-I|Документационная архитектура U.L.I.]]

**4. Документы как рамка действия**  
Мы уже строим governance-документы, onboarding, процессы, роли, стандарты. Это почти буквально то, что OpenAI в руководстве по governed AI agents называет scaffolding и governance: агентам нужны рамки, в которых они действуют безопасно и масштабируемо. ([OpenAI Разработчики](https://developers.openai.com/cookbook/examples/partners/agentic_governance_guide/agentic_governance_cookbook/?utm_source=chatgpt.com "Building Governed AI Agents - A Practical Guide to ..."))

# 🔥 Почему это особенно важно именно в 2025–2026

Потому что индустрия сдвигается от “один хороший ответ в чате” к “длинные цепочки действий с инструментами”. OpenAI в 2025 выпустила блоки именно для building agents; Anthropic в 2025 уже пишет про effective context engineering и effective harnesses for long-running agents; MCP за это время стал заметным межплатформенным стандартом для подключения контекста и tools. Из этого следует важный вывод: **качество агента всё больше определяется не только моделью, но и тем, как организованы контекст, инструменты и правила вокруг неё**. Это уже не inference “из воздуха”, а общий вектор платформ. ([OpenAI](https://openai.com/index/new-tools-for-building-agents/?utm_source=chatgpt.com "New tools for building agents"))

# 🧩 Как это выглядит практически

Представь два уровня документации.

### Уровень A — человеческий

Документ объясняет:

- что такое DET
    
- как устроен onboarding
    
- что значит статус draft
    
- кто за что отвечает

### Уровень B — агентный

Этот же документ или соседний machine-readable слой задаёт:

- допустимые tool calls
    
- required fields
    
- decision rules
    
- validation checks
    
- stop conditions
    
- escalation path
    
- ссылку на canonical schema
    
- версию политики
    

И вот во втором случае документация уже становится **исполняемой на практике**, даже если не “исполняется” напрямую как код. Агент читает её, интерпретирует и действует по ней. OpenAI рекомендует structured outputs именно для таких сценариев, когда результат должен использоваться приложением, а не просто показываться человеку. ([OpenAI Разработчики](https://developers.openai.com/tracks/building-agents/?utm_source=chatgpt.com "Building agents"))

# 🛠️ Во что это можно превратить у нас

Вот где наша экосистема реально может выстрелить.

## 1. Governance docs → policy layer for agents

Наши governance / management / operational документы можно оформить так, чтобы агент понимал:

- где он вообще имеет право действовать
    
- какие действия требует approval
    
- какие репозитории канонические
    
- какие ветки/файлы можно менять автоматически
    
- когда нужно создать issue вместо прямого edit
    

Это будет уже не просто governance “для команды”, а **governance for humans + agents**. Такой подход хорошо сочетается с governed agents и enterprise scaffolding. ([OpenAI Разработчики](https://developers.openai.com/cookbook/examples/partners/agentic_governance_guide/agentic_governance_cookbook/?utm_source=chatgpt.com "Building Governed AI Agents - A Practical Guide to ..."))

## 2. Onboarding → agent-readable tutorial graph

Дальше наши 🎓 Tutorial в Onboarding можно сделать такими, чтобы агент не просто “пересказывал” их, а реально умел:

- определить следующий шаг
    
- проверить результат шага
    
- понять, где пользователь застрял
    
- выбрать релевантный документ
    
- не путать conceptual onboarding с operational onboarding
    

Это уже почти готовая агентная навигация.

## 3. GitHub + docs → execution cockpit

Так как у нас GitHub и документация уже тесно связаны, можно прийти к схеме:

**issue → sub-issue → policy docs → schema docs → tool execution → PR → validation**

То есть агент получает issue, подтягивает канонические документы, выполняет работу в разрешённых границах и возвращает результат в стандартизированном формате. Это прямое продолжение идеи agents + tools + structured outputs.

Мировой тренд смотри в ([OpenAI](https://openai.com/index/new-tools-for-building-agents/?utm_source=chatgpt.com "New tools for building agents"))
У нас смотри в [[work-model|Work Model]] 

*Т.е. уже есть стандарт о создании первых двух звеньев этой цепочки*

## 4. Obsidian / knowledge substrate → context server

С учётом того, что MCP стандартизирует доступ к данным и инструментам, наша knowledge substrate (база знаний) в будущем очень естественно превращается в **контекстный сервер для агентов**: агент не “помнит всё”, а запрашивает нужный канонический контекст из базы знаний. Это одна из самых сильных точек соприкосновения с текущим мышлением. 

Мировой тренд смотри в ([anthropic.com](https://www.anthropic.com/news/model-context-protocol?utm_source=chatgpt.com "Introducing the Model Context Protocol"))
У нас смотри в [[Ecosystem/Infrastructure/Knowledge_Substrate/index|index]] 

# 🧪 Самая важная мысль

Буду очень точен:  
**документы не становятся кодом в буквальном смысле автоматически.**

Но они становятся **контрактом между моделью, инструментами и системой**.  
И чем лучше этот контракт структурирован, тем меньше нужно “магии”, тем надёжнее агент, тем проще масштабирование на новые модели и инструменты. Это и есть причина, почему наша тяга к схемам, таксономии, статусам, canonical docs и versioning — не бюрократия, а очень современная архитектурная линия. Она совпадает с тем, как индустрия переходит от prompt-centric мышления к context/tool/governance-centric мышлению. ([anthropic.com](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents?utm_source=chatgpt.com "Effective context engineering for AI agents"))

# Куда двигаться дальше ❓

Если смотреть на это стратегически, нам стоит проектировать документы сразу в двух проекциях:

**для человека**  
понятно, живо, концептуально, объясняюще

**для агента**  
структурно, однозначно, версионируемо, с явными правилами и схемами

То есть рядом с каждым важным классом документов со временем полезно иметь:

- canonical purpose
    
- scope
    
- authority level
    
- input/output schema
    
- allowed actions
    
- validation rules
    
- linked tools/repos
    
- version / status
    
- escalation / fallback
    

Это уже очень близко к “документация как исполняемый интерфейс”.

# 💡 Если собрать всё в одну формулу

То, что мы строим, можно осмыслить так:

**Source of Truth → Context Layer → Policy Layer → Agent Action Layer**

И в этом смысле мы двигаемся не просто к “хорошо организованной базе знаний”, а к **будущей операционной среде для людей и AI-агентов одновременно**. Это и делает нашу архитектуру настолько созвучной тренду 2025–2026. ([modelcontextprotocol.io](https://modelcontextprotocol.io/?utm_source=chatgpt.com "Model Context Protocol"))

