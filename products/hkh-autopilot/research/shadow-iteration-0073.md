---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0073
date: 2026-08-15
status: approved
sources:
  - https://github.com/robbertvdzon/hkh-autopilot
  - https://hkh-autopilot.vdzonsoftware.nl
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl
  - https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/
  - https://www.europeana.eu/en/collections
  - https://www.collectienederland.nl/zoeken/
---
# Productcyclus 73

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De belangrijkste onbeantwoorde productvraag is hoe HKH een eerste controleerbaar historisch resultaat toont wanneer externe bronnen gedeeltelijk of volledig falen. De publieke zoekflow is navigeerbaar, maar ‘Heemskerk’ levert momenteel geen resultaatkaart, metadata of permanente bronlink op en onderscheidt bronuitval onvoldoende van nulresultaat.

### Publieke zoekflow eindigt zonder historisch resultaat

Productie en acceptatie bieden vrije tekst, plek, persoon, gebeurtenis, periode en bronfilter. Een read-only zoekactie op ‘Heemskerk’ toont geen recordkaart, identifier, metadata of permanente bronlink.

Bronnen: [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl)

### Bronuitval en nulresultaat zijn onvoldoende onderscheiden

De uitkomst meldt dat geen historische bronnen konden worden geraadpleegd, Europeana niet geconfigureerd is en Open Archieven een onvolledig antwoord gaf. Retry en zoekopdracht aanpassen zijn beschikbaar, maar er is geen bruikbaar deelresultaat of heldere nulresultaatstatus.

