---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0031
date: 2026-08-09
status: approved
sources:
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl
  - https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md
  - https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md
  - https://api.github.com/repos/robbertvdzon/hkh-autopilot/git/trees/main?recursive=1
  - https://netwerkdigitaalerfgoed.nl/wat-we-doen/
  - https://netwerkdigitaalerfgoed.nl/versnellen-2026/
  - https://www.kb.nl/over-ons/diensten/delpher
  - https://www.delpher.nl/over-delpher/delpher-open-krantenarchief/wat-zit-er-in-het-delpher-open-krantenarchief
  - https://www.deverhalenvangroningen.nl/
  - https://www.deverhalenvangroningen.nl/verhalenkaart
---
# Productcyclus 31

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Iteratie-28 onderzoek bevestigt en verscherpt de bevinding uit iteratie 27: na 27+ iteraties bestaat hkh-autopilot backend-technisch vrijwel uitsluitend uit AVG/privacyclassificatie-plumbing (GEDCOM RESN, FamilySearch 110/95-regel, NL-openbaarheidstermijnen) en fail-closed linkvalidatie tegen precies één externe bron (archieven.nl/Noord-Hollands Archief), terwijl de productvisie draait om laagdrempelige ontdekking van Heemskerkse geschiedenis in verbinding met bredere bronnen (archieven, musea, beeldbanken, kranten, kaarten). Directe inspectie van de draaiende acceptatieomgeving (2026-08-09, via Playwright-screenshots omdat WebFetch/websearch een HTTP 403 bot-blokkade geven) toont dat de gebruikersapp letterlijk de tekst toont "Ontdek de geschiedenis van Heemskerk vanuit een vraag, plek, persoon of gebeurtenis" maar geen enkel zoek-, filter- of ontdekelement bevat: alleen een titel, een link naar de productvisiepagina, een servicestatusbadge en een statische nieuwsfeed met 5 berichten. Het beheergedeelte bevat alleen een nieuwsbericht-publicatieformulier en een record-intakeformulier voor precies één lokaal record tegelijk — er is geen enkele UI om de reeds gebouwde privacyclassificatie- of externe-verificatieresultaten te bekijken, te doorzoeken of te beoordelen, ondanks dat die backend-modules al 8 stories/PR's hebben gekost. De belofte uit de visie (vraag/plek/persoon/gebeurtenis-gedreven ontdekking, meerstemmigheid, verbinding met de wereld daarbuiten) staat dus lijnrecht tegenover wat een bezoeker vandaag daadwerkelijk kan doen. Extern onderzoek naar Netwerk Digitaal Erfgoed, Delpher en De Verhalen van Groningen bevestigt dat er reële, publiek toegankelijke Nederlandse infrastructuur en concrete UX-voorbeelden bestaan om deze kloof te dichten zonder dat hkh-autopilot zelf een archief hoeft te worden.

### Gebruikersapp toont geen enkele zoek- of ontdekfunctie ondanks expliciete belofte daartoe

Playwright-screenshot van https://hkh-autopilot-acceptance.vdzonsoftware.nl (2026-08-09) toont de tekst 'Ontdek de geschiedenis van Heemskerk vanuit een vraag, plek, persoon of gebeurtenis. Verken betrouwbare historische bronnen en hun verbindingen met de wereld daarbuiten.' direct onder de titel. Onder die tekst staat alleen een knop 'Lees onze productvisie', een servicestatusbadge en een statische lijst van 5 nieuwsberichten. Er is geen zoekveld, geen filter op plek/persoon/gebeurtenis, geen navigatie naar andere pagina's en geen enkele link naar een externe bron. De volledige pagina (fullPage-screenshot, viewport 1280×3000) bevestigt dat dit de complete inhoud van de homepage is.

Bronnen: [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl)

### Beheeromgeving heeft geen UI voor de reeds gebouwde privacy- en verificatiemodules

Playwright-screenshot van https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl (2026-08-09) toont na 'Beheerder geverifieerd' precies twee formulieren: 'Nieuw bericht' (nieuwsfeed publiceren) en 'Nieuwe record-intake' (één lokaal collectierecord aanmaken met verplichte velden zoals rechtenstatus, privacyclassificatie en optionele externe conceptkoppeling). Er is geen enkel scherm om bestaande records, hun privacyclassificatie-uitkomst (Blocked/Published) of hun externe-verificatiestatus (archieven.nl-match, licentiestatus) te bekijken, te doorzoeken of handmatig te beoordelen — terwijl deze modules (privacyclassification, externalverification, linkdossier) volgens de broncode al het grootste deel van de backend vormen.

Bronnen: [https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl)

### Repository bevestigt: 27+ iteraties vrijwel uitsluitend backend-plumbing, frontend ongewijzigd sinds bootstrap

De bestandsstructuur van backend/src/main/kotlin/nl/vdzon/hkh/ bevat de modules auth, externalverification, linkdossier, news, previewdata, privacyclassification, recordintake en system — vrijwel alle met uitgebreide test-suites. frontend/lib/ bevat daarentegen slechts backend_client.dart, backend_status.dart, latest_news.dart, product_vision_page.dart, self_update_prompt.dart en update_checker.dart: geen enkel bestand voor zoeken, filteren, entiteiten (persoon/plek/gebeurtenis) of het tonen van externe bronnen. docs/factory/functional-spec.md bevestigt expliciet dat 'storage, REST-endpoints, beheerinterface en daadwerkelijke publicatieworkflows' en 'andere externe archieven dan het Noord-Hollands Archief-patroon' buiten scope vallen.

