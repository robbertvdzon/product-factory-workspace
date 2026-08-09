---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0009
date: 2026-08-09
status: approved
sources:
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md
  - https://github.com/robbertvdzon/product-factory
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-9-Voeg-expliciete-resolve-stap-toe-bij-batchpublicatie-die.md
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-7-Verifieer-of-dependsOn-verwijzingen-binnen-een-story-batch.md
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/SF-2036-Start-en-eindtijd-bij-productcycli.md
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-4-Voeg-toegankelijk-inline-uitklappaneel-met-scope-disclaimer-toe.md
  - https://github.com/robbertvdzon/product-factory/commit/3b446d25be16cadfcf8f47566e4e7878ddce5ff3.diff
  - https://github.com/robbertvdzon/product-factory/commit/c6c2b706b4b7dd05f0ffbb86f0590a5fa8ad080d.diff
  - https://product-factory-acceptance.vdzonsoftware.nl
  - https://docs.github.com/actions/managing-workflow-runs/using-the-visualization-graph
  - https://www.smashingmagazine.com/2022/08/error-messages-ux-design/
---
# Productcyclus 9

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Onderzoek gebaseerd op de publieke repository robbertvdzon/product-factory (README, /docs, broncode, commitgeschiedenis) op 2026-08-09. De acceptatieomgeving (https://product-factory-acceptance.vdzonsoftware.nl) was ondanks meerdere pogingen (met/zonder trailing slash, http/https, /dashboard-pad, /api/products-pad) niet bereikbaar via de webtool — telkens HTTP 403 Forbidden, vermoedelijk botbescherming die de gebruikte webtool blokkeert. Dit is expliciet als hiaat opgenomen; er zijn géén bevindingen over de draaiende UI gefabriceerd op basis van aannames. In plaats daarvan is de huidige staat vastgesteld via de eigen broncode (met name het enkele Flutter-bestand dashboard-frontend/lib/main.dart) en via recent samengevoegde story-documentatie in docs/stories, die zelf al expliciete "known limitations" beschrijft. De laatste 24 uur (2026-08-08/09) laten zeer actieve ontwikkeling zien: classificatiebadges, uitklapbaar disclaimerpaneel, vergrendelde conclusiewaarde, statische documentatie, en een driedelige dependsOn-oplossing (verifiëren → stabiele sleutel → resolve-stap bij publicatie, stories product-factory-7/8/9) — precies het traject dat critics in eerdere iteraties signaleerden. Vandaag is daarnaast een cyclus-annuleren-functie opgeleverd en is een optioneel adminUrl-veld geïntroduceerd (tot nu toe alleen ingevuld voor hkh-autopilot, niet voor product-factory zelf, dus er is voor dit product geen apart beheergedeelte om te bezoeken). De belangrijkste nog onbeantwoorde productvraag: de zojuist opgeleverde dependsOn/batch-koppeling en resolve-logica hebben geen eigen, voor de eigenaar begrijpelijke plek in het dashboard — de mapping wordt alleen weggeschreven als ruwe JSON-artifact in het dossier, niet als leesbare badge of foutmelding in de story-queue, wat op gespannen voet staat met het principe "bruikbaar voor de eigenaar, niet voor de AI".

### Acceptatieomgeving niet bereikbaar via webtool (403 Forbidden)

Meerdere pogingen om https://product-factory-acceptance.vdzonsoftware.nl te raadplegen (root, met trailing slash, http-variant, /dashboard-pad en /api/products-pad) leverden consequent HTTP 403 Forbidden op. Er kon dus geen eigen visuele inspectie van de draaiende UI (inclusief een eventueel beheergedeelte) worden uitgevoerd in deze sessie. Dit is een reëel hiaat in het onderzoek en geen aanname; de huidige-staatanalyse steunt daarom vervangend op de eigen broncode en documentatie in de repository.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### Doel en werking van Product Factory volgens eigen README/docs

Product Factory is een autonome Kotlin-applicatie (Spring Modulith, PostgreSQL/Flyway, Flutter-dashboard) die voor geregistreerde producten onderzoek doet, productkeuzes maakt, UX ontwerpt en storykandidaten aanbiedt aan een aparte Software Factory, die de uitvoering doet; resultaten worden in de volgende cyclus verwerkt. Sinds recente commits (feat(product): support multiple isolated products, 2026-08-07) beheert het meerdere geïsoleerde producten via een projects.yaml-configuratie, waaronder zichzelf (product-factory) en hkh-autopilot.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md), [https://github.com/robbertvdzon/product-factory](https://github.com/robbertvdzon/product-factory)

### Dashboard-UI is één monolithisch Flutter-bestand met vaste secties, geen zoek/filterfunctie

dashboard-frontend/lib/main.dart (59 KB) bevat de volledige dashboard-UI: metric-tegels, productenlijst, productcycli/onderzoekssessies, Software Factory-stories, benodigde toegangstokens, storyqueue (Error/Bezig/Wachtend/Klaar) en workspace-publicaties. Alle secties tonen standaard 5 items met een 'Meer (N resterend)'-knop; er is geen zoek- of filterfunctionaliteit, alle data wordt volledig gelijst of voorgesorteerd door de backend aangeleverd.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart)

### Classificatiebadge toont alleen het verdict, onderbouwing zit verstopt in ruwe JSON-dossierartefacten

