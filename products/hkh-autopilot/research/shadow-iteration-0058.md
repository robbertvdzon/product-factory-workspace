---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0058
date: 2026-08-12
status: approved
sources:
  - https://github.com/robbertvdzon/hkh-autopilot
  - https://github.com/robbertvdzon/hkh-autopilot/blob/main/README.md
  - https://github.com/robbertvdzon/hkh-autopilot/blob/main/docs/factory/functional-spec.md
  - https://github.com/robbertvdzon/hkh-autopilot/blob/main/frontend/lib/historical/historical_search.dart
  - https://github.com/robbertvdzon/hkh-autopilot/blob/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl/api/version
  - https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/api/version
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl/api/historical-search?q=Heemskerk&limit=3
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl
  - https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/
  - https://www.openarchieven.nl/api/docs/
  - https://www.openarchieven.nl/api/docs/records/search.php
---
# Productcyclus 58

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De belangrijkste onbeantwoorde productvraag is hoe Historisch Heemskerk betrouwbaar bruikbaar blijft wanneer één of meer externe bronnen niet beschikbaar zijn. De live zoekroute retourneert momenteel bij bronuitval HTTP 200 met 49.555 als totaal en nul resultaten; Europeana is uitgeschakeld en Open Archieven tijdelijk niet beschikbaar. Daardoor is niet duidelijk of er geen historische resultaten zijn of dat de bronnen falen.

### Live historische zoekroute faalt semantisch bij bronuitval

De acceptatie-API retourneerde voor een Heemskerk-query geen resultaten, maar wel total 49555. Europeana had status DISABLED en Open Archieven TEMPORARILY_UNAVAILABLE. Dit maakt de gebruikersuitkomst verwarrend en feitelijk onbruikbaar.

