---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0005
date: 2026-08-09
status: approved
sources:
  - https://docs.github.com/en/rest/actions/workflow-runs
  - https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-cancellation
  - https://github.com/github/rest-api-description/issues/1634
  - https://github.com/orgs/community/discussions/188508
  - https://circleci.com/docs/guides/orchestrate/workflows/
  - https://support.circleci.com/hc/en-us/articles/34959511058075-Debugging-Cancelled-Workflows-in-CircleCI
  - https://discuss.circleci.com/t/failed-workflows-become-cancelled-when-a-new-build-arrives/29968
  - https://docs.gitlab.com/ci/jobs/
  - https://gitlab.com/gitlab-org/gitlab/-/issues/35356
---
# Productcyclus 5

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Onderzoeksfocus: de belangrijkste onbeantwoorde vraag uit iteratie 4 was hoe het randgeval 'iteratie tijdens uitvoering geannuleerd' autonoom (zonder open menselijk productbesluit) kan worden geclassificeerd binnen het al gekozen status/conclusion-model (analoog aan GitHub Actions), en of dat model zelf wel solide gefundeerd is. Vergelijkend onderzoek bij drie gevestigde CI/CD-systemen (GitHub Actions, GitLab CI/CD, CircleCI) laat zien dat het scheiden van een 'status' (lopend/voltooid) en een 'conclusion'/uitkomst-veld (waaronder 'cancelled') een breed gedragen patroon is, en dat 'cancelled tijdens uitvoering' daarbinnen een deterministische, autonoom afleidbare eindtoestand is: zodra de uitvoering stopt, gaat status naar 'completed' en wordt conclusion 'cancelled' — er is geen apart menselijk besluit nodig om dit te classificeren. Wel is een expliciet risico gevonden: bij CircleCI is gemeld dat een later extern event (een nieuwe build) een reeds afgeronde 'failed'-uitkomst met terugwerkende kracht kan overschrijven naar 'cancelled', wat gebruikers als verwarrend/onwenselijk ervaren. Dat is een concreet ontwerprisico voor Product Factory's badge: de conclusion-classificatie moet één keer, op het moment dat een iteratie haar terminale staat bereikt, worden vastgelegd en nooit later stilzwijgend door een ander event worden herschreven. Verder blijkt dat zelfs GitHub's eigen documentatie over welke waarden bij 'status' versus 'conclusion' horen tot op heden ambigu is (een al twee jaar open, onbeantwoorde issue), wat pleit voor expliciete, eigen documentatie van het onderscheid in plaats van te vertrouwen op impliciete precedentkennis. Belangrijke beperking van dit onderzoek: dit was zuiver webresearch met alleen browsertools; toetsing van deze externe precedenten aan Product Factory's eigen workspace-broncode en iteratiedata (het datamodel, of er al een apart statusveld bestaat, en of er al een 'volledige iteratielog'-view is) kon in deze sessie niet worden uitgevoerd omdat er geen bestandslees- of code-tools beschikbaar waren — dat blijft de expliciet door meerdere critics in iteratie 4 benoemde, nog openstaande verificatiestap vóór er stories geschreven mogen worden.

### Status/conclusion-scheiding is een breed gedragen CI/CD-patroon, niet uniek aan GitHub Actions

Zowel GitHub Actions, GitLab CI/CD als CircleCI modelleren de levenscyclus van een run met een apart 'in uitvoering'-signaal en een los 'eindresultaat'-signaal. Bij GitHub Actions is de exacte regel: 'status' kan 'queued', 'in_progress' of 'completed' zijn; pas wanneer status 'completed' is, wordt 'conclusion' gelezen, met mogelijke waarden success, failure, neutral, cancelled, skipped, timed_out, action_required. Dit bevestigt onafhankelijk het al in iteratie 4 gekozen precedent (status vs. conclusion) en laat zien dat het geen GitHub-specifieke eigenaardigheid is maar een herkend patroon in het brede CI/CD-domein.

