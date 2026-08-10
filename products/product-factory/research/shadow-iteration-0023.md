---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0023
date: 2026-08-10
status: approved
sources:
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md
  - https://product-factory-acceptance.vdzonsoftware.nl
  - https://product-factory-api-acceptance.vdzonsoftware.nl/api/shadow-iterations
  - https://docs.github.com/en/actions/how-tos/troubleshoot-workflows
---
# Productcyclus 23

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Onderzoek op 2026-08-10 combineerde de publieke broncode/architectuurdocs van product-factory (GitHub) met een live Playwright-doorloop van de acceptatieomgeving inclusief netwerkcapture. Beide punten die de eigenaar in het productoverleg noemde, zijn nu concreet en met bewijs onderbouwd: (1) het hoofdscherm toont zes gelijkwaardige secties zonder visuele hiërarchie tussen de drie dingen die de eigenaar wil zien (nieuwe cyclus starten, wat cycli opleverden, welke stories daaruit volgden) en overige technische info; (2) de reden achter een niet-geaccepteerde cyclus is structureel niet vooraan zichtbaar. Bij een technische mislukking (status FAILED) toont de detaildialoog wél direct een "Foutreden"-veld. Maar bij een inhoudelijke afwijzing/revisie door de eigen criticus (NEEDS_REVISION/REJECTED) bestaat geen los "reden"-veld: de motivatie zit uitsluitend verstopt in de ingeklapte "Criticus"-tegel tussen vier andere rol-tegels, als deels rauwe JSON — de badge zegt dit zelf expliciet ("Dit toont wat de uitkomst was, niet waarom"). Live is bovendien een cyclus aangetroffen met status NEEDS_REVISION waarvan de dialoog helemaal geen Criticus-artefact toont, zonder enige duiding waarom, ook al garandeert de eigen backendcode dat de criticus normaliter altijd vóór zo'n status draait.

### Hoofdscherm bundelt zes gelijkwaardige secties zonder hiërarchie tussen kernacties en detailinfo

OverviewPage (dashboard-frontend/lib/main.dart, build vanaf regel 456) rendert één lange ListView met achtereenvolgens Producten, Productcycli en onderzoekssessies, Software Factory-stories, Overleggen, Storywachtrij en Workspace, allemaal met dezelfde titleLarge-koptekst en zonder tabs, secties of samenvattend startscherm. Live screenshot van de acceptatieomgeving (volledige pagina, 2026-08-10) bevestigt dit: de knop 'Start productcyclus nu' staat verscholen in een productkaart tussen zes andere knoppen/chips, en cyclusoverzicht, stories en overige informatie staan zonder duidelijke prioritering onder elkaar. Dit komt letterlijk overeen met de klacht van de eigenaar dat hij op het hoofdscherm snel drie dingen wil zien (nieuwe cyclus starten, wat eerdere cycli opleverden, welke stories daaruit voortkwamen) maar dat overige technische info in de weg zit.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### Technische mislukking toont wél direct een reden, inhoudelijke afwijzing/revisie niet

In de iteratie-detaildialoog (main.dart, IterationSessionDialog, rond regel 1038) wordt een los 'Foutreden'-blok alleen getoond if (status == 'FAILED'). Live bevestigd op shadow-hkh-autopilot-0002 (classificatie guardrail-conflict): direct onder 'Opdracht' staat 'Foutreden: Workspace-publicatie tijdelijk niet beschikbaar (previewdata, gesimuleerd).' Voor een inhoudelijke uitkomst van de eigen criticus (status NEEDS_REVISION of REJECTED, classificatie onderzoek-onvoldoende/richting-verworpen) bestaat geen equivalent los reden-veld: de dialoog toont alleen de rolgeschiedenis en een lijst inklapbare artefacttegels; de criticus-motivatie (overallVerdict, summary, issues, requiredChanges) zit uitsluitend in de collapsed 'Criticus'-tegel tussen de andere roltegels. classification.dart bevat een expliciete disclaimer in de badge zelf ('Dit toont wat de uitkomst was, niet waarom... die laatste blijft voorbehouden aan de bestaande IterationSessionDialog'), maar die dialoog levert die 'waarom' dus alleen voor FAILED, niet voor REVISE/REJECT.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### Live voorbeeld van een NEEDS_REVISION-cyclus zonder enig zichtbaar criticusoordeel in de UI

