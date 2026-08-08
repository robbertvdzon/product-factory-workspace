---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0004
date: 2026-08-08
status: approved
sources:
  - https://docs.github.com/en/rest/actions/workflow-runs
  - https://github.com/github/rest-api-description/issues/1634
  - https://opentelemetry.io/docs/specs/semconv/http/http-spans/
  - https://www.augmentcode.com/guides/ai-agent-monitoring
  - https://www.nngroup.com/articles/indicators-validations-notifications/
---
# Productcyclus 4

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Onderzoeksvraag voor deze iteratie: hoe ontwerp je een klein, vast aantal wederzijds exclusieve uitkomst-/statuscategorieën (taxonomie) voor autonome agent- of pipeline-runs — inclusief expliciet, gedocumenteerd gedrag voor gevallen die niet ondubbelzinnig in die taxonomie passen — gebaseerd op gevestigde, goed gedocumenteerde precedenten in plaats van op aannames? Deze vraag volgt direct uit iteratie 1: de critic gaf als WARNING dat (a) de productrichting volledig op externe, deels rechtenbeperkte marketingbronnen leunde zonder toetsing aan gevestigde standaarden, en (b) de door de story_writer voorgestelde vier-badge-classificatie een expliciet fallback-gedrag vereist voor niet-classificeerbare data, zonder dat er onderzoek was gedaan naar hoe gevestigde systemen dat oplossen. Deze iteratie zoekt gericht naar hoe volwassen, publiek gedocumenteerde systemen (GitHub Actions API, OpenTelemetry-specificatie) en onderzoeksliteratuur (MAST-taxonomie voor agentfalen) dit oplossen, plus hoe UX-onderzoek (Nielsen Norman Group) bepaalt welk communicatiemiddel (indicator versus melding) bij een dergelijke classificatie past. Belangrijk: dit blijft, net als iteratie 1, extern webonderzoek — de leesbare workspace-kennisbron kon in deze taak niet worden geraadpleegd omdat er geen bestandstools beschikbaar waren, dus de eerdere WARNING over het ontbreken van toetsing aan Product Factory's eigen broncode/data is met deze iteratie nog niet opgelost en moet in een volgende stap alsnog gebeuren voordat concrete mapping-logica wordt gebouwd. Er zijn dit keer bewust bronnen gekozen met een duidelijkere autoriteits- en licentiestatus (officiële API-documentatie, een open-source-governed specificatie, en academisch afgeleide taxonomie) om het eerdere kritiekpunt over onduidelijke/beperkte bronrechten te verkleinen.

### GitHub Actions scheidt 'status' (lopend) van 'conclusion' (eindresultaat) met een vast, gedocumenteerd enum

GitHub's REST API voor workflow runs gebruikt twee aparte velden: 'status' voor de actuele uitvoeringsfase (completed, in_progress, queued, requested, waiting, pending — waarbij waiting/pending/requested alleen door GitHub Actions zelf gezet mogen worden) en 'conclusion' voor het eindresultaat zodra de run is afgerond (documentatie en gerelateerde bronnen noemen expliciet: success, failure, neutral, cancelled, skipped, timed_out, action_required, en stale). Dit is een precedent van een gevestigd, veelgebruikt systeem dat een lopende status bewust scheidt van een afgeronde-uitkomstclassificatie — relevant voor de vraag of Product Factory's iteratie-uitkomstbadge (onderzoek-onvoldoende / guardrail-conflict / richting-gekozen / richting-verworpen) alleen eindresultaten dekt of ook tussentijdse/lopende iteraties moet onderscheiden.