In de lijstweergave toont de classificatiebadge van een cyclus alleen het eindverdict (bijv. 'direction-chosen', 'guardrail-conflict'). De onderliggende onderbouwing (voortgang per agentstap, kritiekverdict, geaccepteerde stories) is alleen te vinden door de cyclus aan te klikken, het 'Volledig productdossier' uit te klappen en losse artifact-kaarten met ruwe JSON-inhoud te doorzoeken. Dit is deels een bewuste keuze (een klein, keyboard-toegankelijk disclaimerpaneel bij de badge zegt expliciet 'dit toont wat de uitkomst was, niet waarom', zie story product-factory-4), maar betekent dat de daadwerkelijke waarom-vraag alleen met JSON-leesvaardigheid te beantwoorden is.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-4-Voeg-toegankelijk-inline-uitklappaneel-met-scope-disclaimer-toe.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-4-Voeg-toegankelijk-inline-uitklappaneel-met-scope-disclaimer-toe.md)

### Nieuw dependsOn-resolutiemechanisme heeft geen zichtbare plek in het dashboard

Story product-factory-9 (samengevoegd 2026-08-09) voegt een resolve-stap toe die dependsOn-sleutels bij batchpublicatie vertaalt naar definitieve backlog-ID's, met selectieve blokkade per kandidaat bij een onoplosbare verwijzing. De volledige sleutel-naar-ID-mapping (incl. geblokkeerde kandidaten) wordt duurzaam weggeschreven als nieuw artifacttype 'dependson_resolution' in de shadow_iteration_artifact-tabel en is 'zichtbaar in het dossier', maar de storytekst bevat expliciet geen eis voor een aparte, herkenbare dashboardweergave van deze mapping of van blokkeerredenen. De code-analyse van main.dart bevestigt dat storykandidaten in de queue alleen titel, productslug, externe sleutel, fase en foutmelding tonen — geen dependency- of batchweergave.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-9-Voeg-expliciete-resolve-stap-toe-bij-batchpublicatie-die.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-9-Voeg-expliciete-resolve-stap-toe-bij-batchpublicatie-die.md), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart)

### Eerdere critic-bevinding: beloofd batch-review-dashboard met badges/preview-modal is nooit gebouwd

In iteratie 7 signaleerden twee onafhankelijke critic-reviews (opgenomen in de eigen projectgeschiedenis) dat een eerder onderzoeksartefact een volledig 'Story-batch Review Dashboard' beschreef (sleutel-badges, statusindicatoren, toegankelijke resolve-preview-modal met ARIA/focus-management), terwijl geen van de drie daadwerkelijk gekozen kandidaten (product-factory-7/8/9) die UI implementeerde — bewust beperkt tot backend/datamodel. Deze discrepantie tussen visie en opgeleverde functionaliteit is dus al eerder binnen het project zelf vastgesteld en nog niet opgevolgd.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-7-Verifieer-of-dependsOn-verwijzingen-binnen-een-story-batch.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-7-Verifieer-of-dependsOn-verwijzingen-binnen-een-story-batch.md), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-9-Voeg-expliciete-resolve-stap-toe-bij-batchpublicatie-die.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-9-Voeg-expliciete-resolve-stap-toe-bij-batchpublicatie-die.md)

### Zelf-gedocumenteerde bekende beperkingen uit story SF-2036 (tijdweergave bij cycli)

De story die start-/eindtijd aan productcycli toevoegde documenteert zelf drie onopgeloste beperkingen: (1) een SDK-versiemismatch tussen pubspec.yaml (Dart ^3.9.0) en pubspec.lock (>=3.10.0-0) is niet opgelost; (2) workspace-publicaties hebben geen bruikbaar tijdstempel en blijven dus ongesorteerd, ze krijgen alleen paginering; (3) er is geen browser-E2E-dekking omdat de omgeving geen screenshot-mogelijkheid of gehoste previews heeft, waardoor sectie-koppeling alleen via codereview is geverifieerd, niet functioneel getest.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/SF-2036-Start-en-eindtijd-bij-productcycli.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/SF-2036-Start-en-eindtijd-bij-productcycli.md)

### Cyclus-annuleren net opgeleverd (2026-08-09), adminUrl-veld nog niet ingevuld voor product-factory zelf

Op 2026-08-09 zijn kort na elkaar een backend-endpoint (POST /api/shadow-iterations/{id}/cancel) en een frontend-knop voor het annuleren van een vastgelopen cyclus opgeleverd, met bevestigingsdialoog, laadstatus en snackbar-feedback. Dezelfde dag is een optioneel adminUrl-veld aan de productconfiguratie toegevoegd, maar in projects.yaml is dat tot nu toe alleen ingevuld voor hkh-autopilot (https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/); voor product-factory zelf staat geen adminUrl geconfigureerd, dus er is voor dit product geen apart beheergedeelte te bezoeken naast de acceptatieomgeving.

