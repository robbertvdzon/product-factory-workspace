---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0041
date: 2026-08-10
status: approved
sources:
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl
  - https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/externalverification/ArchivesNlClient.kt
  - https://www.openarchieven.nl/dashboard/hee
  - https://www.openarchieven.nl/api/docs/
  - https://www.regionaalarchiefalkmaar.nl/over-ons/open-data
  - https://www.heemskerk.nl/over-heemskerk/beeldbank
  - https://www.historischekringheemskerk.nl/cgi-bin/beeldbank.pl
  - https://noord-hollandsarchief.nl/collecties/open-data
  - https://opendata.archieven.nl/nl/over-open-data
  - https://www.erfgoedopdekaart.nl/
---
# Productcyclus 41

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Ik heb eerst de huidige staat vastgesteld door de repository (via raw.githubusercontent.com en de GitHub API) en de draaiende acceptatie- en beheeromgeving (via Playwright-screenshots, want WebFetch werd daar geblokkeerd) te inspecteren, en heb daarna gericht websearch/WebFetch-onderzoek gedaan naar de bronnen die de eigenaar in het laatste overleg al had aangewezen als prioriteit (Open Archieven 'hee', Regionaal Archief Alkmaar, HKH-eigen beeldbank, gemeente Heemskerk-beeldbank, Noord-Hollands Archief), plus het reeds in de code gebruikte opendata.archieven.nl-endpoint. Elke bevinding hieronder is direct gekoppeld aan een op 2026-08-10 zelf geraadpleegde bron met een expliciete rechten-/licentie-indicatie, conform de eerdere afkeuring. Belangrijkste conclusies: de app zelf werkt en toont het 'Ontdek nieuws'-blok met Plek/Gebeurtenis-chips, maar nog geen Persoon-chip, en de admin ondersteunt uitsluitend handmatige, één-voor-één record-intake zonder enige geautomatiseerde koppeling naar externe bronnen. Van de door de eigenaar genoemde bronnen blijkt Regionaal Archief Alkmaar zijn eigen werkgebied expliciet te beperken tot Alkmaar en acht andere gemeenten zónder Heemskerk, wat de eerdere aanname bijstelt; Open Archieven's 'hee'-dataset is vrij (zonder key, wel throttled) bevraagbaar maar zonder expliciete hergebruikslicentie; de gemeente- en HKH-eigen beeldbanken zijn technisch of juridisch niet zomaar automatisch te ontsluiten (auteursrecht resp. geen zichtbare API); en Noord-Hollands Archief en opendata.archieven.nl bieden wél echt open, machineleesbare data met een (grotendeels) permissieve licentie — dat laatste bevestigt en verduidelijkt bovendien de licentieonzekerheid die een eerdere critic-iteratie rond de al bestaande `ArchivesNlClient`-integratie signaleerde.

### Ontdekblok toont Plek/Gebeurtenis-chips maar nog geen Persoon-chip

De homepage van de acceptatieomgeving toont een werkend 'Ontdek nieuws'-blok met vrije-tekstzoeker en klikbare entiteitschips 'Plek: Kerkweg', 'Plek: Slot Assumburg', 'Gebeurtenis: HKH-lezing' en 'Gebeurtenis: Kermis', maar geen enkele 'Persoon:'-chip. Dit bevestigt dat de eerder gesignaleerde lacune (geen gepubliceerd nieuwsbericht gekoppeld aan een gazetteer-persoon) op 2026-08-10 nog steeds bestaat.

Bronnen: [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl)

### Admin ondersteunt alleen handmatige, één-record-tegelijk intake

Het beheergedeelte bevat een formulier 'Nieuwe record-intake' met louter handmatig in te vullen velden (lokale identifier, titel, beschrijving, datering, herkomst, rechtenstatus, privacyclassificatie, optionele externe conceptkoppeling met duurzame URL/koppelmotivering/onzekerheid) voor precies één record per keer. Er is geen bulk-import, harvester of connector naar een externe bron zichtbaar in de UI.

Bronnen: [https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/)

### Open Archieven 'hee'-dataset: vrij bevraagbaar zonder key, maar throttled en zonder expliciete hergebruikslicentie

De dashboardpagina van Open Archieven bevestigt de eerder gevonden omvang van de Historische Kring Heemskerk-dataset ('hee'): 5.362 akten met 10.242 persoonsvermeldingen. De API-documentatie beschrijft Search/Match/Show/Years-ago-endpoints die zonder API-key te bevragen zijn, met een IP-gebaseerde throttling van 4 requests/seconde (hoger op aanvraag), maar noch de datasetpagina noch de API-documentatie geeft een expliciete hergebruikslicentie (zoals CC0) voor de onderliggende data.

