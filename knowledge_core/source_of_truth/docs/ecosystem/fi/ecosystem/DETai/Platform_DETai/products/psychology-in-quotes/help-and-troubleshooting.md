---
title: "Psychology in Quotes — kysymykset ja ongelmanratkaisu"
description: "PiQ:n näyttöjen, vieraskorttien, vesileimojen, kielioikeuksien ja julkaisutilojen tulkinta."
lang: fi
translation_of: /ru/ecosystem/DETai/Platform_DETai/products/psychology-in-quotes/help-and-troubleshooting/
---

# Kysymykset, tilat ja ongelmanratkaisu

Tämä ohje on tarkoitettu käyttäjille ja ulkoisille tekoälyavustajille, jotka tulkitsevat PiQ-kuvakaappausta. Selvitä ensin näkymä, painikkeen nimi, tilaustaso ja tarkka tilatieto. **Älä päättele sitaatin omistusta pelkän kuvan tai vesileiman perusteella.**

## Jos lähetät kuvakaappauksen: miten käyttäjän tila tunnistetaan?

Vaiheet soveltuvat myös GPT- ja muille tekoälypohjaisille tukipalveluille. Älä arvaa tilaa kortin väristä, Telegram-nimestä tai yksittäisestä vesileimasta.

1. **Käyttöympäristö:** verkkosivu (julkinen kokoelma tai henkilökohtainen tili) vai PiQ:n Telegram-botti? Sama henkilö voi olla kirjautunut sivustolle **yhdistämättä Telegramia** DETai Account -tiliinsä.
2. **Tunnistautuminen:** Public on vieras ilman vahvistettua yhteistä tiliä, Free on tilillinen perustason käyttäjä ja Plus/Pro sama osallistuja laajennetulla tilauksella. Projektin ylläpitäjärooli, palvelun lisäoikeudet ja aidosti voimassa oleva tilaus tarkistetaan erikseen. Epäselvässä tilanteessa pyydä avaamaan ”Omat käyttöoikeudet”, älä kysy salasanoja.
3. **Kohde:** julkinen kokoelma, vieraskortti/luonnos, ”Omat sitaatit”, ”Hankitut”, ”Suosikit” ja ”Omat julkaisut” ovat eri tietoryhmiä. Suosikiksi tallentaminen ei anna oikeutta vesileimattomaan kuvaan.
4. **Tarkoitus:** haluaako käyttäjä lukea, tallentaa, hankkia PNG:n, lähettää tarkistettavaksi vai julkaista kanavalle? Julkaistua aineistoa voi lukea ilman tiliä; pysyvät tulokset ja kiintiötä kuluttavat toimet vaativat vahvistetut oikeudet.
5. **Tila ja kieli:** tarkista näkyvä tila, käyttöliittymän kieli, näytetyn version ja lisätyn tekstin kielet sekä median valmistuminen ja lupa. Käyttöliittymän kielen vaihto ei anna oikeutta vesileimattomaan tiedostoon.
6. **Toiminta:** anna yksi selkeä seuraava painike tai polku. Jos tilien yhdistäminen on tarpeen, selitä rekisteröityminen ja erillinen Telegram-yhteys. Älä lupaa välitöntä julkaisua tai vanhentuneiden vierastietojen palautumista.

