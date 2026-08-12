---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0056
date: 2026-08-12
status: approved
sources:
  - https://github.com/robbertvdzon/hkh-autopilot
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/main.dart
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/news/discover_section.dart
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/records/record_detail_page.dart
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend-admin/lib/main.dart
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl
  - https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl
  - https://www.openarchieven.nl/api/docs/
  - https://www.openarchieven.nl/datasets/nha
  - https://opendata.archieven.nl/nl/over-open-data
  - https://www.europeana.eu/en/about-us
---
# Productcyclus 56

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De belangrijkste onbeantwoorde productvraag is hoe de huidige, nieuwsgerichte bezoekersingang kan uitgroeien tot betrouwbare historische ontdekking met externe bronnen, bronverwijzingen en veilige rechten-/privacyweergave. De repository bevat al afzonderlijke bouwstenen voor nieuws, recorddetails, externe bronverificatie en beheer, maar geen voltooide bezoekersroute naar externe historische zoekresultaten. De acceptatieomgeving kon in deze runtime niet visueel worden beoordeeld omdat Chromium door sandbox-permissies niet startte.

### De publieke homepage ontsluit momenteel nieuws, geen historische collecties

De Flutter-homepage controleert eerst de service en toont daarna productvisie, laatste nieuws en een zoekblok dat uitsluitend GET /api/news doorzoekt. De zoekfunctie gebruikt deterministische labels voor plek, persoon en gebeurtenis binnen nieuwsberichten; dit zijn geen historische externe bronnen.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/main.dart), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/news/discover_section.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/news/discover_section.dart), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md)

### Externe bronverificatie bestaat vooral als gekoppelde recorddetailfunctie

De publieke recorddetailcode kan bij een bevestigd record naam, geboortejaar, sterftejaar, licentie en externe bronlink tonen. De code documenteert expliciet dat deze functie niet gekoppeld is aan de homepage-nieuwszoekfunctie en geen historische zoekresultaten levert.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/records/record_detail_page.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/records/record_detail_page.dart), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md)

### De beheerkant ondersteunt intake en verificatie, maar geen volledige publicatieflow

De admin-app bevat authenticatie, nieuwsbeheer, recordintake en externe verificatie. De functionele specificatie beschrijft de intake als intern concept en vermeldt opslag, REST-publicatie, beheerinterface en daadwerkelijke publicatie van het koppelingsdossier als buiten scope. Daardoor ontbreekt een aantoonbare, volledige route van externe bronzoekresultaat naar publiek bezoekersresultaat.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend-admin/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend-admin/lib/main.dart), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md)

### Open Archieven levert een concreet technisch startpunt voor bronontsluiting

De Open Archieven-documentatie beschrijft zoek-, match-, recorddetail-, transcriptie- en OAI-PMH-mogelijkheden. De API is per IP begrensd op vier verzoeken per seconde en vraagt om een beschrijvende user-agent. De datasetpagina voor Noord-Hollands Archief vermeldt miljoenen historische documentmetadata en persoonsvermeldingen, met OAI-PMH/A2A-toegang en CC0 1.0 voor de genoemde datasetdistributies. Dit maakt brondekking technisch haalbaar, maar rechten van afzonderlijke objecten en media moeten zichtbaar onderscheiden blijven van datasetmetadata.

