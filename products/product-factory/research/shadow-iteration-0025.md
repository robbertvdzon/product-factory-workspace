---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0025
date: 2026-08-10
status: approved
sources:
  - https://github.com/robbertvdzon/product-factory
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/test/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngineTest.kt
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-1-Vervang-geslaagd-mislukt-indicator-door-vaste-uitkomstclassificatie-badges.md
  - https://api.github.com/repos/robbertvdzon/product-factory/commits
  - https://product-factory-acceptance.vdzonsoftware.nl
  - https://gitlab.com/gitlab-org/gitlab/-/issues/415242
---
# Productcyclus 25

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Ik heb de huidige staat vastgesteld door de broncode op GitHub (robbertvdzon/product-factory) en de live acceptatieomgeving te onderzoeken, en dit te vergelijken met de bevindingen en besluiten uit de vorige onderzoekscyclus en het overleg van vandaag. Twee eerder gemelde punten zijn inmiddels concreet opgelost: (1) de guardrail-fix die het echte criticusoordeel bewaart is doorgevoerd en met een assertie geborgd, en (2) de nieuwe 'overleg'-functie is al technisch gekoppeld aan de volgende cyclus — het meeting-dossier van vandaag stroomde via `meetings.recentOutcomes()` automatisch mee in déze onderzoeksprompt, wat precies het open verzoek van de eigenaar uit het laatste overleg beantwoordt. Twee kernpunten uit dat overleg zijn echter nog onvoldoende opgelost: het hoofdscherm toont nog steeds 7 gelijkwaardige secties zonder hiërarchie, en de traceerbaarheid van afkeuringen is deels misleidend — de badge 'guardrail-conflict' wordt voor élke technische status FAILED getoond, ook wanneer de daadwerkelijke oorzaak een pure infrastructuurfout is (live gereproduceerd), terwijl echte guardrail-afwijzingen juist een aparte status (REJECTED) en badge ('richting-verworpen') hebben. Dat is een concreet, code-bevestigd naamgevingsprobleem, geen interpretatiekwestie.

### Guardrail-fix uit vorige cyclus (echte criticusoordeel behouden) is volledig doorgevoerd en getest

ShadowIterationEngine.kt geeft in het guardrail-pad nu de echte `verdict`-waarde door aan `repository.markReviewed(...)` in plaats van de eerder hardgecodeerde string 'REJECT'. ShadowIterationEngineTest.kt (regel 82-83) verifieert dit expliciet voor het DUPLICATE-scenario: status blijft REJECTED, maar criticVerdict is nu correct 'ACCEPT'. De eerder gesignaleerde mogelijke tegenstrijdigheid tussen badge en Reden-blok is voor dit pad dus verholpen.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/test/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngineTest.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/test/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngineTest.kt)

### 'guardrail-conflict'-badge dekt ook zuiver technische fouten, niet alleen beleidsblokkades

classification.dart mapt élke status=FAILED naar het vaste label 'guardrail-conflict' (bewust getekst als 'in strijd met de regels' in story product-factory-1). Maar in ShadowIterationEngine.kt (regel 39) wordt status FAILED gezet door een generieke catch-all bij elke onverwachte exception, en ook door de weeskind-iteratie-opruiming (regels ~71, vandaag tweemaal uitgebreid met extra detectie). Dat is een andere categorie dan een echte guardrail/autonomiebeleid-afwijzing, die altijd via het aparte pad naar status REJECTED (badge 'richting-verworpen') loopt. Live gereproduceerd op shadow-hkh-autopilot-0002: badge 'guardrail-conflict' naast Foutreden 'Workspace-publicatie tijdelijk niet beschikbaar (previewdata, gesimuleerd)' — een infrastructuurfout zonder relatie tot een guardrail.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-1-Vervang-geslaagd-mislukt-indicator-door-vaste-uitkomstclassificatie-badges.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-1-Vervang-geslaagd-mislukt-indicator-door-vaste-uitkomstclassificatie-badges.md), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### Overleg-functie is technisch al gekoppeld aan de volgende onderzoekscyclus

