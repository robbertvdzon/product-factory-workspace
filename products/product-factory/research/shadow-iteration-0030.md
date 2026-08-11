---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0030
date: 2026-08-11
status: approved
sources:
  - https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/factory/functional-spec.md
  - https://github.com/robbertvdzon/product-factory/commits/main/
  - https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart
  - https://github.com/robbertvdzon/product-factory/commit/dd9f691338c72dfe920d7dec42d3838abbe5ed66
  - https://github.com/robbertvdzon/product-factory/commit/ce69785cccab3cedfb430efe67360ed13aad1fa4
  - https://product-factory-acceptance.vdzonsoftware.nl
  - https://product-factory-api-acceptance.vdzonsoftware.nl
  - https://www.numeric.io/blog/ai-audit-trail
  - https://eucalipse.com/articles/ai-agent-approval-queue-human-in-the-loop
---
# Productcyclus 30

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Ik heb de huidige staat van Product Factory bepaald via de publieke GitHub-repository (broncode, commitgeschiedenis, story-bestanden) en directe Playwright-inspectie van de draaiende acceptatieomgeving (screenshots, Flutter-semantics/ariaSnapshot, en meegeluisterde API-responses). Cyclus 28's beide kandidaten (story product-factory-26 en -27) staan bevestigd live: "Start productcyclus nu" is nu een losstaande, dominante knop en de configuratievelden (missie, repo, workspace, max-stories, WIP-limiet, AI-provider/model, cyclustijden) zijn verplaatst naar het Instellingen-paneel. Tegelijk is er vandaag (2026-08-11, 12:49–13:44 UTC) buiten de normale Software Factory-storyflow om een volledig nieuwe "roadmap"-functionaliteit (thema's/epics, Product Manager-rol, roadmap-sessies) rechtstreeks naar main gecommit en gedeployed, die twee extra platte topsecties aan de homepage toevoegt — het tegenovergestelde effect van het lopende hiërarchie-thema. Het traceerbaarheidsthema (wie/wat besliste een afkeuring) is bij live-inspectie van alle drie voorbeeldcycli en het bijbehorende broncodefragment nog steeds niet opgelost: er bestaat geen apart, gestructureerd "beslist door"-veld; die informatie zit impliciet verstopt in vrije tekst of ontbreekt volledig bij technische storingen. De functional-spec bevestigt dit zelfs expliciet door bewust te documenteren dat de badge alleen de uitkomst toont, "niet waarom". Eén transiënte volledige-pagina 500-fout werd waargenomen bij de eerste laadpoging vlak na de laatste deploy van vandaag, maar was niet reproduceerbaar bij drie vervolgpogingen.

### Cyclus 28: prominente CTA en verplaatste instellingen zijn live bevestigd

Via een Playwright-sessie op de acceptatieomgeving (Flutter-semantics ingeschakeld + ariaSnapshot) is bevestigd dat 'Start productcyclus nu' nu als losstaande, dominante knop bovenaan de Producten-kaart staat, gescheiden van de secundaire knoppenrij (Pauzeren, Instellingen, Start overleg, Start roadmap-sessie nu). De configuratievelden missie, repo/workspace, max-stories, WIP-limiet, AI-provider/model en cyclustijden zijn niet langer standaard zichtbaar op de kaart zelf. Dit komt overeen met de gemergede stories product-factory-26 en product-factory-27 (commits ce69785 en dd9f691, beide gedeployed vóór 06:31 UTC vandaag) en met de bijgewerkte functional-spec.md.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/commit/dd9f691338c72dfe920d7dec42d3838abbe5ed66](https://github.com/robbertvdzon/product-factory/commit/dd9f691338c72dfe920d7dec42d3838abbe5ed66), [https://github.com/robbertvdzon/product-factory/commit/ce69785cccab3cedfb430efe67360ed13aad1fa4](https://github.com/robbertvdzon/product-factory/commit/ce69785cccab3cedfb430efe67360ed13aad1fa4), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/factory/functional-spec.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/factory/functional-spec.md)

### Nieuwe 'roadmap'-functie voegt vandaag twee extra platte topsecties toe aan de homepage

Tussen 12:49 en 13:44 UTC vandaag zijn zes commits ('roadmap: fase 1' t/m 'fase 6') rechtstreeks naar main gepusht — niet via de gebruikelijke 'product-factory-NN: Software Factory changes (#PR)'-flow die alle overige recente wijzigingen volgt. Live inspectie van de homepage (ariaSnapshot) toont dat dit twee nieuwe, aan alle andere secties gelijkwaardige topsecties toevoegt: 'Roadmap' en 'Roadmap-sessies', naast de al bestaande 'Productcycli en onderzoekssessies', 'Software Factory-stories', 'Overleggen', 'Storywachtrij' en 'Workspace'. De homepage telt nu acht in plaats van zeven gelijkwaardige blokken.

Bronnen: [https://github.com/robbertvdzon/product-factory/commits/main/](https://github.com/robbertvdzon/product-factory/commits/main/), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### 'Wie/wat besliste' is bij live-inspectie van alle drie voorbeeldcycli nog steeds niet expliciet zichtbaar

In de detaildialogen van de drie zichtbare cycli in de acceptatieomgeving (shadow-hkh-autopilot-0001/2/3, opgehaald via Flutter-ariaSnapshot) staat de beslisinformatie alleen impliciet in vrije tekst: iteratie 3 toont 'Reden: Criticusoordeel REVISE geregistreerd...' (impliceert AI-criticus, maar zonder gestructureerd label), iteratie 2 toont enkel 'Foutreden: Workspace-publicatie tijdelijk niet beschikbaar' zonder enige aanduiding dat hier niemand een beslissing nam (technische storing), en iteratie 1 toont losse stapknoppen (Criticus, Product owner, Onderzoeker, ...) zonder samenvattend 'beslist door'-veld. Een grep in de broncode (main.dart, regels 1215-1244) bevestigt dat er geen apart 'beslist door'/decider-veld bestaat: alleen een voorwaardelijke guardrail-notitie wordt toegevoegd voor het randgeval REJECTED+criticVerdict=ACCEPT.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart)

### Functional-spec documenteert expliciet dat de badge 'niet waarom' toont — bevestigt dat theme-0002 nog open staat

De officiële functionele specificatie beschrijft letterlijk dat het activeren van de classificatiebadge een disclaimerpaneel toont met de tekst 'Dit toont wat de uitkomst was, niet waarom'. Dit weerlegt expliciet de eerdere aanname (cyclus 26) dat bestaande badges het traceerbaarheidsprobleem grotendeels al oplossen: het ontwerp erkent zelf dat de badge geen 'waarom'/'wie besliste'-informatie draagt.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/factory/functional-spec.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/factory/functional-spec.md)

