---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0024
date: 2026-08-10
status: approved
sources:
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationApi.kt
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory-contracts/src/main/kotlin/nl/vdzon/productfactory/contracts/Contracts.kt
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/test/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngineTest.kt
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/preview/PreviewDataSeeder.kt
  - https://product-factory-acceptance.vdzonsoftware.nl
  - https://discuss.circleci.com/t/product-update-infrastructure-failure-badge-in-circleci-ui/47282
---
# Productcyclus 24

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Onderzoek combineerde de publieke broncode van product-factory (backend-engine, repository-laag, contracts, frontend) met een live Playwright-doorloop van de acceptatieomgeving, gericht op de expliciete open vraag uit het laatste overleg: is de afkeuringsdata er al, of is er ook een onderliggend dataprobleem? Antwoord: gedeeltelijk allebei. Een nieuw, code-bevestigd data-integriteitsprobleem is gevonden: wanneer de criticus overall 'ACCEPT' geeft maar alle individuele kandidaten alsnog duplicate/geblokkeerd zijn, overschrijft ShadowIterationEngine.kt het echte criticusoordeel met een synthetische 'REJECT'-waarde in de database, zonder markering — waardoor het (in iteratie 23 gebouwde) 'Reden'-blok en de statusbadge elkaar op hetzelfde scherm kunnen tegenspreken. Daarnaast blijft de al eerder gemelde badge 'guardrail-conflict' voor élke technische FAILED-fout live aantoonbaar misleidend (CircleCI's aparte 'Infrastructure Failure'-badge is hier een direct toepasbaar precedent). Twee eerder als problematisch bestempelde zaken bleken bij nader onderzoek genuanceerder: de delivery-label 'niet doorgezet (product staat niet op autonoom)' is een correcte historische snapshot, geen datafout — het probleem is uitsluitend tegenwoordige-tijd bewoording; en de 'Criticus-oordeel ontbreekt'-fallback blijkt via PreviewDataSeeder.kt alleen bereikbaar in gescripte demodata, niet in de echte engine. Ten slotte werkt het reden-patroon op kandidaatniveau (story_candidate.critic_reason, getoond als 'Beoordeling criticus') al goed en kan als voorbeeld dienen. De eerder bewust uitgestelde homepage-herstructurering (drie kernacties vooraan) staat nog open en is nu een logische vervolgstap.

### Guardrail-pad overschrijft het echte criticusoordeel met een synthetische 'REJECT'-waarde

In ShadowIterationEngine.kt (regels 178-188): als `verdict` (het overallVerdict van de criticus) gelijk is aan 'ACCEPT', maar de lijst `accepted` (kandidaten die individueel ACCEPT kregen, niet dupliceren en niet geblokkeerd zijn) leeg is, roept de code `repository.markReviewed(iteration.id, "REJECT", "REJECTED")` aan — met een hardgecodeerde string 'REJECT', niet het daadwerkelijke `verdict` ('ACCEPT'). Dit wordt opgeslagen in de kolom `shadow_iteration.critic_verdict` (ShadowIterationApi.kt regel 441-450) en zo doorgegeven aan de frontend via `ShadowIterationView.criticVerdict` (Contracts.kt regel 131). De frontend-badge (`classifyIterationOutcome` in classification.dart) leest alleen `status` ('REJECTED' → badge 'richting-verworpen'), maar het 'Reden'-blok in main.dart (regel 1068-1101) leest het rauwe criticus-artefact via `criticReasonSummary`, dat wél het echte `overallVerdict` toont. Voor dit specifieke pad kunnen badge en Reden-blok elkaar dus letterlijk tegenspreken op hetzelfde scherm. Het eigen testbestand ShadowIterationEngineTest.kt bevestigt dit pad bestaat (Scenario.DUPLICATE, regel 79-91, status wordt REJECTED) maar verifieert bewust niet `criticVerdict` voor dit geval, in tegenstelling tot vergelijkbare asserts bij de REVISE- en WARNING_ONLY_REVISE-scenario's (regels 97, 120) — een aanwijzing dat dit gat niet doelbewust is dichtgetimmerd.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationApi.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationApi.kt), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory-contracts/src/main/kotlin/nl/vdzon/productfactory/contracts/Contracts.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory-contracts/src/main/kotlin/nl/vdzon/productfactory/contracts/Contracts.kt), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/test/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngineTest.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/test/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngineTest.kt)

### Badge 'guardrail-conflict' voor FAILED is live opnieuw bevestigd als misleidend

classification.dart (regel 33-38) mapt in `kBekendeStatuswaardenPerCategorie` élke status 'FAILED' naar categorie `kGuardrailConflict`. Live Playwright-inspectie van shadow-hkh-autopilot-0002 (2026-08-10) toont badge 'guardrail-conflict', terwijl het bijbehorende 'Foutreden'-veld zegt: 'Workspace-publicatie tijdelijk niet beschikbaar (previewdata, gesimuleerd)'. Dit bevestigt dat de badge-categorie sinds eerdere iteraties ongewijzigd is: elke technische stapfout (agentfout, timeout, parsefout, publicatiefout — via `repository.failStep` in ShadowIterationEngine.kt regel 237) krijgt dezelfde specifieke, maar hier feitelijk onjuiste badge-tekst als een echte autonomiebeleid-blokkade.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### 'Reden'-blok en fallbacktekst uit iteratie 23 zijn opgeleverd en werken zoals ontworpen

main.dart (regel 1068-1101) toont nu bij status NEEDS_REVISION/REJECTED een los 'Reden'-blok, gevuld via `criticReasonSummary` (regel 1345-1365) met leesbare tekst uit `overallVerdict`, `summary` en `requiredChanges` van het meest recente criticus-artefact (`latestCriticArtifact`, regel 1323-1339), met fallbacktekst 'Criticus-oordeel ontbreekt voor deze cyclus' als er geen artefact is. Live bevestigd bij shadow-hkh-autopilot-0003 (NEEDS_REVISION, toont exact deze fallbacktekst) — dit is de eerder besloten en inmiddels gebouwde verbetering uit iteratie 23 (backlogId 41).

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### De 'Criticus-oordeel ontbreekt'-fallback is in de praktijk alleen bereikbaar via gescripte demodata, niet via de echte engine

PreviewDataSeeder.kt (regel 128) zet iteratie shadow-hkh-autopilot-0003 rechtstreeks op NEEDS_REVISION via `iterations.markReviewed(needsRevision.id, "REVISE", "NEEDS_REVISION")` zonder ooit een criticusstap te laten draaien. In de echte productiecode (ShadowIterationEngine.kt regel 163-183) wordt `markReviewed` echter altijd pas aangeroepen nadat de CRITIC-rol via `executeRole` is uitgevoerd en het resultaat als artefact is opgeslagen (regel 233 `repository.completeStep`). Een NEEDS_REVISION/REJECTED-iteratie zonder criticus-artefact kan dus in de echte engine niet ontstaan; het scenario dat live getoond wordt in de acceptatieomgeving is een niet-representatief seed-artefact, geen reproduceerbare productieklacht.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/preview/PreviewDataSeeder.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/preview/PreviewDataSeeder.kt), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt)

