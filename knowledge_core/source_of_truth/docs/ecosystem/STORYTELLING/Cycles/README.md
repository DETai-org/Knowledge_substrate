# Cycles

Циклы — это **отдельная сущность**, объединяющая серию постов вокруг одной линии повествования.
Связь поста с циклом фиксируется в `taxonomy.cycle_ids`.

## Основные правила

- `cycle_ids` **опционально**: если пост не входит в цикл, поле **не указывается**.
- Один пост может ссылаться только на **один** цикл.
- Первый пост цикла может быть помечен как **родительский** через суффикс в `cycle_ids`.

## Формат `cycle_ids`

- Базовый идентификатор цикла: `cycle_123`
- Родительский (первый) пост цикла: `cycle_123:Post-announcement`
- Идентификатор цикла — это название цикла, приведённое к каноническому ID  
  (например, «Сказки о Северном ветре» → `cycle:skazki-o-severnom-vetre`).

## Примеры

### Первый пост цикла (родительский)

```json
{
  "taxonomy": {
    "rubric_ids": ["rubric:shadow-and-light"],
    "category_ids": ["category:top-ideas"],
    "cycle_ids": ["cycle_123:Post-announcement"]
  }
}
```

### Остальные посты цикла

```json
{
  "taxonomy": {
    "rubric_ids": ["rubric:shadow-and-light"],
    "category_ids": ["category:top-ideas"],
    "cycle_ids": ["cycle_123"]
  }
}
```

### Пост вне цикла

```json
{
  "taxonomy": {
    "rubric_ids": ["rubric:shadow-and-light"],
    "category_ids": ["category:top-ideas"]
  }
}
```
