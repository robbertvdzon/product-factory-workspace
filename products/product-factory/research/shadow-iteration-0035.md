---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0035
date: 2026-08-12
status: approved
sources:
  - https://github.com/robbertvdzon/product-factory/blob/main/README.md
  - https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md
  - https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart
  - https://github.com/robbertvdzon/product-factory/blob/main/productfactory-contracts/src/main/kotlin/nl/vdzon/productfactory/contracts/Contracts.kt
  - https://github.com/robbertvdzon/product-factory/blob/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt
  - https://github.com/robbertvdzon/product-factory/blob/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowSchemas.kt
  - https://product-factory-acceptance.vdzonsoftware.nl
  - https://docs.github.com/en/actions/how-tos/monitor-workflows
  - https://docs.gitlab.com/ci/pipelines/
  - https://support.atlassian.com/cloud-automation/docs/what-is-the-automation-audit-log/
  - https://www.w3.org/WAI/tutorials/tables/tips/
  - https://www.w3.org/WAI/WCAG22/Understanding/use-of-color
---
# Productcyclus 35

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De belangrijkste nog onbeantwoorde productvraag is: kan Product Factory bij iedere cyclus betrouwbaar tonen wie of wat de uitkomst bepaalde, zonder herkomst te verzinnen? Het antwoord is: slechts gedeeltelijk. Een technisch falen is aantoonbaar via status en foutvelden; een criticusbesluit via criticVerdict en het criticusartefact. Het publieke contract bevat echter geen expliciet veld voor beslisbron, beslismoment of menselijk besluit. Daarom is een stellige classificatie voor alle cycli niet verantwoord en blijft een expliciete toestand ‘beslisbron onbekend’ noodzakelijk. Tegelijk bevestigt de huidige frontendcode het eigenaarsprobleem: cycli, criticusoordeel en voortgekomen stories staan in afzonderlijke secties, waardoor opbrengst en voortgang niet vanuit één cyclusregel te volgen zijn. De acceptatie-URL was bereikbaar, maar Chromium kon in deze uitvoeringssandbox niet starten; daardoor kon de vereiste visuele en interactieve controle niet betrouwbaar worden voltooid. Er is geen productbesluit genomen en er zijn geen stories geschreven.

### Het cycluscontract registreert geen expliciete beslisbron

ShadowIterationView bevat status, criticVerdict, errorMessage, samenvatting en tijdstippen, maar geen decidedBy-, decisionSource-, actor- of provenanceveld. De frontend kan daardoor niet voor iedere cyclus rechtstreeks bewijzen of mens, criticus, guardrail of runtime de beslisser was.

