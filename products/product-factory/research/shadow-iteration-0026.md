---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0026
date: 2026-08-10
status: approved
sources:
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md
  - https://api.github.com/repos/robbertvdzon/product-factory/commits?per_page=20
  - https://api.github.com/repos/robbertvdzon/product-factory/contents/docs/stories
  - https://product-factory-acceptance.vdzonsoftware.nl
  - https://github.blog/news-insights/product-news/supercharging-github-actions-with-job-summaries/
  - https://www.datadoghq.com/blog/best-practices-for-ci-cd-monitoring/
  - https://docs.github.com/en/enterprise-cloud@latest/actions/how-tos/monitor-workflows/view-workflow-run-history
---
# Productcyclus 26

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Het Product Factory-dashboard is live onderzocht (broncode op GitHub + de draaiende acceptatieomgeving via Playwright-schermafbeeldingen/a11y-snapshots). Belangrijkste bevinding: de badge-fix uit de vorige cyclus (FAILED → 'technische fout' i.p.v. misleidend 'guardrail-conflict') is inmiddels correct doorgevoerd en live gecontroleerd — al toont het eerste paint van de pagina kortstondig nog de oude badge-tekst voordat de data ververst. De twee kernpunten uit het overleg met de eigenaar van vandaag (overladen hoofdscherm; afkeuringen niet traceerbaar) zijn deels al aangepakt door vandaag geleverde stories (18-22): cyclusdetail toont nu een expliciet 'Reden'-blok, per-agentrol-status (Onderzoeker/Product owner/UX-ontwerp/Story writer/Criticus) met COMPLETED-status en tijdstempels, en expandeerbare resultaten per rol. Toch blijft het hoofdscherm nog steeds 7 vlak naast elkaar gepresenteerde secties tonen zonder hiërarchie richting de door de eigenaar genoemde drie kernacties, en voor het geval waarin een cyclus stopt vóórdat de criticus draait (NEEDS_REVISION zonder criticVerdict) blijft de 'Reden' beperkt tot 'Criticus-oordeel ontbreekt voor deze cyclus' zonder de onderliggende oorzaak te noemen. Agentresultaten worden bovendien nog als ruwe JSON-syntax (accolades/aanhalingstekens) rond overigens al leesbare tekst getoond.

### Badge-fix FAILED→'technische fout' is live correct, met kortstondige stale-flash bij eerste paint

classification.dart op main mapt status FAILED nu naar het neutrale label 'technische fout' (paars, WCAG AA-kleurenpaar) i.p.v. het eerder misleidende 'guardrail-conflict'; REJECTED blijft ongewijzigd op 'richting-verworpen'. Dit is live geverifieerd op de acceptatieomgeving: cyclus shadow-hkh-autopilot-0002 (status FAILED) toont na volledige laadtijd het badge 'technische fout' met Foutreden 'Workspace-publicatie tijdelijk niet beschikbaar (previewdata, gesimuleerd)', consistent met de opdracht uit iteratie 25. Bij een eerste screenshot, genomen vóór volledige data-verversing, toonde dezelfde badge echter nog kortstondig de oude tekst 'guardrail-conflict' — een mogelijke stale-cache- of laadvolgorde-flash die het eerste, snelle blikcontact van de eigenaar kort kan misleiden.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### Cyclusdetail toont nu expliciet 'Reden'-blok en per-agentrol-voortgang

De cyclusdetail-dialoog (bijv. shadow-hkh-autopilot-0001, ACCEPTED) toont een 'Voortgang'-sectie met elke agentrol (Onderzoeker, Product owner, UX-ontwerp, Story writer, Criticus) als los, tijdgestempeld item met status COMPLETED, en een expandeerbaar 'Resultaat en onderbouwing'-paneel per rol. Voor NEEDS_REVISION-cyclus shadow-hkh-autopilot-0003 toont de dialoog een apart 'Reden'-blok ('Criticus-oordeel ontbreekt voor deze cyclus') direct onder de badge, vóór de voortgangssectie. Dit is een directe, zichtbare invulling van de eerder door de eigenaar gevraagde traceerbaarheid ('een afkeuring zonder zichtbare reden mag niet kunnen bestaan').

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://api.github.com/repos/robbertvdzon/product-factory/contents/docs/stories](https://api.github.com/repos/robbertvdzon/product-factory/contents/docs/stories)

### Reden bij ontbrekend criticusoordeel blijft oppervlakkig: geen onderliggende oorzaak

Voor cyclus shadow-hkh-autopilot-0003 (NEEDS_REVISION) draaide alléén de Onderzoeker (COMPLETED) met resultaat 'Onvoldoende gedateerde bronnen beschikbaar voor een sluitende tijdlijn', maar de criticus draaide nooit. Het getoonde 'Reden'-blok zegt enkel 'Criticus-oordeel ontbreekt voor deze cyclus' — dit benoemt wélk onderdeel ontbreekt, maar niet waaróm de pipeline daar stopte (bewuste short-circuit op basis van het onderzoeksresultaat, een timeout, of iets anders). Dit is precies het type 'wat i.p.v. waarom'-leemte die de eigenaar in het overleg van vandaag benoemde.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### Hoofdscherm toont nog steeds 7 vlakke secties zonder hiërarchie richting de drie kernacties

