---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0054
date: 2026-08-17
status: approved
sources:
  - https://github.com/robbertvdzon/product-factory
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart
  - https://product-factory.vdzonsoftware.nl
  - https://product-factory-acceptance.vdzonsoftware.nl
  - https://design-system.service.gov.uk/components/error-message/
  - https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs
  - https://github.com/github/docs/blob/main/LICENSE
  - https://docs.sentry.io/product/issues/issue-details/
---
# Productcyclus 54

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De eerdere time-out is expliciet hersteld: repository, productie, acceptatie, beheer, twee productscopevarianten, breed scherm en 320×900 zijn werkelijk met Chromium bekeken en genavigeerd. De belangrijkste nog onbeantwoorde productvraag is nu: hoe kan Product Factory bij een technische cyclusuitval binnen tien seconden begrijpelijk maken wat misging, welke impact dat had, wie of wat de uitkomst bepaalde en welke vervolgstap veilig is—zonder de eigenaar herhaalde implementatielogs te laten interpreteren? De mobiele vindbaarheid uit iteratie 53 is inmiddels aantoonbaar geleverd; dit onderzoek neemt geen productbesluit en schrijft geen story.

### Product Factory is een productspecifieke autonome productregisseur

De applicatie organiseert voor de producteigenaar onderzoek, productkeuzes, UX en storyvorming per geregistreerd product. Geaccepteerde stories gaan naar Software Factory; uitvoering en evaluaties worden gevolgd en voeden volgende cycli. De operationele database bevat toestand zoals runs, wachtrijen, fouten en verwijzingen, terwijl goedgekeurde dossiers leesbaar in de workspace worden gepubliceerd.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md)

### De mobiele kernroute uit iteratie 53 is actueel geleverd

Op 320×900 staan omgeving/build, actief product, een expliciete sectiekeuze, cyclusstart en eerdere cycli direct bovenaan. De sectiekeuze benoemt onder meer Productcycli en Stories. De broncode plaatst in compacte modus start, cyclusgeschiedenis, gekoppelde stories en daarna pas de standaard ingeklapte operationele samenvatting. Het opnieuw onderzoeken van de eerdere vraag over verborgen mobiele kernsecties is daarom niet meer zinvol.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart)

### De twee productscopevarianten gedragen zich aantoonbaar verschillend maar verklaarbaar

HKH Autopilot toont een beschikbare cyclusstart, vier eerdere cycli en één gekoppelde story. Na een niet-mutatieve scopewissel toont Product Factory (synthetische acceptatie) vier cycli en twee gekoppelde stories; starten is uitgeschakeld met de zichtbare uitleg dat het product niet actief is en dat nog een voorwaarde ontbreekt. Daarmee is de productscope herkenbaar, maar blijft de eigenaar voor cyclusbewijs afhankelijk van de kwaliteit van de terminale regels en details.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### Technische uitval is traceerbaar maar nog niet rustig te begrijpen

HKH Autopilot-cyclus 4 toont in het overzicht ‘technische fout’, een gebruikersgerichte stopreden en ‘Technische fout (Afgeleid)’ als beslisbron. Het detail toont daarnaast drie vrijwel identieke JSON-parserfouten, geen agentresultaten en tegelijk de badge ‘kan doorgezet worden’. De eigenaar krijgt hierdoor veel diagnostiek, maar geen eenduidige uitleg van impact, voorwaarden voor doorgaan of de veiligste vervolgstap. Omdat acceptatie gescripte mockresponses gebruikt, bewijst dit alleen de presentatie van foutdata, niet de kwaliteit van echte AI-uitvoer.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### Besliscategorie en bronkwaliteit blijven vermengd

