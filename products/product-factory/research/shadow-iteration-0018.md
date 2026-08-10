---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0018
date: 2026-08-10
status: approved
sources:
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart
  - https://product-factory-acceptance.vdzonsoftware.nl
  - https://product-factory-api-acceptance.vdzonsoftware.nl/api/products
  - https://product-factory-api-acceptance.vdzonsoftware.nl/api/shadow-iterations
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/shadow-mode.md
---
# Productcyclus 18

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Onderzoek op 2026-08-10 combineerde de GitHub-broncode (dashboard-frontend/lib/main.dart), architectuurdocs en een live doorloop van de acceptatieomgeving via Playwright-screenshots. De in iteratie 17 geaccepteerde en inmiddels gepubliceerde 'leesbare rolresultaten'-fix (product-factory-12 t/m -15) is technisch gebouwd op een specifiek verwacht JSON-schema per rol (bv. researcher: summary/findings[]/currentState/sources; product_owner: productDirection/decisions[]; critic: overallVerdict/summary/issues; story_writer: candidates[]). Live doorklikken door alle drie zichtbare productcycli in de acceptatieomgeving (de enige cycli die een echte dashboardgebruiker vandaag ziet) laat zien dat geen van de vijf rolresultaten (Onderzoeker, Product owner, UX-ontwerp, Story writer, Criticus) dit schema matcht — de werkelijke content is een sterk vereenvoudigd schema (bv. {\"findings\": \"...\"} als platte string, {\"decision\": \"...\"}, {\"story\": \"...\"}, {\"verdict\", \"reason\"}). Het gevolg: de eerder als opgelost beoordeelde JSON-leesbaarheidskwestie is voor elke iteratie die een gebruiker vandaag daadwerkelijk kan bekijken nog steeds zichtbaar als rauwe, ingesprongen JSON via het veilige fallbackpad — de functie levert dus (nog) geen waarneembaar voordeel op in de praktijk. Daarnaast is een eerder gesignaleerde, nog niet opgeloste bevinding herbevestigd: de meldingstekst 'niet doorgezet (product staat niet op autonoom)' wordt getoond bij alle drie cycli, terwijl het bijbehorende product (HKH Autopilot) zichtbaar op 'autonomous' staat (bevestigd in zowel de UI als /api/products) — de tekst leidt de conclusie uitsluitend af uit het iteratieveld `mode` in plaats van de werkelijke productinstelling `developmentMode`, die elders op dezelfde pagina al beschikbaar is.

### Leesbare-rolresultaten-fix dekt het werkelijke, live geproduceerde JSON-schema niet

In dashboard-frontend/lib/main.dart (functie `_readableArtifactFields`, vanaf regel 1143) wordt per rol een vast setje veldnamen verwacht, bv. voor 'researcher': data['summary'], data['findings'] (als lijst van objecten met title/finding/sourceUrls), data['currentState'], data['sources'], data['inspiration']; voor 'product_owner': data['productDirection'], data['decisions'] (lijst met decision/rationale/sourceUrls); voor 'critic': data['overallVerdict'], data['summary'], data['issues']; voor 'story_writer': data['candidates'] (met title/description/acceptanceCriteria). Bij geen enkele match blijft `readableFields` leeg en toont de UI de volledige rauwe JSON (regel 1013-1019). Live doorgeklikt op shadow-hkh-autopilot-0001 (ACCEPTED, criticus: ACCEPT, 2 kandidaten — dus precies het soort cyclus waar een eigenaar de onderbouwing wil lezen) tonen alle vijf rolresultaten nog steeds rauwe JSON: Onderzoeker `{"findings": "Vrijwilligers waarderen foto's met herkenbare huisnummers en namen het meest."}`, Product owner `{"decision": "Prioriteer bronnen met een concrete plaats- en persoonsverwijzing."}`, Story writer `{"story": "Als bezoeker wil ik foto's op een kaart zien, zodat ik verhalen bij een plek kan ontdekken."}`, Criticus `{"verdict": "ACCEPT", "reason": "Kleine, toetsbare eerste stap met duidelijke gebruikerswaarde."}`. Dit zijn drie van de drie zichtbare shadow-iteraties in de acceptatieomgeving (0001, 0002, 0003) — er is dus momenteel geen enkele cyclus waarvoor de eerder als 'geaccepteerd' beoordeelde leesbaarheidsverbetering zichtbaar effect heeft voor de eigenaar.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### Meldingstekst over 'niet doorgezet naar Software Factory' is feitelijk onjuist voor shadow-iteraties, ondanks eerdere signalering

`_deliveryLabel(String mode)` (main.dart, regel 1399-1401) bepaalt de tekst 'niet doorgezet (product staat niet op autonoom)' uitsluitend uit `iteration['mode']` ('shadow' vs 'autonomous'), niet uit de werkelijke productinstelling. Live bevestigd op 2026-08-10: het productoverzicht toont HKH Autopilot met expliciete badge 'autonomous' (en de tekst 'Autonomous: de Product Factory mag geaccepteerde stories zelfstandig naar de Software Factory sturen'), terwijl direct daaronder alle drie cycli (waaronder de ACCEPTED iteratie 1) de tekst 'niet doorgezet (product staat niet op autonoom)' tonen. In dezelfde build-methode (rond regel 480-505 en 552-563) is de volledige `product`-map met `developmentMode` al beschikbaar naast de iteratielijst, dus een koppeling op `productSlug` is zonder API-wijziging mogelijk. Dit was al gesignaleerd in de onderzoeksbevindingen van iteratie 17, maar is niet opgevolgd in de daaropvolgende product owner-beslissing (die zich uitsluitend richtte op de JSON-leesbaarheid) en staat dus nog open.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://product-factory-api-acceptance.vdzonsoftware.nl/api/products](https://product-factory-api-acceptance.vdzonsoftware.nl/api/products)

### Product Factory bestuurt zichzelf via dezelfde motor als HKH Autopilot, met precies één geregistreerd product in deze omgeving

README.md en /api/products bevestigen dat Product Factory een zelfstandige Kotlin-applicatie is die productcycli (Onderzoeker → Product owner → UX-ontwerp → Story writer → Criticus) draait voor elk geregistreerd product en geaccepteerde stories aanbiedt aan de Software Factory, zonder zelf productcode te bouwen. In de acceptatieomgeving is precies één product geregistreerd (HKH Autopilot, status 'active', developmentMode 'autonomous'); het dashboard dat hier wordt beoordeeld is Product Factory's eigen bedieningsinterface voor die producten, niet een apart 'product-factory'-product in dezelfde lijst.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md), [https://product-factory-api-acceptance.vdzonsoftware.nl/api/products](https://product-factory-api-acceptance.vdzonsoftware.nl/api/products)

### Huidige applicatie

**Doel:** Product Factory is een zelfstandige Kotlin-applicatie die voor elk geregistreerd product autonome productcycli draait (Onderzoeker → Product owner → UX-ontwerp → Story writer → Criticus), storykandidaten bijhoudt en geaccepteerde stories aanbiedt aan de Software Factory. Dit onderzochte product is Product Factory's eigen dashboard, waarmee de menselijke producteigenaar dat proces volgt en per cyclus kan zien wat er is gebeurd en waarom. In de acceptatieomgeving is precies één product gekoppeld (HKH Autopilot, autonomous/active) met drie zichtbare shadow-productcycli.

**Wat ontbreekt:**
- De in iteratie 17 geaccepteerde 'leesbare rolresultaten'-verbetering (main.dart, _readableArtifactFields) matcht een vast schema per rol, maar geen van de drie live zichtbare shadow-iteraties van HKH Autopilot produceert dat schema; alle vijf rolresultaten (Onderzoeker, Product owner, UX-ontwerp, Story writer, Criticus) van elke zichtbare cyclus vallen daardoor terug op rauwe, ingesprongen JSON — de leesbaarheidsverbetering heeft dus geen waarneembaar effect voor een gebruiker die vandaag het dashboard opent.
- De meldingstekst 'niet doorgezet (product staat niet op autonoom)' wordt getoond bij alle cycli van een product dat wél op 'autonomous' staat (bevestigd via UI-badge en /api/products), omdat de tekst uitsluitend uit het iteratieveld `mode` wordt afgeleid in plaats van de werkelijke productinstelling die elders op dezelfde pagina al beschikbaar is. Dit was al eerder gesignaleerd maar nog niet opgevolgd.

### Verbetermogelijkheden

- Maak de leesbare-rolresultaten-rendering robuuster tegen schemavariatie: val niet in alles-of-niets terug op rauwe JSON wanneer de verwachte sleutels ontbreken, maar toon in elk geval de aanwezige top-level string-/lijstvelden generiek leesbaar (bv. elk primitive veld als gelabelde tekstregel), met de volledige JSON als secundaire 'Toon technische details'. Dat voorkomt dat een kleine schema-afwijking (zoals nu bij alle hkh-autopilot-cycli) de hele verbetering onzichtbaar maakt.
- Onderzoek waarom de content van hkh-autopilot's shadow-iteraties een ander (eenvoudiger) schema gebruikt dan waarop de rolresultaten-parser is gebouwd — is dit verouderde/losstaande testfixture-data in de acceptatieomgeving, of een verschil tussen productspecifieke promptversies? Dat bepaalt of de oplossing bij de frontend-parser ligt, bij de data, of bij beide.
- Laat `_deliveryLabel` de werkelijke `developmentMode` van het bijbehorende product gebruiken (beschikbaar via `productSlug`-koppeling binnen dezelfde build-methode) in plaats van alleen het iteratieveld `mode`, zodat de tekst nooit meer suggereert dat een product niet op autonoom staat terwijl dat wel zo is.

### Inspiratiebronnen

- [LangSmith trace-weergave (Details vs. Messages)](https://docs.langchain.com/langsmith/trace-deep-agents) — Eerder (iteratie 17) al gebruikt als onderbouwing voor progressive disclosure bij agentresultaten; blijft relevant nu blijkt dat de huidige implementatie fragiel is bij schemavariatie — een generieke 'toon wat er is, ongeacht exacte sleutelnamen'-aanpak sluit beter aan bij hoe zulke trace-viewers met heterogene agentoutput omgaan.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart) | 2026-08-10 | Publieke, eigen broncode van het onderzochte product (repository robbertvdzon/product-factory), geen licentiebeperking voor intern gebruik binnen dit onderzoek. | Bron van waarheid voor het daadwerkelijke renderinggedrag van de dashboard-frontend, inclusief de exacte regelnummers voor _deliveryLabel en _readableArtifactFields. |
| [bron](https://product-factory-acceptance.vdzonsoftware.nl) | 2026-08-10 | Eigen, door de opdrachtgever beheerde standing acceptatieomgeving met representatieve nepdata; geen externe rechtenbeperking. | Live verificatie van hoe het dashboard zich daadwerkelijk gedraagt voor een echte gebruiker, via Playwright-screenshots (canvas-rendering, dus geen tekst-scraping mogelijk). |
| [bron](https://product-factory-api-acceptance.vdzonsoftware.nl/api/products) | 2026-08-10 | Eigen operationele API van het onderzochte product met nepdata; geen externe rechtenbeperking. | Bevestigt de werkelijke productinstelling (developmentMode: autonomous) die de misleidende delivery-labeltekst weerspreekt. |
| [bron](https://product-factory-api-acceptance.vdzonsoftware.nl/api/shadow-iterations) | 2026-08-10 | Eigen operationele API met nepdata; geen externe rechtenbeperking. | Levert de lijst en status van alle zichtbare productcycli, gebruikt om te bepalen welke iteraties een echte gebruiker vandaag kan inzien. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md) | 2026-08-10 | Publieke, eigen documentatie van het onderzochte product. | Basis voor de omschrijving van het doel en de architectuur van Product Factory in currentState.purpose. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/shadow-mode.md) | 2026-08-10 | Publieke, eigen documentatie van het onderzochte product. | Verifieert waarom shadow-iteraties per ontwerp altijd intern blijven, relevant voor het begrijpen van de delivery-labeltekst. |

## Productbeslissing

Maak de leesbare-rolresultaten-rendering in het Product Factory-dashboard robuust tegen schemavariatie, zodat de in iteratie 17 geaccepteerde leesbaarheidsverbetering ook daadwerkelijk zichtbaar wordt voor de content die HKH Autopilot vandaag echt produceert. Vervang de alles-of-niets match op een vast, rijk schema per rol door een generieke fallback die elk top-level string- of lijstveld gelabeld en leesbaar toont, met de volledige rauwe JSON nog altijd beschikbaar (maar niet meer standaard getoond) voor content die niet generiek weer te geven is. De wijziging blijft beperkt tot de frontend-renderlaag van Product Factory zelf en raakt geen data of gedrag van HKH Autopilot.

**Waarom:** Live onderzoek toont dat de eerder als 'opgelost' beoordeelde JSON-leesbaarheidsfix in de praktijk geen enkel effect heeft: alle vijf rolresultaten in alle drie zichtbare shadow-iteraties van HKH Autopilot vallen terug op rauwe, ingesprongen JSON, omdat het werkelijke productieschema eenvoudiger is dan het schema waarop de parser is gebouwd. Dit is precies het soort stille kwaliteitsregressie die de missie van dit product ('zelfkritisch, niet zelfgenoegzaam') beoogt op te sporen: een functie die intern als afgerond gold, blijkt voor de eigenaar onzichtbaar. Een generieke, schema-tolerante fallback lost dit op zonder de bestaande rolspecifieke parsing weg te gooien, blijft volledig binnen de frontend van Product Factory (geen risico voor HKH Autopilot's data of de koppeling met de Software Factory), en is als losstaande wijziging te beoordelen en terug te draaien. De eveneens gesignaleerde delivery-labelbug is bewust niet meegenomen om de richting klein te houden, maar blijft als vervolgkandidaat vastgelegd.

### Prioriteiten
- De dashboard-weergave moet daadwerkelijk waarneembaar leesbaar zijn voor de huidige productdata, niet alleen voor een aangenomen ideaalschema
- Wijziging blijft beperkt tot de frontend-renderlaag van Product Factory zelf; geen aanraking van HKH Autopilot's data of generatielogica
- De rauwe-JSON-weergave blijft beschikbaar als expliciete fallback voor content die echt niet generiek weer te geven is
- Verandering is in isolatie te beoordelen en terug te draaien, los van de nog openstaande delivery-labelbug

### Besluiten
- **Vervang de alles-of-niets schemamatch in de rolresultaten-rendering (functie rond `_readableArtifactFields`, main.dart) door een generieke fallback: elk top-level string- of lijst-van-primitieven-veld in de JSON wordt als gelabelde, leesbare regel getoond (sleutel als label), ongeacht of het exact overeenkomt met het eerder aangenomen rijke schema per rol. De volledige rauwe JSON blijft alleen zichtbaar achter 'Toon technische details' wanneer er geen bruikbare top-level velden zijn.** — De in iteratie 17 geaccepteerde leesbaarheidsverbetering ging uit van een vast, rijk schema per rol (bv. researcher: summary/findings[]/sources). Live onderzoek op 2026-08-10 toont dat de daadwerkelijke output van HKH Autopilot's shadow-cycli een sterk vereenvoudigd schema gebruikt ({"findings": "..."}, {"decision": "..."}, {"story": "..."}, {"verdict", "reason"}). Daardoor faalt de match voor alle vijf rollen in alle drie zichtbare cycli (0001-0003) en valt de UI overal terug op rauwe, ingesprongen JSON — de eerder als opgelost beoordeelde functie levert dus nul waarneembaar voordeel op voor de huidige gebruiker. Dit is een zelfkritische correctie: de eerdere aanname over het schema klopte niet met de praktijk, en de fix wordt nu robuust gemaakt tegen schemavariatie in plaats van afhankelijk van exacte sleutelnamen.
- **Beperk deze iteratie uitsluitend tot de rendering-fallback in de dashboard-frontend; raak geen backend-promptlogica of datageneratie van HKH Autopilot aan, en laat de reeds gesignaleerde delivery-labelbug (`_deliveryLabel` gebruikt `iteration['mode']` in plaats van de werkelijke `developmentMode` van het product) bewust liggen voor een volgende, apart te beoordelen cyclus.** — De guardrails verbieden wijzigingen aan gedrag van andere producten (HKH Autopilot) en vragen extra terughoudendheid; het aanpassen van de schemabron zou de productgeneratie van HKH Autopilot raken, terwijl het probleem evengoed puur in de presentatielaag oplosbaar is. De delivery-labelbug is een op zichzelf staand, ook al gediagnosticeerd probleem in dezelfde file, maar het los meenemen zou de wijziging minder klein en minder geïsoleerd toetsbaar maken.

## UX-voorstel: Schema-tolerante leesbare rolresultaten in cyclusdetail

**Gebruikersdoel:** Als producteigenaar wil ik bij elke productcyclus per rol (Onderzoeker, Product owner, UX-ontwerp, Story writer, Criticus) direct een leesbare samenvatting zien van wat er is gebeurd en waarom — ook als de werkelijke output niet het eerder aangenomen rijke JSON-schema volgt — zodat ik nooit meer op rauwe, ingesprongen JSON stuit zonder dat dit expliciet mijn keuze is.

### Flow
1. Gebruiker opent de detailpagina van een productcyclus (shadow-iteratie) in het dashboard.
2. Gebruiker ziet vijf rolresultaat-kaarten (Onderzoeker, Product owner, UX-ontwerp, Story writer, Criticus) onder elkaar of in tabs.
3. Voor elke kaart probeert het systeem eerst het bestaande rijke rolspecifieke schema te matchen (bv. summary/findings[]/sources voor Onderzoeker); bij een match wordt de bestaande gelabelde weergave getoond (geen regressie).
4. Matcht het rijke schema niet, dan itereert het systeem over de top-level JSON-velden van het artefact en toont elk string- of lijst-van-primitieven-veld als gelabelde regel, met de JSON-sleutel omgezet naar een leesbaar label (bv. 'findings' -> 'Bevindingen', 'decision' -> 'Besluit', 'verdict' -> 'Oordeel', 'reason' -> 'Toelichting').
5. Bevat het artefact geen enkel bruikbaar top-level primitief veld (leeg object of uitsluitend geneste complexe structuren), dan toont het systeem de tekst 'Geen leesbare velden gevonden voor dit rolresultaat' met een duidelijk zichtbare toggle-knop 'Toon technische details'.
6. Gebruiker kan de toggle 'Toon technische details' bedienen (muis of toetsenbord) om alsnog de volledige rauwe, ingesprongen JSON in te zien; deze staat standaard ingeklapt wanneer een leesbare weergave beschikbaar is, en de status wordt per rolkaart onthouden tijdens het bezoek van de pagina.
7. Gebruiker navigeert via Tab/pijltoetsen of muis naar de volgende rolkaart binnen dezelfde cyclus zonder dat de paginalayout onverwacht verschuift tussen leesbare en JSON-weergave.

### Wireframe

CYCLUSDETAIL — shadow-hkh-autopilot-0001 (ACCEPTED)
============================================================
[Terug naar overzicht]   Status: ACCEPTED   Modus: shadow

--- Rolresultaat: Onderzoeker -------------------------------
  Bevindingen
    Vrijwilligers waarderen foto's met herkenbare huisnummers
    en namen het meest.
  [ Toon technische details ▾ ]  (ingeklapt, aria-expanded="false")
--------------------------------------------------------------

--- Rolresultaat: Product owner --------------------------------
  Besluit
    Prioriteer bronnen met een concrete plaats- en
    persoonsverwijzing.
  [ Toon technische details ▾ ]
--------------------------------------------------------------

--- Rolresultaat: UX-ontwerp -----------------------------------
  (voorbeeld: als top-level velden ontbreken/onbruikbaar zijn)
  Geen leesbare velden gevonden voor dit rolresultaat.
  [ Toon technische details ▸ ]  <- gebruiker klikt/Enter
    ┌──────────────────────────────────────────────┐
    │ {                                              │
    │   "layout": { "components": [ ... ] }          │
    │ }                                               │
    └──────────────────────────────────────────────┘
--------------------------------------------------------------

--- Rolresultaat: Story writer -----------------------------------
  Story
    Als bezoeker wil ik foto's op een kaart zien, zodat ik
    verhalen bij een plek kan ontdekken.
  [ Toon technische details ▾ ]
--------------------------------------------------------------

--- Rolresultaat: Criticus -----------------------------------
  Oordeel        ACCEPT
  Toelichting    Kleine, toetsbare eerste stap met duidelijke
                 gebruikerswaarde.
  [ Toon technische details ▾ ]
--------------------------------------------------------------

Legenda:
- Elke gelabelde regel = key->label mapping van een top-level
  string- of lijst-van-primitieven-veld in de artefact-JSON.
- Toggle-knop is altijd aanwezig (fallback blijft bereikbaar).
- Kleur/typografie: label vet, waarde normaal; geen kleur-only
  onderscheid tussen leesbare en technische weergave.

### Interactiehypotheses
- Voor iteraties met vereenvoudigd schema (bv. {"findings": "..."}, {"decision": "..."}, {"story": "..."}, {"verdict","reason"}) toont de UI na de wijziging voor alle vijf rollen minstens één gelabelde leesbare regel in plaats van rauwe JSON; automatisch toetsbaar door voor de drie bestaande shadow-iteraties (0001-0003) via ariaSnapshot/CDP AX-tree te controleren dat er geen ingesprongen JSON-blok als hoofdcontent zichtbaar is en er wel gelabelde tekstregels aanwezig zijn.
- Content die wel voldoet aan het oorspronkelijke rijke rolschema (bv. onderzoeker met summary/findings[]/sources) behoudt exact de bestaande rolspecifieke labels en structuur zonder regressie; toetsbaar via een golden-snapshot test op de main.dart artefactrenderer met de iteratie-17 testfixtures.
- Wanneer een top-level veld alleen geneste objecten/arrays van objecten bevat zonder herkenbare primitieve subvelden, valt het systeem terug op de tekst 'Geen leesbare velden gevonden' met zichtbare toggle in plaats van een lege of foutieve weergave; toetsbaar met een synthetische fixture die zo'n structuur bevat en assert op aanwezigheid van de fallbacktekst plus togglestatus aria-expanded=false.
- De toggle 'Toon technische details' is volledig met toetsenbord bedienbaar (focusbaar via Tab, activeerbaar met Enter/Space) en het aria-expanded-attribuut wisselt correct tussen 'false' en 'true'; automatisch toetsbaar via een toetsenbord-simulatie in Playwright die tabvolgorde en aria-status verifieert.
- Het generiek tonen van top-level velden introduceert geen onbedoelde exposure van technische sleutels als ruwe tekst zonder label-mapping voor onbekende sleutels; toetsbaar door een fixture met een niet eerder geziene sleutelnaam te renderen en te controleren dat de sleutel op zijn minst leesbaar geformatteerd wordt getoond (bv. underscore/camelCase omgezet naar spaties met hoofdletter) in plaats van rauw of ontbrekend.

### Toegankelijkheid
- Toggle 'Toon technische details' moet een <button> (of element met role=button) zijn, focusbaar via Tab en bedienbaar met Enter/Space, met aria-expanded dat de open/dicht-status correct weerspiegelt en aria-controls dat verwijst naar het JSON-blok.
- Elke gelabelde regel gebruikt semantische opmaak (bv. definitielijst dt/dd of gelabelde tekstblokken) zodat een schermlezer label en waarde als bij elkaar horend aankondigt, niet enkel via visuele vetgedrukte opmaak.
- Contrastverhouding tussen labeltekst, waardetekst en achtergrond voldoet aan WCAG AA (minimaal 4.5:1 voor normale tekst), ook binnen het ingeklapte technische-details-blok.
- Onderscheid tussen 'leesbare weergave' en 'technische details' mag niet alleen via kleur worden aangegeven; gebruik ook tekst/iconen (bv. pijl-indicator plus labeltekst 'Toon'/'Verberg') zodat kleurenblinde gebruikers en schermlezers de status begrijpen.
- Focusvolgorde tussen rolkaarten en hun toggles blijft logisch en voorspelbaar (top-naar-onder, geen focus-val) wanneer een technische-details-blok wordt in- of uitgeklapt, zodat toetsenbordgebruikers niet de plek in de pagina kwijtraken.

### Privacy
- De gerenderde content betreft uitsluitend operationele metadata van Product Factory zelf (rolresultaten over productideeën/besluiten van HKH Autopilot binnen Product Factory's eigen proces), geen persoonsgegevens van eindgebruikers van andere producten; de wijziging voegt geen nieuwe databronnen of velden toe, alleen een andere presentatie van reeds bestaande artefact-JSON.
- De generieke fallback mag geen velden tonen die expliciet als intern/geheim zijn gemarkeerd (bv. tokens, credentials) mocht een toekomstig schema die per ongeluk bevatten; scope van deze iteratie blijft beperkt tot presentatie, dus er wordt geen filtering op gevoelige sleutelnamen toegevoegd zonder expliciete latere beoordeling — dit als aandachtspunt vastleggen voor een vervolgcyclus.
- De open/dicht-status van 'Toon technische details' wordt alleen lokaal in de paginasessie bijgehouden en niet naar een analytics- of trackingsysteem gestuurd, om te voorkomen dat gebruikersgedrag rond het inzien van technische details wordt gelogd als extra metadata.
- Er wordt geen nieuwe koppeling gelegd met externe systemen of producten buiten Product Factory; de wijziging blijft volledig binnen de frontend-renderlaag en raakt geen data of gedrag van HKH Autopilot.

## Kritische beoordeling

**Oordeel:** ACCEPT

De keten (onderzoek → product owner → UX → story writer) is intern consistent en goed onderbouwd: live Playwright-verificatie op de acceptatieomgeving met concrete broncoderegels toont overtuigend aan dat de eerder als opgelost beoordeelde 'leesbare rolresultaten'-fix (iteratie 17/product-factory-37-38) in de praktijk voor alle drie zichtbare shadow-iteraties terugvalt op rauwe JSON, omdat het werkelijke productieschema eenvoudiger is dan aangenomen. De product owner kiest bewust een smalle, terugdraaibare scope (alleen frontend-renderlaag, geen wijziging aan HKH Autopilot) en stelt de reeds bekende delivery-labelbug expliciet uit naar een volgende cyclus — een redelijke, goed gemotiveerde afbakening. Beide storykandidaten zijn puur presentationeel, met volledig geautomatiseerde acceptatiecriteria (unit-, widget-/golden- en Playwright-toetsenbordtests) en zonder enige stap die een menselijk besluit, handmatige test of externe actie vereist, dus de autonomie-gate wordt gehaald. Eén aandachtspunt: de rijke toegankelijkheidseisen uit de UX-fase (semantische label/waarde-koppeling, WCAG AA-contrast) zijn niet één-op-één vertaald naar toetsbare acceptatiecriteria in kandidaat 1, wat als WARNING wordt gemarkeerd maar niet blokkeert omdat het om statische tekstweergave gaat zonder nieuwe interactieve elementen.
- **WARNING · ACCESSIBILITY** — De UX-fase specificeert expliciet semantische label/waarde-koppeling (dt/dd-achtig) en WCAG AA-contrast voor de generieke fallbackregels, maar de acceptatiecriteria van kandidaat 1 (generic-toplevel-field-fallback-rendering) bevatten geen toetsbare eis hiervoor, in tegenstelling tot het patroon in eerder gepubliceerde stories (bv. product-factory-38) die toegankelijkheid wel expliciet in de acceptatiecriteria opnemen.
- **INFO · SCOPE** — De onderliggende oorzaak (waarom HKH Autopilot's shadow-iteraties een eenvoudiger schema produceren dan waarop de rolspecifieke parser is gebouwd) wordt bewust niet onderzocht in deze iteratie, alleen als improvementOpportunity vastgelegd; dit is een redelijke scope-keuze maar betekent dat de generieke fallback een symptoom oplost, niet de dieperliggende schemamismatch.
- **INFO · CONSISTENCY** — De eerder gesignaleerde delivery-labelbug (_deliveryLabel gebruikt iteratieveld mode i.p.v. productinstelling developmentMode) wordt voor de tweede keer expliciet herkend maar wederom niet meegenomen; dit is consistent en gemotiveerd, maar verdient prioriteit in de eerstvolgende cyclus om niet structureel te blijven liggen.

## Geaccepteerde storykandidaten

### Voeg pure functie toe die JSON-veldnamen van rolresultaten omzet naar leesbare labels

_Sleutel: `readable-key-label-formatter`_

In dashboard-frontend/lib/main.dart wordt de rolresultaten-weergave (rond de bestaande artefact-renderer uit product-factory-37/38) uitgebreid met een pure, losstaande functie (bijvoorbeeld genaamd _humanizeFieldKey) die een JSON-sleutelnaam omzet naar een leesbaar label. De functie controleert eerst een kleine, in code vastgelegde lijst met bekende sleutels die live zijn waargenomen in HKH Autopilot's daadwerkelijke shadow-iteraties, namelijk findings, decision, story, verdict en reason, en geeft daarvoor een vast, leesbaar label terug. Voor elke andere sleutel valt de functie terug op generieke humanisering: onderstrepingstekens worden vervangen door spaties, camelCase-grenzen krijgen een spatie, en elk woord start met een hoofdletter, zodat een technische sleutelnaam nooit rauw of onvertaald in de UI verschijnt. Dit is een puur presentationele, losstaande hulpfunctie zonder wijziging aan bestaande rendering, data-ophaling of aan gedrag van HKH Autopilot; ze legt de basis voor de generieke fallback-rendering uit de vervolgstory.

**Acceptatiecriteria**
- Automatische unit test bevestigt dat elk van de bekende sleutels findings, decision, story, verdict en reason een vast, leesbaar label oplevert dat niet gelijk is aan de rauwe sleutelnaam en geen onderstrepingsteken of aaneengeschreven camelCase bevat.
- Automatische unit test bevestigt dat een onbekende snake_case-sleutel zoals source_urls wordt omgezet naar spatie-gescheiden, met hoofdletter beginnende woorden zoals Source Urls in plaats van rauw te worden getoond.
- Automatische unit test bevestigt dat een onbekende camelCase-sleutel zoals unexpectedFieldName wordt omgezet naar spatie-gescheiden, met hoofdletter beginnende woorden in plaats van rauw te worden getoond.
- Automatische unit test bevestigt dat de functie geen bijwerkingen heeft: identieke invoer levert altijd identieke uitvoer, geen wijziging aan state, widgets of netwerkverkeer.
- De implementerende agent inspecteert eerst geautomatiseerd de huidige staat van de artefact-renderer in main.dart na product-factory-37/38 en documenteert in de PR-beschrijving de exacte functienaam en locatie waarop wordt voortgebouwd, zodat de scope aantoonbaar op de werkelijke code is gebaseerd.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart)

Risico's: De vaste lijst met bekende sleutels dekt alleen de vandaag live waargenomen voorbeelden; nieuwe rolspecifieke sleutels die later verschijnen krijgen automatisch alleen het generieke, mogelijk minder natuurlijk klinkende label totdat de lijst wordt uitgebreid. Dit is bewust aanvaardbaar omdat de generieke fallback nooit een rauwe sleutel toont., Als de code van product-factory-37/38 sinds publicatie is gewijzigd op een manier die niet uit de broncode blijkt, kan de exacte integratieplek afwijken van de aanname in deze story; de verplichte inspectiestap in de acceptatiecriteria mitigeert dit.

### Toon top-level string- en lijstvelden van een rolresultaat generiek leesbaar wanneer het rolspecifieke schema niet matcht

_Sleutel: `generic-toplevel-field-fallback-rendering`_

Live onderzoek op 2026-08-10 toont dat alle drie zichtbare shadow-iteraties van HKH Autopilot (0001 tot en met 0003) voor alle vijf rollen een vereenvoudigd JSON-schema produceren, bijvoorbeeld een findings-veld, een decision-veld, een story-veld, of een verdict- en reason-veld als platte strings, dat niet overeenkomt met het rijke, rolspecifieke schema waarop de in product-factory-37/38 opgeleverde leesbare-tekstweergave is gebouwd, zoals summary, findings-lijst en sources voor Onderzoeker. Hierdoor valt de UI voor elke vandaag zichtbare cyclus terug op rauwe, ingesprongen JSON: de eerder opgeleverde leesbaarheidsverbetering heeft dus geen waarneembaar effect. Deze story voegt aan de bestaande artefact-renderer een generieke fallback toe: matcht het rijke rolspecifieke schema niet, dan itereert de code over de top-level velden van de artefact-JSON en toont elk veld waarvan de waarde een string is, of een lijst van uitsluitend primitieve waarden zoals strings, getallen of booleans, als een gelabelde leesbare regel, met het label afgeleid via de in de vorige story toegevoegde humaniseringsfunctie. Bevat het artefact geen enkel bruikbaar top-level string- of primitief-lijstveld, bijvoorbeeld uitsluitend geneste objecten, dan blijft het bestaande gedrag (rauwe JSON, eventueel achter de toggle uit product-factory-38) ongewijzigd: er wordt geen nieuwe lege of foutieve weergave geintroduceerd. Reeds matchende rijke rolspecifieke schema's, zoals onderzoeker met summary, findings-lijst en sources, blijven exact renderen zoals in product-factory-37/38, zonder regressie. De wijziging blijft volledig beperkt tot de frontend-renderlaag van Product Factory; er wordt geen data of gedrag van HKH Autopilot aangepast.

**Acceptatiecriteria**
- Automatische widget- of golden-test met een fixture die uitsluitend een findings-veld bevat met de tekst over vrijwilligers en herkenbare huisnummers, het live bevestigde Onderzoeker-artefact van shadow-hkh-autopilot-0001, bevestigt dat de gerenderde uitvoer een gelabelde leesbare regel bevat en geen rauw, ingesprongen JSON-blok als primaire content toont.
- Automatische widget- of golden-test met fixtures die respectievelijk alleen een decision-veld, alleen een story-veld, en een verdict- plus reason-veld bevatten (de live bevestigde voorbeelden van Product owner, Story writer en Criticus) bevestigt voor elk dat alle top-level velden als gelabelde leesbare regels verschijnen in plaats van rauwe JSON.
- Regressietest hergebruikt de bestaande testfixtures uit product-factory-37/38 voor een matchend rijk rolschema, zoals onderzoeker met summary, findings-lijst en sources, en bevestigt dat de output structureel identiek blijft aan voor deze wijziging.
- Automatische test met een fixture die uitsluitend geneste objecten of een array van objecten op top-level bevat bevestigt dat het bestaande fallbackgedrag, rauwe JSON eventueel achter de toggle uit product-factory-38, ongewijzigd blijft en er geen lege of kapotte weergave ontstaat.
- Automatische test bevestigt dat een lijstveld met gemengde of niet-primitieve elementen, zoals een lijst van objecten, niet als generieke leesbare regel wordt getoond, maar het bestaande rauwe-JSON-fallbackpad volgt.
- De implementerende agent inspecteert eerst geautomatiseerd de huidige integratie van de humaniseringsfunctie uit de voorgaande story en de exacte structuur van de artefact-renderer in main.dart en documenteert eventuele afwijkingen van deze beschrijving in de pull request.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://product-factory-api-acceptance.vdzonsoftware.nl/api/shadow-iterations](https://product-factory-api-acceptance.vdzonsoftware.nl/api/shadow-iterations)

Afhankelijkheden (candidateKey): readable-key-label-formatter (binnen deze batch herkend als: readable-key-label-formatter)

Risico's: Als het daadwerkelijke schema van rolresultaten in de toekomst arrays van objecten bevat, bijvoorbeeld gestructureerde bronvermeldingen, toont deze generieke fallback die velden bewust niet leesbaar: ze vallen terug op rauwe JSON. Dit is een expliciet aanvaarde scopebeperking, geen defect., De exacte huidige codepositie en structuur van de artefact-renderer na product-factory-37/38 is niet met zekerheid vooraf vastgesteld; de verplichte inspectiestap in de acceptatiecriteria mitigeert het risico dat de aannames in deze beschrijving afwijken van de werkelijke code., De reeds gesignaleerde, aparte bug in de delivery-labelfunctie, die het iteratieveld mode gebruikt in plaats van de werkelijke productinstelling developmentMode, wordt bewust niet meegenomen in deze story, conform de expliciete scope-keuze van de product owner deze cyclus.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