Bronnen: [https://hkh-autopilot-acceptance.vdzonsoftware.nl/api/historical-search?q=Heemskerk&limit=3](https://hkh-autopilot-acceptance.vdzonsoftware.nl/api/historical-search?q=Heemskerk&limit=3), [https://github.com/robbertvdzon/hkh-autopilot/blob/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt](https://github.com/robbertvdzon/hkh-autopilot/blob/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt)

### De applicatie heeft al een publieke bronzoekroute

De homepage bevat een zelfstandige ingang Historisch zoeken met vrije tekst, plek, persoon, gebeurtenis, jaartallen en bronkeuze voor Europeana en Open Archieven. Resultaten bevatten bronidentifier, stabiele URL en ophaaldatum.

Bronnen: [https://github.com/robbertvdzon/hkh-autopilot/blob/main/frontend/lib/main.dart](https://github.com/robbertvdzon/hkh-autopilot/blob/main/frontend/lib/main.dart), [https://github.com/robbertvdzon/hkh-autopilot/blob/main/frontend/lib/historical/historical_search.dart](https://github.com/robbertvdzon/hkh-autopilot/blob/main/frontend/lib/historical/historical_search.dart), [https://github.com/robbertvdzon/hkh-autopilot/blob/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/api/HistoricalSearchController.kt](https://github.com/robbertvdzon/hkh-autopilot/blob/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/api/HistoricalSearchController.kt)

### Rechten en privacy worden fail-closed behandeld

Wanneer metadatarechten of privacy niet expliciet veilig zijn, worden inhoudsvelden weggelaten. De bronlink en statusvelden blijven behouden. Dit beperkt risico’s, maar maakt het des te belangrijker dat onbekend, beperkt, uitgeschakeld en tijdelijk niet beschikbaar begrijpelijk worden onderscheiden.

Bronnen: [https://github.com/robbertvdzon/hkh-autopilot/blob/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchContract.kt](https://github.com/robbertvdzon/hkh-autopilot/blob/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchContract.kt), [https://github.com/robbertvdzon/hkh-autopilot/blob/main/frontend/lib/historical/historical_search.dart](https://github.com/robbertvdzon/hkh-autopilot/blob/main/frontend/lib/historical/historical_search.dart)

### De bronintegraties hebben expliciete operationele beperkingen

Open Archieven documenteert throttling tot vier verzoeken per seconde per IP, een beschrijvende user-agent en server-side caching. De implementatie gebruikt rate limiting, maar de live route toont geen bruikbare fallback wanneer de bron niet antwoordt. Europeana vereist een wskey; de applicatie schakelt de bron uit wanneer die ontbreekt.

Bronnen: [https://www.openarchieven.nl/api/docs/](https://www.openarchieven.nl/api/docs/), [https://github.com/robbertvdzon/hkh-autopilot/blob/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchAdapters.kt](https://github.com/robbertvdzon/hkh-autopilot/blob/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchAdapters.kt), [https://europeana.atlassian.net/wiki/spaces/EF/pages/2385739812](https://europeana.atlassian.net/wiki/spaces/EF/pages/2385739812)

### De huidige frontend maakt gedeeltelijke beschikbaarheid tot een volledige fout

De frontend behandelt iedere TEMPORARILY_UNAVAILABLE- of INVALID_RESPONSE-bronstatus als volledige zoekfout, ook wanneer een andere bron mogelijk resultaten kan leveren. Hierdoor worden partial-success en bron-specifieke waarschuwingen niet als afzonderlijke gebruikersuitkomsten gepresenteerd.

Bronnen: [https://github.com/robbertvdzon/hkh-autopilot/blob/main/frontend/lib/historical/historical_search.dart](https://github.com/robbertvdzon/hkh-autopilot/blob/main/frontend/lib/historical/historical_search.dart), [https://github.com/robbertvdzon/hkh-autopilot/blob/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt](https://github.com/robbertvdzon/hkh-autopilot/blob/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt)

### Admin biedt nog geen brongezondheidsbeeld

Het beheergedeelte ondersteunt authenticatie, admin-nieuws en lokale recordintake. In de gecontroleerde code is geen admin-overzicht gevonden voor bronconfiguratie, laatste succesvolle broncheck, foutduur of operationele bronstatus.

Bronnen: [https://github.com/robbertvdzon/hkh-autopilot/blob/main/frontend-admin/lib/main.dart](https://github.com/robbertvdzon/hkh-autopilot/blob/main/frontend-admin/lib/main.dart), [https://github.com/robbertvdzon/hkh-autopilot/blob/main/docs/factory/functional-spec.md](https://github.com/robbertvdzon/hkh-autopilot/blob/main/docs/factory/functional-spec.md)

### Visuele acceptatie-inspectie kon niet worden afgerond

De vereiste Playwright-screenshotcontrole is geprobeerd voor beide canvas-apps. Zowel de meegeleverde Chromium als systeem-Chrome beëindigden vóór paginalaad met macOS Mach-port/permissiefouten. De API, repositorycode en live deployment konden wel worden gecontroleerd; layout, tekstafbreking en daadwerkelijke canvasinteractie blijven onbeoordeeld.

Bronnen: [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl), [https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/)

### Huidige applicatie

**Doel:** Historisch Heemskerk is bedoeld voor een brede doelgroep: iedereen die vanuit nieuwsgierigheid iets wil onderzoeken over een gebouw, straat, persoon, gebeurtenis of ander onderwerp uit de geschiedenis van Heemskerk. De app verbindt lokale context met externe historische bronnen en moet ontdekkingen betrouwbaar, toegankelijk, herleidbaar en herbruikbaar maken.

**Wat ontbreekt:**
- Bronuitval wordt voor bezoekers onvoldoende onderscheiden van nul zoekresultaten.
- Een groot totaal wordt teruggegeven terwijl de actuele resultatenlijst leeg is door bronproblemen.
- Gedeeltelijke resultaten uit beschikbare bronnen worden niet afzonderlijk van falende bronnen gepresenteerd.
- Europeana is in acceptatie uitgeschakeld door ontbrekende wskey-configuratie.
- Er is geen zichtbare operationele bronstatus of brongezondheidsinformatie in het admin-gedeelte.
- De visuele bruikbaarheid van beide canvas-apps kon door de lokale Chromium-permissionfout niet worden vastgesteld.
- De admin-nieuwsfunctie en recordintake zijn aanwezig, maar vormen geen publieke historische publicatie- of verbindingsworkflow.

### Verbetermogelijkheden

- Scheid expliciet de uitkomsten geen resultaten, bron tijdelijk niet beschikbaar, bron niet geconfigureerd en gedeeltelijk resultaat.
- Toon beschikbare resultaten samen met een compacte bronwaarschuwing voor falende bronnen, in plaats van de volledige zoekactie als fout te behandelen.
- Bereken en presenteer totalen alleen voor daadwerkelijk beschikbare resultaten, of label provider-totalen ondubbelzinnig als niet volledig beschikbaar.
- Maak bronkeuze en bronstatus begrijpelijk voor niet-specialisten met korte uitleg naast technische statuslabels.
- Onderzoek een privacy- en rechtenveilige metadata-cache met expliciete ophaaldatum en cacheleeftijd, zonder zoektermen, ruwe payloads, persoonsgegevens of media op te slaan.
- Voeg in admin een brongezondheidsweergave toe met configuratiestatus, laatste succesvolle check en foutcategorie, zonder credentials of persoonsgegevens.
- Gebruik geaggregeerde, privacy-minimale operationele metingen om terugkerende bronuitval en gebruikersimpact te onderscheiden.
- Verifieer de canvas-UI opnieuw in een browseromgeving waarin screenshots en toetsenbordinteractie uitvoerbaar zijn.

### Inspiratiebronnen

- [Europeana Search API en Collections](https://europeana.atlassian.net/wiki/spaces/EF/pages/2385739812) — Europeana combineert vrije zoeking met filters, provider-/instellingscontext en rights statements. Dat inspireert een begrijpelijkere bron- en rechtenfiltering, zonder mediarechten automatisch over te nemen.
- [Open Archieven API en Open Archives](https://www.openarchieven.nl/api/docs/) — Open Archieven biedt stabiele URI’s, zoek- en recorddetailroutes, paginering, caching en meerdere machineleesbare formaten. Dit ondersteunt herleidbare externe links en expliciete operationele bronstatussen.
- [W3C WAI role=status-richtlijn](https://www.w3.org/WAI/WCAG21/Techniques/aria/ARIA22) — W3C beschrijft dat dynamische zoekstatussen, zoals het aantal gevonden resultaten, via een status/live-regio aan ondersteunende technologie moeten worden meegedeeld. Dit is relevant voor het onderscheiden van nul resultaten, gedeeltelijke resultaten en bronfouten.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://github.com/robbertvdzon/hkh-autopilot) | 2026-08-12 | GitHub rapporteert voor deze publieke repository geen licentie; hergebruikrechten van de code zijn daardoor onbekend. | Primaire bron voor repositorystructuur, actuele implementatie en documentatie. |
| [bron](https://github.com/robbertvdzon/hkh-autopilot/blob/main/README.md) | 2026-08-12 | Publieke repository zonder vastgestelde licentie. | Beschrijving van componenten en actuele productfunctionaliteit. |
| [bron](https://github.com/robbertvdzon/hkh-autopilot/blob/main/docs/factory/functional-spec.md) | 2026-08-12 | Publieke documentatie; specifieke documentlicentie is onbekend. | Functionele scope, privacyregels, broncontracten en admin-afbakening. |
| [bron](https://github.com/robbertvdzon/hkh-autopilot/blob/main/frontend/lib/historical/historical_search.dart) | 2026-08-12 | Code valt onder de repositorylicentie; die is niet vastgesteld. | Publieke zoek-UI, foutafhandeling, statusweergave en bronvelden. |
| [bron](https://github.com/robbertvdzon/hkh-autopilot/blob/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt) | 2026-08-12 | Code valt onder de repositorylicentie; die is niet vastgesteld. | Bronselectie, paginering, mergegedrag en statusafhandeling. |
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl/api/version) | 2026-08-12 | Publieke technische response; specifieke licentie is onbekend. | Vaststelling van de draaiende publieke versie. |
| [bron](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/api/version) | 2026-08-12 | Publieke technische response; specifieke licentie is onbekend. | Vaststelling van de draaiende adminversie. |
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl/api/historical-search?q=Heemskerk&limit=3) | 2026-08-12 | Acceptatie-response met gemockte/representatieve data; rechten op brondata zijn niet afzonderlijk vastgesteld. | Directe observatie van de actuele zoekuitkomst en bronstatussen. |
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl) | 2026-08-12 | Acceptatieomgeving met dummydata en mockkoppelingen; rechtenstatus onbekend. | Publieke canvas-omgeving die visueel gecontroleerd moest worden; browserinspectie werd lokaal geblokkeerd. |
| [bron](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/) | 2026-08-12 | Acceptatieomgeving met dummydata en mockkoppelingen; rechtenstatus onbekend. | Admin-canvasomgeving die visueel gecontroleerd moest worden; browserinspectie werd lokaal geblokkeerd. |
| [bron](https://www.openarchieven.nl/api/docs/) | 2026-08-12 | Publieke Open Archieven-documentatie; licentie van de webpagina niet afzonderlijk vastgesteld. Recordrechten kunnen per bron verschillen. | API-limieten, caching, URI’s, zoekmogelijkheden en toegangsmodellen. |
| [bron](https://www.openarchieven.nl/api/docs/records/search.php) | 2026-08-12 | Publieke API-documentatie; licentie van de webpagina onbekend. | Concrete zoekparameters en pagineringsbeperkingen van Open Archieven. |

## Productbeslissing

Maak de publieke historische zoekroute bronveerkrachtig: toon beschikbare resultaten ook wanneer een andere bron tijdelijk niet beschikbaar, ongeldig of niet geconfigureerd is, en maak het onderscheid tussen nul resultaten en bronuitval expliciet. Bereken totalen uitsluitend over beschikbare resultaten en toon per bron een korte begrijpelijke status met ophaaldatum en oorspronkelijke bronlink.

**Waarom:** Dit is een kleine, samenhangende verbetering binnen epic theme-hkh-autopilot-0002. De huidige route geeft bij bronuitval een misleidend totaal met nul resultaten en behandelt gedeeltelijke beschikbaarheid als volledige fout. De richting versterkt betrouwbaarheid, toegankelijkheid en herleidbaarheid zonder scans, foto’s, ruwe payloads of gevoelige persoonsgegevens lokaal op te slaan. Zij vereist geen menselijke uitvoering behalve eventueel een reeds noodzakelijk extern access token voor een toekomstige bronconfiguratie; ontbrekende configuratie blokkeert de zoekroute niet.

### Prioriteiten
- Definieer eenduidige gebruikersuitkomsten: resultaten, nul resultaten, gedeeltelijk resultaat, tijdelijk niet beschikbaar, niet geconfigureerd en ongeldige bronrespons.
- Pas backend-merge- en totaalgedrag aan zodat alleen beschikbare resultaten meetellen en bronstatussen afzonderlijk behouden blijven.
- Pas de publieke zoekinterface aan met bron-specifieke, begrijpelijke waarschuwingen en een toegankelijke dynamische statusmelding.
- Behoud per resultaat bronidentifier, stabiele externe URL en ophaaldatum; kopieer geen media en sla geen zoektermen of gevoelige bronpayloads op.
- Voeg toetsbare acceptatiegevallen toe voor alle bronnen beschikbaar, één bron uitgevallen, alle bronnen uitgevallen en nul resultaten zonder bronfout.

### Besluiten
- **Behandel bronuitval als een bron-specifieke waarschuwing en niet automatisch als een volledige zoekfout.** — Gedeeltelijke resultaten blijven bruikbaar en gebruikers kunnen zien welke bron niet beschikbaar is.
- **Rapporteer totalen alleen voor daadwerkelijk beschikbare resultaten; toon geen provider-totaal als volledig zoekresultaattotaal wanneer de resultatenlijst door bronproblemen incompleet is.** — Een totaal van 49.555 bij nul teruggegeven resultaten is semantisch misleidend en ondermijnt vertrouwen.
- **Gebruik korte mensgerichte statuslabels naast eventuele technische statuswaarden en maak zoekstatussen toegankelijk via een dynamische statusmelding.** — Bezoekers hoeven technische bronkennis niet te hebben; statuswijzigingen moeten ook voor ondersteunende technologie begrijpelijk zijn.
- **Behoud fail-closed rechten- en privacygedrag: bij onzekerheid worden inhoudsvelden weggelaten, terwijl bronlink en statusinformatie behouden blijven.** — De betrouwbaarheid van de zoekroute mag niet worden verbeterd door onnodig privacy- of auteursrechtrisico te introduceren.

## UX-voorstel: Bronveerkrachtig historisch zoeken

**Gebruikersdoel:** Een bezoeker wil betrouwbare historische informatie over Heemskerk vinden en kunnen onderscheiden of er geen resultaten zijn of dat een bron tijdelijk niet beschikbaar is.

### Flow
1. 1. Bezoeker opent Historisch zoeken.
2. 2. Bezoeker vult een zoekterm in en kiest optioneel plek, persoon, gebeurtenis, jaartallen en bronnen.
3. 3. Bezoeker activeert Zoeken.
4. 4. De interface meldt via een toegankelijke statusregio dat de zoekopdracht wordt uitgevoerd.
5. 5. Beschikbare resultaten worden getoond met bronnaam, stabiele bronlink en ophaaldatum.
6. 6. Per niet-beschikbare bron verschijnt een korte waarschuwing met mensgericht label, zoals Tijdelijk niet beschikbaar of Niet geconfigureerd.
7. 7. Het totaal toont uitsluitend beschikbare resultaten en vermeldt bij gedeeltelijke beschikbaarheid dat de uitkomst mogelijk onvolledig is.
8. 8. Bij nul resultaten zonder bronfout verschijnt Geen resultaten gevonden; bij volledige bronuitval verschijnt Geen resultaten kunnen worden opgehaald door bronproblemen.
9. 9. De bezoeker kan filters aanpassen en opnieuw zoeken of een resultaat openen via de externe bronlink.

### Wireframe

[Pagina: Historisch zoeken]

H1 Historisch zoeken
Korte uitleg: Zoek in historische bronnen over Heemskerk.

[Zoekterm ______________________________]
[Plaats __________] [Persoon __________]
[Gebeurtenis _____] [Vanaf ____] [Tot ____]

Bronnen
[x] Open Archieven — Beschikbaar
[ ] Europeana — Niet geconfigureerd

[Zoeken]

<section role="status" aria-live="polite">
  3 resultaten gevonden uit 1 beschikbare bron.
  Europeana is niet geconfigureerd; de uitkomst kan onvolledig zijn.
</section>

[Waarschuwing]
Europeana is momenteel niet beschikbaar. Je kunt wel zoeken in Open Archieven.

H2 Resultaten (3)

Resultaatkaart
- Titel of beschikbare metadata
- Bron: Open Archieven
- Ophaaldatum: 12 augustus 2026
- [Open bronrecord]

[Geen resultaten / bronuitval-toestand]
Geen resultaten kunnen worden opgehaald omdat de geselecteerde bronnen tijdelijk niet beschikbaar zijn.
[Opnieuw proberen]

Toetsenbordvolgorde: zoekvelden → bronkeuzes → Zoeken → statusmelding → waarschuwingen → resultaten → externe links.

### Interactiehypotheses
- H1: Als bronstatussen in mensentaal per bron worden getoond, kunnen gebruikers nul resultaten onderscheiden van bronuitval; toetsbaar met geautomatiseerde UI-asserties op de labels en statusmelding.
- H2: Als gedeeltelijke resultaten zichtbaar blijven wanneer één bron faalt, blijft de zoektaak bruikbaar; toetsbaar met een scenario waarin één adapter succes en één adapter TEMPORARILY_UNAVAILABLE retourneert.
- H3: Als totalen alleen beschikbare resultaten tellen, bevat de response geen misleidend provider-totaal; toetsbaar met contracttests voor beschikbare, gedeeltelijke en volledig mislukte bronnen.
- H4: Als dynamische zoekstatussen via een status/live-regio worden aangekondigd, zijn resultaatcount en bronwaarschuwingen programmatisch beschikbaar; toetsbaar met accessibility- en DOM-asserties.
- H5: Als resultaten altijd bronidentifier, stabiele URL en ophaaldatum behouden, is herleidbaarheid controleerbaar zonder lokale bronkopie; toetsbaar met API-contracttests.
- H6: Als rechten-onzekere inhoudsvelden leeg blijven terwijl status en bronlink zichtbaar zijn, blijft fail-closed privacy- en rechtenbeleid intact; toetsbaar met responses waarin metadatarechten onbekend zijn.

### Toegankelijkheid
- Gebruik echte formuliervelden, labels en fieldsets voor zoekfilters en bronkeuzes.
- Maak alle bediening volledig toetsenbordbedienbaar met zichtbare focus en logische tabvolgorde.
- Gebruik voldoende kleurcontrast en communiceer bronstatussen niet uitsluitend met kleur of pictogrammen.
- Gebruik een aria-live/statusregio voor laden, resultaatcount, gedeeltelijke beschikbaarheid en bronfouten.
- Geef fout- en waarschuwingsmeldingen nabij de relevante bronkeuze en in begrijpelijke taal.
- Gebruik semantische koppen, lijsten of kaarten met consistente structuur en duidelijke linkteksten.
- Zorg dat externe links expliciet aangeven dat ze naar een bronrecord buiten de applicatie leiden.
- Ondersteun zoom en reflow zonder verlies van filters, statusinformatie of resultaatdetails.

### Privacy
- Sla zoektermen, vrije tekst en filterwaarden niet op; gebruik ze uitsluitend voor de actieve zoekopdracht.
- Sla geen ruwe bronpayloads, scans, foto’s of volledige historische records lokaal op.
- Bewaar alleen noodzakelijke metadata: bronidentifier, stabiele externe URL, status en ophaaldatum, met een duidelijk doel.
- Toon geen inhoudsvelden wanneer privacy- of rechtenstatus onbekend of niet veilig is.
- Log operationele bronstatus geaggregeerd en zonder zoekterm, IP-adres of andere persoonsgegevens, tenzij een afzonderlijk doel en grondslag dit noodzakelijk maken.
- Bewaar geen externe credentials of wskeys in de publieke frontend en toon ze nooit in foutmeldingen.
- Documenteer bewaartermijn, toegangsbeperking en verwijdering voor eventuele technische statusmetingen.
- Gebruik externe bronlinks zonder persoonsgegevens aan de URL toe te voegen.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is klein, toetsbaar en uitvoerbaar zonder handmatige eigenaaractie. Er zijn geen blokkerende problemen; de bronveerkrachtige statussemantiek sluit direct aan op de productrichting en behoudt privacy- en rechtenbeperkingen.
- **WARNING · SOURCE** — Eén bronverwijzing lijkt een inconsistent pad te bevatten: `/backend/src/kotlin/.../HistoricalSearchContract.kt` wijkt af van het gebruikelijke `/backend/src/main/kotlin/...`-pad. Corrigeer of verifieer deze verwijzing voor reproduceerbaarheid.

## Geaccepteerde storykandidaten

### Bronveerkrachtige historische zoekuitkomsten bij gedeeltelijke bronbeschikbaarheid

_Sleutel: `bronuitval-semantiek-en-gedeeltelijke-resultaten`_

Verbeter de bestaande publieke historische zoekroute zodat bronuitval, nul resultaten, gedeeltelijke resultaten, niet-geconfigureerde bronnen en ongeldige bronresponses afzonderlijk en mensgericht worden weergegeven. Beschikbare resultaten blijven zichtbaar; totalen tellen uitsluitend beschikbare resultaten mee en behouden per resultaat de bestaande herleidbare bronmetadata. Bij volledige bronuitval verschijnt een expliciete bronprobleemtoestand zonder misleidend provider-totaal. Rechten- en privacyvelden blijven fail-closed.

**Acceptatiecriteria**
- Wanneer alle geselecteerde bronnen beschikbaar zijn, retourneert en toont de zoekroute de beschikbare resultaten met een totaal dat uitsluitend op die resultaten is gebaseerd.
- Wanneer één geselecteerde bron tijdelijk niet beschikbaar, niet geconfigureerd of ongeldig is en een andere bron resultaten levert, blijven de beschikbare resultaten zichtbaar en wordt per falende bron een korte, begrijpelijke status getoond.
- Wanneer geen bronfout optreedt en geen resultaten bestaan, toont de publieke route expliciet dat geen resultaten zijn gevonden; deze toestand is onderscheiden van volledige bronuitval.
- Wanneer alle geselecteerde bronnen falen of niet beschikbaar zijn, toont de route geen provider-totaal als volledig zoekresultaattotaal en presenteert zij een expliciete bronprobleemtoestand met opnieuw proberen als geautomatiseerd beschikbare actie.
- De backend bewaart per bron de afzonderlijke technische beschikbaarheidsstatus en merge’t resultaten zonder een falende bron als succesvolle bron te behandelen.
- De API- en frontendcontracttests dekken minimaal: alle bronnen beschikbaar, één bron tijdelijk niet beschikbaar met gedeeltelijke resultaten, nul resultaten zonder bronfout en volledige bronuitval.
- De publieke interface communiceert laden, resultaatcount, gedeeltelijke beschikbaarheid en bronfouten via een programmatisch uitleesbare status/live-regio; statusinformatie wordt niet uitsluitend met kleur of pictogrammen weergegeven.
- Elk getoond resultaat behoudt bronidentifier, stabiele externe bron-URL en ophaaldatum; scans, foto’s, zoektermen, ruwe bronpayloads en gevoelige persoonsgegevens worden niet lokaal opgeslagen of naar de frontend doorgegeven wanneer rechten- of privacystatus onzeker is.

Bronnen: [https://hkh-autopilot-acceptance.vdzonsoftware.nl/api/historical-search?q=Heemskerk&limit=3](https://hkh-autopilot-acceptance.vdzonsoftware.nl/api/historical-search?q=Heemskerk&limit=3), [https://github.com/robbertvdzon/hkh-autopilot/blob/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt](https://github.com/robbertvdzon/hkh-autopilot/blob/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt), [https://github.com/robbertvdzon/hkh-autopilot/blob/main/backend/src/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchContract.kt](https://github.com/robbertvdzon/hkh-autopilot/blob/main/backend/src/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchContract.kt), [https://github.com/robbertvdzon/hkh-autopilot/blob/main/frontend/lib/historical/historical_search.dart](https://github.com/robbertvdzon/hkh-autopilot/blob/main/frontend/lib/historical/historical_search.dart), [https://www.w3.org/WAI/WCAG21/Techniques/aria/ARIA22](https://www.w3.org/WAI/WCAG21/Techniques/aria/ARIA22)

Afhankelijkheden: story:62, story:61 (herkend als bestaande stories: 62, 61)

Risico's: De actuele adapters of acceptatieomgeving kunnen bronstatussen anders modelleren dan de onderzochte responses; contracttests moeten de statusmapping expliciet vastleggen., Een ontbrekende Europeana-wskey kan gedeeltelijke beschikbaarheid blijven veroorzaken; de zoekroute moet dit als niet geconfigureerd tonen zonder de overige bronnen te blokkeren., Provider-totalen kunnen bij gedeeltelijke beschikbaarheid niet volledig vergelijkbaar zijn; alleen daadwerkelijk samengevoegde beschikbare resultaten mogen als gebruikers-totaal worden gepresenteerd.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
