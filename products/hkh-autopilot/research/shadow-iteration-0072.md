---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0072
date: 2026-08-14
status: approved
sources:
  - https://github.com/robbertvdzon/hkh-autopilot
  - https://hkh-autopilot.vdzonsoftware.nl
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl
  - https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/
  - https://dera.netwerkdigitaalerfgoed.nl/index.php/Linked_Data
  - https://dera.netwerkdigitaalerfgoed.nl/index.php/Doelen
  - https://netwerkdigitaalerfgoed.nl/nationale-strategie/
  - https://www.europeana.eu/en/collections
  - https://www.collectienederland.nl/zoeken/
---
# Productcyclus 72

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De belangrijkste onbeantwoorde productvraag is hoe HKH een eerste controleerbaar historisch resultaat levert wanneer de bronketen gedeeltelijk of volledig faalt. Productie en acceptatie tonen momenteel geen records; de repository beschrijft wel een rijker zoekcontract.

### Huidige zoekflow

De publieke app biedt vrije tekst, plek, persoon, gebeurtenis, periode en bronfilter. Een read-only zoekactie op ‘Heemskerk’ levert geen records, metadata, identifiers of permanente bronlinks.

Bronnen: [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl)

### Bronstatus is zichtbaar, resultaat niet

De app meldt Europeana als niet geconfigureerd en Open Archieven als onvolledig antwoord. Retry en zoekopdracht aanpassen zijn beschikbaar, maar er is geen bruikbaar deelresultaat of duidelijk onderscheid met een inhoudelijk nulresultaat.

