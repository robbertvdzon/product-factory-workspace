---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0062
date: 2026-08-13
status: approved
sources:
  - https://github.com/robbertvdzon/hkh-autopilot
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl
  - https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/
  - https://api.europeana.eu/en
  - https://www.europeana.eu/en/explore
  - https://www.europeana.eu/en/themes
  - https://www.europeana.eu/en/stories
  - https://www.openarchieven.nl/datasets/
---
# Productcyclus 62

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De belangrijkste onbeantwoorde productvraag is hoe bezoekers vanuit een historisch zoekresultaat begrijpelijk kunnen doorontdekken welke bronnen inhoudelijk samenhangen, zonder dat een zoekingang of metadata-overlap als bewezen historische relatie wordt gelezen. De huidige app heeft hiervoor al een veilige basis, maar de verbinding blijft smal en lokaal aan de resultatenpagina gebonden.

### Huidige applicatiedoel en route

De publieke Flutter-app ‘Historisch Heemskerk’ richt zich op een brede doelgroep en biedt historische zoeking in Europeana en Open Archieven. De app toont resultaten, bronstatus, bronidentifier, stabiele URI, ophaaldatum, rechtenstatus, privacystatus en een externe bronlink.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md), [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl)

### Huidige vervolgontdekking

Vanuit resultaatdetails zijn vervolgzoekingen beschikbaar voor aanwezige, zekere plaats-, persoons-, gebeurtenis- en periodewaarden. De oorspronkelijke bronwaarde wordt exact gebruikt en de interface vermeldt dat dit geen bewezen relatie tussen bronnen is.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart)

### Beperkte relatiebasis

De huidige relatiepresentatie vergelijkt alleen zekere, genormaliseerde plaats-, persoons- en gebeurtenisvelden binnen de zichtbare resultatenpagina en toont maximaal drie resultaten. Periode-overlap vormt op zichzelf geen relatie.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart)

### Bron- en dekkingsbeperking

De implementatie gebruikt slechts Europeana en Open Archieven. De lokale Heemskerk-indicatie is gebaseerd op zekere plaatsmetadata en wordt expliciet niet als historisch bewijs gepresenteerd, maar de onderzochte code onderbouwt niet hoe representatief of volledig die lokale dekking is.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt)

### Acceptatie-UI kon beperkt worden beoordeeld

De publieke acceptatieomgeving levert een Flutter-shell met de titel ‘Historisch Heemskerk’; de adminomgeving heeft de titel ‘HKH Beheer’. Screenshotcontrole via Playwright is uitgevoerd maar Chromium/Chrome beëindigde lokaal met een macOS bootstrap/Mach-port permission error. Daarom zijn geen inhoudelijke visuele claims over de canvas-UI gedaan.

Bronnen: [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl), [https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/)

### Europeana biedt thematische en verhalende navigatie

Europeana combineert zoeken in cultureel-erfgoedmetadata met thematische ingangen en geredigeerde verhalen over personen, plaatsen en ideeën. Dit laat zien dat een zoekroute kan worden aangevuld met begrijpelijke thematische en narratieve oriëntatie.

