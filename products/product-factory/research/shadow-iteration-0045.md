---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0045
date: 2026-08-14
status: approved
sources:
  - https://product-factory.vdzonsoftware.nl
  - https://product-factory-acceptance.vdzonsoftware.nl
  - https://github.com/robbertvdzon/product-factory
  - https://github.com/robbertvdzon/product-factory/blob/main/README.md
  - https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md
  - https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/iteration_evidence_overview_test.dart
  - https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/management_view_test.dart
  - https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/goldens/iteration_cycle_card_states.png
  - https://docs.flutter.dev/testing/overview
  - https://docs.flutter.dev/testing/integration-tests
  - https://docs.flutter.dev/tos
  - https://api.flutter.dev/flutter/flutter_test/MatchesGoldenFile-class.html
---
# Productcyclus 45

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Belangrijkste nog onbeantwoorde productvraag: welke minimale, deterministische acceptatiescenario’s zijn nodig om het productspecifieke dashboardgedrag van Product Factory zelf blijvend en visueel te toetsen? De acceptatieomgeving bevestigt dat dagelijks gebruik en Beheer nu duidelijk gescheiden zijn, maar bevat alleen hkh-autopilot-data. Daardoor blijft de speciaal voor Product Factory gebouwde compacte bewijsregel ondanks widgettests niet onafhankelijk zichtbaar te beoordelen.

### Productie vraagt authenticatie op de exact geconfigureerde URL

De browser is gestart op https://product-factory.vdzonsoftware.nl en bleef op die host. Na de Flutter-render verscheen het Product Factory-loginpaneel met een toegestaan Google-account als vereiste. Er is niet geprobeerd in te loggen. Hiermee verwijst het productie-browserbewijs expliciet naar de juiste geconfigureerde URL.

Bronnen: [https://product-factory.vdzonsoftware.nl](https://product-factory.vdzonsoftware.nl)

### Dagelijks gebruik en beheer zijn zichtbaar van elkaar gescheiden

Acceptatie toont een Productoverzicht met metrics, een productkaart, de dominante actie ‘Start productcyclus nu’ en daaronder cycluskaarten. ‘Beheer’ opent een rustiger scherm met Software Factory-stories en Storywachtrij. Een wachtrijregel opent een dialoog met beschrijving, acceptatiecriteria en criticusbeoordeling. De scheiding is begrijpelijk en sluit aan op de repositorydocumentatie en regressietest.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/management_view_test.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/management_view_test.dart)

### Acceptatie bewijst het productspecifieke gedrag van Product Factory zelf niet

De bekeken acceptatieomgeving bevat één product, HkH Autopilot, en drie hkh-autopilot-iteraties. De repository beschrijft en test daarentegen een compacte bewijsregel die uitsluitend voor terminale cycli met productslug ‘product-factory’ verschijnt. Die gedeployde variant, haar echte CanvasKit-layout en haar bewijsinteractie kunnen met de huidige publieke nepdata niet visueel worden beoordeeld.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/iteration_evidence_overview_test.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/iteration_evidence_overview_test.dart)

### De repository heeft sterke widgetdekking maar geen gevonden dashboard-integratietestmap

De publieke repository bevat gerichte widgettests voor beheer, bewijsregels, beslisbronnen, responsiviteit en interactie, plus een golden voor cycluskaartstatussen. In de geraadpleegde publieke repositoryboom is geen dashboard-frontend/integration_test-map aangetroffen. Dit ondersteunt de inferentie dat componentgedrag goed wordt afgedekt, maar de gedeployde browserflow vooral via handmatige acceptatie-inspectie bewijsbaar is.

