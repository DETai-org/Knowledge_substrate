---
title: "Psychology in Quotes — Architektur und Vertrauen"
description: "Die Rolle von PiQ in DETai sowie Zuständigkeiten für Accounts, API, Datenschutz und Veröffentlichungen."
lang: de
translation_of: /ru/ecosystem/DETai/Platform_DETai/products/psychology-in-quotes/architecture-and-trust/
---

# Wie das Produkt funktioniert und warum Vertrauen wichtig ist

## Die Rolle von PiQ innerhalb von DETai

- **DETai** ist ein Ökosystem aus Psychotherapie, Forschung, Bildung, Technologie und Gemeinschaft.
- **Platform DETai** ist die Produkt- und Technologieschicht sowie die verbundene digitale Umgebung.
- **Psychology in Quotes** ist ein digitales Produkt für Bildung und Wissensvermittlung (primäre Nutzerfunktion), ergänzt um Veröffentlichung und kreative Arbeit. Seine **E2 Brand**-Rolle besteht darin, psychologisches Wissen zu verbreiten und Bekanntheit sowie Vertrauen zu fördern.
- **DETai Account** bietet eine gemeinsame Identität für Website und verbundenes Telegram. Die Registrierung allein gewährt aber keine Rechte an fremden Zitaten.

[DETai-Ökosystem](../../../index.md) · [Platform DETai](../../index.md) · [PiQ-Produktseite](https://detai-x.com/de/technology/platform/psychology-in-quotes).

## Zwei unabhängige Dimensionen der Positionierung

| Frage | Antwort für PiQ |
| --- | --- |
| Welchen Nutzen haben Menschen? | Selbstbestimmtes Lernen durch psychologische Gedanken, Lesen und bewusstes Bewahren von Zitaten |
| Was können sie außerdem tun? | Zitatkarten und Stories erstellen, Inhalte veröffentlichen und teilen |
| Was ist der wichtigste Beitrag zu DETai? | Wissensvermittlung, Vertrauen und Bekanntheit — **E2 Brand** |
| Was verspricht PiQ nicht? | Formale Bildungsprogramme, Zertifikate, Diagnosen oder Psychotherapie |

Diese Trennung ist im [Produktobjektmodell](../../../../../product-market/product-object-model.md) und in der [Logik der Echelons](../../../logic-of-echelons.md) festgelegt. Eine Bildungsfunktion führt nicht automatisch zur Zuordnung zu E1.

## Abgrenzung der Zuständigkeiten

| Oberfläche | Zuständig für | Kein maßgeblicher Ursprung von |
| --- | --- | --- |
| Website `detai-x.com` | Darstellung, Webbereich, Zitate, Katalog, SEO, Rechtsdokumente | Eigenständigen Tarifrechten oder privater SQL-Datenbank |
| PiQ-Telegram-Bot | Erstellungsassistent, Sammlung, Interaktionen und Veröffentlichungen | Separaten Geschäftsregeln oder Registrierung von DETai Accounts |
| DETai Hub | Wahl zwischen Erstellen und Verbinden eines Accounts, Bestätigung der Telegram-Verknüpfung, Spracheinstellungen des Hubs | Eigenständigen PiQ-Accounts oder PiQ-Tarifrechten |
| PiQ-API und serverseitige Produkt-Policy | Erhaltsrechte, aktuelle Tarife, Kontingente, Status, PNG-Bereitschaft und öffentliche Adressen | Übergreifenden Regeln des gesamten Ökosystems |
| Ecosystem Runtime / Commerce Core | Kommerzielle Angebote, bestätigte Zahlungen und Abonnementverlauf | Produktfunktionen oder wöchentlichen Limits von PiQ |
| Knowledge Substrate | Öffentliche Definitionen, Anleitungen, Dokumentationsverknüpfungen, Standards | Aktiven Nutzerdaten, Geheimnissen oder Checkout |
| DETai Account / Identity | Nutzeridentität produktübergreifend verknüpfen | Automatischem Erhalt von Zitaten |

**Ablauf der Übergabe:** PiQ übermittelt Hub das Ziel („Account erstellen oder verbinden“) und einen Hinweis zur Oberflächensprache. Hub prüft zunächst, ob Telegram mit einem gemeinsamen DETai Account verknüpft ist. Ist dies der Fall, zeigt es das Konto; andernfalls bietet es die Erstellung über Telegram oder die Verbindung zu einem bestehenden Website-Account über einen bestätigten Link an. Eine zuvor gewählte Hub-Sprache wird nicht überschrieben. Der Übergang erstellt weder automatisch einen Account noch gewährt er Plus/Pro.

Die gemeinsamen [Regeln zur Sprachübergabe](https://docs.detai-x.com/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/Telegram_Bots/language-handover/) und der [Konfigurationsstandard](https://docs.detai-x.com/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/Telegram_Bots/configuration-standard/) sind gesondert dokumentiert (derzeit auf Russisch). Diese Seite erklärt die Nutzerperspektive, nicht interne Entwicklungsabläufe.

Diese Dokumentation beschreibt **dauerhafte Nutzerprinzipien und Zuständigkeiten**. Interne Arbeitsdateien und Betriebsdetails gehören nicht zur öffentlichen Hilfe.

## Inhalt und Herkunft von Zitaten

Ein Zitat ist mehr als ein Bild. Es besitzt eine dauerhafte `quoteId`, die Person, von der die zitierten Worte stammen, eine bibliografische Quelle, Text und Revision, die Sprache des hinzugefügten Fragments, gegebenenfalls die Originalsprache des Werks, fertige Übersetzungen und Bilder sowie Prüf- und Veröffentlichungsstatus.

**Verfasser der zitierten Worte ≠ Ersteller der Karte ≠ in jedem Fall Verfasser des ursprünglichen Werks.** Metadaten werden nur anhand belegter Quellen gepflegt; KI-Übersetzungen können Fehler enthalten. Fertige Übersetzungen, aufbereitete Bilder und Veröffentlichungsberechtigungen sind verschiedene Zustände.

[Regeln zur Urheberschaft und Nutzung](https://detai-x.com/de/technology/platform/psychology-in-quotes/terms).

## Datenschutz und Nutzungsgrenzen

- Entwürfe und „Meine Zitate“ sind standardmäßig privat; der öffentliche Katalog erfordert ein Veröffentlichungsverfahren.
- Öffentliche Vorschauen fremder Bilder bleiben mit Wasserzeichen versehen.
- Der Erhalt eines Zitats gewährt ein **Nutzungsrecht innerhalb von PiQ**, keine Urheberrechte am literarischen Werk.
- PiQ bietet keine psychotherapeutischen oder diagnostischen Leistungen an.
- Accountdaten, technische Ereignisse und verbundene Dienste unterliegen den [Datenschutzhinweisen des Produkts](https://detai-x.com/de/technology/platform/psychology-in-quotes/privacy).
- Zum Schutz personenbezogener Daten gehören private Zitattexte, Token und Gesundheitsinformationen weder in öffentliche Hilfeseiten noch in Anfragen an externe KI.

## Für Support und KI-Agenten

**Hilfepfad:** [Erste Schritte](getting-started.md) → [Berechtigungsmodell](collection-and-plans.md) → [häufige Probleme](help-and-troubleshooting.md) → [aktuelle PiQ-Produktseite](https://detai-x.com/de/technology/platform/psychology-in-quotes). Dies berechtigt nicht dazu, ohne bestätigte Nutzeridentität Aktionen auszuführen.

Bei Screenshots muss eine KI unterscheiden, was die Dokumentation bestätigt, was auf dem Bildschirm sichtbar ist und was ohne aktuellen Account oder Backend nicht festgestellt werden kann. Über Zahlungen, Berechtigungen, fehlende PNGs oder den Erfolg einer Sendung darf nicht geraten werden.

**Aktualisiert:** 30. Oktober 2026. Aktuelle Funktionen und Angebote finden Sie auf der [PiQ-Seite](https://detai-x.com/de/technology/platform/psychology-in-quotes#piq-plans) und im Bot. Geltende Rechtsbedingungen, Preise und Limits haben Vorrang vor veralteten Kopien der Hilfe.

[← Übersicht](index.md) · [Sammlung und Tarife](collection-and-plans.md)
