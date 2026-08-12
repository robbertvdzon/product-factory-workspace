---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0039
date: 2026-08-12
status: approved
sources:
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/api.dart
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/resources/db/migration/V3__shadow_iterations.sql
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationApi.kt
  - https://api.github.com/repos/robbertvdzon/product-factory
  - https://product-factory-acceptance.vdzonsoftware.nl
  - https://airflow.apache.org/docs/apache-airflow/3.1.3/security/audit_logs.html
  - https://airflow.apache.org/docs/apache-airflow/stable/ui.html
  - https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/viewing-workflow-run-history
---
# Productcyclus 39

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De belangrijkste nog onbeantwoorde productvraag is: kan Product Factory betrouwbaar vastleggen en tonen wie of wat een cyclusuitkomst bepaalde? Het huidige dashboard toont inmiddels “Beslisbron”, maar leidt die achteraf af uit status, criticVerdict en errorMessage. De operationele data bevat geen expliciete beslisser of beslisgebeurtenis. Daardoor blijft een deel “Onbekend” en kan een handmatige annulering zelfs als “Technische fout” worden gepresenteerd. Dit verklaart waarom de recente eigenaarsfeedback niet strookt met de eerdere conclusie dat badges het traceerbaarheidsprobleem grotendeels oplosten. De acceptatieomgeving kon in deze run niet visueel worden beoordeeld: de geïnstalleerde Chromium werd vóór paginalading door de sandbox afgebroken met een Mach-port-permissiefout. Er is geen productbesluit genomen en er zijn geen stories geschreven.

### Product Factory organiseert autonome productontwikkeling en bewaakt de uitvoering

De applicatie organiseert per geregistreerd product onderzoek, productkeuze, UX, storyvorming en kritiek. Geaccepteerde kandidaten worden voor autonome producten één voor één aan de Software Factory geleverd; resultaten en evaluaties worden als context in volgende cycli gebruikt. Het dashboard is primair bedoeld voor de producteigenaar die cycli start, uitkomsten controleert, technische voortgang volgt en alleen bij onvermijdelijke tokenacties hoeft in te grijpen.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md)

### Het hoofdscherm bevat nog veel concurrerende informatiestromen

De gedocumenteerde dashboardopbouw omvat metrics, producten en instellingen, cycli, storykandidaten, publicaties, leveringen, menselijke acties, overleggen en roadmapinformatie. Cycli en stories worden via afzonderlijke globale API-verzoeken opgehaald en in afzonderlijke secties weergegeven. Dat ondersteunt beheer en diagnose, maar sluit onvoldoende aan op de eigenaarsbehoefte om per cyclus direct opbrengst en vervolg te begrijpen.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/api.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/api.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart)

### “Beslisbron” is een afgeleide classificatie, geen opgeslagen provenance

De frontend kent uitsluitend Evaluatie-agent, Technische fout en Onbekend. Evaluatie-agent wordt afgeleid uit drie bewezen verdict/status-paren; FAILED zonder verdict maar met foutmelding wordt Technische fout; alle andere combinaties worden Onbekend. Dit is voorzichtig voor onbekende gevallen, maar het bewijst niet welke actor of guardrail de beslissing werkelijk nam.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart)

### Het huidige datamodel kan de gevraagde beslisser niet eenduidig beantwoorden

De cyclusregistratie bevat onder meer status, critic_verdict en error_message, maar geen decisionActor, decisionMechanism of afzonderlijke beslissingsevent. Daardoor kan de UI onderscheid tussen mens, evaluatie-agent, autonomiegate/guardrail en runtime alleen reconstrueren uit nevenvelden. Dat is het onderliggende datagat achter de eigenaarsfeedback.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/resources/db/migration/V3__shadow_iterations.sql](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/resources/db/migration/V3__shadow_iterations.sql), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationApi.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationApi.kt), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart)

### Een handmatige annulering kan als technische fout worden gelabeld

De annuleeractie zet een lopende cyclus op FAILED met standaardfoutmelding “Handmatig geannuleerd” en zonder criticVerdict. De huidige frontendregel classificeert precies FAILED + geen verdict + niet-lege foutmelding als Beslisbron: Technische fout. Dit is een concrete tegenstrijdigheid: de opgeslagen tekst noemt een menselijke actie, terwijl het overzicht een technische beslisbron toont.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationApi.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationApi.kt), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart)

