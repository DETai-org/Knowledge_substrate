---
type: ecosystem
title: Sites
classification:
  scope: DETai_cluster
  context: platform
  layer: null
  function: index
descriptive:
  id: detai-platform-detai-e2-brand-sites-index
  version: v1
  status: active
  date_ymd: 2026-06-12
  date_update: 2026-06-27
links:
  external_links:
    - type: "MkDocs_ru"
      url: "https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/Platform_DETai/E2-Brand/sites/"
    - type: "GitHub"
      url: "https://github.com/DETai-org/sites"
    - type: "website"
      url: "https://detai.ai/"
  document_links: null
---

# Sites

**sites** — это web-слой DET/DETai: монорепозиторий публичных Next.js-сайтов, через который экосистема становится видимой, навигационной и юридически оформленной для внешнего пользователя.

В него входят:

- `detai-site` — профессиональный сайт экосистемы DETai;
- `personal-site` — персональный сайт Антона Колхонена.

Технический источник находится в GitHub: [DETai-org/sites](https://github.com/DETai-org/sites).

## Роль в экосистеме

`sites` не является только витриной или блогом. Это интерфейсный слой, который переводит внутреннюю структуру DET/DETai в публичные маршруты, тексты, формы, карточки проектов, юридические документы и пользовательские сценарии.

Его главная функция — сделать экосистему доступной для первого контакта:

- объяснить, что такое DET и DETai;
- развести институциональные, технологические, образовательные, исследовательские и персональные контуры;
- дать человеку понятные входы: читать, изучать, вступать в контакт, отправлять заявку, перейти к Telegram/API-сценариям;
- описывать юридическую инфу

Одна из вещей, которая очень сильная, это SEO по сути сам сайт это проект второго эшелона, значит он увеличивает то, что должно увеличивать второе эшелон. Вот как раз таки SEO и прочие методанные это делают очень хорошо.

Сейчас там еще сделаны аккаунты для пользователей. 

## Что делает web-слой

`sites` собирает несколько типов поверхностей:

- **brand / explanation pages** — страницы, объясняющие DET, DETai, проекты и направления;
- **publication surfaces** — блог, публикации, цитаты и связанные SEO-страницы;
- **conversion surfaces** — формы заявок, контакты, события, onboarding-входы;
- **account surfaces** — login, signup, account overview и связанные auth-сценарии;
- **legal surfaces** — privacy, terms, cookies и project-specific notices;
- **technical launch surfaces** — noindex, public, auth-only и другие маршруты, которые должны быть явно зафиксированы перед запуском.
