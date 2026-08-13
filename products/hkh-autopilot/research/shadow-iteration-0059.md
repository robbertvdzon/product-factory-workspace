---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0059
date: 2026-08-13
status: approved
sources:
  - https://github.com/robbertvdzon/hkh-autopilot
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchAdapters.kt
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend-admin/lib/main.dart
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend-admin/lib/recordintake/admin_record_intake.dart
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl
  - https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl/api/historical-search?q=Heemskerk&limit=3
  - https://www.openarchieven.nl/api/docs/
  - https://www.openarchieven.nl/api/docs/records/search.php
---
# Productcyclus 59

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De belangrijkste onbeantwoorde productvraag is hoe bezoekers vanuit een plek, persoon of gebeurtenis daadwerkelijk kunnen doorontdekken naar samenhangende historische bronnen. De huidige app biedt een publieke zoekroute met vrije tekst-, plek-, persoon-, gebeurtenis- en datumvelden en zoekt in Europeana en Open Archieven, maar toont vooral afzonderlijke zoekresultaten met externe links. Een expliciete contextlaag met verbonden personen, plaatsen, perioden, kaarten of vervolgvraag ontbreekt nog. De bronveerkrachtvraag uit iteratie 58 is niet opnieuw onderzocht.

### De huidige publieke app is een zoekingang, geen verbonden historische kenniswereld

De repository beschrijft een publieke Flutter-app met de ingang ‘Historisch zoeken’. De zoekroute ondersteunt vrije tekst, plek, persoon, gebeurtenis en jaartallen en gebruikt Europeana en Open Archieven. De respons bewaart bronidentifier, stabiele bronlink, ophaaldatum en rechten-/privacystatussen. Er is geen zichtbare productfunctie die resultaten inhoudelijk aan elkaar koppelt of een vervolgpad via context aanbiedt.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/api/HistoricalSearchController.kt](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/api/HistoricalSearchController.kt)

### De huidige zoekroute ondersteunt bronstatussen, maar de waarde van resultaten blijft bronafhankelijk

De backend onderscheidt RESULTS, NO_RESULTS, PARTIAL_AVAILABILITY en SOURCE_FAILURE en telt alleen beschikbare bronnen mee. Dit adresseert de eerder onderzochte semantiek van bronuitval. De gebruiker krijgt daarmee statusinformatie, maar nog geen rijkere uitleg over waarom twee resultaten bij elkaar horen of welke volgende ontdekking logisch is.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart)

### De huidige bronnen zijn geschikt voor gefaseerde verbindingen, maar hebben verschillende beperkingen

Open Archieven biedt zoeken naar personen en records, filtering op plaats, bron en gebeurtenis, stabiele URI’s, content negotiation en downloads in onder meer CSV, XML en RDF. De API hanteert throttling van vier verzoeken per seconde per IP en vraagt een beschrijvende user-agent. Europeana vereist in de huidige implementatie een server-side wskey; zonder configuratie wordt die bron uitgeschakeld. Daardoor is een uniforme contextweergave over bronnen niet vanzelfsprekend en moet bronherkomst per item zichtbaar blijven.

Bronnen: [https://www.openarchieven.nl/api/docs/](https://www.openarchieven.nl/api/docs/), [https://www.openarchieven.nl/api/docs/records/search.php](https://www.openarchieven.nl/api/docs/records/search.php), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchAdapters.kt](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchAdapters.kt)

### De beheeromgeving is primair ingericht voor authenticatie, nieuws en recordintake

De beheerapp bevat Google-login of preview-authenticatie, beheer van laatste nieuws en een record-intakeflow met rechten-, privacy-, overlijdens- en externe-archiefvelden. In de geraadpleegde beheerbroncode is geen algemeen brongezondheids- of ontdekkingsdashboard zichtbaar. Dat beperkt de mogelijkheid om beheerders inzicht te geven in welke lokale en externe verbindingen voor bezoekers beschikbaar zijn.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend-admin/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend-admin/lib/main.dart), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend-admin/lib/recordintake/admin_record_intake.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend-admin/lib/recordintake/admin_record_intake.dart)