Bronnen: [https://github.com/robbertvdzon/product-factory](https://github.com/robbertvdzon/product-factory), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/iteration_evidence_overview_test.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/iteration_evidence_overview_test.dart), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/management_view_test.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/management_view_test.dart), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/goldens/iteration_cycle_card_states.png](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/goldens/iteration_cycle_card_states.png)

### Product Factory orkestreert autonome productontwikkeling voor de producteigenaar

De applicatie organiseert onderzoek, productkeuze, UX, storyvorming en kritiek, publiceert goedgekeurde dossiers en biedt stories aan de Software Factory aan. Zij bouwt zelf geen productcode. Het dashboard is de bedienings- en bewijslaag waarmee de producteigenaar cycli, opbrengsten, beslissingen, blokkades en leveringen volgt.

Bronnen: [https://github.com/robbertvdzon/product-factory/blob/main/README.md](https://github.com/robbertvdzon/product-factory/blob/main/README.md), [https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md)

### Huidige applicatie

**Doel:** Product Factory is de orchestratielaag waarmee een producteigenaar autonome productontwikkeling voor geregistreerde producten start en volgt: onderzoek, keuze, UX, stories, kritiek, workspacepublicatie, levering aan Software Factory en evaluatie. Het dashboard moet vooral starten, eerdere opbrengsten en voortgekomen stories begrijpelijk en bewijsbaar maken.

**Wat ontbreekt:**
- De publieke acceptatieomgeving bevat geen Product Factory-product of -cyclus; productspecifieke UI is daardoor niet live te beoordelen.
- De compacte Product Factory-bewijsregel is gedocumenteerd en met widgetfixtures getest, maar acceptatie levert geen visueel bewijs van de gedeployde variant, responsiviteit en browserinteractie.
- Productie vereist Google-authenticatie en kan zonder inloggen niet als alternatief publiek visueel bewijs dienen.
- De acceptatieproductkaart bevat naast de kernactie nog vier secundaire acties en vijf metrics; zonder Product Factory-nepdata blijft onbekend of de eigen-productflow rond de drie eigenaarsvragen voldoende scanbaar is.
- De acceptatiedata is veilig en representatief voor een procesdemo, maar niet voor cruciale productslug-, status- en provenancevarianten die Product Factory over zichzelf moet toetsen.

### Verbetermogelijkheden

- Onderzoek welke minimale deterministische set acceptatiescenario’s nodig is om Product Factory zijn eigen dashboardgedrag blijvend te laten toetsen zonder data van andere producten te gebruiken.
- Overweeg uitsluitend synthetische Product Factory-acceptatiedata met minstens één actieve en meerdere terminale cycli, inclusief expliciete, afgeleide en onbekende beslisbron en gekoppelde en ongekoppelde opbrengst.
- Houd zulke fixtures privacy-minimaal en deterministisch: vaste fictieve titels, datums, statussen en operationele metadata; geen prompts, tokens, stacktraces of gebruikersdata.
- Combineer bestaande widgettests met een kleine integratielaag voor de belangrijkste eigenaarspaden: hoofdscherm laden, bewijsregel openen en sluiten, Beheer openen en storydetail bekijken.
- Breid de bestaande golden-aanpak eventueel uit naar de Product Factory-bewijsregel en Beheer bij smalle en brede schermen en vergrote tekst. Behoud daarnaast een echte browsertest voor CanvasKit, focus en gedeployde samenhang.
- Maak zichtbaar welke synthetische producten en toestanden de acceptatieomgeving afdekt, zodat een reviewer onmiddellijk ziet wat wel en niet onafhankelijk bewijsbaar is.
- Behoud voorlopig de bestaande taakgrens tussen Productoverzicht en Beheer. Beoordeel met representatieve Product Factory-fixtures opnieuw of metrics en secundaire acties nog te veel aandacht vragen.

### Inspiratiebronnen

- [Flutter teststrategie](https://docs.flutter.dev/testing/overview) — Flutter adviseert veel unit- en widgettests plus voldoende integratietests voor belangrijke gebruikspaden. Dit past bij de bestaande sterke widgettests en het geconstateerde gat in gedeployd browserbewijs.
- [Flutter integration_test](https://docs.flutter.dev/testing/integration-tests) — Biedt een framework-eigen manier om complete Flutter-flows te laden, zichtbare inhoud te verifiëren en acties uit te voeren met synthetische scenario’s.
- [Flutter golden-file matcher](https://api.flutter.dev/flutter/flutter_test/MatchesGoldenFile-class.html) — Sluit aan op de bestaande cycluskaart-golden en kan visuele regressies van bewijsregels en beheerstatussen vroeg zichtbaar maken.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://product-factory.vdzonsoftware.nl) | 2026-08-14 | Publiek bereikbare interface; geen hergebruiklicentie zichtbaar, daarom rechten onbekend. | Exact geconfigureerde productie-URL voor browsercontrole van bereikbaarheid en authenticatie. |
| [bron](https://product-factory-acceptance.vdzonsoftware.nl) | 2026-08-14 | Publiek bereikbare acceptatie-interface; geen hergebruiklicentie zichtbaar, daarom rechten onbekend. | Primaire bron voor daadwerkelijke CanvasKit-weergave, veilige navigatie en bruikbaarheidsbeoordeling met nepdata. |
| [bron](https://github.com/robbertvdzon/product-factory) | 2026-08-14 | Publieke repository; GitHub API rapporteert license: null, dus geen repositorylicentie aangetroffen. | Primaire bron voor repositorystructuur en aanwezige testbestanden. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/README.md) | 2026-08-14 | Publiek bronbestand; repositorylicentie niet aangetroffen. | Primaire beschrijving van doel, grenzen en relatie met Software Factory. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md) | 2026-08-14 | Publiek bronbestand; repositorylicentie niet aangetroffen. | Primaire functionele beschrijving van cyclusflow, dashboard, Beheer en de productspecifieke bewijsregel. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/iteration_evidence_overview_test.dart) | 2026-08-14 | Publieke broncode; repositorylicentie niet aangetroffen. | Toont welke Product Factory-bewijsregelgevallen met synthetische data worden getest. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/management_view_test.dart) | 2026-08-14 | Publieke broncode; repositorylicentie niet aangetroffen. | Onderbouwt de bedoelde scheiding en regressiedekking van Productoverzicht en Beheer. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/goldens/iteration_cycle_card_states.png) | 2026-08-14 | Publiek beeldbestand; repositorylicentie niet aangetroffen. | Toont dat al een visuele golden voor cycluskaartstatussen bestaat. |
| [bron](https://docs.flutter.dev/testing/overview) | 2026-08-14 | Documentatie CC BY 4.0; codevoorbeelden BSD-3-Clause volgens de Flutter-voorwaarden. | Autoritatieve onderbouwing voor veel widgettests gecombineerd met voldoende integratietests voor belangrijke gebruikspaden. |
| [bron](https://docs.flutter.dev/testing/integration-tests) | 2026-08-14 | Documentatie CC BY 4.0; codevoorbeelden BSD-3-Clause volgens de Flutter-voorwaarden. | Autoritatieve aanpak voor het geautomatiseerd laden en bedienen van complete Flutter-flows. |
| [bron](https://docs.flutter.dev/tos) | 2026-08-14 | Vermeldt CC BY 4.0 voor site-inhoud en BSD-3-Clause voor codevoorbeelden; Flutter-merken zijn uitgezonderd. | Concrete rechtenindicatie voor de geraadpleegde Flutter-documentatie. |
| [bron](https://api.flutter.dev/flutter/flutter_test/MatchesGoldenFile-class.html) | 2026-08-14 | Flutter API-documentatie; CC BY 4.0 voor site-inhoud en BSD-3-Clause voor codevoorbeelden volgens de Flutter-voorwaarden. | Autoritatieve bron voor pixelvergelijking met goldenbestanden. |

## Productbeslissing

Voeg een kleine, deterministische Product Factory-acceptatieset toe waarmee het dashboard zijn eigen kernflow onafhankelijk kan bewijzen. De set bevat uitsluitend synthetische data voor productslug ‘product-factory’: één actieve cyclus en drie terminale cycli met respectievelijk een expliciete, afgeleide en onbekende beslisbron. Minstens één terminale cyclus heeft gekoppelde opbrengsten en één niet. Automatiseer één eigenaarspad dat het Productoverzicht laadt, de compacte bewijsregel opent en sluit, naar Beheer navigeert en een storydetail opent. Leg voor de compacte bewijsregel visuele referenties vast op een breed en smal scherm. Toon in acceptatie kort dat de gegevens synthetisch zijn en welke toestanden worden afgedekt. Raak productieauthenticatie, bestaande cycli, data van andere producten en de koppeling met Software Factory niet aan.

**Waarom:** De scheiding tussen dagelijks gebruik en Beheer is al zichtbaar en begrijpelijk, maar de acceptatieomgeving bevat alleen hkh-autopilot-data. Daardoor kan juist het productspecifieke gedrag van Product Factory—waaronder de compacte bewijsregel en de weergave van beslisbronnen—niet onafhankelijk in de gedeployde interface worden beoordeeld. Gerichte widgettests bestaan al; de kleinste logische vervolgstap is daarom geen nieuwe dashboardfunctie, maar een privacy-minimale acceptatieset en één complete browserflow. Dit maakt de nog openstaande onderdelen van roadmap-epics 0001 en 0002 toetsbaar zonder migraties of wijzigingen aan andere producten. Onzeker blijft of de bewijsregel hiermee ook werkelijk prettig en scanbaar blijkt; deze richting maakt dat oordeel mogelijk, maar loopt er niet op vooruit.

### Prioriteiten
- Maak eerst vaste, fictieve Product Factory-scenario’s die actieve en terminale cycli, gekoppelde en ongekoppelde opbrengsten en expliciete, afgeleide en onbekende beslisbronnen afdekken.
- Bewijs daarna één complete, niet-mutatieve eigenaarflow: Productoverzicht laden, bewijsregel openen en sluiten, Beheer openen en storydetail bekijken.
- Voeg visuele controle toe voor de compacte bewijsregel op een breed en smal scherm en behoud de bestaande componenttests als snelle regressielaag.
- Maak in acceptatie zichtbaar dat de dataset synthetisch is en welke toestanden zij wel en niet bewijst.
- Houd de wijziging geïsoleerd en terugdraaibaar: geen oude cycli migreren, geen authenticatie aanpassen, geen productiegegevens gebruiken en niets aan Software Factory leveren.

### Besluiten
- **Gebruik uitsluitend synthetische data met productslug ‘product-factory’ in de acceptatieomgeving.** — De huidige acceptatieomgeving bewijst alleen hkh-autopilot-gedrag. Een eigen synthetische productscope voorkomt wijzigingen aan andere producten en maakt de productspecifieke bewijsregel zichtbaar.
- **Beperk de eerste scenarioverzameling tot één actieve cyclus en drie terminale beslisvarianten: expliciet, afgeleid en onbekend.** — Deze compacte matrix dekt zowel de kern van het hoofdscherm als de open traceerbaarheidsvraag af, zonder historische data te migreren of alle statuscombinaties ineens te modelleren.
- **Automatiseer één integratiepad over Productoverzicht, bewijsregel, Beheer en storydetail.** — De repository heeft gerichte widgetdekking, terwijl geen dashboard-integratietestmap is aangetroffen. Flutter adviseert voldoende integratietests voor belangrijke gebruikspaden naast unit- en widgettests.
- **Leg alleen voor de productspecifieke bewijsregel brede en smalle visuele referenties vast.** — Dit sluit aan op de bestaande golden-aanpak en toetst precies het nog onbewezen layout-risico, zonder een brede en onderhoudsintensieve screenshotverzameling te introduceren.
- **Behoud de bestaande scheiding tussen Productoverzicht en Beheer tijdens deze richting.** — Acceptatie laat zien dat deze scheiding begrijpelijk werkt. Eerst representatief bewijs voor Product Factory verzamelen past beter bij ‘eerst begrijpen, dan wijzigen’ dan de navigatie opnieuw ontwerpen.

## UX-voorstel: Product Factory — deterministische acceptatiebewijsflow

**Gebruikersdoel:** Als producteigenaar wil ik in acceptatie snel vaststellen welke synthetische Product Factory-toestanden worden afgedekt, de herkomst en opbrengsten van terminale cycli kunnen inspecteren en daarna Beheer en een storydetail kunnen openen, zonder productiegegevens of mutatieve acties.

### Flow
1. Open het Productoverzicht met uitsluitend deterministische, synthetische metadata voor productslug ‘product-factory’.
2. Lees de melding ‘Synthetische acceptatiedata’ met de afgedekte toestanden: één actieve cyclus en drie terminale cycli met expliciete, afgeleide en onbekende beslisbron; gekoppelde en ongekoppelde opbrengsten.
3. Controleer dat de actieve cyclus als actief herkenbaar is en geen terminale bewijsregel toont.
4. Navigeer met toetsenbord of pointer naar een terminale cyclus en open de compacte bewijsregel.
5. Bekijk in het bewijsdetail de cyclusstatus, beslisbron en eventuele gekoppelde opbrengsten; onbekende of ontbrekende waarden worden letterlijk als ‘Onbekend’ of ‘Geen gekoppelde opbrengsten’ getoond.
6. Sluit het bewijsdetail; de focus keert terug naar de knop waarmee het werd geopend.
7. Open ‘Beheer’ via de hoofdnavigatie.
8. Open een synthetische story uit de Storywachtrij en bekijk beschrijving, acceptatiecriteria en criticusbeoordeling.
9. Sluit het storydetail; de focus keert terug naar de gekozen storyregel. De flow voert geen cyclusstart, verzending of andere mutatie uit.

### Wireframe

BREED SCHERM
┌────────────────────────────────────────────────────────────────────┐
│ Product Factory                         [Productoverzicht] [Beheer] │
├────────────────────────────────────────────────────────────────────┤
│ ℹ Synthetische acceptatiedata                                   │
│ Dekking: 1 actief · 3 terminaal · bronnen: expliciet/afgeleid/?   │
├────────────────────────────────────────────────────────────────────┤
│ Product Factory                                                    │
│ [Start productcyclus nu]                                           │
│                                                                    │
│ ┌ Actieve cyclus ────────────────────────────────────────────────┐ │
│ │ Acceptatiecyclus actief                         Status: Actief │ │
│ └───────────────────────────────────────────────────────────────┘ │
│ ┌ Terminale cyclus ─ expliciet ─────────────────────────────────┐ │
│ │ Afgerond · bron: Expliciet · 2 opbrengsten [Bekijk bewijs ▾] │ │
│ │   Beslisbron: expliciete acceptatiebeslissing                 │ │
│ │   Opbrengsten: Story A, Story B                 [Sluiten]      │ │
│ └───────────────────────────────────────────────────────────────┘ │
│ ┌ Terminale cyclus ─ afgeleid ──────────────────────────────────┐ │
│ │ Afgerond · bron: Afgeleid · geen opbrengsten [Bekijk bewijs] │ │
│ └───────────────────────────────────────────────────────────────┘ │
│ ┌ Terminale cyclus ─ onbekend ──────────────────────────────────┐ │
│ │ Afgerond · bron: Onbekend · 1 opbrengst      [Bekijk bewijs] │ │
│ └───────────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────────┘

SMAL SCHERM
┌──────────────────────────────┐
│ Product Factory       [Menu] │
├──────────────────────────────┤
│ ℹ Synthetische data         │
│ 1 actief · 3 terminaal       │
│ Bronnen: expliciet,          │
│ afgeleid, onbekend           │
├──────────────────────────────┤
│ Product Factory              │
│ [Start productcyclus nu]     │
│ ┌──────────────────────────┐ │
│ │ Afgerond                │ │
│ │ Bron: Expliciet         │ │
│ │ 2 opbrengsten           │ │
│ │ [Bekijk bewijs]         │ │
│ └──────────────────────────┘ │
└──────────────────────────────┘

BEHEER
┌────────────────────────────────────────────────────────────────────┐
│ Product Factory                         [Productoverzicht] [Beheer] │
├────────────────────────────────────────────────────────────────────┤
│ Storywachtrij                                                      │
│ [Synthetische story: Bewijsregel toegankelijk maken             >] │
│                                                                    │
│ DIALOOG: Storydetail                                               │
│ Titel · Beschrijving · Acceptatiecriteria · Criticusbeoordeling    │
│                                                     [Sluiten]      │
└────────────────────────────────────────────────────────────────────┘

### Interactiehypotheses
- Als de synthetische-data-indicator boven de productinhoud staat, kan een geautomatiseerde semantiekstest bevestigen dat deze vóór cyclusdata wordt aangekondigd en exact de vier afgedekte toestanden noemt.
- Als actieve en terminale cycli een expliciet tekstlabel hebben, kunnen widget- en integratietests de status onderscheiden zonder uitsluitend kleur, positie of pictogrammen te gebruiken.
- Als de bewijsregel beslisbron en opbrengstaantal compact toont, kan een integratietest voor elk terminaal scenario de juiste combinatie vinden zonder het detail eerst te openen.
- Als ‘Onbekend’ en ‘Geen gekoppelde opbrengsten’ expliciet worden weergegeven, kunnen tests bevestigen dat ontbrekende metadata niet als lege ruimte, fout of verzonnen herkomst verschijnt.
- Als openen en sluiten echte knoppen met stabiele semantische labels zijn, kan een browsertest de bewijsregel met Enter/Spatie bedienen en controleren dat focus na sluiten terugkeert naar de oorspronkelijke knop.
- Als Productoverzicht en Beheer afzonderlijke navigatiebestemmingen blijven, kan één niet-mutatieve integratietest de route Productoverzicht → bewijsdetail → Beheer → storydetail deterministisch voltooien zonder productieauthenticatie of externe systemen aan te spreken — streefwaarde: alle stappen slagen en er worden nul mutatieve netwerkverzoeken verstuurd, geverifieerd met een request-spy/mockserver test harness; dit vereist application test instrumentation, niet alleen DOM-inspectie in Flutter CanvasKit/LIVE_REGION-accessibility mode en capture van alle fetch/XHR plus WebSocket handshake/payloads en service-worker/background-sync verzoeken gedurende de volledige testcase, met een allowlist van uitsluitend read-only methoden/endpoints en een expliciete fail bij elke POST/PUT/PATCH/DELETE of mutatief bericht; non-HTTP side effects buiten deze geïnstrumenteerde kanalen vallen buiten deze claim en de testomgeving moet externe koppelingen vervangen door fakes/mocks die elke aanroep als on

### Toegankelijkheid
- Alle interactieve elementen zijn bereikbaar in een logische toetsenbordvolgorde; er is geen keyboard trap in bewijs- of storydetails.
- Openen werkt met Enter en Spatie, sluiten met de zichtbare knop en Escape. Na sluiten keert focus terug naar de trigger.
- Gebruik zichtbare focusindicatoren met minimaal 3:1 contrast ten opzichte van aangrenzende kleuren; gewone tekst heeft minimaal 4,5:1 contrast en grote tekst minimaal 3:1.
- Status, beslisbron en opbrengsten worden als tekst aangeboden en nooit uitsluitend via kleur of pictogram gecommuniceerd.
- Knoppen hebben unieke toegankelijke namen, bijvoorbeeld ‘Bekijk bewijs van terminale cyclus expliciet’. Uitgevouwen toestand wordt programmatisch doorgegeven.
- Dialogs hebben een programmatische naam, initiële focus op betekenisvolle inhoud of de sluitknop en een correcte modale semantiek.
- Bij 200% tekstvergroting en op het smalle referentieformaat blijft alle inhoud beschikbaar zonder horizontaal scrollen; regels mogen verticaal uitvouwen.
- Golden-tests op breed en smal formaat worden aangevuld met semantiek-, focusvolgorde-, tekstschaal- en geautomatiseerde contrastcontroles; pixelvergelijking alleen bewijst geen toegankelijkheid.

### Privacy
- Gebruik uitsluitend vaste, fictieve operationele metadata van Product Factory: productslug, synthetische titels, statussen, datums, beslisbroncategorieën en fictieve storykoppelingen.
- Neem geen namen, e-mailadressen, account-id’s, prompts, tokens, stacktraces, vrije gebruikersinvoer of data van andere producten op.
- Gebruik geen kopie van productie- of hkh-autopilot-data; de fixture is geïsoleerd onder productslug ‘product-factory’.
- Laat de testflow uitsluitend lezen. Cyclusstart, storylevering, instellingenwijzigingen en Software Factory-koppelingen zijn uitgeschakeld of vervangen door fakes.
- Log in testuitvoer alleen scenario-id, teststap, status en foutcode; dump geen scherminhoud, headers, cookies of authenticatiemateriaal.
- Maak de synthetische aard en de precieze scenariodekking zichtbaar, zodat testdata niet met echte operationele gegevens wordt verward.
- Geautomatiseerde tests controleren dat fixtures alleen toegestane velden en vooraf vastgelegde fictieve waarden bevatten en falen bij onverwachte persoonsgegevens of productslugs.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is klein, geïsoleerd en autonoom uitvoerbaar. De synthetische acceptatiedata blijft binnen de privacyregel, gebruikt bestaande dashboardlogica, bouwt terecht voort op de gepubliceerde stories 65 en 69 en bevat geautomatiseerde controles voor determinisme, omgevingsisolatie en regressies. Er is geen handmatige test, eigenaarbesluit, account, betaling of externe systeemwijziging vereist.

## Geaccepteerde storykandidaten

### Voeg een deterministische synthetische Product Factory-dataset toe aan acceptatie

_Sleutel: `deterministische-product-factory-acceptatieset`_

Voeg uitsluitend aan de acceptatieomgeving een vaste, synthetische dataset toe voor productslug ‘product-factory’. De dataset bevat exact één actieve cyclus en drie terminale cycli waarvan de bestaande beslisbronclassificatie respectievelijk expliciet, afgeleid en onbekend oplevert. Minstens één terminale cyclus heeft aantoonbaar gekoppelde fictieve stories en minstens één toont geen gekoppelde opbrengsten. Toon boven het Product Factory-overzicht een compacte melding ‘Synthetische acceptatiedata’ met deze scenariodekking. Gebruik alleen vooraf vastgelegde fictieve waarden en isoleer de fixtures van productie, andere productslugs en Software Factory-koppelingen. Deze story voegt nog geen integratieflow of nieuwe dashboardlogica toe; zij maakt de bestaande compacte bewijsregels en beheerweergave autonoom en deterministisch toetsbaar.

**Acceptatiecriteria**
- De acceptatieomgeving laadt voor productslug ‘product-factory’ exact vier vaste cyclusscenario’s: één actieve cyclus zonder terminale bewijsregel en drie terminale cycli die via de bestaande logica respectievelijk een expliciete, afgeleide en onbekende beslisbron tonen.
- Minstens één terminale fixture bevat expliciete, uniek aan die cyclus gekoppelde fictieve stories en minstens één terminale fixture bevat geen gekoppelde opbrengsten; geautomatiseerde tests verifiëren beide toestanden in de bestaande compacte bewijsweergave.
- Boven de Product Factory-inhoud staat zichtbaar en semantisch vóór de cyclusgegevens de melding ‘Synthetische acceptatiedata’, inclusief ‘1 actief’, ‘3 terminaal’ en de afgedekte beslisbroncategorieën expliciet, afgeleid en onbekend.
- Een geautomatiseerde fixturevalidatie faalt bij een andere productslug, niet-allowlisted velden of waarden, persoonsgegevens, prompts, tokens, stacktraces, vrije gebruikersinvoer en verwijzingen naar echte productie- of hkh-autopilot-records.
- De acceptatiefixtures gebruiken vaste identifiers, titels, statussen en tijdstippen, zodat herhaald laden exact dezelfde sortering, labels, beslisbronclassificaties en storykoppelingen oplevert.
- Geautomatiseerde regressietests bevestigen dat de fixtures alleen in de acceptatieconfiguratie beschikbaar zijn en geen productieauthenticatie, bestaande cycli, gegevens van andere producten, API-contracten, opslag of Software Factory-leveringen wijzigen.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/iteration_evidence_overview_test.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/iteration_evidence_overview_test.dart), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/management_view_test.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/management_view_test.dart)

Afhankelijkheden: story:69, story:65 (herkend als bestaande stories: 69, 65)

Risico's: Acceptatiespecifieke fixtures kunnen door configuratiefouten buiten acceptatie beschikbaar worden; een geautomatiseerde omgevingsgrens moet dit blokkeren., Fixtures kunnen na wijziging van de beslisbronclassificatie ongemerkt een andere categorie opleveren; tests moeten de resulterende zichtbare classificatie vastzetten zonder productielogica te dupliceren., Een synthetische dataset bewijst de renderbare toestanden, maar nog niet de volledige gedeployde browsernavigatie, focusflow of CanvasKit-layout; dat blijft geschikt voor een afzonderlijke vervolgstory.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
