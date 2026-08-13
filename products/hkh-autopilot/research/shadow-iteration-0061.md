---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0061
date: 2026-08-13
status: approved
sources:
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl
  - https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/
  - https://www.europeana.eu/en/apis
  - https://www.openarchieven.nl/api/docs/
  - https://www.delpher.nl/over-delpher/handleiding/zoeken-in-delpher/hoe-zoek-je-het-best/zoeken-naar-verschillende-versies-van-een-woord
  - https://www.nationaalarchief.nl/onderzoeken/collectie
---
# Productcyclus 61

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De belangrijkste onbeantwoorde productvraag is hoe HKH bezoekers vanuit betrouwbare zoekresultaten verder laat ontdekken en verbanden laat begrijpen, terwijl iedere relatie herleidbaar en onzekerheid zichtbaar blijft. De huidige app ondersteunt zoeken in Europeana en Open Archieven, maar biedt nog vooral exacte metadatarelaties binnen één resultatenpagina. De acceptatie-UI kon visueel niet worden beoordeeld door een lokale Chromium-startfout.

### Huidige publieke applicatie

De publieke app ondersteunt historische zoeking op tekst, plaats, persoon, gebeurtenis en periode via Europeana en Open Archieven. Zoekopdrachten en externe bronpayloads worden niet lokaal opgeslagen.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt)

### Huidige bron- en contextweergave

Resultaatdetails behouden bronidentifier, stabiele URI, ophaaldatum, rechten- en privacystatus en tonen plaats, persoon, gebeurtenis en periode. Relaties zijn beperkt tot maximaal drie zichtbare resultaten met exact genormaliseerde overeenkomsten in zekere metadata.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart)

### Acceptatieomgeving

De publieke en admin-URL’s leveren Flutter Web Canvas-apps met respectievelijk de titels ‘Historisch Heemskerk’ en ‘HKH Beheer’. Screenshotverificatie via Playwright mislukte door een lokale macOS Chromium-sandbox/Bootstrap-permission-fout; inhoudelijke visuele observaties zijn daarom niet betrouwbaar vastgesteld.

Bronnen: [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl), [https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/)

### Belangrijkste functionele gat

De app ondersteunt zoeken en bronherleiding, maar geen aantoonbare collectie-overstijgende vervolgpaden via naamvarianten, gecontroleerde entiteiten, bredere geografische niveaus, thema’s of tijdlijnen. Daardoor blijft de missie van verbonden en nieuwsgierig ontdekken gedeeltelijk gerealiseerd.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md)

### Onvoldoende uitleg van lokale dekking

Bronstatussen onderscheiden beschikbare, lege, gedeeltelijk beschikbare en uitgevallen bronnen. Er is echter geen aantoonbare uitleg van lokale Heemskerk-dekking, representativiteit of structureel ontbrekende collecties.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md)

### Aanvullende bronkansen

Delpher biedt collectie-overstijgende full-text zoeking in historische kranten, boeken en tijdschriften. Het Nationaal Archief biedt zoeking in archieven, foto’s, indexen, kaarten en bibliotheekcollecties en vermeldt hergebruik van openbare informatie. Deze bronnen kunnen de huidige combinatie van Europeana en Open Archieven inhoudelijk aanvullen.

