---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0069
date: 2026-08-14
status: approved
sources:
  - https://github.com/robbertvdzon/hkh-autopilot
  - https://hkh-autopilot.vdzonsoftware.nl
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl
  - https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/
  - https://www.openarchieven.nl/api/docs/?lang=en
  - https://api.europeana.eu/en
  - https://europeana.atlassian.net/wiki/spaces/EF/pages/2385739812/Search%2BAPI%2BDocumentation?redirectedFromRestrict=true
  - https://www.collectienederland.nl/zoeken/
  - https://about.historypin.org/about/
  - https://historypin.github.io/api-docs/
---
# Productcyclus 69

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De belangrijkste onbeantwoorde productvraag is hoe HKH een eerste zoekresultaat controleerbaar en bruikbaar maakt wanneer bronnen gedeeltelijk of volledig falen. De huidige zoekflow biedt goede ingangen, maar levert bij ‘Heemskerk’ geen records, aantallen, bronmetadata of rechteninformatie.

### Huidig doel

HKH is een brede publieke historische ontdekapp die mensen via vragen, plekken, personen en gebeurtenissen toegang wil geven tot de geschiedenis van Heemskerk en verbonden externe bronnen.

Bronnen: [https://github.com/robbertvdzon/hkh-autopilot](https://github.com/robbertvdzon/hkh-autopilot), [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl)

### Zoekflow faalt bij Heemskerk

Productie en acceptatie bieden tekst-, plek-, persoon-, gebeurtenis- en periodefilters. Een read-only zoekactie op ‘Heemskerk’ toont geen resultaten: Europeana is niet geconfigureerd en Open Archieven gaf een onvolledig antwoord. De zoekvraag blijft behouden en opnieuw proberen is mogelijk.

Bronnen: [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl)

### Ontbrekende controleerbaarheid

De zoekuitkomst toont geen bron-per-bron status, foutcategorie, ophaaltijd, aantallen, stabiele identifiers, permanente bronlinks of rechtenstatussen. Geldige deelresultaten zijn niet zichtbaar.

Bronnen: [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://www.openarchieven.nl/api/docs/?lang=en](https://www.openarchieven.nl/api/docs/?lang=en)

### Beheeromgeving

De beheeracceptatie is zonder zichtbare login bereikbaar en toont een als geverifieerd gepresenteerde beheerder plus mutatieve formulieren voor nieuws en lokale record-intake. Er is niets ingevuld of verzonden.

Bronnen: [https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/)

### Collectie Nederland als zoekinspiratie

Collectie Nederland combineert vrije tekst met filters, veldspecifieke zoeking, facetten en een open API. Dit is een bruikbaar patroon voor gefaseerde verfijning nadat bronrecords betrouwbaar werken.

Bronnen: [https://www.collectienederland.nl/zoeken/](https://www.collectienederland.nl/zoeken/)

### Europeana als rechten- en filterinspiratie

Europeana biedt search/record/API-lagen, facetten, pagination, media- en landingpagefilters en expliciete reusability-statussen. De API vereist een API-key.

Bronnen: [https://api.europeana.eu/en](https://api.europeana.eu/en), [https://europeana.atlassian.net/wiki/spaces/EF/pages/2385739812/Search%2BAPI%2BDocumentation?redirectedFromRestrict=true](https://europeana.atlassian.net/wiki/spaces/EF/pages/2385739812/Search%2BAPI%2BDocumentation?redirectedFromRestrict=true)

### Historypin als contextinspiratie

Historypin verbindt historische verhalen met plaats, tijd, collecties, tours en interactieve kaarten. Dit is relevant voor een latere contextlaag, zodra bronrecords betrouwbaar beschikbaar zijn.

Bronnen: [https://about.historypin.org/about/](https://about.historypin.org/about/), [https://historypin.github.io/api-docs/](https://historypin.github.io/api-docs/)

### Huidige applicatie

**Doel:** Een brede publieke historische ontdekapp voor iedereen die iets wil weten over gebouwen, straten, personen, gebeurtenissen of andere aspecten van de Heemskerkse geschiedenis.

**Wat ontbreekt:**
- Geen historische records zichtbaar bij de kernzoekactie.
- Geen bronstatus, foutcategorie, ophaaltijd, aantallen, identifiers, bronlinks of rechtenstatussen.
- Geen aangetoonde detailweergave, bronverantwoording, contextrelaties, kaart, tijdlijn of vervolgzoeking.
- Publiek bereikbare adminomgeving met mutatieve formulieren vraagt autorisatie- en privacycontrole vóór echte gegevensverwerking.

### Verbetermogelijkheden

- Toon per bron naam, statuscategorie, foutinformatie, ophaaltijd en aantal resultaten.
- Valideer bronantwoorden deterministisch en behoud geldige deelresultaten.
- Maak ‘geen resultaten’, ‘bron niet beschikbaar’, ‘ongeldige response’ en ‘niet geconfigureerd’ afzonderlijk zichtbaar.
- Toon per resultaat een stabiele identifier, beperkte metadata, permanente bronlink en afzonderlijke rechtenstatus.
- Voeg na betrouwbare resultaten een detailweergave en veilige vervolgzoeklinks toe.
- Onderzoek later kaart- en tijdcontext geïnspireerd door Historypin, uitsluitend op expliciete bronmetadata.
- Bescherm admin-publicatie en record-intake achter echte autorisatie en privacycontroles.

### Inspiratiebronnen

- [Collectie Nederland](https://www.collectienederland.nl/zoeken/) — Filters, facetten, veldspecifieke zoeking en open API.
- [Europeana](https://api.europeana.eu/en) — Verbonden erfgoedbronnen, facetten en expliciete rechten-/reusabilitysignalen.
- [Historypin](https://about.historypin.org/about/) — Plaats-, tijd- en verhaalgebaseerde historische ontdekking.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://github.com/robbertvdzon/hkh-autopilot) | 2026-08-14 | Publieke GitHub-repository; concrete licentie niet vastgesteld omdat de webtool een cache-miss gaf. | Opgegeven primaire bron voor broncode en documentatie; lokaal aanwezige leesbare kennisbron diende als kruiscontrole. |
| [bron](https://hkh-autopilot.vdzonsoftware.nl) | 2026-08-14 | Publieke applicatie; rechten van historische broninhoud onbekend. | Productieflow en read-only zoekactie. |
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl) | 2026-08-14 | Acceptatieomgeving met representatieve dummydata en gemockte koppelingen. | Veilige uitgebreide interactie en verificatie van de zoekflow. |
| [bron](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/) | 2026-08-14 | Publieke admin-interface; rechten van UI-inhoud onbekend. | Controle van beheer- en intakefunctionaliteit. |
| [bron](https://www.openarchieven.nl/api/docs/?lang=en) | 2026-08-14 | Publieke officiële API-documentatie; expliciete licentie niet aangetroffen. | Onderbouwt search-, show-, URI- en content-negotiationmogelijkheden. |
| [bron](https://api.europeana.eu/en) | 2026-08-14 | Officiële API-documentatie; objectrechten blijven recordafhankelijk. | Onderbouwt API-key-afhankelijkheid en Europeana-lagen. |
| [bron](https://europeana.atlassian.net/wiki/spaces/EF/pages/2385739812/Search%2BAPI%2BDocumentation?redirectedFromRestrict=true) | 2026-08-14 | Publieke officiële developer-documentatie; documentatielicentie niet afzonderlijk vastgesteld. | Onderbouwt facetten, filters, pagination en reusability. |
| [bron](https://www.collectienederland.nl/zoeken/) | 2026-08-14 | Publieke erfgoedwebsite; rechten van objecten en metadata zijn partner-/recordafhankelijk. | Vergelijkbaar Nederlands zoek- en filterpatroon. |
| [bron](https://about.historypin.org/about/) | 2026-08-14 | Publieke organisatiepagina; rechten van afzonderlijke bijdragen zijn contributor-/assetafhankelijk. | Inspiratie voor verhalen, community-context en kaarten. |
| [bron](https://historypin.github.io/api-docs/) | 2026-08-14 | Publieke API-documentatie; rechten van afzonderlijke pins/media onbekend. | Onderbouwt plaats-, tijd- en collectiegegevens. |

## Productbeslissing

Bouw een kleine, bronveerkrachtige zoek-MVP voor de zoekopdracht ‘Heemskerk’: toon per externe bron een expliciete status, geldige deelresultaten en per record uitsluitend controleerbare metadata met stabiele identifier, permanente bronlink en afzonderlijke rechtenstatus. Maak vervolgzoeken pas beschikbaar vanuit metadata die de bron zelf levert.

**Waarom:** Dit is de kleinste samenhangende stap die de kernbelofte ‘verbonden’ en ‘betrouwbaar’ direct verbetert. De huidige flow bewaart de zoekvraag maar toont geen records, bronstatus, aantallen, identifiers, permanente links of rechteninformatie wanneer bronnen falen. Door bronuitval en geldige deelresultaten afzonderlijk zichtbaar te maken, blijft een antwoord begrijpelijk en herleidbaar zonder onbewezen historische relaties te presenteren. De richting sluit primair aan op epic theme-hkh-autopilot-0002 en ondersteunt daarna gecontroleerde ontdekking uit epic theme-hkh-autopilot-0001.

### Prioriteiten
- Implementeer deterministische bronstatussen: resultaten, geen resultaten, bron niet beschikbaar, ongeldige respons en niet geconfigureerd.
- Gebruik Open Archieven als eerste externe bron en behoud geldige deelresultaten wanneer een andere bron faalt.
- Toon per bron ophaaltijd en aantallen; toon per record beperkte bronmetadata, stabiele identifier, permanente bronlink en rechtenstatus.
- Maak de bronverantwoording en foutmelding begrijpelijk voor een brede doelgroep, zonder technische details als vervanging voor een duidelijk antwoord.
- Voeg alleen vervolgzoeklinks toe wanneer de gebruikte bron de betreffende relatie of zoekmetadata expliciet levert.

### Besluiten
- **Maak Open Archieven de eerste operationele bron van de MVP en ontwerp de bronadapter zo dat latere bronnen afzonderlijk kunnen worden toegevoegd.** — De roadmap noemt Open Archieven als eerstvolgende focus. De officiële documentatie ondersteunt zoeken, recordweergave, URI’s en content negotiation.
- **Behandel bronstatus als eersteklas resultaat naast historische records.** — De huidige productie- en acceptatieflow maakt niet-geconfigureerde en onvolledige bronnen zichtbaar, maar onderscheidt foutcategorieën en geldige deelresultaten onvoldoende. Per-bron status maakt de uitkomst controleerbaar en voorkomt dat bronuitval als ‘geen geschiedenis gevonden’ wordt geïnterpreteerd.
- **Toon rechteninformatie afzonderlijk van inhoudelijke metadata en neem die over uit de bron wanneer beschikbaar; vul niet zelf ontbrekende rechtenclaims in.** — Externe erfgoedrecords hebben recordafhankelijke rechten. Europeana laat zien dat expliciete reusability-signalen bruikbaar zijn, terwijl de rechten van objecten per record kunnen verschillen.
- **Stel facetten, kaart, tijdlijn en uitgebreide contextrelaties uit tot betrouwbare records en detailweergave beschikbaar zijn.** — Collectie Nederland, Europeana en Historypin zijn waardevolle patronen, maar de huidige kernzoekactie levert nog geen bruikbare records. Eerst moet de basisuitkomst herleidbaar en betrouwbaar zijn.

## UX-voorstel: Bronveerkrachtige zoek-MVP voor ‘Heemskerk’

**Gebruikersdoel:** De gebruiker wil historische informatie over Heemskerk vinden en kunnen beoordelen welke bronnen betrouwbaar beschikbaar zijn, zonder bronuitval te verwarren met het ontbreken van historische informatie.

### Flow
1. Open Historisch zoeken.
2. Voer ‘Heemskerk’ in en start de zoekopdracht.
3. Toon de behouden zoekvraag, zoektijd en een samenvatting van de totale uitkomst.
4. Toon per bron een expliciete status: resultaten, geen resultaten, bron niet beschikbaar, ongeldige respons of niet geconfigureerd.
5. Toon geldige deelresultaten ook wanneer een andere bron faalt.
6. Toon per record uitsluitend beperkte bronmetadata, een stabiele identifier, een permanente bronlink en een afzonderlijke rechtenstatus.
7. Toon alleen vervolgzoeklinks wanneer de bron de betreffende zoekmetadata expliciet levert.
8. Bied opnieuw proberen aan zonder de zoekvraag of reeds geldige deelresultaten te verliezen.

### Wireframe

[Pagina: Historisch zoeken]

[H1] Historisch zoeken
[Label] Zoekterm
[Input: Heemskerk]
[Button] Zoeken

[Statusgebied role=status]
Zoekopdracht ‘Heemskerk’ uitgevoerd op [tijd].
[Samenvatting] 1 bron verwerkt · 3 resultaten · 1 bron niet beschikbaar

[H2] Bronnen
[Bronkaart: Open Archieven]
Status: Resultaten beschikbaar
Ophaaltijd: [tijd] · Aantal: 3
[Recordkaart]
- Titel/onderwerp: [bronveld]
- Datum: [bronveld indien beschikbaar]
- Plaats: [bronveld indien beschikbaar]
- Identifier: [stabiele identifier]
- Rechten: [bronwaarde of ‘Niet vermeld door bron’]
[Link] Bekijk permanent bronrecord
[Optionele link] Zoek gerelateerde records volgens bronmetadata

[Bronkaart: Europeana]
Status: Niet geconfigureerd
Er zijn voor deze bron geen resultaten opgehaald.

[Bronkaart: Andere bron]
Status: Bron niet beschikbaar
De bron gaf geen bruikbaar antwoord. Dit betekent niet dat er geen historische informatie bestaat.
[Button] Opnieuw proberen

[H2] Over deze zoekuitkomst
Bronstatussen, aantallen, ophaaltijden en rechteninformatie zijn per bron weergegeven. Rechteninformatie wordt niet door de applicatie aangevuld.

[Link] Nieuwe zoekopdracht

### Interactiehypotheses
- Als bronstatussen per bron afzonderlijk zichtbaar zijn, kunnen gebruikers ‘geen resultaten’ onderscheiden van bronuitval; dit is toetsbaar met geautomatiseerde scenario’s voor alle vijf statuscategorieën.
- Als geldige deelresultaten behouden blijven wanneer een andere bron faalt, blijft minstens één controleerbaar resultaat zichtbaar in een gedeeltelijk geslaagde zoekopdracht; dit is toetsbaar met een gemockte combinatie van een geldige en een falende bron.
- Als elk record een stabiele identifier en permanente bronlink toont, kunnen agents controleren dat ieder resultaat herleidbaar is naar de oorspronkelijke bron.
- Als rechteninformatie als afzonderlijk veld wordt getoond en ontbrekende informatie letterlijk als niet vermeld wordt aangegeven, worden geen onbewezen rechtenclaims toegevoegd; dit is toetsbaar met records met aanwezige en ontbrekende rechtenvelden.
- Als opnieuw proberen de zoekterm en bestaande geldige resultaten behoudt, raakt de gebruiker geen context kwijt bij tijdelijke bronuitval; dit is toetsbaar met een retry-scenario.
- Als vervolgzoeklinks uitsluitend uit expliciet geleverde bronmetadata worden opgebouwd, ontstaan geen onbewezen historische relaties; dit is toetsbaar met records zonder relatievelden en records met expliciete relatievelden.

### Toegankelijkheid
- Gebruik semantische koppen, labels en gegroepeerde bronkaarten; behoud een logische tabvolgorde.
- Maak zoeken, opnieuw proberen en alle bronlinks volledig met toetsenbord bedienbaar.
- Gebruik een zichtbaar focus-indicator en voldoende kleurcontrast; status mag nooit uitsluitend met kleur worden aangeduid.
- Plaats dynamische zoekmeldingen in een passend status- of livegebied zonder de schermlezer onnodig te onderbreken.
- Geef iedere bronstatus tekstueel weer en gebruik begrijpelijke foutmeldingen zonder technische foutdetails als hoofdboodschap.
- Geef links beschrijvende namen, bijvoorbeeld ‘Bekijk permanent bronrecord’, en open externe links voorspelbaar.
- Zorg dat recordmetadata als semantische lijst of tabel wordt voorgelezen met duidelijke veldnamen.
- Ondersteun zoom en kleine schermen zonder horizontaal scrollen voor kerninformatie.

### Privacy
- Sla de zoekterm alleen op zolang dat nodig is voor de actieve zoekopdracht of retry; vermijd permanente opslag zonder duidelijk doel.
- Behandel zoektermen als mogelijk persoonsgevoelige informatie en log geen volledige zoekopdrachten of recordinhoud standaard.
- Toon uitsluitend metadata die de externe bron zelf levert; haal geen extra persoonsgegevens op voor context of relatieafleiding.
- Neem rechteninformatie over uit de bron en vul ontbrekende rechten niet zelf in.
- Gebruik voor deze publieke zoek-MVP geen account, profiel of identificerende gebruikersgegevens.
- Laat externe bronlinks duidelijk herkenbaar zijn en voorkom het delen van gebruikerscontext met externe bronnen tenzij noodzakelijk voor de expliciete zoekactie.
- De adminomgeving en record-intake vallen buiten deze MVP; verwerk daar geen echte persoonsgegevens zonder autorisatie, doelbinding, passende grondslag en bewaarbeleid.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is klein, toetsbaar en agent-uitvoerbaar. Er zijn geen blokkerende problemen. De retry-uitwerking overlapt deels met reeds gepubliceerde bronveerkracht- en loggingstories, maar voegt specifiek behoud en vervanging van zoekcontext bij opnieuw proberen toe.
- **INFO · CONSISTENCY** — De kandidaat overlapt met de reeds gepubliceerde story 63 over bronveerkrachtige zoekuitkomsten en met story 77 over logging. Dit is geen blokkade, mits alleen retrygedrag wordt toegevoegd en bestaande status- en loggingcontracten worden hergebruikt.

## Geaccepteerde storykandidaten

### Zoekcontext en geldige deelresultaten behouden bij opnieuw proberen

_Sleutel: `zoekcontext-behouden-bij-opnieuw-proberen`_

Als bezoeker wil ik een mislukte of gedeeltelijk geslaagde historische zoekopdracht opnieuw kunnen proberen zonder mijn zoekterm, bronstatussen of al beschikbare controleerbare resultaten kwijt te raken, zodat tijdelijke bronuitval niet leidt tot verlies van context.

**Acceptatiecriteria**
- Een opnieuw-proberenactie gebruikt exact dezelfde zoekparameters als de oorspronkelijke zoekopdracht zonder dat de gebruiker de zoekterm opnieuw moet invoeren.
- Tijdens opnieuw proberen blijven de oorspronkelijke zoekterm en reeds beschikbare geldige deelresultaten zichtbaar.
- De interface maakt tekstueel onderscheid tussen de vorige uitkomst en de lopende nieuwe poging.
- Na een succesvolle retry worden de resultaten en bronstatussen vervangen door de nieuwe geldige uitkomst; resultaten uit de vorige poging die niet opnieuw geldig zijn ontvangen worden niet als actuele resultaten behouden.
- Na een mislukte retry blijven de laatst geldige deelresultaten zichtbaar en wordt de nieuwe bronfout afzonderlijk en begrijpelijk getoond.
- Een geautomatiseerde test verifieert dat een retry met een gemockte tijdelijke bronfout geen zoekterm of geldige deelresultaten verliest.
- Een geautomatiseerde test verifieert dat retry-parameters geen volledige zoekgeschiedenis of ruwe bronpayload naar logging of client-state toevoegen.

Bronnen: [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl), [https://www.openarchieven.nl/api/docs/?lang=en](https://www.openarchieven.nl/api/docs/?lang=en)

Afhankelijkheden: story:63 (herkend als bestaande stories: 63)

Risico's: Een retry kan verouderde resultaten tonen als de interface onvoldoende duidelijk onderscheid maakt tussen de vorige en actuele poging., Herhaalde externe aanvragen kunnen bronrate-limits raken; de implementatie moet bestaande time-outs, foutafhandeling en rate-limitgedrag respecteren.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