### 'Niet doorgezet (product staat niet op autonoom)' is een historische snapshot, geen datafout

ShadowIterationApi.kt (regel 79-93) documenteert expliciet: "Modus wordt afgeleid van de productinstelling, niet gekozen door de aanroeper" — `mode` wordt eenmalig vastgelegd bij het starten van een cyclus (`val mode = if (product.developmentMode == "autonomous") "autonomous" else "shadow"`) en daarna nooit bijgewerkt. De frontendfunctie `_deliveryLabel` (main.dart regel 1653-1655) vertaalt een niet-autonome snapshot naar de tegenwoordige-tijd tekst 'niet doorgezet (product staat niet op autonoom)'. Live tonen alle drie zichtbare iteraties van HKH Autopilot (gestart vóórdat het product op 'autonomous' stond) deze tekst, terwijl de productkaart daarboven nu wél de chip 'autonomous' toont — een schijnbare tegenstrijdigheid die in werkelijkheid consistente, historisch correcte data is met misleidende present-tense bewoording.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationApi.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationApi.kt), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### Per-kandidaat criticusreden werkt al goed en kan als voorbeeld dienen voor iteratieniveau

`story_candidate.critic_reason` (gevuld vanuit `candidateReviews[].reason` in het criticusschema, ShadowSchemas.kt regel 52) wordt via `StoryCandidateView.criticReason` (Contracts.kt regel 110) al netjes getoond in de storydetaildialoog (main.dart regel 1902-1909, kopje 'Beoordeling criticus'). Live bevestigd op de storykandidaat 'Kaartweergave met foto-pins': duidelijk leesbare reden 'Kleine, toetsbare eerste stap met duidelijke gebruikerswaarde.' Dit toont dat een goed werkend reden-patroon al bestaat op kandidaatniveau, maar dat het equivalent op iteratieniveau (het 'Reden'-blok) kwetsbaar is voor de hierboven genoemde synthetische-verdict-inconsistentie.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory-contracts/src/main/kotlin/nl/vdzon/productfactory/contracts/Contracts.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory-contracts/src/main/kotlin/nl/vdzon/productfactory/contracts/Contracts.kt), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### Huidige applicatie

**Doel:** Product Factory past haar eigen autonome onderzoek-ontwerp-lever-cyclus toe op zichzelf: het dashboard/orchestratie van Product Factory zelf is hier het product. Primaire gebruiker is de producteigenaar (Robbert), die per productcyclus drie dingen snel wil kunnen zien: een nieuwe cyclus starten, wat eerdere cycli hebben opgeleverd, en welke stories daaruit zijn voortgekomen — plus, expliciet sinds het laatste overleg, altijd een zichtbare reden + wie/wat besliste bij een afkeuring of revisie.

**Wat ontbreekt:**
- Het hoofdscherm bundelt nog steeds 6+ gelijkwaardige secties (Producten, Productcycli, Software Factory-stories, Overleggen, Storywachtrij, Workspace) zonder hiërarchie tussen de drie kernacties en overige technische info; live bevestigd op 2026-08-10 en eerder bewust uitgesteld in iteratie 23 tot na de Reden-blok-verbetering.
- FAILED-iteraties krijgen altijd de badge 'guardrail-conflict', ongeacht de echte oorzaak. Live gereproduceerd op shadow-hkh-autopilot-0002: badge zegt 'guardrail-conflict', maar de eigen 'Foutreden' luidt 'Workspace-publicatie tijdelijk niet beschikbaar (previewdata, gesimuleerd)' — een infrastructuurfout, geen autonomiebeleid-blokkade.
- Nieuw, code-bevestigd data-integriteitsprobleem: als de criticus overall 'ACCEPT' geeft maar alle individuele kandidaten alsnog duplicate/geblokkeerd zijn, overschrijft ShadowIterationEngine.kt (regel 182-188) het echte criticusoordeel met een synthetische waarde 'REJECT' in shadow_iteration.critic_verdict, zonder markering dat dit afgeleid is. Het eigen testdossier (ShadowIterationEngineTest.kt) verifieert dit veld bewust niet voor dit pad. Gevolg: het 'Reden'-blok (dat het rauwe criticus-artefact leest) kan 'Eindoordeel: ACCEPT' tonen naast een badge 'richting-verworpen' op hetzelfde scherm.
- De delivery-labelbug 'niet doorgezet (product staat niet op autonoom)' is live nog steeds zichtbaar naast de productchip 'autonomous', maar is bij nader onderzoek geen datafout: 'mode' is een bewuste, in code gedocumenteerde snapshot van de productinstelling bij cyclusstart, geen live-veld. Het probleem is puur de tegenwoordige-tijd bewoording die een schijnbare tegenstrijdigheid suggereert.
- De fallback 'Criticus-oordeel ontbreekt voor deze cyclus' (gebouwd na iteratie 23) is live zichtbaar bij shadow-hkh-autopilot-0003, maar PreviewDataSeeder.kt bevestigt dat dit scenario alleen via gescripte demodata ontstaat; de echte engine draait de criticusstap altijd vóór NEEDS_REVISION/REJECTED. Eerdere iteraties behandelden dit ten onrechte als reproduceerbaar productiegedrag.