Live doorgeklikt (Playwright semantics-tree-techniek) naar shadow-hkh-autopilot-0003 (status NEEDS_REVISION, criticVerdict REVISE volgens /api/shadow-iterations) toont de detaildialoog onder 'Voortgang' en 'Resultaat en onderbouwing' uitsluitend één voltooide stap en artefact: 'Onderzoeker'. Er is geen Criticus-, Product owner-, UX- of Story writer-tegel te zien, en geen enkele tekst legt uit waarom de cyclus als 'onderzoek-onvoldoende' is geclassificeerd. Vergeleken met een wél volledig doorlopen cyclus (shadow-hkh-autopilot-0001, ACCEPTED) waar alle vijf roltegels inclusief Criticus zichtbaar zijn, ontbreekt hier zelfs de mogelijkheid om de reden zelf op te zoeken. De eigen backendcode (ShadowIterationEngine.kt, regel 142-183) zet een NEEDS_REVISION-status uitsluitend nadat de criticus daadwerkelijk gedraaid heeft en 'REVISE' heeft geoordeeld — in een echte, door de motor uitgevoerde cyclus zou een Criticus-artefact dus horen te bestaan. Dat de acceptatieomgeving (representatieve nepdata) hier een inconsistente/onvolledige staat toont, bevestigt tegelijk dat de UI geen enkele foutmelding of duiding geeft wanneer het verwachte criticusartefact ontbreekt.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt)

### Cyclusoverzicht op het hoofdscherm toont per regel status en criticusverdict, maar geen reden

De iteratielijst op het hoofdscherm (main.dart regel 683-693) bouwt de subtitle-regel op uit status, huidige rol, starttijd, duur, kandidatenaantal, 'criticus: ${criticVerdict}' en een delivery-label, allemaal met een punt gescheiden in doorlopende tekst. Dit toont wél het enkele woord van het verdict (bv. 'REVISE' of 'REJECT'), maar nergens de onderliggende motivatie — de eigenaar moet daarvoor eerst doorklikken naar de detaildialoog én daar zelf de juiste artefacttegel vinden en openklappen, zoals hierboven bevestigd.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart)

### Productmissie en agentketen zijn eenduidig gedocumenteerd, wat de scope van dit gat bevestigt

README.md en docs/architecture/functioneel-overzicht.md beschrijven expliciet dat elke cyclus vijf agenttaken doorloopt (RESEARCHER → PRODUCT_OWNER → UX_DESIGNER → STORY_WRITER → CRITIC) en dat 'elke stap... per stap zichtbaar is in het dashboard (status, starttijd, eindtijd, foutmelding)'. Deze belofte geldt voor de status van een stap, niet expliciet voor de inhoudelijke reden van een REVISE/REJECT-eindoordeel — de documentatie maakt zelf geen onderscheid tussen 'stapstatus zichtbaar' en 'eindoordeel-motivatie vooraan zichtbaar', wat de huidige lacune bevestigt vanuit de eigen bronnen, niet alleen vanuit UI-observatie.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md)

### Huidige applicatie

**Doel:** Product Factory is de zelfstandige Kotlin/Flutter-applicatie die autonome productontwikkeling uitvoert: ze doet webonderzoek, kiest een productrichting, ontwerpt UX en schrijft/beoordeelt storykandidaten in een vaste vijfstaps-agentketen (RESEARCHER → PRODUCT_OWNER → UX_DESIGNER → STORY_WRITER → CRITIC), en biedt geaccepteerde stories aan de Software Factory aan. Deze iteratie betreft Product Factory als product-op-zichzelf (het eigen dashboard en de orchestratie), met de eigenaar zelf als enige gebruiker/bediener via het Flutter-webdashboard; het systeem draait ook voor het productiedomein hkh-autopilot.

**Wat ontbreekt:**
- Het hoofdscherm (OverviewPage) toont zes gelijkwaardige, ongeprioriteerde secties zonder visuele scheiding tussen de drie kernacties die de eigenaar snel wil zien (cyclus starten, cyclusresultaten, voortgekomen stories) en overige detailinformatie.
- Voor cycli die inhoudelijk zijn afgewezen of om revisie vragen door de eigen criticus (NEEDS_REVISION/REJECTED) toont de detaildialoog geen los, direct zichtbaar reden-veld zoals dat wél bestaat voor technische mislukkingen (FAILED → 'Foutreden'); de motivatie zit verstopt in een collapsed, deels rauwe-JSON criticustegel tussen vier andere roltegels.
- Live is een cyclus met status NEEDS_REVISION aangetroffen waarvan de dialoog zelfs geen Criticus-artefact toont — de UI geeft in dat geval geen enkele duiding of foutmelding over het ontbreken van de verwachte motivatie, wat de klacht van de eigenaar ('ik kan niet zien waarom iets is afgekeurd') tot in een concreet, reproduceerbaar voorbeeld bevestigt.
- De iteratielijst op het hoofdscherm toont per cyclus alleen het enkele woord van het criticusoordeel ('criticus: REVISE'), zonder enige indicatie dat er meer context beschikbaar is of hoe die te bereiken is.