Bronnen: [https://www.openarchieven.nl/api/docs/](https://www.openarchieven.nl/api/docs/), [https://www.openarchieven.nl/datasets/nha](https://www.openarchieven.nl/datasets/nha), [https://opendata.archieven.nl/nl/over-open-data](https://opendata.archieven.nl/nl/over-open-data)

### De broninfrastructuur is momentopname- en licentiegevoelig

Opendata.archieven.nl beschrijft resolvable URI’s, content negotiation en periodiek gegenereerde open datasets; een dataset is een momentopname die later wezenlijk kan wijzigen. Dit ondersteunt de behoefte aan stabiele bronidentificatie, opgehaalde-versie/datum en een expliciete onbekende rechtenstatus wanneer broninformatie ontbreekt.

Bronnen: [https://opendata.archieven.nl/nl/over-open-data](https://opendata.archieven.nl/nl/over-open-data), [https://www.openarchieven.nl/api/docs/](https://www.openarchieven.nl/api/docs/)

### De acceptatieomgeving kon niet betrouwbaar worden bekeken

De voorgeschreven Playwright-screenshotcontrole is uitgevoerd met de beschikbare headless Chromium en lokaal geïnstalleerde Chrome, maar beide browsers stopten vóór navigatie door runtime-permissiefouten. Er is daarom geen betrouwbare visuele uitspraak mogelijk over bruikbaarheid, duidelijkheid of doorklikgedrag van de actuele bezoekers- en admin-UI.

Bronnen: [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl), [https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl)

### Huidige applicatie

**Doel:** Historisch Heemskerk is bedoeld voor een brede doelgroep: iedereen die vanuit een gewone vraag, plek, persoon, gebeurtenis of onderwerp de geschiedenis van Heemskerk en de bredere historische context wil ontdekken. De repository positioneert het product als een betrouwbare, verbonden en herbruikbare historische kenniswereld, niet als uitsluitend traditioneel digitaal archief.

**Wat ontbreekt:**
- De publieke homepage zoekt alleen in gepubliceerd admin-nieuws; externe historische collecties zijn daar niet als bezoekersroute ontsloten.
- De bestaande externe bronverificatie is gekoppeld aan afzonderlijke recorddetails en levert geen algemene externe zoek- of ontdekkingsroute vanaf de homepage.
- De specificatie beschrijft wel validatie- en intakecontracten, maar opslag, daadwerkelijke publicatie en een volledige curatoriële publicatieflow zijn buiten scope.
- Broncontracten voor een bezoekerszoekroute zijn nog niet concreet genoeg vastgelegd per bron: zoekvelden, normalisatie, pagination, rate limits, foutgedrag, bronversie en rechten-/privacyvelden.
- De rechtenstatus van metadata, media en afzonderlijke objecten is niet overal hetzelfde; datasetlicentie kan niet zonder meer als objectlicentie worden gebruikt.
- De actuele acceptatie-UI, bruikbaarheid en navigatie konden in deze runtime niet visueel worden geverifieerd door een Chromium-startfout.
- De publieke repository bevat geen aangetroffen standaardlicentiebestand, waardoor hergebruik van repositorycode juridisch onduidelijk blijft.

### Verbetermogelijkheden

- Ontwerp een bezoekersgerichte historische zoekroute die duidelijk gescheiden blijft van admin-nieuws en resultaten rechtstreeks terugleidt naar stabiele externe bronrecords.
- Gebruik per bron een expliciet adaptercontract met bronhouder, stabiele identifier, titel/beschrijving, datering en onzekerheid, metadatarechten, objectrechten, privacystatus, bronversie, requestlimieten en fail-closed foutgedrag.
- Toon bij onduidelijke rechten of privacy alleen de minimaal noodzakelijke herleidbare metadata en een externe bronlink; kopieer geen media zolang objectrechten niet afzonderlijk duidelijk zijn.
- Maak bronstatus zichtbaar en begrijpelijk: geverifieerd, tijdelijk niet bereikbaar, geen match, rechten onbekend of privacy beperkt, met onderscheid tussen bronmetadata en objectmedia.
- Leg de overgang vast tussen externe zoekresultaten, het bestaande publieke recorddetailcontract en eventuele beheer-/curatiecontrole, zodat bezoekers niet in een doodlopend verificatiepad terechtkomen.
- Onderzoek plaatsgerichte navigatie als aanvullende ontdeklaag: historische kaarten en tijdvergelijking kunnen een Heemskerkse plek begrijpelijk maken zonder dat de gebruiker archiefterminologie kent.
- Herhaal de visuele acceptatiebeoordeling in een browserruntime die headless Chromium kan starten en test expliciet zoekroute, bronlink, terugnavigatie, lege resultaten, foutstatussen en toegankelijkheid.

### Inspiratiebronnen

- [Europeana](https://www.europeana.eu/en/about-us) — Toont hoe collecties van duizenden archieven, bibliotheken, musea en andere instellingen via aggregatie, verrijkte metadata, geolocatie en relaties tussen personen, plaatsen en onderwerpen als één brede ontdekomgeving kunnen worden aangeboden.
- [Topotijdreis](https://www.cultureelerfgoed.nl/onderwerpen/b/bronnen-en-kaarten/overzicht/topotijdreis) — Biedt een laagdrempelige tijdreis door historische Nederlandse kaarten van 1815 tot 2015 en laat zien hoe plekgerichte tijdvergelijking geschiedenis beleefbaar kan maken voor zowel professionals als algemeen publiek.
- [Geheugen van Nederland](https://dutchculture.nl/en/location/memory-netherlands) — Combineert collecties van meer dan honderd Nederlandse musea, archieven en bibliotheken met zowel vrij rondkijken als zoeken op onderwerp; relevant voor een brede, nieuwsgierigheidsgedreven toegang tot historische objecten.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://github.com/robbertvdzon/hkh-autopilot) | 2026-08-12 | Publieke GitHub-repository; er is geen LICENSE-, LICENSE.md- of COPYING-bestand aangetroffen, waardoor de licentie voor repository-inhoud onbekend blijft. | Aangewezen publieke repository voor productcode en documentatie. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/main.dart) | 2026-08-12 | Publieke broncode; repository bevat geen aangetroffen expliciete licentie, dus hergebruikstatus onbekend. | Bevestigt de huidige publieke Flutter-homepage-opbouw. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/news/discover_section.dart) | 2026-08-12 | Publieke broncode; expliciete repositorylicentie niet aangetroffen. | Bevestigt dat de ontdekfunctie uitsluitend nieuws en nieuwslabels doorzoekt. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/records/record_detail_page.dart) | 2026-08-12 | Publieke broncode; expliciete repositorylicentie niet aangetroffen. | Bevestigt de bestaande publieke recorddetail- en externe bronverificatiesectie. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend-admin/lib/main.dart) | 2026-08-12 | Publieke broncode; expliciete repositorylicentie niet aangetroffen. | Bevestigt de adminfuncties en authenticatie-opzet. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md) | 2026-08-12 | Publieke technische documentatie; expliciete repositorylicentie niet aangetroffen. | Bevat de contracten, scopegrenzen en publicatiebeperkingen. |
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl) | 2026-08-12 | Publieke acceptatieomgeving met representatieve dummydata; rechten/licentie van UI en dummydata onbekend. | Aangewezen bezoekersomgeving; visuele toegang mislukte door browser-runtimefout. |
| [bron](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl) | 2026-08-12 | Publieke acceptatieomgeving met representatieve dummydata; rechten/licentie van UI en dummydata onbekend. | Aangewezen beheergedeelte; visuele toegang mislukte door browser-runtimefout. |
| [bron](https://www.openarchieven.nl/api/docs/) | 2026-08-12 | Publieke API-documentatie; op de geraadpleegde pagina geen expliciete documentatielicentie gevonden. | Levert actuele zoek-, record-, transcriptie-, OAI-PMH- en rate-limitinformatie. |
| [bron](https://www.openarchieven.nl/datasets/nha) | 2026-08-12 | De datasetpagina vermeldt CC0 1.0 voor de genoemde N-triples- en XML-distributies; rechten op afzonderlijke objecten/media zijn daarmee niet automatisch vastgesteld. | Concrete bron voor omvang, structuur, toegang en licentie-indicatie van Noord-Hollands Archief-metadata. |
| [bron](https://opendata.archieven.nl/nl/over-open-data) | 2026-08-12 | Publieke uitlegpagina van archieven.nl; algemene rechten op de documentatietekst zelf niet expliciet vastgesteld. | Bevestigt resolvable URI’s, content negotiation en momentopnamekarakter van datasets. |
| [bron](https://www.europeana.eu/en/about-us) | 2026-08-12 | Europeana is publiek toegankelijk; rechten en hergebruikvoorwaarden verschillen per object en aanbieder en moeten per item worden gecontroleerd. | Vergelijkbare brede erfgoedaggregator die collecties van archieven, musea en bibliotheken verbindt. |

## Productbeslissing

Bouw één beperkte publieke historische zoekroute vanaf de homepage voor Heemskerk-gerelateerde resultaten uit Open Archieven/Noord-Hollands Archief. Toon uitsluitend herleidbare metadata en een stabiele externe bronlink; kopieer geen media. Maak bronstatus, rechtenstatus en eventuele privacybeperking begrijpelijk zichtbaar en laat elk resultaat veilig doorlinken naar een publiek recorddetail of de externe bron.

**Waarom:** Dit sluit direct aan op missie en roadmapthema hkh-autopilot-0002: bezoekers kunnen vanuit een gewone vraag historische bronnen buiten de lokale collectie ontdekken. Het benut de bestaande homepage, recorddetail- en verificatiebouwstenen, terwijl het huidige doodlopende onderscheid tussen nieuwszoeken en historische bronontsluiting wordt opgelost. Open Archieven biedt een concreet technisch startpunt voor Noord-Hollands Archief-metadata, maar het momentopnamekarakter van datasets en het onderscheid tussen metadatarechten en objectrechten vereisen expliciete bronversie-, rechten- en privacyvelden. Bij onduidelijke rechten of privacy blijft de route beperkt tot minimale metadata en een externe link.

### Prioriteiten
- Definieer één adaptercontract voor Open Archieven/Noord-Hollands Archief met zoekterm, stabiele identifier, titel, beschrijving, datering, bronhouder, bronversie, opgehaaldatum, pagination, rate limiting en foutgedrag.
- Voeg op de homepage een duidelijk van admin-nieuws gescheiden historische zoekingang toe, met eenvoudige zoektaal en resultaten voor plek, persoon, gebeurtenis en onderwerp.
- Toon per resultaat begrijpelijke statussen zoals geverifieerd, tijdelijk niet bereikbaar, geen match, rechten onbekend of privacy beperkt.
- Publiceer alleen minimale herleidbare metadata en stabiele externe bronlinks; sluit lokale media en gevoelige persoonsgegevens uit zolang rechten of privacy niet aantoonbaar veilig zijn.
- Leg terugnavigatie en de overgang naar het bestaande publieke recorddetailcontract vast, inclusief lege resultaten en tijdelijke bronfouten.

### Besluiten
- **Kies Open Archieven met Noord-Hollands Archief als eerste externe bronadapter.** — De bron biedt gedocumenteerde zoek- en recordmogelijkheden, OAI-PMH/A2A-toegang en een concrete Noord-Hollandse dataset met omvangrijke historische metadata.
- **Maak historische zoekresultaten een zelfstandige bezoekersroute en houd ze gescheiden van nieuws.** — De huidige homepage zoekt uitsluitend in admin-nieuws, terwijl nieuws geen historische bron is. De bestaande recorddetailfunctie is niet aan een algemene zoekroute gekoppeld.
- **Gebruik een metadata-eerst, fail-closed publicatiemodel.** — Datasetmetadata kan CC0 zijn zonder dat afzonderlijke objecten of media dezelfde rechten hebben. Bij onbekende rechten of privacy worden daarom alleen minimale metadata en een externe bronlink getoond.
- **Neem bronversie en opgehaaldatum op in het resultaat- en adaptercontract.** — Open datasets zijn momentopnames die later wezenlijk kunnen wijzigen; stabiele identificatie en tijdgebonden bronstatus zijn daarom nodig voor betrouwbaarheid en herleidbaarheid.

## UX-voorstel: Publieke historische zoekroute Heemskerk

**Gebruikersdoel:** Als bezoeker wil ik met een gewone zoekterm historische Heemskerk-gerelateerde bronnen vinden, de herkomst en status ervan begrijpen en veilig doorklikken naar het publieke record of de externe bron.

### Flow
1. Bezoeker kiest op de homepage de zelfstandige ingang “Historische bronnen zoeken”.
2. Bezoeker voert een zoekterm in, bijvoorbeeld een plek, persoon, gebeurtenis of onderwerp.
3. Het systeem toont resultaten uit Open Archieven/Noord-Hollands Archief met titel, datering, bronhouder, stabiele identifier en begrijpelijke bronstatus.
4. Bezoeker opent een resultaatdetail met minimale metadata, bronversie, opgehaaldatum, rechtenstatus en eventuele privacybeperking.
5. Bezoeker kiest “Bekijk publieke bron” om naar het bestaande publieke recorddetail of de externe bron te gaan.
6. Bij geen resultaten, tijdelijke bronuitval, onbekende rechten of beperkte privacy krijgt de bezoeker een duidelijke status en veilige vervolgstap.

### Wireframe

[Header]
Historisch Heemskerk | Nieuws | Historische bronnen zoeken

[Intro]
Ontdek historische bronnen over Heemskerk
Zoek op plek, persoon, gebeurtenis of onderwerp.

[Zoekformulier]
[ Zoekterm                                   ] [Zoeken]
Voorbeeld: “Kerkplein”, “1944” of “familie Van Velsen”

[Resultaatpagina]
Historische bronnen voor: Kerkplein
12 resultaten | [Nieuwe zoekopdracht]

[Resultaatkaart]
Titel van de bron
Datering: 1890–1900
Bronhouder: Noord-Hollands Archief
Status: Geverifieerde metadata
Rechten: Rechten op object/media onbekend
[Details bekijken] [Bekijk publieke bron]

[Detailpagina]
← Terug naar resultaten
Titel van de bron
Beschrijving en datering
Bronhouder + stabiele identifier
Bronversie + opgehaaldatum
Privacystatus: Geen beperkte gegevens getoond
Rechtenstatus: Metadata beschikbaar; objectrechten niet vastgesteld
[Open externe bron]

[Alternatieve staten]
Geen resultaten: probeer een andere zoekterm.
Bron tijdelijk niet bereikbaar: probeer later opnieuw.
Privacy beperkt: alleen minimale metadata beschikbaar.

### Interactiehypotheses
- Minstens 70% van geautomatiseerde scenario’s met een zoekterm leidt binnen twee interacties tot een resultaatlijst of een expliciete foutstatus.
- Een zelfstandige historische zoekingang veroorzaakt minder verwarring tussen nieuws en historische bronnen dan één gecombineerd zoekveld; dit wordt getoetst met navigatie- en labelasserties in browserautomatisering.
- Elk gepubliceerd resultaat bevat een stabiele identifier, bronhouder, bronstatus, rechtenstatus en opgehaaldatum; ontbrekende velden blokkeren publicatie.
- Bij onbekende rechten worden geen media of volledige objectteksten getoond; geautomatiseerde privacy- en payloadtests controleren dit.
- Bij bronuitval blijft de bestaande pagina bruikbaar en verschijnt een niet-misleidende foutstatus zonder gedeeltelijk of verouderd resultaat als actueel te presenteren.
- De terugknop bewaart zoekterm en paginastaat, zodat bezoekers vanuit detail veilig terugkeren naar dezelfde resultatenlijst.

### Toegankelijkheid
- Alle functies zijn bereikbaar met toetsenbord en hebben zichtbare focusstijlen.
- Gebruik semantische headings, landmarks, labels en knoppen die door schermlezers begrijpelijk worden aangekondigd.
- Resultaatkaarten zijn geen volledig klikbare containers; acties hebben afzonderlijke, beschrijvende linkteksten.
- Dynamische laad-, fout- en resultaatmeldingen worden via een geschikt live region aangekondigd.
- Gebruik voldoende kleurcontrast en toon status niet uitsluitend met kleur; combineer kleur met tekst en eventueel een icoon.
- Formuliervalidatie benoemt het probleem programmatisch en geeft focus terug naar het relevante veld.
- De route werkt bij vergroting en kleine schermbreedte zonder horizontaal scrollen of verlies van informatie.

### Privacy
- Verwerk alleen de zoekterm en noodzakelijke technische gegevens voor bronopvraging; sla zoektermen standaard niet op.
- Toon alleen minimale herleidbare metadata die nodig is om de bron te begrijpen.
- Onderdruk gevoelige persoonsgegevens en gegevens van mogelijk levende personen wanneer privacystatus niet aantoonbaar veilig is.
- Kopieer geen media of volledige objectinhoud zolang rechten of privacy niet afzonderlijk zijn vastgesteld.
- Maak per resultaat onderscheid tussen metadatarechten en rechten op object/media.
- Toon privacybeperkingen begrijpelijk zonder verborgen persoonsgegevens in foutmeldingen, URL’s, analytics of logs te plaatsen.
- Gebruik stabiele bronidentifiers en bronlinks voor herleidbaarheid, maar vermijd onnodige lokale profielen, tracking en accountverplichting.
- Documenteer doel, bewaartermijn en grondslag wanneer technische logging of rate-limitmonitoring persoonsgegevens kan bevatten.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is klein, toetsbaar en volledig geautomatiseerd uitvoerbaar. Er is geen materieel probleem dat levering blokkeert.
- **WARNING · PRIVACY** — De regel voor mogelijk levende personen en ‘minimale niet-herleidbare metadata’ blijft deels afhankelijk van bestaande classificatielogica; leg de exacte redactiegrenzen en de behandeling van bronlinks in het contract vast.
- **WARNING · RIGHTS** — Het contract onderscheidt rechtenstatus correct, maar een onbekende rechtenstatus kan nog steeds operationeel onduidelijk zijn. Leg vast welke metadata minimaal publiek mag blijven en dat media/objectinhoud altijd uitgesloten blijft.
- **WARNING · SCOPE** — De rate-limit-eis ‘per IP’ kan bij proxy- of server-side adapters anders uitpakken dan bij directe clients. Documenteer waar de beperking wordt afgedwongen en test dat gedrag.
- **INFO · CONSISTENCY** — Er is inhoudelijke overlap met de eerder afgewezen kandidaat 59, maar deze kandidaat beperkt zich tot het herkomst- en statuscontract en is daarom geen exact duplicaat.

## Geaccepteerde storykandidaten

### Herkomst- en statuscontract voor externe historische bronresultaten

_Sleutel: `bronstatus-herkomstcontract`_

Definieer en implementeer één geautomatiseerd, metadata-only contract waarmee toekomstige publieke historische zoekresultaten hun stabiele bronidentifier, bronhouder, bronversie, opgehaaldatum, rechtenstatus, privacystatus en technische beschikbaarheidsstatus uniform vastleggen. Het contract ondersteunt Open Archieven/Noord-Hollands Archief, respecteert de API-rate-limit en presenteert ontbrekende of tegenstrijdige broninformatie fail-closed zonder media of volledige objectinhoud op te nemen.

**Acceptatiecriteria**
- Het contract valideert per resultaat minimaal stabiele bronidentifier, bronhouder, titel of beschrijving, datering, bronversie of momentopname-identificatie, opgehaaldatum, rechtenstatus, privacystatus en beschikbaarheidsstatus.
- Ontbreekt een verplicht herkomst- of statusveld, of is de waarde tegenstrijdig, dan wordt het resultaat niet als volledig geverifieerd gemarkeerd en blijft alleen een veilige minimale status beschikbaar.
- Het contract bevat geen lokale media, volledige objectinhoud of gevoelige persoonsgegevens; geautomatiseerde payloadtests falen wanneer zulke velden toch worden opgenomen.
- Wanneer een persoon mogelijk leeft, of persoonsgegevens zonder aantoonbaar passende grondslag worden aangetroffen, redigeert het systeem deze gegevens fail-closed uit publieke metadataresultaten en logs; uitsluitend minimale niet-herleidbare metadata en de stabiele bronlink blijven beschikbaar.
- De adapter begrenst uitgaande verzoeken tot maximaal vier verzoeken per seconde per IP en gebruikt een beschrijvende user-agent.
- Geautomatiseerde tests dekken minimaal geldige metadata, onbekende rechten, privacybeperking, tijdelijke bronuitval, lege bronrespons en gewijzigde bronversie.
- Geautomatiseerde privacy- en loggingtests bevestigen dat gegevens van mogelijk levende personen en persoonsgegevens zonder aantoonbare grondslag niet in publieke metadataresultaten of logs terechtkomen.
- De contractdocumentatie maakt expliciet onderscheid tussen rechten op datasetmetadata en rechten op afzonderlijke objecten of media.

Bronnen: [https://www.openarchieven.nl/api/docs/](https://www.openarchieven.nl/api/docs/), [https://www.openarchieven.nl/datasets/nha](https://www.openarchieven.nl/datasets/nha), [https://opendata.archieven.nl/nl/over-open-data](https://opendata.archieven.nl/nl/over-open-data), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md)

Afhankelijkheden: story:18 (herkend als bestaande stories: 18)

Risico's: De externe bron kan schema’s, identifiers of beschikbaarheid wijzigen; versie- en foutafhandeling moet daarom strikt fail-closed blijven., Een datasetlicentie kan ten onrechte als licentie voor afzonderlijke objecten of media worden geïnterpreteerd., Rate limiting of tijdelijke bronuitval kan zoekresultaten vertragen of onvolledig maken.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
