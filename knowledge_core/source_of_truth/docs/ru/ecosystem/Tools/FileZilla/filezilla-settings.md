---
type: ecosystem
classification:
  scope: Tools
  context: filezilla
  layer: null
  function: explanation
descriptive:
  id: tools-filezilla-filezilla-settings
  version: v1
  status: active
  date_ymd: 2026-03-25
links:
  external_links:
    - type: "MkDocs_ru"
      url: "https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Tools/FileZilla/filezilla-settings/"
  document_links:
    - schema: ""
      link_type: ""
      linked_document_id: ""
title: Настройки FileZilla
---

# Настройки FileZilla



📂 **Путь к конфигурационным файлам FileZilla (Windows):**

```
C:\Users\PC\AppData\Roaming\FileZilla
```
___

### 1.🔧 Удаление старых подключений (например, при смене IP):

1. Перейди в директорию 
2. Открой файл `recentservers.xml` в любом текстовом редакторе
3. Найди блок `<Server>...</Server>`, содержащий старый IP (например, `51.250.69.23`).
4. Удали **весь соответствующий блок**, включая открывающий и закрывающий теги `<Server>` и `</Server>`.
5. Перезапусти FileZilla — строка исчезнет из истории подключений.

---

> [!TIP] Быстрое редактирование IP без удаления строки  
> Можно просто заменить IP-адрес в нужном `<Host>` внутри блока `<Server>`, если хочешь сохранить остальные данные (логин, порт, способ входа).

___

### 🚀 Как правильно подключиться приватный ключ в FileZilla:

1. Открой FileZilla.
    
2. В меню сверху: редактирование → Настройки → SFTP**.

добавили  ключ, файл:
    
``` 
C:\Users\PC\.ssh\id_ed25519
```

    (именно приватный ключ, без `.pub`).
    
