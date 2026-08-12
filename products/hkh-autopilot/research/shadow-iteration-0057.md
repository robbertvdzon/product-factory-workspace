---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0057
date: 2026-08-12
status: approved
sources:
  - https://github.com/robbertvdzon/hkh-autopilot
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/main.dart
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/news/discover_section.dart
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend-admin/lib/main.dart
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl
  - https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/
  - https://www.openarchieven.nl/api/docs/
  - https://www.openarchieven.nl/datasets/nha
  - https://opendata.archieven.nl/en/datasets-en/dataset-en?guid=F110BAA9B5B942C196FD551C346F0BBA
  - https://opendata.archieven.nl/nl/over-open-data
---
# Productcyclus 57

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De belangrijkste onbeantwoorde productvraag is hoe de huidige homepage, die uitsluitend admin-nieuws doorzoekt, kan uitgroeien tot een betrouwbare publieke historische ontdekroute met externe resultaten, herleidbare bronmetadata en begrijpelijke rechten-/privacystatus. De repository ondersteunt al statusfeedback, nieuws zoeken, recordintake en externe verificatie, maar de volledige publieke bronzoek- en publicatieketen ontbreekt. De acceptatie-UI kon niet visueel worden beoordeeld omdat Chromium in deze runtime niet startte.

### Publieke homepage zoekt alleen in admin-nieuws

De Flutter-homepage toont productintroductie, service-status, laatste nieuws en een ontdekblok. Het ontdekblok gebruikt uitsluitend GET /api/news en zoekt in gepubliceerde nieuwsberichten op vrije tekst en statische labels voor plek, persoon en gebeurtenis. De functionele specificatie maakt expliciet dat dit geen historische externe bronzoeking is.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/main.dart), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/news/discover_section.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/news/discover_section.dart), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md)

### Bestaande homepage heeft bruikbare status- en toegankelijkheidsbouwstenen

Service en nieuws hebben afzonderlijke laad-, fout-, succes- en lege toestanden. Statusmeldingen gebruiken Semantics-statusnodes; retry-acties zijn toetsenbordbedienbaar en krijgen een contrasterende focusrand. Deze bouwstenen kunnen worden hergebruikt voor externe bronzoeking, maar de externe bronstatus zelf bestaat nog niet als publieke route.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/main.dart), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md)

### Admin ondersteunt nieuwspublicatie en recordintake, maar geen publieke publicatieflow

Het beheergedeelte ondersteunt authenticatie, het publiceren van admin-nieuws en een formulier voor één lokaal collectierecord als intern concept. De specificatie sluit opslag, REST-publicatie, beheer van een volledige collectie en daadwerkelijke publieke publicatie van koppelingsdossiers uit. Daardoor is geen aantoonbare end-to-end route aanwezig van bronintake naar publiek historisch zoekresultaat.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend-admin/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend-admin/lib/main.dart), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md)

### Open Archieven en Noord-Hollands Archief bieden een haalbaar metadata-startpunt

Open Archieven biedt zoek-, match- en recorddetailmogelijkheden en OAI-PMH/A2A-toegang. De API documenteert een limiet van vier verzoeken per seconde per IP, caching en het gebruik van een beschrijvende user-agent. De Noord-Hollands Archiefdataset bevat miljoenen historische documentmetadata en persoonsvermeldingen. Een concrete Heemskerk-dataset vermeldt CC0 1.0, maar rechten op afzonderlijke objecten of media moeten apart worden behandeld.

