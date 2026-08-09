---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0014
date: 2026-08-09
status: approved
sources:
  - https://product-factory-acceptance.vdzonsoftware.nl
  - https://product-factory-api-acceptance.vdzonsoftware.nl/api/shadow-iterations
  - https://product-factory-api-acceptance.vdzonsoftware.nl/api/products
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-11-Toon-blokkeerreden-van-dependsOn-resolutie-op-storykandidaat-kaart.md
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-10-Voeg-read-only-blokkeerreden-veld-toe-aan-storykandidaat.md
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-4-Voeg-toegankelijk-inline-uitklappaneel-met-scope-disclaimer-toe.md
  - https://api.github.com/repos/robbertvdzon/product-factory/commits?per_page=20
---
# Productcyclus 14

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Onderzoek op 2026-08-09 combineerde de acceptatieomgeving (nu wél bereikbaar via een echte Playwright-browser, in tegenstelling tot eerdere 403-meldingen) met de broncode/documentatie op GitHub. De vorige onderzoeksrichting — de blokkeerreden van dependsOn-resolutie zichtbaar maken op storykandidaat-kaarten — is inmiddels volledig opgeleverd en getest (product-factory-10 en -11, beide gemerged op 2026-08-09) en hoeft niet opnieuw onderzocht te worden. Bij het doorlopen van de live iteratiedetails is een nieuw, concreet en broncode-bevestigd gebruiksprobleem gevonden: wanneer een productcyclus FAILED gaat (bijv. "guardrail-conflict"), toont het detaildialoog géén enkele reden — het veld `iteration['errorMessage']`, dat de backend altijd consistent met de status meelevert en dat de classificatiebadge (bijv. "guardrail-conflict") mede bepaalt, wordt in main.dart nergens als tekst gerenderd voor de eigenaar. Daarnaast verdwijnt de betekenisvolle classificatiebadge (met zijn WCAG-toegankelijke uitklap-disclaimer uit product-factory-4) zodra je vanuit de lijst doorklikt naar het detaildialoog: daar is alleen de rauwe backend-statusenum (bijv. "NEEDS_REVISION") te zien, geen classificatie of uitleg. Beide zijn expliciet in de broncode geverifieerd (main.dart en classification.dart) en in de live acceptatieomgeving met screenshots bevestigd (iteraties shadow-hkh-autopilot-0002 en -0003).","

### dependsOn-blokkeerreden op storykandidaat-kaart is volledig opgeleverd (stories 10 en 11)

De in iteratie 9 gekozen richting is afgerond: product-factory-10 voegde een read-only blokkeerreden-veld toe aan de storykandidaat-API/-model, en product-factory-11 rendert dit als een toegankelijk, WCAG AA-conform label ('Geblokkeerd: <reden>') direct op de kaart in de dashboard-wachtrij, met Semantics-ondersteuning voor schermlezers. Beide zijn gemerged op 2026-08-09 (commits/PR's #44 en #45) en de broncode (main.dart regel 1113-1151) bevestigt de implementatie. Dit onderwerp is gesloten.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-11-Toon-blokkeerreden-van-dependsOn-resolutie-op-storykandidaat-kaart.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-11-Toon-blokkeerreden-van-dependsOn-resolutie-op-storykandidaat-kaart.md), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-10-Voeg-read-only-blokkeerreden-veld-toe-aan-storykandidaat.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-10-Voeg-read-only-blokkeerreden-veld-toe-aan-storykandidaat.md), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart)

### errorMessage van een FAILED cyclus wordt nergens aan de eigenaar getoond

In de live acceptatieomgeving toont het detaildialoog van iteratie shadow-hkh-autopilot-0002 (status FAILED, classificatie 'guardrail-conflict') alleen 'Nog geen agentstappen gestart' en 'Nog geen agentresultaten beschikbaar' — geen enkele reden voor de mislukking. Het onderliggende API-veld `errorMessage` bevat wel degelijk een concrete, leesbare reden ('Workspace-publicatie tijdelijk niet beschikbaar (previewdata, gesimuleerd).', bevestigd via /api/shadow-iterations). In de broncode (main.dart) wordt `iteration['errorMessage']` alleen doorgegeven aan `classifyIterationOutcome()` (regel 573) om de badge te bepalen; het wordt nergens als tekst in `IterationSessionDialog` gerenderd. Wel worden `step['errorMessage']` (agentstap-niveau) en `delivery['errorMessage']` (Software Factory-levering) elders wél getoond, wat aantoont dat dit patroon bestaat maar hier ontbreekt.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://product-factory-api-acceptance.vdzonsoftware.nl/api/shadow-iterations](https://product-factory-api-acceptance.vdzonsoftware.nl/api/shadow-iterations), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart)

### Classificatiebadge en toelichting verdwijnen zodra je doorklikt naar het detaildialoog

Op de lijstkaart toont elke iteratie een klikbare `ClassificationBadge` (bijv. 'onderzoek-onvoldoende', 'guardrail-conflict', 'richting-gekozen') die bij activeren een toegankelijk uitklappaneel toont met uitleg dat de badge 'wat' laat zien, niet 'waarom' (product-factory-4). Zodra je op de rij zelf klikt (niet de badge) om het volledige detaildialoog te openen, toont dat dialoog alleen een kale `Chip` met de rauwe backend-status ('NEEDS_REVISION', 'FAILED') — de classificatie, kleurcodering en uitleg zijn volledig afwezig. Dit is een bewuste, gedocumenteerde scope-keuze in product-factory-4 ('geen wijziging aan de bestaande detaildialoog'), maar het resultaat is een inconsistente ervaring: precies op het moment dat de eigenaar dieper wil kijken (waarom deze uitkomst?), valt de enige uitleg weg.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-4-Voeg-toegankelijk-inline-uitklappaneel-met-scope-disclaimer-toe.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-4-Voeg-toegankelijk-inline-uitklappaneel-met-scope-disclaimer-toe.md), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart)