Bronnen: [https://docs.github.com/en/rest/actions/workflow-runs](https://docs.github.com/en/rest/actions/workflow-runs), [https://github.com/github/rest-api-description/issues/1634](https://github.com/github/rest-api-description/issues/1634)

### OpenTelemetry-specificatie eist expliciet een fallback-waarde ('_OTHER') wanneer een waarde niet in de bekende, gedocumenteerde enum-lijst past

De OpenTelemetry semantic conventions voor bijvoorbeeld het attribuut http.request.method schrijven met MUST-taal voor: als de waarde niet 'bekend' is bij de instrumentatie (d.w.z. niet in de vooraf gedocumenteerde lijst staat), MOET de attribuutwaarde worden gezet op de vaste fallback-waarde '_OTHER', met een expliciet mechanisme om de lijst van 'bekende' waarden per implementatie uit te breiden. Dit is een direct bruikbaar precedent voor de door de critic in iteratie 1 vereiste 'expliciete fallback-waarde of build-fout' bij de mapping van bestaande iteratie-data naar een van de vier uitkomstcategorieën: een vaste, herkenbare fallback-waarde (in plaats van een stille default of crash) met een gedocumenteerde, uitbreidbare lijst van bekende waarden is gangbare praktijk in gevestigde observability-standaarden.

Bronnen: [https://opentelemetry.io/docs/specs/semconv/http/http-spans/](https://opentelemetry.io/docs/specs/semconv/http/http-spans/)

### Academische MAST-taxonomie voor AI-agent-falen is multidimensionaal, niet een platte lijst, en classificeert op trajectoryniveau in plaats van op eindresultaat

Een geraadpleegde monitoring-guide verwijst naar de MAST-taxonomie (Multi-Agent System failure taxonomy) die agentfalen indeelt langs vier aparte dimensies — specificatie-/systeemontwerpproblemen, inter-agent-misalignment, taakverificatie-/terminatieproblemen, en semantische fouten (bijv. prompt drift, doel-drift, hallucinatie, tool-misbruik) — in plaats van één platte lijst van uitkomsten. De bron benadrukt expliciet dat classificatie op alleen het eindresultaat ('final-output monitoring') falen kan maskeren, omdat een agent op basis van het eindresultaat betrouwbaarder kan lijken dan een volledige trajectory-evaluatie laat zien. Dit relativeert het idee dat één plat, vier-waardig badge-schema (zoals in iteratie 1 voorgesteld) voldoende nuance biedt; het suggereert dat een toekomstige iteratie zou moeten onderzoeken of Product Factory's uitkomstcategorieën eigenlijk twee losse dimensies vermengen (bijv. 'waarom faalde het' versus 'wat was de uiteindelijke richting-beslissing').

Bronnen: [https://www.augmentcode.com/guides/ai-agent-monitoring](https://www.augmentcode.com/guides/ai-agent-monitoring)

### Nielsen Norman Group: kies bewust tussen indicator, validatie en melding op basis van informatietype, urgentie en of actie vereist is

NN/G onderscheidt drie communicatiemiddelen voor systeemstatus: indicators (passieve, contextuele visuele signalen die geen actie van de gebruiker vereisen — bijv. een icoon of badge), validations (foutmeldingen gekoppeld aan gebruikersinvoer, die uitleggen hoe iets te herstellen) en notifications (meldingen over systeemgebeurtenissen, onderverdeeld in actie-vereist/intrusief versus passief/niet-intrusief). Het artikel stelt dat het verkeerde middel kiezen (bijv. een irrelevante melding sturen waar een indicator zou volstaan) de gebruikerservaring verstoort. Dit bevestigt dat een uitkomstbadge in het iteratieoverzicht qua middel correct gecategoriseerd is als 'indicator' (passief, geen directe actie vereist), maar waarschuwt dat als een van de vier categorieën (bijv. 'guardrail-conflict') in de praktijk wél actie van de eigenaar vereist, een indicator-badge mogelijk het verkeerde communicatiemiddel is en een melding beter zou passen.

Bronnen: [https://www.nngroup.com/articles/indicators-validations-notifications/](https://www.nngroup.com/articles/indicators-validations-notifications/)

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://docs.github.com/en/rest/actions/workflow-runs) | 2026-08-08 | Officiële GitHub-productdocumentatie; op deze pagina zelf geen expliciete licentievermelding waargenomen tijdens raadpleging. GitHub's docs-repository hanteert doorgaans een open documentatielicentie (CC BY 4.0), maar dit is niet specifiek op deze pagina bevestigd — behandel als 'onbekend, vermoedelijk open'. | Gezaghebbend, veelgebruikt voorbeeld van een gevestigd systeem met een klein, gedocumenteerd status/conclusion-enum voor geautomatiseerde runs; direct vergelijkbaar met Product Factory's iteratie-uitkomstclassificatie. |
| [bron](https://github.com/github/rest-api-description/issues/1634) | 2026-08-08 | Publieke GitHub-issue-discussie; content valt onder GitHub's standaard servicevoorwaarden voor door gebruikers gegenereerde content, geen aparte contentlicentie waargenomen. | Bevestigt en detailleert de vage/onvolledige documentatie van de conclusion-enum-waarden vanuit de praktijk van API-gebruikers, wat de noodzaak onderstreept om een eigen taxonomie expliciet en volledig te documenteren. |
| [bron](https://opentelemetry.io/docs/specs/semconv/http/http-spans/) | 2026-08-08 | Onderdeel van de OpenTelemetry-specificatie (CNCF-project); op de geraadpleegde pagina zelf geen expliciete copyright-/licentietekst waargenomen tijdens deze fetch. OpenTelemetry-specificatierepositories staan doorgaans onder Apache License 2.0, maar dit is niet direct op deze pagina geverifieerd — behandel als 'onbekend, vermoedelijk open'. | Geeft expliciete, MUST-niveau normatieve richtlijnen voor het ontwerpen van een klein, gedocumenteerd waardebereik met een verplichte fallback-waarde voor onbekende gevallen — direct toepasbaar op de door de critic vereiste fallback-logica. |
| [bron](https://www.augmentcode.com/guides/ai-agent-monitoring) | 2026-08-08 | © 2026 Augment Code, alle rechten voorbehouden; expliciet vermeld op de pagina. Alleen te gebruiken als informatieve referentie, niet te hergebruiken/republiceren zonder toestemming. | Verwijst naar en vat de academische MAST-foutentaxonomie voor multi-agentsystemen samen, wat een onafhankelijk, onderzoeksgebaseerd tegenwicht biedt tegen de louter marketinggedreven bronnen uit iteratie 1 en een multidimensionale blik op agent-uitkomstclassificatie toevoegt. |
| [bron](https://www.nngroup.com/articles/indicators-validations-notifications/) | 2026-08-08 | © 1998-2026 Nielsen Norman Group, alle rechten voorbehouden, expliciet vermeld op de pagina ('All Rights Reserved'). Alleen te gebruiken als informatieve referentie; hergebruik vereist toestemming van NN/G. | Gezaghebbende, onafhankelijke UX-onderzoeksbron over wanneer een passieve indicator (zoals een badge) het juiste communicatiemiddel is versus een melding die actie vereist — toetst of het gekozen badge-patroon uit iteratie 1 het juiste middel is voor alle vier uitkomstcategorieën. |

## Productbeslissing

Richting voor deze iteratie: leg het ontwerp van de iteratie-uitkomstbadge in Product Factory vast als een afgeronde-status-indicator ('conclusion', naar analogie van GitHub Actions), met (1) een klein, vast aantal wederzijds exclusieve categorieën, (2) een verplichte, herkenbare fallback-categorie voor niet ondubbelzinnig classificeerbare iteraties (naar analogie van OpenTelemetry's '_OTHER'), (3) een expliciete scope-beperking die het badge markeert als eindresultaat-indicator en niet als foutoorzaak-diagnose (naar aanleiding van de MAST-taxonomie), en (4) behoud van het badge als passieve UI-indicator in plaats van een actie-vereisende melding (NN/G). Concrete mapping-logica (welke bestaande iteratiedata naar welke categorie/fallback wordt gemapt) wordt nog niet gebouwd: dat vereist eerst toetsing aan Product Factory's eigen workspace-broncode en iteratiedata, wat in deze iteratie — net als in iteratie 1 — niet mogelijk was omdat er geen bestandstools beschikbaar waren. Dit is de enige nog openstaande blokkade vóór implementatie.

**Waarom:** De missie vraagt continue, eigen toetsing of Product Factory prettig werkt en begrijpelijk is; een duidelijke, voorspelbare iteratie-uitkomstindicator draagt daar direct aan bij, mits ze niet misleidt over lopende versus afgeronde iteraties en niet stil faalt op onverwachte data. De kwaliteitsregel eist dat een wijziging uitlegt waarom het huidige gedrag zo was en in isolatie beoordeelbaar/terug te draaien is — door te steunen op drie onafhankelijke, gezaghebbende precedenten (GitHub Actions API, OpenTelemetry-specificatie, MAST-taxonomie) in plaats van op de marketinggedreven bronnen van iteratie 1, is deze richting beter onderbouwd en de eerdere WARNING over brongezag grotendeels geadresseerd. De guardrail dat er geen andere producten of clusters worden geraakt en geen menselijke uitvoering wordt gepland (behalve een noodzakelijk token) blijft gerespecteerd: dit is een puur informatief, passief UI-element in Product Factory zelf, zonder wijziging aan hkh/hkh-autopilot of aan authenticatie/migraties. De resterende onderzoekslacune — toetsing aan de eigen workspace-broncode/data — wordt expliciet benoemd als volgende stap, in lijn met de eis dat aannames niet worden vervangen door nieuwe aannames maar door verificatie.

### Prioriteiten
- Documenteer het badge-schema (vier categorieën + verplichte fallback-categorie) expliciet vóórdat concrete mapping-logica wordt gebouwd.
- Valideer de mapping in een volgende iteratie tegen Product Factory's eigen workspace-broncode en bestaande iteratiedata — dit kon deze iteratie niet, wegens ontbrekende bestandstools.
- Beperk het badge expliciet tot eindresultaat ('wat'), niet oorzaak ('waarom'), om scope-kruip naar een volledige foutentaxonomie te voorkomen.
- Implementeer het badge als geïsoleerd, optioneel UI-element zodat het zonder neveneffecten beoordeeld en teruggedraaid kan worden.
- Behoud het badge als passieve indicator; heroverweeg pas naar een melding als een categorie ooit verplichte eigenaarsactie blijkt te vereisen.

### Besluiten
- **Modelleer de iteratie-uitkomstbadge als een 'conclusion'-veld dat uitsluitend van toepassing is op afgeronde iteraties, losstaand van een eventuele lopende-voortgangsstatus — analoog aan GitHub Actions' scheiding tussen 'status' (in_progress/queued/waiting) en 'conclusion' (success/failure/cancelled/...).** — GitHub Actions is een gevestigd, veelgebruikt systeem dat bewust twee aparte velden gebruikt in plaats van één vermengd veld. Dit voorkomt dat Product Factory's badge per ongeluk lopende iteraties als 'mislukt' classificeert, en houdt de badge klein en eenduidig — passend bij de kwaliteitsregel dat een wijziging isoleerbaar en beoordeelbaar moet zijn.
- **Definieer een verplichte, vaste en herkenbare fallback-categorie (bv. 'niet-classificeerbaar') voor iteraties waarvan de data niet ondubbelzinnig in één van de vier gedocumenteerde categorieën past, met een expliciet gedocumenteerde en uitbreidbare lijst van 'bekende' waarden — in plaats van een stille default of een build-fout.** — De OpenTelemetry-specificatie schrijft met MUST-taal exact dit patroon voor bij onbekende attribuutwaarden ('_OTHER'). Dit lost de WARNING van de critic in iteratie 1 op door een concreet, gevestigd precedent te volgen in plaats van een aanname.
- **Begrens het badge expliciet tot een coarse eindresultaat-indicator ('wat was de uitkomst') en vermeng dit niet met een oorzaak-/foutentaxonomie ('waarom faalde het'). Documenteer die scope-beperking bij het badge zelf.** — De MAST-taxonomie laat zien dat agentfalen multidimensionaal en trajectory-afhankelijk is; classificatie op alleen het eindresultaat kan onderliggende problemen maskeren. Eén plat badge moet daarom niet doen alsof het een volledige diagnose is — dat voorkomt een te grote, niet-samenhangende uitbreiding in deze iteratie.
- **Behoud het badge als passieve, contextuele UI-indicator (geen melding/notificatie die directe actie van de eigenaar vereist), omdat geen van de vier categorieën momenteel verplichte menselijke actie impliceert buiten de reeds toegestane uitzondering van een noodzakelijk extern toegangstoken.** — NN/G onderscheidt indicators (geen actie vereist) van notifications (actie vereist/intrusief). Het toepassen van het verkeerde middel verstoort de gebruikerservaring; een indicator past bij de huidige guardrail dat er geen andere menselijke uitvoering wordt gepland dan de tokenuitzondering.

## UX-voorstel: Iteratie-uitkomstbadge (conclusion-indicator) in iteratieoverzicht

**Gebruikersdoel:** Als eigenaar/beoordelaar van Product Factory wil ik in het iteratieoverzicht in één oogopslag en zonder verplichte actie kunnen zien wat de afgeronde uitkomst (conclusion) van een iteratie was — inclusief een herkenbare status voor iteraties die niet eenduidig in een vaste categorie passen — zonder dat dit lopende iteraties verkeerd classificeert of een oorzaakdiagnose suggereert.

### Flow
1. Gebruiker opent het iteratieoverzicht (lijst/tabel van alle iteraties van een product, aflopend op datum).
2. Systeem toont per rij een status-veld: lopende iteraties (queued/in_progress/waiting) krijgen een neutrale voortgangsindicator, géén conclusion-badge.
3. Zodra een iteratie is afgerond, toont systeem exact één badge uit de vaste, wederzijds exclusieve set: onderzoek-onvoldoende, guardrail-conflict, richting-gekozen, richting-verworpen.
4. Als de afgeronde iteratiedata niet ondubbelzinnig op één van de vier categorieën mapt, toont systeem verplicht de vaste fallback-badge 'niet-classificeerbaar' (nooit een lege cel, nooit een stille default, nooit een fout).
5. Gebruiker verplaatst focus naar de badge via toetsenbord (Tab) of muis-hover; systeem toont een tooltip/aria-beschrijving met de volledige labelnaam en één zin uitleg wat de categorie betekent.
6. Gebruiker activeert de badge (Enter/Space of klik) om een detailpaneel te openen met: gekozen categorie, scope-disclaimer ('dit toont wát de uitkomst was, niet waaróm'), en een link naar het volledige iteratielog voor diepere diagnose.
7. Gebruiker sluit het detailpaneel (Escape of sluitknop) en keert terug naar het overzicht zonder verlies van scroll-positie of focus.

### Wireframe

SCHERM: Iteratieoverzicht (bestaand overzicht, badge toegevoegd als nieuwe kolom)

┌─────────────────────────────────────────────────────────────────────────┐
│ Product Factory · Iteraties · product-factory                            │
├─────────────────────────────────────────────────────────────────────────┤
│ Iteratie          Datum        Status/Uitkomst                           │
├─────────────────────────────────────────────────────────────────────────┤
│ iteratie-12        08-08-2026   ⏳ Bezig — geen uitkomst-badge            │
│                                  (aria-live="polite", label:"loopt nog")  │
├─────────────────────────────────────────────────────────────────────────┤
│ iteratie-11        07-08-2026   [🟢 Richting-gekozen]  ← focusbaar badge  │
│                                  tabindex=0, role="status",               │
│                                  aria-label="Uitkomst: richting-gekozen"  │
├─────────────────────────────────────────────────────────────────────────┤
│ iteratie-10        06-08-2026   [🟡 Onderzoek-onvoldoende]                │
├─────────────────────────────────────────────────────────────────────────┤
│ iteratie-9         05-08-2026   [🔴 Guardrail-conflict]                   │
├─────────────────────────────────────────────────────────────────────────┤
│ iteratie-8         04-08-2026   [⚪ Richting-verworpen]                   │
├─────────────────────────────────────────────────────────────────────────┤
│ iteratie-7         03-08-2026   [⬛ Niet-classificeerbaar] ← fallback,     │
│                                  altijd zichtbaar i.p.v. lege cel/crash   │
└─────────────────────────────────────────────────────────────────────────┘

Focus/hover op badge → tooltip (role="tooltip", gekoppeld via aria-describedby):
┌───────────────────────────────────────────┐
│ Richting-gekozen                            │
│ De iteratie is afgerond en er is een        │
│ productrichting vastgesteld.                │
│ Dit toont wát er is besloten, niet waarom.  │
└───────────────────────────────────────────┘

Activeren van badge (Enter/klik) → detailpaneel (role="dialog", aria-modal="true",
focus verplaatst naar paneelheader, Escape sluit en geeft focus terug aan badge):
┌─────────────────────────────────────────────────────────────────────────┐
│ Uitkomst iteratie-11                                            [Sluiten]│
├─────────────────────────────────────────────────────────────────────────┤
│ Categorie: Richting-gekozen                                              │
│                                                                            │
│ Let op: dit badge is een eindresultaat-indicator ("wat"), geen           │
│ foutoorzaak-diagnose ("waarom"). Voor de volledige trajectory-analyse:   │
│                                                                            │
│ → Bekijk volledig iteratielog                                            │
└─────────────────────────────────────────────────────────────────────────┘

Kleur is nooit het enige onderscheid: elke badge combineert kleur + icoon +
tekstlabel (WCAG 1.4.1). Contrastverhouding tekst/achtergrond ≥ 4.5:1 (WCAG AA).

### Interactiehypotheses
- H1 (dekking): Voor 100% van de afgeronde iteraties in de testdataset retourneert de mapping-functie precies één van de vijf vaste waarden (4 categorieën + 'niet-classificeerbaar'); een geautomatiseerde test faalt zodra een zesde/onbekende of lege waarde voorkomt.
- H2 (scheiding status/conclusion): Voor 100% van de iteraties met status in {queued, in_progress, waiting} toont de UI geen conclusion-badge maar uitsluitend de voortgangsindicator; een geautomatiseerde snapshot-/DOM-test verifieert afwezigheid van het badge-element in die rijen.
- H3 (fallback i.p.v. stil falen): Wanneer testdata bewust een niet-classificeerbaar patroon bevat (ontbrekende/tegenstrijdige velden), toont de mapping altijd de fallback-badge in plaats van een lege cel, exception of default-waarde; geautomatiseerde unit test injecteert edge-case data en assert op de fallback-output.
- H4 (scope-disclaimer zichtbaar): Bij elke badge-activatie bevat het geopende detailpaneel de exacte scope-disclaimerzin ('wat, niet waarom'); een geautomatiseerde UI-test (bv. Playwright) controleert de aanwezigheid van deze tekst na klik/Enter op elk van de vijf badge-varianten.
- H5 (toetsenbordbereikbaarheid): Elk badge-element is bereikbaar en activeerbaar met alleen het toetsenbord (Tab verplaatst focus, Enter/Space activeert het detailpaneel, Escape sluit en herstelt focus); geautomatiseerde toetsenbord-navigatietest doorloopt alle badges in het overzicht zonder muisinteractie.

### Toegankelijkheid
- Elk badge is bereikbaar via toetsenbord (Tab/Shift+Tab in DOM-volgorde) en activeerbaar met Enter of Space; focus-volgorde volgt de tabelrijen top-naar-onder.
- Badge gebruikt role="status" met aria-label die de volledige categorienaam bevat (niet enkel een icoon of kleurcode), zodat schermlezers de uitkomst voorlezen zonder extra interactie.
- Tooltip/detailpaneel is gekoppeld via aria-describedby resp. aria-modal="true" met role="dialog"; bij openen verplaatst focus naar het paneel, bij sluiten (Escape) keert focus terug naar het activerende badge-element.
- Kleur is nooit het enige onderscheidende kenmerk tussen categorieën: elke badge combineert kleur, icoon-vorm en tekstlabel (WCAG 1.4.1 Use of Color).
- Tekst-op-achtergrondkleur van elk badge voldoet aan een contrastverhouding van minimaal 4.5:1 (WCAG 2.1 AA, 1.4.3), geverifieerd via geautomatiseerde contrast-check op elk van de vijf badge-varianten.
- Lopende iteraties gebruiken aria-live="polite" op de statuscel zodat statuswijzigingen (bijv. van 'bezig' naar een conclusion-badge) door schermlezers worden aangekondigd zonder de gebruiker te onderbreken.

### Privacy
- Het badge en het detailpaneel tonen uitsluitend operationele metadata van Product Factory zelf (iteratie-ID, datum, uitkomstcategorie, log-link); geen persoonsgegevens of gebruikersdata van andere producten worden weergegeven of verwerkt.
- De mapping-logica leest en verwerkt geen inhoudelijke gebruikersdata van hkh/hkh-autopilot of andere producten; input blijft beperkt tot Product Factory's eigen iteratie-status- en conclusionvelden.
- Het detailpaneel linkt naar het volledige iteratielog maar toont dat log niet inline; hiermee blijft het badge zelf minimaal en wordt voorkomen dat mogelijk gevoelige logdetails ongefilterd in de overzichts-UI verschijnen.
- Er wordt geen tracking, analytics of gebruikersgedrag rond badge-interacties opgeslagen die herleidbaar is tot een individuele persoon; eventuele interactiemetrics blijven beperkt tot geaggregeerde, niet-persoonsgebonden operationele telemetrie.

## Kritische beoordeling

**Oordeel:** ACCEPT

Alle drie de kandidaten bouwen consistent voort op het gepubliceerde vierwaardige badge-schema (kandidaat 22) en verwerken de kern-WARNING uit iteratie 1 (ontbrekende fallback-logica) door expliciet, agent-uitvoerbare broncode-/datamodel-inspectie als eerste acceptatiecriterium op te nemen in plaats van vooraf aangenomen randgevallen. Geen van de drie vereist menselijke actie, accountaanmaak, betaling of andere niet-agent-uitvoerbare stap; conditionele paden (bijv. 'geen bestaand veld gevonden → geen wijziging') zijn zelf ook volledig agent-afhandelbaar. Toegankelijkheid (toetsenbord, aria-attributen, contrast ≥4.5:1) en privacy (geen persoonsgegevens, enkel operationele metadata) zijn expliciet en toetsbaar geborgd in elke kandidaat. Blijvend punt van zorg (niet-blokkerend): de onderliggende research/decisions van deze iteratie kon de eigen workspace-broncode zelf nog niet raadplegen (ontbrekende bestandstools) — dat gat wordt terecht doorgeschoven naar de implementatiefase via verplichte inspectiecriteria in alle drie de kandidaten, wat een acceptabele mitigatie is, maar dit blijft een open onderzoekslacune die in een volgende iteratie alsnog direct getoetst moet worden. Er is een sequentiële afhankelijkheidsketen (kandidaat 2→1→0, en 1/2→0) die de orchestrator moet respecteren bij planning; dit is geen inhoudelijk conflict maar wel een leverings-volgorde-aandachtspunt.
- **WARNING · SOURCE** — De onderliggende research (summary/decisions) van deze iteratie kon Product Factory's eigen workspace-broncode en iteratiedata nog niet raadplegen (ontbrekende bestandstools), en leunt voor de badge-ontwerprichting uitsluitend op externe precedenten (GitHub Actions, OpenTelemetry, MAST, NN/G). Dit is grotendeels gemitigeerd doordat elke kandidaat een verplichte broncode-/datamodelinspectie als eerste acceptatiecriterium stelt, maar de directe toetsing aan eigen bronnen staat nog open.
- **WARNING · CONSISTENCY** — Kandidaten 1 en 2 zijn afhankelijk van de fallback-badge-story uit kandidaat 0 (nog niet gepubliceerd), en kandidaat 2 is bovendien afhankelijk van kandidaat 1. Dit vormt een sequentiële leveringsketen (0 → 1 → 2) die de orchestrator expliciet moet respecteren; er is geen inhoudelijk conflict, maar gelijktijdige/losse levering zonder volgorde kan tot een inconsistente tussentoestand leiden.
- **INFO · RIGHTS** — Bronnen van Augment Code en Nielsen Norman Group zijn expliciet '© alle rechten voorbehouden' en mogen niet worden hergebruikt/gereproduceerd; in de kandidaten worden ze correct alleen als informatieve referentie gebruikt voor ontwerpkeuzes (indicator vs. melding, multidimensionale foutclassificatie), niet gereproduceerd. Geen blokkade, wel goed te bewaken bij toekomstige documentatie-uitbreidingen.
- **INFO · SCOPE** — Kandidaat 1 kan resulteren in een PR zonder zichtbare functionele wijziging ('indien geen bestaand onderscheidend veld wordt gevonden, levert de story uitsluitend de gedocumenteerde bevinding op'). Dit is een valide, agent-uitvoerbare spike-achtige uitkomst en geen assumptie-gedreven bouw, maar de orchestrator moet dit resultaattype (documentatie-only) als geldige afronding herkennen.

## Geaccepteerde storykandidaten

### Voeg verplichte fallback-waarde 'niet-classificeerbaar' toe aan de iteratie-uitkomstmapping, gebaseerd op het daadwerkelijke datamodel

Kandidaat 22 introduceert een vaste vierwaardige uitkomstbadge (onderzoek-onvoldoende, guardrail-conflict, richting-gekozen, richting-verworpen), maar specificeert geen gedrag voor iteraties waarvan de bestaande iteratiedata niet ondubbelzinnig op één van deze vier waarden mapt. Deze story voegt aan diezelfde mappinglaag een verplichte, herkenbare vijfde waarde 'niet-classificeerbaar' toe — analoog aan de MUST-fallback ('_OTHER') uit de OpenTelemetry-specificatie — mét het generieke fallback-mechanisme (elke ruwe waarde buiten een gedocumenteerde, uitbreidbare 'bekende waarden'-lijst mapt naar de fallback, nooit naar null/lege cel/crash). In lijn met de criticusfeedback wordt hierbij géén vooraf aangenomen set specifieke randgevallen (zoals 'ontbrekend veld' of 'tegenstrijdige velden') afgeleid uit een extern precedent: de implementerende agent moet eerst de daadwerkelijke broncode/het datamodel van de bestaande iteratie-uitkomstdata (gebruikt door kandidaat 22) inspecteren om de werkelijke set mogelijke ruwe waarden en randgevallen vast te stellen, en die als 'bekende waarden'-lijst en bijbehorende testcases documenteren. Puur een uitbreiding van de bestaande rapportage-/weergavelaag; geen nieuwe dataverzameling, geen nieuwe route, geen aanpassing van de PR-goedkeuringsflow.

**Acceptatiecriteria**
- Voordat de mappingfunctie wordt uitgebreid, inspecteert de implementerende agent de bestaande broncode/het datamodel van de iteratie-uitkomstdata die kandidaat 22 gebruikt, en documenteert (in code/config) een expliciete, uitbreidbare lijst van de daadwerkelijk voorkomende 'bekende' ruwe waarden per categorie.
- Gegeven een afgeronde iteratie waarvan de ruwe waarde niet voorkomt in de gedocumenteerde 'bekende waarden'-lijst, retourneert de mappingfunctie exact de vaste waarde 'niet-classificeerbaar' in plaats van null, undefined, een lege string of een exception.
- Geautomatiseerde unit tests dekken minimaal: elke gedocumenteerde bekende waarde mapt naar de juiste van de vier categorieën, én elke waarde die de agent bij broncode-inspectie buiten die lijst identificeert (in plaats van vooraf aangenomen randgevallen) mapt naar de fallback.
- De fallback-badge wordt in het iteratieoverzicht getoond met een eigen kleur, icoon-vorm én tekstlabel (niet uitsluitend kleur), consistent met de visuele opbouw van de vier bestaande badges.
- De tekst-op-achtergrondkleur van de fallback-badge voldoet aan een contrastverhouding van minimaal 4.5:1 (WCAG 2.1 AA, 1.4.3); een geautomatiseerde contrast-check-test assert dit voor de fallback-variant.
- Geautomatiseerde DOM-test itereert over alle afgeronde-iteratie-rijen in een testdataset (opgebouwd uit de bij inspectie vastgestelde werkelijke waarden) en assert dat elke rij precies één badge toont uit de vijfwaardige set, nooit een lege statuscel.

Bronnen: [https://opentelemetry.io/docs/specs/semconv/http/http-spans/](https://opentelemetry.io/docs/specs/semconv/http/http-spans/), [https://github.com/github/rest-api-description/issues/1634](https://github.com/github/rest-api-description/issues/1634)

Afhankelijkheden: Kandidaat 22: 'Vervang geslaagd/mislukt-indicator door vaste uitkomstclassificatie-badges in het iteratieoverzicht' moet zijn geïmplementeerd, aangezien deze story dezelfde mappingfunctie en badge-component uitbreidt.

Risico's: Als de agent bij broncode-inspectie geen betrouwbare 'bekende waarden'-set kan afleiden omdat de bestaande iteratiedata ongestructureerd is, moet de gedocumenteerde lijst conservatief (smal) worden gehouden zodat onbekende varianten altijd naar de fallback vallen in plaats van foutief geclassificeerd te worden., Als de lijst van 'bekende' waarden niet wordt bijgehouden bij toekomstige uitbreidingen van de iteratiedata, kunnen legitiem nieuwe uitkomsttypes onterecht als 'niet-classificeerbaar' verschijnen.

### Scheid lopende-voortgangsindicator van de conclusion-badge, uitsluitend indien een bestaand data-signaal dit al ondersteunt

De bestaande en geplande uitkomstbadges (kandidaat 22 en de fallback-uitbreiding) classificeren een afgerond eindresultaat ('conclusion'); zonder scheiding kan een lopende iteratie per ongeluk als bijvoorbeeld 'guardrail-conflict' worden weergegeven, analoog aan GitHub Actions' scheiding tussen 'status' en 'conclusion'. In lijn met de criticusfeedback veronderstelt deze story niet langer dat er al een bestaand veld is dat lopend van afgerond onderscheidt: de implementerende agent moet dit eerst zelf, geautomatiseerd, verifiëren door de broncode/het datamodel van het iteratieoverzicht te inspecteren en die bevinding te documenteren. Alleen als een dergelijk bestaand veld bevestigd wordt, wordt de UI-scheiding gebouwd, uitsluitend op basis van dat bestaande veld — er wordt in geen geval een nieuw databaseveld of schema-element toegevoegd. Wordt geen bestaand onderscheidend veld gevonden, dan levert deze story alleen die gedocumenteerde bevinding op en blijft de UI ongewijzigd, zodat de eigen 'geen nieuw schemaveld'-belofte nooit wordt geschonden. Een iteratie die tijdens uitvoering is geannuleerd wordt, indien de scheiding wél gebouwd wordt, behandeld als afgerond en mapt deterministisch naar de fallback-badge 'niet-classificeerbaar'.

**Acceptatiecriteria**
- Voordat enige UI-wijziging wordt gebouwd, inspecteert de implementerende agent de broncode van het bestaande iteratieoverzicht en -datamodel om vast te stellen of er al een veld/signaal bestaat dat onderscheidt of een iteratie nog loopt dan wel is afgerond, en documenteert die bevinding expliciet in de PR-/commitbeschrijving.
- Indien geen bestaand onderscheidend veld wordt gevonden: er wordt geen UI-wijziging en geen nieuw databaseveld/schema-element toegevoegd; de story levert in dat geval uitsluitend de gedocumenteerde bevinding op, geverifieerd doordat de diff geen wijziging aan badge-rendering en geen migratie bevat.
- Indien wél een bestaand onderscheidend veld wordt gevonden: gegeven een iteratie waarvoor dat veld 'lopend' aangeeft, toont het overzicht uitsluitend een neutrale voortgangsindicator en geen van de vijf conclusion-badges voor die rij; gegeven 'afgerond' toont het overzicht exact één conclusion-badge en niet de voortgangsindicator.
- Indien de scheiding wordt gebouwd: een iteratie die tijdens uitvoering is geannuleerd mapt in alle gevallen deterministisch naar de fallback-badge 'niet-classificeerbaar'; een geautomatiseerde unit test met testcase 'geannuleerd tijdens uitvoering' assert exact deze uitkomst.
- Indien de scheiding wordt gebouwd: geautomatiseerde DOM-/snapshot-test doorloopt rijen gegroepeerd op het bevestigde bestaande signaal uit een testdataset en assert wederzijdse exclusiviteit tussen voortgangsindicator en conclusion-badge.
- Indien de scheiding wordt gebouwd: de voortgangsindicator-cel gebruikt het attribuut aria-live="polite", geverifieerd via een geautomatiseerde test.
- In alle gevallen bevat de wijziging aantoonbaar geen nieuw databaseveld of schema-element; dit wordt geverifieerd doordat de implementatie uitsluitend leest uit reeds bestaande, bij inspectie bevestigde iteratievelden (geen migratie in de diff).

Bronnen: [https://docs.github.com/en/rest/actions/workflow-runs](https://docs.github.com/en/rest/actions/workflow-runs), [https://github.com/github/rest-api-description/issues/1634](https://github.com/github/rest-api-description/issues/1634)

Afhankelijkheden: Kandidaat 22: 'Vervang geslaagd/mislukt-indicator door vaste uitkomstclassificatie-badges in het iteratieoverzicht' moet zijn geïmplementeerd., De fallback-badge-story ('niet-classificeerbaar') uit deze iteratie, waarnaar geannuleerde iteraties deterministisch mappen indien de scheiding wordt gebouwd.

Risico's: Als er geen bestaand onderscheidend veld blijkt te bestaan, levert deze story bewust geen zichtbare UI-verandering op in deze iteratie; een latere iteratie kan dan expliciet besluiten of een nieuw schemaveld gerechtvaardigd is — dat besluit valt buiten de scope van deze story., De broncode-inspectiestap is volledig agent-uitvoerbaar (lezen van bestaande code/datamodel), maar de kwaliteit van de bevinding hangt af van hoe volledig de implementerende agent de relevante bestanden doorzoekt.

### Voeg toegankelijk inline uitklappaneel met scope-disclaimer toe bij activeren van de uitkomstbadge

Onderzoek naar de MAST-taxonomie laat zien dat classificatie op alleen het eindresultaat de onderliggende oorzaak van agentgedrag kan maskeren, en NN/G-onderzoek waarschuwt dat een indicator alleen passend is zolang deze geen actie/diagnose suggereert die hij niet biedt. Deze story voegt aan elk van de vijf bestaande badge-varianten (kandidaat 22 + fallback-uitbreiding) een toetsenbord- en muis-activeerbaar inline uitklappaneel toe (disclosure-patroon met aria-expanded op het badge en een direct onder de rij zichtbaar paneel), in plaats van een volledige modale dialoog, om geen afhankelijkheid van een nog niet bevestigde herbruikbare dialoogcomponent te introduceren. Het paneel vermeldt uitsluitend, in platte tekst binnen de bestaande overzichtspagina, dat het badge 'wat' toont en niet 'waarom'; er wordt geen link naar een externe iteratielog-route toegevoegd, omdat het bestaan daarvan niet is bevestigd. De implementerende agent controleert eerst of Product Factory al een herbruikbare modale dialoogcomponent gebruikt in de bestaande UI en documenteert die bevinding, zodat de keuze voor het inline-patroon expliciet getoetst is aan de bestaande componentbibliotheek in plaats van aangenomen. Dit blijft een geïsoleerde uitbreiding van de bestaande badge-component in het iteratieoverzicht; geen nieuwe route, geen wijziging aan authenticatie of PR-flow.

**Acceptatiecriteria**
- Voordat het paneel wordt gebouwd, inspecteert de implementerende agent de bestaande UI-componentbibliotheek op de aanwezigheid van een herbruikbare modale dialoogcomponent en documenteert deze bevinding in de PR-/commitbeschrijving; het inline disclosure-patroon blijft de gekozen implementatie tenzij dit tot aantoonbare inconsistentie leidt die de agent expliciet motiveert en oplost.
- Elk van de vijf badge-varianten (vier categorieën + fallback) is bereikbaar via Tab en activeerbaar via Enter of Space, geverifieerd door een geautomatiseerde toetsenbordnavigatietest zonder muisinteractie.
- Activeren van een badge toggelt aria-expanded op het badge-element van "false" naar "true" en toont een inline paneel binnen dezelfde rij (geen role="dialog", geen aria-modal, geen focus-trap); geautomatiseerde test assert de aanwezigheid van deze toggle en de afwezigheid van dialoog-specifieke attributen.
- De tekstinhoud van het geopende inline paneel bevat voor alle vijf badge-varianten de exacte scope-disclaimerzin (bijvoorbeeld 'Dit toont wat de uitkomst was, niet waarom.'); geautomatiseerde test assert de aanwezigheid van deze zin na activatie van elke variant.
- Nogmaals activeren van hetzelfde badge (of Escape) klapt het paneel weer in (aria-expanded terug naar "false") en focus blijft op of keert terug naar het badge-element; geautomatiseerde test assert dat document.activeElement na Escape gelijk is aan het badge-element.
- Elk badge-element behoudt role="status" en een aria-label met de volledige categorienaam (niet uitsluitend icoon of kleur); geautomatiseerde test assert de aria-label-tekst voor elk van de vijf varianten.
- Het inline paneel bevat geen link of verwijzing naar een externe iteratielog-route; geautomatiseerde test assert de afwezigheid van een dergelijke link.

Bronnen: [https://www.augmentcode.com/guides/ai-agent-monitoring](https://www.augmentcode.com/guides/ai-agent-monitoring), [https://www.nngroup.com/articles/indicators-validations-notifications/](https://www.nngroup.com/articles/indicators-validations-notifications/)

Afhankelijkheden: Kandidaat 22: 'Vervang geslaagd/mislukt-indicator door vaste uitkomstclassificatie-badges in het iteratieoverzicht' moet zijn geïmplementeerd., De fallback-badge-story ('niet-classificeerbaar') uit deze iteratie, zodat het inline paneel voor alle vijf varianten consistent werkt.

Risico's: Door de link naar het volledige iteratielog bewust weg te laten, biedt deze story minder diepere diagnosemogelijkheid dan oorspronkelijk bedoeld; een latere, apart getoetste story kan alsnog een link toevoegen zodra een iteratielog-route bevestigd is., Als bij inspectie blijkt dat er al wél een bevestigde, bestaande modale dialoogcomponent is, moet de agent expliciet motiveren waarom het inline-patroon toch consistent is, of alsnog voor de bestaande dialoogcomponent kiezen.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
