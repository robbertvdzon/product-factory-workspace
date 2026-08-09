---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0017
date: 2026-08-09
status: approved
sources:
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart
  - https://api.github.com/repos/robbertvdzon/product-factory/commits
  - https://product-factory-acceptance.vdzonsoftware.nl
  - https://product-factory-api-acceptance.vdzonsoftware.nl/api/shadow-iterations
  - https://product-factory-api-acceptance.vdzonsoftware.nl/api/products
  - https://www.nngroup.com/articles/progressive-disclosure/
  - https://docs.langchain.com/langsmith/trace-deep-agents
---
# Productcyclus 17

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Onderzoek op 2026-08-09 bevestigt eerst dat de in iteratie 14 gekozen richting volledig is opgeleverd: product-factory-12 (foutreden bij FAILED) en product-factory-13 (classificatiebadge in het detaildialoog) zijn gemerged en live geverifieerd op shadow-hkh-autopilot-0002/-0003 in de acceptatieomgeving. Bij het doorlopen van diezelfde detaildialogen is een nieuw, in de broncode bevestigd gebruiksprobleem gevonden: elk agentresultaat (Onderzoeker, Product owner, UX-ontwerp, Story writer, Criticus) wordt getoond als ruwe, ingesprongen JSON-tekst (main.dart, `_prettyJson`/`ExpansionTile`, regels 990-1051), terwijl elders in dezelfde app (storykandidaat-dialoog) vergelijkbare inhoud al wél volledig leesbaar wordt weergegeven. De bestaande 'Samenvatting voor jou' dekt dit niet af: het API-veld `summary` is alleen gevuld bij geaccepteerde iteraties en `null` bij NEEDS_REVISION/FAILED (bevestigd via /api/shadow-iterations), precies de gevallen waarin de eigenaar de meeste uitleg nodig heeft. Extern onderzoek bij Nielsen Norman Group (progressive disclosure) en LangSmith's Details/Messages-weergavepatroon levert gevalideerde, direct vergelijkbare inspiratie voor hoe technische agentdata leesbaar én toegankelijk secundair getoond kan worden zonder informatie te verliezen.

### Elk agentresultaat in het detaildialoog wordt als ruwe, ingesprongen JSON getoond, niet als leesbare tekst

In dashboard-frontend/lib/main.dart worden de resultaten van elke agentstap (Onderzoeker, Product owner, UX-ontwerp, Story writer, Criticus) binnen IterationSessionDialog gerenderd via een ExpansionTile met daarin `SelectableText(_prettyJson('${artifact['contentJson']}'))` (regels 990-1004); `_prettyJson` (regels 1045-1051) doet niets anders dan `JsonEncoder.withIndent('  ').convert(jsonDecode(value))`. Live bevestigd op shadow-hkh-autopilot-0003 (status NEEDS_REVISION): het uitgeklapte 'Onderzoeker'-blok toont letterlijk `{
  "findings": "Onvoldoende gedateerde bronnen beschikbaar voor een sluitende tijdlijn."
}` inclusief accolades en aanhalingstekens, in plaats van de tekst 'Onvoldoende gedateerde bronnen beschikbaar voor een sluitende tijdlijn.' zelf. Bij rollen met meer velden (bv. Product owner met decisions/rationale/sourceUrls, of Criticus met issues/candidateReviews, zoals te zien in de eerdere-iteraties-context van dit onderzoek) wordt dit een aanzienlijk grotere, geneste JSON-structuur.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://product-factory-api-acceptance.vdzonsoftware.nl/api/shadow-iterations](https://product-factory-api-acceptance.vdzonsoftware.nl/api/shadow-iterations)

### De 'Samenvatting voor jou' dekt alleen de uitkomst, niet de per-rol onderbouwing, en is niet altijd aanwezig

Er bestaat al een leesbare samenvattingskaart bovenaan het dialoog (main.dart regel 861-888, label 'Samenvatting voor jou'), maar deze komt uit het API-veld `summary` op iteratieniveau, dat alleen gevuld is bij (in dit geval) de ACCEPTED-iteratie shadow-hkh-autopilot-0001 ('Onderzoek en ontwerp voor een kaartweergave met foto-pins zijn afgerond en geaccepteerd.') en `null` is bij de NEEDS_REVISION- en FAILED-iteraties (0003 en 0002), rechtstreeks bevestigd via /api/shadow-iterations. Voor precies de iteraties waar de eigenaar het meest wil weten waarom iets niet doorging, ontbreekt dus zowel de samenvatting als een leesbare onderbouwing per rol — alleen de ruwe JSON is beschikbaar.