### Acceptatieomgeving is nu bereikbaar via een echte browser (403 uit eerdere iteraties opgelost)

In tegenstelling tot iteratie 9, waarin WebFetch/WebSearch consequent 403 kregen, is de omgeving deze sessie volledig doorlopen met een headless Chromium-browser (Playwright) die synthetische pointer-events op `flt-semantics-placeholder` afvuurt om Flutters semantics-tree te activeren, gevolgd door `ariaSnapshot()` en netwerkresponse-monitoring. Dit bevestigde dat het backend-API-domein (`product-factory-api-acceptance.vdzonsoftware.nl`) losstaat van het frontend-domein en met dummy-/mockdata voor het enige geregistreerde product 'HKH Autopilot' draait; Product Factory heeft zelf geen zelfreferentiële productregistratie in deze omgeving, wat verwacht gedrag is (het is het orkestratiesysteem, niet een beheerd product).

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://product-factory-api-acceptance.vdzonsoftware.nl/api/products](https://product-factory-api-acceptance.vdzonsoftware.nl/api/products), [https://product-factory-api-acceptance.vdzonsoftware.nl/api/shadow-iterations](https://product-factory-api-acceptance.vdzonsoftware.nl/api/shadow-iterations)

### Huidige applicatie

**Doel:** Product Factory is het orkestratiesysteem dat autonome productontwikkeling (onderzoek, keuze, ontwerp, storylevering aan de Software Factory) mogelijk maakt voor producten zoals HKH Autopilot, en dat via dit dashboard voor de menselijke eigenaar zichtbaar en bedienbaar maakt. Doelgroep is de productiegenaar die per product de autonomie-instellingen beheert en de uitkomsten van elke onderzoeks-/productcyclus wil kunnen begrijpen en beoordelen.

**Wat ontbreekt:**
- Wanneer een productcyclus FAILED gaat, toont het detaildialoog geen enkele reden: het API-veld `errorMessage` wordt alleen gebruikt om de classificatiebadge te bepalen, maar nooit als leesbare tekst aan de eigenaar getoond (bevestigd in main.dart en live in de acceptatieomgeving bij shadow-hkh-autopilot-0002).
- De betekenisvolle classificatiebadge met zijn toegankelijke 'wat vs. waarom'-toelichting (product-factory-1 t/m -4) is alleen zichtbaar op de lijstkaart; zodra je doorklikt naar het volledige detaildialoog, blijft alleen de rauwe backend-statusenum (bv. 'NEEDS_REVISION') over, zonder classificatie of uitleg.
- Workspace-publicaties hebben nog steeds geen tijdstempel en volgen alleen de backend-volgorde in plaats van gesorteerd te zijn op recentie (al eerder gedocumenteerd als bekende beperking, nu bevestigd: 0 publicaties in de huidige acceptatieomgeving maakt dit niet visueel te verifiëren, maar de broncode-beperking bestaat nog).

### Verbetermogelijkheden

- Toon `iteration['errorMessage']` als leesbare tekst in `IterationSessionDialog` wanneer een cyclus FAILED is (analoog aan hoe `step['errorMessage']` en `delivery['errorMessage']` al wél getoond worden), zodat de eigenaar zonder ruwe API-calls kan begrijpen waarom een cyclus mislukte — dit is een kleine, geïsoleerde, alleen-lezen presentatiewijziging op al bestaande data.
- Hergebruik de bestaande `ClassificationBadge` (met zijn WCAG-conforme kleuren en uitklap-disclaimer) ook in `IterationSessionDialog`, naast of in plaats van de kale status-`Chip`, zodat de classificatie en de 'wat vs. waarom'-uitleg niet verloren gaan zodra de eigenaar doorklikt naar het detail — dit sluit de inconsistentie die product-factory-4 bewust openliet.

### Inspiratiebronnen