Bronnen: [https://www.europeana.eu/en/explore](https://www.europeana.eu/en/explore), [https://www.europeana.eu/en/themes](https://www.europeana.eu/en/themes), [https://www.europeana.eu/en/stories](https://www.europeana.eu/en/stories)

### Open Archieven biedt rijkere relatie- en zoekmogelijkheden

Open Archieven ondersteunt zoeken, matchen, recordweergave, statistieken en gevonden links naar externe bronnen. De API biedt bovendien machineleesbare JSON, JSON-LD, XML en GEDCOM-representaties via stabiele URI’s en content negotiation.

Bronnen: [https://www.openarchieven.nl/datasets/](https://www.openarchieven.nl/datasets/), [https://www.openarchieven.nl/api/docs/uri.php](https://www.openarchieven.nl/api/docs/uri.php), [https://www.openarchieven.nl/search-ext.php?lang=nl](https://www.openarchieven.nl/search-ext.php?lang=nl)

### Kaart en tijd zijn bruikbare oriëntatiemodellen

Amsterdam Time Machine combineert locatiegebonden bronontsluiting met een kaart, tijdlijn en zichtbare datadichtheid. Dit is relevant als inspiratie voor het begrijpelijk tonen van lokale dekking en historische lacunes, zonder te suggereren dat afwezigheid van data gelijkstaat aan afwezigheid van geschiedenis.

Bronnen: [https://data.amsterdamtimemachine.nl/about](https://data.amsterdamtimemachine.nl/about), [https://www.amsterdamtimemachine.nl/nl/](https://www.amsterdamtimemachine.nl/nl/)

### Huidige applicatie

**Doel:** De applicatie maakt Heemskerkse geschiedenis toegankelijk voor een brede doelgroep door vanuit gewone zoekvragen historische metadata uit lokale en externe collecties te ontsluiten. De actuele publieke route zoekt in Europeana en Open Archieven en toont herleidbare broncontext, bronstatus en veilige vervolgzoekingen.

**Wat ontbreekt:**
- De relatiepresentatie is beperkt tot exacte overlap binnen één zichtbare resultatenpagina en biedt geen bredere, controleerbare verbinding tussen collecties.
- De app toont geen aantoonbare naamvarianten, gecontroleerde entiteiten, synoniemen of expliciete bronmatches als afzonderlijke, herleidbare concepten.
- De betekenis van de lokale Heemskerk-indicatie, de dekking en structurele lacunes worden onvoldoende uitgelegd.
- Er is geen kaart-, tijdlijn- of thematische oriëntatielaag zichtbaar in de onderzochte implementatie.
- De concrete koppeling van een lokaal HKH-record aan een extern record is niet aangetoond.
- De canvas-gebaseerde acceptatie-UI kon door de lokale browserfout niet op leesvolgorde, begrijpelijkheid, focus of visuele bruikbaarheid worden beoordeeld.
- De actuele repository toont geen aangetroffen LICENSE-bestand; concrete rechten voor repositoryhergebruik blijven daardoor onbekend.

### Verbetermogelijkheden

- Maak per resultaat expliciet onderscheid tussen ‘zelfde metadatawaarde’, ‘nieuwe zoekingang’ en ‘door de bron vastgelegde relatie’, met een korte uitleg van de bewijssterkte.
- Gebruik stabiele identifiers en machineleesbare bronrelaties van Open Archieven waar die werkelijk door de bron worden geleverd; presenteer zulke relaties als bronclaims en niet als door HKH afgeleide feiten.
- Onderzoek gecontroleerde naam- en plaatsentiteiten of naamvarianten als optionele vervolgzoekhulp, waarbij de oorspronkelijke waarde, afgeleide term en bron van de variant zichtbaar blijven.
- Toon per zoekopdracht een compacte dekkingssamenvatting: geraadpleegde bronnen, beschikbare/uitgevallen bronnen, aantallen en betekenis van de lokale indicatie.
- Onderzoek een kaart- en tijdlijnlaag voor Heemskerk naar het model van Amsterdam Time Machine, maar maak datadichtheid en ontbrekende data zichtbaar als dekking, niet als historische zekerheid.
- Gebruik thematische of geredigeerde verhaalingangen naar voorbeeld van Europeana om bezoekers zonder voorkennis te laten starten vanuit onderwerp, plek of periode.
- Voer de ontbrekende browsergebaseerde bruikbaarheidstoets opnieuw uit in een omgeving waarin Flutter CanvasKit en semantiek betrouwbaar kunnen worden geïnspecteerd.
- Beperk elke uitbreiding tot metadata en externe bronlinks totdat per bron concrete rechten- en privacystatus is vastgesteld; kopieer geen media en sla geen persoonsgegevens of klikgeschiedenis op.

### Inspiratiebronnen

- [Amsterdam Time Machine](https://data.amsterdamtimemachine.nl/about) — Combineert kaart, tijdlijn, locatiegebonden bronnen, zichtbare datadichtheid en links naar oorspronkelijke bronnen; relevant voor lokale dekking en historische context.
- [Europeana Explore, Themes en Stories](https://www.europeana.eu/en/explore) — Combineert zoeken met thematische navigatie en geredigeerde verhalen; relevant voor toegankelijke ontdekking zonder voorafgaande archiefkennis.
- [Open Archieven API en content negotiation](https://www.openarchieven.nl/api/docs/uri.php) — Laat zien hoe stabiele URI’s, bronrecords, externe links en meerdere machineleesbare representaties vervolgonderzoek herleidbaar kunnen maken.
- [Historypin](https://www.historypin.org/en/home/) — Publiek voorbeeld van plaatsgebonden historische foto’s, verhalen en collecties; bruikbaar als inspiratie voor locatie- en verhaalgebaseerde ontdekking, met aandacht voor privacy en rechten.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://github.com/robbertvdzon/hkh-autopilot) | 2026-08-13 | Publieke GitHub-repository; in de geraadpleegde root is geen LICENSE- of LICENSE.md-bestand aangetroffen, waardoor de concrete repositorylicentie onbekend is. | Verwijzing naar de actuele publieke productrepository en controle van de aanwezige licentie-indicatie. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md) | 2026-08-13 | Broncode/documentatie uit een publieke repository; bestandsspecifieke licentie onbekend. | Primaire documentatie over productdoel, componenten, bronnen, metadata, relaties en vervolgzoekingen. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart) | 2026-08-13 | Publieke broncode; bestandsspecifieke licentie onbekend. | Primaire bron voor de vervolgzoeklogica, metadata-statussen en exacte querywaarden. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart) | 2026-08-13 | Publieke broncode; bestandsspecifieke licentie onbekend. | Primaire bron voor detailweergave, deterministische relaties, waarschuwing en externe bronlink. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt) | 2026-08-13 | Publieke broncode; bestandsspecifieke licentie onbekend. | Primaire bron voor bronbeschikbaarheid, gedeeltelijke uitval, tellingen en Heemskerk-indicatie. |
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl) | 2026-08-13 | Publieke acceptatieomgeving met representatieve dummydata; rechten/licentie van de dummydata onbekend. | Verificatie van de publieke app-shell en titel; visuele canvasinhoud kon lokaal niet worden vastgelegd. |
| [bron](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/) | 2026-08-13 | Publieke acceptatieomgeving met representatieve dummydata; rechten/licentie van de dummydata onbekend. | Verificatie van de beheerapp-shell en titel; visuele canvasinhoud kon lokaal niet worden vastgelegd. |
| [bron](https://api.europeana.eu/en) | 2026-08-13 | Europeana vermeldt eigen terms & policies; concrete hergebruikrechten verschillen per item en zijn niet automatisch uit de API-landingspagina af te leiden. | Officiële informatie over Search API, Record API, IIIF en collectie-ontsluiting. |
| [bron](https://www.europeana.eu/en/explore) | 2026-08-13 | Europeana-pagina; item- en mediagebruiksrechten verschillen per object; algemene paginalicentie niet afzonderlijk vastgesteld. | Inspiratie voor thematische en verhalende ontdekking. |
| [bron](https://www.europeana.eu/en/themes) | 2026-08-13 | Europeana-pagina; concrete rechten verschillen per gekoppeld object; algemene paginalicentie niet afzonderlijk vastgesteld. | Toont thematische navigatie rond onder meer kaarten, migratie, fotografie en kranten. |
| [bron](https://www.europeana.eu/en/stories) | 2026-08-13 | Europeana-pagina; concrete rechten verschillen per verhaal en gekoppeld object; algemene paginalicentie niet afzonderlijk vastgesteld. | Toont geredigeerde verhalen als laag bovenop collectiezoeking. |
| [bron](https://www.openarchieven.nl/datasets/) | 2026-08-13 | Open Archieven vermeldt dat distributie per bronorganisatie kan verschillen; concrete rechten zijn daarom per dataset/record te controleren. | Officiële bron voor datasets, API’s, OAI-PMH, externe links en hergebruikbeperkingen. |

## Productbeslissing

Voer een herleidbare vervolgontdekking-laag in die per historisch zoekresultaat drie duidelijk gescheiden paden toont: dezelfde zekere metadatawaarde, een nieuwe vervolgzoeking en een door de bron vastgelegde relatie. Voeg per zoekopdracht een compacte dekkingssamenvatting toe met geraadpleegde en uitgevallen bronnen, aantallen en de betekenis van de Heemskerk-indicatie. Beperk de eerste uitvoering tot bestaande zekere plaats-, persoons-, gebeurtenis- en periodewaarden, stabiele bronidentifier/URI’s en externe bronlinks.

**Waarom:** Deze kleine richting bouwt voort op de bestaande veilige vervolgzoekingen en versterkt tegelijk de kernprincipes Verbonden, Betrouwbaar, Toegankelijk en Nieuwsgierig. Bezoekers kunnen verder ontdekken zonder dat metadata-overlap als bewezen historische relatie wordt gelezen. De dekkingssamenvatting maakt bronbeperkingen en lokale dekking transparant. De richting sluit primair aan op epic theme-hkh-autopilot-0002 en ondersteunt daarnaast epic theme-hkh-autopilot-0001. Er worden geen media, persoonsgegevens of klikgeschiedenis opgeslagen en de scope blijft beperkt tot metadata en externe bronlinks totdat rechten- en privacybeleid per bron is vastgesteld.

### Prioriteiten
- Maak bewijssterkte zichtbaar met de labels: metadata-overlap, vervolgzoeking en bronvastgelegde relatie.
- Behoud de oorspronkelijke bronwaarde exact en toon bij elke vervolgactie de gebruikte waarde, bron en stabiele URI waar beschikbaar.
- Voeg per zoekopdracht een compacte bron- en dekkingssamenvatting toe: geraadpleegde bronnen, uitgevallen bronnen, aantallen en uitleg van de lokale Heemskerk-indicatie.
- Gebruik bronvastgelegde relaties alleen wanneer de externe bron deze expliciet levert; presenteer ze als bronclaim, niet als HKH-afgeleide historische waarheid.
- Maak alle nieuwe interacties toegankelijk zonder voorafgaande vakkennis en laat elke uitkomst uitnodigen tot verder onderzoek.

### Besluiten
- **Gebruik bestaande zekere metadatawaarden als eerste vervolgzoekpaden voor plaats, persoon, gebeurtenis en periode.** — De huidige applicatie ondersteunt deze waarden al en gebruikt de oorspronkelijke waarde exact, waardoor de uitbreiding klein, toetsbaar en herleidbaar blijft.
- **Maak onderscheid tussen metadata-overlap, nieuwe zoekingang en bronvastgelegde relatie.** — De huidige relatiepresentatie is beperkt tot genormaliseerde overlap binnen de zichtbare resultatenpagina. Een expliciet onderscheid voorkomt dat bezoekers een zoektechnische overeenkomst als bewezen historische relatie interpreteren.
- **Gebruik stabiele identifiers, URI’s en machineleesbare relaties van Open Archieven alleen wanneer de bron deze werkelijk levert.** — Open Archieven biedt stabiele URI’s, meerdere machineleesbare representaties en externe bronlinks, wat vervolgonderzoek controleerbaar maakt zonder historische claims door HKH af te leiden.
- **Voeg een compacte bron- en dekkingssamenvatting toe aan elke zoekopdracht.** — De applicatie gebruikt momenteel slechts Europeana en Open Archieven en de betekenis en representativiteit van de Heemskerk-indicatie zijn beperkt uitgelegd. Transparante aantallen en bronstatussen ondersteunen betrouwbare interpretatie.
- **Beperk de eerste scope tot metadata en externe bronlinks.** — De onderzoeksbasis stelt dat rechten en privacy per bron/record moeten worden gecontroleerd. Deze scope levert waarde zonder media te kopiëren of nieuwe persoonsgegevens op te slaan.

## UX-voorstel: Herleidbare vervolgontdekking vanuit een historisch zoekresultaat

**Gebruikersdoel:** De bezoeker wil vanuit een historisch zoekresultaat begrijpelijk verder zoeken en kunnen zien hoe sterk iedere verbinding met andere bronnen is.

### Flow
1. Bezoeker voert een zoekopdracht uit.
2. De resultatenpagina toont per resultaat bron, status, identifier, stabiele URI, ophaaldatum, rechtenstatus en privacystatus.
3. Bezoeker opent een resultaatdetail.
4. Het detail toont drie gescheiden secties: ‘Metadata-overlap’, ‘Nieuwe vervolgzoeking’ en ‘Bronvastgelegde relatie’.
5. Bij metadata-overlap ziet de bezoeker welke zekere waarde overeenkomt en dat dit geen bewezen historische relatie is.
6. Bij een vervolgzoeking ziet de bezoeker de exact gebruikte waarde, het veld en de bron; activering voert een nieuwe zoekopdracht uit.
7. Een bronvastgelegde relatie wordt alleen getoond wanneer de externe bron deze expliciet levert, met bronlabel en stabiele URI.
8. De resultatenpagina toont een compacte dekkingssamenvatting met geraadpleegde bronnen, uitgevallen bronnen, aantallen en uitleg over de Heemskerk-indicatie.
9. De bezoeker kan via de stabiele URI of externe bronlink het oorspronkelijke record openen.

### Wireframe

SCHERM: Zoekresultaten
[Terug] [Zoekveld: ...] [Zoeken]

Dekkingssamenvatting
- Geraadpleegde bronnen: Europeana, Open Archieven
- Resultaten: [aantal]
- Niet beschikbaar: [bron + reden, indien bekend]
- Heemskerk-indicatie: zekere plaatsmetadata komt overeen; dit is geen bewijs van lokale herkomst of historische relatie.

Resultaatkaart
[Titel]
Bron: [bron] | Status: [status]
Identifier: [identifier]
[Details openen]

SCHERM: Resultaatdetail
[Terug naar resultaten]
[Titel]
Bron: [bron]   Stabiele URI: [URI]

Metadata-overlap
- Veld: [plaats/persoon/gebeurtenis/periode]
- Waarde: [exacte oorspronkelijke waarde]
Uitleg: Deze overeenkomst is gevonden in de zichtbare resultaten en bewijst geen relatie tussen bronnen.

Nieuwe vervolgzoeking
[Zoek opnieuw op ‘[exacte waarde]’]
Bron en veld: [bron], [veld]

Bronvastgelegde relatie
[Alleen tonen als de bron dit expliciet levert]
- Relatietype: [type]
- Vastgelegd door: [bron]
- URI: [stabiele URI]
[Open oorspronkelijke bron]

[Rechtenstatus] [Privacystatus] [Ophaaldatum]

### Interactiehypotheses
- Als bewijssterkte zichtbaar wordt onderscheiden met de labels ‘metadata-overlap’, ‘vervolgzoeking’ en ‘bronvastgelegde relatie’, dan neemt het aandeel automatisch correct geïnterpreteerde relaties toe in geautomatiseerde inhouds- en toegankelijkheidscontroles.
- Als elke vervolgactie de oorspronkelijke waarde, het veld en de bron toont, dan zijn vervolgzoekingen reproduceerbaar en controleerbaar zonder aanvullende gebruikerscontext.
- Als de dekkingssamenvatting geraadpleegde en uitgevallen bronnen en aantallen toont, dan kan een geautomatiseerde test vaststellen dat bronbeperkingen niet verborgen blijven.
- Als bronvastgelegde relaties uitsluitend verschijnen bij een expliciete externe bronrelatie en altijd een stabiele URI bevatten, dan worden afgeleide HKH-claims niet vermengd met bronclaims.
- Als de interface alleen zekere bestaande metadatawaarden gebruikt, dan blijft de MVP voorspelbaar en toetsbaar zonder onverklaarde naamvarianten of semantische inferenties.
- Als interactieve elementen een logische toetsenbordvolgorde, zichtbare focus en schermlezerlabels hebben, dan kunnen geautomatiseerde accessibility-tests de volledige vervolgflow bedienen.

### Toegankelijkheid
- Gebruik semantische koppen, landmarks, lijsten en knoppen; vermijd betekenisvolle informatie die uitsluitend op canvas of kleur berust.
- Maak alle acties bereikbaar via toetsenbord met zichtbare focusindicator en logische focusvolgorde.
- Geef elke resultaatkaart en actie een unieke, beschrijvende schermlezernaam, inclusief bron en actie.
- Maak status, bewijssterkte en bronbeschikbaarheid beschikbaar als tekst; gebruik kleur alleen als aanvullende aanduiding.
- Gebruik voldoende kleurcontrast en behoud tekstgrootte en reflow bij vergroting.
- Kondig na een vervolgzoeking de nieuwe paginatitel, zoekterm en resultaatstatus aan via een live region.
- Toon waarschuwingen over ‘geen bewezen relatie’ direct bij de betreffende sectie en niet alleen via tooltip of hover.
- Zorg dat externe links duidelijk aangeven dat de bezoeker de app verlaat en waar mogelijk de doelbron benoemen.

### Privacy
- Sla geen persoonsgegevens, zoekgeschiedenis of klikgeschiedenis op voor deze MVP.
- Gebruik zoektermen uitsluitend tijdelijk voor de actuele zoekopdracht, tenzij een afzonderlijk doel en passende grondslag expliciet zijn vastgesteld.
- Toon privacystatus van bronrecords zonder persoonsgegevens uit externe bronnen onnodig te kopiëren of te verrijken.
- Beperk de gegevensuitwisseling tot noodzakelijke metadata, identifiers, URI’s en externe bronlinks.
- Log voor diagnostiek alleen geanonimiseerde technische statusinformatie; vermijd volledige zoektermen en recordinhoud.
- Respecteer bronvoorwaarden, rechtenstatus en eventuele verwijderings- of afschermingsverzoeken van externe collecties.
- Maak duidelijk dat een externe bron eigen privacyvoorwaarden kan hanteren voordat de bezoeker de app verlaat.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is klein, herleidbaar en agent-uitvoerbaar. Er zijn geen materiële blokkades; bronvastgelegde relaties mogen leeg blijven wanneer de huidige bronnen ze niet leveren.
- **WARNING · CONSISTENCY** — Er is gedeeltelijke overlap met story:66, die al contextuele relaties toont. Houd de nieuwe sectie strikt beperkt tot expliciet door externe bronnen vastgelegde relaties en voorkom dubbele presentatie.
- **WARNING · SOURCE** — De aangehaalde bronnen tonen beschikbare API- en URI-mogelijkheden, maar bewijzen niet dat de huidige Europeana- of Open Archieven-resultaten altijd expliciete relaties leveren. Een lege sectie is daarom een geldige uitkomst.
- **WARNING · RIGHTS** — Rechten kunnen per extern record verschillen. Toon alleen metadata en externe links volgens de bronstatus; kopieer geen bronpayloads of media.

## Geaccepteerde storykandidaten

### Bronvastgelegde relaties afzonderlijk tonen bij historische resultaten

_Sleutel: `bronvastgelegde-relaties-tonen`_

Als bezoeker wil ik bij een historisch zoekresultaat expliciet kunnen zien wanneer de oorspronkelijke bron zelf een relatie met een ander record vastlegt, zodat ik bronclaims kan onderscheiden van metadata-overlap en nieuwe vervolgzoekingen. Toon uitsluitend relaties die door de externe bron expliciet worden geleverd, met relatietype, bronnaam, stabiele URI en externe bronlink. Afgeleide HKH-relaties en relaties zonder herleidbare bron worden niet als bronrelatie gepresenteerd.

**Acceptatiecriteria**
- Een resultaatdetail toont een afzonderlijke sectie ‘Bronvastgelegde relatie’ uitsluitend wanneer de externe bron een expliciete relatie met een ander record levert.
- Elke getoonde bronrelatie bevat het relatietype, de naam van de externe bron en een stabiele URI wanneer die door de bron beschikbaar is.
- De interface labelt de relatie duidelijk als een bronclaim en vermeldt dat deze niet door HKH is afgeleid.
- Een bronrelatie zonder stabiele URI of zonder voldoende bronidentificatie wordt niet als verifieerbare bronrelatie getoond; de bestaande metadata-overlap en vervolgzoeking blijven afzonderlijk beschikbaar.
- De externe bronlink opent het oorspronkelijke record en wordt tekstueel aangekondigd als externe link.
- Geautomatiseerde tests controleren zowel het tonen van een expliciete relatie als het niet-tonen van een afgeleide of onvolledig herleidbare relatie.
- De functionaliteit slaat geen media, ruwe bronpayloads, persoonsgegevens, zoekgeschiedenis of klikgeschiedenis op.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart), [https://www.openarchieven.nl/datasets/](https://www.openarchieven.nl/datasets/), [https://www.openarchieven.nl/api/docs/uri.php](https://www.openarchieven.nl/api/docs/uri.php), [https://www.openarchieven.nl/search-ext.php?lang=nl](https://www.openarchieven.nl/search-ext.php?lang=nl)

Afhankelijkheden: story:70 (herkend als bestaande stories: 70)

Risico's: De bestaande bronnen leveren mogelijk nog onvoldoende expliciete machineleesbare relaties; in dat geval blijft de sectie leeg zonder fallback naar afgeleide claims., Bron- en recordrechten kunnen per dataset verschillen en moeten fail-closed zichtbaar blijven., De huidige Flutter-websemantiek kan aanvullende toegankelijkheidsvalidatie vereisen.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
