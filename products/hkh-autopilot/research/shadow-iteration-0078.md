---
product: hkh-autopilot
artifact_type: research
run_id: shadow-hkh-autopilot-0078
date: 2026-08-15
status: approved
sources:
  - https://github.com/robbertvdzon/hkh-autopilot
  - https://hkh-autopilot.vdzonsoftware.nl
  - https://hkh-autopilot-acceptance.vdzonsoftware.nl
  - https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/
  - https://api.openarchieven.nl/1.1/records/search.json?name=Heemskerk&lang=nl&number_show=3
  - https://www.openarchieven.nl/api/docs/records/search.php
  - https://www.openarchieven.nl/api/docs/records/show.php
  - https://www.openarchieven.nl/api/docs/uri.php
  - https://www.openarchieven.nl/datasets/
  - https://www.openarchieven.nl/datasets/ghn
  - https://www.openarchieven.nl/disclaimer.php
  - https://api.europeana.eu/en
---
# Productcyclus 78

**Focus:** Bepaal autonoom de belangrijkste nog onbeantwoorde productvraag op basis van missie, bestaand dossier en eerdere iteraties.

## Onderzoek

De belangrijkste onbeantwoorde productvraag is hoe HKH een Open Archieven-respons betrouwbaar omzet in een herleidbare resultaatkaart en tegelijk nulresultaat, gedeeltelijke beschikbaarheid en bronuitval onderscheidt. De live zoekflow toont nu geen resultaatkaart, terwijl de publieke Open Archieven-API wel resultaten en stabiele bronvelden levert.

### Live zoekflow toont geen historisch resultaat

Productie en acceptatie zijn navigeerbaar. Een read-only zoekactie op ‘Heemskerk’ toont geen recordkaart, identifier, metadata of permanente bronlink.

Bronnen: [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl)

### Open Archieven levert wel resultaten

De publieke API-call voor ‘Heemskerk’ retourneerde 49.555 gevonden records met identifier, archiefnaam, persoonsnaam, eventgegevens, sourcetype en permanente URL. De HKH-foutmelding kan daarom niet gelijkgesteld worden aan een inhoudelijk nulresultaat.

