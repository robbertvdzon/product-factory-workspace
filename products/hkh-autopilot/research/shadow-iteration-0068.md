---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0068
date: 2026-08-14
status: approved
sources:
  - https://hkh-autopilot.vdzonsoftware.nl
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl
  - https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/
  - https://github.com/robbertvdzon/hkh-autopilot
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md
  - https://www.openarchieven.nl/api/docs/records/search.php
  - https://www.openarchieven.nl/api/docs/?lang=en
  - https://pro.europeana.eu/discover-the-data/apis
  - https://pro.europeana.eu/page/the-data-exchange-agreement
  - https://www.collectienederland.nl/zoeken/
  - https://www.collectienederland.nl/search/
  - https://www.europeana.eu/en/stories
---
# Productcyclus 68

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De belangrijkste onbeantwoorde productvraag is hoe HKH bezoekers na een betrouwbare zoekactie van losse bronrecords naar begrijpelijke, controleerbare historische verbanden laat ontdekken. De huidige zoekroute faalt nog volledig bij ‘Heemskerk’, waardoor contextualisering niet beoordeeld kan worden. Publieke voorbeelden laten zien dat filters, kaarten, tijdslijnen, verhalen en expliciete rechteninformatie daarvoor bruikbare patronen zijn.

### Huidig doel en doelgroep

HKH is een brede publieke historische ontdekapp voor iedereen die iets wil weten over Heemskerk. Gebruikers kunnen zoeken vanuit vrije tekst, plek, persoon, gebeurtenis, periode of bron en moeten betrouwbare, herleidbare bronnen in bredere context kunnen ontdekken.

Bronnen: [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md)

### Werkelijke productiestaat

De homepage is bereikbaar en bevat missiecommunicatie, servicebeschikbaarheid, historische zoekingang en een afzonderlijke nieuwssectie. De historische zoekpagina biedt vrije tekst, plek-, persoons- en gebeurtenisfilters, een periodebereik en bronkeuze.

Bronnen: [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl)

### Zoekactie Heemskerk faalt volledig

Een read-only zoekactie op ‘Heemskerk’ toont in productie en acceptatie volledige bronuitval: Europeana is niet geconfigureerd en Open Archieven geeft een onvolledig antwoord. Er zijn geen resultaten, tellingen, identifiers, bronlinks of rechtenstatussen zichtbaar.

Bronnen: [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl)

### Repositorycontract is rijker dan de deployment-uitkomst

De README beschrijft deelbeschikbaarheid, foutcategorieën, stabiele identifiers, originele bronlinks, rechtenstatussen, contextweergave, bronrelaties en vervolgzoeking. Door de actuele bronuitval konden deze functies niet in gebruik worden bevestigd.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md)

### Beheeromgeving publiek zichtbaar

De beheeracceptatie is zonder login bereikbaar en toont nieuws-publicatie en lokale record-intake. Geen formulier is ingevuld of verzonden. Dit blijft een concreet autorisatie- en privacycontrolepunt voordat echte gegevens worden verwerkt.

Bronnen: [https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/)

### Zoek- en filterpatronen bij Collectie Nederland

Collectie Nederland combineert vrije tekst met filters voor dataprovider, collectie, onderwerp, vervaardiger, datum, objectsoort, materiaal, plaatsnaam, techniek en rechten. Dit ondersteunt een gefaseerde verfijning van brede historische zoekvragen.

