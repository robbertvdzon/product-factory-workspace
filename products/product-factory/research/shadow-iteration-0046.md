---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0046
date: 2026-08-14
status: approved
sources:
  - https://github.com/robbertvdzon/product-factory/blob/main/README.md
  - https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md
  - https://github.com/robbertvdzon/product-factory/tree/main/dashboard-frontend/test
  - https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/iteration_evidence_overview_test.dart
  - https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/management_view_test.dart
  - https://product-factory.vdzonsoftware.nl
  - https://product-factory-acceptance.vdzonsoftware.nl
  - https://www.atlassian.com/software/jira/guides/boards/overview
  - https://linear.app/docs/default-team-pages
  - https://linear.app/docs/display-options
  - https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs
  - https://www.w3.org/WAI/WCAG22/Understanding/
---
# Productcyclus 46

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Belangrijkste nog onbeantwoorde productvraag: hoe blijft de eigenaar per product georiënteerd wanneer meerdere producten en hun cycli in één dashboard staan? De synthetische Product Factory-acceptatieset uit iteratie 45 staat live en maakt bewijsregels en storykoppelingen toetsbaar. Tegelijk toont acceptatie nu een nieuw schaalbaarheidsprobleem: twee volledige productkaarten worden gevolgd door één gemengde cyclusstroom, waarin HkH Autopilot vóór de Product Factory-resultaten staat. Daardoor vormen starten, opbrengsten begrijpen en stories volgen nog geen direct scanbare productspecifieke eenheid. Dit is een onderzoeksrichting, geen productbesluit.

### De acceptatieset uit iteratie 45 staat daadwerkelijk live

Na een aanvankelijke Dashboard API 500 en een veilige herlaadactie verscheen de melding ‘Synthetische acceptatiedata’ met één actief en drie terminale scenario’s en expliciet, afgeleid en onbekend beslisgedrag. Beheer toont twee voltooide synthetische Product Factory-stories. Een storydetail toont status, sleutel, fase, beschrijving, acceptatiecriterium en criticusbeoordeling.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md)

### Het hoofdscherm is niet productspecifiek georiënteerd

Acceptatie toont twee volledige productkaarten en daarna één gezamenlijke sectie ‘Productcycli en onderzoekssessies’. De eerste zichtbare cyclus is van hkh-autopilot; de Product Factory-bewijsregels liggen lager. De compacte bewijsregel verdicht dus wel afzonderlijke cycli, maar maakt de drie gewenste eigenaarstaken nog niet tot één snel vindbare Product Factory-flow.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md)

### Multi-productgebruik is structureel, niet alleen acceptatiedata

De repository beschrijft Product Factory als een systeem voor ieder geregistreerd product, waarbij nieuwe producten als data worden toegevoegd. Het functioneel overzicht beschrijft productkaarten en één cycluslijst, maar geen productkeuze, productspecifieke route of groepering. Meer producten zullen de huidige oriëntatievraag daarom waarschijnlijk versterken.

Bronnen: [https://github.com/robbertvdzon/product-factory/blob/main/README.md](https://github.com/robbertvdzon/product-factory/blob/main/README.md), [https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md)

### Beheer is rustiger, maar bevat gemengde productscope

De afzonderlijke Beheer-weergave houdt globale stories en de wachtrij buiten het dagelijkse hoofdscherm. Product en iteratie staan als metadata bij regels, maar Product Factory- en HkH-items blijven in dezelfde lijsten staan zonder zichtbare filter- of groepsscope.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/management_view_test.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/management_view_test.dart)

### Componenttests bewijzen nog niet de complete eigenaarstaak

De publieke testmap bevat gerichte tests voor bewijsregels, beheer, beslisbronnen, instellingen en de acceptatiemelding. In de geraadpleegde repositoryboom is geen dashboard-frontend/integration_test-map aangetroffen. Dit ondersteunt de beperkte inferentie dat losse componenten sterk zijn afgedekt, maar niet dat een eigenaar in de volledige multi-productpagina snel het juiste product, de juiste cyclus en de gekoppelde stories vindt.