Bronnen: [https://api.openarchieven.nl/1.1/records/search.json?name=Heemskerk&lang=nl&number_show=3](https://api.openarchieven.nl/1.1/records/search.json?name=Heemskerk&lang=nl&number_show=3), [https://www.openarchieven.nl/api/docs/records/search.php](https://www.openarchieven.nl/api/docs/records/search.php)

### Bronstatussen zijn onvoldoende onderscheidbaar

De HKH-flow meldt dat geen historische bronnen konden worden geraadpleegd, Europeana niet geconfigureerd is en Open Archieven een onvolledig antwoord gaf. Geldige deelresultaten, nulresultaat en bronuitval worden niet afzonderlijk weergegeven.

Bronnen: [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl)

### Open Archieven ondersteunt een expliciet adaptercontract

De API-documentatie beschrijft number_found, docs, paging via start, maximaal 100 resultaten en filters zoals archive_code, sourcetype, eventplace en birthplace. De detail- en URI-documentatie beschrijven stabiele record-URI’s, JSON/XML/GEDCOM-representaties en foutstatus 406 bij ongeldige content negotiation.

Bronnen: [https://www.openarchieven.nl/api/docs/records/search.php](https://www.openarchieven.nl/api/docs/records/search.php), [https://www.openarchieven.nl/api/docs/records/show.php](https://www.openarchieven.nl/api/docs/records/show.php), [https://www.openarchieven.nl/api/docs/uri.php](https://www.openarchieven.nl/api/docs/uri.php)

### Rechten zijn datasetgebonden

Open Archieven vermeldt dat sommige organisaties herpublicatie niet toestaan. Individuele datasetpagina’s kunnen CC0 vermelden, maar die licentie geldt niet automatisch voor gekoppelde scans of media van derden.

Bronnen: [https://www.openarchieven.nl/datasets/](https://www.openarchieven.nl/datasets/), [https://www.openarchieven.nl/datasets/ghn](https://www.openarchieven.nl/datasets/ghn), [https://www.openarchieven.nl/disclaimer.php](https://www.openarchieven.nl/disclaimer.php)

### Beheeromgeving toont geen bronverificatieketen

De beheeromgeving is zonder login toegankelijk en toont nieuws-publicatie en lokale record-intake. Een zichtbare status voor externe bronverificatie, rechten/privacy en publieke vrijgave ontbreekt.

Bronnen: [https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/), [https://github.com/robbertvdzon/hkh-autopilot](https://github.com/robbertvdzon/hkh-autopilot)

### Zoeksemantiek is niet zichtbaar

Open Archieven documenteert naam- en plaatsfilters afzonderlijk. De HKH-interface toont niet welke bronvelden of query-interpretatie voor de vrije tekst ‘Heemskerk’ zijn gebruikt.

Bronnen: [https://www.openarchieven.nl/api/docs/records/search.php](https://www.openarchieven.nl/api/docs/records/search.php), [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl)

### Huidige applicatie

**Doel:** De HKH-app maakt de geschiedenis van Heemskerk voor een breed publiek toegankelijk en ontdekbaar via vragen en filters op plek, persoon, gebeurtenis en periode, verbonden met historische bronnen in bredere context. Herleidbaarheid, betrouwbaarheid, toegankelijkheid, meerstemmigheid en voorzichtigheid met privacy en rechten zijn kernprincipes.

**Wat ontbreekt:**
- De publieke zoekflow toont geen resultaatkaart na een zoekactie op ‘Heemskerk’.
- Geldig nulresultaat, gedeeltelijke bronrespons en volledige bronuitval zijn niet afzonderlijk zichtbaar.
- Bronidentifier, permanente URL, recordmetadata en rechten-/privacystatus ontbreken in de zichtbare uitkomst.
- De beheeromgeving toont intake en nieuwsbeheer, maar geen bronverificatie- of vrijgaveketen.
- De interface maakt niet duidelijk of vrije tekst als naam, plaats of ander bronveld is doorgegeven.
- De Open Archieven-API levert aantoonbaar meer informatie dan de huidige HKH-flow zichtbaar maakt.

### Verbetermogelijkheden

- Definieer voor de Open Archieven-adapter afzonderlijke statussen voor transportfout, ongeldige respons, geldig nulresultaat, gedeeltelijke respons en geldig resultaat.
- Gebruik number_found, docs, identifier en url als controleerbaar contract voor een resultaatkaart.
- Behoud geldige deelresultaten als een andere bron faalt.
- Toon welke querysemantiek is gebruikt: naam, plaats, gebeurtenis of vrije tekst.
- Haal voor een kaart eventueel het detailrecord op via de permanente bron-URI en toon alleen brongeleverde gegevens.
- Toon rechten- en privacystatus per dataset/recordcontext; gebruik ‘onbekend’ wanneer verificatie ontbreekt.
- Voeg fixtures en contracttests toe voor geldig resultaat, nulresultaat, onvolledige JSON, timeout/5xx, HTTP 406 en gedeeltelijke bronuitval.
- Maak alle statusinformatie tekstueel en toegankelijk, niet uitsluitend kleur- of icoongebaseerd.

### Inspiratiebronnen

- [Open Archieven Records/Search en Records/Show](https://www.openarchieven.nl/api/docs/records/search.php) — Directe inspiratie voor een expliciete zoek- en detailstap met number_found, docs, identifier en permanente URL.
- [Europeana APIs](https://api.europeana.eu/en) — Vergelijkbaar patroon waarin zoeken, recorddetail en mediaweergave afzonderlijke functies zijn; API-keyvereiste maakt het minder geschikt als directe eerste bron.

### Bronverantwoording

| URL | Geraadpleegd | Rechtenindicatie | Onderbouwing |
|---|---|---|---|
| [bron](https://github.com/robbertvdzon/hkh-autopilot) | 2026-08-15 | Publieke repository; geen expliciete softwarelicentie vastgesteld in de geraadpleegde documentatie, dus hergebruikstatus onbekend. | Productdoel, documentatie, roadmapcontext en eerdere onderzoeksdossiers vastgesteld. |
| [bron](https://hkh-autopilot.vdzonsoftware.nl) | 2026-08-15 | Publieke applicatie; rechten op software, UI en eventuele inhoud niet vastgesteld. | Productieflow geopend en historische zoekactie op ‘Heemskerk’ uitgevoerd. |
| [bron](https://hkh-autopilot-acceptance.vdzonsoftware.nl) | 2026-08-15 | Publieke acceptatieomgeving met representatieve nepdata; software/UI-rechten niet vastgesteld. | Acceptatieflow geopend en dezelfde veilige zoekactie uitgevoerd. |
| [bron](https://hkh-autopilot-admin-acceptance.vdzonsoftware.nl/) | 2026-08-15 | Publieke beheerinterface; rechten op software/UI niet vastgesteld. | Beheerflow zonder authenticatie bekeken. |
| [bron](https://api.openarchieven.nl/1.1/records/search.json?name=Heemskerk&lang=nl&number_show=3) | 2026-08-15 | Publieke API-response; hergebruik van onderliggende recorddata niet collectiebreed aangenomen. | Actuele bronrespons voor ‘Heemskerk’ rechtstreeks gecontroleerd. |
| [bron](https://www.openarchieven.nl/api/docs/records/search.php) | 2026-08-15 | Publieke technische documentatie; expliciete documentatielicentie niet vastgesteld. | Zoekcontract, velden, filters en paging geverifieerd. |
| [bron](https://www.openarchieven.nl/api/docs/records/show.php) | 2026-08-15 | Publieke technische documentatie; expliciete documentatielicentie niet vastgesteld. | Detailrecord en bronmetadata geverifieerd. |
| [bron](https://www.openarchieven.nl/api/docs/uri.php) | 2026-08-15 | Publieke technische documentatie; expliciete documentatielicentie niet vastgesteld. | Permanente URI’s, representaties en foutgedrag geverifieerd. |
| [bron](https://www.openarchieven.nl/datasets/) | 2026-08-15 | Publieke datasetcatalogus; voorwaarden verschillen per dataset. | Beperkingen op herpublicatie en beschikbaarheid van dumps/OAI-PMH geverifieerd. |
| [bron](https://www.openarchieven.nl/datasets/ghn) | 2026-08-15 | Deze datasetpagina vermeldt CC0 voor de aangeboden datasetdata; gekoppelde externe media vallen daar niet automatisch onder. | Concreet voorbeeld van datasetgebonden licentie-informatie. |
| [bron](https://www.openarchieven.nl/disclaimer.php) | 2026-08-15 | Publieke disclaimer; rechten- en privacywaarschuwingen blijven van toepassing. | Waarschuwingen over intellectuele rechten, privacy en oneigenlijk gebruik gecontroleerd. |
| [bron](https://api.europeana.eu/en) | 2026-08-15 | Publieke API-documentatie; gebruik vereist volgens de pagina een gratis API-key; rechten blijven collectie-/providergebonden. | Vergelijkbaar Search-, Record- en IIIF-patroon als inspiratie onderzocht. |

## Productbeslissing

Maak van Open Archieven een betrouwbare, herleidbare zoekresultaatkaart voor de zoekterm ‘Heemskerk’. Toon brongeleverde recordgegevens, identifier, permanente bronlink, query-interpretatie en bekende rechten-/privacystatus. Behoud geldige deelresultaten en maak resultaat, nulresultaat, gedeeltelijke respons en bronuitval afzonderlijk zichtbaar.

**Waarom:** Deze richting sluit direct aan op missie en roadmap-epic theme-hkh-autopilot-0002. De huidige HKH-flow toont geen resultaten, terwijl Open Archieven aantoonbaar records en stabiele bronvelden levert. Een expliciet adapter- en presentatiemodel verbetert betrouwbaarheid, toegankelijkheid en nieuwsgierigheid zonder onbewezen historische relaties te introduceren. De scope blijft klein: één bron, één representatieve zoekopdracht en toetsbare fout- en statusgevallen.

### Prioriteiten
- Definieer een Open Archieven-contract rond number_found, docs, identifier en permanente URL.
- Toon minimaal één controleerbaar resultaat met bronnaam, recordgegevens, vaste herkenning, bronlink en rechten-/privacystatus.
- Maak de gebruikte querysemantiek zichtbaar, inclusief of ‘Heemskerk’ als naam, plaats, gebeurtenis of vrije tekst is geïnterpreteerd.
- Maak geldig resultaat, geldig nulresultaat, gedeeltelijke respons, ongeldige respons, timeout/5xx en bronuitval tekstueel onderscheidbaar.
- Behoud geldige Open Archieven-deelresultaten wanneer een andere bron niet beschikbaar is; toon ontbrekende verificatie als ‘onbekend’.

### Besluiten
- **Gebruik Open Archieven als enige externe bron binnen deze slice en bouw de eerste resultaatkaart op de publieke zoekrespons.** — Open Archieven levert zonder zichtbare API-key resultaten voor ‘Heemskerk’ en documenteert de benodigde zoekvelden en responsstructuur.
- **Gebruik identifier en permanente URL als minimale herleidbaarheidseisen; haal alleen indien nodig brongeleverde detailinformatie op via de detail-URI.** — De API-documentatie beschrijft stabiele record-URI’s en afzonderlijke detailrepresentaties. Hierdoor kan de kaart controleerbaar blijven zonder eigen historische interpretaties toe te voegen.
- **Presenteer rechten- en privacystatus per dataset- of recordcontext en gebruik ‘onbekend’ wanneer verificatie ontbreekt.** — Rechten zijn niet collectiebreed af te leiden: datasetvoorwaarden verschillen en gekoppelde scans of media vallen niet automatisch onder dezelfde licentie.
- **Behandel een ontbrekende kaart in de huidige flow als productfout of onvolledige bronverwerking, niet als nulresultaat.** — De live zoekactie toont geen resultaatkaart, terwijl de rechtstreekse Open Archieven-respons 49.555 gevonden records rapporteert.
- **Leg de slice vast met fixtures en contracttests voor resultaat, nulresultaat, onvolledige JSON, HTTP 406, timeout/5xx en gedeeltelijke bronuitval.** — De bron documenteert expliciete fout- en pagingmogelijkheden, terwijl de huidige statusweergave geldige deelresultaten en bronuitval niet afzonderlijk maakt.

## UX-voorstel: Betrouwbare Open Archieven-resultaatkaart voor ‘Heemskerk’

**Gebruikersdoel:** De gebruiker wil een historische zoekopdracht uitvoeren en direct kunnen zien of er resultaten, geen resultaten, gedeeltelijke beschikbaarheid of bronuitval is, met controleerbare brongegevens en een permanente bronlink.

### Flow
1. 1. Open ‘Historisch zoeken’ en vul ‘Heemskerk’ in bij vrije tekst.
2. 2. Start de zoekopdracht; toon een statusbericht met de geïnterpreteerde querysemantiek, bijvoorbeeld ‘gezocht als naam’.
3. 3. Toon afzonderlijk de bronstatus van Open Archieven: resultaat, nulresultaat, gedeeltelijke respons, ongeldige respons of bronuitval.
4. 4. Bij geldige resultaten: toon een resultaatkaart met bronnaam, persoons- en gebeurtenisgegevens, identifier, datasetcontext, rechten-/privacystatus en permanente bronlink.
5. 5. Als een andere bron uitvalt, behoud en label de geldige Open Archieven-resultaten als deelresultaten.
6. 6. Maak de staten uitvoerbaar toetsbaar met fixtures en contracttests voor resultaat, nulresultaat, onvolledige JSON, HTTP 406, timeout/5xx en gedeeltelijke bronuitval.

### Wireframe

[Pagina: Historisch zoeken]

H1 Historisch zoeken

Vrije tekst
[ Heemskerk                                      ]

Query-interpretatie
‘Heemskerk’ wordt gezocht als: naam

[Zoeken]

Statusgebied (role=status, live aangekondigd)
Open Archieven: 49.555 resultaten gevonden.
Andere bronnen: niet beschikbaar. Open Archieven-resultaten blijven zichtbaar.

Resultaten

[Resultaatkaart]
Bron: Open Archieven
Naam: [bronveld]
Gebeurtenis: [type en datum]
Plaats: [bronveld]
Archief: [bronveld]
Identifier: [identifier]
Rechten: Onbekend — controleer de datasetvoorwaarden.
Privacy: Onbekend — gebruik brongegevens zorgvuldig.
[Open permanente bron] (externe link)

[Meer resultaten laden]

Alternatieve staten:
- Nulresultaat: ‘Geen records gevonden voor deze zoekopdracht.’
- Gedeeltelijke respons: ‘De bron gaf gedeeltelijke resultaten. Sommige gegevens ontbreken.’
- Ongeldige respons: ‘De bron gaf een onbruikbaar antwoord. Probeer later opnieuw.’
- Bronuitval: ‘Open Archieven is tijdelijk niet beschikbaar. Andere bronnen zijn wel/ niet beschikbaar.’

### Interactiehypotheses
- Als de query-interpretatie zichtbaar is, kunnen gebruikers beter begrijpen waarom resultaten wel of niet aansluiten; dit is toetsbaar met een fixture waarin naam- en plaatsinterpretatie verschillende resultaten geven.
- Als identifier en permanente bronlink op elke resultaatkaart staan, kunnen geautomatiseerde contracttests herleidbaarheid controleren en kan de gebruiker de bron verifiëren.
- Als geldig nulresultaat, gedeeltelijke respons en bronuitval verschillende tekstuele statussen hebben, worden minder foutieve nulresultaatconclusies getrokken; dit is toetsbaar met afzonderlijke response-fixtures.
- Als geldige deelresultaten zichtbaar blijven wanneer een andere bron uitvalt, blijft de kernzoektaak bruikbaar; dit is toetsbaar met een fixture waarin Open Archieven slaagt en een tweede bron faalt.
- Als rechten en privacy ‘Onbekend’ tonen wanneer verificatie ontbreekt, worden onbewezen claims vermeden; dit is toetsbaar door ontbrekende datasetmetadata in de fixture te simuleren.
- Als alleen brongeleverde velden worden weergegeven, introduceert de MVP geen onbewezen historische relaties; dit is toetsbaar door de kaart te vergelijken met het response-schema.

### Toegankelijkheid
- Gebruik semantische koppen, labels en landmarks; koppel elk invoerveld programmatisch aan zijn label.
- Maak de statusregio toegankelijk met role=status of een passend live-regionmechanisme en kondig statuswijzigingen tekstueel aan.
- Zorg dat alle acties, links en ‘Meer resultaten laden’ volledig met toetsenbord bereikbaar en bedienbaar zijn.
- Toon statusverschillen niet uitsluitend met kleur of iconen; gebruik duidelijke tekst en eventueel aanvullende visuele aanduidingen.
- Handhaaf voldoende kleurcontrast voor tekst, links, foutmeldingen en focusindicatoren.
- Gebruik logische focusvolgorde en behoud focus op een voorspelbare plek na het laden van resultaten.
- Geef externe links een begrijpelijke naam en kondig aan dat ze een nieuwe externe bron openen indien dat gedrag wordt gebruikt.
- Maak ontbrekende velden expliciet, bijvoorbeeld ‘Niet aangeleverd door de bron’, in plaats van lege of betekenisloze waarden.

### Privacy
- Sla de zoekterm alleen op als dat noodzakelijk is voor de actuele zoekopdracht; bewaar deze niet standaard langdurig.
- Verzamel en toon uitsluitend brongeleverde gegevens die nodig zijn voor de resultaatkaart.
- Toon geen conclusies over levende personen of gevoelige persoonsgegevens buiten de broncontext.
- Label privacystatus als ‘Onbekend’ wanneer geen betrouwbare dataset- of recordinformatie beschikbaar is.
- Toon een korte waarschuwing dat brongegevens privacy- en rechtenbeperkingen kunnen hebben en dat gekoppelde scans of media afzonderlijke voorwaarden kunnen kennen.
- Log voor geautomatiseerde tests uitsluitend synthetische of geanonimiseerde fixtures; gebruik geen productiezoektermen of persoonsgegevens in permanente logs.
- Maak permanente bronlinks herkenbaar zonder brondata lokaal te kopiëren wanneer een verwijzing volstaat.

## Kritische beoordeling

**Oordeel:** ACCEPT

De kandidaat is klein, toetsbaar en agent-uitvoerbaar. Er zijn geen materiële blokkades. Er is wel functionele overlap met bestaande stories over de publieke zoekroute, adaptercontracten, statusweergave en resultaatkaarten; dit is informatief en geen reden tot blokkeren.
- **WARNING · SCOPE** — Functionele overlap met gepubliceerde stories 62, 74, 75, 82 en 63. Lever deze kandidaat uitsluitend als transparante weergave van de daadwerkelijk verzonden querymapping; voorkom duplicatie van adapter-, foutclassificatie- of resultaatkaartlogica.
- **INFO · CONSISTENCY** — De kandidaat noemt naam-, plaats- en onbepaalde interpretatie, maar legt geen vaste productkeuze op voor de interpretatie van ‘Heemskerk’. Dat is veilig zolang onbekend wordt getoond wanneer de adaptermapping niet vaststaat.
- **INFO · ACCESSIBILITY** — De kandidaat vereist tekstuele beschikbaarheid en geautomatiseerde toetsing. Zorg bij implementatie aanvullend voor een semantisch gekoppelde statusweergave, zonder uitsluitend visuele positionering te gebruiken.

## Geaccepteerde storykandidaten

### Zichtbare query-interpretatie voor historische zoekopdrachten

_Sleutel: `zichtbare-queryinterpretatie-open-archieven`_

Als bezoeker wil ik kunnen zien hoe mijn vrije zoektekst naar Open Archieven is vertaald, zodat ik begrijp of bijvoorbeeld ‘Heemskerk’ als naam, plaats of ander bronveld is gezocht zonder historische betekenis te veronderstellen.

**Acceptatiecriteria**
- Toon bij iedere uitgevoerde vrije-tekstzoekopdracht de daadwerkelijk gebruikte querysemantiek en bronvelden, gebaseerd op het adapterverzoek; toon geen niet-uitgevoerde interpretatie.
- Gebruik voor ‘Heemskerk’ uitsluitend bronvelden en parameters die door het Open Archieven-contract worden ondersteund, zoals naam, eventplace of birthplace.
- Toon een neutrale tekstuele status wanneer de querysemantiek niet kan worden vastgesteld; verzin geen interpretatie.
- Leg de querysemantiek vast in geautomatiseerde tests voor ten minste naam-, plaats- en onbepaalde interpretatie.
- Maak de informatie tekstueel beschikbaar naast de resultaten en niet uitsluitend via kleur, icoon of visuele positionering.
- De geautomatiseerde tests controleren dat de zichtbare interpretatie overeenkomt met de werkelijk verzonden Open Archieven-parameters.

Bronnen: [https://www.openarchieven.nl/api/docs/records/search.php](https://www.openarchieven.nl/api/docs/records/search.php), [https://hkh-autopilot.vdzonsoftware.nl](https://hkh-autopilot.vdzonsoftware.nl), [https://hkh-autopilot-acceptance.vdzonsoftware.nl](https://hkh-autopilot-acceptance.vdzonsoftware.nl)

Afhankelijkheden: story:74, story:62 (herkend als bestaande stories: 74, 62)

Risico's: De bestaande vrije-tekstfunctionaliteit kan meerdere bronvelden ondersteunen; een verkeerde mapping kan de zoekuitkomst inhoudelijk veranderen., Open Archieven levert niet noodzakelijk een expliciete gebruikersvriendelijke interpretatielabeling; de applicatie moet daarom alleen de eigen werkelijk uitgevoerde mapping tonen., De kandidaat overlapt functioneel met bestaande zoekroute- en statusstories als de scope niet beperkt blijft tot transparante weergave van de uitgevoerde querymapping.

_Dit product stond op autonoom toen deze cyclus draaide: geaccepteerde stories mogen na het mergen van deze workspace-publicatie automatisch naar de Software Factory worden gestuurd._