Bronnen: [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md), [https://api.github.com/repos/robbertvdzon/hkh-autopilot/git/trees/main?recursive=1](https://api.github.com/repos/robbertvdzon/hkh-autopilot/git/trees/main?recursive=1)

### Netwerk Digitaal Erfgoed biedt in 2026 concrete linked-data-infrastructuur om lokale collecties aan landelijke bronnen te koppelen

Netwerk Digitaal Erfgoed voert in 2026 de Nationale Strategie Digitaal Erfgoed uit met twee focusthema's: 'Meerstemmigheid' (verhalen van ondervertegenwoordigde groepen, community-archieven) en 'Verbonden erfgoeddata' (van losse datasets naar bruikbare apps/zoekfuncties via linked data, API's en gezamenlijke serviceplatforms). Het netwerk biedt trainingen, hackathons en collegagroepen voor erfgoedinstellingen die hun collectie willen ontsluiten via duurzame identifiers, een gedeeld termennetwerk en linked open data — precies de infrastructuur die nodig is om Heemskerkse bronnen te verbinden met archieven, musea en beeldbanken daarbuiten, zoals de productvisie beschrijft. Er is geen specifieke licentie-informatie gevonden op de geraadpleegde pagina; voor gebruiksrechten verwijst de site naar info@netwerkdigitaalerfgoed.nl.