### Verbetermogelijkheden

- Bewaar bij het guardrail-pad ('ACCEPT' maar accepted.isEmpty()) het echte criticus-overallVerdict apart van de afgeleide iteratiestatus, in plaats van het te overschrijven met een synthetische 'REJECT'-waarde — zodat badge en Reden-blok nooit meer met elkaar in tegenspraak kunnen zijn op hetzelfde scherm.
- Splits de badge-categorie 'guardrail-conflict' zodat een technische stapfout (agentfout, timeout, parsefout, publicatiefout) een andere naam/kleur krijgt dan een daadwerkelijke autonomiebeleid-blokkade; CircleCI loste exact dit probleem eerder op met een aparte 'Infrastructure Failure'-badge naast reguliere failure-badges.
- Herformuleer de delivery-badgetekst van tegenwoordige tijd ('product staat niet op autonoom') naar expliciete verleden-tijd/snapshot-taal (bv. 'cyclus gestart in shadow-modus op 08-08-2026'), zodat historisch correcte data niet als tegenstrijdig met de huidige productinstelling oogt.
- Pak nu de eerder bewust uitgestelde homepage-herstructurering op (drie kernacties vooraan, overige info eronder), aangezien de daaraan voorafgaande Reden-blok-verbetering uit iteratie 23 inmiddels is opgeleverd en gevalideerd.
- Overweeg of de fallbacktekst 'Criticus-oordeel ontbreekt voor deze cyclus' nog nodig is als defensieve UI-maatregel nu bevestigd is dat dit scenario in de echte engine niet kan optreden — of vervang de demodata zodat de acceptatieomgeving geen niet-representatieve toestand meer toont aan wie het dashboard test.

### Inspiratiebronnen