Bronnen: [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/hkh-autopilot](https://github.com/robbertvdzon/hkh-autopilot)

### Repositorycontract is rijker dan live aantoonbaar gedrag

De README beschrijft bronstatussen, gedeeltelijke resultaten, stabiele identifiers, bronlinks, rechten/privacy, context, relaties en vervolgzoekingen. Deze onderdelen zijn in de live flow niet verifieerbaar zolang geen geldig resultaat verschijnt.

Bronnen: [https://github.com/robbertvdzon/hkh-autopilot](https://github.com/robbertvdzon/hkh-autopilot)

### Beheerflow toont geen zichtbare bronverificatieketen

De beheeracceptatie toont nieuws-publicatie en lokale record-intake als intern concept. Een zichtbare overgang naar brongeverifieerd, rechten- en privacybeoordeeld publiek resultaat ontbreekt.

Bronnen: [https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/), [https://github.com/robbertvdzon/hkh-autopilot](https://github.com/robbertvdzon/hkh-autopilot)

### Europeana biedt inspiratie voor browsen naast zoeken

Europeana organiseert ontdekking via thema, onderwerp, instelling, features, eeuwen en galleries. Dit kan helpen wanneer vrije tekst geen resultaat oplevert.

Bronnen: [https://www.europeana.eu/en/collections](https://www.europeana.eu/en/collections)

### Collectie Nederland biedt inspiratie voor gefaseerde verfijning

Collectie Nederland combineert vrije tekst met filters op instelling, objectsoort, onderwerp, jaartal en materiaal, plus geavanceerde zoekoperatoren.

Bronnen: [https://www.collectienederland.nl/zoeken/](https://www.collectienederland.nl/zoeken/)

### Huidige applicatie

**Doel:** HKH is een publieke historische ontdekkingstool voor een brede doelgroep. Bezoekers kunnen vanuit een vraag, plek, persoon, gebeurtenis of periode de geschiedenis van Heemskerk onderzoeken in verbinding met externe historische collecties. De aparte beheerapp ondersteunt interne nieuws-publicatie en lokale record-intake.

**Wat ontbreekt:**
- Voor ‘Heemskerk’ verschijnt geen controleerbaar historisch resultaat met metadata, stabiele identifier of permanente bronlink.
- Bronuitval, gedeeltelijke beschikbaarheid en inhoudelijk nulresultaat zijn niet duidelijk van elkaar onderscheiden.
- De beschreven rechten-, privacy-, context- en provenancevelden zijn live niet aantoonbaar zonder resultaatkaart.
- De beheerflow toont geen zichtbare bronverificatie- en vrijgaveketen naar publieke historische content.
- Na bronfalen zijn retry en query aanpassen beschikbaar, maar ontbreekt inhoudelijke vervolghulp.

### Verbetermogelijkheden

- Toon een eerste geldige externe respons als resultaatkaart met bronnaam, beschrijving/titel, metadata, stabiele identifier, brongeleverde permanente link en expliciete rechten-/privacystatus.
- Maak beschikbaar resultaat, beschikbaar nulresultaat, gedeeltelijke beschikbaarheid en volledige bronuitval afzonderlijke gebruikersuitkomsten.
- Behoud geldige deelresultaten wanneer één bron faalt en toon de falende bron apart.
- Voeg naast vrije tekst een ontdekkingspad toe via thema, periode of instelling, geïnspireerd door Europeana.
- Voeg gefaseerde verfijning toe met eenvoudige filters en optionele geavanceerde velden, geïnspireerd door Collectie Nederland.
- Sta context- en vervolgzoekingen alleen toe vanuit zekere bronmetadata en label bronclaims los van afgeleide overeenkomsten.
- Maak in beheer zichtbaar welke intakevelden bron, identifier, provenance, rechten en privacy dragen vóór publieke vrijgave.

### Inspiratiebronnen

- [Europeana Collections](https://www.europeana.eu/en/collections) — Thematisch, institutioneel en temporeel browsen naast vrije tekst.
- [Collectie Nederland](https://www.collectienederland.nl/zoeken/) — Facetten en geavanceerde zoeksyntax voor onderzoek en verfijning.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://github.com/robbertvdzon/hkh-autopilot) | 2026-08-15 | Publieke repository; geen expliciete softwarelicentie vastgesteld op de geraadpleegde root/README, dus onbekend. | Productdoel, componenten, zoekcontract en beschreven rechten-, privacy- en provenancevelden. |
| [bron](https://hkh-autopilot.vdzonsoftware.nl) | 2026-08-15 | Applicatie- en contentlicentie onbekend; uitsluitend read-only geraadpleegd. | Werkelijke productiehomepage en historische zoekactie. |
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl) | 2026-08-15 | Applicatie- en representatieve testcontentlicentie onbekend; dummydata/mocks, uitsluitend read-only geraadpleegd. | Werkelijke acceptatieflow en veilige zoekactie met representatieve nepdata. |
| [bron](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/) | 2026-08-15 | Applicatie- en representatieve testcontentlicentie onbekend; zonder formulierverzending geraadpleegd. | Zichtbare beheerworkflow voor nieuws-publicatie en lokale record-intake. |
| [bron](https://www.europeana.eu/en/collections) | 2026-08-15 | Publieke Europeana-pagina; geen uniforme licentie voor volledige sitecontent vastgesteld. Individuele objectrechten zijn contextafhankelijk. | Inspiratie voor thematisch, institutioneel en temporeel browsen. |
| [bron](https://www.collectienederland.nl/zoeken/) | 2026-08-15 | Publieke pagina van Collectie Nederland/RCE; geen uniforme licentie voor site- en objectcontent vastgesteld. | Inspiratie voor facetten, zoekverfijning en geavanceerde zoeksyntax. |

## Productbeslissing

Maak de Open Archieven-MVP betrouwbaar aantoonbaar met één herleidbare resultaatkaart voor een zoekopdracht op ‘Heemskerk’, inclusief bronstatuscontract voor resultaat, nulresultaat, gedeeltelijke beschikbaarheid en volledige bronuitval.

**Waarom:** Dit is de kleinste samenhangende stap binnen epic theme-hkh-autopilot-0002. De huidige flow toont geen controleerbaar resultaat, metadata of permanente bronlink en maakt bronuitval onvoldoende onderscheidbaar van nulresultaat. Een resultaatkaart met expliciete bronstatus vormt bovendien de basis voor betrouwbare vervolgzoekingen en verdere externe bronnen.

### Prioriteiten
- Toon minimaal één Open Archieven-resultaat wanneer de bron een geldig resultaat levert.
- Neem bronnaam, titel of beschrijving, recordgegevens, stabiele identifier, permanente bronlink en bekende rechten- en privacystatus op.
- Maak resultaat, inhoudelijk nulresultaat, gedeeltelijk resultaat en volledige bronuitval afzonderlijke statussen.
- Behoud geldige deelresultaten wanneer een andere bron faalt.
- Toon alleen vervolgzoekingen vanuit expliciete, zekere bronmetadata.

### Besluiten
- **Kies Open Archieven als enige externe bron in deze stap.** — Open Archieven is al als eerste externe bron gekozen en de roadmap noemt hiervoor expliciet de eerstvolgende story.
- **Maak bronstatus en resultaatmetadata onderdeel van één expliciet contract tussen bronadapter, zoekresultaat en gebruikersinterface.** — Het repositorycontract beschrijft deze velden al, terwijl productie en acceptatie geen resultaatkaart tonen. Eén contract maakt de richting zelfstandig uitvoerbaar en toetsbaar.
- **Gebruik brongeleverde identifiers, links en rechten/privacy-informatie zonder historische relaties af te leiden.** — Betrouwbaarheid en herleidbaarheid vereisen dat claims teruggaan naar de bron; relaties mogen alleen worden getoond wanneer bronnen ze expliciet leveren.
- **Definieer acceptatie op controleerbaar gedrag: een zoekactie op ‘Heemskerk’ levert óf een volledig herleidbare kaart óf een ondubbelzinnige status met behoud van geldige deelresultaten.** — De huidige productie- en acceptatieflows eindigen zonder bruikbaar resultaat en onderscheiden bronuitval onvoldoende van nulresultaat.

## UX-voorstel: Herleidbaar Open Archieven-resultaat voor ‘Heemskerk’

**Gebruikersdoel:** Een bezoeker kan een historische zoekopdracht uitvoeren en direct zien of er een controleerbaar resultaat, nulresultaat, gedeeltelijk resultaat of bronuitval is.

### Flow
1. 1. Bezoeker opent ‘Historisch zoeken’.
2. 2. Bezoeker vult ‘Heemskerk’ in en start de zoekopdracht.
3. 3. De interface toont een duidelijke laadstatus en daarna één van vier bronstatussen: resultaat, inhoudelijk nulresultaat, gedeeltelijk beschikbaar of volledige bronuitval.
4. 4. Bij een geldig resultaat verschijnt minimaal één resultaatkaart met titel of beschrijving, bronnaam, recordgegevens, stabiele identifier, permanente bronlink en bekende rechten-/privacystatus.
5. 5. Bij gedeeltelijke beschikbaarheid blijven geldige Open Archieven-resultaten zichtbaar en wordt de falende bron afzonderlijk toegelicht.
6. 6. Bij nulresultaat of volledige bronuitval krijgt de bezoeker een ondubbelzinnige uitleg en acties om opnieuw te proberen of de zoekopdracht aan te passen.
7. 7. Vervolgzoekingen zijn alleen beschikbaar wanneer expliciete, zekere metadata uit de bron aanwezig is.

### Wireframe

Pagina: Historisch zoeken

[Terug naar homepage]

Historische zoekopdracht
[ Heemskerk                                      ] [Zoeken]
Optioneel: [Periode] [Persoon] [Gebeurtenis] [Bron]

Statusgebied
- Statuslabel: ‘Resultaat beschikbaar’ / ‘Geen resultaat’ / ‘Gedeeltelijk beschikbaar’ / ‘Bron niet beschikbaar’
- Korte uitleg in gewone taal
- Beschikbare bronnen: Open Archieven — status en eventueel foutmelding

Resultaatkaart
┌──────────────────────────────────────────────┐
│ Titel of beschrijving                         │
│ Bron: Open Archieven                          │
│ Recordgegevens: datum, plaats, type, personen │
│ Stabiele identifier: [waarde]                 │
│ Rechten: [bekend/onbekend + bronvermelding]   │
│ Privacy: [status en eventuele beperking]      │
│ [Open permanente bronlink]                    │
│ [Vervolgzoeking, alleen bij zekere metadata]  │
└──────────────────────────────────────────────┘

Bij gedeeltelijke beschikbaarheid:
‘1 resultaat gevonden. Andere bron kon niet worden geraadpleegd.’
[Opnieuw proberen] [Zoekopdracht aanpassen]

Bij nulresultaat:
‘Geen historische records gevonden voor deze zoekopdracht.’
[Zoekopdracht aanpassen]

Bij volledige bronuitval:
‘De historische bron is tijdelijk niet beschikbaar. Er is geen inhoudelijk nulresultaat vastgesteld.’
[Opnieuw proberen] [Zoekopdracht aanpassen]

### Interactiehypotheses
- H1: Een resultaatkaart met bronnaam, stabiele identifier en permanente bronlink verhoogt de controleerbaarheid; testbaar met een geautomatiseerde zoekactie op ‘Heemskerk’ die deze velden valideert.
- H2: Vier afzonderlijke bronstatussen voorkomen dat bronuitval als nulresultaat wordt geïnterpreteerd; testbaar door mocks voor resultaat, nulresultaat, gedeeltelijke beschikbaarheid en volledige uitval te doorlopen en de juiste statuslabels te controleren.
- H3: Geldige deelresultaten blijven bruikbaar wanneer een andere bron faalt; testbaar met één succesvolle en één falende bronrespons waarbij de succesvolle kaart zichtbaar blijft.
- H4: Vervolgzoekingen worden alleen aangeboden bij expliciete bronmetadata; testbaar door resultaten met en zonder zekere metadata te vergelijken.
- H5: Rechten- en privacystatus op de kaart vermindert onduidelijkheid over hergebruik; testbaar door aanwezigheid van deze velden en een neutrale ‘onbekend’-weergave wanneer de bron geen waarde levert.

### Toegankelijkheid
- Alle functies zijn volledig met toetsenbord bereikbaar, met zichtbare focusindicatoren.
- Gebruik semantische koppen, formulieren, knoppen, lijsten en een statusregio met aria-live voor laad- en resultaatmeldingen.
- Geef status niet alleen met kleur weer; gebruik tekst en eventueel een icoon met tekstalternatief.
- Handhaaf voldoende kleurcontrast voor tekst, links, foutmeldingen en focusranden.
- Label alle invoervelden expliciet en verbind fout- en statusmeldingen programmatisch met het zoekveld.
- Maak de permanente bronlink beschrijvend, bijvoorbeeld ‘Open record in Open Archieven’, en laat deze logisch in de tabvolgorde verschijnen.
- Zorg dat de kaart en bronstatus op kleine schermen zonder horizontaal scrollen leesbaar blijven.
- Laat schermlezers onderscheid maken tussen inhoudelijk nulresultaat en technische bronuitval.

### Privacy
- Toon en verwerk alleen gegevens die door Open Archieven voor het zoekdoel worden geleverd.
- Sla zoektermen en historische persoonsinformatie niet op tenzij daarvoor een duidelijk doel, minimale bewaartermijn en passende grondslag zijn vastgesteld.
- Toon privacystatus en eventuele beperkingen rechtstreeks uit de bron; leid geen gevoelige eigenschappen of relaties af.
- Markeer ontbrekende rechten- of privacyinformatie als ‘onbekend’ in plaats van deze zelf in te vullen.
- Gebruik permanente bronlinks zonder extra persoonsgegevens aan URL-parameters toe te voegen.
- Maak duidelijk dat externe bronlinks naar een andere verwerkingsverantwoordelijke kunnen leiden.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is veilig en toetsbaar uitvoerbaar. Er zijn wel scope- en overlaprisico’s, maar geen materiële blokkade voor de kleine MVP.
- **WARNING · SCOPE** — De kandidaat breidt de MVP uit met een beheer- en vrijgaveketen die niet noodzakelijk is voor de publieke Open Archieven-resultaatkaart. Houd dit beperkt tot statusweergave en fail-closed gating; bouw geen volledige curatoriële workflow.
- **WARNING · CONSISTENCY** — Er is gedeeltelijke overlap met bestaande stories over bronstatus, rechten/privacy en herleidbare metadata, met name stories 61, 63 en 73. Leg expliciet vast welke beheerstatusvelden nieuw zijn en voorkom dubbele contracten.
- **INFO · RIGHTS** — De geraadpleegde repository vermeldt geen expliciete softwarelicentie en externe rechteninformatie kan ontbreken. De kandidaat handelt dit correct af door onbekend niet als bevestigd te behandelen.
- **INFO · PRIVACY** — De kandidaat beperkt opslag tot bronmetadata en sluit ruwe payloads en extra persoonsgegevens uit. Bewaar alleen noodzakelijke status- en toelichtingsvelden.

## Geaccepteerde storykandidaten

### Beheerstatus voor bronverificatie en publieke vrijgave

_Sleutel: `beheer-bronverificatie-vrijgave-status`_

Als beheerder wil ik per extern historisch resultaat een controleerbare status zien voor bronverificatie, rechten/privacybeoordeling en publieke vrijgave, zodat de overgang van externe bronrespons naar publiek resultaat herleidbaar en fail-closed is. De status gebruikt uitsluitend beschikbare bronmetadata en maakt ontbrekende informatie expliciet onbekend; er worden geen historische relaties of rechtenclaims afgeleid.

**Acceptatiecriteria**
- De beheerflow toont per extern historisch resultaat afzonderlijke statussen voor bronverificatie, rechtenstatus, privacystatus en publieke vrijgave.
- Elke status kan ten minste de waarden bevestigd, onbekend, afgewezen of niet van toepassing representeren, met een tekstuele toelichting.
- Een resultaat wordt niet als publiek vrijgegeven gemarkeerd wanneer bronverificatie, rechtenstatus of privacystatus onbekend of afgewezen is.
- De beheerweergave toont de bronnaam, stabiele identifier en permanente bronlink die bij het resultaat horen, zonder ruwe bronpayload of extra persoonsgegevens op te slaan.
- De statusweergave is reproduceerbaar testbaar met fixtures voor bevestigde bronmetadata, ontbrekende rechteninformatie, ontbrekende privacyinformatie en ongeldige bronmetadata.
- De publieke zoekroute blijft ongewijzigd wanneer een resultaat niet aan de vrijgavevoorwaarden voldoet; het resultaat wordt dan niet als publiek beschikbaar gepresenteerd.
- Alle statussen en blokkades zijn tekstueel beschikbaar en worden niet uitsluitend door kleur of iconen onderscheiden.

Bronnen: [https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/), [https://github.com/robbertvdzon/hkh-autopilot](https://github.com/robbertvdzon/hkh-autopilot), [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl)

Risico's: De huidige beheerflow toont nog geen volledige overgang van intake naar brongeverifieerde publieke vrijgave., Rechten- en privacyinformatie kan door de externe bron ontbreken; de interface moet daarom onbekend tonen zonder zelf conclusies af te leiden., Een extra vrijgavegate kan bestaande testfixtures of publieke zoekresultaten blokkeren wanneer die geen volledige bronmetadata bevatten.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