### Eenmalige, niet-reproduceerbare volledige-pagina 500-fout vlak na de laatste deploy van vandaag

Bij de eerste paginalaad-poging (Playwright, direct na de 'roadmap: fase 6'-deploy die om 13:44:05 UTC afrondde) toonde de homepage de blokkerende fout 'Dashboard kon niet laden: Bad state: Dashboard API gaf 500.' zonder retry-optie. Drie directe vervolgpogingen (elk met netwerkresponse-capture) toonden alle API-aanroepen (products, shadow-iterations, roadmap/themes, etc.) met status 200, dus het probleem was niet reproduceerbaar en lijkt een kortstondige deploy-hik te zijn geweest, geen structureel defect.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/commits/main/](https://github.com/robbertvdzon/product-factory/commits/main/)

### Externe inspiratie: audit-trail-patronen scheiden expliciet 'wat besloten' van 'wie/wat besliste' (bot vs. mens)

Vakliteratuur over audit trails in AI-ondersteunde goedkeuringsworkflows beschrijft als bewezen patroon: een apart tabel/veld per beslissing met status (pending/approved/rejected/auto-completed/reverted) plus expliciete toekenning aan een gestructureerde 'wie/wat'-bron (automatisering vs. menselijke reviewer), omdat 'the model approved it' geen accountable antwoord is voor een toezichthouder of eigenaar. Dit onderbouwt een concreet ontwerprichting voor het nog open traceerbaarheidsthema van Product Factory.

Bronnen: [https://www.numeric.io/blog/ai-audit-trail](https://www.numeric.io/blog/ai-audit-trail), [https://eucalipse.com/articles/ai-agent-approval-queue-human-in-the-loop](https://eucalipse.com/articles/ai-agent-approval-queue-human-in-the-loop)

### Huidige applicatie

**Doel:** Product Factory is het systeem dat autonome productontwikkeling aanstuurt: het onderzoekt, kiest, ontwerpt en levert stories aan de Software Factory voor andere producten (momenteel hkh-autopilot) en past nu diezelfde cyclus toe op zichzelf. De primaire gebruiker is de producteigenaar, die via een Flutter-webdashboard productcycli start, de voortgang en uitkomsten daarvan volgt, en de daaruit voortkomende Software Factory-stories inziet.

**Wat ontbreekt:**
- De homepage is, ondanks de eerste hiërarchie-stap in cyclus 28 (dominante CTA, config naar Instellingen), vandaag opnieuw platter/drukker geworden: een nieuwe 'roadmap'-functie voegt twee extra, gelijkwaardige topsecties toe (Roadmap, Roadmap-sessies), waardoor het totaal van 7 naar 8 platte blokken is gegaan — tegengesteld aan de expliciete eigenaarswens voor duidelijke nadruk op de drie kernacties.
- De traceerbaarheid van afkeuring/revisie ('wie of wat besliste: mens, evaluatie-agent of guardrail-check') is, bevestigd in zowel de live UI van drie voorbeeldcycli als in de broncode, nog steeds niet als apart, gestructureerd veld aanwezig; de informatie zit verstopt in vrije tekst of ontbreekt volledig bij technische storingen.
- De functional-spec documenteert zelf expliciet dat de classificatiebadge alleen de uitkomst toont en niet de reden ('Dit toont wat de uitkomst was, niet waarom'), wat rechtstreeks ingaat tegen de eerdere aanname (cyclus 26) dat bestaande badges dit probleem al grotendeels oplossen.
- De nieuwe roadmap-functionaliteit (thema's/epics, Product Manager-rol, roadmap-sessies) is buiten de normale Software Factory-storyflow om rechtstreeks naar main gedeployed en nog niet vanuit gebruiksperspectief geëvalueerd; in de acceptatieomgeving zijn voor het enige zichtbare product (hkh-autopilot) geen roadmapthema's aanwezig, waardoor de bruikbaarheid van deze nieuwe schermen nog niet met echte data is getoetst.
- Eenmalig een volledige-pagina blokkerende fout waargenomen ('Dashboard API gaf 500') zonder retry-mogelijkheid, direct na een deploy; niet reproduceerbaar bij drie vervolgpogingen, maar de harde, niet-herstelbare foutafhandeling is op zich een aandachtspunt.

### Verbetermogelijkheden

- Voeg een expliciet, gestructureerd 'Beslist door'-veld toe aan zowel de cyclusrij in het overzicht als het detaildialoog, met een vaste set waarden (bijv. 'AI-criticus', 'guardrail (automatisch)', 'technische storing — geen beslisser', 'mens'), in plaats van dit impliciet in vrije Reden-tekst te laten zitten — dit sluit direct aan bij de expliciete eigenaarswens van 2026-08-10 en bij het externe audit-trail-patroon (bot vs. mens) uit de vakliteratuur.
- Zet de hiërarchie-stap van cyclus 28 door naar de resterende twee pijlers uit het overlegdossier: groepeer 'Productcycli en onderzoekssessies', 'Software Factory-stories' en 'Storywachtrij' visueel samen als één 'wat leverden cycli op'-cluster, in plaats van ze als losse, gelijkwaardige secties naast Roadmap/Overleggen/Workspace te laten staan.
- Borg bij toekomstige functionaliteit (zoals de net toegevoegde roadmap-schermen) een expliciete toets tegen het lopende hiërarchiethema vóórdat een nieuwe topsectie aan de platte homepage wordt toegevoegd, zodat nieuwe features het net verbeterde overzicht niet weer verdichten.
- Evalueer de nieuwe roadmap-schermen (thema-detailweergave, roadmap-sessies) op bruikbaarheid zodra er representatieve thema-data in de acceptatieomgeving staat — dit kon in dit onderzoek niet worden getoetst omdat het enige zichtbare demoproduct geen roadmapthema's had.
- Onderzoek of de eenmalige blokkerende 500-fout een structureel patroon is rond deploy-momenten (bijv. door logs/monitoring van de acceptatieomgeving rond deploytijdstippen te bekijken) en overweeg een zachtere foutafhandeling (retry/gedeeltelijke weergave) in plaats van een volledige blokkade.

### Inspiratiebronnen

- [Numeric — AI Audit Trail for Accounting](https://www.numeric.io/blog/ai-audit-trail) — Beschrijft het patroon van een apart, gestructureerd beslissingsveld (status + reden + wie/wat besliste, bot vs. mens) dat compliance-proof is — direct toepasbaar op het nog open 'wie/wat besliste'-traceerbaarheidsprobleem van Product Factory.
- [Eucalipse — The Approval Queue Pattern for AI Agents](https://eucalipse.com/articles/ai-agent-approval-queue-human-in-the-loop) — Beschrijft een 'approval queue'-UI-patroon met expliciete status (pending/approved/rejected/auto-completed) en toegekende beslisser, bruikbaar als ontwerpreferentie voor zowel het traceerbaarheids- als het cyclusoverzicht-thema.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/factory/functional-spec.md) | 2026-08-11 | Publieke GitHub-repository zonder expliciete LICENSE-bestand; eigendom van de producteigenaar (robbertvdzon). Geraadpleegd als eigen productdocumentatie voor intern onderzoek, geen herpublicatie. | Bevat de meest actuele beschrijving van de dashboardstructuur, het Instellingen-paneel en het classificatiebadge-gedrag, en bevestigt daarmee zowel wat al is opgelost als wat bewust nog open staat ('niet waarom'). |
| [bron](https://github.com/robbertvdzon/product-factory/commits/main/) | 2026-08-11 | Publieke GitHub-repository zonder expliciete LICENSE; eigendom van de producteigenaar. Geraadpleegd als eigen commitgeschiedenis. | Toont exact welke stories (26, 27) en welke losstaande 'roadmap'-commits vandaag zijn gemerged en gedeployed, inclusief tijdstippen — nodig om vast te stellen wat al live staat versus wat nog niet is opgepakt. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart) | 2026-08-11 | Publieke GitHub-repository zonder expliciete LICENSE; eigendom van de producteigenaar. Geraadpleegd als eigen broncode voor intern onderzoek. | Bronbewijs op codeniveau dat er geen apart gestructureerd 'beslist door'-veld bestaat, alleen voorwaardelijke vrije tekst — nodig om de bevinding niet louter op UI-observatie te baseren. |
| [bron](https://github.com/robbertvdzon/product-factory/commit/dd9f691338c72dfe920d7dec42d3838abbe5ed66) | 2026-08-11 | Publieke GitHub-repository zonder expliciete LICENSE; eigendom van de producteigenaar. | Merge-commit van story product-factory-27 (prominente CTA), bewijs dat cyclus 28's tweede kandidaat daadwerkelijk is gebouwd en gemerged. |
| [bron](https://github.com/robbertvdzon/product-factory/commit/ce69785cccab3cedfb430efe67360ed13aad1fa4) | 2026-08-11 | Publieke GitHub-repository zonder expliciete LICENSE; eigendom van de producteigenaar. | Merge-commit van story product-factory-26 (verplaatsing configuratievelden naar Instellingen), bewijs dat cyclus 28's eerste kandidaat daadwerkelijk is gebouwd en gemerged. |
| [bron](https://product-factory-acceptance.vdzonsoftware.nl) | 2026-08-11 | Standing acceptatieomgeving van de producteigenaar zelf, zonder login, met representatieve nepdata; expliciet aangewezen als onderzoeksbron door de opdracht. | Directe, feitelijke waarneming van de daadwerkelijk draaiende applicatie via Playwright-screenshots en Flutter-ariaSnapshot, om te verifiëren wat er werkelijk live staat versus wat de broncode/documentatie beweert. |
| [bron](https://product-factory-api-acceptance.vdzonsoftware.nl) | 2026-08-11 | Backend-API van de eigen acceptatieomgeving van de producteigenaar; alleen bevraagd via legitieme, door de frontend zelf gemaakte requests (afgeluisterd met page.on('response')), geen directe scraping van ongedocumenteerde endpoints. | Bevestigt of de dashboard-API daadwerkelijk 200/500 retourneert bij paginalaad, nodig om de eenmalige 500-fout te kunnen beoordelen als transiënt versus structureel. |
| [bron](https://www.numeric.io/blog/ai-audit-trail) | 2026-08-11 | Publiek toegankelijk vakartikel van een softwareleverancier (Numeric); geraadpleegd als achtergrondinspiratie, geen letterlijke overname van tekst of code. | Levert een concreet, extern gevalideerd ontwerppatroon (apart gestructureerd beslissingsveld, bot vs. mens) dat direct aansluit bij het nog open traceerbaarheidsthema van Product Factory. |
| [bron](https://eucalipse.com/articles/ai-agent-approval-queue-human-in-the-loop) | 2026-08-11 | Publiek toegankelijk vakartikel; geraadpleegd als achtergrondinspiratie, geen letterlijke overname. | Aanvullend bewijs voor het 'approval queue'-patroon met expliciete status en beslisser, relevant voor zowel het traceerbaarheids- als het homepage-hiërarchiethema. |

## Productbeslissing

Voeg aan elke productcyclus/iteratie een expliciet, gestructureerd 'Beslist door'-veld toe met een vaste, gesloten waardenset (mens, AI-criticus, guardrail (automatisch), technische storing — geen beslisser), en toon dit veld zowel in de rij van het cyclusoverzicht als in het detaildialoog. Dit vervangt het huidige impliciete gedrag waarbij de beslisinformatie verstopt zit in vrije Reden-tekst, in losse stapknoppen zonder samenvatting, of volledig ontbreekt bij technische storingen. De bestaande classificatiebadge blijft ongewijzigd voor wat betreft de uitkomst (geaccepteerd/afgekeurd/revise), maar wordt aangevuld met dit aparte beslisserveld — de badge zelf documenteert immers zelf al expliciet dat hij 'niet waarom' toont. De volledige hoofdscherm-herindeling (theme-0001) blijft deze cyclus bewust buiten scope, mede omdat de homepage vandaag al buiten de normale storyflow om is uitgebreid met twee nieuwe platte secties (Roadmap, Roadmap-sessies); die ontwikkeling wordt gesignaleerd maar niet in deze richting meegenomen.

**Waarom:** De eigenaar bevestigde op 2026-08-10 expliciet dat afkeuringen nog niet traceerbaar zijn en dat dit zichtbaar moet zijn in het overzicht zelf. Onafhankelijk, actueel onderzoek (live Playwright-inspectie van drie voorbeeldcycli, een codegrep in main.dart, en de functional-spec die zelf documenteert dat de badge 'niet waarom' toont) bevestigt dat dit nog steeds klopt en weerlegt de eerdere aanname uit cyclus 26 dat bestaande badges dit al oplossen. Dit maakt theme-0002 het meest gevalideerde, direct uitvoerbare aanknopingspunt: de oplossing (apart gestructureerd beslissingsveld, bot vs. mens) is bovendien onderbouwd door extern vakmateriaal over audit trails. Theme-0001 is even hoog geprioriteerd, maar de volledige herindeling is eerder al als te groot/risicovol beoordeeld, en is dat nu extra geworden doordat de homepage vandaag ongepland is uitgebreid met twee nieuwe secties buiten de normale storyflow om. Eén kleine, samenhangende richting kiezen (conform het principe 'klein en toetsbaar') betekent dus: nu het traceerbaarheidsveld toevoegen, en de hoofdschermstructuur pas aanpakken zodra de net gewijzigde situatie is gestabiliseerd en apart onderzocht.

### Prioriteiten
- Voeg een gestructureerd 'Beslist door'-veld toe (mens / AI-criticus / guardrail (automatisch) / technische storing — geen beslisser) aan cyclus-/iteratiedata.
- Toon dit veld zowel in de cyclusrij van het overzicht als in het detaildialoog, consistent met elkaar.
- Houd de wijziging klein en geïsoleerd: alleen dit veld, geen bredere homepage-herindeling in dezelfde stap.
- Leg vast waarom het huidige gedrag (badge zonder 'waarom') zo ontstond, voordat het wordt vervangen.
- Raak geen data of gedrag van hkh/hkh-autopilot aan; wijzig alleen presentatie- en classificatielogica binnen Product Factory zelf.

### Besluiten
- **Kies theme-product-factory-0002 (traceerbaarheid van afkeuring) als enige richting voor de komende cyclus: introduceer een expliciet, gestructureerd 'Beslist door'-veld op iedere cyclus/iteratie, met een vaste waardenset (mens, AI-criticus, guardrail (automatisch), technische storing — geen beslisser).** — Live-inspectie van drie voorbeeldcycli en een codegrep in main.dart tonen dat er geen apart 'beslist door'-veld bestaat; de informatie zit verstopt in vrije Reden-tekst of ontbreekt bij technische storingen. De functional-spec bevestigt zelf expliciet dat de classificatiebadge 'wat de uitkomst was, niet waarom' toont. Dit weerlegt de eerdere aanname (cyclus 26) dat bestaande badges dit al oplossen, en sluit direct aan bij de expliciete eigenaarsfeedback van 2026-08-10.
- **Gebruik een vaste, gesloten waardenset voor 'Beslist door' in plaats van vrije tekst, met een expliciet onderscheid tussen automatisering/bot en mens.** — Vakliteratuur over audit trails in AI-ondersteunde workflows beschrijft dit als bewezen patroon: een apart, gestructureerd beslissingsveld met expliciete toekenning aan bot vs. mens, omdat vrije tekst als 'the model approved it' geen accountable antwoord biedt voor een toezichthouder of eigenaar.
- **Het 'Beslist door'-veld moet zowel in de cyclusrij van het overzicht als in het detaildialoog zichtbaar zijn, niet alleen opzoekbaar na doorklikken.** — Live-inspectie toont dat de huidige detaildialogen de beslisinformatie alleen impliciet en inconsistent tonen (vrije Reden-tekst, losse stapknoppen zonder samenvattend veld, of volledige afwezigheid bij technische storingen zoals 'Workspace-publicatie tijdelijk niet beschikbaar'). Dit maakt het onmogelijk om in het overzicht zelf te zien wie/wat besliste.
- **Pak de volledige hoofdscherm-herindeling (theme-product-factory-0001) deze cyclus bewust niet op; laat de scope beperkt tot het traceerbaarheidsveld.** — Vandaag zijn buiten de normale storyflow om zes 'roadmap'-commits rechtstreeks naar main gepusht die de homepage van 7 naar 8 gelijkwaardige platte secties hebben uitgebreid — het tegenovergestelde effect van het hiërarchiethema. Een tweede grote UI-herindeling nu zou samenvallen met een net gewijzigde, nog niet stabiele hoofdschermstructuur en is dus niet 'klein en toetsbaar' in isolatie.
- **Signaleer (zonder er deze cyclus op te acteren) dat de nieuwe roadmap-secties het hiërarchiethema tegenwerken en dat de bruikbaarheid ervan nog niet met echte thema-data is getoetst; dit is materiaal voor een volgend onderzoek, niet voor deze richting.** — De roadmap-schermen zijn buiten de gebruikelijke Software Factory-flow gedeployed en in de acceptatieomgeving is voor het enige zichtbare product geen roadmapthema aanwezig, waardoor bruikbaarheid niet is getoetst. Dit apart benoemen voorkomt dat het traceerbaarheidsvoorstel wordt vervuild met een ander, nog onvoldoende onderzocht probleem.

## UX-voorstel: Structureel 'Beslist door'-veld in cyclusoverzicht en detaildialoog

**Gebruikersdoel:** Als producteigenaar wil ik in het cyclusoverzicht én in het detaildialoog direct en zonder vrije tekst te hoeven lezen kunnen zien wie of wat een afkeuring/revisie/acceptatie heeft besloten (mens, AI-criticus, automatische guardrail, of een technische storing zonder beslisser), zodat elke uitkomst traceerbaar en navraagbaar is.

### Flow
1. Producteigenaar opent de homepage en bekijkt de sectie 'Productcycli en onderzoekssessies'.
2. Elke cyclusrij toont naast de bestaande uitkomstbadge (geaccepteerd/afgekeurd/revise) een nieuwe, altijd zichtbare 'Beslist door'-badge met exact één van de vier vaste waarden.
3. Producteigenaar klikt op een cyclusrij om het detaildialoog te openen.
4. Het detaildialoog toont bovenin, direct onder de uitkomstbadge, dezelfde 'Beslist door'-waarde als in de rij (geen afwijkende of ontbrekende waarde).
5. Voor iteraties met losse stapknoppen (Criticus, Product owner, Onderzoeker, ...) toont het dialoog per stap ook het bijbehorende 'Beslist door'-label naast de bestaande vrije Reden-tekst; de Reden-tekst blijft ongewijzigd als aanvulling, niet als vervanging.
6. Bij een technische storing (zoals 'Workspace-publicatie tijdelijk niet beschikbaar') vult het systeem automatisch 'Technische storing — geen beslisser' in; dit veld is nooit leeg of null.
7. Een automatische validatietest (agent-uitvoerbaar) controleert voor elke cyclus dat het 'Beslist door'-veld aanwezig is, één van de vier toegestane waarden bevat, en in rij en dialoog identiek is.

### Wireframe

HOMEPAGE — sectie 'Productcycli en onderzoekssessies'
┌─────────────────────────────────────────────────────────────────┐
│ Cyclus shadow-hkh-autopilot-0003                                 │
│ [Badge: Afgekeurd]  [Badge: Beslist door: AI-criticus]  12:49 UTC│
│ >                                                                  │
├─────────────────────────────────────────────────────────────────┤
│ Cyclus shadow-hkh-autopilot-0002                                 │
│ [Badge: Fout]  [Badge: Beslist door: Technische storing —        │
│                 geen beslisser]                     11:02 UTC    │
│ >                                                                  │
├─────────────────────────────────────────────────────────────────┤
│ Cyclus shadow-hkh-autopilot-0001                                 │
│ [Badge: Geaccepteerd]  [Badge: Beslist door: Mens]   09:10 UTC   │
│ >                                                                  │
└─────────────────────────────────────────────────────────────────┘

DETAILDIALOOG (na klik op een rij)
┌─────────────────────────────────────────────────────────────────┐
│ Cyclus shadow-hkh-autopilot-0003                              [X]│
│ Uitkomst: Afgekeurd     Beslist door: AI-criticus                │
│ (i) Dit toont wat de uitkomst was, en wie/wat dit besliste;      │
│     niet elk onderliggend argument.                              │
│ ─────────────────────────────────────────────────────────────── │
│ Stap 1  Criticus            Beslist door: AI-criticus            │
│         Reden: Criticusoordeel REVISE geregistreerd...           │
│ Stap 2  Product owner       Beslist door: Mens                   │
│         Reden: Handmatige review, revisie goedgekeurd            │
│ Stap 3  Guardrail-check     Beslist door: Guardrail (automatisch)│
│         Reden: Automatische randgevalcontrole REJECTED+ACCEPT    │
│ ─────────────────────────────────────────────────────────────── │
│                                             [Sluiten]             │
└─────────────────────────────────────────────────────────────────┘

Elke '[Badge: Beslist door: ...]' heeft altijd zichtbare tekst (geen kleur-only indicator) en een uniek toegankelijkheidslabel, gescheiden van de uitkomstbadge, zodat schermlezers beide onafhankelijk kunnen aankondigen.

### Interactiehypotheses
- Voor 100% van de cycli en iteraties is het gestructureerde 'Beslist door'-veld aanwezig en bevat het exact één van de vier vaste waarden (Mens, AI-criticus, Guardrail (automatisch), Technische storing — geen beslisser); geen null, leeg of vrije tekst. Verifieerbaar via een geautomatiseerde datavalidatietest die alle API-responses van cyclus- en iteratiedata doorloopt.
- De 'Beslist door'-waarde in de cyclusrij van het overzicht komt voor elke cyclus exact overeen met de waarde in het bijbehorende detaildialoog. Verifieerbaar via een geautomatiseerde UI-test (Playwright + ariaSnapshot) die rij- en dialoogtekst vergelijkt voor alle zichtbare cycli.
- Wanneer een technische storing optreedt tijdens publicatie of verwerking, wordt het 'Beslist door'-veld automatisch en zonder menselijke tussenkomst gevuld met 'Technische storing — geen beslisser'. Verifieerbaar door een testharnas dat een storing simuleert (bijv. gefaalde workspace-publicatie in een testomgeving) en het resulterende API-veld controleert.
- Een schermlezergebruiker kan het 'Beslist door'-label onderscheiden van het uitkomstlabel zonder het dialoog te openen, omdat beide badges een uniek, expliciet toegankelijkheidslabel hebben. Verifieerbaar via geautomatiseerde ariaSnapshot/AX-tree-inspectie die controleert dat beide labels afzonderlijk als tekst worden aangekondigd.

### Toegankelijkheid
- Beide badges (uitkomst en 'Beslist door') zijn volledig bereikbaar en bedienbaar met Tab/Shift+Tab en Enter/Spatie, met een zichtbare focusindicator; geen muis-only interactie.
- De 'Beslist door'-waarde wordt als leesbare tekst blootgesteld aan de accessibility tree (Flutter semantics/ariaSnapshot), niet uitsluitend via kleur of icoon, zodat schermlezers de waarde correct aankondigen.
- Kleurcontrast van badge-tekst ten opzichte van de achtergrond voldoet aan WCAG AA (minimaal 4.5:1 voor normale tekst); geautomatiseerd controleerbaar met een contrastanalysetool (bijv. axe-core color-contrast-regel).
- De vier waarden van 'Beslist door' zijn elk uniek en ondubbelzinnig geformuleerd (geen afkortingen of iconen-only), zodat ze ook voorleesbaar en begrijpelijk zijn zonder visuele context.
- In het detaildialoog is de leesvolgorde voor schermlezers logisch: uitkomst, dan 'Beslist door', dan per-stap detail — getest via geautomatiseerde AX-tree-traversal in plaats van visuele volgorde.

### Privacy
- Het 'Beslist door'-veld gebruikt uitsluitend de vier vaste, geaggregeerde procescategorieën (Mens, AI-criticus, Guardrail (automatisch), Technische storing — geen beslisser); er wordt geen naam, e-mailadres of andere identificerende informatie van een individuele persoon opgeslagen of getoond bij de waarde 'Mens'.
- Het veld bevat uitsluitend operationele metadata over het eigen besluitvormingsproces van Product Factory (welk type actor besliste), en bevat geen gebruikers- of persoonsgegevens van andere producten zoals hkh-autopilot.
- Er wordt geen nieuwe dataverzameling van externe bronnen toegevoegd; het veld wordt afgeleid uit reeds bestaande interne proceslogica (wie/wat de stap uitvoerde), niet uit nieuwe tracking of monitoring van gebruikersgedrag.
- Bij technische storingen wordt expliciet 'geen beslisser' vastgelegd in plaats van een gok of foutieve toeschrijving aan een persoon of systeem, om onterechte verantwoordelijkheidstoewijzing te voorkomen.

## Kritische beoordeling

**Oordeel:** ACCEPT

Drie samenhangende, correct geketende kandidaten (bereken-waarde, overzicht-badge, detaildialoog) voor theme-product-factory-0002 (traceerbaarheid van wie of wat een beslissing nam). De set corrigeert expliciet en aantoonbaar een eerdere BLOCKING-kritiek door de foutieve aanname te verwijderen dat een voltooide AI-agentrolstap (bijvoorbeeld Product owner) gelijkstaat aan een menselijke beslissing, en verplicht de implementerende agent om dit eerst geautomatiseerd tegen echte data en broncode te verifieren en te documenteren in plaats van aan te nemen. De mapping is goed onderbouwd via reeds gepubliceerde, geverifieerde stories (candidates 41, 42, 44, 45 en 49). Alle drie kandidaten zijn presentatiewijzigingen op de bestaande frontend zonder backend-, database- of privacygevoelige impact, gebruiken uitsluitend vier geaggregeerde, niet-identificerende categorieen, en zijn volledig agent-uitvoerbaar via unit tests, Playwright, ariaSnapshot en axe-core zonder enige menselijke actie, accountaanmaak of externe toegang. Toegankelijkheid (uniek label, toetsenbordbedienbaarheid, WCAG AA-contrast, correcte leesvolgorde voor schermlezers) is expliciet als acceptatiecriterium opgenomen. Geen duplicaten met de eenentwintig reeds gepubliceerde kandidaten. Enkele niet-blokkerende aandachtspunten (mogelijk ongebruikte waarde Mens in de praktijk, lichte visuele verdichting die op gespannen voet staat met het aparte hierarchiethema) zijn door de kandidaten zelf al transparant benoemd als risico en vereisen geen herziening.
- **WARNING · SCOPE** — Kandidaat 0 documenteert zelf dat de waarde Mens mogelijk voor geen van de drie bestaande voorbeeldcycli ooit wordt teruggegeven omdat er geen verifieerbaar handmatig actiesignaal in de huidige data bestaat. Dit is een legitieme, transparant gerapporteerde bevinding, geen gebrek in de story, maar beperkt het praktische traceerbaarheidsnut totdat een toekomstige story een echt Mens-signaal toevoegt.
- **WARNING · CONSISTENCY** — De extra Beslist door badge in kandidaat 1 verdicht de cyclusrij visueel verder, wat op gespannen voet staat met het aparte, lopende hierarchiethema dat juist minder gelijkwaardige elementen op de homepage nastreeft. Dit risico is door de kandidaat zelf al benoemd en gemitigeerd door de badge compact en secundair te houden; geen wijziging vereist, wel iets om te monitoren.
- **INFO · CONSISTENCY** — Kandidaat 2 hangt voor consistentie volledig af van correct hergebruik, dus geen duplicatie, van classifyDecidedBy tussen rij en dialoog. Dit is als expliciet acceptatiecriterium en via dependsOn geborgd, dus er is geen actie nodig, maar het blijft de kritieke succesfactor voor deze story.

## Geaccepteerde storykandidaten

### Voeg pure functie toe die uit bestaande iteratiedata een van vier vaste 'Beslist door'-waarden afleidt, zonder AI-rolstappen als 'Mens' te labelen

_Sleutel: `bereken-beslist-door-waarde`_

In dashboard-frontend/lib/classification.dart wordt, naast de bestaande classifyIterationOutcome() (product-factory-4/22/25/45), een nieuwe pure, losstaande functie toegevoegd (bijv. classifyDecidedBy()) die op basis van reeds beschikbare, al opgehaalde iteratie- en stapdata (status, criticVerdict, errorMessage, en per-stap rolgegevens) exact één van vier vaste waarden retourneert: 'Mens', 'AI-criticus', 'Guardrail (automatisch)' of 'Technische storing — geen beslisser'.

Correctie t.o.v. de vorige versie (criticusfeedback, BLOCKING): de eerdere aanname dat een voltooide 'Product owner'-stap gelijkstaat aan 'Mens' wordt verwijderd. Reeds gepubliceerde kandidaat 37 documenteert expliciet dat Onderzoeker, Product owner, UX-ontwerp, Story writer en Criticus vijf AI-agentrollen zijn binnen dezelfde volledig autonome shadow-iteratiepipeline; een pipeline-rolstap is op zichzelf dus nooit bewijs van een menselijke beslissing.

De implementerende agent inspecteert eerst geautomatiseerd (a) de daadwerkelijke API-responses (/api/shadow-iterations, .../steps, .../artifacts) van de drie bestaande voorbeeldcycli (shadow-hkh-autopilot-0001/2/3) en (b) de broncode van elk dashboardbedieningselement dat een expliciete, buiten de agentpipeline om uitgevoerde actie van de eigenaar registreert (bijv. pauzeren/hervatten of een override-/goedkeuringsactie), om vast te stellen of een concreet, verifieerbaar signaal van menselijke actie in het datamodel bestaat. Deze bevinding — inclusief of zo'n signaal op dit moment wél of niet in de bestaande data voorkomt — wordt als codecommentaar/documentatie vastgelegd vóórdat de logica wordt geïmplementeerd.

Mapping, uitsluitend gebaseerd op geverifieerde signalen: FAILED-status zonder guardrail-signaal (product-factory-45) => 'Technische storing — geen beslisser'; criticVerdict=='ACCEPT' met iteratiestatus 'REJECTED' (product-factory-42/44) => 'Guardrail (automatisch)'; NEEDS_REVISION/REJECTED/ACCEPTED met aanwezig criticus-artefact/criticVerdict (product-factory-41/49) => 'AI-criticus'. 'Mens' wordt uitsluitend toegekend wanneer het gedocumenteerde, verifieerbare signaal van een expliciete handmatige dashboardactie aanwezig is bij die specifieke iteratie/cyclus — nooit op basis van de aanwezigheid van een agentrolstap. Blijkt uit het onderzoek dat zo'n menselijk-actiesignaal in de huidige architectuur nergens in de bestaande data voorkomt, dan documenteert de agent dit expliciet en retourneert de functie voor de drie voorbeeldcycli nooit 'Mens'; de waarde blijft een geldige, ondersteunde retourwaarde voor toekomstige data. Voor elk overig geval dat niet eenduidig op bestaande data is te herleiden, legt de agent een apart, gedocumenteerd deterministisch standaardgeval vast zodat de functie nooit null of een vijfde waarde teruggeeft.

Dit is een pure functie zonder UI-wijziging, zonder nieuw API-veld en zonder backend-wijziging: uitsluitend bestaande, al opgehaalde data wordt gebruikt.

**Acceptatiecriteria**
- Een geautomatiseerde unit-testsuite roept classifyDecidedBy() aan met de daadwerkelijke, opgehaalde iteratiedata van shadow-hkh-autopilot-0001, -0002 en -0003 en verifieert dat elk resultaat exact één van de vier vaste toegestane waarden is, gedocumenteerd en herleidbaar naar de vastgelegde mapping.
- Een geautomatiseerde regressietest bevestigt expliciet dat voor alle drie voorbeeldcycli een voltooide 'Product owner'-stap (of enige andere agentrolstap: Onderzoeker, UX-ontwerp, Story writer, Criticus) op zichzelf nooit resulteert in de waarde 'Mens', met verwijzing naar product-factory-37 als bron dat dit AI-rollen zijn.
- Codecommentaar/documentatie bij de functie beschrijft expliciet, met verwijzing naar de geïnspecteerde echte API-velden en dashboardbedieningselementen, welk concreet, verifieerbaar signaal wél tot 'Mens' leidt, en registreert expliciet of dat signaal in de huidige databron voorkomt.
- Een geautomatiseerde test bevestigt dat de functie voor de drie bestaande voorbeeldcycli, gegeven het geconstateerde ontbreken (of aanwezig zijn) van een menselijk-actiesignaal, consistent het gedocumenteerde gedrag volgt (bijv. nooit 'Mens' teruggeeft als dat signaal ontbreekt in alle drie cycli).
- Een geautomatiseerde test toont aan dat de functie nooit null, een lege string of een vijfde waarde retourneert, ook niet voor input die geen enkel bekend patroon matcht (het gedocumenteerde deterministische standaardgeval).
- Een geautomatiseerde test confirmeert dat het FAILED-scenario van shadow-hkh-autopilot-0002 (Foutreden 'Workspace-publicatie tijdelijk niet beschikbaar') resulteert in 'Technische storing — geen beslisser'.
- Een geautomatiseerde test bevestigt dat de functie puur is: gelijke input levert bij herhaalde aanroepen altijd exact dezelfde output, zonder netwerkaanroepen of neveneffecten.
- Statische analyse/lint bevestigt dat de nieuwe functie geen bestaande classifyIterationOutcome()-logica of bestaand badge-gedrag wijzigt (geen regressie in reeds gepubliceerde classificatiecategorieën).

Bronnen: [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/factory/functional-spec.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/factory/functional-spec.md), [https://www.numeric.io/blog/ai-audit-trail](https://www.numeric.io/blog/ai-audit-trail)

Risico's: Als geen enkel bestaand dashboardbedieningselement een verifieerbaar handmatig-actiesignaal registreert, blijft 'Mens' in de praktijk (voorlopig) ongebruikt; dit moet expliciet als bevinding worden gedocumenteerd in plaats van als tekortkoming behandeld te worden, zodat vervolgstories hier niet ten onrechte op vertrouwen., Zonder gedeeld gebruik van deze ene functie in latere stories (overzicht en detaildialoog) kan de 'Beslist door'-waarde alsnog inconsistent worden weergegeven; dit wordt geadresseerd in de vervolgstories die hierop dependen.

### Toon een aparte, altijd zichtbare 'Beslist door'-badge naast de bestaande uitkomstbadge in het cyclusoverzicht

_Sleutel: `toon-beslist-door-badge-overzicht`_

Bouwt voort op de in kandidaat 'bereken-beslist-door-waarde' toegevoegde pure functie classifyDecidedBy(). Deze story voegt op de homepage-sectie 'Productcycli en onderzoekssessies' (dashboard-frontend/lib/main.dart) per cyclusrij een tweede, altijd zichtbare badge toe naast de bestaande ClassificationBadge voor de uitkomst (product-factory-22/25/34/45), met de tekst 'Beslist door: <waarde>' waarbij <waarde> exact het resultaat van classifyDecidedBy() is — deze story herberekent de waarde nooit zelf en bevat geen eigen mappinglogica. De nieuwe badge hergebruikt het bestaande, toegankelijke badge-component-patroon (kleurcodering + tekst, geen kleur-only indicator) maar krijgt een eigen, van de uitkomstbadge onderscheidbaar kleurenpaar en een uniek toegankelijkheidslabel, zodat schermlezers beide badges onafhankelijk van elkaar aankondigen. De wijziging is een presentatielaag-toevoeging bovenop reeds beschikbare data (geen nieuw API-veld, geen backend-wijziging) en raakt geen andere homepage-secties, geen andere producten en geen bestaande badge-logica.

**Acceptatiecriteria**
- Een geautomatiseerde Playwright/ariaSnapshot-test op de acceptatieomgeving bevestigt dat elke zichtbare cyclusrij voor shadow-hkh-autopilot-0001, -0002 en -0003 een 'Beslist door: <waarde>'-badge toont naast de bestaande uitkomstbadge, met <waarde> gelijk aan het resultaat van classifyDecidedBy() voor die iteratie.
- Een geautomatiseerde AX-tree/ariaSnapshot-test bevestigt dat de nieuwe badge en de bestaande uitkomstbadge elk een uniek, afzonderlijk toegankelijkheidslabel hebben en dus onafhankelijk door een schermlezer worden aangekondigd.
- Een geautomatiseerde contrastanalyse (bijv. axe-core color-contrast-regel) bevestigt dat de tekst van de nieuwe badge minimaal WCAG AA (4.5:1) contrast heeft ten opzichte van de achtergrond.
- Een geautomatiseerde test bevestigt dat de badge volledig met Tab/Shift+Tab bereikbaar is en een zichtbare focusindicator toont, zonder muis-only interactie.
- Een geautomatiseerde regressietest bevestigt dat de bestaande uitkomstbadge (tekst, kleur, gedrag) ongewijzigd blijft en dat geen andere homepage-sectie (Roadmap, Overleggen, Workspace, Storywachtrij) door deze wijziging is aangeraakt.
- Een geautomatiseerde test bevestigt dat de nieuwe badge voor alle drie bestaande voorbeeldcycli altijd tekst toont (nooit leeg, nooit 'null'), en dat de rij zelf geen eigen 'Mens'/rolstap-mapping bevat maar uitsluitend classifyDecidedBy() aanroept.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/factory/functional-spec.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/factory/functional-spec.md), [https://eucalipse.com/articles/ai-agent-approval-queue-human-in-the-loop](https://eucalipse.com/articles/ai-agent-approval-queue-human-in-the-loop)

Afhankelijkheden (candidateKey): bereken-beslist-door-waarde (binnen deze batch herkend als: bereken-beslist-door-waarde)

Risico's: Een extra badge per rij verdicht de al drukke cyclusrij visueel, wat op gespannen voet kan staan met het lopende hiërarchiethema (theme-product-factory-0001); de badge moet compact en secundair aan de uitkomstbadge blijven om dit te beperken., Als de rij-implementatie de waarde zelf herberekent in plaats van de gedeelde classifyDecidedBy()-functie te hergebruiken, ontstaat een risico op afwijking t.o.v. het detaildialoog dat in de vervolgstory wordt aangepakt.

### Toon 'Beslist door' in het detaildialoog, consistent met het overzicht, en borg dit geautomatiseerd

_Sleutel: `toon-beslist-door-detaildialoog-consistent`_

Bouwt voort op 'bereken-beslist-door-waarde' en 'toon-beslist-door-badge-overzicht'. In IterationSessionDialog (dashboard-frontend/lib/main.dart) wordt, direct onder de al aanwezige uitkomstbadge (product-factory-34) en boven het bestaande Reden-/Foutreden-blok (product-factory-33/41/44/47/49), dezelfde 'Beslist door: <waarde>'-badge getoond als in de cyclusrij, gevoed door exact dezelfde classifyDecidedBy()-functie en exact dezelfde iteratiedata die het dialoog al ontvangt — geen aparte berekening en geen eigen 'Mens'/rolstap-mapping in deze story. Voor iteraties met losse stapknoppen/stapresultaten (Criticus, Product owner, Onderzoeker, ...) toont het dialoog per stap optioneel een kort 'Beslist door'-label naast de reeds bestaande Reden-tekst van die stap, opnieuw uitsluitend afgeleid via classifyDecidedBy(), zonder de bestaande Reden-tekst te vervangen. Deze story voegt daarnaast een geautomatiseerde consistentietest toe die voor elke iteratie controleert dat de 'Beslist door'-waarde in de cyclusrij en in het detaildialoog identiek zijn. De wijziging blijft beperkt tot de presentatielaag van IterationSessionDialog; geen nieuw API-veld, geen backend-wijziging, geen wijziging aan HKH Autopilot.

**Acceptatiecriteria**
- Een geautomatiseerde Playwright/ariaSnapshot-test opent het detaildialoog voor shadow-hkh-autopilot-0001, -0002 en -0003 en bevestigt dat de getoonde 'Beslist door'-waarde daar exact overeenkomt met de waarde in de bijbehorende cyclusrij van het overzicht.
- Een geautomatiseerde test bevestigt dat de 'Beslist door'-badge in het dialoog direct onder de uitkomstbadge staat, vóór het Reden-/Foutreden-blok, en niet de bestaande Reden-tekst overschrijft of verwijdert.
- Een geautomatiseerde test bevestigt dat het dialoog en de rij dezelfde classifyDecidedBy()-functie en dezelfde onderliggende data gebruiken (bijv. door te controleren dat een wijziging in de invoerdata voor beide plekken tegelijk tot dezelfde nieuwe waarde leidt in een geïsoleerde testomgeving).
- Een geautomatiseerde AX-tree-test bevestigt een logische leesvolgorde voor schermlezers: uitkomst, dan 'Beslist door', dan per-stap detail.
- Voor iteraties met meerdere stappen bevestigt een geautomatiseerde test dat elk stapresultaat met een eigen Reden-tekst nu ook een 'Beslist door'-label toont dat uitsluitend via classifyDecidedBy() is afgeleid (geen zelfstandige 'Product owner => Mens'-aanname in deze weergavelaag), zonder de bestaande Reden-tekst van die stap te wijzigen.
- Een geautomatiseerde regressietest bevestigt dat bestaande, reeds gepubliceerde dialoogfunctionaliteit (Foutreden-blok, Reden-blok, roltegels, technische-details-toggle) ongewijzigd blijft werken.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart), [https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/factory/functional-spec.md](https://raw.githubusercontent.com/robbertvdzon/product-factory/main/docs/factory/functional-spec.md), [https://www.numeric.io/blog/ai-audit-trail](https://www.numeric.io/blog/ai-audit-trail)

Afhankelijkheden (candidateKey): bereken-beslist-door-waarde, toon-beslist-door-badge-overzicht (binnen deze batch herkend als: bereken-beslist-door-waarde, toon-beslist-door-badge-overzicht)

Risico's: Als de per-stap 'Beslist door'-labels te veel visuele ruimte innemen naast de al bestaande Reden-teksten per stap, kan het dialoog voller ogen; de implementatie moet dit compact houden (label, geen extra alinea)., Consistentie tussen rij en dialoog is alleen gegarandeerd als beide daadwerkelijk dezelfde gedeelde functie en databron gebruiken; hergebruik van code (niet dupliceren) is essentieel om regressie te voorkomen.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
