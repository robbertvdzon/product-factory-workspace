---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0079
date: 2026-08-16
status: approved
sources:
  - https://github.com/robbertvdzon/hkh-autopilot
  - https://hkh-autopilot.vdzonsoftware.nl
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl
  - https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/
  - https://api.openarchieven.nl/1.1/records/search.json?name=Heemskerk&lang=nl&number_show=3
  - https://www.openarchieven.nl/api/docs/records/search.php
  - https://www.openarchieven.nl/datasets/
  - https://www.openarchieven.nl/disclaimer.php
  - https://digitalnz.org/developers/api-docs-v3/search-records-api-v3
  - https://digitalnz.org/developers/api-docs-v3
  - https://api.europeana.eu/en
  - https://www.delpher.nl/over-delpher/handleiding/zoeken-in-delpher/hoe-zoek-je-het-best/zoeken-naar-verschillende-versies-van-een-woord
---
# Productcyclus 79

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De belangrijkste onbeantwoorde productvraag is hoe HKH een geldige Open Archieven-respons betrouwbaar, herleidbaar en begrijpelijk presenteert, inclusief onderscheid tussen resultaat, nulresultaat, gedeeltelijke respons en bronuitval. De live flow toont bij ‘Heemskerk’ momenteel een bronfout, terwijl dezelfde publieke API op 2026-08-16 HTTP 200 en 49.555 records retourneerde.

### De actuele zoekflow faalt zichtbaar bij een geldige query

Productie en acceptatie tonen na zoeken op ‘Heemskerk’ geen resultaatkaart, maar melden dat geen historische bronnen konden worden geraadpleegd, Europeana niet is geconfigureerd en Open Archieven een fout gaf.