Het hoofdscherm (Productoverzicht) toont achtereenvolgens: statuscijfers, Producten, Productcycli en onderzoekssessies, Software Factory-stories, Overleggen, Storywachtrij, en Workspace — zeven secties met vergelijkbaar visueel gewicht. De drie acties die de eigenaar vandaag expliciet als kern noemde (nieuwe cyclus starten, cyclusuitkomsten zien, voortgekomen stories zien) zijn wel aanwezig maar niet visueel onderscheiden van de overige, meer technische secties (Storywachtrij, Workspace).

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### Agentresultaten nog als ruwe JSON-syntax gepresenteerd ondanks eerdere humaniseringsstories

Het expandeerbare 'Resultaat en onderbouwing'-paneel voor de Onderzoeker-rol toont de tekst nog letterlijk omringd door JSON-syntax: '{ "findings": "Onvoldoende gedateerde bronnen beschikbaar voor een sluitende tijdlijn." }' — de waarde zelf is leesbaar Nederlands, maar de accolades en veldnaam-aanhalingstekens blijven zichtbaar, ondanks dat stories #16 en #17 (JSON-veldnamen humaniseren; top-level string/lijstvelden apart tonen) al zijn geleverd.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://api.github.com/repos/robbertvdzon/product-factory/contents/docs/stories](https://api.github.com/repos/robbertvdzon/product-factory/contents/docs/stories)

### 8 stories in één dag geleverd (product-factory-15 t/m 22), direct gericht op badge/reden-duidelijkheid

De GitHub-commitgeschiedenis toont dat op 2026-08-10 acht stories (product-factory-15 t/m product-factory-22) zijn samengevoegd, stuk voor stuk gericht op leesbaarheid van cyclusuitkomsten: van 'verplaats ruwe JSON achter...' (15) en 'pure functie voor JSON-veldnamen' (16), via 'toon direct zichtbaar Reden-blok bij NEEDS_REVISION' (18) en 'bewaar het echte criticus-eindoordeel' (19), tot de badge-fix zelf (22). Dit bevestigt dat de traceerbaarheidsrichting uit eerdere iteraties al actief en snel wordt doorgevoerd, niet alleen besproken.