- [CircleCI 'Infrastructure Failure' badge](https://discuss.circleci.com/t/product-update-infrastructure-failure-badge-in-circleci-ui/47282) — CircleCI had exact hetzelfde probleem als hier gevonden: elke pipelinefout toonde dezelfde generieke 'Failure'-badge, ongeacht of de oorzaak een infrastructuurprobleem of een echte testfout was. De oplossing was een losse, herkenbare badge specifiek voor infrastructuurfouten — een direct toepasbaar patroon voor het hier gevonden 'guardrail-conflict'-probleem, waarbij technische stapfouten en echte guardrail-blokkades nu identiek geclassificeerd worden.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt) | 2026-08-10 | Publieke GitHub-repository robbertvdzon/product-factory; eigen broncode van de opdrachtgever, geen aparte licentievermelding aangetroffen in dit bestand. | Bevat de kernlogica die bepaalt hoe FAILED/NEEDS_REVISION/REJECTED-uitkomsten worden vastgelegd, inclusief het gevonden synthetische-verdict-overschrijvingspad. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationApi.kt) | 2026-08-10 | Publieke GitHub-repository robbertvdzon/product-factory; eigen broncode van de opdrachtgever, geen aparte licentievermelding aangetroffen in dit bestand. | Bevat de repository-laag (markReviewed, saveCandidate, mode-afleiding bij cyclusstart) die de daadwerkelijke database-opslag en -documentatie van afkeuringsdata regelt. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory-contracts/src/main/kotlin/nl/vdzon/productfactory/contracts/Contracts.kt) | 2026-08-10 | Publieke GitHub-repository robbertvdzon/product-factory; eigen broncode van de opdrachtgever, geen aparte licentievermelding aangetroffen in dit bestand. | Definieert de precieze velden (criticVerdict, errorMessage, summary) die via de API aan de frontend worden blootgesteld, nodig om te bepalen welke data al bestaat versus ontbreekt. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart) | 2026-08-10 | Publieke GitHub-repository robbertvdzon/product-factory; eigen broncode van de opdrachtgever, geen aparte licentievermelding aangetroffen in dit bestand. | Bevat de UI-logica van het Reden-blok, het Foutreden-blok, de delivery-label en de storydetaildialoog die live is geverifieerd. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart) | 2026-08-10 | Publieke GitHub-repository robbertvdzon/product-factory; eigen broncode van de opdrachtgever, geen aparte licentievermelding aangetroffen in dit bestand. | Bevat de badge-classificatietabel die bepaalt welke statuswaarden tot welke (soms misleidende) badge-tekst leiden. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/test/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngineTest.kt) | 2026-08-10 | Publieke GitHub-repository robbertvdzon/product-factory; eigen broncode van de opdrachtgever, geen aparte licentievermelding aangetroffen in dit bestand. | Bevestigt dat het DUPLICATE/guardrail-pad een bestaand, geteste scenario is en laat zien welke velden daarbij bewust wel/niet geverifieerd worden. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/preview/PreviewDataSeeder.kt) | 2026-08-10 | Publieke GitHub-repository robbertvdzon/product-factory; eigen broncode van de opdrachtgever, geen aparte licentievermelding aangetroffen in dit bestand. | Toont dat de live zichtbare 'criticus-oordeel ontbreekt'-situatie een gescript demodata-artefact is en geen bereikbaar pad in de echte engine. |
| [bron](https://product-factory-acceptance.vdzonsoftware.nl) | 2026-08-10 | Standing acceptatieomgeving van de opdrachtgever zelf, met representatieve nepdata; geen externe rechtenbeperking van toepassing, eigen systeem. | Live Playwright-doorloop (screenshots van hoofdscherm, iteratiedetails 1/2/3 en storydetail) om de code-analyse te verifiëren tegen daadwerkelijk gerenderd gedrag. |
| [bron](https://discuss.circleci.com/t/product-update-infrastructure-failure-badge-in-circleci-ui/47282) | 2026-08-10 | Publiek CircleCI-communityforum; gebruikt uitsluitend als inspiratie/referentie voor UI-patroon, geen content overgenomen. | Concreet precedent van een vergelijkbaar CI/CD-dashboard dat exact hetzelfde 'alle fouten dezelfde badge'-probleem oploste met een aparte infrastructuurfout-badge. |

## Productbeslissing

Los in de eerstvolgende cyclus het code-bevestigde data-integriteitsprobleem op in ShadowIterationEngine.kt: wanneer de criticus overall ACCEPT geeft maar alle individuele kandidaten alsnog duplicate/geblokkeerd zijn, wordt dat echte ACCEPT-oordeel nu overschreven door een hardgecodeerde 'REJECT'-waarde in `shadow_iteration.critic_verdict`. Dit veroorzaakt dat de statusbadge en het pas opgeleverde 'Reden'-blok (iteratie 23) elkaar op hetzelfde scherm kunnen tegenspreken. De richting: sla het werkelijke criticus-oordeel op zoals het was, apart van de afgeleide iteratiestatus (REJECTED), zodat beide UI-elementen altijd consistent blijven — en breid het bestaande DUPLICATE-testscenario uit met een assertie die dit pad voortaan bewaakt. Overige gevonden aandachtspunten (badge-taxonomie 'guardrail-conflict', delivery-labelwoording, homepage-herstructurering) worden bewust niet meegenomen in deze cyclus, om de wijziging klein, samenhangend en in isolatie beoordeelbaar te houden.

**Waarom:** Het laatste overleg stelde expliciet de open vraag of er, naast het al opgeleverde Reden-blok, ook een onderliggend dataprobleem is. Het onderzoek beantwoordt die vraag met een concreet, code-bevestigd 'ja': het guardrail-pad in ShadowIterationEngine.kt overschrijft het echte criticusoordeel met een synthetische waarde, zonder markering, en het eigen testdossier bevestigt dat dit pad bewust ongetest is op dit punt. Dit is precies het soort probleem dat de missie van dit product raakt — niet wachten tot de eigenaar het meldt, maar zelf toetsen of het systeem nog klopt — en het voldoet aan de kwaliteitsregels: het is uit te leggen waarom het huidige gedrag zo is (een guardrail die een status wil afdwingen maar daarbij het brondata-oordeel verliest), en de fix is klein, geïsoleerd tot één functie en één testbestand, dus in isolatie te beoordelen en terug te draaien. Andere gevonden issues (badge-misclassificatie, labelwoording, homepage) zijn reëel maar groter van scope of louter cosmetisch; ze bewust uitstellen past bij het principe 'klein en toetsbaar' boven alles in één keer aanpakken.

### Prioriteiten
- Bewaar het echte criticus-overallVerdict apart van de afgeleide iteratiestatus in het guardrail-pad van ShadowIterationEngine.kt (regels 178-188), zodat badge en Reden-blok nooit meer tegenstrijdig kunnen zijn op hetzelfde scherm.
- Voeg een expliciete assertie op `criticVerdict` toe aan het DUPLICATE-scenario in ShadowIterationEngineTest.kt, zodat de fix in isolatie toetsbaar en terugdraaibaar is.
- Laat de badge-taxonomie voor 'guardrail-conflict' ongewijzigd deze cyclus; documenteer het als vervolgrichting met het CircleCI-precedent als referentie.
- Laat de delivery-labeltekst en de PreviewDataSeeder-demodata ongewijzigd; dit zijn wordings- respectievelijk demodatakwesties, geen datajuistheidsrisico's.
- Houd de homepage-herstructurering aan tot een volgende cyclus, na bevestiging dat de onderliggende iteratiedata weer consistent is.

### Besluiten
- **Volgende Product Factory-cyclus richt zich op het bewaren van het echte criticusoordeel (`overallVerdict`) los van de afgeleide iteratiestatus in het guardrail-pad van ShadowIterationEngine.kt, in plaats van het te overschrijven met de hardgecodeerde string 'REJECT'.** — Dit is het enige gevonden probleem dat code-bevestigd een data-integriteitsfout is (geen interpretatieverschil of wordingskwestie): wanneer de criticus overall ACCEPT geeft maar alle kandidaten alsnog geblokkeerd/duplicate zijn, wordt dat echte ACCEPT-oordeel in de database vervangen door 'REJECT', zonder markering dat dit afgeleid is. Daardoor kunnen de statusbadge en het pas in iteratie 23 gebouwde 'Reden'-blok elkaar letterlijk tegenspreken op hetzelfde scherm — precies het risico dat het laatste overleg expliciet als open vraag stelde ('is er ook een onderliggend dataprobleem?'). De fix is klein: één guardrail-pad in één bestand, met een bestaand testscenario (DUPLICATE) dat al aantoont waar de ontbrekende assertie zit.
- **De fix moet het bestaande testscenario ShadowIterationEngineTest.kt (DUPLICATE, regel 79-91) uitbreiden met een expliciete assertie op `criticVerdict`, zodat het pad dat nu bewust ongetest is, voortaan geverifieerd terugdraaibaar is.** — Kwaliteitsregel vereist dat een wijziging in isolatie te beoordelen en terug te draaien is; het testbestand toont al vergelijkbare asserts bij REVISE/WARNING_ONLY_REVISE (regels 97, 120) maar mist deze bewust bij DUPLICATE — dit is de kleinst mogelijke, toetsbare stap om het gat te sluiten zonder ander gedrag te raken.
- **De badge-taxonomieherziening voor 'guardrail-conflict' (elke FAILED-status krijgt dezelfde tekst, ongeacht infrastructuurfout vs. echte beleidsblokkade) wordt bewust niet in deze cyclus opgepakt, maar vastgelegd als vervolgrichting voor een latere cyclus.** — Dit is een reëel, live bevestigd probleem, maar vereist een nieuwe badge-taxonomie (zoals het CircleCI-precedent met een aparte 'Infrastructure Failure'-badge) — dat is een grotere, aparte ontwerpbeslissing dan de kleine, geïsoleerde data-integriteitsfix. Klein en toetsbaar per cyclus weegt zwaarder dan alles in één keer aanpakken.
- **De delivery-labeltekst 'niet doorgezet (product staat niet op autonoom)' wordt niet in deze cyclus herschreven, omdat onderzoek bevestigt dat dit geen datafout is maar een correcte historische snapshot met misleidende tegenwoordige-tijd bewoording — dit wordt als kleine, losse wordingsverbetering voor een volgende cyclus vastgelegd.** — Eerst begrijpen, dan wijzigen: nu duidelijk is dat `mode` bewust een snapshot bij cyclusstart is (gedocumenteerd in ShadowIterationApi.kt), is dit een cosmetische wordingskwestie, geen risico voor datavertrouwen zoals de synthetische-verdict-bug. Het verdient een eigen kleine, geïsoleerde stap in plaats van meeliften op deze fix.
- **De homepage-herstructurering (drie kernacties vooraan) blijft bewust uitgesteld tot na deze cyclus, ondanks dat de eerder blokkerende Reden-blok-verbetering nu is opgeleverd.** — De nieuw gevonden badge/Reden-tegenspraak ondermijnt het vertrouwen in precies de informatie die een herstructureerd hoofdscherm prominenter zou tonen; eerst de onderliggende datajuistheid herstellen is coherenter dan de layout eromheen te verbeteren terwijl de data zelf nog tegenstrijdig kan zijn.

## UX-voorstel: Consistent criticusoordeel bij afgekeurde/herziene iteratie (guardrail-pad)

**Gebruikersdoel:** Als producteigenaar wil Robbert op het iteratiedetailscherm altijd een Reden-blok zien dat het werkelijke criticusoordeel toont, zodat het nooit tegenstrijdig is met de statusbadge — ook niet wanneer het guardrail-pad (overall ACCEPT maar alle kandidaten geblokkeerd/duplicaat) de reden is dat een cyclus niet doorgaat.

### Flow
1. Robbert opent het hoofdscherm en ziet de productcyclus-kaart met de bestaande statusbadge (bv. 'richting-verworpen').
2. Robbert klikt op de iteratiekaart om het detailscherm te openen.
3. Detailscherm haalt iteratiedata op via de API; het rauwe, nooit-overschreven criticus-eindoordeel (overallVerdict) wordt apart meegegeven naast de afgeleide iteratiestatus.
4. Het Reden-blok toont twee gescheiden regels: 'Eindoordeel criticus: {overallVerdict}' en de bestaande statusbadge, zodat beide altijd zichtbaar en apart herkenbaar zijn.
5. Als overallVerdict=ACCEPT samenvalt met status=REJECTED (guardrail-pad), toont het Reden-blok automatisch een extra toelichtingszin: 'Alle voorgestelde kandidaten zijn geblokkeerd (duplicaat of guardrail), waardoor deze cyclus niet doorgaat ondanks een positief criticusoordeel.'
6. Voor overige REJECTED/NEEDS_REVISION-iteraties (geen guardrail-pad) blijft het Reden-blok ongewijzigd: alleen 'Eindoordeel criticus: {overallVerdict}' plus bestaande samenvatting/vereiste wijzigingen.
7. Robbert kan vanuit het Reden-blok doorklikken naar de betrokken storykandidaten voor het reeds bestaande, goed werkende 'Beoordeling criticus'-detail per kandidaat.
8. Een geautomatiseerde agenttest bevraagt de API-respons van een guardrail-pad-iteratie en controleert dat criticVerdict='ACCEPT' teruggegeven wordt (niet 'REJECT'), en dat de gerenderde pagina zowel het eindoordeel als de toelichtingszin bevat.
9. Een uitgebreide databasetest (DUPLICATE-scenario in ShadowIterationEngineTest.kt) verifieert dat de kolom shadow_iteration.critic_verdict het echte overallVerdict bevat in plaats van de hardgecodeerde string 'REJECT'.

### Wireframe

[Hoofdscherm]
┌─────────────────────────────────────────────┐
│ Product: HKH Autopilot        [autonomous]   │
│ Iteratie shadow-hkh-autopilot-0002            │
│ Status: [richting-verworpen]  ▸ klik voor detail │
└─────────────────────────────────────────────┘

[Iteratiedetailscherm — na klik]
┌─────────────────────────────────────────────┐
│ ← Terug          Iteratie shadow-...-0002     │
│                                                │
│ Status: [richting-verworpen]                  │
│                                                │
│ ── Reden ────────────────────────────────────│
│ Eindoordeel criticus: ACCEPT                  │
│                                                │
│ ⚠ Alle voorgestelde kandidaten zijn geblokkeerd│
│   (duplicaat of guardrail), waardoor deze     │
│   cyclus niet doorgaat ondanks een positief   │
│   criticusoordeel.                            │
│                                                │
│ Samenvatting: <bestaande tekst>               │
│ Vereiste wijzigingen: <bestaande lijst>       │
│ ───────────────────────────────────────────  │
│                                                │
│ [Storykandidaten]                             │
│  • Kandidaat A — status: geblokkeerd (dupl.)  │
│    ▸ Beoordeling criticus: "..."              │
│  • Kandidaat B — status: geblokkeerd (guardrail)│
│    ▸ Beoordeling criticus: "..."              │
└─────────────────────────────────────────────┘

[Regulier REJECTED/NEEDS_REVISION scherm — geen guardrail-pad, ongewijzigd]
┌─────────────────────────────────────────────┐
│ Status: [richting-verworpen]                  │
│ ── Reden ─────────────────────────────────── │
│ Eindoordeel criticus: REJECT                  │
│ Samenvatting: <bestaande tekst>               │
│ Vereiste wijzigingen: <bestaande lijst>       │
└─────────────────────────────────────────────┘

### Interactiehypotheses
- Voor iteraties die het guardrail-pad doorlopen (overall ACCEPT, alle kandidaten geblokkeerd/duplicaat) toont het Reden-blok 'Eindoordeel criticus: ACCEPT' plus de guardrail-toelichtingszin; verifieerbaar doordat een agenttest de API-respons opvraagt (criticVerdict=ACCEPT) en de gerenderde DOM-tekst hiermee matcht.
- De statusbadge en het Reden-blok bevatten nooit een onverklaarde tegenspraak: een geautomatiseerde contractcheck controleert voor elke REJECTED/NEEDS_REVISION-iteratie dat, wanneer criticVerdict=ACCEPT, de guardrail-toelichtingszin aanwezig is in de respons/DOM.
- Het bestaande DUPLICATE-testscenario in ShadowIterationEngineTest.kt kan worden uitgebreid met een assertie dat shadow_iteration.critic_verdict exact het opgeslagen overallVerdict bevat (niet de hardgecodeerde 'REJECT'); geautomatiseerd verifieerbaar via een databasequery in de test.
- Voor reguliere REJECTED-iteraties zonder guardrail-pad (overallVerdict=REJECT) blijft het Reden-blok ongewijzigd consistent; te verifiëren via regressietests op de bestaande WARNING_ONLY_REVISE- en REVISE-scenario's, waarbij geen toelichtingszin verschijnt.
- De nieuwe toelichtingszin verschijnt uitsluitend wanneer overallVerdict en afgeleide status feitelijk uiteenlopen (guardrail-pad), en nooit bij overeenstemmende waarden; te toetsen met een geautomatiseerde snapshottest over alle bekende scenario's uit ShadowIterationEngineTest.kt.

### Toegankelijkheid
- Het Reden-blok gebruikt semantische headings (bv. h3 'Reden') zodat schermlezers de sectie los van de statusbadge kunnen aankondigen.
- De guardrail-toelichtingszin krijgt een expliciet ARIA-label of role='note' zodat een schermlezer deze niet overslaat als losse alinea zonder context.
- Statusbadge en 'Eindoordeel criticus'-tekst zijn beide met tekst (niet uitsluitend kleur) onderscheiden, met een contrastratio van minimaal 4.5:1 voor normale tekst.
- Alle interactieve elementen (terug-knop, doorklik naar storykandidaat) zijn met Tab bereikbaar en hebben zichtbare focusindicatoren.
- De toelichtingszin bij het guardrail-pad wordt niet uitsluitend via een waarschuwingsicoon (⚠) gecommuniceerd; het icoon krijgt een tekstuele aria-label-equivalent ('Let op:').

### Privacy
- Het Reden-blok en de toelichtingszin bevatten uitsluitend operationele metadata van Product Factory zelf (criticusoordeel, iteratiestatus, kandidaatlabels) — geen persoonsgegevens of data van andere producten.
- De databasetestuitbreiding op ShadowIterationEngineTest.kt bevraagt alleen synthetische testdata binnen de eigen teststore, niet productie- of gebruikersdata van derden.
- Er wordt geen nieuwe logging of opslag van gebruikersidentificeerbare informatie geïntroduceerd; enkel het al bestaande criticVerdict-veld wordt correct bewaard in plaats van overschreven.

## Kritische beoordeling

**Oordeel:** ACCEPT

De drie kandidaten vormen een samenhangende, klein-en-toetsbare drieslag die precies het door de eigenaar gestelde open vraagstuk beantwoordt: het guardrail-pad in ShadowIterationEngine.kt overschrijft het echte criticusoordeel met een hardgecodeerde 'REJECT'-string in shadow_iteration.critic_verdict, wat badge en Reden-blok (opgeleverd in candidate 41) tegenstrijdig kan maken. Kandidaat 0 (fix) is minimaal, geïsoleerd tot één guardrail-branch, behoudt de afgeleide status REJECTED en herstelt alleen het opgeslagen verdict — dit voldoet aan de kwaliteitsregel dat een wijziging uitlegt waarom het huidige gedrag zo was (guardrail wil status afdwingen, maar verliest daarbij per ongeluk het brondata-oordeel) en in isolatie beoordeelbaar/terugdraaibaar is. Kandidaat 1 verankert deze fix met een concrete, al bestaande testcase-uitbreiding. Kandidaat 2 is correct afhankelijk gemaakt van kandidaat 0 en voegt uitsluitend tekstuele, toegankelijke duiding toe zonder de bestaande badge-classificatie te wijzigen. Alle drie zijn volledig agent-uitvoerbaar: geen handmatige test, mensbesluit, accountaanmaak of externe actie is vereist, en verificatie loopt via bestaande/uit te breiden geautomatiseerde tests. Bronvermelding is overal gebaseerd op eigen broncode met concrete regelnummers, geen aannames. Geen privacy- of toegankelijkheidsproblemen: kandidaat 2 expliciteert tekstuele (niet uitsluitend kleur/icoon) communicatie, in lijn met bestaande WCAG AA-stijl van de app.
- **INFO · SCOPE** — Kandidaat 0 noemt het risico dat andere codepaden mogelijk stilzwijgend vergelijken met de letterlijke string 'REJECT' op critic_verdict, maar dit staat alleen in 'risks', niet als expliciet acceptatiecriterium. Aanbevolen om deze grep-controle als harde acceptatie-eis op te nemen zodat de implementerende agent dit niet kan overslaan.
- **INFO · CONSISTENCY** — Kandidaat 0 laat historische, al opgeslagen iteraties met de foutieve hardgecodeerde waarde bewust ongecorrigeerd (geen backfill). Dit is een expliciete, beargumenteerde scope-keuze en geen blokkerend probleem, maar de eigenaar zal deze oude iteraties dus nog steeds inconsistent zien tonen na de fix.
- **INFO · SCOPE** — Kandidaat 2 is functioneel afhankelijk van kandidaat 0 (zonder de fix heeft de conditie geen effect); de dependsOn-relatie is correct vastgelegd, dus dit is geen blokkade, alleen een aandachtspunt voor uitvoeringsvolgorde.

## Geaccepteerde storykandidaten

### Bewaar het echte criticus-eindoordeel in plaats van een hardgecodeerde 'REJECT'-waarde in het guardrail-pad van ShadowIterationEngine.kt

_Sleutel: `preserve-real-critic-verdict-guardrail`_

In ShadowIterationEngine.kt (regels 178-188) roept de code, wanneer het overall criticusoordeel `verdict`=='ACCEPT' is maar de lijst `accepted` leeg is (alle kandidaten duplicate/geblokkeerd), `repository.markReviewed(iteration.id, "REJECT", "REJECTED")` aan met een hardgecodeerde string 'REJECT' in plaats van de daadwerkelijke waarde van `verdict` ('ACCEPT'). Deze waarde komt terecht in de kolom `shadow_iteration.critic_verdict` (ShadowIterationApi.kt regel 441-450) en wordt via `ShadowIterationView.criticVerdict` (Contracts.kt regel 131) aan de frontend blootgesteld. Omdat het reeds gepubliceerde 'Reden'-blok (candidate 41) dit veld direct toont, kan het huidige gedrag leiden tot een onjuiste weergave van het criticusoordeel. Deze story past uitsluitend deze ene guardrail-branch aan: in plaats van de hardgecodeerde string 'REJECT' wordt de werkelijke waarde van de lokale variabele `verdict` doorgegeven aan `markReviewed`, zodat `critic_verdict` altijd het daadwerkelijke oordeel van de criticus bevat, terwijl de afgeleide iteratiestatus 'REJECTED' (het tweede argument) ongewijzigd blijft. Geen nieuw databaseveld, geen schema-migratie, geen wijziging aan andere markReviewed-aanroepen (REVISE/WARNING_ONLY_REVISE-paden) die al de echte `verdict`-waarde doorgeven.

**Acceptatiecriteria**
- Wanneer het criticus-overallVerdict 'ACCEPT' is maar alle kandidaten individueel duplicate of geblokkeerd zijn (guardrail-pad in ShadowIterationEngine.kt), bevat de opgeslagen `shadow_iteration.critic_verdict` na de fix de waarde 'ACCEPT', niet de string 'REJECT'.
- De afgeleide iteratiestatus voor dit pad blijft ongewijzigd 'REJECTED' (het tweede argument van markReviewed wijzigt niet).
- Voor alle overige bestaande markReviewed-aanroepen (REVISE-, WARNING_ONLY_REVISE- en reguliere REJECT-paden) blijft `critic_verdict` exact de reeds daadwerkelijk doorgegeven waarde bevatten; er treedt geen regressie op in deze paden.
- De wijziging is beperkt tot de guardrail-branch (huidige regels 178-188) in ShadowIterationEngine.kt: geen nieuw databaseveld, geen nieuwe API-respons-property, geen wijziging aan Contracts.kt of ShadowIterationApi.kt.
- Bestaande, niet aan dit pad gerelateerde unit- en integratietests van ShadowIterationEngine blijven slagen na de wijziging.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationApi.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationApi.kt), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory-contracts/src/main/kotlin/nl/vdzon/productfactory/contracts/Contracts.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory-contracts/src/main/kotlin/nl/vdzon/productfactory/contracts/Contracts.kt), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/test/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngineTest.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/test/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngineTest.kt)