ShadowIterationEngine.kt (regel 101) haalt `meetings.recentOutcomes(product.slug)` op en geeft dit als `meetingContext` mee aan de researchPrompt (regel 109, 617: 'EERDERE OVERLEGGEN MET DE EIGENAAR'). Dit is precies het mechanisme waarmee het overlegdossier van vandaag automatisch in déze onderzoekscyclus terechtkwam — het expliciete verzoek van de eigenaar hierover in het vorige overleg is dus al technisch opgelost, al is dit nergens in de UI zichtbaar gemaakt.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt)

### Hoofdscherm blijft 7 gelijkwaardige secties tonen ondanks expliciete eigenaarsfeedback van vandaag

Live op de acceptatieomgeving (2026-08-10, gecontroleerd na het overleg) toont het hoofdscherm nog Productoverzicht-stats, Producten, Productcycli en onderzoekssessies, Software Factory-stories, Overleggen, Storywachtrij en Workspace als visueel gelijkwaardige blokken, zonder hiërarchie tussen de drie door de eigenaar genoemde kernacties (cyclus starten, opbrengst eerdere cycli, voortgekomen stories) en de rest.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### Cyclusdetail toont per-rol voortgang en resultaat, sluit al deels aan bij de traceerbaarheidswens

De detailweergave van een geaccepteerde iteratie (shadow-hkh-autopilot-0001) toont een samenvatting, opdracht, en per rol (Onderzoeker, Product owner, UX-ontwerp, Story writer, Criticus) status en tijdstip, plus een uitklapbaar 'Resultaat en onderbouwing'-blok. Dit beantwoordt een deel van de eigenaarswens om te zien wie/wat besliste, al blijft die informatie verborgen achter een klik in plaats van zichtbaar in het lijstoverzicht zelf.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### Huidige applicatie

**Doel:** Het Product Factory-dashboard is de interface waarmee de eigenaar (Robbert) autonome productcycli start en inspecteert voor twee producten: Product Factory zelf en hkh-autopilot. Kerngebruik: (1) een nieuwe cyclus starten, (2) zien wat eerdere cycli hebben opgeleverd (geaccepteerd/afgewezen/needs-revision, met reden), (3) de daaruit voortgekomen Software Factory-stories bekijken, en sinds vandaag ook (4) een 'overleg' (chat) voeren met de product-AI waarvan de uitkomst automatisch wordt meegenomen in de volgende cyclus.

**Wat ontbreekt:**
- Het hoofdscherm toont live (2026-08-10) nog steeds 7 vrijwel gelijkwaardige secties (stats, Producten, Productcycli, Software Factory-stories, Overleggen, Storywachtrij, Workspace) zonder hiërarchie richting de drie kernacties die de eigenaar in het overleg van vandaag expliciet noemde — ondanks dat dit specifieke punt al bekend was.
- De badge 'guardrail-conflict' (status FAILED) wordt zowel gebruikt voor echte autonomiebeleid-conflicten als voor pure technische/infrastructuurfouten (onverwachte exceptions, weeskind/timeout-iteraties), terwijl die twee in de backend juist wél apart worden vastgelegd (FAILED via generieke catch-all vs. REJECTED via het guardrail-pad). Live gereproduceerd: badge 'guardrail-conflict' naast Foutreden 'Workspace-publicatie tijdelijk niet beschikbaar (previewdata, gesimuleerd)'.
- De net gebouwde badge-disclaimer ('Dit toont wat de uitkomst was, niet waarom') veronderstelt dat het label zelf neutraal is, maar 'guardrail-conflict' benoemt een specifieke (hier onjuiste) oorzaak — dat ondermijnt precies het doel van de disclaimer.
- De functionele koppeling tussen een gehouden overleg en de opdracht van de daaropvolgende cyclus (die er backend al is) is nergens zichtbaar in de UI van de cyclusdetail zelf; de eigenaar kan niet zien dát en welk overleg een cyclus heeft beïnvloed.

### Verbetermogelijkheden