### Verbetermogelijkheden

- Voeg voor NEEDS_REVISION/REJECTED-cycli een los, direct zichtbaar "Reden"-blok toe aan de detaildialoog (analoog aan het bestaande "Foutreden"-blok bij FAILED), gevuld met het criticus-summary/overallVerdict, zodat de eigenaar niet meer zelf de juiste roltegel hoeft te vinden en open te klappen.
- Geef de cyclusregel op het hoofdscherm een korte, leesbare samenvatting van de reden (niet alleen het verdictwoord), zodat "waarom" al zichtbaar is vóór het openen van de detaildialoog — vergelijkbaar met hoe GitHub Actions faal-annotaties vooraan in de run-samenvatting toont in plaats van verstopt in logs.
- Herstructureer het hoofdscherm zodat cyclus-starten, cyclusoverzicht en voortgekomen stories een eigen, prominente plek krijgen (bijvoorbeeld los cyclusoverzichtscherm met duidelijke "nieuwe cyclus starten"-knop, zoals de eigenaar zelf voorstelde), en verplaats overige technische secties (Overleggen, Workspace, Storywachtrij) naar een minder prominente plek of apart tabblad.
- Voeg defensieve UI-tekst toe voor het geval een verwacht criticusartefact ontbreekt (zoals live waargenomen bij shadow-hkh-autopilot-0003), zodat de eigenaar een expliciete melding krijgt in plaats van een dialoog die stilzwijgend minder informatie toont dan de eigen documentatie belooft.

### Inspiratiebronnen