Bronnen: [https://www.collectienederland.nl/search/](https://www.collectienederland.nl/search/), [https://www.collectienederland.nl/zoeken/](https://www.collectienederland.nl/zoeken/)

### Bronstatus en rechten moeten afzonderlijk blijven

Europeana beschrijft dat metadata onder CC0 wordt gepubliceerd, terwijl ieder digitaal object een afzonderlijke rights statement nodig heeft. Dit ondersteunt HKH’s onderscheid tussen metadatarechten en object- of medierechten.

Bronnen: [https://pro.europeana.eu/page/the-data-exchange-agreement](https://pro.europeana.eu/page/the-data-exchange-agreement), [https://pro.europeana.eu/discover-the-data/apis](https://pro.europeana.eu/discover-the-data/apis)

### Open Archieven biedt een controleerbaar zoekcontract

De officiële API-documentatie beschrijft verplichte naamzoeking, archive_code-filtering, maximaal 100 resultaten, paginering en een response met query, aantal gevonden records en record-identifiers. De algemene documentatie noemt throttling en server-side caching.

Bronnen: [https://www.openarchieven.nl/api/docs/records/search.php](https://www.openarchieven.nl/api/docs/records/search.php), [https://www.openarchieven.nl/api/docs/?lang=en](https://www.openarchieven.nl/api/docs/?lang=en)

### Huidige applicatie

**Doel:** Een brede publieke historische ontdekapp voor Heemskerk, bedoeld voor inwoners, geïnteresseerden, onderzoekers, onderwijs en bezoekers zonder voorafgaande archiefkennis. De app wil lokale bronnen verbinden met historische collecties daarbuiten en zoekers via herleidbare broninformatie laten doorvragen.

**Wat ontbreekt:**
- De kernzoekactie op ‘Heemskerk’ levert momenteel geen historische records op door volledige bronuitval.
- De gebruiker krijgt geen deelresultaten, aantallen, identifiers, originele bronlinks of rechtenstatussen wanneer een bron faalt.
- De actuele foutmelding helpt technisch onderscheid maken, maar biedt geen inhoudelijk alternatief of context om verder te ontdekken.
- De beschreven context-, relatie- en vervolgzoekfuncties konden door bronuitval niet in de gebruikersflow worden beoordeeld.
- De publiek bereikbare beheeromgeving toont muterende formulieren zonder zichtbare login; autorisatie en privacycontrole moeten vóór echte gegevensverwerking worden bevestigd.
- De afzonderlijke nieuwsfunctie is zichtbaar naast historische zoeking, maar vormt volgens de productcontext geen historische bron en moet duidelijk gescheiden blijven.

### Verbetermogelijkheden

- Maak bronresponsvalidatie deterministisch en onderscheid geldig nulresultaat, ongeldige JSON, ontbrekende velden, timeout en HTTP-fout.
- Toon per bron query, ophaalmoment, status, foutcategorie en aantal records; behoud geldige deelresultaten wanneer een andere bron uitvalt.
- Gebruik de Open Archieven-responsevelden stabiele identifier, originele bronlink en beperkte metadata als minimale controleerbare resultaatkaart.
- Houd metadatarechten en object- of medierechten afzonderlijk; onbekende rechten mogen niet als toestemming worden geïnterpreteerd.
- Gebruik een herstelpad met behouden zoekvraag, opnieuw proberen, bronfiltering en een begrijpelijke uitleg van wat wel en niet is geraadpleegd.
- Voeg na herstel een contextlaag toe met plaats, periode, persoon en gebeurtenis, waarbij bronclaims duidelijk gescheiden blijven van door HKH afgeleide verbanden.
- Onderzoek een kaart- of tijdlijnweergave voor zekere plaats- en periodegegevens. De RCE Erfgoedatlas laat zien dat kaartlagen en contextlagen samen historische ontdekking kunnen ondersteunen.
- Gebruik een verhalende laag naast zoeken. Europeana Stories toont hoe losse erfgoedobjecten kunnen worden verbonden in thematische, redactionele verhalen zonder de onderliggende bronrecords te vervangen.

### Inspiratiebronnen

- [Collectie Nederland](https://www.collectienederland.nl/zoeken/) — Inspiratie voor brede zoekingang met filters op plaats, datum, onderwerp, collectie en rechten.
- [Europeana Stories](https://www.europeana.eu/en/stories) — Inspiratie voor het verbinden van afzonderlijke erfgoedrecords tot begrijpelijke thematische verhalen.
- [Historypin](https://about.historypin.org/about/) — Inspiratie voor lokale geschiedenis via verhalen, plaatsen, kaarten en communitycollecties. De API documenteert bovendien plaats- en tijdmetadata als kernvelden: https://historypin.github.io/api-docs/.
- [Erfgoedatlas](https://www.cultureelerfgoed.nl/onderwerpen/b/bronnen-en-kaarten/overzicht/erfgoedatlas) — Inspiratie voor kaartlagen, geografische context en combineren van historische en actuele ruimtelijke informatie.
- [Topotijdreis](https://www.kadaster.nl/-/nieuwe-kaarten-en-luchtfoto-s-op-topotijdreis) — Inspiratie voor tijdreizen door historische kaarten en luchtfoto’s met een tijdsbalk.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://hkh-autopilot.vdzonsoftware.nl) | 2026-08-14 | Publieke webapp; licentie- en hergebruikstatus van applicatie-inhoud is onbekend. | Werkelijk bekeken productiehomepage, zoekflow en read-only zoekactie. |
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl) | 2026-08-14 | Acceptatieomgeving met representatieve nepdata; licentie- en hergebruikstatus is onbekend. | Werkelijk bekeken acceptatiehomepage, zoekflow en read-only zoekactie. |
| [bron](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/) | 2026-08-14 | Publieke beheeromgeving; licentie- en hergebruikstatus is onbekend. | Werkelijk bekeken beheerflow zonder login of mutatie. |
| [bron](https://github.com/robbertvdzon/hkh-autopilot) | 2026-08-14 | Publieke repository; expliciete licentie is op de geraadpleegde repositorypagina niet vastgesteld. | Repositorycontext en publieke productdocumentatie. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md) | 2026-08-14 | Publiek repositorybestand; expliciete licentie is in het geraadpleegde bestand niet vastgesteld. | Bevestigt huidige architectuur, zoekcontract, bronstatussen, rechtenvelden en contextfuncties. |
| [bron](https://www.openarchieven.nl/api/docs/records/search.php) | 2026-08-14 | Openbare API-documentatie; specifieke documentlicentie is niet vermeld op de geraadpleegde pagina. | Primaire bron voor zoekparameters, paging, recordvelden en responscontract. |
| [bron](https://www.openarchieven.nl/api/docs/?lang=en) | 2026-08-14 | Openbare API-documentatie; specifieke documentlicentie is niet vermeld op de geraadpleegde pagina. | Primaire bron voor throttling, caching en gebruiksaanwijzingen. |
| [bron](https://pro.europeana.eu/discover-the-data/apis) | 2026-08-14 | Europeana metadata wordt volgens de pagina onder CC0 aangeboden; digitale objecten hebben afzonderlijke rechtenstatussen. | Primaire bron voor Europeana API’s en rights-aware metadata-ontwerp. |
| [bron](https://pro.europeana.eu/page/the-data-exchange-agreement) | 2026-08-14 | Europeana metadata: CC0 Public Domain Dedication; digitale objecten moeten een afzonderlijke rights statement dragen. | Primaire bron voor scheiding tussen metadatarechten en objectrechten. |
| [bron](https://www.collectienederland.nl/zoeken/) | 2026-08-14 | Rechten- en hergebruiklicentie van de webinterface en gepresenteerde collectiegegevens is op de geraadpleegde pagina niet volledig vastgesteld. | Inspiratie voor gefilterd zoeken en expliciete verfijning van brede collectiequeries. |
| [bron](https://www.collectienederland.nl/search/) | 2026-08-14 | Rechten- en hergebruiklicentie van de webinterface en gepresenteerde collectiegegevens is op de geraadpleegde pagina niet volledig vastgesteld. | Werkelijke zoekinterface met filters waaronder plaatsnaam en rechten. |
| [bron](https://www.europeana.eu/en/stories) | 2026-08-14 | Europeana-pagina; rechten verschillen per verhaal en onderliggende objecten, met licentie-informatie per object waar beschikbaar. | Inspiratie voor redactionele historische verhalen naast recordzoeking. |

## Productbeslissing

Herstel eerst de betrouwbare Open Archieven-zoek-MVP voor de zoekvraag ‘Heemskerk’: valideer bronantwoorden deterministisch, toon geldige deelresultaten als controleerbare resultaatkaarten en geef per bron een begrijpelijke status met herstelactie.

**Waarom:** De kernzoekactie levert momenteel geen historische records op door bronuitval, waardoor de missie van verbonden en herleidbare ontdekking niet wordt bereikt. Open Archieven heeft een gedocumenteerd zoek- en responscontract met identifiers, aantallen en recordvelden. Deze kleine richting herstelt eerst de betrouwbare basis voor verdere context, relaties en vervolgzoeking. De scope blijft beperkt tot Open Archieven, zodat uitvoering toetsbaar is zonder onbewezen historische verbanden of extra redactionele complexiteit.

### Prioriteiten
- Maak bronresponsvalidatie deterministisch voor geldig resultaat, geldig nulresultaat, ongeldige JSON, ontbrekende velden, timeout en HTTP-fout.
- Behoud en toon geldige Open Archieven-deelresultaten wanneer een andere bron uitvalt.
- Toon per zoekactie de bron, query, ophaalmoment, status en aantal gevonden records.
- Toon per record minimaal een stabiele identifier, beperkte bronmetadata en een permanente originele bronlink.
- Maak rechtenstatus en metadatarechten afzonderlijk zichtbaar; onbekende rechten worden niet als toestemming geïnterpreteerd, maar blokkeren alleen publicatie van het betreffende object of medium wanneer dat materieel relevant is.

### Besluiten
- **Gebruik Open Archieven als enige externe bron in deze uitvoeringsslice.** — De roadmap benoemt Open Archieven als eerste bron en de officiële documentatie beschrijft een concreet zoekcontract zonder API-key als noodzakelijke voorwaarde.
- **Maak bronstatus en foutcategorie onderdeel van de gebruikersuitkomst, naast eventuele records.** — De huidige productie- en acceptatiezoekactie toont volledige bronuitval zonder resultaten of bronmetadata. Een expliciete status maakt zichtbaar wat wel en niet is geraadpleegd en ondersteunt herstel zonder de zoekvraag kwijt te raken.
- **Publiceer alleen controleerbare recordmetadata en originele bronlinks; voeg in deze slice geen afgeleide relaties, kaart, tijdlijn of verhaal toe.** — De missie vereist herleidbaarheid en betrouwbaarheid. Afgeleide context is pas verantwoord nadat de basiszoeking stabiel resultaten en bronmetadata levert; de repository beschrijft daarvoor al een latere context- en vervolgzoekrichting.
- **Scheid metadatarechten van rechten op digitale objecten of media.** — De Europeana-documentatie laat zien dat metadata en digitale objecten afzonderlijke rechtenstatussen kunnen hebben. Dit voorkomt dat beschikbare metadata ten onrechte als toestemming voor hergebruik van objecten wordt behandeld.

## UX-voorstel: Betrouwbaar zoeken naar Heemskerk via Open Archieven

**Gebruikersdoel:** De gebruiker zoekt op ‘Heemskerk’ en kan geldige historische records controleren, herleiden naar de oorspronkelijke bron en begrijpen welke broninformatie wel of niet beschikbaar is.

### Flow
1. Open Historisch zoeken.
2. Vul ‘Heemskerk’ in als zoekterm en start de zoekactie.
3. Toon de behouden zoekvraag, ophaaltijdstip en Open Archieven-bronstatus.
4. Valideer het bronantwoord deterministisch en toon geldige records als resultaatkaarten.
5. Toon per kaart een stabiele identifier, beperkte metadata, periode of plaats indien beschikbaar en een permanente originele bronlink.
6. Toon rechteninformatie afzonderlijk voor metadata en digitale objecten; markeer onbekende rechten expliciet.
7. Bij nulresultaten of een bronfout: toon de foutcategorie in begrijpelijke taal, behoud de zoekterm en bied ‘Opnieuw proberen’ en ‘Alleen deze bron proberen’.
8. Laat de gebruiker een resultaatkaart openen in een detailweergave met bronverantwoording; voeg in deze MVP geen afgeleide historische verbanden toe.

### Wireframe

[Header]
HKH — Historisch zoeken

[Zoekformulier]
Zoekterm: [ Heemskerk                         ]
[Zoeken]

[Samenvatting]
Zoekvraag: Heemskerk
Bron geraadpleegd: Open Archieven
Ophaaltijdstip: 14 augustus 2026, 10:32
Status: Gedeeltelijk beschikbaar
Gevonden: 12 records

[Bronstatus]
Open Archieven — 12 resultaten — Beschikbaar
  Query: Heemskerk
  [Broninformatie]
Andere bronnen — Niet geraadpleegd in deze MVP

[Resultaten]
Resultaat 1
  Titel/naam: …
  Periode: …
  Plaats: …
  Identifier: OA-…
  Metadatarechten: …
  Objectrechten: Onbekend / niet van toepassing
  [Bekijk oorspronkelijke bron]

[Resultaat 2]
…

[Bij bronfout]
Open Archieven kon niet betrouwbaar worden gelezen.
Categorie: Timeout / HTTP-fout / ongeldig antwoord / ontbrekend veld
Uw zoekvraag is bewaard.
[Opnieuw proberen] [Bronstatus bekijken]

[Footer]
Bronverantwoording · Rechtenuitleg · Privacy

### Interactiehypotheses
- Als gebruikers per bron een duidelijke status, query, ophaaltijdstip en aantal resultaten zien, kunnen zij beter beoordelen wat de zoekactie daadwerkelijk heeft opgeleverd.
- Als geldige deelresultaten zichtbaar blijven wanneer een bron faalt, kunnen gebruikers historische informatie blijven ontdekken zonder een volledige foutmelding als eindpunt te ervaren.
- Als iedere resultaatkaart een stabiele identifier en originele bronlink toont, kunnen gebruikers records zelfstandig controleren en terugvinden.
- Als metadatarechten en rechten op digitale objecten afzonderlijk worden weergegeven, zullen gebruikers minder snel beschikbare metadata verwarren met toestemming voor mediagebruik.
- Als de zoekterm behouden blijft bij fouten en opnieuw proberen één duidelijke actie is, kunnen gebruikers sneller herstellen zonder hun zoekcontext opnieuw in te voeren.
- Automatisch testbaar: simuleer geldige resultaten, nulresultaat, ongeldige JSON, ontbrekende velden, timeout en HTTP-fout en controleer statuslabel, foutcategorie, behouden query en resultaatweergave.

### Toegankelijkheid
- Gebruik semantische headings, landmarks, labels en een echte form-submitactie.
- Maak alle functies volledig toetsenbordbedienbaar met zichtbare focusindicatoren en logische tabvolgorde.
- Kondig laadstatus, bronstatus en foutmeldingen aan via een geschikt live region zonder focus onverwacht te verplaatsen.
- Gebruik tekst naast kleur voor statussen; voldoe aan voldoende contrast voor tekst, links, knoppen en focus.
- Geef links duidelijke namen, bijvoorbeeld ‘Bekijk oorspronkelijke bron voor record OA-…’, en open geen nieuwe context zonder waarschuwing.
- Maak resultaatkaarten lineair leesbaar met een consistente headingstructuur.
- Ondersteun zoom en smalle schermen zonder horizontaal scrollen of verlies van informatie.
- Toon datum, periode en onbekende waarden in begrijpelijke tekst; gebruik geen uitsluitend visuele iconen.

### Privacy
- Bewaar alleen de zoekterm tijdelijk voor herstel binnen dezelfde sessie, tenzij een expliciet doel en grondslag voor langere opslag bestaat.
- Sla geen persoonsgegevens, zoekgeschiedenis of gebruikersprofielen op voor deze MVP.
- Beperk doorgifte aan Open Archieven tot noodzakelijke zoekparameters; documenteer doel, bewaartermijn en eventuele logging.
- Redigeer technische logs zodat volledige zoekvragen of persoonsnamen niet onnodig langdurig worden opgeslagen.
- Toon bronmetadata alleen voor het doel van historische ontdekking en herleidbaarheid; interpreteer onbekende rechten niet als toestemming voor publicatie of hergebruik.
- Neem geen beheer-, intake- of publicatiefunctie op in deze gebruikersflow; daarvoor zijn afzonderlijke authenticatie-, autorisatie- en privacycontroles vereist.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is klein, privacygericht en volledig geautomatiseerd toetsbaar. Er is geen materieel blokkadepunt.
- **WARNING · PRIVACY** — Inventariseer ook bestaande logging buiten de Open Archieven-adapter, zodat zoektermen of bronpayloads niet via middleware, tracing of foutafhandeling alsnog worden vastgelegd.
- **INFO · CONSISTENCY** — De kandidaat overlapt functioneel met de reeds gepubliceerde foutdiagnose in story:75, maar voegt operationele logging toe en is daarom geen exact duplicaat.

## Geaccepteerde storykandidaten

### Privacyveilige operationele logging voor Open Archieven-zoekacties

_Sleutel: `privacyveilige-bronfetch-logging`_

Als beheerbare historische zoekdienst wil ik dat Open Archieven-ophaalacties diagnostische statusinformatie opleveren zonder zoektermen, persoonsnamen of ruwe bronpayloads langdurig te loggen, zodat bronbeschikbaarheid en foutcategorieën kunnen worden onderzocht zonder onnodige persoonsgegevens of zoekgeschiedenis vast te leggen.

**Acceptatiecriteria**
- Elke Open Archieven-ophaalactie registreert uitsluitend bron, technische uitkomstcategorie, duur, HTTP-statusklasse en aantal verwerkte resultaten wanneer beschikbaar.
- Zoektermen, persoonsnamen, volledige queryparameters, response-body’s en stabiele recordpayloads worden niet in applicatie- of foutlogs opgeslagen.
- De logging werkt voor geldig resultaat, geldig nulresultaat, timeout, HTTP-fout, ongeldige JSON en ontbrekende verplichte velden.
- Geautomatiseerde tests bewijzen dat voorbeeldzoektermen zoals ‘Heemskerk’ en persoonsnamen niet herkenbaar in loguitvoer voorkomen.
- De logging verandert de publieke zoekuitkomst niet en introduceert geen opslag van zoekgeschiedenis of gebruikersprofielen.
- Bij ontbrekende of tegenstrijdige broninformatie blijft de logging fail-closed en wordt geen gevoelige fallback-inhoud toegevoegd.

Bronnen: [https://www.openarchieven.nl/api/docs/records/search.php](https://www.openarchieven.nl/api/docs/records/search.php), [https://www.openarchieven.nl/api/docs/?lang=en](https://www.openarchieven.nl/api/docs/?lang=en), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md), [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl)

Afhankelijkheden: story:75 (herkend als bestaande stories: 75)

Risico's: Te weinig operationele context kan foutanalyse bemoeilijken; daarom blijven niet-herleidbare categorieën, timing en aantallen beschikbaar., Bestaande logging buiten de Open Archieven-adapter kan alsnog zoektermen bevatten en moet binnen deze scope worden geïnventariseerd of afgeschermd., Logretentie en toegangsbeheer vallen buiten deze story wanneer zij niet door de applicatie worden beheerd.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
