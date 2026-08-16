---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0081
date: 2026-08-16
status: approved
sources:
  - https://hkh-autopilot.vdzonsoftware.nl
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl
  - https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/
  - https://github.com/robbertvdzon/hkh-autopilot
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/technical-spec.md
  - https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html
  - https://commons.wikimedia.org/w/index.php?search=Heemskerk&title=Special:MediaSearch&type=image
  - https://commons.wikimedia.org/wiki/File:Heemskerk_H_Laurentius_kerk.jpg
  - https://www.wikidata.org/w/index.php?search=Heemskerk&title=Special:Search&ns0=1
  - https://www.wikidata.org/wiki/Q9926
---
# Productcyclus 81

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De publieke app is een historische zoekingang voor een brede doelgroep, maar een geldige zoekopdracht op “Heemskerk” levert in productie en acceptatie nog steeds volledige bronuitval op. De repository beschrijft al een rijk status-, provenance-, rechten- en privacycontract dat de live UI niet zichtbaar maakt. Aanvullend onderzoek wijst op bruikbare patronen voor statuscommunicatie, per-item licenties en stabiele bronidentifiers. Er is geen productbesluit genomen.

### Geldige historische zoekopdracht levert geen bronnen

Productie en acceptatie tonen na zoeken op “Heemskerk” geen resultaatkaarten. De UI meldt volledige bronuitval, Europeana niet geconfigureerd en Open Archieven fout/onvolledig.

Bronnen: [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl)

### Live UI is armer dan het repositorycontract

README en specs beschrijven afzonderlijke statussen voor resultaten, nulresultaat, gedeeltelijke beschikbaarheid en bronuitval, plus source_name, stable_identifier, original_source_url, rechten, privacy en context. Deze contractvelden zijn niet zichtbaar in de live fouttoestand.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/technical-spec.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/technical-spec.md)

### Toegankelijke statuscommunicatie ondersteunt de gewenste zoekflow

W3C noemt zoekstatussen zoals laden, aantal resultaten en geen resultaten als statusberichten die programmatisch aangekondigd moeten worden zonder focusverlies. Dit ondersteunt één duidelijke statusregio met passende herstelacties.

Bronnen: [https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)

### Commons toont een sterk per-item provenance- en licentiepatroon

Wikimedia Commons combineert visueel zoeken met filters, sortering, resultaatcount en paginering. Een concreet Heemskerk-item toont afzonderlijk beschrijving, datum, bron, auteur, locatie, structured data, gebruiksopties en licentie; het bekeken item vermeldt CC BY-SA 3.0 en GFDL.