Bronnen: [https://www.openarchieven.nl/api/docs/](https://www.openarchieven.nl/api/docs/), [https://www.openarchieven.nl/datasets/nha](https://www.openarchieven.nl/datasets/nha), [https://opendata.archieven.nl/en/datasets-en/dataset-en?guid=F110BAA9B5B942C196FD551C346F0BBA](https://opendata.archieven.nl/en/datasets-en/dataset-en?guid=F110BAA9B5B942C196FD551C346F0BBA), [https://opendata.archieven.nl/nl/over-open-data](https://opendata.archieven.nl/nl/over-open-data)

### Metadatarechten en objectrechten moeten zichtbaar gescheiden blijven

De geraadpleegde Noord-Hollands Archiefdataset vermeldt CC0 1.0 voor de dataset, terwijl het dossier en de externe broncontext geen automatisch hergebruikrecht voor scans, foto’s of andere objectmedia bewijzen. Een veilige publieke route moet daarom kunnen volstaan met minimale metadata en een stabiele externe bronlink wanneer objectrechten onbekend zijn.

Bronnen: [https://opendata.archieven.nl/en/datasets-en/dataset-en?guid=F110BAA9B5B942C196FD551C346F0BBA](https://opendata.archieven.nl/en/datasets-en/dataset-en?guid=F110BAA9B5B942C196FD551C346F0BBA), [https://opendata.archieven.nl/nl/over-open-data](https://opendata.archieven.nl/nl/over-open-data), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md)

### Externe API’s tonen bruikbare patronen voor bronstatus, facetten en pagination

Europeana biedt Search-, Record-, Entity- en Thumbnail-API’s, met zoekfilters, rechten-/herbruikbaarheidsindeling en paginering. Het Rijksmuseum biedt een keyloze Search API met persistente identifiers, gecontroleerde vocabularia en pageToken-pagination. Deze patronen zijn relevant voor een bronadapter die zoekresultaten beperkt, herleidbaar en uitbreidbaar maakt.

Bronnen: [https://pro.europeana.eu/discover-the-data/apis](https://pro.europeana.eu/discover-the-data/apis), [https://pro.europeana.eu/post/can-i-use-it](https://pro.europeana.eu/post/can-i-use-it), [https://data.rijksmuseum.nl/docs/search](https://data.rijksmuseum.nl/docs/search), [https://data.rijksmuseum.nl/docs/](https://data.rijksmuseum.nl/docs/)

### Visuele acceptatiebeoordeling is niet gelukt

De voorgeschreven Playwright-screenshotmethode is uitgevoerd voor de publieke en admin-acceptatieomgeving, maar Chromium beëindigde zichzelf vóór navigatie door een macOS mach-port-permissionfout. Er zijn daarom geen betrouwbare visuele observaties over layout, labels, doorkliknavigatie of bruikbaarheid van de draaiende omgevingen.

Bronnen: [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl), [https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/)

### Huidige applicatie

**Doel:** De applicatie is een brede publieke historische ontdekervaring voor mensen die iets willen weten over een gebouw, straat, persoon, gebeurtenis of ander onderwerp uit de geschiedenis van Heemskerk. De beoogde werking is historische kennis toegankelijk maken via gewone taal en verbindingen met externe bronnen. Het admin-gedeelte is bedoeld voor geautoriseerde beheerders die admin-nieuws en lokale recordintake beheren.

**Wat ontbreekt:**
- De publieke homepage zoekt momenteel in admin-nieuws; er is geen aantoonbare algemene historische zoekroute naar externe collecties.
- Zoekresultaten uit externe bronnen, bronhouder, stabiele identifier, bronversie, ophaaldatum en technische beschikbaarheidsstatus zijn nog geen publieke resultaatvelden.
- De huidige publieke code toont geen uniforme, begrijpelijke rechtenstatus en privacybeperking per extern resultaat.
- De admin-recordintake maakt interne concepten, maar de functionele specificatie sluit opslag/publicatie van een volledige publieke koppelingsflow uit.
- De acceptatieomgeving kon niet visueel worden gevalideerd door Chromium-runtimebeperkingen; actuele UI-bruikbaarheid en navigatie blijven daardoor gedeeltelijk onbevestigd.
- Er is geen bewijs in de geraadpleegde repositorybestanden dat objectmedia, externe recordresultaten of metadatarechten publiek veilig worden doorgegeven.

### Verbetermogelijkheden

- Maak een zelfstandige historische zoekingang naast ‘Laatste nieuws’, zodat nieuwsberichten niet langer als historische bron of zoekindex fungeren. Dit volgt direct uit de huidige scheiding in de code en de beschikbare Open Archieven zoekmogelijkheden. Bronnen: https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/news/discover_section.dart, https://www.openarchieven.nl/api/docs/.
- Gebruik per resultaat een compact herkomstblok met stabiele identifier, bronhouder, titel/beschrijving, datering, bronversie of momentopname, ophaaldatum en externe recordlink. Dat maakt resultaten controleerbaar en bestand tegen gewijzigde externe datasets. Bronnen: https://www.openarchieven.nl/api/docs/, https://www.openarchieven.nl/datasets/nha.
- Toon bronbeschikbaarheid, rechtenstatus en privacybeperking als tekstuele statussen naast resultaten, met fail-closed gedrag bij ontbrekende of tegenstrijdige waarden. Houd metadata en objectmedia afzonderlijk, omdat CC0 voor metadata geen bewijs is voor mediagebruik. Bronnen: https://opendata.archieven.nl/en/datasets-en/dataset-en?guid=F110BAA9B5B942C196FD551C346F0BBA, https://opendata.archieven.nl/nl/over-open-data.
- Ontwerp zoekresultaten voor gewone vragen én gerichte verkenning via plek, persoon, gebeurtenis, datum en bron, met pagination en lege-/fouttoestanden. De huidige Semantics- en retry-bouwstenen kunnen hiervoor worden hergebruikt. Bronnen: https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/main.dart, https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md, https://data.rijksmuseum.nl/docs/search.
- Onderzoek een gefaseerde bronstrategie: start met keyloze of al beschikbare bronnen en leg voor bronnen met API-key alleen de aanvraagroute vast totdat eigenaarstoestemming of toegang geregeld is. Europeana is inhoudelijk relevant maar vereist een API-key; Rijksmuseum biedt een keyloze Search API, maar is primair een museumcollectie en niet specifiek Heemskerk. Bronnen: https://pro.europeana.eu/discover-the-data/apis, https://pro.europeana.eu/page/get-api, https://data.rijksmuseum.nl/docs/search.
- Gebruik persistente identifiers en eventueel IIIF-manifests uitsluitend als externe verwijzing of viewer-integratie wanneer rechten dit toelaten. IIIF biedt een gestandaardiseerde Presentation API, maar de huidige veilige scope hoeft geen media te kopiëren. Bron: https://iiif.io/api/presentation/3.0/.
- Herhaal de volledige visuele acceptatiecontrole in een omgeving waarin Chromium kan starten, inclusief publieke zoekflow, lege resultaten, bronfout, statuslabels, terugnavigatie en admin-intake. Bron: https://hkh-autopilot-acceptance.vdzonsoftware.nl, https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/.

### Inspiratiebronnen

- [Europeana](https://www.europeana.eu/en/) — Vergelijkbare brede erfgoedzoekomgeving die collecties van musea, bibliotheken en archieven samenbrengt; de API-documentatie toont Search-, Record- en Entity-API’s en rechten-/herbruikbaarheidsfilters.
- [Rijksmuseum Collection Online en Data Services](https://data.rijksmuseum.nl/docs/search) — Relevant patroon voor zoeken op kenmerken, persistente identifiers, gecontroleerde vocabularia, keyloze toegang en pageToken-pagination; de collectiepagina voegt thematische ontdekking en verhalen toe.
- [IIIF Presentation API](https://iiif.io/api/presentation/3.0/) — Interoperabiliteitsinspiratie voor stabiele externe objectpresentaties en manifests zonder lokale mediakopie; toepassen vereist afzonderlijke rechtencontrole.
- [Open Archieven](https://www.openarchieven.nl/) — Direct relevante Nederlandse bronervaring en technische inspiratie voor persoons-, gebeurtenis- en recordzoeken met A2A/OAI-PMH-herkomst.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://github.com/robbertvdzon/hkh-autopilot) | 2026-08-12 | Publieke GitHub-repository; geen LICENSE- of LICENSE.md-bestand gevonden op main, dus repositorylicentie onbekend. | Repository-overzicht en primaire bron voor de applicatiecomponenten. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md) | 2026-08-12 | Geen afzonderlijke licentie-indicatie in het geraadpleegde bestand; onbekend. | Bevestigt componenten, frontenddoel en algemene architectuur. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/main.dart) | 2026-08-12 | Geen afzonderlijke licentie-indicatie in het bronbestand; repositorylicentie onbekend. | Primaire bron voor homepage-opbouw, statusstaten en nieuwsroute. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/news/discover_section.dart) | 2026-08-12 | Geen afzonderlijke licentie-indicatie in het bronbestand; repositorylicentie onbekend. | Primaire bron voor het huidige homepage-ontdekblok en de beperking tot nieuws. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend-admin/lib/main.dart) | 2026-08-12 | Geen afzonderlijke licentie-indicatie in het bronbestand; repositorylicentie onbekend. | Primaire bron voor admin-authenticatie, nieuwsbeheer en recordintake. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md) | 2026-08-12 | Geen afzonderlijke licentie-indicatie in het document; repositorylicentie onbekend. | Primaire bron voor functionele scope, privacyregels, bronverificatie en uitgesloten publicatieflow. |
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl) | 2026-08-12 | Onbekend; de omgeving kon door runtimefout niet visueel worden geladen. | Verplichte publieke acceptatieomgeving voor beoordeling van feitelijke bruikbaarheid. |
| [bron](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/) | 2026-08-12 | Onbekend; de omgeving kon door runtimefout niet visueel worden geladen. | Verplichte admin-acceptatieomgeving voor beoordeling van beheerflow en duidelijkheid. |
| [bron](https://www.openarchieven.nl/api/docs/) | 2026-08-12 | Rechten/licentie van de documentatiepagina niet vastgesteld; API-gebruiksvoorwaarden en rate-limit staan publiek beschreven. | Technische bron voor zoek-, record-, OAI-PMH-, caching- en rate-limitmogelijkheden. |
| [bron](https://www.openarchieven.nl/datasets/nha) | 2026-08-12 | Licentie-indicatie van de datasetpagina geraadpleegd; afzonderlijke objectrechten niet automatisch vastgesteld. | Onderbouwt omvang, A2A/OAI-PMH-beschikbaarheid en bronomvang van Noord-Hollands Archiefmetadata. |
| [bron](https://opendata.archieven.nl/en/datasets-en/dataset-en?guid=F110BAA9B5B942C196FD551C346F0BBA) | 2026-08-12 | CC0 1.0 zoals expliciet vermeld op de datasetpagina; dit is geen automatisch bewijs voor objectmediarechten. | Concrete Heemskerk-dataset met data-eigenaar, permanente datasetlink en licentie-indicatie. |
| [bron](https://opendata.archieven.nl/nl/over-open-data) | 2026-08-12 | Rechteninformatie zoals publiek op de bronpagina; exacte afzonderlijke objectrechten blijven bronafhankelijk. | Context voor open data, metadatahergebruik en het onderscheid tussen dataset- en objectrechten. |

## Productbeslissing

Bouw één publieke historische zoekroute voor Heemskerk met uitsluitend herleidbare metadata en externe recordlinks uit Open Archieven/Noord-Hollands Archief, naast de bestaande admin-nieuwsrubriek. Start met vrije tekst plus plek, persoon, gebeurtenis en datum als zoekingangen; toon per resultaat bronhouder, titel of beschrijving, datering, stabiele identifier, ophaaldatum, externe link en afzonderlijke statussen voor beschikbaarheid, rechten en privacy.

**Waarom:** Dit is een kleine, samenhangende stap richting de missie en het open roadmapthema voor externe archiefbronnen. De huidige homepage gebruikt nieuws als ontdekindex, terwijl Open Archieven en Noord-Hollands Archief een haalbare metadata-ingang bieden. De scope blijft veilig en uitvoerbaar: geen lokale mediakopieën, geen gevoelige persoonsgegevens en geen publicatie van onbewezen objectrechten. Herleidbare metadata, expliciete bronstatussen en externe links ondersteunen de principes verbonden, betrouwbaar, toegankelijk, open en herbruikbaar.

### Prioriteiten
- Maak de historische zoekroute functioneel onafhankelijk van admin-nieuws.
- Implementeer één bronadapter voor Open Archieven/Noord-Hollands Archief met rate limiting, caching, beschrijvende user-agent en paginering.
- Toon herkomstvelden en een stabiele externe recordlink per resultaat.
- Scheid metadatarechten van rechten op scans, foto’s en andere media; toon ontbrekende of tegenstrijdige rechten- en privacyinformatie als niet-vrijgegeven status.
- Herbruik bestaande laad-, fout-, lege-, retry- en toegankelijkheidsstatussen op de publieke zoekroute.

### Besluiten
- **Gebruik Open Archieven/Noord-Hollands Archief als eerste en enige externe bron in deze richting.** — Deze bron is inhoudelijk relevant voor Noord-Holland, technisch toegankelijk en geschikt voor een beperkte metadatazoekroute zonder nieuwe eigenaarstoegang.
- **Publiceer alleen minimale metadata en een externe bronlink; kopieer geen lokale media.** — Een CC0-indicatie voor een dataset bewijst niet automatisch hergebruikrechten voor afzonderlijke objectmedia. Externe verwijzing beperkt rechtenrisico’s en houdt de broncontext zichtbaar.
- **Maak bron-, rechten- en privacystatus begrijpelijke tekstvelden in elk resultaat.** — Resultaten moeten controleerbaar zijn en concrete risico’s zichtbaar maken. Ontbrekende of tegenstrijdige informatie blokkeert mediagebruik en gevoelige publicatie, maar blokkeert de veilige metadatazoekroute niet automatisch.
- **Gebruik vrije tekst en gerichte facetten voor plek, persoon, gebeurtenis en datum, met duidelijke lege-, fout- en beschikbaarheidsstatussen.** — Dit sluit aan op gewone nieuwsgierigheid en het open roadmapthema ontdekken via plek, persoon en gebeurtenis, terwijl bestaande toegankelijkheidsbouwstenen herbruikbaar blijven.

## UX-voorstel: Publieke historische zoekroute Heemskerk

**Gebruikersdoel:** Een bezoeker vindt betrouwbare historische metadata over een plek, persoon, gebeurtenis of periode en kan het originele externe archiefrecord openen.

### Flow
1. Bezoeker opent de homepage en kiest ‘Historisch zoeken’, los van ‘Laatste nieuws’.
2. Bezoeker voert vrije tekst in en kan optioneel plek, persoon, gebeurtenis, datum en bron instellen.
3. Bezoeker activeert ‘Zoeken’. De interface toont laadstatus en kondigt die aan aan schermlezers.
4. De resultatenlijst toont uitsluitend minimale metadata met bronhouder, titel of beschrijving, datering, stabiele identifier, ophaaldatum en externe recordlink.
5. Per resultaat ziet de bezoeker afzonderlijke statussen voor bronbeschikbaarheid, metadatarechten, objectmediarechten en privacy.
6. Bezoeker opent ‘Bekijk origineel record’ in de externe bron; lokaal worden geen scans of andere media gekopieerd.
7. Bij geen resultaten, bronfout of tijdelijke onbeschikbaarheid ziet de bezoeker een begrijpelijke status, mogelijke vervolgstap en toetsenbordbedienbare retry-actie.

### Wireframe

[Header]
Logo / Heemskerk Historisch Kennisplatform
Navigatie: Historisch zoeken | Laatste nieuws

[Intro]
Historisch zoeken in bronnen over Heemskerk
Zoek op gewone woorden, plek, persoon, gebeurtenis of periode.

[Zoekformulier]
Vrije zoekterm: [________________________]
Plek: [optioneel]  Persoon: [optioneel]
Gebeurtenis: [optioneel]  Vanaf datum: [____]  Tot datum: [____]
Bron: [Open Archieven / Noord-Hollands Archief]
[Zoeken]

[Statusgebied]
‘Zoeken in Open Archieven en Noord-Hollands Archief…’

[Resultaten]
12 resultaten gevonden
[Resultaatkaart]
Titel of beschrijving
Datering: … | Plek: …
Bronhouder: … | Identifier: …
Ophaaldatum: …
Bronstatus: Beschikbaar / Tijdelijk niet beschikbaar
Metadatarechten: Bekend / Onbekend
Objectmediarechten: Niet vastgesteld — media niet lokaal getoond
Privacystatus: Geen extra beperking vastgesteld / Beperkt
[ Bekijk origineel record ]

[Pagination]
[Vorige] Pagina 1 van … [Volgende]

[Lege- of foutstatus]
Geen passende records gevonden. Probeer een bredere zoekterm.
[Opnieuw proberen]

### Interactiehypotheses
- Als historisch zoeken een zelfstandige ingang naast nieuws krijgt, begrijpen bezoekers beter dat resultaten uit externe archiefbronnen komen; toetsbaar via geautomatiseerde controle van route, koppen en bronlabels.
- Als elk resultaat bronhouder, stabiele identifier, ophaaldatum en externe link toont, kunnen agents met vaste fixtures controleren dat ieder resultaat herleidbaar is.
- Als metadatarechten en objectmediarechten afzonderlijk worden weergegeven, neemt het risico af dat gebruikers datasetrechten interpreteren als toestemming voor scans of foto’s; toetsbaar via UI- en contracttests op beide statussen.
- Als vrije tekst wordt gecombineerd met optionele filters voor plek, persoon, gebeurtenis en datum, accepteert de zoekroute zowel gewone vragen als gerichte verkenning; toetsbaar met een matrix van zoekparameters en verwachte query-transformatie.
- Als laad-, lege-, fout- en retry-statussen semantisch worden aangekondigd, blijft de route begrijpelijk zonder visuele beoordeling; toetsbaar met accessibility-automatisering en DOM-asserties.
- Als ontbrekende of tegenstrijdige rechten- en privacyinformatie fail-closed als ‘Onbekend’ of ‘Niet vastgesteld’ verschijnt, wordt geen onbewezen mediahergebruik gesuggereerd; toetsbaar met fixtures met ontbrekende en conflicterende bronvelden.

### Toegankelijkheid
- Alle bedieningselementen zijn via toetsenbord bereikbaar met zichtbare, contrastrijke focusindicator.
- Gebruik semantische koppen, labels, formuliergroeperingen en een logische tabvolgorde.
- Maak het statusgebied live voor schermlezers; kondig laden, aantal resultaten, lege resultaten en fouten aan zonder de focus onverwacht te verplaatsen.
- Gebruik betekenisvolle linkteksten zoals ‘Bekijk origineel record bij Open Archieven’ en waarschuw wanneer een link extern opent.
- Zorg voor voldoende kleurcontrast en geef statussen altijd ook tekstueel weer, niet alleen met kleur of pictogrammen.
- Maak foutmeldingen gekoppeld aan het relevante veld en bied een toetsenbordbedienbare retry-actie.
- Ondersteun zoom en smalle schermen zonder verlies van informatie of horizontale afhankelijkheid.

### Privacy
- Bewaar zoektermen standaard niet; verwerk ze tijdelijk voor de zoekaanvraag.
- Sla geen namen, geboortegegevens of andere persoonsgegevens lokaal op buiten de minimale metadata die noodzakelijk is voor het zoekresultaat.
- Toon alleen persoonsmetadata die door de externe bron publiek beschikbaar wordt gesteld en noodzakelijk is voor historische identificatie.
- Gebruik een duidelijke privacystatus per resultaat; bij ontbrekende of tegenstrijdige informatie wordt ‘Niet vastgesteld’ getoond en worden gevoelige details of media niet lokaal gepubliceerd.
- Vermeld bronhouder, externe recordlink en ophaaldatum zodat bezoekers de actuele privacycontext bij de bron kunnen controleren.
- Beperk logging tot technische diagnostiek, minimaliseer query-inhoud en anonimiseer of pseudonimiseer waar logging noodzakelijk is.
- Gebruik rate limiting, caching en een beschrijvende user-agent voor externe bronaanvragen zonder persoonsgegevens aan de publieke interface toe te voegen.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is een kleine, samenhangende en autonoom toetsbare uitbreiding. Er zijn geen materiële blokkades; de bestaande broncontractafhankelijkheid is expliciet en de scope beperkt veilig tot metadata en externe links.
- **WARNING · CONSISTENCY** — Er is inhoudelijke overlap met de eerder afgewezen kandidaat 59. Dit is geen exact reeds geleverd resultaat en vormt daarom geen blokkade; houd de actuele scope met geautomatiseerde fixtures en zonder live brondekking aan.
- **WARNING · SOURCE** — ‘Bron’ omvat Open Archieven en Noord-Hollands Archief, terwijl de kandidaat spreekt over één bestaand externe-broncontract. Leg in de contracttests vast hoe bronselectie en bronidentiteit worden onderscheiden.
- **INFO · RIGHTS** — De kandidaat behandelt metadata- en objectmediarechten afzonderlijk en kopieert geen media. De precieze bronstatusmapping kan later per recordtype worden uitgebreid zonder deze MVP te blokkeren.

## Geaccepteerde storykandidaten

### Publieke historische zoekroute met herleidbare bronmetadata

_Sleutel: `publieke-zoekroute-voor-bronmetadata`_

Voeg naast ‘Laatste nieuws’ een zelfstandige publieke zoekroute toe die zoekopdrachten voor vrije tekst, plek, persoon, gebeurtenis en datum naar het bestaande externe-broncontract stuurt. Toon uitsluitend minimale metadata en externe recordlinks, met afzonderlijke tekstuele statussen voor beschikbaarheid, rechten en privacy. Lokale media en ruwe externe persoonsgegevens worden niet getoond of opgeslagen.

**Acceptatiecriteria**
- De homepage bevat een zelfstandige, gelabelde ingang ‘Historisch zoeken’ die niet de admin-nieuwszoekfunctie gebruikt.
- Het zoekformulier ondersteunt vrije tekst en optionele filters voor plek, persoon, gebeurtenis, vanafdatum, einddatum en bron.
- Elk resultaat toont, wanneer beschikbaar, bronhouder, titel of beschrijving, datering, stabiele identifier, ophaaldatum en een externe recordlink.
- Elk resultaat toont afzonderlijke tekstuele statussen voor technische beschikbaarheid, metadatarechten, objectmediarechten en privacy; ontbrekende of tegenstrijdige waarden worden fail-closed als ‘Onbekend’ of ‘Niet vastgesteld’ weergegeven.
- De interface bevat geautomatiseerde laad-, succes-, lege-, fout- en retry-statussen; de status wordt semantisch aangekondigd en retry is toetsenbordbedienbaar.
- De route ondersteunt paginering zonder lokale kopieën van scans, foto’s, ruwe API-responses of zoektermen op te slaan.
- Geautomatiseerde contract- en UI-tests verifiëren dat nieuwsresultaten, record-intakegegevens en privacyclassificaties niet via deze route worden ontsloten.
- Een geautomatiseerde test verifieert dat elke getoonde externe link naar het bronrecord verwijst en duidelijk als externe link is gelabeld.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/main.dart), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/news/discover_section.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/news/discover_section.dart), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md), [https://www.openarchieven.nl/api/docs/](https://www.openarchieven.nl/api/docs/), [https://www.openarchieven.nl/datasets/nha](https://www.openarchieven.nl/datasets/nha), [https://opendata.archieven.nl/en/datasets-en/dataset-en?guid=F110BAA9B5B942C196FD551C346F0BBA](https://opendata.archieven.nl/en/datasets-en/dataset-en?guid=F110BAA9B5B942C196FD551C346F0BBA), [https://opendata.archieven.nl/nl/over-open-data](https://opendata.archieven.nl/nl/over-open-data)

Afhankelijkheden: story:61 (herkend als bestaande stories: 61)

Risico's: Externe bronvelden kunnen ontbreken of wijzigen; de UI moet onbekende statuswaarden veilig blijven tonen zonder beschikbaarheid of hergebruikrechten te suggereren., Rate limiting, caching of tijdelijke bronuitval kan zoekresultaten vertragen of leeg maken; fout- en beschikbaarheidsstatussen moeten dit expliciet onderscheiden., De beschikbare datasetlicentie bewijst niet automatisch rechten op objectmedia; de scope blijft daarom beperkt tot metadata en externe links.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