[Public- ja Account-tilojen visuaalinen vertailu](https://detai-x.com/fi/technology/platform/psychology-in-quotes#piq-access) · [Aloittaminen](getting-started.md) · [Tasot ja kiintiöt](collection-and-plans.md).

**Versioista:** vierasmuokkain, suosikit, toistuvat väliaikaiset jaksot ja tulosten siirto tilin yhdistämisen jälkeen toteutettiin [PiQ:n PR:ssä #37](https://github.com/DETai-org/psychology-in-quotes/pull/37). Ajantasaiset vierasrajat näet botista ja [Free / Plus / Pro -rajat verkkosivulta](https://detai-x.com/fi/technology/platform/psychology-in-quotes#piq-plans). PR:n yhdistäminen ja käyttöönotto ovat eri asioita. Ristiriitatilanteessa noudata toimivan botin käyttöliittymää.

## Yhdistä DETai Account ja Telegram luomatta toista tiliä

Valitse PiQ:n kehotteesta **”Avaa DETai Hub”**. Jos Telegram on jo yhdistetty DETai Account -tiliin, Hub näyttää olemassa olevan tilin. Muutoin voit luoda uuden Hubissa tai yhdistää [verkkosivulla](https://detai-x.com/fi/account) jo rekisteröidyn tilin valitsemalla ”Yhdistä Telegram” ja vahvistamalla kertakäyttölinkin. **Pelkkä Hubin avaaminen tai verkkosivulle kirjautuminen ei yhdistä Telegramia.** Kun palaat PiQ:hun, seuraava tavallinen toimenpide tarkistaa yhteyden automaattisesti. ”Tarkista yhteys” päivittää näkymän halutessasi heti.

Hub voi käyttää siirtymässä PiQ:n kieltä vain, jos Hubissa ei ole aiemmin tallennettua kielivalintaa. Jos kieli on väärä, muuta sitä Hubissa; sitaatin ja käännöksen kielet eivät muutu. [Vaiheittainen ohje](getting-started.md).

## Mitä vieraskortti ja sen voimassaoloaika tarkoittavat?

**Public:** väliaikainen tulos, joka liittyy varmennettavaan Telegram ID:hen, **ei** yhteisen Account-tilin pysyvä sitaatti. Vieraskortin, kuvien luontikertojen, suosikkien ja säilytysajan rajoitukset tulee tarkistaa botista. [Free / Plus / Pro -ehdot](https://detai-x.com/fi/technology/platform/psychology-in-quotes#piq-plans) löytyvät erikseen sivustolta. Vieraskuvissa on vesileima, eikä sisältöä ole vielä tarkastettu toimituksellisesti. PNG:n lähettäminen yksityiskeskusteluun **ei ole sama asia** kuin julkaiseminen Telegram-kanavalla tai yhteisessä kokoelmassa.

**Jos näkyy ”Luonnos”:** suosittele ”Jatka luomista”, älä uuden luonnoksen tekemistä. **Jos kortti on valmis:** näytä säilytysaika ja mahdollisuus tallentaa Account-tilille. **Jos aika on päättynyt:** älä lupaa vanhojen tietojen palautumista, mutta uusi vierasjakso voi olla käytettävissä. **Jos tili yhdistettiin juuri:** tarkista siirron ja moderoinnin tila; oman sisällön tallennus on eri asia kuin julkaisuhyväksyntä.

**Muistutukset:** käyttöjakson päättymisestä tai uuden jakson alkamisesta voidaan lähettää yksittäisiä palveluilmoituksia sovitun käytännön mukaan. Telegram-viestin toimitusvirhe tai botin estäminen ei merkitse tietojen välitöntä poistamista. Säilytysajan (TTL) rajat ja mahdollisuus kieltää oma-aloitteiset ilmoitukset ovat voimassa.

## Mitä kokoelman osiot tarkoittavat?

**Omat sitaatit** ovat käyttäjän luomia, **Hankitut** sisältävät muiden kokoelmasta hankittuja sitaatteja, **Suosikit** ovat kirjanmerkkejä ja **Omat julkaisut** muodostavat lähetysten historian. Sama sisältö voi eri perustein kuulua useaan osioon.

[Lue kokoelman käsitteistä](collection-and-plans.md#piq-collection-terms).

## Oman sitaattini kuva ei vielä ole saatavilla {#piq-image-not-ready}

**Merkitys:** teksti ja lähde on tallennettu PiQ:hun, mutta *nykyiselle versiolle* ei ole vahvistettua valmista PNG-kuvaa. Karusellin muut sitaatit voivat silti toimia.

**Toimi näin:** avaa ”Oma kokoelma” → ”Omat sitaatit”, katso laskuria `1/N` ja selaa kortteja. Valitse ”Tarkista tila”. Jos järjestelmä tarjoaa nimenomaan **keskeneräisen luonnoksen** jatkamista, viimeistele se.

**Vältä:** saman sitaatin uudelleenluomista, pelkkää odottamista silloin kun kuvantehtävää ei ole edes käynnistetty, tai aiemman version PNG:n esittämistä ajantasaisena.

**Pyydä apua, kun:** PNG:tä eikä palautuspainiketta ole. Lähetä tukeen sitaatin ID, ajankohta ja tilan nimi – älä tilisi salaisuuksia.

## Miksi kuvassa lukee PREVIEW tai näkyy vesileima?

**Kokoelma:** toisten sitaattien julkiset esikatselut on tarkoituksella vesileimattu. Pelkkä DETai Account ei poista leimaa.

**Hankitut:** vahvistetun hankinnan jälkeen voit ladata vesileimattoman tiedoston sallitulla kielellä. Free-tasolla oikeus koskee valittua kieltä ja aiemmin säilyneitä vahvistettuja kielioikeuksia.

**Omat sitaatit:** vahvistettu Account-omistaja voi nähdä oman sitaatin valmiin PNG:n ilman vesileimaa myös Free-tasolla. Vieraan kokeilukortti jää vesileimatuksi, kun vierasmuokkain on käytössä. Jos verkkosivun ”Omat sitaatit” näyttää yhä PREVIEW, tarkista kirjautuneen käyttäjän versio; omaa sitaattia ei tarvitse hankkia uudelleen.

[Hankinnan säännöt](collection-and-plans.md).

## Miksi Language ei avaa käännöstä?

**Merkitys:** Free-tasolla vesileimattomat versiot on rajattu valittuun kieleen. Plus/Pro tarjoavat lisäkieliä vain, jos versiot on valmisteltu ja hyväksytty. Käyttöliittymän kieli ei vaikuta hankintaoikeuteen.

**Toimi näin:** tarkista ”Omat käyttöoikeudet” ja käännöksen tila. Jos versio on kesken, älä hanki sitaattia uudelleen. Se tulee saataville valmistelun ja hyväksynnän jälkeen. Vesileimattu esikatselu voi silti näkyä.

## Miksi julkaisu ei lähtenyt?

**Merkitys:** lähetys voi olla tilassa `pending`, `failed`, `cancelled`, `uncertain` tai vahvistetusti onnistunut.

**Toimi näin:** ”Omat julkaisut” → ”Tarkista tulos”. Varmista, että kanava on yhdistetty, sisältö hyväksytty, toisen sitaatti hankittu etukäteen ja kiintiö riittää.

**Vältä:** `uncertain`-tilassa lähettämistä sokkona uudelleen. Tuloksen tarkistaminen ei saa käynnistää toista lähetystä.

## Miksi sitaattini ei vielä näy julkisessa kokoelmassa?

Oman sitaatin tallentaminen **ei ole julkinen julkaisu**. Tarkistus sekä kieliversioiden ja kuvien valmistelu voivat viedä aikaa. Prossa on luotettu hyväksyntämenettely, mutta se ei takaa välitöntä julkaisua ilman valmistelua.

## Miksi oikeudet muuttuivat tilauksen vaihdon jälkeen?

Hankitut sitaatit eivät katoa tilaustason laskun vuoksi. Lisäkielten, kanavien ja toimintojen käyttö voi kuitenkin vähentyä. Tarkista oikeudet ja rajoitukset kohdasta ”Omat käyttöoikeudet”. [Ajantasainen vertailu](https://detai-x.com/fi/technology/platform/psychology-in-quotes#piq-plans).

## Näin pyydät tekoälyltä apua paljastamatta tietojasi

Voit lähettää **kuvakaappauksen virheestä ja linkin tähän ohjeeseen** sekä kertoa ”Olen kohdassa … ja näen viestin …”. Varmista ajantasainen tila toimivasta palvelusta; ohjeet voivat olla käyttöliittymää jäljessä.

**Älä lähetä:** salasanoja, tunnuksia, evästeitä, vahvistuskoodeja, palautuslinkkejä, kolmansien osapuolten yksityisiä tekstejä tai terveystietoja. Ulkoinen tekoäly ilman hyväksyttyä pääsyä voi selittää käyttöliittymää, mutta ei tarkistaa käyttöoikeuksia, suorittaa maksua tai muuttaa Account-tiliäsi.

Tuki: **detai.founder@gmail.com**. [Tietosuoja](https://detai-x.com/fi/technology/platform/psychology-in-quotes/privacy).

[← Yleiskatsaus](index.md) · [Arkkitehtuuri ja luottamus →](architecture-and-trust.md)
