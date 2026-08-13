---
product: product-factory
artifact_type: research
run_id: shadow-product-factory-0043
date: 2026-08-13
status: approved
sources:
  - https://github.com/robbertvdzon/product-factory/blob/main/README.md
  - https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md
  - https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart
  - https://product-factory-acceptance.vdzonsoftware.nl
  - https://www.nngroup.com/articles/progressive-disclosure/
  - https://docs.github.com/en/actions/how-tos/monitor-workflows/view-workflow-run-history
  - https://argo-workflows.readthedocs.io/en/latest/fields/
  - https://argo-workflows.readthedocs.io/en/latest/workflow-archive/
  - https://www.w3.org/TR/WCAG22/
  - https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html
---
# Productcyclus 43

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

Belangrijkste nog onbeantwoorde productvraag: hoe kan het hoofdscherm per cyclus direct uitkomst, beslisser/reden en voortgekomen stories tonen, terwijl technische procesinformatie en bewijs bereikbaar blijven zonder het overzicht te overladen? De repository bevestigt dat de benodigde informatie nu over een informatierijke cycluskaart, uitklapbare opbrengstgroepen en een detailvenster is verdeeld. Alleen handmatige annulering heeft al een expliciet beslisrecord; andere uitkomsten worden nog conservatief afgeleid. De acceptatieomgeving is geraadpleegd, maar visuele inspectie kon niet worden voltooid: zowel Playwright Chromium als lokaal Chrome werden door de macOS-processandbox afgebroken voordat een screenshot ontstond. Daarom zijn geen onbewezen live-UI-waarnemingen opgenomen.

### Product Factory orkestreert de volledige productcyclus, maar bouwt zelf geen productcode

De applicatie organiseert voor geregistreerde producten achtereenvolgens onderzoek, productkeuze, UX, storyvorming en kritiek, publiceert goedgekeurde dossiers en kandidaten en volgt vervolgens uitvoering en evaluatie via Software Factory. De primaire gebruiker is de producteigenaar die autonome cycli start, resultaten beoordeelt en blokkades of vragen afhandelt.

