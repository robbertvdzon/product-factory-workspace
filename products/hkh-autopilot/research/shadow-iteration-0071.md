---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0071
date: 2026-08-14
status: approved
sources:
  - https://github.com/robbertvdzon/hkh-autopilot
  - https://hkh-autopilot.vdzonsoftware.nl
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl
  - https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/
  - https://www.openarchieven.nl/api/docs/?lang=en
  - https://www.openarchieven.nl/api/docs/uri.php
  - https://www.openarchieven.nl/datasets/nha?lang=en
  - https://www.archieven.nl/nl/zoeken?miadt=236&micode=1032&milang=nl&minr=1090322&mivast=0&miview=inv2&mizig=210
  - https://europeana.atlassian.net/wiki/spaces/EF/pages/2329346049/How%2Bto%2Bsearch%2BEuropeana%2Bwebsite%2Band%2BAPI
  - https://europeana.atlassian.net/wiki/spaces/EF/pages/2385739812/Search
---
# Productcyclus 71

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De belangrijkste onbeantwoorde productvraag is hoe de app een controleerbaar eerste zoekresultaat kan leveren wanneer externe bronnen gedeeltelijk of volledig falen. Productie en acceptatie leveren voor ‘Heemskerk’ geen records; Open Archieven meldt een onvolledig antwoord en Europeana is niet geconfigureerd. Publieke bronnen tonen wel relevante Heemskerk-dekking en stabiele metadata-infrastructuur.

### Huidige zoekflow

Productie en acceptatie bieden vrije tekst en filters voor plek, persoon, gebeurtenis, periode en bron. Een read-only zoekactie op ‘Heemskerk’ toont geen records, Europeana als niet geconfigureerd en Open Archieven als onvolledig antwoord.

Bronnen: [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl)

### Repositoryarchitectuur

De publieke repository beschrijft een Flutter-webapp, aparte admin-app en een historische zoekroute die Europeana en Open Archieven bevraagt. De README beschrijft al bronstatussen, stabiele identifiers, rechtenvelden en retry/cachinggedrag, maar de live zoekuitkomst levert nog geen controleerbaar record.