Risico's: Historische, al opgeslagen iteraties met de foutieve hardgecodeerde 'REJECT'-waarde worden niet met terugwerkende kracht gecorrigeerd (geen backfill in scope); deze blijven het oude, incorrecte oordeel tonen totdat een nieuwe guardrail-pad-iteratie optreedt., Als andere, nog niet geïdentificeerde codepaden stilzwijgend aannemen dat `critic_verdict` bij status REJECTED altijd letterlijk 'REJECT' is, kan deze fix daar een onverwacht neveneffect hebben; de implementerende agent moet dit vooraf geautomatiseerd controleren door te zoeken naar vergelijkingen met de letterlijke string 'REJECT' op dit veld.

### Voeg expliciete assertie op criticVerdict toe aan het bestaande DUPLICATE-testscenario in ShadowIterationEngineTest.kt

_Sleutel: `test-critic-verdict-duplicate-scenario`_

ShadowIterationEngineTest.kt bevat al een DUPLICATE-scenario (regels 79-91) dat het guardrail-pad test (overall ACCEPT, alle kandidaten duplicate) en verifieert dat de iteratiestatus 'REJECTED' wordt, maar verifieert bewust niet de waarde van `critic_verdict` voor dit specifieke geval — in tegenstelling tot de REVISE- en WARNING_ONLY_REVISE-scenario's (regels 97 en 120), die dat wel doen. Deze story breidt uitsluitend het bestaande DUPLICATE-testscenario uit met een expliciete assertie dat de opgeslagen/geretourneerde `criticVerdict` gelijk is aan het werkelijke overallVerdict ('ACCEPT'), zodat de fix uit de guardrail-verdict-story geautomatiseerd bewaakt wordt en niet in een latere wijziging opnieuw kan sluipen. Er wordt geen nieuw testscenario toegevoegd en geen bestaande assertie verzwakt of verwijderd.