Bronnen: [https://commons.wikimedia.org/w/index.php?search=Heemskerk&title=Special:MediaSearch&type=image](https://commons.wikimedia.org/w/index.php?search=Heemskerk&title=Special:MediaSearch&type=image), [https://commons.wikimedia.org/wiki/File:Heemskerk_H_Laurentius_kerk.jpg](https://commons.wikimedia.org/wiki/File:Heemskerk_H_Laurentius_kerk.jpg)

### Wikidata toont stabiele identiteit en verbonden context

Wikidata toont bij zoekresultaten stabiele Q-identifiers, beschrijvingen, statement-/sitelink-aantallen en paginering. Het Heemskerk-item bevat tijdgebonden waarden, coördinaten, archiefrelaties, externe identifiers en referenties. Wikidata-data is volgens de data-accesspagina CC0 en via persistente URI’s en JSON/RDF-content negotiation toegankelijk.

Bronnen: [https://www.wikidata.org/w/index.php?search=Heemskerk&title=Special:Search&ns0=1](https://www.wikidata.org/w/index.php?search=Heemskerk&title=Special:Search&ns0=1), [https://www.wikidata.org/wiki/Q9926](https://www.wikidata.org/wiki/Q9926), [https://www.wikidata.org/wiki/Wikidata:Data_access](https://www.wikidata.org/wiki/Wikidata:Data_access)

### Beheer heeft velden maar geen zichtbare provenanceketen

De beheeracceptatie toont nieuwsbeheer, record-intake, rechtenstatus, privacyclassificatie, permalink, overlijdensstatus, levende-nabestaandeoptie en een historische-bronnenresultatenblok. In de bekeken toestand waren geen concrete resultaten of zichtbare bronverificatie-/vrijgavestatussen aanwezig.

Bronnen: [https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md)

### Huidige applicatie

**Doel:** Een publieke historische ontdekkingsapp voor een brede doelgroep. Bezoekers kunnen vanuit een gewone vraag, plek, persoon, gebeurtenis of onderwerp zoeken naar de geschiedenis van Heemskerk binnen bredere externe collecties. De repository beschrijft normalisatie van Europeana en Open Archieven, herleidbare bronmetadata, rechten/privacy en geen lokale opslag van zoekgeschiedenis of bronpayloads. De beheerapp is een aparte acceptance-interface voor nieuws en lokale record-intake.

**Wat ontbreekt:**
- Geldige zoekopdracht op “Heemskerk” levert in productie en acceptatie geen controleerbare historische resultaten.
- De publieke status onderscheidt onvoldoende tussen invoerfout, nulresultaat, gedeeltelijke bronbeschikbaarheid en volledige bronuitval.
- Resultaatkaarten met bronnaam, stabiele identifier, oorspronkelijke bronlink, recordmetadata, ophaaldatum en rechten-/privacystatus ontbreken live.
- Europeana staat zichtbaar als niet geconfigureerd en Open Archieven levert geen bruikbaar alternatief resultaat.
- Deployment-pariteit is voor bezoekers niet aantoonbaar omdat beide omgevingen dezelfde bronuitval tonen.
- De beheerinterface toont intakevelden en een resultatenblok, maar geen zichtbare concrete provenance-, verificatie-, rechten-, privacy- of vrijgaveketen.
- Buiten de falende zoekroute is geen direct voorbeeld van kaart-, tijd- of vervolgcontext zichtbaar.

### Verbetermogelijkheden

- Herstel een controleerbare end-to-end resultaatkaart voor Heemskerk.
- Maak de statusketen expliciet: lokale queryfout, geldig nulresultaat, gedeeltelijke beschikbaarheid en volledige bronuitval elk met eigen tekst en passende actie.
- Gebruik één programmatisch aangekondigde statusregio voor laden, resultaatcount, nulresultaat en bronfout, zonder focusverlies.
- Toon per bron beschikbaarheid, zoekinterpretatie, aantal zichtbare resultaten en veilige technische foutreden.
- Gebruik per resultaat bronhouder, stabiele identifier, oorspronkelijke URL, datering/plaats, ophaaldatum en afzonderlijke metadata-, objectrechten- en privacystatus.
- Behandel licenties per record/item en toon UNKNOWN expliciet; combineer metadatarechten niet automatisch met mediagebruik.
- Gebruik persistente externe identifiers en URI’s als vervolgankers en label relaties als bronclaims, niet als automatisch afgeleide historische feiten.
- Maak beheer bruikbaar voor verificatie met concrete resultaatkaarten en serverzijdige bron-, rechten-, privacy-, vrijgave- en mediastatussen zonder ruwe payloads of onnodige persoonsgegevens.

### Inspiratiebronnen

- [Wikimedia Commons MediaSearch](https://commons.wikimedia.org/w/index.php?search=Heemskerk&title=Special:MediaSearch&type=image) — Visueel erfgoedzoeken met licentie-, bestandstype-, formaat- en communityfilters, sortering, resultaatcount en paginering.
- [Wikimedia Commons itempagina](https://commons.wikimedia.org/wiki/File:Heemskerk_H_Laurentius_kerk.jpg) — Per-item patroon voor bron, auteur, locatie, structured data, gebruiksopties en expliciete licentie.
- [Wikidata Search](https://www.wikidata.org/w/index.php?search=Heemskerk&title=Special:Search&ns0=1) — Zoekresultaten met stabiele Q-identifiers, beschrijvingen, aantallen en paginering.
- [Wikidata Heemskerk item](https://www.wikidata.org/wiki/Q9926) — Verbonden context via tijdreeksen, coördinaten, archiefrelaties, categorieën, externe identifiers en referenties.
- [Wikidata Data access](https://www.wikidata.org/wiki/Wikidata:Data_access) — Persistente URI’s, JSON/RDF-content negotiation, onderscheid tussen zoeken en entity-ophalen, en CC0-data.
- [W3C WCAG 2.2 Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) — Toegankelijk patroon voor zoekstatussen zoals laden, resultaten, nulresultaat en fouten zonder focusverlies.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://hkh-autopilot.vdzonsoftware.nl) | 2026-08-16 | Publieke applicatie; rechten/licentie van UI en inhoud niet vastgesteld. | Productieflow read-only bekeken, inclusief productvisie, terugnavigatie en historische zoeking. |
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl) | 2026-08-16 | Representatieve nepdata; rechten/licentie van applicatie-inhoud niet vastgesteld. | Acceptatieflow gebruikt voor lege zoekstaat, bronkeuze, geldige zoekterm en foutstatus. |
| [bron](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/) | 2026-08-16 | Rechten/licentie van beheerapplicatie niet vastgesteld. | Beheeromgeving zonder login bekeken en naar het record-intakegedeelte gescrold; geen formulier verzonden. |
| [bron](https://github.com/robbertvdzon/hkh-autopilot) | 2026-08-16 | Publieke GitHub-repository; geen expliciete LICENSE-verificatie in de bekeken repositoryweergave, dus licentie onbekend. | Repositorystructuur, componenten en actuele hoofdbranch bekeken. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md) | 2026-08-16 | Publiek raw repositorybestand; code/documentlicentie niet expliciet vastgesteld. | Bevat het publieke zoek-, status-, configuratie- en rechten/privacycontract. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md) | 2026-08-16 | Publieke repositorydocumentatie; licentie niet expliciet vastgesteld. | Bevat functionele zoekstatussen, toegankelijkheid, privacy, rechten en historische metadata. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/technical-spec.md) | 2026-08-16 | Publieke repositorydocumentatie; licentie niet expliciet vastgesteld. | Bevat adapter-, endpoint-, identifier-, foutclassificatie- en rechtenmappingdetails. |
| [bron](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) | 2026-08-16 | W3C publieke technische documentatie; specifieke hergebruiklicentie niet afzonderlijk vastgesteld. | Onderbouwt toegankelijke statusmeldingen zonder focusverlies. |
| [bron](https://commons.wikimedia.org/w/index.php?search=Heemskerk&title=Special:MediaSearch&type=image) | 2026-08-16 | Commons-resultaten hebben individuele rechten; de interface biedt een licentiefilter. | Werkelijk bekeken Heemskerk-zoekraster met filters, sortering en resultaatcount. |
| [bron](https://commons.wikimedia.org/wiki/File:Heemskerk_H_Laurentius_kerk.jpg) | 2026-08-16 | Dit concrete bestand vermeldt CC BY-SA 3.0 en GFDL; structured data wordt als CC0 aangeduid; overige tekst heeft aanvullende voorwaarden. | Per-item provenance-, structured-data- en licentievermelding gecontroleerd. |
| [bron](https://www.wikidata.org/w/index.php?search=Heemskerk&title=Special:Search&ns0=1) | 2026-08-16 | Zoekinterface; datarechten zijn volgens Wikidata’s data-accesspagina CC0. | Zoekresultaten met stabiele identifiers, beschrijvingen en aantallen bekeken. |
| [bron](https://www.wikidata.org/wiki/Q9926) | 2026-08-16 | Wikidata-data valt volgens de data-accesspagina onder CC0; individuele referenties en externe links blijven provenance-informatie. | Heemskerk-item met tijdreeksen, kaartcontext, archiefrelaties en identifiers bekeken. |

## Productbeslissing

Herstel de historische zoekketen voor “Heemskerk” end-to-end: zorg voor deployment-pariteit in productie en acceptatie, correcte verwerking van geldige Open Archieven-antwoorden en één controleerbare resultaatkaart met bronmetadata, stabiele identifier, permanente bronlink, rechten-/privacystatus en duidelijke statuscommunicatie.

**Waarom:** BUG-2 is een open P1-bug in de primaire productervaring en krijgt daarom voorrang. De geldige zoekopdracht levert momenteel volledige bronuitval op in zowel productie als acceptatie. Deze richting sluit direct aan op epic theme-hkh-autopilot-0002, de missie en de principes betrouwbaar, verbonden, toegankelijk en herbruikbaar. De scope blijft klein en toetsbaar: herstel eerst één geldige Heemskerk-zoeking voordat bronuitbreiding, verbanden of rijke visualisaties worden opgepakt.

### Prioriteiten
- 1. Reproduceer en classificeer de fout afzonderlijk voor productie, acceptatie en de publieke Open Archieven-API: configuratie, HTTP, timeout, JSON, veldmapping of deployment-pariteit.
- 2. Herstel de adapter/configuratie zodat een geldig Open Archieven-antwoord niet als bronfout of onvolledig antwoord wordt behandeld.
- 3. Lever minimaal één resultaatkaart voor “Heemskerk” met bronnaam, recordgegevens, stable identifier, oorspronkelijke bronlink, datering/plaats, ophaaldatum en expliciete rechten-/privacystatus.
- 4. Maak de statusketen onderscheidend voor laden, geldig resultaat, nulresultaat, gedeeltelijke beschikbaarheid en volledige bronuitval; gebruik één toegankelijk aangekondigde statusregio met passende vervolgstap.
- 5. Voeg een reproduceerbare contracttest en smoke-test toe die productie- en acceptatieconfiguratie gelijkwaardig toetst zonder ruwe bronpayloads of onnodige persoonsgegevens op te slaan.

### Besluiten
- **BUG-2 wordt de eerstvolgende productrichting; BUG-1 wordt niet gelijktijdig opgepakt.** — Beide zijn P1, maar BUG-2 blokkeert de primaire missie-ervaring en de open roadmap-epic voor externe historische bronnen. Een werkende zoekketen levert direct controleerbare historische waarde; terugnavigatie blijft daarna afzonderlijk onderhoudswerk.
- **Open Archieven blijft de enige bron in deze herstelrichting.** — Onderzoek bevestigt dat Open Archieven de gekozen eerste externe bron is en dat de huidige fout waarschijnlijk in verwerking, configuratie of pariteit zit. Europeana en nieuwe collecties vergroten de scope voordat de primaire keten betrouwbaar werkt.
- **Resultaten worden bronvast en per item herleidbaar gepresenteerd.** — De repositorycontracten vragen vaste identifiers, oorspronkelijke links en rechten-/privacyvelden. Wikidata en Wikimedia Commons tonen dat stabiele identifiers en per-item provenance bruikbare ankers zijn; licenties mogen niet globaal op de hele zoekopdracht worden toegepast.
- **Statuscommunicatie wordt als aparte, toegankelijke productfunctie gevalideerd.** — Gebruikers moeten kunnen onderscheiden of hun invoer ongeldig is, er geen resultaten zijn, een bron gedeeltelijk beschikbaar is of alle bronnen uitvallen. W3C ondersteunt één programmatisch aangekondigde statusregio zonder focusverlies.

## UX-voorstel: Herstel en controleerbare historische zoekflow voor “Heemskerk”

**Gebruikersdoel:** Een bezoeker zoekt op “Heemskerk” en begrijpt betrouwbaar of er resultaten zijn, welke bron beschikbaar is en hoe elk resultaat verder onderzocht of gecontroleerd kan worden.

### Flow
1. Open de pagina Historisch zoeken.
2. Voer “Heemskerk” in en activeer Zoeken.
3. Toon in één statusregio dat de zoekopdracht wordt verwerkt.
4. Toon per bron de beschikbaarheid, het aantal resultaten en eventuele beperkte foutinformatie.
5. Bij een geldig resultaat: toon minimaal één resultaatkaart met titel, datering, plaats, bronhouder, stabiele identifier, permanente bronlink, ophaaldatum en afzonderlijke rechten- en privacystatus.
6. Laat de bezoeker de oorspronkelijke bron openen via een duidelijk gelabelde link.
7. Bij nulresultaat: toon een expliciete melding met acties om de zoekterm aan te passen of een andere bron te kiezen.
8. Bij gedeeltelijke beschikbaarheid of volledige bronuitval: toon welke bron faalt, wat nog beschikbaar is en een actie om opnieuw te proberen.

### Wireframe

Pagina: Historisch zoeken

[Hoofdnavigatie]
Historisch zoeken

[Zoeksectie]
Label: Zoek in historische collecties
[ tekstveld: Heemskerk                         ] [Zoeken]
[Bronnen kiezen]  Open Archieven geselecteerd

[Statusregio, role=status, aria-live=polite]
Zoeken naar “Heemskerk”…

[Bronstatus]
Open Archieven — Beschikbaar — 1 resultaat gevonden

[Resultaten]
Resultaatkaart
- Titel: [recordtitel]
- Datering: [datum of Onbekend]
- Plaats: [plaats of Onbekend]
- Bron: Open Archieven
- Stabiele identifier: [identifier]
- Ophaaldatum: [datum/tijd]
- Rechten: [status of UNKNOWN]
- Privacy: [status of UNKNOWN]
[Open oorspronkelijke bron]

[Secundaire acties]
[Opnieuw zoeken] [Zoekopdracht aanpassen]

Foutvariant:
[Statusregio] Open Archieven is tijdelijk niet beschikbaar. Er zijn geen controleerbare resultaten geladen.
[Opnieuw proberen] [Zoekopdracht aanpassen]

Nulresultaatvariant:
[Statusregio] Geen resultaten gevonden voor “Heemskerk”.
[Zoekopdracht aanpassen] [Bronnen kiezen]

### Interactiehypotheses
- Als een geldige zoekopdracht minimaal één bronstatus en één controleerbare resultaatkaart toont, stijgt het percentage geautomatiseerde smoke-tests dat een bruikbaar resultaat detecteert naar minimaal 100% in acceptatie en productie.
- Als gebruikers een onderscheidende status zien voor resultaat, nulresultaat, gedeeltelijke beschikbaarheid en bronuitval, kunnen geautomatiseerde toegankelijkheids- en contracttests elke toestand uniek herkennen zonder afhankelijk te zijn van visuele interpretatie.
- Als elk resultaat een stabiele identifier en oorspronkelijke bronlink bevat, kan een contracttest controleren dat resultaten herleidbaar zijn zonder ruwe bronpayloads lokaal op te slaan.
- Als rechten- en privacystatus per item expliciet worden weergegeven en UNKNOWN toegestaan is, worden ontbrekende metadata niet stilzwijgend als vrijgegeven of onbeperkt gebruikt.
- Als de zoekstatus via één programmatische statusregio wordt aangekondigd zonder focusverplaatsing, blijven toetsenbord- en schermlezerflows uitvoerbaar tijdens laden, resultaatweergave en foutafhandeling.

### Toegankelijkheid
- Gebruik semantische HTML met een herkenbaar zoekformulier, zichtbaar label, knop en logische koppen.
- Maak de statusregio programmatisch beschikbaar met role=status of een passend live-regionmechanisme; verplaats de focus niet automatisch tijdens laden.
- Zorg dat alle functies volledig met het toetsenbord werken, met zichtbare focusindicatoren en een logische tabvolgorde.
- Gebruik voldoende kleurcontrast en communiceer bronstatussen niet uitsluitend met kleur of iconen; voeg tekstlabels toe.
- Geef resultaatkaarten betekenisvolle koppen en toegankelijke linkteksten, bijvoorbeeld “Open oorspronkelijke bron voor [titel]”.
- Gebruik foutmeldingen die de oorzaak en herstelactie uitleggen en koppel invoerfouten programmatisch aan het zoekveld.
- Valideer automatisch met toegankelijkheidschecks, toetsenbordgerichte browser-tests en schermlezer-compatibele semantische assertions.

### Privacy
- Sla geen zoekgeschiedenis, vrije zoektermen of ruwe bronpayloads lokaal op tenzij daarvoor een expliciet, noodzakelijk productdoel en passende grondslag bestaat.
- Verwerk alleen metadata die nodig is voor zoeken, herleidbaarheid, rechten en privacyclassificatie.
- Toon privacystatus per record en maskeer of beperk persoonsgegevens wanneer de bron dat vereist; gebruik UNKNOWN wanneer de bron geen betrouwbare status levert.
- Vermijd persoonsgegevens in client-side logging, foutmeldingen, analytics en testfixtures.
- Gebruik stabiele externe identifiers en bronlinks als herleidbaarheidsanker, maar kopieer geen volledige persoonsdossiers naar de applicatie.
- Laat geautomatiseerde tests uitsluitend synthetische of geminimaliseerde historische metadata gebruiken en controleer dat foutresponses geen onnodige persoonsgegevens bevatten.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is klein, toetsbaar en volledig geautomatiseerd verifieerbaar. Er is geen blokkerend probleem.
- **WARNING · SCOPE** — De fix betreft BUG-1, terwijl de actuele productrichting prioriteit geeft aan BUG-2. Dit is een prioriteringsconflict, geen blokkade voor veilige uitvoering van deze geïsoleerde bugfix.

## Geaccepteerde storykandidaten

### Werkende terugnavigatie vanaf Productvisie

_Sleutel: `productvisie-terugnavigatie-herstellen`_
_Bug: `BUG-1`_

Als bezoeker wil ik vanaf de pagina Productvisie met de zichtbare Back-knop terugkeren naar de startpagina, zodat ik niet vast kom te zitten in de productvisie. Deze gerichte bugfix lost BUG-1 op zonder de historische zoekfunctionaliteit uit te breiden.

**Acceptatiecriteria**
- Een geautomatiseerde browser-test opent de publieke startpagina, navigeert via “Lees onze productvisie” naar Productvisie en activeert de zichtbare Back-knop.
- Na activatie wordt de startpagina geladen en is de Productvisiepagina niet langer de actieve route.
- De terugnavigatie werkt zowel via muisklik als via toetsenbordactivatie van de knop of link.
- De bestaande browsergeschiedenis en directe navigatie naar Productvisie blijven intact.
- De test controleert de navigatie in productie- en acceptatieconfiguratie voor zover beide omgevingen beschikbaar zijn, zonder handmatige verificatie.

Bronnen: [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl)

Risico's: Een wijziging aan gedeelde navigatie kan andere routes beïnvloeden; voeg regressietests voor de hoofdnavigatie toe., De exacte route-implementatie kan per deployment verschillen; productie en acceptatie moeten dezelfde navigatieconfiguratie gebruiken.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