### Guardrail- en eigenaarspaden zijn zichtbaar als reden, maar niet als beslisbron

De hoofdschermcode kent uitkomstredenen zoals POLICY_CONFLICT en OWNER_DECISION_REQUIRED en toont in detail een speciale toelichting wanneer een positief criticusoordeel alsnog door duplicaat- of guardrailblokkering niet doorgaat. De beslisbronclassificatie kent daarvoor echter geen afzonderlijke categorie. De reden en de beslisser kunnen dus conceptueel uiteenlopen of de beslisser blijft Onbekend.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart)

### Traceerbaarheid vereist gebeurtenisdata met wie, wat en wanneer

Airflow behandelt auditlogs als een gestructureerde historische registratie van wie of welk systeemonderdeel een actie initieerde, welke handeling plaatsvond en wanneer. Het onderscheidt gebruikersacties van systeemgebeurtenissen en bewaart onder meer actor, eventtype, tijdstip en run-id. Dit ondersteunt de gevolgtrekking dat expliciete provenance betrouwbaarder is dan achteraf classificeren uit een eindstatus.

Bronnen: [https://airflow.apache.org/docs/apache-airflow/3.1.3/security/audit_logs.html](https://airflow.apache.org/docs/apache-airflow/3.1.3/security/audit_logs.html)

### Acceptatieomgeving kon niet worden geïnspecteerd

Een echte Playwright/Chromium-poging is uitgevoerd, maar Chromium stopte vóór paginalading met SIGTRAP en “MachPortRendezvousServer … Permission denied (1100)”. Er zijn daarom geen betrouwbare livebevindingen over visuele hiërarchie, scanbaarheid, doorkliknavigatie of beheer. De repositorybeschrijving en eigenaarsfeedback mogen niet worden voorgesteld als vervanging van live visuele verificatie.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### Huidige applicatie

**Doel:** Product Factory is de autonome productontwikkelingsmotor voor de producteigenaar van Product Factory zelf en hkh-autopilot, later uitbreidbaar naar meer producten. Zij onderzoekt, kiest, ontwerpt en vormt stories, laat die door een criticus beoordelen, levert geaccepteerd werk begrensd aan Software Factory en gebruikt uitvoeringsresultaten in volgende cycli. Het dashboard moet de eigenaar vooral controle en begrip geven zonder reguliere handmatige tussenkomst.

**Wat ontbreekt:**
- De werkelijke beslisser of het beslismechanisme wordt niet expliciet opgeslagen; de UI reconstrueert dit uit eindstatus, criticVerdict en foutmelding.
- De categorieën Evaluatie-agent, Technische fout en Onbekend kunnen mens, autonomiegate, duplicaatcontrole en andere guardrails niet afzonderlijk weergeven.
- Een handmatig geannuleerde cyclus voldoet aan de huidige regel voor “Technische fout”, waardoor het overzicht feitelijk misleidend kan zijn.
- Reden, beslisbron en eindstatus komen uit verschillende afleidingen; er is geen centraal, onveranderlijk beslisrecord dat onderlinge consistentie afdwingt.
- Cycli en voortgekomen stories blijven technisch en visueel afzonderlijke globale informatiestromen; de samenhang per cyclus is nog onvoldoende direct zichtbaar.
- De actuele live bruikbaarheid en visuele duidelijkheid konden niet worden geverifieerd doordat Chromium vóór paginalading door de uitvoeringssandbox werd afgebroken.

### Verbetermogelijkheden

- Onderzoek een expliciet, append-only beslisrecord per terminale cyclusovergang met minimaal actorType, mechanism, reasonCode, timestamp en iterationId. Dit voorkomt reconstructie uit nevenvelden en sluit aan bij het wie/wat/wanneer-model van Airflow: https://airflow.apache.org/docs/apache-airflow/3.1.3/security/audit_logs.html.
- Scheid in het informatiemodel de initiator van een cyclus, de beoordelaar van kandidaten en het mechanisme dat de uiteindelijke cyclusstatus bepaalde. Een evaluatie-agent kan bijvoorbeeld ACCEPT adviseren terwijl een duplicaatcontrole of autonomiegate levering blokkeert; één generiek veld “Beslisbron” verbergt dat onderscheid.
- Los eerst de aantoonbare handmatige-annuleringscasus op in het begripsmodel: een gebruikersactie is geen technische fout. Gebruik daarbij de bestaande cancelcode en classificatieregels als regressiecasus: https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationApi.kt en https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart.
- Maak reden en beslisser op de cyclusregel afkomstig uit hetzelfde primaire beslisrecord en laat detailinformatie dezelfde bron gebruiken. Daarmee wordt tegenstrijdigheid tussen overzicht en detail structureel voorkomen in plaats van met steeds meer frontendheuristieken gecorrigeerd.
- Behoud progressive disclosure: toon op de regel een compacte, menselijke broncategorie en kernreden; ontsluit in detail de volledige beslisketen, criteria en technische gebeurtenissen. Airflow en GitHub Actions laten zien hoe runoverzicht en diepere diagnostiek kunnen worden gescheiden: https://airflow.apache.org/docs/apache-airflow/stable/ui.html en https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/viewing-workflow-run-history.
- Plan afzonderlijke live visuele verificatie zodra een agent-uitvoerbare Chromium-omgeving beschikbaar is; zonder screenshotbewijs blijven uitspraken over scanbaarheid, reflow en het beheergedeelte onzeker: https://product-factory-acceptance.vdzonsoftware.nl.

### Inspiratiebronnen

- [Apache Airflow Audit Logs](https://airflow.apache.org/docs/apache-airflow/3.1.3/security/audit_logs.html) — Registreert expliciet wie of welk systeemonderdeel wat deed en wanneer, gekoppeld aan een specifieke run; bruikbaar als conceptueel voorbeeld voor beslisprovenance.
- [Apache Airflow UI](https://airflow.apache.org/docs/apache-airflow/stable/ui.html) — Combineert compacte runstatus en recente fouten met afzonderlijke run-, taak-, event- en logdetails.
- [GitHub Actions workflow run history](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/viewing-workflow-run-history) — Laat eerst recente runs zien en ontsluit daarna een runsummary en status/logs per job en stap; relevant voor compacte overzicht-naar-detailnavigatie.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md) | 2026-08-12 | Publiek leesbaar; de GitHub Repository API meldt license: null, dus hergebruikrechten zijn onbekend. | Primaire productbeschrijving en afbakening van Product Factory ten opzichte van Software Factory en de workspace. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md) | 2026-08-12 | Publiek leesbaar; repositorylicentie ontbreekt volgens de GitHub Repository API. | Primaire functionele documentatie van cyclusketen, levering en dashboardonderdelen. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart) | 2026-08-12 | Publiek leesbare broncode; repositorylicentie ontbreekt volgens de GitHub Repository API. | Primaire bron voor de actuele dashboardstructuur, redenweergave, beslisbronbutton en guardrailtoelichting. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart) | 2026-08-12 | Publiek leesbare broncode; repositorylicentie ontbreekt volgens de GitHub Repository API. | Primaire bron voor de exacte afleidingsregels en gesloten waardenverzameling van Beslisbron. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/api.dart) | 2026-08-12 | Publiek leesbare broncode; repositorylicentie ontbreekt volgens de GitHub Repository API. | Toont welke globale datasets en cyclusdetails het dashboard afzonderlijk ophaalt. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/resources/db/migration/V3__shadow_iterations.sql) | 2026-08-12 | Publiek leesbare broncode; repositorylicentie ontbreekt volgens de GitHub Repository API. | Primaire bron voor de opgeslagen cyclusvelden en het ontbreken van expliciete beslisprovenance. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationApi.kt) | 2026-08-12 | Publiek leesbare broncode; repositorylicentie ontbreekt volgens de GitHub Repository API. | Primaire bron voor annuleren, statusmutatie en foutreden, waarmee de concrete misclassificatie aantoonbaar is. |
| [bron](https://api.github.com/repos/robbertvdzon/product-factory) | 2026-08-12 | GitHub API-output; repositoryveld license is null. | Controle van publieke status, default branch en licentie-indicatie van de productrepository. |
| [bron](https://product-factory-acceptance.vdzonsoftware.nl) | 2026-08-12 | Publiek toegankelijke acceptatieomgeving met dummydata; auteursrecht en licentie van de UI zijn onbekend. | Beoogde primaire bron voor actuele bruikbaarheid; inspectie mislukte vóór paginalading door een lokale Chromium-sandboxfout. |
| [bron](https://airflow.apache.org/docs/apache-airflow/3.1.3/security/audit_logs.html) | 2026-08-12 | Apache Airflow-project; documentatiebron valt onder Apache License 2.0 zoals vastgelegd in https://github.com/apache/airflow/blob/main/LICENSE. | Primaire documentatie van een bestaand workflowproduct dat actor, gebeurtenis, tijdstip en runcontext expliciet registreert. |
| [bron](https://airflow.apache.org/docs/apache-airflow/stable/ui.html) | 2026-08-12 | Apache Airflow-project; Apache License 2.0 volgens https://github.com/apache/airflow/blob/main/LICENSE. | Inspiratie voor overzicht-naar-detailnavigatie, recente runs, status en foutdiagnostiek. |
| [bron](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/viewing-workflow-run-history) | 2026-08-12 | GitHub Docs-inhoud is gepubliceerd onder Creative Commons Attribution 4.0 volgens https://github.com/github/docs/blob/main/LICENSE. | Inspiratie voor runhistorie waarbij overzicht, runsummary en job-/staplogs progressief worden ontsloten. |

## Productbeslissing

Introduceer één backward-compatible provenance-slice voor handmatige annulering. Voeg aan het cyclusmodel een optioneel, expliciet beslisrecord toe met iterationId, actorType, mechanism, reasonCode en decidedAt. Laat uitsluitend de bestaande annuleeractie dit record aanvankelijk vullen met actorType=HUMAN en mechanism=MANUAL_CANCELLATION. Het cyclusoverzicht en detailscherm tonen bron en reden uit ditzelfde record. Voor historische cycli zonder record blijft de bestaande afleiding zichtbaar, maar expliciet gemarkeerd als ‘afgeleid’ of ‘onbekend’. Zo wordt de aantoonbare onjuistheid ‘handmatig geannuleerd → technische fout’ geïsoleerd opgelost en ontstaat een toetsbare basis voor latere beslispaden, zonder gedrag van andere producten of de levering aan Software Factory te wijzigen.

**Waarom:** De huidige classificatie was begrijpelijk als kleine UI-oplossing: beschikbare velden zoals status, criticVerdict en errorMessage werden hergebruikt, zodat geen datamodelwijziging nodig was. Onderzoek toont nu echter dat die velden niet bewijzen wie de uitkomst bepaalde. De annuleeractie demonstreert het concrete gevolg: zij schrijft FAILED plus ‘Handmatig geannuleerd’, waarna de frontend dit als ‘Technische fout’ classificeert. Een beperkte, optionele provenance-slice corrigeert precies deze bewezen casus. De toevoeging is in isolatie te beoordelen, laat historische data intact, is functioneel terug te draaien door het nieuwe record niet meer te lezen en raakt geen authenticatie, andere producten of Software Factory-koppelingen. Onzeker blijft hoe goed de nieuwe weergave visueel scanbaar is, omdat acceptatie niet live kon worden geïnspecteerd; daarom hoort visuele validatie bij de acceptatiecriteria en niet bij aannames vooraf.

### Prioriteiten
- Definieer één gedeeld beslisrecord en een gesloten betekenis voor HUMAN en MANUAL_CANCELLATION; houd beoordelaar, initiator en uiteindelijk beslismechanisme conceptueel gescheiden.
- Sla het record atomair op bij de bestaande handmatige annuleeractie, met dezelfde iterationId en hetzelfde tijdstip als de terminale overgang; verander verder geen cyclus- of leveringsgedrag.
- Laat overzicht en detail dezelfde API-velden gebruiken voor ‘Beslisbron’ en reden. Expliciete provenance heeft voorrang; bestaande heuristiek blijft alleen fallback voor historische records en wordt als afgeleid herkenbaar gemaakt.
- Voeg regressietests toe voor minimaal: handmatige annulering is ‘Mens’ en nooit ‘Technische fout’; bestaande evaluatie-agentcycli zonder nieuw record behouden hun huidige weergave; onbekende historische combinaties blijven ‘Onbekend’.
- Verifieer op acceptatie dat bron en kernreden op de cyclusregel samen leesbaar zijn en dat detail exact dezelfde waarden toont. Als browserinspectie opnieuw technisch onmogelijk is, leg dat als onbevestigde UI-validatie vast en blokkeer alleen de visuele claim, niet de geautomatiseerde regressietests.

### Besluiten
- **Gebruik expliciete provenance als primaire bron en frontendclassificatie uitsluitend als historische fallback.** — Het huidige model bevat geen beslisser of beslisgebeurtenis. Actor, gebeurtenis, tijdstip en runcontext expliciet registreren voorkomt dat een eindstatus als bewijs voor de beslisser wordt behandeld.
- **Beperk de eerste implementatie tot het reeds bewezen pad voor handmatige annulering.** — De annuleeractie schrijft aantoonbaar FAILED met ‘Handmatig geannuleerd’, terwijl de huidige regel dit als technische fout classificeert. Deze smalle verticale slice is zelfstandig testbaar en levert direct correcte traceerbaarheid.
- **Toon bron en reden compact op de cyclusregel en gebruik in detail exact hetzelfde primaire record.** — Dit sluit aan op de eigenaarsbehoefte om de beslisser zonder zoeken in details te zien, terwijl diepere diagnostiek progressief ontsloten kan blijven. Eén gegevensbron voorkomt nieuwe tegenstrijdigheden tussen overzicht en detail.
- **Maak de datatoevoeging optioneel en backward-compatible; migreer of herschrijf historische cycli niet.** — Historische beslissers kunnen niet betrouwbaar uit nevenvelden worden gereconstrueerd. Niet invullen is eerlijker dan schijnzekerheid en beperkt het risico van een datamigratie.

## UX-voorstel: Handmatige annulering met expliciete beslisprovenance

**Gebruikersdoel:** Als producteigenaar wil ik in het cyclusoverzicht en -detail direct en betrouwbaar zien dat een cyclus door een mens handmatig is geannuleerd, zonder dat dit als technische fout wordt gepresenteerd.

### Flow
1. De eigenaar opent het dashboard en navigeert met toetsenbord of schermlezer naar de lijst met cycli.
2. Op de regel van een handmatig geannuleerde cyclus staan status ‘Geannuleerd’, beslisbron ‘Mens’ en kernreden ‘Handmatig geannuleerd’. Deze waarden komen uit het expliciete beslisrecord.
3. De eigenaar activeert de cyclusregel of de knop ‘Bekijk details’.
4. Het detailscherm toont onder ‘Beslissing’ dezelfde bron en reden, aangevuld met mechanisme ‘Handmatige annulering’ en het beslissingstijdstip.
5. De eigenaar keert terug naar het overzicht; focus wordt hersteld op de eerder geopende cyclusregel.
6. Bij een historische cyclus zonder beslisrecord gebruikt de interface de bestaande classificatie en markeert zij de bron zichtbaar en voor schermlezers als ‘Afgeleid’. Een niet-classificeerbare cyclus toont ‘Onbekend’.
7. Geautomatiseerde API-, component- en end-to-endtests controleren de volledige flow, inclusief toetsenbordbediening, toegankelijke namen, focusvolgorde, tekstcontrast en gelijkheid van overzichts- en detailwaarden.

### Wireframe

CYCLI

[Filter op status]  [Filter op beslisbron]

Cyclus #184                         Status: Geannuleerd
Product Factory · 12 aug 2026       Beslisbron: Mens
                                    Reden: Handmatig geannuleerd
                                    [Bekijk details]

Cyclus #183                         Status: Afgerond
Product Factory · 11 aug 2026       Beslisbron: Evaluatie-agent · Afgeleid
                                    [Bekijk details]

────────────────────────────────────────────────────
DETAIL — CYCLUS #184                              [Sluiten]

Status
Geannuleerd

Beslissing
Beslisbron:  Mens
Mechanisme:  Handmatige annulering
Reden:       Handmatig geannuleerd
Beslist op:  12 aug 2026, 14:32

[Terug naar cycli]

Semantiek: de volledige cyclusregel is geen verborgen klikvlak; ‘Bekijk details’ is een echte, benoemde knop. Status, bron en reden worden als tekst aangeboden en niet uitsluitend via kleur of iconen onderscheiden.

### Interactiehypotheses
- Als handmatige annulering een expliciet beslisrecord met actorType=HUMAN en mechanism=MANUAL_CANCELLATION oplevert, dan tonen API-, component- en end-to-endtests in zowel overzicht als detail ‘Mens’ en nooit ‘Technische fout’.
- Als overzicht en detail hetzelfde beslisrecord gebruiken, dan zijn actorType, mechanism, reasonCode en decidedAt in beide weergaven identiek; een contracttest vergelijkt de gerenderde waarden met één API-response.
- Als expliciete provenance voorrang heeft boven de historische heuristiek, dan blijft de weergave ‘Mens’ wanneer status=FAILED en errorMessage aanwezig zijn; een prioriteitstest dekt deze conflicterende invoer af.
- Als een historische cyclus geen beslisrecord heeft, dan blijft de bestaande evaluatie-agentclassificatie behouden en krijgt de zichtbare én toegankelijke naam de kwalificatie ‘Afgeleid’.
- Als historische velden geen betrouwbare classificatie toelaten, dan toont de interface ‘Onbekend’ en verzint zij geen actor; dit wordt met parametrische componenttests gecontroleerd.
- Als de compacte regel bron en reden als afzonderlijke tekstvelden toont, dan kan een geautomatiseerde DOM-test beide waarden zonder het detailscherm vinden en aan de juiste iterationId koppelen.

### Toegankelijkheid
- Alle acties zijn bereikbaar met alleen Tab, Shift+Tab, Enter en Spatie; een end-to-endtest controleert focusvolgorde en activering.
- Na openen krijgt de detailtitel programmatisch focus; na sluiten keert focus terug naar de knop van dezelfde cyclus.
- Gebruik semantische koppen, lijst- of tabelstructuur en echte buttons. Iedere cyclus, status, beslisbron en reden heeft een eenduidige toegankelijke naam en relatie.
- ‘Afgeleid’, ‘Onbekend’ en statussen worden als tekst aangeboden; betekenis is nooit uitsluitend afhankelijk van kleur, vorm of pictogram.
- Tekst en interactieve elementen voldoen geautomatiseerd aan minimaal WCAG AA-contrast: 4,5:1 voor normale tekst en 3:1 voor grote tekst en relevante UI-componenten.
- Bij 200% zoom en een viewport van 320 CSS-pixels blijft informatie zonder horizontaal scrollen beschikbaar; een geautomatiseerde screenshot- en overflowtest controleert dit.
- Geautomatiseerde axe- of gelijkwaardige controles rapporteren geen ernstige of kritieke overtredingen voor overzicht en detail.

### Privacy
- Het beslisrecord bevat uitsluitend operationele metadata van Product Factory: iterationId, actorType, mechanism, reasonCode en decidedAt.
- Sla geen naam, e-mailadres, account-id, vrije tekst of andere persoonsgegevens van de annulerende gebruiker op; ‘HUMAN’ beschrijft alleen het actortype.
- Neem geen gebruikersdata of identifiers uit andere producten op en toon die niet in overzicht, detail, logs of testfixtures.
- Gebruik een gesloten reasonCode en vaste presentatietekst; hergebruik errorMessage niet als provenance en voorkom daarmee onbedoelde weergave van vrije of gevoelige tekst.
- API-contracttests controleren dat het beslisrecord uitsluitend toegestane velden bevat; fixtures gebruiken synthetische operationele metadata.
- Telemetry registreert hoogstens iterationId, actorType, mechanism en reasonCode en bevat geen scherminhoud, vrije tekst of kruisproductdata.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is een kleine, backward-compatible en volledig agent-uitvoerbare verticale slice die de bewezen misclassificatie van handmatige annulering structureel corrigeert. De kandidaat respecteert privacy, houdt historisch en leveringsgedrag intact, gebruikt story:57 terecht als fallback-afhankelijkheid en bevat voldoende geautomatiseerde verificatie zonder handmatige eigenaaractie.
- **INFO · CONSISTENCY** — De kandidaat overlapt bewust met story:57, maar dupliceert die niet: story:57 blijft uitsluitend de historische fallback, terwijl expliciete provenance voortaan voorrang krijgt.
- **INFO · RIGHTS** — De productrepository heeft volgens de aangeleverde context geen expliciete licentie, maar de kandidaat vraagt geen overname van externe broncode of vormgeving. Airflow wordt alleen als conceptuele inspiratie gebruikt; dit belemmert veilige uitvoering niet.
- **WARNING · ACCESSIBILITY** — De kandidaat borgt tekstuele bron- en redenweergave en geautomatiseerde toegankelijkheidscontroles, maar noemt contrastwaarden, toetsenbordflow, focusherstel en reflow minder volledig dan het aangeleverde UX-ontwerp. Dit blokkeert niet omdat de nieuwe velden niet interactief zijn en de bindende dashboardregel tijdens implementatie geautomatiseerd kan worden bewaakt.

## Geaccepteerde storykandidaten

### Registreer en toon handmatige annulering als expliciete menselijke beslissing

_Sleutel: `registreer-handmatige-annulering-als-mens`_

Voeg aan een cyclus een optioneel beslisrecord toe met iterationId, actorType, mechanism, reasonCode en decidedAt. De bestaande annuleeractie schrijft dit record atomair met actorType=HUMAN, mechanism=MANUAL_CANCELLATION en reasonCode=MANUALLY_CANCELLED, zonder persoonsgegevens of vrije tekst. Het cyclusoverzicht en het detail gebruiken ditzelfde record en tonen respectievelijk ‘Beslisbron: Mens’, ‘Reden: Handmatig geannuleerd’ en in detail ook ‘Mechanisme: Handmatige annulering’ en het beslissingstijdstip. Expliciete provenance heeft voorrang boven de classificatie uit story:57. Historische cycli zonder record behouden die bestaande classificatie, met de zichtbare en toegankelijke kwalificatie ‘Afgeleid’; niet-classificeerbare combinaties blijven ‘Onbekend’. Er worden geen historische records teruggevuld en status-, criticus- en leveringsgedrag blijven ongewijzigd.

**Acceptatiecriteria**
- Een geautomatiseerde migratie- en repositorytest bewijst dat het optionele beslisrecord iterationId, actorType, mechanism, reasonCode en decidedAt kan opslaan en ophalen, zonder naam, e-mailadres, account-id of vrije-tekstveld.
- Een API-integratietest annuleert programmatisch een lopende cyclus en bewijst dat status en beslisrecord in dezelfde transactie worden vastgelegd met actorType=HUMAN, mechanism=MANUAL_CANCELLATION, reasonCode=MANUALLY_CANCELLED en een decidedAt gelijk aan het tijdstip van de terminale overgang.
- Een regressietest met status FAILED, een gevulde errorMessage en het expliciete annuleringsrecord toont in de cyclusregel ‘Beslisbron: Mens’ en ‘Reden: Handmatig geannuleerd’, en toont nergens voor deze cyclus ‘Technische fout’.
- Een component- of end-to-endtest bewijst dat het detail voor dezelfde cyclus exact dezelfde bron en reden als het overzicht toont, aangevuld met ‘Mechanisme: Handmatige annulering’ en het uit hetzelfde record afkomstige beslissingstijdstip.
- Geautomatiseerde fallbacktests bewijzen dat een historische cyclus zonder beslisrecord de classificatie uit story:57 behoudt en zichtbaar én in de toegankelijke naam als ‘Afgeleid’ wordt gemarkeerd, terwijl een niet-classificeerbare historische combinatie ‘Onbekend’ toont.
- Contracttests bewijzen dat cycli zonder beslisrecord geldig blijven, dat geen historische cyclus wordt teruggevuld en dat bestaande status-, criticVerdict- en leveringsvelden door deze wijziging niet veranderen.
- Geautomatiseerde widget- en toegankelijkheidstests bewijzen dat bron en reden zonder openen van het detail aan de juiste iterationId gekoppeld zijn, niet uitsluitend via kleur worden overgebracht en geen ernstige of kritieke axe-equivalente overtredingen introduceren.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/resources/db/migration/V3__shadow_iterations.sql](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/resources/db/migration/V3__shadow_iterations.sql), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationApi.kt](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/productfactory/src/main/kotlin/nl/vdzon/productfactory/iteration/ShadowIterationApi.kt), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/classification.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://airflow.apache.org/docs/apache-airflow/3.1.3/security/audit_logs.html](https://airflow.apache.org/docs/apache-airflow/3.1.3/security/audit_logs.html)

Afhankelijkheden: story:57 (herkend als bestaande stories: 57)

Risico's: Een apart beslisrecord en de bestaande cyclusstatus kunnen bij niet-atomische opslag uiteenlopen; transactie- en rollbacktests moeten dit voorkomen., De gesloten waarden zijn aanvankelijk alleen semantisch vastgesteld voor handmatige annulering en mogen niet zonder afzonderlijk onderzoek op guardrails of evaluatie-agentbeslissingen worden toegepast., De extra provenancevelden wijzigen backend-, API- en frontendcontracten tegelijk, waardoor compatibiliteit met historische records expliciet bewaakt moet worden., Live visuele scanbaarheid kon door de Chromium-sandboxfout niet worden vastgesteld; deze kandidaat claimt daarom alleen geautomatiseerd verifieerbare inhoudelijke en toegankelijkheidseigenschappen.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
