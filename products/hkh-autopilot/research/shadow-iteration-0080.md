---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0080
date: 2026-08-16
status: approved
sources:
  - https://github.com/robbertvdzon/hkh-autopilot
  - https://github.com/robbertvdzon/hkh-autopilot/blob/main/docs/factory/functional-spec.md
  - https://github.com/robbertvdzon/hkh-autopilot/blob/main/docs/factory/technical-spec.md
  - https://hkh-autopilot.vdzonsoftware.nl
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl
  - https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/
  - https://www.topotijdreis.nl/
  - https://www.amsterdamtimemachine.nl/
  - https://www.amsterdamtimemachine.nl/data/
  - https://www.openhistoricalmap.org/
  - https://www.openhistoricalmap.org/copyright
  - https://www.europeana.eu/en
---
# Productcyclus 80

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De belangrijkste onbeantwoorde productvraag is hoe HKH een actuele, deployment-paritaire en bronbewuste ontdekkingservaring kan bieden: onderscheid tussen invoerfout, nulresultaat en bronuitval, gevolgd door verkenning via plaats en tijd zonder onbewezen relaties.

### Live zoekflow faalt bij Heemskerk

Productie en acceptatie tonen na zoeken op ‘Heemskerk’ geen resultaten maar bronuitval. Resultaatkaarten, tellingen, identifiers, permanente links en rechten-/privacystatussen ontbreken zichtbaar.

Bronnen: [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl)

### Lege zoekopdracht wordt niet lokaal gevalideerd

Een lege zoekopdracht leidt in acceptatie tot een Open Archieven-fout in plaats van een lokale instructie vóór de bronaanroep.

