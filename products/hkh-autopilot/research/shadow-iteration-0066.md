---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0066
date: 2026-08-13
status: approved
sources:
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart
  - https://hkh-autopilot.vdzonsoftware.nl
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl
  - https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/
  - https://api.openarchieven.nl/1.1/records/search.json?name=Heemskerk&archive_code=hee&number_show=3
  - https://www.openarchieven.nl/api/docs/
  - https://www.openarchieven.nl/api/docs/oai-pmh/
  - https://api.europeana.eu/en
  - https://www.europeana.eu/en/rights/usage-guidelines-for-metadata
  - https://geheugenvannederland.nl/
---
# Productcyclus 66

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De belangrijkste onbeantwoorde productvraag is hoe HKH een bruikbare, herleidbare historische ontdekkingstocht kan bieden wanneer externe bronnen uitvallen of onvoldoende dekking geven. De acceptatiezoekactie op ‘Heemskerk’ eindigt momenteel in een generieke foutmelding zonder resultaten, bronstatussen of diagnose. Open Archieven is direct bereikbaar en bevat een Heemskerk-relevante bronset; Europeana vereist een API-key.

### Huidig doel en doelgroep

Een brede publieke historische zoek- en ontdekapp voor iedereen die iets wil weten over Heemskerkse gebouwen, straten, personen, gebeurtenissen of onderwerpen.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md), [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl)

### Actuele zoekflow

De zoekpagina biedt vrije tekst, plek, persoon, gebeurtenis, periode en bronfilter. Een werkelijke acceptatiezoekactie op ‘Heemskerk’ eindigde na laden met alleen ‘Geen historische bronnen konden worden geraadpleegd’, ‘Opnieuw proberen’ en ‘Zoekopdracht aanpassen’.

Bronnen: [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl)

### Technische basis is rijker dan de zichtbare fouttoestand

De repository modelleert bronstatus, deelbeschikbaarheid, tellingen, stabiele identifiers, bronlinks, rechten-, privacy-, context- en relatievelden, maar deze zijn in de actuele volledige-uitvalflow niet zichtbaar.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart)

### Open Archieven is direct testbaar

De publieke API accepteert zoekopdrachten zonder login. Een werkelijke API-aanroep met archive_code ‘hee’ leverde records van Historische Kring Heemskerk met identifiers, gebeurtenisplaatsen, bronsoorten en oorspronkelijke recordlinks.