**Acceptatiecriteria**
- Het bestaande DUPLICATE-testscenario in ShadowIterationEngineTest.kt bevat na deze wijziging een expliciete assertie dat `critic_verdict` (of het equivalente geretourneerde veld) gelijk is aan 'ACCEPT'.
- De nieuwe assertie faalt aantoonbaar tegen het oude (pre-fix) gedrag waarbij `critic_verdict` hardgecodeerd 'REJECT' was, en slaagt tegen het gefixte gedrag — dit wordt door de implementerende agent expliciet geverifieerd/gedocumenteerd als bewijs dat de test de regressie daadwerkelijk dekt.
- De bestaande assertie dat de iteratiestatus 'REJECTED' wordt voor dit scenario blijft ongewijzigd aanwezig.
- Geen enkele andere bestaande testcase of assertie in ShadowIterationEngineTest.kt wordt gewijzigd, verzwakt of verwijderd.
- De volledige bestaande testsuite van het testbestand compileert en slaagt na de wijziging.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/test/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngineTest.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/test/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngineTest.kt), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt)

Afhankelijkheden (candidateKey): preserve-real-critic-verdict-guardrail (binnen deze batch herkend als: preserve-real-critic-verdict-guardrail)

Risico's: Als de guardrail-verdict-fix niet exact zo geïmplementeerd wordt als beschreven (bv. andere variabelenaam of structuur), moet de assertie op de daadwerkelijke, geïmplementeerde datastructuur worden gebaseerd in plaats van aangenomen namen.