Bronnen: [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://github.com/robbertvdzon/hkh-autopilot](https://github.com/robbertvdzon/hkh-autopilot)

### Repository en deployment lopen uiteen

De README beschrijft bronstatussen, stabiele identifiers, permanente links, rechten- en privacymetadata, context, relaties en retry/cachegedrag. Deze contractonderdelen zijn in de live flow niet aantoonbaar omdat geen record wordt getoond.

Bronnen: [https://github.com/robbertvdzon/hkh-autopilot](https://github.com/robbertvdzon/hkh-autopilot), [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl)

### Beheerworkflow

De beheeracceptatie toont nieuws-publicatie en lokale record-intake als intern concept. De overgang van concept naar brongeverifieerd, rechten- en privacybeoordeeld publiek resultaat is niet zichtbaar.

Bronnen: [https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/)

### Herleidbaarheid en rechten

DERA beschrijft duurzame identifiers, provenance en expliciete rechtenstatus als voorwaarden om erfgoedinformatie te beoordelen en hergebruiken. Deze patronen sluiten aan bij de missie en het beschreven HKH-contract.

Bronnen: [https://dera.netwerkdigitaalerfgoed.nl/index.php/Linked_Data](https://dera.netwerkdigitaalerfgoed.nl/index.php/Linked_Data), [https://dera.netwerkdigitaalerfgoed.nl/index.php/Doelen](https://dera.netwerkdigitaalerfgoed.nl/index.php/Doelen)

### Inspiratie voor ontdekking

Europeana biedt browse-ingangen via thema, onderwerp, eeuw en instelling. Collectie Nederland combineert vrij zoeken met filters op instelling, objectsoort, onderwerp, jaartal en materiaal.

Bronnen: [https://www.europeana.eu/en/collections](https://www.europeana.eu/en/collections), [https://www.collectienederland.nl/zoeken/](https://www.collectienederland.nl/zoeken/)

### Huidige applicatie

**Doel:** HKH-autopilot is bedoeld voor een brede doelgroep die vanuit nieuwsgierigheid de geschiedenis van Heemskerk wil onderzoeken via plekken, personen, gebeurtenissen en onderwerpen. De app moet lokale bronnen verbinden met externe historische collecties en ontdekkingen bronherleidbaar, toegankelijk, privacybewust en herbruikbaar maken.

**Wat ontbreekt:**
- Geen historisch record bij zoeken op ‘Heemskerk’.
- Geen zichtbare bronmetadata, stabiele identifier of permanente bronlink.
- Geen bruikbare deelresultaten bij bronuitval.
- Europeana is niet geconfigureerd.
- Rechten-, privacy-, context- en relatievelden zijn zonder record niet verifieerbaar.
- De publiceerbaarheidsketen van lokale intake naar publiek resultaat is niet zichtbaar.

### Verbetermogelijkheden

- Maak de end-to-end bronketen aantoonbaar werkend voor minimaal één controleerbaar resultaat.
- Maak transportfout, ongeldig antwoord, nulresultaat en gedeeltelijke beschikbaarheid expliciet verschillend.
- Toon per geldig resultaat bronnaam, bronmetadata, stabiele identifier, permanente link en rechten-/privacystatus.
- Behoud beschikbare deelresultaten bij gedeeltelijke bronuitval.
- Gebruik zekere metadata voor bronherleidbare vervolgnavigatie.
- Maak in beheer de statussen van intern concept tot publiceerbaar resultaat inzichtelijk.
- Gebruik provenance- en rights-patronen uit DERA als toetsingskader.

### Inspiratiebronnen

- [Europeana Collections](https://www.europeana.eu/en/collections) — Thematische, temporele en institutionele browse-ingangen.
- [Collectie Nederland](https://www.collectienederland.nl/zoeken/) — Vrij zoeken met filters op instelling, objectsoort, onderwerp, jaartal en materiaal.
- [DERA Linked Data](https://dera.netwerkdigitaalerfgoed.nl/index.php/Linked_Data) — Referentie voor identifiers, provenance en rechtenstatus.
- [Nationale Strategie Digitaal Erfgoed](https://netwerkdigitaalerfgoed.nl/nationale-strategie/) — Kader voor het verbinden van verspreide erfgoedcollecties.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://github.com/robbertvdzon/hkh-autopilot) | 2026-08-14 | Publieke repository; in de geraadpleegde rootbestanden geen expliciete licentie vastgesteld. | Repositorystructuur en README voor productfunctie, zoekcontract en architectuur. |
| [bron](https://hkh-autopilot.vdzonsoftware.nl) | 2026-08-14 | Applicatie- en contentlicentie onbekend; read-only geraadpleegd. | Productieflow en echte zoekuitkomst. |
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl) | 2026-08-14 | Representatieve nepdata; licentie van UI en dummy-inhoud onbekend. | Acceptatieflow en veilige zoekinteractie. |
| [bron](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/) | 2026-08-14 | Preview-beheeromgeving; licentie van interface en dummy-identiteit onbekend. | Beheer- en intakeworkflow. |
| [bron](https://dera.netwerkdigitaalerfgoed.nl/index.php/Linked_Data) | 2026-08-14 | Publieke DERA-kennisbank; concrete licentie van de pagina niet vastgesteld. | Identifiers, rechtenstatus en linked-data-principes. |
| [bron](https://dera.netwerkdigitaalerfgoed.nl/index.php/Doelen) | 2026-08-14 | Publieke DERA-kennisbank; concrete licentie van de pagina niet vastgesteld. | Doelen rond navigatie, bruikbaarheid en duurzame toegankelijkheid. |
| [bron](https://netwerkdigitaalerfgoed.nl/nationale-strategie/) | 2026-08-14 | Publieke NDE-informatie; concrete licentie van de pagina niet vastgesteld. | Beleidscontext voor verbonden digitale collecties. |
| [bron](https://www.europeana.eu/en/collections) | 2026-08-14 | Publieke Europeana-website; licentie van interface en volledige content niet vastgesteld. | Inspiratie voor thematische en temporele ontdekking. |
| [bron](https://www.collectienederland.nl/zoeken/) | 2026-08-14 | Publieke RCE-website; concrete licentie van de pagina niet vastgesteld. | Inspiratie voor vrij zoeken en verfijningsfilters. |

## Productbeslissing

Maak de Open Archieven-zoek-MVP end-to-end bewijsbaar voor de zoekterm ‘Heemskerk’: toon minimaal één controleerbaar resultaat wanneer beschikbaar, met bronnaam, metadata, stabiele identifier, permanente bronlink en expliciete rechten-/privacystatus. Maak bronuitval, ongeldig antwoord, nulresultaat en gedeeltelijke beschikbaarheid afzonderlijk begrijpelijk en behoud geldige deelresultaten.

**Waarom:** Deze richting sluit direct aan op epic theme-hkh-autopilot-0002 en vermindert de grootste huidige onzekerheid: de productieflow levert geen aantoonbaar historisch resultaat en maakt bronuitval niet onderscheidbaar van een inhoudelijk nulresultaat. Ze verbindt lokale nieuwsgierigheid met een externe collectie, maakt antwoorden herleidbaar en legt een toetsbare basis voor latere vervolgzoekingen. De uitvoering blijft smal: Open Archieven als eerste bron, zoekopdracht ‘Heemskerk’, resultaatcontract en fout-/deelsuccesgedrag.

### Prioriteiten
- Open Archieven toegankelijkheid en antwoordvalidatie voor ‘Heemskerk’ vaststellen.
- Een geldig resultaat tonen met bronnaam, metadata, stabiele identifier en permanente bronlink.
- Rechten- en privacystatus per resultaat expliciet tonen.
- Transportfout, ongeldig antwoord, nulresultaat en gedeeltelijke beschikbaarheid duidelijk onderscheiden.
- Beschikbare geldige deelresultaten behouden bij gedeeltelijke bronuitval en retry mogelijk maken.

### Besluiten
- **Kies Open Archieven als enige externe bron voor deze MVP.** — De roadmap benoemt Open Archieven als eerste externe bron en het onderzoek bevestigt dat een externe bron zonder API-key bruikbaar kan zijn wanneer de publieke API daadwerkelijk toegankelijk is.
- **Maak bronherleidbaarheid onderdeel van het minimale resultaatcontract.** — Duurzame identifiers, provenance en expliciete rechtenstatus zijn volgens DERA voorwaarden voor beoordeling en hergebruik van erfgoedinformatie.
- **Behandel gedeeltelijk succes als bruikbaar resultaat en toon bronstatus apart.** — De huidige app toont wel bronstatus maar geen bruikbaar deelresultaat; het onderzoek identificeert dit als kernprobleem voor betrouwbare historische ontdekking.
- **Gebruik alleen zekere resultaatmetadata als basis voor vervolgzoekingen.** — De productrichting moet nieuwsgierigheid ondersteunen zonder onbewezen historische relaties als feiten te presenteren; bronvastgelegde metadata biedt daarvoor een veilige basis.

## UX-voorstel: Open Archieven-resultaat voor ‘Heemskerk’

**Gebruikersdoel:** De gebruiker vindt minimaal één controleerbaar historisch resultaat en kan zien hoe betrouwbaar, herleidbaar en privacybewust de bron is.

### Flow
1. Open Historisch zoeken.
2. Vul ‘Heemskerk’ in en start de zoekopdracht.
3. Toon een duidelijke laadstatus en daarna afzonderlijke bronstatussen.
4. Toon elk geldig resultaat met titel, korte metadata, bronnaam, stabiele identifier, permanente bronlink en rechten-/privacystatus.
5. Toon beschikbare resultaten ook wanneer een andere bron of respons gedeeltelijk faalt.
6. Maak onderscheid tussen transportfout, ongeldig antwoord, nulresultaat en gedeeltelijke beschikbaarheid.
7. Bied bij herstelbare fouten een toetsenbordtoegankelijke knop ‘Opnieuw proberen’.
8. Laat de gebruiker vanuit een resultaat terugkeren naar de zoekopdracht zonder filters en context te verliezen.

### Wireframe

[Pagina: Historisch zoeken]\n\nH1 Historisch zoeken\n[Zoekterm __________________ Heemskerk] [Zoeken]\n\nStatusgebied aria-live=polite:\n‘Zoeken in Open Archieven…’\n\n[Resultaatstatus]\nOpen Archieven — gedeeltelijk beschikbaar\n2 resultaten gevonden. 1 bronantwoord kon niet worden verwerkt.\n[Opnieuw proberen]\n\n[Resultaatkaart]\nTitel: …\nType/periode/plaats/persoon: …\nBron: Open Archieven\nStabiele identifier: …\n[Open permanente bronlink]\nRechten: …\nPrivacy: openbaar / beperkt / onbekend\nProvenance: bronmetadata beschikbaar\n\n[Resultaatkaart]\n…\n\n[Geen resultaten-state]\nGeen geldige resultaten gevonden voor ‘Heemskerk’. Dit is niet hetzelfde als een bronfout.\n[Zoekopdracht aanpassen]\n\n[Fout-state: transport]\nOpen Archieven kon niet worden bereikt. Beschikbare resultaten van andere bronnen blijven zichtbaar.\n[Opnieuw proberen]\n\n[Fout-state: ongeldig antwoord]\nOpen Archieven gaf een onbruikbaar antwoord. Er worden geen onbevestigde resultaten getoond.\n[Opnieuw proberen]

### Interactiehypotheses
- Als elk geldig resultaat een bronnaam, stabiele identifier en permanente bronlink toont, kunnen gebruikers de herkomst van een resultaat zelfstandig controleren; toetsbaar via geautomatiseerde DOM- en linkvalidatie.
- Als gedeeltelijke beschikbaarheid resultaten en bronstatus afzonderlijk toont, begrijpen gebruikers beter dat zichtbare resultaten bruikbaar zijn ondanks bronuitval; toetsbaar via scenario-tests met één geldige en één falende bronrespons.
- Als transportfout, ongeldig antwoord en inhoudelijk nulresultaat verschillende statuscomponenten en tekst hebben, worden deze toestanden niet ten onrechte als hetzelfde geïnterpreteerd; toetsbaar via snapshot- en tekstasserties.
- Als alleen zekere metadata als vervolgcontext wordt getoond, ontstaan geen onbewezen historische relaties; toetsbaar door te controleren dat ontbrekende relatievelden niet worden ingevuld.
- Als ‘Opnieuw proberen’ de zoekterm en filters behoudt, kunnen gebruikers herstelacties uitvoeren zonder hun invoer opnieuw te doen; toetsbaar met end-to-end state assertions.
- Als rechten- en privacystatus per resultaat zichtbaar zijn, kunnen gebruikers de herbruikbaarheid en gevoeligheid van informatie beoordelen voordat zij de bron openen; toetsbaar op aanwezigheid en toegestane statuswaarden.

### Toegankelijkheid
- Gebruik semantische HTML, één duidelijke H1 en logisch geordende headings.
- Maak alle interacties bereikbaar met toetsenbord en toon een zichtbare focusindicator.
- Gebruik een echte button voor zoeken, opnieuw proberen en zoekopdracht aanpassen; gebruik links voor permanente bronlinks.
- Koppel labels programmatisch aan invoervelden en geef begrijpelijke foutmeldingen naast het statusgebied.
- Gebruik aria-live=polite voor laad-, succes- en gedeeltelijke-foutstatussen zonder de focus onverwacht te verplaatsen.
- Zorg voor voldoende kleurcontrast en geef status niet uitsluitend met kleur weer; combineer kleur met tekst en eventueel een pictogram.
- Maak resultaatkaarten leesbaar voor schermlezers en vermijd betekenisvolle informatie uitsluitend in tooltip of hover.
- Respecteer zoom, reflow en kleine schermen; voorkom horizontaal scrollen bij 200 procent zoom.

### Privacy
- Bewaar de zoekterm alleen zolang nodig voor de actieve zoekopdracht en herstelactie; sla geen zoekgeschiedenis op zonder afzonderlijk doel en grondslag.
- Stuur alleen de noodzakelijke zoekparameters naar Open Archieven en documenteer deze gegevensdoorgifte in de privacyinformatie.
- Toon privacystatus per resultaat en label onbekende status expliciet als ‘onbekend’; vul geen persoonsgevoelige context aan uit aannames.
- Beperk het tonen van persoonsgegevens tot wat de bron rechtmatig en noodzakelijk publiceert; maskeer of reduceer niet-noodzakelijke gegevens waar mogelijk.
- Bewaar bronmetadata en identifiers alleen met een duidelijk doel, passende grondslag en bewaartermijn.
- Log technische foutinformatie zonder volledige zoektermen of andere persoonsgegevens wanneer die niet nodig zijn voor diagnose.
- Maak duidelijk wanneer een permanente bronlink naar een externe partij leidt en voorkom het laden van niet-noodzakelijke tracking- of externe inhoud.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is klein, toetsbaar en agent-uitvoerbaar. Er zijn geen materiële blokkades; resterende punten zijn beperkte overlap en specificatieverduidelijking.
- **WARNING · CONSISTENCY** — Er is gedeeltelijke overlap met stories 61, 62, 63 en 73 rond resultaatmetadata, statusvelden en rechteninformatie. Houd de implementatie beperkt tot de contract-naar-publieke-kaartkoppeling en wijzig bestaande adapter- of foutlogica niet.
- **WARNING · SCOPE** — ‘Relevante metadata’ is niet exact gedefinieerd. Leg de concrete toegestane velden vast in het bestaande resultaatcontract of de testfixtures, zonder nieuw productbeleid te introduceren.
- **INFO · RIGHTS** — De kandidaat toont rechten- en privacystatus alleen bron- of contractgestuurd en gebruikt ‘Onbekend’ bij ontbrekende waarden; dit is passend fail-closed gedrag.

## Geaccepteerde storykandidaten

### Open Archieven-resultaatkaart met volledig herleidbaar metadata-contract

_Sleutel: `open-archieven-resultaatkaart-contractkoppeling`_

Als bezoeker wil ik een geldig Open Archieven-resultaat als consistente publieke resultaatkaart kunnen bekijken, zodat de bronherleidbaarheid uit het externe metadata-contract daadwerkelijk zichtbaar wordt in de zoekflow. Deze story koppelt het bestaande resultaatcontract aan de publieke weergave en valt terug op expliciete onbekende waarden wanneer optionele broninformatie ontbreekt; adapterlogica, foutclassificatie, retrygedrag en bronkeuze blijven buiten scope.

**Acceptatiecriteria**
- Een geldige Open Archieven-fixture wordt via het bestaande resultaatcontract naar een publieke resultaatkaart gerenderd.
- Elke resultaatkaart toont bronnaam, titel of primaire beschrijving, relevante metadata, stabiele identifier en een klikbare permanente bronlink.
- De kaart toont rechtenstatus en privacystatus uitsluitend als door de bron of het contract aangeleverde waarden; ontbrekende waarden worden als ‘Onbekend’ weergegeven.
- Een ontbrekende verplichte identifier of permanente bronlink maakt het resultaat ongeldig voor publieke weergave en toont geen onbevestigde kaart.
- De permanente bronlink bevat een expliciet linklabel, verwijst naar de bron-URI uit het resultaatcontract en opent veilig zonder lokale broninhoud of ruwe payload te kopiëren.
- De contract-naar-weergavekoppeling is geautomatiseerd getest met minimaal één volledig geldige fixture en fixtures met ontbrekende optionele en verplichte velden.
- Bestaande bronstatussen, foutcategorieën, gedeeltelijke resultaten en retrycontext blijven ongewijzigd en worden door deze koppeling niet als inhoudelijk nulresultaat gepresenteerd.

Bronnen: [https://github.com/robbertvdzon/hkh-autopilot](https://github.com/robbertvdzon/hkh-autopilot), [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl), [https://dera.netwerkdigitaalerfgoed.nl/index.php/Linked_Data](https://dera.netwerkdigitaalerfgoed.nl/index.php/Linked_Data), [https://dera.netwerkdigitaalerfgoed.nl/index.php/Doelen](https://dera.netwerkdigitaalerfgoed.nl/index.php/Doelen)

Afhankelijkheden: story:61, story:63, story:73, story:74 (herkend als bestaande stories: 61, 63, 73, 74)

Risico's: De externe bron kan minder metadata leveren dan het contract verwacht; ontbrekende waarden moeten daarom fail-closed en expliciet onbekend blijven., De bestaande publieke zoekroute kan nog geen geldige live-respons ontvangen; geautomatiseerde fixtures en gecontroleerde mocks zijn noodzakelijk voor reproduceerbare verificatie., Een permanente bronlink kan naar een externe omgeving verwijzen die tijdelijk niet beschikbaar is; de kaart mag daarom alleen herleidbaarheid tonen en geen externe inhoud lokaal cachen.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
