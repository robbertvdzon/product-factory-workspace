---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0049
date: 2026-08-15
status: approved
sources:
  - https://github.com/robbertvdzon/product-factory
  - https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart
  - https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/iteration_evidence.dart
  - https://product-factory.vdzonsoftware.nl
  - https://product-factory-acceptance.vdzonsoftware.nl
  - https://docs.github.com/en/actions/how-tos/monitor-workflows?tool=webui
  - https://www.atlassian.com/software/jira/guides/jql/tutorials
  - https://www.atlassian.com/software/jira/guides/issues/overview
---
# Productcyclus 49

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Belangrijkste nog onbeantwoorde productvraag: hoe wordt ‘Eerdere cycli’ voor alle producten compact en scanbaar, zonder reden of beslisbron onnauwkeurig voor te stellen? De eerder onderzochte uitleg bij de uitgeschakelde startactie is inmiddels op acceptatie aanwezig. Product Factory-cycli hebben compacte bewijsregels, maar HKH Autopilot valt door productspecifieke bronlogica terug op grote technische kaarten. Er is nog geen productbesluit genomen.

### De vorige startblokkade is inmiddels opgelost op acceptatie

Na selectie van Product Factory toont de uitgeschakelde startknop direct dat het product niet actief is, meldt zij één aanvullende onvervulde voorwaarde en biedt zij een read-only link naar productdetails. Deze eerdere onderzoeksvraag is daarom niet opnieuw onderzocht.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart)

### Compact bewijs is nog productspecifiek

De drie terminale synthetische Product Factory-cycli verschijnen als niet-uitklapbare bewijsregels met afzonderlijke velden voor datum, uitkomst, reden, beslisbron en gekoppelde opbrengst. HKH Autopilot toont daarentegen grote kaarten met technische tellingen, backendtekst en ‘Toon opbrengst’. De broncode beperkt `shouldShowIterationEvidence` expliciet tot `productSlug == product-factory` en vijf terminale statussen.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/iteration_evidence.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/iteration_evidence.dart), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart)

### Een actieve cyclus krijgt ten onrechte beslistaal

De actieve Product Factory-kaart toont ‘Beslisbron: Onbekend (Afgeleid)’, hoewel een lopende cyclus nog geen terminale beslissing heeft. De bewijsregelpredicate sluit actieve cycli uit, maar de generieke kaart gebruikt een ander presentatiepad. Dit wijst op behoefte aan toestandsbewuste semantiek: bij lopend werk voortgang tonen en pas na een terminale uitkomst reden en beslisbron presenteren.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/iteration_evidence.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/iteration_evidence.dart), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart)

### De hoofdflow is verbeterd, maar de hiërarchie breekt bij productwisseling

Productkeuze, startactie, eerdere cycli en gekoppelde stories staan in de gewenste volgorde. Productwisseling werkt en Beheer is bereikbaar. Bij HKH Autopilot vullen enkele terminale kaarten echter vrijwel het scherm, waardoor eerdere uitkomsten en gekoppelde stories niet snel scanbaar zijn. De compacte Product Factory-regels functioneren visueel beter als overzicht.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### Externe run-overzichten scheiden samenvatting van diagnose

GitHub Actions documenteert een runhistorie met status en afzonderlijke runlogs voor diagnose. Jira beschrijft een lijstweergave voor veel werkitems en een detailweergave voor rijke context. Dit patroon past bij Product Factory: stabiele kernvelden in de cyclilijst en volledige evaluatie- en technische details achter een read-only bewijsdetail.