Bronnen: [https://www.delpher.nl/over-delpher/handleiding/zoeken-in-delpher/hoe-zoek-je-het-best/zoeken-naar-verschillende-versies-van-een-woord](https://www.delpher.nl/over-delpher/handleiding/zoeken-in-delpher/hoe-zoek-je-het-best/zoeken-naar-verschillende-versies-van-een-woord), [https://www.nationaalarchief.nl/onderzoeken/collectie](https://www.nationaalarchief.nl/onderzoeken/collectie)

### Adminfunctie

De repository bevat adminmodules voor nieuws, recordintake, externe verificatie en privacyclassificatie. Een beheeroverzicht voor bronconnectorstatus, lokale dekking of curatoriële ontdekkingspaden is niet aantoonbaar aanwezig.

Bronnen: [https://github.com/robbertvdzon/hkh-autopilot](https://github.com/robbertvdzon/hkh-autopilot), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md)

### Huidige applicatie

**Doel:** Een brede doelgroep helpen de geschiedenis van Heemskerk te onderzoeken via gewone vragen, plaatsen, personen, gebeurtenissen en perioden, gekoppeld aan historische bronnen buiten Heemskerk. De app toont herleidbare metadata en externe bronlinks; de adminapp ondersteunt nieuws, recordintake, bronverificatie en privacyclassificatie.

**Wat ontbreekt:**
- Visuele bruikbaarheid en duidelijkheid van beide Canvas-rendered acceptatie-UI’s konden niet betrouwbaar worden vastgesteld door de lokale browserstartfout.
- Relaties zijn beperkt tot exacte metadata-overlap binnen één zichtbare zoekresultatenpagina.
- Naamvarianten, entiteitsidentifiers, geografische schaalverschillen, thema’s, tijdlijnen en kaartgebaseerde verkenning zijn niet aantoonbaar beschikbaar.
- Lokale Heemskerk-dekking en de betekenis van ontbrekende of niet-beschikbare collecties worden niet concreet uitgelegd.
- De adminapp toont volgens de repositorystructuur geen overzicht van brondekking, connectorgezondheid of curatoriële ontdekkingspaden.

### Verbetermogelijkheden

- Maak per zoekopdracht bronverdeling, lokale Heemskerk-indicatie, beschikbaarheidsstatus en ontbrekende collecties begrijpelijk zichtbaar.
- Maak zekere plaats-, persoons- en gebeurtenisvelden klikbare vervolgzoekingen, met behoud van de oorspronkelijke bronwaarde en een expliciet onderscheid tussen zoekingang en bewezen relatie.
- Gebruik stabiele bron- of entiteitsidentifiers voor naamvarianten en synoniemen wanneer de externe bron die zelf levert; label afgeleide matches als onzeker.
- Voeg een tijdlijn- of kaartweergave toe op basis van voldoende precieze bronvelden, met zichtbare onzekerheid voor geschatte datums of plaatsen.
- Onderzoek aanvullende directe bronnen zoals Delpher en Nationaal Archief voor kranten, kaarten, foto’s en archiefbeschrijvingen; beperk veilige eerste koppelingen tot metadata en externe links wanneer rechten of privacy niet expliciet zijn.
- Voeg in admin een overzicht toe van bronstatus, lokale dekking, rechten/privacy-onzekerheid en structurele bronlacunes.
- Voer echte browseracceptatietests uit voor Canvas-rendering, toetsenbordnavigatie, screenreaderlabels en de begrijpelijkheid van bron- en onzekerheidsmeldingen.

### Inspiratiebronnen

- [Delpher](https://www.delpher.nl/over-delpher/handleiding/zoeken-in-delpher/hoe-zoek-je-het-best/zoeken-naar-verschillende-versies-van-een-woord) — Laat zien hoe één zoekingang meerdere historische collectie-typen en full-text vervolgverkenning kan ontsluiten.
- [Nationaal Archief collectiezoeking](https://www.nationaalarchief.nl/onderzoeken/collectie) — Combineert zoeking in archieven, foto’s, indexen, kaarten en bibliotheekcollecties en maakt open-hergebruikcontext zichtbaar.
- [Europeana API](https://www.europeana.eu/en/apis) — Bestaande gebruikte bron voor collectie-overstijgende erfgoedmetadata en stabiele bronverwijzingen.
- [Open Archieven API](https://www.openarchieven.nl/api/docs/) — Bestaande gebruikte bron voor herleidbare genealogische records en URI-gebaseerde vervolgverkenning.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md) | 2026-08-13 | Publieke repositorydocumentatie; expliciete repositorylicentie niet vastgesteld. | Vaststellen van applicatiedoel, componenten, zoekroute en opslaggrenzen. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt) | 2026-08-13 | Publieke broncode; expliciete licentie van dit bestand niet vastgesteld. | Verifiëren van bronstatussen, foutafhandeling en resultaataggregatie. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart) | 2026-08-13 | Publieke broncode; expliciete licentie van dit bestand niet vastgesteld. | Verifiëren van zoekvelden, metadata en bronstatusmodel. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart) | 2026-08-13 | Publieke broncode; expliciete licentie van dit bestand niet vastgesteld. | Verifiëren van detailweergave en relatie-algoritme. |
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl) | 2026-08-13 | Publieke acceptatieomgeving met dummydata; rechten/licentie van de data onbekend. | Beoogde visuele beoordeling van de publieke applicatie. |
| [bron](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/) | 2026-08-13 | Publieke acceptatieomgeving met dummydata; rechten/licentie van de data onbekend. | Beoogde visuele beoordeling van de beheerapplicatie. |
| [bron](https://www.europeana.eu/en/apis) | 2026-08-13 | Officiële Europeana-documentatie; documentatielicentie niet expliciet vastgesteld. | Bestaande gebruikte bron en referentie voor collectie-overstijgende erfgoedmetadata. |
| [bron](https://www.openarchieven.nl/api/docs/) | 2026-08-13 | Officiële Open Archieven API-documentatie; documentatielicentie niet expliciet vastgesteld. | Bestaande gebruikte bron en referentie voor herleidbare genealogische records. |
| [bron](https://www.delpher.nl/over-delpher/handleiding/zoeken-in-delpher/hoe-zoek-je-het-best/zoeken-naar-verschillende-versies-van-een-woord) | 2026-08-13 | Officiële Delpher-pagina; gebruiks- en auteursrechtinformatie staat op de website, hergebruik van teksten niet afzonderlijk vastgesteld. | Inspiratie voor full-text zoeken over meerdere historische collectie-typen. |
| [bron](https://www.nationaalarchief.nl/onderzoeken/collectie) | 2026-08-13 | Officiële Nationaal Archief-pagina; de pagina vermeldt openbare informatie als herbruikbaar. | Inspiratie en mogelijke aanvullende bron voor archieven, foto’s, kaarten en indexen. |

## Productbeslissing

Maak de bestaande publieke historische zoekroute begrijpelijker met een herleidbaar ‘vervolg ontdekken’-paneel per zoekresultaat. Toon alleen zekere, aanwezige metadata als klikbare vervolgzoeking voor plaats, persoon, gebeurtenis en periode, met behoud van de oorspronkelijke bronwaarde. Scheid expliciet ‘zoeken op dit kenmerk’ van ‘bewezen relatie’ en toon per resultaat bronstatus, lokale Heemskerk-indicatie, ophaaldatum, bronidentifier, rechten/privacystatus en de externe bronlink. Beperk de eerste implementatie tot bestaande Europeana- en Open Archieven-metadata; kopieer geen scans, foto’s of andere media.

**Waarom:** Deze kleine richting sluit direct aan op missie en principes Verbonden, Betrouwbaar, Toegankelijk en Nieuwsgierig. De huidige app ondersteunt de relevante zoekvelden en herleidbare metadata al, maar relaties blijven beperkt tot exacte overlap binnen één resultatenpagina. Klikbare vervolgzoekingen maken collectie-overstijgend ontdekken mogelijk zonder onbewezen entiteitskoppelingen of nieuwe rechten- en privacyrisico’s. De richting draagt primair bij aan epic theme-hkh-autopilot-0002 en ondersteunt daarnaast epic theme-hkh-autopilot-0001.

### Prioriteiten
- Maak plaats-, persoon-, gebeurtenis- en periodevelden in resultaatdetails klikbaar als nieuwe zoekingang.
- Toon duidelijk dat een vervolgzoeking geen bewezen relatie tussen bronnen vormt.
- Behoud en toon bronidentifier, stabiele URI, ophaaldatum, rechten- en privacystatus en externe bronlink.
- Maak bronbeschikbaarheid en lokale Heemskerk-indicatie per zoekopdracht begrijpelijk zichtbaar.
- Voeg alleen toetsbare metadata- en externe-linkfunctionaliteit toe; geen lokale opslag, media-kopieën, naamvarianten of afgeleide matches.

### Besluiten
- **Gebruik bestaande Europeana- en Open Archieven-connectors als enige bronnen in deze richting.** — Deze bronnen zijn al onderdeel van de publieke zoekroute en bieden bestaande API- en metadatafundamenten voor herleidbare resultaten.
- **Maak zekere metadatawaarden klikbaar voor vervolgzoekingen, maar label dit als een nieuwe zoekingang en niet als bewezen relatie.** — De huidige detailweergave bevat plaats, persoon, gebeurtenis en periode, terwijl de bestaande relatiepresentatie alleen exacte metadata-overlap toont. Deze scheiding voorkomt dat gebruikers zoekresultaten als historisch bewijs interpreteren.
- **Maak bronstatus, lokale Heemskerk-indicatie en structurele lacunes zichtbaar in de zoekcontext.** — Bronstatussen bestaan al, maar lokale dekking en ontbrekende collecties worden onvoldoende uitgelegd. Dit versterkt betrouwbaarheid en maakt beperkingen zichtbaar zonder de zoekroute te blokkeren.
- **Beperk de eerste oplevering tot metadata en externe bronlinks.** — De productrichting moet zelfstandig uitvoerbaar blijven en geen nieuwe rechten-, privacy- of opslagrisico’s introduceren. De onderzoekscontext ondersteunt metadatahergebruik en externe bronverwijzingen, maar niet het kopiëren van lokale media.

## UX-voorstel: Herleidbaar vervolg ontdekken vanuit een zoekresultaat

**Gebruikersdoel:** Een bezoeker vindt vanuit een betrouwbaar historisch zoekresultaat nieuwe relevante bronnen via zekere metadata, zonder een zoekingang te verwarren met bewezen historisch verband.

### Flow
1. 1. De bezoeker voert een zoekopdracht uit op tekst, plaats, persoon, gebeurtenis of periode.
2. 2. De zoekcontext toont per bron de status, lokale Heemskerk-indicatie en eventuele ontbrekende broninformatie.
3. 3. De bezoeker opent een resultaatdetail met titel, oorspronkelijke metadatawaarden, bronidentifier, stabiele URI, ophaaldatum, rechten- en privacystatus.
4. 4. In het paneel ‘Vervolg ontdekken’ kiest de bezoeker een aanwezige, zekere waarde zoals plaats, persoon, gebeurtenis of periode.
5. 5. De app start een nieuwe zoekopdracht met de gekozen waarde en toont duidelijk dat dit een nieuwe zoekingang is, geen bewezen relatie tussen de bronnen.
6. 6. De bezoeker kan het oorspronkelijke resultaat en de externe bronlink blijven openen of terugkeren naar de vorige zoekopdracht.

### Wireframe

[Header]
Historisch Heemskerk | Zoekopdracht | Toegankelijkheidsopties

[Zoekcontext]
Zoekopdracht: <oorspronkelijke zoekvraag>
Bronnen: Europeana — beschikbaar | Open Archieven — gedeeltelijk beschikbaar
Lokale Heemskerk-indicatie: aanwezig / niet vastgesteld / niet aanwezig
Ontbrekende of uitgevallen bronnen: <uitleg indien van toepassing>
Ophaaldatum: <datum>

[Resultaatkaart]
Titel: <titel>
Bron: <Europeana of Open Archieven>
Plaats: <waarde> [Zoek opnieuw op plaats]
Persoon: <waarde> [Zoek opnieuw op persoon]
Gebeurtenis: <waarde> [Zoek opnieuw op gebeurtenis]
Periode: <waarde> [Zoek opnieuw op periode]

[Herleidbaarheid]
Bronidentifier: <identifier>
Stabiele bron-URI: <URI>
Rechtenstatus: <status>
Privacystatus: <status>
[Open externe bron]

[Vervolg ontdekken]
Kies een zekere metadatawaarde om een nieuwe zoekingang te starten.
Let op: dit bewijst geen relatie tussen de bronnen.
[Plaats: <waarde>] [Persoon: <waarde>]
[Gebeurtenis: <waarde>] [Periode: <waarde>]

[Resultaatnavigatie]
[Terug naar zoekresultaten] [Nieuwe zoekopdracht]

### Interactiehypotheses
- H1: Als zekere plaats-, persoons-, gebeurtenis- en periodewaarden als duidelijke vervolgzoekknoppen worden aangeboden, start minstens 20% van de gebruikers vanuit een resultaatdetail een vervolgzoekopdracht.
- H2: Als de tekst ‘nieuwe zoekingang, geen bewezen relatie’ direct bij de vervolgacties staat, classificeert minstens 90% van geautomatiseerde inhoudscontroles de relatie-uitleg als expliciet en niet-misleidend.
- H3: Als bronstatus, lokale Heemskerk-indicatie en ontbrekende bronnen boven de resultaten staan, kunnen geautomatiseerde UI-tests voor elke zoekopdracht een status en uitleg vinden, ook bij lege of uitgevallen bronnen.
- H4: Als elke resultaatkaart een bronidentifier, stabiele URI, ophaaldatum, rechtenstatus, privacystatus en externe link toont, voldoen alle volledige resultaten aan de minimale herleidbaarheidsasserties.
- H5: Als alleen aanwezige en zekere metadatawaarden acties opleveren, worden geen knoppen of vervolgqueries gegenereerd voor lege, onbekende of afgeleide waarden.
- H6: Als een vervolgzoeking de vorige zoekcontext behoudt in navigatiegeschiedenis, kan een geautomatiseerde browserflow terugkeren naar het oorspronkelijke resultaat zonder verlies van de zoekvraag.

### Toegankelijkheid
- Alle interactieve elementen zijn bereikbaar met toetsenbord en hebben een zichtbare focusindicator.
- Gebruik semantische headings, landmarks, buttons en links; geef geen betekenis uitsluitend via kleur of Canvas-pixels.
- Geef elk metadata-veld en elke vervolgactie een duidelijk schermlezerlabel, bijvoorbeeld ‘Zoek opnieuw op plaats Heemskerk’.
- Gebruik voldoende kleurcontrast voor tekst, statuslabels, focus en foutmeldingen; combineer statuskleur altijd met tekst.
- Maak bronstatus, onzekerheid en de waarschuwing over ‘geen bewezen relatie’ programmatisch beschikbaar en leesbaar in logische volgorde.
- Ondersteun zoom en reflow zonder verlies van informatie of horizontaal scrollen op kleine schermen.
- Toets geautomatiseerd toetsenbordvolgorde, focusbeheer na een vervolgzoeking, naam/rol/waarde van controls, contrast en volledige tekstuele aanwezigheid van Canvas-inhoud.
- Gebruik geen automatische beweging, time-outs of hover-only informatie.

### Privacy
- Sla zoekopdrachten, bronpayloads en gekozen metadatawaarden niet lokaal op; gebruik ze uitsluitend voor de actieve zoekactie en navigatiestatus.
- Toon alleen persoonsgegevens die al door de bron als relevante metadata worden geleverd en beperk de weergave tot het productdoel: historische bronverkenning.
- Bewaar geen gebruikersidentiteit, gedragsprofiel, klikgeschiedenis of vrije zoekgeschiedenis zonder afzonderlijk doel, grondslag en transparante informatie.
- Toon de privacystatus van elk resultaat en blokkeer of beperk vervolgacties wanneer de bron aangeeft dat publicatie of hergebruik niet passend is.
- Kopieer geen scans, foto’s of andere media; link uitsluitend naar de externe bron en respecteer de bronrechten.
- Maak in toegankelijkheids- en functionele tests controleerbaar dat lege of privacygevoelige velden niet per ongeluk als klikbare vervolgquery worden aangeboden.
- Leg eventuele technische logs vast zonder zoektermen of persoonsmetadata, of anonimiseer die gegevens met een aantoonbaar bewaardoel en beperkte bewaartermijn.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is klein, toetsbaar en agent-uitvoerbaar. Er zijn geen materiële blokkades voor veilige bouw of verificatie.
- **WARNING · PRIVACY** — De detectie van ‘privacygevoelige’ metadatawaarden is niet volledig gespecificeerd. Implementeer dit fail-closed op basis van ontbrekende of niet-toegestane privacystatus: bij onzekerheid geen vervolgactie aanbieden.
- **INFO · CONSISTENCY** — De kandidaat bouwt voort op story:66 en raakt gedeeltelijk aan de bestaande bronstatus-/dekkingsfunctionaliteit. Bewaak dat alleen het vervolgzoekpaneel wordt uitgebreid en bestaande bronstatuslogica niet dubbel wordt geïmplementeerd.

## Geaccepteerde storykandidaten

### Herleidbare vervolgzoeking vanuit zekere resultaatmetadata

_Sleutel: `zekere-metadata-vervolgzoeking`_

Als bezoeker wil ik vanuit een historisch resultaat op een aanwezige, zekere plaats-, persoons-, gebeurtenis- of periodewaarde kunnen zoeken, zodat ik nieuwe bronnen kan ontdekken zonder een nieuwe zoekingang als bewezen historische relatie te interpreteren. De functionaliteit gebruikt uitsluitend bestaande Europeana- en Open Archieven-metadata, behoudt de oorspronkelijke bronwaarde en kopieert geen media of ruwe bronpayloads.

**Acceptatiecriteria**
- In de bestaande resultaatdetailweergave zijn alleen niet-lege, aanwezige metadatawaarden voor plaats, persoon, gebeurtenis en periode als vervolgzoekactie beschikbaar.
- Elke vervolgactie start een nieuwe zoekopdracht met de gekozen oorspronkelijke metadatawaarde en toont duidelijk dat dit een nieuwe zoekingang is en geen bewezen relatie tussen bronnen.
- De oorspronkelijke bronwaarde blijft ongewijzigd zichtbaar naast de vervolgactie.
- De vervolgzoeking gebruikt uitsluitend bestaande Europeana- en Open Archieven-connectors en slaat zoekopdrachten, bronpayloads of klikgeschiedenis niet lokaal op.
- Lege, onbekende, privacygevoelige of afgeleide metadatawaarden leveren geen vervolgactie op.
- Geautomatiseerde tests controleren dat de vervolgquery exact de gekozen bronwaarde gebruikt, dat de waarschuwing over het ontbreken van een bewezen relatie tekstueel aanwezig is en dat terugnavigatie naar het oorspronkelijke resultaat werkt.
- De bestaande bronidentifier, stabiele bron-URI, ophaaldatum, rechtenstatus, privacystatus en externe bronlink blijven in het resultaatdetail beschikbaar.
- Alle vervolgacties zijn semantische buttons of links met duidelijke toegankelijke labels, zichtbare focus en programmatisch beschikbare status- en onzekerheidstekst.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt), [https://www.europeana.eu/en/apis](https://www.europeana.eu/en/apis), [https://www.openarchieven.nl/api/docs/](https://www.openarchieven.nl/api/docs/)

Afhankelijkheden: story:66 (herkend als bestaande stories: 66)

Risico's: Bronmetadata kan onvoldoende uniform of precies zijn voor veilige vervolgqueries; lege of onzekere waarden moeten daarom fail-closed worden uitgesloten., Gebruikers kunnen ondanks de expliciete tekst een vervolgzoeking als bewijsrelatie interpreteren; de interface moet dit onderscheid consequent tonen., Wijzigingen in bestaande zoeknavigatie kunnen bestaande terugnavigatie of resultaatcontext beïnvloeden.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