Bronnen: [https://github.com/robbertvdzon/product-factory/commit/3b446d25be16cadfcf8f47566e4e7878ddce5ff3.diff](https://github.com/robbertvdzon/product-factory/commit/3b446d25be16cadfcf8f47566e4e7878ddce5ff3.diff), [https://github.com/robbertvdzon/product-factory/commit/c6c2b706b4b7dd05f0ffbb86f0590a5fa8ad080d.diff](https://github.com/robbertvdzon/product-factory/commit/c6c2b706b4b7dd05f0ffbb86f0590a5fa8ad080d.diff)

### Huidige applicatie

**Doel:** Product Factory is de eigen autonome motor die haar toepassing op zichzelf richt: hetzelfde onderzoeks-, keuze-, ontwerp- en storylevering-mechanisme dat voor producten als hkh-autopilot wordt gebruikt, wordt nu ook gebruikt om het eigen dashboard, de orchestratielogica en werking van Product Factory zelf continu te toetsen en te verbeteren. De primaire gebruiker is de producteigenaar/beheerder (robbertvdzon) die via het Flutter-dashboard cycli, storykandidaten, kritiekverdicten en leveringen aan de Software Factory volgt en bijstuurt.

**Wat ontbreekt:**
- De draaiende acceptatieomgeving (https://product-factory-acceptance.vdzonsoftware.nl) was in deze sessie niet bereikbaar (HTTP 403 bij elke poging), waardoor geen eigen visuele/interactieve inspectie van het dashboard of een eventueel beheergedeelte kon plaatsvinden; de analyse steunt daarom op broncode en documentatie in plaats van live-observatie.
- Het net opgeleverde dependsOn-resolutiemechanisme (product-factory-9) heeft geen eigen, herkenbare weergave in het dashboard: de sleutel-naar-ID-mapping en blokkeerredenen zitten alleen in ruwe JSON-dossierartefacten, niet in de storyqueue-lijst zelf.
- De classificatiebadge van een cyclus toont het eindverdict, maar de onderbouwing is alleen bereikbaar door handmatig door geneste JSON-artifact-kaarten in een dialoogvenster te bladeren.
- Er is geen zoek- of filterfunctie in het dashboard; naarmate cycli, storykandidaten en publicaties toenemen kan dit de behapbaarheid van de overzichtspagina onder druk zetten.
- Workspace-publicaties hebben geen sorteerbaar tijdstempel (zelf gedocumenteerd in story SF-2036) en blijven daardoor ongesorteerd.
- adminUrl is een nieuw, optioneel productveld maar staat voor product-factory zelf nog niet ingevuld, terwijl de onderzoeksopdracht expliciet vraagt het beheergedeelte te bezoeken 'als dat er is'.

### Verbetermogelijkheden

- Voeg in de storyqueue-lijst een compacte, leesbare indicatie toe wanneer een storykandidaat door een dependsOn-resolutieprobleem is geblokkeerd (bijv. 'geblokkeerd: verwijzing naar onbekende sleutel X'), in plaats van dit alleen als ruwe JSON in het dossier te loggen — sluit aan bij algemene UX-richtlijnen om foutmeldingen specifiek en direct bij het betreffende item te tonen in plaats van generiek of verborgen.
- Overweeg een minimale, alleen-lezen visualisatie van dependsOn-relaties tussen kandidaten binnen één batch (bijv. een eenvoudige lijst 'hangt af van: <sleutel>' per kaart), naar analogie van hoe GitHub Actions taakafhankelijkheden ('needs') zichtbaar maakt in de workflow-run-view, zodat de eigenaar kan zien welke kandidaten aan elkaar gekoppeld zijn zonder het ruwe dossier te hoeven lezen.
- Verhelder in de UI zelf (niet alleen in documentatie) dat er voor het huidige product geen apart beheergedeelte is geconfigureerd, zodat toekomstige onderzoeksagenten en de eigenaar niet onnodig naar een niet-bestaande adminUrl zoeken.
- Los de zelf-gedocumenteerde SDK-versiemismatch (pubspec.yaml vs. pubspec.lock) op, en voeg een sorteerbaar tijdstempel toe aan workspace-publicaties zodat deze net als andere lijsten chronologisch te doorlopen zijn.
- Overweeg lichte browser-E2E-dekking (bijv. screenshot- of gehoste previewcontrole) toe te voegen, omdat het ontbreken daarvan nu al twee keer zelf als beperking is gedocumenteerd (SF-2036) en sectiekoppeling alleen via codereview wordt geverifieerd.

### Inspiratiebronnen

- [GitHub Actions workflow visualisatiegraaf (needs-afhankelijkheden)](https://docs.github.com/actions/managing-workflow-runs/using-the-visualization-graph) — Toont hoe een gevestigd systeem taakafhankelijkheden (needs) visueel en statusgebonden weergeeft binnen een enkele run — direct herbruikbaar patroon voor het zichtbaar maken van dependsOn-relaties tussen storykandidaten in een batch, wat nu ontbreekt in het Product Factory-dashboard.
- [Smashing Magazine — Designing Better Error Messages UX](https://www.smashingmagazine.com/2022/08/error-messages-ux-design/) — Algemeen geaccepteerde richtlijnen voor specifieke, contextuele foutmeldingen in plaats van generieke labels; relevant voor het herontwerpen van hoe geblokkeerde storykandidaten (door dependsOn-fouten) hun reden tonen.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md) | 2026-08-09 | Publiek toegankelijk op GitHub; licentie van de repository niet expliciet gecontroleerd, aangenomen eigen projectbron van de opdrachtgever (robbertvdzon/product-factory), geraadpleegd puur als documentatiebron, niet hergepubliceerd | Officiële projectbeschrijving en architectuuroverzicht direct van de bronrepository, nodig om het doel en de doelgroep van de applicatie vast te stellen |
| [bron](https://github.com/robbertvdzon/product-factory) | 2026-08-09 | Publieke GitHub-repository, eigendom van de opdrachtgever/producteigenaar; alleen gelezen, geen wijzigingen aangebracht | Uitgangspunt om bestandsstructuur, modules en algemene opzet van het systeem te verifiëren |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart) | 2026-08-09 | Publiek toegankelijke broncode uit dezelfde repository; puur ter analyse geraadpleegd | Enige manier om de daadwerkelijke UI-structuur, secties en gedrag van het dashboard vast te stellen nu de draaiende acceptatieomgeving niet bereikbaar was |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-9-Voeg-expliciete-resolve-stap-toe-bij-batchpublicatie-die.md) | 2026-08-09 | Publieke projectdocumentatie in dezelfde repository | Bevat de exacte acceptatiecriteria en opslaglocatie van het nieuwe dependsOn-resolutiemechanisme, essentieel om te bepalen of dit al zichtbaar is voor de eigenaar |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-7-Verifieer-of-dependsOn-verwijzingen-binnen-een-story-batch.md) | 2026-08-09 | Publieke projectdocumentatie in dezelfde repository | Bevestigt de eerdere critic-bevinding over het ontbreken van UI voor het beloofde batch-review-dashboard |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/SF-2036-Start-en-eindtijd-bij-productcycli.md) | 2026-08-09 | Publieke projectdocumentatie in dezelfde repository | Bevat door het project zelf gedocumenteerde bekende beperkingen (SDK-mismatch, ontbrekende sortering, geen E2E-dekking) |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-4-Voeg-toegankelijk-inline-uitklappaneel-met-scope-disclaimer-toe.md) | 2026-08-09 | Publieke projectdocumentatie in dezelfde repository | Verklaart het bewuste ontwerp achter de badge-disclaimer, nodig om de badge/onderbouwing-bevinding correct te interpreteren |
| [bron](https://github.com/robbertvdzon/product-factory/commit/3b446d25be16cadfcf8f47566e4e7878ddce5ff3.diff) | 2026-08-09 | Publieke commit-diff op GitHub binnen dezelfde repository | Toont de daadwerkelijke, zeer recente implementatie van de cyclus-annuleren-functie in frontend en backend-proxy |
| [bron](https://github.com/robbertvdzon/product-factory/commit/c6c2b706b4b7dd05f0ffbb86f0590a5fa8ad080d.diff) | 2026-08-09 | Publieke commit-diff op GitHub binnen dezelfde repository | Bevestigt dat adminUrl vooralsnog alleen voor hkh-autopilot is geconfigureerd en niet voor product-factory zelf |
| [bron](https://product-factory-acceptance.vdzonsoftware.nl) | 2026-08-09 | Publiek bedoelde acceptatieomgeving zonder login, met nepdata; toegang werd echter geweigerd (403) aan de gebruikte webtool | Verplichte stap volgens de onderzoeksopdracht om de huidige staat van de draaiende applicatie te beoordelen; opgenomen als bron ondanks mislukte toegang om het hiaat transparant te documenteren |
| [bron](https://docs.github.com/actions/managing-workflow-runs/using-the-visualization-graph) | 2026-08-09 | Publieke GitHub-productdocumentatie, © GitHub, vrij raadpleegbaar | Vergelijkbaar precedent voor het visueel tonen van taakafhankelijkheden ('needs') in een workflow-run, relevant als inspiratie voor het zichtbaar maken van dependsOn-relaties tussen storykandidaten |
| [bron](https://www.smashingmagazine.com/2022/08/error-messages-ux-design/) | 2026-08-09 | Publiek toegankelijk redactioneel artikel, © Smashing Magazine, vrij raadpleegbaar als achtergrondbron | Algemeen erkende UX-richtlijnen voor het tonen van specifieke, contextuele foutmeldingen in plaats van generieke labels — relevant voor de bevinding over de dependsOn-blokkademelding |

## Productbeslissing

Richt de volgende cyclus op één kleine, samenhangende verbetering: maak de blokkeerreden van het net opgeleverde dependsOn-resolutiemechanisme (story product-factory-9) zichtbaar op de storykandidaat-kaarten in de dashboard-queue, in plaats van dat deze alleen als ruwe JSON in het productdossier terug te vinden is. De onderliggende data (sleutel-naar-ID-mapping, blokkeerreden per kandidaat) wordt al duurzaam opgeslagen als dependson_resolution-artefact; dit voorstel voegt uitsluitend een alleen-lezen, tekstuele weergave toe aan de bestaande kaartcomponent in main.dart (bijv. 'geblokkeerd: verwijzing naar onbekende sleutel X'). Er wordt geen resolve-logica, backend-berekening of grafische afhankelijkheidsvisualisatie toegevoegd — dat blijft bewust buiten scope voor een latere, apart te beoordelen stap.

**Waarom:** Het onderzoek laat zien dat Product Factory net (2026-08-09) een driedelig dependsOn-resolutiemechanisme heeft opgeleverd, maar dat de uitkomst daarvan — welke storykandidaat geblokkeerd is en waarom — alleen als ruwe JSON in het dossier zichtbaar is, niet in de storyqueue zelf waar de eigenaar normaal kijkt. Dit is precies het patroon dat critics in een eerdere iteratie al signaleerden (een beloofd batch-review-dashboard dat nooit werd gebouwd) en raakt direct het productprincipe 'bruikbaar voor de eigenaar, niet voor de AI': een technisch correcte functionaliteit die alleen met JSON-leesvaardigheid te doorgronden is, is niet af volgens de eigen productvisie. Door de wijziging te beperken tot het alleen-lezen tonen van al bestaande data, blijft de stap klein, toetsbaar en terugdraaibaar (principe 'klein en toetsbaar'), raakt ze geen data-migraties, authenticatie of de koppeling met de Software Factory (guardrail), en is uit te leggen waarom het huidige gedrag zo ontstond: de stories 7/8/9 kozen bewust voor backend/datamodel-scope, wat de UI-kloof verklaart in plaats van verdoezelt.

### Prioriteiten
- Toon de blokkeerreden van het dependsOn-resolutiemechanisme direct op de storykandidaat-kaart, afkomstig uit de al bestaande dependson_resolution-artefactdata.
- Houd de wijziging read-only en losstaand van de resolve-logica zelf, zodat ze in isolatie te beoordelen en terug te draaien is.
- Gebruik een specifieke, contextuele meldingstekst per geblokkeerde kaart in plaats van een generiek label of alleen dossierdocumentatie.
- Neem in deze richting geen volledige afhankelijkheidsgraaf, zoekfunctie, SDK-mismatch-fix of publicatiesortering mee — apart agenderen.
- Documenteer het onbereikbare acceptatieomgeving-hiaat (403) als bekende onderzoeksbeperking zonder de besluitvorming erop te laten wachten.

### Besluiten
- **Kies als enige, samenhangende richting voor de volgende cyclus: maak de blokkeerreden van het net opgeleverde dependsOn-resolutiemechanisme (product-factory-9) zichtbaar op de storykandidaat-kaarten in de storyqueue, in plaats van alleen als ruwe JSON in het dossier.** — Dit verbindt een concrete, recent geleverde functionaliteit (resolve-stap bij batchpublicatie) met een al eerder door critics gesignaleerd gat (ontbrekend batch-review-dashboard, iteratie 7) en met het productprincipe 'bruikbaar voor de eigenaar, niet voor de AI': de mapping bestaat al, maar is nu alleen leesbaar voor wie JSON kan doorzoeken.
- **Beperk de scope expliciet tot alleen-lezen weergave van bestaande dependson_resolution-artefactdata (sleutel-naar-ID-mapping en blokkeerreden) op de kaart; geen wijziging aan de resolve-logica, geen nieuwe backend-berekeningen, geen grafische afhankelijkheidsvisualisatie.** — Sluit aan bij 'klein en toetsbaar' en 'onomkeerbaarheid is een zwaarder gewicht dan gemak': de data wordt al duurzaam weggeschreven, dus dit is een pure presentatiewijziging die in isolatie te beoordelen en terug te draaien is, zonder de koppeling met de Software Factory of de resolutielogica zelf te raken.
- **Gebruik het patroon van specifieke, contextuele foutmeldingen (bijv. 'geblokkeerd: verwijzing naar onbekende sleutel X') direct bij het betreffende storykandidaat-item, in plaats van een generiek label of alleen documentatie in het dossier.** — Algemeen erkende UX-richtlijn voor foutmeldingen (specifiek en contextueel in plaats van generiek/verborgen) en analoog aan hoe gevestigde systemen taakafhankelijkheden zichtbaar maken — direct toepasbaar op de al bestaande blokkeerreden-data zonder nieuwe berekening.
- **Laat het 403-toegangshiaat op de acceptatieomgeving expliciet openstaan als onderzoeksbeperking, maar laat dit de besluitvorming niet blokkeren; vertrouw op de consistente broncode- en storydocumentatie als onderbouwing.** — 'Eerst begrijpen, dan wijzigen' vraagt om begrijpen wat er al is, niet om een volledig visuele bevestiging voordat een klein, terugdraaibaar besluit genomen wordt; de code (main.dart) en de eigen storytekst (product-factory-9) zijn onderling consistent over het ontbreken van UI voor de dependency-mapping.

## UX-voorstel: Zichtbare blokkeerreden bij dependsOn-resolutie in de storyqueue

**Gebruikersdoel:** Als producteigenaar wil ik direct op de storykandidaat-kaart in de dashboard-queue zien of en waarom een kandidaat geblokkeerd is door een dependsOn-resolutieprobleem, zonder ruwe JSON-artefacten in het productdossier te hoeven doorzoeken.

### Flow
1. Eigenaar opent het Product Factory-dashboard en navigeert naar de bestaande sectie 'Storyqueue' (Error/Bezig/Wachtend/Klaar).
2. Voor elke getoonde storykandidaat-kaart controleert het dashboard of er een bijbehorend dependson_resolution-artefact met status 'geblokkeerd' bestaat voor de externe sleutel van die kandidaat.
3. Indien geblokkeerd: de kaart toont automatisch, zonder extra klik, een compact tekstueel label met icoon, bv. 'Geblokkeerd: verwijzing naar onbekende sleutel PF-99' — direct onder de bestaande titel/sleutel-regel.
4. Indien niet geblokkeerd: de kaart blijft ongewijzigd zoals in de huidige weergave (geen label).
5. Eigenaar kan met Tab naar de kaart navigeren; de blokkeerreden is onderdeel van de accessible name/description van de kaart, dus een schermlezer leest deze automatisch mee voor.
6. Eigenaar kan optioneel (bestaand gedrag, ongewijzigd) de kaart activeren om het 'Volledig productdossier' te openen voor de onderliggende ruwe artefactdata en meer detail.
7. Er wordt geen nieuwe actie, mutatie of resolve-berekening toegevoegd: de weergave is puur alleen-lezen op basis van al bestaande, duurzaam opgeslagen artefactdata.

### Wireframe

Storyqueue-sectie (bestaande lijst, ongewijzigd qua structuur, met één toegevoegde regel per kaart):

┌───────────────────────────────────────────────────────────┐
│ [Fase-badge: Wachtend]        Storykandidaat-titel          │
│ Product: product-factory      Sleutel: PF-12                │
│ ⚠ Geblokkeerd: hangt af van onbekende sleutel "PF-99"       │
│   (niet gevonden in deze batch)                              │
│ Foutmelding: (bestaand veld, indien aanwezig, ongewijzigd)  │
│ [› Volledig productdossier openen]  (bestaande link)         │
└───────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────┐
│ [Fase-badge: Klaar]           Andere storykandidaat-titel   │
│ Product: product-factory      Sleutel: PF-13                │
│ (geen blokkeerlabel — geen dependson_resolution-blokkade)   │
│ [› Volledig productdossier openen]                            │
└───────────────────────────────────────────────────────────┘

Interactiedetails:
- Het ⚠-label en de tekst vormen samen één semantisch blok binnen de kaart (bv. via een Semantics-wrapper met label "Geblokkeerd: ..."), zodat Tab-navigatie het in één stap voorleest.
- Kleurgebruik: waarschuwingsicoon + tekst in een kleur met minimaal 4.5:1 contrast t.o.v. de kaartachtergrond (geen kleur-only signalering; icoon + tekstlabel "Geblokkeerd:" zijn beide aanwezig).
- Geen nieuwe knoppen, geen nieuwe dialogen; de bestaande 'Volledig productdossier'-link blijft het enige interactiepunt voor verdere diepgang.

### Interactiehypotheses
- H1: Wanneer een storykandidaat een dependson_resolution-artefact heeft met status 'geblokkeerd' voor zijn externe sleutel, toont de kaart in de storyqueue een tekstueel label beginnend met 'Geblokkeerd:' — verifieerbaar met een geautomatiseerde widget-test die dit label detecteert bij een gemockt artefact met status 'geblokkeerd'.
- H2: Wanneer een storykandidaat geen bijbehorend geblokkeerd dependson_resolution-artefact heeft, toont de kaart géén blokkeerlabel — verifieerbaar met een widget-test die de afwezigheid van de tekst 'Geblokkeerd:' controleert bij een kandidaat zonder blokkade-artefact.
- H3: Het blokkeerlabel is onderdeel van de accessible name/description van de kaart en dus bereikbaar via toetsenbordnavigatie zonder muis — verifieerbaar via een geautomatiseerde semantics-/accessibility-test die de Flutter semantics-tree van de kaart inspecteert op aanwezigheid van de blokkeertekst.
- H4: De contrastratio van het waarschuwingsicoon en de labeltekst tegen de kaartachtergrond is minimaal 4.5:1 (WCAG AA) — verifieerbaar met een geautomatiseerde contrastcheck-tool op de gebruikte kleurwaarden in de stylesheet/theme.
- H5: De wijziging introduceert geen extra netwerkverzoek of state-mutatie ten opzichte van de huidige kaartweergave (puur presentatie van reeds opgehaalde artefactdata) — verifieerbaar met een test die het aantal API-calls voor en na de wijziging vergelijkt bij het renderen van dezelfde kaartenlijst.
- H6: Bij meerdere blokkeerredenen voor dezelfde kandidaat toont de kaart alle relevante onbekende sleutels in één samengevoegd label in plaats van de kaart te laten crashen of alleen de eerste te tonen — verifieerbaar met een widget-test die een artefact met meerdere geblokkeerde sleutels mockt en controleert of alle sleutels in de tekst voorkomen.

### Toegankelijkheid
- Blokkeerlabel is te bereiken en voor te lezen via uitsluitend toetsenbordnavigatie (Tab), zonder muisinteractie nodig te hebben.
- Label combineert icoon én tekst (niet uitsluitend kleur of icoon) zodat de betekenis ook zonder kleurperceptie duidelijk is.
- Icoon+tekst voldoen aan minimaal WCAG AA-contrast (≥4.5:1) tegen de kaartachtergrond, ook in eventuele dark-mode variant.
- Blokkeertekst is onderdeel van de accessible name/description van de kaart zodat schermlezers (VoiceOver/TalkBack/NVDA) deze automatisch meelezen bij focus, zonder dat een aparte actie nodig is.
- Geen nieuwe modale dialogen of focus-traps toegevoegd; bestaande focusvolgorde en 'Volledig productdossier'-link blijven ongewijzigd bereikbaar.

### Privacy
- De blokkeerreden bevat uitsluitend operationele metadata van Product Factory zelf (interne story-sleutels zoals 'PF-99', fase, batch-referentie) en geen persoonsgegevens of gebruikersdata van andere producten.
- Er wordt geen nieuwe data verzameld of opgeslagen; de wijziging toont uitsluitend reeds bestaande, duurzaam opgeslagen dependson_resolution-artefactdata read-only.
- Geen koppeling met authenticatie, gebruikersaccounts of persoonsidentificeerbare velden; de sleutel-naar-ID-mapping betreft uitsluitend interne storykandidaten, geen personen.
- Geen wijziging aan toegangsrechten of tokens: de weergave is beperkt tot dezelfde gebruikers die nu al toegang hebben tot de storyqueue en het productdossier.

## Kritische beoordeling

**Oordeel:** ACCEPT

Beide kandidaten (expose-dependson-blocked-reason en render-blocked-reason-storycard) bouwen op een consistente, goed onderbouwde manier voort op de al gepubliceerde dependsOn-resolutiefunctionaliteit (kandidaat 30). Ze zijn klein, alleen-lezen, expliciet terugdraaibaar, agent-uitvoerbaar zonder enig menselijk besluitmoment (geen accountaanmaak, betaling, DNS-wijziging of handmatige test vereist), en bevatten concrete, geautomatiseerd verifieerbare acceptatiecriteria voor zowel backend als toegankelijkheid (contrast, semantics, toetsenbordnavigatie). Privacyoverwegingen zijn correct: uitsluitend eigen operationele metadata, geen persoonsgegevens. Het onderzoek documenteert eerlijk het hiaat dat de acceptatieomgeving niet bereikbaar was (403) en compenseert methodologisch met broncode- en documentatieonderzoek, conform de eigen bronregel. Geen blokkerende problemen gevonden; enkele niet-blokkerende aandachtspunten zijn opgenomen.
- **WARNING · SOURCE** — Kandidaat 0 citeert geen backend/Kotlin-broncodebestand (bv. de controller/repository die de storyqueue-API voedt) om te bevestigen dat blokkeerdata daar nog ontbreekt; alleen main.dart (frontend) en storydocumentatie worden aangehaald. De acceptatiecriteria compenseren dit door de agent zelf eerst te laten verifiëren, wat het risico beperkt maar niet wegneemt.
- **INFO · SOURCE** — De acceptatieomgeving was niet bereikbaar (403) tijdens het onderzoek; dit is transparant gedocumenteerd als hiaat en ondermijnt de besluitvorming niet omdat broncode en storydocumentatie onderling consistent zijn, maar blijft een blinde vlek voor eventuele reeds bestaande UI-elementen die niet uit main.dart blijken.
- **INFO · ACCESSIBILITY** — Kandidaat 1 vereist een geautomatiseerde contrastcheck-tool op bestaande themekleuren; niet bevestigd of zo'n tool al in de repository aanwezig is, dus de implementerende agent moet mogelijk eerst tooling toevoegen of een geschikt alternatief kiezen.
- **INFO · SCOPE** — Kandidaat 1 is functioneel afhankelijk van kandidaat 0 (dependsOn); dit is correct gemodelleerd, maar betekent dat kandidaat 1 alleen zinvol geleverd kan worden als kandidaat 0 in dezelfde of eerdere batch succesvol resolveert.

## Geaccepteerde storykandidaten

### Voeg read-only blokkeerreden-veld toe aan storykandidaat-data op basis van bestaand dependson_resolution-artefact

_Sleutel: `expose-dependson-blocked-reason`_

Bouwt voort op de al opgeleverde resolve-stap (story product-factory-9) die dependsOn-sleutels vertaalt naar backlog-ID's en niet-resolverende verwijzingen als 'geblokkeerd' vastlegt in een dependson_resolution-artefact. Op dit moment is die blokkeerinformatie alleen als ruwe JSON in het productdossier te vinden; het API-pad dat de dashboard-storyqueue van data voorziet, bevat deze informatie (nog) niet aantoonbaar. Deze story voegt een puur alleen-lezen uitbreiding toe aan de bestaande data die de storyqueue voedt: per storykandidaat een computed veld 'blocked' (boolean) en 'blockedReason' (tekst of null), afgeleid via een read-only query/mapping op de al bestaande, duurzaam opgeslagen dependson_resolution-artefactdata. Er wordt geen nieuwe schrijfoperatie, geen wijziging aan de resolve-logica zelf en geen nieuw mutable databaseveld toegevoegd — uitsluitend een leeslaag bovenop bestaande data. De implementerende agent inspecteert eerst geautomatiseerd of deze data al in de bestaande API-response aanwezig is en documenteert die bevinding, zodat de scope aantoonbaar op de werkelijke codebase is gebaseerd in plaats van aangenomen.

**Acceptatiecriteria**
- Agent inspecteert eerst geautomatiseerd de bestaande backend-broncode (het pad dat de dashboard-storyqueue van data voorziet) en documenteert expliciet of blokkeerdata van dependson_resolution-artefacten al in die API-response aanwezig is; deze bevinding wordt vastgelegd in de commit-/PR-beschrijving.
- Indien niet beschikbaar: het bestaande API-response-model voor storykandidaten wordt uitgebreid met twee alleen-lezen velden (blocked: boolean, blockedReason: tekst of null), afgeleid via een read-only query/mapping op de bestaande dependson_resolution-artefactdata; er wordt geen nieuwe mutable kolom, geen wijziging aan de resolve-logica zelf en geen nieuwe schrijfoperatie toegevoegd.
- Bij meerdere onopgeloste dependsOn-sleutels voor dezelfde kandidaat bevat blockedReason alle betreffende onbekende sleutels in één samengevoegde, leesbare tekst (bijv. 'verwijzing naar onbekende sleutels: X, Y'), geverifieerd met een geautomatiseerde test met een geseed artefact dat meerdere geblokkeerde sleutels bevat.
- Voor een storykandidaat zonder bijbehorend geblokkeerd dependson_resolution-artefact retourneert de API blocked: false en blockedReason: null, geverifieerd met een geautomatiseerde test.
- De uitbreiding wijzigt geen bestaande endpoint-URL's of -methoden en breekt geen bestaande consumer; alle bestaande backend-tests voor het/de betreffende endpoint(s) blijven slagen.
- Er wordt minstens één nieuwe geautomatiseerde unit- of integratietest toegevoegd die het nieuwe veld valideert voor zowel de geblokkeerde als de niet-geblokkeerde situatie.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-9-Voeg-expliciete-resolve-stap-toe-bij-batchpublicatie-die.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-9-Voeg-expliciete-resolve-stap-toe-bij-batchpublicatie-die.md), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-7-Verifieer-of-dependsOn-verwijzingen-binnen-een-story-batch.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-7-Verifieer-of-dependsOn-verwijzingen-binnen-een-story-batch.md)

Risico's: Koppeling aan het interne dataformaat van het dependson_resolution-artefact (story product-factory-9) betekent dat een toekomstige wijziging van dat formaat deze mapping kan breken; mitigatie: hergebruik de bestaande artefact-leesfunctie in plaats van het formaat te dupliceren., Als de blokkeerdata via een extra query per kandidaat wordt opgehaald kan dit latency toevoegen bij grote batches; mitigatie: hergebruik het bestaande artefact-ophaalpad en test op representatieve datavolumes., Risico dat interne, ooit als tijdelijk bedoelde kandidaatsleutels nu structureel via de API zichtbaar worden; dit is inhoudelijk gelijk aan wat al in het dossier staat en bevat geen persoonsgegevens, dus het risico is beperkt.

### Toon blokkeerreden van dependsOn-resolutie op storykandidaat-kaart in de dashboard-queue, toegankelijk en met voldoende contrast

_Sleutel: `render-blocked-reason-storycard`_

Maakt gebruik van het in de voorgaande kandidaat (sleutel: expose-dependson-blocked-reason) toegevoegde alleen-lezen blocked/blockedReason-veld om op de bestaande storykandidaat-kaart in de dashboard-storyqueue (main.dart) een compact waarschuwingslabel te tonen wanneer een kandidaat geblokkeerd is door een onopgeloste dependsOn-verwijzing, in plaats van dat de eigenaar dit alleen via ruwe JSON in het productdossier kan achterhalen. De wijziging is uitsluitend presentationeel: geen nieuwe knop, dialoog, route of berekening, direct zichtbaar zonder extra klik, en volledig toetsenbord-/schermlezertoegankelijk conform bestaande WCAG AA-verwachtingen in de app.

**Acceptatiecriteria**
- Wanneer de kaartdata blocked: true en een blockedReason bevat, toont de storykandidaat-kaart direct (zonder extra klik) een label met icoon en tekst beginnend met 'Geblokkeerd:', direct onder de bestaande titel/sleutel-regel; geverifieerd met een geautomatiseerde Flutter widget-test die dit label detecteert bij gemockte kaartdata met blocked: true.
- Wanneer blocked: false of blockedReason ontbreekt, toont de kaart geen blokkeerlabel; geverifieerd met een widget-test die de afwezigheid van de tekst 'Geblokkeerd:' controleert.
- Het label (icoon + tekst) is onderdeel van de accessible name/description van de kaart; geverifieerd met een geautomatiseerde Flutter semantics-test die de semantics-tree van de kaart inspecteert op aanwezigheid van de blokkeertekst wanneer blocked: true.
- De kleurcombinatie van icoon en labeltekst tegen de kaartachtergrond heeft een contrastratio van minimaal 4.5:1 (WCAG AA), geverifieerd met een geautomatiseerde contrastcheck op de gebruikte kleurwaarden in het bestaande theme/stylesheet.
- De wijziging voegt geen nieuw netwerkverzoek toe ten opzichte van de bestaande kaartweergave; het label wordt uitsluitend gerenderd uit reeds opgehaalde kaartdata, geverifieerd met een test die het aantal API-calls voor en na de wijziging vergelijkt bij het renderen van dezelfde kaartenlijst.
- Bestaande elementen van de kaart (fase-badge, titel, sleutel, bestaande foutmelding, link naar 'Volledig productdossier') blijven ongewijzigd aanwezig en functioneel; alle bestaande widget-tests voor de storyqueue-kaart blijven slagen.
- Er wordt geen nieuwe knop, dialoog, route of resolve-berekening toegevoegd; de wijziging is puur presentationeel bovenop het bestaande kaartcomponent.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-9-Voeg-expliciete-resolve-stap-toe-bij-batchpublicatie-die.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/stories/product-factory-9-Voeg-expliciete-resolve-stap-toe-bij-batchpublicatie-die.md), [https://www.smashingmagazine.com/2022/08/error-messages-ux-design/](https://www.smashingmagazine.com/2022/08/error-messages-ux-design/), [https://docs.github.com/actions/managing-workflow-runs/using-the-visualization-graph](https://docs.github.com/actions/managing-workflow-runs/using-the-visualization-graph)

Afhankelijkheden (candidateKey): expose-dependson-blocked-reason (binnen deze batch herkend als: expose-dependson-blocked-reason)

Risico's: Bij meerdere gelijktijdig geblokkeerde kandidaten kan de storyqueue visueel drukker worden; mitigatie: label compact en single-line houden, geen extra iconografie per sleutel., Het samenvoegen van het nieuwe label in de bestaande Semantics-boom van de kaart kan per ongeluk de bestaande accessible name overschrijven in plaats van aanvullen; dit vraagt zorgvuldige integratie en een gerichte semantics-test., Het gekozen waarschuwingsicoon/kleur moet aansluiten bij eventueel al bestaande warning/error-kleurtokens in de app om inconsistente styling te voorkomen; dit moet bij implementatie expliciet geverifieerd worden.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
