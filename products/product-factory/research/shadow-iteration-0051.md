---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0051
date: 2026-08-16
status: approved
sources:
  - https://github.com/robbertvdzon/product-factory
  - https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md
  - https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart
  - https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/iteration_evidence.dart
  - https://product-factory.vdzonsoftware.nl
  - https://product-factory-acceptance.vdzonsoftware.nl
  - https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-githubs-form-schema
  - https://linear.app/docs/issue-templates
---
# Productcyclus 51

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Belangrijkste nog onbeantwoorde productvraag: hoe kan de eigenaar bij een handmatige cyclusstart vooraf de onderzoeksvraag controleren of aanvullen, terwijl de autonome standaard behouden blijft? De runtime ondersteunt en bewaart al een vrije focus en het cyclusdetail toont die als ‘Opdracht’, maar de prominente startknop voert onmiddellijk uit zonder zichtbare invoer of bevestiging. Daardoor kan actuele eigenaarcontext niet betrouwbaar via de hoofdflow worden meegegeven of vooraf gecontroleerd. Er is nog geen productbesluit genomen. De eerder gekozen omgevingsidentiteit en compacte cyclusregels zijn inmiddels zichtbaar op acceptatie.

### Focus bestaat in de cyclus, maar niet in de handmatige startflow

De functionele documentatie vermeldt dat iedere cyclus een korte vrije focus meekrijgt en dat de autonome standaard luidt dat het systeem zelf de belangrijkste onbeantwoorde productvraag bepaalt. De actuele frontend koppelt de knop echter direct aan `startCycle(slug)`, zonder zichtbare focusparameter, invoer of bevestiging. Dit is het belangrijkste resterende gat tussen de beschikbare cycluscontext en de bediening door de eigenaar.

Bronnen: [https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl)

### De opdracht wordt achteraf wel zichtbaar en is dus een bruikbaar traceerpunt

Na doorklikken op ‘Bekijk cyclusdetail’ toonde acceptatie voor productcyclus 3 een afzonderlijk onderdeel ‘Opdracht’ met de concrete onderzoeksvraag. De informatie kan dus achteraf onderdeel van het cyclusbewijs zijn. Wat ontbreekt is een zichtbare verbinding tussen die opgeslagen opdracht en wat de eigenaar vóór het starten heeft gekozen of geaccepteerd.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md)

### De eerder openstaande deploymentonzekerheid is op acceptatie opgelost

Acceptatie toont nu per terminale cyclus een compacte bewijsregel met datum, uitkomst, reden, beslisbron, gekoppelde opbrengst en omgevingsverwijzing. Beheer toont bovendien ‘Omgeving: Acceptatie’, revisie/build-ID `feb1202d1992` en uitroltijd `15-08-2026 22:20`. Dit sluit aan op de actuele hoofdbranch en maakt het eerdere verschil tussen repository en acceptatie geen nieuwe onderzoeksvraag meer.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/iteration_evidence.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/iteration_evidence.dart)

### Traceerbaarheid is verbeterd, maar historische onbekendheid blijft zichtbaar

De compacte regels tonen afzonderlijke beslisbronnen, waaronder ‘Evaluatie-agent (Afgeleid)’ en ‘Technische fout (Afgeleid)’. Bij de bekeken cycli stond de reden in het overzicht nog als ‘Onbekend’; het detail van cyclus 3 gaf wel de concretere uitleg dat een REVISE-oordeel was geregistreerd maar geen onderliggend criticusartefact beschikbaar was. Het overzicht is daardoor veel rustiger en eerlijker, maar informatieverlies in oudere gegevens kan niet volledig door presentatie worden opgelost.

Bronnen: [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md)

### Vergelijkbare intakepatronen ondersteunen gerichte context zonder zwaar formulier

GitHub Issue Forms ondersteunt instructietekst, enkelregelige invoer, tekstgebieden en validatie. Linear onderscheidt snelle standaardtemplates met placeholders van formelere form templates met verplichte velden. Deze patronen laten zien dat context gericht kan worden uitgevraagd, maar ondersteunen ook terughoudendheid: voor één optionele onderzoeksvraag is een uitgebreid meer-veldenformulier niet vanzelfsprekend nodig.

