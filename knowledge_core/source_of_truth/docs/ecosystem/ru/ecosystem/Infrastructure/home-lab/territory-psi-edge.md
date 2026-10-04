---
type: ecosystem
classification:
  scope: Infrastructure
  context: servers
  layer: architecture-and-logic
  function: explanation
descriptive:
  id: infrastructure-home-lab-territory-psyche-edge
  version: v1
  status: active
  date_ymd: 2026-10-04
governance:
  canonicality: canonical
  visibility: public
object_state:
  architecture_status: canonical
  implementation_status: operational
  evidence_status: validated-within-scope
  visibility_status: public
links:
  external_links:
    - type: "MkDocs_ru"
      url: "https://docs.detai-x.com/ru/ecosystem/Infrastructure/home-lab/territory-psi-edge/"
    - type: "GitHub"
      url: "https://github.com/DETai-org/Infrastructure/tree/main/home-psi-lab/territory-psyche"
  document_links:
    - schema: ecosystem
      link_type: belongs-to
      linked_document_id: infrastructure-home-lab
title: Territory Ψ Edge — дачный контур Home Ψ Lab
---

# Territory Ψ Edge

**Territory Ψ Edge** — отдельный дачный infrastructure-контур внутри
[Home Ψ Lab](index.md) и физический сетевой слой
[Территории Психеи](https://detai-x.com/p/territory-psyche). Территория Психеи
задумана как место для очной психотерапии, групповых форматов, тренингов,
семинаров и мастер-классов, поэтому инфраструктура здесь является частью среды,
а не отдельным пользовательским продуктом.

Главный принцип контура прост: **сложность должна оставаться внутри
Infrastructure**. Посетителю не нужно понимать, какой LTE-канал сейчас работает,
как устроены туннели или где проходит граница между дачей и городом. Для него
связь должна быть такой же базовой частью пространства, как свет, электричество
или готовая аудитория: она просто работает.

## Место в Home Ψ Lab

Home Ψ Lab — собирательное название инфраструктуры на собственном оборудовании.
Городской Beelink / Proxmox даёт общие сетевые и вычислительные среды, а
Territory Ψ Edge имеет собственный физический edge на Dell Wyse и собственную
локальную сеть. Городские компоненты могут предоставлять дачному контуру
network capability, но место размещения не смешивает ответственность: дачный
контур остаётся самостоятельной площадкой внутри общей инфраструктурной группы.

В пользовательском слое это выражено двумя сетями: **Local** даёт обычный
прямой доступ через доступный LTE, а **World** использует защищённый городской
egress. Технические детали failover, маршрутизации, management и конкретной
топологии не являются предметом этой страницы.

## Почему это связано с психотерапией

Territory Ψ Edge сам не ведёт терапию и не создаёт образовательную программу.
Его роль — подготовить среду до того, как в ней появится человек. Хорошая
инфраструктура чаще всего заметна тогда, когда её нет; когда она сделана хорошо,
она может оставаться почти невидимой. В этом смысле контур продолжает общий
принцип DETai: технология имеет ценность не сама по себе, а когда освобождает
пространство для человеческой, профессиональной и образовательной работы.

Технический desired state, оборудование и эксплуатационная документация
ведутся в репозитории
[Infrastructure / Territory Ψ Edge](https://github.com/DETai-org/Infrastructure/tree/main/home-psi-lab/territory-psyche).
Эта страница фиксирует только устойчивый смысл, архитектурную границу и связь
контура с Home Ψ Lab и Территорией Психеи.