- [GitHub Actions workflow-run annotaties en job-summaries](https://docs.github.com/en/actions/how-tos/troubleshoot-workflows) — Toont hoe een vergelijkbaar orchestratiesysteem (een reeks automatische stappen met een pass/fail-uitkomst) faal-reden prominent in de run-samenvatting plaatst in plaats van verstopt in logs — relevant patroon voor het zichtbaar maken van de criticus-motivatie zonder te hoeven doorklikken naar een losse, ingeklapte tegel.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart) | 2026-08-10 | Publieke, eigen open GitHub-repository (robbertvdzon/product-factory); geen aparte licentiebepaling gevonden in de repo-root, maar dit is de eigen broncode van het product zelf, vrij te raadplegen en te citeren voor eigen productonderzoek. | Bevat de Flutter-frontendlogica van OverviewPage en IterationSessionDialog, de directe bron voor hoe het hoofdscherm en de cyclusdetail momenteel zijn opgebouwd. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart) | 2026-08-10 | Publieke, eigen open GitHub-repository; eigen broncode. | Bevat de classificatielogica en badge-widget die het 'wat' van een cyclus toont, met een expliciete code-comment die bevestigt dat het 'waarom' bewust elders (de detaildialoog) hoort te staan. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt) | 2026-08-10 | Publieke, eigen open GitHub-repository; eigen broncode. | Backend-orchestratielogica die vastlegt wanneer en hoe een NEEDS_REVISION/REJECTED-status ontstaat en of een criticusartefact daadwerkelijk gepersisteerd wordt, nodig om de live waargenomen lege dialoog correct te interpreteren. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md) | 2026-08-10 | Publieke, eigen open GitHub-repository; eigen documentatie. | Bevat de officiële productdoelbeschrijving (wat Product Factory doet, voor welke producten) en dient als bron voor currentState.purpose. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md) | 2026-08-10 | Publieke, eigen open GitHub-repository; eigen documentatie. | Beschrijft expliciet de vaste agentketen per cyclus en de belofte over dashboardzichtbaarheid per stap, nodig om te toetsen of het huidige gedrag aan de eigen documentatie voldoet. |
| [bron](https://product-factory-acceptance.vdzonsoftware.nl) | 2026-08-10 | Eigen, publiek toegankelijke acceptatieomgeving zonder login, expliciet bedoeld voor dit onderzoek, met representatieve nepdata (geen persoonsgegevens). | Live doorloop (Playwright, semantics-tree-techniek) van het daadwerkelijke, draaiende dashboard om te verifiëren hoe het hoofdscherm en de cyclusdetaildialoog er in de praktijk uitzien, inclusief netwerkcapture van de echte API-responses. |
| [bron](https://product-factory-api-acceptance.vdzonsoftware.nl/api/shadow-iterations) | 2026-08-10 | Eigen, publiek bereikbare acceptatie-API met representatieve nepdata, geraadpleegd via netwerkcapture tijdens een echte paginalaad in de browser. | Toont de ruwe status/criticVerdict-waarden per iteratie (NEEDS_REVISION/REVISE, FAILED, ACCEPTED/ACCEPT) die de basis vormen voor de classificatie- en dialooglogica. |
| [bron](https://docs.github.com/en/actions/how-tos/troubleshoot-workflows) | 2026-08-10 | Publieke, officiële GitHub-documentatie; vrij raadpleegbaar, geciteerd als inspiratiebron, niet als eigen bron voor productfeiten. | Beschrijft hoe GitHub Actions faal-'annotations' prominent in de workflow-run-samenvatting toont in plaats van verstopt in logs, relevant als inspiratie voor het vooraan tonen van een afwijzingsreden. |

## Productbeslissing

Voeg voor cycli met status NEEDS_REVISION of REJECTED een los, direct zichtbaar \"Reden\"-blok toe aan de bestaande IterationSessionDialog — met dezelfde prominentie en positie als het bestaande \"Foutreden\"-blok dat nu alleen bij status FAILED verschijnt. Dit reden-blok wordt gevuld met de motivatie uit het Criticus-artefact (overallVerdict, summary, requiredChanges) zodat de eigenaar niet meer zelf de collapsed, deels rauwe-JSON Criticus-tegel tussen vier andere roltegels hoeft te vinden en open te klappen. Voor het live waargenomen randgeval waarin een NEEDS_REVISION/REJECTED-cyclus géén Criticus-artefact bevat (terwijl de backend dit normaliter garandeert), toont de dialoog expliciete tekst dat het oordeel ontbreekt, in plaats van de tegel stilzwijgend weg te laten. De bredere herstructurering van het hoofdscherm (hiërarchie tussen cyclus starten, cyclusresultaten, stories en overige technische secties) wordt bewust niet in deze iteratie meegenomen, om de wijziging klein, geïsoleerd toetsbaar en terugdraaibaar te houden.

**Waarom:** De eigenaar noemde in het productoverleg letterlijk dat de reden achter een niet-geaccepteerde cyclus niet vooraan zichtbaar is. Het onderzoek onderbouwt dit met code (main.dart, classification.dart) en een reproduceerbaar live voorbeeld (shadow-hkh-autopilot-0003) waarbij zelfs geen Criticus-artefact zichtbaar is. Deze richting sluit aan bij de missie (zelfkritisch toetsen of bestaand gedrag nog klopt) en de productprincipes: hij legt eerst uit waarom het huidige gedrag zo is (Foutreden bestaat alleen voor FAILED, classification.dart documenteert zelf dat 'waarom' bewust in de dialoog hoort), is klein en in isolatie te beoordelen/terug te draaien, en is bruikbaar vanuit het perspectief van de eigenaar als enige gebruiker — niet vanuit wat intern het makkelijkst te bouwen is. De grotere hoofdschermherstructurering is bewust apart gehouden omdat die te veel gelijktijdige, onderling afhankelijke wijzigingen zou vergen voor één toetsbare stap.

### Prioriteiten
- Voeg een "Reden"-blok toe aan IterationSessionDialog voor status NEEDS_REVISION/REJECTED, gevoed uit het Criticus-artefact (overallVerdict, summary, requiredChanges).
- Voeg expliciete fallback-tekst toe wanneer bij NEEDS_REVISION/REJECTED het verwachte Criticus-artefact ontbreekt, zodat dit zichtbaar is als afwijking in plaats van stille leegte.
- Beoordeel na oplevering of de cyclusregel op het hoofdscherm (nu alleen het woord 'criticus: REVISE') een korte samenvatting van de reden verdient, als losse vervolgstap.
- Herstructurering van het hoofdscherm (hiërarchie tussen cyclus starten/resultaten/stories en overige secties) bewust uitstellen tot een volgende, apart te beoordelen iteratie.

### Besluiten
- **Voeg in IterationSessionDialog een los, direct zichtbaar "Reden"-blok toe voor cycli met status NEEDS_REVISION of REJECTED, gevuld met het overallVerdict/summary/requiredChanges uit het Criticus-artefact — analoog aan het bestaande "Foutreden"-blok dat nu alleen bij status FAILED getoond wordt.** — Dit lost precies het gat op dat de eigenaar zelf benoemde: bij FAILED staat de reden al vooraan, maar bij een inhoudelijke afwijzing/revisie door de eigen criticus moet hij nu eerst doorklikken en de juiste, deels rauwe-JSON roltegel openklappen. classification.dart bevestigt zelf expliciet dat de badge het 'wat' toont en dat het 'waarom' bewust in deze dialoog hoort te staan — dat is nu niet het geval. Hergebruik van het bestaande Foutreden-patroon houdt de wijziging klein, herkenbaar en makkelijk te beoordelen en terug te draaien.
- **Toon expliciete tekst in de detaildialoog (bijv. "Criticus-oordeel ontbreekt voor deze cyclus") wanneer status NEEDS_REVISION of REJECTED is maar geen Criticus-artefact aanwezig is, in plaats van de tegel stilzwijgend weg te laten.** — Live is dit exacte geval aangetroffen bij shadow-hkh-autopilot-0003: status NEEDS_REVISION zonder enig Criticus-artefact in de dialoog. ShadowIterationEngine.kt garandeert dat de criticus normaliter altijd vóór zo'n status draait, dus het ontbreken ervan is een afwijking die de eigenaar moet kunnen zien, niet een stille leegte die de indruk wekt dat er simpelweg geen reden is.
- **Laat de bredere herstructurering van het hoofdscherm (zes gelijkwaardige secties, geen hiërarchie tussen cyclus-starten/resultaten/stories en overige technische info) deze iteratie ongemoeid; dit wordt een aparte, latere richting.** — Deze herstructurering raakt zes onafhankelijke secties tegelijk en is daarmee niet in één klein, geïsoleerd te beoordelen en terug te draaien stap te vatten, in tegenstelling tot het reden-veld dat één duidelijk afgebakende dialoog-uitbreiding is. Eerst deze kleinere, scherp onderbouwde verbetering doorvoeren en evalueren voordat een grotere layoutwijziging wordt overwogen, sluit aan bij 'klein en toetsbaar'.

## UX-voorstel: Reden-blok bij niet-geaccepteerde cyclus (NEEDS_REVISION/REJECTED)

**Gebruikersdoel:** Als eigenaar/enige gebruiker van het Product Factory dashboard wil ik bij het openen van een cyclusdetail direct zien waaróm een cyclus om revisie vraagt of is afgewezen door de criticus, zonder zelf de collapsed, deels rauwe-JSON Criticus-tegel tussen vier andere roltegels te hoeven vinden en openklappen.

### Flow
1. Eigenaar opent het dashboard en ziet de cycluslijst op het hoofdscherm, met per regel status en criticusverdict (bv. 'criticus: REVISE').
2. Eigenaar klikt op een cyclusregel met status NEEDS_REVISION of REJECTED; de bestaande IterationSessionDialog opent.
3. Dialoog toont direct onder 'Opdracht' en vóór de roltegels-sectie een nieuw 'Reden'-blok, met dezelfde prominentie en positie als het bestaande 'Foutreden'-blok dat nu alleen bij status FAILED verschijnt.
4. Als een Criticus-artefact aanwezig is, vult het Reden-blok automatisch met leesbare tekst op basis van overallVerdict, summary en requiredChanges (geen rauwe JSON).
5. Als ondanks status NEEDS_REVISION/REJECTED geen Criticus-artefact aanwezig is, toont het Reden-blok expliciet 'Criticus-oordeel ontbreekt voor deze cyclus' in plaats van de sectie stilzwijgend weg te laten.
6. Eigenaar kan optioneel nog steeds de onderliggende Criticus-roltegel openklappen voor het volledige artefact, als aanvullende diepgang naast het samengevatte Reden-blok.
7. Eigenaar sluit de dialoog; bestaand gedrag voor status FAILED (Foutreden-blok) en ACCEPTED/PENDING (geen Reden-blok) blijft ongewijzigd.

### Wireframe

IterationSessionDialog (bijgewerkt)
┌──────────────────────────────────────────────────────┐
│ Cyclus #shadow-hkh-autopilot-0003              [X]     │
│ Status: NEEDS_REVISION   Criticus: REVISE               │
├──────────────────────────────────────────────────────┤
│ Opdracht: <opdrachtomschrijving>                         │
│                                                            │
│ (bestaand, alleen bij status = FAILED)                    │
│   Foutreden: <technische foutmelding>                     │
│                                                            │
│ NIEUW — Reden-blok (alleen bij NEEDS_REVISION/REJECTED):  │
│   Variant A — Criticus-artefact aanwezig:                 │
│   ┌────────────────────────────────────────────────┐     │
│   │ Reden                                            │     │
│   │ Oordeel: REVISE                                  │     │
│   │ Samenvatting: <overallVerdict.summary>           │     │
│   │ Vereiste aanpassingen:                           │     │
│   │  • <requiredChanges[0]>                          │     │
│   │  • <requiredChanges[1]>                          │     │
│   └────────────────────────────────────────────────┘     │
│   Variant B — geen Criticus-artefact aanwezig:            │
│   ┌────────────────────────────────────────────────┐     │
│   │ ⚠ Reden                                          │     │
│   │ Criticus-oordeel ontbreekt voor deze cyclus.     │     │
│   │ Normaliter draait de criticus vóór deze status,   │     │
│   │ maar er is geen artefact opgeslagen gevonden.     │     │
│   └────────────────────────────────────────────────┘     │
│                                                            │
│ Voortgang / Roltegels (bestaand, ongewijzigd):            │
│  [Onderzoeker ✓]  [Product owner …]  [UX …]                │
│  [Story writer …] [Criticus ▸ open voor volledig artefact] │
└──────────────────────────────────────────────────────────┘
Positie: Reden-blok staat direct onder 'Opdracht' en vóór de roltegels, zichtbaar zonder scrollen bij normale dialooggrootte, visueel gelijk gestyled (kader, label) aan het bestaande Foutreden-blok. Voor status ACCEPTED/PENDING wordt geen Reden-blok getoond.

### Interactiehypotheses
- Voor elke cyclus met status NEEDS_REVISION of REJECTED én een aanwezig Criticus-artefact toont de dialoog een 'Reden'-blok met niet-lege samenvattingstekst; verifieerbaar via een geautomatiseerde widget-/integratietest die de dialoog opent en het Reden-blok controleert op een niet-leeg tekstelement.
- Voor elke cyclus met status NEEDS_REVISION of REJECTED zonder Criticus-artefact toont de dialoog exact de fallbacktekst 'Criticus-oordeel ontbreekt voor deze cyclus'; verifieerbaar via een geautomatiseerde test tegen een gemockte API-respons zonder Criticus-artefact.
- Voor cycli met status ACCEPTED of PENDING wordt geen Reden-blok gerenderd (regressie op bestaand gedrag); verifieerbaar door assertie dat het Reden-widget afwezig is in de widget tree.
- Het gerenderde Reden-blok bevat geen rauwe-JSON-patronen (accolades/aanhalingstekens rond sleutel-waardeparen); verifieerbaar via een geautomatiseerde regex-check op de gerenderde tekstinhoud.
- Het bestaande Foutreden-blok bij status FAILED blijft ongewijzigd zichtbaar en functioneel na deze wijziging; verifieerbaar via een regressietest op de bestaande widgetlocatie en teksteigenschap.

### Toegankelijkheid
- Reden-blok is met toetsenbord bereikbaar/focusbaar in dezelfde tab-volgorde als het bestaande Foutreden-blok, direct na 'Opdracht' en vóór de roltegels-sectie.
- Reden-blok krijgt een semantisch label (bv. Semantics(label: 'Reden voor status') zodat schermlezers de sectie expliciet aankondigen vóór de detailtekst wordt voorgelezen.
- Kleurcontrast van tekst en kaderrand in het Reden-blok voldoet aan WCAG AA (minimaal 4,5:1 voor platte tekst), voor zowel de normale invulling als de waarschuwingsvariant.
- De waarschuwingsvariant (ontbrekend Criticus-artefact) communiceert de afwijking niet uitsluitend via kleur of icoon (⚠), maar ook via expliciete tekst, zodat het ook zonder kleurwaarneming duidelijk is.
- Leesvolgorde voor schermlezers volgt de visuele volgorde: Reden-blok wordt voorgelezen vóór de inklapbare roltegels, niet ertussen of erna.

### Privacy
- Het Reden-blok toont uitsluitend operationele metadata van Product Factory zelf (criticusoordeel, samenvatting, vereiste aanpassingen over de productcyclus) — geen persoonsgegevens of gebruikersdata van andere producten.
- Geen wijziging aan databronnen of API's die persoonsgegevens verwerken; het Reden-blok hergebruikt uitsluitend reeds bestaande, al opgeslagen Criticus-artefactvelden.
- De fallbacktekst bij een ontbrekend Criticus-artefact bevat geen technische stacktraces, interne systeempaden of andere gevoelige debuginformatie — alleen een neutrale, begrijpelijke melding.
- Deze wijziging introduceert geen nieuwe logging, tracking of externe token-uitwisseling; het blijft een presentatielaag-aanpassing op reeds beschikbare, eigen operationele data.

## Kritische beoordeling

**Oordeel:** ACCEPT

Eén kandidaat ter beoordeling: "Toon direct zichtbaar 'Reden'-blok bij NEEDS_REVISION/REJECTED, gevuld uit Criticus-artefact of expliciete fallback". De onderbouwing is sterk: concrete code-referenties (main.dart, classification.dart, ShadowIterationEngine.kt), een live-geverifieerd voorbeeld (shadow-hkh-autopilot-0003 zonder zichtbaar Criticus-artefact) en directe aansluiting op de expliciete klacht van de eigenaar. De wijziging is presentationeel, klein, geïsoleerd en terugdraaibaar, introduceert geen nieuwe API-velden en raakt geen HKH Autopilot-data. Privacy is niet in het geding (alleen eigen operationele metadata) en toegankelijkheid is expliciet meegenomen (toetsenbordvolgorde, semantisch label, contrast, geen kleur-only signalering). De autonomie-gate is gerespecteerd: alle acceptatiecriteria zijn agent-verifieerbaar via geautomatiseerde widget-/mocktests, geen menselijk besluitmoment vereist. Er is één relevante spanning die de kandidaat zelf al herkent en mitigeert: de veronderstelde Criticus-velden (overallVerdict/summary/requiredChanges) uit het onderzoeksdocument komen niet overeen met wat candidate 40 (gepubliceerd, op basis van live inspectie) meldt over de daadwerkelijke, vereenvoudigde schema's (verdict/reason als platte strings) voor alle drie zichtbare iteraties. De kandidaat dwingt echter expliciet een voorafgaande geautomatiseerde inspectiestap af en laat ruimte voor "de werkelijk aangetroffen equivalenten", dus dit is voldoende afgedekt en niet blokkerend — vergelijkbaar met hoe candidates 37-40 hetzelfde risico al behandelden.
- **WARNING · CONSISTENCY** — De onderzoeksbron en het wireframe gaan uit van een rijk Criticus-schema (overallVerdict/summary/issues/requiredChanges), terwijl het reeds gepubliceerde candidate 40 op basis van live inspectie meldt dat alle drie zichtbare iteraties juist een vereenvoudigd schema hebben (bv. verdict/reason als platte strings). De kandidaat mitigeert dit al met een verplichte vooraf-inspectiestap en de formulering 'of de werkelijk aangetroffen equivalenten', dus dit is geen blokkade, maar de implementerende agent moet dit scherp naleven om geen mismatch met de echte data te introduceren.
- **INFO · CONSISTENCY** — Het nieuwe Reden-blok en de bestaande, onderliggende Criticus-roltegel (candidates 37/38) tonen deels overlappende informatie in dezelfde dialoog. De kandidaat erkent dit zelf als risico en vraagt om een beknopte samenvatting in plaats van volledige herhaling; dit is een aandachtspunt voor de implementatie, geen blokkerend issue.

## Geaccepteerde storykandidaten

### Toon direct zichtbaar 'Reden'-blok bij NEEDS_REVISION/REJECTED, gevuld uit Criticus-artefact of expliciete fallback

_Sleutel: `reden-blok-needs-revision-rejected`_

IterationSessionDialog toont vandaag alleen voor status FAILED een los, direct zichtbaar 'Foutreden'-blok (candidate 33). Voor cycli die inhoudelijk door de eigen criticus zijn afgewezen of om revisie vragen (status NEEDS_REVISION/REJECTED) bestaat geen equivalent: de motivatie is weliswaar sinds de candidates 37-40 als leesbare tekst beschikbaar, maar zit uitsluitend verstopt in de standaard ingeklapte Criticus-roltegel tussen vier andere roltegels (candidate 38). Live is bovendien op shadow-hkh-autopilot-0003 een cyclus met status NEEDS_REVISION aangetroffen zonder enig zichtbaar Criticus-artefact, zonder duiding, terwijl ShadowIterationEngine.kt garandeert dat de criticus normaliter altijd vóór zo'n status draait. Deze story voegt aan IterationSessionDialog, direct onder 'Opdracht' en vóór de roltegels-sectie, een nieuw 'Reden'-blok toe met dezelfde visuele prominentie/stijl als het bestaande Foutreden-blok, dat uitsluitend wordt getoond bij status NEEDS_REVISION of REJECTED. Is een Criticus-artefact aanwezig, dan vult het blok automatisch met leesbare samenvattingstekst (geen rauwe JSON) afgeleid van de daadwerkelijke velden van dat artefact. Is geen Criticus-artefact aanwezig ondanks deze status, dan toont het blok een vaste, neutrale fallbacktekst die het ontbreken van het oordeel expliciet meldt, in plaats van de sectie stilzwijgend weg te laten. De implementerende agent inspecteert eerst geautomatiseerd de werkelijke Criticus-artefactstructuur (zoals die na de candidates 37-40 in productie bestaat) om te bepalen welke velden daadwerkelijk beschikbaar zijn, zodat het blok op de echte datastructuur is gebaseerd. De wijziging is een presentatielaag-aanpassing zonder nieuwe API-velden, nieuwe dataverzameling of wijziging aan HKH Autopilot zelf, en houdt de bredere hoofdschermherstructurering (zes gelijkwaardige secties) bewust buiten scope.

**Acceptatiecriteria**
- Voor status NEEDS_REVISION of REJECTED toont IterationSessionDialog een nieuw 'Reden'-blok direct onder 'Opdracht' en vóór de roltegels-sectie, visueel gestyled (kader, label) analoog aan het bestaande Foutreden-blok uit candidate 33.
- Wanneer een Criticus-artefact aanwezig is, bevat het Reden-blok niet-lege, leesbare samenvattingstekst afgeleid van de daadwerkelijke velden van dat artefact (bv. overallVerdict/summary/requiredChanges of de werkelijk aangetroffen equivalenten), zonder rauwe JSON-notatie (geen accolades/aanhalingstekens rond sleutel-waardeparen), verifieerbaar via een geautomatiseerde widget-/regexcheck.
- Wanneer geen Criticus-artefact aanwezig is ondanks status NEEDS_REVISION/REJECTED, toont het Reden-blok in plaats daarvan een vaste, neutrale fallbacktekst (bv. 'Criticus-oordeel ontbreekt voor deze cyclus') zonder technische stacktraces of interne paden, verifieerbaar via een geautomatiseerde test tegen een gemockte iteratie zonder Criticus-artefact.
- Voor status ACCEPTED of PENDING wordt geen Reden-blok gerenderd; een geautomatiseerde regressietest bevestigt de afwezigheid van het widget in de widget tree voor deze statussen.
- Het bestaande Foutreden-blok bij status FAILED (candidate 33) en de bestaande, standaard ingeklapte Criticus-roltegel met volledig artefact (candidate 37/38) blijven ongewijzigd zichtbaar en functioneel; een regressietest dekt dit.
- Het Reden-blok is toetsenbord-bereikbaar in dezelfde taborde als het Foutreden-blok en heeft een semantisch label voor schermlezers, zodat het vóór de roltegels wordt aangekondigd.
- De implementerende agent documenteert vooraf, op basis van geautomatiseerde inspectie van de daadwerkelijke Criticus-contentJson-structuur in productie, welke velden voor het Reden-blok daadwerkelijk beschikbaar zijn en past de renderlogica daarop aan.
- Er wordt geen nieuw API-veld, geen wijziging aan classification.dart en geen wijziging aan HKH Autopilot-data geïntroduceerd; de wijziging is beperkt tot de bestaande IterationSessionDialog-renderlaag.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

Risico's: De werkelijke Criticus-artefactstructuur (na candidates 37-40) kan afwijken van de in het onderzoek aangenomen velden (overallVerdict/summary/requiredChanges); gemitigeerd door de verplichte inspectiestap voordat de renderlogica wordt geschreven., Het nieuwe Reden-blok en de bestaande, onderliggende Criticus-roltegel tonen deels dezelfde informatie op twee plekken in dezelfde dialoog; zorgvuldige positionering en beknoptheid van het Reden-blok (samenvatting, geen volledige herhaling) is nodig om de dialoog niet rommelig te maken., Het live aangetroffen ontbrekende Criticus-artefact bij een NEEDS_REVISION-cyclus kan wijzen op een onderliggend backend-datainconsistentieprobleem; deze story lost alleen de UI-weergave van dat scenario op, niet de onderliggende oorzaak.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
