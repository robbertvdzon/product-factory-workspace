---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0060
date: 2026-08-13
status: approved
sources:
  - https://github.com/robbertvdzon/hkh-autopilot
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend-admin/lib/main.dart
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl
  - https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/
  - https://www.europeana.eu/en/apis
  - https://europeana.atlassian.net/wiki/spaces/EF/pages/2385739812
  - https://www.openarchieven.nl/api/docs/
  - https://historypin.github.io/api-docs/items/map/index.html
---
# Productcyclus 60

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De huidige app is inmiddels een publieke historische zoekapp met contextuele resultaatdetails. De belangrijkste onbeantwoorde productvraag is hoe de app vanuit deze generieke zoekresultaten betrouwbare, lokaal relevante en betekenisvolle ontdekkingspaden voor Heemskerk kan bieden. De acceptatie-UI kon door een lokale Chromium-sandboxfout niet visueel worden gescreenshot; de publieke HTML en repositorycode zijn wel gecontroleerd.

### De publieke route ondersteunt zoeken én contextdetails

De repository beschrijft zoeken in Europeana en Open Archieven met vrije tekst, plaats, persoon, gebeurtenis en periode. Resultaatdetails tonen bronmetadata, stabiele bron-URI, ophaaldatum, rechten- en privacystatus, plus plaats, persoon, gebeurtenis en periode. Verwante resultaten worden beperkt tot maximaal drie en alleen gebaseerd op exact gedeelde zekere metadata uit de zichtbare resultaten.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart)

### De verbindingen zijn technisch betrouwbaar maar inhoudelijk smal

Relaties worden alleen gelegd via genormaliseerde exacte overeenkomsten op plaats, persoon of gebeurtenis. Periode-overlap is slechts aanvullende informatie en vormt op zichzelf geen relatie. Daardoor blijven historische naamvarianten, synoniemen, geografische schaalverschillen en inhoudelijke verbanden buiten beeld. De huidige implementatie voorkomt daarmee onbewezen relaties, maar levert waarschijnlijk weinig verbindingen op.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt)

### Bronbeschikbaarheid en dekking blijven zichtbaar maar beperken de ervaring

De backend onderscheidt RESULTS, NO_RESULTS, PARTIAL_AVAILABILITY en SOURCE_FAILURE en telt alleen beschikbare bronnen mee. Europeana vereist een API-key en kan daardoor server-side uitgeschakeld zijn; Open Archieven hanteert throttling. De app kan dus een correct maar onvolledig beeld geven, terwijl nog niet duidelijk wordt gemaakt welke lokale Heemskerkse collecties structureel ontbreken.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt), [https://www.europeana.eu/en/apis](https://www.europeana.eu/en/apis), [https://www.openarchieven.nl/api/docs/](https://www.openarchieven.nl/api/docs/)

### De beheeromgeving is gericht op nieuws en recordintake, niet op historische curatie

De admin-app gebruikt Google-authenticatie en bevat modules voor laatste nieuws en recordintake. In de geïnspecteerde hoofdcode is geen beheerfunctie zichtbaar voor het beoordelen, corrigeren, verrijken of verbinden van historische bronmetadata. Daardoor is er geen duidelijke menselijke route om lokale relevantie of meerstemmige context gecontroleerd toe te voegen.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend-admin/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend-admin/lib/main.dart), [https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/)

### De acceptatieomgeving was bereikbaar, maar visuele inspectie werd door tooling geblokkeerd

Beide acceptatie-URL’s gaven op 2026-08-13 HTTP 200 en leveren Flutter Web/CanvasKit-pagina’s. De vereiste Playwright-screenshot kon niet worden gemaakt omdat zowel de meegeleverde Chromium als de lokale Google Chrome door de macOS-sandbox vóór navigatie crashte. Hierdoor blijven visuele bruikbaarheid, layout en doorklikgedrag van de draaiende omgeving onbeoordeeld.

Bronnen: [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl), [https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/)