Bronnen: [https://www.openarchieven.nl/dashboard/hee](https://www.openarchieven.nl/dashboard/hee), [https://www.openarchieven.nl/api/docs/](https://www.openarchieven.nl/api/docs/)

### Regionaal Archief Alkmaar noemt Heemskerk niet in zijn eigen werkgebied

De officiële open-datapagina van Regionaal Archief Alkmaar omschrijft het werkgebied expliciet als 'Alkmaar en de gemeenten daar omheen (Bergen, Castricum, Den Helder, Dijk en Waard (Heerhugowaard en Langedijk), Heiloo, Hollands Kroon, Schagen en Texel)'. Heemskerk wordt niet genoemd. Dit stelt de eerder als kansrijk aangemerkte RAA-route bij: RAA is niet gegarandeerd een primaire bron van Heemskerk-materiaal, ook al biedt het instituut wel echte open API's (o.a. via maior.memorix.nl/api/oai) voor de collecties die het wél beheert.

Bronnen: [https://www.regionaalarchiefalkmaar.nl/over-ons/open-data](https://www.regionaalarchiefalkmaar.nl/over-ons/open-data)

### Gemeente Heemskerk-beeldbank is auteursrechtelijk beschermd, geen vrij hergebruik

De gemeentelijke beeldbank (473 foto's op 2026-08-10) bevat een expliciete 'Auteursrechten'-sectie met de tekst: 'De foto's uit de beeldbank zijn beschermd met auteursrecht. Wilt u een van de foto's ergens anders delen? Vraag eerst toestemming bij ons.' Er is geen API of exportfunctie zichtbaar; automatische koppeling zou dus zonder overleg met de gemeente een auteursrechtprobleem opleveren.

Bronnen: [https://www.heemskerk.nl/over-heemskerk/beeldbank](https://www.heemskerk.nl/over-heemskerk/beeldbank)

### HKH's eigen beeldbank: geen zichtbare API, legacy CGI-zoekinterface

De eigen beeldbank van de Historische Kring Heemskerk bevat op 2026-08-10 bevestigd 11.986 foto's, doorzoekbaar via een klassieke CGI-zoekinterface (velden, periode/jaar, weergave als galerij/lijst). Er is geen API, RSS, export of licentie-/hergebruikinformatie zichtbaar op de pagina; de pagina verwijst wel naar aanvullende eigen beeldbanken ('archief beeldbank', 'bibliotheek beeldbank'). Dit bevestigt dat koppeling hier alleen via direct contact/overleg met de beheerder haalbaar lijkt, zoals de eigenaar al vermoedde.

Bronnen: [https://www.historischekringheemskerk.nl/cgi-bin/beeldbank.pl](https://www.historischekringheemskerk.nl/cgi-bin/beeldbank.pl)

### Noord-Hollands Archief biedt echte machineleesbare open data met permissieve licentie

Noord-Hollands Archief heeft een expliciete 'Open Data'-pagina die downloadbare XML-bestanden aanbiedt (archieftoegangen in EAD-formaat; bevolkingsregisters en justitiële bronnen in A2A-standaard), vrij, gratis en anoniem toegankelijk zonder key, plus API-toegang via het Archives Portal Europe (APE). De pagina omschrijft open data als informatie die 'vrij beschikbaar is met een minimum aan beperkingen' en zonder auteursrecht van derden.

Bronnen: [https://noord-hollandsarchief.nl/collecties/open-data](https://noord-hollandsarchief.nl/collecties/open-data)

### opendata.archieven.nl (reeds in code gebruikt) bevestigt contract en verduidelijkt licentie

De officiële uitlegpagina van opendata.archieven.nl bevestigt exact het URI-patroon en de content-negotiation (JSON-LD/RDF/Turtle/N-Triples via Accept-header op `http://opendata.archieven.nl/id/<adtid>/<guid>`) die de bestaande `RestClientArchivesNlClient` in de backend-repository al gebruikt, en stelt dat de gegevens 'openbaar toegankelijk en auteursrechtenvrij' zijn, waarbij hergebruik in sommige gevallen een bronvermelding vereist. Dit verduidelijkt de licentieonzekerheid die een eerdere critic-iteratie rond deze integratie signaleerde.

Bronnen: [https://opendata.archieven.nl/nl/over-open-data](https://opendata.archieven.nl/nl/over-open-data), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/externalverification/ArchivesNlClient.kt](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/externalverification/ArchivesNlClient.kt)

### Huidige applicatie

**Doel:** De HKH-autopilot-app wil, conform de productvisie, de geschiedenis van Heemskerk toegankelijk maken door lokale bronnen (van de Historische Kring Heemskerk) te verbinden met bredere historische bronnen uit Noord-Holland, Nederland en daarbuiten, zodat iedereen vanuit een vraag, plek, persoon of gebeurtenis op ontdekking kan gaan. De eigenaar heeft bevestigd dat de doelgroep bewust zo breed mogelijk is (geen specifieke keuze voor bijvoorbeeld scholen of toeristen) en dat voor de komende cyclus prioriteit ligt bij het daadwerkelijk koppelen van externe bronnen, boven het uitwerken van vorm/UX.

**Wat ontbreekt:**
- De kernbelofte 'ontdekken vanuit plek, persoon of gebeurtenis' is nog niet volledig waargemaakt: het ontdekblok toont Plek- en Gebeurtenis-chips maar geen Persoon-chip, omdat geen gepubliceerd nieuwsbericht aan een gazetteer-persoon is gekoppeld (bevestigd via live inspectie op 2026-08-10).
- Er is geen enkele geautomatiseerde of bulk-koppeling met een externe historische bron; de admin ondersteunt uitsluitend handmatige intake van precies één record tegelijk, met alle velden met de hand ingevuld.
- De bestaande externe-verificatiefunctionaliteit (ArchivesNlClient) haalt alleen kernvelden (naam, geboorte-/sterftedatum, licentie) op voor verificatie van één record, en importeert geen volledige externe bronrecords of collecties.
- De door de eigenaar eerder als kansrijk aangemerkte bron Regionaal Archief Alkmaar noemt Heemskerk niet in zijn eigen, expliciet omschreven werkgebied, wat de haalbaarheid van deze route als primaire Heemskerk-bron relativeert.
- Zowel de eigen HKH-beeldbank als de gemeente Heemskerk-beeldbank zijn niet zomaar automatisch te ontsluiten: de gemeentebank is expliciet auteursrechtelijk beschermd met een toestemmingsvereiste, en de HKH-bank heeft geen zichtbare API/exportfunctie.
- Er bestaat nog geen kaart-, thema- of routegebaseerde ontdeklaag; de huidige presentatie is beperkt tot een lijst met nieuwsberichten plus zoekveld/chips.

### Verbetermogelijkheden

- Bouw een eerste geautomatiseerde koppeling met de Open Archieven 'hee'-dataset (persoon-/recordmatching) via de key-loze, wel gethrottelde (4 req/s) Search/Match-API, en documenteer expliciet dat de exacte hergebruikslicentie van deze dataset niet op de datasetpagina staat — navragen bij Open Archieven of Historische Kring Heemskerk voordat data breed herpubliceerd wordt.
- Geef Noord-Hollands Archief en opendata.archieven.nl prioriteit boven Regionaal Archief Alkmaar als bron voor automatische koppeling: beide bieden bevestigd vrije, machineleesbare data met een permissievere licentie-indicatie, terwijl RAA zijn eigen werkgebied expliciet zonder Heemskerk omschrijft.
- Breid de bestaande externe-verificatie-integratie met opendata.archieven.nl uit van 'alleen verifiëren' naar het daadwerkelijk tonen/opslaan van de citeerbare kernvelden (naam, data, licentie) bij een gekoppeld record, nu het contract en de licentiewoorden van die bron bevestigd zijn.
- Vermijd automatisch scrapen van de gemeente Heemskerk-beeldbank of de eigen HKH-beeldbank; beide vereisen expliciet menselijk overleg (auteursrecht resp. ontbrekende API) — leg dit vast als input voor een gesprek met de eigenaar over eventuele contactopname, in plaats van het als technische taak op te pakken.
- Overweeg op langere termijn een kaart- of routegebaseerde ontdeklaag (bijv. geïnspireerd op Erfgeod op de Kaart) zodra er daadwerkelijk meerdere externe bronnen gekoppeld zijn, zodat vorm/UX de al aanwezige brondiversiteit zichtbaar maakt in plaats van vooruit te lopen op nog niet bestaande koppelingen.

### Inspiratiebronnen

- [Erfgoed op de Kaart](https://www.erfgoedopdekaart.nl/) — Bestaand platform dat expliciet lokale historische informatie van 35+ archieven, musea en heemkundekringen verbindt via een kaartinterface met historische kaartlagen, GPS-gebaseerde ontdekking en thematische routes — een directe parallel met de HKH-missie om Heemskerk te verbinden met bredere bronnen, en een concreet vormvoorbeeld voor een toekomstige ontdeklaag zodra meer bronnen gekoppeld zijn.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl) | 2026-08-10 | Niet-productie acceptatieomgeving met representatieve nepdata; geen publieke licentie van toepassing, uitsluitend voor eigen productonderzoek geraadpleegd. | Directe, actuele inspectie van de draaiende HKH-autopilot-app om de huidige staat van het ontdekblok/entiteitschips vast te stellen. |
| [bron](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/) | 2026-08-10 | Niet-productie acceptatieomgeving; geen publieke licentie van toepassing, uitsluitend voor eigen productonderzoek geraadpleegd. | Inspectie van het beheergedeelte om de daadwerkelijke intakemogelijkheden (handmatig vs. bulk/automatisch) voor externe bronnen vast te stellen. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/externalverification/ArchivesNlClient.kt) | 2026-08-10 | Repository-inhoud van het productteam; rechten liggen bij de producteigenaar/Product Factory, geen apart open-sourcelicentiebestand aangetroffen tijdens dit bezoek. | Broncode van de bestaande archieven.nl-integratie, gebruikt om het URI-patroon en contract te vergelijken met de officiële documentatie van opendata.archieven.nl. |
| [bron](https://www.openarchieven.nl/dashboard/hee) | 2026-08-10 | Publieke aggregatorpagina van Open Archieven; geen expliciete hergebruikslicentie op deze pagina vermeld, rechten op onderliggende data onbekend. | Officiële bron voor de omvang en herkomst van de Historische Kring Heemskerk-dataset ('hee') binnen Open Archieven, eerder als kansrijke bron genoemd door de eigenaar. |
| [bron](https://www.openarchieven.nl/api/docs/) | 2026-08-10 | Publieke API-documentatie; geen expliciete datalicentie vermeld, wel vrije toegang zonder API-key met throttling. | Vaststellen van technische toegankelijkheid (wel/geen key nodig, ratelimiet, endpoints) van de Open Archieven-API voor eventuele koppeling. |
| [bron](https://www.regionaalarchiefalkmaar.nl/over-ons/open-data) | 2026-08-10 | Officiële pagina van een overheids-/archiefinstelling, expliciet gepresenteerd als 'Open data'; gericht op vrij hergebruik, exacte licentie per subcollectie niet op deze pagina volledig gespecificeerd. | Verifiëren of Heemskerk daadwerkelijk binnen het werkgebied van Regionaal Archief Alkmaar valt, zoals de eigenaar had gevraagd na te gaan. |
| [bron](https://www.heemskerk.nl/over-heemskerk/beeldbank) | 2026-08-10 | Gemeentelijke website; pagina vermeldt expliciet auteursrechtelijke bescherming van de foto's, hergebruik elders vereist voorafgaande toestemming van de gemeente. | Toegankelijkheid en licentiestatus van de gemeente Heemskerk-beeldbank vaststellen, zoals door de eigenaar als openstaand punt benoemd. |
| [bron](https://www.historischekringheemskerk.nl/cgi-bin/beeldbank.pl) | 2026-08-10 | Eigen beeldbank van de Historische Kring Heemskerk; geen licentie- of hergebruikinformatie zichtbaar op de pagina zelf, rechten onbekend. | Vaststellen van omvang, zoekmogelijkheden en (afwezigheid van) API/exportopties van de eigen HKH-beeldbank, waarvoor de eigenaar overleg/toestemming als vervolgstap noemde. |
| [bron](https://noord-hollandsarchief.nl/collecties/open-data) | 2026-08-10 | Officiële pagina van een archiefinstelling; stelt dat gegevens vrij, gratis en anoniem te downloaden zijn en in beginsel zonder auteursrecht van derden, met soms een attributievereiste bij hergebruik. | Toegankelijkheid van Noord-Hollands Archief controleren, een door de eigenaar expliciet genoemd nog te checken bron. |
| [bron](https://opendata.archieven.nl/nl/over-open-data) | 2026-08-10 | Officiële pagina van archieven.nl/opendata.archieven.nl; stelt dat gegevens openbaar toegankelijk en auteursrechtenvrij zijn, hergebruik soms met attributievereiste. | Verduidelijken van de licentie- en contractdetails van het reeds in de code geïntegreerde opendata.archieven.nl-endpoint, om een eerder door een critic gesignaleerde onzekerheid te adresseren. |
| [bron](https://www.erfgoedopdekaart.nl/) | 2026-08-10 | Publieke marketingpagina van een commercieel/non-profit platform; eigen content, niet als open dataset geraadpleegd maar uitsluitend als vormgevings-/conceptinspiratie. | Vergelijkbaar bestaand platform gevonden dat, net als de HKH-missie, lokale historische bronnen van tientallen instellingen verbindt via kaart, GPS en thematische routes. |

## Productbeslissing

Verdiep in deze cyclus de bestaande opendata.archieven.nl-integratie (ArchivesNlClient) van 'alleen verifiëren' naar het daadwerkelijk vastleggen en tonen van de citeerbare kernvelden (naam, geboorte-/sterftedatum, licentie, duurzame bron-URI) bij een gekoppeld HKH-record. Dit is de enige nieuwe koppeling die deze cyclus wordt opgepakt: geen nieuwe externe bron-integraties (Open Archieven, Noord-Hollands Archief, beeldbanken), geen kaart-/route-UX, en geen actie van de eigenaar nodig omdat de bron keyloos en licentie-bevestigd open is.

**Waarom:** De eigenaar heeft voor deze cyclus prioriteit gegeven aan het daadwerkelijk koppelen van externe bronnen boven vorm/UX. Van alle onderzochte bronnen is opendata.archieven.nl de enige die tegelijk (a) al technisch geïntegreerd is in de code, (b) bevestigd keyloos en met een expliciete, permissieve licentie-indicatie toegankelijk is, en (c) direct de productprincipes 'Betrouwbaar' (herleidbaar tot bronnen) en 'Verbonden' (Heemskerk nooit een geïsoleerd eiland) waarmaakt. Andere kansrijke bronnen (Open Archieven, Noord-Hollands Archief) zijn wel open maar vragen een nieuwe integratie of hebben onduidelijke hergebruikslicentie; RAA dekt Heemskerk niet; de beeldbanken vragen mensontsluiting die buiten autonome Product/Software Factory-uitvoering valt. Door één bestaande, laagrisico-koppeling te verdiepen ontstaat een kleine, samenhangende, zelfstandig uitvoerbare stap zonder dat een token of menselijke actie van de eigenaar nodig is.

### Prioriteiten
- Verdiep de bestaande, licentie-bevestigde opendata.archieven.nl-koppeling van verificatie naar het daadwerkelijk tonen/opslaan van citeerbare brondata bij gekoppelde records
- Respecteer de attributievereiste van opendata.archieven.nl bij het tonen van gekoppelde brondata
- Houd Regionaal Archief Alkmaar buiten scope zolang Heemskerk-dekking niet bevestigd is
- Automatiseer geen ontsluiting van de gemeente- of HKH-beeldbank zonder expliciete rechtenverheldering door de eigenaar
- Houd de scope deze cyclus klein: geen nieuwe ontdek-UX, geen nieuwe brono-integraties naast het verdiepen van de bestaande

### Besluiten
- **Verdiep de bestaande opendata.archieven.nl-integratie (ArchivesNlClient) van 'alleen verifiëren' naar het daadwerkelijk opslaan en tonen van de citeerbare kernvelden (naam, geboorte-/sterftedatum, licentie, duurzame bron-URI) bij een gekoppeld HKH-record.** — De backend heeft al een werkend, keyloos contract met opendata.archieven.nl waarvan nu bevestigd is dat de data openbaar toegankelijk en auteursrechtenvrij is (met soms een attributievereiste). Dit is de kleinste samenhangende stap die een bestaande, licentie-bevestigde koppeling volledig benut en direct de productprincipes 'Betrouwbaar' en 'Verbonden' waarmaakt, zonder nieuwe externe toegang of tokens nodig te hebben.
- **Regionaal Archief Alkmaar wordt deze cyclus niet ingezet als bron voor automatische Heemskerk-koppeling.** — RAA omschrijft zijn eigen werkgebied expliciet als Alkmaar en acht andere gemeenten, zonder Heemskerk te noemen. Automatisch koppelen zou daarmee geen gegarandeerd Heemskerk-relevante data opleveren.
- **Geen geautomatiseerde ontsluiting of scraping van de gemeente Heemskerk-beeldbank of de eigen HKH-beeldbank in deze cyclus.** — De gemeentelijke beeldbank is expliciet auteursrechtelijk beschermd met een toestemmingsvereiste, en de HKH-beeldbank heeft geen zichtbare API of licentie-informatie. Beide vragen mensontsluiting/overleg vooraf, wat buiten de scope van autonoom uitvoerbare Product/Software Factory-taken valt.
- **De Open Archieven 'hee'-dataset (persoon-/recordmatching) wordt als kansrijke vervolgstap genoteerd, maar niet deze cyclus gestart, in afwachting van duidelijkheid over de hergebruikslicentie.** — De dataset is technisch vrij bevraagbaar zonder key (met 4 req/s throttling), maar er is geen expliciete hergebruikslicentie gevonden op de dataset- of API-documentatiepagina. Breed herpubliceren zonder licentiezekerheid past niet bij het productprincipe 'Betrouwbaar'.
- **Een kaart- of routegebaseerde ontdeklaag (geïnspireerd op Erfgoed op de Kaart) wordt uitgesteld tot er daadwerkelijk meerdere externe bronnen gekoppeld zijn.** — Vorm/UX-werk is deze cyclus door de eigenaar bewust lager geprioriteerd dan het daadwerkelijk koppelen van bronnen; een kaartlaag zou nu vooruitlopen op brondiversiteit die er nog niet is.

## UX-voorstel: Brongegevens opendata.archieven.nl vastleggen en tonen bij record-intake

**Gebruikersdoel:** Als beheerder van HKH-autopilot wil ik dat wanneer ik bij record-intake een externe conceptkoppeling naar opendata.archieven.nl invul, de citeerbare kernvelden (naam, geboorte-/sterftedatum, licentie, duurzame bron-URI) automatisch worden opgehaald, getoond ter controle, en na bevestiging vastgelegd bij het record — zodat het record herleidbaar, betrouwbaar en correct bronvermeld is, zonder dat dit het opslaan blokkeert als de bron niet bereikbaar is.

### Flow
1. Beheerder opent 'Nieuwe record-intake' (of bewerkt bestaand record) en vult zoals nu al kan het optionele veld 'Externe conceptkoppeling' met een duurzame opendata.archieven.nl-URI plus koppelmotivering en onzekerheid.
2. Bij het verlaten van het URI-veld (of via expliciete 'Ophalen'-knop) roept het systeem de bestaande ArchivesNlClient aan om de externe bron te bevragen, net als bij de huidige verificatiestap.
3. Systeem toont in een nieuw, niet-blokkerend paneel 'Brongegevens (extern, ter controle)' de opgehaalde kernvelden: naam, geboortedatum, sterftedatum, licentie/rechtenstatus en de duurzame bron-URI, vóór opslag.
4. Beheerder controleert de getoonde kernvelden, past zo nodig koppelmotivering/onzekerheid aan, en bevestigt expliciet (aparte bevestigingsactie, geen impliciete acceptatie).
5. Bij bevestigen slaat het systeem de opgehaalde kernvelden samen met ophaaldatum en bron-URI bij het record op (in plaats van alleen een verificatie-vlag zoals nu).
6. Als de externe bron niet bereikbaar is of geen match geeft, toont het paneel een duidelijke foutstatus/lege-staat; het record kan zonder externe verrijking worden opgeslagen (opslaan wordt niet geblokkeerd).
7. Op de publieke recorddetail-/nieuwsberichtpagina toont het systeem een 'Bron'-citatieblok met de vastgelegde kernvelden, de bron-URI en de vereiste attributietekst, alleen wanneer kernvelden daadwerkelijk zijn vastgelegd.

### Wireframe

ADMIN — Nieuwe record-intake (bestaand formulier, uitgebreid)
┌─────────────────────────────────────────────────────────┐
│ Lokale identifier: [____________]                       │
│ Titel:             [____________]                       │
│ Beschrijving:      [____________]                       │
│ Datering:          [____________]                       │
│ Herkomst:           [____________]                       │
│ Rechtenstatus:      [____________]                       │
│ Privacyclassificatie:[__ dropdown __]                    │
│                                                           │
│ Externe conceptkoppeling (optioneel)                     │
│ Duurzame URL: [https://opendata.archieven.nl/id/...] [Ophalen]│
│ Koppelmotivering: [____________]                        │
│ Onzekerheid:       [__ dropdown __]                       │
│                                                           │
│ ── Brongegevens (extern, ter controle) [aria-live] ──    │
│ Status: ● Geverifieerd / ○ Geen match / ○ Niet bereikbaar│
│ Naam:            Jan Klaasz de Boer                      │
│ Geboortedatum:    12-03-1841                              │
│ Sterftedatum:     04-11-1902                               │
│ Licentie:         Auteursrechtenvrij (attributie vereist) │
│ Bron-URI:         https://opendata.archieven.nl/id/...    │
│                                                            │
│ [ Bevestig brongegevens en gebruik bij record ]           │
│ [ Sla op zonder externe brongegevens ]                     │
│                                                            │
│ [Opslaan record]                                          │
└─────────────────────────────────────────────────────────┘

PUBLIEK — Recorddetail / nieuwsbericht (uitbreiding)
┌─────────────────────────────────────────────────────────┐
│ <Titel nieuwsbericht>                                     │
│ <Beschrijving...>                                          │
│                                                            │
│ <cite> Bron                                                │
│   Jan Klaasz de Boer (12-03-1841 – 04-11-1902)             │
│   Bron: opendata.archieven.nl — auteursrechtenvrij,        │
│   bronvermelding vereist. [Bekijk bron ↗]                  │
│ </cite>                                                     │
└─────────────────────────────────────────────────────────┘
(Bronblok verschijnt uitsluitend als kernvelden zijn vastgelegd; anders geen blok.)

### Interactiehypotheses
- Bij een geldige opendata.archieven.nl-URI toont het brongegevens-paneel de opgehaalde kernvelden (naam, geboorte-/sterftedatum, licentie, bron-URI) binnen de opgegeven timeout — geautomatiseerd te testen met een e2e-test die een bekende geldige URI invoert en de aanwezigheid van elk veld in de DOM controleert.
- Bij een ongeldige of niet-matchende URI toont het paneel een expliciete foutstatus en blokkeert dit het opslaan van het record niet — geautomatiseerd te testen door een niet-bestaande/foutieve URI te simuleren en te controleren dat de opslaan-actie beschikbaar blijft.
- Het publieke broncitatieblok verschijnt uitsluitend wanneer kernvelden daadwerkelijk zijn vastgelegd bij het record, nooit als leeg of gedeeltelijk blok — testbaar via DOM-snapshot-assertions voor records met en zonder vastgelegde brongegevens.
- De vereiste attributietekst wordt consistent naast de bron-URI getoond conform de licentie-indicatie van opendata.archieven.nl — geautomatiseerd te testen door te controleren dat de vaste attributiestring aanwezig is in het bronblok.
- Alle interactieve elementen in het brongegevens-paneel (Ophalen-knop, bevestigingsactie, alternatieve opslaan-zonder-verrijking-actie) zijn volledig bedienbaar met alleen het toetsenbord en hebben correcte ARIA-labels — geautomatiseerd te testen met een axe-core-scan plus een keyboard-only e2e-navigatietest.

### Toegankelijkheid
- Het URI-invoerveld heeft een expliciet gekoppeld <label> en foutmeldingen worden via aria-describedby aan het veld gekoppeld.
- Het paneel 'Brongegevens (extern, ter controle)' is een aria-live="polite"-regio zodat schermlezers de opgehaalde data automatisch aankondigen zodra deze binnenkomt, zonder focus te forceren.
- Statuslabels (Geverifieerd/Geen match/Niet bereikbaar) voldoen aan WCAG AA-kleurcontrast (minimaal 4.5:1) en worden niet uitsluitend met kleur gecommuniceerd, maar ook met tekst/icoon.
- Alle acties (Ophalen, Bevestig brongegevens, Sla op zonder externe brongegevens, Opslaan record) zijn bereikbaar en bedienbaar via Tab/Enter/Spatie in een logische, voorspelbare focusvolgorde.
- Het publieke broncitatieblok gebruikt semantische opmaak (bijv. <cite>/<blockquote> met duidelijke koppen) zodat het als samenhangend geheel door een schermlezer wordt voorgelezen.
- Foutmeldingen bij een niet-bereikbare externe bron zijn tekstueel duidelijk, niet alleen kleur- of icoongebaseerd, en programmatisch gekoppeld aan het relevante veld.

### Privacy
- Alleen de functioneel noodzakelijke citatievelden (naam, geboorte-/sterftedatum, licentie, bron-URI) worden opgeslagen; overige persoonsgegevens uit de externe API-respons worden niet gekopieerd of bewaard.
- De ruwe API-response van opendata.archieven.nl wordt niet permanent opgeslagen, alleen de gestructureerde kernvelden, om scope-creep van dataverzameling te voorkomen.
- Ophaaldatum en bron-URI worden vastgelegd uitsluitend voor herleidbaarheid/auditdoeleinden van het record, niet voor overige verwerking.
- De bestaande 'privacyclassificatie'-vraag in het intakeformulier wordt hergebruikt om expliciet af te wegen of de gekoppelde persoon mogelijk nog in leven is, vóór de externe gegevens publiek getoond worden.
- De attributievereiste van opendata.archieven.nl wordt consequent nageleefd bij elke publieke weergave van de gekoppelde brongegevens, in plaats van data zonder bronvermelding te herpubliceren.
- Foutmeldingen en eventuele logging rond het ophalen bevatten geen persoonsgegevens verder dan strikt noodzakelijk voor technische diagnose.

## Kritische beoordeling

**Oordeel:** ACCEPT

De enige kandidaat ("extern-brongegevens-vastleggen-bij-intake") verdiept de al gepubliceerde, keyloze opendata.archieven.nl-koppeling (kandidaat 18) van verificatie naar daadwerkelijke, citeerbare vastlegging van kernvelden, hard gekoppeld aan de bestaande fail-closed AVG-classificatie (kandidaat 17/20/21) plus een nieuwe, aanvullende fail-closed check op tegenstrijdige verse externe data. Het onderzoek dat eraan voorafgaat is zorgvuldig: elke bevinding heeft een expliciet geraadpleegde bron met datum en rechten-/licentie-indicatie, en kansrijke maar risicovolle routes (Open Archieven 'hee' zonder expliciete licentie, RAA dat Heemskerk niet dekt, gemeente-/HKH-beeldbanken die auteursrecht resp. ontbrekende API vereisen) worden terecht uitgesteld of afgewezen in plaats van als taak opgepakt. De eerder voorgestelde publieke citatieweergave is bewust geschrapt om geen conflict te creëren met kandidaat 35, die record-intake- en privacyclassificatiegegevens expliciet van publieke/REST-blootstelling uitsluit. Alle acceptatiecriteria zijn agent-uitvoerbaar (backend-asserties, gemockte externe respons, e2e/axe-core/keyboard-tests) zonder dat een menselijke actie, token-aanvraag of ander eigenaarsbesluit nodig is, wat voldoet aan de harde autonomie-gate. Er zijn geen BLOCKING issues; enkele kleine, niet-blokkerende aandachtspunten worden hieronder genoemd.
- **WARNING · CONSISTENCY** — Het veld 'dependsOn' van de kandidaat is leeg, terwijl de beschrijving expliciet en meermaals bouwt op reeds gepubliceerde kandidaten 16, 17, 18, 19, 20, 21 en 35. Dit metadata-veld zou de tekstuele afhankelijkheden moeten weerspiegelen voor betere traceerbaarheid door de orchestrator.
- **INFO · PRIVACY** — De privacyoverweging uit het flow-document ('foutmeldingen en logging bevatten geen persoonsgegevens verder dan strikt noodzakelijk') is niet expliciet terug te vinden als apart toetsbaar acceptatiecriterium in de kandidaat zelf; AC7 dekt alleen opslag, niet logging.
- **INFO · SOURCE** — Het onderzoek benoemt correct en expliciet dat de Open Archieven 'hee'-dataset geen bevestigde hergebruikslicentie heeft en stelt terecht voor deze route deze cyclus niet te starten — goede toepassing van het bronnenprincipe.
- **INFO · SCOPE** — De eerder in het flow-/wireframe-document voorgestelde publieke broncitatieweergave wordt in de uiteindelijke kandidaat expliciet geschrapt om scope-conflict met kandidaat 35 (die record-intake-/privacyclassificatiegegevens van publieke blootstelling uitsluit) te vermijden; dit is correct zelf-gecorrigeerd binnen de inzending.

## Geaccepteerde storykandidaten

### Leg citeerbare kernvelden van opendata.archieven.nl alleen vast bij bevestigde koppeling, fail-closed 'Processable'-classificatie én consistente verse brondata

_Sleutel: `extern-brongegevens-vastleggen-bij-intake`_

Breid de bestaande 'Nieuwe record-intake'-flow en de werkende, keyloze ArchivesNlClient-integratie (opendata.archieven.nl, JSON-LD content-negotiation op http://opendata.archieven.nl/id/<adtid>/<guid>) uit van 'alleen verifiëren' naar 'daadwerkelijk vastleggen'. Bij invullen/verlaten van het veld 'Externe conceptkoppeling' (of klik op 'Ophalen', met debounce/cooldown zodat opeenvolgende wijzigingen niet elk een eigen aanroep triggeren) bevraagt het systeem ArchivesNlClient en toont de kernvelden (naam, geboortedatum, sterftedatum, licentie, bron-URI) in een niet-blokkerend paneel 'Brongegevens (extern, ter controle)' met statuslabel (Geverifieerd/Geen match/Niet bereikbaar). De beheerder bevestigt expliciet via 'Bevestig brongegevens en gebruik bij record'. Persistentie van naam en geboorte-/sterftedatum blijft hard gekoppeld aan de gepubliceerde fail-closed AVG-classificatie (kandidaat 17/20/21): alleen bij status 'Processable' worden deze velden gepersisteerd; bij 'Blocked' of onbekende classificatie weigert het systeem vastlegging, ook na bevestiging, met expliciete blokkeringsmelding. Nieuw t.o.v. de vorige versie (verwerking van de niet-blokkerende WARNING): zelfs bij lokale classificatie 'Processable' voert het systeem een aanvullende, onafhankelijke fail-closed check uit op de zojuist opgehaalde externe data zelf. Spreekt de externe data de lokale classificatiebasis tegen — bv. geen sterftedatum gevonden voor de gematchte persoon, terwijl de lokale 'Processable'-status uitging van bevestigd overlijden — dan weigert het systeem alsnog persistentie van naam en geboorte-/sterftedatum, ongeacht lokale status, en toont een expliciete waarschuwing dat de externe bron het overlijden niet bevestigt. Niet-persoonsgebonden velden (licentie, bron-URI, ophaaldatum) mogen altijd vastgelegd worden. Alternatief: 'Sla op zonder externe brongegevens'. Bij onbereikbare bron of geen match toont het paneel een foutstatus zonder opslaan te blokkeren. Uitsluitend gestructureerde kernvelden worden opgeslagen, nooit de ruwe API-respons. Scope: deze story wijzigt het opslagmodel van het gepubliceerde record-intake-domein (kandidaat 16/18/19) door velden toe te voegen die uitsluitend gevuld worden onder de bestaande fail-closed classificatiegate (kandidaat 17/20/21) plus deze verse-data-consistentiecheck; geen nieuw extern protocol, token of menselijke tussenstap naast de bestaande beheerdersbevestiging. De eerder voorgestelde publieke citatieweergave is deze cyclus geschrapt: er is geen bevestigde publieke detailpagina voor record-intake-/genealogische records, en de bevestigde publieke laag (nieuwsbericht-discoverydomein, kandidaat 35/36) sluit privacyclassificatie- en record-intakegegevens expliciet uit van publieke/REST-blootstelling om precies dit lekrisico te voorkomen. Deze kandidaat levert dus uitsluitend interne, citeerbare vastlegging, zonder publieke weergave.

**Acceptatiecriteria**
- Gegeven een geldige opendata.archieven.nl-URI in het conceptkoppelingsveld, wanneer de beheerder 'Ophalen' activeert of het veld verlaat, dan toont het paneel binnen de opgegeven timeout de velden naam, geboortedatum, sterftedatum, licentie en bron-URI, en wordt bij snel opeenvolgende invoerwijzigingen slechts één netwerkaanroep naar ArchivesNlClient gedaan dankzij debouncing — geautomatiseerd verifieerbaar met een e2e-test die veldwaarden in de DOM controleert en een test die snel herhaalde inputwijzigingen simuleert en het aantal netwerkaanroepen telt.
- Gegeven een ongeldige of niet-matchende URI, wanneer het ophalen wordt uitgevoerd, dan toont het paneel een expliciete foutstatus ('Geen match' of 'Niet bereikbaar') en blijft de actie 'Opslaan record' beschikbaar en functioneel — geautomatiseerd verifieerbaar door een gesimuleerde foutieve URI en een assertie dat opslaan alsnog slaagt.
- Gegeven getoonde brongegevens bij een record waarvan de bestaande fail-closed AVG-classificatie (kandidaat 17/20/21) status 'Processable' oplevert én de externe data een sterftedatum bevestigt die niet tegenstrijdig is met de lokale classificatiebasis, wanneer de beheerder 'Bevestig brongegevens en gebruik bij record' activeert en opslaat, dan bevat het opgeslagen record de kernvelden (naam, geboorte-/sterftedatum, licentie, bron-URI, ophaaldatum) — geautomatiseerd verifieerbaar via een backend-/API-assertie na opslag.
- Gegeven getoonde brongegevens bij een record waarvan de classificatie status 'Blocked' heeft óf nog niet is uitgevoerd, wanneer de beheerder desondanks 'Bevestig brongegevens en gebruik bij record' activeert, dan weigert het systeem het persisteren van naam en geboorte-/sterftedatum en toont een expliciete blokkeringsmelding die verwijst naar de classificatiestatus — geautomatiseerd verifieerbaar via een backend-assertie dat deze twee velden leeg blijven ondanks de bevestigingsactie.
- Gegeven een record met lokale classificatiestatus 'Processable' op basis van een bevestigd overlijden, wanneer de zojuist opgehaalde externe brongegevens geen sterftedatum bevatten voor de gematchte persoon (tegenspraak met de lokale classificatiebasis), dan weigert het systeem alsnog de persistentie van naam en geboorte-/sterftedatum en toont een expliciete waarschuwing die de tegenspraak benoemt — geautomatiseerd verifieerbaar via een backend-test met een gefixeerde externe respons zonder sterftedatum tegen een lokaal 'Processable'-record.
- Gegeven getoonde brongegevens, wanneer de beheerder in plaats daarvan 'Sla op zonder externe brongegevens' activeert, dan wordt het record opgeslagen zonder dat enige externe kernvelden bij het record worden vastgelegd — geautomatiseerd verifieerbaar via een backend-assertie dat de betreffende velden leeg blijven.
- Een geautomatiseerde test op de backend-opslaglaag bevestigt dat uitsluitend de gestructureerde kernvelden worden gepersisteerd en dat de volledige/ruwe externe API-respons nergens wordt opgeslagen.
- Het paneel 'Brongegevens (extern, ter controle)' is een aria-live="polite"-regio en alle interactieve elementen (Ophalen, Bevestig brongegevens, Sla op zonder externe brongegevens) zijn volledig bedienbaar met Tab/Enter/Spatie in een logische focusvolgorde — geautomatiseerd verifieerbaar met een axe-core-scan en een keyboard-only e2e-test, volgens de vastgelegde Flutter-web-a11y-inspectietechniek (flt-semantics-placeholder + CDP AX-boom).

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/externalverification/ArchivesNlClient.kt](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/externalverification/ArchivesNlClient.kt), [https://opendata.archieven.nl/nl/over-open-data](https://opendata.archieven.nl/nl/over-open-data), [https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/)

Risico's: Serverwijde afdwinging is vereist: de weigering van persistentie bij 'Blocked'/onbekende classificatie of bij tegenstrijdige verse externe data moet op serverniveau afgedwongen worden, niet alleen in de UI, zodat een gemanipuleerde clientaanroep niet alsnog kan opslaan., opendata.archieven.nl zelf documenteert geen expliciet rate limit op het bevraagde URI-patroon; de 4 req/s-throttling die eerder is aangetroffen geldt voor de afzonderlijke Open Archieven 'hee'-API en niet voor dit endpoint. Toch beperkt debouncing van de 'Ophalen'-actie onnodige belasting en voorkomt het race conditions tussen snel opeenvolgende invoerwijzigingen., Als de externe bron tijdelijk afwijkende of onvolledige data teruggeeft (bv. wél sterftedatum bij een volgende poging), kan herhaald ophalen tot wisselende blokkeringsuitkomsten leiden; dit is bedoeld fail-closed gedrag maar kan de beheerder verwarren zonder duidelijke, herhaalde uitleg in de waarschuwingstekst.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
