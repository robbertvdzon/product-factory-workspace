---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0065
date: 2026-08-13
status: approved
sources:
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt
  - https://hkh-autopilot.vdzonsoftware.nl
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl
  - https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/
  - https://api.europeana.eu/en
  - https://europeana.atlassian.net/wiki/spaces/EF/pages/2385739812
  - https://europeana.atlassian.net/wiki/spaces/EF/pages/2360508417
  - https://www.rijksmuseum.nl/en/collection
  - https://www.rijksmuseum.nl/en/footer/faq-collection-and-data
  - https://data.rijksmuseum.nl/assets/files/RMA_InformationDataPolicy_ENG_v1.1_def-4cc333d4f8d60978a500348bf39887e8.pdf
---
# Productcyclus 65

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De belangrijkste onbeantwoorde productvraag is hoe de bestaande historische zoekroute betrouwbaar en begrijpelijk blijft wanneer externe bronnen geheel of gedeeltelijk uitvallen, terwijl bronherkomst, rechtenstatus en Heemskerk-dekking zichtbaar en niet-misleidend blijven. De actuele acceptatieflow toont volledige bronuitval zonder resultaten of per-brondiagnose.

### Doel en huidige productstructuur

De app is een brede publieke historische ontdek- en zoekapp voor Heemskerk. Bezoekers kunnen zoeken vanuit vrije tekst, plek, persoon, gebeurtenis, periode en bron. De homepage scheidt historische ontdekking van een apart blok voor laatste nieuws.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md), [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl)

### Werkelijke acceptatiezoekactie eindigt in volledige bronuitval

Na invoer van ‘Heemskerk’ en een uitgevoerde zoekactie verscheen eerst een laadstatus en daarna ‘Geen historische bronnen konden worden geraadpleegd’, met ‘Opnieuw proberen’ en ‘Zoekopdracht aanpassen’. Er waren geen resultaten, bronstatussen, tellingen of foutredenen zichtbaar.

Bronnen: [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart)

### Technische basis ondersteunt meer transparantie dan de UI toont

De repository beschrijft zoeking in Europeana en Open Archieven zonder lokale opslag van zoekopdrachten of bronpayloads. De backend modelleert bronstatus, gedeeltelijke beschikbaarheid, volledige uitval, tellingen en een Heemskerk-indicatie; de huidige zichtbare volledige-uitvaltoestand maakt deze informatie niet beschikbaar voor de gebruiker.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt)

### Vervolgontdekking en herleidbaarheid zijn in code voorzien maar niet visueel geverifieerd

De repository beschrijft contextdetails met bron-, identifier-, URL-, rechten- en privacymetadata, expliciete bronrelaties en vervolgzoekingen vanuit zekere metadata. Door volledige bronuitval konden deze functies in de publieke flow niet worden gecontroleerd.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart)

### Beheeromgeving is zonder login zichtbaar

De beheeracceptatieomgeving toont ‘Beheerder geverifieerd’, een formulier voor nieuwspublicatie en een formulier voor lokale record-intake. Geen mutatieve actie is uitgevoerd; de feitelijke autorisatie- en beveiligingsgrenzen zijn daarom niet vastgesteld.

Bronnen: [https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/)

### Europeana biedt bruikbare federatieve zoek- en rechtenmetadata

Europeana biedt Search-, Record- en IIIF-API’s voor culturele erfgoedmetadata. De API ondersteunt zoeken en filteren op herbruikbaarheid en rechten; volgens de officiële FAQ is metadata CC0, terwijl gekoppelde digitale objecten hun eigen rights statement behouden.