### Huidige applicatie

**Doel:** Een breed publiek helpen de geschiedenis van Heemskerk te onderzoeken via historische zoekvragen over tekst, plaats, persoon, gebeurtenis en periode. De app verbindt zoekresultaten uit externe erfgoedbronnen met herleidbare metadata en externe bronlinks; de beheeromgeving ondersteunt authenticatie, admin-nieuws en recordintake.

**Wat ontbreekt:**
- De huidige relaties zijn beperkt tot exacte metadata-overeenkomsten binnen één zichtbare zoekresultatenpagina.
- Lokale Heemskerkse dekking en de verhouding tussen lokale bronnen en Europeana/Open Archieven zijn nog niet duidelijk zichtbaar of structureel verrijkt.
- Er is geen zichtbare semantische laag voor naamvarianten, alternatieve plaatsnamen, entiteiten, thema’s of tegenstrijdige context.
- Er is geen zichtbare beheerworkflow voor historische metadata-curatie, bronbeoordeling of het gecontroleerd toevoegen van lokale context.
- De visuele bruikbaarheid en navigatie van de draaiende acceptatieomgeving zijn niet kunnen worden beoordeeld door de Chromium-startfout.

### Verbetermogelijkheden

- Maak bron- en lokaledekking expliciet: toon per zoekopdracht welke collecties zijn bevraagd, welke bronnen ontbreken en hoeveel resultaten uit Heemskerk of de regio komen.
- Onderzoek een gecontroleerde normalisatielaag voor plaatsnamen, persoonsvarianten en gebeurtenissen, met behoud van oorspronkelijke bronwaarden en zichtbare onzekerheid.
- Bied meerdere ontdekkingspaden naast exacte relaties, bijvoorbeeld zoeken op gedeelde plaats, periode of thema, maar label afgeleide verbanden duidelijk als suggestie in plaats van feit.
- Gebruik stabiele identifiers en bron-URI’s als verbindingsankers en laat de oorspronkelijke bron leidend blijven voor inhoud, rechten en privacy.
- Onderzoek een kleine curatiefunctie in het admin-gedeelte waarmee bevoegde beheerders lokale context of correcties kunnen beoordelen zonder externe bronpayloads of media lokaal te kopiëren.
- Maak gedeeltelijke bronbeschikbaarheid begrijpelijker voor bezoekers door bronstatus, dekking en onzekerheid direct naast resultaten te tonen.
- Voer na herstel van de browserinspectie een gerichte usability-beoordeling uit op zoekstart, resultaatdetail, verwante resultaten, externe bronlink en admin-login.

### Inspiratiebronnen