### Toon een vaste toelichtingszin in het bestaande Reden-blok wanneer het criticusoordeel ACCEPT is maar de iteratie toch REJECTED is (guardrail-pad)

_Sleutel: `guardrail-explanation-in-reden-blok`_

Het in candidate 41 opgeleverde 'Reden'-blok in IterationSessionDialog (main.dart) toont bij status NEEDS_REVISION/REJECTED leesbare tekst afgeleid van het criticus-artefact, waaronder het eindoordeel. Zodra de guardrail-verdict-fix is doorgevoerd, kan `criticVerdict` legitiem 'ACCEPT' zijn terwijl de iteratiestatus 'REJECTED' is (het guardrail-pad: alle kandidaten duplicate/geblokkeerd ondanks een positief criticusoordeel). Zonder duiding zou dit voor de eigenaar als een tegenstrijdigheid op het scherm ogen. Deze story voegt aan het bestaande Reden-blok een voorwaardelijke, vaste toelichtingszin toe die uitsluitend verschijnt wanneer criticVerdict=='ACCEPT' en de iteratiestatus 'REJECTED' is: "Alle voorgestelde kandidaten zijn geblokkeerd (duplicaat of guardrail), waardoor deze cyclus niet doorgaat ondanks een positief criticusoordeel." Voor elke andere combinatie van status en criticVerdict blijft het Reden-blok exact zoals opgeleverd in candidate 41, zonder wijziging.