Bronnen: [https://api.europeana.eu/en](https://api.europeana.eu/en), [https://europeana.atlassian.net/wiki/spaces/EF/pages/2385739812](https://europeana.atlassian.net/wiki/spaces/EF/pages/2385739812), [https://europeana.atlassian.net/wiki/spaces/EF/pages/2360508417](https://europeana.atlassian.net/wiki/spaces/EF/pages/2360508417)

### Rijksmuseum toont publieksvriendelijke collectie-ontdekking

De Rijksmuseum-collectie combineert zoeken, thematische ontdekking, visitor stories en persoonlijke galerijen. De officiële informatie verwijst daarnaast naar een afzonderlijk open-databeleid, wat bruikbaar is als inspiratie voor een duidelijke scheiding tussen collectiecontext en hergebruikrechten.

Bronnen: [https://www.rijksmuseum.nl/en/collection](https://www.rijksmuseum.nl/en/collection), [https://www.rijksmuseum.nl/en/footer/faq-collection-and-data](https://www.rijksmuseum.nl/en/footer/faq-collection-and-data), [https://data.rijksmuseum.nl/assets/files/RMA_InformationDataPolicy_ENG_v1.1_def-4cc333d4f8d60978a500348bf39887e8.pdf](https://data.rijksmuseum.nl/assets/files/RMA_InformationDataPolicy_ENG_v1.1_def-4cc333d4f8d60978a500348bf39887e8.pdf)

### Huidige applicatie

**Doel:** De applicatie maakt de geschiedenis van Heemskerk toegankelijk via publieke historische bronnen. Een brede doelgroep kan zoeken vanuit een gewone vraag of filters voor plek, persoon, gebeurtenis, periode en bron, met als doel lokale geschiedenis in bredere historische context te ontdekken.

**Wat ontbreekt:**
- Een veilige acceptatiezoekactie eindigt in volledige bronuitval zonder per-bronstatus, foutreden of resultaatinformatie.
- De gebruiker kan niet zien welke externe bronnen zijn geraadpleegd, welke beschikbaar waren of hoeveel resultaten elke bron leverde.
- Resultaatdetails, bronrelaties, vervolgzoekingen en de betekenis van de Heemskerk-indicatie konden door bronuitval niet visueel worden beoordeeld.
- De zoekinterface toont in de bekeken toestand geen zichtbare rechten- of privacymetadata.
- De publieke beheeromgeving toont nieuwspublicatie en lokale record-intake zonder dat de autorisatiegrenzen in dit onderzoek zijn vastgesteld.
- De CanvasKit-weergave maakt volledige semantische toegankelijkheidscontrole via DOM-inspectie niet mogelijk; visuele controle alleen bewijst geen schermlezerondersteuning.

### Verbetermogelijkheden

- Toon per geselecteerde bron een duidelijke status, korte foutcategorie en zichtbare resultatentelling.
- Behoud en label beschikbare deelresultaten wanneer slechts één bron faalt.
- Maak volledige bronuitval diagnostisch met bronoverzicht, concrete vervolgstap en uitleg over ontbrekende dekking.
- Leg de Heemskerk-indicatie uit als metadata-indicatie en niet als historische waarheid.
- Toon per resultaat bronnaam, stabiele identifier, originele bronlink, ophaalstatus en rechtenstatus; gebruik ‘onbekend’ wanneer rechten niet expliciet zijn vastgesteld.
- Gebruik herleidbare metadata voor veilige vervolgzoekingen vanuit plaats, persoon, gebeurtenis en periode, zonder onbewezen relaties als feiten te presenteren.
- Voeg voorbeelden of invoerhints toe voor bezoekers zonder archiefkennis.
- Test laad-, fout- en bronstatussen programmatisch met toetsenbord en schermlezer in de Flutter-webdoelomgeving.

### Inspiratiebronnen

- [Europeana](https://www.europeana.eu/en) — Federatieve ontdekking over collecties van meerdere instellingen; relevant voor zoekfilters, broncontext en rechtenmetadata.
- [Rijksmuseum Collection Online](https://www.rijksmuseum.nl/en/collection) — Publieksvriendelijke combinatie van collectiezoeken, thematische ontdekking en visitor stories; relevant voor betekenisvolle vervolgnavigatie.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md) | 2026-08-13 | Publieke GitHub-repository; expliciete repositorylicentie is in de geraadpleegde README niet vastgesteld. | Primaire productdocumentatie over componenten, zoekgedrag, privacy, bronmetadata en vervolgontdekking. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart) | 2026-08-13 | Publieke broncode; expliciete licentie is op de geraadpleegde raw-bestandspagina niet vastgesteld. | Primaire bron voor de Flutter-zoekroute, zoekvelden, bronkeuze en fout-/statusgedrag. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt) | 2026-08-13 | Publieke broncode; expliciete licentie is op de geraadpleegde raw-bestandspagina niet vastgesteld. | Primaire bron voor bronstatussen, gedeeltelijke beschikbaarheid, volledige uitval, tellingen en Heemskerk-indicatie. |
| [bron](https://hkh-autopilot.vdzonsoftware.nl) | 2026-08-13 | Publieke applicatie; expliciete interface-licentie of hergebruikrecht niet vastgesteld. | Werkelijk bekeken productiehomepage en historische zoekroute. |
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl) | 2026-08-13 | Publieke acceptatieomgeving met representatieve nepdata; expliciete interface-licentie of hergebruikrecht niet vastgesteld. | Werkelijk bekeken zoekactie met dummyterm en volledige-uitvaltoestand. |
| [bron](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/) | 2026-08-13 | Publieke beheerinterface; expliciete interface-licentie of hergebruikrecht niet vastgesteld. | Werkelijk bekeken beheeromgeving zonder login; mutaties zijn overgeslagen. |
| [bron](https://api.europeana.eu/en) | 2026-08-13 | Europeana API-dienst met eigen gebruiksvoorwaarden; rechten op objecten volgen de metadata van de betreffende bron. | Officiële documentatie over Search-, Record- en IIIF-API’s. |
| [bron](https://europeana.atlassian.net/wiki/spaces/EF/pages/2385739812) | 2026-08-13 | Publieke Europeana-ontwikkelaarsdocumentatie; afzonderlijke documentlicentie niet vastgesteld. | Officiële specificatie van zoekfilters, rechtenvelden en herbruikbaarheidsfilters. |
| [bron](https://europeana.atlassian.net/wiki/spaces/EF/pages/2360508417) | 2026-08-13 | Publieke Europeana-FAQ; afzonderlijke documentlicentie niet vastgesteld. De FAQ vermeldt CC0 voor API-metadata en recordafhankelijke rechten voor gekoppelde objecten. | Rechtenindicatie voor metadata versus digitale bronobjecten. |
| [bron](https://www.rijksmuseum.nl/en/collection) | 2026-08-13 | Publieke Rijksmuseum-website; rechten op afbeeldingen en collectieobjecten zijn object- en beleidsafhankelijk. | Werkelijk geraadpleegde vergelijkbare collectie- en ontdekervaring. |
| [bron](https://www.rijksmuseum.nl/en/footer/faq-collection-and-data) | 2026-08-13 | Publieke Rijksmuseum-informatieve pagina; hergebruik van paginatekst niet als licentie vastgesteld. | Verwijst naar het open-databeleid en de regels rond digitale objecten. |
| [bron](https://data.rijksmuseum.nl/assets/files/RMA_InformationDataPolicy_ENG_v1.1_def-4cc333d4f8d60978a500348bf39887e8.pdf) | 2026-08-13 | Publiek Rijksmuseum-beleidsdocument; expliciete hergebruiklicentie van het document zelf niet vastgesteld. | Officieel beleidsanker voor informatie-, data- en copyrightprincipes. |

## Productbeslissing

Maak de externe historische zoekroute brontransparant en veerkrachtig: toon per geselecteerde bron de status, korte foutcategorie en resultatentelling; behoud beschikbare deelresultaten; geef bij volledige uitval een concrete uitleg en vervolgstap; toon bij elk resultaat de bronnaam, stabiele identifier, oorspronkelijke bronlink en expliciete rechtenstatus, met ‘onbekend’ wanneer die status niet is vastgesteld.

**Waarom:** Deze kleine, samenhangende richting sluit direct aan op epic theme-hkh-autopilot-0002 en adresseert de aantoonbare tekortkoming dat volledige bronuitval nu eindigt zonder diagnose, dekking of broninformatie. Zij versterkt betrouwbaarheid, openheid en herbruikbaarheid zonder historische claims toe te voegen. De technische basis modelleert al bronstatus, gedeeltelijke beschikbaarheid, volledige uitval, tellingen en Heemskerk-indicatie; de richting maakt die bestaande informatie zichtbaar en voorkomt dat rechten- of Heemskerk-indicaties als historische waarheden worden geïnterpreteerd.

### Prioriteiten
- Per-bronstatus en resultatentelling zichtbaar maken in normale, gedeeltelijke en volledige-uitvaltoestanden.
- Beschikbare deelresultaten behouden wanneer een andere bron faalt, met duidelijke dekkingsuitleg.
- Volledige bronuitval voorzien van een begrijpelijke diagnose en concrete vervolgstap.
- Resultaatmetadata uitbreiden met bronnaam, stabiele identifier, oorspronkelijke bronlink en rechtenstatus; onbekende rechten expliciet als onbekend tonen.
- Laad-, fout- en bronstatussen programmatisch toetsen met toetsenbord- en schermlezerondersteuning in de Flutter-webdoelomgeving.

### Besluiten
- **Maak bronstatus en dekking een vast onderdeel van de zoekresultaatweergave.** — De acceptatieflow toont nu alleen een generieke foutmelding, terwijl de backend al onderscheid maakt tussen beschikbaarheidstoestanden en tellingen. Dit maakt de zoekroute controleerbaar en begrijpelijk bij externe bronproblemen.
- **Behoud deelresultaten en label ontbrekende brondekking expliciet.** — De missie vraagt verbinding met bronnen buiten Heemskerk; tijdelijke uitval van één bron mag daarom niet leiden tot het verlies van bruikbare resultaten uit andere bronnen. De interface moet wel ondubbelzinnig aangeven welke dekking ontbreekt.
- **Toon herleidbare bron- en rechtenmetadata zonder rechtenstatus af te leiden.** — Bronlinks en identifiers ondersteunen betrouwbaarheid en hergebruik. Europeana maakt onderscheid tussen metadatarechten en rechten op gekoppelde objecten; daarom wordt alleen expliciete rechteninformatie getoond en anders ‘onbekend’ gebruikt.

## UX-voorstel: Brontransparante historische zoekroute

**Gebruikersdoel:** Een bezoeker zoekt historische informatie over Heemskerk en begrijpt welke bronnen beschikbaar waren, welke resultaten betrouwbaar herleidbaar zijn en wat ontbrekende brondekking betekent.

### Flow
1. Bezoeker opent Historisch zoeken en voert bijvoorbeeld ‘Heemskerk’ in.
2. Bezoeker start de zoekactie en ziet een toegankelijke laadstatus.
3. De resultatenpagina toont per geselecteerde bron status, korte foutcategorie en resultatentelling.
4. Beschikbare deelresultaten blijven zichtbaar wanneer een andere bron uitvalt, met een duidelijke dekkingswaarschuwing.
5. Bij volledige bronuitval toont de pagina per-brondiagnose, uitleg over ontbrekende dekking en acties ‘Opnieuw proberen’ en ‘Zoekopdracht aanpassen’.
6. Elk resultaat toont bronnaam, stabiele identifier, oorspronkelijke bronlink en expliciete rechtenstatus; ontbrekende rechten worden als ‘Onbekend’ weergegeven.
7. Bezoeker kan via toetsenbord broninformatie openen en een originele bronlink volgen zonder onbewezen historische relaties als feiten te zien.

### Wireframe

[Pagina: Historisch zoeken]\n\nTerug naar zoeken\n\nZoekopdracht: [ Heemskerk                         ] [Zoeken]\nFilters: plek | persoon | gebeurtenis | periode | bron\n\nStatusregio (aria-live): ‘Zoekresultaten worden geladen’\n\n[Bronoverzicht]\n- Europeana — Beschikbaar — 12 resultaten\n- Open Archieven — Tijdelijk niet beschikbaar — foutcategorie: time-out — 0 resultaten\n\n[Dekkingsmelding]\n‘Er zijn resultaten gevonden, maar niet alle geselecteerde bronnen konden worden geraadpleegd. De resultaten vertegenwoordigen daarom geen volledige brondekking.’\n\n[Resultaatkaart]\nTitel\nKorte context\nBron: Europeana\nIdentifier: XXXXX\nRechten: Onbekend\n[Open originele bron]\n\n[Volledige uitvalvariant]\n‘Geen historische bronnen konden worden geraadpleegd.’\nPer-bronstatussen en foutcategorieën\n‘Er zijn geen resultaten beschikbaar zolang de bronnen niet reageren.’\n[Opnieuw proberen] [Zoekopdracht aanpassen]\n\nToetsenbordvolgorde: zoekveld → filters → Zoeken → bronoverzicht → melding → resultaatkaarten → acties.

### Interactiehypotheses
- H1: Als per-bronstatussen en tellingen zichtbaar zijn, kunnen geautomatiseerde UI-tests vaststellen dat gebruikers bij normale, gedeeltelijke en volledige uitval een onderscheidende diagnose ontvangen.
- H2: Als deelresultaten behouden blijven, toont een geautomatiseerde test bij uitval van één bron nog steeds resultaten van beschikbare bronnen en een expliciete melding over ontbrekende dekking.
- H3: Als elk resultaat identifier, originele bronlink en rechtenstatus bevat, kunnen tests verifiëren dat metadata herleidbaar is en dat ontbrekende rechten als ‘Onbekend’ worden weergegeven.
- H4: Als laad- en foutmeldingen in een aria-live-status staan en acties semantische knoppen en links zijn, kunnen toetsenbord- en toegankelijkheidstests alle toestanden bereiken en benoemen.
- H5: Als de Heemskerk-indicatie als metadata-indicatie wordt gelabeld, bevat de interface geen formulering die deze indicatie als bewezen historische waarheid presenteert.
- H6: Als ‘Opnieuw proberen’ en ‘Zoekopdracht aanpassen’ beschikbaar zijn bij volledige uitval, kunnen tests verifiëren dat beide acties naar een voorspelbare volgende toestand leiden zonder zoekgegevens lokaal op te slaan.

### Toegankelijkheid
- Gebruik semantische koppen, labels, knoppen, links en een logisch tabvolgorde.
- Maak laad-, gedeeltelijke-uitval- en volledige-uitvalmeldingen programmatisch beschikbaar via aria-live of equivalente Flutter-semantiek.
- Gebruik statuslabels naast kleur, zodat beschikbaarheid en fouten niet alleen via kleur worden onderscheiden.
- Voldoe aan voldoende kleurcontrast en behoud zichtbare focusindicatoren.
- Maak foutcategorieën en dekkingsmeldingen begrijpelijk voor schermlezers.
- Laat alle zoek-, filter-, retry- en navigatieacties volledig met het toetsenbord uitvoeren.
- Test geautomatiseerd op focusvolgorde, naam/rol/waarde, toetsenbordbediening en statusupdates in Flutter Web.

### Privacy
- Sla geen zoekopdrachten, identifiers of bronpayloads lokaal of op de server op tenzij daarvoor een duidelijk productdoel, minimale bewaartermijn en passende grondslag bestaat.
- Verstuur alleen de noodzakelijke zoekparameters naar externe bronnen; voeg geen persoonsgegevens of gebruikersprofielen toe.
- Toon bronmetadata en rechteninformatie uitsluitend zoals door de bron aangeleverd; leid geen rechten af uit een URL of algemene bronstatus.
- Gebruik stabiele bronidentifiers voor herleidbaarheid, maar vermijd het koppelen ervan aan individuele bezoekers.
- Documenteer in de interface of privacyinformatie dat zoekopdrachten naar externe bronnen kunnen worden doorgestuurd en welke gegevens daarbij worden gedeeld.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is klein, toetsbaar en uitvoerbaar zonder handmatige productbesluiten of externe eigenaaracties. Er zijn geen blokkerende problemen.
- **WARNING · CONSISTENCY** — Er is gedeeltelijke overlap met gepubliceerde stories 61, 62 en 63 over rechtenstatus en bronmetadata. Bewaak dat deze kandidaat uitsluitend de uitleg en fail-closed weergavelogica toevoegt en geen concurrerend metadata-contract introduceert.
- **INFO · SOURCE** — De aangehaalde publieke broncode- en documentatiepagina’s hebben geen vastgestelde expliciete hergebruiklicentie. De kandidaat reproduceert echter geen omvangrijke broninhoud en gebruikt de bronnen alleen als functionele en rechteninhoudelijke basis.

## Geaccepteerde storykandidaten

### Uitleg over rechtenstatus bij historische bronresultaten

_Sleutel: `rechtenstatus-uitleg-bij-bronmetadata`_

Maak bij de rechtenstatus van elk historisch zoekresultaat zichtbaar wat de bron wel en niet bevestigt. De interface onderscheidt metadatarechten van rechten op gekoppelde digitale objecten en toont ‘Onbekend’ wanneer de externe bron geen expliciete status levert, zonder zelf rechten af te leiden.

**Acceptatiecriteria**
- Elk resultaat toont een tekstuele rechtenstatus die uitsluitend uit de aangeleverde bronmetadata komt.
- De interface legt begrijpelijk uit dat rechten op metadata kunnen verschillen van rechten op gekoppelde digitale objecten.
- Ontbrekende, tegenstrijdige of niet-verifieerbare rechteninformatie wordt als ‘Onbekend’ weergegeven.
- Geautomatiseerde tests verifiëren dat een bronlink, algemene API-status of herkomstlabel nooit zelfstandig een rechtenstatus oplevert.
- De uitleg is beschikbaar via toetsenbordbedienbare semantische interface-elementen en wordt niet uitsluitend door kleur of een icoon overgebracht.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart), [https://api.europeana.eu/en](https://api.europeana.eu/en), [https://europeana.atlassian.net/wiki/spaces/EF/pages/2385739812](https://europeana.atlassian.net/wiki/spaces/EF/pages/2385739812), [https://europeana.atlassian.net/wiki/spaces/EF/pages/2360508417](https://europeana.atlassian.net/wiki/spaces/EF/pages/2360508417)

Afhankelijkheden: story:61, story:62 (herkend als bestaande stories: 61, 62)

Risico's: De gebruikte externe bron kan rechteninformatie onvolledig of inconsistent aanleveren; de implementatie moet daarom fail-closed blijven., De uitleg kan door gebruikers worden opgevat als juridisch advies; tekst moet beperkt blijven tot brontransparantie en geen hergebruikstoestemming suggereren.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
