# Cross‑site ссылки между detai‑site и personal‑site

Этот файл объясняет простой формат ссылок, которые автоматически подставляют домен и язык. Он нужен, чтобы в тексте постов не менять URL при переезде на новый домен.

## ✅ Синтаксис

Используйте макрос‑ссылки в Markdown:

- `site:personal:blog/<slug>` — ссылка на персональный сайт.
- `site:detai:blog/<slug>` — ссылка на профессиональный сайт.
- `site:personal:post:<postId>` / `site:personal:id:<postId>` — ссылка на пост по ID (slug подставится автоматически).
- `site:detai:post:<postId>` / `site:detai:id:<postId>` — ссылка на пост по ID (slug подставится автоматически).

`<slug>` — это путь поста без языка, например `sila-i-svet-haus-i-mrak`.
`<postId>` — это ID поста из frontmatter.

## ✅ Что подставляется автоматически

1. **Язык** — берётся из текущего языка поста (`ru`, `en` и т.д.).
2. **Домен** — берётся из `.env.local`:
   - `NEXT_PUBLIC_PERSONAL_SITE_URL`
   - `NEXT_PUBLIC_DETAI_SITE_URL`

## ✅ Примеры

**RU** (пост на русском):

```
[Сила и свет, хаус и мрак](site:personal:blog/sila-i-svet-haus-i-mrak)
```

В итоге это станет:

```
https://personal-site.example/ru/blog/sila-i-svet-haus-i-mrak
```

**EN** (пост на английском, slug подставится автоматически по postId):

```
[Light and shadow](site:personal:post:detai-limbo-2024)
```

В итоге это станет:

```
https://personal-site.example/en/blog/light-and-shadow
```

## ✅ Когда использовать slug, когда postId

| Сценарий | Что использовать | Почему |
| --- | --- | --- |
| Slug одинаковый во всех языках | `site:<key>:blog/<slug>` | Быстрее и короче. |
| Slug отличается между языками | `site:<key>:post:<postId>` / `site:<key>:id:<postId>` | Slug подставится автоматически для текущего языка. |

Если slug различается между языками — используйте postId‑макрос.

## 🔧 Использование helper в разделе концепции DET

В `detai-site/lib/concept/externalLinks.ts` используется helper `buildPersonalBlogUrl(slug, lang)`: он собирает URL вида `${base}/${lang}/blog/${slug}` на основе `NEXT_PUBLIC_PERSONAL_SITE_URL` и `NEXT_PUBLIC_DETAI_SITE_URL`, с удалением конечного `/` у домена.

Сейчас helper применяется только в страницах концепции:
- `detai-site/app/(det)/det/concept/shadow-and-light/page.tsx`
- `detai-site/app/(det)/det/concept/overcoming/page.tsx`
- `detai-site/app/(det)/det/concept/personality-types/page.tsx`

Назначение: формировать кросс-сайтовые ссылки на рубрики блога в блоке `relatedRubric` и централизовать fallback-поведение, если env не задан.

Дополнительно в `/det/concept/*` ссылки на источники внутри текста и в блоках с материалами оформляются через `CitationDot` и helper `buildPersonalBlogUrl`, чтобы единообразно строить круглые надстрочные ссылки на релевантные посты.
