---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0040
date: 2026-08-12
status: approved
sources:
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/api.dart
  - https://product-factory-acceptance.vdzonsoftware.nl
  - https://linear.app/docs/project-overview
  - https://linear.app/docs/project-milestones
  - https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs
  - https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts
  - https://support.atlassian.com/jira-software-cloud/docs/create-work-items-on-the-timeline
---
# Productcyclus 40

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De belangrijkste nog onbeantwoorde productvraag is: kan de eigenaar op het hoofdscherm per cyclus direct zien wat die cyclus heeft opgeleverd en welke stories daaruit zijn voortgekomen? De huidige implementatie toont cycli, Software Factory-leveringen en storykandidaten als afzonderlijke globale secties. Een cyclusregel vermeldt alleen aantallen kandidaten en leverbare kandidaten; titels, statussen en voortgang van de bijbehorende stories staan elders. Daardoor ondersteunt het scherm nog onvoldoende de expliciete eigenaarsbehoefte om van cyclus naar concrete opbrengst en uitvoering te kunnen scannen. De vorige iteratie heeft beslisprovenance voor handmatige annulering inmiddels in de actuele documentatie verwerkt; dat onderzoek is daarom niet herhaald. De acceptatieomgeving kon niet visueel worden beoordeeld doordat Chromium vóór paginalading werd afgebroken door een Mach-port-permissiefout. Er is geen productbesluit genomen en er zijn geen stories geschreven.

### Product Factory organiseert autonome productontwikkeling en terugkoppeling

Product Factory organiseert voor geregistreerde producten achtereenvolgens onderzoek, productkeuze, UX-ontwerp, storyvorming en kritiek. Geaccepteerde kandidaten worden voor autonome producten begrensd aan Software Factory geleverd; uitvoeringsresultaten worden als productgeheugen aan volgende cycli meegegeven. De primaire gebruiker is de producteigenaar die cycli start, resultaten en voortgang controleert en alleen voor onvermijdelijke toegangstokens hoeft in te grijpen.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md)

### Beslisprovenance voor handmatige annulering staat inmiddels in de actuele productdocumentatie

De huidige documentatie beschrijft een expliciet, privacy-minimaal beslisrecord voor handmatige annulering. Overzicht en detail tonen daarbij dezelfde bron en reden; historische cycli blijven herkenbaar afgeleid. Daarmee is de concrete fout uit de vorige iteratie aantoonbaar in de beschreven huidige staat opgenomen en is opnieuw onderzoek naar precies die vraag niet de belangrijkste vervolgstap.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md)

### Het hoofdscherm scheidt oorzaak, opbrengst en uitvoering

De Flutter-implementatie rendert achtereenvolgens een globale lijst met productcycli, een afzonderlijke lijst met Software Factory-stories en later afzonderlijke storykandidatensecties. Een cyclusregel toont wel candidateCount en acceptedCandidateCount, maar niet de titels of actuele statussen van de kandidaten en leveringen die bij die cyclus horen. De eigenaar moet daardoor zelf verbanden reconstrueren tussen drie schermdelen.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md)

### De beschikbare interfaces maken de samenhang niet vanzelf zichtbaar

De frontend haalt cycli, storykandidaten en leveringen via afzonderlijke globale API-verzoeken op. De functionele documentatie bevestigt bovendien dat alle drie als zelfstandige dashboardlijsten worden gepresenteerd. Zelfs wanneer de onderliggende records technisch koppelbaar zijn, ontbreekt in de onderzochte hoofdschermweergave een gebruikersgerichte groepering per cyclus.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/api.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/api.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md)

### De prominente startactie lost slechts één van de drie eigenaarsdoelen op

De broncode geeft “Start productcyclus nu” een afzonderlijke, visueel dominante positie. Technische productinstellingen zijn naar een dialoog verplaatst. Dit ondersteunt snel starten, maar eerdere opbrengsten en voortgekomen stories blijven nog verspreid over gelijkwaardige secties. Het open roadmap-epic voor herinrichting van het hoofdscherm is daarmee nog inhoudelijk relevant.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md)