Bronnen: [https://docs.github.com/en/actions/how-tos/monitor-workflows?tool=webui](https://docs.github.com/en/actions/how-tos/monitor-workflows?tool=webui), [https://www.atlassian.com/software/jira/guides/jql/tutorials](https://www.atlassian.com/software/jira/guides/jql/tutorials), [https://www.atlassian.com/software/jira/guides/issues/overview](https://www.atlassian.com/software/jira/guides/issues/overview)

### Huidige applicatie

**Doel:** Product Factory organiseert autonome productontwikkeling voor geregistreerde producten: onderzoek, productkeuze, UX- en storyvorming, aanbieding aan de Software Factory en verwerking van uitkomsten in volgende iteraties. De primaire dashboardgebruiker is de producteigenaar, die per gekozen product snel een cyclus moet kunnen starten, eerdere uitkomsten moet begrijpen en gekoppelde stories moet volgen. Beheer bevat de globale operationele lijsten.

**Wat ontbreekt:**
- Terminale cyclusweergave is niet uniform: alleen Product Factory krijgt compacte bewijsregels; HKH Autopilot houdt grote technische, uitklapbare kaarten.
- De hoofdcode encodeert de productidentiteit `product-factory` in plaats van een algemeen terminale-cycluscontract, waardoor een tweede product niet dezelfde scanbare hoofdflow krijgt.
- Een actieve cyclus toont een beslisbron terwijl er nog geen eindbeslissing is; ‘Onbekend (Afgeleid)’ suggereert bewijs dat semantisch nog niet bestaat.
- De generieke HKH-kaarten benadrukken interne kandidaten, leveringen en backendstatus boven de eigenaarstaken uitkomst, reden, beslisser en gekoppelde opbrengst.
- De compacte Product Factory-regels zijn op desktop zichtbaar beoordeeld, maar responsieve scanbaarheid op een smalle viewport blijft in dit onderzoek onbewezen.

### Verbetermogelijkheden

- Generaliseer de compacte terminale bewijsregel op basis van terminale status en beschikbare bewijsvelden, niet op productslug; gebruik één productonafhankelijk presentatiemodel voor datum, uitkomst, reden, beslisbron en gekoppelde opbrengst.
- Maak de lijst toestandsbewust: actieve cycli tonen status, huidige stap en betrouwbare laatste voortgang; terminale cycli tonen uitkomst, reden en beslisbron. Toon geen beslisbron zolang geen beslissing bestaat.
- Gebruik de compacte regel als scanlaag en ‘Bekijk bewijs’ als read-only detailroute voor input, evaluatieonderbouwing, gekoppelde stories en technische diagnose.
- Definieer expliciete fallbacksemantiek: ‘Onbekend’ wanneer brondata ontbreekt, ‘Afgeleid’ alleen wanneer een geldige terminale uitkomst aantoonbaar uit bestaande gegevens is gereconstrueerd en geen fictieve beslissing voor `RUNNING`.
- Toets een eventuele generalisatie met synthetische varianten voor beide producten en alle terminale statussen, plus een actieve cyclus, handmatige annulering, expliciete agentbeslissing, afgeleide historische beslissing en volledig onbekende provenance.
- Controleer dezelfde kernvelden en navigatie geautomatiseerd op brede en smalle viewports, met toetsenbordfocus en semantische labels.

### Inspiratiebronnen

- [GitHub Actions workflow run history](https://docs.github.com/en/actions/how-tos/monitor-workflows?tool=webui) — Scheidt overzicht van runstatus en uitvoertijd van diagnostische job- en staplogs; bruikbaar als referentie voor scanlaag versus bewijsdetail.
- [Jira list/detail views](https://www.atlassian.com/software/jira/guides/jql/tutorials) — Gebruikt een lijstweergave om veel items te scannen en een detailweergave voor rijke context; dit ondersteunt compacte cycli zonder onderbouwing weg te laten.
- [Jira work-item field hierarchy](https://www.atlassian.com/software/jira/guides/issues/overview) — Maakt onderscheid tussen belangrijkste velden, contextvelden en overige details; relevant voor het terugdringen van technische tusseninformatie op het hoofdscherm.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://github.com/robbertvdzon/product-factory) | 2026-08-15 | Publieke repository zonder LICENSE-bestand op de geraadpleegde hoofdbranch; auteursrechtelijke hergebruiksrechten zijn daarom onbekend. | Primaire bron voor doel, architectuur en huidige dashboardimplementatie. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart) | 2026-08-15 | Geen repositorylicentie aangetroffen; de code is publiek leesbaar, maar het hergebruiksrecht is onbekend. | Toont de productflow, keuze tussen bewijsregel en generieke kaart, actieve-cycluspresentatie en startbeschikbaarheidsuitleg. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/iteration_evidence.dart) | 2026-08-15 | Geen repositorylicentie aangetroffen; de code is publiek leesbaar, maar het hergebruiksrecht is onbekend. | Primaire bron voor de productspecifieke predicate en afleiding van datum, uitkomst, reden en beslisbron. |
| [bron](https://product-factory.vdzonsoftware.nl) | 2026-08-15 | Publiek bereikbare applicatie; concrete hergebruikslicentie onbekend. | Verplichte productiecontrole; toont dat de productomgeving Google-authenticatie vereist. |
| [bron](https://product-factory-acceptance.vdzonsoftware.nl) | 2026-08-15 | Publiek bereikbare acceptatie-UI met synthetische data; concrete hergebruikslicentie onbekend. | Primaire visuele bron voor de actuele hoofdflow, productwisseling, bewijsregels, generieke kaarten en Beheer. |
| [bron](https://docs.github.com/en/actions/how-tos/monitor-workflows?tool=webui) | 2026-08-15 | Copyright GitHub; gebruik valt onder de GitHub-sitevoorwaarden. Geen open hergebruikslicentie vastgesteld. | Vergelijkbaar patroon voor runhistorie, status, uitvoertijd en afzonderlijke diagnose via logs. |
| [bron](https://www.atlassian.com/software/jira/guides/jql/tutorials) | 2026-08-15 | Copyright Atlassian; gebruik valt onder de Atlassian-sitevoorwaarden. Geen open hergebruikslicentie vastgesteld. | Beschrijft lijst- en detailweergaven en scanbaarheid bij grotere aantallen werkitems. |
| [bron](https://www.atlassian.com/software/jira/guides/issues/overview) | 2026-08-15 | Copyright Atlassian; gebruik valt onder de Atlassian-sitevoorwaarden. Geen open hergebruikslicentie vastgesteld. | Geeft inspiratie voor prioritering van kernvelden en scheiding tussen belangrijke context en overige details. |

## Productbeslissing

Maak ‘Eerdere cycli’ productonafhankelijk en toestandsbewust: toon voor ieder product terminale cycli als compacte, niet-uitklapbare bewijsregels en houd actieve cycli als voortgangskaarten zonder reden- of beslistaal. Gebruik één presentatiemodel op basis van cyclusstatus en beschikbare bewijsvelden, niet op productslug. Dit is een kleine, terugdraaibare uitbreiding van de bestaande Product Factory-weergave en rondt primair roadmap-epic theme-product-factory-0001 af, terwijl zij de semantische fout uit theme-product-factory-0002 wegneemt.

**Waarom:** De hoofdflow is al correct geordend, maar breekt bij productwisseling doordat alleen Product Factory compacte bewijsregels krijgt. HKH Autopilot valt terug op grote technische kaarten, terwijl een actieve cyclus ten onrechte een beslisbron toont. De gekozen richting behoudt het bestaande onderscheid tussen lopend werk en bewezen uitkomsten: actieve cycli tonen uitsluitend status, huidige stap en betrouwbare laatste voortgang; terminale cycli tonen afzonderlijk datum, uitkomst, concrete reden, beslisbron en gekoppelde opbrengst. Technische diagnose en volledige onderbouwing blijven via een read-only detail beschikbaar. Er worden geen historische gegevens gemigreerd en geen koppelingen, authenticatie of gedrag van andere producten gewijzigd. Onzekerheid blijft bestaan over de scanbaarheid op smalle schermen; daarom hoort responsieve verificatie expliciet bij de acceptatie.

### Prioriteiten
- Vervang de productslugvoorwaarde door een productonafhankelijke terminale-statusvoorwaarde voor de bestaande compacte bewijsregel.
- Scheid actieve en terminale semantiek strikt: toon bij RUNNING geen reden, beslissing, beslisbron, ‘Onbekend’ of ‘Afgeleid’.
- Behoud in iedere terminale bewijsregel afzonderlijk gelabelde velden voor datum, uitkomst, reden, beslisbron en gekoppelde opbrengst; gebruik alleen ‘Afgeleid’ wanneer een terminale bron aantoonbaar uit bestaande gegevens is gereconstrueerd.
- Bied vanuit een terminale regel een read-only ‘Bekijk bewijs’-detail voor evaluatieonderbouwing, gekoppelde stories en technische diagnose, zonder de regel zelf uitklapbaar te maken.
- Verifieer geïsoleerd met synthetische cycli voor beide producten: actief, handmatig geannuleerd, expliciete agentbeslissing, afgeleide historische beslissing en onbekende bron; controleer brede en smalle viewport, toetsenbordfocus en semantische labels.

### Besluiten
- **Gebruik één productonafhankelijk presentatiemodel voor terminale cycli.** — De huidige productslugcontrole veroorzaakt aantoonbaar verschillende hoofdschermen voor Product Factory en HKH Autopilot, terwijl dezelfde eigenaarstaak en kernvelden gelden.
- **Toon actieve cycli als voortgang en terminale cycli als bewijs.** — Een actieve cyclus heeft nog geen eindbeslissing. De huidige tekst ‘Beslisbron: Onbekend (Afgeleid)’ stelt daarom bewijs voor dat nog niet kan bestaan.
- **Maak terminale bewijsregels compact en niet-uitklapbaar voor alle relevante producten.** — De compacte Product Factory-regels ondersteunen scanbaarheid; de grote HKH Autopilot-kaarten vullen vrijwel het scherm en verhinderen snel overzicht van eerdere uitkomsten en gekoppelde stories.
- **Scheid de scanlaag van read-only bewijsdetails.** — Externe run- en werkitempatronen ondersteunen een compacte historie met een afzonderlijke detailweergave voor onderbouwing en diagnose.
- **Migreer geen historische cycli en wijzig geen brondata.** — De verbetering kan volledig in de presentatie en semantische afleiding worden uitgevoerd. Ontbrekende historische provenance blijft eerlijk ‘Onbekend’; alleen aantoonbare reconstructie wordt ‘Afgeleid’.

## UX-voorstel: Productonafhankelijke, toestandsbewuste cyclusgeschiedenis

**Gebruikersdoel:** Als producteigenaar wil ik na productselectie lopend werk direct onderscheiden van bewezen uitkomsten en eerdere cycli compact kunnen scannen, zonder dat reden of beslisbron nauwkeuriger wordt voorgesteld dan de beschikbare operationele metadata toelaat.

### Flow
1. De gebruiker kiest een product; focus blijft logisch bij de productselector en de secties worden voor dat product bijgewerkt.
2. Onder ‘Huidige cyclus’ verschijnt een RUNNING-cyclus als voortgangskaart met status, huidige stap, laatste betrouwbare voortgang en een read-only detailactie. Reden, uitkomst, beslissing, beslisbron, ‘Onbekend’ en ‘Afgeleid’ ontbreken.
3. Onder ‘Eerdere cycli’ verschijnen terminale cycli van ieder product als compacte, niet-uitklapbare bewijsregels, gesorteerd van nieuw naar oud.
4. Elke bewijsregel toont afzonderlijk gelabelde kernvelden: datum, uitkomst, reden, beslisbron en gekoppelde opbrengst. Ontbrekende provenance wordt ‘Onbekend’; ‘Afgeleid’ verschijnt uitsluitend bij aantoonbare reconstructie van een terminale uitkomst.
5. De gebruiker activeert ‘Bekijk bewijs’ met toetsenbord, schermlezer of aanwijzer en opent een read-only detailweergave met evaluatieonderbouwing, gekoppelde stories en technische diagnose.
6. Via ‘Terug naar eerdere cycli’ keert de gebruiker terug naar dezelfde productselectie, scrollpositie en eerder geactiveerde bewijsregel.

### Wireframe

BREED SCHERM

[Product Factory]                                      [Beheer]

Product
[ Product Factory                                      v ]

Huidige cyclus
┌─────────────────────────────────────────────────────────┐
│ Status: Bezig                                           │
│ Huidige stap: UX-ontwerp                                │
│ Laatste voortgang: 15 aug 2026, 14:32                   │
│ [Bekijk voortgang]                                      │
└─────────────────────────────────────────────────────────┘

Eerdere cycli
┌─────────────────────────────────────────────────────────┐
│ 14 aug 2026 | Afgerond                                  │
│ Reden: Productrichting voldoende onderbouwd             │
│ Beslisbron: Agentbeslissing                              │
│ Opbrengst: 2 gekoppelde stories     [Bekijk bewijs]      │
├─────────────────────────────────────────────────────────┤
│ 12 aug 2026 | Geannuleerd                               │
│ Reden: Handmatig geannuleerd                            │
│ Beslisbron: Handmatige actie                            │
│ Opbrengst: Geen                     [Bekijk bewijs]      │
├─────────────────────────────────────────────────────────┤
│ 10 aug 2026 | Afgerond                                  │
│ Reden: Historische evaluatie beschikbaar                │
│ Beslisbron: Afgeleid                [Bekijk bewijs]      │
└─────────────────────────────────────────────────────────┘

Gekoppelde stories
[compacte bestaande lijst]

SMAL SCHERM

Product
[ Product Factory                    v ]

Huidige cyclus
[Status: Bezig]
[Huidige stap: UX-ontwerp]
[Laatste voortgang: 15 aug, 14:32]
[Bekijk voortgang]

Eerdere cycli
┌──────────────────────────────┐
│ 14 aug 2026                  │
│ Uitkomst: Afgerond           │
│ Reden: Productrichting…      │
│ Beslisbron: Agentbeslissing  │
│ Opbrengst: 2 stories         │
│ [Bekijk bewijs]              │
└──────────────────────────────┘

BEWIJSDETAIL — READ-ONLY
[← Terug naar eerdere cycli]
Cyclus van 14 aug 2026 — Afgerond
[Kernbewijs]
[Evaluatieonderbouwing]
[Gekoppelde stories]
[Technische diagnose]

### Interactiehypotheses
- Als de productslugvoorwaarde wordt verwijderd en terminale status het presentatiemodel bepaalt, renderen equivalente terminale cycli van Product Factory en HKH Autopilot dezelfde velden en componentstructuur. Toets met component- en snapshottests voor beide producten.
- Een RUNNING-cyclus bevat nergens reden- of beslistaal. Toets in de semantische UI-boom dat labels voor uitkomst, reden, beslissing, beslisbron, ‘Onbekend’ en ‘Afgeleid’ afwezig zijn.
- Iedere terminale cyclus toont datum, uitkomst, reden, beslisbron en gekoppelde opbrengst in een vaste volgorde. Toets met parametrische tests voor afgerond, mislukt en handmatig geannuleerd.
- ‘Afgeleid’ verschijnt alleen wanneer een terminale uitkomst volgens expliciete afleidingsregels uit bestaande metadata kan worden gereconstrueerd; ontbrekende provenance toont ‘Onbekend’. Toets met fixtures voor expliciete agentbeslissing, handmatige annulering, afgeleide historie en ontbrekende bron.
- De overzichtsregel is niet uitklapbaar en ‘Bekijk bewijs’ navigeert naar een afzonderlijke read-only detailweergave. Toets dat Enter en Spatie de actie uitvoeren, de URL of routestatus verandert en geen muterende bediening aanwezig is.
- Op een viewport van 320 CSS-pixels blijven alle kernlabels en ‘Bekijk bewijs’ zichtbaar zonder horizontaal scrollen of tekstoverlap. Toets met geautomatiseerde responsive screenshots en layout-asserties op overflow en clipping groepen na screenshot comparison/test tooling in CI environment which can assert geometry programmatically and agents can review resulting diffs without manual approval or test requirement being prescribed to humans (automated review only). Scanning order in accessibility tree must remain meaningful independent of visual layout. No user personal data fixtures may be used—synthetic operational metadata only, and screenshots generated locally in ephemeral CI; no transmission to third parties permitted. Ensure paired comparison for both products and all required states. Mobile typography labels may wrap but values remain adjacent and unambiguous; test DOM ordering and accessible names programmatically rather than relying solely upon images, using existing project’s/

### Toegankelijkheid
- Alle interactieve elementen zijn bereikbaar in een logische toetsenbordvolgorde; de volledige bewijsregel is geen impliciet klikgebied. Alleen de duidelijk benoemde actie ‘Bekijk bewijs’ is interactief.
- Gebruik semantische koppen voor ‘Huidige cyclus’, ‘Eerdere cycli’ en het bewijsdetail. Markeer de cyclusverzameling als lijst en iedere cyclus als lijstitem.
- Koppel ieder zichtbaar veldlabel programmatisch aan zijn waarde. De toegankelijke naam van de detailactie bevat de cyclusdatum en uitkomst, bijvoorbeeld ‘Bekijk bewijs van cyclus 14 augustus 2026, afgerond’.
- Status en beslisbron worden niet uitsluitend met kleur onderscheiden. Iconen zijn decoratief of hebben een passende tekstuele naam.
- Focus is altijd zichtbaar met minimaal 3:1 contrast tegen aangrenzende kleuren; tekst en essentiële UI-componenten voldoen minimaal aan WCAG 2.2 AA-contrast.
- Na opening van het bewijsdetail gaat focus naar de detailkop. Bij terugkeer wordt focus hersteld naar de eerder geactiveerde actie; productwisseling kondigt de bijgewerkte cyclusinhoud beknopt aan.
- Bij 200% zoom en op 320 CSS-pixels ontstaan geen horizontale scroll, overlap of verlies van kerninformatie. De lees- en focusvolgorde blijft gelijk aan de visuele volgorde.
- Geautomatiseerde toegankelijkheidstests controleren toetsenbordbediening, focusherstel, semantische rollen, toegankelijke namen, contrast en afwezigheid van ernstige axe-regelovertredingen.

### Privacy
- Gebruik uitsluitend operationele metadata van Product Factory zelf: productidentificatie, cyclusstatus, tijdstippen, processtap, evaluatieresultaat, provenance en verwijzingen naar Product Factory-opbrengsten.
- Verwerk of toon geen persoonsgegevens en geen gebruikersdata, inhoud of diagnostiek uit andere producten. Productnamen mogen alleen als geregistreerde operationele identificatie worden gebruikt.
- De bewijsdetailweergave is strikt read-only en introduceert geen mutaties, vrije tekstinvoer, tracking of nieuwe externe koppelingen.
- Toon alleen de minimale diagnose die nodig is om de cyclus te begrijpen. Verberg tokens, geheimen, authenticatiegegevens, ruwe prompts, infrastructuurdetails en mogelijk herleidbare loginhoud.
- Gebruik uitsluitend synthetische fixtures in tests. Controleer geautomatiseerd dat verboden velden en patronen voor e-mailadressen, tokens en geheimen niet in overzicht, toegankelijkheidsboom, URL of detailweergave verschijnen.
- Bewaar geen nieuwe historische gegevens en vul ontbrekende provenance niet speculatief aan. ‘Onbekend’ is de veilige standaard; ‘Afgeleid’ vereist een deterministische, toetsbare regel op reeds toegestane metadata.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is klein, terugdraaibaar en volledig autonoom uitvoerbaar en toetsbaar. Hij hergebruikt bestaande frontenddata en classificatie, voorkomt beslistaal bij actieve cycli en bevat geautomatiseerde controles voor responsiviteit, toegankelijkheid en privacy. Er zijn geen materiële blokkades.
- **WARNING · SOURCE** — De acceptatieomgeving is een veranderlijke visuele bron en de externe GitHub- en Atlassian-patronen zijn slechts inspiratie. Baseer de implementatie en tests primair op de actuele repositorycontracten; kopiëren uit de extern gelicentieerde voorbeelden is niet nodig.
- **INFO · CONSISTENCY** — De huidige productspecifieke vertakking is verklaarbaar vanuit de beperkte scope van gepubliceerde story:69. Leg dit bij de wijziging kort vast, zodat aan de kwaliteitsregel over het waarom van het bestaande gedrag wordt voldaan.
- **INFO · SCOPE** — De kandidaat overlapt bewust met story:69 en story:78, maar generaliseert een nog niet geleverd resultaat naar andere producten en corrigeert daarnaast de actieve-cyclussemantiek; dit is geen exact duplicaat.

## Geaccepteerde storykandidaten

### Toon voor ieder product een toestandsbewuste, compacte cyclusgeschiedenis

_Sleutel: `generaliseer-toestandsbewuste-cyclusgeschiedenis`_

Bouw voort op de bestaande productscope en bewijsregels en vervang de productslugvoorwaarde door één productonafhankelijk presentatiemodel. Toon iedere terminale cyclus, ongeacht product, als compacte, niet-uitklapbare bewijsregel met afzonderlijk gelabelde datum, uitkomst, reden, beslisbron en gekoppelde opbrengst. Gebruik voor expliciete, afgeleide en onbekende beslisbronnen uitsluitend de bestaande conservatieve classificatie; ‘Afgeleid’ is alleen toegestaan bij een deterministisch reconstrueerbare terminale uitkomst. Toon actieve cycli uitsluitend als voortgangskaart met status, huidige stap en beschikbare laatste voortgang, zonder uitkomst, reden, beslissing, beslisbron, ‘Onbekend’ of ‘Afgeleid’. De bestaande read-only detailactie blijft beschikbaar; er komen geen nieuwe API’s, opslag, migraties, telemetrie of muterende acties.

**Acceptatiecriteria**
- Geautomatiseerde componenttests bewijzen met synthetische equivalente terminale cycli voor Product Factory en HKH Autopilot dat productslug geen invloed heeft op componenttype, veldvolgorde of labels: beide renderen als compacte, niet-uitklapbare bewijsregel met datum, uitkomst, reden, beslisbron, gekoppelde opbrengst en één read-only detailactie.
- Parametrische tests voor alle ondersteunde terminale statussen bewijzen dat iedere regel de vijf kernvelden afzonderlijk en toegankelijk gelabeld toont en dat de bestaande detailactie naar precies de bijbehorende cyclus navigeert zonder muterende bediening toe te voegen.
- Tests voor expliciete agentbeslissing, handmatige annulering, reconstrueerbare historische provenance en ontbrekende provenance bewijzen respectievelijk de bestaande expliciete classificatie, ‘Afgeleid’ en ‘Onbekend’; geen fixture zonder aantoonbare afleidingsgrond mag ‘Afgeleid’ tonen.
- Een RUNNING-fixture voor ieder product rendert als voortgangskaart met status, huidige stap en alleen beschikbare betrouwbare voortgang; geautomatiseerde tekst- en semantiekasserties bewijzen dat uitkomst, reden, beslissing, beslisbron, ‘Onbekend’ en ‘Afgeleid’ volledig ontbreken.
- Geautomatiseerde tests op een brede viewport en op 320 CSS-pixels bewijzen voor beide producten dat de kernvelden en detailactie zichtbaar blijven zonder horizontale overflow, clipping of overlap en dat de DOM- en toegankelijkheidsvolgorde gelijk blijft aan de betekenisvolle leesvolgorde.
- Geautomatiseerde toegankelijkheidscontroles bewijzen dat de geschiedenis een semantische lijst vormt, iedere cyclus een lijstitem is, de detailactie een unieke toegankelijke naam met cyclusdatum en uitkomst heeft, toetsenbordfocus zichtbaar is en geen ernstige axe-regelovertredingen optreden.
- Alle tests gebruiken uitsluitend synthetische operationele metadata; geautomatiseerde controles bevestigen dat overzicht, detailactie, URL en toegankelijkheidsboom geen e-mailadressen, tokens, geheimen, ruwe prompts of foutlogs bevatten.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/iteration_evidence.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/iteration_evidence.dart), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart), [https://docs.github.com/en/actions/how-tos/monitor-workflows?tool=webui](https://docs.github.com/en/actions/how-tos/monitor-workflows?tool=webui), [https://www.atlassian.com/software/jira/guides/jql/tutorials](https://www.atlassian.com/software/jira/guides/jql/tutorials), [https://www.atlassian.com/software/jira/guides/issues/overview](https://www.atlassian.com/software/jira/guides/issues/overview)

Afhankelijkheden: story:69, story:78, story:57, story:60 (herkend als bestaande stories: 69, 78, 57, 60)

Risico's: Historische cycli kunnen onvoldoende provenance bevatten; de presentatie moet dan conservatief ‘Onbekend’ blijven en mag geen gegevens reconstrueren zonder deterministische grond., Productspecifieke backendteksten kunnen ongeschikt of te technisch zijn als concrete reden; alleen reeds toegestane presentatieteksten mogen in de compacte regel verschijnen., Lange redenen of productnamen kunnen op 320 CSS-pixels de scanbaarheid verminderen; wrapping en overflow moeten daarom programmatisch worden geborgd., Generalisatie kan onbedoeld niet-terminale of onbekende statussen als bewijsregel renderen; een gesloten terminale-statusvoorwaarde en parametrische regressietests zijn vereist.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
