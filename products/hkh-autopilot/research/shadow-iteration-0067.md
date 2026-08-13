---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0067
date: 2026-08-13
status: approved
sources:
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart
  - https://github.com/robbertvdzon/hkh-autopilot
  - https://hkh-autopilot.vdzonsoftware.nl
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl
  - https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/
  - https://www.openarchieven.nl/api/docs/records/search.php
  - https://www.openarchieven.nl/api/docs/
  - https://www.openarchieven.nl/datasets/
  - https://www.europeana.eu/en/apis
  - https://www.europeana.eu/eu/rights/usage-guidelines-for-metadata
---
# Productcyclus 67

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De publieke zoekroute is bruikbaar qua invoervelden, maar een zoekactie op ‘Heemskerk’ eindigt in productie en acceptatie met volledige bronuitval. De repository beschrijft al bronstatussen, deelresultaten, stabiele identifiers en rechtenvelden, maar die zijn niet zichtbaar in de gedeployde flow. De belangrijkste onbeantwoorde productvraag is hoe gebruikers ondanks bronuitval controleerbaar verder kunnen zoeken.

### Huidig doel en doelgroep

Historisch Heemskerk is een publieke historische ontdekapp voor een brede doelgroep. Gebruikers zoeken vanuit vrije tekst, plek, persoon, gebeurtenis, periode of bron en moeten Heemskerk in bredere historische context kunnen verkennen.

Bronnen: [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md)

### Werkelijke zoekuitkomst

Een read-only zoekactie op ‘Heemskerk’ toont in productie en acceptatie: ‘Geen historische bronnen konden worden geraadpleegd’, ‘Europeana: niet geconfigureerd’ en ‘Open Archieven: ongeldige bronrespons’. Er verschijnen geen resultaten, tellingen, identifiers of bronlinks.

Bronnen: [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl)

### Verschil tussen repository en deployment

De repository beschrijft ondersteuning voor resultaten, nulresultaten, gedeeltelijke beschikbaarheid, stabiele Open Archieven-identifiers, externe bronlinks, rechtenstatussen en context. Deze functionaliteit is in de bekeken gedeployde fouttoestand niet zichtbaar.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart)

### Beheeroppervlak

De beheeracceptatie is zonder login bereikbaar en toont nieuws-publicatie en lokale record-intake. Geen formulier is verzonden. Dit is een relevant privacy- en toegangscontrolepunt zodra echte gegevens worden verwerkt.

Bronnen: [https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/)

### Open Archieven-contract

De officiële API ondersteunt een verplichte naamquery, optionele archive_code, paginering en maximaal 100 resultaten. De algemene documentatie noemt throttling tot 4 requests per seconde per IP en server-side caching.