- Splits de FAILED-badgecategorie in classification.dart in twee eerlijke labels: één voor zuiver technische/infrastructurele fouten (catch-all exceptions, weeskind/timeout-iteraties) en één voor echte guardrail/autonomiebeleid-conflicten — dit is een kleine, geïsoleerde wijziging in de mapping-tabel zonder backend- of schemawijziging, en lost de misleidende 'wat'-claim van de huidige badge op.
- Geef het hoofdscherm een visuele hiërarchie die de drie door de eigenaar genoemde kernacties (cyclus starten, opbrengst eerdere cycli, voortgekomen stories) laat domineren en de overige secties (Workspace, Storywachtrij, Interne storykandidaten-stat) inklapt of degradeert — dit specifieke gat is nu voor de tweede opeenvolgende onderzoekscyclus vastgesteld.
- Toon in de cyclusdetail een korte, klikbare referentie naar het overleg dat de opdracht van die cyclus heeft gevoed (de data bestaat al via `meetings.recentOutcomes`), zodat de al bestaande backend-koppeling ook zichtbaar wordt voor de eigenaar.
- Omdat weeskind-/timeout-detectie vandaag tweemaal is uitgebreid (bij opstart én periodiek), wordt dit een steeds normaler voorkomend scenario in plaats van een zeldzame uitzondering — de badge-taxonomie verdient daarom evenveel zorgvuldigheid voor dit pad als voor het guardrail-pad.

### Inspiratiebronnen

