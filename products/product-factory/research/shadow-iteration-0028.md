---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0028
date: 2026-08-11
status: approved
sources:
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/factory/functional-spec.md
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-25-Herstel-tegenspraak-in-Reden-blok-toon-criticusoordeel-geregistreerd.md
  - https://api.github.com/repos/robbertvdzon/product-factory/commits
  - https://github.com/robbertvdzon/product-factory/actions/runs/31460797418
  - https://product-factory-acceptance.vdzonsoftware.nl
  - https://product-factory-api-acceptance.vdzonsoftware.nl/api/shadow-iterations/shadow-hkh-autopilot-0003?productSlug=hkh-autopilot
  - https://cicd.watch/web
  - https://docs.gitlab.com/user/analytics/ci_cd_analytics/
---
# Productcyclus 28

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Live verificatie (broncode via GitHub + Playwright-sessies met API-capture op de acceptatieomgeving) bevestigt dat de traceerbaarheids-reeks uit eerdere iteraties nu daadwerkelijk werkt: story product-factory-25 (gemerged 2026-08-11T05:10:41Z) loste de laatst overgebleven tegenspraak op — cyclus shadow-hkh-autopilot-0003 toonde tot voor kort in het overzicht "criticus: REVISE" maar in het detaildialoog nog de misleidende tekst "Criticus-oordeel ontbreekt voor deze cyclus". Ik heb de deploy-pijplijn live gevolgd (merge → build container images → deploy-pincommit → rollout, ~4 minuten) en na afronding herbevestigd dat het detaildialoog nu correct toont: "Criticusoordeel REVISE geregistreerd, maar geen onderliggend criticus-artefact beschikbaar." Deze specifieke databug/UI-tegenspraak is dus opgelost en nu ook feitelijk live, niet alleen gemerged. Het grotere, evenwaardige punt uit het overleg van 2026-08-10 — een overladen, plat hoofdscherm zonder hiërarchie richting de drie kernacties (nieuwe cyclus starten / cyclusresultaten zien / stories bekijken) — is echter nog volledig onaangeroerd: `docs/factory/functional-spec.md` beschrijft nog steeds exact dezelfde 7 gelijkwaardige platte secties (metric-tegels, Producten, Productcycli, Software Factory-stories, access tokens, Storywachtrij, Workspace) als vóór iteratie 27, en de live homepage-screenshot bevestigt dit. De primaire actie "Start productcyclus nu" staat bovendien visueel gelijkwaardig tussen dichte configuratietekst (missie, repo, workspace, WIP, AI-provider/model, cyclustijden, twee checkboxes) in plaats van als duidelijk geprioriteerde call-to-action.

### Story product-factory-25 lost de laatst overgebleven Reden-blok-tegenspraak op — nu bevestigd live, inclusief het volgen van de deploy-pijplijn

Op het moment dat dit onderzoek startte was product-factory-25 net gemerged (main.dart-commit 3d039b3, 2026-08-11T05:10:41Z) maar nog niet gedeployed: het detaildialoog voor shadow-hkh-autopilot-0003 toonde live nog de oude tekst 'Criticus-oordeel ontbreekt voor deze cyclus', terwijl de cyclusrij ernaast 'criticus: REVISE' toonde — exact de tegenspraak die iteratie 27 identificeerde. Door de GitHub Actions-run (build container images, run 31460797418) en de daaropvolgende 'deploy: pin images'-commit (3d039b3, 2026-08-11T05:14:15Z) te volgen tot afronding, en de acceptatieomgeving daarna opnieuw te bevragen, is bevestigd dat het detaildialoog nu wél de nieuwe, consistente tekst toont: 'Criticusoordeel REVISE geregistreerd, maar geen onderliggend criticus-artefact beschikbaar.' De drie deelcasussen (artefact aanwezig / criticVerdict null zonder artefact / criticVerdict gezet zonder artefact) zijn ook expliciet en correct gedocumenteerd in `docs/factory/functional-spec.md` (regels 79-119).

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-25-Herstel-tegenspraak-in-Reden-blok-toon-criticusoordeel-geregistreerd.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-25-Herstel-tegenspraak-in-Reden-blok-toon-criticusoordeel-geregistreerd.md), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/factory/functional-spec.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/factory/functional-spec.md), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://product-factory-api-acceptance.vdzonsoftware.nl/api/shadow-iterations/shadow-hkh-autopilot-0003?productSlug=hkh-autopilot](https://product-factory-api-acceptance.vdzonsoftware.nl/api/shadow-iterations/shadow-hkh-autopilot-0003?productSlug=hkh-autopilot), [https://github.com/robbertvdzon/product-factory/actions/runs/31460797418](https://github.com/robbertvdzon/product-factory/actions/runs/31460797418)

### Homepage-hiërarchie: nog steeds 7 platte, gelijkwaardige secties zonder prioritering naar de drie kernacties van de eigenaar