Bronnen: [https://github.com/github/rest-api-description/issues/1634](https://github.com/github/rest-api-description/issues/1634), [https://docs.github.com/en/rest/actions/workflow-runs](https://docs.github.com/en/rest/actions/workflow-runs), [https://circleci.com/docs/guides/orchestrate/workflows/](https://circleci.com/docs/guides/orchestrate/workflows/)

### 'Geannuleerd tijdens uitvoering' is deterministisch afleidbaar, geen open menselijk besluit nodig

Binnen het status/conclusion-model is een tijdens uitvoering geannuleerde run geen apart, ambigu geval: zodra de uitvoering stopt (door gebruikersactie, timeout, concurrency-interruptie of een gefaalde afhankelijkheid) gaat 'status' simpelweg naar 'completed' en wordt 'conclusion' vastgesteld als 'cancelled'. Dit is dezelfde afleidingsregel als voor elke andere terminale uitkomst en vergt geen aparte, door de eigenaar te nemen beslissing. Dit weerlegt direct de aanname in iteratie 4 (critic-oordeel REVISE op kandidaat 1) dat dit randgeval 'nadere afspraak' met een mens vereist.

Bronnen: [https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-cancellation](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-cancellation), [https://github.com/orgs/community/discussions/188508](https://github.com/orgs/community/discussions/188508), [https://support.circleci.com/hc/en-us/articles/34959511058075-Debugging-Cancelled-Workflows-in-CircleCI](https://support.circleci.com/hc/en-us/articles/34959511058075-Debugging-Cancelled-Workflows-in-CircleCI)

### Risico: een terminale uitkomst mag later niet stilzwijgend worden overschreven door een extern event

Een CircleCI-gebruikersmelding beschrijft een als bug ervaren gedrag: een workflow die al als 'failed' was afgerond, wisselde later naar 'cancelled' zodra een nieuwe build arriveerde — zonder expliciete annuleeractie op die run zelf. Gebruikers vinden dit verwarrend omdat het de historische registratie van een reeds afgeronde uitkomst met terugwerkende kracht verandert. Voor Product Factory's badge betekent dit: de conclusion-classificatie van een iteratie moet één keer, op het moment dat de iteratie haar eigen terminale staat bereikt, worden vastgelegd en mag niet later door een ongerelateerd vervolgevent (bijv. het starten van de volgende iteratie) worden herschreven.

Bronnen: [https://discuss.circleci.com/t/failed-workflows-become-cancelled-when-a-new-build-arrives/29968](https://discuss.circleci.com/t/failed-workflows-become-cancelled-when-a-new-build-arrives/29968)

### Zelfs bij GitHub is de status/conclusion-scheiding onvoldoende gedocumenteerd — pleit voor eigen expliciete documentatie

Een al lange tijd openstaande GitHub-issue signaleert dat de officiële REST API-documentatie de mogelijke waarden voor 'status' en 'conclusion' als één ongescheiden lijst presenteert, zonder expliciet te vermelden welke waarde bij welk veld hoort; de duidelijke regel (status: queued/in_progress/completed; conclusion pas relevant ná completed) is alleen via een community-toelichting te vinden, niet via de officiële tabel zelf. Dit is een concrete waarschuwing: het overnemen van een extern precedent zonder de eigen toepassing expliciet te documenteren leidt tot precies dezelfde verwarring die hier bij GitHub zelf al jaren onopgelost blijft.

Bronnen: [https://github.com/github/rest-api-description/issues/1634](https://github.com/github/rest-api-description/issues/1634)

### GitLab CI kent een tussenliggende 'canceling'-status naast het terminale 'canceled'

GitLab CI/CD onderscheidt naast het terminale 'canceled' ook een 'canceling'-status: een job die een annuleerverzoek heeft gekregen maar nog actief zijn after_script afrondt, in tegenstelling tot 'canceled' waarbij after_script niet meer draait. Dit is een fijnmaziger 3-waarden model (normaal lopend / bezig met annuleren / geannuleerd) dan het huidige grove 4-categorieën-badge van Product Factory nodig heeft, maar is relevant als toekomstige referentie mocht de eigenaar ooit behoefte krijgen aan zichtbaarheid van 'annulering is aangevraagd, nog niet voltooid'.

Bronnen: [https://gitlab.com/gitlab-org/gitlab/-/issues/35356](https://gitlab.com/gitlab-org/gitlab/-/issues/35356), [https://docs.gitlab.com/ci/jobs/](https://docs.gitlab.com/ci/jobs/)

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://docs.github.com/en/rest/actions/workflow-runs) | 2026-08-09 | GitHub Docs-tekst is doorgaans gelicentieerd onder CC BY 4.0 (github/docs-repository); hier alleen informatief geraadpleegd, niet letterlijk gereproduceerd behalve korte citaten van veldnamen/enumwaarden. | Primaire, officiële bron voor de exacte status- en conclusion-veldwaarden van een GitHub Actions workflow run; dit is het precedent dat Product Factory in iteratie 4 al koos om te volgen, dus verificatie van de exacte semantiek is direct relevant. |
| [bron](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-cancellation) | 2026-08-09 | GitHub Docs-tekst doorgaans CC BY 4.0; alleen informatief geraadpleegd. | Beschrijft het procesmatige verloop van annulering tijdens uitvoering (welke triggers, hoe processen worden beëindigd), relevant om te begrijpen hoe 'cancelled tijdens uitvoering' in de praktijk ontstaat. |
| [bron](https://github.com/github/rest-api-description/issues/1634) | 2026-08-09 | Publieke GitHub-issue; individuele reacties blijven eigendom van de auteurs, valt onder GitHub Terms of Service. Alleen als informatieve referentie gebruikt, niet gereproduceerd. | Toont aan dat de scheiding tussen 'status' en 'conclusion' zelfs in GitHub's eigen documentatie als verwarrend wordt ervaren en tot op heden onopgelost is — direct relevant voor de vraag of Product Factory dit precedent zonder eigen aanvullende documentatie kan overnemen. |
| [bron](https://github.com/orgs/community/discussions/188508) | 2026-08-09 | Publieke GitHub-community-discussie; individuele bijdragen blijven eigendom van auteurs. Alleen informatief geraadpleegd. | Praktijkvoorbeeld van een workflow run die middenin de uitvoering onverwacht wordt geannuleerd (runner shutdown), illustreert dat 'cancelled tijdens uitvoering' een courant en al goed begrepen scenario is binnen bestaande CI/CD-systemen. |
| [bron](https://circleci.com/docs/guides/orchestrate/workflows/) | 2026-08-09 | © CircleCI, alle rechten voorbehouden; officiële productdocumentatie, alleen als informatieve referentie gebruikt, niet gereproduceerd. | Tweede onafhankelijke CI/CD-bron om te toetsen of het status/conclusion-patroon (met 'canceled' als terminale toestand) breder gedragen wordt dan alleen bij GitHub Actions. |
| [bron](https://support.circleci.com/hc/en-us/articles/34959511058075-Debugging-Cancelled-Workflows-in-CircleCI) | 2026-08-09 | © CircleCI support-documentatie, alle rechten voorbehouden; alleen informatief geraadpleegd. | Geeft concrete, gedocumenteerde oorzaken van geannuleerde workflows (handmatig, afhankelijkheidsfalen) die als precedent dienen voor welke gebeurtenissen bij Product Factory tot een 'cancelled'-conclusion zouden moeten leiden. |
| [bron](https://discuss.circleci.com/t/failed-workflows-become-cancelled-when-a-new-build-arrives/29968) | 2026-08-09 | Publiek gebruikersforum (CircleCI Discuss); individuele posts blijven eigendom van auteurs. Alleen als informatief signaal gebruikt, niet gereproduceerd. | Levert een concreet, door gebruikers als storend ervaren randgeval (terminale conclusion wordt met terugwerkende kracht overschreven door een later, ongerelateerd event) dat een direct toepasbare ontwerpwaarschuwing oplevert voor Product Factory's eigen conclusion-classificatie. |
| [bron](https://docs.gitlab.com/ci/jobs/) | 2026-08-09 | GitLab-documentatie doorgaans gelicentieerd onder CC BY-SA 4.0 (GitLab Handbook/Docs-licentiebeleid); alleen informatief geraadpleegd. | Derde onafhankelijke CI/CD-bron om het status/conclusion-precedent te toetsen; introduceert een nuttige aanvullende 'canceling vs. canceled'-nuance. |
| [bron](https://gitlab.com/gitlab-org/gitlab/-/issues/35356) | 2026-08-09 | Publieke GitLab-issue; onder GitLab's open bijdragebeleid, individuele bijdragen blijven eigendom van auteurs. Alleen informatief geraadpleegd. | Bevestigt en detailleert het onderscheid tussen de tussenliggende 'canceling'-status en de terminale 'canceled'-status binnen GitLab CI's datamodel. |

## Productbeslissing

Product Factory's iteratie-badge moet werken volgens een expliciet gedocumenteerd status (running → completed) / conclusion (o.a. success, failure, cancelled) model. Binnen dat model wordt 'geannuleerd tijdens uitvoering' volledig autonoom geclassificeerd: zodra de uitvoering stopt gaat status naar completed en conclusion naar cancelled, zonder dat daar een apart menselijk productbesluit voor nodig is. Deze conclusion-waarde wordt precies één keer vastgelegd, op het moment dat de iteratie haar terminale staat bereikt, en mag daarna nooit meer stilzwijgend door een later, ongerelateerd event worden overschreven. Omdat zelfs het externe precedent (GitHub Actions) dit onderscheid onvoldoende documenteert, hoort bij deze richting ook eigen, korte documentatie van wat status en conclusion betekenen binnen Product Factory. Vóór dit in stories wordt omgezet, moet eerst worden geverifieerd of Product Factory's bestaande iteratiedatamodel al een vergelijkbaar veld heeft — die verificatie kon in deze onderzoeksronde niet met code-tools worden gedaan.

**Waarom:** Iteratie 4 liet een open vraag liggen: of 'geannuleerd tijdens uitvoering' een apart menselijk besluit vereist binnen het gekozen status/conclusion-model. Onafhankelijk vergelijkend onderzoek bij drie gevestigde CI/CD-systemen bevestigt dat dit randgeval deterministisch en dus autonoom afleidbaar is, wat past bij de missie om Product Factory zelf continu te toetsen zonder te wachten op een menselijk gemelde beslissing. Het onderzoek levert tegelijk een concreet, vermijdbaar risico (CircleCI's retroactieve overschrijving van een terminale uitkomst) dat direct het principe 'onomkeerbaarheid weegt zwaarder dan gemak' raakt: een badge die achteraf van betekenis verandert is verwarrend voor de eigenaar. En omdat zelfs GitHub's eigen documentatie deze scheiding niet helder maakt, sluit eigen documentatie aan bij 'eerst begrijpen, dan wijzigen' — het voorkomt dat Product Factory dezelfde onduidelijkheid overneemt die het externe precedent al jaren kent.

### Prioriteiten
- Verifieer eerst tegen Product Factory's eigen iteratie-datamodel en broncode of er al een status- en/of conclusion-achtig veld bestaat, vóórdat er stories worden geschreven — dit kon deze onderzoekssessie niet worden vastgesteld door het ontbreken van code-/bestandstools.
- Specificeer dat conclusion='cancelled' automatisch en zonder menselijk besluit wordt afgeleid zodra de uitvoering van een iteratie stopt, ongeacht de trigger.
- Specificeer dat de conclusion-waarde van een iteratie na het bereiken van de terminale staat onveranderlijk is en nooit door een later event mag worden herschreven.
- Schrijf korte, eigen documentatie van de status/conclusion-semantiek voor Product Factory, los van het externe precedent.
- Laat GitLab's 'canceling'-tussenstatus expliciet buiten scope voor deze iteratie.

### Besluiten
- **Adopteer voor iteratie-uitkomsten een status (running/completed) + conclusion (uitkomst, incl. 'cancelled') model, analoog aan het reeds gekozen GitHub Actions-precedent, en bevestig dit als een breed gedragen CI/CD-patroon (ook bij GitLab CI/CD en CircleCI) in plaats van een GitHub-specifieke eigenaardigheid.** — Onafhankelijke bevestiging bij drie gevestigde systemen verhoogt het vertrouwen dat dit patroon solide gefundeerd is, wat aansluit bij het productprincipe 'eerst begrijpen, dan wijzigen': het huidige gedrag/precedent wordt niet blind overgenomen maar getoetst.
- **Classificeer 'geannuleerd tijdens uitvoering' volledig autonoom: zodra de uitvoering stopt (door welke trigger dan ook) gaat status naar 'completed' en wordt conclusion vastgesteld als 'cancelled', zonder apart menselijk besluitmoment.** — Weerlegt de aanname uit iteratie 4 dat dit randgeval nadere menselijke afspraak vereist; het is dezelfde deterministische afleidingsregel als voor elke andere terminale uitkomst, dus geen open productbesluit nodig — in lijn met de opdracht om zelfstandig uitvoerbare richtingen te ontwerpen.
- **Leg vast dat de conclusion van een iteratie precies één keer wordt bepaald, op het moment dat de iteratie haar eigen terminale staat bereikt, en dat geen later, ongerelateerd event (zoals het starten van een volgende iteratie) deze waarde met terugwerkende kracht mag overschrijven.** — Een gedocumenteerd CircleCI-gebruikersprobleem toont dat het ontbreken van deze garantie tot verwarrende, met terugwerkende kracht gewijzigde historische uitkomsten leidt — een concreet, vermijdbaar ontwerprisico voor de badge van Product Factory zelf.
- **Documenteer de status/conclusion-semantiek expliciet en zelfstandig in Product Factory (welke waarden bij welk veld horen, wanneer conclusion pas geldig is), in plaats van te vertrouwen op impliciete kennis van het externe precedent.** — Zelfs GitHub's eigen officiële documentatie is hierover al twee jaar aantoonbaar ambigu; het overnemen van een extern patroon zonder eigen uitleg zou dezelfde verwarring herhalen die het principe 'bruikbaar voor de eigenaar' juist wil voorkomen.
- **Neem GitLab's tussenliggende 'canceling'-status (annulering aangevraagd maar nog niet voltooid) nu niet over; bewaar het als mogelijke toekomstige verfijning, geen onderdeel van de huidige richting.** — Het huidige grove statusmodel van Product Factory heeft dit fijnmazige onderscheid niet nodig; het toevoegen ervan nu zou de wijziging groter en minder in isolatie beoordeelbaar maken dan nodig, in strijd met het principe 'klein en toetsbaar'.

## UX-voorstel: Iteratie-badge: status/conclusion met vergrendelde 'cancelled'-classificatie

**Gebruikersdoel:** Als Product Factory-eigenaar in één oogopslag zien of een iteratie nog loopt of klaar is, en bij afronding de definitieve, nooit-meer-wijzigende uitkomst (waaronder 'geannuleerd tijdens uitvoering') begrijpen zonder ambiguïteit.

### Flow
1. Eigenaar opent het iteratie-overzicht van Product Factory (lijst van iteraties).
2. Elke rij toont een badge met twee gescheiden velden: status (running/completed) en, alleen indien completed, conclusion (success/failure/cancelled/skipped/timed_out).
3. Voor een lopende iteratie toont de badge uitsluitend 'Running' (tekstueel label, geen conclusion-waarde zichtbaar).
4. Wanneer de uitvoering van een iteratie stopt (door welke trigger dan ook, inclusief annulering), verandert het systeem autonoom status naar 'Completed' en zet conclusion eenmalig, zonder tussenkomst.
5. Eigenaar navigeert met Tab/pijltoetsen naar een badge; bij focus verschijnt een tekstueel tooltip/panel dat de status/conclusion-semantiek van Product Factory zelf uitlegt.
6. Eigenaar activeert (Enter/klik) een badge om het detailpaneel van die iteratie te openen.
7. Detailpaneel toont: starttijdstip, tijdstip van terminale staat, vastgestelde conclusion-waarde, en een vaste vermelding 'deze uitkomst is definitief en wordt niet meer gewijzigd'.
8. Eigenaar start (elders in de UI) een nieuwe iteratie; het systeem verifieert dat de conclusion van de vorige, al afgeronde iteratie ongewijzigd blijft.
9. Eigenaar kan vanuit het detailpaneel doorklikken naar de korte, statische documentatiepagina over het status/conclusion-model.

### Wireframe

[Iteratie-overzicht]
--------------------------------------------------
| Iteratie #123  [● Running]                     |
| Iteratie #122  [✔ Completed · success]          |
| Iteratie #121  [✖ Completed · failure]          |
| Iteratie #120  [⦸ Completed · cancelled]         |
--------------------------------------------------
(elke badge is een <button> met aria-label:
 "Status: Completed. Conclusion: cancelled. Iteratie 120.
  Activeer voor details.")

[Focus op badge #120 → tooltip/inline panel]
--------------------------------------------------
| ⦸ Completed · cancelled                         |
| Uitleg: 'Status' = of de iteratie nog draait     |
| of klaar is. 'Conclusion' = het eindresultaat,   |
| pas geldig zodra status = Completed. 'cancelled' |
| betekent: uitvoering is gestopt vóór een normale |
| afronding (bv. onderbroken). Deze waarde is      |
| definitief.                    [Meer uitleg »]   |
--------------------------------------------------

[Detailpaneel iteratie #120]
--------------------------------------------------
| Iteratie #120                                   |
| Status: Completed                               |
| Conclusion: cancelled                           |
| Gestart: 2026-08-09 10:02                       |
| Terminale staat bereikt: 2026-08-09 10:04        |
| "Deze uitkomst is eenmalig vastgesteld op het    |
|  moment van afronden en wordt nooit later door   |
|  een ander event overschreven."                 |
| [Volledige log tonen]  [Documentatie status/     |
|  conclusion »]                                   |
--------------------------------------------------

[Documentatiepagina status/conclusion — statisch, eigen tekst]
--------------------------------------------------
| Wat betekent status?                            |
| - running: iteratie is nog bezig                |
| - completed: iteratie is klaar, conclusion geldt |
| Wat betekent conclusion? (alleen bij completed)  |
| - success / failure / cancelled / skipped /      |
|   timed_out                                      |
| 'cancelled' wordt automatisch bepaald zodra de   |
| uitvoering stopt, ongeacht de trigger; er is geen|
| apart besluitmoment. Eenmaal vastgesteld, blijft |
| de conclusion ongewijzigd.                       |
--------------------------------------------------

### Interactiehypotheses
- H1: Wanneer de uitvoering van een iteratie door een agent/testscript wordt afgebroken, zet het systeem binnen een vaste timeout autonoom status=completed en conclusion=cancelled, meetbaar door een geautomatiseerde test die het proces beëindigt en de badge-state pollt.
- H2: Na het bereiken van de terminale staat blijft de conclusion-waarde van een iteratie ongewijzigd, ook nadat een volgende iteratie start; getoetst door een geautomatiseerde test die de opgeslagen conclusion vóór en ná het starten van een nieuwe iteratie vergelijkt.
- H3: Elke badge bevat een tekstueel, niet-alleen-op-kleur-gebaseerd label voor zowel status als conclusion, verifieerbaar via een geautomatiseerde axe-core/toegankelijkheidsscan die controleert op aanwezige tekstinhoud naast eventuele kleurcodering.
- H4: Alle badges zijn bereikbaar en activeerbaar met uitsluitend het toetsenbord (Tab/Enter), en hebben een aria-label dat status én conclusion samen benoemt; getoetst met een geautomatiseerde keyboard-navigatie- en screenreader-attribuuttest.
- H5: De kleurcombinaties van elke badge-status (running/success/failure/cancelled) voldoen aan een contrastratio van minimaal 4.5:1, geautomatiseerd gemeten met een contrast-checktool tegen de gerenderde kleurwaarden.
- H6: De documentatiepagina over status/conclusion is statisch, bevat geen externe of persoonsgegevens, en is via een geautomatiseerde linkcheck bereikbaar vanuit elk detailpaneel.

### Toegankelijkheid
- Alle badges zijn native <button>- of <a>-elementen met volledige toetsenbordbereikbaarheid (Tab-volgorde, Enter/Spatie activeert), zonder muisafhankelijke interacties.
- Elke badge combineert status en conclusion als tekst in het aria-label (bv. 'Status: Completed. Conclusion: cancelled.'), zodat schermlezers geen kleur hoeven te interpreteren.
- Statuskleuren worden altijd aangevuld met een tekstlabel en/of icoon (niet uitsluitend kleur) om kleurenblindheid te ondersteunen.
- Kleurcontrast van tekst en iconen op badges voldoet aan WCAG 2.1 AA (≥4.5:1 voor normale tekst).
- Het tooltip/uitleg-panel bij focus is ook programmatisch gekoppeld (aria-describedby) zodat schermlezergebruikers de uitleg automatisch horen bij focus op de badge.
- Focusvolgorde is logisch: lijst → badge → detailpaneel → documentatielink, zonder focus-vallen.

### Privacy
- De badge en het detailpaneel tonen uitsluitend operationele metadata van Product Factory zelf (iteratie-id, tijdstempels, status, conclusion) en geen persoonsgegevens of gebruikersdata van andere producten.
- Er worden geen namen, e-mailadressen of accountgegevens van personen in de badge, tooltip of detailpaneel weergegeven.
- De documentatiepagina bevat uitsluitend statische, eigen uitleg over het status/conclusion-model en verwijst niet naar externe systemen die persoonsgegevens zouden kunnen lekken.
- De volledige iteratielog (indien getoond via 'Volledige log tonen') blijft beperkt tot Product Factory's eigen procesmetadata; logvelden die per ongeluk persoonsgegevens zouden bevatten, worden niet weergegeven zonder aparte redactiestap.
- Er is geen handmatige menselijke goedkeuring of fysieke controle in deze flow vereist; het enige mogelijke externe element is een onvermijdelijk toegangstoken voor het ophalen van iteratiedata, dat niet in de UI wordt gelogd of getoond.

## Kritische beoordeling

**Oordeel:** ACCEPT

Beide nieuwe kandidaten (0: write-once guard op de conclusion-waarde; 1: eigen statische status/conclusion-documentatie) zijn goed onderbouwd met externe bronnen (GitHub Actions, GitLab CI, CircleCI), correct als informatieve referentie gebruikt zonder rechten- of privacyproblemen, en volledig agent-uitvoerbaar zonder menselijk besluitmoment, betaling, accountaanmaak of andere eigenaarsactie — ze voldoen daarmee aan de autonomie-gate. Beide zijn expliciet voorwaardelijk gemaakt aan de daadwerkelijke, nog te verifiëren staat van het bestaande datamodel (via kandidaat 24) en leveren in elk scenario (inclusief 'niets gevonden'/'onzeker') een klein, terugdraaibaar, in isolatie beoordeelbaar resultaat op zonder nieuwe schemavelden, routes, authenticatie- of PR-wijzigingen. Er zijn geen blokkerende issues; twee INFO- en één WARNING-issue (vooral een fragiele zelf-referentie naar 'Kandidaat 0' in de dependsOn van kandidaat 1, die na publicatie een ander ID krijgt) verdienen aandacht maar vereisen geen herwerking.
- **WARNING · CONSISTENCY** — Kandidaat 1 (documentatiestory) verwijst in dependsOn naar 'Kandidaat 0: Vergrendel de conclusion-waarde...' — dit is een zelf-referentie naar de zusterkandidaat in deze batch op basis van het nulgebaseerde reviewindex-nummer, niet op basis van een uiteindelijk backlog-ID. Na publicatie krijgt kandidaat 0 waarschijnlijk een ander doorlopend ID (bv. 26), waardoor de dependsOn-vermelding 'Kandidaat 0' niet meer resolveert en de implementerende agent het verkeerde of geen item kan vinden.
- **INFO · SCOPE** — Kandidaat 0 hangt af van zowel kandidaat 24 als kandidaat 23, en kandidaat 1 hangt weer af van kandidaat 0, 22 én 24. Deze meerlaagse conditionele afhankelijkheidsketen is elk voor zich goed onderbouwd met expliciete fallback-uitkomsten, maar vergroot het risico dat de orchestrator de stories in de verkeerde volgorde oppakt of een tussenliggende 'unconfirmed'-uitkomst niet correct doorgeeft aan de volgende story.
- **INFO · ACCESSIBILITY** — Kandidaat 1 specificeert niet expliciet dat het nieuwe statische documentatie-artefact (indien als tekstblok in de UI toegevoegd) semantische HTML, correcte kopstructuur en een via toetsenbord bereikbare link naar/vanuit het detailpaneel gebruikt. Dit is waarschijnlijk triviaal te vervullen maar is niet als acceptatiecriterium vastgelegd.

## Geaccepteerde storykandidaten

### Vergrendel de conclusion-waarde van een iteratie zodra de terminale staat is bereikt, zodat latere events deze nooit overschrijven

Vergelijkend onderzoek bij CircleCI toont een gedocumenteerd, door gebruikers als verwarrend ervaren randgeval: een reeds afgeronde 'failed'-uitkomst werd met terugwerkende kracht overschreven naar 'cancelled' zodra een latere, ongerelateerde build arriveerde. Dit is een concreet ontwerprisico voor Product Factory's eigen badge (kandidaat 24's status/conclusion-scheiding): een uitkomst die achteraf van betekenis verandert ondermijnt het doel van de badge (in één oogopslag de definitieve stand zien). Deze story is uitdrukkelijk voorwaardelijk aan kandidaat 24: alleen indien die kandidaat concludeert dat een echte status/conclusion-scheiding op een bestaand veld is gebouwd, heeft deze story een basis om op voort te bouwen. De implementerende agent inspecteert eerst, geautomatiseerd, het bestaande schrijfpad van het conclusion-veld en documenteert expliciet één van drie mogelijke uitkomsten: (a) het veld is al van nature write-once (geen extra code nodig, immutabiliteit is bevestigd), (b) het veld is kwetsbaar voor herschrijven en er wordt een write-once-guard toegevoegd, of (c) het schrijfpad is te complex om binnen deze story volledig te dekken (bijv. meerdere code-paden of asynchrone events) en er wordt geen garantie afgegeven, alleen een gedocumenteerde bevinding. Bij uitkomst (b) voegt de agent een schrijf-eenmaal-guard toe op het bestaande veld (geen nieuw schemaveld): zodra conclusion voor een iteratie is vastgesteld, wordt elke volgende schrijfpoging op datzelfde veld voor diezelfde iteratie genegeerd en gelogd als afgewezen, in plaats van de waarde stilzwijgend te wijzigen. Deze story levert in alle drie de gevallen een machineleesbaar, ondubbelzinnig resultaatstatus op (bijv. 'confirmed-immutable-native', 'guard-added', 'unconfirmed-partial-coverage') zodat afhankelijke stories (zoals de documentatiestory) daarop kunnen voortbouwen zonder aannames te hoeven doen. Puur een guard op bestaande dataverwerking; geen nieuwe route, geen wijziging aan authenticatie, PR-goedkeuringsflow of clusterconfiguratie.

**Acceptatiecriteria**
- Story is expliciet voorwaardelijk aan het resultaat van kandidaat 24: indien die geen status/conclusion-scheiding op een bestaand veld heeft gebouwd, levert deze story alleen een gedocumenteerde bevinding op en verandert er geen code
- Implementerende agent inspecteert en documenteert het huidige schrijfpad van het conclusion-veld en registreert het resultaat als exact één van drie machineleesbare uitkomsten: 'confirmed-immutable-native' (al write-once), 'guard-added' (kwetsbaar gevonden en guard toegevoegd), of 'unconfirmed-partial-coverage' (schrijfpad te complex om volledig te verifiëren binnen deze story)
- Bij uitkomst 'guard-added': voegt een schrijf-eenmaal-guard toe op het bestaande conclusion-veld zodat een tweede schrijfpoging voor dezelfde iteratie wordt genegeerd en gelogd, in plaats van de bestaande waarde te overschrijven
- Er wordt in geen geval een nieuw databaseveld of schema-element toegevoegd; elke wijziging werkt uitsluitend op het reeds bestaande, door kandidaat 24 bevestigde veld
- Geautomatiseerde test simuleert twee opeenvolgende iteraties en verifieert dat de opgeslagen conclusion-waarde van de eerste, al afgeronde iteratie ongewijzigd blijft nadat de tweede iteratie start en afrondt (van toepassing bij uitkomst 'confirmed-immutable-native' en 'guard-added')
- De vastgestelde uitkomst ('confirmed-immutable-native', 'guard-added' of 'unconfirmed-partial-coverage') wordt als expliciet, voor vervolgstories leesbaar artefact vastgelegd (bijv. in de story-oplevering/documentatie van deze story zelf)
- Geen wijziging aan Git-, GitHub-, OpenShift-, database-schema- of PR-goedkeuringsflow buiten de beschreven guard-logica
- Indien de guard een afgewezen schrijfpoging tegenkomt, wordt dit als traceerbare logregel vastgelegd zodat toekomstige diagnose mogelijk blijft

Bronnen: [https://discuss.circleci.com/t/failed-workflows-become-cancelled-when-a-new-build-arrives/29968](https://discuss.circleci.com/t/failed-workflows-become-cancelled-when-a-new-build-arrives/29968), [https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-cancellation](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-cancellation), [https://docs.github.com/en/rest/actions/workflow-runs](https://docs.github.com/en/rest/actions/workflow-runs)

Afhankelijkheden: Kandidaat 24: Scheid lopende-voortgangsindicator van de conclusion-badge — deze story heeft alleen basis als 24 een echte status/conclusion-scheiding op een bestaand veld bevestigt en bouwt, Kandidaat 23: fallback-waarde 'niet-classificeerbaar' — de guard moet ook fallback-waarden als definitief behandelen zodra vastgesteld

Risico's: Als kandidaat 24 geen bestaande scheiding vindt en dus niets bouwt, heeft deze story geen aangrijpingspunt en levert alleen een documentatiebevinding op — dit moet expliciet als geldig, klein resultaat worden geaccepteerd, niet als falen, Een te strikte guard kan een legitieme, toekomstige correctiemogelijkheid (bijv. handmatige databugfix door een agent) blokkeren; de guard moet uitsluitend automatische, ongerelateerde schrijfevents blokkeren, geen expliciete correctietooling, Bij uitkomst 'unconfirmed-partial-coverage' wordt geen garantie afgegeven; afhankelijke stories moeten deze onzekerheid overnemen in plaats van immutabiliteit als vaststaand te vermelden

### Voeg eigen, statische documentatie toe die het status/conclusion-onderscheid van Product Factory expliciet en zelfstandig uitlegt, conditioneel op de bevestigde vergrendelingsuitkomst

Een langlopende, onopgeloste GitHub-issue laat zien dat zelfs de officiële GitHub Actions-documentatie de status- en conclusion-velden als één ongescheiden lijst presenteert, zonder expliciet te vermelden welke waarde bij welk veld hoort. Product Factory volgt ditzelfde patroon (kandidaat 22/23/24) maar loopt het risico dezelfde verwarring over te nemen als er geen eigen uitleg bestaat. Deze story voegt een enkel, op zichzelf staand statisch documentatie-artefact toe (bijv. een docs-bestand of een statisch tekstblok in de bestaande overzichtspagina) dat uitlegt wat 'status' (lopend/voltooid) en 'conclusion' (het eindresultaat, alleen geldig bij voltooid) betekenen binnen Product Factory, inclusief de expliciete vermelding dat een tijdens uitvoering onderbroken iteratie autonoom wordt geclassificeerd zonder apart menselijk besluitmoment. De claim over immutabiliteit van conclusion ('wijzigt na vaststelling niet meer') wordt niet onvoorwaardelijk gepubliceerd, maar rechtstreeks afgeleid uit de door kandidaat 0 (write-once-guard) daadwerkelijk vastgestelde, machineleesbare uitkomst: bij uitkomst 'confirmed-immutable-native' of 'guard-added' schrijft de documentatie expliciet dat conclusion na vaststelling definitief is; bij uitkomst 'unconfirmed-partial-coverage', of indien kandidaat 0 zelf niet is uitgevoerd omdat kandidaat 24 geen scheiding bevestigde, schrijft de documentatie in plaats daarvan expliciet dat deze garantie momenteel niet volledig geverifieerd is, zonder de onvoorwaardelijke immutabiliteitsclaim te maken. De implementerende agent baseert de overige inhoud uitsluitend op de daadwerkelijk bevestigde velden en waarden uit kandidaten 22–24 (niet op het aspirational onderzoeksmodel), en documenteert expliciet elke afwijking tussen de daadwerkelijke implementatie en het hier beschreven model. Puur additief: geen nieuwe route, geen wijziging aan databaseschema, authenticatie of PR-goedkeuringsflow.

**Acceptatiecriteria**
- Voegt exact één nieuw, statisch documentatie-artefact toe (bestand of vast tekstblok) dat uitlegt wat status en conclusion betekenen binnen Product Factory's iteratieoverzicht
- Documentatie bevat expliciet de zin dat status alleen 'lopend' of 'voltooid' kan zijn en dat conclusion pas relevant/geldig is zodra status voltooid is
- Documentatie vermeldt expliciet dat een tijdens uitvoering onderbroken iteratie automatisch en zonder apart menselijk besluitmoment wordt geclassificeerd
- De immutabiliteitsclaim over conclusion is conditioneel geformuleerd op de machineleesbare uitkomst van kandidaat 0: bij 'confirmed-immutable-native' of 'guard-added' vermeldt de documentatie expliciet en onvoorwaardelijk dat conclusion na vaststelling definitief is; bij 'unconfirmed-partial-coverage' of als kandidaat 0 niet is uitgevoerd, vermeldt de documentatie expliciet dat deze garantie momenteel niet volledig geverifieerd is en geen onvoorwaardelijke claim wordt gedaan
- Kandidaat 0 (de write-once-guard/immutabiliteitsverificatie) is toegevoegd aan de dependsOn-lijst van deze story, en de implementerende agent leest de daadwerkelijke uitkomst van kandidaat 0 vóór het schrijven van de immutabiliteitszin
- Implementerende agent baseert de vermelde veldnamen en overige waarden uitsluitend op wat door kandidaten 22, 23 en 24 daadwerkelijk in de bestaande code/het datamodel is bevestigd; indien die kandidaten geen scheiding bevestigen, beschrijft de documentatie alleen het daadwerkelijk bestaande gedrag en niet het aspirational model
- Geautomatiseerde check verifieert dat het documentatie-artefact bestaat en de vereiste kernzinnen bevat (status-definitie, autonome cancelled-classificatie, en de conditioneel juiste immutabiliteitszin die overeenkomt met de daadwerkelijke uitkomst van kandidaat 0)
- Geen wijziging aan bestaande routes, databaseschema, authenticatie of PR-goedkeuringsflow

Bronnen: [https://github.com/github/rest-api-description/issues/1634](https://github.com/github/rest-api-description/issues/1634), [https://docs.github.com/en/rest/actions/workflow-runs](https://docs.github.com/en/rest/actions/workflow-runs)

Afhankelijkheden: Kandidaat 22: uitkomstclassificatie-badges — documentatie moet aansluiten op de daadwerkelijk daar bevestigde vaste waarden, Kandidaat 24: status/conclusion-scheiding — documentatie-inhoud is voorwaardelijk aan wat deze kandidaat daadwerkelijk bevestigt en bouwt, Kandidaat 0: Vergrendel de conclusion-waarde zodra de terminale staat is bereikt — de immutabiliteitszin in deze documentatie is rechtstreeks afhankelijk van en conditioneel op de machineleesbare uitkomst ('confirmed-immutable-native', 'guard-added' of 'unconfirmed-partial-coverage') van deze story

Risico's: Als kandidaat 24 geen bestaande status/conclusion-scheiding bevestigt, mag deze documentatie geen niet-bestaand gedrag beschrijven; de agent moet de inhoud dan beperken tot wat daadwerkelijk geïmplementeerd is, om geen misleidende documentatie te publiceren, Als kandidaat 0 uitkomst 'unconfirmed-partial-coverage' oplevert, moet de documentatie de onzekerheid expliciet benoemen in plaats van deze te verzwijgen of de garantie toch als vaststaand te formuleren, Documentatie kan na toekomstige codewijzigingen uit sync raken als er geen koppeling of test bestaat die inhoud tegen de broncode valideert; dit risico wordt bewust geaccepteerd omdat een volledige sync-mechanisme buiten de kleine scope van deze story valt, Overlap met kandidaat 25's inline uitklappaneel is mogelijk qua doel (uitleg geven); deze story is uitdrukkelijk beperkt tot een eigen, volledig documentatie-artefact los van de badge-interactie, niet een vervanging van het disclosure-paneel

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