Bronnen: [https://api.github.com/repos/robbertvdzon/product-factory/commits?per_page=20](https://api.github.com/repos/robbertvdzon/product-factory/commits?per_page=20), [https://api.github.com/repos/robbertvdzon/product-factory/contents/docs/stories](https://api.github.com/repos/robbertvdzon/product-factory/contents/docs/stories)

### Software Factory-stories en Workspace-publicaties zijn leeg in de acceptatiedataset

De stats-balk op het hoofdscherm toont '0 Workspace-publicaties' en '0 Software Factory-stories', en de sectie 'Software Factory-stories' toont expliciet 'Nog geen stories naar de Software Factory gestuurd'. Hierdoor kan in deze acceptatieomgeving niet worden gecontroleerd hoe een daadwerkelijk verzonden/gepubliceerde story of een overleg-naar-cyclus-koppeling in de UI wordt weergegeven.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### Huidige applicatie

**Doel:** Het Product Factory-dashboard is de interface waarmee de eigenaar (Robbert) autonome productcycli start en inspecteert voor de twee geregistreerde producten: Product Factory zelf en hkh-autopilot. Kerngebruik, expliciet bevestigd in het overleg van vandaag: (1) een nieuwe cyclus starten, (2) zien wat eerdere cycli hebben opgeleverd (geaccepteerd/afgewezen/needs-revision, met reden), (3) de daaruit voortgekomen Software Factory-stories bekijken, en (4) een 'overleg' (chat) voeren met de product-AI waarvan de uitkomst wordt meegenomen in de volgende cyclus.

**Wat ontbreekt:**
- Het hoofdscherm toont nog steeds 7 vrijwel gelijkwaardige secties (stats, Producten, Productcycli, Software Factory-stories, Overleggen, Storywachtrij, Workspace) zonder visuele hiërarchie richting de drie kernacties die de eigenaar vandaag expliciet noemde.
- Bij een NEEDS_REVISION-cyclus waarvan de criticus nooit draaide, blijft het 'Reden'-blok beperkt tot 'Criticus-oordeel ontbreekt voor deze cyclus' — dit zegt wélk onderdeel ontbreekt, niet waaróm de pipeline vóór de criticus stopte.
- Bij het eerste paint van de pagina toont de FAILED-badge kortstondig nog de oude, inmiddels gecorrigeerde tekst 'guardrail-conflict' voordat deze ververst naar 'technische fout' — een mogelijke stale-cache-flash tijdens een snelle blik.
- Agentresultaten (bv. Onderzoeker-bevindingen) worden nog steeds omringd door zichtbare ruwe JSON-syntax (accolades, veldnaam-aanhalingstekens) in plaats van volledig als leesbare platte tekst, ondanks eerder geleverde humaniseringsstories.
- De koppeling tussen een gehouden overleg en de opdracht van een daaropvolgende cyclus is niet te verifiëren in deze acceptatieomgeving, omdat het enige overleg in de dataset nog leeg is ('Nog geen berichten').

### Verbetermogelijkheden

- Herstructureer het hoofdscherm rond de drie door de eigenaar genoemde kernacties (nieuwe cyclus starten, cyclusuitkomsten zien, voortgekomen stories zien) door deze visueel te promoten boven secundaire/technische secties zoals Workspace en Storywachtrij-interne details, bijvoorbeeld via een primair 'boven de vouw'-blok en een ingeklapt 'details'-gebied voor de rest.
- Verrijk het 'Reden'-blok voor NEEDS_REVISION-cycli zonder criticusoordeel met de concrete aanleiding van de vroegtijdige stop (bv. verwijzing naar de Onderzoeker-bevinding die tot stoppen leidde, of een expliciete vermelding 'gestopt vanwege onvoldoende onderzoeksresultaat' vs. 'gestopt door timeout'), zodat 'waarom' ook beantwoord is wanneer er geen formeel criticusoordeel is.
- Onderzoek de kortstondige stale-badge-flash bij het eerste paint (mogelijk client-side cache/race tussen initiële render en databinding) zodat de eerste weergave direct de juiste classificatie toont.
- Maak de 'Resultaat en onderbouwing'-weergave af door JSON-veldwaarden als pure leesbare tekst te tonen zonder omringende accolades/aanhalingstekens, in lijn met de al ingezette richting van stories #13-#17.
- Verifieer, zodra er een niet-lege testdataset met daadwerkelijke Software Factory-stories en workspace-publicaties beschikbaar is, hoe de koppeling 'cyclus → story' en 'overleg → beïnvloedde cyclus' in de UI wordt getoond — dit kan nu niet worden vastgesteld met de huidige (lege) acceptatiedata.

### Inspiratiebronnen

- [GitHub Actions workflow run summary page (job-per-stap status + expandeerbare samenvatting)](https://github.blog/news-insights/product-news/supercharging-github-actions-with-job-summaries/) — Vergelijkbaar patroon als het bestaande per-agentrol-voortgangspaneel in Product Factory (Onderzoeker/Product owner/UX-ontwerp/Story writer/Criticus als losse 'jobs' met status en expandeerbaar resultaat); bruikbaar referentiepunt voor hoe zo'n paneel verder leesbaar te maken zonder ruwe JSON.
- [GitHub Actions workflow run history overzicht](https://docs.github.com/en/enterprise-cloud@latest/actions/how-tos/monitor-workflows/view-workflow-run-history) — Toont hoe een lijst van eerdere runs met status, duur en directe doorklik naar reden/detail wordt gestructureerd — relevant voor het herinrichten van de 'Productcycli en onderzoekssessies'-lijst op het Product Factory-hoofdscherm.
- [CI/CD-dashboard structuur: top-level overzicht + drill-down (Datadog-praktijken)](https://www.datadoghq.com/blog/best-practices-for-ci-cd-monitoring/) — Onderbouwt het scheiden van een compact top-level statusoverzicht van technische drill-down-details, wat direct aansluit bij de wens van de eigenaar om drie kernacties snel te zien zonder tussenliggende technische info.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart) | 2026-08-10 | Publieke GitHub-repository (robbertvdzon/product-factory), geen expliciete LICENSE-bestand aanwezig (404); broncode geraadpleegd als eigen productbron, niet herverspreid. | Directe bron voor de status-naar-badge-mapping en kleurdefinities die eerdere iteraties wilden corrigeren; nodig om te verifiëren of de FAILED→'technische fout'-fix daadwerkelijk in main staat. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md) | 2026-08-10 | Publieke GitHub-repository, geen expliciete licentie; geraadpleegd als eigen productdocumentatie. | Geeft de officiële doelomschrijving van Product Factory (autonome productcyclus-orchestrator die stories aanbiedt aan de Software Factory) als basis voor currentState.purpose. |
| [bron](https://api.github.com/repos/robbertvdzon/product-factory/commits?per_page=20) | 2026-08-10 | GitHub REST API, publieke, niet-geauthenticeerde read-only opvraging van commitmetadata van een publieke repository. | Toont de meest recente commitgeschiedenis (o.a. de 8 vandaag samengevoegde stories) om vast te stellen wat er sinds de vorige iteratie daadwerkelijk is opgeleverd. |
| [bron](https://api.github.com/repos/robbertvdzon/product-factory/contents/docs/stories) | 2026-08-10 | GitHub REST API, publieke, niet-geauthenticeerde read-only opvraging van een publieke repository-directory. | Volledige lijst van geleverde storybestanden, gebruikt om te bepalen welke concrete stories (15 t/m 22) recent zijn doorgevoerd en waar ze over gingen. |
| [bron](https://product-factory-acceptance.vdzonsoftware.nl) | 2026-08-10 | Interne, niet-publieke acceptatieomgeving zonder login, expliciet aangewezen als onderzoeksbron door de opdrachtgever; alleen leesbaar geraadpleegd, geen wijzigingen aangebracht. | De daadwerkelijk draaiende applicatie, bezocht via Playwright om de live UI (badges, cyclusdetail, instellingen, overleg) te inspecteren zoals de eigenaar die ook zou zien. |
| [bron](https://github.blog/news-insights/product-news/supercharging-github-actions-with-job-summaries/) | 2026-08-10 | Publiek GitHub-blogartikel (github.blog), vrij toegankelijk; geraadpleegd als achtergrondbron, niet herverspreid. | Referentie voor hoe een vergelijkbaar multi-stap pipeline-overzicht (per-job status + expandeerbare samenvatting) elders wordt vormgegeven, als inspiratie voor het per-agentrol-voortgangspaneel. |
| [bron](https://www.datadoghq.com/blog/best-practices-for-ci-cd-monitoring/) | 2026-08-10 | Publiek toegankelijk blogartikel van Datadog; geraadpleegd als achtergrondbron over dashboardstructuur, niet herverspreid. | Onderbouwt de aanbeveling om een top-level overzicht (aantallen/uitkomsten) te scheiden van drill-down detailschermen, relevant voor het herstructureren van het overladen hoofdscherm. |
| [bron](https://docs.github.com/en/enterprise-cloud@latest/actions/how-tos/monitor-workflows/view-workflow-run-history) | 2026-08-10 | Officiële, publiek toegankelijke GitHub-documentatie; geraadpleegd als achtergrondbron, niet herverspreid. | Aanvullende inspiratiebron voor hoe workflow-/pipeline-geschiedenis met status en reden leesbaar wordt gepresenteerd in een vergelijkbaar multi-run overzicht. |

## Productbeslissing

Zet de al ingezette traceerbaarheids- en leesbaarheidslijn (stories #15-#22) door met twee kleine, losstaand toetsbare verbeteringen aan de cyclusdetailweergave: (1) het 'Reden'-blok bij een NEEDS_REVISION-cyclus zonder criticusoordeel toont voortaan de daadwerkelijke onderliggende stopoorzaak in plaats van alleen te melden wat ontbreekt, en (2) het resultaatpaneel per agentrol toont agentresultaten als volledig platte, leesbare tekst zonder omringende JSON-syntax. Beide wijzigingen raken alleen de weergavelaag van het Product Factory-dashboard, niet de onderliggende data, migraties, authenticatie of de koppeling met de Software Factory, en zijn elk afzonderlijk te beoordelen en terug te draaien.

**Waarom:** Het overleg met de eigenaar van vandaag noemde expliciet twee knelpunten: een overladen hoofdscherm en niet-traceerbare afkeuringen. Live onderzoek bevestigt dat traceerbaarheid al sterk verbeterd is (Reden-blok, per-rol status, badge-fix) maar op twee punten nog oppervlakkig blijft: het Reden-blok bij ontbrekend criticusoordeel benoemt niet de echte oorzaak, en agentresultaten tonen nog zichtbare JSON-restjes ondanks eerdere humaniseringsstories. Dit zijn de kleinste, meest samenhangende en direct doorzetbare verbeteringen binnen de reeds gevalideerde richting; de grotere hoofdscherm-herstructurering en de nog onbegrepen badge-flash zijn bewust niet gekozen omdat ze breder oppervlak raken of eerst onderzoek vereisen, in lijn met de productprincipes 'klein en toetsbaar' en 'eerst begrijpen, dan wijzigen'.

### Prioriteiten
- Reden-blok bij ontbrekend criticusoordeel moet de daadwerkelijke stopoorzaak benoemen, niet alleen wat ontbreekt
- Verwijder resterende ruwe JSON-syntax rond agentresultaten en rond de humanisering van stories #15-#17 af
- Wijzigingen blijven beperkt tot de weergavelaag van het Product Factory-dashboard; geen wijziging aan andere producten of aan de Software Factory-koppeling
- Elke wijziging legt uit waarom het huidige gedrag zo was voordat het wordt aangepast
- Grotere hoofdscherm-herstructurering en onderzoek naar de badge-flash worden bewust uitgesteld tot een volgende cyclus

### Besluiten
- **Verrijk het 'Reden'-blok bij een NEEDS_REVISION-cyclus zonder criticusoordeel met de daadwerkelijke onderliggende stopoorzaak (bv. 'gestopt omdat de Onderzoeker onvoldoende bronnen vond' vs. 'gestopt door timeout'), in plaats van alleen te melden dat het criticusoordeel ontbreekt.** — Live onderzoek op de acceptatieomgeving toont dat cyclus shadow-hkh-autopilot-0003 als Reden enkel 'Criticus-oordeel ontbreekt voor deze cyclus' geeft, terwijl de Onderzoeker wél een concreet resultaat opleverde ('Onvoldoende gedateerde bronnen beschikbaar'). Dit is precies het 'wat i.p.v. waarom'-gebrek dat de eigenaar in het overleg van vandaag benoemde over niet-traceerbare afkeuringen.
- **Rond de humanisering van agentresultaten af door de resterende ruwe JSON-syntax (accolades, veldnaam-aanhalingstekens) rond de tekst in het 'Resultaat en onderbouwing'-paneel te verwijderen, zodat alleen platte leesbare tekst overblijft.** — Ondanks dat stories #15-17 (JSON-veldnamen humaniseren, top-level velden apart tonen) al zijn geleverd, toont het Onderzoeker-resultaatpaneel op de acceptatieomgeving nog letterlijk '{ "findings": "..." }' rond een overigens leesbare Nederlandse tekst. Dit is een kleine, geïsoleerde afronding van een reeds ingezette en gevalideerde richting, geen nieuwe richting.
- **Neem de herstructurering van het hoofdscherm (7 vlakke secties) en het onderzoek naar de kortstondige badge-flash bij eerste paint nog niet mee in deze cyclus; behandel ze als apart, later te onderzoeken/ontwerpen werk.** — Beide raken breder oppervlak (visuele hiërarchie van het hele dashboard, resp. een nog onbegrepen client-side cache/render-race) en zijn daarmee niet 'klein en in isolatie beoordeelbaar' zoals de productprincipes vereisen; het principe 'eerst begrijpen, dan wijzigen' vraagt om onderzoek vóór een fix bij de badge-flash.

## UX-voorstel: Cyclusdetail — traceerbare stopreden en platte agentresultaten

**Gebruikersdoel:** Als producteigenaar wil ik in de cyclusdetailweergave direct en zonder interpretatie zien waaróm een cyclus zonder criticusoordeel is gestopt (NEEDS_REVISION), en de resultaten per agentrol als platte leesbare tekst kunnen lezen, zodat ik een afkeuring kan vertrouwen zonder ruwe JSON-syntax te hoeven ontcijferen.

### Flow
1. Eigenaar opent het Product Factory-hoofdscherm en ziet de lijst 'Productcycli en onderzoekssessies'.
2. Eigenaar klikt op een cyclus met badge NEEDS_REVISION (bv. shadow-hkh-autopilot-0003); de cyclusdetail-dialoog opent (modal, focus verplaatst naar dialoogtitel).
3. Direct onder de badge toont het 'Reden'-blok niet enkel 'Criticus-oordeel ontbreekt', maar de onderliggende stopoorzaak: welke rol als laatste voltooide, diens resultaat-samenvatting, en dat de pipeline daarna bewust stopte (geen timeout).
4. Eigenaar scrolt naar 'Voortgang' en ziet per agentrol (Onderzoeker/Product owner/UX-ontwerp/Story writer/Criticus) status en tijdstempel; rollen die niet draaiden tonen expliciet 'NIET GESTART' i.p.v. te ontbreken.
5. Eigenaar klikt/toetst Enter op 'Resultaat en onderbouwing' bij een voltooide rol (aria-expanded togglet); het paneel klapt open en toont de bevinding als platte tekst zonder omringende accolades of veldnaam-aanhalingstekens.
6. Eigenaar sluit de dialoog via de 'Sluiten'-knop of Escape-toets; focus keert terug naar de aanklikbare cyclusrij in de lijst.

### Wireframe

[Cyclusdetail-dialoog] (modal, role="dialog", aria-modal="true", focus-trap, Esc sluit, focus keert terug naar trigger)

┌───────────────────────────────────────────────────┐
│ Cyclus: shadow-hkh-autopilot-0003            [Sluiten] │
│ Badge: ⬤ NEEDS_REVISION  (paars/wit, WCAG AA-contrast) │
│                                                     │
│ Reden                                              │
│ ┌─────────────────────────────────────────────────┐│
│ │ Gestopt na de stap 'Onderzoeker': "Onvoldoende   ││
│ │ gedateerde bronnen beschikbaar voor een sluitende││
│ │ tijdlijn." De pipeline is op basis van dit       ││
│ │ resultaat vroegtijdig gestopt; Criticus is niet  ││
│ │ gestart (geen timeout, geen technische fout).    ││
│ └─────────────────────────────────────────────────┘│
│                                                     │
│ Voortgang (verticale stappenlijst, elk item is een │
│ toggle-knop met aria-expanded)                     │
│  ● Onderzoeker     COMPLETED   10:03   [▾ tonen]   │
│    └ Resultaat en onderbouwing (uitgeklapt):       │
│      Onvoldoende gedateerde bronnen beschikbaar    │
│      voor een sluitende tijdlijn.                  │
│      (platte tekst — geen { }, geen "veld": )      │
│  ○ Product owner    NIET GESTART                   │
│  ○ UX-ontwerp        NIET GESTART                   │
│  ○ Story writer      NIET GESTART                   │
│  ○ Criticus           NIET GESTART                   │
│                                                     │
│                                        [Sluiten]    │
└───────────────────────────────────────────────────┘

Statusoverzicht (ter vergelijking, ongewijzigd gedrag):
- ACCEPTED / REJECTED / FAILED tonen hun bestaande Reden-tekst ongewijzigd; alleen het NEEDS_REVISION-zonder-criticus-pad en de resultaatpanelen worden aangepast.

### Interactiehypotheses
- Voor elke NEEDS_REVISION-cyclus zonder criticusoordeel bevat het Reden-blok de naam van de laatst voltooide agentrol én diens resultaat-samenvatting, en is de tekst niet meer gelijk aan de oude generieke string 'Criticus-oordeel ontbreekt voor deze cyclus'; geautomatiseerd toetsbaar via een tekst-assertie op de gerenderde dialoog.
- Het 'Resultaat en onderbouwing'-paneel bevat voor elke voltooide rol geen JSON-syntaxtekens ({, }, aanhalingstekens rond veldnamen) in de zichtbare tekst; geautomatiseerd toetsbaar door de gerenderde tekst te scannen op afwezigheid van de patronen '{', '}' en '":'.
- Cycli met status ACCEPTED, REJECTED of FAILED tonen na deze wijziging exact dezelfde Reden-tekst als vóór de wijziging (regressietest via snapshotvergelijking), zodat alleen het NEEDS_REVISION-zonder-criticus-pad verandert.
- De volledige cyclusdetail-dialoog, inclusief het Reden-blok en het uitklappen van resultaatpanelen, is met uitsluitend het toetsenbord te bedienen (Tab/Shift+Tab/Enter/Escape) en aria-expanded wisselt correct tussen true/false; geautomatiseerd toetsbaar met een toetsenbord-navigatietest en axe/a11y-scan.

### Toegankelijkheid
- Dialoog krijgt role="dialog" en aria-modal="true", met focus-trap; focus gaat bij openen naar de dialoogtitel en keert bij sluiten terug naar de rij die de dialoog opende.
- Elk 'Resultaat en onderbouwing'-paneel is een knop met aria-expanded en een unieke aria-controls-relatie naar het uitklapbare paneel, zodat schermlezers de open/dicht-status aankondigen.
- Badgekleuren (o.a. het bestaande paars voor 'technische fout'/NEEDS_REVISION) behouden minimaal WCAG AA-contrast (4.5:1) tussen tekst en achtergrond.
- Reden-blok staat in de leesvolgorde direct na de badge, vóór de Voortgang-lijst, zodat schermlezergebruikers de stopoorzaak als eerste horen na de status.
- Rollen die niet gestart zijn krijgen een tekstuele status 'NIET GESTART' (geen enkel visueel icoon-only signaal), zodat de informatie niet uitsluitend op kleur of vorm steunt.
- Alle interactieve elementen (Sluiten-knop, toggle-knoppen per rol) zijn bereikbaar via Tab in logische volgorde en bedienbaar met Enter/Spatie.

### Privacy
- Het Reden-blok en de resultaatpanelen tonen uitsluitend operationele metadata van Product Factory zelf (cyclusstatus, agentrol, tijdstempel, onderzoeksresultaat-samenvatting); geen persoonsgegevens of gebruikersdata van andere producten worden verwerkt of getoond.
- Bij het verrijken van de stopoorzaak mag geen technische foutdetail (bv. stacktrace, interne tokens, API-sleutels) uit onderliggende logs letterlijk in het Reden-blok terechtkomen; alleen de al bestaande, voor mensen bedoelde resultaat-samenvatting van de rol wordt hergebruikt.
- Het verwijderen van JSON-syntax rond agentresultaten verandert alleen presentatie, niet de onderliggende opgeslagen data; er wordt geen extra data verzameld, gelogd of naar externe systemen verstuurd.

## Kritische beoordeling

**Oordeel:** ACCEPT

Beide kandidaten zijn goed onderbouwd met live-onderzoek op de acceptatieomgeving en verwijzingen naar de daadwerkelijke broncode (classification.dart, main.dart, docs/stories), bouwen expliciet en zonder overlap voort op reeds gepubliceerde candidates (41 resp. 37-40), en zijn strikt beperkt tot de presentatielaag van het Product Factory-dashboard: geen backend-, schema-, database- of HKH Autopilot-wijziging. Beide voldoen aan de autonomie-gate: alle acceptatiecriteria zijn geautomatiseerd toetsbaar (tekst-assertie, snapshotvergelijking, patroonscan op JSON-syntax) en vereisen geen handmatig productbesluit, accountaanmaak of andere actie van de eigenaar — waar onzekerheid bestaat (bv. of een bewuste stop van een timeout te onderscheiden is, of de werkelijke oorzaak van de zichtbare JSON-syntax) wordt de agent expliciet geïnstrueerd dit eerst te documenteren en zich te beperken tot wat met zekerheid uit bestaande data volgt, in plaats van te gokken of een menselijk besluitmoment te vereisen. Privacy is niet in het geding (uitsluitend operationele Product Factory-metadata). Er zijn geen blokkerende issues; twee kleine WARNING-punten zijn het overwegen waard maar houden de kandidaten niet tegen.
- **WARNING · SCOPE** — Candidate 1 erkent in 'risks' dat de werkelijke oorzaak van de zichtbare JSON-syntax buiten de frontend-renderlaag kan liggen (bv. een stale/oudere build op de acceptatieomgeving, vergelijkbaar met de apart gesignaleerde badge-flash bij eerste paint), maar dit is niet als formeel acceptatiecriterium vastgelegd — alleen als risico genoemd. Zonder een expliciet criterium dat de agent bij een niet-frontend oorzaak moet rapporteren i.p.v. de scope stilzwijgend te vergroten, is de scope-begrenzing minder hard afdwingbaar dan bij andere candidates.
- **WARNING · CONSISTENCY** — Candidate 0 laat de exacte formulering van de nieuwe Reden-tekst (rolnaam + resultaatsamenvatting) aan de implementerende agent over; er is geen expliciete eis dat deze tekst qua toon/stijl aansluit bij de reeds gepubliceerde Reden-blok-teksten uit candidate 41 en het Foutreden-blok uit candidate 33, wat tot stilistische inconsistentie tussen statussen kan leiden.
- **INFO · ACCESSIBILITY** — Beide candidates wijzigen alleen tekstuele inhoud binnen al bestaande, eerder toegankelijk gemaakte componenten (Reden-blok, roltegel-panelen); er is geen expliciete regressietoets opgenomen die bevestigt dat aria-expanded/leesvolgorde na de tekstwijziging ongewijzigd blijft. Waarschijnlijk geen probleem, maar het is goed als de implementerende agent dit kort bevestigt.

## Geaccepteerde storykandidaten

### Verrijk het Reden-blok bij NEEDS_REVISION zonder criticusoordeel met de daadwerkelijke stopoorzaak i.p.v. alleen 'ontbreekt'

_Sleutel: `reden-blok-onderliggende-stopoorzaak`_

Live onderzoek op de acceptatieomgeving toont dat cyclus shadow-hkh-autopilot-0003 (status NEEDS_REVISION, criticus nooit gestart) in het door candidate 41 opgeleverde 'Reden'-blok uitsluitend de vaste fallbacktekst 'Criticus-oordeel ontbreekt voor deze cyclus' toont, terwijl de Onderzoeker-rol wél als COMPLETED staat met een concreet resultaat ('Onvoldoende gedateerde bronnen beschikbaar voor een sluitende tijdlijn'). Dit is precies het 'wat i.p.v. waarom'-gebrek dat de eigenaar in het overleg noemde: het blok benoemt wélk onderdeel ontbreekt, niet waaróm de pipeline daar vroegtijdig stopte. Deze story bouwt voort op het al gepubliceerde Reden-blok (candidate 41) en vervangt, uitsluitend voor het specifieke geval NEEDS_REVISION zonder criticVerdict, de generieke fallbacktekst door een tekst die de naam van de laatst voltooide agentrol en een samenvatting van diens resultaat bevat. De implementerende agent inspecteert eerst geautomatiseerd de bestaande roldata (status/tijdstempel/resultaat per rol) om vast te stellen welke velden daadwerkelijk beschikbaar zijn, en documenteert of het onderliggende datamodel een bewuste stop van een timeout/technische fout kan onderscheiden; kan dat onderscheid niet betrouwbaar worden afgeleid, dan beperkt de tekst zich tot wat wél met zekerheid uit bestaande data volgt (rol + resultaat), zonder te gokken naar een oorzaak. Voor cycli waar geen enkele rol voltooide, toont het blok een aparte, expliciete fallbacktekst die dat meldt. Alle overige status/criticVerdict-combinaties (inclusief NEEDS_REVISION mét criticusoordeel, ACCEPTED, REJECTED, FAILED) blijven qua Reden-tekst exact ongewijzigd. De wijziging blijft beperkt tot de presentatielaag van IterationSessionDialog in dashboard-frontend; geen nieuw API-veld, geen backend-wijziging, geen wijziging aan HKH Autopilot.

**Acceptatiecriteria**
- Voor een cyclus met status NEEDS_REVISION en zonder criticVerdict waarbij minstens één rol COMPLETED is, toont het Reden-blok de naam van de laatst voltooide agentrol en een leesbare samenvatting van diens resultaat, in plaats van uitsluitend de string 'Criticus-oordeel ontbreekt voor deze cyclus'.
- De implementerende agent documenteert of het datamodel een bewuste stop kan onderscheiden van een timeout/technische fout; alleen indien dat betrouwbaar is vastgesteld wordt dat onderscheid expliciet in de tekst benoemd, anders blijft de tekst beperkt tot rol + resultaat zonder gegokte oorzaak.
- Voor een NEEDS_REVISION-cyclus zonder criticVerdict waarbij geen enkele rol COMPLETED is, toont het Reden-blok een aparte, expliciete fallbacktekst die dat meldt (geen lege of technisch foutieve tekst zoals 'undefined').
- Een geautomatiseerde test verifieert voor het scenario 'laatste rol Onderzoeker COMPLETED, criticus niet gestart' dat de gerenderde Reden-tekst niet meer gelijk is aan de oude generieke string en wél de rolnaam en resultaatsamenvatting bevat.
- Een geautomatiseerde regressietest/snapshotvergelijking bevestigt dat de Reden-tekst voor ACCEPTED, REJECTED, FAILED en NEEDS_REVISION-mét-criticVerdict exact ongewijzigd blijft ten opzichte van vóór deze wijziging.
- De wijziging blijft volledig beperkt tot de presentatielaag van IterationSessionDialog in dashboard-frontend; er wordt geen nieuw API-veld, database-schemaveld of wijziging aan HKH Autopilot geïntroduceerd.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://api.github.com/repos/robbertvdzon/product-factory/contents/docs/stories](https://api.github.com/repos/robbertvdzon/product-factory/contents/docs/stories), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart)

Risico's: Het onderliggende datamodel geeft mogelijk geen betrouwbaar signaal om een bewuste stop van een timeout te onderscheiden; de agent moet dit expliciet als onbevestigd documenteren in plaats van een oorzaak te verzinnen., Als de roldata voor sommige oudere/legacy-cycli ontbreekt of een ander formaat heeft, moet de fallbacktekst robuust blijven zonder crashes of lege secties.

### Verwijder resterende ruwe JSON-syntax uit het primaire 'Resultaat en onderbouwing'-paneel per agentrol

_Sleutel: `resultaatpaneel-zonder-json-syntax`_

Ondanks dat candidates 37-40 al leesbare tekst en een generieke fallback voor top-level string-/lijstvelden hebben toegevoegd, en candidate 38 de ruwe JSON al achter een 'Toon technische details'-toggle heeft verplaatst, toont het primaire 'Resultaat en onderbouwing'-paneel op de acceptatieomgeving voor cyclus shadow-hkh-autopilot-0003 (rol Onderzoeker) nog letterlijk '{ "findings": "Onvoldoende gedateerde bronnen beschikbaar voor een sluitende tijdlijn." }' inclusief accolades en veldnaam-aanhalingstekens, in plaats van alleen de platte tekst. Dit wijst op een resterende inconsistentie tussen de bedoelde (en elders al bevestigde) leesbare weergave en het daadwerkelijk live gerenderde resultaat. Deze story laat de implementerende agent eerst geautomatiseerd de actuele renderlogica inspecteren en documenteren waarom de JSON-syntax nog zichtbaar is in het primaire paneel (bijvoorbeeld: verkeerde componentvolgorde, een schema-mismatch die niet naar de generieke fallback doorschakelt, of een ander renderpad), en past vervolgens uitsluitend de renderlogica van dat primaire paneel aan zodat voor elke voltooide rol alleen platte, leesbare tekst zichtbaar is zonder omringende JSON-syntax. De reeds bestaande 'Toon technische details'-toggle (candidate 38) met de ongewijzigde ruwe JSON blijft daaronder intact beschikbaar. Voor artefacten zonder enig herkend leesbaar of fallback-bruikbaar veld verandert er niets. De wijziging blijft beperkt tot de frontend-renderlaag van Product Factory; geen wijziging aan HKH Autopilot-data of backend-schema.

**Acceptatiecriteria**
- De implementerende agent documenteert, op basis van geautomatiseerde inspectie van de huidige broncode, de concrete oorzaak waarom het primaire resultaatpaneel ondanks candidates 37-40 nog JSON-syntax rond leesbare tekst toont.
- Na de fix bevat de zichtbare tekst in het primaire 'Resultaat en onderbouwing'-paneel (buiten de 'Toon technische details'-toggle) voor elke voltooide rol geen accolades en geen aanhalingstekens direct rond een veldnaam gevolgd door een dubbele punt; dit is geautomatiseerd toetsbaar door de gerenderde tekst te scannen op deze patronen.
- De ruwe JSON blijft ongewijzigd en volledig beschikbaar achter de bestaande 'Toon technische details'-toggle uit candidate 38.
- Een geautomatiseerde test reproduceert het live waargenomen scenario (Onderzoeker-rol met findings-veld 'Onvoldoende gedateerde bronnen beschikbaar voor een sluitende tijdlijn.') en verifieert dat de primaire weergave deze tekst platgetoond bevat zonder omringende JSON-syntax.
- Artefacten zonder enig herkend leesbaar of top-level string-/lijstveld (het bestaande fallback-pad uit candidate 40) tonen na deze wijziging exact hetzelfde gedrag als vóór de wijziging.
- De wijziging blijft volledig beperkt tot de frontend-renderlaag van Product Factory (dashboard-frontend); geen wijziging aan data, schema of gedrag van HKH Autopilot.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://api.github.com/repos/robbertvdzon/product-factory/contents/docs/stories](https://api.github.com/repos/robbertvdzon/product-factory/contents/docs/stories), [https://api.github.com/repos/robbertvdzon/product-factory/commits?per_page=20](https://api.github.com/repos/robbertvdzon/product-factory/commits?per_page=20)

Risico's: De werkelijke oorzaak kan dieper liggen dan presentatie (bv. candidates 37-40 zijn wel gemerged maar niet correct uitgerold, of de acceptatieomgeving draait een oudere build); de agent moet dit onderscheiden voordat een fix wordt toegepast om geen verkeerde laag aan te passen., Als de oorzaak buiten de frontend-renderlaag blijkt te liggen (bv. build/deploy-proces), valt de fix mogelijk buiten de beoogde kleine scope van deze story en moet dat expliciet gerapporteerd worden in plaats van de scope stilzwijgend te vergroten.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