- [GitLab issue: Job failures should be distinguishable between infrastructure and build problems](https://gitlab.com/gitlab-org/gitlab/-/issues/415242) — Documenteert exact hetzelfde soort probleem (technische/infrastructuurfout vermengd met inhoudelijke/beleidsfout in één statuslabel) in een vergelijkbare CI/CD-achtige statusweergave, en onderbouwt dat een aparte categorie voor infrastructuurfouten een erkend, zinvol ontwerppatroon is.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://github.com/robbertvdzon/product-factory) | 2026-08-10 | Publieke GitHub-repository van de opdrachtgever zelf; eigen broncode, geen externe rechtenbeperking voor dit interne productonderzoek. | Bronrepository van het te onderzoeken product; nodig om de huidige staat van de code (niet aannames) vast te stellen. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt) | 2026-08-10 | Eigen broncode van de opdrachtgever, publiek via raw.githubusercontent.com; geen externe rechtenbeperking. | Bevat het guardrail-pad, de FAILED-catch-all en de meeting-context-koppeling die centraal staan in de bevindingen. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/test/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngineTest.kt) | 2026-08-10 | Eigen broncode van de opdrachtgever, publiek via raw.githubusercontent.com; geen externe rechtenbeperking. | Bevestigt dat de guardrail-fix uit de vorige cyclus daadwerkelijk met een assertie is geborgd. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart) | 2026-08-10 | Eigen broncode van de opdrachtgever, publiek via raw.githubusercontent.com; geen externe rechtenbeperking. | Definieert de vaste badge-taxonomie en de status-naar-label-mapping die de 'guardrail-conflict'-bevinding onderbouwt. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-1-Vervang-geslaagd-mislukt-indicator-door-vaste-uitkomstclassificatie-badges.md) | 2026-08-10 | Eigen productdocumentatie van de opdrachtgever, publiek via raw.githubusercontent.com; geen externe rechtenbeperking. | Legt de oorspronkelijke ontwerpkeuze en formulering ('in strijd met de regels') achter het guardrail-conflict-label vast. |
| [bron](https://api.github.com/repos/robbertvdzon/product-factory/commits) | 2026-08-10 | Publieke GitHub API-data van de eigen repository; geen externe rechtenbeperking. | Geeft een feitelijk, tijdgestempeld overzicht van recente wijzigingen (meeting-feature, sessie-auth, weeskind-detectie) sinds de vorige onderzoekscyclus. |
| [bron](https://product-factory-acceptance.vdzonsoftware.nl) | 2026-08-10 | Standing acceptatieomgeving van de opdrachtgever zelf met nepdata, geen productie; vrij toegankelijk zonder login op eigen infrastructuur. | Enige manier om de daadwerkelijke, gerenderde gebruikerservaring te beoordelen (canvas-app, dus alleen via screenshots inspecteerbaar) i.p.v. alleen de broncode te lezen. |
| [bron](https://gitlab.com/gitlab-org/gitlab/-/issues/415242) | 2026-08-10 | Publiek zichtbare GitLab-issue in een open-source projectbeheersysteem; hier alleen als naamgevings-/patroonreferentie geciteerd, geen content overgenomen. | Bevestigt dat 'infrastructuurfout vs. beleidsfout niet onderscheiden in status-UI' een erkend, generiek UX-probleem is in vergelijkbare CI/CD-achtige statusoverzichten, en dient als inspiratie voor een oplossingsrichting. |

## Productbeslissing

Deze cyclus richt zich op één kleine, geïsoleerde correctie: het foutief label 'guardrail-conflict' dat vandaag getoond wordt bij status=FAILED (onverwachte technische fouten, weeskind-/timeout-opruiming) terwijl dat label feitelijk 'in strijd met de regels' betekent en al correct gereserveerd is voor status=REJECTED (het echte guardrail-pad). De backend maakt dit onderscheid al correct en getest; het is uitsluitend een verkeerde weergave-keuze in classification.dart. De aanpak: vervang in de status-naar-badge-mapping het label voor FAILED door een neutrale, technisch-accurate tekst (bijv. 'technische fout'), zonder het REJECTED-pad, het statusschema of enige backend-logica aan te raken. Dit is klein, in isolatie beoordeelbaar en zonder gevolgen voor andere producten terug te draaien, en herstelt het eerlijkheidsdoel van de recent gebouwde badge-disclaimer. De homepage-hiërarchie en het zichtbaar maken van de overleg-cyclus-koppeling zijn wel erkend als openstaande, herhaald gesignaleerde verbeterpunten, maar worden bewust niet in deze cyclus meegenomen om de wijziging klein en toetsbaar te houden.

**Waarom:** De missie vraagt continu te toetsen of Product Factory nog begrijpelijk en betrouwbaar aanvoelt, ook zonder gemelde klacht. Het onderzoek toont code-bevestigd en live gereproduceerd aan dat de badge 'guardrail-conflict' een onjuiste oorzaak claimt bij pure technische fouten, terwijl de backend het juiste onderscheid (REJECTED vs FAILED) al maakt en test. Dat is precies het soort stil, niet-gemeld gebrek waar het productprincipe 'zelfkritisch, niet zelfgenoegzaam' om vraagt. Het principe 'klein en toetsbaar' wijst de badge-correctie aan als de te kiezen richting boven de grotere, subjectievere homepage-herstructurering: de badge-fix is een enkele mapping-regel, in isolatie te beoordelen en terug te draaien, terwijl de homepage-hiërarchie een bredere, minder eenduidig af te bakenen wijziging is die al twee cycli achtereen is gesignaleerd zonder dat er een scherp afgebakend, klein voorstel voor is. De overleg-koppeling in cyclusdetail is functioneel al opgelost in de backend en dus minder urgent dan een actief misleidend label. Onomkeerbaarheid speelt hier geen rol: er wordt niets aan data, authenticatie of levering aan de Software Factory gewijzigd, dus geen extra voorzichtigheid nodig buiten de gebruikelijke isolatie-eis.

### Prioriteiten
- Corrigeer de misleidende badge-tekst voor status=FAILED zodat een technische fout niet langer als 'guardrail-conflict' wordt getoond
- Beperk de wijziging tot de mapping-laag (classification.dart) zonder backend-, schema- of statuswijzigingen aan te raken
- Behandel de homepage-hiërarchie en de zichtbaarheid van de overleg-koppeling in cyclusdetail als aparte, latere stappen — niet in deze cyclus

### Besluiten
- **Corrigeer in classification.dart de badge-tekst voor status=FAILED: gebruik niet langer het label 'guardrail-conflict' (met betekenis 'in strijd met de regels'), maar een neutraal label voor onverwachte technische fouten, bijvoorbeeld 'technische fout'. De badge voor status=REJECTED ('richting-verworpen') blijft ongewijzigd en dekt al correct de echte guardrail-afwijzingen.** — De code toont dat backend al twee aparte statuswaarden kent voor twee wezenlijk verschillende oorzaken: REJECTED loopt via het expliciete guardrail-pad in ShadowIterationEngine.kt en wordt al correct als 'richting-verworpen' getoond; FAILED ontstaat uit de generieke catch-all bij onverwachte exceptions en uit de weeskind/timeout-opruiming, en heeft dus niets met een guardrail te maken. Toch mapt classification.dart élke FAILED-status op hetzelfde 'guardrail-conflict'-label, wat live is gereproduceerd naast een foutreden die evident een infrastructuurprobleem is, niet een regelovertreding. Dit is precies het soort 'wat i.p.v. waarom'-probleem dat de eigen product-factory-1-story wilde oplossen, en ondermijnt de nieuw gebouwde disclaimer die veronderstelt dat het label zelf neutraal is.
- **Beperk deze wijziging expliciet tot de status-naar-labeltabel in classification.dart (frontend); geen wijziging aan ShadowIterationEngine.kt, het statusschema, of enige database-/API-structuur, omdat het backend-onderscheid tussen REJECTED en FAILED al correct en getest bestaat.** — Aansluitend bij het principe 'klein en toetsbaar': de wijziging is dan in isolatie te beoordelen (één mapping-regel), te testen (bestaande statuswaarden blijven ongewijzigd, alleen de weergave verandert) en zonder moeite terug te draaien, zonder enig risico voor andere producten of voor de al werkende guardrail-fix en test (ShadowIterationEngineTest.kt) uit de vorige cyclus.

## UX-voorstel: Neutrale badge voor technische fout (status FAILED) i.p.v. 'guardrail-conflict'

**Gebruikersdoel:** Robbert wil in het cyclusoverzicht en de cyclusdetailweergave in één oogopslag correct kunnen onderscheiden of een niet-geslaagde cyclus kwam door een pure technische fout (status FAILED) of door een echte guardrail-afwijzing (status REJECTED), zodat hij nooit ten onrechte denkt dat het systeem een autonomiebeleidsregel heeft overtreden.

### Flow
1. Robbert opent het dashboard en navigeert naar de sectie 'Productcycli'.
2. Het overzicht toont per cyclus een uitkomstbadge naast de status.
3. Voor cycli met backend-status FAILED rendert het systeem nu badge-tekst 'technische fout' (neutraal, geen suggestie van regelovertreding) i.p.v. het oude 'guardrail-conflict'.
4. Voor cycli met backend-status REJECTED blijft badge 'richting-verworpen' ongewijzigd, aangezien dit het enige echte guardrail-pad is.
5. Robbert klikt op een cyclus met badge 'technische fout' en opent de detailweergave.
6. In de detailweergave ziet Robbert de bestaande Foutreden-tekst (bijv. 'Workspace-publicatie tijdelijk niet beschikbaar'), nu consistent met een neutraal label i.p.v. een misleidende beleidsclaim.
7. Robbert opent ter vergelijking een cyclus met badge 'richting-verworpen' en ziet daar de criticus-onderbouwing die wél een echte guardrail-afwijzing motiveert.
8. De bestaande badge-disclaimer-tooltip ('Dit toont wat de uitkomst was, niet waarom') blijft zichtbaar en is nu voor beide labels inhoudelijk correct.

### Wireframe

[Dashboard > Productcycli]
--------------------------------------------------
| Cyclus            | Status-badge          | (i) |
--------------------------------------------------
| shadow-hka-0022    | [technische fout]     | (i) |   <- was 'guardrail-conflict', kleur: neutraal grijs/oranje
| shadow-hka-0021    | [richting-verworpen]  | (i) |   <- ongewijzigd, kleur: rood/paars
| shadow-hka-0020    | [geaccepteerd]        | (i) |   <- ongewijzigd
--------------------------------------------------
(i) = disclaimer-tooltip: "Dit toont wat de uitkomst was, niet waarom"

[Cyclusdetail: shadow-hka-0022]
--------------------------------------------------
Badge: [technische fout]
Foutreden: "Workspace-publicatie tijdelijk niet beschikbaar (previewdata, gesimuleerd)"
--------------------------------------------------
Per rol: Onderzoeker | Product owner | UX-ontwerp | Story writer | Criticus
  status + tijdstip per rol (ongewijzigd)
--------------------------------------------------

[Cyclusdetail: shadow-hka-0021 ter vergelijking]
--------------------------------------------------
Badge: [richting-verworpen]
Foutreden/onderbouwing: criticusoordeel-tekst die de guardrail-afwijzing motiveert
--------------------------------------------------

### Interactiehypotheses
- Als status=FAILED wordt gemapt naar badge-tekst 'technische fout' i.p.v. 'guardrail-conflict', dan bevat de gerenderde badge-string voor géén enkele FAILED-testcase nog het woord 'guardrail' — verifieerbaar met een geautomatiseerde unit/golden test op classification.dart die voor alle FAILED-fixtures assert dat output niet 'guardrail' bevat en wel 'technische fout' bevat.
- De badge voor status=REJECTED blijft exact 'richting-verworpen' (geen regressie) — verifieerbaar via een bestaande of uitgebreide unit test die voor REJECTED-invoer dezelfde output-string retourneert als vóór de wijziging.
- In alle bestaande seed-/testfixtures correleert de badge-tekst 1-op-1 met de onderliggende status-enum (FAILED->'technische fout', REJECTED->'richting-verworpen', overige statussen ongewijzigd) — controleerbaar door een agent die de API-respons of gerenderde acceptatieomgeving doorloopt en elk status+badge-paar tegen de mappingtabel valideert.
- De accessible name (semantics-label) van de FAILED-badge bevat 'technische fout' en niet 'guardrail' of 'regel' — controleerbaar via de Flutter-Web a11y-inspectietechniek (flt-semantics-placeholder click + ariaSnapshot + CDP AX tree) op de gerenderde badge-node.
- De disclaimer-tooltiptekst blijft ongewijzigd aanwezig en toetsenbord-bereikbaar (Tab/Enter) naast zowel de FAILED- als REJECTED-badge — verifieerbaar via geautomatiseerde toetsenbordnavigatietest die focus-volgorde en tooltip-zichtbaarheid controleert.

### Toegankelijkheid
- Badge-tekst 'technische fout' moet als accessible name/semantics-label beschikbaar zijn voor schermlezers, niet uitsluitend als visuele tekst of kleur.
- Kleurcodering mag niet het enige onderscheidende signaal zijn tussen 'technische fout' en 'richting-verworpen'; het tekstlabel moet in alle gevallen aanwezig en voorleesbaar zijn.
- Contrastverhouding tussen badge-tekst en achtergrondkleur moet minimaal WCAG AA (4.5:1) zijn, geautomatiseerd te controleren met een contrastcheck-tool op de gebruikte kleurwaarden.
- Focusvolgorde en toetsenbordbediening (Tab/Enter) naar badge en disclaimer-tooltip blijven ongewijzigd en volledig operabel zonder muis.

### Privacy
- De wijziging betreft uitsluitend een frontend-labelmapping (classification.dart) en introduceert geen verwerking van persoonsgegevens of gebruikersdata van andere producten.
- Foutreden-teksten blijven ongewijzigd en beperkt tot operationele metadata van Product Factory zelf (cyclus-status, technische foutmelding); alleen het bijbehorende badge-label verandert.
- Er wordt geen extra logging, opslag of doorgifte van data toegevoegd; de wijziging raakt geen backend-, schema- of database-laag.
- Foutreden-strings mogen geen stack traces of interne systeeminformatie (zoals hostnamen) bevatten; deze cyclus wijzigt die strings niet, dus bestaande privacywaarborgen blijven intact.

## Kritische beoordeling

**Oordeel:** ACCEPT

Eén kandidaat is voorgelegd: het vervangen van het misleidende badge-label 'guardrail-conflict' door een neutraal 'technische fout' voor status FAILED in classification.dart. De onderbouwing is solide en code-verankerd (concrete regelverwijzingen in classification.dart en ShadowIterationEngine.kt, live gereproduceerd op de acceptatieomgeving op shadow-hkh-autopilot-0002), de wijziging is expliciet beperkt tot de frontend-mappinglaag zonder backend/schema-impact, en de acceptatiecriteria zijn volledig agent-uitvoerbaar (unit-/goldentests, grep-inspectie naar overige kGuardrailConflict-verwijzingen, geautomatiseerde WCAG AA-contrastcheck, en de reeds bekende Flutter-Web a11y-inspectietechniek voor de accessible name). Er is geen overlap met bestaande PUBLISHED-kandidaten en geen stap vereist die een menselijk besluit, handmatige test, accountaanmaak of vergelijkbare eigenaarsactie noodzaakt. De kandidaat voldoet aan bronnen-, privacy-, toegankelijkheids- en kwaliteitseisen en bevat geen blokkerende issues.
- **INFO · SCOPE** — De kandidaat lost alleen de labelverwarring voor status FAILED op; een verdere opsplitsing tussen catch-all-exceptions en weeskind-/timeout-opruiming (beide nu nog samen 'technische fout') is bewust buiten scope, conform de expliciete productbeslissing om de wijziging klein te houden. Dit is een terechte afbakening, geen gebrek.
- **INFO · ACCESSIBILITY** — De keuze van het exacte kleurenpaar voor de nieuwe 'technische fout'-categorie wordt aan de implementerende agent overgelaten; dit is aanvaardbaar zolang de agent zelf WCAG AA-contrast (4.5:1) verifieert zoals in de acceptatiecriteria vastgelegd.

## Geaccepteerde storykandidaten

### Vervang badge-label 'guardrail-conflict' door neutraal 'technische fout' voor status FAILED

_Sleutel: `technische-fout-badge-voor-failed-status`_

In dashboard-frontend/lib/classification.dart mapt de tabel `kBekendeStatuswaardenPerCategorie` de backend-status FAILED naar de classificatiecategorie `kGuardrailConflict`, waarvan het badge-label 'in strijd met de regels' claimt (zie docs/stories/product-factory-1). De backend kent echter al een correct, apart en getest onderscheid: status REJECTED ontstaat uitsluitend via het echte guardrail-pad in ShadowIterationEngine.kt en wordt al terecht als `kRichtingVerworpen` ('richting-verworpen') getoond, terwijl status FAILED ontstaat uit een generieke catch-all bij onverwachte exceptions en uit de weeskind-/timeout-opruiming — een zuiver technische oorzaak zonder relatie tot een autonomiebeleidsregel. Live gereproduceerd op shadow-hkh-autopilot-0002: badge 'guardrail-conflict' naast Foutreden 'Workspace-publicatie tijdelijk niet beschikbaar (previewdata, gesimuleerd)'. Dit ondermijnt het doel van de al gebouwde badge-disclaimer ('Dit toont wat de uitkomst was, niet waarom'), omdat het label zelf een onjuiste oorzaak claimt. Deze story voegt in classification.dart een nieuwe, neutrale classificatiecategorie toe (bijvoorbeeld `kTechnischeFout` met badge-tekst 'technische fout' en een eigen WCAG AA-conform kleurenpaar, consistent met de bestaande vijf categorieën), past de mapping voor FAILED aan zodat deze naar de nieuwe categorie wijst in plaats van naar `kGuardrailConflict`, en laat de mapping voor REJECTED (`kRichtingVerworpen`) ongewijzigd. De implementerende agent grept eerst geautomatiseerd naar alle overige verwijzingen naar `kGuardrailConflict` (widgets, tests, golden-bestanden) om te bepalen of deze categorie na de wijziging ongebruikt is en dus veilig verwijderd kan worden, of dat ze bewust behouden blijft; deze bevinding wordt gedocumenteerd. De wijziging blijft volledig beperkt tot de status-naar-badge-mappinglaag in classification.dart (frontend); er wordt geen backend-, schema-, database- of API-wijziging aangebracht, en het statusschema (FAILED/REJECTED/ACCEPTED/NEEDS_REVISION/QUEUED/RUNNING) blijft ongewijzigd.

**Acceptatiecriteria**
- classification.dart bevat een nieuwe classificatiecategorie-constante (bv. kTechnischeFout) met badge-tekst 'technische fout' en een WCAG 2.1 AA-conform voorgrond/achtergrond-kleurenpaar (contrastratio minimaal 4.5:1 voor normale tekst), analoog aan de bestaande vijf categorieën.
- In kBekendeStatuswaardenPerCategorie wijst de sleutel FAILED naar de nieuwe categorie kTechnischeFout in plaats van naar kGuardrailConflict; dit is geverifieerd met een geautomatiseerde unit-/goldentest.
- De mapping voor REJECTED naar kRichtingVerworpen ('richting-verworpen') blijft exact ongewijzigd, geverifieerd met een (uitgebreide of bestaande) regressietest die voor REJECTED-invoer dezelfde outputstring retourneert als vóór de wijziging.
- classifyIterationOutcome() retourneert voor elke FAILED-testfixture een badge-string die het woord 'technische fout' bevat en niet het woord 'guardrail' bevat; dit is afgedwongen met een nieuwe of uitgebreide automatische testcase.
- De mappings voor ACCEPTED (kRichtingGekozen) en NEEDS_REVISION/QUEUED/RUNNING (kOnderzoekOnvoldoende) blijven ongewijzigd, geverifieerd met bestaande of uitgebreide regressietests.
- De accessible name/semantics-label van de FAILED-badge bevat 'technische fout' en niet 'guardrail' of 'regel', gecontroleerd via de Flutter-Web a11y-inspectietechniek (flt-semantics-placeholder click + ariaSnapshot + CDP AX tree) op de gerenderde badge-node in de acceptatieomgeving.
- De bestaande disclaimer-tooltip ('Dit toont wat de uitkomst was, niet waarom') blijft ongewijzigd aanwezig en toetsenbord-/schermlezerbereikbaar (Tab/Enter) bij zowel de FAILED- als de REJECTED-badge.
- De implementerende agent documenteert het resultaat van de grep naar overige verwijzingen naar kGuardrailConflict (widgets, tests, golden-bestanden) en past die consistent aan (verwijderen indien ongebruikt, behouden en updaten indien nog elders gerefereerd), zonder de backend, het statusschema of de database te wijzigen.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationEngine.kt), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-1-Vervang-geslaagd-mislukt-indicator-door-vaste-uitkomstclassificatie-badges.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-1-Vervang-geslaagd-mislukt-indicator-door-vaste-uitkomstclassificatie-badges.md), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

Risico's: Als kGuardrailConflict elders in de codebase (widgets, tests, golden-bestanden) nog wordt gerefereerd los van de FAILED-mapping, kan het zonder de voorgeschreven grep-stap per ongeluk kapot gaan of dubbel blijven bestaan; de acceptatiecriteria dwingen deze inspectie daarom expliciet af., Bestaande unit-/golden-tests die letterlijk op de string 'guardrail-conflict' voor FAILED-fixtures assert-en, falen na deze wijziging totdat ze bijgewerkt zijn naar 'technische fout'; dit is voorzien in de acceptatiecriteria maar vraagt zorgvuldige, volledige test-inventarisatie door de implementerende agent., Het nieuwe kleurenpaar voor 'technische fout' moet onafhankelijk op WCAG AA-contrast gecontroleerd worden; hergebruik van een bestaand, niet-goedgekeurd kleurenpaar zou de toegankelijkheidseis stilzwijgend kunnen schenden.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
