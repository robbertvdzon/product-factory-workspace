---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0050
date: 2026-08-15
status: approved
sources:
  - https://product-factory.vdzonsoftware.nl
  - https://product-factory-acceptance.vdzonsoftware.nl
  - https://github.com/robbertvdzon/product-factory
  - https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart
  - https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/iteration_evidence.dart
  - https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md
  - https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/view-deployment-history?apiVersion=2022-11-28
  - https://linear.app/docs/assigning-issues
---
# Productcyclus 50

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Belangrijkste nog onbeantwoorde productvraag: hoe kan de eigenaar betrouwbaar zien welke Product Factory-versie daadwerkelijk op iedere omgeving draait? De publieke hoofdbranch bevat inmiddels de productonafhankelijke, toestandsbewuste cyclusgeschiedenis, terwijl acceptatie nog grote technische HKH-kaarten toont. Zonder build- of revisie-informatie kan de eigenaar niet bepalen of een zichtbaar tekort nog gebouwd moet worden of alleen nog niet is uitgerold. Er is geen productbesluit genomen.

### Productie is aantoonbaar onderzocht en vraagt authenticatie

Productie is met headless Chromium geopend. De eerste screenshot liet een laadspinner zien. Na expliciete navigatie naar de beheerroute verscheen het scherm ‘Log in met een toegestaan Google-account’. Er is niet geprobeerd in te loggen. Hiermee is de tekortkoming uit de vorige onderzoekspoging expliciet hersteld.

Bronnen: [https://product-factory.vdzonsoftware.nl](https://product-factory.vdzonsoftware.nl)

### Acceptatie en de actuele hoofdbranch tonen verschillende productstaten

Acceptatie toont terminale HKH Autopilot-cycli nog als grote kaarten met technische tellingen, backendtekst en ‘Toon opbrengst’. De actuele publieke hoofdbranch stuurt daarentegen alle terminale statussen, onafhankelijk van productslug, naar een compacte IterationEvidenceRow en actieve statussen naar IterationProgressCard. Dit is een geobserveerd verschil tussen uitgerolde omgeving en repository; de oorzaak daarvan is niet vastgesteld.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/iteration_evidence.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/iteration_evidence.dart)

### Het dashboard onthult niet welke versie wordt beoordeeld

Op het acceptatie-overzicht en in Beheer is geen zichtbare build-ID, bronrevisie of uitroltijd aangetroffen. Daardoor is het versieverschil alleen door vergelijking met de repository te ontdekken. Voor een systeem dat zichzelf continu beoordeelt, verzwakt dit de herleidbaarheid van visuele acceptatiebevindingen.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md)

### De kernflow en beheerscheiding zijn aanwezig maar de oude HKH-weergave blijft overladen

Acceptatie ordent de hoofdflow rond actief product, ‘Cyclus starten’, ‘Eerdere cycli’ en verderop gekoppelde stories. Beheer is werkelijk geopend en bevat de globale operationele storywachtrij en leveringsinformatie. Op het hoofdscherm nemen twee zichtbare HKH-kaarten echter vrijwel de volledige viewport in, waardoor snelle vergelijking van uitkomsten en het bereiken van gekoppelde stories moeilijk blijft zolang de nieuwere compacte weergave niet op deze omgeving draait.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md)

### Productie-initialisatie geeft geen stabiele, onmiddellijke authenticatiestatus

In de onderzochte productierun bleef de eerste opname op een spinner staan. De browserconsole meldde een lege Google-accountlijst, een FedCM-tokenfout en daarna een null-checkfout. Na aanvullende routenavigatie verscheen wel het bedoelde inlogscherm. Dit duidt op een foutgevoelig initialisatiepad in deze headless browsersituatie; er is niet vastgesteld of gewone ingelogde gebruikers dit eveneens ervaren.