Bronnen: [https://netwerkdigitaalerfgoed.nl/wat-we-doen/](https://netwerkdigitaalerfgoed.nl/wat-we-doen/), [https://netwerkdigitaalerfgoed.nl/versnellen-2026/](https://netwerkdigitaalerfgoed.nl/versnellen-2026/)

### Delpher biedt 130 miljoen doorzoekbare krantenpagina's (1618-2005), maar zonder duidelijk gedocumenteerde publieke API

Delpher (beheerd door de KB, nationale bibliotheek) geeft gratis toegang tot ruim 130 miljoen gedigitaliseerde pagina's uit Nederlandse kranten, boeken en tijdschriften uit Nederland, Nederlands-Indië, de Antillen, Amerika en Suriname. Dit is direct relevant voor het 'kranten'-brontype dat de productvisie noemt maar dat backend-technisch nog volledig onaangeroerd is. Zoekresultaten bevestigen wel de wens vanuit digital humanities-onderzoekers voor API-toegang tot metadata/OCR, maar geven geen concrete, direct geraadpleegde API-documentatie — dit is dus een kans die nader technisch onderzoek vereist voordat een koppeling haalbaar is.

Bronnen: [https://www.kb.nl/over-ons/diensten/delpher](https://www.kb.nl/over-ons/diensten/delpher), [https://www.delpher.nl/over-delpher/delpher-open-krantenarchief/wat-zit-er-in-het-delpher-open-krantenarchief](https://www.delpher.nl/over-delpher/delpher-open-krantenarchief/wat-zit-er-in-het-delpher-open-krantenarchief)

### 'De Verhalen van Groningen' toont een concreet, werkend voorbeeld van plek-gedreven ontdekking voor regionale geschiedenis

Het platform 'De Verhalen van Groningen' biedt een interactieve verhalenkaart waarmee bezoekers verhalen kunnen ontdekken op locatie: zoeken in de eigen regio, rond een vakantiebestemming, of vrij rondzwerven tot een verhaal 'je vindt'. Verhalen komen uit de hele provincie en gebruikers kunnen eigen verhalen toevoegen. Dit is een direct vergelijkbaar Nederlands precedent voor de 'plek'-dimensie uit de HKH-productvisie ('vanuit een vraag, plek, persoon of gebeurtenis') en toont dat een kaartgedreven ontdekinterface voor lokale geschiedenis technisch en organisatorisch haalbaar is gebleken.

Bronnen: [https://www.deverhalenvangroningen.nl/](https://www.deverhalenvangroningen.nl/), [https://www.deverhalenvangroningen.nl/verhalenkaart](https://www.deverhalenvangroningen.nl/verhalenkaart)

### Huidige applicatie

**Doel:** hkh-autopilot is een autonoom ontwikkelde vergelijkingsversie van de HKH-app (Historische Kring Heemskerk), bedoeld om de geschiedenis van Heemskerk toegankelijk te maken door lokale bronnen te verbinden met bredere historische collecties (archieven, musea, beeldbanken, kranten, kaarten) uit Noord-Holland, Nederland en daarbuiten. Doelgroep: mensen die vanuit een vraag, plek, persoon of gebeurtenis de geschiedenis van Heemskerk willen ontdekken, zonder vooraf te weten waar informatie is opgeslagen (volgens docs/productvisie.md en de tekst op de homepage van de acceptatieomgeving).

**Wat ontbreekt:**
- De gebruikersapp bevat geen enkele zoek-, filter- of ontdekfunctie, terwijl de homepage-tekst zelf expliciet 'ontdek vanuit een vraag, plek, persoon of gebeurtenis' belooft; alleen een statische nieuwsfeed en een link naar de productvisie zijn aanwezig (bevestigd via live screenshot, 2026-08-09).
- Er is precies één externe bron gekoppeld (archieven.nl/Noord-Hollands Archief, alleen voor verificatie, niet voor ontdekking); kranten, musea, beeldbanken en kaarten uit de productvisie zijn nog volledig onaangeroerd.
- De beheeromgeving biedt geen enkele UI om de reeds gebouwde privacyclassificatie- of externe-verificatieresultaten in te zien, te doorzoeken of te beoordelen — deze bestaan alleen als backend-logica/tests, niet als bruikbaar beheerinstrument.
- 27+ iteraties zijn vrijwel volledig besteed aan backend-plumbing (AVG/privacyclassificatie voor genealogische GEDCOM-records, fail-closed linkvalidatie) zonder dat dit ooit zichtbaar is geworden in een gebruikersgerichte functie.
- Record-intake is beperkt tot precies één lokaal record per keer via een handmatig formulier; er is geen bulk-import, geen GEDCOM-volledige integratie (alleen synthetische testfixtures) en geen zichtbare workflow van intake naar daadwerkelijke publicatie.
- Meerstemmigheid (een kernprincipe uit de productvisie: 'verschillende en tegenstrijdige verhalen mogen naast elkaar bestaan') is nergens in de huidige app terug te zien; er is geen enkel mechanisme om meerdere perspectieven op eenzelfde persoon/plek/gebeurtenis te tonen.

### Verbetermogelijkheden

- Bouw een minimale, echte ontdekfunctie op de homepage (bijv. een zoekveld of een klein aantal klikbare entiteiten: plekken, personen, gebeurtenissen) die daadwerkelijk resultaten toont uit de al bestaande news/record-data, zodat de kloof tussen belofte ('ontdek vanuit een vraag, plek, persoon of gebeurtenis') en werkelijkheid wordt gedicht — dit hoeft geen externe koppeling te vereisen om al waarde te leveren.
- Geef beheerders zichtbaarheid op de reeds gebouwde privacyclassificatie- en externe-verificatiemodules (bijv. een overzichtslijst van records met hun classificatie- en verificatiestatus), zodat het geïnvesteerde backend-werk ook daadwerkelijk bruikbaar en controleerbaar wordt, in lijn met het productprincipe 'Betrouwbaar' (herleidbare antwoorden).
- Onderzoek een concrete, smalle koppeling met één aanvullende externe bron buiten archieven.nl (bijv. Delpher voor kranten of het Netwerk Digitaal Erfgoed-termennetwerk voor gedeelde begrippen/plaatsnamen) om de 'verbonden'-belofte van de visie voor het eerst buiten genealogische AVG-context waar te maken.
- Voeg een minimale manier toe om meerdere/tegenstrijdige verhalen over dezelfde persoon, plek of gebeurtenis naast elkaar te tonen, zodat het productprincipe 'Meerstemmig' niet alleen op papier bestaat.
- Overweeg een plek-gedreven interface (kaart of lijst van locaties) naar het voorbeeld van De Verhalen van Groningen, als laagdrempelige eerste stap richting de 'plek'-dimensie uit de productvisie, gebruikmakend van reeds aanwezige recordgegevens (bijv. 'Kerkweg', 'Slot Assumburg' uit de huidige nieuwsberichten).

### Inspiratiebronnen

- [De Verhalen van Groningen (Verhalenkaart)](https://www.deverhalenvangroningen.nl/verhalenkaart) — Werkend Nederlands voorbeeld van plek-gedreven ontdekking van regionale geschiedenis via een interactieve kaart; direct toepasbaar op de 'plek'-dimensie uit de HKH-productvisie en toont dat dit haalbaar is voor een vergelijkbare regionale erfgoedorganisatie.
- [Netwerk Digitaal Erfgoed — Verbonden Erfgoeddata / Termennetwerk](https://netwerkdigitaalerfgoed.nl/wat-we-doen/) — Landelijke infrastructuur (linked open data, duurzame identifiers, gedeeld termennetwerk) specifiek gebouwd om lokale erfgoedcollecties zoals die van Heemskerk te verbinden met archieven, musea en beeldbanken elders in Nederland — precies de kernbelofte van de HKH-productvisie.
- [Delpher (KB) — historisch krantenarchief](https://www.delpher.nl/) — Grootschalig, gratis doorzoekbaar Nederlands krantenarchief (1618-2005); direct relevant voor het nog volledig onaangeroerde 'kranten'-brontype uit de productvisie en een concreet kandidaat-doel voor een toekomstige externe koppeling.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl) | 2026-08-09 | Standing acceptatieomgeving met nepdata, geen productie; geen expliciete licentie van toepassing op de geraadpleegde inhoud zelf (dummy-content) | Draaiende gebruikersapp; enige manier om de daadwerkelijke huidige gebruikerservaring te beoordelen i.p.v. alleen documentatie |
| [bron](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl) | 2026-08-09 | Standing acceptatieomgeving met nepdata, geen productie; geen expliciete licentie van toepassing | Draaiende beheeromgeving; nodig om te beoordelen welke backend-functionaliteit wel/niet via UI bruikbaar is gemaakt voor beheerders |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md) | 2026-08-09 | Publieke GitHub-repository (robbertvdzon/hkh-autopilot), geen expliciete OSS-licentie gedeclareerd volgens GitHub API (license: null) | Officiële projectdocumentatie over architectuur en huidige featureset |
| [bron](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md) | 2026-08-09 | Publieke GitHub-repository, geen expliciete OSS-licentie gedeclareerd | Functionele specificatie die scope en expliciete out-of-scope-items van het product vastlegt |
| [bron](https://api.github.com/repos/robbertvdzon/hkh-autopilot/git/trees/main?recursive=1) | 2026-08-09 | Publieke GitHub API-data over een publieke repository, geen persoonsgegevens | Volledige bestandsstructuur om te bevestigen welke modules wel/niet bestaan in backend en frontend |
| [bron](https://netwerkdigitaalerfgoed.nl/wat-we-doen/) | 2026-08-09 | Publieke website van een Nederlandse non-profit netwerkorganisatie (onderdeel Nationale Strategie Digitaal Erfgoed); expliciete gebruiksrechten van content niet vermeld op de pagina zelf, nog onbekend | Beschrijft de landelijke infrastructuur (linked data, termennetwerk, duurzame identifiers) die relevant is voor het verbinden van Heemskerkse bronnen met andere Nederlandse erfgoedcollecties, zoals de productvisie vereist |
| [bron](https://netwerkdigitaalerfgoed.nl/versnellen-2026/) | 2026-08-09 | Publieke website, gebruiksrechten van content niet expliciet vermeld, nog onbekend | Actuele 2026-programma-informatie over het aantal deelnemende erfgoedinstellingen en trainingsaanbod |
| [bron](https://www.kb.nl/over-ons/diensten/delpher) | 2026-08-09 | Publieke website van de Koninklijke Bibliotheek (Nederlandse nationale bibliotheek, publieke instelling); Delpher-content is gratis raadpleegbaar, exacte hergebruikslicentie per bron kan variëren en is niet op deze pagina gespecificeerd | Officiële bron over omvang en toegankelijkheid van het Nederlandse historische krantenarchief, relevant voor het 'kranten'-brontype uit de productvisie |
| [bron](https://www.delpher.nl/over-delpher/delpher-open-krantenarchief/wat-zit-er-in-het-delpher-open-krantenarchief) | 2026-08-09 | Publieke website van Delpher/KB; specifiek 'open krantenarchief' suggereert vrij hergebruik maar exacte licentievoorwaarden zijn niet direct op deze pagina bevestigd, nog onbekend | Beschrijft welk deel van de krantencollectie specifiek als 'open' is gemarkeerd, relevant voor haalbaarheid van een toekomstige koppeling |
| [bron](https://www.deverhalenvangroningen.nl/) | 2026-08-09 | Publieke website van een regionaal erfgoedplatform (provincie Groningen); contentrechten niet expliciet vermeld op de geraadpleegde pagina, nog onbekend | Vergelijkbaar Nederlands platform dat plek-gedreven ontdekking van lokale geschiedenis daadwerkelijk heeft gerealiseerd, direct bruikbaar als inspiratiebron voor de 'plek'-dimensie uit de HKH-visie |
| [bron](https://www.deverhalenvangroningen.nl/verhalenkaart) | 2026-08-09 | Publieke website, contentrechten niet expliciet vermeld, nog onbekend | Specifieke interactieve-kaart-functionaliteit die als concreet UX-voorbeeld kan dienen voor een toekomstige HKH-ontdekfunctie |

## Productbeslissing

Bouw een minimale, echt werkende ontdekfunctie op de homepage van hkh-autopilot die de bestaande belofte ('ontdek vanuit een vraag, plek, persoon of gebeurtenis') voor het eerst waarmaakt, uitsluitend op basis van reeds aanwezige lokale data (nieuwsberichten en record-intake). Concreet: leid uit de bestaande nieuws- en recordgegevens entiteiten af (plek, persoon, gebeurtenis) en toon deze als klikbare/doorzoekbare ingangen op de homepage; bij selectie tonen deze de gerelateerde bestaande items mét herleidbare bronvermelding (rechtenstatus/herkomst, reeds verplichte velden bij record-intake). Geen nieuwe externe bronkoppeling, geen kaartinfrastructuur en geen beheer-dashboard voor privacy-/verificatiedata in deze stap — die volgen pas in een latere fase, nadat deze basis staat en er voldoende entiteiten/verhalen zijn om meerstemmigheid en plek-gedreven kaartweergave zinvol te maken. Dit is volledig uitvoerbaar door Product Factory- en Software Factory-agents zonder extern toegangstoken, omdat het enkel bestaande, reeds gepubliceerde interne data hergebruikt.

**Waarom:** Na 27+ iteraties is de grootste, best onderbouwde bevinding dat de backend vrijwel volledig bestaat uit AVG/privacy-plumbing en verificatie tegen precies één externe bron, terwijl de gebruikersapp — bevestigd via directe inspectie van de acceptatieomgeving — geen enkele zoek-, filter- of ontdekfunctie bevat, ondanks dat de homepage dit letterlijk belooft. Dit is de meest missie-kritieke kloof: zonder een zichtbare ontdekervaring kan geen enkel productprincipe (Verbonden, Meerstemmig, Toegankelijk, Nieuwsgierig) waargemaakt worden, hoe goed de onderliggende privacy-logica ook is. Externe bronnen zoals Delpher en Netwerk Digitaal Erfgoed bieden relevante toekomstige infrastructuur, maar rechten en API-toegang zijn nog onduidelijk, dus een directe koppeling nu zou een niet-noodzakelijk risico en mogelijk een extern toegangstoken vereisen. Door eerst een kleine, zelfstandig bouwbare ontdekfunctie op bestaande lokale data te realiseren, wordt de belofte-werkelijkheid-kloof gedicht zonder externe afhankelijkheden, en ontstaat de basis waarop latere, grotere stappen (kaartgedreven plek-ontdekking, meerstemmigheid, externe koppelingen) logisch kunnen voortbouwen.

### Prioriteiten
- Sluit de kloof tussen de belofte 'ontdek vanuit een vraag, plek, persoon of gebeurtenis' en de huidige statische homepage door een echte, minimale ontdekfunctie te bouwen.
- Gebruik voor deze eerste ontdekfunctie uitsluitend reeds aanwezige lokale data (nieuws, record-intake); geen nieuwe externe bronkoppeling in deze stap.
- Behoud herleidbaarheid naar bron per getoond item, in lijn met het productprincipe 'Betrouwbaar'.
- Stel externe koppelingen (Delpher, Netwerk Digitaal Erfgoed) uit tot rechten en API-toegang concreet zijn onderzocht.
- Stel kaartgedreven plek-ontdekking en meerstemmigheid uit tot een latere fase, na een werkende basis-ontdekfunctie.

### Besluiten
- **Bouw als eerstvolgende stap een minimale, echt werkende ontdekfunctie op de homepage van hkh-autopilot (bijv. klikbare/doorzoekbare entiteiten voor plek, persoon en gebeurtenis) die daadwerkelijk resultaten toont, in plaats van verder te investeren in nieuwe backend privacy-/verificatie-plumbing of een nieuwe externe bronkoppeling.** — De homepage belooft expliciet 'Ontdek de geschiedenis van Heemskerk vanuit een vraag, plek, persoon of gebeurtenis', maar bevat volgens live-inspectie alleen een titel, een link naar de productvisie, een statusbadge en een statische nieuwsfeed van 5 berichten — geen enkel zoek-, filter- of ontdekelement. Dit is de grootste kloof tussen missie/visie en werkelijkheid na 27+ iteraties.
- **Baseer deze eerste ontdekfunctie uitsluitend op reeds aanwezige lokale data (nieuwsberichten, record-intake) en niet op een nieuwe externe bronkoppeling.** — Delpher heeft geen duidelijk gedocumenteerde publieke API en Netwerk Digitaal Erfgoed vermeldt geen expliciete gebruiksrechten op de geraadpleegde pagina's; een externe koppeling nu zou het risico op een niet te vermijden extern toegangstoken en onduidelijke rechten introduceren, wat een kleine, zelfstandig uitvoerbare stap in de weg staat.
- **Zorg dat elk getoond ontdekresultaat herleidbaar blijft tot zijn bron (bestaande velden zoals rechtenstatus en herkomst uit de record-intake), zodat het productprincipe 'Betrouwbaar' ook in deze minimale versie geldt.** — De functional-spec en de beheeromgeving laten zien dat rechtenstatus en privacyclassificatie al verplichte velden zijn bij record-intake; deze bestaande gegevens kunnen direct hergebruikt worden om herleidbaarheid te tonen zonder nieuwe backend-scope.
- **Stel het bouwen van een plek-gedreven kaartinterface (naar voorbeeld van De Verhalen van Groningen) en van meerstemmigheid (tegenstrijdige verhalen naast elkaar) uit tot een latere fase, na deze eerste minimale entiteitgedreven ontdekfunctie.** — De Verhalenkaart van Groningen toont dat kaartgedreven plek-ontdekking waardevol en haalbaar is, maar vereist geocoding/kaartinfrastructuur die nu ontbreekt; dit is te groot voor één kleine, samenhangende stap en bouwt logisch voort op een eerst werkende, eenvoudigere ontdekfunctie.
- **Stel het bouwen van een beheerinterface voor de reeds gebouwde privacyclassificatie- en externe-verificatiemodules uit tot na de gebruikersgerichte ontdekfunctie.** — Deze modules bestaan al als backend-logica met uitgebreide tests, maar het ontbreken van UI ervoor is een intern kwaliteits-/beheervraagstuk, niet de kern van de kloof tussen missie en bezoekerservaring; de missie vraagt eerst om zichtbare waarde voor bezoekers.

## UX-voorstel: Ontdek Heemskerk vanuit vraag, plek, persoon of gebeurtenis (homepage-ontdekblok)

**Gebruikersdoel:** Als bezoeker van hkh-autopilot wil ik vanaf de homepage snel bestaande Heemskerkse verhalen kunnen ontdekken door te zoeken op een vrije vraag of te klikken op een plek, persoon of gebeurtenis, zodat de belofte "ontdek de geschiedenis van Heemskerk" voor het eerst waargemaakt wordt met herleidbare bronvermelding, zonder dat er nieuwe externe koppelingen of persoonsgegevens nodig zijn.

### Flow
1. Bezoeker opent de homepage en ziet, direct onder de bestaande introductietekst, een nieuw ontdekblok met een zoekveld en een rij klikbare entiteitchips (plek/persoon/gebeurtenis) die automatisch zijn afgeleid uit bestaande, reeds gepubliceerde nieuws- en recorddata.
2. Bezoeker typt een vrije zoekterm in het zoekveld óf klikt direct op een entiteitchip (bijv. 'Slot Assumburg' of 'Kerkweg').
3. Systeem toont een resultatenlijst van bestaande, reeds gepubliceerde items (nieuwsberichten/records) die matchen op de gekozen entiteit of zoekterm, elk met titel, korte samenvatting en een entiteitstype-badge (plek/persoon/gebeurtenis).
4. Elk resultaat toont een herleidbare bronvermelding op basis van bestaande verplichte velden (rechtenstatus, herkomst) uit de record-intake, zodat het productprincipe 'Betrouwbaar' zichtbaar is.
5. Bezoeker klikt op een resultaat en komt op een detailweergave met de volledige inhoud plus expliciete bron- en rechteninformatie en een link 'terug naar overzicht'.
6. Als een zoekterm of entiteit geen resultaten oplevert, toont het systeem een duidelijke, niet-lege lege-staat met suggestie om een andere term te proberen of een van de getoonde entiteitchips te gebruiken.
7. Bezoeker kan op elk moment de zoekopdracht wissen of terugnavigeren naar het volledige entiteitoverzicht via een altijd zichtbare 'wis zoekopdracht'-actie.

### Wireframe

HOMEPAGE (bestaand + nieuw ontdekblok)
=========================================================
[Titel] Historische Kring Heemskerk – hkh-autopilot
[Tekst] "Ontdek de geschiedenis van Heemskerk vanuit een
         vraag, plek, persoon of gebeurtenis. ..."

[NIEUW] Ontdekblok
---------------------------------------------------------
 Label: "Waar, wie of wat zoek je?"
 [ Zoekveld: __________________________ ] [Zoek-knop]

 Ontdek via een van deze onderwerpen:
 (Plek)   (Persoon)  (Gebeurtenis) (Plek)   (Persoon)
 [Kerkweg][J. de Vries][Opening museum][Slot Assumburg][...]
 <-- elke chip is een <button>, focusbaar, met type-badge -->
---------------------------------------------------------
[Knop] Lees onze productvisie
[Badge] Servicestatus: OK
[Sectie] Laatste nieuws (bestaand, ongewijzigd)
=========================================================

RESULTATENWEERGAVE (na zoeken of chip-klik)
=========================================================
[Terug-link] < Terug naar overzicht        [Wis zoekopdracht]
[Kop, aria-live] "12 resultaten voor 'Slot Assumburg'"
---------------------------------------------------------
 [Kaart] Titel item 1                 [Badge: Plek]
         Korte samenvatting...
         Bron: Noord-Hollands Archief · Rechtenstatus: Publiek
 ---------------------------------------------------------
 [Kaart] Titel item 2                 [Badge: Gebeurtenis]
         Korte samenvatting...
         Bron: HKH-nieuwsbericht · Rechtenstatus: Publiek
=========================================================

LEGE STAAT (geen resultaten)
=========================================================
[Terug-link] < Terug naar overzicht
[Tekst] "Geen resultaten voor 'xyz'."
[Suggestie] "Probeer een van deze onderwerpen:"
 (Kerkweg) (J. de Vries) (Opening museum)
=========================================================

DETAILWEERGAVE (na klik op resultaat)
=========================================================
[Terug-link] < Terug naar resultaten
[Kop] Titel item                      [Badge: type]
[Volledige tekst / samenvatting]
[Sectie] Bron & rechten
  - Herkomst: ...
  - Rechtenstatus: ...
  - Privacyclassificatie: ...
=========================================================

### Interactiehypotheses
- H1 (functioneel): elke getoonde entiteitchip op de homepage leidt bij klikken tot een resultatenlijst met minimaal 1 item en zonder foutrespons; geautomatiseerd verifieerbaar via een e2e-test die alle chips doorloopt en de HTTP-status en itemcount van elke respons controleert.
- H2 (betrouwbaarheid): elk getoond resultaat en elke detailweergave bevat een niet-lege bronvermelding (herkomst- en rechtenstatusveld); geautomatiseerd verifieerbaar door de API-respons te asserten op aanwezigheid en non-leegheid van deze velden voor alle testfixtures.
- H3 (robuustheid): een lege, onbekende of willekeurige zoekterm resulteert altijd in een expliciete lege-staat-melding met suggesties, nooit in een crash of lege witruimte; geautomatiseerd verifieerbaar via een UI-test die een set willekeurige/onbekende termen invoert en de aanwezigheid van de lege-staat-component controleert.
- H4 (toegankelijkheid): alle interactieve elementen (zoekveld, chips, resultaatkaarten, terug-links) zijn volledig bedienbaar met alleen het toetsenbord in een logische tab-volgorde; geautomatiseerd verifieerbaar via een Playwright-toetsenbordnavigatietest gecombineerd met axe-core contrast- en ARIA-checks.
- H5 (herleidbaarheid van data): entiteiten (plek/persoon/gebeurtenis) worden uitsluitend afgeleid uit reeds gepubliceerde, niet-geblokkeerde records; geautomatiseerd verifieerbaar door te asserten dat geen enkel getoond entiteit- of resultaatitem verwijst naar een record met privacyclassificatie 'Blocked' in de testdataset.

### Toegankelijkheid
- Zoekveld heeft een programmatisch gekoppeld <label> (of aria-label) en een zichtbare focusrand die voldoet aan WCAG 2.2 focus-appearance.
- Entiteitchips zijn geïmplementeerd als semantische <button>-elementen (geen <div onclick>), volledig bereikbaar en activeerbaar via Tab + Enter/Spatie.
- Resultatenlijst gebruikt een semantische lijststructuur (ul/li of heading-hiërarchie) zodat schermlezers het aantal en de volgorde van resultaten correct aankondigen.
- Het aantal resultaten wordt aangekondigd via een aria-live="polite" regio bij elke nieuwe zoekactie, zodat schermlezergebruikers feedback krijgen zonder focusverlies.
- Alle tekst-op-achtergrond combinaties (inclusief badges en chips) voldoen aan minimaal 4.5:1 contrastratio conform WCAG 2.2 AA.
- Terug-links en 'wis zoekopdracht'-acties staan in een consistente, voorspelbare positie en zijn met toetsenbord bereikbaar zonder tussenliggende onzichtbare elementen.
- Lege-staat- en foutmeldingen zijn als tekst (niet alleen als icoon/kleur) waarneembaar en met een schermlezer voorleesbaar.

### Privacy
- Alleen reeds gepubliceerde records met een niet-geblokkeerde privacyclassificatie worden gebruikt om entiteiten (plek/persoon/gebeurtenis) af te leiden en te tonen; geblokkeerde of nog niet beoordeelde records blijven volledig buiten de ontdekfunctie.
- Er worden geen nieuwe persoonsgegevens verzameld of opgeslagen voor deze functie; entiteiten worden alleen afgeleid uit velden die al bestaan en al een rechtsgrondslag/doel hebben binnen de bestaande record-intake.
- Vrije zoektermen van bezoekers worden niet gekoppeld aan een identificeerbare gebruiker opgeslagen; als zoekgedrag geaggregeerd wordt gelogd voor productverbetering, gebeurt dit anoniem en met een duidelijk, vooraf gedocumenteerd doel.
- Er worden voor deze functie geen nieuwe trackingcookies of fingerprinting-technieken toegevoegd; de functie werkt zonder persoonsgebonden sessieopslag.
- Bronvermelding (rechtenstatus/herkomst) wordt getoond zoals reeds vastgelegd bij record-intake, zodat bezoekers kunnen zien onder welke voorwaarden een item beschikbaar is, zonder dat hiervoor aanvullende persoonsgegevens nodig zijn.
- Bij twijfel over de privacyclassificatie van een record (bijv. onvolledige of tegenstrijdige status) wordt het record fail-closed uitgesloten van de ontdekresultaten, in lijn met de bestaande privacyclassificatie-aanpak.

## Kritische beoordeling

**Oordeel:** ACCEPT

Beide kandidaten vormen een coherente, klein-stapse invulling van het productbesluit uit iteratie 28 om de kloof tussen de ontdek-belofte en de statische homepage te dichten, zonder externe koppelingen of persoonsgegevens. Kandidaat 0 lost proactief een BLOCKING scope-conflict met functional-spec.md op door de databron te versmallen tot uitsluitend gepubliceerde nieuwsberichten (geen record-intake/privacyclassificatie/verificatiedata via API), en onderbouwt dit expliciet. Kandidaat 1 bouwt daarop voort met sterke, geautomatiseerd toetsbare toegankelijkheidscriteria (WCAG 2.2 AA, aria-live, toetsenbordvolgorde, axe-core) en herkent zelf het consistentieprobleem met de bestaande INTERNAL kandidaat 13, onderbouwd met live Playwright-bewijs dat kandidaat 13's premisse (een bestaande primaire ontdekactie) niet meer klopt. Alle acceptatiecriteria in beide kandidaten zijn volledig geautomatiseerd verifieerbaar (contracttests, integratietests, Playwright e2e, axe-core, toetsenbordnavigatietests) zonder handmatige test, menselijk productbesluit, accountaanmaak, betaling, DNS-wijziging, apparaatcontrole of extern toegangstoken — de autonomie-hardegate wordt gehaald. Bronnen, onzekerheid en rechten zijn consequent zichtbaar gemaakt (inclusief "nog onbekend"-labels voor inspiratiebronnen die niet daadwerkelijk geïntegreerd worden). Geen BLOCKING issues gevonden; beide kandidaten krijgen ACCEPT.
- **WARNING · CONSISTENCY** — Kandidaat 1 stelt voor dat de bestaande INTERNAL kandidaat 13 wordt ingetrokken/gesuperseded zodra dit ontdekblok wordt opgeleverd, maar een kandidaat kan de status van een andere kandidaat niet zelf wijzigen. De orchestrator moet dit expliciet afhandelen bij levering, anders ontstaat risico op dubbel of conflicterend homepage-layout-/toetsenbordvolgordewerk als kandidaat 13 alsnog los wordt opgepakt.
- **INFO · SCOPE** — De heuristiek om plek/persoon/gebeurtenis-entiteiten uit vrije nieuwsteksten af te leiden zonder gelabelde taxonomie kan tot verkeerde classificatie leiden; het risico is al transparant benoemd door de kandidaat zelf met een mitigatie (deterministisch patroongebaseerd i.p.v. vrije-tekst-NLP) en hoeft de oplevering niet te blokkeren, maar verdient aandacht bij implementatie.
- **INFO · SOURCE** — Inspiratiebronnen (Netwerk Digitaal Erfgoed, Delpher, De Verhalen van Groningen) hebben nog onbekende contentrechten; dit is correct zichtbaar gemaakt in de sourcelijst en er is geen daadwerkelijke data-integratie met deze bronnen gepland in de huidige kandidaten, dus geen blokkerend rechtenrisico. Herbevestig rechten expliciet vóórdat een toekomstige story deze bronnen wél daadwerkelijk koppelt.

## Geaccepteerde storykandidaten

### Uitbreiding van de bestaande nieuws-API: entiteiten en zoekfilter afgeleid uit gepubliceerde nieuwsberichten

_Sleutel: `discovery-api-entities-and-search`_

Los het BLOCKING scope-conflict op door géén nieuw REST-contract te openen: breid uitsluitend het reeds bestaande nieuws-afleverpad uit (het contract dat frontend/lib/latest_news.dart en backend_client.dart vandaag al gebruiken) met (1) deterministisch afgeleide entiteitsmetadata (type plek/persoon/gebeurtenis + label) per gepubliceerd nieuwsbericht, en (2) een zoek-/filterparameter op dat bestaande contract die matcht op vrije tekst of op een gekozen entiteit. Uit docs/factory/functional-spec.md blijkt dat alléén de modules linkdossier en privacyclassificatie (voor genealogische records) expliciet 'geen REST-endpoint/opslag' uitsluiten — precies om te voorkomen dat privacygevoelige genealogische gegevens via API lekken; record-intake en het nieuwsbericht-domein kennen die uitsluiting niet. Om dat blokkerende conflict volledig te vermijden, gebruikt deze kandidaat daarom uitsluitend reeds gepubliceerde nieuwsberichten als databron voor entiteiten en zoekresultaten — geen record-intake-, privacyclassificatie- of externe-verificatiegegevens worden ontsloten. Dit is een bewuste versmalling ten opzichte van het eerdere productbesluit (dat ook record-intake noemde als bron); het ontsluiten van record-intakegegevens via een eigen contract blijft voor een latere, apart geautoriseerde stap.

**Acceptatiecriteria**
- Geautomatiseerde contracttest bevestigt dat na deze wijziging geen nieuwe REST-route of -controller is toegevoegd: het aantal geregistreerde routes blijft gelijk aan vóór de wijziging; de uitbreiding bestaat uitsluitend uit extra velden en een optionele queryparameter op het bestaande nieuwsbericht-responscontract dat frontend/lib/latest_news.dart al consumeert.
- Geautomatiseerde integratietest bewijst dat entiteitsmetadata (type, label, itemtelling) uitsluitend wordt afgeleid uit nieuwsberichten met status 'gepubliceerd'; een testfixture voor een concept- of ongepubliceerd nieuwsbericht verschijnt nooit in de entiteitenlijst of -telling.
- Geautomatiseerde test bewijst dat de zoekparameter, gegeven een vrije zoekterm die matcht op titel/samenvatting van een bestaand gepubliceerd nieuwsbericht, dat bericht retourneert met een niet-lege bronvermelding ('afkomstig uit gepubliceerd HKH-nieuwsbericht', inclusief publicatiedatum).
- Geautomatiseerde test bewijst dat filtering op een geselecteerde entiteit (plek/persoon/gebeurtenis) uitsluitend nieuwsberichten retourneert die aan die entiteit gekoppeld zijn, elk voorzien van het juiste entiteitstype-label.
- Geautomatiseerde test bewijst dat een zoekterm of entiteit zonder matches een expliciet leeg resultaat oplevert (HTTP 200, lege lijst, totaal=0) op het bestaande contract, zonder foutstatus of onverwachte exceptie.
- Geautomatiseerde test bevestigt dat geen enkel endpoint, veld of queryparameter uit deze uitbreiding record-intake-, privacyclassificatie- of externe-verificatiedata retourneert of raadpleegt — alleen het nieuwsbericht-domein wordt aangeraakt.
- Het uitgebreide responscontract wordt automatisch als onderdeel van de build gedocumenteerd/getest (bijv. gegenereerd schema-diff), zodat een vervolgstory hier zonder handmatige afstemming op kan voortbouwen.

Bronnen: [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/docs/factory/functional-spec.md), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md), [https://api.github.com/repos/robbertvdzon/hkh-autopilot/git/trees/main?recursive=1](https://api.github.com/repos/robbertvdzon/hkh-autopilot/git/trees/main?recursive=1)

Risico's: Door uitsluitend nieuwsberichten als bron te gebruiken (in plaats van ook record-intake, zoals het oorspronkelijke productbesluit voorstelde) is de initiële hoeveelheid entiteiten mogelijk klein; dit is een bewuste, tijdelijke versmalling om het BLOCKING scope-conflict met functional-spec.md op te lossen en kan in een latere, apart geautoriseerde stap worden uitgebreid., De heuristiek om vrije tekst in nieuwsberichten te herleiden naar plek/persoon/gebeurtenis kan zonder gelabelde taxonomie verkeerd classificeren; mitigatie: start met een klein, deterministisch veld-/patroongebaseerd afleidingsmechanisme in plaats van vrije-tekst-NLP., Als het bestaande nieuws-contract nog geen expliciete velden voor herkomst/publicatiedatum blootgeeft, moet dit als non-breaking toevoeging aan dat contract worden gedaan; een testfixture voor een ouder nieuwsbericht zonder deze velden moet expliciet worden afgedekt zodat fail-closed gedrag (uitsluiten i.p.v. crashen) gegarandeerd is.

### Homepage-ontdekblok: zoekveld en entiteitchips over gepubliceerde nieuwsberichten, met toegankelijke resultaten

_Sleutel: `homepage-discover-block`_

Implementeer op de hkh-autopilot-homepage het onderzochte ontdekblok: een gelabeld zoekveld plus een rij klikbare entiteitchips (plek/persoon/gebeurtenis), gevoed door de uitgebreide, bestaande nieuws-contract uit kandidaat 'discovery-api-entities-and-search' (dus uitsluitend gepubliceerde nieuwsberichten, geen record-intake-, privacyclassificatie- of verificatiedata). Een chipklik of zoekopdracht toont een resultatenlijst (titel, samenvatting, entiteitstype-badge, bronregel 'afkomstig uit gepubliceerd HKH-nieuwsbericht' met publicatiedatum) of, bij nul resultaten, een niet-lege lege-staat met suggestiechips. Elk resultaat opent een detailweergave met volledige inhoud plus expliciete bronvermelding en een terug-link. Alle interactieve elementen zijn volledig met het toetsenbord bedienbaar en het aantal resultaten wordt aangekondigd via een aria-live-regio (WCAG 2.2 AA), volgens de eerder vastgelegde Flutter-web-a11y-inspectietechniek (flt-semantics-placeholder + CDP AX-boom). Reconciliatie met de bestaande INTERNAL kandidaat 13 ('Maak de bestaande primaire ontdekactie toegankelijk met toetsbare statusfeedback'): de live-inspectiebevindingen in dit onderzoek (Playwright, 2026-08-09) tonen aan dat er op dit moment géén primaire ontdekactie op de homepage bestaat — kandidaat 13's premisse klopt dus feitelijk niet meer. Dit ontdekblok wordt vanaf het eerste ontwerp volledig toegankelijk gebouwd (aria-live, semantische knoppen, volledige toetsenbordvolgorde, axe-core-gevalideerd) en levert daarmee zelf de 'toegankelijke primaire ontdekactie' die kandidaat 13 beoogde. Voorstel: kandidaat 13 wordt introkken/gesuperseded door deze kandidaat zodra deze is opgeleverd, zodat er geen dubbel of conflicterend homepage-layout-/toetsenbordvolgordewerk ontstaat; er wordt geen aparte, parallelle 'primaire ontdekactie' toegevoegd naast dit ontdekblok.

**Acceptatiecriteria**
- Playwright-e2e-test laadt de homepage, controleert dat het zoekveld en minstens één entiteitchip renderen op basis van data uit het uitgebreide nieuws-contract, klikt een chip aan en controleert dat een resultatenlijst met minimaal 1 item en een niet-lege bronregel ('afkomstig uit gepubliceerd HKH-nieuwsbericht') verschijnt.
- Playwright-e2e-test voert een onbekende/onzinnige zoekterm in en controleert dat de lege-staat-component met suggestiechips verschijnt in plaats van een lege of foutieve weergave.
- Playwright-e2e-test klikt een resultaatkaart aan en controleert dat de detailweergave de volledige berichttekst, publicatiedatum en bronvermelding toont, plus een werkende 'terug naar resultaten'-link.
- Geautomatiseerde toetsenbordnavigatietest doorloopt zoekveld, chips, resultaatkaarten en terug-/wisknoppen in logische tab-volgorde en activeert elk element uitsluitend via Enter/Spatie zonder muisgebruik, als enige en volledige homepage-'primaire ontdekactie' (geen los, tweede toegankelijkheidspad).
- Geautomatiseerde axe-core-scan van het ontdekblok (standaardstaat, resultatenstaat, lege staat, detailweergave) rapporteert nul kritieke/ernstige violations, inclusief contrast- en ARIA-rolcontroles.
- Geautomatiseerde test bevestigt dat de resultatentelling wordt blootgesteld via een aria-live="polite"-regio en dat de tekst na elke nieuwe zoekactie of chipselectie wijzigt.
- Geautomatiseerde end-to-end-test bevestigt dat geen enkele chip of resultaatitem ooit data uit record-intake-, privacyclassificatie- of externe-verificatiebronnen toont, uitsluitend gepubliceerde nieuwsberichten, in lijn met de versmalde scope van de onderliggende API-kandidaat.

Bronnen: [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl), [https://www.deverhalenvangroningen.nl/verhalenkaart](https://www.deverhalenvangroningen.nl/verhalenkaart), [https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md](https://raw.githubusercontent.com/robbertvdzon/hkh-autopilot/main/README.md)

Afhankelijkheden (candidateKey): discovery-api-entities-and-search (binnen deze batch herkend als: discovery-api-entities-and-search)

Risico's: Dit ontdekblok is bedoeld als vervanging/superset van de bestaande INTERNAL kandidaat 13; als kandidaat 13 desondanks parallel wordt opgeleverd, ontstaat een layout- en toetsenbordvolgordeconflict op de homepage — mitigatie: kandidaat 13 expliciet intrekken/superseden zodra dit ontdekblok wordt aangeboden., De frontend leunt volledig op het uitgebreide nieuws-contract uit de API-kandidaat; wijzigt dat contract nadat deze story start, dan is herwerk nodig — mitigatie: bevries het uitgebreide contract voordat deze story start., Flutter-web-toegankelijkheidssemantiek vereist een specifieke inspectietechniek (flt-semantics-placeholder + CDP AX-boom) in plaats van gewone DOM-inspectie; geautomatiseerde a11y-tests moeten hiermee rekening houden om valse negatieven te voorkomen., Omdat de databron voor deze iteratie beperkt is tot gepubliceerde nieuwsberichten, kan het aantal beschikbare entiteitchips klein zijn; dit is een bewuste, tijdelijke versmalling om het BLOCKING scope-conflict met functional-spec.md op te lossen.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