Bronnen: [https://www.openarchieven.nl/api/docs/records/search.php](https://www.openarchieven.nl/api/docs/records/search.php), [https://www.openarchieven.nl/api/docs/](https://www.openarchieven.nl/api/docs/)

### Europeana-toegang en rechten

Europeana Search- en Record-API’s vereisen een gratis account en API-key. Europeana-metadata is CC0 1.0, maar bronvermelding blijft gewenst en rechten, privacy en wetgeving rond digitale objecten moeten afzonderlijk worden beoordeeld.

Bronnen: [https://www.europeana.eu/en/apis](https://www.europeana.eu/en/apis), [https://www.europeana.eu/eu/rights/usage-guidelines-for-metadata](https://www.europeana.eu/eu/rights/usage-guidelines-for-metadata)

### Vergelijkbare inspiratie

Geheugen van Nederland combineert zoeken met thema’s, verhalen en verbonden collecties. Delpher laat zien hoe filters op periode, verspreidingsgebied, titel en herkomst historisch vervolgonderzoek ondersteunen.

Bronnen: [https://geheugenvannederland.nl/](https://geheugenvannederland.nl/), [https://www.delpher.nl/over-delpher/handleiding/zoeken-in-delpher/hoe-zoek-je-het-best/zoeken-naar-verschillende-versies-van-een-woord](https://www.delpher.nl/over-delpher/handleiding/zoeken-in-delpher/hoe-zoek-je-het-best/zoeken-naar-verschillende-versies-van-een-woord)

### Huidige applicatie

**Doel:** Een brede publieke historische ontdekapp maken die geschiedenis van Heemskerk toegankelijk, betekenisvol en beleefbaar maakt door lokale bronnen te verbinden met historische collecties daarbuiten.

**Wat ontbreekt:**
- De actuele zoekroute levert geen resultaten bij ‘Heemskerk’.
- De foutmelding geeft geen concrete diagnose, dekking, telling, ophaalmoment of alternatieve bron.
- De zichtbare flow toont geen deelresultaten bij gedeeltelijke bronuitval.
- Stabiele identifiers, originele bronlinks, rechtenstatus en context zijn niet zichtbaar in de fouttoestand.
- De beheeromgeving toont muterende formulieren zonder zichtbare login.

### Verbetermogelijkheden

- Maak de gedeployde flow consistent met het beschreven zoekcontract.
- Toon per bron status, foutcategorie, telling, query, ophaalmoment en dekking.
- Behoud deelresultaten wanneer minstens één bron beschikbaar is.
- Maak nulresultaat, ongeldige respons, timeout en volledige uitval duidelijk onderscheidbaar.
- Toon stabiele identifiers, originele bronlinks en metadata-/objectrechten afzonderlijk.
- Beperk persoonsmetadata tot noodzakelijke velden en maak privacystatus zichtbaar.
- Beveilig beheerfunctionaliteit passend voordat echte publicatie- of intakegegevens worden verwerkt.
- Gebruik thematische/verhalende ingangen naast filters, geïnspireerd door Geheugen van Nederland en Delpher.

### Inspiratiebronnen

- [Geheugen van Nederland](https://geheugenvannederland.nl/) — Zoeken gecombineerd met thema’s, verhalen en verbonden collecties.
- [Delpher](https://www.delpher.nl/over-delpher/handleiding/zoeken-in-delpher/hoe-zoek-je-het-best/zoeken-naar-verschillende-versies-van-een-woord) — Voorbeeld van verfijnde historische zoekfilters en bronvermelding.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md) | 2026-08-13 | Geen LICENSE, LICENSE.md of NOTICE gevonden in gecontroleerde standaardpaden; licentie onbekend. | Primaire technische productbeschrijving. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt) | 2026-08-13 | Licentie van het bestand onbekend. | Bronstatussen en deelbeschikbaarheid. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart) | 2026-08-13 | Licentie van het bestand onbekend. | Resultaat-, context-, rechten- en relatievelden. |
| [bron](https://github.com/robbertvdzon/hkh-autopilot) | 2026-08-13 | Publieke repository; licentie onbekend. | Repository-identiteit. |
| [bron](https://hkh-autopilot.vdzonsoftware.nl) | 2026-08-13 | Applicatierechten/licentie onbekend; read-only gebruikt. | Productieflow gecontroleerd. |
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl) | 2026-08-13 | Representatieve nepdata en gemockte koppelingen; UI-rechten onbekend. | Acceptatieflow gecontroleerd. |
| [bron](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/) | 2026-08-13 | Rechten/licentie onbekend; geen mutatie uitgevoerd. | Beheerflow gecontroleerd. |
| [bron](https://www.openarchieven.nl/api/docs/records/search.php) | 2026-08-13 | Documentatielicentie onbekend; brondatarechten kunnen per archief verschillen. | Officieel API-zoekcontract. |
| [bron](https://www.openarchieven.nl/api/docs/) | 2026-08-13 | Documentatielicentie onbekend. | Officiële API-limieten en caching. |
| [bron](https://www.openarchieven.nl/datasets/) | 2026-08-13 | Metadata- en hergebruikstatus kan per archieforganisatie verschillen. | Dataset- en bronoverzicht. |
| [bron](https://www.europeana.eu/en/apis) | 2026-08-13 | API-gebruik vereist account, API-key en de vermelde voorwaarden. | Officiële toegangsinformatie. |
| [bron](https://www.europeana.eu/eu/rights/usage-guidelines-for-metadata) | 2026-08-13 | Metadata CC0 1.0; bronvermelding gewenst; objectrechten afzonderlijk. | Officiële rechteninformatie. |

## Productbeslissing

Herstel de historische zoek-MVP voor Open Archieven met een controleerbare deelresultaatweergave: zoek op ‘Heemskerk’, toon beschikbare records met stabiele identifier, originele bronlink, minimale metadata en rechtenstatus, en toon per bron een expliciete status wanneer een bron uitvalt.

**Waarom:** Deze kleine richting sluit direct aan op epic theme-hkh-autopilot-0002 en maakt de kernbelofte opnieuw bruikbaar. De huidige productie- en acceptatieflow toont bij ‘Heemskerk’ volledige bronuitval zonder resultaten, tellingen, identifiers of bronlinks. De repository beschrijft al bronstatussen, deelbeschikbaarheid, identifiers, links, rechten en context; de uitvoeringsfocus is daarom het zichtbaar en betrouwbaar maken van dit bestaande zoekcontract. Open Archieven ondersteunt een verplichte naamquery, paginering en maximaal 100 resultaten. De richting blijft controleerbaar doordat query, ophaalmoment, bronstatus en originele bronlink zichtbaar zijn. Europeana blijft buiten deze eerste MVP omdat toegang een account en API-key vereist.

### Prioriteiten
- Laat Open Archieven een geldige zoekrespons leveren voor de query ‘Heemskerk’.
- Behoud en toon deelresultaten wanneer minstens één bron beschikbaar is.
- Toon per bron status, foutcategorie, aantal resultaten, query en ophaalmoment.
- Toon per record alleen noodzakelijke metadata, een stabiele identifier, originele bronlink en afzonderlijke rechtenstatus.
- Maak nulresultaat, ongeldige respons, timeout en volledige bronuitval zichtbaar verschillend.

### Besluiten
- **Gebruik Open Archieven als enige externe bron in deze herstelstap.** — Open Archieven is als eerste externe bron gekozen en heeft een gedocumenteerd zoekcontract zonder verplichte API-key.
- **Maak bronuitval niet fataal voor de volledige zoekactie wanneer een andere bron resultaten levert.** — De repository beschrijft deelbeschikbaarheid, maar de gedeployde fouttoestand toont geen deelresultaten. Dit ondersteunt betrouwbaarheid en voorkomt dat één defecte bron de ontdekking blokkeert.
- **Maak elke getoonde record herleidbaar via stabiele identifier en permanente originele bronlink.** — Herleidbaarheid is een productprincipe en de repository beschrijft deze velden al; ze ontbreken in de actuele foutweergave.
- **Toon rechtenstatus en beperkte persoonsmetadata afzonderlijk van de inhoudelijke recordmetadata.** — Externe brondata kunnen verschillende rechten- en privacycondities hebben; rechten van metadata en digitale objecten moeten afzonderlijk worden beoordeeld.

## UX-voorstel: Controleerbaar zoeken in Open Archieven

**Gebruikersdoel:** De gebruiker zoekt op ‘Heemskerk’ en kan beschikbare historische records betrouwbaar bekijken, ook wanneer een bron gedeeltelijk uitvalt.

### Flow
1. Open de pagina Historisch zoeken.
2. Voer ‘Heemskerk’ in en activeer Zoeken.
3. Toon de zoekopdracht, het ophaalmoment en per bron de status, foutcategorie en het aantal resultaten.
4. Toon beschikbare records met minimale metadata, stabiele identifier, originele bronlink en afzonderlijke rechtenstatus.
5. Toon bronuitval als gedeeltelijke beschikbaarheid wanneer andere resultaten beschikbaar zijn.
6. Toon een duidelijk onderscheiden nulresultaat of volledige bronuitval met diagnose en opnieuw proberen-optie.

### Wireframe

[Pagina: Historisch zoeken]

H1 Historisch zoeken
[Zoekterm, verplicht: Heemskerk] [Zoeken]

Zoekstatus
Query: Heemskerk | Ophaalmoment: datum en tijd

Bronnen
- Open Archieven: Beschikbaar / Gedeeltelijk beschikbaar / Geen resultaten / Ongeldige respons / Timeout
  Aantal resultaten: n
  Foutdetails: begrijpelijke categorie en vervolgstap

Resultaten
[Recordkaart]
Titel of gebeurtenis
Datum | Plaats | Bron/collectie
Identifier: stabiele-id
[Open originele bron]
Rechtenstatus: status of Onbekend

[Meer resultaten laden]

Bij volledige uitval:
‘Geen bronnen konden worden geraadpleegd.’
Per bron: status, oorzaak, query, ophaalmoment
[Opnieuw proberen]

### Interactiehypotheses
- Als Open Archieven een geldige respons retourneert, ziet minstens 95% van geautomatiseerde scenario’s voor ‘Heemskerk’ een resultaatlijst of expliciet nulresultaat in plaats van een generieke foutmelding.
- Als één bron uitvalt terwijl een andere bron resultaten levert, blijft de resultaatlijst zichtbaar en wordt de uitgevallen bron afzonderlijk gemarkeerd als gedeeltelijke beschikbaarheid.
- Als per bron query, status, telling en ophaalmoment worden getoond, kunnen geautomatiseerde UI-tests deze vier velden onderscheiden voor beschikbaarheid, nulresultaat, timeout, ongeldige respons en volledige uitval.
- Als elke record een stabiele identifier en originele bronlink bevat, kan een geautomatiseerde test controleren dat beide velden aanwezig en uniek/herleidbaar zijn.
- Als rechtenstatus apart van recordmetadata wordt weergegeven, worden records zonder bekende rechtenstatus niet als vrij herbruikbaar gepresenteerd.
- Als de zoekactie alleen de noodzakelijke zoekterm en bronmetadata verwerkt, wordt geen extra persoonsgegeven opgeslagen voor deze MVP.

### Toegankelijkheid
- Gebruik semantische koppen, labels en een formulier met een expliciete submitknop.
- Maak bronstatussen beschikbaar als tekst; gebruik geen kleur als enige betekenisdrager.
- Plaats fout- en statusmeldingen in een live region met passende aria-live-instelling.
- Zorg dat alle bediening met toetsenbord bereikbaar is en een zichtbare focusindicator heeft.
- Gebruik voldoende contrast voor tekst, links, statussen en foutmeldingen.
- Geef links beschrijvende namen, bijvoorbeeld ‘Open originele bron voor record …’.
- Maak laden, nulresultaat en fouttoestanden programmatisch herkenbaar voor schermlezers.
- Behoud een logische focusvolgorde en voorkom dat focus onverwacht naar nieuwe resultaten springt.

### Privacy
- Gebruik de zoekterm uitsluitend voor het uitvoeren en tijdelijk loggen van de zoekactie; sla deze niet langer op dan noodzakelijk.
- Toon alleen noodzakelijke persoonsmetadata uit bronrecords, bijvoorbeeld naam, datum en context; verberg overbodige details.
- Maak duidelijk dat brondata extern zijn en dat privacy- en rechtenstatus per record kunnen verschillen.
- Sla geen gebruikersprofielen, zoekgeschiedenis of identificerende analytics op zonder duidelijk doel, grondslag en bewaartermijn.
- Gebruik voor publieke zoekresultaten geen beheer- of intakegegevens.
- Beveilig beheerfunctionaliteit en lokale record-intake met passende authenticatie voordat echte persoonsgegevens worden verwerkt.
- Toon ‘Onbekend’ wanneer rechten- of privacystatus niet betrouwbaar kan worden vastgesteld; suggereer geen toestemming of vrij hergebruik.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is agent-uitvoerbaar, beperkt tot deterministische foutnormalisatie en geautomatiseerde fixtures. Er zijn geen blokkerende bron-, privacy-, rechten-, toegankelijkheids- of scopeproblemen.
- **WARNING · CONSISTENCY** — Er is gedeeltelijke overlap met de bestaande kandidaten story:63 en story:74, die respectievelijk bronstatussen en de Open Archieven-adapter behandelen. Deze kandidaat voegt echter voldoende specifieke responsclassificatie en fixturedekking toe en is daarom geen exact duplicaat.

## Geaccepteerde storykandidaten

### Herleidbare foutdiagnose voor Open Archieven-responsen

_Sleutel: `openarchieven-responsdiagnose`_

Als Product Factory wil ik dat de Open Archieven-adapter technische responsproblemen deterministisch omzet naar veilige, afzonderlijke foutcategorieën, zodat de bestaande historische zoekroute onderscheid maakt tussen time-out, HTTP-fout, ongeldige JSON, ontbrekende verplichte velden en geldig nulresultaat zonder technische bronpayloads of persoonsgegevens aan bezoekers te tonen.

**Acceptatiecriteria**
- Een geldige Open Archieven-respons met nul records wordt uitsluitend als nulresultaat geclassificeerd en niet als bronfout.
- Fixtures voor time-out, niet-succesvolle HTTP-respons, ongeldige JSON en ontbrekende verplichte responsvelden leveren elk een eigen stabiele foutcategorie op.
- De foutcategorie wordt via het bestaande bronstatuscontract beschikbaar gemaakt aan de zoekroute en blijft reproduceerbaar in geautomatiseerde tests.
- Bezoekers zien per foutcategorie een begrijpelijke, niet-technische status; ruwe responsinhoud, stacktraces en onnodige persoonsgegevens worden niet gerenderd of opgeslagen.
- De bestaande stabiele identifiers, oorspronkelijke bronlinks, rechtenstatussen en beschikbare resultaten blijven ongewijzigd wanneer de respons geldig is.

Bronnen: [https://www.openarchieven.nl/api/docs/records/search.php](https://www.openarchieven.nl/api/docs/records/search.php), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt), [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl)

Afhankelijkheden: story:74, story:63 (herkend als bestaande stories: 74, 63)

Risico's: Het externe API-contract kan wijzigen, waardoor fixtures en validatieregels periodiek moeten worden bijgewerkt., De externe bron kan tijdelijk onbereikbaar zijn; tests moeten daarom deterministische fixtures gebruiken naast eventuele integratietests., Een te grove foutnormalisatie kan een geldig nulresultaat ten onrechte als bronstoring classificeren.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