Bronnen: [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl), [https://api.openarchieven.nl/1.1/records/search.json?name=Heemskerk&lang=nl&number_show=3](https://api.openarchieven.nl/1.1/records/search.json?name=Heemskerk&lang=nl&number_show=3)

### Open Archieven levert aantoonbaar een geldige respons

De publieke API gaf HTTP 200, number_found=49555 en drie documenten met identifier, archieforganisatie, persoons- en eventgegevens, sourcetype en permanente URL.

Bronnen: [https://api.openarchieven.nl/1.1/records/search.json?name=Heemskerk&lang=nl&number_show=3](https://api.openarchieven.nl/1.1/records/search.json?name=Heemskerk&lang=nl&number_show=3), [https://www.openarchieven.nl/api/docs/records/search.php](https://www.openarchieven.nl/api/docs/records/search.php)

### Querymapping is beperkt transparant

De UI toont vrije tekst en optionele velden voor plek, persoon, gebeurtenis, periode en bron. Na zoeken toont de app alleen ‘naam (name)’, terwijl Open Archieven ook eventplace, birthplace, sourcetype, archive_code en andere parameters ondersteunt.

Bronnen: [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl), [https://www.openarchieven.nl/api/docs/records/search.php](https://www.openarchieven.nl/api/docs/records/search.php)

### Herleidbaarheid en rechten zijn bronafhankelijk

Open Archieven documenteert stabiele recordvelden en URL’s, maar waarschuwt dat sommige organisaties herpublicatie als open data niet toestaan. Rechten kunnen daarom niet generiek op alle resultaten worden gezet.

Bronnen: [https://www.openarchieven.nl/api/docs/records/search.php](https://www.openarchieven.nl/api/docs/records/search.php), [https://www.openarchieven.nl/datasets/](https://www.openarchieven.nl/datasets/), [https://www.openarchieven.nl/disclaimer.php](https://www.openarchieven.nl/disclaimer.php)

### Beheeromgeving toont geen zichtbare provenanceketen

De publiek toegankelijke beheeracceptatie toont nieuwspublicatie en lokale record-intake. In het bekeken scherm ontbreken zichtbare statussen voor externe bronverificatie, rechten, privacy en publieke vrijgave.

Bronnen: [https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/)

### Repositorydocumentatie bevestigt bron- en statusgerichte architectuur

De README beschrijft een Kotlin-backend, Flutter-frontend en historische zoek-API met Open Archieven en optioneel Europeana, inclusief querysemantics en herleidbare metadata. De live flow levert bij de representatieve query nog geen kaart.

Bronnen: [https://github.com/robbertvdzon/hkh-autopilot](https://github.com/robbertvdzon/hkh-autopilot)

### Huidige applicatie

**Doel:** Historisch Heemskerk is een brede publieke ontdekkingstoegang voor iedereen die iets wil weten over de geschiedenis van Heemskerk. De app wil lokale bronnen verbinden met externe historische collecties en bezoekers vanuit gewone vragen laten zoeken. De beheeromgeving ondersteunt administratieve mededelingen en intake van lokale records.

**Wat ontbreekt:**
- Een geldige Open Archieven-respons wordt als bronfout gepresenteerd; nulresultaat, adapterfout, bronuitval en geldig resultaat zijn onvoldoende onderscheiden.
- Er ontbreekt een zichtbare resultaatkaart met bronnaam, recordmetadata, identifier en permanente bronlink.
- De werkelijk verzonden queryparameters zijn onvoldoende transparant.
- Rechten- en privacystatus zijn niet zichtbaar in de publieke resultaatflow of gekoppeld aan lokale record-intake.
- De cross-source belofte is in de bekeken flow niet beleefbaar: Europeana is niet geconfigureerd en Open Archieven levert geen zichtbaar resultaat.

### Verbetermogelijkheden

- Valideer en presenteer response.number_found, docs, identifier en url afzonderlijk; toon geldige deelresultaten ook wanneer een andere bron ontbreekt.
- Maak aparte statussen voor geldig resultaat, nulresultaat, gedeeltelijke respons, ongeldige respons, timeout/5xx en bronuitval.
- Toon de werkelijk verzonden bronparameters en maak de mapping van vrije tekst en velden expliciet.
- Gebruik compacte herleidbare resultaatkaarten met bronmetadata, identifier, permanente link, query-interpretatie en rechten-/privacystatus.
- Behandel rechten fail-closed op record- of datasetniveau en toon ‘onbekend’ wanneer verificatie ontbreekt.
- Maak lokale record-intake provenance-aware met bron, identifier, verificatie-, rechten/privacy- en publicatiestatus.
- Gebruik DigitalNZ als inspiratie voor result_count, facetten en rights/commercial-use-filters; Delpher voor zoekuitleg en verfijning; Europeana en Rijksmuseum voor persistent identifiers en cross-collection discovery.
- Test de flow met geldige respons, nulresultaat, bronuitval, gedeeltelijke respons en ambigu interpreteerbare zoektermen.

### Inspiratiebronnen

- [DigitalNZ](https://digitalnz.org/developers/api-docs-v3/search-records-api-v3) — Metadata-aggregator met result_count, facetten voor plaats/jaar/rechten/collectie en expliciete commerciële-use-informatie.
- [Delpher](https://www.delpher.nl/over-delpher/handleiding/zoeken-in-delpher/hoe-zoek-je-het-best/zoeken-naar-verschillende-versies-van-een-woord) — Laagdrempelige Nederlandse historische zoekdienst met full-textzoeking, collectiekeuze, syntaxisuitleg en verfijning.
- [Europeana APIs](https://api.europeana.eu/en) — Cross-collection erfgoedlaag met Search API, Record API en IIIF-toegang.
- [Rijksmuseum Data Services](https://data.rijksmuseum.nl/docs/search) — API met zoekparameters, Linked Open Data-identifiers en persistent identifier-resolutie.
- [Rijksmuseum Collection Online](https://data.rijksmuseum.nl/about/) — Combineert objectmetadata, controlled vocabularies en per object zichtbare CC0/public-domainstatus waar mogelijk.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://github.com/robbertvdzon/hkh-autopilot) | 2026-08-16 | Publieke GitHub-repository; geen concrete licentie voor het gehele product vastgesteld. | Repository en README bekeken voor doel, architectuur, bronstrategie en gedocumenteerde statuslogica. |
| [bron](https://hkh-autopilot.vdzonsoftware.nl) | 2026-08-16 | Publieke applicatie; rechten/licentie op interface-inhoud onbekend. | Productieomgeving geopend, naar historisch zoeken genavigeerd en read-only gezocht op ‘Heemskerk’. |
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl) | 2026-08-16 | Publieke acceptatieomgeving met representatieve nepdata; rechten/licentie op interface-inhoud onbekend. | Acceptatieomgeving geopend, zoekflow doorlopen en dummycontent beoordeeld. |
| [bron](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/) | 2026-08-16 | Publieke beheeracceptatieomgeving; rechten/licentie op interface-inhoud onbekend. | Beheerscherm zonder login bekeken, zonder formulieren te verzenden. |
| [bron](https://api.openarchieven.nl/1.1/records/search.json?name=Heemskerk&lang=nl&number_show=3) | 2026-08-16 | API-respons; rechten op onderliggende genealogische records zijn niet uniform en moeten per dataset/context worden geverifieerd. | Via headless Chromium gecontroleerd dat de representatieve query HTTP 200 en concrete records oplevert. |
| [bron](https://www.openarchieven.nl/api/docs/records/search.php) | 2026-08-16 | Publieke API-documentatie; concrete hergebruiklicentie van de documentatietekst niet vastgesteld. | Bevestigt parameters, responsstructuur, identifiers, permanente URL’s, paging en foutcodes. |
| [bron](https://www.openarchieven.nl/datasets/) | 2026-08-16 | Publieke datasetinformatie; vermeldt expliciet dat sommige organisaties herpublicatie als open data niet toestaan. | Relevant voor dataset-, rechten- en hergebruikstatus. |
| [bron](https://www.openarchieven.nl/disclaimer.php) | 2026-08-16 | Publieke disclaimer; bronvoorwaarden zijn leidend en recordrechten blijven contextafhankelijk. | Relevant om geen algemene rechtenstatus aan alle resultaten toe te kennen. |
| [bron](https://digitalnz.org/developers/api-docs-v3/search-records-api-v3) | 2026-08-16 | Publieke API-documentatie; verwijst naar Developer API Terms of Use en het veld is_commercial_use. | Inspiratie voor result_count, facetten, rightsfilters en expliciete commerciële-use-status. |
| [bron](https://digitalnz.org/developers/api-docs-v3) | 2026-08-16 | Publieke API-documentatie; publieke content is zonder key toegankelijk, maar partnerrechten en gebruiksvoorwaarden blijven gelden. | Inspiratie voor metadata-aggregatie met links naar partnercollecties. |
| [bron](https://api.europeana.eu/en) | 2026-08-16 | Publieke API-informatie; gratis API-key vereist en rechten zijn recordafhankelijk. | Relevant als cross-collection inspiratie voor Search API, Record API en IIIF. |
| [bron](https://www.delpher.nl/over-delpher/handleiding/zoeken-in-delpher/hoe-zoek-je-het-best/zoeken-naar-verschillende-versies-van-een-woord) | 2026-08-16 | Publieke KB/Delpher-informatie; raadplegen kan zonder account, terwijl data- en tekstgebruik onder voorwaarden valt. | Inspiratie voor laagdrempelige historische full-textzoeking en queryuitleg. |

## Productbeslissing

Maak de bestaande historische zoekflow tot een betrouwbare Open Archieven-MVP voor de query ‘Heemskerk’: toon de geïnterpreteerde zoekopdracht, verwerk een geldige respons als resultaat, en onderscheid zichtbaar resultaat, nulresultaat, gedeeltelijke respons en bronuitval. Elke resultaatkaart bevat bronnaam, recordgegevens, identifier, permanente bronlink en rechten-/privacystatus; onbekende status wordt expliciet als ‘onbekend’ getoond.

**Waarom:** Deze kleine richting sluit direct aan op open roadmap-epic theme-hkh-autopilot-0002 en verhelpt het belangrijkste aangetoonde probleem: een geldige Open Archieven-respons wordt momenteel als bronfout gepresenteerd. De publieke API levert aantoonbaar concrete records voor ‘Heemskerk’, terwijl de huidige gebruikersflow geen resultaatkaart, query-uitleg of betrouwbare status toont. De richting is toetsbaar met één representatieve query en maakt bronherleidbaarheid, betrouwbaarheid en toegankelijkheid zichtbaar zonder onbewezen relaties of generieke rechtenclaims.

### Prioriteiten
- Verzend en toon de werkelijk geïnterpreteerde Open Archieven-parameters, inclusief dat ‘Heemskerk’ als naamzoekopdracht wordt gebruikt.
- Presenteer response.number_found en geldige documenten als compacte, herleidbare resultaatkaarten met archieforganisatie, persoons-/eventgegevens, sourcetype, identifier en permanente URL.
- Gebruik afzonderlijke statussen voor geldig resultaat, nulresultaat, gedeeltelijke respons, ongeldige respons en bronuitval/time-out.
- Toon rechten- en privacystatus per record of dataset; gebruik ‘onbekend’ wanneer verificatie ontbreekt en blokkeer geen resultaat zonder concreet materieel risico.
- Test minimaal de scenario’s geldige respons, nulresultaat, bronuitval en gedeeltelijke respons.

### Besluiten
- **Gebruik Open Archieven als enige externe bron in deze MVP en maak een geldige respons onafhankelijk van de status van andere bronnen zichtbaar.** — Open Archieven is als eerste externe bron gekozen en de representatieve query levert HTTP 200 met 49.555 records en concrete documenten. De huidige flow laat juist zien dat ontbrekende Europeana-configuratie een bruikbaar Open Archieven-resultaat niet mag overschaduwen.
- **Maak query-interpretatie zichtbaar vóór of naast de resultaten, met de exacte bronparameters en een begrijpelijke samenvatting.** — De huidige UI toont vrije tekst en filters, maar maakt niet duidelijk welke parameters werkelijk naar de bron worden verzonden. De API ondersteunt meerdere expliciete zoekvelden; transparantie voorkomt dat bezoekers een andere zoekopdracht veronderstellen dan werkelijk is uitgevoerd.
- **Gebruik bronmetadata en permanente links als minimale provenance, en publiceer rechten- of privacystatus alleen wanneer die per dataset/context is vastgesteld.** — De API documenteert stabiele identifiers en permanente URL’s, maar rechten op onderliggende records zijn niet uniform. De datasetinformatie en disclaimer waarschuwen dat sommige organisaties herpublicatie als open data niet toestaan; daarom is ‘onbekend’ veiliger dan een algemene open-status.
- **Beperk deze richting tot resultaatpresentatie en foutsemantiek; stel relaties, nieuwe bronnen en uitgebreide lokale provenance uit.** — Een smalle MVP is zelfstandig toetsbaar en herstelt eerst de kernbelofte dat bezoekers een betrouwbare, herleidbare externe bron kunnen raadplegen. Relaties en extra bronnen voegen complexiteit toe voordat de basisrespons betrouwbaar zichtbaar is.

## UX-voorstel: Betrouwbaar historisch zoeken met Open Archieven

**Gebruikersdoel:** Zoek op ‘Heemskerk’, begrijp welke opdracht is uitgevoerd en bekijk herleidbare historische resultaten met een duidelijke bronstatus.

### Flow
1. Open Historisch zoeken.
2. Vul ‘Heemskerk’ in en dien de zoekopdracht in.
3. Toon de geïnterpreteerde opdracht: naam=Heemskerk, taal=nl en overige verzonden parameters.
4. Toon bronstatus en result_count van Open Archieven.
5. Presenteer geldige documenten als resultaatkaarten met archieforganisatie, persoons- en gebeurtenisgegevens, sourcetype, identifier en permanente bronlink.
6. Toon afzonderlijke schermstatussen voor geldig resultaat, nulresultaat, gedeeltelijke respons, ongeldige respons en bronuitval/time-out.
7. Toon per kaart de rechten-/privacystatus als vastgesteld; toon anders expliciet ‘Onbekend’.
8. Laat de gebruiker een permanente bronlink openen zonder de bronmetadata te verliezen.

### Wireframe

[Pagina: Historisch zoeken]

H1 Historisch zoeken
[Zoekterm __________________ Heemskerk]
[Optionele filters] [Zoeken]

Na verzenden:

Zoekopdracht
Samenvatting: Zoek naar de naam ‘Heemskerk’ in Open Archieven.
Verzonden parameters: name=Heemskerk · lang=nl · number_show=3
[Toon minder details]

Bronstatus
Open Archieven — Geldige respons
49.555 gevonden · 3 getoond

Resultaatkaart
Bron: [archieforganisatie]
Titel/samenvatting: [persoons- en gebeurtenisgegevens]
Type: [sourcetype]
Identifier: [identifier]
Rechten/privacy: Onbekend
[Open permanente bronlink]

Resultaatkaart
[zelfde structuur]

Bij nulresultaat:
Open Archieven — Geen resultaten
Er zijn geen records gevonden voor deze zoekopdracht.
[Zoekopdracht aanpassen]

Bij gedeeltelijke respons:
Gedeeltelijk resultaat
De bron leverde resultaten, maar sommige gegevens of bronnen konden niet worden opgehaald.
[Toon beschikbare resultaten] [Details]

Bij bronuitval/time-out:
Bron niet beschikbaar
Open Archieven kon tijdelijk niet worden geraadpleegd. Er zijn geen resultaten weergegeven alsof ze geldig zijn.
[Opnieuw proberen] [Zoekopdracht aanpassen]

### Interactiehypotheses
- Als de exacte geïnterpreteerde parameters zichtbaar zijn, kunnen geautomatiseerde UI-tests controleren dat ‘Heemskerk’ als name=Heemskerk wordt verzonden en weergegeven.
- Als een HTTP 200-respons met number_found en docs wordt ontvangen, toont de interface ‘Geldige respons’ en minstens één resultaatkaart met identifier en permanente URL.
- Als number_found=0 wordt ontvangen, toont de interface ‘Geen resultaten’ zonder foutmelding of lege resultaatkaarten.
- Als één bron succesvol antwoordt en een andere bron faalt, toont de interface beschikbare resultaten én de status ‘Gedeeltelijk resultaat’.
- Als de bron time-out, 4xx, 5xx of een ongeldige payload retourneert, toont de interface ‘Bron niet beschikbaar’ of ‘Ongeldige respons’ en geen onbevestigde resultaatkaart.
- Als rechtenmetadata ontbreekt, toont iedere kaart ‘Onbekend’ en niet ‘open’, ‘vrij herbruikbaar’ of ‘privacyvrij’.

### Toegankelijkheid
- Alle interactieve elementen zijn volledig met het toetsenbord bereikbaar en hebben een zichtbare focusindicator.
- Gebruik semantische headings, landmarks, labels en links; resultaatkaarten zijn logisch gegroepeerd.
- Statuswijzigingen worden via een toegankelijk live region aangekondigd zonder de toetsenbordfocus onverwacht te verplaatsen.
- Gebruik voldoende kleurcontrast en laat status niet uitsluitend door kleur, iconen of positie communiceren.
- Zorg voor begrijpelijke foutteksten, consistente tabvolgorde en een expliciete naam voor de knop ‘Opnieuw proberen’.
- Permanente bronlinks zijn beschrijvend gelabeld, bijvoorbeeld ‘Open record Heemskerk bij Open Archieven’.
- De interface blijft bruikbaar bij vergroting, kleine schermen, schermlezers en zonder muis.

### Privacy
- Verwerk alleen de zoekterm en gekozen filters die nodig zijn voor de zoekopdracht.
- Sla zoektermen niet duurzaam op tenzij daarvoor een duidelijk doel en passende grondslag bestaat.
- Toon persoonsgegevens uit bronrecords alleen voor zover de bronrespons ze verstrekt en nodig zijn om het record te begrijpen.
- Neem geen algemene conclusie over openbaarheid, privacyvrijheid of herpublicatierecht; toon per record of dataset ‘Onbekend’ wanneer verificatie ontbreekt.
- Vermijd analytics waarin vrije zoektermen of recorddetails standaard als persoonsgegevens worden opgeslagen.
- Beperk logging tot technische diagnostiek, minimaliseer zoekinhoud en pas passende bewaartermijnen toe.
- Verwijs voor volledige bronvoorwaarden naar de permanente bronlink en de geldende voorwaarden van de dataset.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is autonoom uitvoerbaar en bevat reproduceerbare, toetsbare criteria. Er is wel aanzienlijke overlap met bestaande stories voor adapterfoutclassificatie, bronveerkracht en de geautomatiseerde Heemskerk-smoketest, maar dit is geen materiële blokkade.
- **INFO · SCOPE** — De kandidaat overlapt gedeeltelijk met story:75, story:63 en story:81. Stem fixtures, statusnamen en eigenaarschap af om dubbele testdekking en conflicterende contracten te voorkomen.
- **INFO · CONSISTENCY** — ‘Gedeeltelijke respons’ is in deze MVP met één externe bron beperkt of alleen relevant voor gedeeltelijk beschikbare velden. Leg vast welke fixture dit scenario representeert, zonder nieuwe productfunctionaliteit te vereisen.

## Geaccepteerde storykandidaten

### Geautomatiseerde statusmatrix voor de publieke Open Archieven-flow

_Sleutel: `openarchieven-statusmatrix-publieke-flow`_

Als Product Factory wil ik een geautomatiseerde contracttestmatrix voor de publieke historische zoekflow, zodat geldige resultaten, nulresultaten, gedeeltelijke responsen, ongeldige payloads en bronuitval aantoonbaar als afzonderlijke gebruikersstatussen worden weergegeven zonder onbevestigde resultaatkaarten.

**Acceptatiecriteria**
- De test gebruikt reproduceerbare fixtures of gecontroleerde netwerk-mocks voor geldige respons, nulresultaat, gedeeltelijke respons, ongeldige payload en timeout/5xx.
- Bij een geldige respons controleert de test minimaal de bronstatus, het gevonden aantal, één resultaatkaart, identifier en permanente bronlink.
- Bij nulresultaat controleert de test een expliciete nulresultaatstatus zonder lege of verzonnen resultaatkaarten.
- Bij gedeeltelijke respons controleert de test dat beschikbare resultaten zichtbaar blijven en de bronbeperking tekstueel wordt gemeld.
- Bij ongeldige respons of bronuitval controleert de test een expliciete foutstatus zonder onbevestigde resultaten.
- De test controleert dat ontbrekende rechten- of privacymetadata als ‘Onbekend’ wordt weergegeven.
- De test is uitvoerbaar zonder handmatige interactie en maakt failures reproduceerbaar met duidelijke diagnostiek.

Bronnen: [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://api.openarchieven.nl/1.1/records/search.json?name=Heemskerk&lang=nl&number_show=3](https://api.openarchieven.nl/1.1/records/search.json?name=Heemskerk&lang=nl&number_show=3), [https://www.openarchieven.nl/api/docs/records/search.php](https://www.openarchieven.nl/api/docs/records/search.php), [https://github.com/robbertvdzon/hkh-autopilot](https://github.com/robbertvdzon/hkh-autopilot)

Afhankelijkheden: story:75, story:82, story:63 (herkend als bestaande stories: 75, 82, 63)

Risico's: De kandidaat raakt aan bestaande stories voor adaptervalidatie, resultaatkaarten en foutstatussen; de scope blijft daarom beperkt tot de geautomatiseerde publieke contracttestmatrix., Fixtures kunnen verouderen wanneer het publieke broncontract wijzigt; tests moeten uitsluitend het afgesproken metadata-contract valideren en geen actuele aantallen hard coderen.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
