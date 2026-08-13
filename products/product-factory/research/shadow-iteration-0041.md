---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0041
date: 2026-08-13
status: approved
sources:
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart
  - https://product-factory-acceptance.vdzonsoftware.nl
  - https://linear.app/docs/default-team-pages
  - https://linear.app/docs/use-cycles
  - https://linear.app/docs/project-overview
  - https://docs.github.com/en/actions/how-tos/monitor-workflows/view-workflow-run-history
---
# Productcyclus 41

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De belangrijkste nog onbeantwoorde productvraag is: welke informatie moet na de gerealiseerde cycluskaarten nog op het hoofdscherm blijven, zodat de eigenaar daar werkelijk alleen een cyclus start, eerdere opbrengsten begrijpt en de voortgekomen stories volgt? De actuele implementatie ondersteunt deze drie taken beter dan voorheen, maar plaatst er nog veel gelijkwaardige operationele secties omheen. Daardoor is epic theme-product-factory-0001 nog niet afgerond. Visuele verificatie in de acceptatieomgeving was niet mogelijk doordat Chromium vóór paginalading afbrak met een lokale Mach-port-permissiefout; conclusies over de huidige visuele hiërarchie zijn daarom gebaseerd op de actuele publieke implementatie en blijven onzeker totdat het gerenderde scherm wel kan worden bekeken. Er is geen productbesluit genomen en er zijn geen stories geschreven.

### Product Factory organiseert een autonome productcyclus voor producteigenaren

De applicatie organiseert per geregistreerd product onderzoek, productkeuze, UX-ontwerp, storyvorming en kritiek. Geaccepteerde kandidaten worden voor autonome producten aan Software Factory geleverd en uitvoeringsresultaten worden in volgende cycli teruggekoppeld. De primaire gebruiker is de producteigenaar die cycli start en uitkomsten, uitvoering, fouten en uitzonderlijke tokenacties bewaakt.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md)

### De cycluskaarten uit iteratie 40 staan inmiddels op main

Het hoofdscherm groepeert geladen kandidaten en leveringen per cyclus in compacte, afzonderlijk uitklapbare kaarten. In gesloten toestand toont een kaart onder meer status, startmoment, kernreden, beslisbron en aantallen; na uitklappen verschijnen gekoppelde titels met afzonderlijke kandidaat- en leveringsstatus. Ambigue of ontbrekende koppelingen worden niet geraden maar eenmaal globaal gemeld.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md)

### De drie eigenaarstaken concurreren nog met veel operationele hoofdschermsecties

Naast de prominente startactie en cycluskaarten rendert hetzelfde scrolloverzicht nog vijf metriekkaarten, productbeheer, een afzonderlijke Software Factory-lijst, epic-roadmap, afgehandelde onderzoeksvragen, roadmap-sessies, overleggen, eventuele tokenacties, een afzonderlijke storywachtrij en workspace-publicaties. Leveringen en kandidaten komen daarmee zowel in cycluscontext als in globale secties voor. Dit is concreet resterende informatieduplicatie; zonder visuele acceptatie-inspectie kan niet worden vastgesteld hoe hinderlijk die in de uiteindelijke layout is.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart)

### Globale lijsten zijn nog als terugval nuttig, maar hun permanente prominentie is niet vanzelfsprekend

De cycluskaarten labelen resultaten terecht als afkomstig uit geladen gegevens en tonen onafhankelijke laad- en fouttoestanden. De globale leveringslijst en storywachtrij bieden daardoor nog een controle- en totaalperspectief wanneer koppelingen of bronnen onvolledig zijn. De open onderzoeksvraag is niet of deze informatie moet verdwijnen, maar of zij continu op hetzelfde taakgerichte hoofdscherm moet staan of alleen bij uitzondering of via een secundaire weergave nodig is.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart)

### Vergelijkbare producten scheiden overzicht, onderliggende items en detail

