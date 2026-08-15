---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0048
date: 2026-08-15
status: approved
sources:
  - https://github.com/robbertvdzon/product-factory
  - https://github.com/robbertvdzon/product-factory/blob/main/README.md
  - https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart
  - https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/product_scope.dart
  - https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/iteration_evidence.dart
  - https://github.com/robbertvdzon/product-factory/blob/main/docs/stories/product-factory-32-Toon-afgeronde-Product-Factory-cycli-als-compacte-bewijsregels.md
  - https://github.com/robbertvdzon/product-factory/blob/main/docs/stories/product-factory-34-Bundel-de-drie-kernacties-onder-een-actieve-productscope.md
  - https://product-factory.vdzonsoftware.nl
  - https://product-factory-acceptance.vdzonsoftware.nl
  - https://design-system.service.gov.uk/components/button/
  - https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs
  - https://docs.github.com/en/actions/how-tos/manage-workflow-runs
---
# Productcyclus 48

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Belangrijkste nog onbeantwoorde productvraag: hoe maakt Product Factory direct begrijpelijk waarom de primaire actie ‘Start productcyclus nu’ niet beschikbaar is en wat de eigenaar vervolgens veilig kan doen? Op acceptatie is de knop voor Product Factory uitgeschakeld zonder uitleg. De broncode koppelt beschikbaarheid aan productstatus en workspaceOwnership, niet aan de eveneens zichtbare extreem langlopende cyclus. De UI laat de eigenaar daardoor zelf naar de oorzaak raden. Dit raakt de open epic rond de drie kernacties rechtstreeks. Er is nog geen productbesluit genomen.

### Productspecifieke hoofdflow is inmiddels zichtbaar

Acceptatie biedt één compacte productkeuze. Na selectie van Product Factory staan ‘Cyclus starten’ en ‘Eerdere cycli’ binnen de gekozen scope; terminale Product Factory-cycli verschijnen als compacte bewijsregels met Datum, Cyclusuitkomst, Reden, Beslisbron, Gekoppelde opbrengst en ‘Bekijk bewijs’. De publieke repository bevat hiervoor expliciete selectie-, filter- en bewijslogica.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/product_scope.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/product_scope.dart), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/iteration_evidence.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/iteration_evidence.dart)

### De primaire startactie is onverklaard uitgeschakeld

Voor de synthetische Product Factory-scope is ‘Start productcyclus nu’ zichtbaar maar uitgeschakeld. Er staat geen toelichting naast de knop. De huidige frontendcode schakelt de actie uitsluitend in wanneer Product.status exact ‘active’ is en workspaceOwnership exact ‘product-factory’ is. Die voorwaarden en de falende waarde zijn niet zichtbaar op het hoofdscherm.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart)

### De zichtbare langlopende cyclus verklaart de blokkade niet

De actieve kaart toont iteratie 9204 als RUNNING met rol Onderzoeker en een looptijd van 5348 uur. Dit lijkt verdacht, maar de geraadpleegde startknoplogica controleert geen actieve cyclus. Het zou daarom onjuist zijn om zonder aanvullend operationeel contract te stellen dat deze cyclus de knop blokkeert. Wel ontbreekt voor de eigenaar een betrouwbaar onderscheid tussen werkelijk actief, wachtend en mogelijk vastgelopen werk.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart)

### De actieve kaart blijft technisch georiënteerd

De kaart toont status, huidige agentrol, starttijd, totale looptijd, aantallen kandidaten en leveringen en een backendcyclusregel. Zij toont geen laatste betekenisvolle voortgang, wachtoorzaak of eigenaar-gerichte gezondheidsindicatie. Totale looptijd alleen is onvoldoende bewijs dat een cyclus is vastgelopen.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart)

### Beheer werkt productspecifiek en detailnavigatie is aanwezig