Bronnen: [https://api.openarchieven.nl/1.1/records/search.json?name=Heemskerk&archive_code=hee&number_show=3](https://api.openarchieven.nl/1.1/records/search.json?name=Heemskerk&archive_code=hee&number_show=3), [https://www.openarchieven.nl/api/docs/records/search.php](https://www.openarchieven.nl/api/docs/records/search.php)

### Rechten- en bronnuance

Open Archieven documenteert CC0 voor datasetdata via OAI-PMH, maar scans en viewers van derden vallen daar niet automatisch onder. Europeana stelt metadata onder CC0 beschikbaar, terwijl digitale objecten afzonderlijke rechtenstatements hebben en API-toegang een sleutel vereist.

Bronnen: [https://www.openarchieven.nl/api/docs/oai-pmh/](https://www.openarchieven.nl/api/docs/oai-pmh/), [https://www.europeana.eu/en/rights/usage-guidelines-for-metadata](https://www.europeana.eu/en/rights/usage-guidelines-for-metadata), [https://www.europeana.eu/es/rights/terms-of-use](https://www.europeana.eu/es/rights/terms-of-use)

### Vergelijkbare inspiratie

Geheugen van Nederland combineert zoeken met thema’s, verhalen en verbonden collecties. Delpher biedt verfijning op periode, verspreidingsgebied, titel en herkomst.

Bronnen: [https://geheugenvannederland.nl/](https://geheugenvannederland.nl/), [https://www.delpher.nl/over-delpher/handleiding/zoeken-in-delpher/hoe-zoek-je-het-best/zoeken-naar-verschillende-versies-van-een-woord](https://www.delpher.nl/over-delpher/handleiding/zoeken-in-delpher/hoe-zoek-je-het-best/zoeken-naar-verschillende-versies-van-een-woord)

### Huidige applicatie

**Doel:** Geschiedenis van Heemskerk toegankelijk maken door gebruikers vanuit vragen, plekken, personen en gebeurtenissen te verbinden met externe historische collecties.

**Wat ontbreekt:**
- Volledige bronuitval toont alleen een generieke melding.
- Geen zichtbare per-bronstatus, foutcategorie, telling of dekkingsuitleg.
- Herleidbaarheid, rechteninformatie en vervolgontdekking konden bij actuele uitval niet praktisch worden gecontroleerd.
- Open Archieven is aantoonbaar beschikbaar, maar nog niet zichtbaar in de publieke productflow.
- Europeana is afhankelijk van een API-key en aparte objectrechten.

### Verbetermogelijkheden

- Onderzoek een directe koppeling met Open Archieven als publiek bereikbare, Heemskerk-relevante bron.
- Toon per bron beschikbaarheid, foutcategorie, query, telling en ontbrekende dekking.
- Behoud deelresultaten wanneer slechts één bron faalt.
- Toon bronnaam, stabiele identifier, oorspronkelijke link, ophaalmoment en gescheiden metadata-/objectrechten.
- Behandel ontbrekende of tegenstrijdige rechten als onbekend.
- Maak brede vrije tekst en lokale bron-/plaatsdekking expliciet onderscheidbaar.
- Gebruik bronrelaties uitsluitend als bronclaims, niet als door HKH afgeleide feiten.
- Maak succes-, gedeeltelijke-uitval- en volledige-uitvaltoestanden deterministisch testbaar in acceptatie.

### Inspiratiebronnen

- [Open Archieven](https://www.openarchieven.nl/api/docs/) — Open API, stabiele identifiers, A2A/OAI-PMH en bronrelaties.
- [Geheugen van Nederland](https://geheugenvannederland.nl/) — Thema’s, verhalen en verbonden erfgoedcollecties.
- [Delpher](https://www.delpher.nl/over-delpher/handleiding/zoeken-in-delpher/hoe-zoek-je-het-best/zoeken-naar-verschillende-versies-van-een-woord) — Historische zoekverfijning op periode, herkomst en broncontext.
- [Europeana APIs](https://api.europeana.eu/en) — Federated erfgoedzoeking met Search-, Record-, Entity- en IIIF-lagen.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md) | 2026-08-13 | Geen expliciete licentie aangetroffen; rechtenstatus onbekend. | Productdoel, bronstrategie en technische beloften. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt) | 2026-08-13 | Geen expliciete licentie aangetroffen; rechtenstatus onbekend. | Bronstatussen en uitvalgedrag. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart) | 2026-08-13 | Geen expliciete licentie aangetroffen; rechtenstatus onbekend. | Frontendvelden voor resultaten, rechten en context. |
| [bron](https://hkh-autopilot.vdzonsoftware.nl) | 2026-08-13 | Rechten/licentie van getoonde inhoud onbekend. | Productieflow werkelijk bekeken via Chromium. |
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl) | 2026-08-13 | Rechten/licentie van dummy-inhoud onbekend. | Acceptatieflow werkelijk bekeken en zoekactie uitgevoerd. |
| [bron](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/) | 2026-08-13 | Rechten/licentie van beheerinhoud onbekend. | Beheeromgeving zonder login bekeken; niets gewijzigd. |
| [bron](https://api.openarchieven.nl/1.1/records/search.json?name=Heemskerk&archive_code=hee&number_show=3) | 2026-08-13 | Dataset CC0 volgens OAI-PMH-documentatie; derdepartijscans en viewers kunnen eigen rechten hebben. | Werkelijke API-verificatie van Heemskerk-relevante records. |
| [bron](https://www.openarchieven.nl/api/docs/) | 2026-08-13 | Licentie van documentatietekst onbekend. | API-contract en gebruikslimieten. |
| [bron](https://www.openarchieven.nl/api/docs/oai-pmh/) | 2026-08-13 | CC0 voor geleverde dataset; scans/viewers van derden uitgezonderd. | Hergebruik en rechtenafbakening. |
| [bron](https://api.europeana.eu/en) | 2026-08-13 | API- en platformvoorwaarden van Europeana gelden. | Mogelijkheden en API-keyafhankelijkheid. |
| [bron](https://www.europeana.eu/en/rights/usage-guidelines-for-metadata) | 2026-08-13 | Europeana-metadata CC0; bronattributie gevraagd. | Metadatarechten en bronvermelding. |
| [bron](https://geheugenvannederland.nl/) | 2026-08-13 | Rechten van site-inhoud onbekend. | Inspiratie voor thema’s, verhalen en collectiekoppeling. |

## Productbeslissing

Maak de historische zoekroute bronbewust en veerkrachtig: integreer Open Archieven als eerste controleerbare externe bron en toon per zoekactie resultaten, bronstatus, telling, ophaalmoment, stabiele identifier en oorspronkelijke bronlink. Behoud deelresultaten bij gedeeltelijke uitval en geef bij volledige uitval een concrete diagnose en dekkingsuitleg.

**Waarom:** Deze kleine richting sluit direct aan op epic theme-hkh-autopilot-0002 en verhelpt de huidige generieke foutmelding. Open Archieven is zonder login testbaar en leverde Heemskerk-relevante records met identifiers en oorspronkelijke links. De repository bevat al modellen voor bronstatus, tellingen, identifiers, links en rechtenvelden, waardoor de richting zelfstandig uitvoerbaar en toetsbaar is. Ze versterkt de principes Verbonden, Betrouwbaar, Toegankelijk, Open en Herbruikbaar zonder onbewezen historische relaties te introduceren.

### Prioriteiten
- Integreer Open Archieven voor Heemskerk-relevante metadata en externe bronlinks.
- Maak succes, gedeeltelijke uitval en volledige uitval deterministisch zichtbaar.
- Toon per bron status, foutcategorie, telling, query en ophaalmoment.
- Toon metadatarechten en objectrechten afzonderlijk; behandel onbekende rechten als onbekend.
- Maak iedere vervolgstap herleidbaar naar bronclaims en stabiele identifiers.

### Besluiten
- **Gebruik Open Archieven als eerste externe bron voor de publieke zoekroute.** — De bron is direct bereikbaar zonder login en een werkelijke zoekactie leverde Heemskerk-relevante records op.
- **Presenteer metadata en externe links, maar geen automatisch overgenomen scans of objecten.** — Open Archieven beschrijft datasetdata als CC0, terwijl scans en viewers van derden eigen rechten kunnen hebben.
- **Maak bronstatus en gedeeltelijke beschikbaarheid zichtbaar in de zoekresultaten.** — De actuele volledige-uitvalflow toont alleen een generieke melding, terwijl de technische basis al bronstatussen en deelbeschikbaarheid modelleert.
- **Beperk vervolgontdekking tot expliciete bronrelaties en bronvastgelegde metadata.** — De productrichting moet verbanden toegankelijk maken zonder onbewezen historische relaties als feiten te presenteren.

## UX-voorstel: Bronbewust zoeken naar Heemskerkse geschiedenis

**Gebruikersdoel:** De gebruiker vindt herleidbare historische metadata over Heemskerk en begrijpt welke bronnen beschikbaar, beperkt of uitgevallen zijn.

### Flow
1. Open Historisch zoeken.
2. Voer een zoekterm in, bijvoorbeeld ‘Heemskerk’, en verstuur de zoekopdracht.
3. Bekijk resultaten met bronnaam, korte metadata, stabiele identifier en oorspronkelijke bronlink.
4. Bekijk per bron de status, telling, zoekopdracht en ophaalmoment.
5. Open optioneel de bronverantwoording met metadatarechten en objectrechten.
6. Bij gedeeltelijke uitval: gebruik beschikbare resultaten en bekijk welke bron ontbreekt.
7. Bij volledige uitval: lees de concrete diagnose en kies ‘Opnieuw proberen’ of pas de zoekopdracht aan.

### Wireframe

[Pagina: Historisch zoeken]

H1 Historisch zoeken
[Zoekterm________________] [Zoeken]
[Plaats] [Persoon] [Gebeurtenis] [Periode] [Bron]

Zoekopdracht: Heemskerk
Status: Gedeeltelijk beschikbaar
2 bronnen geraadpleegd · opgehaald om 13-08-2026 14:32

Bronnen
[Beschikbaar] Open Archieven · 12 resultaten
  Zoekopdracht: name=Heemskerk, archive=hee
  [Toon broninformatie]
[Beperkt] Andere bron · tijdelijk niet beschikbaar
  Reden: time-out · [Opnieuw proberen]

Resultaten
1. Titel of gebeurtenis
   Plaats: Heemskerk · Datum: onbekend
   Identifier: OA-12345 · [Open oorspronkelijke bron]
   Metadatarechten: CC0 · Objectrechten: onbekend

[Meer resultaten laden]

Volledige uitval:
Geen historische bronnen konden worden geraadpleegd.
Diagnose: Open Archieven gaf een time-out; andere bronnen zijn niet geconfigureerd.
[Opnieuw proberen] [Zoekopdracht aanpassen]

### Interactiehypotheses
- Als per bron status, foutcategorie en telling zichtbaar zijn, kunnen gebruikers beter begrijpen of een zoekactie gedeeltelijk geslaagd is; toetsbaar met geautomatiseerde assertions op zichtbaarheid en correcte statuslabels.
- Als elk resultaat een stabiele identifier en oorspronkelijke bronlink toont, kunnen gebruikers de herkomst van metadata controleren; toetsbaar met een fixture waarin identifier en link exact overeenkomen met het bronrecord.
- Als gedeeltelijke resultaten behouden blijven wanneer één bron faalt, blijft de zoekroute bruikbaar zonder foutieve volledigheidsclaim; toetsbaar met deterministische success-, partial-failure- en full-failure-scenario’s.
- Als metadatarechten en objectrechten afzonderlijk worden getoond en onbekende rechten expliciet als ‘onbekend’ verschijnen, ontstaan minder onterechte hergebruikclaims; toetsbaar met rechtenfixtures.
- Als de query, het ophaalmoment en dekkingsbeperking zichtbaar zijn, kunnen gebruikers de actualiteit en reikwijdte van resultaten beter inschatten; toetsbaar met tekst- en tijdstempelassertions.
- Als vervolgrelaties uitsluitend expliciete bronrelaties tonen, worden onbewezen historische verbanden niet als feiten gepresenteerd; toetsbaar met testdata zonder bronrelatie waarin geen relatiekaart verschijnt.

### Toegankelijkheid
- Gebruik semantische koppen, landmarks, labels en een logisch toetsenbordvolgorde.
- Maak zoeken, opnieuw proberen, filters, broninformatie en externe links volledig met toetsenbord bedienbaar.
- Kondig laad-, succes-, gedeeltelijke-uitval- en volledige-uitvalstatussen aan via een live region.
- Gebruik voldoende kleurcontrast en combineer kleur altijd met tekst of een pictogram met tekstalternatief.
- Geef focusindicatoren, zichtbare foutuitleg en herstelacties.
- Gebruik tabellen of gegroepeerde resultaatkaarten met begrijpelijke schermlezerlabels.
- Maak externe links duidelijk herkenbaar en vermeld dat ze een andere website openen.

### Privacy
- Verwerk vrije zoektermen alleen voor het uitvoeren en tijdelijk loggen van de zoekopdracht; verzamel geen account- of profielgegevens in deze MVP.
- Sla zoektermen niet langer op dan noodzakelijk voor foutdiagnose en operationele monitoring; anonimiseer of aggregeer logs.
- Beperk logging van bronresponses tot technische metadata, identifiers en foutcategorieën; vermijd onnodige persoonsgegevens uit historische records.
- Toon persoonsgegevens uit externe bronnen alleen wanneer ze door de bron worden geleverd en functioneel nodig zijn voor het zoekresultaat.
- Documenteer de verwerkingsdoelen, bewaartermijnen en grondslag voor eventuele technische logs.
- Behandel rechteninformatie die ontbreekt of tegenstrijdig is als ‘onbekend’ en bied geen download- of hergebruikclaim voor objecten zonder duidelijke rechtenstatus.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is uitvoerbaar, toetsbaar en vereist geen handmatige eigenaaractie. Er zijn wel inhoudelijke overlap en een beperkte privacyverduidelijking.
- **WARNING · CONSISTENCY** — De adapter- en contractscope overlapt sterk met het reeds gepubliceerde story:61 en de foutafhandeling met story:63. Controleer vóór levering dat dit geen dubbel implementatieresultaat oplevert; hergebruik of markeer bestaande dekking waar mogelijk.
- **WARNING · PRIVACY** — De kandidaat beperkt zich tot metadata, maar specificeert niet expliciet welke persoonsvelden maximaal mogen worden verwerkt. Beperk verwerking en presentatie tot functioneel noodzakelijke velden en vermijd onnodige ruwe persoonsgegevens.

## Geaccepteerde storykandidaten

### Open Archieven als controleerbare externe bronadapter

_Sleutel: `openarchieven-bronadapter-met-contractfixtures`_

Als bezoeker wil ik dat de historische zoekroute Heemskerk-relevante metadata uit Open Archieven kan ophalen, zodat ik resultaten met stabiele identifiers en oorspronkelijke bronlinks kan bekijken wanneer deze externe bron beschikbaar is. Implementeer de adapter tegen het gedocumenteerde zoekcontract en valideer succes-, nulresultaat- en ongeldige-responsegevallen met reproduceerbare fixtures. Toon uitsluitend metadata en externe links; scans, volledige objectinhoud en onbevestigde rechtenclaims blijven buiten scope.

**Acceptatiecriteria**
- Een zoekopdracht met de fixture voor ‘Heemskerk’ en archive_code ‘hee’ levert resultaten met bronnaam, stabiele identifier, gebeurtenisplaats indien aanwezig en oorspronkelijke bronlink.
- De adapter accepteert uitsluitend het vastgelegde Open Archieven-contract en zet ontbrekende of ongeldig gevormde identifiers, links of verplichte velden om naar een expliciete bronfout zonder het resultaat als geldig te presenteren.
- Een geldig nulresultaat wordt onderscheiden van een technische fout en toont geen verzonnen resultaat of provider-totaal.
- De adapter bewaart of toont geen scans, digitale objectbestanden of ruwe API-payloads.
- Ontbrekende of tegenstrijdige rechteninformatie wordt als ‘Onbekend’ weergegeven en leidt niet tot een hergebruik- of downloadclaim.
- Geautomatiseerde contracttests dekken minimaal een geldig resultaat, nulresultaat, time-out en ongeldige bronresponse met deterministische assertions.
- De implementatie respecteert de gedocumenteerde API-aanroepvorm en rate-limitinformatie zonder eigenaaractie of autorisatietoken.

Bronnen: [https://api.openarchieven.nl/1.1/records/search.json?name=Heemskerk&archive_code=hee&number_show=3](https://api.openarchieven.nl/1.1/records/search.json?name=Heemskerk&archive_code=hee&number_show=3), [https://www.openarchieven.nl/api/docs/records/search.php](https://www.openarchieven.nl/api/docs/records/search.php), [https://www.openarchieven.nl/api/docs/](https://www.openarchieven.nl/api/docs/), [https://www.openarchieven.nl/api/docs/oai-pmh/](https://www.openarchieven.nl/api/docs/oai-pmh/), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart)

Afhankelijkheden: story:61, story:63 (herkend als bestaande stories: 61, 63)

Risico's: Open Archieven kan tijdelijk niet beschikbaar zijn of het externe contract wijzigen., De bron levert mogelijk persoonsgegevens of objectlinks waarvan rechten- en privacystatus niet volledig bekend zijn; daarom blijft de verwerking metadata-only en fail-closed., Deze kandidaat levert de adapter en contractvalidatie; gebruikersgerichte statuspresentatie blijft afhankelijk van de bestaande bronveerkrachtige zoekuitkomst.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
