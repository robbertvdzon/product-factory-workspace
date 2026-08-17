---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0053
date: 2026-08-17
status: approved
sources:
  - https://product-factory.vdzonsoftware.nl
  - https://product-factory-acceptance.vdzonsoftware.nl
  - https://github.com/robbertvdzon/product-factory
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/bugs.dart
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/iteration_evidence.dart
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/preview/AcceptanceDataFixtures.kt
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/resources/db/migration/V25__bugs_and_test_sessions.sql
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/resources/db/migration/V28__manual_cycle_start_origin.sql
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/test/manual_cycle_start_test.dart
  - https://github.com/robbertvdzon/product-factory/commit/bdd806d2e823
---
# Productcyclus 53

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Belangrijkste nog onbeantwoorde productvraag: hoe moet de mobiele informatiehiërarchie worden ingericht zodat de eigenaar de actieve productscope, cyclusstart, recente cyclusuitkomsten en gekoppelde stories direct vindt, zonder belangrijk bewijs te verbergen? Op 320 CSS-pixels komen nu de acceptatiemelding en vijf metriekkaarten vóór de productscope; ‘Cyclus starten’ verschijnt pas na PageDown en Productcessies en Stories liggen buiten de zichtbare horizontale navigatie. Daarnaast kan acceptatie de zelfkritische bugflow nog niet bewijzen, omdat de vaste dataset geen bugs of testsessies bevat. Er is geen productbesluit genomen en er zijn geen stories geschreven.

### Product Factory is de regiekamer voor autonome productontwikkeling

De repository beschrijft een systeem dat per geregistreerd product onderzoek, productkeuzes, UX-ontwikkeling en storyvorming organiseert, stories aan Software Factory aanbiedt en uitvoeringsresultaten in volgende iteraties verwerkt. Het dashboard is bedoeld voor de eigenaar om binnen één productscope cycli te starten, uitkomsten te begrijpen, stories te volgen en beheerinformatie te raadplegen.

Bronnen: [https://github.com/robbertvdzon/product-factory](https://github.com/robbertvdzon/product-factory), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md)

### De mobiele hiërarchie plaatst systeemmetrics vóór het dagelijkse werk

Op de visueel beoordeelde 320×900-weergave vullen de acceptatiemelding, navigatieacties en vijf losse metriekkaarten het eerste scherm en een groot deel van het volgende. Pas na PageDown verschijnen actieve productscope en ‘Cyclus starten’. Dit botst met de productrichting waarin starten, uitkomsten en stories binnen tien seconden vindbaar moeten zijn.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md)

### Kerninformatie is op acceptatie verdeeld over deels verborgen secties

Op breed scherm konden Productcessies, Stories en Bugs afzonderlijk worden geopend. Op 320px waren aanvankelijk alleen Overzicht en Roadmap zichtbaar; Productcessies en Stories vereisten onuitgelegde horizontale navigatie. Het actuele acceptatiescherm biedt daardoor wel alle onderdelen, maar presenteert de drie dagelijkse behoeften niet als één direct scanbare mobiele werkruimte.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/bugs.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/bugs.dart)

### Expliciete handmatige annulering is traceerbaar

Cyclus 9203 toonde in overzicht en detail beslisbron ‘Mens’, reden ‘Handmatig geannuleerd’, mechanisme ‘Handmatige annulering’ en een beslistijd. De vaste fixture en het datamodel bevatten hiervoor een expliciet beslisrecord. Dit ondersteunt de aanname dat handmatige annulering zonder afleiding kan worden gepresenteerd.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/preview/AcceptanceDataFixtures.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/preview/AcceptanceDataFixtures.kt), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/iteration_evidence.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/iteration_evidence.dart)

### Categorie en inferentiestatus zijn nog vermengd