Bronnen: [https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-githubs-form-schema](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-githubs-form-schema), [https://linear.app/docs/issue-templates](https://linear.app/docs/issue-templates)

### Huidige applicatie

**Doel:** Product Factory maakt autonome productontwikkeling mogelijk voor de eigenaar van Product Factory en gekoppelde producten zoals HKH Autopilot. Het systeem onderzoekt productvragen, kiest en ontwerpt richtingen, vormt storykandidaten, levert geaccepteerd werk aan de Software Factory en verwerkt resultaten in volgende cycli. Het dashboard ondersteunt productscope, handmatige cyclusstart, beoordeling van eerdere cycli en beheer van kandidaten en leveringen.

**Wat ontbreekt:**
- De prominente handmatige startactie maakt de effectieve focus niet vooraf zichtbaar en biedt geen manier om een actuele eigenaarvraag mee te geven of te controleren.
- Het dashboard maakt achteraf niet expliciet onderscheid tussen een autonoom gekozen standaardfocus en een bewust door de eigenaar opgegeven opdracht.
- Bij historische cycli kan het overzicht terecht ‘Onbekend’ tonen terwijl het detail nog een beperkte technische verklaring bevat; volledige traceerbaarheid blijft afhankelijk van daadwerkelijk geregistreerde brondata.
- Productie kon inhoudelijk niet worden vergeleken met acceptatie, omdat een toegestaan Google-account vereist is.

### Verbetermogelijkheden

- Onderzoek een lichte startintake waarin de eigenaar één korte, optionele onderzoeksvraag kan meegeven en de autonome standaard zichtbaar blijft wanneer het veld leeg is.
- Toon vóór uitvoering de effectieve focus in gewone gebruikerstaal, zodat de eigenaar kan controleren of de cyclus autonoom kiest of een concrete aanleiding volgt.
- Behoud de prominente snelle start voor volledig autonome cycli; vergelijk bijvoorbeeld een compacte inline-uitbreiding, een korte bevestigingsdialoog en twee expliciete startkeuzes op begrijpelijkheid en foutgevoeligheid.
- Leg in het cyclusdetail vast welke herkomst de opdracht had—autonome standaard of eigenaarinput—zonder persoonsgegevens of context van andere producten op te slaan.
- Onderzoek of een meegegeven focus ook in de compacte cyclusregel herkenbaar moet zijn, of dat het detail voldoende is; voorkom dat het heringerichte hoofdscherm opnieuw overladen raakt.
- Gebruik bij ontbrekende historische redengegevens een consistente verklaring van de beperking, maar wek geen zekerheid door detailtekst naar een formele reden of beslisbron om te zetten.

### Inspiratiebronnen

- [GitHub Issue Forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-githubs-form-schema) — Laat zien hoe instructies, korte invoer, langere tekst en validatie gericht kunnen worden gecombineerd; bruikbaar als patroonbibliotheek, niet als aanleiding voor een volledig formulier.
- [Linear Issue Templates](https://linear.app/docs/issue-templates) — Maakt expliciet onderscheid tussen snelle standaardtemplates met placeholders en formelere form templates met verplichte velden. Dat onderscheid is relevant bij de keuze hoeveel frictie een handmatige Product Factory-start nodig heeft.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://github.com/robbertvdzon/product-factory) | 2026-08-16 | Publieke repository; via de publieke GitHub-license-endpoint is geen repositorylicentie aangetroffen. Hergebruikrechten zijn daarom onbekend. | Primaire bron voor de actuele productimplementatie en documentatie. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md) | 2026-08-16 | Onderdeel van de publieke repository zonder aangetroffen repositorylicentie; hergebruikrechten onbekend. | Beschrijft de handmatige en automatische start, de vrije focus, agentketen en dashboardflow. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart) | 2026-08-16 | Onderdeel van de publieke repository zonder aangetroffen repositorylicentie; hergebruikrechten onbekend. | Toont dat de frontendstart direct `startCycle(slug)` aanroept en bevestigt de actuele dashboardstructuur. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/iteration_evidence.dart) | 2026-08-16 | Onderdeel van de publieke repository zonder aangetroffen repositorylicentie; hergebruikrechten onbekend. | Ondersteunt de beoordeling van de compacte, productonafhankelijke cyclusbewijsweergave. |
| [bron](https://product-factory.vdzonsoftware.nl) | 2026-08-16 | Publiek bereikbare applicatiepagina; auteursrecht en overige hergebruikrechten niet vermeld en dus onbekend. | Primaire productieomgeving; liet zien dat inhoudelijke toegang authenticatie vereist. |
| [bron](https://product-factory-acceptance.vdzonsoftware.nl) | 2026-08-16 | Publiek raadpleegbare acceptatieapplicatie met synthetische data; auteursrecht en hergebruikrechten niet vermeld en dus onbekend. | Werkelijk genavigeerde omgeving voor beoordeling van hoofdscherm, cyclusdetail en Beheer. |
| [bron](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-githubs-form-schema) | 2026-08-16 | © GitHub; publieke documentatie. Specifieke hergebruiklicentie op de geraadpleegde pagina niet vastgesteld. | Publieke productspecificatie van gerichte invoer, instructies en validatie in intakeformulieren. |
| [bron](https://linear.app/docs/issue-templates) | 2026-08-16 | © Linear; publieke productdocumentatie. Specifieke hergebruiklicentie niet vastgesteld. | Vergelijkingsbron voor lichte placeholders versus gestructureerde form templates en verplichte velden. |

## Productbeslissing

Maak ‘Cyclus starten’ controleerbaar met één lichte startdialoog voor het actieve product. Toon daarin de autonome standaard als vooraf geselecteerde keuze en bied daarnaast één optioneel tekstveld voor een korte onderzoeksvraag van de eigenaar. Vóór uitvoering moet in gewone taal zichtbaar zijn welke opdracht effectief wordt gestart. Sla bij de cyclus alleen de effectieve opdracht en haar herkomst op als ‘Autonome standaard’ of ‘Eigenaarinput’, en toon beide achteraf in het bestaande cyclusdetail. Houd de compacte cyclusregels en de werking van andere producten ongewijzigd. Deze richting sluit aan op roadmap-epic theme-product-factory-0001 doordat zij de kernactie ‘Cyclus starten’ binnen de actieve productscope begrijpelijk en toetsbaar maakt.

**Waarom:** De directe startknop was logisch ontworpen voor minimale frictie en autonome werking, maar benut niet dat de runtime al een vrije focus ondersteunt en bewaart. Daardoor kan de eigenaar de actuele vraag vóór een handmatige start niet controleren of meegeven, terwijl de opdracht pas achteraf in het detail zichtbaar wordt. Een dialoog met één optionele vraag behoudt de snelle autonome standaard, voegt alleen noodzakelijke controle toe en voorkomt de zwaarte van een intakeformulier. De wijziging is klein, afzonderlijk te accepteren en terug te draaien. Er blijft onzekerheid of iedere handmatige start deze extra bevestiging prettig maakt; daarom moet acceptatie expliciet toetsen of een autonome start met hoogstens één bevestiging kan worden voltooid en of de effectieve opdracht vóór uitvoering ondubbelzinnig is.

### Prioriteiten
- Behoud de autonome standaard als snelste en vooraf gekozen route.
- Maak vóór uitvoering zichtbaar welk product en welke effectieve opdracht worden gestart.
- Sta één korte, optionele onderzoeksvraag toe zonder extra velden of verplichte eigenaarinput.
- Registreer en toon de herkomst van de opdracht eerlijk als ‘Autonome standaard’ of ‘Eigenaarinput’.
- Beperk de wijziging tot handmatige start en cyclusdetail; verander geen data of gedrag van HKH, HKH Autopilot, bestaande cycli of de Software Factory-koppeling.

### Besluiten
- **Open vanuit ‘Cyclus starten’ een compacte dialoog binnen de huidige actieve productscope.** — De huidige knop start onmiddellijk via `startCycle(slug)`. Een lokale dialoog maakt controle mogelijk zonder de heringerichte hoofdflow of productscope opnieuw op te bouwen.
- **Bied twee toestanden: de vooraf geselecteerde autonome standaard en een optionele korte onderzoeksvraag van de eigenaar.** — De functionele opzet kent al een vrije focus én een autonome standaard. Eén gerichte invoer volgt bovendien het lichte templatepatroon; een uitgebreid formulier is voor deze ene contextvraag niet gerechtvaardigd.
- **Toon vóór de definitieve start een leesbare samenvatting van product en effectieve opdracht.** — De opdracht is nu pas achteraf zichtbaar. De samenvatting voorkomt dat een lege, verouderde of onbedoelde eigenaarvraag ongemerkt wordt uitgevoerd en maakt de start zelfstandig toetsbaar.
- **Bewaar per nieuwe handmatig gestarte cyclus de effectieve opdracht en een gesloten herkomstlabel: ‘Autonome standaard’ of ‘Eigenaarinput’. Toon dit in het cyclusdetail naast ‘Opdracht’.** — Het detail is al het bestaande traceerpunt voor de opdracht. Een expliciet herkomstlabel maakt achteraf duidelijk of het systeem of de eigenaar de richting bepaalde, zonder dit af te leiden of persoonsgegevens vast te leggen.
- **Migreer oude cycli niet en voeg de opdracht niet toe aan de compacte bewijsregels.** — Historische brondata is niet altijd volledig en de compacte regels zijn juist bedoeld om het hoofdscherm rustig te houden. Het cyclusdetail biedt voldoende ruimte voor opdracht en herkomst; bestaande gegevens blijven onaangetast.

## UX-voorstel: Controleerbare handmatige cyclusstart

**Gebruikersdoel:** Als eigenaar wil ik voor het actieve product een autonome cyclus snel kunnen starten of één korte onderzoeksvraag kunnen meegeven, waarbij ik vóór uitvoering de effectieve opdracht kan controleren en achteraf de herkomst kan terugzien.

### Flow
1. De eigenaar activeert in het productoverzicht ‘Cyclus starten’.
2. Een compacte modale dialoog opent met het actieve product, bijvoorbeeld ‘product-factory’; de focus start op de dialoogtitel.
3. ‘Autonome standaard’ is vooraf geselecteerd. De dialoog legt uit dat Product Factory dan zelf de belangrijkste onbeantwoorde productvraag bepaalt.
4. De eigenaar kan desgewenst ‘Eigen onderzoeksvraag’ selecteren. Dan verschijnt één tekstveld voor een korte vraag; er verschijnen geen andere invoervelden.
5. De dialoog toont continu een samenvatting met het actieve product, de effectieve opdracht en de herkomst ‘Autonome standaard’ of ‘Eigenaarinput’.
6. Bij ‘Start cyclus’ wordt exact één cyclus gestart. Tijdens verwerking is de actie uitgeschakeld en wordt de voortgang toegankelijk gemeld.
7. Na succes sluit de dialoog en verschijnt een statusmelding met een link naar het cyclusdetail. Bij een fout blijven keuze en invoer behouden en kan opnieuw worden geprobeerd.
8. Het cyclusdetail toont bij nieuwe handmatig gestarte cycli ‘Opdracht’ en ‘Herkomst’. Oude cycli worden niet gemigreerd; ontbrekende herkomst wordt niet afgeleid.

### Wireframe

PRODUCTOVERZICHT
[Actief product: product-factory]                 [Cyclus starten]

Na activering:
┌──────────────────────────────────────────────────────────┐
│ Cyclus starten                                      [×] │
│ Product: product-factory                                │
│                                                        │
│ Kies de opdracht                                       │
│ (●) Autonome standaard                                 │
│     Product Factory kiest de belangrijkste open vraag. │
│ ( ) Eigen onderzoeksvraag                              │
│     [Korte onderzoeksvraag…                         ]  │
│     [0/300]                                            │
│                                                        │
│ Samenvatting                                           │
│ Product: product-factory                               │
│ Opdracht: Product Factory bepaalt de belangrijkste     │
│           onbeantwoorde productvraag.                  │
│ Herkomst: Autonome standaard                           │
│                                                        │
│ [Annuleren]                              [Start cyclus] │
└──────────────────────────────────────────────────────────┘

CYCLUSDETAIL
Opdracht: <effectieve opdracht>
Herkomst: Autonome standaard | Eigenaarinput

### Interactiehypotheses
- Als de dialoog opent, is ‘Autonome standaard’ geselecteerd en kan een autonome cyclus met maximaal één extra bevestigingsactie worden gestart. Toetsbaar met een component- of end-to-endtest.
- Als ‘Eigen onderzoeksvraag’ wordt geselecteerd en geldige tekst is ingevoerd, zijn samenvatting en startverzoek exact gelijk aan de getrimde invoer en is de herkomst ‘Eigenaarinput’. Toetsbaar met component- en API-contracttests.
- Als de eigenaarroute leeg of uitsluitend uit witruimte bestaat, kan geen lege eigenaaropdracht worden gestart; de interface toont een gekoppelde foutmelding. Toetsbaar met invoervalidatietests.
- Als tussen de twee keuzes wordt gewisseld, verandert de effectieve opdracht en herkomst direct en deterministisch; niet-actieve invoer wordt nooit onbedoeld verzonden. Toetsbaar met statetests.
- Als ‘Start cyclus’ herhaald wordt geactiveerd terwijl het verzoek loopt, ontstaat maximaal één cyclus. Toetsbaar met een end-to-endtest en idempotentiecontrole.
- Na een succesvolle gerichte start toont het cyclusdetail dezelfde effectieve opdracht en herkomst als in de voorafgaande samenvatting. Toetsbaar met een integratietest over start- en detail-API’s heen. Bestaande compacte cyclusregels blijven ongewijzigd via regressietests en snapshots.

### Toegankelijkheid
- De dialoog gebruikt correcte dialog-semantie, een programmatisch gekoppelde titel en focus trapping; Escape en ‘Annuleren’ sluiten zonder start.
- Bij openen gaat focus naar de titel of eerste keuze; bij sluiten keert focus terug naar ‘Cyclus starten’. De volledige flow werkt met Tab, Shift+Tab, pijltjestoetsen, Enter en Spatie.
- Keuzes vormen één benoemde radiogroep. Het tekstveld heeft een zichtbaar label, instructie, tekenlimiet en programmatisch gekoppelde foutmelding; placeholdertekst is niet het enige label.
- De samenvatting heeft een herkenbare kop en wordt bij wijzigingen begrijpelijk aangekondigd zonder overmatige live-regionmeldingen.
- Laadstatus, succes en fouten worden via passende status- of alertsemantiek gemeld. Focus gaat bij validatiefouten naar het eerste ongeldige element.
- Tekst, randen, focusindicatoren en interactieve toestanden voldoen minimaal aan WCAG 2.2 AA-contrast. Selectie wordt niet uitsluitend met kleur aangeduid.
- Geautomatiseerde toegankelijkheidstests controleren onder meer naam/rol/waarde, focusvolgorde, toetsenbordbediening, focusbehoud, zoom/reflow en kleurcontrast.

### Privacy
- Bewaar alleen operationele metadata van Product Factory: product-ID, effectieve opdracht, gesloten herkomstlabel, cyclus-ID en noodzakelijke tijd/statusmetadata.
- Vraag geen naam, e-mailadres of andere persoonsgegevens. De toelichting waarschuwt kort om geen persoonsgegevens, geheimen of gegevens van andere producten in de onderzoeksvraag op te nemen.
- Beperk de invoer tot 300 tekens en pas server-side dezelfde lengte- en inhoudsvalidatie toe; clientvalidatie alleen is onvoldoende.
- Koppel de opdracht uitsluitend aan het actieve product. Tests moeten aantonen dat invoer niet naar HKH, HKH Autopilot of andere productscope lekt.
- Neem vrije tekst niet op in algemene telemetry, analytics of foutlogs. Log zo nodig alleen cyclus-ID, product-ID, herkomst, lengte en technische foutcode.
- Toon de opgeslagen opdracht alleen binnen bestaande autorisatie voor het betreffende Product Factory-product. Oude cycli worden niet verrijkt of afgeleid uit andere bronnen.
- Geautomatiseerde privacytests controleren productscope-isolatie, toegangscontrole, logredactie, maximale invoerlengte en dat de API alleen toegestane operationele velden accepteert.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is klein, autonoom uitvoerbaar en geautomatiseerd toetsbaar. Scope, toegankelijkheid, productscheiding, idempotentie, foutafhandeling en terugwaartse compatibiliteit zijn voldoende afgebakend. Er is geen materieel conflict of reeds geleverd duplicaat.
- **WARNING · PRIVACY** — Het vrije tekstveld kan ondanks lengtebegrenzing door de eigenaar worden gebruikt voor persoonsgegevens, geheimen of gegevens van andere producten. De kandidaat beperkt opslag, autorisatie, logging en productscope afdoende voor deze MVP, maar een korte zichtbare invoerinstructie uit het UX-ontwerp blijft wenselijk; dit vereist geen menselijk besluit en blokkeert levering niet.
- **INFO · RIGHTS** — Voor de publieke repository en vergelijkingsdocumentatie zijn geen specifieke hergebruikrechten vastgesteld. De kandidaat gebruikt deze bronnen alleen als onderbouwing en patroonreferentie en vereist geen herkenbare overname van beschermde tekst of vormgeving.
- **INFO · CONSISTENCY** — De kandidaat bouwt expliciet voort op gepubliceerde story:78 en wijzigt bewust het daar behouden directe startgedrag. Dit is een gerichte vervolgwijziging, geen duplicaat of conflict.

## Geaccepteerde storykandidaten

### Maak de handmatige cyclusstart controleerbaar met een optionele onderzoeksvraag

_Sleutel: `controleerbare-handmatige-cyclusstart`_

Bouw voort op de actieve productscope uit story:78. Open vanuit ‘Cyclus starten’ een compacte dialoog voor het actieve product, met ‘Autonome standaard’ vooraf geselecteerd en daarnaast ‘Eigen onderzoeksvraag’ met één tekstveld van maximaal 300 tekens. Toon vóór uitvoering steeds het actieve product, de effectieve opdracht en het gesloten herkomstlabel ‘Autonome standaard’ of ‘Eigenaarinput’. Start per bevestiging maximaal één cyclus en bewaar bij nieuwe handmatig gestarte cycli exact die effectieve opdracht en herkomst. Toon beide achteraf in het bestaande cyclusdetail. Migreer oude cycli niet en wijzig de compacte cyclusregels, automatische starts, andere producten en de Software Factory-koppeling niet.

**Acceptatiecriteria**
- Activering van ‘Cyclus starten’ opent voor de huidige productslug een programmatisch benoemde modale dialoog; ‘Autonome standaard’ is geselecteerd en een geautomatiseerde toetsenbordtest bevestigt focusinsluiting, sluiten met Escape en focusherstel naar de startknop.
- De autonome route toont vóór uitvoering het actieve product, de effectieve standaardopdracht en ‘Herkomst: Autonome standaard’ en start met één bevestiging exact één cyclus voor die productslug.
- Selectie van ‘Eigen onderzoeksvraag’ toont uitsluitend één zichtbaar gelabeld tekstveld; na trimmen accepteert client en server maximaal 300 tekens, terwijl lege of alleen uit witruimte bestaande invoer de start blokkeert met een programmatisch gekoppelde foutmelding.
- Bij eigenaarinput zijn de effectieve opdracht in de samenvatting, het startverzoek en de opgeslagen opdracht bytegelijk aan dezelfde getrimde invoer en wordt uitsluitend ‘Herkomst: Eigenaarinput’ opgeslagen; niet-geselecteerde invoer wordt nooit verzonden.
- Tijdens een lopend startverzoek is de startactie uitgeschakeld en garandeert een geautomatiseerde integratietest dat herhaalde activering maximaal één cyclus creëert; bij een fout blijven keuze en invoer behouden en wordt een toegankelijke foutstatus getoond.
- Na een geslaagde start toont het bestaande cyclusdetail voor de nieuwe cyclus exact dezelfde effectieve opdracht en hetzelfde gesloten herkomstlabel als de voorafgaande samenvatting; ontbrekende herkomst bij bestaande cycli wordt niet afgeleid of teruggevuld.
- Geautomatiseerde regressietests bevestigen dat automatische starts, bestaande cycli, compacte cyclusregels, andere productslugs en Software Factory-koppelingen functioneel en inhoudelijk ongewijzigd blijven.
- Geautomatiseerde beveiligings- en privacytests bevestigen dat vrije opdrachttekst niet in algemene telemetry of foutlogs verschijnt, uitsluitend binnen de bestaande autorisatie van het gekozen product leesbaar is en niet naar een andere productscope lekt.

Bronnen: [https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart), [https://product-factory-acceptance.vdzonsoftware.nl](https://product-factory-acceptance.vdzonsoftware.nl), [https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-githubs-form-schema](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-githubs-form-schema), [https://linear.app/docs/issue-templates](https://linear.app/docs/issue-templates)

Afhankelijkheden: story:78 (herkend als bestaande stories: 78)

Risico's: De extra dialoog voegt één bevestigingsactie toe aan iedere handmatige autonome start., Vrije tekst kan gevoelige informatie bevatten; lengtebegrenzing, productscope-isolatie, bestaande autorisatie en logredactie moeten daarom zowel client- als server-side worden geborgd., Zonder idempotente afhandeling kan herhaalde activering dubbele cycli veroorzaken., De exacte formulering van de autonome standaard moet één gedeelde bron gebruiken om verschillen tussen samenvatting, opslag en detail te voorkomen.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