- [Europeana Explore](https://www.europeana.eu/en/explore) — Laat zien hoe een grote erfgoedcollectie naast zoeken ook thematische verkenning en curated discovery kan bieden.
- [Historypin](https://www.historypin.org/en/home/) — Relevante inspiratie voor lokale historische ontdekking via plaatsen, collecties en community-verhalen.
- [Historypin Map API](https://historypin.github.io/api-docs/items/map/index.html) — Toont een concreet patroon voor filteren en ontdekken van historische items op kaart en periode.
- [Europeana API Search Documentation](https://europeana.atlassian.net/wiki/spaces/EF/pages/2385739812) — Geeft bruikbare patronen voor zoekfilters, herbruikbaarheidsselectie, facetten en landing pages.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://github.com/robbertvdzon/hkh-autopilot) | 2026-08-13 | Geen LICENSE, LICENSE.md of COPYING-bestand gevonden in de publieke repository; rechten/licentie van repository-inhoud zijn daarom onbekend. | Broncode en repositorydocumentatie voor de actuele productfunctionaliteit. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md) | 2026-08-13 | Geen expliciete licentie-indicatie in het geraadpleegde README; onbekend. | Beschrijving van componenten, historische zoekroute, bronstatussen en configuratie. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart) | 2026-08-13 | Geen expliciete licentie-indicatie in het geraadpleegde bronbestand; onbekend. | Actuele publieke zoekvelden, resultaatvelden en bronstatusweergave. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart) | 2026-08-13 | Geen expliciete licentie-indicatie in het geraadpleegde bronbestand; onbekend. | Actuele implementatie van contextdetails en deterministische relaties. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt) | 2026-08-13 | Geen expliciete licentie-indicatie in het geraadpleegde bronbestand; onbekend. | Bronfoutafhandeling, paginering, bronstatussen en totaalberekening. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend-admin/lib/main.dart) | 2026-08-13 | Geen expliciete licentie-indicatie in het geraadpleegde bronbestand; onbekend. | Beheerfuncties en authenticatiestroom. |
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl) | 2026-08-13 | Acceptatieomgeving gebruikt representatieve dummydata; rechten/licentie van die data zijn onbekend. | Draaiende publieke acceptatieomgeving en Flutter Web-shell. |
| [bron](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/) | 2026-08-13 | Acceptatieomgeving gebruikt representatieve dummydata; rechten/licentie van die data zijn onbekend. | Draaiende beheer-acceptatieomgeving. |
| [bron](https://www.europeana.eu/en/apis) | 2026-08-13 | Europeana vermeldt dat API-gebruik een gratis API-key vereist; objectrechten volgen per item de rechtenverklaring. Metadata wordt volgens Europeana als CC0 aangeboden, maar gekoppelde objecten kunnen andere rechten hebben. | Actuele toegangs- en rechtenvoorwaarden voor een bestaande bronintegratie. |
| [bron](https://europeana.atlassian.net/wiki/spaces/EF/pages/2385739812) | 2026-08-13 | Europeana-documentatie; metadata wordt als CC0 beschreven, terwijl media/objecten hun eigen rights statement behouden. | Zoekvelden, filters op herbruikbaarheid, landing pages en stabiele recordlinks. |
| [bron](https://www.openarchieven.nl/api/docs/) | 2026-08-13 | De geraadpleegde API-documentatie vermeldt throttling en URI’s, maar geeft op deze pagina geen volledige algemene contentlicentie; rechtenstatus van recordinhoud blijft daarom per bron/item te controleren. | API-mogelijkheden, stabiele URI’s en operationele beperkingen van Open Archieven. |
| [bron](https://historypin.github.io/api-docs/items/map/index.html) | 2026-08-13 | API-documentatie geeft geen concrete algemene contentlicentie voor kaartitems; rechten van afzonderlijke bijdragen zijn onbekend. | Inspiratie voor kaartgebaseerd ontdekken op plaats en periode. |

## Productbeslissing

Maak de publieke historische zoekroute transparanter met een compacte bron- en dekkingssamenvatting per zoekopdracht. Toon welke collecties zijn bevraagd, hoeveel resultaten per bron beschikbaar zijn, welke bronnen tijdelijk ontbreken en hoeveel resultaten direct aan Heemskerk gekoppeld zijn. Behoud bestaande metadata, bron-URI’s en externe links; kopieer geen scans, foto’s of bronpayloads.

**Waarom:** De huidige zoekroute verbindt al Open Archieven en Europeana met herleidbare metadata, maar bezoekers zien onvoldoende wanneer resultaten onvolledig zijn of hoe lokaal de dekking is. Expliciete bronstatus en lokale relevantie versterken betrouwbaarheid, toegankelijkheid en nieuwsgierigheid zonder onbewezen historische relaties te introduceren. Deze richting is klein, toetsbaar en sluit direct aan op epic theme-hkh-autopilot-0002.

### Prioriteiten
- Definieer een eenduidig samenvattingsmodel per bron: bevraagd, beschikbaar, geen resultaten, gedeeltelijk beschikbaar of fout.
- Toon naast resultaten de bronverdeling en een herkenbare Heemskerk-indicatie op basis van bestaande zekere plaatsmetadata.
- Maak ontbrekende of gedeeltelijk beschikbare bronnen zichtbaar als onzekerheid, zonder de zoekopdracht automatisch als mislukt te behandelen.
- Verifieer dat elke bronvermelding verwijst naar de oorspronkelijke bron en dat rechten- en privacystatus behouden blijven.
- Voeg acceptatietests toe voor volledige beschikbaarheid, gedeeltelijke beschikbaarheid, bronfout en nulresultaten.

### Besluiten
- **Gebruik de bestaande bronstatussen en tel alleen daadwerkelijk beschikbare bronnen mee in de dekkingssamenvatting.** — De backend onderscheidt al RESULTS, NO_RESULTS, PARTIAL_AVAILABILITY en SOURCE_FAILURE en telt beschikbare bronnen afzonderlijk. Hergebruik voorkomt nieuwe semantiek en maakt operationele onzekerheid begrijpelijk voor bezoekers.
- **Bepaal lokale relevantie uitsluitend uit bestaande zekere plaatsmetadata en behoud de oorspronkelijke bronwaarde zichtbaar.** — De huidige relaties gebruiken genormaliseerde exacte metadata-overeenkomsten om onbewezen verbanden te voorkomen. Een eerste lokale indicator moet dezelfde terughoudendheid volgen en mag geen naamvarianten, geografische aannames of semantische relaties als feiten presenteren.
- **Toon per resultaat de bestaande bronmetadata, stabiele URI, ophaaldatum en rechten- en privacystatus naast de nieuwe dekkingstoelichting.** — Deze velden zijn al onderdeel van de contextdetails en maken de zoekroute controleerbaar en herleidbaar. De oorspronkelijke bron blijft leidend voor inhoud, rechten en privacy.
- **Beperk de eerste uitvoering tot Open Archieven en Europeana; voeg geen nieuwe collectie, kaartlaag of lokale media-import toe.** — Deze bronnen zijn al onderdeel van de publieke zoekroute. Europeana heeft een API-key nodig en Open Archieven kent throttling; de eerste verbetering moet daarom de bestaande beschikbaarheid begrijpelijk maken in plaats van de integratiescope vergroten.

## UX-voorstel: Transparante historische zoekopdracht met lokale dekking

**Gebruikersdoel:** Een bezoeker zoekt historische informatie over Heemskerk, begrijpt welke bronnen beschikbaar waren en beoordeelt snel hoe lokaal relevant de resultaten zijn.

### Flow
1. Bezoeker voert een vrije zoekterm in en kan optioneel plaats, persoon, gebeurtenis of periode invullen.
2. Bezoeker start de zoekopdracht.
3. De app toont een compacte samenvatting met per bron de status, het aantal resultaten en eventuele beperkingen.
4. De app toont hoeveel resultaten een expliciete Heemskerk-plaatsmetadata bevatten; deze indicatie wordt niet getoond als historisch bewijs.
5. Bezoeker filtert of scant resultaten en opent een resultaatdetail.
6. Resultaatdetail toont oorspronkelijke bronmetadata, stabiele bron-URI, ophaaldatum, rechtenstatus, privacystatus en de lokale relevantie-indicatie.
7. Bij gedeeltelijke beschikbaarheid of een bronfout toont de app een begrijpelijke waarschuwing met behoud van beschikbare resultaten.
8. Bezoeker volgt desgewenst de link naar de oorspronkelijke bron.

### Wireframe

[Pagina: Historisch zoeken]

Titel: Zoek in de geschiedenis van Heemskerk
[Zoekterm________________] [Plaats______________]
[Persoon_________________] [Gebeurtenis_________]
[Van periode____] [Tot periode____] [Zoeken]

[Samenvatting zoekopdracht]
2 bronnen bevraagd · 18 resultaten beschikbaar
Heemskerk in plaatsmetadata: 7 resultaten

Bronnen
- Open Archieven — Beschikbaar — 12 resultaten
- Europeana — Gedeeltelijk beschikbaar — 6 resultaten
  Sommige collectiegegevens konden niet worden opgehaald.

[Resultaten]
1. Titel van resultaat
   Bron: Open Archieven · Plaats: Heemskerk
   [Bekijk details]
2. Titel van resultaat
   Bron: Europeana · Plaats: onbekend
   [Bekijk details]

[Resultaatdetail]
Titel
Bron en oorspronkelijke metadata
Plaats: Heemskerk
Lokale indicatie: expliciete plaatsmetadata bevat Heemskerk
Ophaaldatum
Rechtenstatus · Privacystatus
[Open oorspronkelijke bron]
[Terug naar resultaten]

### Interactiehypotheses
- Als bezoekers per bron status en aantallen zien, kunnen zij beter inschatten hoe volledig een zoekresultaat is; toetsbaar met acceptatietests op correcte statuslabels en tellingen.
- Als expliciete Heemskerk-plaatsmetadata als afzonderlijke indicatie wordt getoond, herkennen bezoekers sneller lokaal relevante resultaten zonder dat onbewezen relaties worden gesuggereerd; toetsbaar met tests die alleen exacte zekere plaatsmetadata meetellen.
- Als gedeeltelijke beschikbaarheid direct naast de bronverdeling staat, interpreteren bezoekers beschikbare resultaten minder vaak als volledig; toetsbaar met scenario’s voor RESULTS, NO_RESULTS, PARTIAL_AVAILABILITY en SOURCE_FAILURE.
- Als elk resultaat een stabiele URI, bronmetadata, ophaaldatum, rechtenstatus en privacystatus toont, kunnen bezoekers de herkomst en gebruiksvoorwaarden controleren; toetsbaar met aanwezigheid-, link- en behoudtests.
- Als de eerste MVP uitsluitend bestaande bronnen en metadata gebruikt, blijft de implementatie beperkt en worden geen scans, foto’s of bronpayloads gekopieerd; toetsbaar met contracttests op payloadvelden en bronlinks.

### Toegankelijkheid
- Alle zoekvelden, filters, resultaatkaarten, waarschuwingen en links zijn volledig met toetsenbord bereikbaar en hebben zichtbare focus.
- Gebruik semantische koppen, labels en formulierrelaties; statusinformatie wordt niet uitsluitend via kleur of pictogram overgebracht.
- Maak bronstatussen beschikbaar als tekst en geef gedeeltelijke beschikbaarheid en fouten via een toegankelijk status- of alertgebied door aan schermlezers.
- Gebruik voldoende kleurcontrast voor tekst, knoppen, links en statusbadges; ondersteun vergroting en reflow zonder horizontaal scrollen.
- Geef resultaten en details een logische tabvolgorde en duidelijke linkteksten, bijvoorbeeld 'Open oorspronkelijke bron: Open Archieven'.
- Toets automatisch op semantiek, focus, toetsenbordbediening, contrast en foutmeldingen; voeg geautomatiseerde scenario’s toe voor alle bronstatussen.

### Privacy
- Sla alleen zoekcriteria en bronmetadata op als dat noodzakelijk is voor de zoekopdracht; bewaar geen persoonsgegevens of zoekgeschiedenis standaard.
- Behandel persoonsnamen in zoekvelden en bronresultaten als mogelijk persoonsgegevens; gebruik ze alleen voor het expliciete zoekdoel en beperk logging.
- Kopieer geen scans, foto’s of volledige externe bronpayloads; toon metadata en verwijs naar de oorspronkelijke bron-URI.
- Behoud per resultaat de bestaande rechten- en privacystatus en toon die vóór het openen van de externe bron.
- Maak in fout- en analysetelemetrie zoektermen en persoonsnamen onherkenbaar of laat ze weg.
- Documenteer doel, bewaartermijn en grondslag wanneer zoekgegevens toch tijdelijk worden opgeslagen; bied standaard geen account- of profielvereiste voor publiek zoeken.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is klein, toetsbaar en uitvoerbaar zonder handmatige eigenaaractie. Er zijn geen materiële blokkades voor veilige bouw of verificatie.
- **INFO · SOURCE** — De lokale telling blijft beperkt tot expliciete, genormaliseerde plaatsmetadata en kan daardoor onvolledig zijn; dit is correct als expliciete beperking vastgelegd.
- **INFO · RIGHTS** — De kandidaat behoudt bron-URI’s en bestaande rechten- en privacystatussen en introduceert geen lokale kopie van scans, foto’s of volledige payloads.

## Geaccepteerde storykandidaten

### Transparante bron- en Heemskerk-dekkingssamenvatting bij historische zoekresultaten

_Sleutel: `bron-en-lokaledekking-samenvatting`_

Als bezoeker wil ik per historische zoekopdracht zien welke bestaande bronnen zijn bevraagd, hoeveel resultaten per bron beschikbaar zijn, welke bronnen gedeeltelijk of niet beschikbaar zijn en hoeveel resultaten expliciete plaatsmetadata ‘Heemskerk’ bevatten, zodat ik de volledigheid en lokale relevantie van de resultaten kan inschatten zonder onbewezen historische verbanden te krijgen.

**Acceptatiecriteria**
- De publieke historische zoekroute toont een compacte samenvatting met per bestaande bron (Open Archieven en Europeana) de status en het aantal beschikbare resultaten.
- De samenvatting onderscheidt ten minste beschikbare resultaten, nul resultaten, gedeeltelijke beschikbaarheid en bronfout, in overeenstemming met de bestaande bronstatussen.
- Bij gedeeltelijke beschikbaarheid of een bronfout blijven beschikbare resultaten zichtbaar en wordt een begrijpelijke tekstuele waarschuwing getoond; de zoekopdracht wordt niet automatisch als mislukt weergegeven.
- Het aantal lokaal relevante resultaten telt uitsluitend resultaten waarvan de bestaande zekere plaatsmetadata na normalisatie exact ‘Heemskerk’ oplevert; ontbrekende of andere plaatsmetadata wordt niet als lokaal resultaat geteld.
- De oorspronkelijke plaatswaarde blijft zichtbaar bij elk resultaat en de lokale telling wordt expliciet als indicatie op basis van plaatsmetadata gelabeld, niet als historisch bewijs.
- Bestaande bronmetadata, stabiele bron-URI, ophaaldatum, rechtenstatus en privacystatus blijven per resultaat behouden en worden niet vervangen door de samenvatting.
- Geautomatiseerde tests verifiëren de tellingen en statusweergave voor volledige beschikbaarheid, nulresultaten, gedeeltelijke beschikbaarheid, bronfout en volledige bronuitval.
- Contract- of integratietests bevestigen dat geen scans, foto’s of volledige externe bronpayloads worden opgeslagen of weergegeven en dat bronlinks naar de oorspronkelijke URI blijven verwijzen.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md), [https://www.europeana.eu/en/apis](https://www.europeana.eu/en/apis), [https://www.openarchieven.nl/api/docs/](https://www.openarchieven.nl/api/docs/)

Afhankelijkheden: story:62, story:63 (herkend als bestaande stories: 62, 63)

Risico's: Europeana kan zonder server-side API-key niet beschikbaar zijn; de samenvatting moet dit als bronstatus tonen en mag geen niet-bestaande resultaten meetellen., Open Archieven kan door throttling tijdelijk gedeeltelijke resultaten opleveren; status- en tellingstests moeten dit deterministisch afdekken., Exacte plaatsmetadata geeft mogelijk beperkte lokale dekking en mist naamvarianten of geografische synoniemen; deze story claimt daarom uitsluitend expliciete Heemskerk-metadata., Rechten- en privacy-informatie uit externe bronnen kan ontbreken of tegenstrijdig zijn; bestaande fail-closed statusweergave mag niet worden versoepeld.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
