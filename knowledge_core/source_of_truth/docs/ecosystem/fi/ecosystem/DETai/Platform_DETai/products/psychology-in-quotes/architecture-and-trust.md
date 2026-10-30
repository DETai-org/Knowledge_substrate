---
title: "Psychology in Quotes — arkkitehtuuri ja luottamus"
description: "PiQ:n paikka DETaissa sekä tilien, API:n, tietosuojan ja julkaisemisen vastuunjako."
lang: fi
translation_of: /ru/ecosystem/DETai/Platform_DETai/products/psychology-in-quotes/architecture-and-trust/
---

# Miten tuote toimii ja mihin luottamus perustuu

## PiQ osana DETaita

- **DETai** on psykoterapian, tutkimuksen, koulutuksen, teknologian ja yhteisön yhdistävä ekosysteemi.
- **Platform DETai** on sen tuote- ja teknologiakerros sekä yhtenäinen digitaalinen ympäristö.
- **Psychology in Quotes** on digitaalinen oppimisen ja tiedon jakamisen tuote (ensisijainen käyttäjätoiminto), joka tukee myös julkaisemista ja luovaa työtä. Sen **E2 Brand** -rooli on levittää psykologista tietoa sekä vahvistaa tunnettuutta ja luottamusta.
- **DETai Account** tarjoaa yhteisen käyttäjäidentiteetin sivustolla ja yhdistetyssä Telegramissa. Rekisteröityminen ei kuitenkaan yksin anna oikeuksia muiden sitaatteihin.