Bronnen: [https://github.com/robbertvdzon/product-factory/tree/main/dashboard-frontend/test](https://github.com/robbertvdzon/product-factory/tree/main/dashboard-frontend/test), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/iteration_evidence_overview_test.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/iteration_evidence_overview_test.dart), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/management_view_test.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/management_view_test.dart)

### Bestaande producten gebruiken expliciete scope en verdieping

Jira onderscheidt alle werk in een space van geselecteerde boardweergaven en ondersteunt aparte en cross-space boards. Linear biedt hoog-niveau cyclusvergelijking, doorklik naar één cyclus en instelbare groepering en filtering. GitHub Actions toont eerst uitkomst en voortgang per run en biedt daarna diagnostische logs. Deze patronen zijn relevante inspiratie voor productscoping en overzicht-naar-detail, maar bepalen nog niet welke oplossing Product Factory nodig heeft.

Bronnen: [https://www.atlassian.com/software/jira/guides/boards/overview](https://www.atlassian.com/software/jira/guides/boards/overview), [https://linear.app/docs/default-team-pages](https://linear.app/docs/default-team-pages), [https://linear.app/docs/display-options](https://linear.app/docs/display-options), [https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs)

### Automatische statusveranderingen moeten toegankelijk blijven

Product Factory ververst dashboardgegevens automatisch. W3C-richtlijnen vragen dat statusinformatie over voortgang, resultaten en fouten programmatically determined is, zodat hulptechnologie veranderingen kan melden zonder focus te verplaatsen. Dit blijft relevant wanneer productfilters, samenvattingen of dynamische tellingen worden onderzocht.

Bronnen: [https://www.w3.org/WAI/WCAG22/Understanding/](https://www.w3.org/WAI/WCAG22/Understanding/), [https://www.w3.org/WAI/WCAG21/Understanding/status-messages.html](https://www.w3.org/WAI/WCAG21/Understanding/status-messages.html)

### Huidige applicatie

**Doel:** Product Factory organiseert voor een producteigenaar autonome productontwikkeling over meerdere geregistreerde producten: onderzoek, richtingkeuze, UX, storyvorming en kritiek. Daarna publiceert het dossiers, levert geaccepteerde kandidaten begrensd aan Software Factory, volgt uitvoering en gebruikt evaluaties in volgende cycli. Het dashboard moet vooral starten, begrijpen en volgen mogelijk maken zonder de eigenaar met interne agentdetails te belasten.

**Wat ontbreekt:**
- Het overzicht combineert meerdere volledige productkaarten met één gezamenlijke cyclusstroom; productspecifieke opbrengsten en stories vormen daardoor geen direct scanbare eenheid.
- De compacte Product Factory-bewijsregels staan lager dan de HkH-productkaart en minstens één HkH-cyclus; compactheid lost vindbaarheid per product niet vanzelf op.
- Beheer bevat stories uit meerdere producten in gemengde lijsten. Product en iteratie zijn metadata, maar er is geen zichtbare productscope of groepering.
- De acceptatieomgeving gaf bij de eerste run een Dashboard API 500 en herstelde na herladen. De foutweergave bood geen zichtbare herhaalactie of verdere herstelcontext.
- De synthetische Product Factory-kaart staat gepauzeerd en handmatig. De dataset bewijst bewijsregels en storykoppeling, maar niet de echte autonome startpresentatie van Product Factory zelf.
- Er is geen complete browser-integratietest aangetroffen die overzicht, productscope, bewijs en Beheer als één eigenaarstaak borgt.

### Verbetermogelijkheden

- Onderzoek een expliciete productscope op het hoofdscherm, bijvoorbeeld productkeuze, gegroepeerde secties of een productspecifieke overzichtsroute; vergelijk varianten op tijd tot de juiste cyclus en foutnavigaties.
- Houd binnen de gekozen productscope de drie eigenaarstaken bijeen: cyclus starten, eerdere opbrengsten begrijpen en voortgekomen stories volgen.
- Onderzoek een compacte portfolio-laag met per product alleen status, laatste cyclus en open blokkade, gevolgd door verdieping naar één product.
- Maak de actieve productcontext ook in Beheer zichtbaar en behoud bewust een optie ‘alle producten’ voor globale operationele controle.
- Voeg een niet-mutatieve end-to-end acceptatiecontrole toe die bij minstens twee producten de gekozen scope, bewijsregel, gekoppelde opbrengst en storydetail doorloopt op breed en smal scherm.
- Onderzoek de eerste-loadfout afzonderlijk: bied een begrijpelijke herhaalactie en onderscheid algemene API-uitval van gedeeltelijk niet-beschikbare gegevens, met toegankelijke statusmelding bij herstel.
- Toets met synthetische scenario’s ook de autonome Product Factory-presentatie zonder werkelijk een cyclus te starten; de huidige gepauzeerde handmatige kaart wijkt af van echt zelfgebruik.

### Inspiratiebronnen

- [Linear Cycles en display options](https://linear.app/docs/default-team-pages) — Toont hoog-niveau vergelijking met doorklik naar één scope; Linear laat views daarnaast gericht groeperen en filteren.
- [Jira boards en spaces](https://www.atlassian.com/software/jira/guides/boards/overview) — Maakt onderscheid tussen alle werk in een space en een geselecteerde workflowweergave, inclusief aparte en cross-space boards.
- [GitHub Actions workflow runs](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs) — Combineert scanbare runuitkomsten met verdieping naar jobs en doorzoekbare diagnostiek, zonder technische logs op het hoofdscherm te plaatsen.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/README.md) | 2026-08-14 | Publiek leesbare repository; geen LICENSE-bestand aangetroffen op de geraadpleegde hoofdbranch, dus hergebruikrechten onbekend. | Primaire bron voor het doel, de multi-productscope en systeemgrenzen. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md) | 2026-08-14 | Publiek leesbaar repositorydocument; geen afzonderlijke licentie aangetroffen, dus hergebruikrechten onbekend. | Primaire actuele functionele specificatie van cycli, dashboard, bewijsregels en acceptatiecatalogus. |
| [bron](https://github.com/robbertvdzon/product-factory/tree/main/dashboard-frontend/test) | 2026-08-14 | Publiek leesbare broncode; geen LICENSE-bestand aangetroffen, dus hergebruikrechten onbekend. | Primaire bron voor de actuele frontend-testinventaris. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/iteration_evidence_overview_test.dart) | 2026-08-14 | Publiek leesbare broncode; geen LICENSE-bestand aangetroffen, dus hergebruikrechten onbekend. | Primaire bron voor componenttests rond compacte bewijsregels en opbrengstkoppeling. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/management_view_test.dart) | 2026-08-14 | Publiek leesbare broncode; geen LICENSE-bestand aangetroffen, dus hergebruikrechten onbekend. | Primaire bron voor testdekking van de beheerweergave. |
| [bron](https://product-factory.vdzonsoftware.nl) | 2026-08-14 | Publiek bereikbare webinterface; geen afzonderlijke contentlicentie zichtbaar, dus rechtenstatus onbekend. | Actuele productieomgeving, uitsluitend geraadpleegd tot het loginpaneel. |
| [bron](https://product-factory-acceptance.vdzonsoftware.nl) | 2026-08-14 | Publiek raadpleegbare webinterface met verklaarde synthetische data; geen afzonderlijke contentlicentie zichtbaar, dus rechtenstatus onbekend. | Primaire bron voor de actuele UI, multi-productindeling, beheerflow en synthetische scenario’s. |
| [bron](https://www.atlassian.com/software/jira/guides/boards/overview) | 2026-08-14 | © Atlassian; publieke productdocumentatie, hergebruik onder Atlassians voorwaarden. | Inspiratie voor expliciete scope via space-, board- en cross-spaceweergaven. |
| [bron](https://linear.app/docs/default-team-pages) | 2026-08-14 | © Linear; publieke productdocumentatie, hergebruikrechten voorbehouden. | Inspiratie voor hoog-niveau cyclusoverzichten met verdieping naar één cyclus. |
| [bron](https://linear.app/docs/display-options) | 2026-08-14 | © Linear; publieke productdocumentatie, hergebruikrechten voorbehouden. | Inspiratie voor gebruikersgestuurde groepering, filtering en zichtbare eigenschappen. |
| [bron](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs) | 2026-08-14 | GitHub Docs: documentatie volgens GitHub onder CC BY 4.0 en codevoorbeelden onder MIT, tenzij anders aangegeven. | Inspiratie voor compacte runstatus met verdieping naar diagnostisch detail. |
| [bron](https://www.w3.org/WAI/WCAG22/Understanding/) | 2026-08-14 | W3C-document; W3C copyright en document use rules zijn van toepassing. | Officiële toegankelijkheidsuitleg voor reflow, toetsenbordbediening, naam/rol/waarde en statusmeldingen. |

## Productbeslissing

Maak het hoofdscherm productspecifiek: toon eerst een compacte productkeuze en vervolgens voor precies één gekozen product de drie kernacties als samenhangende flow: cyclus starten, compacte bewijsregels van eerdere cycli begrijpen en gekoppelde stories volgen. Kies bij binnenkomst deterministisch het laatst gebruikte product indien lokaal beschikbaar, anders het eerste product; maak de actieve productnaam steeds zichtbaar. Laat wisselen van product alleen de weergavescope veranderen en nooit cycli, stories of instellingen muteren. Neem dezelfde scope over in Beheer, met daar aanvullend een expliciete optie ‘Alle producten’. Deze kleine, terugdraaibare vervolgstap valt onder roadmap-epic theme-product-factory-0001 en verandert niets aan andere producten of de levering aan Software Factory.

**Waarom:** De huidige inrichting was begrijpelijk toen volledige productkaarten en één centrale cycluslijst nog voldoende overzicht boden: zij maken alle geregistreerde producten en activiteiten direct zichtbaar en Beheer houdt globale operationele lijsten buiten het dagelijkse hoofdscherm. Met meerdere producten ontstaat echter een oriëntatieprobleem: productkaarten, cycli en stories staan niet als één productspecifieke eigenaarstaak bijeen; op acceptatie verschijnen HkH-items vóór de Product Factory-bewijsregels. De gekozen richting behoudt bestaande gegevens en acties, maar begrenst uitsluitend hun presentatie. Daarmee sluit zij aan op de missie om het dashboard prettig en begrijpelijk te houden, voltooit zij de beoogde drie-actiestructuur van epic 0001 en blijft zij in isolatie toetsbaar en eenvoudig terug te draaien. Onzekerheid blijft bestaan over de beste standaardselectie; daarom wordt deze deterministisch en zonder server-side opslag gehouden.

### Prioriteiten
- P1 — Productspecifieke hoofdschermscope met permanent zichtbare actieve productnaam en een toegankelijke productkeuze.
- P1 — Binnen die scope de drie kernacties bijeenhouden: starten, compacte afzonderlijk gelabelde bewijsregels begrijpen en gekoppelde stories volgen.
- P1 — Bestaande compactheids- en bewijsvereisten van epic 0001 behouden; productscoping mag geen terugkeer naar grote uitklapbare kaarten veroorzaken.
- P2 — De actieve productscope meenemen naar Beheer, plus een bewuste optie ‘Alle producten’ voor globale controle.
- P2 — Een niet-mutatieve end-to-end acceptatiecontrole voor minstens twee producten toevoegen op breed en smal scherm: product kiezen, bewijsregel vinden, gekoppelde opbrengst volgen en storydetail openen; ook toetsen dat de selectie en dynamische tellingen programmatisch herkenbaar zijn voor hulptechnologie.

### Besluiten
- **Kies één actieve productscope op het hoofdscherm in plaats van één gemengde cyclusstroom.** — Dit maakt starten, begrijpen en volgen per product direct scanbaar, terwijl de onderliggende multi-productgegevens en het gedrag van hkh en hkh-autopilot onaangeraakt blijven.
- **Gebruik een compacte productkeuze met verdieping naar het gekozen product; introduceer geen nieuwe productroute of server-side voorkeursopslag in deze stap.** — Een presentatiefilter is de kleinste omkeerbare ingreep. Het volgt het bewezen overzicht-naar-detailpatroon zonder navigatiearchitectuur, authenticatie of persistentie te veranderen.
- **Behoud compacte, niet-uitklapbare bewijsregels binnen de actieve productscope en toon gekoppelde stories daar direct bij.** — Productscoping lost vindbaarheid op, maar mag de nog open acceptatiekloof van epic 0001 niet maskeren. De bestaande componenttests bieden een basis om compact bewijs en koppelingen te behouden.
- **Neem de productcontext mee naar Beheer en bied daar expliciet ‘Alle producten’ aan.** — Dagelijks volgen profiteert van een gerichte scope, terwijl globale operationele controle legitiem blijft. Een expliciete alle-productenstand voorkomt dat gefilterde en globale lijsten stilzwijgend door elkaar lopen.
- **Borg de volledige eigenaarstaak met een niet-mutatieve browseracceptatie voor twee producten en toegankelijke dynamische statusinformatie.** — De gevonden tests dekken losse componenten, maar tonen niet aan dat een eigenaar in de volledige multi-productflow snel het juiste bewijs en storydetail vindt. Automatische verversing en scopewissels moeten bovendien zonder focusverplaatsing herkenbaar blijven voor hulptechnologie.

## UX-voorstel: Productspecifiek productoverzicht — kleine MVP-stap

**Gebruikersdoel:** Als producteigenaar wil ik één actieve productcontext kiezen en daarin achtereenvolgens een cyclus kunnen starten, eerdere opbrengsten kunnen begrijpen en gekoppelde stories kunnen volgen, zonder gegevens van andere producten te zien of te wijzigen.

### Flow
1. Open het hoofdscherm. Selecteer deterministisch het lokaal laatst gebruikte beschikbare product; ontbreekt dat, selecteer dan het eerste product in de ontvangen productvolgorde.
2. Toon de actieve productnaam permanent in de paginakop en markeer hetzelfde product als geselecteerd in de compacte productkeuze.
3. Toon binnen deze scope drie opeenvolgende secties: ‘Cyclus starten’, ‘Eerdere cycli’ en ‘Gekoppelde stories’.
4. Laat ‘Cyclus starten’ de bestaande startmogelijkheid en operationele productstatus tonen. De MVP introduceert geen nieuw startgedrag.
5. Toon bij ‘Eerdere cycli’ compacte, afzonderlijk gelabelde bewijsregels met status, opbrengst en beslisbron; bied alleen bestaande niet-muterende verdieping aan.
6. Toon per cyclus de eraan gekoppelde stories en laat een storydetail openen met behoud van de actieve productcontext.
7. Bij een productwissel verandert uitsluitend de zichtbare scope. Focus blijft op de productkeuze en een programmatisch herkenbare statusmelding noemt het nieuw getoonde product en de bijgewerkte aantallen.
8. Open ‘Beheer’ met dezelfde actieve productscope. Bied daar daarnaast expliciet ‘Alle producten’ aan; deze optie bestaat niet op het hoofdscherm.
9. Bij terugkeer uit Beheer blijft de lokale selectie behouden zolang het product nog beschikbaar is. Een verdwenen selectie valt deterministisch terug op het eerste beschikbare product.
10. Bij een laadfout blijft de productcontext zichtbaar en verschijnt een begrijpelijke, toetsenbordbedienbare ‘Opnieuw proberen’-actie. Herstel wordt als statusmelding aangeboden zonder focus te verplaatsen.

### Wireframe

BREED SCHERM
┌──────────────────────────────────────────────────────────────────────┐
│ Product Factory                         [Beheer]                     │
│ Actief product: Product Factory                                      │
│ Product: [ Product Factory ▼ ]                                      │
│ [statusmelding voor hulptechnologie; visueel alleen indien relevant] │
├──────────────────────────────────────────────────────────────────────┤
│ 1. CYCLUS STARTEN                                                   │
│ Operationele status · startmodus · [Bestaande startactie]           │
├──────────────────────────────────────────────────────────────────────┤
│ 2. EERDERE CYCLI                                                    │
│ Iteratie 45 · Voltooid · 1 actief / 3 terminaal                     │
│ Bewijs: expliciet … · afgeleid … · onbekend …                       │
│ Opbrengst: [Bekijken]                                                │
│ └─ Gekoppelde stories (2)                                           │
│    [Toegankelijke cyclusstatus] [Tweede story]                      │
│ Iteratie 44 · …                                                     │
├──────────────────────────────────────────────────────────────────────┤
│ 3. GEKOPPELDE STORIES                                               │
│ Filter binnen actief product · status · iteratie · [Storydetail]    │
└──────────────────────────────────────────────────────────────────────┘

SMAL SCHERM
┌──────────────────────────────┐
│ Product Factory      [Beheer]│
│ Actief product               │
│ [Product Factory         ▼]  │
├──────────────────────────────┤
│ 1. Cyclus starten            │
│ status                       │
│ [Bestaande startactie]       │
├──────────────────────────────┤
│ 2. Eerdere cycli             │
│ Iteratie 45 · Voltooid       │
│ compacte bewijsregels        │
│ [Opbrengst] · [2 stories]    │
├──────────────────────────────┤
│ 3. Gekoppelde stories        │
│ storyregels                  │
└──────────────────────────────┘

BEHEER
Actief product: [Product Factory ▼] met optie [Alle producten]. Elke lijst toont de actieve scope in de kop. Storydetail opent als bestaande dialoog of pagina en vermeldt product en iteratie.

### Interactiehypotheses
- Als één product actief is, bevat de hoofdscherm-DOM na laden uitsluitend cycli en stories waarvan productKey gelijk is aan de geselecteerde productKey. Automatiseer dit met synthetische data voor minstens twee producten.
- Als een geldige lokale productKey bestaat, wordt die geselecteerd; bij een onbekende of ontbrekende sleutel wordt exact het eerste beschikbare product geselecteerd. Test beide toestanden zonder serveropslag.
- Als een agent van Product Factory naar HkH Autopilot wisselt, veranderen alleen gefilterde presentatiegegevens en lokale voorkeur; API-spies registreren geen muterende requests en bronobjecten blijven identiek.
- Binnen iedere productscope staan de drie sectiekoppen in DOM- en tabvolgorde als ‘Cyclus starten’, ‘Eerdere cycli’ en ‘Gekoppelde stories’. Test dit op brede en smalle viewports.
- Elke compacte cyclusregel exposeert programmatisch product, iteratie, status, bewijslabels, opbrengstkoppeling en aantal gekoppelde stories, zonder standaard uitgeklapte detailkaart. Controleer semantiek en afmetingen met component- en snapshottests.
- Vanuit minstens twee productscope-scenario’s kan een browsertest via cyclus, opbrengstkoppeling en gekoppelde story naar het juiste storydetail navigeren; het detail bevat dezelfde productKey en iterationKey als de broncyclus. De test blijft volledig niet-mutatief behalve lokale UI-state binnen de testsessie als operationele metadata van Product Factory zelf product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory-product-factory

### Toegankelijkheid
- Gebruik een native select-element of een equivalent met correct toegankelijke naam, rol, waarde en volledig toetsenbordgedrag; vermijd een reeks alleen visueel geselecteerde kaarten.
- Maak de actieve productnaam zichtbaar als tekst én programmatisch bepaalbaar. Kleur is nooit de enige selectie-indicator.
- Behoud een logische koppenstructuur en DOM-volgorde. Bij reflow naar een smal scherm blijft de lees- en tabvolgorde gelijk aan de visuele volgorde.
- Plaats scopewissel- en herstelmeldingen in een rustige statusregio, bijvoorbeeld role=status met aria-live=polite. Verplaats de focus niet bij automatische verversing.
- Laat de focus na productwissel op de productkeuze staan. Bij openen van storydetail gaat focus naar de detailkop; bij sluiten terug naar de activerende storylink.
- Alle acties zijn met alleen toetsenbord bereikbaar, hebben een zichtbare focusindicator en voldoen aan minimaal 4,5:1 tekstcontrast en 3:1 contrast voor grote tekst, bedieningselementen en focusindicatoren.
- Geef dynamische aantallen een volledige toegankelijke naam, bijvoorbeeld ‘2 gekoppelde stories voor Product Factory’; voorkom losse, contextloze cijfers.
- Automatiseer controles met semantische widgettests, toetsenbordnavigatietests, axe-achtige browserregels, contrastasserties en viewporttests. Vereis geen handmatige toegankelijkheidscontrole.

### Privacy
- Gebruik uitsluitend operationele metadata van Product Factory zelf: productKey, productnaam, iterationKey, cyclusstatus, bewijsstatus, storyKey, storystatus en de lokale scopevoorkeur.
- Sla de laatst gekozen productKey alleen lokaal op; voeg voor deze MVP geen server-side profiel, gebruikersidentificatie, analytics-event of cross-productvoorkeur toe.
- Toon op het hoofdscherm nooit cycli, stories of tellingen van niet-geselecteerde producten. ‘Alle producten’ is alleen een expliciete Beheerstand.
- Een scopewissel mag geen product-, cyclus-, story- of instellingenmutatie veroorzaken. Automatiseer dit met netwerkasserties die muterende requests afwijzen.
- Gebruik in tests uitsluitend synthetische Product Factory-data. Neem geen persoonsgegevens, productie-inhoud of gebruikersdata van andere producten op in fixtures, screenshots, logs of foutmeldingen.
- Beperk foutmeldingen tot operationele status en herstelactie; toon geen tokens, accountgegevens, requestinhoud of interne gegevens van andere producten.
- Wis of negeer een lokaal opgeslagen productKey zodra die niet meer in de beschikbare productlijst voorkomt.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is autonoom uitvoerbaar en geautomatiseerd toetsbaar. De productscope gebruikt uitsluitend operationele Product Factory-metadata, veroorzaakt geen mutaties en bevat concrete toetsen voor filtering, lokale voorkeur, toegankelijkheid en Beheer. Er zijn geen materiële problemen die veilige bouw of toetsing van de kleine MVP onmogelijk maken.
- **WARNING · ACCESSIBILITY** — Het criterium dat secties in ‘tabvolgorde’ staan is technisch onnauwkeurig, omdat niet-interactieve sectiekoppen normaal geen tabstop zijn. Interpreteer en test dit als: correcte DOM- en leesvolgorde, waarbij de focusbare bedieningselementen binnen de secties dezelfde logische volgorde volgen. Dit blokkeert de uitvoering niet.
- **WARNING · ACCESSIBILITY** — De kandidaat borgt toetsenbordbediening, semantiek, focus en statusmeldingen, maar noemt in de acceptatiecriteria niet expliciet het bindende vereiste van voldoende tekst-, component- en focuscontrast. Dit kan binnen de bestaande geautomatiseerde component- of contrasttests worden meegenomen zonder nieuw productbesluit of handmatige controle.
- **INFO · CONSISTENCY** — De overlap met gepubliceerde stories 69 en 65 is bewust en aanvullend: compacte bewijsregels en de bestaande Beheer-weergave worden hergebruikt en als afhankelijkheden genoemd. Er is geen exact reeds geleverd resultaat.
- **INFO · RIGHTS** — Enkele repository- en inspiratiebronnen hebben onbekende of voorbehouden hergebruikrechten. De kandidaat vraagt echter alleen om implementatie in de eigen codebase en om toepassing van algemene interfacepatronen; overname van beschermde tekst, code of vormgeving is niet vereist.
- **INFO · PRIVACY** — Lokale opslag blijft beperkt tot de canonieke productslug als operationele metadata van Product Factory. Er worden geen persoonsgegevens, telemetrie of gegevens van andere producten toegevoegd of verwerkt.

## Geaccepteerde storykandidaten

### Bundel de drie kernacties onder één actieve productscope

_Sleutel: `productspecifieke-dashboardscope`_

Vervang op het hoofdscherm de volledige productkaarten en gemengde cyclusstroom door een compacte productkeuze met exact één actieve productscope. Gebruik de bestaande productslug als canonieke productidentificatie, met deze expliciete mapping: `Product.slug` voor productrecords, `Iteration.productSlug` voor cyclusrecords, de `productSlug` van de bijbehorende `Iteration` voor bewijsregels en `StoryCandidate.productSlug` voor storyrecords. Gebruik uitsluitend deze mapping voor selectie, filtering, lokale opslag, tellingen en detailnavigatie en borg haar in gedeelde frontendlogica en geautomatiseerde contracttests. Selecteer bij laden de lokaal laatst gekozen, nog beschikbare canonieke productidentificatie en anders deterministisch het eerste product uit de ontvangen volgorde; toon de actieve productnaam permanent. Presenteer binnen deze scope, in vaste volgorde, de bestaande onderdelen ‘Cyclus starten’, ‘Eerdere cycli’ en ‘Gekoppelde stories’. Filter cycli, bewijsregels, tellingen en stories uitsluitend op een exacte overeenkomst van de volgens deze mapping bepaalde productslug; records waarin die relatie ontbreekt of ambigu is, blijven buiten de productscope. Behoud de compacte, niet-uitklapbare bewijsregels uit story:69 en het bestaande start- en detailgedrag. Een productwissel wijzigt alleen lokale presentatiestatus en veroorzaakt geen muterende API-aanroep. Open Beheer vanuit dezelfde scope en voeg daar, naast afzonderlijke producten, de expliciete keuze ‘Alle producten’ toe; op het hoofdscherm bestaat die keuze niet. Sla uitsluitend de canonieke productslug lokaal op, verwijder een niet meer beschikbare voorkeur en voeg geen backendopslag, telemetrie, routing- of API-wijziging toe.

**Acceptatiecriteria**
- Een geautomatiseerde contracttest bewijst voor de bestaande modellen en synthetische fixtures de vaste mapping `Product.slug` → `Iteration.productSlug` → bewijsregel via `Iteration.productSlug` → `StoryCandidate.productSlug` en bewijst dat selectie, filtering, lokale opslag, tellingen en detailnavigatie uitsluitend de zo bepaalde productslug gebruiken.
- Met synthetische gegevens voor minstens twee producten selecteren geautomatiseerde tests een geldige lokaal opgeslagen canonieke productidentificatie; bij een ontbrekende of onbekende waarde wordt exact het eerste product in de ontvangen volgorde gekozen.
- Na laden bevat iedere hoofdschermsectie uitsluitend cycli, bewijsregels, tellingen en stories waarvan de volgens de vastgelegde mapping bepaalde productslug exact gelijk is aan `Product.slug` van het actieve product; records zonder eenduidige overeenkomst worden niet aan het geselecteerde product toegeschreven.
- De zichtbare en programmatisch bepaalbare actieve productnaam en de secties ‘Cyclus starten’, ‘Eerdere cycli’ en ‘Gekoppelde stories’ staan op brede en smalle viewports in deze DOM-, lees- en tabvolgorde.
- ‘Eerdere cycli’ behoudt de compacte, niet standaard uitklapbare bewijsregels met de afzonderlijk gelabelde velden van story:69; gekoppelde story-acties openen het bestaande juiste detail waarvan `StoryCandidate.productSlug` gelijk is aan `Iteration.productSlug` en waarvan het bestaande expliciete cycluskoppelveld naar die cyclus verwijst.
- Een geautomatiseerde netwerk- en toestandstest wisselt tussen twee producten en bewijst dat alleen de zichtbare scope en lokale productvoorkeur veranderen, dat geladen bronobjecten gelijk blijven en dat geen muterende HTTP-request wordt verstuurd.
- De productkeuze is volledig met het toetsenbord bedienbaar en exposeert naam, rol, actuele waarde en focusindicator; na wisselen blijft focus op de keuze en meldt een role=status/aria-live=polite-regio het gekozen product en de bijgewerkte aantallen zonder focusverplaatsing.
- Beheer opent standaard met dezelfde actieve canonieke productslug en toont die scope zichtbaar in elke lijstkop. Beheer biedt expliciet de optie ‘Alle producten’. Een geautomatiseerde test bewijst dat iedere afzonderlijke productscope uitsluitend records toont waarvan de volgens de vaste mapping bepaalde productslug exact overeenkomt en dat ‘Alle producten’ de bestaande globale lijsten toont; records met een ontbrekende of ambigue productrelatie verschijnen uitsluitend in ‘Alle producten’.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/README.md](https://github.com/robbertvdzon/product-factory/blob/main/README.md), [https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/iteration_evidence_overview_test.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/iteration_evidence_overview_test.dart), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/management_view_test.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/test/management_view_test.dart), [https://www.w3.org/WAI/WCAG21/Understanding/status-messages.html](https://www.w3.org/WAI/WCAG21/Understanding/status-messages.html)

Afhankelijkheden: story:69, story:65 (herkend als bestaande stories: 69, 65)

Risico's: Records met een ontbrekende of ambigue productslug worden conservatief buiten een afzonderlijke productscope gehouden en blijven in Beheer uitsluitend onder ‘Alle producten’ zichtbaar; geautomatiseerde contracttests bewaken de vaste mapping `Product.slug` → `Iteration.productSlug` → bewijsregel via `Iteration.productSlug` → `StoryCandidate.productSlug`., Lokale selectie kan verouderd raken wanneer een product verdwijnt of wordt hernoemd; de deterministische beschikbaarheidscontrole en fallback moeten vóór het renderen van gefilterde inhoud plaatsvinden., Het meenemen van scope naar Beheer kan bestaande globale operationele controle onbedoeld verbergen; daarom moet ‘Alle producten’ daar expliciet beschikbaar en geautomatiseerd getest blijven., Automatische gegevensverversing kan tellingen wijzigen terwijl een product actief is; statusmeldingen moeten wijzigingen toegankelijk maken zonder focus te verplaatsen of herhaaldelijk storende aankondigingen te veroorzaken.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