**Acceptatiecriteria**
- Wanneer de iteratiestatus 'REJECTED' is en criticVerdict=='ACCEPT' (guardrail-pad), toont het bestaande Reden-blok naast het eindoordeel de vaste toelichtingszin over geblokkeerde kandidaten.
- Voor alle overige REJECTED- en NEEDS_REVISION-iteraties (criticVerdict != 'ACCEPT') rendert het Reden-blok exact zoals vóór deze wijziging (candidate 41), zonder de toelichtingszin.
- De toelichtingszin is statische, vaste tekst; er wordt geen nieuw API-veld of nieuwe backendlogica toegevoegd.
- Een geautomatiseerde frontendtest (widget-/integratietest) dekt zowel het guardrail-pad-geval (toelichtingszin zichtbaar) als een regulier REJECTED-geval (toelichtingszin afwezig), en faalt als deze twee gevallen door elkaar gehaald worden.
- De toelichtingszin is tekstueel herkenbaar (bijv. voorvoegsel 'Let op:') en niet uitsluitend via kleur of icoon gecommuniceerd, conform de bestaande toegankelijkheidsstijl van de app.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationApi.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationApi.kt)

Afhankelijkheden (candidateKey): preserve-real-critic-verdict-guardrail (binnen deze batch herkend als: preserve-real-critic-verdict-guardrail)

Risico's: Zonder de guardrail-verdict-fix zou deze story geen effect hebben, omdat criticVerdict dan nog steeds hardgecodeerd 'REJECT' is en de conditie nooit waar wordt; deze story heeft daarom weinig waarde als losstaande wijziging., Als er in de praktijk meerdere oorzaken voor het guardrail-pad bestaan (niet uitsluitend duplicate/geblokkeerd), kan de vaste toelichtingszin te specifiek of onjuist zijn voor een edge case; de implementerende agent dient dit te verifiëren tegen de daadwerkelijke code vóór implementatie.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