### De acceptatieomgevingen waren technisch bereikbaar, maar visuele inspectie kon niet worden afgerond

Beide acceptatie-URL’s gaven op 2026-08-13 HTTP 200 via Bash. De vereiste Playwright-screenshotprocedure kon in deze uitvoeromgeving niet starten: de aanwezige Chromium/Chrome-processen beëindigden met een macOS Mach-port/permission-fout. Daardoor kon de canvas-gerenderde publieke en beheer-UI niet betrouwbaar visueel worden beoordeeld. De live historische API-aanvraag liep in deze controle tegen een timeout aan; dat is onvoldoende bewijs voor een inhoudelijke productstatus.

Bronnen: [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl), [https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/), [https://hkh-autopilot-acceptance.vdzonsoftware.nl/api/historical-search?q=Heemskerk&limit=3](https://hkh-autopilot-acceptance.vdzonsoftware.nl/api/historical-search?q=Heemskerk&limit=3)

### Bestaande historische applicaties laten zien dat tijd en plaats krachtige ontdekkingsingangen zijn

Amsterdam Time Machine ontsluit historische informatie locatie- en tijdgebonden via een kaartindex over meerdere databronnen. Topotijdreis laat gebruikers historische kaarten over ongeveer tweehonderd jaar vergelijken. Paleo-maps gebruikt een tijdschuif en kaart om landschapsverandering beleefbaar te maken. Deze voorbeelden ondersteunen een contextuele vervolgnavigatie rond plaats en periode, zonder dat daaruit een productbesluit volgt.

Bronnen: [https://www.amsterdamtimemachine.nl/nl/](https://www.amsterdamtimemachine.nl/nl/), [https://www.amsterdamtimemachine.nl/nl/data/](https://www.amsterdamtimemachine.nl/nl/data/), [https://www.cultureelerfgoed.nl/onderwerpen/b/bronnen-en-kaarten/overzicht/topotijdreis](https://www.cultureelerfgoed.nl/onderwerpen/b/bronnen-en-kaarten/overzicht/topotijdreis), [https://www.deltares.nl/en/expertise/projects/time-traveling-in-the-netherlands-paleo-maps](https://www.deltares.nl/en/expertise/projects/time-traveling-in-the-netherlands-paleo-maps)

### Huidige applicatie

**Doel:** De applicatie maakt de geschiedenis van Heemskerk toegankelijk voor een brede doelgroep: iedereen die iets wil weten over een gebouw, straat, persoon, gebeurtenis of onderwerp. De publieke route verbindt zoekvragen met externe historische bronnen en toont herleidbare metadata en externe bronlinks, met terughoudende privacy- en rechtenverwerking.

**Wat ontbreekt:**
- De actuele publieke en beheer-UI kon door een browser-startfout niet visueel worden beoordeeld; dit blijft een verificatiegat.
- Zoekresultaten worden nog niet zichtbaar gepresenteerd als verbonden context rond personen, plaatsen, gebeurtenissen en perioden.
- Er is geen duidelijke vervolgnavigatie van één resultaat naar verwante bronnen, tijdlijn, kaart, betrokken personen of gerelateerde gebeurtenissen.
- De publieke route bevat nog geen zichtbare lokale HKH-collectie als gelijkwaardige bron naast Europeana en Open Archieven.
- Europeana is afhankelijk van server-side configuratie van een wskey en kan daardoor voor bezoekers uitgeschakeld zijn.
- De beheeromgeving bevat geen zichtbaar bronoverzicht dat dekking, configuratie, actualiteit en uitval per bron begrijpelijk maakt.
- De live API was tijdens deze controle niet betrouwbaar reproduceerbaar door een timeout; actuele acceptatie-inhoud en bronstatus zijn daarom niet volledig vastgesteld.

### Verbetermogelijkheden

- Maak van ieder zoekresultaat een contextuele detailweergave met bron, datering, plaats, betrokken persoon/gebeurtenis, onzekerheid en expliciete links naar verwante resultaten. Dit sluit aan op de missie om verbanden te laten ontdekken en op de bestaande bronmetadata.
- Voeg een laagdrempelige ontdekmodus toe naast formulierzoeken: start vanaf een plek, persoon of gebeurtenis en bied kaart-, tijdlijn- en gerelateerde-resultaatnavigatie. Amsterdam Time Machine, Topotijdreis en Paleo-maps tonen dat plaats plus tijd begrijpelijke publieke ingangen zijn.
- Gebruik stabiele bron-URI’s en bronidentifiers als verbindingsankers, maar toon per verbinding de bronherkomst en retrievaldatum. Open Archieven ondersteunt URI’s en meerdere exportformaten; dat maakt herleidbare koppelingen mogelijk zonder bronpayloads lokaal te kopiëren.
- Onderzoek een kleine, geautoriseerde lokale HKH-bronintegratie die alleen metadata en externe links ontsluit. De huidige externe zoekroute voldoet nog niet aan het lokale deel van de productmissie.
- Maak bronstatus in de beheeromgeving operationeel inzichtelijk: geconfigureerd, bereikbaar, laatste succesvolle ophaling, rechtenstatus en dekking. Dit helpt beheerders de publieke betrouwbaarheid te verklaren zonder historische inhoud als nieuws te vermengen.
- Ontwerp een toegankelijke vervolgvraagstructuur met eenvoudige taal, duidelijke bronlabels en programmatisch leesbare statusinformatie. Dit vermindert de afstand tussen een gewone bezoekersvraag en historisch onderzoek.
- Houd privacy en rechten fail-closed: sla geen ruwe bronpayloads, scans, foto’s, zoektermen of onnodige persoonsgegevens lokaal op; behandel onbekende rechten en privacystatus als onzeker en laat de oorspronkelijke bron beslissend blijven.

### Inspiratiebronnen

- [Amsterdam Time Machine](https://www.amsterdamtimemachine.nl/nl/) — Locatiegebonden toegang tot meerdere historische databronnen en een kaart als voordeur voor brede ontdekking.
- [Amsterdam Time Machine Data](https://www.amsterdamtimemachine.nl/nl/data/) — Laat zien hoe uniforme URI’s en linked-open-data-relaties verschillende datasets samenhangend kunnen maken.
- [Topotijdreis](https://www.cultureelerfgoed.nl/onderwerpen/b/bronnen-en-kaarten/overzicht/topotijdreis) — Toegankelijke tijd- en kaartvergelijking die veranderingen van een plek door de jaren heen zichtbaar maakt.
- [Paleo-maps](https://www.deltares.nl/en/expertise/projects/time-traveling-in-the-netherlands-paleo-maps) — Beleefbare tijdschuif en kaartnavigatie voor een breed publiek.
- [OldMapsOnline mobiele app](https://www.oldmapsonline.org/nl/app) — Combineert zoeken op locatie, historische kaarten, tijdlijn, kaartvergelijking en GPS-geleide ontdekking.
- [History Lives Here](https://pilot.historyliveshere.nl/) — Voorbeeld van lokale geschiedenis die op basis van de huidige locatie straat- en gebouwgewijs wordt ontdekt; relevant als inspiratie voor plekgerichte vervolgnavigatie.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://github.com/robbertvdzon/hkh-autopilot) | 2026-08-13 | Publieke GitHub-repository. In de geraadpleegde repository is geen LICENSE-bestand aangetroffen; licentie voor de code is daarom onbekend. | Primaire publieke repository voor productstructuur, documentatie en broncode. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md) | 2026-08-13 | Onderdeel van een publieke GitHub-repository; geen expliciete licentie aangetroffen. | Beschrijft componenten, doelgroep van de publieke route en gebruikte historische bronnen. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart) | 2026-08-13 | Publieke broncode; expliciete licentie onbekend. | Toont zoekvelden, bronkeuze, bronmetadata en gebruikersstatussen. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt) | 2026-08-13 | Publieke broncode; expliciete licentie onbekend. | Toont mergegedrag, bronstatussen en totalen. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchAdapters.kt) | 2026-08-13 | Publieke broncode; expliciete licentie onbekend. | Toont de operationele beperkingen en fail-closed metadata-/privacyverwerking van Europeana en Open Archieven. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend-admin/lib/main.dart) | 2026-08-13 | Publieke broncode; expliciete licentie onbekend. | Toont de beheerfuncties en authenticatie-opzet. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend-admin/lib/recordintake/admin_record_intake.dart) | 2026-08-13 | Publieke broncode; expliciete licentie onbekend. | Toont recordintake, externe archiefpreview en privacyvelden. |
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl) | 2026-08-13 | Publieke acceptatieomgeving met representatieve dummydata; rechten/licentie van de getoonde applicatie-inhoud zijn niet vastgesteld. | Vereiste live bron voor de publieke gebruikerservaring; HTTP 200 vastgesteld, canvas-screenshot niet uitvoerbaar door browseromgeving. |
| [bron](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/) | 2026-08-13 | Publieke acceptatieomgeving met representatieve dummydata; rechten/licentie van de getoonde applicatie-inhoud zijn niet vastgesteld. | Vereiste live bron voor de beheerervaring; HTTP 200 vastgesteld, canvas-screenshot niet uitvoerbaar door browseromgeving. |
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl/api/historical-search?q=Heemskerk&limit=3) | 2026-08-13 | Publieke acceptatie-API met mock-/dummydata; rechten/licentie van response-inhoud onbekend. | Vereiste live controle van de historische zoekroute; aanvraag liep tijdens deze controle tegen een timeout aan. |
| [bron](https://www.openarchieven.nl/api/docs/) | 2026-08-13 | Publieke API-documentatie; concrete hergebruiklicentie voor de documentatie niet vastgesteld. | Primaire documentatie voor API-mogelijkheden, throttling, URI’s en export-/harvestopties. |
| [bron](https://www.openarchieven.nl/api/docs/records/search.php) | 2026-08-13 | Publieke API-documentatie; concrete hergebruiklicentie voor de documentatie niet vastgesteld. | Primaire specificatie van zoeken op naam, plaats, gebeurtenis en bron. |

## Productbeslissing

Bouw een contextuele detailweergave voor één historisch zoekresultaat. Toon naast de bestaande bronmetadata een compacte set herleidbare contextvelden — plaats, periode, persoon of gebeurtenis wanneer beschikbaar — en bied maximaal drie vervolglinks naar verwante resultaten uit dezelfde zoekopdracht. Iedere relatie vermeldt de bron en stabiele bronlink; er worden geen scans, foto’s of ruwe bronpayloads lokaal gekopieerd.

**Waarom:** Deze kleine, samenhangende uitbreiding verandert de bestaande publieke zoekroute stap voor stap van losse resultaten naar een verbonden historische ontdekkingservaring. Zij sluit direct aan op de missie en de principes Verbonden, Betrouwbaar, Meerstemmig, Toegankelijk, Nieuwsgierig, Open en Herbruikbaar. De huidige route beschikt al over zoekvelden, bronidentifier, stabiele bronlink, ophaaldatum en bronstatussen, maar mist context en vervolgnavigatie. Open Archieven ondersteunt stabiele URI’s en zoeken op persoon, plaats, gebeurtenis en bron. Daarom kan de eerste versie worden gebouwd zonder nieuwe bronintegratie, lokale mediaopslag of onvermijdelijke menselijke uitvoering. Onbekende rechten-, privacy- of contextgegevens blijven zichtbaar als onzeker en blokkeren de relatie.

### Prioriteiten
- Maak één resultaatdetailweergave beschikbaar vanuit de publieke historische zoekroute.
- Gebruik uitsluitend reeds beschikbare metadata en expliciete bronlinks uit Europeana en Open Archieven.
- Toon bronherkomst, stabiele identifier of URI, ophaaldatum en onzekerheidsstatus per resultaat en per vervolglink.
- Bied eenvoudige vervolgnavigatie op gedeelde plaats, persoon, gebeurtenis of periode; toon maximaal drie suggesties.
- Behoud bestaande bronstatussen en laat bronuitval of gedeeltelijke beschikbaarheid begrijpelijk zien zonder resultaten als volledig te presenteren.

### Besluiten
- **Start met contextuele vervolgnavigatie binnen de bestaande zoekresultaten en voeg nog geen kaart, tijdlijn of nieuwe lokale HKH-bron toe.** — Dit is de kleinste toetsbare stap naar een verbonden kenniswereld en gebruikt bestaande gegevens. Kaart- en tijdlijnfuncties zijn waardevolle vervolgstappen, maar vergroten de scope en vereisen waarschijnlijk aanvullende normalisatie en bronkoppeling.
- **Gebruik stabiele bron-URI’s en bronmetadata als verbindingsankers en toon de oorspronkelijke bron als beslissende plek voor inhoud, rechten en privacy.** — Open Archieven documenteert stabiele URI’s, zoekfilters en export-/harvestmogelijkheden. De bestaande implementatie bewaart al bronidentifier, bronlink, ophaaldatum en rechten-/privacystatussen. Dit ondersteunt herleidbaarheid zonder bronpayloads of beschermde media lokaal te kopiëren.
- **Laat relaties alleen zien wanneer een gedeeld contextkenmerk aantoonbaar uit bronmetadata volgt; label ontbrekende of onzekere kenmerken expliciet.** — Een betrouwbare historische kenniswereld mag geen verbanden suggereren die niet uit de bronnen blijken. Deze keuze ondersteunt meerstemmigheid en voorkomt dat bronafhankelijke, onvolledige resultaten als zekere historische feiten worden gepresenteerd.

## UX-voorstel: Contextuele detailweergave voor historische zoekresultaten

**Gebruikersdoel:** Een bezoeker ontdekt vanuit één historisch zoekresultaat betrouwbare, samenhangende bronnen via plaats, periode, persoon of gebeurtenis.

### Flow
1. Bezoeker opent de publieke route ‘Historisch zoeken’.
2. Bezoeker voert een zoekvraag in en start de zoekopdracht.
3. De app toont resultaten met bronlabel, bronstatus, datering en stabiele bronlink.
4. Bezoeker opent één resultaat via een duidelijk benoemde knop ‘Bekijk context’.
5. De detailweergave toont beschikbare contextvelden: plaats, periode, persoon en gebeurtenis.
6. De app toont maximaal drie verwante resultaten wanneer een gedeeld contextkenmerk aantoonbaar is.
7. Elke relatie vermeldt het gedeelde kenmerk, de bron, identifier of URI en ophaaldatum.
8. Bezoeker opent een verwant resultaat of de oorspronkelijke bron in een nieuw tabblad.
9. Bij ontbrekende of onzekere metadata toont de app dit expliciet en biedt zij geen onbewezen relatie aan.
10. Bij gedeeltelijke bronbeschikbaarheid of bronuitval blijft de status zichtbaar en blijft de bezoeker in de huidige route.

### Wireframe

[Pagina: Historisch zoeken]

Titel: Historisch zoeken
Zoekvelden: Vrije tekst | Plaats | Persoon | Gebeurtenis | Vanaf jaar | Tot jaar
[Zoeken]

Resultaatkaart
- Titel
- Korte beschrijving
- Plaats: Heemskerk
- Periode: 1920–1930
- Bron: Open Archieven
- Bronstatus: Beschikbaar / Gedeeltelijk beschikbaar / Bron niet beschikbaar
- Ophaaldatum: datum
[Bekijk context] [Open oorspronkelijke bron]

[Pagina: Context van resultaat]
Terug naar zoekresultaten
Titel van resultaat
Bron: Open Archieven
Identifier/URI: stabiele link
Ophaaldatum: datum
Rechten/privacy: Bekend / Onbekend / Beperkt

Context
- Plaats: waarde of ‘Niet beschikbaar’
- Periode: waarde of ‘Niet beschikbaar’
- Persoon: waarde of ‘Niet beschikbaar’
- Gebeurtenis: waarde of ‘Niet beschikbaar’

Verwante resultaten
‘Gedeelde plaats: Heemskerk’
- Resultaattitel
- Bronlabel en stabiele bronlink
- Ophaaldatum
[Open resultaat]

‘Gedeelde periode: 1920–1930’
- Resultaattitel
- Bronlabel en stabiele bronlink
- Ophaaldatum
[Open resultaat]

Statusmelding: ‘Niet alle bronnen waren beschikbaar. Deze context is gebaseerd op de getoonde bronnen.’
[Open oorspronkelijke bron]

### Interactiehypotheses
- H1: Bezoekers openen vaker een resultaatdetail wanneer de actieknop expliciet ‘Bekijk context’ heet dan wanneer alleen een generieke resultaatlink beschikbaar is. Toets: geautomatiseerde interactietest meet dat de knop zichtbaar, bereikbaar en gekoppeld aan het juiste detailresultaat is.
- H2: Een detailweergave met maximaal drie gelabelde vervolgsuggesties verhoogt het aantal vervolgnavigaties per zoekopdracht zonder de eerste bronopening te verminderen. Toets: eventmetingen vergelijken detailopeningen, suggestie-openingen en bronopeningen met de bestaande route.
- H3: Bronlabel, stabiele URI en ophaaldatum vergroten de begrijpelijkheid van relaties. Toets: UI-tests controleren dat elk resultaat en elke relatie deze metadata toont wanneer beschikbaar.
- H4: Alleen relaties op basis van aantoonbaar gedeelde metadata verminderen misleidende context. Toets: contracttests controleren dat relaties ontbreken wanneer plaats, persoon, gebeurtenis of periode niet exact of aantoonbaar gedeeld is.
- H5: Expliciete bronstatussen voorkomen dat gedeeltelijke resultaten als volledig worden geïnterpreteerd. Toets: scenario-tests controleren de meldingen RESULTS, NO_RESULTS, PARTIAL_AVAILABILITY en SOURCE_FAILURE.
- H6: Een toetsenbord- en schermlezer-vriendelijke detailroute behoudt toegang tot contextuele ontdekking. Toets: geautomatiseerde accessibility-tests controleren focusvolgorde, semantische namen, kopstructuur, linkdoelen en contrast.

### Toegankelijkheid
- Alle interactieve elementen zijn met toetsenbord bereikbaar en hebben een zichtbare focusindicator.
- De focusvolgorde volgt de visuele en inhoudelijke leesvolgorde.
- Knoppen en links hebben unieke, beschrijvende namen, zoals ‘Bekijk context van [titel]’.
- Resultaatkaarten gebruiken semantische koppen en structurele HTML-/Flutter-semantiek.
- Bronstatussen en onzekerheidsmeldingen worden programmatisch aangekondigd en niet alleen met kleur weergegeven.
- Tekst en interactieve elementen voldoen aan minimaal WCAG AA-contrast.
- Ontbrekende waarden worden expliciet als ‘Niet beschikbaar’ weergegeven.
- Nieuwe detailpagina’s ondersteunen terugnavigatie zonder verlies van zoekresultaten of focuscontext.

### Privacy
- Sla geen vrije zoektermen, IP-adressen, scans, foto’s of ruwe bronpayloads lokaal op tenzij daarvoor een afzonderlijk, duidelijk doel en passende grondslag bestaat.
- Gebruik uitsluitend reeds beschikbare metadata, bronidentifier, stabiele bronlink, ophaaldatum en bronstatus.
- Toon persoonsgegevens alleen wanneer zij door de oorspronkelijke bron publiek en functioneel relevant zijn voor de context.
- Neem geen nieuwe persoonsgegevens op in analytics; meet alleen geanonimiseerde gebeurtenistypen zoals detail geopend of vervolglink gekozen.
- Behandel onbekende privacy- en rechtenstatussen als onzeker en toon de oorspronkelijke bron als beslissende plek voor toegang en voorwaarden.
- Genereer geen relatie wanneer de bronmetadata onvoldoende bewijs levert; voorkom inferenties over personen of gebeurtenissen.
- Gebruik externe bronlinks zonder broninhoud lokaal te kopiëren en maak duidelijk dat de bezoeker de oorspronkelijke bron verlaat.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is klein, toetsbaar en uitvoerbaar zonder handmatige eigenaaractie. Er zijn geen materiële blokkades; bronrechten blijven een aandachtspunt maar verhinderen deze metadata- en linkgebaseerde uitbreiding niet.
- **WARNING · RIGHTS** — De aangehaalde repository en sommige documentatiebronnen hebben geen vastgestelde expliciete licentie. De kandidaat kopieert echter geen bronpayloads of media en verwijst naar de oorspronkelijke bronnen.
- **INFO · SOURCE** — De contextvelden en relaties zijn afhankelijk van onvolledige of niet-uniforme metadata van bestaande bronnen; dit kan leiden tot weinig verwante resultaten, maar is als risico benoemd en niet blokkerend.

## Geaccepteerde storykandidaten

### Contextuele detailweergave voor historische zoekresultaten

_Sleutel: `contextuele-historische-resultaatdetailweergave`_

Als bezoeker wil ik vanuit één historisch zoekresultaat beschikbare context over plaats, periode, persoon en gebeurtenis kunnen bekijken en maximaal drie aantoonbaar verwante resultaten kunnen openen, zodat ik betrouwbare historische verbanden kan ontdekken zonder dat scans, foto’s of ruwe bronpayloads lokaal worden gekopieerd.

**Acceptatiecriteria**
- De publieke historische zoekroute biedt per resultaat een duidelijk benoemde actie om de contextuele detailweergave te openen.
- De detailweergave toont, wanneer beschikbaar, titel, plaats, periode, persoon, gebeurtenis, bronlabel, stabiele bronidentifier of URI, ophaaldatum en rechten-/privacystatus.
- Ontbrekende of onzekere contextmetadata wordt expliciet als niet beschikbaar of onzeker weergegeven en leidt niet tot een relatie.
- De detailweergave toont maximaal drie verwante resultaten en vermeldt per relatie het aantoonbaar gedeelde contextkenmerk, de bron en de stabiele bronlink.
- Relaties worden uitsluitend gegenereerd op basis van aantoonbaar gedeelde metadata uit de bestaande zoekresultaten; er worden geen onbewezen persoons- of gebeurtenisverbanden afgeleid.
- Elke externe bronlink verwijst naar de oorspronkelijke bron en er worden geen scans, foto’s of ruwe externe bronpayloads lokaal opgeslagen.
- De bestaande bronstatussen RESULTS, NO_RESULTS, PARTIAL_AVAILABILITY en SOURCE_FAILURE blijven zichtbaar en worden in de detailweergave begrijpelijk toegelicht.
- Bij gedeeltelijke bronbeschikbaarheid worden uitsluitend beschikbare resultaten en hun herleidbare metadata gebruikt; provider-totalen worden niet als volledig gepresenteerd wanneer bronnen ontbreken of uitvallen.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchAdapters.kt](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchAdapters.kt), [https://www.openarchieven.nl/api/docs/](https://www.openarchieven.nl/api/docs/), [https://www.openarchieven.nl/api/docs/records/search.php](https://www.openarchieven.nl/api/docs/records/search.php)

Afhankelijkheden: story:62, story:63, story:61 (herkend als bestaande stories: 62, 63, 61)

Risico's: Bronnen leveren contextvelden niet uniform of volledig, waardoor weinig of geen verwante resultaten beschikbaar zijn., Exacte metadata-overeenkomst kan historische naam-, plaats- of periodevarianten missen en daardoor de ontdekkingswaarde beperken., Onbekende rechten- of privacystatussen kunnen veel relaties uitsluiten; dit blijft noodzakelijk voor fail-closed publicatie., Open Archieven hanteert throttling en Europeana kan zonder server-side wskey uitgeschakeld zijn, waardoor context gedeeltelijk beschikbaar kan zijn.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