`docs/factory/functional-spec.md` beschrijft de overzichtspagina expliciet als 'van boven naar beneden': metric-tegels, Producten, Productcycli en onderzoekssessies, Software Factory-stories, Benodigde access tokens, Storywachtrij, Workspace — zeven gelijkwaardige, louter verticaal gestapelde secties. Live screenshot van de acceptatieomgeving (dashboard vandaag) bevestigt dit exact: geen tabs, geen visuele nadruk op één van de drie dingen die de eigenaar op 2026-08-10 vroeg (nieuwe cyclus starten, cyclusresultaten zien, voortgekomen stories zien). De primaire actieknop 'Start productcyclus nu' staat in de Producten-kaart tussen missietekst, repo/workspace-metadata, max-stories, WIP-limiet, AI-provider/model en cyclustijden-checkboxes, zonder visuele voorrang boven 'Pauzeren'/'Instellingen'/'Start overleg' ernaast.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/factory/functional-spec.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/factory/functional-spec.md), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### Afkeuring-traceerbaarheid op overzichtsniveau is inmiddels goed opgelost (classificatiebadges), maar 'wie/wat besliste' blijft impliciet

Iedere cyclusrij op het hoofdscherm toont nu direct — zonder extra klik — een classificatiebadge (`onderzoek-onvoldoende`, `technische fout`, `richting-gekozen`, `richting-verworpen`, `niet-classificeerbaar`), live bevestigd via de ariaSnapshot van de acceptatieomgeving voor alle drie zichtbare hkh-autopilot-cycli. Dit lost het zichtbaarheidsdeel van de eigenaarsklacht ('ik kan niet zien of iets is afgekeurd') grotendeels op. Wat nog ontbreekt is een expliciete koppeling naar wie/wat de beslissing nam (mens, evaluatie-agent, guardrail) zoals letterlijk gevraagd op 2026-08-10 — dit is momenteel alleen impliciet af te leiden (bv. een guardrail-alinea verschijnt alleen bij REJECTED+ACCEPT-combinatie) en vereist domeinkennis van het classificatiesysteem om te doorzien.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/factory/functional-spec.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/factory/functional-spec.md), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### Software Factory-stories sectie is in de acceptatieomgeving leeg — belangrijk deel van de 'drie kernacties' van de eigenaar is niet end-to-end te beoordelen met de huidige seed-data

Live geverifieerd: de sectie 'Software Factory-stories' toont 'Nog geen stories naar de Software Factory gestuurd', ondanks 3 shadow-iteraties waarvan er één geaccepteerd is (iteratie 1, criticus: ACCEPT). Dit komt doordat het product op de acceptatieomgeving niet op autonoom staat ('niet doorgezet (product staat niet op autonoom)' staat bij elke cyclus). Hierdoor is het derde kernpunt van de eigenaar (voortgekomen stories zien) in deze omgeving niet te beoordelen op werkelijke inhoud/kwaliteit van storyweergave, alleen op de lege-staat-tekst.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### Huidige applicatie

**Doel:** Product Factory is de motor die producten (nu: zichzelf en hkh-autopilot) autonoom laat doorontwikkelen: per product draaien productcycli waarin agents onderzoeken, storykandidaten schrijven en — als het product op autonoom staat — deze als stories naar de Software Factory sturen. Het dashboard (Flutter-web) is voor de productoperator/eigenaar (Robbert) om cycli te starten, resultaten en afkeuringsredenen te bekijken en voortgekomen stories te volgen.

**Wat ontbreekt:**
- De homepage bestaat nog steeds uit 7 gelijkwaardige, louter verticaal gestapelde secties (metric-tegels, Producten, Productcycli, SF-stories, access tokens, Storywachtrij, Workspace) zonder enige visuele hiërarchie richting de drie kernacties die de eigenaar op 2026-08-10 expliciet vroeg (cyclus starten / resultaten zien / stories zien) — bevestigd ongewijzigd in zowel functional-spec.md als de live acceptatieomgeving.
- De primaire actieknop 'Start productcyclus nu' staat visueel gelijkwaardig tussen dichte configuratietekst (missie, repo, workspace, WIP, AI-provider/model, cyclustijden) in plaats van als duidelijk geprioriteerde call-to-action.
- 'Wie/wat besliste' (mens, evaluatie-agent, guardrail) — expliciet gevraagd op 2026-08-10 — is nog steeds niet als losstaand, direct leesbaar gegeven in de UI aanwezig; het is alleen impliciet af te leiden uit welke classificatiebadge/Reden-tekstpad van toepassing is.
- De Software Factory-stories-sectie is in de acceptatieomgeving leeg (product staat niet op autonoom), waardoor het derde kernpunt van de eigenaar (voortgekomen stories beoordelen) nu niet inhoudelijk te toetsen is, alleen als lege staat.

### Verbetermogelijkheden