[DETai-ekosysteemi](../../../index.md) · [Platform DETai](../../index.md) · [PiQ:n tuotesivu](https://detai-x.com/fi/technology/platform/psychology-in-quotes).

## Tuotteen asemoinnin kaksi toisistaan riippumatonta ulottuvuutta

| Kysymys | PiQ:n vastaus |
| --- | --- |
| Mitä käyttäjä saa? | Omaehtoista oppimista psykologisten ajatusten, lukemisen ja sitaattien merkityksellisen tallentamisen avulla |
| Mitä muuta voi tehdä? | Luoda sitaattikortteja ja Stories-sisältöjä, julkaista ja jakaa |
| Mikä on tärkein panos DETaille? | Tiedon levittäminen, luottamus ja tunnettuus – **E2 Brand** |
| Mitä PiQ ei lupaa? | Virallista koulutusohjelmaa, sertifiointia, diagnostiikkaa tai psykoterapiaa |

Erottelu perustuu [tuoteobjektin malliin](../../../../../product-market/product-object-model.md) ja [tasoluokituksen logiikkaan](../../../logic-of-echelons.md). Koulutuksellinen käyttötarkoitus ei automaattisesti siirrä tuotetta E1-luokkaan.

## Vastuiden erottaminen

| Järjestelmä tai käyttöliittymä | Vastaa seuraavista | Ei ole tietolähde seuraaville |
| --- | --- | --- |
| Verkkosivu `detai-x.com` | Esittely, verkkotili, sitaatit, julkinen kokoelma, SEO, oikeudelliset dokumentit | Erilliset tilausten oikeudet tai yksityinen SQL |
| PiQ:n Telegram-botti | Sitaattien luonti, kokoelma, vuorovaikutus ja julkaisut | Omat irralliset maksusäännöt tai DETai Account -rekisteröinti |
| DETai Hub | Account-tilin luomisen tai yhdistämisen valinta, Telegram-yhteyden vahvistus ja Hubin kieliasetus | Erilliset PiQ-tilit tai PiQ-tilausten oikeudet |
| PiQ-API ja tuotteen palvelinpuolen käytännöt | Hankintaoikeus, aktiiviset tasot, kiintiöt, tilat, PNG-valmius ja julkiset osoitteet | Koko ekosysteemin yleiset säännöt |
| Ecosystem Runtime / Commerce Core | Kaupalliset tarjoukset, vahvistetut maksut ja tilaushistoria | PiQ:n tuoteominaisuuksia tai viikoittaisia rajoituksia |
| Knowledge Substrate | Julkiset käsitteet, ohjeet, dokumentaatiolinkit ja standardit | Reaaliaikainen käyttäjätietokanta, salaisuudet tai maksun suorittaminen |
| DETai Account / Identity | Käyttäjän yhdistäminen tuotteiden välillä | Automaattisesti hankitut sitaatit |

**Näin siirtymä toimii:** PiQ välittää Hubille tavoitteen (”luo Account tai yhdistä olemassa oleva”) ja vihjeen käyttöliittymän kielestä. Hub tarkistaa ensin, onko Telegram jo yhdistetty yhteiseen DETai Account -tiliin. Jos on, Hub näyttää tilin. Muussa tapauksessa se tarjoaa tilin luontia Telegramissa tai verkkosivun tilin yhdistämistä vahvistettavan linkin avulla. Hubin aiempaa kielivalintaa ei korvata. Siirtymä ei luo tiliä automaattisesti eikä anna Plus/Pro-oikeuksia.

Yleiset [bottien välisen kielivalinnan säännöt](https://docs.detai-x.com/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/Telegram_Bots/language-handover/) ja [konfiguraatiostandardi](https://docs.detai-x.com/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/Telegram_Bots/configuration-standard/) on dokumentoitu erikseen (toistaiseksi venäjäksi). Tämä sivu kuvaa käyttäjälle olennaiset rajat, ei sisäisiä kehitysvaiheita.

Tämä dokumentaatio kuvaa **pysyviä käyttäjäperiaatteita ja vastuunjakoa**. Sisäiset työtiedostot ja käyttöympäristön asetukset eivät kuulu julkiseen ohjeeseen.

## Sitaatin sisältö ja alkuperä

Sitaatti ei ole vain kuva. Sillä on pysyvä `quoteId`, lainattujen sanojen tekijä, bibliografinen lähde, teksti ja sen versio, lisätyn katkelman kieli, mahdollinen alkuperäisteoksen kieli, valmiit käännökset, kuvat sekä tarkistuksen ja julkaisun tilat.

**Lainattujen sanojen tekijä ≠ kortin luoja ≠ kaikissa tapauksissa alkuperäisteoksen kirjoittaja.** Metatiedot täydennetään vain todennettujen lähteiden perusteella; tekoälykäännöksissä voi olla virheitä. Käännöksen valmistuminen, kuvan renderöinti ja julkaisun hyväksyntä ovat eri tiloja.

[Tekijyyttä ja käyttöä koskevat säännöt](https://detai-x.com/fi/technology/platform/psychology-in-quotes/terms).

## Yksityisyys ja käytön rajat

- Luonnokset ja ”Omat sitaatit” ovat oletusarvoisesti yksityisiä. Julkiseen kokoelmaan pääsy edellyttää julkaisuprosessia.
- Muiden sitaattien julkiset esikatselukuvat ovat vesileimattuja.
- Sitaatin hankkiminen antaa **käyttöoikeuden PiQ:n sisällä**, ei kirjallisen teoksen tekijänoikeuksia.
- PiQ ei tarjoa psykoterapia- tai diagnoosipalveluja.
- Account-tiedot, tekniset tapahtumat ja yhdistetyt palvelut kuuluvat [tuotteen tietosuojailmoituksen](https://detai-x.com/fi/technology/platform/psychology-in-quotes/privacy) piiriin.
- Henkilötietojen turvaamiseksi yksityisiä sitaattitekstejä, tokeneita tai terveystietoja ei pidä lisätä julkisiin ohjeisiin tai ulkoisen tekoälyn kyselyihin.

## Tukea ja tekoälyavustajia varten

**Ohjepolku:** [aloittaminen](getting-started.md) → [käyttöoikeusmalli](collection-and-plans.md) → [ongelmanratkaisu](help-and-troubleshooting.md) → [PiQ:n ajantasainen tuotesivu](https://detai-x.com/fi/technology/platform/psychology-in-quotes). Polku ei anna oikeutta suorittaa toimintoja vahvistamattoman käyttäjän puolesta.

Kuvakaappausta tulkitessa tekoälyn on erotettava, mitä dokumentaatio vahvistaa, mitä ruudulla todella näkyy ja mitä ei voi tietää ilman ajantasaista Account- tai taustajärjestelmän tietoa. Maksuja, oikeuksia, puuttuvan PNG:n syytä tai lähetyksen onnistumista ei pidä arvata.

**Päivitetty:** 30.10.2026. Tarkista ajantasaiset ominaisuudet ja tarjoukset [PiQ:n sivulta](https://detai-x.com/fi/technology/platform/psychology-in-quotes#piq-plans) ja botista. Voimassa olevat oikeudelliset ehdot, hinnat ja rajoitukset ovat ensisijaisia vanhentuneisiin ohjekopioihin nähden.

[← Yleiskatsaus](index.md) · [Kokoelma ja tilaustasot](collection-and-plans.md)