Bronnen: [https://github.com/robbertvdzon/hkh-autopilot](https://github.com/robbertvdzon/hkh-autopilot)

### Open Archieven-contract

Open Archieven documenteert zoek-, match- en show-operaties, vaste record-URI’s, content negotiation, OpenSearch, OAI-PMH, server-side caching en een limiet van vier verzoeken per seconde per IP.

Bronnen: [https://www.openarchieven.nl/api/docs/?lang=en](https://www.openarchieven.nl/api/docs/?lang=en), [https://www.openarchieven.nl/api/docs/uri.php](https://www.openarchieven.nl/api/docs/uri.php)

### NHA-dekking en rechten

De NHA-dataset bevat miljoenen documentmetadata en historische persoonsvermeldingen, gebruikt A2A/OAI-PMH en vermeldt CC0 voor de datasetmetadata. Afbeeldingen en third-party-viewers vallen expliciet buiten die CC0-vermelding.

Bronnen: [https://www.openarchieven.nl/datasets/nha?lang=en](https://www.openarchieven.nl/datasets/nha?lang=en)

### Heemskerk-archieftoegang

Archieven.nl toont voor Heemskerk een publieke archieftoegang met 1.371 beschreven stukken, 228 gedigitaliseerde stukken, een duurzaam webadres, openbare raadpleegbaarheid en CC0 voor metadata.

Bronnen: [https://www.archieven.nl/nl/zoeken?miadt=236&micode=1032&milang=nl&minr=1090322&mivast=0&miview=inv2&mizig=210](https://www.archieven.nl/nl/zoeken?miadt=236&micode=1032&milang=nl&minr=1090322&mivast=0&miview=inv2&mizig=210)

### Europeana als aanvullende bron

Europeana ondersteunt querysyntax, facets en filters op onder meer personen en jaren. De officiële documentatie vermeldt dat API-gebruik een persoonlijke API-key vereist, wat aansluit bij de huidige status ‘niet geconfigureerd’.

Bronnen: [https://europeana.atlassian.net/wiki/spaces/EF/pages/2329346049/How%2Bto%2Bsearch%2BEuropeana%2Bwebsite%2Band%2BAPI](https://europeana.atlassian.net/wiki/spaces/EF/pages/2329346049/How%2Bto%2Bsearch%2BEuropeana%2Bwebsite%2Band%2BAPI), [https://europeana.atlassian.net/wiki/spaces/EF/pages/2385739812/Search](https://europeana.atlassian.net/wiki/spaces/EF/pages/2385739812/Search)

### Huidige applicatie

**Doel:** De applicatie is een publieksgerichte historische zoekingang voor een brede doelgroep. Gebruikers kunnen vanuit vrije tekst of filters zoeken naar historische informatie over Heemskerk en die plaatsen binnen een bredere context van publieke bronnen.

**Wat ontbreekt:**
- Zoeken op ‘Heemskerk’ levert in productie en acceptatie geen historische records.
- De UI toont geen recordmetadata, stabiele identifier of permanente bronlink.
- De foutmelding over het onvolledige Open Archieven-antwoord is niet diagnostisch genoeg.
- Europeana is niet geconfigureerd.
- De aantoonbare Heemskerk-dekking bij NHA/Archieven.nl is niet zichtbaar verbonden met de app.
- De zoekuitkomst biedt alleen opnieuw proberen of de zoekopdracht aanpassen.
- Rechteninformatie ontbreekt in de zichtbare zoekuitkomst, terwijl metadatarechten en objectrechten volgens de bron afzonderlijk moeten worden beoordeeld.
- De beheeromgeving toont lokale record-intake als intern concept, maar de publieke flow toont geen status van zulke records.

### Verbetermogelijkheden

- Maak de eerste bronketen end-to-end controleerbaar: valideer de bronrespons, normaliseer complete metadata en toon per bron afzonderlijk succes, nulresultaat, gedeeltelijke beschikbaarheid, uitval en niet-geconfigureerd.
- Gebruik uitsluitend door Open Archieven geleverde stabiele URI’s, identifiers en bronlinks; maak ontbrekende velden expliciet zichtbaar.
- Gebruik de aantoonbare NHA-Heemskerkdekking als verificatiecontext, maar scheid CC0 voor metadata van rechten op afbeeldingen en third-party-viewers.
- Stem verzoekbudget en caching expliciet af op de actuele Open Archieven-documentatie en voorkom dubbele gelijktijdige aanvragen.
- Toon bruikbare deelresultaten wanneer één bron uitvalt, zodat bronuitval niet wordt verward met nulresultaten.
- Maak foutmeldingen handelingsgericht zonder ruwe providerpayloads of exceptiondetails te tonen.
- Gebruik Archieven.nl als inspiratie voor zoekhulp, periode- en digitaliseringsfilters, hiërarchische context en duurzame webadressen.
- Behandel Europeana als aanvullende bron met expliciete uitleg over configuratiestatus en API-keyafhankelijkheid.

### Inspiratiebronnen

- [Archieven.nl / Noord-Hollands Archief](https://www.archieven.nl/nl/zoeken?miadt=236&micode=1032&milang=nl&minr=1090322&mivast=0&miview=inv2&mizig=210) — Heemskerk-specifieke inspiratie voor zoekuitleg, filters, hiërarchische context, duurzame URL’s en rechtenmetadata.
- [Open Archieven API](https://www.openarchieven.nl/api/docs/?lang=en) — Inspiratie voor stabiele record-URI’s, bronstatussen, caching en gestructureerde zoekresultaten.
- [Europeana Collections](https://www.europeana.eu/en/search?query=who%3AVermeer) — Inspiratie voor discovery via querysyntax, facets, personen-/jaarfilters en metadata-based browsing.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://github.com/robbertvdzon/hkh-autopilot) | 2026-08-14 | Publieke repository; concrete licentie niet vastgesteld. | README en repositorystructuur geraadpleegd voor huidige architectuur en zoekfunctionaliteit. |
| [bron](https://hkh-autopilot.vdzonsoftware.nl) | 2026-08-14 | Publieke interface; rechten op interface en externe inhoud niet vastgesteld. | Exacte productie-URL geopend, naar historisch zoeken genavigeerd en read-only op ‘Heemskerk’ gezocht. |
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl) | 2026-08-14 | Publieke acceptatie-interface met representatieve nepdata; concrete licentie niet vastgesteld. | Acceptatieomgeving geopend, doorgeklikt naar historisch zoeken en read-only gezocht. |
| [bron](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/) | 2026-08-14 | Publieke beheerinterface; concrete licentie niet vastgesteld. | Zonder login bekeken; nieuws- en lokale record-intakeformulieren geobserveerd zonder mutatie. |
| [bron](https://www.openarchieven.nl/api/docs/?lang=en) | 2026-08-14 | Publieke documentatie; concrete paginatekstlicentie niet vastgesteld. | Primaire bron voor API-operaties, rate limiting, caching, OpenSearch en OAI-PMH. |
| [bron](https://www.openarchieven.nl/api/docs/uri.php) | 2026-08-14 | Publieke documentatie; concrete paginatekstlicentie niet vastgesteld. | Primaire bron voor stabiele URI’s en content negotiation. |
| [bron](https://www.openarchieven.nl/datasets/nha?lang=en) | 2026-08-14 | Datasetmetadata onder CC0 Public Domain Dedication; afbeeldingen en third-party-viewers expliciet uitgesloten. | Primaire datasetbeschrijving voor omvang, structuur, harvesting en rechten. |
| [bron](https://www.archieven.nl/nl/zoeken?miadt=236&micode=1032&milang=nl&minr=1090322&mivast=0&miview=inv2&mizig=210) | 2026-08-14 | Metadata vermeldt CC0; objectmediarechten afzonderlijk niet vastgesteld. | Primaire Heemskerk-archieftoegang voor dekking, duurzame URL en zoekinspiratie. |
| [bron](https://europeana.atlassian.net/wiki/spaces/EF/pages/2329346049/How%2Bto%2Bsearch%2BEuropeana%2Bwebsite%2Band%2BAPI) | 2026-08-14 | Publieke Europeana-documentatie; concrete paginatekstlicentie niet vastgesteld. | Officiële bron voor zoeksyntax, productie-API en API-keyvereiste. |
| [bron](https://europeana.atlassian.net/wiki/spaces/EF/pages/2385739812/Search) | 2026-08-14 | Publieke Europeana-documentatie; concrete paginatekstlicentie niet vastgesteld. | Officiële bron voor zoekfilters en verfijning. |

## Productbeslissing

Lever een smalle, controleerbare zoek-MVP voor ‘Heemskerk’ met Open Archieven als eerste en enige actieve externe bron. Toon per zoekactie bruikbare recordmetadata, een stabiele identifier en permanente bronlink; maak bronstatussen expliciet voor succes, nulresultaat, gedeeltelijke beschikbaarheid en uitval. Europeana blijft zichtbaar als niet-geconfigureerd, zonder de MVP te blokkeren.

**Waarom:** Deze richting sluit direct aan op missie en epic theme-hkh-autopilot-0002. De huidige flow levert geen controleerbare records en maakt onvolledige beschikbaarheid onvoldoende begrijpelijk. Open Archieven biedt gedocumenteerde zoekoperaties en stabiele URI’s, terwijl de NHA-dekking een relevante verificatiecontext biedt. De MVP blijft klein, toetsbaar, bronherleidbaar en uitvoerbaar zonder nieuwe menselijke handelingen, behalve eventueel later noodzakelijke configuratie van een extern token.

### Prioriteiten
- Valideer en normaliseer de Open Archieven-respons voordat resultaten worden getoond.
- Toon alleen brongeleverde metadata, stabiele identifiers en permanente bronlinks.
- Maak per bron onderscheid tussen succes, nulresultaat, gedeeltelijke beschikbaarheid, uitval en niet-geconfigureerd.
- Toon bruikbare deelresultaten wanneer een bron gedeeltelijk of volledig uitvalt.
- Gebruik caching en een begrensd verzoekbudget conform de Open Archieven-documentatie; voorkom dubbele gelijktijdige aanvragen.

### Besluiten
- **Open Archieven wordt de enige actieve externe bron in deze eerste MVP.** — De roadmap noemt Open Archieven expliciet als eerste bron en de bron documenteert publieke zoekoperaties zonder dat in het onderzoek een tokenvereiste is vastgesteld.
- **Een resultaat is pas controleerbaar wanneer het minimaal bronmetadata, een stabiele identifier en een permanente bronlink bevat.** — Open Archieven documenteert vaste record-URI’s en de huidige zoekuitkomst toont nog geen herleidbaar record.
- **Bronstatus wordt zichtbaar en afzonderlijk gepresenteerd; bronuitval mag niet als nulresultaat worden weergegeven.** — De huidige productie- en acceptatieflow toont een onvolledig Open Archieven-antwoord zonder voldoende diagnostische uitleg. De architectuurbeschrijving voorziet al in bronstatussen en retry/cachinggedrag.
- **Rechteninformatie wordt per metadata en objectmedia gescheiden weergegeven zodra die informatie door de bron wordt geleverd.** — De NHA-bron vermeldt CC0 voor datasetmetadata maar sluit afbeeldingen en third-party-viewers expliciet uit; de app moet die verschillen niet samenvoegen.
- **Europeana blijft voorlopig een expliciet gemarkeerde niet-geconfigureerde aanvullende bron.** — Europeana vereist volgens de officiële documentatie een persoonlijke API-key; activering zou daarom buiten de kleine Open Archieven-MVP vallen.

## UX-voorstel: Controleerbare zoekactie op ‘Heemskerk’

**Gebruikersdoel:** De gebruiker wil historische records vinden en direct kunnen controleren via bronmetadata, een stabiele identifier en een permanente bronlink.

### Flow
1. Open Historisch zoeken.
2. Voer ‘Heemskerk’ in en start de zoekactie.
3. Toon een laadstatus met de geraadpleegde bron en voorkom dubbele gelijktijdige aanvragen.
4. Toon per bron een duidelijke status: succes, nulresultaat, gedeeltelijk beschikbaar, uitval of niet-geconfigureerd.
5. Toon bij beschikbare records alleen gevalideerde bronmetadata, een stabiele identifier en een permanente bronlink.
6. Toon bij gedeeltelijke beschikbaarheid bruikbare records plus een handelingsgerichte waarschuwing.
7. Toon bij uitval een begrijpelijke foutmelding met ‘Opnieuw proberen’ en behoud de zoekopdracht.
8. Toon Europeana als aanvullende bron met status ‘Niet geconfigureerd’ zonder de Open Archieven-resultaten te blokkeren.
9. Laat de gebruiker de zoekopdracht aanpassen of opnieuw proberen.​​​​

### Wireframe

Pagina: Historisch zoeken

[Terug]
Historisch zoeken
Zoek in publieke historische bronnen.

[Zoekterm ____________________] [Zoeken]
Voorbeeld: Heemskerk

Bronstatus
┌──────────────────────────────────────────────┐
│ Open Archieven   [Gedeeltelijk beschikbaar]  │
│ 12 resultaten gevonden. Sommige gegevens    │
│ konden niet worden opgehaald.                │
└──────────────────────────────────────────────┘

Resultaten
┌──────────────────────────────────────────────┐
│ Titel of beschrijving                         │
│ Datum/periode: brongeleverde waarde          │
│ Plaats/persoon: brongeleverde waarde         │
│ Identifier: OA-12345                          │
│ Metadatarechten: brongeleverde waarde        │
│ Objectmediarechten: onbekend/niet geleverd   │
│ [Open permanente bronlink]                    │
└──────────────────────────────────────────────┘

Herhaalbare resultaatkaart voor elk record.

Aanvullende bronnen
┌──────────────────────────────────────────────┐
│ Europeana       [Niet geconfigureerd]        │
│ Deze bron is momenteel niet beschikbaar.     │
└──────────────────────────────────────────────┘

[Opnieuw proberen] [Zoekopdracht aanpassen]

Bij nulresultaat: ‘Geen records gevonden voor deze zoekopdracht.’
Bij volledige uitval: ‘Open Archieven kon tijdelijk niet worden geraadpleegd. Er zijn geen resultaten opgehaald; dit is geen bevestiging dat er geen records bestaan.’

### Interactiehypotheses
- Als bronstatussen per bron afzonderlijk zichtbaar zijn, kunnen gebruikers onderscheid maken tussen nulresultaat en bronuitval; dit is toetsbaar met geautomatiseerde statusfixtures en tekstasserties.
- Als elk resultaat een stabiele identifier en permanente bronlink bevat, kan een agent automatisch controleren of het record herleidbaar is zonder providergegevens te raden of aan te vullen.
- Als gedeeltelijke resultaten naast een waarschuwing worden getoond, blijft de zoekactie bruikbaar bij gedeeltelijke bronuitval; dit is toetsbaar met een fixture waarin een deel van de records ongeldig of ontbrekend is.
- Als dubbele gelijktijdige zoekacties worden geblokkeerd of samengevoegd, blijft het verzoekbudget binnen de bronlimiet; dit is toetsbaar met netwerk-mocks en request-count assertions.
- Als rechten voor metadata en objectmedia afzonderlijk worden weergegeven, wordt CC0 voor metadata niet onterecht geïnterpreteerd als toestemming voor afbeeldingen; dit is toetsbaar met ontbrekende- en gescheiden-rechtenvelden.
- Als Europeana zichtbaar als niet-geconfigureerd wordt gemarkeerd, begrijpt de gebruiker dat deze bron niet is geraadpleegd en wordt de Open Archieven-MVP niet geblokkeerd.

### Toegankelijkheid
- Alle functies zijn volledig met het toetsenbord bereikbaar; de focusvolgorde volgt de visuele leesvolgorde.
- Gebruik semantische koppen, een formulier voor de zoekactie, echte knoppen en links, en een lijst met resultaatkaarten.
- Publiceer laad-, succes-, gedeeltelijke- en foutstatussen in een aria-live-regio zonder focus onverwacht te verplaatsen.
- Geef elke resultaatkaart een duidelijke structuur en beschrijvende linktekst, bijvoorbeeld ‘Open permanente bronlink voor record OA-12345’.
- Gebruik voldoende kleurcontrast en combineer statuskleuren altijd met tekst en/of een toegankelijk statuslabel.
- Maak foutmeldingen begrijpelijk zonder ruwe providerpayloads; behoud de ingevoerde zoekterm na een fout.
- Ondersteun schermlezers bij lege resultaten, gedeeltelijke resultaten en niet-geconfigureerde bronnen met expliciete tekst.

### Privacy
- Sla alleen de zoekterm en technische cachegegevens op wanneer dit noodzakelijk is voor functionaliteit, rate limiting of foutdiagnose.
- Bewaar geen persoonsprofielen, IP-adressen of zoekgeschiedenis langer dan noodzakelijk; anonimiseer of aggregeer technische logs.
- Toon uitsluitend door de bron geleverde historische persoonsgegevens die nodig zijn voor het zoekresultaat; voeg geen afgeleide persoonsgegevens toe.
- Maak duidelijk dat externe bronlinks naar een andere website kunnen leiden en daar eigen privacyvoorwaarden kunnen gelden.
- Gebruik geen extern Europeana-token in deze MVP; voeg configuratie alleen toe met een duidelijk doel, beperkte toegang en passende geheimenbeheermaatregelen.
- Scheid metadatarechten van rechten op afbeeldingen en third-party-viewers; publiceer geen media zonder expliciete rechtenbasis.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is klein, geautomatiseerd en uitvoerbaar zonder eigenaaractie. Er zijn geen blokkerende problemen; enkele aandachtspunten blijven niet-blokkerend.
- **WARNING · CONSISTENCY** — De formulering ‘volledige keten’ kan ten onrechte suggereren dat een live Open Archieven-contract wordt gevalideerd, terwijl de test uitsluitend fixtures en netwerk-mocks gebruikt. Verduidelijk dat dit een applicatiecontracttest is en geen live bronvalidatie.
- **INFO · CONSISTENCY** — De eis dat bij volledige bronfout beschikbare resultaten behouden blijven is alleen relevant wanneer er al deelresultaten zijn; formuleer dit als eis voor gedeeltelijke uitval en controleer bij volledige uitval uitsluitend de expliciete bronprobleemstatus.
- **INFO · SCOPE** — De kandidaat overlapt gedeeltelijk met gepubliceerde stories 63, 74, 75 en 80, maar levert een afzonderlijke integrerende regressietest en is daarom geen exact duplicaat.

## Geaccepteerde storykandidaten

### Geautomatiseerd smokecontract voor de controleerbare Heemskerk-zoekketen

_Sleutel: `heemskerk-bronketen-smokecontract`_

Als Product Factory wil ik een reproduceerbare geautomatiseerde smoke-test voor de volledige Heemskerk-zoekketen, zodat wordt vastgesteld dat een zoekactie via de publieke route een geldig Open Archieven-resultaat, bronstatus en permanente bronlink kan opleveren zonder providergegevens te raden of te verbergen. De test gebruikt alleen fixtures en gecontroleerde netwerk-mocks en vormt geen nieuwe gebruikersfunctionaliteit.

**Acceptatiecriteria**
- De test start met de zoekterm ‘Heemskerk’ en verifieert de volledige keten van zoekactie tot weergegeven bronresultaat.
- Bij een geldige Open Archieven-respons controleert de test dat elk zichtbaar resultaat brongeleverde metadata, een stabiele identifier en een permanente bronlink bevat.
- Bij een geldig nulresultaat controleert de test dat nulresultaat niet als bronuitval wordt weergegeven.
- Bij een gedeeltelijke of volledige bronfout controleert de test dat beschikbare resultaten behouden blijven en dat de foutstatus niet als nulresultaat wordt gepresenteerd.
- De test controleert dat een niet-geconfigureerde Europeana-bron de Open Archieven-resultaten niet blokkeert.
- De test controleert dat een herhaalde identieke zoekactie geen extra gelijktijdige Open Archieven-aanvraag veroorzaakt en binnen het ingestelde verzoekbudget blijft.
- De smoke-test draait automatisch in de bestaande geautomatiseerde testpipeline en faalt met een specifieke assertion wanneer status, metadata, identifier of permanente bronlink ontbreekt.
- De test gebruikt geen echte persoonsgegevens, ruwe providerpayloads of externe wijzigingen en is reproduceerbaar zonder eigenaaractie of extern toegangstoken.

Bronnen: [https://github.com/robbertvdzon/hkh-autopilot](https://github.com/robbertvdzon/hkh-autopilot), [https://www.openarchieven.nl/api/docs/?lang=en](https://www.openarchieven.nl/api/docs/?lang=en), [https://www.openarchieven.nl/api/docs/uri.php](https://www.openarchieven.nl/api/docs/uri.php), [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl)

Afhankelijkheden: story:74, story:75, story:80, story:63 (herkend als bestaande stories: 74, 75, 80, 63)

Risico's: De smoke-test kan slagen op fixtures terwijl live broncontracten later wijzigen; periodieke contractvalidatie tegen de gedocumenteerde API blijft nodig., Een test die de publieke route te strikt aan exacte providertekst koppelt kan onnodig breekbaar worden; assertions moeten zich beperken tot het afgesproken status- en metadata-contract., Een live externe controle kan onderhevig zijn aan rate limits of tijdelijke uitval en hoort daarom niet als verplicht onderdeel van iedere pipeline-run te worden uitgevoerd.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