- Herontwerp de informatiearchitectuur van de homepage rond de drie door de eigenaar genoemde kernacties (nieuwe cyclus / cyclusresultaten / stories) als expliciet gescheiden, prioritaire zones of tabs, met de huidige metric-tegels en configuratiedetails gedegradeerd naar secundaire of standaard-ingeklapte plaatsing — dit is de belangrijkste nog openstaande, expliciet door de eigenaar benoemde wens uit het overleg van 2026-08-10.
- Geef 'Start productcyclus nu' een duidelijk dominante visuele behandeling (bv. losstaand van de Instellingen/Pauzeren-knoppenrij, of bovenaan de kaart), en verplaats missietekst/repo/WIP/AI-instellingen achter de bestaande 'Instellingen'-knop zodat de kaart niet meer als één ondifferentieerd blok tekst oogt.
- Maak 'wie/wat besliste' (mens vs. evaluatie-agent vs. guardrail) een expliciet, zichtbaar label bij elke classificatiebadge/Reden-tekst in plaats van alleen impliciet afleidbaar — dit sluit de traceerbaarheidsvraag van de eigenaar volledig af, in plaats van alleen het 'wat' (classificatie) zichtbaar te maken.
- Overweeg, voordat een volgende story wordt geschreven op precies dit Reden-blok/criticVerdict-gebied (na inmiddels vier opeenvolgende, steeds verder verfijnde stories: 18, 19, 23, 25), eerst te verifiëren of alle status/criticVerdict/artefact-combinaties nu daadwerkelijk gedekt zijn (bv. FAILED met een gezet criticVerdict), om een vijfde incrementele patch op hetzelfde detectiepad te voorkomen.

### Inspiratiebronnen

