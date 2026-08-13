---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0063
date: 2026-08-13
status: approved
sources:
  - https://github.com/robbertvdzon/hkh-autopilot
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt
  - https://hkh-autopilot.vdzonsoftware.nl
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl
  - https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/
  - https://www.europeana.eu/en/collections
  - https://www.dp.la/about/search-tips
  - https://www.rijksmuseum.nl/en/rijksstudio
  - https://www.w3.org/WAI/WCAG22/Understanding/error-identification
---
# Productcyclus 63

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De belangrijkste onbeantwoorde productvraag is hoe de app bezoekers begrijpelijk laat doorwerken wanneer externe historische bronnen gedeeltelijk of volledig uitvallen, zonder bronbetrouwbaarheid of lokale dekking te overschatten. De huidige zoekroute en herleidbare metadata bestaan, maar de acceptatieomgeving eindigde bij een veilige zoekactie in een generieke tijdelijke-beschikbaarheidsfout; resultaten en vervolgontdekking waren daardoor niet aantoonbaar bruikbaar.

### Huidige productdoel en gebruikersroute

Historisch Heemskerk richt zich breed op bezoekers die via een vraag, plek, persoon of gebeurtenis historische informatie willen ontdekken. De homepage biedt een aparte ingang voor historisch zoeken naast een nieuws-/mededelingenblok. De zoekpagina bevat vrije tekst, plek, persoon, gebeurtenis, periode en bronkeuze.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md), [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl)

### Huidige technische basis voor bronvergelijking

De repository gebruikt Europeana en Open Archieven, toont per bron status en aantallen, geeft een als zodanig gelabelde Heemskerk-indicatie en bewaart volgens de documentatie geen zoekopdrachten of bronpayloads. Resultaatdetails bevatten bron-, identifier-, URI-, rechten- en privacymetadata; metadata-overlap, nieuwe zoekingangen en expliciete bronrelaties zijn afzonderlijk gemodelleerd.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt)

### Actuele zoekervaring is niet aantoonbaar beschikbaar

In productie en acceptatie kon de historische zoekpagina worden geopend. In acceptatie is de dummyzoekterm ‘Heemskerk’ ingevuld en verzonden; na laden verscheen ‘Historisch zoeken is tijdelijk niet beschikbaar’ met alleen ‘Opnieuw proberen’. Daardoor konden actuele zoekresultaten, detailweergave, bronstatussamenvatting, vervolgzoekingen en bronvastgelegde relaties niet visueel worden gecontroleerd.

Bronnen: [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart)

### Foutmelding geeft onvoldoende diagnose en handelingsperspectief

De zichtbare fouttoestand maakt niet duidelijk welke bron of bronnen faalden, of gedeeltelijke resultaten beschikbaar waren, hoeveel bronnen zijn geraadpleegd of wanneer opnieuw proberen zinvol is. Dit is relevant omdat de backend bronstatussen en gedeeltelijke beschikbaarheid al onderscheidt, terwijl de actuele UI in de geteste toestand alleen een algemene melding toont.

Bronnen: [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart)

### Beheeromgeving is zonder authenticatie zichtbaar

De opgegeven beheeracceptatieomgeving opent zonder login en toont ‘HKH Beheer’, ‘Beheerder geverifieerd’, een formulier voor nieuwe berichten en een formulier voor nieuwe record-intake. Er is niets ingevuld of verzonden. Dit is een concreet deployment- en least-privilege-aandachtspunt dat nader geverifieerd moet worden, geen vastgesteld security-incident.

Bronnen: [https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/)

### Externe inspiratie ondersteunt gefaseerde ontdekking

Europeana combineert zoeken met thematische, institutionele en temporele verkenning. DPLA toont één zoekingang over veel instellingen en biedt verfijning op type, onderwerp, locatie, datum, taal en instelling. Rijksstudio illustreert laagdrempelig verder ontdekken via collecties en sets. Deze patronen zijn bruikbaar als inspiratie voor begrijpelijke context en verfijning, zonder bronmedia over te nemen.

