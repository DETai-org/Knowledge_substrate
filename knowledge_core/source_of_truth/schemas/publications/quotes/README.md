# Quote Schema

`schemas/publications/quotes/` хранит контракт документов типа `quote`.

Здесь фиксируются:
- структура Quote Record;
- правила атрибуции;
- правила хранения asset references;
- границы между canonical quote data и производными binary assets.

Основной контракт:
- `quote_record_contract.md`

Связь с другими слоями:
- сами quote-документы должны жить в `source_of_truth/docs/publications/quotes/`;
- SQL-нормализация для query/core layer относится к производному operational представлению, а не к каноническому документу;
- project runtime data пользователей не относятся к этому каталогу и должны жить вне publications schema.