- [CI/CD Watch — web dashboard](https://cicd.watch/web) — Toont een dashboardpatroon met een duidelijke trigger/actie gescheiden van een recente-runs-geschiedenis met kleurcodering en drill-down — relevant model voor hoe 'nieuwe cyclus starten' en 'cyclusresultaten zien' in Product Factory visueel te scheiden zijn.
- [GitLab CI/CD analytics](https://docs.gitlab.com/user/analytics/ci_cd_analytics/) — Gevestigd voorbeeld van een productiematuur systeem dat trigger-actie, statusoverzicht/trends en drill-down-detailtabellen (Projects/Pipelines/Jobs) van elkaar scheidt in plaats van alles in één platte lijst te tonen — direct toepasbaar op de door de eigenaar gevraagde 3-kernacties-hiërarchie.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart) | 2026-08-11 | Publieke GitHub-repository (robbertvdzon/product-factory); eigen broncode van de opdrachtgever, geen licentievraag van toepassing | Bevat de daadwerkelijke IterationSessionDialog-implementatie en homepage-sectiestructuur, nodig om te verifiëren wat er echt gebouwd is t.o.v. de story-omschrijving |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/factory/functional-spec.md) | 2026-08-11 | Publieke GitHub-repository, eigen documentatie van de opdrachtgever | Normatieve, actuele beschrijving van de homepage-sectievolgorde en Reden-blok-logica; bevestigt dat de 7-secties-structuur ongewijzigd is sinds het overleg van 2026-08-10 |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-25-Herstel-tegenspraak-in-Reden-blok-toon-criticusoordeel-geregistreerd.md) | 2026-08-11 | Publieke GitHub-repository, eigen storydocumentatie | Bevat scope, acceptatiecriteria en eindsamenvatting van de story die de in iteratie 27 gevonden tegenspraak claimt op te lossen |
| [bron](https://api.github.com/repos/robbertvdzon/product-factory/commits) | 2026-08-11 | Publieke GitHub API, alleen-lezen | Nodig om te bepalen of en wanneer product-factory-25 daadwerkelijk gemerged én gedeployed is (deploy-pincommit als bewijs van rollout) |
| [bron](https://github.com/robbertvdzon/product-factory/actions/runs/31460797418) | 2026-08-11 | Publieke GitHub Actions-runlog van de opdrachtgever, alleen-lezen | Bevestigt in real-time dat de build/deploy-pijplijn voor de story-25-merge daadwerkelijk afrondde, i.p.v. aan te nemen dat 'gemerged' gelijk is aan 'live' |
| [bron](https://product-factory-acceptance.vdzonsoftware.nl) | 2026-08-11 | Standing acceptatieomgeving zonder login, met representatieve nepdata; door de opdrachtgever aangewezen als onderzoeksbron, geen productiedata | Enige manier om te zien wat de eigenaar daadwerkelijk te zien krijgt; homepage-structuur, cyclusoverzicht en detaildialoog zijn hier direct met Playwright geïnspecteerd |
| [bron](https://product-factory-api-acceptance.vdzonsoftware.nl/api/shadow-iterations/shadow-hkh-autopilot-0003?productSlug=hkh-autopilot) | 2026-08-11 | Publieke, ongeauthenticeerde API van de acceptatieomgeving, alleen-lezen | Bevestigt de onderliggende data (criticVerdict='REVISE', geen critic-artefact) die de UI-tegenspraak veroorzaakte, onafhankelijk van de UI-laag |
| [bron](https://cicd.watch/web) | 2026-08-11 | Publieke productwebsite; onbekende contentlicentie, uitsluitend als inspiratie geraadpleegd, niet als feitelijke bron over Product Factory | Voorbeeld van een CI/CD-dashboardpatroon met duidelijke trigger-actie + recente-runs-geschiedenis, relevant voor de homepage-hiërarchievraag |
| [bron](https://docs.gitlab.com/user/analytics/ci_cd_analytics/) | 2026-08-11 | Publieke officiële GitLab-documentatie; onbekende hergebruikslicentie, uitsluitend als inspiratie geraadpleegd | Toont hoe een gevestigd product trigger, statusoverzicht en drill-down-detail scheidt van configuratie — relevant patroon voor de gevraagde 3-kernacties-hiërarchie |

## Productbeslissing

Deze cyclus richt zich op één kleine, isoleerbare stap in de Producten-kaart op de homepage: 'Start productcyclus nu' krijgt duidelijke visuele voorrang als losstaande call-to-action, en de dichte configuratietekst eromheen (missie, repo/workspace, max-stories, WIP-limiet, AI-provider/model, cyclustijden) verhuist achter de bestaande 'Instellingen'-knop. Dit is de eerste, in isolatie toetsbare en terugdraaibare stap richting de bredere, door de eigenaar op 2026-08-10 gevraagde hiërarchie tussen de drie kernacties (cyclus starten / resultaten zien / stories zien) — zonder in één keer alle zeven homepage-secties te herstructureren.

**Waarom:** Het onderzoek toont dat de laatst overgebleven Reden-blok-tegenspraak (story product-factory-25) inmiddels live geverifieerd is opgelost, terwijl het grotere, evenwaardige punt uit hetzelfde overleg — een platte, ongehiërarchiseerde homepage — nog volledig onaangeroerd is in zowel functional-spec.md als de live acceptatieomgeving. Dit is dus de meest urgente, expliciet door de eigenaar benoemde en nog niet opgepakte verbetering. Om te voldoen aan de kwaliteitsregel dat elke wijziging in isolatie beoordeelbaar en terugdraaibaar moet zijn, kies ik voor de kleinste zinvolle eerste stap (CTA-prominentie binnen één kaart) in plaats van de volledige 7-secties-redesign, en laat ik de recent gestabiliseerde Reden-blok/classificatielogica bewust met rust.

### Prioriteiten
- Geef 'Start productcyclus nu' duidelijke visuele voorrang binnen de Producten-kaart, losstaand van de Pauzeren/Instellingen/Start overleg-knoppenrij.
- Verplaats missie, repo/workspace-metadata, max-stories, WIP-limiet, AI-provider/model en cyclustijden-checkboxes achter de bestaande 'Instellingen'-knop.
- Beperk deze wijziging tot de Producten-kaart; raak de overige zes secties (metric-tegels, Productcycli, SF-stories, access tokens, Storywachtrij, Workspace) niet aan.
- Laat de recent gevalideerde classificatiebadges en Reden-blok-teksten ongewijzigd; die traceerbaarheidsketen is zojuist live bevestigd als correct.
- Verifieer vóór een volgende story op het Reden-blok/criticVerdict-detectiepad eerst of er echt ongedekte combinaties bestaan, in plaats van direct te patchen.

### Besluiten
- **Kies als enige richting voor deze cyclus: de Producten-kaart op de homepage herindelen zodat 'Start productcyclus nu' een duidelijk dominante, losstaande call-to-action wordt, en de secundaire configuratie-informatie (missie, repo/workspace, max-stories, WIP-limiet, AI-provider/model, cyclustijden-checkboxes) verplaatst wordt achter de bestaande 'Instellingen'-knop — als eerste, isoleerbare stap richting de door de eigenaar gevraagde hiërarchie, in plaats van de volledige 7-secties-redesign in één keer.** — Het onderzoek bevestigt dat dit de belangrijkste, herhaaldelijk benoemde en nog volledig onaangeroerde wens van de eigenaar is (overleg 2026-08-10): geen enkele visuele voorrang tussen 'Start productcyclus nu' en dichte configuratietekst. Een volledige IA-redesign van alle 7 secties tegelijk zou echter niet 'klein en toetsbaar' zijn zoals de kwaliteitsregels vereisen; het isoleren tot de Producten-kaart maakt de wijziging in isolatie te beoordelen en terug te draaien, zonder de rest van de homepage of andere producten te raken.
- **Verplaats configuratie-items achter 'Instellingen' in plaats van ze te verwijderen, een nieuw scherm te bouwen of data-structuren te wijzigen.** — Dit betreft een zuivere UI-herindeling zonder impact op data, migraties, authenticatie of de Software Factory-koppeling — in lijn met het principe dat onomkeerbaarheid zwaarder weegt dan gemak. Alle bestaande informatie blijft bereikbaar, wat de wijziging reversibel houdt.
- **Stel het expliciet labelen van 'wie/wat besliste' en een eventuele vijfde patch op het Reden-blok/criticVerdict-detectiepad uit tot een latere, aparte cyclus.** — Story product-factory-25 heeft de laatst overgebleven Reden-blok-tegenspraak inmiddels live opgelost, en classificatiebadges tonen nu al het 'wat' zonder extra klik — het traceerbaarheidsprobleem is dus grotendeels verholpen. Deze twee onderwerpen combineren met de CTA-herindeling zou de wijziging minder klein en minder in isolatie beoordeelbaar maken; bovendien is nog niet geverifieerd of er daadwerkelijk ongedekte criticVerdict-combinaties bestaan, dus een nieuwe patch zou voorbarig zijn.

## UX-voorstel: Producten-kaart: prominente CTA "Start productcyclus nu" + configuratie achter Instellingen

**Gebruikersdoel:** Als producteigenaar wil ik in de Producten-kaart op de homepage in één oogopslag zien welke actie ik nu kan nemen (een productcyclus starten), zonder die actie te moeten zoeken tussen dichte configuratietekst (missie, repo, workspace, WIP-limiet, AI-provider/model, cyclustijden).

### Flow
1. Eigenaar opent de homepage van Product Factory en ziet de Producten-kaart voor een product (bv. hkh-autopilot).
2. De kaart toont bovenaan alleen: productnaam, status (autonoom/handmatig), en de knop 'Start productcyclus nu' als visueel dominante, losstaande call-to-action — vóór en los van de knoppenrij Pauzeren/Instellingen/Start overleg.
3. Missie, repo/workspace-metadata, max-stories, WIP-limiet, AI-provider/model en cyclustijden-checkboxes zijn niet meer standaard zichtbaar op de kaart; ze zijn verplaatst achter de bestaande knop 'Instellingen'.
4. Eigenaar klikt op 'Start productcyclus nu' → cyclus start direct (bestaand gedrag ongewijzigd) zonder dat eerst door configuratietekst gescrold hoeft te worden.
5. Eigenaar die de configuratie wél wil zien of aanpassen klikt op 'Instellingen' → bestaand instellingenpaneel/dialoog opent met alle verplaatste velden (geen inhoudelijke wijziging aan die velden, alleen verplaatsing).
6. Eigenaar sluit Instellingen en keert terug naar de vereenvoudigde kaartweergave met de CTA weer prominent zichtbaar.

### Wireframe

Producten-kaart (vóór → na), tekstueel wireframe:

VOOR (huidige, platte indeling):
+-----------------------------------------------------+
| hkh-autopilot                                        |
| Missie: "..." | Repo: ... | Workspace: ...            |
| Max stories: 5 | WIP-limiet: 2                        |
| AI-provider: ... | Model: ...                         |
| Cyclustijden: [ ] Ochtend  [ ] Avond                   |
| [Start productcyclus nu] [Pauzeren] [Instellingen] [Start overleg] |
+-----------------------------------------------------+

NA (voorgestelde herindeling):
+-----------------------------------------------------+
| hkh-autopilot                    Status: ● Autonoom   |
|                                                        |
|   [ ▶ Start productcyclus nu ]   <- grote, losstaande CTA, primaire knopstijl, eigen rij |
|                                                        |
| ---------------------------------------------------- |
| [Pauzeren]  [Instellingen ▾]  [Start overleg]          |
+-----------------------------------------------------+

Bij klik op "Instellingen ▾" (uitklap-paneel of dialoog, bestaande component, alleen verplaatste inhoud):
+-----------------------------------------------------+
| Instellingen — hkh-autopilot                    [x]   |
| Missie: [........................]                    |
| Repo: ...   Workspace: ...                             |
| Max stories: [5]   WIP-limiet: [2]                     |
| AI-provider: [...]  Model: [...]                        |
| Cyclustijden: [ ] Ochtend  [ ] Avond                    |
|                                   [Annuleren] [Opslaan] |
+-----------------------------------------------------+

Focus-volgorde (toetsenbord/tab): productnaam-heading → status-badge → Start productcyclus nu (eerste interactieve element, direct na heading) → Pauzeren → Instellingen → Start overleg. Instellingen-paneel: focus-trap binnen dialoog, Escape sluit en retourneert focus naar de Instellingen-knop.

### Interactiehypotheses
- Als 'Start productcyclus nu' losstaand en visueel dominant boven de secundaire knoppenrij staat, dan daalt de tijd-tot-eerste-klik op die knop meetbaar t.o.v. de huidige indeling, te toetsen met een agent-gestuurde interactietest die viewport-coördinaten en klikvolgorde logt op zowel de oude als nieuwe kaartlayout.
- Als configuratievelden (missie, repo, WIP, AI-model, cyclustijden) verplaatst worden achter 'Instellingen', dan blijft elk veld 100% functioneel bereikbaar en opslaanbaar, te toetsen met een geautomatiseerde Playwright-test die elk veld invult, opslaat en de opgeslagen waarde terugleest via de API.
- Als de kaart wordt vereenvoudigd tot naam + status + CTA + knoppenrij, dan blijft de verticale hoogte van de Producten-kaart op de homepage significant kleiner dan de huidige kaart, meetbaar via een geautomatiseerde bounding-box-meting (getBoundingClientRect) vóór en na de wijziging.
- Als de focus-volgorde zo is ingericht dat 'Start productcyclus nu' het eerste interactieve element na de kaart-heading is, dan bereikt een schermlezer/toetsenbordgebruiker deze knop met minder Tab-stappen dan in de huidige indeling, te toetsen met een geautomatiseerde axe-core/Playwright-toetsenbordnavigatietest die het aantal Tab-toetsaanslagen tot aan de CTA telt.

### Toegankelijkheid
- 'Start productcyclus nu' is een <button> (geen div/span) met zichtbare focusring en accessible name gelijk aan de zichtbare tekst; bereikbaar en activeerbaar met alleen Tab + Enter/Spatie.
- Contrastverhouding van de primaire CTA-knop (tekst-op-achtergrond) is minimaal 4.5:1 (WCAG 2.1 AA), en de knop is ook zonder kleur te onderscheiden van secundaire knoppen (bv. via grootte, rand, positie), zodat kleurenblinde gebruikers de hiërarchie ook zien.
- Het 'Instellingen'-paneel/dialoog krijgt role="dialog" met aria-modal="true", een focus-trap, en sluit met Escape waarbij focus terugkeert naar de 'Instellingen'-knop, zodat schermlezer- en toetsenbordgebruikers niet 'verdwalen'.
- Status-indicator (autonoom/handmatig) mag niet alleen op kleur (bolletje) steunen; voeg een tekstlabel toe (bv. 'Autonoom') zodat de status ook voor schermlezers en kleurenblinde gebruikers duidelijk is.
- Alle verplaatste velden in het Instellingen-paneel behouden hun bestaande, correct gekoppelde <label>-for-relaties en foutmeldingen (aria-describedby) — verplaatsing mag geen labels loskoppelen van hun invoervelden.

### Privacy
- Deze wijziging betreft uitsluitend layout/indeling van reeds bestaande, niet-persoonsgebonden operationele metadata van Product Factory zelf (missie, repo, WIP-limiet, AI-model, cyclustijden); er wordt geen nieuwe data verzameld, opgeslagen of getoond.
- Er worden geen persoonsgegevens of gebruikersdata van andere producten in deze flow verwerkt of weergegeven; de kaart toont alleen productconfiguratie van Product Factory-producten die de eigenaar zelf beheert.
- Het verplaatsen van velden achter 'Instellingen' vermindert onbedoelde blootstelling van configuratiedetails (bv. repo-URL, AI-provider) bij een vluchtige blik op de homepage of bij scherm delen tijdens een demo, omdat deze details pas zichtbaar worden na een bewuste klik.
- Geen wijziging aan authenticatie, tokens of toegangscontrole; de bestaande 'Instellingen'-knop en onderliggende endpoints blijven ongewijzigd qua rechten en zichtbaarheid.

## Kritische beoordeling

**Oordeel:** ACCEPT

Beide kandidaten (0: configuratievelden naar Instellingen verplaatsen; 1: 'Start productcyclus nu' prominenter maken) vormen samen een goed onderbouwde, kleine eerste stap richting de door de eigenaar op 2026-08-10 gevraagde homepage-hiërarchie. De sourcing is sterk (functional-spec.md, main.dart, live acceptatieomgeving, GitHub Actions-run als bewijs van daadwerkelijke deploy), de scope is expliciet beperkt tot de Producten-kaart, de wijziging is een zuivere presentatielaag-aanpassing (geen backend/DB/API-wijziging) en dus goed isoleerbaar en terugdraaibaar, en toegankelijkheid (contrast, focus-trap, aria-modal, label-for, toetsenbordvolgorde) is expliciet in de acceptatiecriteria opgenomen — inclusief het correcte Flutter-web a11y-testpatroon (flt-semantics-placeholder + ariaSnapshot/CDP AX-tree) in plaats van het onbetrouwbare page.accessibility/innerText-pad. Er zijn geen persoonsgegevens betrokken en geen enkele acceptatiecriterium vereist menselijke tussenkomst (handmatige test, accountaanmaak, betaling, DNS-wijziging) — alles is geformuleerd als geautomatiseerde Playwright-/axe-core-/toetsenbordtests, wat aan de autonomie-harde-gate voldoet. Enige aandachtspunt: kandidaat 0 gaat ervan uit dat er al een functioneel 'Instellingen'-paneel/dialoog bestaat waarin de velden passen, zonder dat dit met een concreet broncodefragment is bevestigd in het onderzoek — dit wordt zelf als risico benoemd en gemitigeerd door een verplichte agent-uitvoerbare inspectiestap vooraf, dus dit blokkeert niet maar blijft een aandachtspunt (WARNING). Geen overlap of tegenspraak met de bestaande gepubliceerde kandidaten (Reden-blok/JSON-leesbaarheid-reeks, dependsOn-sleutel-reeks) — dit is een nieuw, orthogonaal onderwerp (homepage-hiërarchie).
- **WARNING · SOURCE** — Kandidaat 0 (verplaats-productconfig-naar-instellingen) veronderstelt dat er al een functioneel 'Instellingen'-paneel/dialoog bestaat waarin de zes velden simpelweg passen, maar het onderzoek citeert geen daadwerkelijk broncodefragment uit main.dart dat de huidige inhoud/structuur van dat paneel bevestigt — de eigen risico-sectie erkent expliciet dat het mogelijk 'alleen een lege knop' is. Dit is een aanname i.p.v. bronbevestiging, wat strikt genomen tegen de bronnen-regel ingaat, al wordt het gemitigeerd door de verplichte agent-uitvoerbare inspectiestap in acceptatiecriterium 1.
- **INFO · SCOPE** — Als de verplichte inspectiestap in kandidaat 0 uitwijst dat er nog geen Instellingen-dialoog bestaat, is er geen expliciet gedefinieerd fallbackgedrag in de acceptatiecriteria (alleen 'documenteren') — dit kan de daadwerkelijke omvang van de wijziging laten groeien voorbij de als 'klein en isoleerbaar' bedoelde scope, al blijft de uitvoering zelf volledig agent-uitvoerbaar zonder menselijk besluitmoment.
- **INFO · CONSISTENCY** — Kandidaat 1's acceptatiecriterium over kaarthoogte-vergelijking (getBoundingClientRect vóór/na) is afhankelijk van de daadwerkelijke afronding van kandidaat 0; als kandidaat 0 door scope-groei (zie vorig punt) een andere kaartstructuur oplevert dan aangenomen, blijft de vergelijking wel zinvol maar mogelijk minder voorspelbaar in exacte uitkomst. Geen blokkerend probleem, dependsOn-relatie is correct met de reeds gepubliceerde stabiele-sleutel-mechaniek (candidates 29/30) gemodelleerd.

## Geaccepteerde storykandidaten

### Verplaats missie/repo/workspace/max-stories/WIP-limiet/AI-model/cyclustijden van de Producten-kaart naar het bestaande Instellingen-paneel

_Sleutel: `verplaats-productconfig-naar-instellingen`_

Live onderzoek (functional-spec.md en de acceptatieomgeving) bevestigt dat de Producten-kaart op de Product Factory-homepage momenteel missie, repo/workspace-metadata, max-stories, WIP-limiet, AI-provider/model en cyclustijden-checkboxes allemaal standaard zichtbaar toont, gelijkwaardig aan elkaar en aan de primaire actieknop 'Start productcyclus nu'. Dit is exact de door de eigenaar op 2026-08-10 benoemde klacht: geen visuele hiërarchie tussen de kernactie (cyclus starten) en dichte configuratietekst. Deze story verplaatst uitsluitend deze zes configuratie-items van de directe kaartweergave naar het bestaande 'Instellingen'-paneel/dialoog van dezelfde kaart, zodat de kaart zelf compacter wordt zonder dat er informatie verloren gaat of onbereikbaar wordt. De implementerende agent inspecteert eerst geautomatiseerd de daadwerkelijke huidige Instellingen-knop-implementatie in dashboard-frontend/lib/main.dart (bestaat er al een dialoog/paneel, en welke velden bevat die al) en documenteert deze bevinding voordat wijzigingen worden aangebracht, zodat de scope op de werkelijke codebase is gebaseerd. Dit is een zuivere presentatielaag-verplaatsing: geen nieuw databaseveld, geen backend-wijziging, geen wijziging aan het opslaan/laden van deze velden via de bestaande API, en geen wijziging aan andere homepage-secties of andere producten.

**Acceptatiecriteria**
- De implementerende agent inspecteert eerst geautomatiseerd de huidige Instellingen-knop-implementatie in dashboard-frontend/lib/main.dart en documenteert of er al een dialoog/paneel bestaat en welke velden dit al bevat, vóórdat wijzigingen worden aangebracht.
- Missie, repo/workspace-metadata, max-stories, WIP-limiet, AI-provider/model en cyclustijden-checkboxes zijn na de wijziging niet meer standaard zichtbaar op de Producten-kaart zelf.
- Alle zes verplaatste velden zijn volledig bereikbaar, invoerbaar en opslaanbaar via het Instellingen-paneel/dialoog, geverifieerd met een geautomatiseerde Playwright-test die elk veld wijzigt, opslaat en de opgeslagen waarde terugleest via de bestaande API.
- Het Instellingen-paneel/dialoog heeft role="dialog" en aria-modal="true", bevat een focus-trap, en sluit met Escape waarbij de focus teruggaat naar de Instellingen-knop, geverifieerd met een geautomatiseerde toetsenbordtest.
- Alle verplaatste velden behouden hun bestaande label-for-koppelingen en foutmeldingen (aria-describedby); geen enkel label raakt los van zijn invoerveld, geverifieerd met een geautomatiseerde axe-core-scan zonder nieuwe schendingen t.o.v. de baseline.
- Geen wijziging aan backend, database, API-schema, of aan de overige homepage-secties (metric-tegels, Productcycli, SF-stories, access tokens, Storywachtrij, Workspace) of aan andere producten.
- De knoppen Pauzeren en Start overleg op de Producten-kaart blijven functioneel exact ongewijzigd.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/factory/functional-spec.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/factory/functional-spec.md), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

Risico's: Als er nog geen Instellingen-dialoog bestaat (alleen een lege knop), is een nieuw paneel nodig, wat de scope vergroot; mitigatie: de verplichte inspectiestap documenteert dit vooraf en de implementatie blijft alsnog beperkt tot de presentatielaag., Flutter-web accessibility-tests op dialogen kunnen niet betrouwbaar worden geverifieerd met page.accessibility of innerText; gebruik in plaats daarvan het flt-semantics-placeholder-klikpatroon met ariaSnapshot/CDP AX-tree voor consistente testresultaten., Verkeerd verplaatste velden kunnen per ongeluk hun bestaande validatie/foutmeldingskoppeling verliezen; expliciete assertie op label-for-behoud mitigeert dit.

### Maak 'Start productcyclus nu' een visueel dominante, losstaande call-to-action bovenaan de Producten-kaart

_Sleutel: `prominente-cta-start-cyclus`_

Bouwt voort op de kandidaat die de configuratievelden naar het Instellingen-paneel verplaatst (verplaats-productconfig-naar-instellingen); zonder die opschoning zou een prominentere CTA nog steeds tussen dichte configuratietekst staan. Deze story herpositioneert 'Start productcyclus nu' op de Producten-kaart naar een eigen rij, los van en vóór de bestaande Pauzeren/Instellingen/Start overleg-knoppenrij, met een primaire knopstijl die zich visueel (grootte/rand/positie, niet uitsluitend kleur) onderscheidt van de secundaire knoppen. De status (autonoom/handmatig) krijgt een tekstlabel naast de productnaam in plaats van alleen een gekleurd statusbolletje. Dit is een pure UI-herindeling binnen de al bestaande kaartcomponent: geen nieuwe knop-functionaliteit, geen wijziging aan wat er gebeurt bij een klik, geen wijziging aan andere homepage-secties of andere producten.

**Acceptatiecriteria**
- 'Start productcyclus nu' is een <button>-element met zichtbare focusring, staat op een eigen rij vóór en los van de Pauzeren/Instellingen/Start overleg-knoppenrij, en heeft een primaire knopstijl die visueel onderscheiden is van de secundaire knoppen via grootte en/of rand, niet uitsluitend via kleur.
- Contrastverhouding van tekst-op-achtergrond van de CTA is minimaal 4.5:1 (WCAG 2.1 AA), geverifieerd met een geautomatiseerde axe-core-scan.
- De status (autonoom/handmatig) wordt naast de productnaam getoond met een zichtbaar tekstlabel, niet uitsluitend met een gekleurd bolletje.
- Een geautomatiseerde toetsenbordnavigatietest bevestigt dat 'Start productcyclus nu' het eerste interactieve element is dat met Tab bereikt wordt na de kaart-heading/status-label, met minder of gelijk aantal Tab-stappen dan vóór deze wijziging.
- Klikken op 'Start productcyclus nu' start een cyclus met exact dezelfde bestaande API-aanroep en resulterend gedrag als vóór deze wijziging, geverifieerd met een geautomatiseerde test (geen functionele regressie).
- Een geautomatiseerde meting (getBoundingClientRect) toont dat de verticale hoogte van de Producten-kaart na deze wijziging kleiner is dan de hoogte vóór de wijziging (candidate verplaats-productconfig-naar-instellingen), gemeten op dezelfde viewportbreedte.
- Geen wijziging aan de overige zes homepage-secties (metric-tegels, Productcycli, SF-stories, access tokens, Storywachtrij, Workspace) of aan andere producten.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/factory/functional-spec.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/factory/functional-spec.md), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://cicd.watch/web](https://cicd.watch/web), [https://docs.gitlab.com/user/analytics/ci_cd_analytics/](https://docs.gitlab.com/user/analytics/ci_cd_analytics/)

Afhankelijkheden (candidateKey): verplaats-productconfig-naar-instellingen (binnen deze batch herkend als: verplaats-productconfig-naar-instellingen)

Risico's: Als de voorafgaande kandidaat nog niet is doorgevoerd, is de kaarthoogte-vergelijking niet zinvol meetbaar; de dependsOn-relatie borgt de juiste volgorde., Flutter-web knop-/focusvolgorde-tests vereisen het flt-semantics-placeholder-klikpatroon met ariaSnapshot/CDP AX-tree in plaats van page.accessibility, om betrouwbare resultaten te krijgen., Herstijling van de primaire knop kan onbedoeld bestaande golden/widget-tests op exacte pixelposities breken; de implementerende agent dient bestaande tests op deze kaart eerst te identificeren en zo nodig bewust te actualiseren.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