Bronnen: [https://github.com/robbertvdzon/product-factory/blob/main/productfactory-contracts/src/main/kotlin/nl/vdzon/productfactory/contracts/Contracts.kt](https://github.com/robbertvdzon/product-factory/blob/main/productfactory-contracts/src/main/kotlin/nl/vdzon/productfactory/contracts/Contracts.kt)

### Alleen enkele beslisbronnen zijn met bestaand bewijs veilig herkenbaar

De engine schrijft een criticusverdict bij ACCEPTED, NEEDS_REVISION en REJECTED en schrijft een foutmelding bij FAILED. Het criticusartefact bevat bovendien overallVerdict, issues en requiredChanges. Daarmee zijn ‘criticus/evaluatie’ en ‘technische fout’ in specifieke gevallen aantoonbaar; de code levert geen gelijkwaardig bewijs voor een menselijke beslisser. Ambigue gevallen moeten daarom onbekend blijven.

Bronnen: [https://github.com/robbertvdzon/product-factory/blob/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt](https://github.com/robbertvdzon/product-factory/blob/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt), [https://github.com/robbertvdzon/product-factory/blob/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowSchemas.kt](https://github.com/robbertvdzon/product-factory/blob/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowSchemas.kt), [https://github.com/robbertvdzon/product-factory/blob/main/productfactory-contracts/src/main/kotlin/nl/vdzon/productfactory/contracts/Contracts.kt](https://github.com/robbertvdzon/product-factory/blob/main/productfactory-contracts/src/main/kotlin/nl/vdzon/productfactory/contracts/Contracts.kt)

### Het hoofdscherm scheidt cyclusuitkomst en storyvoortgang

De frontend bouwt eerst een sectie ‘Productcycli en onderzoekssessies’ met status, classificatie, datum, kandidaatcount en eventueel criticusoordeel. Daarna volgt een afzonderlijke sectie ‘Software Factory-stories’. De cyclusregel toont geen korte opbrengst, reden, beslisbron of geaggregeerde voortgang van de gekoppelde stories. De eigenaar moet de samenhang dus reconstrueren via aparte lijsten en detailweergaven.

Bronnen: [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart)

### De bestaande gegevensrelatie ondersteunt samenhang zonder statusmutaties

Storykandidaten bevatten iterationSequenceNumber en leveringen worden via candidateId gekoppeld. De frontend gebruikt die gegevens al om stories in wachtrij, bezig, fout en klaar te groeperen. Een presentatie die per cyclus aantallen per voortgangstoestand aggregeert kan daarom waarschijnlijk op bestaande data steunen; dit is een technische mogelijkheid, nog geen productkeuze.

Bronnen: [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart), [https://github.com/robbertvdzon/product-factory/blob/main/productfactory-contracts/src/main/kotlin/nl/vdzon/productfactory/contracts/Contracts.kt](https://github.com/robbertvdzon/product-factory/blob/main/productfactory-contracts/src/main/kotlin/nl/vdzon/productfactory/contracts/Contracts.kt)

### Redenen bestaan, maar zijn vooral detailinformatie

Het detailscherm construeert bij NEEDS_REVISION of REJECTED een zichtbaar Reden-blok uit criticVerdict, criticusartefacten of de laatst voltooide rol. De overzichtsregel toont alleen de classificatie en eventueel de ruwe criticusverdictwaarde. Dit verklaart waarom eerdere reparaties het detail consistenter maakten, maar de door de eigenaar gevraagde traceerbaarheid in het overzicht nog niet volledig oplossen.

Bronnen: [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart)

### De productarchitectuur verklaart de huidige informatie-overdaad

Product Factory omvat onderzoek, productkeuze, UX, criticusbeoordeling, workspace-publicatie, storylevering, voortgang, vragen en evaluatie. Het functionele overzicht beschrijft deze als afzonderlijke operationele onderdelen; de frontend weerspiegelt die groei met meerdere secties. Dat is functioneel verklaarbaar, maar niet optimaal voor de drie kerntaken van de eigenaar.

Bronnen: [https://github.com/robbertvdzon/product-factory/blob/main/README.md](https://github.com/robbertvdzon/product-factory/blob/main/README.md), [https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart)

### Acceptatie-interface kon niet visueel worden gevalideerd

De acceptatie-URL antwoordde op 2026-08-12 met HTTP 200. Twee Playwright-pogingen—met de meegeleverde Chromium en met Google Chrome—faalden voordat een pagina kon openen doordat macOS de Chromium Mach-port in de uitvoeringssandbox blokkeerde. Er is daarom geen screenshot geïnterpreteerd en er worden geen onbewezen claims gedaan over de actuele visuele weergave, doorkliknavigatie of het beheergedeelte.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### Vergelijkbare workflowproducten combineren overzicht met gerichte verdieping

GitHub Actions toont uitvoeringsstatus in runhistorie en laat vanuit een run naar jobs, mislukte stappen en logs navigeren. GitLab toont een filterbaar pipelineoverzicht en een detailpagina met alle jobs. Atlassian Automation toont per uitvoering datum, flow, status en duur en laat een uitvoering uitklappen naar stapdetails. Deze voorbeelden ondersteunen het patroon ‘scanbare runlijst plus detail’, zonder dat Product Factory hun vormgeving hoeft over te nemen.

Bronnen: [https://docs.github.com/en/actions/how-tos/monitor-workflows](https://docs.github.com/en/actions/how-tos/monitor-workflows), [https://docs.gitlab.com/ci/pipelines/](https://docs.gitlab.com/ci/pipelines/), [https://support.atlassian.com/cloud-automation/docs/what-is-the-automation-audit-log/](https://support.atlassian.com/cloud-automation/docs/what-is-the-automation-audit-log/)

### Huidige applicatie

**Doel:** Product Factory organiseert voor de eigenaar van geregistreerde producten autonoom productonderzoek, productkeuzes, UX-ontwikkeling en storyvorming, publiceert geaccepteerde dossiers naar een leesbare workspace, biedt geaccepteerde stories aan de Software Factory aan en volgt uitvoering en evaluatie. Voor Product Factory zelf dient dezelfde cyclus om dashboard en orchestratie continu op bruikbaarheid, begrijpelijkheid en aansluiting bij werkelijk gebruik te toetsen.

**Wat ontbreekt:**
- Het cycluscontract heeft geen expliciet, uniform bewijsveld voor beslisbron, beslismoment en beslisreden.
- De huidige lijstregel kan criticus en technische fout soms aantonen, maar kan niet betrouwbaar iedere uitkomst aan mens, evaluatie-agent, guardrail of runtime toeschrijven.
- Afwezig of ambigu bewijs heeft in het contract geen eigen provenance-toestand; iedere gesloten vierwaardemapping zou daardoor schijnzekerheid kunnen opleveren.
- Korte opbrengst, reden, beslisbron en voortgang van voortgekomen stories staan niet samen in het cyclusoverzicht.
- Cycli en Software Factory-stories worden in aparte secties gepresenteerd, waardoor de eigenaar hun relatie handmatig moet reconstrueren.
- De acceptatieomgeving kon door een sandboxblokkade van Chromium niet visueel en interactief worden beoordeeld; actuele bruikbaarheid, smalle viewport, toetsenbordgedrag en beheernavigatie blijven daarom onbevestigd.

### Verbetermogelijkheden

- Inventariseer per mogelijke weergavewaarde een bewijsregel: criticus alleen bij een aanwezig criticVerdict met passend criticusartefact; technische fout alleen bij FAILED/errorMessage; blokkade alleen bij een expliciet blokkadeveld; anders ‘beslisbron onbekend’.
- Behandel ‘onbekend’ als volwaardige, zichtbare toestand en toon geen menselijke of guardrail-beslisser op basis van indirecte tekst, status of vaste fallback.
- Presenteer bestaande cyclusidentiteit, datum, status, korte veilig begrensde opbrengst, bewijsbare beslisbron, reden en geaggregeerde storyvoortgang in één scanbare structuur, terwijl detailinformatie via de bestaande cyclusdialoog bereikbaar blijft.
- Gebruik de bestaande koppeling iterationSequenceNumber/candidateId uitsluitend voor read-only aggregatie van storytoestanden; verander daarbij geen leveringsstatus of backendgedrag.
- Maak redenweergave veilig door uitsluitend vooraf geselecteerde artifactvelden te gebruiken, met lengtebegrenzing en een neutrale tekst wanneer geen geschikte samenvatting bestaat; toon geen ruwe prompts, logs of onverwachte vrije tekst in het overzicht.
- Behoud in elke responsieve variant de programmatische relatie tussen cyclus en bijbehorende waarden. Gebruik zichtbare tekst naast kleur voor status en zorg dat de volledige rij en afzonderlijke storyactie duidelijke toegankelijke namen hebben.
- Voer vóór een productbesluit alsnog een visuele acceptatie-inspectie uit op desktop en smalle viewport, inclusief cyclusdetail, storydetail, instellingen/beheer, toetsenbordvolgorde, focusherstel, tekstvergroting en alle onbekend-/fouttoestanden.

### Inspiratiebronnen

- [GitHub Actions workflow run history en run summary](https://docs.github.com/en/actions/how-tos/monitor-workflows) — Toont uitvoeringsstatus op overzichtsniveau en biedt gerichte verdieping naar jobs, stappen en logs.
- [GitLab CI/CD pipelines](https://docs.gitlab.com/ci/pipelines/) — Combineert een filterbare lijst van runs met een detailpagina waarin alle onderliggende jobs zichtbaar zijn.
- [Atlassian Automation audit log](https://support.atlassian.com/cloud-automation/docs/what-is-the-automation-audit-log/) — Laat per automatiseringsrun datum, flow, status en duur zien en maakt stapdetails uitklapbaar; relevant als compact overzicht-plus-detailpatroon.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/README.md) | 2026-08-12 | Publiek raadpleegbaar; de repository rapporteert geen licentie, dus hergebruikrechten zijn onbekend. | Primaire beschrijving van productdoel, architectuur en gegevensgrenzen. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md) | 2026-08-12 | Publiek raadpleegbaar; de repository rapporteert geen licentie, dus hergebruikrechten zijn onbekend. | Primaire functionele beschrijving van cycli, agentketen, publicatie, storylevering en dashboard. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart) | 2026-08-12 | Publiek raadpleegbare broncode; de repository rapporteert geen licentie, dus hergebruikrechten zijn onbekend. | Primaire implementatiebron voor hoofdscherm, cyclusregels, redenweergave, storylijsten en navigatie. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/productfactory-contracts/src/main/kotlin/nl/vdzon/productfactory/contracts/Contracts.kt) | 2026-08-12 | Publiek raadpleegbare broncode; de repository rapporteert geen licentie, dus hergebruikrechten zijn onbekend. | Primaire bron voor de werkelijk beschikbare velden in cyclus-, stap-, story- en leveringscontracten. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt) | 2026-08-12 | Publiek raadpleegbare broncode; de repository rapporteert geen licentie, dus hergebruikrechten zijn onbekend. | Primaire bron voor statusovergangen, criticusverdicts, foutregistratie en publicatievoorwaarden. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowSchemas.kt) | 2026-08-12 | Publiek raadpleegbare broncode; de repository rapporteert geen licentie, dus hergebruikrechten zijn onbekend. | Primaire bron voor de structuur van criticusartefacten en beschikbare redenen. |
| [bron](https://product-factory-acceptance.vdzonsoftware.nl) | 2026-08-12 | Eigen publieke acceptatieomgeving met representatieve nepdata; publieke hergebruiklicentie onbekend. | Bedoeld voor visuele en interactieve verificatie van de draaiende applicatie. Bereikbaarheid is vastgesteld, maar browserinspectie werd door de uitvoeringssandbox geblokkeerd. |
| [bron](https://docs.github.com/en/actions/how-tos/monitor-workflows) | 2026-08-12 | GitHub-documentatie; inhoud van de publieke github/docs-repository valt onder CC BY 4.0, codevoorbeelden onder MIT. | Inspiratie voor runhistorie, statusoverzicht en verdieping naar uitvoeringsdetails. |
| [bron](https://docs.gitlab.com/ci/pipelines/) | 2026-08-12 | GitLab-documentatie; copyright GitLab, hergebruikvoorwaarden niet afzonderlijk geverifieerd. | Inspiratie voor een filterbaar pipelineoverzicht gekoppeld aan een jobdetailweergave. |
| [bron](https://support.atlassian.com/cloud-automation/docs/what-is-the-automation-audit-log/) | 2026-08-12 | Copyright Atlassian; publieke hergebruiklicentie onbekend. | Vergelijkbaar patroon voor recente automatiseringsruns met datum, status, duur en uitklapbare stapdetails. |
| [bron](https://www.w3.org/WAI/tutorials/tables/tips/) | 2026-08-12 | W3C-documentlicentie en trademarkvoorwaarden; hergebruik toegestaan volgens het W3C Document License met bronvermelding. | Toegankelijkheidsreferentie voor eenvoudige, responsieve gegevenspresentatie en behoud van structurele relaties. |
| [bron](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color) | 2026-08-12 | W3C-documentlicentie en trademarkvoorwaarden; hergebruik toegestaan volgens het W3C Document License met bronvermelding. | Onderbouwt dat status en betekenis niet uitsluitend door kleur mogen worden overgebracht. |

## Productbeslissing

Voeg aan iedere cyclusregel op het hoofdscherm één expliciete, tekstuele aanduiding ‘Beslisbron’ toe, uitsluitend afgeleid uit bestaand bewijs: ‘Evaluatie-agent’ wanneer een criticVerdict aanwezig is, ‘Technische fout’ bij FAILED met foutbewijs, en anders ‘Onbekend’. Maak de aanduiding aanklikbaar via de bestaande cyclusdetailweergave voor de onderliggende reden. Dit is een read-only frontendwijziging zonder contract-, status-, authenticatie- of leveringswijzigingen.

**Waarom:** Deze kleine richting adresseert rechtstreeks roadmapthema theme-product-factory-0002 en de recente eigenaarsfeedback dat de beslisser in het overzicht ontbreekt. Het huidige gedrag is verklaarbaar: het contract is ontworpen rond cyclusstatus, criticusoordeel en fouten, niet rond uniforme beslisprovenance; daardoor kon het overzicht hooguit losse badges tonen. Een volledige classificatie als mens, evaluatie-agent, guardrail of runtime zou nu herkomst verzinnen. De expliciete toestand ‘Onbekend’ maakt die onzekerheid zichtbaar en voorkomt schijnzekerheid. De wijziging is per cyclusregel te beoordelen, eenvoudig terug te draaien en raakt geen andere producten of operationele processen.

### Prioriteiten
- Toon ‘Beslisbron’ als zichtbare tekst in iedere cyclusregel; betekenis mag niet uitsluitend via kleur worden overgebracht.
- Gebruik een gesloten, conservatieve bewijsregel: criticVerdict aanwezig → ‘Evaluatie-agent’; FAILED met foutbewijs → ‘Technische fout’; alle overige gevallen → ‘Onbekend’.
- Toon nooit ‘Mens’ of ‘Guardrail’ op basis van status, vrije tekst, labels of aannames; daarvoor ontbreekt expliciet bewijs.
- Behoud de bestaande detailweergave als plaats voor de volledige reden en laat de nieuwe aanduiding daarnaar navigeren.
- Test afzonderlijk minimaal een criticusuitkomst, een technische fout en een ambigu geval; controleer dat geen backenddata, leveringsstatus of gedrag van andere producten verandert.

### Besluiten
- **Kies eerst voor beslisbron in het bestaande cyclusoverzicht, niet voor een bredere herinrichting van het hoofdscherm.** — Dit lost de expliciet bevestigde traceerbaarheidskloof op met een kleine, geïsoleerde presentatiewijziging. De frontend toont cycli en stories nu in afzonderlijke secties; samenvoegen zou een grotere ontwerpstap zijn.
- **Maak ‘Onbekend’ een volwaardige beslisbroncategorie.** — Het publieke cycluscontract bevat geen uniform veld voor beslisbron, actor of beslismoment. Onbekende herkomst expliciet tonen is daarom betrouwbaarder dan een volledige classificatie afleiden.
- **Leid alleen ‘Evaluatie-agent’ en ‘Technische fout’ af wanneer de bestaande gegevens daarvoor direct bewijs leveren.** — De engine registreert criticusverdicts voor beoordeelde uitkomsten en foutinformatie bij FAILED; het criticusartefact bevat het oordeel en bijbehorende inhoud. Voor menselijke of guardrailbesluiten bestaat geen gelijkwaardig bewijs.
- **Houd de overzichtstekst compact en gebruik de bestaande detailweergave voor de reden.** — Het detailscherm heeft al een Reden-blok voor afkeuring en revisie. Hergebruik van die verdieping voorkomt duplicatie en volgt het bewezen patroon van een scanbare runlijst met gerichte details.
- **Gebruik naast eventuele kleur altijd een zichtbaar tekstlabel.** — Status en betekenis moeten zonder kleur herkenbaar blijven; dit ondersteunt begrijpelijkheid en toegankelijkheid.

## UX-voorstel: Beslisbron per productcyclus bekijken

**Gebruikersdoel:** De eigenaar kan vanuit het cyclusoverzicht snel en betrouwbaar zien welke aantoonbare bron de uitkomst bepaalde en bij onzeker bewijs herkennen dat de beslisbron onbekend is.

### Flow
1. De eigenaar opent het hoofdscherm en navigeert naar ‘Productcycli en onderzoekssessies’.
2. Iedere cyclusregel toont naast de bestaande gegevens het tekstlabel ‘Beslisbron’ met exact één waarde: ‘Evaluatie-agent’, ‘Technische fout’ of ‘Onbekend’.
3. De frontend bepaalt de waarde conservatief: een aanwezig criticVerdict geeft ‘Evaluatie-agent’; anders geeft status FAILED met niet-lege errorMessage ‘Technische fout’; alle overige combinaties geven ‘Onbekend’.
4. De eigenaar activeert de beslisbron met muis, Enter of Spatie; dezelfde bestaande cyclusdetailweergave opent zonder backendmutatie.
5. De detailweergave toont de reeds veilig geselecteerde redeninformatie of een neutrale melding wanneer geen geschikte reden beschikbaar is.
6. Na sluiten van het detail keert de focus terug naar de geactiveerde beslisbron in de cyclusregel.

### Wireframe

HOOFDSCHERM

Productcycli en onderzoekssessies
┌──────────────────────────────────────────────────────────────┐
│ Cyclus #42                 Status: NEEDS_REVISION            │
│ 12 aug 2026                Kandidaten: 3                     │
│ Beslisbron: [Evaluatie-agent — bekijk reden]                 │
└──────────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────────┐
│ Cyclus #41                 Status: FAILED                    │
│ 11 aug 2026                Kandidaten: 0                     │
│ Beslisbron: [Technische fout — bekijk reden]                 │
└──────────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────────┐
│ Cyclus #40                 Status: COMPLETED                 │
│ 10 aug 2026                Kandidaten: 2                     │
│ Beslisbron: [Onbekend — bekijk details]                      │
└──────────────────────────────────────────────────────────────┘

CYCLESDETAIL (bestaande dialoog)
┌──────────────────────────────────────────────────────────────┐
│ Cyclus #42                                           [Sluit] │
│ Beslisbron: Evaluatie-agent                                  │
│ Reden                                                        │
│ <bestaande, veilig geselecteerde redeninformatie>            │
└──────────────────────────────────────────────────────────────┘

Smalle viewport: iedere cyclus blijft één semantisch gegroepeerde kaart; waarden komen onder hun labels te staan zonder horizontaal scrollen.

### Interactiehypotheses
- Als criticVerdict aanwezig is, toont een componenttest exact ‘Beslisbron: Evaluatie-agent’, ongeacht andere statusvelden.
- Als criticVerdict ontbreekt en status FAILED plus een niet-lege errorMessage aanwezig zijn, toont een componenttest exact ‘Beslisbron: Technische fout’.
- Als criticVerdict ontbreekt of leeg is en niet beide voorwaarden voor een technische fout gelden, toont een parametrische test altijd ‘Beslisbron: Onbekend’.
- Als zowel criticVerdict als foutbewijs aanwezig zijn, wint ‘Evaluatie-agent’ volgens de vastgelegde beslisvolgorde; een unit test borgt deze prioriteit.
- Geen invoercombinatie kan ‘Mens’ of ‘Guardrail’ opleveren; een uitputtende mappingtest controleert de gesloten verzameling toegestane waarden.
- Activatie van de beslisbron met klik, Enter en Spatie opent steeds de bestaande detailweergave voor het juiste cyclusnummer; widgettests valideren dit zonder netwerkmutaties te versturen of backendstatus te wijzigen. De kliktest mag apart zijn van de twee toetsenbordtests om dubbele activatie te voorkomen en gebruikt een echte button/link-semantiek in plaats van een click-handler op statische tekst; als de hele rij al interactief is, wordt de beslisbron geen geneste knop maar onderdeel van de eenduidige rijactie met dezelfde toegankelijke naam en bestemming naar het detail van die cyclus. Daarbij controleert een test ook dat detailinformatie niet naar een andere cyclus lekt en dat bij sluiten de focus terugkeert naar de oorspronkelijke rijactie/beslisbrontrigger, ongeacht de gekozen semantische variant. De detailweergave heeft daarbij één duidelijke sluitactie en sluit voorspelbaar via die actie en Escape, waarna dezelfde focusherstelassertie geldt. Daarnaast validerert een state-test,

### Toegankelijkheid
- Gebruik zichtbare labels en waarden; kleur, pictogram of positie is nooit de enige drager van betekenis.
- Implementeer de beslisbron als semantische knop of link met een toegankelijke naam zoals ‘Beslisbron Evaluatie-agent, bekijk reden voor cyclus 42’.
- Zorg voor bediening met Tab, Shift+Tab, Enter en Spatie, een zichtbare focusindicator en logisch focusherstel na het sluiten van het detail.
- Groepeer op smalle schermen ieder label programmatisch met zijn waarde; behoud een zinvolle schermlezervolgorde zonder horizontaal scrollen bij 320 CSS-pixels.
- Laat geautomatiseerde toegankelijkheidstests controleren op naam, rol, status, focusvolgorde, focusherstel, toetsenbordactivatie en afwezigheid van ernstige axe-overtredingen.
- Borg minimaal WCAG 2.2 AA-contrast: 4,5:1 voor normale tekst, 3:1 voor grote tekst en 3:1 voor essentiële component- en focusgrenzen.
- Ondersteun 200% tekstvergroting zonder verlies van inhoud, overlappende tekst of onbereikbare bediening; valideer dit met geautomatiseerde viewport- en overflowtests.

### Privacy
- Gebruik uitsluitend bestaande operationele metadata van Product Factory: cyclusstatus, criticVerdict en aanwezigheid van errorMessage.
- Toon in het overzicht geen ruwe foutmelding, prompt, log, artefacttekst, persoonsgegevens of gegevens van andere producten.
- Beperk de detailreden tot bestaande vooraf geselecteerde en begrensde velden; gebruik een neutrale tekst als geen veilige reden beschikbaar is.
- Voer voor deze read-only interactie geen schrijfverzoek, statusmutatie, tracking-event of extra gegevensopslag uit; netwerktests controleren dat alleen bestaande leesacties plaatsvinden.
- Testfixtures bevatten uitsluitend synthetische operationele metadata en geen productie- of gebruikersgegevens.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is voldoende onderbouwd, conservatief in herkomsttoeschrijving, read-only en autonoom uitvoerbaar. De verfijnde koppeling van criticVerdict aan een overeenkomende eindstatus voorkomt met name een onjuiste classificatie van het guardrailpad. Er zijn geen blokkerende problemen; enkele acceptatiecriteria verdienen redactionele aanscherping.
- **WARNING · CONSISTENCY** — Het lange acceptatiecriterium over cyclusisolatie bevat een grammaticaal beschadigde passage ('niet wordt getoond lekt ... komt daarbij niet voor'), waardoor de precieze assertie onnodig lastig leesbaar is. De omliggende tekst maakt de beoogde deterministische DOM-isolatietest nog wel voldoende duidelijk.
- **WARNING · ACCESSIBILITY** — De kandidaat borgt native toetsenbordinteractie en focusherstel, maar maakt voldoende contrast, een expliciete toegankelijke naam, 320-CSS-pixel reflow en 200% tekstvergroting niet afzonderlijk toetsbaar in de acceptanceCriteria. Deze eisen staan wel in de aangeleverde UX-randvoorwaarden en moeten bij uitvoering behouden blijven.
- **INFO · SOURCE** — De kernmapping steunt op primaire contract- en enginebroncode. De externe WCAG-bron wordt alleen als toegankelijkheidsreferentie gebruikt; er is geen beoogde overname van extern beschermd ontwerp of tekst.
- **INFO · SCOPE** — De kandidaat overlapt inhoudelijk met de beslisbroncomponent van bestaande kandidaat 56, maar 56 is REJECTED en aanzienlijk breder. Kandidaten 53–55 zijn expliciet als vervangen aangemerkt en worden via een selectiecontrole uitgesloten, zodat geen uitvoeringsconflict hoeft te ontstaan.

## Geaccepteerde storykandidaten

### Toon per cyclus een eenduidig bewijsbare beslisbron met expliciete onbekend-toestand

_Sleutel: `toon-conservatieve-beslisbron-per-cyclus`_

Toon in iedere bestaande cyclusregel het zichtbare tekstlabel ‘Beslisbron’ met exact één waarde uit een gesloten verzameling: ‘Evaluatie-agent’, ‘Technische fout’ of ‘Onbekend’. Classificeer alleen als ‘Evaluatie-agent’ wanneer criticVerdict en eindstatus een door de engine gedocumenteerde, rechtstreeks overeenkomende uitkomst vormen: ACCEPT met ACCEPTED, REVISE of WARNING_ONLY_REVISE met NEEDS_REVISION, of REJECT met REJECTED. Classificeer alleen als ‘Technische fout’ wanneer criticVerdict ontbreekt, de status FAILED is en errorMessage niet leeg is. Iedere andere, ontbrekende, ambigue of tegenstrijdige combinatie toont ‘Onbekend’; dit omvat expliciet ACCEPT met REJECTED, omdat daarbij een guardrail de eindstatus kan hebben bepaald. De beslisbron opent via één native interactieve bediening de bestaande detailweergave van precies die cyclus. De wijziging blijft read-only en beperkt tot de frontend: geen API-, contract-, backend-, status- of leveringswijzigingen. Deze kandidaat vervangt de interne kandidaten 53, 54 en 55; een geautomatiseerde planningscontrole verhindert dat die kandidaten naast deze kandidaat voor levering worden geselecteerd.

**Acceptatiecriteria**
- Een pure, centraal hergebruikte classificatiefunctie normaliseert lege waarden en retourneert uitsluitend ‘Evaluatie-agent’, ‘Technische fout’ of ‘Onbekend’; parametrische tests dekken ontbrekende, lege, ambigue en tegenstrijdige invoer.
- De functie retourneert exact ‘Evaluatie-agent’ voor ACCEPT met ACCEPTED, REVISE met NEEDS_REVISION, WARNING_ONLY_REVISE met NEEDS_REVISION en REJECT met REJECTED, mits criticVerdict en status beide aanwezig zijn.
- Zonder criticVerdict retourneert FAILED met een niet-lege errorMessage exact ‘Technische fout’; FAILED zonder foutbewijs en FAILED met enig criticVerdict retourneren exact ‘Onbekend’.
- Regressietests borgen dat het gedocumenteerde guardrail-pad criticVerdict ACCEPT met status REJECTED exact ‘Onbekend’ oplevert; aanvullende parametrische tests controleren alle niet-overeenkomende combinaties van ACCEPT, REVISE, WARNING_ONLY_REVISE en REJECT met ACCEPTED, NEEDS_REVISION, REJECTED en FAILED.
- Geen invoercombinatie kan ‘Mens’ of ‘Guardrail’ produceren; een uitputtende mappingtest borgt zowel de gesloten waardenverzameling als de regel dat ambigue provenance nooit stellig wordt toegeschreven.
- Iedere cyclusregel toont zichtbaar ‘Beslisbron: Evaluatie-agent’, ‘Beslisbron: Technische fout’ of ‘Beslisbron: Onbekend’, zodat de betekenis niet uitsluitend door kleur, positie of een pictogram wordt overgebracht.
- De bestaande cyclusdetailweergave wordt geopend met één native interactiepatroon: een button ondersteunt klik, Enter en Spatie; een link ondersteunt klik en Enter. Widgettests volgen het gekozen native gedrag, verifiëren het juiste cyclusnummer en voorkomen statische click-handlers en geneste interactieve bediening.
- Geautomatiseerde widgettests bevestigen dat sluiten via de zichtbare sluitactie en Escape de focus herstelt naar de oorspronkelijke cyclusbediening en dat detailinformatie van een andere cyclus niet wordt getoond lekt naar de geopende cyclusdetailweergave komt daarbij niet voor in de DOM van de geopende detailweergave na activatie van een cyclusregel, en de test faalt als tekst die uitsluitend bij een andere fixturecyclus hoort zichtbaar is. De test gebruikt per fixture unieke, synthetische redenstekst en cyclusnummers zodat deze isolatie deterministisch aantoonbaar is. Daarnaast bevestigt een test dat het overzicht geen ruwe errorMessage, prompts, logs of artefactinhoud rendert en dat de interactie geen schrijfverzoek of statusmutatie uitvoert. Een geautomatiseerde plannings-/selectietest faalt wanneer kandidaat 53, 54 of 55 tegelijk met ‘toon-conservatieve-beslisbron-per-cyclus’ voor levering is geselecteerd; de orchestrator markeert 53–55 als vervangen voordat deze kandidaat leverbaar wordt.

Bronnen: [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart), [https://github.com/robbertvdzon/product-factory/blob/main/productfactory-contracts/src/main/kotlin/nl/vdzon/productfactory/contracts/Contracts.kt](https://github.com/robbertvdzon/product-factory/blob/main/productfactory-contracts/src/main/kotlin/nl/vdzon/productfactory/contracts/Contracts.kt), [https://github.com/robbertvdzon/product-factory/blob/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt](https://github.com/robbertvdzon/product-factory/blob/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt), [https://github.com/robbertvdzon/product-factory/blob/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowSchemas.kt](https://github.com/robbertvdzon/product-factory/blob/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowSchemas.kt), [https://www.w3.org/WAI/WCAG22/Understanding/use-of-color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color)

Risico's: De mapping naar ‘Evaluatie-agent’ steunt op de huidige gedocumenteerde relatie tussen criticVerdict en eindstatus; nieuwe verdicts of statusovergangen vallen bewust terug op ‘Onbekend’ totdat hun provenance aantoonbaar is., ‘Onbekend’ kan vaak voorkomen zolang het contract geen expliciet provenanceveld bevat, maar voorkomt een onjuiste toeschrijving aan een mens, evaluatie-agent of guardrail., Interne kandidaten 53, 54 en 55 bevatten een ruimer, conflicterend classificatiemodel; de geautomatiseerde uitsluitingscontrole moet voorkomen dat zij parallel worden geleverd., Een afzonderlijke bediening kan geneste interactie veroorzaken wanneer de hele cyclusrij al interactief is; de implementatie moet daarom exact één native rij- of beslisbronactie gebruiken.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