Bronnen: [https://product-factory-api-acceptance.vdzonsoftware.nl/api/shadow-iterations](https://product-factory-api-acceptance.vdzonsoftware.nl/api/shadow-iterations), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart)

### Foutreden en classificatiebadge in het detaildialoog zijn inmiddels opgelost (iteratie 14, stories 12 en 13)

De twee in iteratie 14 goedgekeurde en aan de Software Factory geleverde stories zijn beide gemerged en live actief: product-factory-12 (commit 3d508887, PR #46) voegt een 'Foutreden'-blok toe dat `iteration['errorMessage']` toont bij status FAILED (main.dart regel 896-925), en product-factory-13 (commit 6ef6da62, PR #47) toont de bestaande `ClassificationBadge` in de kop van het detaildialoog (main.dart regel 836-842). Live geverifieerd: op shadow-hkh-autopilot-0002 (FAILED) toont het dialoog nu zowel de badge 'guardrail-conflict' als de tekst 'Workspace-publicatie tijdelijk niet beschikbaar (previewdata, gesimuleerd).' onder 'Foutreden'.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://api.github.com/repos/robbertvdzon/product-factory/commits](https://api.github.com/repos/robbertvdzon/product-factory/commits)

### Storykandidaat-detaildialoog toont wél al volledig leesbare tekst — inconsistentie binnen dezelfde app

Ter vergelijking: het detaildialoog van een storykandidaat in de wachtrij ('Kaartweergave met foto-pins', hkh-autopilot iteratie 1) toont titel, omschrijving, acceptatiecriteria en criticus-beoordeling volledig als leesbare, opgemaakte tekst zonder enige JSON-notatie — dit bevestigt dat leesbare weergave elders in dezelfde applicatie al de norm is, en dat de ruwe-JSON-weergave in het iteratie-detaildialoog een inconsistentie is binnen de eigen app, niet een onvermijdelijke technische beperking.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### Huidige applicatie

**Doel:** Product Factory is het systeem dat autonome productontwikkeling faciliteert: het draait onderzoeks-/beslissingscycli (Onderzoeker → Product owner → UX-ontwerp → Story writer → Criticus) per gekoppeld product (nu: HKH Autopilot), houdt storykandidaten en hun status bij, en levert geaccepteerde stories aan de Software Factory. Dit specifieke product (Product Factory zelf) is het dashboard waarmee de menselijke producteigenaar dat proces volgt, bijstuurt (instellingen, autonome modus, cyclustijden) en per cyclus/iteratie kan doorklikken naar wat er precies is gebeurd en waarom.

**Wat ontbreekt:**
- De iteratie-detaildialoog (IterationSessionDialog) toont de resultaten van elke agentrol (Onderzoeker, Product owner, UX-ontwerp, Story writer, Criticus) als ruwe, met JsonEncoder.withIndent geformatteerde JSON-tekst in een SelectableText-blok (main.dart, functie _prettyJson, regels 990-1004, 1045-1051), in plaats van als leesbare tekst — terwijl de productvisie expliciet vraagt om leesbaarheid 'vanuit wie het dashboard daadwerkelijk gebruikt, niet vanuit wat intern het makkelijkst te bouwen is'.
- Er bestaat wél een korte 'Samenvatting voor jou' (main.dart regel 861-888), maar die is optioneel (alleen gevuld bij bepaalde afgeronde iteraties — bevestigd in /api/shadow-iterations: summary is null bij NEEDS_REVISION en FAILED, alleen gevuld bij ACCEPTED) en dekt niet de per-rol onderbouwing (bv. waarom de Criticus 'REVISE' gaf, wat de Onderzoeker precies vond) die alleen als ruwe JSON in de uitklapbare rol-tegels te vinden is.
- De eerder geconstateerde gaten uit iteratie 14 (ontbrekende foutreden bij FAILED, ontbrekende classificatiebadge in het detaildialoog) zijn beide bevestigd opgelost: live geverifieerd op shadow-hkh-autopilot-0002/-0003 en in de broncode (main.dart regel 836-842 toont ClassificationBadge, regel 896-925 toont het Foutreden-blok).

### Verbetermogelijkheden

- Vervang, of vul aan naast, de ruwe _prettyJson-weergave per agentrol door leesbare, veldspecifieke tekst (bv. voor Onderzoeker: 'findings' als lopende tekst; voor Product owner: elke 'decision' met zijn 'rationale' als leesbare alinea's; voor Criticus: 'overallVerdict' en 'summary' als leesbare tekst, 'issues' als lijst) — analoog aan hoe het storykandidaat-dialoog dit al doet, zodat de app intern consistent wordt.
- Overweeg, in lijn met het LangSmith-patroon (technische 'Details' naast leesbare 'Messages'), de ruwe JSON niet te verwijderen maar als secundaire/technische weergave te behouden (bv. achter een 'Toon technische details'-schakelaar) zodat niets verloren gaat voor wie het wél nodig heeft, terwijl de standaardweergave leesbaar is — dit sluit aan bij de NN/g-richtlijn om frequent benodigde informatie primair te tonen en secundaire/technische details pas op verzoek.
- Onderzoek of het API-veld `summary` (nu alleen gevuld bij afgeronde/geaccepteerde iteraties) ook bij NEEDS_REVISION en FAILED een korte, leesbare samenvatting kan bevatten, zodat de bestaande 'Samenvatting voor jou'-kaart consistent verschijnt ongeacht uitkomst, in plaats van dat de eigenaar bij een mislukte cyclus meteen op ruwe JSON stuit.

### Inspiratiebronnen

- [LangSmith (LangChain) — Details view vs. Messages view voor agent traces](https://docs.langchain.com/langsmith/trace-deep-agents) — Toont hetzelfde onderliggende probleem in een vergelijkbaar domein (AI-agent-observability-dashboard): een technische, volledige 'Details'-weergave van de trace bestaat naast een leesbare 'Messages'-weergave die alleen relevante vraag/antwoord/tool-uitkomst in gewone taal toont. Direct toepasbaar patroon voor Product Factory's rol-uitklaptegels.
- [Nielsen Norman Group — Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/) — Onderbouwt methodisch waarom en hoe je gedetailleerde/technische inhoud (zoals ruwe agent-JSON) achter een secundaire, duidelijk gelabelde weergave plaatst terwijl de primaire weergave beperkt en leesbaar blijft — relevant kader om de verbetermogelijkheden hierboven te motiveren.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart) | 2026-08-09 | Eigen repository van de opdrachtgever (robbertvdzon/product-factory), geen open-sourcelicentie vermeld in de GitHub-repositorymetadata; geraadpleegd als interne broncode via de publieke raw-GitHub-URL voor dit productonderzoek. | Primaire broncode van het dashboard; bevat de exacte rendering-logica (_prettyJson, ExpansionTile, IterationSessionDialog) die de kernbevinding over ruwe JSON-weergave bevestigt. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart) | 2026-08-09 | Eigen repository van de opdrachtgever, geen open-sourcelicentie vermeld; publieke raw-GitHub-URL. | Bevat ClassificationBadge en classifyIterationOutcome, gebruikt om te bevestigen dat de in iteratie 14 besloten badge-hergebruik correct en volledig is doorgevoerd. |
| [bron](https://api.github.com/repos/robbertvdzon/product-factory/commits) | 2026-08-09 | Publieke GitHub API van eigen repository, geen aparte licentie; gebruikt als feitelijke commitgeschiedenis. | Bevestigt dat product-factory-12 en -13 (uit iteratie 14) daadwerkelijk gemerged en gedeployed zijn (commits 3d508887 en 6ef6da62, PR #46/#47), zodat dit onderzoek niet opnieuw een al opgelost gat rapporteert. |
| [bron](https://product-factory-acceptance.vdzonsoftware.nl) | 2026-08-09 | Standing acceptatieomgeving van de opdrachtgever met representatieve nepdata, geen productieomgeving; geraadpleegd via headless Chromium/Playwright zoals voorgeschreven, geen persoonsgegevens verwerkt. | Live-verificatie van het daadwerkelijke gebruikersgedrag: bevestigt zowel de opgeloste foutreden/badge-weergave als de nieuwe bevinding (ruwe JSON in rol-uitklaptegels) en de leesbare weergave in het storykandidaat-dialoog, via schermafbeeldingen. |
| [bron](https://product-factory-api-acceptance.vdzonsoftware.nl/api/shadow-iterations) | 2026-08-09 | Interne API van de acceptatieomgeving van de opdrachtgever, gesimuleerde/nepdata; publiek bereikbaar zonder login voor deze standing testomgeving. | Levert de exacte, ongefilterde API-respons (status, errorMessage, summary, mode) die de bevindingen over wanneer 'summary' wel/niet gevuld is, en over het per-iteratie mode-veld, feitelijk onderbouwt. |
| [bron](https://product-factory-api-acceptance.vdzonsoftware.nl/api/products) | 2026-08-09 | Interne API van de acceptatieomgeving van de opdrachtgever, gesimuleerde/nepdata; publiek bereikbaar zonder login. | Gebruikt om te controleren of de weergave 'niet doorgezet (product staat niet op autonoom)' een inconsistentie was; bevestigde dat dit een correcte historische snapshot per iteratie is (developmentMode is later dan de seed-iteraties op autonomous gezet), dus geen bug. |
| [bron](https://www.nngroup.com/articles/progressive-disclosure/) | 2026-08-09 | Publiek toegankelijk artikel van Nielsen Norman Group, © NN/g; vrij te raadplegen redactionele UX-content, niet vrij te herpubliceren. | Gevalideerde, gezaghebbende UX-bron over het tonen van technische/gedetailleerde inhoud aan gebruikers via secundaire, uitklapbare weergaven zonder de primaire leesbaarheid te verliezen — direct relevant voor hoe agentresultaten leesbaar én toegankelijk getoond kunnen worden. |
| [bron](https://docs.langchain.com/langsmith/trace-deep-agents) | 2026-08-09 | Publieke productdocumentatie van LangChain/LangSmith, © LangChain; vrij raadpleegbaar als documentatie, geen hergebruikslicentie geclaimd. | Concreet vergelijkbaar dashboardpatroon voor AI-agentresultaten: een technische 'Details'-weergave naast een leesbare 'Messages'-weergave, wat direct als inspiratie dient voor een leesbare rol-samenvatting naast de bestaande ruwe data in Product Factory. |

## Productbeslissing

Maak het iteratie-detaildialoog (IterationSessionDialog in dashboard-frontend/lib/main.dart) intern consistent met het al bestaande storykandidaat-dialoog: toon het resultaat van elke agentrol (Onderzoeker, Product owner, UX-ontwerp, Story writer, Criticus) primair als leesbare, veldspecifieke tekst in plaats van als ruwe, ingesprongen JSON (_prettyJson). De bestaande ruwe JSON-weergave blijft behouden, maar verplaatst naar een secundaire, expliciet gelabelde 'Toon technische details'-uitklap binnen dezelfde ExpansionTile, zodat niets verloren gaat voor wie de volledige data nodig heeft. Dit is een zuiver frontend-rendering-wijziging: geen aanpassing aan API, database of levering aan de Software Factory, en dus in isolatie te beoordelen en terug te draaien. Het API-veld `summary` (nu null bij NEEDS_REVISION/FAILED) blijft ongewijzigd in deze richting; het gat dat de eigenaar bij juist die iteraties minder uitleg krijgt, wordt met deze wijziging al grotendeels verkleind omdat de onderliggende rolresultaten dan zelf leesbaar worden.

**Waarom:** Het onderzoek toont een concrete, in de broncode bevestigde inconsistentie binnen dezelfde app: het storykandidaat-dialoog toont agentinhoud al volledig leesbaar, terwijl het iteratie-detaildialoog dezelfde soort inhoud als ruwe JSON toont (main.dart, _prettyJson, regels 990-1051). Dit raakt direct de productvisie-eis dat leesbaarheid beoordeeld wordt 'vanuit wie het dashboard daadwerkelijk gebruikt'. De gekozen richting is klein (alleen dashboard-rendering), legt uit waarom het huidige gedrag zo was (JSON was de makkelijkste implementatie, geen bewuste keuze tegen leesbaarheid) en is in isolatie toetsbaar en terug te draaien — conform de kwaliteitsregels. De bredere, risicovollere wijziging aan het `summary`-API-veld wordt bewust niet meegenomen, in lijn met het principe dat onomkeerbaarheid zwaarder weegt dan gemak.

### Prioriteiten
- Los de inconsistentie op: agentrolresultaten in het iteratie-detaildialoog leesbaar tonen zoals al gebeurt in het storykandidaat-dialoog
- Behoud de ruwe JSON-data toegankelijk via een secundaire, duidelijk gelabelde technische weergave (geen informatieverlies)
- Houd de wijziging klein en geïsoleerd tot dashboard-rendering (main.dart), zonder API- of databasewijzigingen
- Laat het `summary`-veld-gat bij NEEDS_REVISION/FAILED bewust buiten scope voor nu; markeer als vervolgonderzoek

### Besluiten
- **Vervang in IterationSessionDialog (dashboard-frontend/lib/main.dart) de weergave van elk agentrolresultaat: toon per rol leesbare, veldspecifieke tekst als primaire weergave in plaats van ruwe JsonEncoder.withIndent-tekst. Concreet per rol: Onderzoeker → 'findings' als lopende tekst plus bronnen als leesbare lijst; Product owner → elke 'decision' met bijbehorende 'rationale' als leesbare alinea's en sourceUrls als links; UX-ontwerp en Story writer → hun tekstuele velden (bv. titel, omschrijving, acceptatiecriteria) net zoals al gebeurt in het bestaande storykandidaat-dialoog; Criticus → 'overallVerdict'/'summary' als leesbare tekst en 'issues' als opsomming.** — De productvisie eist leesbaarheid 'vanuit wie het dashboard daadwerkelijk gebruikt'. Het storykandidaat-dialoog in dezelfde app toont vergelijkbare agentinhoud al volledig leesbaar zonder JSON-notatie — deze wijziging maakt de app intern consistent in plaats van een nieuw patroon te verzinnen.
- **Behoud de ruwe JSON niet als enige weergave maar als secundaire, expliciet gelabelde 'Toon technische details'-uitklap binnen dezelfde ExpansionTile, in plaats van de _prettyJson-weergave te verwijderen.** — Progressive disclosure: veelgevraagde informatie (leesbare uitleg) staat primair, technische/volledige data blijft voor wie dat nodig heeft secundair beschikbaar zonder informatieverlies — precies het patroon dat LangSmith hanteert voor agent-traces (Details vs. Messages) en dat NN/g methodisch onderbouwt.
- **Laat het API-veld `summary` op iteratieniveau (nu alleen gevuld bij ACCEPTED, null bij NEEDS_REVISION/FAILED) in dit voorstel ongewijzigd; dit wordt niet meegenomen in de huidige richting.** — Dit vraagt een wijziging aan API/backend-gedrag in plaats van alleen dashboard-rendering, en weegt zwaarder volgens het principe 'onomkeerbaarheid weegt zwaarder dan gemak'. Met leesbare per-rol weergave (bovenstaande beslissingen) is de belangrijkste pijn — ruwe JSON bij juist de iteraties waar uitleg het meest nodig is — al grotendeels verholpen zonder de API aan te raken; dit blijft een kleine, geïsoleerde, terug te draaien frontend-wijziging.

## UX-voorstel: Leesbare agentrolresultaten in het iteratie-detaildialoog

**Gebruikersdoel:** Als producteigenaar wil ik in het iteratie-detaildialoog per agentrol (Onderzoeker, Product owner, UX-ontwerp, Story writer, Criticus) direct leesbare tekst zien in plaats van ruwe JSON, zodat ik snel begrijp wat er per rol is gebeurd en waarom — zonder JSON te hoeven interpreteren — terwijl de volledige ruwe data voor wie dat nodig heeft beschikbaar blijft.

### Flow
1. Eigenaar klikt in het iteratie-overzicht op een iteratie; IterationSessionDialog opent.
2. Dialoog toont bovenaan de bestaande koptekst: classificatiebadge, foutreden (indien FAILED) en 'Samenvatting voor jou' (indien aanwezig).
3. Eigenaar klikt een agentrol-ExpansionTile open (bv. 'Criticus').
4. Het uitgeklapte paneel toont primair leesbare, veldspecifieke tekst: bv. 'overallVerdict' en 'summary' als lopende tekst, 'issues' als opsomming, 'decisions' met 'rationale' als alinea's, 'sourceUrls' als klikbare links.
5. Onder de leesbare tekst staat een samengevouwen, duidelijk gelabelde subsectie 'Toon technische details'.
6. Eigenaar klikt/activeert optioneel 'Toon technische details' om de bestaande ruwe, ingesprongen JSON (_prettyJson) alsnog te zien.
7. Eigenaar doorloopt alle rol-tegels en toggles volledig via toetsenbord (Tab, Shift+Tab, Enter/Spatie) zonder muis.
8. Eigenaar sluit het dialoog en keert terug naar het iteratie-overzicht; gekozen uitklapstatus hoeft niet bewaard te blijven.

### Wireframe

┌─ IterationSessionDialog ──────────────────────────────────────────┐
│ Iteratie #14 · hkh-autopilot                    [Badge: guardrail]│
│ Foutreden: "Workspace-publicatie tijdelijk niet beschikbaar..."   │
│ ┌─ Samenvatting voor jou (indien aanwezig) ──────────────────────┐│
│ │ Onderzoek en ontwerp voor ... zijn afgerond en geaccepteerd.   ││
│ └─────────────────────────────────────────────────────────────── ┘│
│                                                                    │
│ ▸ Onderzoeker                                                     │
│ ▾ Product owner                                                   │
│   ┌───────────────────────────────────────────────────────────┐  │
│   │ Beslissing: "Kies voor kaartweergave met foto-pins"        │  │
│   │ Onderbouwing: "Sluit aan bij gebruikersbehoefte om..."     │  │
│   │ Bronnen: • nngroup.com/... • docs.langchain.com/...        │  │
│   │                                                             │  │
│   │ ▸ Toon technische details                                   │  │
│   │   (uitgeklapt toont: rauwe JSON zoals voorheen, monospace,  │  │
│   │    binnen SelectableText, ongewijzigd)                      │  │
│   └───────────────────────────────────────────────────────────┘  │
│ ▸ UX-ontwerp                                                      │
│ ▸ Story writer                                                    │
│ ▾ Criticus                                                        │
│   ┌───────────────────────────────────────────────────────────┐  │
│   │ Oordeel: NEEDS_REVISION                                    │  │
│   │ Samenvatting: "Onvoldoende gedateerde bronnen beschikbaar   │  │
│   │  voor een sluitende tijdlijn."                              │  │
│   │ Aandachtspunten:                                            │  │
│   │  • Bron X mist publicatiedatum                              │  │
│   │  • Bron Y is niet verifieerbaar                             │  │
│   │                                                             │  │
│   │ ▸ Toon technische details                                   │  │
│   └───────────────────────────────────────────────────────────┘  │
│                                                          [Sluiten] │
└────────────────────────────────────────────────────────────────── ┘

Legenda: ▸ = ingeklapt, ▾ = uitgeklapt. Elk rol-paneel: leesbare tekst
primair zichtbaar bij uitklappen; ruwe JSON alleen zichtbaar na een
extra, expliciete "Toon technische details"-actie (progressive disclosure).

### Interactiehypotheses
- Bij een NEEDS_REVISION- of FAILED-iteratie bevat de primair zichtbare tekst in het uitgeklapte Criticus- en Product owner-paneel geen rauwe JSON-syntax (geen { } of "sleutel": als eerste zichtbare inhoud) — automatisch toetsbaar door de gerenderde tekst te controleren op afwezigheid van JSON-structuurtekens.
- De ruwe JSON onder 'Toon technische details' is byte-voor-byte gelijk aan de oorspronkelijke contentJson van dat artefact — automatisch toetsbaar door JSON.decode van de technische-detailtekst te vergelijken met de brondata uit de API-respons.
- Alle interactieve elementen (rol-ExpansionTiles en de nieuwe 'Toon technische details'-toggles) zijn volledig bereikbaar en bedienbaar met alleen het toetsenbord (Tab-volgorde, Enter/Spatie activeert) — automatisch toetsbaar via een toetsenbordnavigatie-simulatie (Flutter widget/integration test of Playwright keyboard events op de web-build).
- Voor rollen met ontbrekende of lege velden (bv. geen sourceUrls, lege issues-lijst) toont de leesbare weergave geen 'null' of lege restanten, maar laat het veld weg — automatisch toetsbaar met unit tests op de renderfunctie tegen edge-case payloads (leeg array, ontbrekende sleutel, null-waarde).
- De bestaande badge- en foutreden-weergave (uit iteratie 14) blijft ongewijzigd zichtbaar en functioneel na deze wijziging — automatisch toetsbaar door regressietests op shadow-hkh-autopilot-0002/-0003 te herhalen na de wijziging.

### Toegankelijkheid
- Alle rol-ExpansionTiles en de nieuwe 'Toon technische details'-toggles zijn volledig bereikbaar en bedienbaar met alleen het toetsenbord (Tab, Shift+Tab, Enter, Spatie), zonder muisafhankelijkheid.
- Leesbare tekstblokken per rol krijgen semantische labels (Flutter Semantics) zodat een schermlezer bijvoorbeeld 'Product owner, beslissing: ..., onderbouwing: ...' aankondigt in plaats van rauwe JSON-tekens voor te lezen.
- De 'Toon technische details'-toggle communiceert zijn in-/uitgeklapte status semantisch (equivalent van aria-expanded) zodat schermlezergebruikers weten of de technische data zichtbaar is.
- Tekstkleur en achtergrond van zowel de leesbare weergave als de technische-detailsectie voldoen aan minimaal WCAG AA-contrastratio (4.5:1 voor platte tekst).
- Focus blijft zichtbaar en voorspelbaar: bij het uitklappen van een rol-tile of technische-detailsectie verspringt de toetsenbordfocus niet onverwacht naar een ander element.
- Links binnen 'Bronnen' (sourceUrls) zijn herkenbaar als link (onderstreping/kleur, niet alleen kleur) en hebben een programmatisch toegankelijk linkdoel voor schermlezers.

### Privacy
- De wijziging betreft uitsluitend de renderingslaag (dashboard-frontend); er wordt geen nieuwe data verzameld, opgeslagen of naar externe diensten verzonden.
- De getoonde leesbare tekst en de technische-detailweergave bevatten dezelfde operationele metadata van Product Factory zelf (findings, decisions, verdicts) die al via de bestaande API beschikbaar was — geen nieuwe velden worden blootgelegd.
- Er worden geen persoonsgegevens of gebruikersdata van andere producten (bv. HKH Autopilot-eindgebruikers) verwerkt of getoond; de agentresultaten gaan over het eigen ontwikkelproces, niet over derden.
- Bronlinks (sourceUrls) worden alleen als leesbare, klikbare tekst getoond zonder tracking-parameters toe te voegen of gebruikersinteractie daarmee te loggen.

## Kritische beoordeling

**Oordeel:** ACCEPT

Beide kandidaten zijn goed onderbouwd met eigen broncode (main.dart, exacte regelnummers) en live-verificatie op de acceptatieomgeving, betreffen uitsluitend de frontend-renderinglaag (geen API/DB/auth-wijzigingen), zijn in isolatie te beoordelen en terug te draaien, en bevatten expliciete, agent-uitvoerbare inspectie-/fallbackpaden zodat geen menselijk besluitmoment nodig is tijdens implementatie. Geen overlap met de 13 reeds gepubliceerde kandidaten (22-34), die over classificatiebadges/dependsOn gaan, niet over JSON-leesbaarheid. Kandidaat 1 bouwt correct en expliciet voort op kandidaat 0 via dependsOn. Enige aandachtspunten zijn niet-blokkerend: kandidaat 0 specificeert geen expliciete toegankelijkheidstoets voor de nieuwe leesbare tekst (al is platte tekst inherent toegankelijker dan rauwe JSON binnen dezelfde al-toegankelijke ExpansionTile), en kandidaat 1's a11y-verificatie moet de Flutter-semantics-/AX-tree-laag inspecteren in plaats van zichtbare tekst, in lijn met de eerder vastgelegde inspectietechniek.
- **WARNING · ACCESSIBILITY** — Kandidaat 0 (leesbare-rolresultaten-basis) bevat geen expliciet acceptatiecriterium dat toetsenbord-/schermlezertoegang tot de nieuwe leesbare tekstblokken verifieert, terwijl de productvisie dit expliciet eist. Risico is laag omdat platte tekst binnen een al-toegankelijke ExpansionTile wordt geplaatst, maar dit zou expliciet getoetst moeten worden.
- **WARNING · ACCESSIBILITY** — Kandidaat 1's acceptatiecriterium voor aria-expanded-equivalent gedrag moet de Flutter-semantics-/AX-tree-laag inspecteren (flt-semantics-placeholder + CDP AX tree), niet page.accessibility of zichtbare tekst, om betrouwbaar te zijn op de Flutter-webbuild.
- **INFO · CONSISTENCY** — Geen van beide kandidaten benoemt expliciet in de storytekst zelf waarom het huidige gedrag (rauwe JSON) zo was (onbewuste implementatiekeuze, geen bewust ontwerp); dit staat wel in de bredere onderzoekscontext maar niet in de kandidaat-omschrijving zelf.

## Geaccepteerde storykandidaten

### Toon leesbare, veldspecifieke tekst naast de bestaande ruwe JSON per agentrol in het iteratie-detaildialoog

_Sleutel: `leesbare-rolresultaten-basis`_

In dashboard-frontend/lib/main.dart toont IterationSessionDialog het resultaat van elke agentrol (Onderzoeker, Product owner, UX-ontwerp, Story writer, Criticus) momenteel uitsluitend als ruwe, ingesprongen JSON via `SelectableText(_prettyJson(...))` binnen een ExpansionTile (regels 990-1004, 1045-1051). Live bevestigd op shadow-hkh-autopilot-0003: het Onderzoeker-blok toont letterlijk `{
  "findings": "..."
}` inclusief accolades in plaats van de tekst zelf. Ter vergelijking toont het storykandidaat-dialoog in dezelfde app vergelijkbare agentinhoud al volledig leesbaar zonder JSON-notatie — dit is dus een bestaand, bewezen intern patroon dat hier wordt hergebruikt, geen nieuw ontwerp. Deze story voegt per rol leesbare, veldspecifieke tekst toe (bv. Onderzoeker: 'findings' als lopende tekst; Product owner: elke 'decision' met 'rationale' als alinea's en sourceUrls als lijst; UX-ontwerp/Story writer/Criticus: hun tekstuele velden analoog aan het storykandidaat-dialoog) bovenop, niet in plaats van, de bestaande ruwe JSON-weergave. Omdat de exacte JSON-veldstructuur per rol-artefacttype niet is bevestigd tegen de actuele broncode/database (het onderzoek beschrijft alleen voorbeeldstructuren), inspecteert de implementerende agent eerst geautomatiseerd de daadwerkelijke contentJson-structuur per rol en documenteert een 'bekende velden'-lijst; artefacten met afwijkende structuur vallen terug op alleen de bestaande ruwe weergave (geen crash, geen halfwerk).

**Acceptatiecriteria**
- De implementerende agent inspecteert geautomatiseerd de daadwerkelijke contentJson-structuur van bestaande artefacten per rol (Onderzoeker, Product owner, UX-ontwerp, Story writer, Criticus) en documenteert de gevonden veldnamen als 'bekende velden'-lijst, als basis voor de renderlogica.
- Voor elk rol-artefacttype waarvan bekende tekstuele velden zijn gevonden, toont IterationSessionDialog deze velden als leesbare tekst en/of lijst bovenaan de rol-tegel, zichtbaar zonder extra klik na het uitklappen van de tegel, zonder de bestaande ruwe JSON-weergave te verwijderen.
- Voor artefacten met een structuur die niet (volledig) in de gedocumenteerde bekende-veldenlijst voorkomt, blijft uitsluitend de bestaande ruwe JSON-weergave zichtbaar; er verschijnt geen lege of foutieve leesbare sectie en de app crasht niet.
- Velden die leeg, null of een lege lijst zijn, worden volledig weggelaten uit de leesbare weergave (geen zichtbare tekst 'null' of lege opsommingstekens).
- Een geautomatiseerde unit- of widgettest dekt minimaal drie gevallen: een Onderzoeker-artefact met tekstuele findings, een Product owner-artefact met een decisions-array inclusief rationale, en een artefact met een niet-herkende veldstructuur (fallback-pad).
- De bestaande classificatiebadge, het foutreden-blok bij FAILED en de 'Samenvatting voor jou'-kaart (reeds gepubliceerde kandidaten) blijven na deze wijziging ongewijzigd zichtbaar en functioneel, geverifieerd met een regressietest.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://product-factory-api-acceptance.vdzonsoftware.nl/api/shadow-iterations](https://product-factory-api-acceptance.vdzonsoftware.nl/api/shadow-iterations)

Risico's: De daadwerkelijke JSON-schema's per rol kunnen sterk verschillen tussen rollen of zelfs binnen dezelfde rol over verschillende iteraties, wat de 'bekende velden'-lijst onvolledig kan maken; het verplichte inspectie-/fallbackpad in de acceptatiecriteria beperkt dit risico., Toevoegen van leesbare tekst náást (in plaats van in plaats van) de ruwe JSON kan het dialoog langer en drukker maken; dit wordt in een vervolgstory (progressive disclosure) verholpen door de ruwe JSON in te klappen., Als de contentJson-structuur per rol al vaker wijzigt in de bestaande pipeline, kan de renderlogica achterlopen bij toekomstige velduitbreidingen; dit wordt gemitigeerd doordat onbekende structuren altijd netjes terugvallen op de ruwe weergave.

### Verplaats de ruwe JSON-weergave per agentrol achter een toegankelijke, standaard ingeklapte 'Toon technische details'-toggle

_Sleutel: `technische-details-toggle`_

Bouwt voort op de vorige story (leesbare-rolresultaten-basis), die leesbare tekst toevoegt náást de bestaande ruwe JSON per agentrol. Om het dialoog overzichtelijk te houden zonder informatie te verliezen, past deze story het progressive-disclosure-patroon toe (analoog aan LangSmith's 'Details' vs. 'Messages'-weergave voor agent-traces, en de NN/g-richtlijn om secundaire/technische data pas op verzoek te tonen): de al bestaande ruwe JSON-weergave (waar leesbare tekst voor is toegevoegd) wordt verplaatst naar een nieuwe, standaard ingeklapte subsectie met het label 'Toon technische details', volledig toetsenbord- en schermlezerbedienbaar. Voor artefacten zonder herkende leesbare velden (het fallback-pad uit de vorige story) blijft de ruwe JSON direct zichtbaar, zonder extra toggle-stap, zodat gebruikers daar nooit data hoeven te 'ontdekken' achter een toggle die geen leesbaar alternatief biedt.

**Acceptatiecriteria**
- Binnen elke rol-ExpansionTile die leesbare tekst toont (opgeleverd in de vorige story), wordt de bestaande ruwe JSON-weergave verplaatst naar een nieuwe, standaard ingeklapte subsectie met het zichtbare label 'Toon technische details'.
- De 'Toon technische details'-toggle is volledig bereikbaar en bedienbaar met alleen het toetsenbord (Tab/Shift+Tab bereikt de toggle, Enter of Spatie activeert/deactiveert), geverifieerd met een geautomatiseerde toetsenbordnavigatietest.
- De toggle communiceert zijn in-/uitgeklapte status semantisch equivalent aan aria-expanded, geverifieerd via een geautomatiseerde accessibility-/AX-tree-inspectie van de Flutter-webbuild.
- De inhoud van de technische-detailweergave na uitklappen is, na JSON-decodering, functioneel gelijk aan de oorspronkelijke contentJson van dat artefact, geverifieerd door een geautomatiseerde vergelijking tussen de getoonde tekst en de brondata uit de API-respons.
- Voor artefacten zonder herkende leesbare velden (fallback-pad) blijft de ruwe JSON direct zichtbaar zoals vóór deze wijziging, zonder dat daarvoor een extra toggle-klik nodig is.
- De bestaande classificatiebadge, het foutreden-blok bij FAILED en de 'Samenvatting voor jou'-kaart blijven na deze wijziging ongewijzigd zichtbaar en functioneel, geverifieerd met een regressietest.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://www.nngroup.com/articles/progressive-disclosure/](https://www.nngroup.com/articles/progressive-disclosure/), [https://docs.langchain.com/langsmith/trace-deep-agents](https://docs.langchain.com/langsmith/trace-deep-agents)

Afhankelijkheden (candidateKey): leesbare-rolresultaten-basis (binnen deze batch herkend als: leesbare-rolresultaten-basis)

Risico's: Het achter een toggle plaatsen van de ruwe data kan de vindbaarheid ervan verminderen voor wie juist de volledige, ongefilterde JSON nodig heeft (bv. debugging); dit wordt gemitigeerd door een duidelijk, consistent label en door het fallback-pad waarbij de ruwe JSON zonder toggle zichtbaar blijft wanneer er geen leesbaar alternatief is., Flutter-webapps renderen toegankelijkheidsstatus (zoals aria-expanded-equivalenten) niet altijd op de gebruikelijke manier in de DOM; geautomatiseerde verificatie moet de semantics-laag (bv. flt-semantics-placeholder/AX-tree) inspecteren in plaats van alleen zichtbare tekst, om dit betrouwbaar te kunnen toetsen., Als de vorige story (leesbare-rolresultaten-basis) niet is opgeleverd of de leesbare tekst mist voor bepaalde rollen, mag deze story die rol-tegels niet alsnog achter een toggle verstoppen zonder leesbaar alternatief.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