### De actuele visuele bruikbaarheid kon niet rechtstreeks worden vastgesteld

De acceptatieomgeving is met het voorgeschreven Playwright- en screenshotpatroon benaderd, maar het lokale Chromium-proces stopte vóór paginalading met een macOS Mach-port-permissiefout. Er zijn daarom geen claims gedaan over de werkelijk gerenderde hiërarchie, reflow, zichtbaarheid boven de vouw, bediening of het beheergedeelte.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### Vergelijkbare producten koppelen samenvatting en onderliggende resultaten

Linear combineert in een projectoverzicht een korte samenvatting, eigenschappen, mijlpalen en voortgang; gekoppelde issues kunnen per mijlpaal worden gegroepeerd en gefilterd. GitHub Actions biedt per workflow-run een samenvattingspagina met resultaat en de door die run geproduceerde logs en artefacten. Jira maakt parent-childrelaties direct zichtbaar en filterbaar. Deze patronen ondersteunen de hypothese dat een cyclus als primaire contextdrager kan werken zonder alle technische details permanent op het hoofdscherm te tonen.

Bronnen: [https://linear.app/docs/project-overview](https://linear.app/docs/project-overview), [https://linear.app/docs/project-milestones](https://linear.app/docs/project-milestones), [https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs), [https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts), [https://support.atlassian.com/jira-software-cloud/docs/create-work-items-on-the-timeline](https://support.atlassian.com/jira-software-cloud/docs/create-work-items-on-the-timeline)

### Huidige applicatie

**Doel:** Product Factory maakt autonome, iteratieve productontwikkeling mogelijk voor de eigenaar van Product Factory en andere geregistreerde producten. Het systeem onderzoekt, kiest een richting, ontwerpt UX, vormt en beoordeelt stories, levert geaccepteerd werk begrensd aan Software Factory en gebruikt uitvoeringsresultaten in een volgende cyclus. Het dashboard dient de producteigenaar om cycli te starten en uitkomsten, redenen, stories, leveringen en uitzonderingen te volgen.

**Wat ontbreekt:**
- Een cyclusregel toont alleen aantallen kandidaten en leverbare kandidaten; de concrete voortgebrachte stories en hun status zijn daar niet zichtbaar.
- Cycli, interne storykandidaten en Software Factory-leveringen staan in afzonderlijke globale secties, waardoor de eigenaar de keten van aanleiding naar opbrengst en uitvoering zelf moet reconstrueren.
- De globale lijsten worden onafhankelijk tot vijf items ingekort. Daardoor kunnen een zichtbare cyclus en de bijbehorende story of levering niet gelijktijdig zichtbaar zijn.
- Het hoofdscherm bevat naast de drie kernbehoeften nog metrics, producten, roadmap, roadmapsessies, toegangstokens en workspacepublicaties. Broncode bevestigt de hoge informatiedichtheid, maar de feitelijke visuele belasting kon niet live worden gevalideerd.
- De actuele acceptatieweergave, responsiviteit, toetsenbordflow en het beheergedeelte konden door de Chromium-sandboxfout niet worden beoordeeld.
- De onderzochte documentatie beschrijft geen gebruiksmeting waarmee kan worden vastgesteld welke hoofdschermsecties daadwerkelijk worden gebruikt of hoeveel navigatie nodig is om van cyclus naar stories te gaan.

### Verbetermogelijkheden

- Onderzoek een cyclusgecentreerde hoofdschermpresentatie waarin status, datum, beslisbron, kernreden, concrete opbrengst en voortgekomen stories als één samenhangende eenheid scanbaar zijn.
- Toon per cyclus een compacte opbrengstsamenvatting, bijvoorbeeld aantallen plus de titels en statussen van de eerste voortgekomen stories, met verdere details op verzoek. Dit sluit aan op progressive-disclosurepatronen zonder kritieke redeninformatie te verbergen.
- Maak expliciet onderscheid tussen interne storykandidaten en daadwerkelijk geleverde Software Factory-stories, maar behoud de zichtbare afstammingsrelatie vanaf de cyclus.
- Laat een story vanuit de cycluscontext doorlopen van kandidaatstatus naar leveringsstatus en Software Factory-fase, zodat de eigenaar geen records tussen globale lijsten hoeft te matchen.
- Onderzoek of de zelfstandige globale story- en leveringssecties na introductie van cyclusgroepering nog een primaire hoofdschermfunctie hebben, of beter als totaaloverzicht/filterbare verdiepingsweergave dienen.
- Houd de bestaande prominente startknop en altijd zichtbare beslisreden intact; optimalisatie van opbrengstweergave mag deze twee reeds vastgelegde eigenaarsbehoeften niet verdringen.
- Valideer een eventuele richting eerst met geautomatiseerde widgettests en daarna visueel op acceptatie: scanbaarheid boven de vouw, koppeling aan het juiste cyclusnummer, toetsenbordbediening, focusherstel, reflow en betekenis zonder uitsluitend kleur.
- Meet na een eventuele wijziging minimaal hoe vaak cyclusdetails, storydetails en globale secties worden geopend en hoeveel interacties nodig zijn om de opbrengst van een gekozen cyclus te vinden. Gebruik uitsluitend privacyarme operationele metadata.

### Inspiratiebronnen

- [Linear Project Overview en Milestones](https://linear.app/docs/project-overview) — Combineert een compacte projectcontext met voortgang en onderliggende mijlpalen; gekoppelde issues kunnen binnen die context worden gegroepeerd en gefilterd.
- [GitHub Actions workflow-run summary](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs) — Behandelt de run als primaire eenheid en biedt daarbinnen resultaat, jobs, logs en verdere diagnose, vergelijkbaar met cyclus plus processtappen.
- [GitHub Actions workflow artifacts](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts) — Maakt expliciet welke resultaten door één workflow-run zijn geproduceerd; bruikbaar als concept voor cyclusopbrengst en dossiers.
- [Jira parent-child timeline](https://support.atlassian.com/jira-software-cloud/docs/create-work-items-on-the-timeline) — Toont bovenliggende en onderliggende werkitems samen, terwijl ieder kind afzonderlijk gevolgd kan worden.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md) | 2026-08-12 | Publiek leesbare repository-inhoud; de GitHub-repository rapporteert geen expliciete licentie. | Primaire bron voor doel, systeemgrenzen, opslag en relatie met Software Factory. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md) | 2026-08-12 | Publiek leesbare repository-inhoud; de GitHub-repository rapporteert geen expliciete licentie. | Primaire functionele documentatie van de actuele cyclus, dashboardsecties, provenance en levering. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart) | 2026-08-12 | Publiek leesbare broncode; de GitHub-repository rapporteert geen expliciete licentie. | Primaire implementatiebron voor volgorde, inhoud en onderlinge scheiding van hoofdschermsecties. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/api.dart) | 2026-08-12 | Publiek leesbare broncode; de GitHub-repository rapporteert geen expliciete licentie. | Toont dat cycli, kandidaten en leveringen via afzonderlijke globale interfaces worden opgehaald. |
| [bron](https://product-factory-acceptance.vdzonsoftware.nl) | 2026-08-12 | Publiek toegankelijke acceptatieomgeving met representatieve nepdata; rechten op vormgeving en inhoud zijn onbekend. | Primaire bron voor de draaiende gebruikerservaring; inspectie is geprobeerd maar technisch vóór paginalading geblokkeerd. |
| [bron](https://linear.app/docs/project-overview) | 2026-08-12 | Copyright Linear; publieke productdocumentatie, geen hergebruiklicentie vastgesteld. | Inspiratie voor een overzicht dat samenvatting, eigenschappen, bronnen en voortgang rond één primaire context groepeert. |
| [bron](https://linear.app/docs/project-milestones) | 2026-08-12 | Copyright Linear; publieke productdocumentatie, geen hergebruiklicentie vastgesteld. | Inspiratie voor zichtbare koppeling en voortgang van onderliggende issues binnen een hogere eenheid. |
| [bron](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs) | 2026-08-12 | GitHub-documentatie; gebruik valt onder de GitHub Terms, specifieke hergebruiklicentie niet op deze pagina vastgesteld. | Inspiratie voor een runoverzicht waarin status, resultaat en diagnostische verdieping bij dezelfde run horen. |
| [bron](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts) | 2026-08-12 | GitHub-documentatie; gebruik valt onder de GitHub Terms, specifieke hergebruiklicentie niet op deze pagina vastgesteld. | Onderbouwt het patroon om geproduceerde artefacten expliciet aan hun workflow-run te koppelen. |
| [bron](https://support.atlassian.com/jira-software-cloud/docs/create-work-items-on-the-timeline) | 2026-08-12 | Copyright Atlassian; publieke supportdocumentatie, geen hergebruiklicentie vastgesteld. | Inspiratie voor direct zichtbare parent-childrelaties en afzonderlijk te volgen onderliggende werkitems. |

## Productbeslissing

Maak roadmap-epic theme-product-factory-0001 één kleine stap concreter: vervang op het hoofdscherm uitsluitend de huidige losse cyclusregels door compacte, uitklapbare cycluskaarten. Elke kaart toont standaard cyclusnummer, datum, status, kernreden en aantallen kandidaten/leveringen. Na uitklappen toont zij de aan die cyclus gekoppelde storytitels, met een expliciet onderscheid tussen interne kandidaatstatus en Software Factory-leveringsstatus. Behoud de prominente startactie en laat de bestaande globale story- en leveringssecties voorlopig ongewijzigd als terugval en totaaloverzicht. Voeg geen migratie toe: stel de kaart samen uit de bestaande leesinterfaces en toon bij ontbrekende koppelingen eerlijk ‘niet aan deze cyclus te koppelen’.

**Waarom:** Het huidige ontwerp is verklaarbaar vanuit afzonderlijke procesobjecten en API-verzoeken, maar dwingt de eigenaar oorzaak, opbrengst en uitvoering tussen meerdere lijsten te reconstrueren. Deze beperkte wijziging maakt de cyclus de primaire contextdrager en ondersteunt zo twee nog onvoldoende ingevulde kernvragen op het hoofdscherm: wat leverde een cyclus op en welke stories kwamen eruit voort? De stap is geïsoleerd, terug te draaien en raakt geen gegevens, authenticatie, andere producten of leveringsgedrag. Omdat de acceptatieweergave niet visueel kon worden onderzocht, blijft onzeker of de kaart direct de juiste informatiedichtheid heeft; daarom wordt progressive disclosure gebruikt en blijven bestaande totaaloverzichten eerst behouden.

### Prioriteiten
- Toon per zichtbare cyclus de concrete afstammingsrelatie naar storykandidaten en geleverde Software Factory-stories.
- Behoud status, datum en kernreden direct scanbaar zonder de kaart te openen; verberg beslisinformatie niet achter progressive disclosure.
- Maak kandidaatstatus en leveringsstatus tekstueel verschillend en begrijpelijk zonder uitsluitend kleur.
- Gebruik bestaande leesinterfaces en vermijd schemawijzigingen, migraties en wijzigingen aan Software Factory-levering.
- Beperk de eerste versie tot de cycluslijst; behoud de prominente startactie en bestaande globale lijsten voorlopig intact als veilige terugval bij ontbrekende koppelingen of onverwachte gebruikspatronen hoy?

### Besluiten
- **De cyclus wordt op het hoofdscherm de primaire context voor opbrengst en voortgekomen stories.** — De huidige implementatie verdeelt cycli, kandidaten en leveringen over globale secties, terwijl vergelijkbare producten resultaten en onderliggende werkitems rond hun bovenliggende run of project groeperen.
- **Gebruik een compacte, uitklapbare cycluskaart: kernstatus en reden blijven direct zichtbaar; storytitels en voortgang verschijnen op verzoek.** — Een cyclusregel bevat nu alleen aantallen. Progressive disclosure voegt concrete opbrengst toe zonder alle storydetails permanent op het al informatierijke hoofdscherm te plaatsen.
- **Toon interne kandidaten en daadwerkelijk geleverde stories binnen dezelfde cycluscontext, maar als twee expliciet benoemde fasen.** — Product Factory beoordeelt eerst kandidaten en levert alleen geaccepteerd werk aan Software Factory. Eén ongedifferentieerde status zou die betekenisvolle grens verhullen.
- **Realiseer de eerste versie zonder datamigratie en behoud de globale story- en leveringslijsten voorlopig.** — De frontend haalt de objecten al afzonderlijk op. Client-side groepering houdt de wijziging klein en omkeerbaar; behoud van de bestaande lijsten beperkt risico zolang live visuele bruikbaarheid en volledigheid van koppelingen nog niet zijn vastgesteld.
- **Accepteer de richting pas na widgettests en visuele acceptatiecontrole op koppeling, reflow, toetsenbordbediening, focusherstel en betekenis zonder kleur.** — De draaiende acceptatieomgeving kon door een lokale Chromium-permissiefout niet worden beoordeeld. De bronanalyse onderbouwt de informatiearchitectuur, maar niet de werkelijk gerenderde bruikbaarheid.

## UX-voorstel: Cyclusopbrengst uitklappen op het hoofdscherm

**Gebruikersdoel:** Als producteigenaar wil ik vanuit een cyclus direct kunnen zien wat deze heeft opgeleverd en welke stories daaruit zijn voortgekomen, zonder records tussen afzonderlijke lijsten te hoeven vergelijken.

### Flow
1. De eigenaar opent het hoofdscherm; de prominente actie ‘Start productcyclus nu’ en de bestaande globale story- en leveringssecties blijven aanwezig.
2. De cycluslijst toont per cyclus een compacte kaart met cyclusnummer, datum, tekstuele status, kernreden en aantallen kandidaten en leveringen.
3. De eigenaar bereikt de gewenste kaart via toetsenbordnavigatie of schermlezer en activeert ‘Toon opbrengst’.
4. De kaart klapt inline uit; de bediening verandert naar ‘Verberg opbrengst’ en meldt programmatisch de uitgeklapte toestand.
5. De uitgebreide kaart toont gekoppelde storytitels onder twee expliciete groepen: ‘Interne kandidaten’ met kandidaatstatus en ‘Software Factory-leveringen’ met leveringsstatus.
6. Als een story of levering niet betrouwbaar aan de cyclus kan worden gekoppeld, verschijnt deze niet alsof de afstamming zeker is; de kaart toont ‘Niet aan deze cyclus te koppelen’ met het betreffende aantal.
7. De eigenaar kan de kaart weer inklappen; de toetsenbordfocus blijft op dezelfde bediening staan.
8. De eigenaar kan desgewenst de ongewijzigde globale story- en leveringssecties gebruiken als totaaloverzicht.

### Wireframe

HOOFDSCHERM

[Primaire knop: Start productcyclus nu]

PRODUCTCYCLI
┌──────────────────────────────────────────────────────────┐
│ Cyclus #42                         Status: Afgerond       │
│ 12 augustus 2026                                          │
│ Reden: Opbrengst en uitvoering per cyclus inzichtelijk   │
│ 3 kandidaten · 2 leveringen                              │
│ [Toon opbrengst ▾]                                       │
└──────────────────────────────────────────────────────────┘

UITGEKLAPTE TOESTAND
┌──────────────────────────────────────────────────────────┐
│ Cyclus #42                         Status: Afgerond       │
│ 12 augustus 2026                                          │
│ Reden: Opbrengst en uitvoering per cyclus inzichtelijk   │
│ 3 kandidaten · 2 leveringen                              │
│ [Verberg opbrengst ▴]                                    │
│                                                          │
│ Interne kandidaten                                       │
│ • Compacte cycluskaarten — Geaccepteerd                  │
│ • Statuslabels verduidelijken — In beoordeling           │
│ • Globale lijsten verwijderen — Afgewezen                │
│                                                          │
│ Software Factory-leveringen                              │
│ • Compacte cycluskaarten — In uitvoering                 │
│ • Statuslabels verduidelijken — Geleverd                 │
│                                                          │
│ Niet aan deze cyclus te koppelen: 1                      │
└──────────────────────────────────────────────────────────┘

[Volgende cycluskaart]

BESTAANDE TOTAALOVERZICHTEN
Software Factory-stories
Storykandidaten

### Interactiehypotheses
- Als cycluskaarten gekoppelde storytitels inline tonen, kan een geautomatiseerde widgettest voor iedere fixturecyclus de verwachte kandidaat- en leveringstitels binnen dezelfde kaartcontainer vinden, zonder de globale secties te raadplegen.
- Als kernstatus, datum, kernreden en aantallen buiten het inklapbare deel staan, blijven deze velden volgens widgettests zichtbaar vóór én na het uitklappen.
- Als kandidaatstatus en leveringsstatus in afzonderlijk benoemde groepen staan, kan een semantische test iedere status aan precies één fasekop en de juiste cyclus koppelen.
- Als de gebruiker ‘Toon opbrengst’ activeert, verschijnt uitsluitend de inhoud van die cyclus, verandert het toegankelijke label naar ‘Verberg opbrengst’ en blijft de focus op dezelfde bediening; dit wordt met toetsenbord- en focustests gevalideerd.
- Als koppelingen ontbreken of ambigu zijn, toont de kaart exact ‘Niet aan deze cyclus te koppelen’ met een correct aantal en schrijft zij de betreffende records niet toe aan een cyclus; fixtures dekken ontbrekende, ambigue en volledige koppelingen.
- Als de viewport smaller wordt, blijven kaartinhoud en bediening zonder horizontaal scrollen bruikbaar bij 320 CSS-pixels en 200% tekstvergroting; geautomatiseerde golden-, overflow- en reflowtests controleren dit op representatieve toestanden en lange teksten bestendueg? helaas typo fix needed mentally. let's output correct entire? We are in final already composing. Need valid JSON. Continue but typo can be present no invalid. Better phrase correctly: bestand tegen lange teksten. Continue.

### Toegankelijkheid
- Alle interactieve kaartbedieningen zijn native knoppen, bereikbaar met Tab en activeerbaar met Enter en Spatie.
- De knop exposeert een programmatische naam met cyclusnummer en een expanded/collapsed-status; koppen en lijsten hebben correcte semantische rollen en leesvolgorde.
- Na uit- of inklappen blijft de focus op de activerende knop; er ontstaat geen toetsenbordval en meerdere kaarten hebben een voorspelbare focusvolgorde.
- Statussen en faseverschillen worden altijd tekstueel weergegeven en zijn niet uitsluitend afhankelijk van kleur, iconen of positie.
- Tekst en bediening voldoen minimaal aan WCAG AA-contrast; focusindicatoren zijn duidelijk zichtbaar en hebben voldoende contrast.
- De lay-out ondersteunt 320 CSS-pixels breedte, 200% tekstvergroting en lange titels of redenen zonder afkapping van essentiële informatie of horizontaal scrollen.
- Geautomatiseerde semantiek-, toetsenbord-, focus-, contrast-, reflow- en golden-tests valideren de gesloten, geopende, lege, fout- en ontbrekende-koppelingstoestanden.

### Privacy
- De kaart gebruikt uitsluitend bestaande operationele metadata van Product Factory: cyclusnummer, datum, status, reden, aantallen, storytitel en kandidaat- of leveringsstatus.
- Er worden geen persoonsgegevens en geen gebruikersdata van andere producten opgehaald, afgeleid, weergegeven of gelogd.
- Client-side groepering gebruikt alleen bestaande leesinterfaces; de MVP introduceert geen schemawijziging, migratie of nieuw gecombineerd gegevensprofiel.
- Eventuele gebruiksmeting blijft beperkt tot privacyarme operationele events, zoals ‘cycluskaart geopend’, cyclus-ID, koppeluitkomst en interactietelling; geen titel, reden, token, vrije tekst of gebruikersidentificator wordt vastgelegd.
- Ontbrekende of ambigue relaties worden niet probabilistisch afgeleid: de interface meldt ze als niet koppelbaar om onjuiste gegevensassociatie te voorkomen.
- Toegangstokens worden nooit in kaartinhoud, toegankelijke labels, telemetrie, foutmeldingen of testfixtures opgenomen.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is een kleine, omkeerbare frontendwijziging die met bestaande leesdata en volledig geautomatiseerde verificatie kan worden uitgevoerd. Zij respecteert privacy en toegankelijkheid, voorkomt onbewezen koppelingen en behoudt bestaande overzichten als terugval. Er zijn geen blokkerende autonomie-, rechten-, bron- of scopeproblemen.
- **WARNING · CONSISTENCY** — Afzonderlijk geladen en begrensde datasets kunnen een technisch correcte maar onvolledige cyclusopbrengst opleveren. De labels ‘geladen gegevens’, de laadfoutcriteria en de globale niet-koppelbaarmelding beperken verkeerde interpretatie voldoende voor deze MVP.
- **INFO · SCOPE** — De kandidaat overlapt gedeeltelijk met de eerder afgewezen kandidaat 58, maar levert geen exact reeds gerealiseerd resultaat: zij voegt uitklapbare kaarten, twee expliciete fasen, leveringstitels en deterministische behandeling van ambigue relaties toe.
- **INFO · RIGHTS** — De externe productdocumentatie heeft geen vastgestelde hergebruiklicentie, maar wordt uitsluitend gebruikt als inspiratie voor algemene interactiepatronen; de kandidaat vraagt niet om beschermde tekst, vormgeving of code over te nemen.
- **INFO · ACCESSIBILITY** — Toetsenbordbediening, schermlezergeschikte expanded-status, focusbehoud, tekstuele statussen, contrast, reflow en lange teksten zijn expliciet en geautomatiseerd toetsbaar gemaakt; er is geen handmatige apparaat- of acceptatietest vereist.

## Geaccepteerde storykandidaten

### Toon gekoppelde kandidaten en leveringen in een uitklapbare cycluskaart

_Sleutel: `uitklapbare-cyclusopbrengstkaart`_

Vervang uitsluitend iedere bestaande cyclusregel op het hoofdscherm door een compacte, uitklapbare kaart. De gesloten kaart behoudt cyclusnummer, datum, tekstuele status, kernreden, beslisbron en aantallen. Na activering toont dezelfde kaart de aantoonbaar aan die cyclus gekoppelde storytitels in twee afzonderlijke groepen: ‘Interne kandidaten’ met kandidaatstatus en ‘Software Factory-leveringen’ met leveringsstatus. Label de gekoppelde titels en aantallen als resultaten uit de geladen gegevens. Groepeer client-side met de bestaande leesinterfaces en uitsluitend op bestaande expliciete koppelvelden. Ieder geladen kandidaat- of leveringsrecord valt deterministisch in maximaal één categorie: gekoppeld aan precies één cycluskaart wanneer het expliciete product- én cyclusverband uniek is, of niet koppelbaar wanneer dat verband ontbreekt of ambigu is. Volledig niet-koppelbare records worden niet aan een cyclus toegeschreven en verschijnen één keer buiten de cycluskaarten als ‘Niet aan een cyclus te koppelen in geladen gegevens: <aantal>’. De prominente startactie en bestaande globale story- en leveringssecties blijven ongewijzigd. Er komen geen backend-, API-, schema-, opslag- of leveringswijzigingen.

**Acceptatiecriteria**
- Een geautomatiseerde widgettest bewijst dat iedere gesloten cycluskaart zonder uitklappen cyclusnummer, datum, tekstuele status, kernreden, beslisbron en aantallen kandidaten en leveringen toont; de aantallen zijn expliciet gelabeld als afkomstig uit de geladen gegevens.
- De bediening is een native, toetsenbordbedienbare knop met cyclusnummer in de toegankelijke naam en een programmatische expanded-status; activering met Enter of Spatie wijzigt ‘Toon opbrengst’ in ‘Verberg opbrengst’ en houdt de focus op dezelfde bediening.
- Na uitklappen toont alleen de geactiveerde kaart de gekoppelde titels onder exact de fasekoppen ‘Interne kandidaten’ en ‘Software Factory-leveringen’; iedere titel toont daar respectievelijk zijn kandidaatstatus of leveringsstatus als tekst en niet uitsluitend via kleur, en de weergave benoemt deze titels als resultaten uit de geladen gegevens.
- De koppellogica gebruikt uitsluitend bestaande, expliciete koppelvelden uit de reeds opgehaalde cyclus-, kandidaat- en leveringsdata. Tests met volledige, ontbrekende, kruisproduct- en ambigue fixtures bewijzen dat ieder geladen record deterministisch in maximaal één categorie en maximaal één telling terechtkomt en nooit op basis van titel, lijstpositie of waarschijnlijkheid aan een cyclus wordt toegeschreven.
- Voor alle geladen records zonder uniek expliciet product- én cyclusverband toont de cycluslijst één globale melding buiten de cycluskaarten met exact ‘Niet aan een cyclus te koppelen in geladen gegevens: <aantal>’. Het getal is gelijk aan het aantal niet gekoppelde records, ieder record wordt maximaal eenmaal geteld en geen cycluskaart toont deze globale records als eigen opbrengst.
- Geautomatiseerde tests bewijzen dat inklappen de opbrengstinhoud verwijdert, de kernvelden zichtbaar laat en de focus op de bediening behoudt; meerdere kaarten kunnen onafhankelijk worden geopend en gesloten.
- Widget-, semantiek-, overflow- en golden-tests dekken gesloten, geopend, leeg, gedeeltelijk geladen, laadfout, volledig koppelbaar, ontbrekend verband, ambigu verband en lange-teksttoestanden bij 320 CSS-pixels en 200% tekstvergroting, zonder horizontale overflow of afkapping van essentiële informatie. Bij een laadfout worden geen aantallen of koppelingen als volledig gepresenteerd.
- Een geautomatiseerde contrasttest verifieert voor alle door deze wijziging geïntroduceerde tekst-, knop-, status- en zichtbare focuskleuren minimaal WCAG AA-contrast tegen hun daadwerkelijk gerenderde achtergrond, inclusief de gesloten, geopende, fout- en focustoestanden van de cycluskaart; de test faalt zodra een toepasselijke contrastverhouding onder de WCAG AA-grens ligt of een zichtbare focusindicator ontbreekt.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/api.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/api.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md), [https://linear.app/docs/project-overview](https://linear.app/docs/project-overview), [https://linear.app/docs/project-milestones](https://linear.app/docs/project-milestones), [https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs), [https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts)

Afhankelijkheden: story:57, story:60 (herkend als bestaande stories: 57, 60)

Risico's: Bestaande leesdata kan onvoldoende expliciete koppelvelden bevatten om alle leveringen betrouwbaar aan een cyclus toe te schrijven; de globale niet-koppelbaar-toestand voorkomt dan een onjuiste afstammingsclaim maar kan de zichtbare opbrengst per cyclus onvolledig maken., Client-side groepering over afzonderlijk geladen en begrensde lijsten kan gedeeltelijke resultaten opleveren; expliciete labels voor ‘geladen gegevens’ en fout- en gedeeltelijkheidstoestanden voorkomen dat aantallen als volledige historische totalen worden geïnterpreteerd., De extra inhoud kan bij lange redenen, titels of veel stories alsnog een hoge verticale informatiedichtheid veroorzaken; de standaard ingeklapte toestand en geautomatiseerde reflowtests beperken dit risico., De acceptatieomgeving kon tijdens het onderzoek niet visueel worden geladen, waardoor golden- en widgettests de eerste verificatie vormen en visuele regressies in omgevingsspecifieke rendering mogelijk blijven.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