Bronnen: [https://product-factory.vdzonsoftware.nl](https://product-factory.vdzonsoftware.nl)

### De repository bevestigt het beoogde publiek en de systeemrol

De publieke documentatie beschrijft Product Factory als een zelfstandige toepassing die per geregistreerd product onderzoek, productkeuzes, UX en storyvorming organiseert, geaccepteerde kandidaten aan Software Factory aanbiedt en uitvoeringsresultaten in volgende iteraties verwerkt. Het dashboard is daarbij de bedienings- en verantwoordingslaag voor de eigenaar.

Bronnen: [https://github.com/robbertvdzon/product-factory](https://github.com/robbertvdzon/product-factory), [https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md)

### Huidige applicatie

**Doel:** Product Factory organiseert autonoom productonderzoek, productkeuzes, UX-ontwikkeling en storyvorming voor geregistreerde producten. Het biedt geaccepteerde stories aan Software Factory aan, volgt de uitvoering en gebruikt resultaten als context voor volgende cycli. Het dashboard is primair voor de producteigenaar, die per product een cyclus moet kunnen starten, eerdere opbrengsten en beslissingen moet begrijpen en gekoppelde stories moet volgen.

**Wat ontbreekt:**
- Acceptatie draait visueel nog niet de compacte, productonafhankelijke cyclusgeschiedenis die inmiddels op de publieke hoofdbranch staat.
- Geen zichtbare build-ID, bronrevisie of uitroltijd maakt het onmogelijk om vanuit het dashboard vast te stellen welke implementatie wordt beoordeeld.
- De grote HKH-cycluskaarten op acceptatie tonen technische details in het hoofdoverzicht en duwen gekoppelde stories naar beneden.
- De eerste productieweergave bleef op een spinner staan en rapporteerde browserfouten voordat het inlogscherm na routenavigatie verscheen.
- De acceptatieomgeving vermeldt wel dat zij synthetische data gebruikt, maar niet hoe actueel die omgeving ten opzichte van de repository is.

### Verbetermogelijkheden

- Onderzoek een kleine, read-only omgevingsidentiteit met omgevingsnaam, korte bronrevisie/build-ID en uitroltijd, zodat iedere acceptatiebevinding aan de werkelijk draaiende versie kan worden gekoppeld.
- Onderzoek of het dashboard een neutrale status kan tonen wanneer acceptatie achterloopt op de verwachte bronrevisie, zonder deploymentbeheer of muterende bediening aan het hoofdscherm toe te voegen.
- Koppel eventueel vanuit die omgevingsidentiteit naar bestaande read-only deploymentdetails; houd technische historie buiten de drie kernacties van het hoofdscherm.
- Maak productie-initialisatie fouttolerant: toon onmiddellijk een begrijpelijke login- of authenticatiestatus wanneer geen sessie beschikbaar is, zonder langdurige spinner of null-checkfout.
- Gebruik bij toekomstige onafhankelijke acceptatiecontroles eerst de zichtbare omgevingsrevisie om te voorkomen dat reeds gebouwde maar nog niet uitgerolde functionaliteit opnieuw als productontwerptekort wordt onderzocht.

### Inspiratiebronnen

- [GitHub deployment history](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/view-deployment-history?apiVersion=2022-11-28) — GitHub toont per omgeving de actieve en eerdere deployments met gekoppelde commit, status, workflowlogs en deployment-URL. Dit is relevante inspiratie voor minimale, controleerbare omgevingsherkomst.
- [Linear Activity history](https://linear.app/docs/assigning-issues) — Linear houdt veranderingen met actor chronologisch bij in een Activity-feed. Dit illustreert hoe herkomst en verantwoordelijkheid in een read-only detail kunnen staan zonder het primaire overzicht te overladen.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://product-factory.vdzonsoftware.nl) | 2026-08-15 | Publiek bereikbare webapp; auteursrecht en hergebruiklicentie van de UI zijn onbekend. | Direct browserbewijs van het productie-laadgedrag en de authenticatiegrens. |
| [bron](https://product-factory-acceptance.vdzonsoftware.nl) | 2026-08-15 | Publiek bereikbare acceptatieapp; auteursrecht en hergebruiklicentie van de UI zijn onbekend. | Direct visueel bewijs van de werkelijk uitgerolde acceptatie-UX en het beheergedeelte. |
| [bron](https://github.com/robbertvdzon/product-factory) | 2026-08-15 | Publieke repository, maar GitHub rapporteert geen repositorylicentie; hergebruikrechten zijn daarom onbekend. | Primaire bron voor doel, architectuur en actuele implementatie van Product Factory. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart) | 2026-08-15 | Onderdeel van een publieke repository zonder gedetecteerde licentie; hergebruikrechten onbekend. | Primaire implementatiebron voor schermvolgorde, productselectie, cycluscomponenten en Beheer. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/iteration_evidence.dart) | 2026-08-15 | Onderdeel van een publieke repository zonder gedetecteerde licentie; hergebruikrechten onbekend. | Primaire implementatiebron voor de productonafhankelijke statusclassificatie en bewijsweergave. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md) | 2026-08-15 | Onderdeel van een publieke repository zonder gedetecteerde licentie; hergebruikrechten onbekend. | Functionele documentatie van de productcyclus en de bedoelde dashboardweergave. |
| [bron](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/view-deployment-history?apiVersion=2022-11-28) | 2026-08-15 | GitHub-documentatie; gebruik valt onder de GitHub Terms en het toepasselijke sitecopyright. Specifieke hergebruikvoorwaarden zijn niet afzonderlijk vastgesteld. | Officiële beschrijving van een omgevingsgerichte deploymentgeschiedenis met actieve deployment, commit, status, logs en URL. |
| [bron](https://linear.app/docs/assigning-issues) | 2026-08-15 | Linear-documentatie; auteursrechtelijk beschermd, specifieke hergebruiklicentie onbekend. | Officiële beschrijving van een Activity-feed die veranderingen en verantwoordelijke actor chronologisch toont. |

## Productbeslissing

Maak de werkelijk draaiende dashboardversie zichtbaar met één compacte, read-only omgevingsidentiteit. Toon in Beheer voor de huidige omgeving: omgevingsnaam, korte bronrevisie of build-ID en uitroltijd. Toon dezelfde identiteit subtiel bij onafhankelijke acceptatiebewijzen, zodat een bevinding ondubbelzinnig aan een deployment kan worden gekoppeld. Als gegevens ontbreken, toon per veld expliciet ‘Onbekend’; leid geen revisie af en voeg geen deploymentbediening toe. Deze wijziging raakt geen productdata, authenticatie, Software Factory-koppeling of gedrag van andere producten en moet afzonderlijk kunnen worden verwijderd.

**Waarom:** Acceptatie toont nog de grote HKH Autopilot-kaarten, terwijl de publieke hoofdbranch al productonafhankelijke compacte bewijsregels bevat. Het dashboard vermeldt nergens welke versie wordt beoordeeld. Daardoor is niet betrouwbaar te onderscheiden of roadmap-epic theme-product-factory-0001 nog implementatiewerk vereist of dat de gebouwde wijziging alleen nog niet op acceptatie draait. Een minimale omgevingsidentiteit ondersteunt de missie om Product Factory continu en eerlijk te toetsen: eerst wordt vastgesteld wát werkelijk draait, pas daarna wordt bestaand gedrag opnieuw ontworpen. De richting is klein, read-only en omkeerbaar. Onzeker blijft of revisie en uitroltijd momenteel al door de build- of deploymentketen worden aangeboden; de uitvoering moet bij ontbreken daarvan eerlijk ‘Onbekend’ tonen en mag geen menselijke beheerhandeling plannen.

### Prioriteiten
- Lever eerst een deterministische read-only bron voor omgevingsnaam, korte revisie/build-ID en uitroltijd, zonder runtime-afleiding uit repository-inhoud.
- Plaats de volledige omgevingsidentiteit in Beheer en houd het hoofdscherm bij de drie kernacties; hoogstens een compacte verwijzing mag bij acceptatiebewijs staan.
- Maak ontbrekende metadata zichtbaar als ‘Onbekend’ en behandel gedeeltelijke of ongeldige metadata fouttolerant, zonder spinner of blokkade van de kernflow.
- Breid de onafhankelijke controle van roadmap-epic theme-product-factory-0001 uit: leg vóór de visuele beoordeling de zichtbare omgevingsidentiteit vast en beoordeel daarna pas de compacte terminale bewijsregels.
- Verifieer de wijziging geïsoleerd op brede en smalle schermen en bevestig dat geen productdata, cyclusgedrag, authenticatie of Software Factory-levering verandert.

### Besluiten
- **Kies zichtbare omgevingsherkomst als eerstvolgende kleine productrichting.** — Het geobserveerde verschil tussen acceptatie en de actuele hoofdbranch maakt iedere visuele acceptatie-uitspraak ambigu zolang de draaiende revisie onbekend is.
- **Toon drie afzonderlijk gelabelde velden: omgeving, revisie/build-ID en uitroltijd.** — Deze minimale combinatie identificeert waar en welke build wordt beoordeeld en wanneer die is uitgerold. Omgevingsgerichte deploymentgeschiedenis koppelt eveneens een omgeving aan commit en deploymentstatus.
- **Plaats de volledige informatie in Beheer en houd haar read-only.** — Beheer bevat al globale operationele informatie, terwijl het hoofdscherm bedoeld is voor de productscope en kernacties. Zo verbetert traceerbaarheid zonder de heringerichte hoofdflow opnieuw te belasten.
- **Gebruik expliciet ‘Onbekend’ wanneer deploymentmetadata ontbreekt en blokkeer de UI niet.** — Eerlijke onbekendheid past bij controleerbaar bewijs. Het geobserveerde productiepad met spinner en browserfouten laat bovendien zien dat aanvullende metadata nooit een voorwaarde voor een bruikbare dashboardtoestand mag worden.
- **Gebruik de zichtbare identiteit als voorwaarde voor toekomstige onafhankelijke acceptatie van de compacte cyclusweergave.** — De hoofdbranch classificeert terminale cycli al productonafhankelijk als compacte bewijsregels, terwijl acceptatie nog oude grote kaarten toont. Vastlegging van de draaiende versie voorkomt dat een deploymentachterstand opnieuw als ontwerptekort wordt behandeld.

## UX-voorstel: Omgevingsidentiteit controleren

**Gebruikersdoel:** Als producteigenaar wil ik vóór het beoordelen van acceptatiebewijs kunnen vaststellen welke Product Factory-versie werkelijk op de huidige omgeving draait.

### Flow
1. De eigenaar opent Beheer via toetsenbord, schermlezer of aanwijzer.
2. Boven de bestaande operationele informatie staat een read-only sectie ‘Omgevingsidentiteit’.
3. De eigenaar leest drie afzonderlijk gelabelde waarden: omgeving, revisie/build-ID en uitroltijd.
4. Als een waarde ontbreekt, ongeldig is of niet geladen kan worden, toont uitsluitend dat veld ‘Onbekend’; Beheer en de kernflow blijven bruikbaar.
5. Bij onafhankelijk acceptatiebewijs staat een subtiele compacte verwijzing met dezelfde omgevingsnaam en revisie/build-ID.
6. Een agent legt de zichtbare identiteit vast en vergelijkt deze deterministisch met de verwachte deploymentmetadata voordat de agent de cyclusweergave beoordeelt.
7. De identiteit biedt geen knoppen voor deployen, vernieuwen, terugdraaien of wijzigen.

### Wireframe

BEHEER

[Terug naar dashboard]

Omgevingsidentiteit
┌──────────────────────────────────────────────┐
│ Omgeving          Acceptatie                 │
│ Revisie/build-ID  a1b2c3d                    │
│ Uitgerold op      15 aug 2026, 10:42 CEST    │
│                                              │
│ Alleen-lezen informatie                      │
└──────────────────────────────────────────────┘

[Overige bestaande beheerinhoud]

COMPACT ACCEPTATIEBEWIJS
┌──────────────────────────────────────────────┐
│ [bestaande bewijsinhoud]                     │
│ Omgeving: Acceptatie · revisie: a1b2c3d      │
└──────────────────────────────────────────────┘

ONTBREKENDE METADATA
Omgeving          Acceptatie
Revisie/build-ID  Onbekend
Uitgerold op      Onbekend

### Interactiehypotheses
- Als omgeving, revisie/build-ID en uitroltijd zichtbaar zijn in Beheer, kan een agent iedere acceptatiebevinding aan exact één waargenomen deploymentidentiteit koppelen; toetsbaar met componenttests die de drie labels en waarden uitlezen.
- Als metadata geheel ontbreekt, toont elk betrokken veld ‘Onbekend’ en blijven navigatie, cyclusstart en bestaande beheerinhoud beschikbaar; toetsbaar met geautomatiseerde UI-tests zonder metadatafixture.
- Als metadata gedeeltelijk of ongeldig is, blijft geldige metadata zichtbaar en krijgt alleen ieder onbruikbaar veld ‘Onbekend’; toetsbaar met fixtures voor ontbrekende revisie, ongeldige tijd en onbekende omgeving.
- De compacte verwijzing bij acceptatiebewijs bevat dezelfde genormaliseerde omgeving en revisie als Beheer; toetsbaar met een end-to-endtest die beide schermwaarden vergelijkt.
- De toevoeging verandert geen productselectie, cyclusstatus, authenticatie of Software Factory-levering; toetsbaar met bestaande regressietests en netwerk-/state-asserties die bevestigen dat alleen read-only metadata wordt gelezen.
- Op brede en smalle viewports blijven labels en waarden leesbaar zonder horizontaal scrollen of overlap; toetsbaar met geautomatiseerde layout- en screenshottests op vooraf vastgelegde viewportmaten.

### Toegankelijkheid
- Gebruik semantische koppen en een beschrijvende sectienaam ‘Omgevingsidentiteit’.
- Koppel elk label programmatisch aan zijn tekstwaarde; vertrouw niet op kolompositie, kleur of typografie.
- Maak de sectie volledig leesbaar met toetsenbord en schermlezer; voeg geen niet-focusbare interactieve imitatie of onnodige tabstop toe.
- Laat ‘Onbekend’ als expliciete tekst uitspreken en gebruik geen pictogram als enige foutaanduiding.
- Behoud een logische lees- en focusvolgorde: terugnavigatie, omgevingsidentiteit, bestaande beheerinhoud.
- Voldoe minimaal aan WCAG 2.2 AA-contrast: 4,5:1 voor normale tekst en 3:1 voor grote tekst en betekenisvolle visuele componenten; toetsbaar met een geautomatiseerde toegankelijkheidsscan.
- Ondersteun tekstvergroting tot 200% en smalle schermen zonder verlies van inhoud; waarden mogen afbreken, maar labels en waarden blijven ondubbelzinnig gekoppeld.
- Valideer automatisch op toegankelijke naamgeving, semantische structuur, toetsenbordbereikbaarheid, contrast en horizontale overflow.

### Privacy
- Verwerk uitsluitend operationele metadata van Product Factory zelf: omgevingsnaam, revisie/build-ID en uitroltijd.
- Verwerk geen persoonsgegevens, accountgegevens, IP-adressen, gebruikersactiviteit, productinhoud of data van andere producten.
- Toon geen commitbericht, auteur, e-mailadres, deploymentactor, token, geheime configuratie of interne repository-URL.
- Beperk revisie/build-ID tot een niet-geheime korte identifier die voldoende is voor deploymentcorrelatie.
- Maak de metadata read-only en voeg geen analytics of nieuwe gebruikersregistratie toe.
- Test met synthetische metadata en laat geautomatiseerde tests falen wanneer niet-toegestane velden of patronen voor tokens en e-mailadressen in het component verschijnen.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is klein, read-only, privacybewust, toegankelijk gespecificeerd en volledig agent-uitvoerbaar en geautomatiseerd toetsbaar. De fallback ‘Onbekend’ voorkomt afhankelijkheid van handmatige deploymentconfiguratie. Er is wel een niet-blokkerend risico dat alleen fixturetests slagen terwijl een werkelijk gebouwde deployment geen bruikbare revisie of uitroltijd aanbiedt.
- **WARNING · SCOPE** — De acceptatiecriteria bewijzen met fixtures dat metadata kan worden weergegeven, maar eisen niet expliciet dat de echte build- of deploymentketen de beschikbare revisie en uitroltijd automatisch aanlevert. Daardoor kan de story formeel slagen terwijl de uitgerolde omgeving overal ‘Onbekend’ toont en het productdoel slechts gedeeltelijk bereikt. Voeg bij uitvoering bij voorkeur een geautomatiseerde packaging- of integratietest toe die beschikbare CI/buildmetadata zonder eigenaarshandeling doorgeeft; behoud ‘Onbekend’ uitsluitend wanneer een veld werkelijk niet beschikbaar is.
- **INFO · RIGHTS** — De repository en externe inspiratiebronnen hebben geen duidelijk vastgestelde hergebruiklicentie. De kandidaat vraagt echter alleen om eigen implementatie van algemene deploymentmetadata en niet om overname van beschermde UI, tekst of broncode; dit blokkeert levering niet.
- **INFO · CONSISTENCY** — De kandidaat sluit inhoudelijk aan op de gepubliceerde stories 65 en 85 en dupliceert geen reeds geleverd resultaat. De gedeelde bron en normalisatie voor Beheer en bewijsregels beperken het risico op tegenstrijdige identiteiten.

## Geaccepteerde storykandidaten

### Toon de draaiende omgevingsidentiteit in Beheer en bij acceptatiebewijs

_Sleutel: `toon-omgevingsidentiteit-bij-acceptatiebewijs`_

Voeg één read-only omgevingsidentiteit toe die bestaat uit afzonderlijk gelabelde velden voor omgevingsnaam, korte bronrevisie of build-ID en uitroltijd. Lees deze waarden uit deterministisch tijdens build of deployment aangeleverde metadata; leid ze niet af uit repository-inhoud of productdata. Toon de volledige identiteit boven de bestaande operationele inhoud in Beheer en toon bij iedere compacte terminale bewijsregel uitsluitend een subtiele verwijzing met dezelfde genormaliseerde omgevingsnaam en revisie/build-ID. Ontbrekende, ongeldige of niet-laadbare waarden worden onafhankelijk als ‘Onbekend’ weergegeven en blokkeren het dashboard niet. De toevoeging bevat geen deploymentgeschiedenis of muterende bediening en verandert geen productdata, authenticatie, cyclusgedrag, productselectie of Software Factory-koppeling.

**Acceptatiecriteria**
- Geautomatiseerde componenttests bevestigen dat Beheer onder de semantische kop ‘Omgevingsidentiteit’ drie afzonderlijk programmatisch gekoppelde labels en waarden toont: ‘Omgeving’, ‘Revisie/build-ID’ en ‘Uitgerold op’.
- Een deterministische testfixture met geldige deploymentmetadata toont de aangeleverde omgevingsnaam, een niet-geheime verkorte revisie/build-ID en een geformatteerde uitroltijd; de UI leest hiervoor geen repository-inhoud, productrecord of cyclusrecord.
- Fixtures met geheel ontbrekende metadata, een ontbrekende revisie, een ongeldige uitroltijd en een onbekende omgeving bevestigen dat uitsluitend ieder onbruikbaar veld exact ‘Onbekend’ toont, terwijl Beheer, productnavigatie en de bestaande cyclusweergave zonder spinner of fout blijven renderen.
- Een geautomatiseerde end-to-endtest vergelijkt Beheer met een compacte terminale bewijsregel en bevestigt dat beide exact dezelfde genormaliseerde omgevingsnaam en revisie/build-ID tonen; de bewijsregel toont geen uitroltijd en blijft compact en niet-uitklapbaar.
- Geautomatiseerde controles bevestigen dat de identiteit geen knoppen of acties voor deployen, vernieuwen, wijzigen of terugdraaien bevat en geen muterende netwerkverzoeken veroorzaakt.
- Geautomatiseerde regressietests bevestigen dat productselectie, cyclusstart en -status, authenticatie en Software Factory-levering ongewijzigd blijven en dat uitsluitend read-only deploymentmetadata wordt gelezen.
- Tests met synthetische metadata laten de component falen wanneer weergegeven metadata commitberichten, auteurs, e-mailadressen, tokens, geheime configuratie of interne repository-URL’s bevat.
- Geautomatiseerde toegankelijkheids-, layout- en screenshottests op vooraf vastgelegde brede en smalle viewports bevestigen semantische koppen, gekoppelde labels en waarden, logische leesvolgorde, WCAG 2.2 AA-contrast, 200% tekstvergroting en afwezigheid van horizontale overflow.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/iteration_evidence.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/iteration_evidence.dart), [https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md), [https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/view-deployment-history?apiVersion=2022-11-28](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/view-deployment-history?apiVersion=2022-11-28)

Afhankelijkheden: story:65, story:85 (herkend als bestaande stories: 65, 85)

Risico's: De huidige build- of deploymentketen levert mogelijk nog geen revisie en uitroltijd aan; de implementatie moet dan eerlijk ‘Onbekend’ tonen zonder runtime-afleiding., Een revisie/build-ID kan onbedoeld gevoelige deploymentinformatie bevatten; verkorting en een strikte allowlist zijn nodig., Als Beheer en bewijsregels metadata afzonderlijk normaliseren, kunnen tegenstrijdige identiteiten ontstaan; beide presentaties moeten exact dezelfde read-only bron en normalisatie gebruiken., De compacte bewijsregel kan op smalle schermen opnieuw te veel informatie bevatten; de toevoeging moet beperkt blijven tot omgeving en revisie en automatisch op overflow worden gecontroleerd.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