Bronnen: [https://www.europeana.eu/en/collections](https://www.europeana.eu/en/collections), [https://www.dp.la/about/search-tips](https://www.dp.la/about/search-tips), [https://www.rijksmuseum.nl/en/rijksstudio](https://www.rijksmuseum.nl/en/rijksstudio)

### Huidige applicatie

**Doel:** Historisch Heemskerk maakt de geschiedenis van Heemskerk toegankelijk voor een brede doelgroep door gewone zoekvragen te verbinden met controleerbare historische bronnen, waaronder Europeana en Open Archieven, met metadata en externe bronlinks.

**Wat ontbreekt:**
- Een acceptatiezoekactie eindigt in een generieke tijdelijke-beschikbaarheidsfout; de actuele resultaten- en detailflow is daardoor niet aantoonbaar bruikbaar.
- De fouttoestand toont niet welke bron uitviel, welke bronnen wel geraadpleegd zijn, hoeveel resultaten beschikbaar zijn of wat de lokale Heemskerk-indicatie betekent.
- De zichtbare homepage scheidt het historische zoekproduct en het aparte nieuws-/mededelingenblok niet expliciet genoeg om verwarring over historische bronstatus uit te sluiten.
- De beheeracceptatieomgeving is zonder login zichtbaar en bevat mutatieformulieren; de toegangsconfiguratie verdient afzonderlijke verificatie.
- Door de CanvasKit-rendering is semantische tekstinspectie beperkt; toegankelijkheid van dynamische fout- en statusmeldingen moet daarom expliciet visueel en met assistieve technologie worden getoetst.

### Verbetermogelijkheden

- Maak degraded search per bron zichtbaar: geraadpleegd, beschikbaar, uitgevallen, aantal resultaten en reden van uitval.
- Behoud bruikbare gedeeltelijke resultaten wanneer één bron uitvalt en leg duidelijk uit dat de dekking onvolledig is; toon een lege maar informatieve toestand wanneer alle bronnen uitvallen.
- Maak de foutmelding tekstueel diagnostisch en toegankelijk, met een concrete vervolgstap zoals opnieuw proberen en eventueel een alternatieve zoekroute. W3C benadrukt dat fouten in tekst benoemd en beschreven moeten worden.
- Laat de betekenis van de Heemskerk-indicatie en bronstatus naast resultaten staan, zodat lokale relevantie niet als historische waarheid wordt gelezen.
- Maak nieuws duidelijk herkenbaar als productmededeling en niet als historische bron.
- Verifieer de deploymentgrens van het beheeroppervlak en beperk publieke toegang tot geautoriseerde beheerders voordat echte mutaties mogelijk zijn.
- Gebruik inspiratie van Europeana en DPLA voor verfijning op bron, plaats, periode en instelling, en van Rijksstudio voor optionele verzamel- of verder-ontdekkenpatronen; behoud metadata/externe-links-scope zolang rechtenbeleid niet per record is vastgesteld.

### Inspiratiebronnen

- [Europeana collections](https://www.europeana.eu/en/collections) — Thematische, institutionele en temporele verkenning over geaggregeerde erfgoedcollecties.
- [Digital Public Library of America search tips](https://www.dp.la/about/search-tips) — Zoekverfijning op type, onderwerp, locatie, datum, taal, partner en instelling.
- [Rijksstudio](https://www.rijksmuseum.nl/en/rijksstudio) — Laagdrempelig verder ontdekken via collecties en sets rond objecten.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://github.com/robbertvdzon/hkh-autopilot) | 2026-08-13 | Publieke GitHub-repository; er is geen LICENSE-pad in de actuele repositoryboom aangetroffen, dus hergebruikrechten van concrete bestanden zijn onbekend. | Overzicht van de actuele publieke productrepository en documentatie. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md) | 2026-08-13 | Publieke README; concrete auteursrecht- of licentie-indicatie ontbreekt in de geraadpleegde inhoud. | Documenteert productdoel, componenten, bronkoppelingen en privacy-/opslaggedrag. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart) | 2026-08-13 | Publieke broncode; licentie niet vastgesteld omdat geen LICENSE-bestand is aangetroffen. | Bevat zoekvelden, bronstatusmodellen, vervolgzoekingen en foutstatuslogica. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_context_detail.dart) | 2026-08-13 | Publieke broncode; licentie onbekend. | Bevat detailweergave, bronclaims, metadata-overlap en vervolgontdekking. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt) | 2026-08-13 | Publieke broncode; licentie onbekend. | Bevat bronstatussen, gedeeltelijke bronbeschikbaarheid en tellingen. |
| [bron](https://hkh-autopilot.vdzonsoftware.nl) | 2026-08-13 | Rechten/licentie van publieke UI-tekst en visuals onbekend; uitsluitend read-only bekeken. | Werkelijke productiehomepage en historische zoeknavigatie. |
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl) | 2026-08-13 | Volgens de opdracht representatieve dummydata en gemockte koppelingen; rechten/licentie van UI-inhoud niet afzonderlijk vermeld. | Werkelijke acceptatiehomepage, zoekformulier en fouttoestand. |
| [bron](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/) | 2026-08-13 | Rechten/licentie van beheer-UI onbekend; alleen bekeken, geen mutatie uitgevoerd. | Werkelijke beheeromgeving zonder authenticatie. |
| [bron](https://www.europeana.eu/en/collections) | 2026-08-13 | Europeana-webcontent is publiek toegankelijk maar concrete rechten verschillen per object en instelling; geen bronmedia hergebruikt. | Inspiratie voor thematisch, institutioneel en temporeel ontdekken in geaggregeerde collecties. |
| [bron](https://www.dp.la/about/search-tips) | 2026-08-13 | Publieke DPLA-helpcontent; concrete licentie van de paginatekst niet afzonderlijk vastgesteld. | Documenteert verfijning op type, onderwerp, locatie, datum, taal en instelling. |
| [bron](https://www.rijksmuseum.nl/en/rijksstudio) | 2026-08-13 | Publieke Rijksmuseum-webcontent; rechten verschillen per object; niets gekopieerd. | Inspiratie voor verder ontdekken via collecties en sets. |
| [bron](https://www.w3.org/WAI/WCAG22/Understanding/error-identification) | 2026-08-13 | W3C publieke standaard-/richtlijndocumentatie; hergebruikvoorwaarden van de pagina niet afzonderlijk gecontroleerd. | Onderbouwt dat foutmeldingen het probleem tekstueel moeten identificeren en gebruikers moeten helpen begrijpen wat misging. |

## Productbeslissing

Maak historisch zoeken veerkrachtig en begrijpelijk bij bronuitval: toon per geraadpleegde bron de status, het aantal resultaten en een korte reden bij uitval; behoud gedeeltelijke resultaten en toon bij volledige uitval een informatieve lege toestand met opnieuw proberen. Leg daarnaast de betekenis van de Heemskerk-indicatie uit naast de resultaten.

**Waarom:** Deze kleine richting adresseert de aantoonbare blokkade in de huidige zoekroute: een generieke foutmelding maakt resultaten, brondekking en vervolgstappen onduidelijk. Ze sluit direct aan op epic theme-hkh-autopilot-0002 en versterkt de principes betrouwbaar, verbonden, toegankelijk en nieuwsgierig. De benodigde bronstatussen, gedeeltelijke beschikbaarheid, tellingen en Heemskerk-indicatie bestaan al in de technische basis; de richting maakt die informatie zichtbaar zonder nieuwe historische relaties of bronmedia te introduceren.

### Prioriteiten
- Per bron zichtbaar maken: geraadpleegd, beschikbaar, uitgevallen, aantal resultaten en foutreden.
- Gedeeltelijke resultaten blijven tonen met een duidelijke waarschuwing dat de brondekking onvolledig is.
- Bij volledige bronuitval een tekstueel diagnostische lege toestand tonen met opnieuw proberen en een alternatieve zoekroute.
- De Heemskerk-indicatie expliciet als metadata-indicatie uitleggen, niet als historische waarheid.
- Dynamische status- en foutmeldingen visueel en met assistieve technologie toetsen.

### Besluiten
- **Prioriteer bronveerkracht en transparante bronstatus boven nieuwe zoekfilters, verzamel-functies of extra bronnen.** — De actuele acceptatiezoekactie eindigt in een generieke tijdelijke-beschikbaarheidsfout; daardoor is de bestaande zoek- en vervolgroute niet aantoonbaar bruikbaar. De voorgestelde richting maakt de bestaande basis betrouwbaar bruikbaar voordat verdere ontdekfuncties worden uitgebreid.
- **Gebruik uitsluitend metadata, bronclaims en externe bronlinks in deze verbetering; voeg geen bronmedia of onbewezen historische relaties toe.** — De huidige productbasis modelleert bron-, identifier-, URI-, rechten- en privacymetadata en expliciete bronrelaties afzonderlijk. De richting blijft daarmee binnen de bestaande scope en bewaakt herleidbaarheid en betrouwbaarheid.
- **Formuleer foutmeldingen als concrete, begrijpelijke statusinformatie met een handelingsperspectief.** — De huidige melding identificeert geen falende bron, gedeeltelijke dekking of volgende stap. De geraadpleegde W3C-richtlijn ondersteunt tekstuele foutidentificatie en uitleg voor gebruikers.

## UX-voorstel: Veerkrachtig historisch zoeken bij bronuitval

**Gebruikersdoel:** Een bezoeker zoekt historische informatie over Heemskerk, begrijpt welke bronnen beschikbaar zijn en kan verantwoord verdergaan wanneer één of meer bronnen uitvallen.

### Flow
1. Bezoeker opent Historisch zoeken.
2. Bezoeker vult een vraag in, bijvoorbeeld ‘Heemskerk’, en kiest eventueel plek, persoon, gebeurtenis, periode of bronnen.
3. Bezoeker start de zoekactie.
4. De interface toont per bron de status: geraadpleegd, beschikbaar of uitgevallen, inclusief resultaat-aantal en korte foutreden.
5. Bij gedeeltelijke beschikbaarheid worden beschikbare resultaten getoond met een duidelijke melding dat de dekking onvolledig is.
6. Bij volledige uitval toont de interface een informatieve lege toestand met de opties ‘Opnieuw proberen’ en ‘Zoekopdracht aanpassen’.
7. Bij elk resultaat wordt de Heemskerk-indicatie uitgelegd als metadata-indicatie, niet als bewijs van historische waarheid.
8. Bezoeker opent een resultaatdetail met bron, identifier, rechteninformatie en externe bronlink en kan van daaruit verder zoeken.

### Wireframe

Pagina: Historisch zoeken

[H1] Historisch zoeken
[Instructie] Zoek in historische metadata uit meerdere bronnen.

[Label: Zoekvraag] [tekstveld: Heemskerk]
[Optionele filters: Plek] [Persoon] [Gebeurtenis] [Periode]
[Bronkeuze: Europeana □] [Open Archieven □]
[Button: Zoeken]

Na zoeken:
[Statusregio, live]
2 bronnen geraadpleegd. 1 bron beschikbaar, 1 bron tijdelijk niet beschikbaar.

[Bronstatus-kaarten]
- Europeana — Beschikbaar — 24 resultaten
- Open Archieven — Tijdelijk niet beschikbaar — Reden: time-out — Geen resultaten opgehaald

[Waarschuwing]
Deze resultaten zijn gebaseerd op een gedeeltelijke bronselectie. De zoekdekking kan onvolledig zijn.

[Resultaatlijst]
[Resultaatkaart]
Titel
Korte metadata
Heemskerk-indicatie: mogelijk lokaal relevant op basis van metadata
[Button/link: Bekijk details]

Bij volledige uitval:
[Statusregio, live]
Geen bronnen konden worden geraadpleegd. Er zijn geen resultaten beschikbaar.
[Button: Opnieuw proberen] [Button: Zoekopdracht aanpassen]
[Helptekst] Controleer uw zoekterm of probeer het later opnieuw.

### Interactiehypotheses
- Als de status en het resultaat-aantal per bron zichtbaar zijn, kunnen bezoekers beter inschatten hoe volledig de zoekdekking is; toetsbaar via geautomatiseerde UI-asserties op statuslabels, aantallen en dekkingstekst.
- Als gedeeltelijke resultaten behouden blijven wanneer één bron faalt, bereiken meer zoekacties een bruikbare resultaatweergave dan bij een generieke volledige fout; toetsbaar met mocks voor nul, één en alle falende bronnen.
- Als een uitgevallen bron een korte begrijpelijke foutreden toont, begrijpen bezoekers beter wat er misging; toetsbaar via aanwezigheid van bronnaam, status, reden en vervolgstap in de toegankelijkheidsboom.
- Als de volledige-uitvaltoestand zowel opnieuw proberen als zoekopdracht aanpassen aanbiedt, is er altijd een geautomatiseerd aantoonbare vervolgstap zonder gegevensverlies.
- Als de Heemskerk-indicatie direct als metadata-indicatie wordt gelabeld, wordt lokale relevantie minder snel geïnterpreteerd als historische zekerheid; toetsbaar via expliciete disclaimertekst naast ieder relevant resultaat.
- Als status- en foutinformatie in een live-regio wordt geplaatst, ontvangen schermlezers dynamische updates zonder focusverlies; toetsbaar met semantische rollen, aria-live-status en toetsenbordfocusregels.

### Toegankelijkheid
- Gebruik semantische headings, labels, fieldsets en beschrijvingen voor alle zoekvelden en bronkeuzes.
- Maak alle interacties volledig toetsenbordbedienbaar met zichtbare focus, logische tabvolgorde en geen hover-only acties.
- Gebruik tekst én betekenisvolle iconen voor bronstatus; kleur mag nooit de enige statusdrager zijn.
- Zorg voor voldoende contrast volgens WCAG 2.2 AA en behoud leesbaarheid bij tekstvergroting en reflow.
- Exposeer laad-, gedeeltelijke-fout- en volledige-foutstatus via een passende live-regio, zonder onverwachte focusverplaatsing.
- Laat foutmeldingen het probleem, de betrokken bron en een concrete vervolgstap benoemen.
- Maak externe bronlinks duidelijk herkenbaar, inclusief bestemming wanneer dat relevant is.
- Ondersteun screenreaders met beschrijvende resultaatlabels en behoud de relatie tussen resultaat, bronstatus en Heemskerk-indicatie.

### Privacy
- Sla zoekopdrachten, zoektermen en bronpayloads niet op; verwerk ze alleen tijdelijk voor de aanvraag en weergave.
- Verzamel geen persoonsgegevens voor deze MVP. Vrije tekstvelden moeten geen persoonsgegevens vereisen.
- Toon alleen noodzakelijke bronmetadata, identifiers, rechteninformatie, privacymetadata en externe links.
- Maak externe links duidelijk herkenbaar, zodat bezoekers weten wanneer zij de applicatie verlaten en mogelijk onder ander privacybeleid vallen.
- Gebruik fout- en statuslogging uitsluitend geaggregeerd of technisch noodzakelijk; voorkom zoektermen en herleidbare gebruikersgegevens in logs.
- Behandel de Heemskerk-indicatie als afgeleide metadata en presenteer deze niet als persoons- of locatiebewijs.
- Valideer geautomatiseerd dat gedeeltelijke foutresponses geen verborgen persoonsgegevens of onnodige bronpayloads aan de client blootstellen.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is klein, toetsbaar en uitvoerbaar zonder handmatige eigenaaractie. De scope sluit aan op de bestaande bronstatus- en zoekfunctionaliteit en bevat passende privacy- en toegankelijkheidswaarborgen.
- **INFO · CONSISTENCY** — Er is gedeeltelijke overlap met bestaande stories 14, 63 en 68, maar deze kandidaat voegt specifiek geautomatiseerde live-statusfeedback en toegankelijkheidsdekking toe. Dit is geen blokkerend duplicaat.

## Geaccepteerde storykandidaten

### Toegankelijke live-statusfeedback voor historische zoekresultaten

_Sleutel: `historische-zoekstatus-livefeedback`_

Maak de bestaande historische zoekroute begrijpelijk voor gebruikers van assistieve technologie door laadstatus, gedeeltelijke bronuitval en volledige bronuitval als dynamische, tekstuele statusupdates beschikbaar te maken. De status benoemt de betrokken bron, het aantal beschikbare resultaten of de uitvalreden en biedt een geautomatiseerd toetsbare vervolgstap zonder focusverlies. De Heemskerk-indicatie wordt als metadata-indicatie gelabeld en niet als historische zekerheid.

**Acceptatiecriteria**
- De historische zoekroute bevat een semantisch herkenbare live-regio waarin laadstatus, gedeeltelijke beschikbaarheid en volledige bronuitval programmatisch worden aangekondigd.
- Bij gedeeltelijke bronuitval benoemt de live-regio minstens de beschikbare bron, de uitgevallen bron en de beschikbare resultatentelling; de bestaande beschikbare resultaten blijven zichtbaar.
- Bij volledige bronuitval benoemt de interface tekstueel dat geen bronnen konden worden geraadpleegd en biedt zij de acties ‘Opnieuw proberen’ en ‘Zoekopdracht aanpassen’.
- De statusupdate verplaatst de toetsenbordfocus niet onverwacht en alle vervolgstappen zijn via toetsenbord en toegankelijkheidsboom beschikbaar.
- Elke getoonde Heemskerk-indicatie bevat expliciet de kwalificatie dat het om een metadata-indicatie gaat en niet om bewijs van historische waarheid.
- Geautomatiseerde UI- en toegankelijkheidstests dekken nul, één en alle falende bronnen, inclusief statusnaam, foutreden, resultaat-aantal en vervolgstap.
- Geautomatiseerde tests bevestigen dat zoektermen, bronpayloads en niet-noodzakelijke persoonsgegevens niet in de statusweergave of clientrespons worden toegevoegd.

Bronnen: [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/frontend/lib/historical/historical_search.dart), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/backend/src/main/kotlin/nl/vdzon/hkh/historicalsearch/HistoricalSearchService.kt), [https://www.w3.org/WAI/WCAG22/Understanding/error-identification](https://www.w3.org/WAI/WCAG22/Understanding/error-identification)

Afhankelijkheden: story:63, story:68 (herkend als bestaande stories: 63, 68)

Risico's: De huidige Flutter-web-rendering kan geautomatiseerde semantische inspectie van dynamische meldingen bemoeilijken., De betekenis van de Heemskerk-indicatie kan ondanks de kwalificatie nog steeds verkeerd worden geïnterpreteerd; de story introduceert geen nieuwe historische validatie., De actuele externe bronbeschikbaarheid kan verschillen van acceptatie-fixtures; tests moeten daarom deterministische bronstatusfixtures gebruiken.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