Terminale regels tonen onder meer ‘Technische fout (Afgeleid)’ en ‘Evaluatie-agent (Afgeleid)’, terwijl andere cycli voor de reden ‘Onbekend’ tonen. De inferentiestatus is dus onderdeel van de categorienaam in plaats van een afzonderlijke bronkwaliteit. Dat belemmert het onderscheid tussen expliciet vastgelegd bewijs, afleiding en ontbrekende provenance en bevestigt dat BUG-6 en de open capability voor beslisbewijs nog actueel zijn.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart)

### Op breed scherm blijft technische informatie vóór de dagelijkse productscope staan

Het brede overzicht toont eerst vijf metriekkaarten; cyclusgeschiedenis en stories zijn afzonderlijke secties. Beheeracties staan eveneens in het overzicht. De mobiele herordening heeft deze ruis aantoonbaar verminderd, maar de bredere epic voor één rustige productscope is daarmee nog niet volledig gerealiseerd.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart)

### Vergelijkbare systemen gebruiken progressieve foutdiagnose

GitHub Actions toont eerst runuitkomst en de falende stap en biedt daarna doorzoekbare of downloadbare logs. Sentry groepeert gebeurtenissen tot een issue, begint bij bron en impact en biedt vervolgens events, stacktrace en breadcrumbs. GOV.UK adviseert specifiek te beschrijven wat er misging en hoe herstel werkt, maar waarschuwt een serviceprobleem niet te presenteren als iets dat de gebruiker zelf kan repareren.