- [GitHub Actions workflow run summary (failure reason panel)](https://docs.github.com/actions/managing-workflow-runs/using-the-visualization-graph) — GitHub Actions toont bij een mislukte workflow-run altijd een duidelijk zichtbare foutmelding/reden direct in de rundetailweergave, niet alleen als statuslabel in de lijst — een direct precedent voor het alsnog tonen van iteration.errorMessage in het Product Factory-detaildialoog.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://product-factory-acceptance.vdzonsoftware.nl) | 2026-08-09 | Eigen, door de gebruiker beheerde acceptatieomgeving met representatieve nepdata; geen externe rechten van toepassing. | Levende weergave van hoe de eigenaar het dashboard daadwerkelijk gebruikt, inclusief detaildialogen die niet uit statische broncode alleen af te leiden zijn. |
| [bron](https://product-factory-api-acceptance.vdzonsoftware.nl/api/shadow-iterations) | 2026-08-09 | Eigen backend-API van dezelfde acceptatieomgeving; geen externe rechten van toepassing. | Bevestigt dat het API-veld errorMessage daadwerkelijk een leesbare foutreden bevat die niet in de UI wordt getoond, direct onderbouwend voor de belangrijkste bevinding. |
| [bron](https://product-factory-api-acceptance.vdzonsoftware.nl/api/products) | 2026-08-09 | Eigen backend-API; geen externe rechten van toepassing. | Bevestigt de huidige productconfiguratie (HKH Autopilot) en dat Product Factory zelf geen zelfreferentiële productregistratie heeft in deze omgeving. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart) | 2026-08-09 | Publieke, door de gebruiker beheerde broncoderepository (robbertvdzon/product-factory); eigen code, geen externe licentiebeperking van toepassing. | Primaire bron om te verifiëren waar classificatiebadges, blokkeerredenen en errorMessage-velden wel/niet gerenderd worden — noodzakelijk om UI-bevindingen te onderbouwen buiten wat zichtbaar is in de mockdata. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart) | 2026-08-09 | Publieke, door de gebruiker beheerde broncoderepository; eigen code. | Bevestigt hoe classifyIterationOutcome de badge (bv. guardrail-conflict) afleidt uit status/criticVerdict/errorMessage. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-11-Toon-blokkeerreden-van-dependsOn-resolutie-op-storykandidaat-kaart.md) | 2026-08-09 | Publieke, door de gebruiker beheerde storydocumentatie; eigen content. | Bevestigt dat de vorige onderzoeksrichting (blokkeerreden zichtbaar maken) volledig en getest is opgeleverd, inclusief acceptatiecriteria en toegankelijkheidswerk. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-10-Voeg-read-only-blokkeerreden-veld-toe-aan-storykandidaat.md) | 2026-08-09 | Publieke, door de gebruiker beheerde storydocumentatie; eigen content. | Bevestigt de backend-kant van de dependsOn-blokkeerreden-functionaliteit. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-4-Voeg-toegankelijk-inline-uitklappaneel-met-scope-disclaimer-toe.md) | 2026-08-09 | Publieke, door de gebruiker beheerde storydocumentatie; eigen content. | Bevestigt de bewuste scope-keuze om het detaildialoog niet aan te passen bij het toevoegen van de classificatiebadge-toelichting, wat de nu gevonden inconsistentie verklaart. |
| [bron](https://api.github.com/repos/robbertvdzon/product-factory/commits?per_page=20) | 2026-08-09 | Publieke GitHub API voor een door de gebruiker beheerde repository; eigen content. | Vaststellen van de meest recente commit-/opleveractiviteit sinds iteratie 9, om te bepalen welke onderwerpen al gesloten zijn. |

## Productbeslissing

Sluit de inconsistentie die product-factory-4 bewust openliet: op de lijstkaart krijgt de eigenaar een toegankelijke classificatiebadge mét 'wat vs. waarom'-uitleg, maar zodra hij doorklikt naar het volledige detaildialoog (`IterationSessionDialog`) valt die uitleg volledig weg — alleen de rauwe backend-statusenum (bv. 'NEEDS_REVISION', 'FAILED') blijft over, en bij een FAILED cyclus wordt de daadwerkelijke foutreden (`iteration['errorMessage']`) nergens getoond, terwijl dat veld al consistent door de backend wordt meegeleverd en al wordt gebruikt om de badge te bepalen. De richting is: (1) render `iteration['errorMessage']` als leesbare tekst in het detaildialoog wanneer de status FAILED is, op dezelfde manier als `step['errorMessage']` en `delivery['errorMessage']` daar al getoond worden; en (2) hergebruik de bestaande `ClassificationBadge`-component (met kleurcodering en uitklap-disclaimer) in het detaildialoog in plaats van, of naast, de kale status-Chip. Beide zijn zuivere presentatiewijzigingen op data die al bestaat en al elders in de codebase gerenderd wordt, dus laag risico, geïsoleerd en eenvoudig terug te draaien.

**Waarom:** Het onderzoek toont met broncode (main.dart, classification.dart) en live gedrag in de acceptatieomgeving (shadow-hkh-autopilot-0002/-0003) aan dat de eigenaar precies op het moment dat hij dieper wil kijken naar een uitkomst — het detaildialoog — de minste uitleg krijgt: geen foutreden bij FAILED, geen classificatie-toelichting. Dit raakt direct de missie (blijft het dashboard begrijpelijk en prettig bedienbaar?) en het productprincipe 'eerst begrijpen, dan wijzigen': product-factory-4 sloot het detaildialoog bewust uit van scope, wat nu een concreet, verifieerbaar gebruiksprobleem oplevert. Omdat beide onderdelen dezelfde onderliggende oorzaak delen (badge/foutreden bestaan al, maar worden niet in het detaildialoog gerenderd) en beide klein, geïsoleerd en zonder databewerkingen, authenticatie- of Software Factory-impact zijn, passen ze bij 'klein en toetsbaar' en de guardrail om terughoudend te zijn bij onomkeerbare wijzigingen. De workspace-publicatiesortering is een apart, niet-gerelateerd en momenteel niet-verifieerbaar probleem en is bewust niet meegenomen om de stap samenhangend en klein te houden.

### Prioriteiten
- Toon iteration.errorMessage als leesbare tekst in het detaildialoog bij FAILED-cycli, zodat de eigenaar zonder ruwe API-calls begrijpt waarom een cyclus mislukte.
- Hergebruik de bestaande, toegankelijke ClassificationBadge (incl. 'wat vs. waarom'-uitklap) in het detaildialoog in plaats van de kale rauwe-status-Chip.
- Blijf strikt binnen presentatie van reeds bestaande backend-velden; geen wijziging aan API's, datamodellen of de Software Factory-koppeling.
- Lever de wijziging als kleine, in isolatie beoordeelbare en terug te draaien stap, consistent met hoe step- en delivery-errorMessages al elders in hetzelfde dialoog worden getoond.

### Besluiten
- **Toon `iteration['errorMessage']` als leesbare tekst in `IterationSessionDialog` wanneer een cyclus de status FAILED heeft, analoog aan hoe `step['errorMessage']` en `delivery['errorMessage']` elders al wél getoond worden.** — De backend levert dit veld al consistent mee en gebruikt het intern om de classificatiebadge te bepalen (main.dart regel 573), maar rendert het nergens als tekst voor de eigenaar. Live bevestigd op shadow-hkh-autopilot-0002: het dialoog toont alleen 'Nog geen agentstappen gestart', terwijl de API een concrete reden bevat.
- **Hergebruik de bestaande `ClassificationBadge` (met kleurcodering en de toegankelijke 'wat vs. waarom'-uitklap uit product-factory-4) in `IterationSessionDialog`, naast of in plaats van de kale rauwe-status-`Chip` ('NEEDS_REVISION', 'FAILED').** — De classificatie en haar uitleg zijn al gebouwd en getest op de lijstkaart, maar product-factory-4 sloot het detaildialoog expliciet uit van scope. Het gevolg is dat precies op het moment dat de eigenaar dieper wil kijken, de enige uitleg wegvalt — een inconsistentie die met bestaande componenten op te lossen is.
- **Beperk deze richting nadrukkelijk tot een presentatiewijziging op reeds bestaande, reeds door de backend geleverde data (errorMessage, classificatie-afleiding); geen wijziging aan API-contracten, data-modellen of de koppeling met de Software Factory.** — Sluit aan bij de productprincipes 'klein en toetsbaar' en 'onomkeerbaarheid weegt zwaarder dan gemak': de velden bestaan al en worden elders in dezelfde dialoog al gerenderd (step/delivery errorMessage), dus dit is laag-risico, geïsoleerd en makkelijk terug te draaien.
- **Behandel de ontbrekende tijdstempel/sortering van workspace-publicaties dit cyclus niet als richting; dit blijft een bekende, niet-blokkerende beperking voor een volgende cyclus.** — Deze cyclus focust op één samenhangend, in de acceptatieomgeving zichtbaar en broncode-bevestigd probleem (verlies van uitleg bij FAILED/detail). De publicatie-sortering is nu (0 publicaties in de acceptatieomgeving) niet visueel te verifiëren en vermengt twee aparte verbeteringen in één stap.

## UX-voorstel: Detaildialoog: foutreden en classificatie tonen bij een mislukte productcyclus

**Gebruikersdoel:** Als producteigenaar wil ik, wanneer ik vanuit de iteratielijst doorklik naar het detaildialoog van een cyclus, direct zien wélke classificatie de uitkomst heeft (met de bestaande 'wat vs. waarom'-toelichting) én, als de cyclus FAILED is, een leesbare reden waarom — zonder ruwe API-calls te hoeven doen.

### Flow
1. Eigenaar opent het dashboard en ziet de iteratielijst met per rij een klikbare ClassificationBadge (bv. 'guardrail-conflict') die al een toegankelijke uitklaptoelichting biedt.
2. Eigenaar klikt op een rij (niet op de badge) om het volledige IterationSessionDialog te openen.
3. Dialoog opent en toont bovenaan, op de plek van de huidige kale status-Chip, dezelfde ClassificationBadge-component inclusief kleurcodering en uitklapbare 'wat vs. waarom'-toelichting, gebaseerd op reeds beschikbare velden (status, criticVerdict, errorMessage).
4. Als de onderliggende status FAILED is en iteration.errorMessage niet leeg is, toont het dialoog direct onder de badge een leesbaar tekstblok met het label 'Foutreden' en de inhoud van iteration.errorMessage, in dezelfde stijl als de bestaande step.errorMessage- en delivery.errorMessage-blokken.
5. Als iteration.errorMessage leeg of afwezig is bij een FAILED cyclus, toont het dialoog een neutrale placeholdertekst ('Geen foutreden beschikbaar') in plaats van niets te tonen, zodat het ontbreken van data niet met een niet-geladen scherm wordt verward.
6. Eigenaar kan de uitklaptoelichting van de badge openen/sluiten met muis, toetsenbord (Enter/Spatie) of schermlezer, net als op de lijstkaart.
7. Eigenaar sluit het dialoog; de lijstweergave en de kaart-badge blijven ongewijzigd zichtbaar en consistent met wat in het dialoog stond.

### Wireframe

[IterationSessionDialog — herziene kop]
┌───────────────────────────────────────────────────────────┐
│ Iteratie shadow-hkh-autopilot-0002                    [x] │
├───────────────────────────────────────────────────────────┤
│ [Badge: "guardrail-conflict" ▾]  (herbruikte Classification│
│  Badge-component; kleurcodering + focusring; klikbaar/     │
│  toetsenbord-uitklapbaar)                                  │
│  ⌄ Uitleg (uitgeklapt indien geactiveerd):                 │
│    "Deze badge toont de classificatie van de uitkomst      │
│     (wat), niet de onderliggende reden (waarom)."          │
│                                                             │
│  ── Foutreden ──────────────────────────────────────────   │
│  ⚠ Workspace-publicatie tijdelijk niet beschikbaar          │
│    (previewdata, gesimuleerd).                              │
│  (alleen zichtbaar wanneer status = FAILED; anders          │
│   verborgen, geen leeg blok)                                │
├───────────────────────────────────────────────────────────┤
│ Agentstappen                                               │
│  • Stap 1 ...  [errorMessage indien aanwezig, bestaand]     │
│ Agentresultaten                                             │
│  • ... (bestaand, ongewijzigd)                              │
│ Workspace-publicaties (Software Factory levering)            │
│  • [delivery.errorMessage indien aanwezig, bestaand]         │
└───────────────────────────────────────────────────────────┘

Verschil t.o.v. huidige staat:
- Kale Chip("NEEDS_REVISION"/"FAILED") vervangen door ClassificationBadge
  (zelfde component/props als op de lijstkaart, alleen-lezen hergebruik).
- Nieuw, voorwaardelijk tekstblok "Foutreden" direct onder de badge,
  gevuld met iteration.errorMessage, in dezelfde visuele stijl als de
  bestaande step- en delivery-errorMessage-blokken (label + waarschuwings-
  icoon + tekst, geen actieknoppen).
- Geen wijziging aan lijstweergave, geen nieuwe velden, geen nieuwe
  API-calls: alle getoonde data komt al mee in de bestaande
  /api/shadow-iterations respons.

### Interactiehypotheses
- Als de ClassificationBadge met uitklaptoelichting ook in het detaildialoog verschijnt, kan een geautomatiseerde UI-test (Flutter widget/integration test) aantonen dat voor elke iteratie met status FAILED of NEEDS_REVISION de badge in het dialoog dezelfde tekst en kleur toont als op de bijbehorende lijstkaart.
- Als iteration.errorMessage bij FAILED-cycli als leesbare tekst in het dialoog wordt gerenderd, kan een geautomatiseerde test met gemockte /api/shadow-iterations-responses aantonen dat voor elke FAILED-iteratie met een niet-lege errorMessage die exacte tekst als widget/tekstnode in het dialoog aanwezig is.
- Als errorMessage ontbreekt bij een FAILED-iteratie, kan een geautomatiseerde test aantonen dat de placeholdertekst 'Geen foutreden beschikbaar' verschijnt in plaats van een leeg of afwezig blok, zodat 'geen data' nooit visueel identiek is aan 'nog niet geladen'.
- Als de badge en het foutredenblok toetsenbordbedienbaar zijn, kan een geautomatiseerde toetsenbordnavigatietest (bv. via Flutter's FocusTraversal-simulatie of Playwright keyboard-tab-simulatie op de web-build) aantonen dat de badge met Tab bereikbaar is en met Enter/Spatie de uitklaptoelichting toggelt, zonder muisinteractie.
- Als de wijziging strikt presentatie is op bestaande velden, kan een geautomatiseerde contracttest aantonen dat de API-respons van /api/shadow-iterations ongewijzigd blijft (zelfde velden, zelfde types) vóór en na deze wijziging.

### Toegankelijkheid
- Hergebruik de bestaande Semantics-labels van ClassificationBadge (uit product-factory-4) ongewijzigd in het detaildialoog, zodat schermlezers dezelfde aankondiging ('classificatie: guardrail-conflict, geactiveer om uitleg te tonen') geven als op de lijstkaart.
- Het nieuwe foutredenblok krijgt een expliciet Semantics-label ('Foutreden: <tekst>') zodat een schermlezer het als afzonderlijk, betekenisvol tekstblok aankondigt en niet als onderdeel van de badge.
- Badge en uitklaptoelichting blijven volledig bedienbaar met toetsenbord (Tab om te focussen, Enter/Spatie om te activeren), consistent met de bestaande implementatie op de lijstkaart; geen nieuwe muis-only interacties.
- Kleurcodering van de badge voldoet aan minimaal WCAG AA-contrast (bestaande eis uit product-factory-4); het foutredenblok gebruikt tekst plus een waarschuwingsicoon (geen kleur-alleen-signalering) zodat het ook zonder kleurperceptie duidelijk is.
- Focusvolgorde in het dialoog is logisch: badge eerst, dan foutredenblok (indien aanwezig), dan bestaande secties (agentstappen, resultaten, publicaties), zodat schermlezergebruikers de belangrijkste uitleg als eerste tegenkomen.
- Placeholdertekst 'Geen foutreden beschikbaar' wordt ook door schermlezers voorgelezen (geen aria-hidden/verborgen leeg element), zodat gebruikers niet in onzekerheid blijven of de inhoud nog laadt.

### Privacy
- Alle getoonde velden (iteration.status, classificatie, errorMessage) zijn al onderdeel van de bestaande, door Product Factory zelf beheerde operationele metadata over productcycli; er wordt geen nieuwe data verzameld of van een ander systeem opgehaald.
- errorMessage-teksten worden ongefilterd hergebruikt zoals ze al elders in hetzelfde dialoog (step/delivery) worden getoond; er wordt geen aanvullende validatie of maskering toegevoegd, en er is geen aanwijzing dat dit veld persoonsgegevens van eindgebruikers van andere producten bevat — het betreft systeem-/procesfouten (bv. 'workspace-publicatie tijdelijk niet beschikbaar').
- Er worden geen nieuwe API-calls, endpoints of dataopslag geïntroduceerd; de wijziging is zuiver presentatie op reeds opgehaalde responsdata binnen de sessie van de ingelogde producteigenaar.
- De uitklaptoelichting en foutredentekst blijven alleen zichtbaar binnen het reeds geauthenticeerde dashboard van de producteigenaar; er is geen nieuwe blootstelling naar publieke of gedeelde schermen voorzien in deze stap.
- Toekomstige errorMessage-teksten uit de backend moeten door de eigenaar van dat veld (backend/agentproces) vrij blijven van persoonsgegevens; deze UX-wijziging voegt geen filtering toe en veronderstelt dat de bestaande operationele-metadata-afspraak (geen persoonsgegevens) al gehandhaafd wordt bij het vullen van dit veld.

## Kritische beoordeling

**Oordeel:** ACCEPT

Beide kandidaten zijn goed onderbouwd met concrete broncoderegels (main.dart, classification.dart), live-verificatie in de acceptatieomgeving (Playwright/ariaSnapshot, /api/shadow-iterations) en expliciete verwijzing naar de eerdere bewuste scope-keuze in product-factory-4 die het gat verklaart — dit voldoet aan de kwaliteitseis om uit te leggen waarom het huidige gedrag zo is. Privacy en toegankelijkheid zijn expliciet en concreet behandeld (Semantics-labels, toetsenbordbediening, WCAG AA-contrast, geen nieuwe persoonsgegevens). Alle acceptatiecriteria zijn geautomatiseerd toetsbaar (widget-/integratietests, contracttest, ariaSnapshot, automatische contrastberekening) zonder handmatige testen, menselijke besluiten, accountaanmaak of andere niet-agentische stappen — dit voldoet aan de autonomiegate. Geen overlap met de 32 bestaande, reeds gepubliceerde kandidaten (het afgeronde dependsOn-onderwerp wordt terecht niet herhaald). Twee niet-blokkerende aandachtspunten: beide kandidaten wijzigen dezelfde kop-sectie van IterationSessionDialog zonder expliciete dependsOn-relatie, en er is een lichte terminologische inconsistentie ("naast of in plaats van" in de onderzoeksnarratief vs. een harde vervanging in kandidaat 2's acceptatiecriteria).
- **WARNING · CONSISTENCY** — Beide kandidaten wijzigen dezelfde kopsectie van IterationSessionDialog (badge/Chip-gebied) zonder expliciete dependsOn-relatie tussen hen. Los, in willekeurige volgorde geïmplementeerd is waarschijnlijk conflictvrij (verschillende sub-elementen: badge vs. foutredenblok), maar dit is niet expliciet geborgd in de kandidaten zelf.
- **INFO · CONSISTENCY** — De onderzoeksnarratief (productDirection/wireframe) gebruikt 'naast of in plaats van' voor de badge-vervanging, terwijl kandidaat 2's eigen acceptatiecriteria een harde vervanging voorschrijven (rauwe Chip mag niet meer aanwezig zijn). De kandidaat zelf is intern consistent; alleen de bredere onderzoekstekst is losser geformuleerd.

## Geaccepteerde storykandidaten

### Toon iteration.errorMessage als leesbare foutreden in het detaildialoog bij een FAILED-iteratie

_Sleutel: `show-iteration-errormessage-in-detail-dialog`_

In dashboard-frontend/lib/main.dart wordt `iteration['errorMessage']` momenteel uitsluitend doorgegeven aan `classifyIterationOutcome()` (regel ~573) om de classificatiebadge te bepalen; de tekst zelf wordt nergens in `IterationSessionDialog` gerenderd. Dit is live bevestigd in de acceptatieomgeving (shadow-hkh-autopilot-0002, status FAILED): het dialoog toont alleen 'Nog geen agentstappen gestart' en 'Nog geen agentresultaten beschikbaar', terwijl de API (/api/shadow-iterations) wél een concrete reden meelevert ('Workspace-publicatie tijdelijk niet beschikbaar (previewdata, gesimuleerd).'). Elders in hetzelfde dialoog worden `step['errorMessage']` en `delivery['errorMessage']` al wél als tekst getoond, dus dit patroon bestaat al in de codebase en wordt hier eenvoudig hergebruikt. Voeg in `IterationSessionDialog` een voorwaardelijk tekstblok toe met het label 'Foutreden' dat `iteration['errorMessage']` toont wanneer de iteratiestatus FAILED is en het veld niet leeg is; toon bij FAILED met een leeg/ontbrekend veld de neutrale placeholdertekst 'Geen foutreden beschikbaar' (nooit een leeg of ontbrekend blok, om 'geen data' niet te verwarren met 'nog niet geladen'). Bij elke andere status blijft het blok volledig verborgen (geen wijziging aan bestaand gedrag). Dit is een zuivere, alleen-lezen presentatiewijziging: geen nieuw API-veld, geen wijziging aan `/api/shadow-iterations`, geen wijziging aan de classificatielogica in classification.dart.

**Acceptatiecriteria**
- Een geautomatiseerde Flutter widget-/integratietest mockt een /api/shadow-iterations-respons met een iteratie met status FAILED en een niet-lege errorMessage, opent het detaildialoog voor die iteratie, en verifieert dat een tekstnode met het label 'Foutreden' en de exacte inhoud van errorMessage aanwezig is in de widget-tree.
- Een geautomatiseerde test mockt een iteratie met status FAILED en errorMessage leeg of null, opent het detaildialoog, en verifieert dat in plaats daarvan exact de tekst 'Geen foutreden beschikbaar' zichtbaar is (geen leeg of ontbrekend blok).
- Een geautomatiseerde test mockt een iteratie met een status ongelijk aan FAILED (bv. COMPLETED of NEEDS_REVISION) met een gevulde errorMessage, opent het detaildialoog, en verifieert dat het 'Foutreden'-blok afwezig is in de widget-tree (geen regressie op het bestaande gedrag voor niet-FAILED statussen).
- Het nieuwe foutredenblok heeft een expliciet Semantics-label 'Foutreden: <tekst>', geverifieerd via een geautomatiseerde ariaSnapshot/semantics-tree-inspectie op de web-build, zodat het als afzonderlijk betekenisvol blok wordt aangekondigd.
- Een geautomatiseerde contracttest bevestigt dat de velden en types van de /api/shadow-iterations-respons vóór en na deze wijziging ongewijzigd zijn (geen backend-aanpassing in deze story).
- De bestaande, elders in hetzelfde dialoog al gerenderde step['errorMessage']- en delivery['errorMessage']-blokken blijven functioneel ongewijzigd, geverifieerd door de bestaande of een equivalente geautomatiseerde test die deze blokken al dekt.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://product-factory-api-acceptance.vdzonsoftware.nl/api/shadow-iterations](https://product-factory-api-acceptance.vdzonsoftware.nl/api/shadow-iterations), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

Risico's: Als errorMessage-teksten in de toekomst rijke opmaak of zeer lange technische stacktraces bevatten, kan het tekstblok visueel overweldigend worden; dit wordt in deze story niet opgelost en is een bekende beperking voor een latere iteratie., Het correct onderscheiden van 'leeg/null' errorMessage vereist consistente behandeling van beide gevallen in de mock-/testdata; als de backend soms een lege string en soms null teruggeeft, moet de implementatie beide dekken om de placeholder betrouwbaar te tonen.

### Hergebruik de bestaande ClassificationBadge (met 'wat vs. waarom'-uitklap) in het detaildialoog in plaats van de kale rauwe-status-Chip

_Sleutel: `reuse-classification-badge-in-detail-dialog`_

Op de lijstkaart toont elke iteratie een toegankelijke `ClassificationBadge` (kleurcodering + toetsenbord-/schermlezerbedienbare uitklaptoelichting, opgeleverd in product-factory-22/25) die met `classifyIterationOutcome()` uit status/criticVerdict/errorMessage een van de vaste classificaties afleidt (bv. 'guardrail-conflict', 'onderzoek-onvoldoende'). Zodra de eigenaar vanuit de lijst doorklikt naar het volledige `IterationSessionDialog`, toont dat dialoog in plaats daarvan alleen een kale `Chip` met de rauwe backend-statusenum (bv. 'NEEDS_REVISION', 'FAILED') — een bewuste scope-keuze uit product-factory-4 die nu een bevestigde inconsistentie oplevert (live geverifieerd in de acceptatieomgeving op shadow-hkh-autopilot-0002/-0003 en in main.dart). Vervang in `IterationSessionDialog` de bestaande rauwe-status-`Chip` door de reeds bestaande `ClassificationBadge`-component (dezelfde widget/props als op de lijstkaart, inclusief de uitklapbare 'wat vs. waarom'-disclaimer uit product-factory-4), gevoed met exact dezelfde iteratiedata die al in het dialoog beschikbaar is. Dit is een puur presentationele hergebruik-wijziging: geen nieuwe classificatielogica, geen nieuw API-veld, geen wijziging aan classification.dart zelf.

**Acceptatiecriteria**
- Een geautomatiseerde Flutter widget-/integratietest mockt voor elke van de vijf bestaande classificatiewaarden (onderzoek-onvoldoende, guardrail-conflict, richting-gekozen, richting-verworpen, niet-classificeerbaar) een iteratie, opent zowel de lijstkaart-badge als het detaildialoog voor dezelfde iteratie, en verifieert dat badge-tekst en -kleur in beide plekken identiek zijn.
- Een geautomatiseerde test verifieert dat de kale rauwe-status-Chip (die de rauwe backend-enum zoals 'NEEDS_REVISION' toont) niet langer aanwezig is in de widget-tree van IterationSessionDialog na deze wijziging.
- Een geautomatiseerde toetsenbordnavigatietest (bv. FocusTraversal-simulatie of Playwright keyboard-tab-simulatie op de web-build) toont aan dat de badge in het detaildialoog met Tab bereikbaar is en met Enter of Spatie de 'wat vs. waarom'-uitklaptoelichting toggelt, net als op de lijstkaart.
- Een geautomatiseerde ariaSnapshot/semantics-tree-inspectie op de web-build bevestigt dat de badge in het detaildialoog dezelfde Semantics-aankondigingstekst geeft als de badge op de lijstkaart (zelfde classificatienaam + hint dat activeren de uitleg toont).
- Een geautomatiseerde contrastcontrole (geautomatiseerde WCAG AA-contrastberekening op de gebruikte kleurwaarden) bevestigt dat de badge in het detaildialoog dezelfde, al goedgekeurde kleurcodering uit product-factory-22/25 hergebruikt zonder contrastregressie.
- Focusvolgorde in het dialoog is geautomatiseerd geverifieerd: de badge is het eerste interactieve element na het openen van het dialoog, vóór de secties agentstappen/agentresultaten/workspace-publicaties.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-4-Voeg-toegankelijk-inline-uitklappaneel-met-scope-disclaimer-toe.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-4-Voeg-toegankelijk-inline-uitklappaneel-met-scope-disclaimer-toe.md), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

Risico's: Als IterationSessionDialog momenteel op basis van de rauwe Chip-tekst een breedte- of layoutaanname maakt, kan het vervangen door de bredere ClassificationBadge-component met uitklappaneel de dialooglayout beïnvloeden; dit dient tijdens implementatie visueel/geautomatiseerd op layoutoverflow gecontroleerd te worden., Mocht ClassificationBadge in de huidige codebase strak gekoppeld zijn aan de lijstkaart-context (bv. vaste breedte, rij-specifieke callbacks), dan is mogelijk een kleine, niet-functionele parameterisatie nodig om hem ook in het dialoog te kunnen hergebruiken zonder de bestaande lijstkaart-werking te wijzigen.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