Bronnen: [https://github.com/robbertvdzon/product-factory/blob/main/README.md](https://github.com/robbertvdzon/product-factory/blob/main/README.md), [https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md)

### De hoofdweergave beantwoordt de kernvragen nog niet als één scanbaar geheel

Een cycluskaart bevat momenteel onder meer status, rol, starttijd, doorlooptijd, aantallen, revisierondes, uitkomstreden en criticusoordeel. Opbrengsten staan achter een afzonderlijke uitklapactie met twee groepen; de beslisbron is een andere knop die het detail opent. Deze verdeling verklaart waarom een eigenaar meerdere waarden en interacties nodig heeft om vast te stellen wat een cyclus opleverde en waarom hij zo eindigde.

Bronnen: [https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart)

### Traceerbaarheid is alleen voor handmatige annulering expliciet opgeslagen

De huidige documentatie beschrijft één privacy-minimaal beslisrecord voor geslaagde handmatige annulering. Zonder zo'n record leidt de frontend de beslisbron af uit status, criticVerdict en errorMessage en toont zij expliciet 'Afgeleid' of 'Onbekend'. Voor alle terminale paden bestaat dus nog geen uniforme, expliciete en rechtstreeks bewijsgekoppelde provenance.

Bronnen: [https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart)

### De bestaande detailweergave is geschikt als bewijslaag, maar niet als primair overzicht

Het cyclusdetail bevat de opdracht, vijf agentstappen, tijden, fouten, dossier en leesbare rolresultaten; technische JSON is waar mogelijk verder ingeklapt. Dat ondersteunt onderzoek en diagnose, maar de omvang maakt het minder geschikt voor de snelle hoofdtaak van de eigenaar. De huidige scheiding biedt wel een basis voor progressive disclosure: kerninformatie bovenaan, bewijs op verzoek.

Bronnen: [https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md), [https://www.nngroup.com/articles/progressive-disclosure/](https://www.nngroup.com/articles/progressive-disclosure/)

### Een uniforme cyclusregel vereist eerst een stabiel samenvattingscontract

De huidige statussen maken onderscheid tussen ACCEPTED, NEEDS_REVISION, REJECTED, NO_CHANGE en FAILED; daarnaast zijn kandidaatacceptatie en levering afzonderlijke processen. Eén overzichtsregel kan daarom niet betrouwbaar uit alleen de technische cyclusstatus worden samengesteld. Een expliciete, privacy-minimale samenvatting per terminale cyclus moet uitkomst, bron, concrete reden en bewijsreferentie eenduidig vastleggen en de opbrengst afzonderlijk koppelen.

Bronnen: [https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md), [https://argo-workflows.readthedocs.io/en/latest/fields/](https://argo-workflows.readthedocs.io/en/latest/fields/)

### Vergelijkbare workflowproducten scheiden recente runs van run-details

GitHub Actions presenteert recente workflowruns als een lijst en opent per gekozen run een samenvatting, waarna jobs, stappen en logs verder kunnen worden bekeken. Argo bewaart eveneens een compacte lifecyclefase en menselijk bericht naast gedetailleerde nodes, resultaten en artefacten. Dit ondersteunt het patroon van een scanbaar overzicht met een afzonderlijke bewijslaag, zonder dat hun vormgeving hoeft te worden gekopieerd.

Bronnen: [https://docs.github.com/en/actions/how-tos/monitor-workflows/view-workflow-run-history](https://docs.github.com/en/actions/how-tos/monitor-workflows/view-workflow-run-history), [https://argo-workflows.readthedocs.io/en/latest/fields/](https://argo-workflows.readthedocs.io/en/latest/fields/), [https://argo-workflows.readthedocs.io/en/latest/workflow-archive/](https://argo-workflows.readthedocs.io/en/latest/workflow-archive/)

### Vereenvoudiging mag toegankelijkheid van acties en dynamische status niet verminderen

Wanneer kaartinhoud of status dynamisch verandert, moet die status programmatisch bepaalbaar zijn zonder focus te verplaatsen. Tekst vraagt bij WCAG 2.2 AA normaal minimaal 4,5:1 contrast; bediening moet toetsenbordtoegankelijk en zichtbaar gefocust blijven. Deze eisen gelden ook wanneer meerdere huidige kaartacties worden samengevoegd of secundair gemaakt.

Bronnen: [https://www.w3.org/TR/WCAG22/](https://www.w3.org/TR/WCAG22/), [https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html](https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html)

### Huidige applicatie

**Doel:** Product Factory stelt producteigenaren in staat autonome productontwikkeling voor Product Factory zelf en andere geregistreerde producten te organiseren. Het systeem onderzoekt productvragen, kiest richting, ontwerpt UX, vormt en beoordeelt storykandidaten, levert geaccepteerd werk aan Software Factory en gebruikt uitvoeringsresultaten in volgende cycli.

**Wat ontbreekt:**
- Het hoofdscherm verdeelt de drie eigenaarsvragen — wat was de uitkomst, waarom/door wie, en welke stories kwamen eruit — over verschillende waarden, uitklapacties en het detailvenster.
- Alleen handmatige annulering heeft een expliciet beslisrecord; andere terminale uitkomsten gebruiken afgeleide provenance, inclusief een onbekende fallback.
- Een cyclusstatus alleen beschrijft niet volledig de productopbrengst: individuele kandidaten kunnen verschillen en leveringen hebben een eigen vervolgstatus.
- De huidige kaart toont veel operationele metadata op hetzelfde niveau als de eigenaarsinformatie, waardoor de visuele prioriteit van kerninformatie onvoldoende scherp is.
- De live bruikbaarheid en navigatie konden in deze onderzoeksrun niet betrouwbaar visueel worden vastgesteld doordat de beschikbare headless browsers lokaal door de processandbox werden beëindigd. Dit is een onderzoekslacune, geen geconstateerd applicatiedefect.

### Verbetermogelijkheden

- Onderzoek één stabiel, privacy-minimaal terminale-cycluscontract met afzonderlijke velden voor uitkomst, actorType, mechanism, begrensde reasonCode/ownerSummary, decidedAt en verplichte evidenceRef; maak bij vroege technische uitval atomair een minimaal intern bewijsartefact.
- Onderzoek een compacte cyclusrij die primair datum/status, concrete reden en beslisbron toont, met een direct herkenbare opbrengstsamenvatting zoals aantallen of korte storytitels; houd runtimefasen, rolstappen, JSON en fouten secundair.
- Behoud het bestaande detail als bewijslaag en laat kaart en detail aantoonbaar dezelfde evidenceRef gebruiken, zodat vereenvoudiging geen nieuwe tegenstrijdigheid introduceert.
- Maak expliciet onderscheid tussen cyclusuitkomst, kandidaatuitkomst en leveringsstatus. Daarmee kan de eigenaar bijvoorbeeld zien dat een richting is gekozen terwijl een story nog wacht of wordt uitgevoerd.
- Toets met representatieve fixtures minimaal ACCEPTED, NEEDS_REVISION, REJECTED, NO_CHANGE, technische uitval vóór bestaand artefact, handmatige annulering, gedeeltelijk geaccepteerde kandidaten en historische records zonder expliciet beslisrecord.
- Meet na een eventuele wijziging of de eigenaar zonder detailnavigatie correct kan antwoorden: wat leverde de laatste cyclus op, waarom eindigde hij zo, wie/wat besliste en welke stories zijn ontstaan.
- Borg in geautomatiseerde browsertests toetsenbordvolgorde, focusherstel, toegankelijke namen met cycluscontext, statusaankondiging en WCAG 2.2 AA-contrast voor alle nieuwe tekst- en interactiestaten.
- Plan een afzonderlijke live visuele acceptatiecontrole zodra een uitvoeromgeving beschikbaar is waarin Chromium-processen wel mogen starten; gebruik die controle om informatiedichtheid, responsieve reflow en het beheergedeelte daadwerkelijk te beoordelen.

### Inspiratiebronnen

- [GitHub Actions workflow run history](https://docs.github.com/en/actions/how-tos/monitor-workflows/view-workflow-run-history) — Toont recente runs eerst als selecteerbaar overzicht en ontsluit runsummary, jobs, stappen en logs pas na selectie.
- [Argo Workflows lifecyclemodel en archive](https://argo-workflows.readthedocs.io/en/latest/fields/) — Scheidt een compacte lifecyclefase en menselijk bericht van gedetailleerde nodes, outputs en artefacten; bruikbaar als conceptuele inspiratie voor overzicht versus bewijs.
- [Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/) — Onderbouwt het direct tonen van frequente kerninformatie en het op verzoek ontsluiten van zeldzame technische details, mits de overgang duidelijk gelabeld blijft.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/README.md) | 2026-08-13 | Publieke repository; in de geraadpleegde hoofdboom is geen LICENSE-bestand aangetroffen, dus hergebruikrechten zijn onbekend. | Primaire beschrijving van doel, verantwoordelijkheden, opslag en relatie met Software Factory. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md) | 2026-08-13 | Publieke repository zonder aangetroffen LICENSE-bestand; hergebruikrechten onbekend. | Primaire en gedetailleerde bron voor actuele cycluswerking, dashboardinhoud, provenance en detailweergave. |
| [bron](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart) | 2026-08-13 | Publieke broncode zonder aangetroffen LICENSE-bestand; hergebruikrechten onbekend. | Primaire implementatiebron voor de actuele Flutter-dashboardstructuur en interacties. |
| [bron](https://product-factory-acceptance.vdzonsoftware.nl) | 2026-08-13 | Publiek toegankelijke acceptatieomgeving; auteurs- en hergebruikrechten onbekend. | Aangewezen primaire bron voor live bruikbaarheid. De pagina werd benaderd, maar de verplichte screenshotinspectie werd lokaal geblokkeerd doordat beide Chromium-processen vóór paginalading door de macOS-sandbox werden beëindigd. |
| [bron](https://www.nngroup.com/articles/progressive-disclosure/) | 2026-08-13 | Copyright Nielsen Norman Group; All Rights Reserved. Alleen functionele inzichten geparafraseerd. | Onderbouwing voor het scheiden van frequente kerntaken en zelden benodigde technische details. |
| [bron](https://docs.github.com/en/actions/how-tos/monitor-workflows/view-workflow-run-history) | 2026-08-13 | Copyright GitHub, Inc.; gebruik onder de voorwaarden van GitHub Docs. Alleen het interactiepatroon als inspiratie beschreven. | Vergelijkbaar publiek voorbeeld van een recente-runlijst met afzonderlijke samenvatting, stappen en logs. |
| [bron](https://argo-workflows.readthedocs.io/en/latest/fields/) | 2026-08-13 | Argo Workflows-project is Apache-2.0-gelicenseerd; documentatie valt onder de projectrepositoryvoorwaarden. | Vergelijkingsbron voor scheiding tussen lifecyclefase, menselijk statusbericht, nodes, resultaten en artefacten. |
| [bron](https://argo-workflows.readthedocs.io/en/latest/workflow-archive/) | 2026-08-13 | Argo Workflows-project is Apache-2.0-gelicenseerd; documentatie valt onder de projectrepositoryvoorwaarden. | Vergelijkingsbron voor blijvende toegang tot afgeronde workflowstatus, resultaten en bewijsartefacten. |
| [bron](https://www.w3.org/TR/WCAG22/) | 2026-08-13 | W3C-document onder de W3C Document License. | Normatieve toegankelijkheidsbron voor contrast, toetsenbordbediening en statusberichten. |
| [bron](https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html) | 2026-08-13 | W3C-document onder de W3C Document License; informatieve toelichting, niet normatief. | Concrete toelichting op zichtbaarheid, omvang en contrast van toetsenbordfocus. |

## Productbeslissing

Introduceer als eerstvolgende, geïsoleerde stap één compacte cyclusregel op het hoofdscherm voor uitsluitend afgeronde cycli. De regel toont datum, cyclusuitkomst, concrete reden, beslisbron en een afzonderlijke opbrengstsamenvatting met aantal voortgekomen stories. Gebruik bestaande gegevens zonder migratie: expliciete beslisgegevens waar aanwezig en anders een zichtbaar als ‘Afgeleid’ of ‘Onbekend’ gemarkeerde bron. Eén actie ‘Bekijk bewijs’ opent het bestaande detailvenster. Laat actieve cycli en andere producten ongemoeid.

**Waarom:** Deze richting maakt de drie belangrijkste eigenaarsvragen in één scanbare regel zichtbaar en draagt daardoor direct bij aan roadmap-epic 0001. Tegelijk maakt zij het resterende provenanceprobleem uit epic 0002 eerlijk zichtbaar, zonder nu al een risicovol nieuw opslagcontract of migratie te introduceren. Het huidige gedrag is verklaarbaar: cycluskaarten groeiden mee met operationele informatie, opbrengsten kregen een aparte uitklapactie en bewijs kwam in het detailvenster terecht. De kleine wijziging herschikt alleen bestaande presentatie. Ze is daardoor afzonderlijk te beoordelen en eenvoudig terug te draaien. Onzekerheid blijft bestaan over de informatiedichtheid in de live interface, omdat visuele inspectie van de acceptatieomgeving niet lukte; daarom hoort responsieve en visuele acceptatie expliciet bij de uitvoering.

### Prioriteiten
- Definieer één eenduidig presentatiemodel voor een afgeronde cyclusregel: datum, uitkomst, reden, beslisbron, storyaantal en bewijsactie.
- Gebruik dezelfde bestaande bronvelden en afleidingslogica als het detailvenster, zodat overzicht en bewijslaag geen nieuwe tegenstrijdigheid introduceren.
- Maak provenance expliciet eerlijk: toon de geregistreerde actor indien beschikbaar en anders letterlijk ‘Afgeleid’ of ‘Onbekend’; suggereer geen menselijke beslissing zonder bewijs.
- Houd cyclusuitkomst en storyopbrengst visueel en semantisch gescheiden; een afgeronde cyclus betekent niet automatisch dat alle kandidaten geaccepteerd of geleverd zijn.
- Beperk de eerste oplevering tot terminale cycli en bestaande data; geen migratie, authenticatiewijziging of aanpassing van Software Factory-koppelingen en geen wijziging aan hkh of hkh-autopilotdata of -gedrag als onderdeel van deze richting. Alleen generieke dashboardcode mag worden aangepast waar dat nodig is om Product Factory-cycli zo te presenteren, zonder andere producten functioneel te veranderen. Als productscheiding in het huidige dashboard niet veilig mogelijk is, stop de implementatie

### Besluiten
- **Vervang voor afgeronde Product Factory-cycli de informatierijke kaart door een compacte, scanbare regel; behoud het bestaande detail als bewijslaag.** — De kerninformatie is nu verdeeld over kaartwaarden, een opbrengstuitklapper en een detailactie. Progressive disclosure ondersteunt het direct tonen van frequente eigenaarsinformatie en het secundair houden van technische stappen, JSON en fouten.
- **Toon per regel zowel de cyclusuitkomst als een afzonderlijk storyaantal.** — De technische cyclusstatus beschrijft niet volledig wat uit een cyclus voortkwam; kandidaatacceptatie en levering zijn afzonderlijke processen. De scheiding voorkomt dat een status ten onrechte als story- of leveringsstatus wordt gelezen.
- **Gebruik in deze stap geen nieuw persistent besliscontract; toon bestaande expliciete provenance en label iedere fallback zichtbaar als ‘Afgeleid’ of ‘Onbekend’.** — Alleen handmatige annulering heeft momenteel een expliciet beslisrecord. Een uniform contract voor alle terminale paden zou opslag- en procesgedrag wijzigen en is groter en minder omkeerbaar dan de gewenste eerste UI-stap. Eerlijke fallbacklabels voorkomen schijnzekerheid.
- **Laat ‘Bekijk bewijs’ naar het bestaande cyclusdetail leiden en verwijder daar in deze stap geen informatie.** — Het detail bevat al opdracht, agentstappen, tijden, fouten, dossier en rolresultaten. Het is daarmee geschikt als bewijslaag, terwijl vergelijkbare workflowproducten recente runs compact tonen en details na selectie ontsluiten.
- **Accepteer de wijziging alleen met representatieve fixtures en toegankelijke interactietests.** — Test minimaal ACCEPTED, NEEDS_REVISION, REJECTED, NO_CHANGE, FAILED, handmatige annulering, gedeeltelijk geaccepteerde kandidaten en historische records zonder beslisrecord. Borg daarnaast toetsenbordbediening, zichtbare focus, programmatisch bepaalbare dynamische status en voldoende contrast. Laat browsertests in Product Factory en Software Factory autonoom uitvoeren; een testomgeving die geen browser kan starten is een infrastructuurblokkade en geen taak voor de eigenaar.

## UX-voorstel: Afgeronde Product Factory-cyclus scannen en bewijs openen

**Gebruikersdoel:** Als producteigenaar wil ik op het hoofdscherm direct zien wat een afgeronde Product Factory-cyclus opleverde, waarom en door wie of wat die uitkomst is bepaald, en hoeveel stories eruit voortkwamen, met toegang tot het bestaande bewijsdetail.

### Flow
1. De gebruiker opent het hoofdscherm van Product Factory.
2. Het dashboard toont actieve cycli ongewijzigd en presenteert uitsluitend afgeronde Product Factory-cycli als compacte regels.
3. De gebruiker scant per regel de datum, cyclusuitkomst, concrete reden, beslisbron en afzonderlijke storyopbrengst.
4. Als expliciete beslisgegevens ontbreken, ziet de gebruiker bij de beslisbron ondubbelzinnig het label ‘Afgeleid’ of ‘Onbekend’.
5. De gebruiker activeert ‘Bekijk bewijs’ met muis, toetsenbord of schermlezer.
6. Het bestaande cyclusdetail opent met opdracht, agentstappen, tijden, fouten, dossier en rolresultaten.
7. Na sluiten van het detail keert de focus terug naar ‘Bekijk bewijs’ van dezelfde cyclusregel.

### Wireframe

HOOFDSCHERM — PRODUCT FACTORY

Afgeronde cycli
┌──────────────────────────────────────────────────────────────────────────────┐
│ 12 aug 2026                                                                 │
│ [GEACCEPTEERD]  Richting voldoet aan de gestelde criteria                   │
│ Beslisbron: Criticus (Afgeleid)                                              │
│ Opbrengst: 3 voortgekomen stories                    [Bekijk bewijs]         │
└──────────────────────────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────────────────────────┐
│ 11 aug 2026                                                                 │
│ [MISLUKT]  Technische cyclusfout                                             │
│ Beslisbron: Onbekend                                                         │
│ Opbrengst: 0 voortgekomen stories                    [Bekijk bewijs]         │
└──────────────────────────────────────────────────────────────────────────────┘

Smalle viewport, per regel onder elkaar:
12 aug 2026
[GEACCEPTEERD]
Richting voldoet aan de gestelde criteria
Beslisbron: Criticus (Afgeleid)
Opbrengst: 3 voortgekomen stories
[Bekijk bewijs]

BEWIJSDETAIL — bestaand venster
┌──────────────────────────────────────────────┐
│ Cyclusbewijs                           [Sluit]│
│ Opdracht · agentstappen · tijden · fouten    │
│ Dossier · rolresultaten · technische details │
└──────────────────────────────────────────────┘

### Interactiehypotheses
- Wanneer datum, uitkomst, reden, beslisbron en storyaantal zonder uitklappen in één regel staan, kan een geautomatiseerde test voor iedere terminale fixture alle vijf waarden in dezelfde semantische rij vinden.
- Wanneer cyclusuitkomst en storyopbrengst afzonderlijke labels en toegankelijke namen hebben, verwarren geautomatiseerde semantische tests een geaccepteerde cyclus niet met geaccepteerde of geleverde stories.
- Wanneer expliciete provenance ontbreekt, bevat de zichtbare én toegankelijke tekst exact ‘Afgeleid’ of ‘Onbekend’; tests mogen dan geen onbewezen menselijke actor aantreffen.
- Wanneer ‘Bekijk bewijs’ het bestaande detail opent, komen de samenvattingswaarden overeen met dezelfde bronvelden en afleidingslogica in het detail; contracttests vergelijken beide representaties per fixture.
- Wanneer het detail sluit, wordt de focus programmatisch hersteld naar de bewijsactie van de geopende cyclus; een browsertest controleert dit zonder menselijke beoordeling.
- De compacte regel blijft bij smalle viewports leesbaar zonder horizontaal scrollen of overlappende tekst; geautomatiseerde screenshots en layout-asserties toetsen vaste representatieve viewportbreedtes en tekstvergroting tot 200%. Mission-critical inhoud wordt niet afgekapt zonder toegankelijke volledige tekstondersteuning via een expliciete uitklap of volledige tekst in de regel.

### Toegankelijkheid
- Gebruik per cyclus een semantisch gegroepeerde rij met een unieke toegankelijke naam waarin datum en uitkomst voorkomen.
- Presenteer datum, uitkomst, reden, beslisbron en opbrengst als gelabelde tekst; vertrouw niet uitsluitend op kleur, positie of pictogrammen.
- Maak ‘Bekijk bewijs’ een echte knop met cycluscontext in de toegankelijke naam, bijvoorbeeld ‘Bekijk bewijs voor cyclus van 12 augustus 2026’.
- Hanteer een logische toetsenbordvolgorde, zichtbare focus en focuscontrast volgens WCAG 2.2; alle acties moeten zonder aanwijzer bedienbaar zijn.
- Open het bewijsdetail als correct benoemd dialoogvenster, plaats de focus bij openen voorspelbaar in het venster, begrens de focus zolang het modaal is en herstel die bij sluiten.
- Kondig asynchrone wijzigingen in cyclusstatus of opbrengst programmatisch aan via een passende statusregio zonder de focus te verplaatsen.
- Borg minimaal 4,5:1 contrast voor normale tekst en voldoende contrast voor statusindicatoren, focusmarkering en bediening in alle toestanden.
- Voer geautomatiseerde semantiek-, toetsenbord-, focus-, contrast- en responsiviteitstests uit voor ACCEPTED, NEEDS_REVISION, REJECTED, NO_CHANGE, FAILED, annulering, gedeeltelijke kandidaatacceptatie en ontbrekende provenance.

### Privacy
- Toon uitsluitend operationele metadata van Product Factory: cyclusdatum, uitkomst, begrensde reden, beslisbron en storyaantal.
- Neem geen persoonsgegevens, vrije gebruikersinvoer, gegevens van andere producten of inhoud uit hkh en hkh-autopilot op in de cyclusregel.
- Gebruik bestaande beslisgegevens alleen wanneer ze expliciet zijn vastgelegd; toon anders ‘Afgeleid’ of ‘Onbekend’ en construeer geen persoonsidentiteit.
- Beperk de reden tot bestaande, voor presentatie geschikte operationele tekst of een begrensde redenclassificatie; toon geen tokens, secrets, prompts, stacktraces of ongeschoonde foutinhoud op het hoofdscherm.
- Laat gevoelige technische diagnostiek uitsluitend in de bestaande bewijslaag staan en behoud daar de bestaande toegangsbeperking en redactie.
- Controleer met fixtures en statische assertions dat regels geen velden van andere producten, e-mailadressen, namen, access tokens of vrije foutpayloads renderen.
- Deze MVP introduceert geen nieuwe opslag, tracking, telemetrie, authenticatiewijziging of koppeling met persoonsgegevens.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is klein, geïsoleerd, terugdraaibaar en volledig agent-uitvoerbaar. Hij gebruikt gepubliceerde bestaande gegevens en classificatie, houdt andere producten en actieve cycli buiten scope, voorkomt schijnprovenance en bevat geautomatiseerde privacy- en toegankelijkheidstoetsing. Er is geen materieel probleem dat veilige bouw of toetsing van de MVP verhindert.
- **WARNING · CONSISTENCY** — Voor historische cycli met een ontbrekende of lege bestaande presentatiereden specificeert de kandidaat geen exacte zichtbare fallback. Dit blokkeert de bouw niet, maar een vaste neutrale waarde zoals ‘Geen reden beschikbaar’ zou de vijf verplichte velden en fixtures deterministischer maken.
- **INFO · SOURCE** — De primaire repositorybronnen zijn publiek maar hebben volgens de aangeleverde bronregistratie geen aangetroffen licentie. De kandidaat gebruikt ze als productspecifieke implementatiebron en kopieert geen beschermde externe vormgeving of tekst; daardoor ontstaat voor deze wijziging geen materieel rechtenprobleem.
- **INFO · SCOPE** — Er is gedeeltelijke overlap met story:64, maar geen exact reeds geleverd resultaat: deze kandidaat vervangt alleen voor terminale Product Factory-cycli de uitklapbare kaart door een compacte bewijsregel en behoudt story:64 als expliciete gegevensbasis.

## Geaccepteerde storykandidaten

### Toon afgeronde Product Factory-cycli als compacte bewijsregels

_Sleutel: `compacte-afgeronde-product-factory-cycli`_

Bouw voort op story:64 en vervang uitsluitend de uitklapbare kaarten van terminale Product Factory-cycli op het hoofdscherm door compacte, niet-uitklapbare regels. Iedere regel toont in afzonderlijk gelabelde velden: datum, cyclusuitkomst, concrete bestaande presentatiereden, beslisbron en het aantal aantoonbaar gekoppelde voortgekomen stories uit de reeds geladen gegevens. Gebruik voor beslisbron exact dezelfde bestaande expliciete gegevens en conservatieve classificatie als story:57 en story:60; ontbrekende expliciete provenance blijft zichtbaar gekwalificeerd als ‘Afgeleid’ of ‘Onbekend’. Eén echte knop ‘Bekijk bewijs’ opent het bestaande cyclusdetail. Actieve cycli, cycli van andere producten, het detailvenster, onderliggende koppellogica en Software Factory-leveringen blijven ongewijzigd. Er komen geen nieuwe API’s, opslag, migraties, telemetrie of proceswijzigingen.

**Acceptatiecriteria**
- Uitsluitend terminale Product Factory-cycli met status ACCEPTED, NEEDS_REVISION, REJECTED, NO_CHANGE, FAILED of handmatig geannuleerd worden als compacte regels gerenderd; geautomatiseerde widgettests bewijzen dat actieve cycli en cycli van andere producten hun bestaande weergave behouden.
- Iedere compacte regel bevat binnen één semantisch gegroepeerde container zichtbare, afzonderlijk gelabelde waarden voor datum, cyclusuitkomst, reden, beslisbron en storyaantal; tests verifiëren deze vijf waarden voor representatieve fixtures van iedere ondersteunde terminale status.
- Het storyaantal gebruikt uitsluitend de bestaande expliciete product- en cycluskoppeling uit story:64 en wordt aangeduid als gekoppelde opbrengst, zodat het niet als acceptatie- of leveringsstatus kan worden gelezen; ontbrekende of ambigue koppelingen worden niet meegeteld.
- De beslisbron hergebruikt zonder eigen mappinglogica de classificatie uit story:57 en de expliciete handmatige-annuleringsgegevens uit story:60; fixtures zonder expliciet record tonen zichtbaar en semantisch ‘Afgeleid’ of ‘Onbekend’ en tonen nooit een onbewezen menselijke beslisser.
- De reden wordt uitsluitend uit de bestaande, voor presentatie gebruikte operationele reden gehaald; tests bewijzen dat tokens, prompts, stacktraces, ruwe foutpayloads, persoonsgegevens en gegevens van andere producten niet in de compacte regel verschijnen.
- De knop ‘Bekijk bewijs’ heeft een toegankelijke naam met cycluscontext, opent het bestaande detail van precies dezelfde cyclus en herstelt na sluiten programmatisch de focus naar dezelfde knop; een geautomatiseerde toetsenbordtest verifieert openen, focusbegrenzing, sluiten en focusherstel.
- Geautomatiseerde tests op representatieve smalle en brede viewports en bij 200% tekstvergroting bewijzen dat de vijf kernwaarden en bewijsactie zonder horizontaal scrollen, overlap of ontoegankelijke afkapping bruikbaar blijven; semantiek-, focus- en contrastcontroles voldoen aan WCAG 2.2 AA.

Bronnen: [https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md](https://github.com/robbertvdzon/product-factory/blob/main/docs/architecture/functioneel-overzicht.md), [https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart](https://github.com/robbertvdzon/product-factory/blob/main/dashboard-frontend/lib/main.dart), [https://www.nngroup.com/articles/progressive-disclosure/](https://www.nngroup.com/articles/progressive-disclosure/), [https://www.w3.org/TR/WCAG22/](https://www.w3.org/TR/WCAG22/), [https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html](https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html)

Afhankelijkheden: story:64, story:57, story:60 (herkend als bestaande stories: 64, 57, 60)

Risico's: De compacte regel vervangt voor afgeronde Product Factory-cycli de uitklapbare storytitelweergave uit story:64; het bestaande detail moet voldoende toegang tot bewijs en opbrengsten behouden zonder gekoppelde informatie onbereikbaar te maken., Historische cycli kunnen onvolledige reden- of provenancegegevens bevatten; conservatieve fallbacks moeten schijnzekerheid en nieuwe tegenstrijdigheden voorkomen., De informatiedichtheid en responsieve reflow konden tijdens het onderzoek niet live visueel worden beoordeeld; geautomatiseerde viewport-, tekstvergrotings- en screenshottests moeten dit uitvoeringsrisico afdekken., Een onvoldoende betrouwbare productscheiding kan andere producten functioneel raken; als terminale Product Factory-cycli niet deterministisch kunnen worden geselecteerd met bestaande gegevens, mag de compacte weergave niet worden geactiveerd.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