Bronnen: [https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs), [https://docs.sentry.io/product/issues/issue-details/](https://docs.sentry.io/product/issues/issue-details/), [https://design-system.service.gov.uk/components/error-message/](https://design-system.service.gov.uk/components/error-message/)

### Huidige applicatie

**Doel:** Product Factory helpt de producteigenaar per actieve productscope een autonome productcyclus starten, eerdere uitkomsten en hun bewijs begrijpen, gekoppelde stories volgen en geaccepteerd werk via Software Factory laten uitvoeren. Dezelfde motor onderzoekt Product Factory zelf zodat dashboard en orchestratie begrijpelijk, bruikbaar en zelfkritisch blijven.

**Wat ontbreekt:**
- Technische foutdetails beginnen niet met een rustige, gebruikersgerichte samenvatting van betekenis, impact en veilige vervolgstap.
- Drie identieke mislukte pogingen worden afzonderlijk en prominent herhaald in plaats van gegroepeerd.
- ‘Kan doorgezet worden’ wordt niet uitgelegd naast drie mislukte pogingen en ontbrekende agentresultaten.
- Beslisbroncategorie en inferentiestatus zijn samengevoegd; daardoor vallen zichtbare labels buiten de afgesproken gesloten categorieën.
- Sommige terminale cycli tonen ‘Onbekend’ als reden; de interface maakt niet duidelijk welk bewijs precies ontbreekt.
- Op breed scherm staan vijf technische metriekkaarten vóór de actieve productscope en blijven cycli en stories aparte secties.
- In de geraadpleegde UI is geen toets zichtbaar waarmee wordt vastgesteld of de eigenaar fout, beslisser en veilige vervolgstap daadwerkelijk binnen tien seconden begrijpt.

### Verbetermogelijkheden

- Onderzoek een gelaagd foutbewijs: eerst betekenis, impact en bronkwaliteit; daarna gegroepeerde pogingen; technische details uitsluitend als expliciete verdieping.
- Maak de vervolgstatus controleerbaar met afzonderlijke toestanden zoals automatisch opnieuw geprobeerd, veilig hervatbaar, beheercontrole nodig of geen actie mogelijk—alleen wanneer expliciete brondata dit ondersteunt.
- Toon precies één gesloten beslisbroncategorie en presenteer expliciet, afgeleid of onbekend als afzonderlijke bronkwaliteit.
- Groepeer identieke technische fouten en toon aantal pogingen en tijdsverloop, zodat herhaling bewijs toevoegt in plaats van ruis.
- Toets met synthetische actieve, afgewezen en technisch gefaalde cycli of de eigenaar binnen tien seconden kan aangeven wat misging, wie of wat besliste en wat veilig kan volgen, zonder logtekst te interpreteren.
- Beoordeel afzonderlijk of de mobiele taakhiërarchie ook op breed scherm toepasbaar is, zonder desktopfunctionaliteit of beheerbereik te verwijderen.
- Houd technische foutpayloads beperkt tot operationele metadata van Product Factory en voorkom vrije tekst, secrets of gegevens van andere producten in zichtbare diagnostiek.

### Inspiratiebronnen

- [GitHub Actions workflow run logs](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs) — Presenteert eerst runuitkomst en falende stap; volledige logs blijven gericht doorzoekbaar, downloadbaar en deelbaar als verdieping.
- [Sentry Issue Details](https://docs.sentry.io/product/issues/issue-details/) — Groepeert herhaalde events in één issue en scheidt bron, impact, aanbevolen event, stacktrace en breadcrumbs.
- [GOV.UK Error message guidance](https://design-system.service.gov.uk/components/error-message/) — Geeft geteste principes voor specifieke, begrijpelijke fouttaal en waarschuwt om serviceproblemen niet als door de gebruiker herstelbare invoerfout te presenteren.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://github.com/robbertvdzon/product-factory) | 2026-08-17 | Publieke repository; geen LICENSE-bestand of hergebruiklicentie aangetroffen op de geraadpleegde hoofdpagina, dus hergebruikrechten onbekend. | Visueel geraadpleegde repositoryhoofdpagina met projectstructuur, README en links naar architectuurdocumentatie. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md) | 2026-08-17 | Geen licentie aangetroffen in de publieke repository; hergebruikrechten onbekend. | Primaire bron voor productdoel, doelgroep, gegevensverdeling en relatie met Software Factory en workspace. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md) | 2026-08-17 | Geen licentie aangetroffen in de publieke repository; hergebruikrechten onbekend. | Primaire functionele documentatie over cyclusstart, agentketen, resultaten, levering, dashboard en beslisbewijs. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart) | 2026-08-17 | Geen licentie aangetroffen in de publieke repository; hergebruikrechten onbekend. | Actuele frontendimplementatie van productscope, mobiele sectiekeuze, kernvolgorde, bewijsregels en operationele samenvatting. |
| [bron](https://product-factory.vdzonsoftware.nl) | 2026-08-17 | Publieke loginpagina van de producteigenaar; geen hergebruiklicentie aangetroffen, dus rechten onbekend. | Verplichte productiecontrole; toont dat de productflow achter Google-authenticatie staat. |
| [bron](https://product-factory-acceptance.vdzonsoftware.nl) | 2026-08-17 | Eigen publieke acceptatieapp met representatieve nepdata; geen hergebruiklicentie aangetroffen, dus rechten onbekend. | Primaire visuele bron voor actuele brede en mobiele UI, productscopewisseling, cycli, stories, foutdetail en beheer. |
| [bron](https://design-system.service.gov.uk/components/error-message/) | 2026-08-17 | Open Government Licence v3.0, behalve waar anders vermeld; Crown copyright. | Primaire ontwerp- en toegankelijkheidsrichtlijn voor specifieke fouttaal en onderscheid tussen gebruikers- en serviceproblemen. |
| [bron](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs) | 2026-08-17 | GitHub Docs-content valt volgens de geraadpleegde github/docs-LICENSE onder Creative Commons Attribution 4.0 International. | Vergelijkbare functie die status, falende stap en verdiepende logs in lagen presenteert. |
| [bron](https://github.com/github/docs/blob/main/LICENSE) | 2026-08-17 | Creative Commons Attribution 4.0 International. | Rechtenindicatie voor de geraadpleegde GitHub Docs-content. |
| [bron](https://docs.sentry.io/product/issues/issue-details/) | 2026-08-17 | Publieke documentatie; geen specifieke hergebruiklicentie op de geraadpleegde pagina aangetroffen, dus onbekend. | Vergelijkbare issue-detailfunctie met gegroepeerde events, impact, stacktrace en breadcrumbs. |

## Productbeslissing

Maak technische cyclusuitval binnen de bestaande cyclusweergave in één kleine, terugdraaibare slice begrijpelijk: toon eerst een compacte foutbewijsregel met wat misging, de impact, precies één gesloten beslisbroncategorie en een afzonderlijke bronkwaliteit (‘expliciet’, ‘afgeleid’ of ‘onbekend’). Toon alleen een veilige vervolgstap wanneer expliciete toestand die ondersteunt. Groepeer identieke mislukte pogingen tot één samenvatting met aantal en tijdsverloop; behoud ruwe diagnostiek uitsluitend achter expliciete verdieping. Pas dit consistent toe in overzicht en detail, zonder cyclusdata te migreren of gedrag van andere producten en Software Factory-koppelingen te wijzigen.

**Waarom:** Er zijn geen open P0- of P1-bugs. De actuele acceptatiecontrole bevestigt wel BUG-6 en laat zien dat technische uitval veel diagnostiek maar onvoldoende betekenis biedt: de eigenaar ziet herhaalde parserfouten, geen agentresultaten en tegelijk een onverklaarde melding dat doorgaan mogelijk is. De gekozen slice draagt direct bij aan NOW-epic theme-product-factory-0002 en aan de missie om bestaand gedrag begrijpelijker te maken. Het huidige gedrag lijkt te zijn ontstaan vanuit operationele traceerbaarheid: foutpogingen en diagnostiek worden rechtstreeks zichtbaar gemaakt. Die informatie blijft beschikbaar, maar wordt progressief ontsloten. De wijziging is geïsoleerd te beoordelen met synthetische foutcycli en eenvoudig terug te draaien naar de bestaande presentatie.

### Prioriteiten
- Herstel eerst BUG-6: houd de gesloten beslisbroncategorie strikt gescheiden van bronkwaliteit; ‘(Afgeleid)’ mag geen onderdeel van de categorienaam zijn.
- Toon bovenaan betekenis en impact in producttaal, zonder een service- of parserprobleem als gebruikersfout te presenteren.
- Bereken geen handelingsadvies uit aannames: toon ‘veilig hervatbaar’, ‘beheercontrole nodig’ of een andere vervolgstap alleen bij expliciet bewijs; anders ‘vervolgstap onbekend’.
- Groepeer identieke pogingen en verplaats payloads, stacktraces en parserdetails naar een uitklapbare technische verdieping.
- Verifieer overzicht en detail met deterministische synthetische scenario’s: expliciete foutbron, afgeleide foutbron, ontbrekende provenance, herhaalde identieke fouten en tegenstrijdige vervolgstatus. Acceptatiecriterium: de eigenaar kan binnen tien seconden benoemen wat misging, wat de impact is, wie of wat de uitkomst bepaalde en of een veilige vervolgstap bekend is.

### Besluiten
- **Kies gelaagd foutbewijs als eerstvolgende productrichting binnen theme-product-factory-0002.** — De acceptatieomgeving toont concreet dat technische foutdata traceerbaar maar niet rustig interpreteerbaar is. De richting combineert die nieuwe bevinding met de al openstaande categorie-inconsistentie, zonder een bredere dashboardherbouw te vereisen.
- **Behoud technische diagnostiek, maar maak haar een expliciete tweede informatielaag.** — Het bestaande gedrag ondersteunt diagnose, maar herhaalde ruwe parsermeldingen belasten de dagelijkse productregie. Vergelijkbare systemen beginnen bij uitkomst, bron of falende stap en bieden logs, events en stacktraces als verdieping.
- **Presenteer alleen hersteladvies dat door expliciete toestand wordt gedragen.** — De huidige combinatie van drie mislukte pogingen, ontbrekende agentresultaten en ‘kan doorgezet worden’ is niet zelfverklarend. Richtlijnen voor foutmeldingen adviseren specifiek te maken wat misging en hoe herstel werkt, zonder een serviceprobleem ten onrechte bij de gebruiker neer te leggen.
- **Voer geen migratie of wijziging van orchestratie- en leveringsgedrag uit.** — De onderzochte tekortkoming zit aantoonbaar in de presentatie en interpretatie van bestaand foutbewijs. Een presentatieslice is kleiner, omkeerbaar en voorkomt risico voor andere producten en de Software Factory-koppeling.

## UX-voorstel: Gelaagd foutbewijs bij technische cyclusuitval

**Gebruikersdoel:** Binnen tien seconden begrijpen wat er misging, wat de impact is, wie of wat de uitkomst bepaalde en of een veilige vervolgstap bekend is, zonder implementatielogs te interpreteren.

### Flow
1. De eigenaar opent Productcycli binnen de actieve productscope.
2. Een technisch mislukte cyclus toont in het overzicht één compacte foutbewijsregel met status, betekenis, impact, beslisbroncategorie, afzonderlijke bronkwaliteit en vervolgstatus.
3. De eigenaar opent de cyclus. Het detail herhaalt bovenaan dezelfde kerninformatie, zodat overzicht en detail semantisch consistent zijn.
4. Identieke mislukte pogingen staan gegroepeerd als één regel met het aantal pogingen en het tijdsverloop.
5. Alleen als expliciete toestand een veilige actie ondersteunt, verschijnt een concrete vervolgstap. Anders staat er ‘Vervolgstap onbekend’ zonder actieknop.
6. De eigenaar kan ‘Technische details tonen’ uitklappen om gesaniteerde operationele diagnostiek per poging te bekijken.
7. Terug navigeren behoudt de actieve productscope en brengt de eigenaar terug naar dezelfde positie in de cycluslijst.

### Wireframe

OVERZICHT — Productcycli

[Technische fout] Cyclus 4                         [Details bekijken]
Wat ging mis: De cyclusuitvoer kon niet worden verwerkt.
Impact: Geen agentresultaten; de cyclus is gestopt.
Beslisbron: Technische fout
Bronkwaliteit: Afgeleid
Vervolgstap: Onbekend
Pogingen: 3 identieke fouten in 42 seconden

DETAIL — Cyclus 4

Technische fout
Wat ging mis
De cyclusuitvoer kon niet worden verwerkt.

Impact
Geen agentresultaten; er is niets doorgezet naar Software Factory.

Beslisbewijs
Beslisbron: Technische fout
Bronkwaliteit: Afgeleid

Veilige vervolgstap
Vervolgstap onbekend
[geen actieknop]

Pogingen
3 identieke fouten · eerste 10:21:03 · laatste 10:21:45

[▸ Technische details tonen]
  Fouttype: JSON-parserfout
  Poging 1 …
  Poging 2 …
  Poging 3 …

### Interactiehypotheses
- Als foutbewijs met betekenis en impact begint, dan bevatten overzicht en detail voor elk synthetisch foutscenario dezelfde verwachte velden en teksten; toets dit met component- en snapshottests.
- Als beslisbroncategorie en bronkwaliteit afzonderlijke velden zijn, dan behoort iedere categorie exact tot de gesloten toegestane set en bevat geen categorielabel ‘Afgeleid’, ‘Expliciet’, ‘Onbekend’ of haakjessuffixen; toets dit met parametrische tests.
- Als vervolgadvies uitsluitend uit expliciete toestand komt, dan verschijnt een actieknop alleen bij synthetische fixtures met een expliciet ondersteunde actie; bij afgeleide, ontbrekende of tegenstrijdige toestand verschijnt ‘Vervolgstap onbekend’; toets dit met beslismatrixtests.
- Als identieke fouten worden gegroepeerd, dan levert een fixture met drie gelijke foutvingerafdrukken één samenvattingsregel met aantal 3 en correct tijdsverloop op, terwijl verschillende vingerafdrukken afzonderlijke groepen vormen; toets dit met unit- en componenttests.
- Als technische diagnostiek progressief wordt ontsloten, dan staat ruwe diagnostiek aanvankelijk niet in de zichtbare of toegankelijkheidsboom en wordt deze pas na activering van de uitklapbediening beschikbaar; toets dit met browser- en toegankelijkheidstests.
- Als overzicht en detail één bewijsmodel gebruiken, dan zijn betekenis, impact, categorie, bronkwaliteit en vervolgstatus voor dezelfde fixture identiek; toets dit met contracttests tegen gedeelde synthetische scenario’s in plaats van productiegegevens.

### Toegankelijkheid
- Alle informatie en bediening moet volledig met toetsenbord bereikbaar zijn, met een zichtbare focusindicator en logische focusvolgorde.
- Gebruik een echte knop voor ‘Technische details tonen’, met programmatisch beschikbare naam en actuele aria-expanded-toestand; verplaats focus niet automatisch bij uitklappen.
- Maak status niet uitsluitend met kleur herkenbaar: combineer kleur met tekst en, indien gebruikt, een decoratief pictogram dat voor schermlezers verborgen is.
- Gebruik semantische koppen en definitielijsten voor betekenis, impact, beslisbewijs en vervolgstap, zodat schermlezers de structuur efficiënt kunnen navigeren.
- Zorg voor minimaal WCAG AA-contrast: 4,5:1 voor normale tekst en 3:1 voor grote tekst, focusindicatoren en betekenisvolle UI-componenten.
- Laat geautomatiseerde browsertests de flow op breed scherm en 320×900 uitvoeren met uitsluitend toetsenbordacties; voer daarnaast axe-core- of gelijkwaardige checks uit op overzicht, detail en open technische verdieping.
- Gebruik geen automatisch verdwijnende foutinformatie en vermijd live-regionmeldingen bij alleen het openen van bestaande details.

### Privacy
- Gebruik uitsluitend operationele metadata van Product Factory zelf, zoals cyclus-ID, fouttype, pogingnummer, tijdstip, duur, broncategorie en bronkwaliteit.
- Toon geen persoonsgegevens, vrije gebruikersinvoer of gegevens en payloads van andere producten in foutbewijs of technische details.
- Sanitiseer diagnostiek vóór presentatie: verwijder tokens, secrets, autorisatieheaders, URL-queryparameters, bestandspaden met gebruikersnamen en onbegrensde request- of responsepayloads.
- Gebruik deterministische synthetische fixtures voor alle validatie; haal geen productiegegevens, externe productdata of echte logpayloads op.
- Maak technische details standaard ingeklapt en begrens inhoud en lengte, maar behandel inklappen niet als privacymaatregel: gevoelige data mag ook na uitklappen niet aanwezig zijn.
- Voeg geautomatiseerde regressietests toe met herkenbare canary-secrets en persoonsgegevens; de test slaagt alleen wanneer deze nergens in gerenderde tekst, DOM of toegankelijkheidsboom voorkomen.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is een kleine, read-only en terugdraaibare reparatie van BUG-6. Uitvoering en verificatie zijn volledig automatiseerbaar met synthetische fixtures; er is geen eigenaaractie, migratie, productie-inzage of mutatie nodig. De beperktere scope levert nog niet het volledige gelaagde foutbewijs, maar dat is geen blokkade voor deze zelfstandig toetsbare slice.
- **INFO · RIGHTS** — Voor de projectspecifieke repositorybronnen is geen hergebruiklicentie aangetroffen. De kandidaat gebruikt deze bronnen alleen als bewijs van bestaand gedrag en vereist geen overname van beschermde inhoud; dit blokkeert de implementatie daarom niet.
- **INFO · SCOPE** — De kandidaat scheidt alleen beslisbroncategorie en bronkwaliteit. Betekenis, impact, gegroepeerde foutpogingen en een expliciet onderbouwde vervolgstap blijven buiten deze slice. Dat is een aanvaardbare begrenzing omdat BUG-6 hiermee zelfstandig, veilig en terugdraaibaar wordt hersteld.
- **INFO · CONSISTENCY** — De kandidaat overlapt bewust met het reeds geleverde classificatiemodel uit story:57 en de presentaties uit stories 85 en 60, maar levert niet exact hetzelfde resultaat: hij corrigeert de huidige vermenging van categorie en kwaliteitskwalificatie en borgt consistentie tussen overzicht en detail.

## Geaccepteerde storykandidaten

### Scheid beslisbroncategorie van bronkwaliteit bij terminale cycli

_Sleutel: `scheid-beslisbron-en-bronkwaliteit`_
_Bug: `BUG-6`_

Herstel BUG-6 door in overzicht en cyclusdetail precies één beslisbroncategorie uit de gesloten bestaande set ‘Evaluatie-agent’, ‘Technische fout’ of ‘Onbekend’ te tonen en de kwalificatie daarvan afzonderlijk weer te geven als ‘Expliciet’, ‘Afgeleid’ of ‘Onbekend’. Gebruik in beide weergaven één gedeeld presentatiemodel op basis van bestaande cyclusdata. Verwijder kwalificaties zoals ‘(Afgeleid)’ uitsluitend uit de categorienaam; vul ontbrekende provenance niet aan en migreer geen historische cycli. Actieve cycli blijven vrij van terminale bewijsvelden. De wijziging is read-only en verandert geen cyclusstatus, orchestratie, andere productdata of Software Factory-koppeling.

**Acceptatiecriteria**
- Geautomatiseerde parametrische tests bewijzen voor alle ondersteunde terminale scenario’s dat ‘Beslisbron’ exact één waarde uit ‘Evaluatie-agent’, ‘Technische fout’ of ‘Onbekend’ bevat en nooit een haakjessuffix of de woorden ‘Expliciet’ of ‘Afgeleid’.
- Iedere terminale cyclus toont naast ‘Beslisbron’ een afzonderlijk gelabelde ‘Bronkwaliteit’ met exact één waarde uit ‘Expliciet’, ‘Afgeleid’ of ‘Onbekend’; ontbrekende of tegenstrijdige provenance resulteert conservatief in ‘Onbekend’ en wordt niet als feit aangevuld.
- Contracttests met deterministische synthetische fixtures bewijzen dat overzicht en detail voor dezelfde cyclus identieke waarden voor beslisbron en bronkwaliteit tonen, inclusief expliciete, afgeleide, ontbrekende en tegenstrijdige brondata.
- Geautomatiseerde componenttests bewijzen dat actieve cycli in overzicht en detail geen terminale velden voor beslisbron of bronkwaliteit tonen.
- Browsertests voeren de bewijsroute op een breed scherm en op 320×900 volledig met het toetsenbord uit en bevestigen dat labels, waarden en de bestaande detailactie programmatisch herkenbaar en bereikbaar zijn.
- Regressietests bewijzen dat de wijziging geen historische data migreert en geen muterende API-aanroep, cyclusstatuswijziging, cross-productwrite of Software Factory-levering veroorzaakt.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md)

Afhankelijkheden: story:57, story:85 (herkend als bestaande stories: 57, 85)

Risico's: Bestaande overzichts- en detaillogica kunnen bronkwaliteit verschillend afleiden; zonder één gedeeld presentatiemodel blijft semantische tegenspraak mogelijk., Historische cycli bevatten mogelijk onvoldoende of tegenstrijdige provenance, waardoor ‘Onbekend’ vaker zichtbaar wordt; dit is eerlijker maar kan bestaande schijnzekerheid verminderen., Een uitsluitend tekstuele aanpassing kan BUG-6 cosmetisch verbergen terwijl interne mappings buiten de gesloten sets blijven; daarom moeten tests de waarden vóór rendering valideren.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