Beheer op acceptatie nam de actieve Product Factory-scope over, maakte de scope zichtbaar in de lijstkoppen en toonde gekoppelde Software Factory-stories en de storywachtrij. Een geopend storydetail bevatte status, sleutel, fase, omschrijving, acceptatiecriteria en criticusbeoordeling.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/docs/stories/product-factory-34-Bundel-de-drie-kernacties-onder-een-actieve-productscope.md](https://github.com/robbertvdzon/product-factory/blob/main/docs/stories/product-factory-34-Bundel-de-drie-kernacties-onder-een-actieve-productscope.md)

### Een stille disabled-knop is een erkend begrips- en toegankelijkheidsrisico

GOV.UK waarschuwt dat disabled knoppen door laag contrast en onduidelijkheid verwarrend kunnen zijn en alleen gebruikt moeten worden wanneer onderzoek aantoont dat dit de interface begrijpelijker maakt. Dat ondersteunt nader onderzoek naar een zichtbare reden of een alternatief interactiepatroon, maar schrijft nog geen specifieke Product Factory-oplossing voor.

Bronnen: [https://design-system.service.gov.uk/components/button/](https://design-system.service.gov.uk/components/button/)

### Vergelijkbare run-interfaces scheiden toestand, diagnose en herstel

GitHub Actions maakt per run onderscheid tussen lopend en afgerond, toont jobs en stappen met logs voor diagnose en biedt afzonderlijke beheeracties zoals annuleren en opnieuw uitvoeren. Dit is bruikbare inspiratie voor gelaagde informatie: een korte status op overzichtsniveau, doorklikbare diagnose en expliciete herstelacties. Product Factory moet dit patroon niet letterlijk overnemen en moet annulering afzonderlijk op risico beoordelen.

Bronnen: [https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs), [https://docs.github.com/en/actions/how-tos/manage-workflow-runs](https://docs.github.com/en/actions/how-tos/manage-workflow-runs)

### Huidige applicatie

**Doel:** Product Factory organiseert voor de eigenaar autonoom productonderzoek, productkeuzes, UX-ontwikkeling en storyvorming voor geregistreerde producten. Het levert stories aan Software Factory, volgt de uitvoering en verwerkt resultaten in volgende iteraties. Het dashboard moet de eigenaar vooral in staat stellen een cyclus te starten, eerdere opbrengsten te begrijpen en voortgekomen stories te volgen.

**Wat ontbreekt:**
- De primaire actie ‘Start productcyclus nu’ kan uitgeschakeld zijn zonder zichtbare reden, terwijl de onderliggende code minstens twee verschillende voorwaarden kent. De eigenaar kan op het hoofdscherm niet bepalen welke voorwaarde faalt.
- Een extreem langlopende synthetische RUNNING-cyclus toont alleen totale looptijd, huidige rol en technische tellers. Er is geen betrouwbare zichtbare indicatie van laatste voortgang, wachten, blokkade of mogelijke stilstand.
- De combinatie van een disabled startactie en een langlopende cyclus wekt een causale indruk die de geraadpleegde frontendcode niet ondersteunt. Dit vergroot het risico op een verkeerde diagnose door de eigenaar.
- De actieve kaart bevat veel interne termen, waaronder backendcyclus, kandidaten, leveringen en criticusstatus, terwijl de eigenaar-gerichte betekenis en veilige volgende stap minder prominent zijn.
- Productie is achter Google-authenticatie en kon volgens de opdracht niet inhoudelijk worden onderzocht; verschillen tussen productie en acceptatie blijven daarom onbekend.
- Op het zichtbare acceptatiescherm ontbreekt een expliciete verklaring of synthetische langlooptijden representatief zijn. De banner verklaart wel dat de dataset synthetisch is, zodat 5348 uur niet als productie-incident mag worden geïnterpreteerd.

### Verbetermogelijkheden

- Onderzoek of de startactie actief kan blijven als uitlegbare bediening die bij niet-beschikbaarheid de exacte reden en veilige vervolgstap toont, in plaats van een stille disabled knop. Laat productstatus en workspaceOwnership daarbij in eigenaarstaal vertalen.
- Plaats direct bij ‘Cyclus starten’ een korte, datagedreven beschikbaarheidsmelding, bijvoorbeeld welke concrete voorwaarde starten verhindert. Vermijd aannames dat een zichtbare RUNNING-cyclus automatisch de oorzaak is.
- Onderzoek welke bestaande operationele timestamps of fase-events betrouwbaar ‘laatste betekenisvolle voortgang’ kunnen leveren. Toon geen ‘vastgelopen’-label op basis van alleen totale looptijd.
- Overweeg een conservatieve tussentoestand zoals ‘mogelijk geen recente voortgang’ die de backendstatus RUNNING niet overschrijft, duidelijk maakt waarop de indicatie is gebaseerd en naar read-only diagnose leidt.
- Vervang of verduidelijk technische actieve-kaartregels vanuit de eigenaarstaak: huidige fase, sinds wanneer, laatste bevestigde overgang en waarom de volgende kernactie wel of niet beschikbaar is. Houd ruwe technische details secundair.
- Gebruik het bestaande cyclusdetail als diagnosepad voordat nieuwe muterende herstelacties worden overwogen. Annuleren, timeoutbeleid en automatische statuscorrectie hebben grotere operationele gevolgen en vragen afzonderlijk onderzoek.
- Toets met toetsenbord en schermlezer of een beschikbaarheidsreden programmatisch aan de startactie gekoppeld is en niet uitsluitend via kleur, disabled styling of visuele nabijheid wordt overgebracht.
- Valideer de hypothese eerst met synthetische varianten voor inactief product, verkeerd workspaceOwnership, werkelijk lopende cyclus, wachtende worker en ontbrekende metadata; zo kan worden bepaald of één patroon alle oorzaken begrijpelijk afdekt.

### Inspiratiebronnen

- [GitHub Actions workflow runs](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs) — Scheidt overzichtsstatus, jobs/stappen, tijdsduur en doorklikbare logs. Het patroon kan inspireren tot een compacte eigenaarstatus met afzonderlijke diagnose, zonder de technische UI letterlijk over te nemen.
- [GitHub Actions run management](https://docs.github.com/en/actions/how-tos/manage-workflow-runs) — Maakt starten, annuleren en opnieuw uitvoeren expliciete, afzonderlijke acties met eigen voorwaarden. Dit illustreert dat beschikbaarheid en herstel begrijpelijker worden wanneer acties niet impliciet uit één statusbadge moeten worden afgeleid.
- [GOV.UK Design System – Button](https://design-system.service.gov.uk/components/button/) — Geen vergelijkbare workflowapp, maar een relevante interactiereferentie: disabled knoppen kunnen verwarren en horen alleen gebruikt te worden wanneer ze aantoonbaar meer duidelijkheid geven.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://github.com/robbertvdzon/product-factory) | 2026-08-15 | Publieke repository; GitHub rapporteert geen gedeclareerde licentie. Hergebruiksrechten zijn daarom onbekend/voorbehouden. | Vastgesteld dat dit de publieke Kotlin-repository is en README, dashboardfrontend, backend en documentatie bevat. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/README.md) | 2026-08-15 | Geen gedeclareerde repositorylicentie; hergebruiksrechten onbekend/voorbehouden. | Beschrijft doel, doelgroepcontext, autonome productcyclus, Software Factory-overdracht en scheiding tussen operationele database en leesbare workspace. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart) | 2026-08-15 | Geen gedeclareerde repositorylicentie; hergebruiksrechten onbekend/voorbehouden. | Bevat de actuele hoofdscherm-, startknop-, actieve-cyclus-, detail- en beheerpresentatie. Bevestigt de exacte enablementvoorwaarden van de startactie. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/product_scope.dart) | 2026-08-15 | Geen gedeclareerde repositorylicentie; hergebruiksrechten onbekend/voorbehouden. | Bevestigt canonieke productslugselectie, productspecifieke filtering, lokale voorkeur en beheerscope. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/iteration_evidence.dart) | 2026-08-15 | Geen gedeclareerde repositorylicentie; hergebruiksrechten onbekend/voorbehouden. | Bevestigt welke terminale statussen compacte bewijsregels krijgen en hoe uitkomst, reden en beslisbron worden gepresenteerd. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/docs/stories/product-factory-32-Toon-afgeronde-Product-Factory-cycli-als-compacte-bewijsregels.md) | 2026-08-15 | Geen gedeclareerde repositorylicentie; hergebruiksrechten onbekend/voorbehouden. | Legt de bedoelde compacte bewijsweergave en haar begrenzing tot terminale Product Factory-cycli vast. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/docs/stories/product-factory-34-Bundel-de-drie-kernacties-onder-een-actieve-productscope.md) | 2026-08-15 | Geen gedeclareerde repositorylicentie; hergebruiksrechten onbekend/voorbehouden. | Beschrijft de reeds geïmplementeerde productscope, vaste volgorde van kernacties en productspecifiek Beheer. |
| [bron](https://product-factory.vdzonsoftware.nl) | 2026-08-15 | Publiek bereikbare loginpagina; auteurs- en hergebruiksrechten onbekend. Geen inhoud hergebruikt. | Productieomgeving is met Chromium bekeken; inhoudelijke productflow bleek zonder authenticatie niet toegankelijk. |
| [bron](https://product-factory-acceptance.vdzonsoftware.nl) | 2026-08-15 | Publiek raadpleegbare acceptatie-UI met synthetische data; auteurs- en hergebruiksrechten onbekend. Alleen onderzocht, niet hergebruikt. | Primaire live bron voor bruikbaarheid, productscope, compacte bewijsregels, actieve cyclus, uitgeschakelde startactie en Beheer. |
| [bron](https://design-system.service.gov.uk/components/button/) | 2026-08-15 | Open Government Licence v3.0, behalve waar anders vermeld; Crown copyright. | Onderbouwt het begrips- en toegankelijkheidsrisico van disabled knoppen zonder duidelijke meerwaarde. |
| [bron](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs) | 2026-08-15 | Rechtenindicatie op deze specifieke pagina niet afzonderlijk vastgesteld; hergebruik niet beoogd. | Publieke documentatie van een bestaande run-interface die status, stappen, tijdsduur en doorklikbare diagnose combineert. |
| [bron](https://docs.github.com/en/actions/how-tos/manage-workflow-runs) | 2026-08-15 | Rechtenindicatie op deze specifieke pagina niet afzonderlijk vastgesteld; hergebruik niet beoogd. | Publieke documentatie van afzonderlijke acties voor starten, annuleren en opnieuw uitvoeren van workflowruns. |

## Productbeslissing

Maak de primaire actie ‘Start productcyclus nu’ zelfverklarend: behoud de bestaande startvoorwaarden en het uitgeschakelde gedrag, maar toon direct bij de actie in eigenaarstaal welke concrete voorwaarde starten verhindert en welke veilige, niet-muterende vervolgstap beschikbaar is. Deze kleine richting sluit rechtstreeks aan op roadmap-epic theme-product-factory-0001 en verandert geen cyclus-, product- of Software Factory-gedrag.

**Waarom:** Het huidige gedrag is vermoedelijk conservatief ontworpen: starten is alleen toegestaan wanneer het product exact actief is en de workspace door Product Factory wordt beheerd. Dat beschermt tegen starten in een ongeschikte scope, maar de interface toont nu alleen de uitkomst van die controle en niet de reden. Daardoor kan de eigenaar de zichtbare langlopende RUNNING-cyclus ten onrechte als oorzaak zien, terwijl de geraadpleegde startlogica die cyclus niet controleert. Door uitsluitend de bestaande beschikbaarheidsbeslissing uit te leggen, wordt de kernactie begrijpelijker zonder risicovolle wijzigingen aan orchestratie, authenticatie, andere producten of de Software Factory-koppeling.

### Prioriteiten
- Definieer één uitlegbaar beschikbaarheidsmodel dat dezelfde voorwaarden gebruikt als de startactie en per falende voorwaarde een eigenaarstekst oplevert: product niet actief, workspace niet door Product Factory beheerd, of beschikbaarheid niet betrouwbaar vast te stellen.
- Toon de reden direct en programmatisch gekoppeld aan ‘Start productcyclus nu’; gebruik niet uitsluitend kleur, disabled styling of visuele nabijheid. Bij meerdere falende voorwaarden wordt één primaire reden met compacte aanvullende context getoond.
- Bied alleen een veilige, read-only vervolgstap wanneer die werkelijk helpt, zoals productscope controleren of details bekijken. Voeg geen annulering, retry, statuscorrectie of andere muterende herstelactie toe.
- Maak expliciet dat een zichtbare RUNNING-cyclus alleen als blokkadereden mag worden genoemd wanneer het startcontract dat daadwerkelijk bevestigt. Leid dit nooit af uit totale looptijd.
- Toets de wijziging geïsoleerd met synthetische varianten voor een actief geldig product, inactief product, afwijkend workspaceOwnership, ontbrekende metadata en een langlopende RUNNING-cyclus. Verifieer daarbij dat startbeschikbaarheid ongewijzigd blijft en dat elke blokkade een begrijpelijke reden heeft.

### Besluiten
- **Behoud de bestaande enablementvoorwaarden en wijzig alleen hun presentatie.** — Dit maakt de verbetering klein, terugdraaibaar en onafhankelijk te beoordelen. De strikte voorwaarden lijken een beschermingsmechanisme; onderzoek rechtvaardigt niet dat ze worden versoepeld.
- **Plaats een concrete beschikbaarheidsreden direct bij de primaire startactie.** — Op acceptatie is de actie zonder uitleg uitgeschakeld. Een stille disabled knop laat de eigenaar raden en vormt een bekend begrips- en toegankelijkheidsrisico.
- **Vertaal interne voorwaarden naar eigenaarstaal, maar behoud een eerlijke onbekende toestand wanneer gegevens ontbreken.** — De huidige beslissing gebruikt technische waarden voor productstatus en workspaceOwnership. Een expliciete onbekende toestand voorkomt dat de interface een niet-aangetoonde oorzaak presenteert.
- **Behandel een langlopende RUNNING-cyclus niet automatisch als blokkade of als vastgelopen.** — De zichtbare totale looptijd wekt een causale indruk, maar de onderzochte startlogica controleert geen actieve cyclus en looptijd alleen bewijst geen stilstand.
- **Gebruik gelaagde, read-only diagnose als vervolgstap en houd herstelacties buiten deze richting.** — Vergelijkbare run-interfaces scheiden status, diagnose en beheeracties. Dat ondersteunt een korte verklaring met doorklikbare details, zonder nu risicovollere mutaties te introduceren.

## UX-voorstel: Zelfverklarende beschikbaarheid van ‘Start productcyclus nu’

**Gebruikersdoel:** Als producteigenaar begrijp ik direct waarom ik voor de gekozen Product Factory-scope geen cyclus kan starten en welke veilige, read-only vervolgstap ik kan nemen, zonder een langlopende cyclus ten onrechte als oorzaak te zien.

### Flow
1. De eigenaar selecteert een product; de productnaam blijft zichtbaar als actieve scope.
2. Het dashboard berekent de startbeschikbaarheid met exact de bestaande voorwaarden: productstatus is ‘active’ en workspaceOwnership is ‘product-factory’.
3. Bij geldige voorwaarden is ‘Start productcyclus nu’ actief en staat er geen blokkademelding.
4. Bij een falende of onbekende voorwaarde blijft de knop uitgeschakeld en verschijnt direct eronder een programmatisch gekoppelde melding met reden en veilige vervolgstap.
5. Reden ‘Product niet actief’: toon ‘Starten is niet beschikbaar omdat dit product niet actief is.’ met de read-only link ‘Bekijk productdetails’.
6. Reden ‘Andere workspace-eigenaar’: toon ‘Starten is niet beschikbaar omdat deze workspace niet door Product Factory wordt beheerd.’ met de read-only link ‘Bekijk productdetails’.
7. Reden ‘Gegevens ontbreken’: toon ‘Startbeschikbaarheid kan niet betrouwbaar worden vastgesteld.’ met de read-only actie ‘Vernieuw status’ en eventueel ‘Bekijk productdetails’.
8. Bij meerdere falende voorwaarden wordt één primaire reden getoond in vaste prioriteit: ontbrekende gegevens, product niet actief, afwijkend workspaceOwnership. Een compacte tekst ‘Nog 1 voorwaarde niet voldaan’ maakt aanvullende context uitklapbaar.
9. Een zichtbare RUNNING-cyclus wordt niet als blokkadereden genoemd, tenzij een toekomstig startcontract dit expliciet als startvoorwaarde levert.
10. De eigenaar kan via de link product- of cyclusdetails read-only bekijken en terugkeren; deze MVP voegt geen annulering, retry of statuscorrectie toe.

### Wireframe

PRODUCT FACTORY

Product
[ Product Factory                         ▾ ]

Cyclus starten
Start een nieuwe onderzoeks- en besliscyclus voor dit product.

[ Start productcyclus nu — uitgeschakeld ]
ⓘ Starten is niet beschikbaar omdat deze workspace niet door Product Factory wordt beheerd.
[ Bekijk productdetails → ]

Actieve cyclus
RUNNING · Onderzoeker
Gestart: …  |  Looptijd: …
[ Bekijk cyclusdetails → ]

De actieve cyclus staat visueel los van de beschikbaarheidsmelding. Technische diagnostiek blijft in het detail. In de actieve toestand vervalt de melding en wordt de knop bedienbaar: [ Start productcyclus nu ].

### Interactiehypotheses
- H1 — Voor elk synthetisch product waarvoor de startactie uitgeschakeld is, bevat de gerenderde UI precies één niet-lege primaire reden die overeenkomt met de falende bestaande voorwaarde. Automatiseerbaar met componenttests voor inactief product, afwijkend workspaceOwnership en ontbrekende metadata.
- H2 — De wijziging verandert de startbeslissing niet: voor alle combinaties van productstatus en workspaceOwnership is de enabled/disabled-uitkomst vóór en na de presentatieaanpassing identiek. Automatiseerbaar met parametrische regressietests.
- H3 — Een geldig actief product met workspaceOwnership ‘product-factory’ toont een actieve startknop en geen blokkademelding. Automatiseerbaar met een widgettest en semantische-tree-asserties.
- H4 — Een langlopende RUNNING-cyclus beïnvloedt tekst en beschikbaarheid niet wanneer de twee bestaande startvoorwaarden geldig zijn. Automatiseerbaar door dezelfde productfixture met en zonder RUNNING-cyclus te vergelijken.
- H5 — Ontbrekende of onbekende waarden leveren de eerlijke melding ‘Startbeschikbaarheid kan niet betrouwbaar worden vastgesteld’ en nooit een afgeleide claim over een RUNNING-cyclus. Automatiseerbaar met null-, lege- en onbekende-waardefixtures.
- H6 — Bij meerdere falende voorwaarden kiest het model deterministisch de vastgelegde primaire reden en vermeldt het aantal aanvullende oorzaken. Automatiseerbaar met tabelgedreven unit-tests voor alle combinaties en volgordes van invoerdata.

### Toegankelijkheid
- Koppel de reden programmatisch aan de knop via de toepasselijke beschrijvingsrelatie, zodat een schermlezer bij focus zowel actienaam, onbeschikbaarheid als reden aankondigt.
- Zorg dat reden en vervolgstap in logische DOM- en focusvolgorde direct na de actie staan; de read-only link is volledig met toetsenbord bedienbaar en heeft een zichtbare focusindicator.
- Communiceer beschikbaarheid nooit uitsluitend met kleur, opacity of nabijheid; gebruik expliciete tekst en een semantische status.
- Laat disabled tekst, melding, links en focusindicatoren voldoen aan WCAG 2.2 AA-contrast: minimaal 4,5:1 voor normale tekst en 3:1 voor grote tekst en relevante UI-componenten.
- Gebruik geen tooltip als enige drager van de reden, omdat die minder betrouwbaar beschikbaar is voor toetsenbord- en schermlezergebruik.
- Automatische tests controleren toetsenbordvolgorde, toegankelijke naam en beschrijving, semantische disabled-state, aanwezigheid van reden per blokkadefixture en contrasttokens.
- De uitklapbare aanvullende context gebruikt een echte button met aria-expanded-equivalent en blijft optioneel; de primaire reden is zonder uitklappen beschikbaar.

### Privacy
- Gebruik uitsluitend operationele metadata van Product Factory zelf: productstatus, workspaceOwnership, beschikbaarheidsuitkomst en eventueel cyclusstatus.
- Toon, log of verzend geen persoonsgegevens en geen gebruikers- of inhoudsdata uit andere producten.
- Productdetails en cyclusdetails blijven gefilterd op de actieve Product Factory-scope en zijn read-only binnen deze MVP.
- Voeg voor de uitleg geen nieuwe analytics-events met identifiers, vrije tekst of cross-productgegevens toe; indien operationele meting noodzakelijk is, beperk die tot geaggregeerde reden-codes zonder gebruikersidentificatie.
- Meldingen gebruiken vaste eigenaarsteksten en tonen geen ruwe backendpayloads, tokens, paden of interne foutdetails.
- Automatische privacytests verifiëren dat het beschikbaarheidsmodel alleen toegestane velden consumeert en dat gerenderde meldingen geen metadata van andere productfixtures bevatten.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is klein, read-only, privacybegrensd en volledig agent-uitvoerbaar en automatiseerbaar. Hij behoudt de bestaande startvoorwaarden, voorkomt een onbewezen koppeling met een RUNNING-cyclus en overlapt niet exact met gepubliceerd werk. Er zijn geen blokkerende problemen.
- **WARNING · ACCESSIBILITY** — De acceptatiecriteria toetsen semantische koppeling, toetsenbordbediening en kleur-onafhankelijke communicatie, maar noemen geen expliciete geautomatiseerde contrastcontrole voor de nieuwe melding, link en focusindicator. Borg bij uitvoering WCAG 2.2 AA-contrast met bestaande gevalideerde tokens of een geautomatiseerde token-/componenttest; dit vereist geen handmatige controle.
- **WARNING · CONSISTENCY** — De acceptatiecriteria lijken een bestaande read-only productdetailbestemming te vereisen, terwijl het risico erkent dat deze mogelijk niet voor elke toestand bestaat en dan moet worden weggelaten. Maak bij uitvoering eenduidig dat alleen aantoonbaar bestaande, scope-behoudende bestemmingen worden getoond en dat afwezigheid ervan geen nieuwe route of muterende actie rechtvaardigt.
- **INFO · RIGHTS** — Voor de repository en acceptatie-UI is geen duidelijke hergebruikslicentie vastgesteld. De kandidaat gebruikt deze bronnen alleen als feitelijke onderbouwing en vraagt niet om overname van beschermde tekst of code; dit belemmert levering niet.
- **INFO · SCOPE** — De kandidaat raakt story:78, maar dupliceert die niet: story:78 introduceerde de actieve productscope en behield het startgedrag, terwijl deze kandidaat uitsluitend de verklaring van de bestaande disabled-state toevoegt.

## Geaccepteerde storykandidaten

### Toon waarom ‘Start productcyclus nu’ niet beschikbaar is

_Sleutel: `verklaar-startblokkade`_

Maak de bestaande startactie binnen de actieve productscope zelfverklarend zonder de startvoorwaarden of het startgedrag te wijzigen. Leid vanuit exact dezelfde beschikbaarheidsberekening één deterministische primaire reden af en toon die direct bij de uitgeschakelde knop in eigenaarstaal. Gebruik de vaste prioriteit: ontbrekende of onbekende metadata, product niet actief, workspace niet door Product Factory beheerd. Bied uitsluitend een bestaande read-only detailbestemming als vervolgstap; bij ontbrekende gegevens mag daarnaast de bestaande statusverversing worden gebruikt. Een zichtbare RUNNING-cyclus, de looptijd daarvan en andere niet-gecontroleerde gegevens worden nooit als oorzaak genoemd. Voeg geen herstelacties, nieuwe API’s, opslag, telemetrie of wijzigingen aan cyclus- en Software Factory-processen toe.

**Acceptatiecriteria**
- Een gedeeld beschikbaarheidsmodel gebruikt uitsluitend de bestaande voorwaarden `Product.status == active` en `workspaceOwnership == product-factory` voor zowel de enabled/disabled-state als de uitleg; een tabelgedreven regressietest bewijst voor alle geldige, ongeldige, ontbrekende en onbekende waardecombinaties dat de startbeslissing ongewijzigd blijft.
- Bij een actief product met workspaceOwnership `product-factory` is de startknop actief en ontbreekt de blokkademelding; bij iedere uitgeschakelde toestand staat direct bij de knop exact één niet-lege primaire reden in eigenaarstaal.
- De primaire reden volgt deterministisch deze prioriteit: ontbrekende of onbekende metadata toont `Startbeschikbaarheid kan niet betrouwbaar worden vastgesteld.`, een niet-actief product toont `Starten is niet beschikbaar omdat dit product niet actief is.`, en afwijkend workspaceOwnership toont `Starten is niet beschikbaar omdat deze workspace niet door Product Factory wordt beheerd.`; bij meerdere oorzaken vermeldt compacte aanvullende context het aantal overige onvervulde voorwaarden zonder de primaire reden te vervangen.
- De blokkademelding biedt alleen een bestaande, productscope-behoudende read-only bestemming naar productdetails; uitsluitend bij ontbrekende of onbekende metadata mag ook de bestaande statusverversing worden aangeboden. Er worden geen annuleer-, retry-, statuscorrectie- of andere nieuwe muterende acties toegevoegd.
- Geautomatiseerde tests vergelijken dezelfde geldige productfixture met en zonder een langlopende RUNNING-cyclus en bewijzen dat knopstatus en blokkadetekst identiek blijven en nooit looptijd, stilstand of de RUNNING-cyclus als oorzaak noemen.
- Widget- en semantische tests bewijzen dat de disabled-state en reden programmatisch aan de startactie zijn gekoppeld, de primaire reden zonder uitklappen beschikbaar is, de read-only vervolgstap per toetsenbord bereikbaar is en beschikbaarheid niet uitsluitend door kleur of visuele nabijheid wordt gecommuniceerd.
- Geautomatiseerde tests bewijzen dat het model alleen productstatus en workspaceOwnership consumeert, dat meldingen vaste teksten gebruiken en dat geen gegevens, ruwe backendwaarden of identifiers van andere productfixtures worden gerenderd.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/product_scope.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/product_scope.dart), [https://design-system.service.gov.uk/components/button/](https://design-system.service.gov.uk/components/button/)

Afhankelijkheden: story:78 (herkend als bestaande stories: 78)

Risico's: Wanneer uitleg en knopbeschikbaarheid later afzonderlijk worden aangepast, kunnen ze uiteenlopen; één gedeeld beschikbaarheidsmodel en contracttests moeten dit voorkomen., Een productdetailbestemming of statusverversing kan in de actuele frontend niet voor iedere toestand bestaan; in dat geval moet de implementatie de niet-beschikbare vervolgstap weglaten en mag zij geen nieuwe muterende route introduceren., Technische waarden kunnen buiten de bekende verzameling vallen; deze moeten conservatief onder de onbekende toestand vallen en mogen niet als een specifieke oorzaak worden gepresenteerd.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