Bronnen: [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/hkh-autopilot/blob/main/docs/factory/functional-spec.md](https://github.com/robbertvdzon/hkh-autopilot/blob/main/docs/factory/functional-spec.md)

### Repositorycontract is rijker dan de live flow

De repositorydocumentatie beschrijft statusmatrices, resultaatkaarten, context, bronrelaties, rechten/privacy en vervolgzoekingen; deze functies zijn in de publieke flow niet zichtbaar door de bronfout.

Bronnen: [https://github.com/robbertvdzon/hkh-autopilot](https://github.com/robbertvdzon/hkh-autopilot), [https://github.com/robbertvdzon/hkh-autopilot/blob/main/docs/factory/functional-spec.md](https://github.com/robbertvdzon/hkh-autopilot/blob/main/docs/factory/functional-spec.md), [https://github.com/robbertvdzon/hkh-autopilot/blob/main/docs/factory/technical-spec.md](https://github.com/robbertvdzon/hkh-autopilot/blob/main/docs/factory/technical-spec.md)

### Beheeromgeving mist zichtbare provenanceketen

De beheeracceptatie toont publicatie- en record-intakevelden, maar geen zichtbare statusketen voor bronverificatie, rechten, privacy of publieke vrijgave.

Bronnen: [https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/)

### Tijd- en plaatsnavigatie is bewezen inspiratie

Topotijdreis biedt een historische kaart met jaarbereik en vergelijkfunctie. Amsterdam Time Machine gebruikt een locatiegebonden data-index met tijd, ruimte, Linked Open Data en URI’s. OpenHistoricalMap combineert kaart, datum en historisch bereik.

Bronnen: [https://www.topotijdreis.nl/](https://www.topotijdreis.nl/), [https://www.amsterdamtimemachine.nl/](https://www.amsterdamtimemachine.nl/), [https://www.amsterdamtimemachine.nl/data/](https://www.amsterdamtimemachine.nl/data/), [https://www.openhistoricalmap.org/](https://www.openhistoricalmap.org/)

### Curatoriële en lokale verhalen versterken ontdekking

Europeana combineert zoeken met thema’s, stories, collections en galleries. Historypin verbindt lokale foto-, audio- en videopinverhalen met kaarten en collecties.

Bronnen: [https://www.europeana.eu/en](https://www.europeana.eu/en), [https://www.historypin.org/](https://www.historypin.org/), [https://www.historypin.org/collections/](https://www.historypin.org/collections/)

### Rechten moeten bronafhankelijk blijven

OpenHistoricalMap vermeldt CC0 als standaard voor veel data, met mogelijke CC BY/CC BY-SA-licenties per element. Europeana publiceert afzonderlijke beleidsdocumenten. Historypin vermeldt dat site-inhoud alle rechten voorbehoudt.

Bronnen: [https://www.openhistoricalmap.org/copyright](https://www.openhistoricalmap.org/copyright), [https://www.europeana.eu/en/rights](https://www.europeana.eu/en/rights), [https://about.historypin.org/policies/terms-of-use/](https://about.historypin.org/policies/terms-of-use/), [https://www.historypin.org/](https://www.historypin.org/)

### Huidige applicatie

**Doel:** Historisch Heemskerk is een publieke webapp voor een brede doelgroep die vanuit een vraag, plek, persoon, gebeurtenis of onderwerp de geschiedenis van Heemskerk in bredere context wil ontdekken. De homepage biedt productvisie, service-status, nieuws en Historisch zoeken. De repository beschrijft Kotlin/Spring, Flutter en bron-/privacybewuste historische zoekfunctionaliteit.

**Wat ontbreekt:**
- De live zoekflow levert geen historische resultaten voor ‘Heemskerk’.
- De live flow maakt invoerfout, nulresultaat en bronuitval onvoldoende onderscheidbaar.
- Gedocumenteerde resultaatkaarten, context, relaties en vervolgzoekingen zijn publiek niet aantoonbaar bereikbaar.
- Bij externe bronuitval ontbreekt een zichtbaar alternatief ontdekkingspad.
- De beheeracceptatie toont geen zichtbare provenance-, rechten-, privacy- of vrijgavestatussen.

### Verbetermogelijkheden

- Maak deployment en runtime-configuratie aantoonbaar gelijk aan het actuele zoekcontract.
- Valideer lege zoekopdrachten lokaal vóór een bronaanroep.
- Toon bronkeuze, werkelijk verstuurde semantische parameters, bronstatus, telling en bronlink expliciet.
- Voeg plaats- en tijdgebaseerde verkenning toe, bijvoorbeeld kaart, periodebereik en vergelijking van historische lagen.
- Bouw een bronindex die collectie, periode, plaatsdekking en permanente URI’s uitlegt.
- Voeg expliciet gelabelde thema’s en lokale verhalen toe zonder historische relaties af te leiden.
- Maak beheerstatussen voor broncontrole, rechten, privacy, relatie en vrijgave afzonderlijk zichtbaar.
- Toon metadata- en objectrechten afzonderlijk met bronlink en attributie-instructie.

### Inspiratiebronnen

- [Topotijdreis](https://www.topotijdreis.nl/) — Historische kaart met jaarbereik en vergelijkfunctie.
- [Amsterdam Time Machine](https://www.amsterdamtimemachine.nl/) — Locatiegebonden historische data-index met tijd/ruimte en URI’s.
- [OpenHistoricalMap](https://www.openhistoricalmap.org/) — Historische kaart met datum- en periodebediening en expliciete licentie-informatie.
- [Europeana](https://www.europeana.eu/en) — Thematische navigatie, stories, collections en galleries naast zoeken.
- [Historypin](https://www.historypin.org/) — Lokale verhalen, media, kaarten en communitycollecties.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://github.com/robbertvdzon/hkh-autopilot) | 2026-08-16 | Publieke repository; concrete open-source-licentie niet vastgesteld. | Actuele README en repositorystructuur voor productdoel en technische componenten. |
| [bron](https://github.com/robbertvdzon/hkh-autopilot/blob/main/docs/factory/functional-spec.md) | 2026-08-16 | Publieke repositorydocumentatie; concrete licentie niet vastgesteld. | Functionele status-, zoek-, intake- en toegankelijkheidsspecificaties. |
| [bron](https://github.com/robbertvdzon/hkh-autopilot/blob/main/docs/factory/technical-spec.md) | 2026-08-16 | Publieke repositorydocumentatie; concrete licentie niet vastgesteld. | Technisch zoekcontract en bron-/metadataregels. |
| [bron](https://hkh-autopilot.vdzonsoftware.nl) | 2026-08-16 | Publieke productieapp; rechten op inhoud en media niet vastgesteld. | Werkelijke productieflow onderzocht. |
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl) | 2026-08-16 | Publieke acceptatieomgeving met representatieve nepdata; rechten op dummy-inhoud niet vastgesteld. | Veilige interactieve productinspectie. |
| [bron](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/) | 2026-08-16 | Zonder authenticatie publiek zichtbaar; rechten op beheerinhoud niet vastgesteld. | Beheer- en intakeflow bekeken. |
| [bron](https://www.topotijdreis.nl/) | 2026-08-16 | Interface vermeldt ‘Powered by Esri’; specifieke hergebruiklicentie niet vastgesteld. | Inspiratie voor historische kaart, tijdslider en vergelijken. |
| [bron](https://www.amsterdamtimemachine.nl/) | 2026-08-16 | Publieke projectwebsite; uniforme licentie niet vastgesteld. | Inspiratie voor locatiegebonden historische data-index. |
| [bron](https://www.amsterdamtimemachine.nl/data/) | 2026-08-16 | Linked Open Data-principes beschreven; geen uniforme licentie voor alle datasets vastgesteld. | Bron voor URI’s en datasetkoppeling. |
| [bron](https://www.openhistoricalmap.org/) | 2026-08-16 | Publieke interactieve kaart; rechten gespecificeerd op de copyrightpagina. | Inspiratie voor datum- en periodebediening. |
| [bron](https://www.openhistoricalmap.org/copyright) | 2026-08-16 | CC0 voor veel data en stijlen; mogelijke CC BY/CC BY-SA per element; documentatie CC BY-SA 2.0. | Concrete licentiebron voor bronafhankelijke rechtenweergave. |
| [bron](https://www.europeana.eu/en) | 2026-08-16 | Eigen terms/policies; rechten verschillen per individueel item. | Inspiratie voor thema’s, stories, collections en galleries. |

## Productbeslissing

Herstel BUG-2 (P1): maak de historische zoekflow deployment-paritair en verwerk geldige Open Archieven-antwoorden als resultaten. Valideer daarnaast de statusketen zodat invoerfout, nulresultaat en bronuitval afzonderlijk worden getoond, met per resultaat bronnaam, recordgegevens, vaste identificatie, permanente bronlink en bekende of eerlijk onbekende rechten-/privacystatus.

**Waarom:** Dit is de belangrijkste blokkade voor de missie: bezoekers kunnen momenteel geen historische bronnen ontdekken. Productie en acceptatie tonen bij een geldige zoekopdracht volledige bronuitval, terwijl het repositorycontract een rijker zoek- en statusmodel beschrijft. De richting sluit direct aan op open epic theme-hkh-autopilot-0002 en is klein en toetsbaar: herstel de bestaande externe zoekflow, maak runtime-configuratie gelijk aan het actuele contract en bewijs de drie uitkomsttypen met Heemskerk-resultaten. BUG-1 en BUG-3 blijven daarna afzonderlijk uitvoerbaar; nieuwe ontdekfunctionaliteit krijgt geen voorrang zolang historisch zoeken faalt.

### Prioriteiten
- Herstel Open Archieven-integratie en configuratie in productie en acceptatie.
- Toon bij een geldige Heemskerk-zoekopdracht aantoonbare resultaatkaarten met bron, recordgegevens, identifier en permanente link.
- Scheid invoerfout, nulresultaat, gedeeltelijk resultaat en bronuitval in de publieke statusweergave.
- Toon rechten en privacy per bron of markeer deze expliciet als onbekend wanneer niet vastgesteld.
- Voorkom dat een geldige bronrespons als bronfout of onvolledig antwoord wordt behandeld.

### Besluiten
- **Kies BUG-2 als eerstvolgende productrichting.** — Historisch zoeken is de kerningang naar externe collecties en levert momenteel geen bronnen op. Dit blokkeert toegankelijkheid, betrouwbaarheid en verbondenheid direct.
- **Gebruik Open Archieven als eerste hersteldoel en behoud de bestaande bronvolgorde.** — Open Archieven is volgens het onderzoek de gekozen eerste externe bron en geldige antwoorden worden nu onterecht als fout verwerkt. De MVP moet eerst geldige Heemskerk-resultaten aantoonbaar tonen voordat nieuwe bronnen worden toegevoegd.
- **Maak bronstatus en resultaatmetadata zichtbaar in dezelfde zoekervaring.** — De huidige flow verbergt resultaatkaarten, tellingen, identifiers, permanente links en rechten-/privacystatussen. Expliciete metadata maakt antwoorden herleidbaar en ondersteunt betrouwbare vervolgontwikkeling.

## UX-voorstel: BUG-2 MVP: bronbewuste historische zoekflow

**Gebruikersdoel:** Een bezoeker zoekt op “Heemskerk” en kan betrouwbare historische resultaten openen, terwijl duidelijk is of de invoer ongeldig is, niets oplevert, gedeeltelijk werkt of door bronuitval is mislukt.

### Flow
1. Bezoeker opent Historisch zoeken.
2. Bezoeker voert een niet-lege zoekterm in en activeert Zoeken met toetsenbord of knop.
3. De applicatie valideert de invoer lokaal; een lege invoer krijgt direct een begrijpelijke instructie zonder bronaanroep.
4. De applicatie toont tijdens laden een statusmelding en maakt duidelijk welke bron wordt geraadpleegd.
5. Bij een geldige respons toont de applicatie telling, bronstatus en resultaatkaarten met titel, datum of plaats indien beschikbaar, identifier, permanente bronlink en afzonderlijke rechten- en privacystatus.
6. Bij nulresultaat toont de applicatie een aparte melding met de gebruikte zoekterm en een beperkte suggestie om de zoekterm aan te passen.
7. Bij bronuitval toont de applicatie een foutmelding met bronnaam, beperkte technische uitleg en een opnieuw proberen-actie; de situatie wordt niet als nulresultaat gepresenteerd.
8. Bij gedeeltelijke resultaten toont de applicatie de beschikbare kaarten plus een expliciete waarschuwing dat niet alle bronnen konden antwoorden.
9. Bezoeker opent een permanente bronlink in een nieuw of bestaand tabblad met duidelijke linktekst en behoudt de zoekresultaten.

### Wireframe

[Header]
Historisch zoeken

[Zoekveld]
Label: Zoek in historische bronnen
Input: Heemskerk
[Zoeken]

[Statusregio, live aangekondigd]
Bron: Open Archieven
Status: Resultaten gevonden / Geen resultaten / Bron niet beschikbaar
Aantal: 12 resultaten

[Resultaatlijst]
[Kaart 1]
Titel: …
Datum/plaats: …
Bron: Open Archieven
Identifier: …
Rechten: Bekend: … / Onbekend
Privacy: Beoordeeld: … / Onbekend
[Open permanente bronlink]

[Kaart 2]
…

[Alternatieve toestanden]
Lege invoer: “Vul een zoekterm in voordat je zoekt.”
Nulresultaat: “Geen resultaten gevonden voor ‘…’.”
Bronuitval: “Open Archieven is tijdelijk niet beschikbaar. Je zoekopdracht is niet als nulresultaat verwerkt.” [Opnieuw proberen]
Gedeeltelijk: “Sommige bronnen konden niet antwoorden. De getoonde resultaten zijn mogelijk onvolledig.”

### Interactiehypotheses
- Als lege zoekopdrachten lokaal worden afgewezen, daalt het aantal onnodige externe bronaanroepen naar nul en krijgt de bezoeker vóór verzending een bruikbare instructie.
- Als geldige Open Archieven-antwoorden deployment-paritair worden verwerkt, toont een zoekopdracht op “Heemskerk” minimaal één resultaatkaart in productie en acceptatie.
- Als invoerfout, nulresultaat, gedeeltelijk resultaat en bronuitval elk een unieke status en tekst hebben, kunnen geautomatiseerde tests de vier toestanden betrouwbaar onderscheiden zonder interpretatie van foutmeldingen.
- Als iedere resultaatkaart bron, identifier, permanente link, rechtenstatus en privacystatus toont, is ieder resultaat herleidbaar en kan een geautomatiseerde contracttest ontbrekende metadata signaleren.
- Als rechten en privacy afzonderlijk en bronafhankelijk worden weergegeven, worden onbekende statussen niet ten onrechte als toestemming of privacyvrijgave geïnterpreteerd.
- Als de statusregio tijdens laden en na afronding programmatisch wordt aangekondigd, blijft de zoekflow begrijpelijk voor schermlezers.

### Toegankelijkheid
- Gebruik een zichtbaar gekoppeld label voor het zoekveld en behoud de invoerwaarde na fouten.
- Maak Zoeken bereikbaar via Enter en toetsenbordfocus zichtbaar met voldoende contrast.
- Gebruik semantische headings, een lijst voor resultaten en een unieke, beschrijvende linktekst per permanente bronlink.
- Gebruik een aria-live-statusregio voor laden, tellingen en bronstatus; verplaats de focus alleen bij een duidelijke fout of wanneer dat de oriëntatie verbetert.
- Geef foutmeldingen naast kleur ook tekst en ondersteunende iconografie; voldoe aan minimaal WCAG 2.2 AA-contrast.
- Laat interactieve elementen logisch doorlopen in de tabvolgorde en voorkom dat links of statusinformatie alleen visueel beschikbaar zijn.
- Zorg dat de interface bruikbaar blijft bij 200% tekstzoom en op kleine schermen zonder horizontaal scrollen voor kerninformatie.
- Gebruik geen automatische time-out voor fout- of statusmeldingen.

### Privacy
- Sla zoektermen niet persistent op tenzij daarvoor een expliciet, noodzakelijk doel en passende grondslag bestaat.
- Verstuur alleen de noodzakelijke zoekparameter naar Open Archieven; voeg geen account-, apparaat- of locatiegegevens toe.
- Maak in de interface onderscheid tussen rechten op metadata en rechten op het historische object of de media.
- Toon privacystatus per bron of record wanneer vastgesteld; toon anders expliciet “Onbekend” en doe geen privacyclaim.
- Log voor diagnose uitsluitend technische statusinformatie en minimaliseer of anonimiseer zoektermen wanneer logging noodzakelijk is.
- Gebruik permanente bronlinks zonder trackingparameters die niet nodig zijn voor de bronfunctie.
- Geef bij externe bronuitval geen bronrecord of persoonsgegeven weer dat niet succesvol en controleerbaar is opgehaald.
- Laat geautomatiseerde tests controleren dat foutmeldingen geen volledige querypayloads, tokens of onnodige persoonsgegevens bevatten.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is klein, toetsbaar en uitvoerbaar zonder handmatige productbesluiten. Er zijn wel duidelijke overlaps met reeds gepubliceerd werk, maar deployment-pariteit voegt een onderscheiden configuratie- en contracttestdoel toe.
- **INFO · CONSISTENCY** — Gedeeltelijke overlap met gepubliceerde stories 74, 75 en 81 voor de Open Archieven-adapter, foutclassificatie en de Heemskerk-smoketest. Behoud deze kandidaat alleen voor het onderscheiden deployment-pariteitsaspect.
- **WARNING · SCOPE** — Maak in de uitwerking expliciet welke configuratiebron als norm geldt en hoe productie- en acceptatieconfiguratie geautomatiseerd worden uitgelezen of gevalideerd; voorkom dat de smoke-test alsnog afhankelijk wordt van een live externe bron.

## Geaccepteerde storykandidaten

### Deployment-pariteit voor Open Archieven-configuratie

_Sleutel: `deployment-pariteit-open-archieven`_
_Bug: `BUG-2`_

Als Product Factory wil ik dat productie en acceptatie dezelfde actuele Open Archieven-configuratie en het bestaande zoekcontract gebruiken, zodat een geldige zoekopdracht op “Heemskerk” niet langer als bronfout wordt behandeld en BUG-2 wordt opgelost zonder nieuwe zoekfunctionaliteit toe te voegen.

**Acceptatiecriteria**
- De productie- en acceptatie-deployments gebruiken aantoonbaar dezelfde gevalideerde Open Archieven-endpoint-, parameter- en featureconfiguratie als het actuele technische zoekcontract.
- Een geautomatiseerde integratietest met een geldige Open Archieven-fixture classificeert de respons als geldig en niet als bronfout of ongeldig antwoord.
- Een geautomatiseerde deployment-pariteitstest faalt wanneer productie of acceptatie een afwijkende, ontbrekende of niet-gevalideerde Open Archievenconfiguratie gebruikt.
- Een geautomatiseerde smoke-test via de publieke zoekroute met de zoekterm “Heemskerk” bereikt de Open Archieven-adapter en levert ten minste één controleerbaar metadataresultaat met identifier en permanente bronlink op wanneer de gecontroleerde bronrespons geldig is.
- Bestaande fout-, nulresultaat- en gedeeltelijke-resultaatstatussen blijven ongewijzigd en worden niet opnieuw als geldige resultaten geclassificeerd.
- De wijziging introduceert geen nieuwe externe bron, kaart-, tijd- of vervolgzoekfunctionaliteit en logt geen tokens of volledige zoekpayloads.

Bronnen: [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/hkh-autopilot](https://github.com/robbertvdzon/hkh-autopilot), [https://github.com/robbertvdzon/hkh-autopilot/blob/main/docs/factory/functional-spec.md](https://github.com/robbertvdzon/hkh-autopilot/blob/main/docs/factory/functional-spec.md), [https://github.com/robbertvdzon/hkh-autopilot/blob/main/docs/factory/technical-spec.md](https://github.com/robbertvdzon/hkh-autopilot/blob/main/docs/factory/technical-spec.md)

Afhankelijkheden: story:74, story:75, story:81 (herkend als bestaande stories: 74, 75, 81)

Risico's: Een gewijzigde of tijdelijk niet-beschikbare externe bron kan de live smoke-test beïnvloeden; gebruik daarom gecontroleerde fixtures en mocks voor deterministische contracttests., Onbedoelde configuratieverschillen tussen omgevingen kunnen pas na deployment zichtbaar worden; de pariteitstest moet vóór vrijgave tegen beide deploymentconfiguraties draaien., De externe bron kan optionele metadata ontbreken; de bestaande fail-closed behandeling van rechten en privacy moet behouden blijven.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