Cyclus 9202 toont ‘Evaluatie-agent (Afgeleid)’. De frontend bouwt dit label door ‘(Afgeleid)’ aan de beslisbroncategorie toe te voegen. Daardoor blijft de bekende BUG-6 zichtbaar: de gesloten categorie en de epistemische status zijn niet afzonderlijk leesbaar.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/iteration_evidence.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/iteration_evidence.dart)

### Acceptatie bewijst de bug- en testsessieflow niet

De versieerbare acceptatiecatalogus bevat exact cycli, beslissingen, kandidaten en leveringen, maar geen bugs of testsessies. Daarom toont de Bugs-sectie ‘0 open’ en kan deze omgeving niet aantonen dat prioriteiten, bronherkomst, statusovergangen, blokkades en storykoppelingen voor bugs correct en compleet werken. Het product heeft hiervoor technisch al een productgebonden datamodel en UI.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/preview/AcceptanceDataFixtures.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/preview/AcceptanceDataFixtures.kt), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/resources/db/migration/V25__bugs_and_test_sessions.sql](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/resources/db/migration/V25__bugs_and_test_sessions.sql), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/bugs.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/bugs.dart)

### Broncode bevat de controleerbare startdialoog, maar de onderzochte acceptatiebuild is ouder

De actuele hoofdbranch documenteert en test de dialoog met autonome standaard, optionele eigenaarsvraag, voorafsamenvatting, focusbeheer en opgeslagen herkomst. Beheer op acceptatie toont build bdd806d2e823 van 16-08-2026 19:37; deze commit betreft een eerdere wijziging. Omdat de synthetische Product Factory-scope gepauzeerd is, kon de dialoog zonder mutatie niet in de draaiende omgeving worden geopend.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/test/manual_cycle_start_test.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/test/manual_cycle_start_test.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/resources/db/migration/V28__manual_cycle_start_origin.sql](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/resources/db/migration/V28__manual_cycle_start_origin.sql), [https://github.com/robbertvdzon/product-factory/commit/bdd806d2e823](https://github.com/robbertvdzon/product-factory/commit/bdd806d2e823), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### Vergelijkbare producten gebruiken een rustige kernlaag met expliciete verdieping

Linear gebruikt een afzonderlijke triage-inbox voor beoordelen, prioriteren, accepteren, dupliceren, afwijzen en uitstellen. Sentry zet kernimpact en acties bovenaan en verplaatst tijdlijn, koppelingen en diagnostiek naar detail. GitHub Projects ondersteunt taakgerichte opgeslagen views en filters voor ontbrekende metadata. Dit zijn bruikbare patronen voor onderzoek naar overzicht versus verdieping, zonder beschermde teksten of vormgeving over te nemen.

Bronnen: [https://linear.app/docs/triage](https://linear.app/docs/triage), [https://docs.sentry.io/product/issues/issue-details/](https://docs.sentry.io/product/issues/issue-details/), [https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects)

### Huidige applicatie

**Doel:** Product Factory is voor de producteigenaar een per product begrensde regiekamer die autonome productontwikkeling organiseert en zichzelf continu moet toetsen. Zij onderzoekt, kiest, ontwerpt en vormt stories, biedt geaccepteerde stories aan Software Factory aan, volgt uitvoering en gebruikt resultaten in volgende iteraties. Het dashboard bedient momenteel Product Factory en HKH Autopilot en moet vooral starten, eerdere uitkomsten begrijpen en voortgekomen stories volgen ondersteunen.

**Wat ontbreekt:**
- Op 320 CSS-pixels staan de acceptatiemelding en vijf metriekkaarten vóór productscope en cyclusstart; de primaire actie vereist PageDown.
- Productcessies en Stories zijn op smal scherm buiten het zichtbare deel van de horizontale sectienavigatie, zonder duidelijke overflowindicatie.
- Het acceptatiescenario bevat geen bugs of testsessies en kan deze zelfkritische productflow daarom niet deterministisch bewijzen.
- Een lege buglijst toont niet of alle aanleverbronnen recent en succesvol hebben gedraaid; nul registraties kan daardoor niet van ontbrekende dekking worden onderscheiden.
- Beslisbroncategorie en inferentiestatus zijn nog gecombineerd in labels zoals ‘Evaluatie-agent (Afgeleid)’.
- Productie blokkeert een afgemelde gebruiker langdurig met alleen een laadindicator voordat de handmatige Google-inlogkaart verschijnt.
- De zichtbare acceptatiebuild bdd806d2e823 loopt achter op de geraadpleegde hoofdbranch, waarin de controleerbare startdialoog al is vastgelegd.

### Verbetermogelijkheden

- Onderzoek een mobiele volgorde waarin actieve productscope, cyclusstart, recente cyclusbewijzen en gekoppelde stories vóór globale metriekkaarten staan.
- Beoordeel of globale tellingen op smalle schermen naar Beheer kunnen verhuizen of als secundaire, inklapbare samenvatting kunnen worden aangeboden.
- Maak Productcessies en Stories zonder verborgen horizontale scroll ontdekbaar, bijvoorbeeld via een expliciete overflowindicatie of een mobiele sectiekeuze.
- Breid de deterministische acceptatiecatalogus uit met synthetische bugs en testsessies die prioriteit, status, provenance, herhaling en storykoppeling afdekken.
- Toon bij een lege buglijst de dekking en versheid van roadmap- en testsessiebronnen; gebruik ‘Onbekend’ wanneer volledigheid niet aantoonbaar is.
- Presenteer de gesloten beslisbroncategorie en ‘afgeleid/expliciet/onbekend’ als afzonderlijke velden.
- Laat een mislukte of lege FedCM-selectie de handmatige Google-inlogkaart niet tientallen seconden blokkeren.

### Inspiratiebronnen

- [Linear Triage](https://linear.app/docs/triage) — Een afzonderlijke inbox voor gecontroleerde issue-intake met expliciete acceptatie, prioritering, duplicaat, afwijzing en uitstel. Rechtenindicatie: specifieke documentatielicentie niet vastgesteld.
- [Sentry Issue Details](https://docs.sentry.io/product/issues/issue-details/) — Plaatst kernimpact en acties bovenaan en bewaart tijdlijn, koppelingen, gebeurtenissen en diagnostiek voor verdieping. De onderliggende documentatierepository vermeldt FSL-1.1-Apache-2.0 met een Apache-2.0 future license.
- [GitHub Projects filters](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects) — Ondersteunt taakgerichte opgeslagen views, statusfilters en expliciete filters voor ontbrekende metadata. GitHub Docs is gelicentieerd onder CC BY 4.0.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://product-factory.vdzonsoftware.nl) | 2026-08-17 | Publiek bereikbaar achter Google-authenticatie; auteursrecht en hergebruiklicentie van de interface onbekend. | Exact geconfigureerde productie-URL voor verplicht productie-browserbewijs en beoordeling van de authenticatiebarrière. |
| [bron](https://product-factory-acceptance.vdzonsoftware.nl) | 2026-08-17 | Publiek raadpleegbare acceptatie-interface; auteursrecht en hergebruiklicentie onbekend. | Draaiende publieke omgeving met representatieve synthetische data, gebruikt voor brede en mobiele navigatie. |
| [bron](https://github.com/robbertvdzon/product-factory) | 2026-08-17 | Publieke repository; geen LICENSE-bestand op de repositoryroot aangetroffen, dus specifieke hergebruikrechten onbekend. | Repositorystructuur, actuele hoofdbranch en algemene productbeschrijving. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md) | 2026-08-17 | Geen repositorylicentie aangetroffen; hergebruikrechten onbekend. | Primaire beschrijving van doel, architectuur en verhouding tot Software Factory en de workspace. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md) | 2026-08-17 | Geen repositorylicentie aangetroffen; hergebruikrechten onbekend. | Actuele functionele beschrijving van cyclusstart, dashboardvolgorde, provenance en detailweergaven. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/bugs.dart) | 2026-08-17 | Geen repositorylicentie aangetroffen; hergebruikrechten onbekend. | Primaire bron voor sectienavigatie, bugtelling, prioriteitsblokkade en lege bugstaat. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/iteration_evidence.dart) | 2026-08-17 | Geen repositorylicentie aangetroffen; hergebruikrechten onbekend. | Primaire bron voor actieve en terminale presentatie, handmatige annulering en afgeleide beslisbronlabels. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/preview/AcceptanceDataFixtures.kt) | 2026-08-17 | Geen repositorylicentie aangetroffen; hergebruikrechten onbekend. | Definieert exact welke synthetische scenario’s acceptatie bevat en welke ontbreken. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/resources/db/migration/V25__bugs_and_test_sessions.sql) | 2026-08-17 | Geen repositorylicentie aangetroffen; hergebruikrechten onbekend. | Primaire bron voor productscope, prioriteit, status, herkomst en storykoppeling van bugs en testsessies. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/resources/db/migration/V28__manual_cycle_start_origin.sql) | 2026-08-17 | Geen repositorylicentie aangetroffen; hergebruikrechten onbekend. | Primaire bron voor de gesloten opgeslagen herkomstwaarden van handmatige starts. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/test/manual_cycle_start_test.dart) | 2026-08-17 | Geen repositorylicentie aangetroffen; hergebruikrechten onbekend. | Actueel bronbewijs voor gedrag en toegankelijkheid van de controleerbare startdialoog. |
| [bron](https://github.com/robbertvdzon/product-factory/commit/bdd806d2e823) | 2026-08-17 | Publieke repositorycommit zonder aangetroffen overkoepelende licentie; hergebruikrechten onbekend. | Koppelt de op acceptatie zichtbare build-ID aan een concrete publieke commit. |

## Productbeslissing

Herorden het mobiele hoofdscherm tot één rustige productscope voor de drie kernhandelingen. Op 320 CSS-pixels staan na een compacte acceptatie-/omgevingsaanduiding achtereenvolgens: actief product, cyclusstart, recente cyclusuitkomsten als toestandsbewuste bewijsregels en gekoppelde stories. Verplaats de vijf globale metriekkaarten op mobiel naar een secundaire, standaard ingeklapte samenvatting met een duidelijke ingang naar Beheer. Vervang de verborgen horizontale sectienavigatie door een volledig toetsenbordbedienbare mobiele sectiekeuze waarin Productcycli en Stories direct benoemd en bereikbaar zijn. Beperk deze richting tot presentatie en navigatie binnen Product Factory: geen datamigratie, authenticatiewijziging, downstreamlevering of wijziging aan hkh/hkh-autopilot. Maak de wijziging afzonderlijk terugdraaibaar en toets haar met bestaande synthetische cyclus- en storydata op 320px en breed scherm.

**Waarom:** Er zijn geen open P0- of P1-bugs, waardoor een roadmaprichting gekozen mag worden. De sterkste gevalideerde frictie raakt rechtstreeks de open epic voor het kernoverzicht: op 320px komen vijf metriekkaarten vóór productscope en startactie, is PageDown nodig om te kunnen starten en zijn Productcycli en Stories verborgen achter onuitgelegde horizontale navigatie. Dat ondermijnt de beloofde vindbaarheid van starten, begrijpen en volgen. Een uitsluitend responsieve herordening is klein, geïsoleerd en omkeerbaar; zij verandert geen productdata, beslislogica, authenticatie of Software Factory-koppeling. De richting lost niet tegelijk BUG-6 of ontbrekende bugfixtures op: die verdienen aparte onderhoudseenheden, zodat het resultaat en de terugweg van deze UX-wijziging helder blijven.

### Prioriteiten
- P1 — Toon op 320px actief product en de beschikbare of verklaard niet-beschikbare cyclusstart direct na de compacte omgevingsaanduiding, zonder PageDown als voorwaarde.
- P1 — Plaats recente cyclusbewijzen en gekoppelde stories in dezelfde productscope en vaste taakvolgorde; actieve cycli houden uitsluitend voortgang, terminale cycli hun bestaande bewijsvelden.
- P1 — Maak alle kernsecties expliciet zichtbaar en bereikbaar via toetsenbord en schermlezer; voorkom navigatie die alleen via onzichtbare horizontale scroll ontdekt wordt.
- P2 — Maak globale metriekkaarten op mobiel secundair en standaard ingeklapt, met behoud van toegang via samenvatting of Beheer.
- P2 — Verifieer deterministisch op 320×900 en breed scherm dat de drie kernhandelingen vindbaar zijn, productscope behouden blijft en desktopgedrag niet regressief verandert.

### Besluiten
- **Sluit deze richting aan op open roadmap-epic theme-product-factory-0001, omdat zij de nog ontbrekende consistente mobiele uitvoering van de drie kernacties adresseert.** — Het onderzoek toont dat alle onderdelen bestaan, maar op mobiel niet als één direct scanbare werkruimte worden gepresenteerd. De repository beschrijft juist een productgebonden dashboard voor starten, uitkomsten begrijpen en stories volgen.
- **Gebruik op mobiel een verticale taakhiërarchie: productscope, starten, recente uitkomsten, gekoppelde stories; plaats globale metrics daaronder of ingeklapt.** — Visuele beoordeling op 320×900 liet zien dat acceptatiemelding en vijf metriekkaarten het dagelijkse werk verdringen en dat de startactie pas na PageDown verschijnt. De gekozen volgorde volgt de gevalideerde dagelijkse behoeften en laat bewijs zichtbaar zonder het eerste scherm ermee te overladen.
- **Vervang verborgen horizontale sectie-overflow op mobiel door een expliciete, toegankelijke sectiekeuze.** — Op 320px waren aanvankelijk alleen Overzicht en Roadmap zichtbaar, terwijl Productcycli en Stories onuitgelegde horizontale navigatie vereisten. Een expliciete keuze maakt de informatiearchitectuur begrijpelijk en kan los van datamodel en backend worden beoordeeld en teruggedraaid.
- **Behoud de bestaande toestands- en provenancebetekenis tijdens de herordening; wijzig in deze richting geen bewijslabels of broncategorieën.** — Handmatige annulering is expliciet traceerbaar, terwijl categorie en inferentiestatus bij andere cycli nog vermengd zijn. Een responsieve herordening mag dat bewijs niet verliezen, maar het oplossen van BUG-6 is een afzonderlijke onderhoudswijziging met eigen acceptatiecriteria.
- **Toets deze wijziging zonder productie- of cross-productwrites met de bestaande synthetische Product Factory-cycli en gekoppelde stories.** — De acceptatieomgeving bevat één actieve en drie terminale cycli plus twee gekoppelde stories, voldoende om de gekozen mobiele kernroute read-only te beoordelen. Ontbrekende bugs en testsessies beperken een andere flow, maar blokkeren deze afgebakende UX-toets niet.

## UX-voorstel: Mobiele kernroute: productscope, cyclus en stories

**Gebruikersdoel:** Als producteigenaar wil ik op een scherm van 320 CSS-pixels direct zien in welk product ik werk, of ik een cyclus kan starten, wat recente cycli opleverden en welke stories daaraan gekoppeld zijn, zonder verborgen navigatie of verlies van bewijsinformatie.

### Flow
1. Open het dashboard; na een compacte omgevingsaanduiding staat de actieve productscope bovenaan de hoofdinhoud.
2. Controleer de cyclusstatus. Toon bij beschikbaarheid de knop ‘Cyclus starten’; toon anders op dezelfde plek de uitgeschakelde actie met een programmatisch gekoppelde verklaring.
3. Kies desgewenst een andere kernsectie via de mobiele sectiekeuze met expliciete opties ‘Overzicht’, ‘Productcycli’, ‘Stories’, ‘Roadmap’ en ‘Bugs’.
4. Scan onder de startactie de recente cyclusuitkomsten. Actieve cycli tonen alleen voortgang; terminale cycli tonen hun bestaande status, besluitbron, reden, mechanisme en beslistijd zonder betekeniswijziging.
5. Open een cyclusregel om de bestaande bewijsdetails te bekijken; terugnavigatie herstelt productscope, gekozen sectie en focus.
6. Scan daarna de gekoppelde stories en open desgewenst een storydetail binnen dezelfde productscope.
7. Klap alleen indien nodig ‘Operationele samenvatting’ open voor de vijf globale metriekwaarden of volg de expliciete ingang naar Beheer.

### Wireframe

320px MOBIEL
┌──────────────────────────────────┐
│ Product Factory          [Beheer]│
│ Acceptatie · synthetische data   │
├──────────────────────────────────┤
│ Sectie                           │
│ [Overzicht                  ▾]   │
│ opties: Overzicht, Productcycli, │
│ Stories, Roadmap, Bugs           │
├──────────────────────────────────┤
│ ACTIEF PRODUCT                   │
│ Product Factory                  │
│ Status: gepauzeerd               │
│ [Cyclus starten — niet beschikb.]│
│ Reden: product is gepauzeerd     │
├──────────────────────────────────┤
│ RECENTE PRODUCTCYCLI   [Alles >] │
│ ● Actief · cyclus 9204           │
│   Voortgang: …                   │
│                                  │
│ ✓ Geannuleerd · cyclus 9203 [>]  │
│   Bron: Mens                     │
│   Reden: Handmatig geannuleerd   │
│   Mechanisme: Handmatige annul.  │
│   Beslist: …                     │
├──────────────────────────────────┤
│ GEKOPPELDE STORIES     [Alles >] │
│ Story … · Afgerond           [>] │
│ Story … · Afgerond           [>] │
├──────────────────────────────────┤
│ [› Operationele samenvatting]    │
│ 5 metrics, standaard ingeklapt   │
└──────────────────────────────────┘

BREED SCHERM
Behoud de bestaande desktopnavigatie en metriekpresentatie. De hoofdinhoud gebruikt dezelfde semantische volgorde en bewijsvelden; alleen de responsieve presentatie verandert.

### Interactiehypotheses
- H1 — Bij een geautomatiseerde viewporttest op 320×900 zijn omgevingsaanduiding, actieve productnaam en cyclusstartactie of de verklaring van onbeschikbaarheid zichtbaar zonder scrollen of PageDown.
- H2 — Een agent kan vanaf de paginatop met uitsluitend Tab, Shift+Tab, Enter, Spatie en pijltjestoetsen iedere kernsectie bereiken; geen sectie vereist horizontaal scrollen.
- H3 — Een toegankelijkheidsboomtest vindt één benoemde sectiekeuze met alle vijf opties, een herkenbare hoofdheading en unieke toegankelijke namen voor cyclus- en storylinks.
- H4 — Geautomatiseerde volgordecontrole bevestigt op maximaal 320px: productscope vóór cyclusstart, cyclusstart vóór recente uitkomsten, uitkomsten vóór gekoppelde stories en stories vóór globale metrics.
- H5 — Snapshot- of widgettests met de bestaande synthetische data tonen één actieve cyclus uitsluitend met voortgang en iedere terminale cyclus met alle reeds beschikbare bewijsvelden; herordening verandert geen waarden of labels.
- H6 — Na openen en sluiten van een cyclusdetail herstelt een integratietest de gekozen productscope en sectie en staat toetsenbordfocus op de eerder geactiveerde cyclusregel of terugkeeractie volgens de bestaande navigatiestructuur, zonder focusverlies naar de documentstart tenzij een volledige paginanavigatie dat vereist en dit programmatisch wordt aangekondigd via de paginatitel en hoofdheading zichtbaar is bij aankomst.'

### Toegankelijkheid
- Gebruik native interactieve elementen: een gelabelde select/combobox voor de mobiele sectiekeuze, buttons voor acties en links voor navigatie naar details.
- Maak de visuele leesvolgorde gelijk aan de DOM- en schermlezer-volgorde; gebruik CSS-herordening niet om een afwijkende semantische volgorde te creëren.
- De uitgeschakelde cyclusstart moet waarneembaar blijven. Koppel de reden programmatisch met aria-describedby; voorkom dat alleen kleur of disabled-styling de toestand communiceert.
- Behoud een zichtbare focusindicator met minimaal 3:1 contrast tegen aangrenzende kleuren en toets tekst en essentiële iconen op minimaal WCAG AA-contrast.
- Geef status niet uitsluitend met kleur of pictogram aan; gebruik zichtbare tekst zoals ‘Actief’, ‘Afgerond’ of ‘Geannuleerd’.
- Voorzie inklapbare metrics van een button met programmatisch bepaalde naam en aria-expanded; de ingeklapte inhoud mag niet in de tabvolgorde staan.
- Garandeer touchdoelen van minimaal 24×24 CSS-pixels en bij voorkeur 44×44, zonder overlappende doelen.
- Automatiseer controles met widget/integratietests, toetsenbordscenario’s, semantische-tree-asserties en een axe-achtige WCAG-scan op 320×900 en breed scherm.

### Privacy
- Gebruik uitsluitend operationele metadata van Product Factory: productnaam, cyclusstatus, bewijsvelden, storystatus, metrics en omgevingsidentiteit.
- Neem geen persoonsgegevens, vrije gebruikersprofielen of gegevens uit HKH, HKH Autopilot of andere producten op in fixtures, logging, screenshots of toegankelijkheidslabels.
- Behoud productscope bij iedere query en navigatie; geautomatiseerde tests moeten aantonen dat wisselen of terugnavigeren geen data van een andere productscope toont.
- Laat ingeklapte metrics en schermlezerteksten geen verborgen cross-producttotalen of andere niet-zichtbare gegevens bevatten.
- Gebruik voor snapshots en integratietests alleen de bestaande synthetische Product Factory-cycli en stories; maskeer eventuele tokens, sessiegegevens en authenticatieheaders.
- Voeg voor deze MVP geen analytics, nieuwe tracking, authenticatiewijziging of opslag van interactiegedrag toe.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is afgebakend, autonoom uitvoerbaar en geautomatiseerd toetsbaar. Hij gebruikt alleen operationele Product Factory-metadata, borgt toetsenbord- en schermlezertoegang, verandert geen gegevens of externe koppelingen en overlapt niet exact met geleverd werk. Er zijn geen blokkerende issues.
- **WARNING · CONSISTENCY** — De kandidaat beschrijft duidelijk welk huidig mobiel gedrag wordt gewijzigd, maar verklaart niet expliciet waarom de bestaande volgorde met metrics en horizontale sectienavigatie oorspronkelijk zo is ontstaan. Voeg tijdens uitvoering een korte, op broncode of historie gebaseerde verklaring toe; als de oorzaak niet aantoonbaar is, vermeld dat expliciet. Dit belemmert de veilige kleine MVP niet.
- **INFO · RIGHTS** — Voor de primaire repositorybronnen is geen hergebruiklicentie vastgesteld. De kandidaat neemt echter geen beschermde teksten of vormgeving over en beperkt zich tot een eigen responsieve implementatie, waardoor dit geen leveringsblokkade vormt.
- **INFO · SCOPE** — De kandidaat bouwt functioneel voort op gepubliceerde story:78, maar levert geen exact reeds gerealiseerd resultaat: hij voegt specifiek de mobiele volgorde, expliciete sectiekeuze en ingeklapte operationele samenvatting toe.

## Geaccepteerde storykandidaten

### Maak de drie kernhandelingen direct bereikbaar op 320px

_Sleutel: `mobiele-kernroute-zonder-verborgen-secties`_

Bouw voort op story:78 en wijzig uitsluitend de responsieve presentatie van het productgebonden hoofdscherm. Toon op maximaal 320 CSS-pixels, na een compacte omgevingsaanduiding, in DOM- en leesvolgorde: het actieve product, de bestaande cyclusstartactie met eventuele bestaande verklaring van onbeschikbaarheid, recente toestandsbewuste cyclusregels en gekoppelde stories. Vervang op mobiel de horizontaal overlopende sectienavigatie door één native, gelabelde sectiekeuze met Overzicht, Productcycli, Stories, Roadmap en Bugs. Plaats de vijf bestaande globale metriekwaarden onder een standaard ingeklapte ‘Operationele samenvatting’. Behoud op brede schermen de bestaande navigatie en metriekpresentatie. Wijzig geen gegevens, bewijswaarden, startvoorwaarden, authenticatie, andere productscope of Software Factory-koppeling.

**Acceptatiecriteria**
- Een geautomatiseerde viewporttest op 320×900 toont zonder scrollen de compacte omgevingsaanduiding, actieve productnaam en de bestaande cyclusstartactie; wanneer starten niet beschikbaar is, is de bestaande primaire verklaring programmatisch aan de actie gekoppeld.
- Op maximaal 320 CSS-pixels is de DOM- en zichtbare volgorde exact: productscope, cyclusstart, recente cycli, gekoppelde stories en daarna de operationele samenvatting; CSS-herordening veroorzaakt geen afwijkende semantische leesvolgorde.
- De mobiele sectiekeuze is een native, toegankelijk benoemde bediening met exact de opties Overzicht, Productcycli, Stories, Roadmap en Bugs; een geautomatiseerd toetsenbordscenario bereikt en activeert iedere optie zonder horizontaal scrollen.
- Widget- of snapshottests met de bestaande synthetische Product Factory-data bevestigen dat de herordening bewijswaarden niet verandert: de actieve cyclus toont alleen voortgang en terminale cycli behouden alle reeds beschikbare bewijsvelden en detailacties.
- De operationele samenvatting is op maximaal 320 CSS-pixels standaard ingeklapt, gebruikt een button met correcte aria-expanded-status en houdt ingeklapte inhoud buiten de focusvolgorde; alle vijf bestaande metriekwaarden blijven na uitklappen beschikbaar.
- Geautomatiseerde tests op 320×900 en een brede viewport bevestigen dat productscope en gekozen sectie behouden blijven bij detailnavigatie, dat terugkeer de focus logisch herstelt en dat desktopnavigatie en desktopmetrics niet regressief wijzigen.
- Contract- en integratietests bevestigen dat de wijziging geen nieuwe API, opslag, telemetrie of muterende aanroep introduceert en geen gegevens van een andere productslug in de actieve productscope toont.
- Een geautomatiseerde contrastcontrole op 320×900 en een brede viewport bevestigt WCAG AA-contrast voor tekst en essentiële iconen en minimaal 3:1 contrast voor zichtbare focusindicatoren van ten minste de mobiele sectiekeuze, de cyclusactie, detail- en storylinks en de knop ‘Operationele samenvatting’.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/bugs.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/bugs.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/preview/AcceptanceDataFixtures.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/preview/AcceptanceDataFixtures.kt)

Afhankelijkheden: story:78 (herkend als bestaande stories: 78)

Risico's: De compacte acceptatiemelding of langere vertalingen kunnen de cyclusstart alsnog onder de eerste 900 CSS-pixels duwen; viewporttests moeten daarom met realistische tekst en tekstschaling werken., Een afzonderlijke mobiele sectiekeuze kan status verliezen bij detailnavigatie als zij niet dezelfde bestaande presentatiestatus gebruikt., Het verplaatsen van metrics kan hun zichtbaarheid verminderen; ze blijven daarom geautomatiseerd aantoonbaar bereikbaar via de ingeklapte samenvatting en Beheer., Deze kandidaat verandert bewust geen beslisbronlabels en lost BUG-6 niet op.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