Linear toont op de Cycles-pagina een hoog-overzicht van huidige, toekomstige en eerdere cycli en laat gebruikers doorklikken naar de bijbehorende issues en grafieken. Projectdetails en uitgebreidere informatie kunnen bovendien in een apart zijpaneel worden geopend. GitHub Actions gebruikt eveneens een lijst van runs als ingang en opent daarna een afzonderlijke runsamenvatting met jobs, stappen en logs. Deze patronen ondersteunen onderzoek naar een taakgericht overzicht met detail op verzoek, zonder te bepalen dat Product Factory ze letterlijk moet overnemen.

Bronnen: [https://linear.app/docs/default-team-pages](https://linear.app/docs/default-team-pages), [https://linear.app/docs/use-cycles](https://linear.app/docs/use-cycles), [https://linear.app/docs/project-overview](https://linear.app/docs/project-overview), [https://docs.github.com/en/actions/how-tos/monitor-workflows/view-workflow-run-history](https://docs.github.com/en/actions/how-tos/monitor-workflows/view-workflow-run-history)

### De live bruikbaarheid blijft in deze onderzoeksronde onbewezen

De acceptatie-URL is benaderd via het voorgeschreven Playwright/Chromium-pad, maar de browser stopte vóór paginalading met een MachPortRendezvousServer-permissiefout. Er konden daarom geen screenshots, doorklikacties of visuele beoordelingen van hoofdscherm en beheer worden uitgevoerd. De omgeving zelf leverde in deze poging geen observeerbare UI-inhoud op; dit is een onderzoeksbeperking, geen vastgesteld applicatiedefect.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### Huidige applicatie

**Doel:** Product Factory stelt producteigenaren in staat autonome productcycli te starten en te volgen. Het systeem onderzoekt productvragen, kiest een richting, werkt UX en storykandidaten uit, laat die kritisch beoordelen, levert geaccepteerde stories aan Software Factory en gebruikt uitvoeringsresultaten als geheugen voor volgende cycli. Het bedient nu Product Factory zelf en hkh-autopilot.

**Wat ontbreekt:**
- Het hoofdscherm bevat na de nieuwe cycluskaarten nog steeds veel gelijkwaardige beheer- en processecties naast de drie door de eigenaar genoemde kerntaken.
- Kandidaten en Software Factory-leveringen worden zowel binnen cycluskaarten als in globale secties gepresenteerd, waardoor de eigenaar nog steeds tussen meerdere perspectieven moet bepalen welk overzicht leidend is.
- De globale lijsten blijven nuttig bij onvolledige koppelingen, maar de interface maakt nog geen duidelijk onderscheid tussen normale eigenaarstaken en uitzonderlijke operationele controle.
- De daadwerkelijke visuele informatiedichtheid, scanbaarheid, responsiviteit en doorklikervaring konden door de lokale Chromium-startfout niet in de acceptatieomgeving worden beoordeeld.
- De broncode alleen bewijst niet welke secties de eigenaar werkelijk gebruikt; er is geen geraadpleegd openbaar gebruikssignaal dat de juiste resterende hoofdscherminhoud objectief rangschikt.

### Verbetermogelijkheden

- Onderzoek een taakgerichte eerste schermlaag die de startactie, recente cycli en voortgekomen stories centraal houdt en overige operationele onderdelen als afzonderlijke of ingeklapte beheerlaag aanbiedt.
- Onderzoek of de globale Software Factory-lijst en storywachtrij één gezamenlijk totaal- of uitzonderingenoverzicht kunnen vormen, zodat dezelfde story niet in meerdere gelijkwaardige secties hoeft te worden geïnterpreteerd.
- Maak expliciet welke informatie alleen als veilige terugval dient bij een laadfout of niet-koppelbaar record; zo kan die informatie conditioneel zichtbaar worden zonder controleerbaarheid te verliezen.
- Onderzoek productfiltering of een productgerichte ingang, omdat de huidige globale secties gegevens van meerdere producten mengen terwijl de cycluskaarten hun context per product tonen.
- Gebruik uitsluitend privacyarme operationele metadata om vast te stellen welke hoofdschermfuncties daadwerkelijk worden geopend, bijvoorbeeld geaggregeerde interactietellingen zonder identiteit, vrije tekst of gegevens van andere producten.
- Herhaal de visuele acceptatie-inspectie zodra Chromium in een geschikte runtime kan starten en toets dan ten minste desktop- en smalle viewport, gesloten en geopende cycluskaarten, lange redenen, laad/fouttoestanden en navigatie naar beheer.
- Beoordeel bij verdere reductie expliciet of afkeurredenen en beslisbron scanbaar blijven; vereenvoudiging mag de even belangrijke roadmaprichting rond afkeurtraceerbaarheid niet terugdraaien.

### Inspiratiebronnen

- [Linear Cycles](https://linear.app/docs/default-team-pages) — Presenteert huidige, toekomstige en eerdere cycli eerst op hoofdlijnen en opent onderliggende issues en grafieken per gekozen cyclus.
- [Linear Project Details Sidebar](https://linear.app/docs/project-overview) — Laat zien hoe uitgebreide projectinformatie beschikbaar kan blijven zonder permanent alle informatie in de primaire overzichtslaag te tonen.
- [GitHub Actions run history](https://docs.github.com/en/actions/how-tos/monitor-workflows/view-workflow-run-history) — Gebruikt een scanbare runlijst als ingang en verplaatst jobs, stappen en logs naar een afzonderlijke runsamenvatting.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md) | 2026-08-13 | Geen repositorylicentie aangetroffen via het publieke GitHub-license-endpoint; hergebruiksrechten daarom onbekend. Alleen feitelijk geanalyseerd. | Primaire productbeschrijving, systeemgrenzen en relatie met Software Factory en de workspace. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md) | 2026-08-13 | Geen repositorylicentie aangetroffen; hergebruiksrechten onbekend. Alleen feitelijk geanalyseerd. | Primaire functionele documentatie van cyclusstart, agentketen, levering, dashboardgedrag en actuele cycluskaarten. |
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart) | 2026-08-13 | Geen repositorylicentie aangetroffen; broncodehergebruik is niet verondersteld en er is niets overgenomen. | Actuele primaire implementatiebron voor hoofdschermhiërarchie, startactie, cycluskaarten, beslisbron, globale leveringslijst, roadmap, storywachtrij en workspace-sectie. |
| [bron](https://product-factory-acceptance.vdzonsoftware.nl) | 2026-08-13 | Rechtenindicatie onbekend; uitsluitend benaderd voor visuele productevaluatie. | Draaiende acceptatieomgeving die de feitelijke gebruikerservaring had moeten tonen; raadpleging bleef beperkt doordat de lokale browser vóór paginalading stopte. |
| [bron](https://linear.app/docs/default-team-pages) | 2026-08-13 | Publiek toegankelijke commerciële productdocumentatie; hergebruiklicentie onbekend. Alleen het algemene interactiepatroon is geanalyseerd. | Beschrijft hoe Linear hoog-overzicht van cycli scheidt van de onderliggende issue- en grafiekdetails. |
| [bron](https://linear.app/docs/use-cycles) | 2026-08-13 | Publiek toegankelijke commerciële productdocumentatie; hergebruiklicentie onbekend. Geen tekst, vormgeving of code overgenomen. | Vergelijkingsbron voor cycli als primaire context en de relatie tussen historische totalen en actuele onderliggende items. |
| [bron](https://linear.app/docs/project-overview) | 2026-08-13 | Publiek toegankelijke commerciële productdocumentatie; hergebruiklicentie onbekend. Alleen als inspiratie gebruikt. | Toont het patroon van een compacte overzichtscontext met uitgebreidere informatie in een afzonderlijk detailszijpaneel. |
| [bron](https://docs.github.com/en/actions/how-tos/monitor-workflows/view-workflow-run-history) | 2026-08-13 | GitHub Docs-content is volgens de GitHub Docs-repository beschikbaar onder CC BY 4.0; handelsmerken en overige onderdelen kunnen afzonderlijke voorwaarden hebben. | Vergelijkingsbron voor een runlijst die naar een afzonderlijke samenvatting, stappen en logs leidt. |

## Productbeslissing

Maak van het hoofdscherm een taakgerichte eerste laag rond één primaire startactie en een compacte lijst met recente cycluskaarten. Iedere kaart toont in gesloten toestand status, startmoment, kernreden, beslisbron en aantallen; uitklappen toont de kandidaten en leveringen van die cyclus. Verplaats de afzonderlijke Software Factory-lijst, storywachtrij en overige operationele secties naar één secundaire beheerweergave. Toon op het hoofdscherm alleen een duidelijke waarschuwing met een link naar die beheerweergave wanneer gegevens niet geladen of niet betrouwbaar aan een cyclus gekoppeld kunnen worden. Productbeheer, roadmap, onderzoeksvragen, sessies, overleggen en workspace-publicaties blijven buiten deze wijziging functioneel ongewijzigd en worden uitsluitend vanuit de primaire hoofdschermlaag bereikbaar gemaakt. Dit is een presentatie- en navigatiewijziging: geen datamigratie, geen wijziging aan cyclusuitvoering, levering, authenticatie of andere producten.

**Waarom:** Het huidige hoofdscherm is historisch gegroeid als gecombineerd bedienings- en operationeel controlescherm. Daardoor waren globale lijsten nuttig voordat cyclusresultaten betrouwbaar in samenhang konden worden getoond. Nu de cycluskaarten die samenhang op main bieden, zorgt de permanente herhaling van kandidaten en leveringen vooral voor concurrerende perspectieven. De gekozen richting voltooit een kleine, omkeerbare volgende stap binnen epic theme-product-factory-0001: de drie eigenaarstaken krijgen één duidelijke ingang, terwijl controleerbaarheid behouden blijft via beheer en expliciete uitzonderingsmeldingen. Onzeker blijft hoe groot de visuele winst werkelijk is, omdat de acceptatieomgeving niet gerenderd kon worden; daarom moet de wijziging geïsoleerd blijven en na implementatie visueel worden getoetst.

### Prioriteiten
- Behoud de prominente actie om direct een nieuwe productcyclus te starten.
- Maak recente cycluskaarten het leidende overzicht voor eerdere opbrengsten en voortgekomen stories.
- Behoud status, kernreden en beslisbron in de scanbare gesloten kaart, zodat vereenvoudiging epic theme-product-factory-0002 niet ondermijnt.
- Verplaats dubbele globale kandidaten- en leveringslijsten naar één secundaire beheerweergave zonder gegevens of controlefuncties te verwijderen.
- Toon laadfouten en niet-koppelbare records als expliciete uitzonderingen met toegang tot het volledige beheerperspectief; raad nooit koppelingen en verberg geen afwijkingen stilzwijgend wegeneen compacte UI wenselijker lijkt dan controleerbaarheid zou zijn geweest—hmm avoid malformed Dutch. Let's correct entire string? Need valid JSON. I'll regenerate cleanly.

### Besluiten
- **Gebruik de bestaande cycluskaarten als primaire informatiedrager op het hoofdscherm.** — Ze groeperen kandidaten en leveringen al per cyclus en tonen in gesloten toestand de belangrijkste scaninformatie, inclusief beslisbron. Dit beperkt de wijziging tot hiërarchie en navigatie.
- **Bundel de afzonderlijke Software Factory-lijst en storywachtrij in één secundaire beheerweergave.** — De globale lijsten dupliceren informatie uit de cycluskaarten, maar blijven waardevol als totaal- en controleperspectief wanneer koppelingen of bronnen onvolledig zijn.
- **Maak uitzonderingen conditioneel zichtbaar op het hoofdscherm en laat ze doorlinken naar beheer.** — Laadfouten en ambigue koppelingen mogen niet verdwijnen door vereenvoudiging. Een expliciete waarschuwing bewaart controleerbaarheid zonder het normale hoofdscherm permanent met terugvalinformatie te belasten.
- **Beperk deze iteratie tot informatiehiërarchie en navigatie; verander geen onderliggende data of processen.** — De productmissie en architectuur maken levering aan Software Factory en terugkoppeling naar volgende cycli bedrijfskritisch. Een geïsoleerde presentatiewijziging is beter terug te draaien en raakt geen andere producten.
- **Accepteer de richting pas als visuele toetsing aantoont dat desktop en smalle viewport scanbaar blijven en beslisbron, lange redenen, open kaarten en fouttoestanden begrijpelijk zijn.** — De live interface kon tijdens het onderzoek niet worden bekeken. Broncode alleen bewijst niet dat de nieuwe hiërarchie werkelijk prettiger werkt; deze onzekerheid moet expliciet onderdeel van de acceptatie zijn.

## UX-voorstel: Taakgericht hoofdscherm met beheer bij uitzondering

**Gebruikersdoel:** Als producteigenaar wil ik vanuit één rustige eerste laag een productcyclus starten, recente opbrengsten begrijpen en voortgekomen stories volgen, terwijl operationele details en afwijkingen controleerbaar blijven.

### Flow
1. De eigenaar opent het hoofdscherm en krijgt focus op de paginatitel; direct daarna staat de primaire actie ‘Nieuwe cyclus starten’.
2. De eigenaar activeert ‘Nieuwe cyclus starten’ en volgt de bestaande startflow; cyclusuitvoering en gegevensverwerking veranderen niet.
3. Onder de startactie scant de eigenaar de recente cycluskaarten, standaard gesloten en logisch geordend van meest naar minst recent.
4. Iedere gesloten kaart toont product, status, startmoment, kernreden, beslisbron en aantallen kandidaten en leveringen.
5. De eigenaar klapt één kaart open via een echte knop en ziet de kandidaten en leveringen van uitsluitend die cyclus, inclusief hun afzonderlijke statussen.
6. De eigenaar activeert een kandidaat of levering om via de bestaande bestemming de beschikbare details te openen.
7. Alleen bij een laadfout of niet-betrouwbaar koppelbaar record verschijnt boven de cycluslijst een waarschuwing met aard en aantal van de afwijkingen en de actie ‘Bekijk in beheer’. Koppelingen worden nooit geraden.
8. Via ‘Beheer’ opent de eigenaar een secundaire weergave met het globale totaal- en uitzonderingenperspectief, waaronder de Software Factory-leveringen en storywachtrij.
9. Productbeheer, roadmap, onderzoeksvragen, sessies, overleggen en workspace-publicaties zijn vanuit de beheerweergave bereikbaar en blijven functioneel ongewijzigd.
10. De eigenaar kan vanuit beheer via ‘Terug naar overzicht’ terugkeren; focus wordt na navigatie voorspelbaar op de paginatitel geplaatst.

### Wireframe

HOOFDSCHERM

[Skiplink: Ga naar hoofdinhoud]

Product Factory                                      [Beheer]
Start en volg autonome productcycli

[ Nieuwe cyclus starten ]  ← primaire actie

[Waarschuwing — alleen bij afwijkingen]
2 records konden niet aan een cyclus worden gekoppeld.
[ Bekijk in beheer ]

Recente cycli
[Productfilter, alleen indien al beschikbaar]

┌ Cyclus: Product Factory · 12 aug 2026 ───────── [Uitklappen ▾] ┐
│ Status: Afgerond                                             │
│ Kernreden: Hoofdscherm vereenvoudigen                        │
│ Beslisbron: Productbesluit                                   │
│ 3 kandidaten · 2 leveringen                                  │
└──────────────────────────────────────────────────────────────┘

OPEN TOESTAND
┌ Cyclus: Product Factory · 12 aug 2026 ─────────── [Inklappen ▴] ┐
│ Status, kernreden, beslisbron en aantallen                     │
│ Kandidaten                                                     │
│ • Taakgericht hoofdscherm                         Geaccepteerd  │
│ • Beheerweergave                                  Geaccepteerd  │
│ Leveringen                                                     │
│ • Story PF-123                                    Uitgevoerd   │
│ • Story PF-124                                    In wachtrij   │
└────────────────────────────────────────────────────────────────┘

[Meer cycli laden]

BEHEERWEERGAVE

[← Terug naar overzicht]
Beheer
[Uitzonderingen (2)] [Stories en leveringen] [Overige onderdelen]
Globale controle-informatie zonder duplicatie op het hoofdscherm.

### Interactiehypotheses
- Als de globale story- en leveringslijsten naar beheer worden verplaatst, bevat het hoofdscherm bij een foutloze toestand alleen de startactie en recente cycli als primaire taaksecties. Toets met een geautomatiseerde component- of semantische DOM-test.
- Als cycluskaarten standaard gesloten zijn, blijven status, startmoment, kernreden, beslisbron en beide aantallen zonder interactie beschikbaar in de accessibility tree. Toets voor elke kaart met widgettests en accessibility-tree-asserties.
- Als een kaart wordt uitgeklapt, verschijnen uitsluitend kandidaten en leveringen met dezelfde betrouwbare cycluskoppeling; ambigue records verschijnen daar nooit. Toets met fixtures voor correcte, ontbrekende en ambigue koppelingen.
- Als een bron niet laadt of records niet betrouwbaar koppelbaar zijn, verschijnt precies één waarschuwing met type en aantal afwijkingen en een werkende beheerlink. Toets met fout- en randgevalfixtures.
- Als er geen afwijkingen zijn, ontbreekt de uitzonderingswaarschuwing volledig uit zowel het zichtbare scherm als de accessibility tree. Toets met een foutloze fixture.
- Als beheer wordt geopend, zijn de globale storywachtrij en Software Factory-leveringen daar vindbaar zonder gegevensverlies en zonder dezelfde globale lijsten op het hoofdscherm. Toets met navigatie- en inhoudsvergelijkingstests op vaste fixtures zonder persoonsgegevens of data van andere producten te gebruiken of op te slaan als telemetrie-event payloads. Indien multi-product-fixtures functioneel nodig zijn, blijven die synthetisch en worden ze alleen gebruikt om productisolatie te verifiëren, niet om echte andere-productdata te verwerken of tonen binnen een gekozen productcontext. Normale bediening voegt geen nieuwe cross-product verwerking toe; beheer toont uitsluitend reeds geautoriseerde operationele metadata binnen de bestaande productgrenzen. Verwijder deze zin? Need concise and hypotheses shouldn't privacy clutter. Better rewrite cleanly entire item: '... vaste synthetische fixtures.' If product global relevant perhaps okay. Tests shouldn't use actual data. Use synthetic only.

### Toegankelijkheid
- Alle acties zijn native knoppen of links met een zichtbare focusindicator en een logische toetsenbordvolgorde: skiplink, beheer, startactie, waarschuwing, cycluskaarten en vervolgacties.
- Elke uitklapknop heeft een toegankelijke naam met cyclusidentificatie en gebruikt aria-expanded plus aria-controls; de statuswijziging is voor schermlezers waarneembaar.
- Koppen en landmarks vormen een consistente hiërarchie; kaarten zijn geen klikbare containers en geneste kandidaat- en leveringsacties hebben afzonderlijke namen.
- Status, beslisbron en waarschuwingen worden nooit uitsluitend door kleur of iconen overgebracht; tekstlabels blijven beschikbaar.
- Tekst en interactieve elementen voldoen minimaal aan WCAG 2.2 AA-contrast; focusindicatoren hebben voldoende contrast tegen aangrenzende kleuren.
- Lange kernredenen kunnen afbreken of uitvouwen zonder horizontaal scrollen, overlap of verlies van bediening op een smalle viewport.
- Na navigatie naar overzicht of beheer wordt focus programmatisch naar de paginatitel verplaatst; uitklappen veroorzaakt geen onverwachte focusverplaatsing.
- Geautomatiseerde controles omvatten toetsenbordnavigatie, semantiek/accessibility tree, tekstschaling, contrast, smalle viewport en gesloten, open, laad-, lege en fouttoestanden.

### Privacy
- De wijziging introduceert geen nieuwe gegevensverzameling, datamigratie, authenticatieverwerking of vrije tekst.
- Toon uitsluitend operationele metadata van Product Factory zelf: cyclusidentificatie, productcontext, status, tijdstip, kernreden, beslisbron, aantallen, kandidaatstatus, leveringsstatus en technische afwijkingscategorie.
- Verwerk of toon geen persoonsgegevens en geen gebruikersdata van andere producten; tests gebruiken uitsluitend synthetische Product Factory-fixtures.
- Waarschuwingen tonen alleen categorie en aantal afwijkingen, geen payloads, tokens, geheime waarden of onnodige recordinhoud.
- Voeg voor deze MVP geen gebruikstelemetrie, gebruikersidentificatoren, sessiereplay of cross-productanalyse toe.
- De beheerweergave erft de bestaande autorisatie en bewaartermijnen; de presentatiewijziging maakt geen operationele metadata voor nieuwe ontvangers toegankelijk.
- Een eventueel onvermijdelijk extern access token wordt uitsluitend via het bestaande beveiligde mechanisme verstrekt en wordt nooit in kaarten, waarschuwingen, logging of testfixtures opgenomen.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is een kleine, geïsoleerde en agent-uitvoerbaar te verifiëren frontendwijziging. Zij behoudt bestaande gegevens, fouttoestanden en detailacties, introduceert geen privacygevoelige verwerking en overlapt niet exact met reeds geleverd werk. Er zijn geen blokkerende problemen.
- **WARNING · ACCESSIBILITY** — De criteria toetsen toetsenbordbediening, focus, accessibility-tree-aanwezigheid, tekstschaling en smalle viewports, maar noemen geen expliciete geautomatiseerde contrastcontrole voor tekst, links en focusindicatoren. Dit blokkeert niet, omdat bestaande toegankelijke stijlen kunnen worden hergebruikt, maar voldoende contrast blijft een bindende productregel.
- **INFO · SOURCE** — De primaire repositorybronnen zijn geschikt voor feitelijke analyse van het bestaande gedrag. De hergebruiksrechten van de repository en commerciële vergelijkingsbronnen zijn deels onbekend; de kandidaat vereist echter geen overname van externe tekst, code of vormgeving.
- **INFO · SCOPE** — De kandidaat verplaatst alleen de twee dubbele globale lijsten en laat andere operationele hoofdschermsecties staan. Dit is een bewuste, omkeerbare deelstap en hoeft epic theme-product-factory-0001 niet zelfstandig af te ronden.
- **INFO · CONSISTENCY** — De afhankelijkheid van story:64 is inhoudelijk noodzakelijk omdat de cycluskaarten het leidende overzicht worden. De afhankelijkheid van story:52 lijkt niet noodzakelijk voor deze verplaatsing, maar beide stories zijn al gepubliceerd en dit belemmert autonome uitvoering niet.

## Geaccepteerde storykandidaten

### Verplaats globale storywachtrij en leveringslijst naar één beheerweergave

_Sleutel: `verplaats-storylijsten-naar-beheer`_

Voeg een secundaire beheerweergave toe en verplaats daarheen uitsluitend de bestaande globale storywachtrij en Software Factory-leveringslijst. Verwijder deze twee lijsten van het hoofdscherm, waar de gepubliceerde cycluskaarten uit story:64 voortaan het leidende overzicht van kandidaten en leveringen vormen. Plaats op het hoofdscherm een native link ‘Beheer’ naar de nieuwe weergave en in beheer een link ‘Terug naar overzicht’. Hergebruik de bestaande gegevensbronnen, inhoud, statussen, laad-, lege en fouttoestanden en bestaande detailbestemmingen zonder records opnieuw te koppelen of onderliggende processen te wijzigen. Productbeheer, roadmap, onderzoeksvragen, sessies, overleggen, tokenacties en workspace-publicaties blijven in deze story functioneel en qua plaatsing ongewijzigd. Dit is uitsluitend een frontendwijziging zonder nieuwe API, opslag, telemetrie, authenticatie- of leveringslogica.

**Acceptatiecriteria**
- Het hoofdscherm bevat na succesvolle gegevenslading geen globale storywachtrij en geen globale Software Factory-leveringslijst meer; een geautomatiseerde widget- of DOM-test verifieert dat beide secties daar ook niet in de accessibility tree voorkomen.
- Een native link met de zichtbare naam ‘Beheer’ opent één secundaire beheerweergave waarin zowel de bestaande globale storywachtrij als de bestaande Software Factory-leveringslijst aanwezig zijn.
- De beheerweergave toont voor vaste synthetische fixtures exact dezelfde records, zichtbare statussen en bestaande detailacties als de twee huidige globale hoofdschermsecties, zonder records te verliezen, samen te voegen of aan een cyclus toe te schrijven.
- De bestaande laad-, lege en fouttoestanden van beide gegevensbronnen blijven onafhankelijk zichtbaar en semantisch benoemd in beheer; geautomatiseerde tests dekken voor elke bron succes, leegte en fout.
- Een native link ‘Terug naar overzicht’ navigeert terug naar het hoofdscherm; geautomatiseerde toetsenbordtests verifiëren een logische tabvolgorde en zichtbare focus voor beide navigatielinks.
- De uitklapbare cycluskaarten, prominente cyclusstartactie en alle overige hoofdschermsecties behouden hun bestaande gedrag; regressietests verifiëren ten minste starten, openen/sluiten van een cycluskaart en aanwezigheid van status, kernreden en beslisbron in de gesloten kaart.
- Geautomatiseerde tests op een smalle viewport en met tekstschaling verifiëren dat de beheerlinks en beide verplaatste lijsten zonder horizontale pagina-scroll, overlap of onbereikbare bediening bruikbaar blijven.
- De implementatie voegt geen backend-, API-, schema-, database-, authenticatie-, telemetrie- of Software Factory-leveringswijziging toe.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/dashboard-frontend/lib/main.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/architecture/functioneel-overzicht.md), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/README.md), [https://linear.app/docs/project-overview](https://linear.app/docs/project-overview), [https://docs.github.com/en/actions/how-tos/monitor-workflows/view-workflow-run-history](https://docs.github.com/en/actions/how-tos/monitor-workflows/view-workflow-run-history)

Afhankelijkheden: story:64, story:52 (herkend als bestaande stories: 64, 52)

Risico's: De beheerweergave kan als nieuwe navigatielaag minder vindbaar zijn voor operationele controle; duidelijke wederzijdse links en geautomatiseerde toegankelijkheidstests beperken dit risico., De twee bestaande lijsten kunnen impliciete afhankelijkheden van hun huidige hoofdschermcontext hebben; regressietests moeten daarom detailacties en alle laad-, lege en fouttoestanden bewaken., Omdat de acceptatieomgeving tijdens het onderzoek niet kon worden gerenderd, is de werkelijke visuele winst onzeker; geautomatiseerde viewport-, semantiek- en screenshottests moeten de wijziging verifieerbaar maken., Het hoofdscherm bevat na deze kleine stap nog andere operationele secties; deze kandidaat rondt epic theme-product-factory-0001 daarom niet zelfstandig af.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
